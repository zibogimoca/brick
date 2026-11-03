"""Generate a fixed-pose, stud-connected skeletal Tyrannosaurus display study in one MPD."""
import hashlib,json,math
from collections import Counter,defaultdict
from decimal import Decimal
from pathlib import Path
D=json.loads(Path('docs/gobricks-dictionary.json').read_text());parts={p['gobricks_id']:p for p in D['parts']}
# part, GoBricks ID, nominal footprint in studs, body height in plate units
spec={'3001':('542',4,2,3),'3003':('540',2,2,3),'3005':('531',1,1,3),'3020':('511',4,2,1),'3024':('501',1,1,1),'3004':('532',2,1,3),'3010':('534',4,1,3),'3023b':('502',2,1,1),'3022':('509',2,2,1),'3710':('504',4,1,1),'3034':('513',8,2,1),'3832':('514',10,2,1),'3031':('519',4,4,1),'3032':('520',6,4,1),'3062b':('605',1,1,3),'6141':('615',1,1,1),'54200':('833',1,1,2),'15068':('659',2,2,2),'59900':('606',1,1,3)}
I=[1,0,0,0,1,0,0,0,1];YAW=[0,0,1,0,1,0,-1,0,0]
items=[];occupied={};contacts=[]
def put(part,x,z,top,group,color=19,yaw=False):
 gid,l,w,h=spec[part];l,w=(w,l) if yaw else (l,w);bottom=top-h
 cells={(i,j,k) for i in range(x,x+l) for j in range(z,z+w) for k in range(bottom,top)}
 for cell in cells:assert cell not in occupied,('Overlapping nominal body volumes',part,group,cell,occupied.get(cell))
 offers=[o for o in parts[gid]['offers'] if str(D['colors'][o['color_id']].get('ldraw_color_id'))==str(color) and (o['inventory_at_observation'] or 0)>0]
 assert offers,('No sale color',gid,color)
 offer=offers[0];item={'id':f'{group}-{sum(o["group"]==group for o in items)+1:03}','group':group,'part':part+'.dat','gobricks_id':gid,'sku':offer['sku'],'color':color,'position':[(x+(l-1)/2)*20,-top*8,(z+(w-1)/2)*20],'matrix':YAW if yaw else I,'grid':{'x':x,'z':z,'length':l,'width':w,'top':top,'bottom':bottom},'top_studs':part not in ['54200','15068','59900']}
 for cell in cells:occupied[cell]=item['id']
 items.append(item)
# A connected two-layer museum base; offset upper plates bridge all lower seams.
for x in range(-10,38,6):
 for z in [-1,3,7]:put('3032',x,z,0,'display-base',0)
for x in range(-7,35,6):
 for z in [0,4,8]:put('3032',x,z,1,'display-base',0)
# Three toes per foot, ankle, forward knee and large thigh.
for side,z0 in [('left',0),('right',8)]:
 for toe in range(3):
  put('3710',15,z0+toe,2,side+'-foot');put('54200',18,z0+toe,4,side+'-claws',15)
 put('3031',12,z0,3,side+'-foot')
 for level in [6,9]:put('3003',13,z0+1,level,side+'-shin')
 put('3020',13,z0+1,10,side+'-knee')
 for level in [13,16,19]:put('3003',15,z0+1,level,side+'-thigh')
# An explicit display support under the pelvis limits unsupported cantilever demand.
for level in [4,7,10,13,16,19]:put('3003',15,4,level,'display-support',0)
put('3832',15,1,20,'pelvis',yaw=True)
for z in [4,6]:
 put('3034',11,z,21,'torso-frame');put('3020',19,z,21,'torso-frame')
# Open ribs rather than a filled torso.
for x in [12,15,18,21]:
 for z in [4,7]:
  for level in [24,27,30]:put('3062b',x,z,level,'ribs')
 put('3010',x,4,33,'ribs',yaw=True)
for z in [5]:
 put('3034',11,z,34,'spine');put('3020',19,z,34,'spine')
put('3020',17,5,35,'spine')
for x in [12,15]:
 for z in [4,7]:put('59900',x,z,36,'spinal-processes')
# Long tapered tail; underlapping plates carry the final progressively lower tip.
put('3832',3,5,22,'tail')
for x in [3,5,7,9,11]:put('3022',x,5,23 if x<9 else 25,'tail') if x<9 else put('3003',x,5,25,'tail')
put('3034',-4,5,21,'tail');put('3710',-7,5,20,'tail');put('3023b',-8,5,19,'tail')
# Small, two-finger forelimbs attached to the rib columns.
for side,z in [('left',3),('right',8)]:
 put('3023b',18,z if side=='left' else 7,34,side+'-arm',yaw=True)
 put('3062b',18,z,37,side+'-arm')
 put('3710',18,z,38,side+'-arm')
 put('3023b',21,z if side=='left' else 8,39,side+'-hand',yaw=True)
 for finger in range(2):put('54200',21,(z if side=='left' else 8)+finger,41,side+'-fingers',15)
# Rising neck and large open skull. Mouth and eye cavities are deliberate open space.
put('3003',20,5,38,'neck');put('3020',20,5,39,'neck');put('3003',22,5,42,'neck')
for z in [4,6]:put('3034',22,z,43,'lower-jaw')
for z in [4,7]:
 put('3710',26,z,44,'lower-jaw')
 for x in [26,27,29]:put('59900',x,z,47,'teeth',15)
for level in [46,49]:put('3001',22,4,level,'skull',yaw=True)
for z in [4,6]:put('3034',22,z,50,'skull')
put('3031',22,4,51,'skull')
for z in [4,6]:put('15068',26,z,52,'snout')
for z in [4,7]:put('6141',28,z,51,'nostrils',0)
# Check nominal seating-grid connectivity, independently of the order of generation.
graph={o['id']:set() for o in items}
for a in items:
 ga=a['grid']
 for b in items:
  gb=b['grid']
  if a is b or not a['top_studs'] or ga['top']!=gb['bottom']:continue
  xs=set(range(ga['x'],ga['x']+ga['length']))&set(range(gb['x'],gb['x']+gb['length']))
  zs=set(range(ga['z'],ga['z']+ga['width']))&set(range(gb['z'],gb['z']+gb['width']))
  if xs and zs:
   graph[a['id']].add(b['id']);graph[b['id']].add(a['id']);contacts.append({'a':a['id'],'b':b['id'],'studs':len(xs)*len(zs)})
seen=set();queue=[items[0]['id']]
while queue:
 n=queue.pop()
 if n in seen:continue
 seen.add(n);queue+=list(graph[n]-seen)
assert len(seen)==len(items),('Disconnected pieces',[o['id'] for o in items if o['id'] not in seen])
counts=Counter(o['sku'] for o in items);offers={o['sku']:o for p in parts.values() for o in p['offers']};cost=Decimal('0')
for sku,n in counts.items():assert offers[sku]['inventory_at_observation']>=n,(sku,n);cost+=Decimal(offers[sku]['unit_price_cny'])*n
state={'status':'complete_first_digital_design_physical_validation_pending','model':'Tyrannosaurus skeletal display','style':'Stud-grid stylized fossil skeleton; fixed pose with explicit black display base/support. Not a replica of an official set.','requirements':['large open skull','long tapering tail','two hind legs with three toes each','two short forelimbs with two fingers each','open rib cage','display support'],'piece_count':len(items),'unique_sale_skus':len(counts),'listed_retail_parts_cost_cny':str(cost),'cost_scope':'Public listed unit prices at catalog observation; shipping/tax/bulk discounts excluded.','validation':{'nominal_body_grid_overlaps':0,'all_pieces_in_one_stud_contact_graph':True,'reference_asset_closure':'verified separately','exact_mesh_collision':'not_tested','clutch_and_load':'not_tested','physical_build':'not_tested'},'next':'Review the complete rendered design; refine silhouette and connections based on user feedback; physically test joints before assembly claims.','instances':items,'contacts':contacts,'bom':[{'sku':s,'quantity':n,'unit_price_cny':offers[s]['unit_price_cny']} for s,n in sorted(counts.items())]}
# Model plus metadata and submodels are a single editable source file.
lines=['0 FILE tyrannosaurus.ldr','0 BRICK Fossils - Tyrannosaurus','0 Name: tyrannosaurus.mpd','0 Author: BRICK project','0 !BRICK_STATE '+json.dumps(state,separators=(',',':'))]
groups=list(dict.fromkeys(o['group'] for o in items))
for g in groups:lines.append('1 16 0 0 0 1 0 0 0 1 0 0 0 1 '+g+'.ldr')
for g in groups:
 lines+=['0 FILE '+g+'.ldr','0 '+g]
 for o in items:
  if o['group']==g:lines+=['0 !BRICK_INSTANCE '+o['id']+' '+o['sku'],'1 '+str(o['color'])+' '+' '.join(str(v) for v in o['position']+o['matrix'])+' '+o['part']]
lines.append('0 NOFILE');Path('models/tyrannosaurus.mpd').write_text('\n'.join(lines)+'\n')
print('Complete digital first design:',len(items),'pieces,',len(counts),'sale SKUs,',len(groups),'submodels,',cost,'CNY listed retail.')
