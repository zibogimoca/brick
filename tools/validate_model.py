"""
기능: 지정한 MPD의 실제 배치와 상태 기록, 부품 사전·가격·형상 무결성을 검사한다.
입력: models/<모델>.mpd 위치 인자, docs/gobricks-dictionary.json, assets/policy.md.
선택: --check-body-overlaps로 직육면체 몸체 겹침을 검사한다. 곡선·관절은 제외한다.
출력: 콘솔 검사 결과만 출력한다. 파일을 생성·수정하지 않는다.
실행: python3 tools/validate_model.py models/tyrannosaurus-v1.mpd
범위: BRICK schema_version 3; 계층 변환·회전행렬·수량·SKU·색상·중복 배치 검사.
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
   fields=line.split();assert current and len(fields)==15
   defs[current].append((marker,int(fields[1]),list(map(float,fields[2:5])),list(map(float,fields[5:14])),fields[14]));marker=None
 exported={};identity=[1,0,0,0,1,0,0,0,1]
 def visit(name,mat,pos,stack=()):
  assert name not in stack,'Cyclic MPD submodel'
  for ident,color,t,m,child in defs[name]:
   rm=mm(mat,m);rt=plus(pos,mv(mat,t))
   if child.endswith('.dat'):
    assert ident and ident not in exported,'Duplicate or missing instance ID'
    assert (root/'parts'/child).is_file(),child
    exported[ident]=(color,rt,rm,child)
   else:
    assert child in defs,child
    visit(child,rm,rt,stack+(name,))
 visit(next(iter(defs)),identity,[0,0,0])
 items={i['id']:i for i in state['instances']};assert len(items)==len(state['instances'])
 assert set(items)==set(exported) and len(items)==state['piece_count']
 d=json.loads(Path('docs/gobricks-dictionary.json').read_text());parts={p['gobricks_id']:p for p in d['parts']};counts=Counter();total=Decimal(0);seen=set();lo=[float('inf')]*3;hi=[-float('inf')]*3
 for ident,o in items.items():
  color,t,m,part=exported[ident];assert color==o['color'] and part==o['part'] and near(t,o['position']) and near(m,o['matrix']),ident
  assert all(math.isfinite(x) for x in t+m),ident
  transposed=[m[c*3+r] for r in range(3) for c in range(3)];assert near(mm(m,transposed),identity),'Scaled/skewed physical part '+ident
  det=m[0]*(m[4]*m[8]-m[5]*m[7])-m[1]*(m[3]*m[8]-m[5]*m[6])+m[2]*(m[3]*m[7]-m[4]*m[6]);assert abs(det-1)<1e-5,'Mirrored physical part '+ident
  key=(part,tuple(round(x,4) for x in t+m));assert key not in seen,'Exact duplicate part placement '+ident;seen.add(key)
  p=parts[o['gobricks_id']];offer=next(v for v in p['offers'] if v['sku']==o['sku']);assert str(d['colors'][offer['color_id']]['ldraw_color_id'])==str(color)
  assert Path(p['geometry']['file']).name==part and hashlib.sha256(Path(p['geometry']['file']).read_bytes()).hexdigest()==p['geometry']['sha256']
  counts[o['sku']]+=1;total+=Decimal(offer['unit_price_cny'])
  if o['group']!='support':
   bounds=p['dimensions']['bounds']
   for x in [bounds['min'][0],bounds['max'][0]]:
    for y in [bounds['min'][1],bounds['max'][1]]:
     for z in [bounds['min'][2],bounds['max'][2]]:
      q=plus(t,mv(m,[x,y,z]));lo=[min(a,b) for a,b in zip(lo,q)];hi=[max(a,b) for a,b in zip(hi,q)]
 assert total==Decimal(state['listed_retail_parts_cost_cny']) and len(counts)==state['unique_sale_skus']
 alloffers={o['sku']:o for p in d['parts'] for o in p['offers']}
 for sku,count in counts.items():assert alloffers[sku]['inventory_at_observation']>=count,sku+' exceeds recorded stock'
 for j in state.get('joints',[]):
  assert j['submodel'] in defs
  for axis,limits in j['axes'].items():assert axis in 'xyz' and len(limits)==2 and limits[0]<=0<=limits[1]
 measured=dict(zip(['length','height','width'],[round((b-a)*.04,2) for a,b in zip(lo,hi)]));assert measured==state['reference_geometry_bounds_cm'],measured
 if check_body:
  errors=body_overlaps(state,parts)
  print('Nominal rectangular body intersections:',len(errors))
  print('Groups:',dict(Counter(tuple(sorted([a['group'],b['group']])) for a,b in errors)))
  for a,b in errors[:20]:print(a['id'],a['part'],a['group'],a['position'],'<>',b['id'],b['part'],b['group'],b['position'])
  assert not errors,'Nominal rectangular bodies intersect; do not treat this design as assembly-ready'
 print('DATA PASS:',model,len(items),'physical part references;',len(manifest['files']),'asset hashes;',len(counts),'SKUs;',total,'CNY')
 print('Reference geometry bounding envelope (cm):',measured)
 print('NOT VERIFIED: assembly connectivity, exact mesh collision, joint range/strength, load stability, superiority to reference product.')
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('model',type=Path);parser.add_argument('--check-body-overlaps',action='store_true',help='직육면체 브릭 몸체의 명목 간섭 검사; 실패 시 0이 아닌 코드 반환');args=parser.parse_args();run(args.model,args.check_body_overlaps)
