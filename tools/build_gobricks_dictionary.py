"""Build and validate the single shared dictionary from official catalog page responses."""
import argparse,hashlib,json,math
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--cache',type=Path,required=True)
p.add_argument('--output',type=Path,default=Path('docs/gobricks-dictionary.json'))
a=p.parse_args();first=json.loads((a.cache/'0001.json').read_text());total=first['count'];pages=math.ceil(total/96)
rows={};evidence=[]
for page in range(1,pages+1):
 f=a.cache/f'{page:04}.json';d=json.loads(f.read_text())
 assert d['count']==total,'Catalog count changed'
 assert len(d['rows'])==min(96,total-(page-1)*96),'Unexpected page length'
 evidence.append({'offset':(page-1)*96,'rows':len(d['rows']),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
 for row in d['rows']:
  assert row['id'] not in rows,'Duplicate sale SKU'
  rows[row['id']]=row
assert len(rows)==total
parts={};colors={}
for row in rows.values():
 key=str(row['product_id']);part=parts.setdefault(key,{'gobricks_id':key,'names':[],'categories':[],'ldraw_candidates':[],'geometry':None,'dimensions':None,'connectors':None,'geometry_verification':'not_verified','offers':[]})
 for field,values in [('names',[row.get('caption_en'),row.get('caption')]),('categories',[row.get('ldd_catalog')]),('ldraw_candidates',str(row.get('ldraw_no') or '').split(','))]:
  for value in values:
   value=(value or '').strip()
   if value and value not in part[field]:part[field].append(value)
 color_id=str(row['color_id']);c=row.get('color_data') or {}
 colors[color_id]={k:c.get(k) for k in ['id','name','name_en','color','lego_color_id','ldraw_color_id','brick_link_color_id']}
 price=str(row['price']) if row.get('price') is not None else None
 if price is not None:assert Decimal(price).is_finite() and Decimal(price)>=0
 part['offers'].append({'sku':row['id'],'color_id':color_id,'unit_price_cny':price,'list_unit_price_cny':row.get('eshop_price'),'source_discount_percent_of_list':row.get('discount'),'inventory_at_observation':row.get('inventory'),'purchase_limit':row.get('buy_limit'),'shelf_state':row.get('shelf_state'),'enabled':row.get('enable'),'image_url':row.get('picture'),'source_url':'https://gobricks.cn/part_detail/'+row['id']})
for part in parts.values():part['offers'].sort(key=lambda x:x['sku'])
result={'schema_version':2,'status':'sale_catalog_collected_geometry_pending','observed_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'collection':{'scope':'Public manufacturer type=2 catalog, variety=all; no in-stock filter. Other product types excluded.','endpoint':'https://gobricks.cn/frontend/v1/item/filter','query':{'limit':96,'type':2,'variety':'all','orderby':'created_at','order_direction':'desc'},'page_count':pages,'expected_sale_variant_count':total,'collected_sale_variant_count':len(rows),'collected_shape_count':len(parts),'listing_complete_for_query':True,'geometry_complete':False,'source_pages':evidence},'pricing':{'currency':'CNY','purchase_unit_quantity':1,'basis':'Public product detail shows per-item price and quantity selector starting at 1. purchase_limit is an order cap, not bundle quantity.','bulk_offers':[],'bulk_pricing_status':'No verified bundle or quantity-price tiers collected; do not infer discounts for 100 or 1000 pieces.','cost_estimation':'Displayed retail unit price times model quantity is a retail parts estimate, not bulk procurement cost. Shipping, tax and currency conversion excluded.','bundle_offer_fields_when_verified':['sku','quantity','total_price','currency','unit_price','minimum_order_quantity','source_url','observed_at']},'geometry_note':'LDraw identifiers are manufacturer-listed candidates, not verified interchangeable mappings. No geometry or connector measurements were collected.','colors':colors,'parts':sorted(parts.values(),key=lambda x:x['gobricks_id'])}
tmp=a.output.with_suffix('.tmp');tmp.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');json.loads(tmp.read_text());tmp.replace(a.output)
print('Validated shapes:',len(parts),'sale variants:',len(rows),'colors:',len(colors),'pages:',pages)
