"""
기능: 지정한 MPD의 실제 배치와 상태 기록, 부품 사전·가격·형상 무결성을 검사한다.
입력: models/<모델>.mpd 위치 인자, docs/gobricks-dictionary.json, assets/policy.md.
선택: --check-body-overlaps로 직육면체 몸체 겹침을 검사한다. 곡선·관절은 제외한다.
출력: 기본은 읽기 전용. --sync-state는 schema 3의 ID·수량·좌표 상태만 본문에서 갱신한다.
      --sync-only와 함께 쓰면 상태 갱신만 수행한다. 형상·목표 치수·검증 판정은 바꾸지 않는다.
실행: python3 tools/validate_model.py models/tyrannosaurus-v1.mpd
범위: BRICK schema_version 3; 계층·회전·수량·중복 배치 검사.
      v0는 LEGO 형상을 검사하며, 다른 버전은 GoBricks SKU·색상·가격도 검사한다.
한계: 기계적으로 조립 가능한지, 접촉·간섭·결합력·하중·실제 가동 범위는 검증하지 않는다.
      예전 티라노 전용 격자·160개·특정부위 조건으로 새 모델을 통과시키지 않는다.
"""
import argparse,hashlib,json,math
from pathlib import Path
from collections import Counter
from decimal import Decimal

def mm(a,b):return [sum(a[r*3+k]*b[k*3+c] for k in range(3)) for r in range(3) for c in range(3)]
def mv(a,b):return [sum(a[r*3+k]*b[k] for k in range(3)) for r in range(3)]
def plus(a,b):return [x+y for x,y in zip(a,b)]
def near(a,b):return all(abs(x-y)<1e-4 for x,y in zip(a,b))
def body_overlaps(state, parts):
 # Nominal solid rectangular bodies only; studs, cavities and curved/Technic parts excluded.
 names={x+'.dat' for x in ['3001','3003','3005','3004','3010','3622','3020','3024','3023b','3022','3710','3623','3666','3460','3034','3832','3031','3032','60479']}
 def dot(a,b):return sum(x*y for x,y in zip(a,b))
 def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
 boxes=[]
 for o in state['instances']:
  if o['part'] not in names:continue
  bounds=parts[o['gobricks_id']]['dimensions']['bounds'];low=list(bounds['min']);low[1]=0;high=bounds['max'];m=o['matrix'];center=plus(o['position'],mv(m,[(a+b)/2 for a,b in zip(low,high)]));h=[(b-a)/2 for a,b in zip(low,high)];axes=[[m[r*3+c] for r in range(3)] for c in range(3)];ext=[sum(abs(m[r*3+c])*h[c] for c in range(3)) for r in range(3)];boxes.append((o,center,axes,h,[a-b for a,b in zip(center,ext)],[a+b for a,b in zip(center,ext)]))
 boxes.sort(key=lambda b:b[4][0]);errors=[]
 for idx,(o,c,axes,h,low,high) in enumerate(boxes):
  for other,c2,axes2,h2,low2,high2 in boxes[idx+1:]:
   if low2[0]>=high[0]-.3:break
   if any(min(a,b)-max(d,e)<.3 for a,b,d,e in zip(high,high2,low,low2)):continue
   delta=[b-a for a,b in zip(c,c2)];separated=False
   for axis in axes+axes2+[cross(a,b) for a in axes for b in axes2]:
    norm=math.sqrt(dot(axis,axis))
    if norm<.001:continue
    radius=sum(h[k]*abs(dot(axes[k],axis))+h2[k]*abs(dot(axes2[k],axis)) for k in range(3))
    if abs(dot(delta,axis))>=radius-.3*norm:separated=True;break
   if not separated:errors.append((o,other))
 return errors

def sync_state(model):
 """Derive schema-3 metadata without changing any type-1 geometry or verification claims."""
 text=model.read_text();lines=text.splitlines(keepends=True)
 state_line=next(i for i,l in enumerate(lines) if l.startswith('0 !BRICK_STATE '))
 state=json.loads(lines[state_line].split(' ',2)[2])
 if state.get('schema_version')!=3:
  raise ValueError('--sync-state supports schema 3 only; the model was not changed')
 identity=[1,0,0,0,1,0,0,0,1];defs={};current=None;marker=None;used=set();edits={};insertions={}
 reserved={l.split()[2] for l in lines if l.startswith('0 !BRICK_INSTANCE ')}
 serial=1
 for idx,line in enumerate(lines):
  if line.startswith('0 FILE '):
   current=line[7:].strip();marker=None
   if current in defs:raise ValueError('Duplicate FILE '+current)
   defs[current]=[]
  elif line.startswith('0 NOFILE'):current=None;marker=None
  elif line.startswith('0 !BRICK_INSTANCE '):marker=idx
  elif line.startswith('1 ') and current:
   f=line.split(maxsplit=14)
   if len(f)!=15:raise ValueError('Invalid type-1 line')
   child=f[14].strip();ident=lines[marker].split()[2] if marker is not None else None
   if child.lower().endswith('.dat') and not current.lower().endswith('.dat'):
    if not ident or ident in used:
     while 'part-%04d'%serial in reserved:serial+=1
     ident='part-%04d'%serial;reserved.add(ident);serial+=1
     replacement='0 !BRICK_INSTANCE '+ident+'\n'
     if marker is None:insertions[idx]=replacement
     else:edits[marker]=replacement
    used.add(ident)
   defs[current].append((ident,int(f[1]),list(map(float,f[2:5])),list(map(float,f[5:14])),child))
   marker=None
 if not defs:raise ValueError('No MPD definitions')
 old={o['id']:o for o in state.get('instances',[])}
 for group in state.get('unplaced_submodels',[]):
  old.update({o['id']:o for o in group.get('instances',[])})
 reached=set();emitted=set()
 def walk(name,mat,pos,color=16,stack=()):
  if name in stack:raise ValueError('Cyclic MPD '+name)
  reached.add(name);result=[]
  for ident,c,t,m,child in defs[name]:
   c=color if c==16 else c;rt=plus(pos,mv(mat,t));rm=mm(mat,m)
   if child.lower().endswith('.dat'):
    if ident in emitted:
     raise ValueError('Repeated physical definition '+str(ident)+': use unique physical IDs per placed occurrence before syncing; model unchanged')
    emitted.add(ident);prior=old.get(ident,{})
    item=dict(prior)
    if prior and (prior.get('part')!=child or prior.get('color')!=c):
     item.pop('gobricks_id',None);item.pop('sku',None)
     item['catalog_mapping_status']='not_verified'
    item.update(id=ident,part=child,color=c,position=rt,matrix=rm)
    item.setdefault('group',name)
    result.append(item)
   else:
    if child not in defs:raise ValueError('Missing internal submodel '+child)
    result.extend(walk(child,rm,rt,c,stack+(name,)))
  return result
 placed=walk(next(iter(defs)),identity,[0,0,0]);unplaced=[]
 # Only unreferenced local roots are listed, not every nested definition twice.
 remaining=set(defs)-reached
 children={child for name in remaining for _,_,_,_,child in defs[name] if child in remaining}
 roots=[name for name in defs if name in remaining-children and not name.lower().endswith('.dat')]
 previous={g['file']:g for g in state.get('unplaced_submodels',[])}
 for name in roots:
  items=walk(name,identity,[0,0,0])
  group=dict(previous.get(name,{}));group.update(file=name,instances=items)
  group.setdefault('status','local_definition_not_root_reachable');unplaced.append(group)
 if any(name not in reached and not name.lower().endswith('.dat') for name in defs):
  raise ValueError('Unreachable cyclic definitions; model unchanged')
 state.update(instances=placed,piece_count=len(placed),placed_piece_count=len(placed),unplaced_submodels=unplaced,unplaced_piece_count=sum(len(g['instances']) for g in unplaced))
 edits[state_line]='0 !BRICK_STATE '+json.dumps(state,ensure_ascii=False,separators=(',',':'))+'\n'
 result=''.join(insertions.get(i,'')+edits.get(i,l) for i,l in enumerate(lines))
 # Type-1 rows, local coordinates and all connection/coverage claims stay unchanged.
 model.write_text(result)
 print('STATE SYNC:',len(placed),'root parts;',state['unplaced_piece_count'],'unplaced parts. Geometry and verification claims unchanged.')

def run(model, check_body=False):
 root=Path('assets');manifest=json.loads((root/'policy.md').read_text().split('<!-- asset-manifest:start -->\n```json\n',1)[1].split('\n```\n<!-- asset-manifest:end -->',1)[0])
 for rel,entry in manifest['files'].items():
  data=(root/rel).read_bytes();assert hashlib.sha256(data).hexdigest()==entry['sha256'],rel
  assert len(data)==entry['bytes'],rel
  for line in data.decode('utf-8-sig').splitlines():
   f=line.split(maxsplit=14)
   if len(f)==15 and f[0]=='1':
    name=f[14].replace('\\','/').lower();assert any((root/p/name).is_file() for p in ['','parts','primitives']),name
 text=model.read_text();state=json.loads(next(l.split(' ',2)[2] for l in text.splitlines() if l.startswith('0 !BRICK_STATE ')))
 assert state['schema_version']==3,'This validator supports BRICK schema 3'
 defs={};current=None;marker=None
 for line in text.splitlines():
  if line.startswith('0 FILE '):
   current=line[7:].strip();assert current not in defs;defs[current]=[];marker=None
  elif line.startswith('0 !BRICK_INSTANCE '):marker=line.split()[2]
  elif line.startswith('1 '):
   fields=line.split(maxsplit=14);fields[-1]=fields[-1].strip();assert current and len(fields)==15
   defs[current].append((marker,int(fields[1]),list(map(float,fields[2:5])),list(map(float,fields[5:14])),fields[14]));marker=None
 exported={};identity=[1,0,0,0,1,0,0,0,1]
 def visit(name,mat,pos,stack=(),inherited_color=16):
  assert name not in stack,'Cyclic MPD submodel'
  for ident,color,t,m,child in defs[name]:
   rm=mm(mat,m);rt=plus(pos,mv(mat,t));color=inherited_color if color==16 else color
   if child.endswith('.dat'):
    assert ident and ident not in exported,'Duplicate or missing instance ID'
    assert (root/'parts'/child).is_file(),child
    exported[ident]=(color,rt,rm,child)
   else:
    assert child in defs,child
    visit(child,rm,rt,stack+(name,),color)
 visit(next(iter(defs)),identity,[0,0,0])
 items={i['id']:i for i in state['instances']};assert len(items)==len(state['instances'])
 assert set(items)==set(exported) and len(items)==state['piece_count']
 lego_v0=model.stem.endswith('-v0')
 cad_import=lego_v0 and state.get('status')=='cad_import'
 for o in items.values():
  assert ('gobricks_id' in o)==('sku' in o),'Partial GoBricks metadata; record both a verified product ID and SKU, or neither'
  assert lego_v0 or (o.get('gobricks_id') and o.get('sku')),'GoBricks mapping is required outside v0'
 # v0 reconstructs LEGO originals. Legacy candidate/empty commercial fields
 # are not verified sales mappings and must not gate its geometry checks.
 has_catalog=not lego_v0 and any('gobricks_id' in o for o in items.values())
 d=json.loads(Path('docs/gobricks-dictionary.json').read_text()) if has_catalog else {'parts':[],'colors':{}}
 parts={p['gobricks_id']:p for p in d['parts']};counts=Counter();total=Decimal(0);seen={};duplicates=[];lo=[float('inf')]*3;hi=[-float('inf')]*3
 for ident,o in items.items():
  color,t,m,part=exported[ident];assert color==o['color'] and part==o['part'] and near(t,o['position']) and near(m,o['matrix']),ident
  assert all(math.isfinite(x) for x in t+m),ident
  # Imported CADs retain their rounded matrices; this is numerical fidelity,
  # not a claim that LEGO connections tolerate the accumulated rounding error.
  matrix_tolerance=.01 if cad_import else 1e-4
  transposed=[m[c*3+r] for r in range(3) for c in range(3)];assert all(abs(a-b)<matrix_tolerance for a,b in zip(mm(m,transposed),identity)),'Scaled/skewed physical part '+ident
  det=m[0]*(m[4]*m[8]-m[5]*m[7])-m[1]*(m[3]*m[8]-m[5]*m[6])+m[2]*(m[3]*m[7]-m[4]*m[6]);assert abs(det-1)<(.01 if cad_import else 1e-5),'Mirrored physical part '+ident
  key=(part,tuple(round(x,4) for x in t+m))
  if key in seen:duplicates.append((seen[key],ident,part,t))
  else:seen[key]=ident
  if not lego_v0 and 'gobricks_id' in o:
   p=parts[o['gobricks_id']];offer=next(v for v in p['offers'] if v['sku']==o['sku']);assert str(d['colors'][offer['color_id']]['ldraw_color_id'])==str(color)
   assert Path(p['geometry']['file']).name==part and hashlib.sha256(Path(p['geometry']['file']).read_bytes()).hexdigest()==p['geometry']['sha256']
   counts[o['sku']]+=1;total+=Decimal(offer['unit_price_cny'])
  if not lego_v0 and 'gobricks_id' in o and o.get('group')!='support':
   bounds=p['dimensions']['bounds']
   for x in [bounds['min'][0],bounds['max'][0]]:
    for y in [bounds['min'][1],bounds['max'][1]]:
     for z in [bounds['min'][2],bounds['max'][2]]:
      q=plus(t,mv(m,[x,y,z]));lo=[min(a,b) for a,b in zip(lo,q)];hi=[max(a,b) for a,b in zip(hi,q)]
 all_mapped=len(counts)>0 and len({o['id'] for o in items.values() if 'gobricks_id' in o})==len(items)
 if all_mapped:
  assert total==Decimal(state['listed_retail_parts_cost_cny']) and len(counts)==state['unique_sale_skus']
  alloffers={o['sku']:o for p in d['parts'] for o in p['offers']}
  for sku,count in counts.items():assert alloffers[sku]['inventory_at_observation']>=count,sku+' exceeds recorded stock'
 for j in state.get('joints',[]):
  # v0 can record unresolved connection evidence without declaring a pose axis.
  if lego_v0 and 'axes' not in j:continue
  assert j['submodel'] in defs
  for axis,limits in j['axes'].items():assert axis in 'xyz' and len(limits)==2 and limits[0]<=0<=limits[1]
 if duplicates:
  print('Exact duplicate placements:',len(duplicates))
  for first,second,part,pos in duplicates[:50]:print(first,second,part,pos)
  assert not duplicates,'MPD contains physically coincident duplicate part instances; resolve against the manual before treating geometry as clean'
 if all_mapped:
  measured=dict(zip(['length','height','width'],[round((b-a)*.04,2) for a,b in zip(lo,hi)]));assert measured==state['reference_geometry_bounds_cm'],measured
 if check_body:
  assert all_mapped,'--check-body-overlaps requires verified catalog dimensions for every part'
  errors=body_overlaps(state,parts)
  print('Nominal rectangular body intersections:',len(errors))
  print('Groups:',dict(Counter(tuple(sorted([a['group'],b['group']])) for a,b in errors)))
  for a,b in errors[:20]:print(a['id'],a['part'],a['group'],a['position'],'<>',b['id'],b['part'],b['group'],b['position'])
  assert not errors,'Nominal rectangular bodies intersect; do not treat this design as assembly-ready'
 if all_mapped:
  print('DATA PASS:',model,len(items),'physical part references;',len(manifest['files']),'asset hashes;',len(counts),'SKUs;',total,'CNY')
  print('Reference geometry bounding envelope (cm):',measured)
 elif cad_import:
  print('CAD DATA PASS:',model,len(items),'physical part references;',len(manifest['files']),'asset hashes; imported rounded matrices retained.')
 else:
  print('LEGO GEOMETRY PASS:',model,len(items),'physical part references;',len(manifest['files']),'asset hashes;',len(counts),'verified GoBricks SKUs; GoBricks product mapping is not required for v0.')
 print('NOT VERIFIED: assembly connectivity, exact mesh collision, joint range/strength, load stability, superiority to reference product.')
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('model',type=Path);parser.add_argument('--check-body-overlaps',action='store_true',help='직육면체 브릭 몸체의 명목 간섭 검사; 실패 시 0이 아닌 코드 반환');parser.add_argument('--sync-state',action='store_true',help='schema 3 본문 기준 상태 갱신; 반복 호출의 ID가 모호하면 저장 없이 실패');parser.add_argument('--sync-only',action='store_true',help='--sync-state와 함께 상태 갱신만 실행');args=parser.parse_args()
 if args.sync_only and not args.sync_state:parser.error('--sync-only requires --sync-state')
 if args.sync_state:sync_state(args.model)
 if not args.sync_only:run(args.model,args.check_body_overlaps)
