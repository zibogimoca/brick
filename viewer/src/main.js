import './style.css';
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { LDrawLoader } from 'three/addons/loaders/LDrawLoader.js';
import { LDrawConditionalLineMaterial } from 'three/addons/materials/LDrawConditionalLineMaterial.js';

const $ = id => document.getElementById(id);
const scene = new THREE.Scene(); scene.background = new THREE.Color('#14191f');
const camera = new THREE.PerspectiveCamera(40, 1, .01, 1000000);
const renderer = new THREE.WebGLRenderer({ antialias: true }); renderer.setPixelRatio(Math.min(devicePixelRatio, 2)); $('viewport').append(renderer.domElement);
const controls = new OrbitControls(camera, renderer.domElement); controls.enableDamping = true;
scene.add(new THREE.HemisphereLight(0xffffff, 0x657080, 3));
const light = new THREE.DirectionalLight(0xffffff, 3); light.position.set(200, 400, 300); scene.add(light);
let model, selected, generation = 0;
let latestEntryRequest = 0;
let poseJoints = [], poseGroups = new Map();
let instanceBatches = [];
const hidden = [];
let viewDirection = new THREE.Vector3(-.35, .25, 1);
function status(text) { $('status').textContent = text; }
function fit() {
  if (!model) return;
  model.updateMatrixWorld(true);
  const box = new THREE.Box3();
  model.traverseVisible(object => {
    if (!object.isMesh || object.isInstancedMesh) return;
    object.geometry.computeBoundingBox();
    box.union(object.geometry.boundingBox.clone().applyMatrix4(object.matrixWorld));
  });
  if (box.isEmpty()) return;
  const size = box.getSize(new THREE.Vector3()); const center = box.getCenter(new THREE.Vector3());
  const radius = Math.max(size.x, size.y, size.z, 1) * .6;
  const direction = viewDirection.clone().normalize();
  const right = new THREE.Vector3().crossVectors(camera.up, direction).normalize();
  const up = new THREE.Vector3().crossVectors(direction, right).normalize();
  const tanV = Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)), tanH = tanV * camera.aspect;
  let distance = 1;
  for (const x of [box.min.x, box.max.x]) for (const y of [box.min.y, box.max.y]) for (const z of [box.min.z, box.max.z]) {
    const delta = new THREE.Vector3(x, y, z).sub(center);
    distance = Math.max(distance, delta.dot(direction) + Math.abs(delta.dot(up)) / (tanV * .86), delta.dot(direction) + Math.abs(delta.dot(right)) / (tanH * .86));
  }
  camera.position.copy(center).addScaledVector(direction, distance);
  camera.near = Math.max(radius / 100, .1); camera.far = (distance + radius) * 10; camera.updateProjectionMatrix();
  controls.target.copy(center); controls.update();
}
function dispose(object) {
  const geometries = new Set(), materials = new Set(), textures = new Set();
  object.traverse(o => {
    if (o.geometry) geometries.add(o.geometry);
    // LDraw material arrays can be sparse. Instanced batches also share their
    // original meshes' geometry and materials; dispose each resource once.
    for (const material of [].concat(o.material || [])) if (material?.isMaterial) materials.add(material);
  });
  for (const geometry of geometries) geometry.dispose();
  for (const material of materials) {
    for (const value of Object.values(material)) if (value?.isTexture) textures.add(value);
    material.dispose();
  }
  for (const texture of textures) texture.dispose();
}
async function open(buffer, name, revision) {
  const current = ++generation; let failed = false; status('모델을 읽는 중…'); $('models').disabled = true;
  const manager = new THREE.LoadingManager(); manager.onError = () => { failed = true; };
  let next, metadata;
  try {
    if (/\.(mpd|ldr)$/i.test(name)) {
      const loader = new LDrawLoader(manager); loader.smoothNormals = true;
      loader.setConditionalLineMaterial(LDrawConditionalLineMaterial);
      {
        loader.setPartsLibraryPath(new URL('./parts-library/', location.href).href);
        const manifestResponse = await fetch('./parts-library/policy.md?v=' + encodeURIComponent(revision), { cache: 'no-store' });
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
          const resolved = new URL(manifest.files[relative] ? loader.partsLibraryPath + relative : url);
          resolved.searchParams.set('v', manifest.files[relative]?.sha256 || revision); return resolved.href;
        });
      }
      await loader.preloadMaterials(loader.partsLibraryPath + 'LDConfig.ldr');
      const text = new TextDecoder().decode(buffer);
      const record = text.split('\n').find(line => line.startsWith('0 !BRICK_STATE '));
      if (record) { try { metadata = JSON.parse(record.slice(15)); } catch { /* optional model metadata */ } }
      next = await new Promise((resolve, reject) => loader.parse(text, resolve, reject));
      next.rotation.x = Math.PI;
    } else throw new Error();
    if (current !== generation) { dispose(next); return; }
    if (failed || new THREE.Box3().setFromObject(next).isEmpty()) { dispose(next); throw new Error(); }
    if (model) { scene.remove(model); dispose(model); }
    model = next; scene.add(model); buildInstanceBatches(); configurePose(metadata); selected = null; hidden.length = 0; $('hide').disabled = true; $('reset').disabled = false; $('selection').textContent = '부품을 클릭하면 선택됩니다.';
    $('side-view').disabled = false; $('front-view').disabled = false;
    $('empty').hidden = true; $('fit').disabled = false; fit();
    renderer.domElement.dataset.modelLoaded = 'true';
    $('summary').textContent = metadata?.piece_count ? `${metadata.piece_count}개 부품 · 공개 판매가 기준 ${metadata.listed_retail_parts_cost_cny || '미확인'} CNY` : '';
    if (metadata?.status === 'instruction_reconstruction_in_progress') $('summary').textContent = [`${metadata.piece_count}개 배치`, metadata.body_draft_piece_count != null ? `본체 초안 ${metadata.body_draft_piece_count}개` : null, metadata.layout_note, typeof metadata.unresolved === 'string' ? metadata.unresolved : null, metadata.support_note, '설명서 재구성 중 · 잠정 배치 포함'].filter(Boolean).join(' · ');
    if (metadata?.status === 'cad_import') $('summary').textContent = [`${metadata.piece_count}개 부품`, '버전 0 · CAD 모델', metadata.layout_note].filter(Boolean).join(' · ');
    if (metadata?.status === 'reference_visual_approximation') $('summary').textContent = `${metadata.piece_count}개 부품 · 재구성 전 초안. 내부 구조와 부품 구성은 미확인.`;
    if (metadata?.parts_system === 'LEGO' && metadata?.status === 'original_lego_design_in_progress') $('summary').textContent = [`${metadata.piece_count}개 부품`, metadata.layout_note, 'LEGO 창작 설계 중'].filter(Boolean).join(' · ');
    if (metadata?.reference_geometry_bounds_cm) { const d = metadata.reference_geometry_bounds_cm; $('summary').textContent += ` · 약 ${d.length} × ${d.width} × ${d.height}cm`; }
    $('version').textContent = `${metadata?.version_label ? metadata.version_label + ' · ' : ''}${name} · ${revision}`; status(metadata?.status === 'cad_import' ? '버전 0 · CAD 모델. 실제 조립성은 미검증입니다.' : metadata?.status === 'instruction_reconstruction_in_progress' ? (metadata.layout === 'integrated_instruction_model' ? (metadata.stand_draft_piece_count ? '버전 0 · 받침대 포함 검토본. 미완성입니다.' : '버전 0 · 본체 연결본. 자세·결합 검증 중입니다.') : '버전 0 · 작업 중. 펼침 배치이며 조립 완료 상태가 아닙니다.') : metadata?.status === 'reference_visual_approximation' ? '버전 0 · 재구성 진행 전 초안. 조립 미검증.' : ['articulated_geometry_prototype', 'gobricks_only_redesign_in_progress'].includes(metadata?.status) ? '모델을 불러왔습니다 · 검토안. 연결·강도 미검증.' : '모델을 불러왔습니다. 조립 가능 여부를 검증한 결과는 아닙니다.');
    configureStudyViews(metadata);
  } catch (error) { console.error('Model loading failed', error); if (current === generation) status('모델을 완전히 불러오지 못했습니다. 이전 모델이 있다면 그대로 표시됩니다.'); }
  finally { if (current === generation) $('models').disabled = false; }
}
let entries = [];
async function fetchCatalog() {
  const response = await fetch('./models/index.json?t=' + Date.now(), { cache: 'no-store' });
  if (!response.ok) throw new Error('Model index unavailable');
  const data = await response.json();
  return data.map(entry => {
    const file = entry.url?.split('/').pop()?.replace(/\.mpd$/i, '') || entry.name;
    const match = file.match(/^(.*)-v(\d+)$/);
    return { ...entry, modelId: entry.modelId || (match ? match[1] : entry.name), modelName: entry.modelName || (match ? entry.name.replace(/\s*·\s*버전\s*\d+$/, '') : entry.name), versionLabel: entry.versionLabel || (match ? `버전 ${match[2]}` : '기본') };
  });
}
async function loadEntry(selectedEntry) {
  if (!selectedEntry) return;
  const request = ++latestEntryRequest;
  try {
    const latest = await fetchCatalog();
    const entry = latest.find(item => item.url === selectedEntry.url); if (!entry) throw new Error('Model removed');
    const url = new URL(entry.url, location.href); url.searchParams.set('v', entry.version || String(Date.now()));
    const response = await fetch(url.href, { cache: 'no-store' }); if (!response.ok) throw new Error('Model unavailable');
    const data = await response.arrayBuffer();
    const digest = await crypto.subtle.digest('SHA-256', data);
    const revision = [...new Uint8Array(digest)].map(x => x.toString(16).padStart(2, '0')).join('').slice(0, 12);
    if (entry.version && entry.version !== revision) throw new Error('Model index and contents disagree');
    if (request !== latestEntryRequest) return;
    await open(data, entry.url, revision);
  } catch { if (request === latestEntryRequest) status('최신 모델 파일을 가져오지 못했습니다. 잠시 후 다시 선택하세요.'); }
}
$('models').onchange = () => {
  const modelId = $('models').value; const versions = $('versions');
  versions.replaceChildren(new Option('버전 선택', ''));
  const matches = entries.map((entry, index) => ({ entry, index })).filter(x => x.entry.modelId === modelId)
    .sort((a, b) => (b.entry.designVersion ?? -1) - (a.entry.designVersion ?? -1));
  versions.disabled = !matches.length;
  for (const { entry, index } of matches) versions.add(new Option(entry.versionLabel, String(index)));
  if (matches.length) { versions.value = String(matches[0].index); loadEntry(matches[0].entry); }
  else status('모델을 선택하세요.');
};
$('versions').onchange = () => { if ($('versions').value !== '') loadEntry(entries[Number($('versions').value)]); };
$('fit').onclick = fit;
$('hide').onclick = () => { if (!selected) return; selected.visible = false; hidden.push(selected); selected = null; $('hide').disabled = true; $('selection').textContent = '선택한 부품을 숨겼습니다.'; refreshInstanceBatches(); };
$('reset').onclick = () => { for (const item of hidden) item.visible = true; hidden.length = 0; refreshInstanceBatches(); fit(); };
const raycaster = new THREE.Raycaster(); let down;
renderer.domElement.addEventListener('pointerdown', e => { down = [e.clientX, e.clientY]; });
renderer.domElement.addEventListener('pointerup', e => { if (!model || !down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 5) return; const rect = renderer.domElement.getBoundingClientRect(); raycaster.setFromCamera(new THREE.Vector2((e.clientX - rect.left) / rect.width * 2 - 1, -(e.clientY - rect.top) / rect.height * 2 + 1), camera); const hits = raycaster.intersectObject(model, true).filter(h => { for (let p = h.object; p; p = p.parent) if (!p.visible) return false; return h.object.isMesh; }); selected = hits[0]?.object?.isInstancedMesh ? hits[0].object.userData.sourceMeshes[hits[0].instanceId] : hits[0]?.object || null; while (selected?.parent && selected.parent !== model && selected.userData.type !== 'Part') selected = selected.parent; $('hide').disabled = !selected; $('selection').textContent = selected ? `선택: ${selected.userData.fileName || selected.name || '부품'}` : '부품을 클릭하면 선택됩니다.'; });
new ResizeObserver(() => { const w = $('viewport').clientWidth, h = $('viewport').clientHeight; renderer.setSize(w, h); camera.aspect = w / h; camera.updateProjectionMatrix(); }).observe($('viewport'));
renderer.setAnimationLoop(() => { controls.update(); renderer.render(scene, camera); });
fetchCatalog().then(data => {
  entries = data;
  const models = [...new Map(entries.map(entry => [entry.modelId, entry.modelName])).entries()];
  for (const [id, name] of models) $('models').add(new Option(name, id));
  if (entries.length) status('모델을 선택하세요.');
}).catch(() => status('모델 목록을 가져오지 못했습니다. 페이지를 다시 열어주세요.'));

function configurePose(metadata) {
  poseJoints = metadata?.joints || []; poseGroups = new Map();
  model.traverse(object => {
    if (object.userData.fileName?.endsWith('.ldr')) {
      poseGroups.set(object.userData.fileName, object);
      object.userData.baseQuaternion = object.quaternion.clone();
      object.userData.basePosition = object.position.clone();
      object.userData.poseAngles = { x: 0, y: 0, z: 0 };
    }
  });
  $('pose-panel').hidden = !poseJoints.length; $('joint').replaceChildren();
  for (const j of poseJoints) { const o = document.createElement('option'); o.value = j.id; o.textContent = j.label; $('joint').append(o); }
  $('joint').onchange = showJoint;
  $('pose-reset').onclick = () => { for (const o of poseGroups.values()) { o.quaternion.copy(o.userData.baseQuaternion); o.position.copy(o.userData.basePosition); o.userData.poseAngles = { x: 0, y: 0, z: 0 }; } showJoint(); refreshInstanceBatches(); fit(); };
  $('support-toggle').textContent = '지지대 숨기기';
  $('support-toggle').hidden = !poseGroups.has('support.ldr');
  $('support-toggle').parentElement.classList.toggle('two', poseGroups.has('support.ldr'));
  $('support-toggle').onclick = () => { const o = poseGroups.get('support.ldr'); if (o) { o.visible = !o.visible; $('support-toggle').textContent = o.visible ? '지지대 숨기기' : '지지대 보기'; refreshInstanceBatches(); } };
  showJoint();
}
function showJoint() {
  $('joint-axes').replaceChildren(); const j = poseJoints.find(j => j.id === $('joint').value); if (!j) return;
  const o = poseGroups.get(j.submodel); if (!o) return;
  $('pose-hint').textContent = j.note || '화면상 가동 검토 · 실물 범위 미검증';
  for (const [axis, limits] of Object.entries(j.axes)) {
    const label = document.createElement('label'), text = document.createElement('span'), input = document.createElement('input');
    const names = { x: '좌우 기울임', y: '좌우 회전', z: '상하 회전' };
    input.type = 'range'; input.min = limits[0]; input.max = limits[1]; input.step = 1; input.value = o.userData.poseAngles[axis]; input.dataset.axis = axis;
    const update = () => {
      text.textContent = `${j.axis_labels?.[axis] || names[axis]} ${input.value}${j.motion === 'linear' ? (j.unit || '%') : '°'}`;
      o.userData.poseAngles[axis] = Number(input.value);
      const a = o.userData.poseAngles, value = k => a[k] * (j.axis_scale?.[k] ?? 1);
      if (j.motion === 'linear') o.position.copy(o.userData.basePosition).add(new THREE.Vector3(...['x','y','z'].map(value)));
      else o.quaternion.copy(o.userData.baseQuaternion).multiply(new THREE.Quaternion().setFromEuler(new THREE.Euler(...['x','y','z'].map(k => THREE.MathUtils.degToRad(value(k))))));
      refreshInstanceBatches();
    };
    input.oninput = update; update(); label.append(text, input); $('joint-axes').append(label);
  }
}
$('side-view').onclick = () => { viewDirection.set(0, .04, 1); fit(); };
$('front-view').onclick = () => { viewDirection.set(-1, .08, 0); fit(); };

// Reuse identical physical part meshes while keeping original groups for posing.
function buildInstanceBatches() {
  instanceBatches = []; const buckets = new Map();
  model.updateMatrixWorld(true);
  const inverse = model.matrixWorld.clone().invert(), relative = new THREE.Matrix4();
  model.traverse(object => {
    if (object.isLineSegments) { object.visible = false; return; }
    if (!object.isMesh) return;
    // InstancedMesh does not support negative scales. Keep mirrored LDraw
    // parts as ordinary meshes so their face winding renders correctly.
    if (relative.multiplyMatrices(inverse, object.matrixWorld).determinant() < 0) return;
    const materials = Array.isArray(object.material) ? object.material : [object.material];
    const key = object.geometry.uuid + ':' + materials.map(m => m.uuid).join(',');
    if (!buckets.has(key)) buckets.set(key, []);
    buckets.get(key).push(object); object.layers.set(1);
  });
  for (const meshes of buckets.values()) {
    const batch = new THREE.InstancedMesh(meshes[0].geometry, meshes[0].material, meshes.length);
    batch.userData.sourceMeshes = meshes; batch.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
    batch.frustumCulled = false; model.add(batch); instanceBatches.push(batch);
  }
  refreshInstanceBatches();
}
function refreshInstanceBatches() {
  if (!model) return;
  model.updateMatrixWorld(true);
  const inverse = model.matrixWorld.clone().invert(), matrix = new THREE.Matrix4(), zero = new THREE.Matrix4().makeScale(0, 0, 0);
  for (const batch of instanceBatches) {
    batch.userData.sourceMeshes.forEach((mesh, i) => {
      let visible = true; for (let p = mesh; p && p !== model; p = p.parent) if (!p.visible) { visible = false; break; }
      batch.setMatrixAt(i, visible ? matrix.multiplyMatrices(inverse, mesh.matrixWorld) : zero);
    });
    batch.instanceMatrix.needsUpdate = true;
    batch.computeBoundingBox(); batch.computeBoundingSphere();
  }
}

// Study roots remain independent of part hiding and pose controls.
function configureStudyViews(metadata) {
  $('component-visibility').hidden = true;
  $('component-options').replaceChildren();
  $('components-all').onclick = null;
  $('study-hint').textContent = '부위별 설계 표본 · 전체 성당 조립 전';
  if (metadata?.component_views?.length) { configureComponentViews(metadata); return; }
  const views = metadata?.study_views || [];
  const select = $('study-view');
  select.replaceChildren();
  $('study-panel').hidden = !views.length;
  select.onchange = null;
  if (!views.length) return;
  const roots = new Map();
  // A root group has no .ldr ancestor inside the loaded MPD.
  model.traverse(object => {
    if (!object.userData.fileName?.endsWith('.ldr')) return;
    for (let p = object.parent; p && p !== model; p = p.parent) {
      if (p.userData.fileName?.endsWith('.ldr')) return;
    }
    roots.set(object.userData.fileName, object);
  });
  const available = views.filter(view => view.files?.length && view.files.every(file => roots.has(file)));
  if (!available.length) { $('study-panel').hidden = true; return; }
  select.add(new Option('전체 표본', 'all'));
  for (const view of available) select.add(new Option(view.label, view.id));
  const apply = () => {
    const view = available.find(view => view.id === select.value);
    for (const [file, object] of roots) object.visible = !view || view.files.includes(file);
    selected = null; $('hide').disabled = true;
    $('selection').textContent = '부품을 클릭하면 선택됩니다.';
    refreshInstanceBatches(); fit();
    $('summary').textContent = view ? `${view.label} 설계 표본 · 전체 성당 아님 · 연결·외형 검토 중` : `${metadata.piece_count}개 부품 · 독립 설계 표본 모음 · 전체 성당 아님`;
    status('부위별 설계 표본입니다. 최종 비례·외피·구조를 검토 중입니다.');
  };
  select.onchange = apply;
  select.value = available.some(view => view.id === metadata.default_study_view) ? metadata.default_study_view : 'all';
  apply();
}

// Architectural sections can include nested assemblies (for example, the arena
// and sword courtyard under a shared container). Toggle only named sections,
// leaving their containers visible and individual part hiding independent.
function configureComponentViews(metadata) {
  const select = $('study-view'), groups = new Map();
  select.replaceChildren(); select.onchange = null;
  model.traverse(object => {
    const file = object.userData.fileName;
    if (!file?.endsWith('.ldr')) return;
    if (!groups.has(file)) groups.set(file, []);
    groups.get(file).push(object);
  });
  const available = metadata.component_views.filter(view => view.files?.length && view.files.every(file => groups.has(file)));
  $('study-panel').hidden = !available.length;
  if (!available.length) return;
  $('component-visibility').hidden = false;
  $('study-hint').textContent = '한 구역만 보거나 체크박스로 여러 구역을 함께 표시하세요.';
  select.add(new Option('전체 모델', 'all'));
  const boxes = new Map();
  for (const view of available) {
    select.add(new Option(view.label, view.id));
    const label = document.createElement('label'), input = document.createElement('input');
    input.type = 'checkbox'; input.checked = true; input.value = view.id;
    label.append(input, document.createTextNode(view.label));
    $('component-options').append(label); boxes.set(view.id, input);
  }
  const custom = new Option('직접 선택', 'custom'); custom.disabled = true;
  select.add(custom);
  const baseSummary = $('summary').textContent;
  const apply = () => {
    const enabled = available.filter(view => boxes.get(view.id).checked);
    for (const view of available) for (const file of view.files) {
      for (const group of groups.get(file)) group.visible = boxes.get(view.id).checked;
    }
    select.value = enabled.length === available.length ? 'all' : enabled.length === 1 ? enabled[0].id : 'custom';
    selected = null; $('hide').disabled = true;
    $('selection').textContent = '부품을 클릭하면 선택됩니다.';
    refreshInstanceBatches(); fit();
    $('summary').textContent = select.value === 'all' ? baseSummary : `${enabled.length === 1 ? enabled[0].label : `${enabled.length}개 구역 선택`} · ${baseSummary}`;
    status(enabled.length ? `${enabled.length}/${available.length}개 구역 표시 · LEGO 창작 설계 중` : '모든 구역이 숨겨져 있습니다. 체크박스나 전체 모델 복원으로 다시 표시하세요.');
  };
  for (const input of boxes.values()) input.onchange = apply;
  select.onchange = () => {
    if (select.value === 'custom') return;
    for (const [id, input] of boxes) input.checked = select.value === 'all' || select.value === id;
    apply();
  };
  $('components-all').onclick = () => {
    for (const item of hidden) item.visible = true;
    hidden.length = 0;
    for (const input of boxes.values()) input.checked = true;
    apply();
  };
  apply();
}
