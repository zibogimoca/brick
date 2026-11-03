import './style.css';
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { LDrawLoader } from 'three/addons/loaders/LDrawLoader.js';
import { LDrawConditionalLineMaterial } from 'three/addons/materials/LDrawConditionalLineMaterial.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const $ = id => document.getElementById(id);
const scene = new THREE.Scene(); scene.background = new THREE.Color('#14191f');
const camera = new THREE.PerspectiveCamera(40, 1, .01, 1000000);
const renderer = new THREE.WebGLRenderer({ antialias: true }); renderer.setPixelRatio(Math.min(devicePixelRatio, 2)); $('viewport').append(renderer.domElement);
const controls = new OrbitControls(camera, renderer.domElement); controls.enableDamping = true;
scene.add(new THREE.HemisphereLight(0xffffff, 0x657080, 3));
const light = new THREE.DirectionalLight(0xffffff, 3); light.position.set(200, 400, 300); scene.add(light);
let model, selected, generation = 0;
const hidden = [];
function status(text) { $('status').textContent = text; }
function fit() {
  if (!model) return;
  const box = new THREE.Box3().setFromObject(model); if (box.isEmpty()) return;
  const size = box.getSize(new THREE.Vector3()); const center = box.getCenter(new THREE.Vector3());
  const radius = Math.max(size.x, size.y, size.z, 1) * .6;
  const distance = radius / Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)) * Math.max(1, 1 / camera.aspect);
  camera.position.copy(center).add(new THREE.Vector3(1, .7, 1).normalize().multiplyScalar(distance));
  camera.near = Math.max(radius / 10000, .001); camera.far = distance * 100; camera.updateProjectionMatrix();
  controls.target.copy(center); controls.update();
  for (let attempt = 0; attempt < 6; attempt++) {
    camera.updateMatrixWorld();
    let extent = 0;
    for (const x of [box.min.x, box.max.x]) for (const y of [box.min.y, box.max.y]) for (const z of [box.min.z, box.max.z]) {
      const point = new THREE.Vector3(x, y, z).project(camera);
      extent = Math.max(extent, Math.abs(point.x), Math.abs(point.y));
    }
    if (extent <= .9) break;
    camera.position.sub(center).multiplyScalar(extent / .9 * 1.03).add(center);
    controls.update();
  }
}
function dispose(object) { const materials = new Set(); object.traverse(o => { o.geometry?.dispose(); if (o.material) for (const m of [].concat(o.material)) materials.add(m); }); for (const m of materials) { for (const v of Object.values(m)) if (v?.isTexture) v.dispose(); m.dispose(); } }
async function open(buffer, name, revision) {
  const current = ++generation; let failed = false; status('모델을 읽는 중…'); $('load').disabled = true;
  const manager = new THREE.LoadingManager(); manager.onError = () => { failed = true; };
  let next, metadata;
  try {
    if (/\.(mpd|ldr)$/i.test(name)) {
      const loader = new LDrawLoader(manager); loader.smoothNormals = true;
      loader.setConditionalLineMaterial(LDrawConditionalLineMaterial);
      const library = $('library').value.trim();
      if (library) { const url = new URL(library); if (!['https:', 'http:'].includes(url.protocol)) throw new Error(); loader.setPartsLibraryPath(url.href.replace(/\/?$/, '/')); }
      else {
        loader.setPartsLibraryPath(new URL('./parts-library/', location.href).href);
        const manifestResponse = await fetch('./parts-library/policy.md');
        if (!manifestResponse.ok) throw new Error('Parts manifest missing');
        const policy = await manifestResponse.text();
        const manifest = JSON.parse(policy.split('<!-- asset-manifest:start -->\n```json\n')[1].split('\n```\n<!-- asset-manifest:end -->')[0]);
        for (const path of Object.keys(manifest.files)) {
          if (path.endsWith('.dat')) loader.fileMap[path.replace(/^(parts|primitives)\//, '')] = path;
        }
        manager.setURLModifier(url => {
          if (!url.startsWith(loader.partsLibraryPath)) return url;
          let relative = url.slice(loader.partsLibraryPath.length).toLowerCase();
          while (!manifest.files[relative] && /^(parts|primitives)\//.test(relative)) relative = relative.replace(/^(parts|primitives)\//, '');
          return manifest.files[relative] ? loader.partsLibraryPath + relative : url;
        });
      }
      await loader.preloadMaterials(loader.partsLibraryPath + 'LDConfig.ldr');
      const text = new TextDecoder().decode(buffer);
      const record = text.split('\n').find(line => line.startsWith('0 !BRICK_STATE '));
      if (record) { try { metadata = JSON.parse(record.slice(15)); } catch { /* optional model metadata */ } }
      next = await new Promise((resolve, reject) => loader.parse(text, resolve, reject));
      next.rotation.x = Math.PI;
    } else if (/\.(glb|gltf)$/i.test(name)) {
      next = (await new GLTFLoader(manager).parseAsync(buffer, '')).scene;
    } else throw new Error();
    if (current !== generation) { dispose(next); return; }
    if (failed || new THREE.Box3().setFromObject(next).isEmpty()) { dispose(next); throw new Error(); }
    if (model) { scene.remove(model); dispose(model); }
    model = next; scene.add(model); selected = null; hidden.length = 0; $('hide').disabled = true;
    $('selection').textContent = '부품을 클릭하면 선택됩니다.';
    $('empty').hidden = true; $('fit').disabled = false; $('reset').disabled = false; fit();
    renderer.domElement.dataset.modelLoaded = 'true';
    $('summary').textContent = metadata?.piece_count ? `${metadata.piece_count}개 부품 · 공개 판매가 기준 ${metadata.listed_retail_parts_cost_cny || '미확인'} CNY` : '';
    $('version').textContent = `${name} · ${revision}`; status('모델을 불러왔습니다. 조립 가능 여부를 검증한 결과는 아닙니다.');
  } catch (error) { console.error('Model loading failed', error); if (current === generation) status('모델을 완전히 불러오지 못했습니다. 파일 형식과 외부 부품 라이브러리를 확인하세요. 이전 모델이 있다면 그대로 표시됩니다.'); }
  finally { if (current === generation) $('load').disabled = !$('models').value; }
}
$('file').onchange = async e => { const file = e.target.files[0]; if (!file) return; const data = await file.arrayBuffer(); const hash = await crypto.subtle.digest('SHA-256', data); const revision = [...new Uint8Array(hash)].map(x => x.toString(16).padStart(2, '0')).join('').slice(0, 12); await open(data, file.name, revision); };
$('models').onchange = () => { $('load').disabled = !$('models').value; if ($('models').value) $('load').click(); };
let entries = [];
$('load').onclick = async () => { const entry = entries[Number($('models').value)]; if (!entry) return; try { const response = await fetch(entry.url); if (!response.ok) throw new Error(); await open(await response.arrayBuffer(), entry.url, entry.version || '버전 미지정'); } catch { status('공개 모델 파일을 가져오지 못했습니다.'); } };
$('fit').onclick = fit;
$('hide').onclick = () => { if (!selected) return; selected.visible = false; hidden.push(selected); selected = null; $('hide').disabled = true; $('selection').textContent = '선택한 부품을 숨겼습니다.'; };
$('reset').onclick = () => { for (const item of hidden) item.visible = true; hidden.length = 0; fit(); };
const raycaster = new THREE.Raycaster(); let down;
renderer.domElement.addEventListener('pointerdown', e => { down = [e.clientX, e.clientY]; });
renderer.domElement.addEventListener('pointerup', e => { if (!model || !down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 5) return; const rect = renderer.domElement.getBoundingClientRect(); raycaster.setFromCamera(new THREE.Vector2((e.clientX - rect.left) / rect.width * 2 - 1, -(e.clientY - rect.top) / rect.height * 2 + 1), camera); const hits = raycaster.intersectObject(model, true).filter(h => { for (let p = h.object; p; p = p.parent) if (!p.visible) return false; return h.object.isMesh; }); selected = hits[0]?.object || null; while (selected?.parent && selected.parent !== model && selected.userData.type !== 'Part') selected = selected.parent; $('hide').disabled = !selected; $('selection').textContent = selected ? `선택: ${selected.userData.fileName || selected.name || '부품'}` : '부품을 클릭하면 선택됩니다.'; });
new ResizeObserver(() => { const w = $('viewport').clientWidth, h = $('viewport').clientHeight; renderer.setSize(w, h); camera.aspect = w / h; camera.updateProjectionMatrix(); }).observe($('viewport'));
renderer.setAnimationLoop(() => { controls.update(); renderer.render(scene, camera); });
fetch('./models/index.json').then(r => { if (!r.ok) throw new Error(); return r.json(); }).then(data => { entries = data; entries.forEach((entry, index) => { const option = document.createElement('option'); option.value = String(index); option.textContent = entry.name; $('models').append(option); }); if (entries.length) status('공개 모델을 선택하거나 내 기기의 파일을 여세요.'); }).catch(() => status('공개 모델 목록을 가져오지 못했습니다. 내 기기 파일은 열 수 있습니다.'));
