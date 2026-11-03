"""Validate exported MPD records, licensed reference assets and nominal stud-grid connectivity."""
import hashlib,json,math
from pathlib import Path
from collections import Counter
from decimal import Decimal
root=Path('assets/ldraw');manifest=json.loads(Path('assets/policy.md').read_text().split('<!-- asset-manifest:start -->\n```json\n',1)[1].split('\n```\n<!-- asset-manifest:end -->',1)[0])
for rel,entry in manifest['files'].items():
 data=(root/rel).read_bytes();assert hashlib.sha256(data).hexdigest()==entry['sha256'],rel
 assert len(data)==entry['bytes'],rel
 for line in data.decode('utf-8-sig').splitlines():
  f=line.split(maxsplit=14)
  if len(f)==15 and f[0]=='1':
   name=f[14].replace('\\','/').lower();assert any((root/p/name).is_file() for p in ['parts','p','']),name
text=Path('models/tyrannosaurus.mpd').read_text();state=json.loads(next(l.split(' ',2)[2] for l in text.splitlines() if l.startswith('0 !BRICK_STATE ')))
items={i['id']:i for i in state['instances']};exported={};current=None
for line in text.splitlines():
 if line.startswith('0 !BRICK_INSTANCE '):current=line.split()[2]
 if line.startswith('1 ') and line.split()[-1].endswith('.dat'):
  fields=line.split();assert current and current not in exported;exported[current]=fields
assert set(exported)==set(items) and len(items)==state['piece_count']==160
occupied={}
for key,fields in exported.items():
 o=items[key];g=o['grid'];assert fields[14]==o['part'];assert int(fields[1])==o['color']
 assert [float(n) for n in fields[2:14]]==o['position']+o['matrix']
 m=o['matrix'];assert abs(m[0]*(m[4]*m[8]-m[5]*m[7])-m[1]*(m[3]*m[8]-m[5]*m[6])+m[2]*(m[3]*m[7]-m[4]*m[6])-1)<1e-9
 assert o['position']==[(g['x']+(g['length']-1)/2)*20,-g['top']*8,(g['z']+(g['width']-1)/2)*20]
 for x in range(g['x'],g['x']+g['length']):
  for z in range(g['z'],g['z']+g['width']):
   for level in range(g['bottom'],g['top']):
    cell=(x,z,level);assert cell not in occupied,(key,occupied.get(cell));occupied[cell]=key
connections={k:set() for k in items}
for ka,a in items.items():
 ga=a['grid']
 for kb,b in items.items():
  gb=b['grid']
  if ka==kb or not a['top_studs'] or ga['top']!=gb['bottom']:continue
  if max(ga['x'],gb['x'])<min(ga['x']+ga['length'],gb['x']+gb['length']) and max(ga['z'],gb['z'])<min(ga['z']+ga['width'],gb['z']+gb['width']):connections[ka].add(kb);connections[kb].add(ka)
seen=set();queue=[next(iter(items))]
while queue:
 k=queue.pop()
 if k in seen:continue
 seen.add(k);queue+=list(connections[k]-seen)
assert seen==set(items),'Disconnected source model'
d=json.loads(Path('docs/gobricks-dictionary.json').read_text());parts={p['gobricks_id']:p for p in d['parts']};offers={o['sku']:o for p in parts.values() for o in p['offers']};counts=Counter(o['sku'] for o in items.values());total=Decimal('0')
for sku,count in counts.items():
 assert offers[sku]['inventory_at_observation']>=count;total+=Decimal(offers[sku]['unit_price_cny'])*count
assert total==Decimal(state['listed_retail_parts_cost_cny'])
for o in items.values():
 p=parts[o['gobricks_id']];assert p['geometry'] and p['geometry']['file'].endswith('/'+o['part']);assert str(d['colors'][offers[o['sku']]['color_id']]['ldraw_color_id'])==str(o['color'])
assert len(list(Path('docs').iterdir()))==3
assert all(any(g in o['group'] for o in items.values()) for g in ['skull','neck','ribs','tail','left-foot','right-foot','left-arm','right-arm'])
print('PASS:',len(manifest['files']),'asset hashes/dependencies;',len(items),'exported part placements; no nominal body overlaps; one contact graph; source SKU/color availability; BOM and listed retail total',total,'CNY.')
print('Not tested: exact mesh collision, manufacturing tolerance, physical assembly, clutch strength or load stability.')
