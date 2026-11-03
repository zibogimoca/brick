"""
기능: 확보한 형상에서 외곽 치수와 일부 연결 위치를 계산해 부품 사전에 반영한다.
입력: assets의 형상, docs/gobricks-dictionary.json, 코드의 부품 대응 mapping.
출력: docs/gobricks-dictionary.json의 형상 참조·해시·치수·선택된 연결 정보.
실행: python3 tools/enrich_dictionary.py
주의: 현재 대응표에 등록된 38종을 처리한다. 다른 부품에는 대응과 연결 규칙 검토가 필요하다.
한계: 일부 연결은 추정이며 실물 공차·결합력·하중을 검증하지 않는다.
      모델을 생성하는 도구가 아니다.
"""
import hashlib,json,math
from pathlib import Path
ROOT=Path('assets')
IDENTITY=[1,0,0,0,1,0,0,0,1]
def mv(m,v):return [sum(m[r*3+c]*v[c] for c in range(3)) for r in range(3)]
def mm(a,b):return [sum(a[r*3+k]*b[k*3+c] for k in range(3)) for r in range(3) for c in range(3)]
def add(a,b):return [x+y for x,y in zip(a,b)]
def resolve(name):
 name=name.replace('\\','/').lower()
 for directory in ['','parts','primitives']:
  p=ROOT/directory/name
  if p.is_file():return p
 raise ValueError(name)
def flatten(name,m=None,t=None,stack=()):
 m=IDENTITY if m is None else m;t=[0,0,0] if t is None else t;p=resolve(name)
 assert p not in stack,'Cyclic reference'
 vertices=[];studs=[]
 for line in p.read_text(errors='strict').splitlines():
  fields=line.split(maxsplit=14)
  if not fields:continue
  if fields[0]=='1' and len(fields)==15:
   tm=list(map(float,fields[2:5]));rm=list(map(float,fields[5:14]));world_t=add(t,mv(m,tm));world_m=mm(m,rm);child=fields[14]
   if Path(child.lower()).name in ['stud.dat','stud2.dat','stud2a.dat']:
    studs.append({'kind':'stud','position':world_t,'axis':mv(world_m,[0,-1,0]),'evidence':str(p)+' -> '+child})
   v,s=flatten(child,world_m,world_t,stack+(p,));vertices+=v;studs+=s
  elif fields[0] in ['3','4']:
   nums=list(map(float,line.split()[2:]));vertices += [add(t,mv(m,nums[i:i+3])) for i in range(0,len(nums),3)]
 return vertices,studs
mapping={'542':'3001','540':'3003','531':'3005','511':'3020','501':'3024','623':'3700','578':'3705','912':'4274','807':'2429','808':'2430','849':'14417','851':'14418','904':'14419'}
mapping.update({'532':'3004','534':'3010','533':'3622','502':'3023b','509':'3022','504':'3710','503':'3623','505':'3666','506':'3460','513':'3034','514':'3832','519':'3031','520':'3032','605':'3062b','615':'6141','609':'4032','607':'3941','833':'54200','656':'11477','659':'15068','606':'59900','883':'30374','646':'60478','508':'60479','587':'60477'})
p=Path('docs/gobricks-dictionary.json');dictionary=json.loads(p.read_text())
for part in dictionary['parts']:
 if part['gobricks_id'] not in mapping:continue
 name=mapping[part['gobricks_id']];v,studs=flatten(name+'.dat')
 lo=[min(x[i] for x in v) for i in range(3)];hi=[max(x[i] for x in v) for i in range(3)]
 part['geometry']={'file':'assets/parts/'+name+'.dat','sha256':hashlib.sha256((ROOT/'parts'/f'{name}.dat').read_bytes()).hexdigest(),'source':'LDraw official complete.zip','mapping_basis':'Manufacturer-listed LDraw candidate and source name checked; exact GoBricks mold equivalence and physical tolerance NOT measured.','asset_manifest':'assets/policy.md#에셋-목록'}
 part['dimensions']={'units':'LDU','mm_per_ldu':0.4,'frame':'right-handed, up=-Y, original LDraw origin','bounds':{'min':lo,'max':hi},'size_mm':[round((hi[i]-lo[i])*.4,6) for i in range(3)],'basis':'Recursive triangle/quad vertex envelope of LDraw reference geometry; includes protrusions, not a physical measurement.'}
 connectors=list(studs)
 for idx,c in enumerate(connectors):c['id']='stud-'+str(idx)
 if name in ['3001','3003','3005','3020','3024','14417','14418','14419']:
  bottom=24 if name.startswith('300') else 8
  for idx,stud in enumerate(studs):
   # Corresponding underside grid acceptance position is inferred, not a measured clutch contact.
   connectors.append({'id':'underside-'+str(idx),'kind':'stud_receptacle','position':[stud['position'][0],bottom,stud['position'][2]],'axis':[0,1,0],'evidence':'Top stud grid projected to nominal bottom seating plane; mating semantics inferred, not physical clutch verification.'})
 if name in ['14418','14419']:connectors.append({'id':'socket','kind':'joint8_socket','position':[30,4,0],'axis':[1,0,0],'evidence':f'assets/parts/{name}.dat type-1 joint8socket1.dat translation; source !HELP documents motion but no physical test.'})
 if name=='14419':connectors.append({'id':'ball','kind':'joint8_ball','position':[-30,4,0],'axis':[-1,0,0],'evidence':'14419.dat sphere primitive translations and center of 8-8sphe.dat.'})
 if name=='14417':connectors.append({'id':'ball','kind':'joint8_ball','position':[0,4,-20],'axis':[0,0,-1],'evidence':'14417.dat joint8ball.dat translation.'})
 if name=='3700':connectors.append({'id':'pin-hole','kind':'technic_pin_hole','position':[0,10,0],'axis':[0,0,1],'evidence':'3700.dat opposing peghole.dat instances at z=+/-10; seating/insertion not verified.'})
 part['connectors']=connectors or None
 part['geometry_verification']='reference_mesh_resolved; reference bounds computed; selected connector annotations; physical fit unverified'
 # Save only top stud and selected connection information, not an exhaustive automatic connection inventory.
 part['connection_inventory_scope']='Selected obvious stud/underside and named joint primitives only; not all legal attachment modes or physical compatibility.'
dictionary['geometry_enrichment']={'reference_parts_prepared':len(mapping),'reference_assets':'assets/policy.md#에셋-목록','physical_tests':False,'remaining_parts_geometry_pending':len(dictionary['parts'])-len(mapping)}
p.write_text(json.dumps(dictionary,ensure_ascii=False,indent=2)+'\n')
print('Enriched',len(mapping),'reference parts with resolved geometry and selected connection annotations.')
