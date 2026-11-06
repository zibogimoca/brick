"""
기능: 지정한 MPD의 실제 배치와 상태 기록, 부품 사전·가격·형상 무결성을 검사한다.
입력: models/<모델>.mpd 위치 인자, docs/gobricks-dictionary.json, assets/policy.md.
선택: --check-body-overlaps로 직육면체 몸체 겹침을 검사한다. 곡선·관절은 제외한다.
      --check-stud-connectivity --instance-prefix A- --expect-stud-components 2는
      본문에서 지원 부품의 명목 스터드·힌지 연결망을 계산한다. 실물 체결 판정이 아니다.
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
from collections import Counter,defaultdict
from decimal import Decimal

def mm(a,b):return [sum(a[r*3+k]*b[k*3+c] for k in range(3)) for r in range(3) for c in range(3)]
def mv(a,b):return [sum(a[r*3+k]*b[k] for k in range(3)) for r in range(3)]
def plus(a,b):return [x+y for x,y in zip(a,b)]
def near(a,b):return all(abs(x-y)<1e-4 for x,y in zip(a,b))
def body_overlaps(state, parts):
 # Nominal solid rectangular bodies only; studs, cavities and curved/Technic parts excluded.
 names={x+'.dat' for x in ['3001','3003','3005','3004','3010','3622','3020','3024','3023b','3022','3710','3623','3666','3460','3034','3832','3795','15573','3031','3032','3033','3035','3036','41539','3007','3008','2431','3068b','3069b','3070b','63864','60479']}
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

def sync_state(model,write=True):
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
 if write:
  model.write_text(result)
  print('STATE SYNC:',len(placed),'root parts;',state['unplaced_piece_count'],'unplaced parts. Geometry and verification claims unchanged.')
 return state

def stud_connectivity(state,prefix=''):
 """Nominal named seating grids, not a general clutch or solid-interference solver.

 Unknown parts remain unresolved nodes. Named hinge pairs add edges only when
 their reference centers and axes coincide. Side attachments, tubes, clips,
 load, detent torque and physical mold tolerance are outside this inventory.
 """
 shapes={
  '3001':(4,2,24),'3003':(2,2,24),'3004':(2,1,24),'3005':(1,1,24),
  '3007':(8,2,24),'3008':(8,1,24),'3010':(4,1,24),'3622':(3,1,24),
  '3020':(4,2,8),'3021':(3,2,8),'3022':(2,2,8),'3023b':(2,1,8),
  '3024':(1,1,8),'3031':(4,4,8),'3032':(6,4,8),'3033':(10,6,8),
  '3034':(8,2,8),'3035':(8,4,8),'3036':(8,6,8),'3710':(4,1,8),
  '3795':(6,2,8),'15573':(2,1,8),'3623':(3,1,8),'3666':(6,1,8),'3460':(8,1,8),'3832':(10,2,8),
  '41539':(8,8,8),'3062b':(1,1,24),'3941':(2,2,24),'6141':(1,1,8),
  '2431':(4,1,8),'3068b':(2,2,8),'3069b':(2,1,8),'3070b':(1,1,8),
  '63864':(3,1,8),'60592':(2,1,48),'3659':(4,1,24),'3307':(6,1,48),
  '4275b':(2,1,8),'4276b':(2,1,8),'44301':(2,1,8),'44302':(2,1,8)}
 tiles={'2431','3068b','3069b','3070b','63864','15068'}
 hinges={'2429':('vertical','male',[0,4,0],[0,1,0]),
         '2430':('vertical','female',[0,4,0],[0,1,0]),
         '4275b':('finger','male',[30,4,0],[0,0,1]),
         '4276b':('finger','female',[30,4,0],[0,0,1]),
         '44301':('click','male',[30,2,0],[0,0,1]),
         '44302':('click','female',[30,2,0],[0,0,1])}
 rows=[o for o in state['instances'] if o['id'].startswith(prefix)]
 if not rows:raise ValueError('No physical instances match prefix '+repr(prefix))
 ids={o['id'] for o in rows}
 if len(ids)!=len(rows):raise ValueError('Connectivity requires unique physical IDs')
 adj={id:set() for id in ids};tops=defaultdict(list);pivots=defaultdict(list)
 unknown=Counter();contact_pairs=Counter();hinge_pairs=set();epsilon=1e-4
 def key(p):return tuple(math.floor(x/epsilon) for x in p)
 def neighbors(p):
  k=key(p)
  return [(k[0]+x,k[1]+y,k[2]+z) for x in (-1,0,1) for y in (-1,0,1) for z in (-1,0,1)]
 def close(a,b):return sum((x-y)**2 for x,y in zip(a,b))<=epsilon**2
 def dot(a,b):return sum(x*y for x,y in zip(a,b))
 def seats(o,upper):
  n=Path(o['part']).stem
  if n not in shapes and n not in {'2429','2430','43722','43723','60477','15068'}:return None
  if upper and n in tiles:return []
  if n=='15573' and upper:local=[[0,0,0]]
  elif n in {'2429','2430'}:
   xs=(-30,-10) if n=='2429' else (10,30)
   local=[[x,0 if upper else 8,10] for x in xs]
  elif n in {'43722','43723'}:
   local=[[10 if n=='43722' else -10,0 if upper else 8,z] for z in (-20,0,20)]
  elif n=='60477':local=[[0,0,0]] if upper else [[0,24,z] for z in (-60,-40,-20,0)]
  elif n=='15068':local=[[x,0,z] for x in (-10,10) for z in (-10,10)]
  else:
   w,d,h=shapes[n]
   local=[[(x-(w-1)/2)*20,0 if upper else h,(z-(d-1)/2)*20]
          for x in range(w) for z in range(d)
          if not (n in {'3659','3307'} and not upper and x not in (0,w-1))]
  normal=mv(o['matrix'],[0,-1 if upper else 1,0])
  return [(plus(o['position'],mv(o['matrix'],v)),normal) for v in local]
 for o in rows:
  points=seats(o,True)
  if points is None:unknown[o['part']]+=1;continue
  for p,n in points:tops[key(p)].append((o['id'],p,n))
 for o in rows:
  for p,n in seats(o,False) or []:
   for k in neighbors(p):
    for other,q,normal in tops[k]:
     if other!=o['id'] and close(p,q) and abs(dot(n,normal)+1)<1e-5:
      adj[other].add(o['id']);adj[o['id']].add(other)
      contact_pairs[tuple(sorted((other,o['id'])))]+=1
  n=Path(o['part']).stem
  if n in hinges:
   family,sex,pivot,axis=hinges[n];p=plus(o['position'],mv(o['matrix'],pivot));axis=mv(o['matrix'],axis)
   for k in neighbors(p):
    for other,f,s,q,a in pivots[k]:
     if family==f and sex!=s and close(p,q) and abs(abs(dot(axis,a))-1)<1e-5:
      adj[other].add(o['id']);adj[o['id']].add(other);hinge_pairs.add(tuple(sorted((other,o['id']))))
   pivots[key(p)].append((o['id'],family,sex,p,axis))
 remaining=set(ids);components=[]
 while remaining:
  seen=set();todo=[min(remaining)]
  while todo:
   id=todo.pop()
   if id in seen:continue
   seen.add(id);todo.extend(adj[id]-seen)
  remaining-=seen;components.append(sorted(seen))
 components.sort(key=lambda c:(-len(c),c[0]))
 return {'components':components,'unsupported_parts':dict(unknown),
         'stud_matches':sum(contact_pairs.values()),'hinge_pairs':sorted(hinge_pairs),
         'stud_pairs':dict(contact_pairs),'instances':len(rows)}

def report_stud_connectivity(model,prefix='',expected=None):
 # Derive from actual FILE references, not potentially stale !BRICK_STATE positions.
 result=stud_connectivity(sync_state(model,write=False),prefix)
 print('NOMINAL CONNECTIVITY:',prefix or '(all)',result['instances'],'instances;',
       result['stud_matches'],'stud-grid matches;',len(result['hinge_pairs']),'hinge pairs')
 print('Component sizes:',[len(c) for c in result['components']])
 for c in result['components']:
  print(' COMPONENT',len(c),'parts; sample IDs:',','.join(c[:8]))
 print('Unsupported part instances:',result['unsupported_parts'])
 print('SCOPE: named nominal seating grids and hinge center/axis coincidence only; '
       'unsupported or unmodeled side connections remain unresolved. Not clutch, mesh, torque or load verification.')
 if expected is not None:
  if result['unsupported_parts']:raise ValueError('Cannot assert component count with unsupported parts')
  if len(result['components'])!=expected:
   raise ValueError('Expected '+str(expected)+' nominal components; found '+str(len(result['components'])))
 return result

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
 print('NOT VERIFIED: physical assembly/clutch, exact mesh collision, joint range/strength, load stability, superiority to reference product.')
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('model',type=Path);parser.add_argument('--check-body-overlaps',action='store_true',help='직육면체 브릭 몸체의 명목 간섭 검사; 실패 시 0이 아닌 코드 반환');parser.add_argument('--sync-state',action='store_true',help='schema 3 본문 기준 상태 갱신; 반복 호출의 ID가 모호하면 저장 없이 실패');parser.add_argument('--sync-only',action='store_true',help='--sync-state와 함께 상태 갱신만 실행')
 parser.add_argument('--check-stud-connectivity',action='store_true',help='본문에서 명목 스터드·힌지 연결망 보고; 실물 체결 검사가 아님')
 parser.add_argument('--instance-prefix',default='',help='연결망을 검사할 물리 ID 접두어, 예: A-')
 parser.add_argument('--expect-stud-components',type=int,help='지원 부품으로만 구성된 범위의 예상 연결 성분 수; 다르면 실패')
 args=parser.parse_args()
 if args.sync_only and not args.sync_state:parser.error('--sync-only requires --sync-state')
 if args.instance_prefix and not args.check_stud_connectivity:parser.error('--instance-prefix requires --check-stud-connectivity')
 if args.expect_stud_components is not None and args.expect_stud_components<1:parser.error('--expect-stud-components must be positive')
 if args.expect_stud_components is not None and not args.check_stud_connectivity:parser.error('--expect-stud-components requires --check-stud-connectivity')
 if args.sync_state:sync_state(args.model)
 if args.check_stud_connectivity:report_stud_connectivity(args.model,args.instance_prefix,args.expect_stud_components)
 if not args.sync_only:run(args.model,args.check_body_overlaps)
