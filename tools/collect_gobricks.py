import urllib.request,urllib.parse,json,math,time,concurrent.futures
from pathlib import Path
import argparse
parser=argparse.ArgumentParser(description='Collect the public GoBricks catalog. Use a fresh cache for a new observation.')
parser.add_argument('--cache',type=Path,required=True)
args=parser.parse_args()
cache=args.cache;cache.mkdir(parents=True,exist_ok=True)
base={'limit':96,'type':2,'variety':'all','orderby':'created_at','order_direction':'desc'}
def fetch(page):
 p=cache/f'{page:04}.json'
 if p.exists():return page,json.loads(p.read_text())
 q=base|{'offset':(page-1)*96}
 req=urllib.request.Request('https://gobricks.cn/frontend/v1/item/filter?'+urllib.parse.urlencode(q),headers={'platform':'pc','Accept':'application/json'})
 with urllib.request.urlopen(req,timeout=40) as r:d=json.load(r)
 d=d.get('data',d);assert isinstance(d['rows'],list) and isinstance(d['count'],int)
 p.write_text(json.dumps(d,ensure_ascii=False));return page,d
p,first=fetch(1);total=first['count'];pages=math.ceil(total/96);seen={}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for page,data in pool.map(fetch,range(1,pages+1)):
  for row in data['rows']:seen[str(row['id'])]=row
  if page%10==0 or page==pages:print('pages',page,'/',pages,'unique sale variants',len(seen),'expected',total,flush=True)
assert len(seen)==total, 'Incomplete catalog; do not mark collection complete'
print('All sale SKUs collected; run build_gobricks_dictionary.py on this cache.')
