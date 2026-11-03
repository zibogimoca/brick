"""
기능: 공식 LDraw ZIP에서 지정 부품과 참조 조각을 추출하고 읽기 쉬운 경로로 변환한다.
입력: archive 위치 인자(이미 확보한 complete.zip); 코드의 TOP 부품 목록.
출력: assets/parts, assets/primitives, assets/LDConfig.ldr와 assets/policy.md 내부 목록.
실행: python3 tools/prepare_geometry.py <complete.zip 경로>
주의: TOP에 없는 기존 형상은 정리될 수 있다. 모든 모델의 필요 부품을 확인하고
      새 형상 파일 생성 범위를 먼저 보고한다. 별도 manifest 파일은 만들지 않는다.
한계: 형상 출처와 무결성을 기록하며, 고브릭스 실물과의 일치를 보장하지 않는다.
"""
import argparse,hashlib,json,zipfile
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('archive',type=Path);args=p.parse_args()
ROOT=Path('assets');TOP=['3001','3003','3005','3020','3024','3700','3705','4274','2429','2430','14417','14418','14419','3004','3010','3622','3023b','3022','3710','3623','3666','3460','3034','3832','3031','3032','3062b','6141','4032','3941','54200','11477','15068','59900','30374','60478','60479','60477']
source='https://library.ldraw.org/library/updates/complete.zip'
def local_path(name):
 return name.replace('parts/s/', 'parts/subparts/').replace('p/48/', 'primitives/high-resolution/').replace('p/', 'primitives/', 1) if name.startswith('p/') else name.replace('parts/s/', 'parts/subparts/')
ROOT.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(args.archive) as z:
 names={n.lower():n for n in z.namelist()};done={};queue={'parts/'+x+'.dat' for x in TOP}
 def resolve(name):
  name=name.replace('\\','/').lower();assert '..' not in name.split('/') and not name.startswith('/')
  for rel in ['parts/'+name,'p/'+name,name]:
   if 'ldraw/'+rel in names:return rel
  raise ValueError('Missing dependency: '+name)
 while queue:
  rel=queue.pop()
  if local_path(rel) in done:continue
  original=names['ldraw/'+rel];data=z.read(original) # zipfile validates member CRC on read
  text=data.decode('utf-8-sig',errors='strict');lines=[]
  for line in text.splitlines(keepends=True):
   f=line.split(maxsplit=14)
   if len(f)==15 and f[0]=='1':
    child=resolve(f[14].strip());queue.add(child)
    ending='\r\n' if line.endswith('\r\n') else '\n' if line.endswith('\n') else ''
    line=' '.join(f[:14])+' '+local_path(child)+ending
   lines.append(line)
  converted=''.join(lines).encode('utf-8');local=local_path(rel)
  dest=ROOT/local;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(converted)
  done[local]={'source_archive':source,'archive_member':original,'source_sha256':hashlib.sha256(data).hexdigest(),'sha256':hashlib.sha256(converted).hexdigest(),'bytes':len(converted),'modification':'Dependency paths renamed for readable folders; geometry coordinates unchanged.','author':next((l[10:].strip() for l in text.splitlines() if l.startswith('0 Author:')),None),'license':next((l[11:].strip() for l in text.splitlines() if l.startswith('0 !LICENSE')),None)}
 for rel in ['LDConfig.ldr']:
  data=z.read(names['ldraw/'+rel.lower()]);(ROOT/rel).write_bytes(data)
  done[rel]={'source_archive':source,'archive_member':names['ldraw/'+rel.lower()],'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
 # Remove only stale geometry files from earlier downloads that are not in this closure.
 for folder in ['parts','p','primitives']:
  for f in (ROOT/folder).rglob('*.dat'):
   if f.relative_to(ROOT).as_posix() not in done:f.unlink()
 for folder in sorted((f for f in ROOT.rglob('*') if f.is_dir()),key=lambda f:len(f.parts),reverse=True):
  if not any(folder.iterdir()):folder.rmdir()
 manifest={'source':source,'archive_sha256':hashlib.sha256(args.archive.read_bytes()).hexdigest(),'verification':'HTTPS source, ZIP member CRCs and retained per-file SHA-256; archive SHA is an observation, not a separately published signature.','parts':TOP,'files':done}
 policy=ROOT/'policy.md';text=policy.read_text();start='<!-- asset-manifest:start -->\n```json\n';end='\n```\n<!-- asset-manifest:end -->'
 before,rest=text.split(start,1);_,after=rest.split(end,1)
 policy.write_text(before+start+json.dumps(manifest,ensure_ascii=False,indent=2)+end+after)
print('Extracted and verified',len(done),'files for',len(TOP),'parts')
