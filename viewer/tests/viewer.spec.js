import { test, expect } from '@playwright/test';
test.setTimeout(300000);
async function load(page) {
  await page.goto('/');
  await expect.poll(() => page.locator('#models option').count()).toBeGreaterThan(1);
  await page.selectOption('#models', { label: '티라노사우루스' });
  await expect(page.locator('#models')).toBeEnabled({ timeout: 180000 });
  await page.selectOption('#versions', { label: '버전 1' });
  await expect(page.locator('#version')).toContainText('tyrannosaurus-v1.mpd', { timeout: 180000 });
  await expect(page.locator('#models')).toBeEnabled({ timeout: 180000 });
  await expect(page.locator('#versions')).toBeEnabled();
  await expect(page.locator('#status')).toContainText('모델을 불러왔습니다', { timeout: 180000 });
}
test('renders the actual model and switches camera views', async ({ page }) => {
  const errors = []; page.on('pageerror', error => errors.push(error.message));
  await load(page);
  await expect(page.locator('#empty')).toBeHidden();
  await expect(page.locator('#version')).toContainText('tyrannosaurus');
  await page.click('#side-view'); await page.click('#front-view'); await page.click('#fit');
  const box = await page.locator('canvas').boundingBox();
  for (let y = .35; y <= .65; y += .1) {
    for (let x = .25; x <= .75; x += .05) {
      await page.mouse.click(box.x + box.width * x, box.y + box.height * y);
      if (await page.locator('#hide').isEnabled()) break;
    }
    if (await page.locator('#hide').isEnabled()) break;
  }
  await expect(page.locator('#hide')).toBeEnabled();
  await page.click('#hide');
  await expect(page.locator('#selection')).toContainText('숨겼습니다');
  await page.click('#reset');
  expect(errors).toEqual([]);
});
test('model and version selectors stay separate and filter available versions', async ({ page }) => {
  await page.goto('/');
  await expect.poll(() => page.locator('#models option').count()).toBeGreaterThan(1);
  await page.selectOption('#models', { label: '트리케라톱스' });
  await expect(page.locator('#versions option')).toHaveText(['버전 선택', '버전 0']);
  await expect(page.locator('#status')).toContainText('버전 0 · 작업 중. 펼침 배치', { timeout: 180000 });
  await expect(page.locator('#version')).toContainText('triceratops-v0.mpd');
  await page.selectOption('#models', { label: '티라노사우루스' });
  await expect(page.locator('#versions option')).toHaveText(['버전 선택', '버전 2', '버전 1', '버전 0']);
  await expect(page.locator('#versions')).toHaveValue(/\d+/);
  await page.selectOption('#versions', { label: '버전 0' });
  await expect(page.locator('#status')).toContainText('버전 0 · 받침대 포함 검토본. 미완성입니다.', { timeout: 180000 });
  await page.selectOption('#models', { label: '노트르담 대성당' });
  await expect(page.locator('#versions option')).toHaveText(['버전 선택', '버전 0']);
  await expect(page.locator('#version')).toContainText('notre-dame-v0.mpd', { timeout: 180000 });
});
test('rejects a broken catalog model while preserving the previous model', async ({ page }) => {
  const { createHash } = await import('node:crypto');
  const { readFile } = await import('node:fs/promises');
  await load(page); const revision = await page.locator('#version').textContent();
  const broken = '0 FILE missing.ldr\n1 16 0 0 0 1 0 0 0 1 0 0 0 1 no-such-part.dat\n0 NOFILE\n';
  const hash = createHash('sha256').update(broken).digest('hex').slice(0, 12);
  const entries = JSON.parse(await readFile('dist/models/index.json', 'utf8'));
  await page.route('**/models/index.json?*', route => route.fulfill({ json: entries.map(entry => ({ ...entry, version: hash })) }));
  await page.route('**/models/*.mpd?*', route => route.fulfill({ body: broken, contentType: 'text/plain' }));
  await page.selectOption('#models', '');
  await page.selectOption('#models', { label: '티라노사우루스' });
  await expect(page.locator('#status')).toContainText('완전히 불러오지 못했습니다', { timeout: 180000 });
  await expect(page.locator('#version')).toHaveText(revision);
});
test('keeps controls compact in the left sidebar and renders at mobile size', async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 720 });
  await load(page);
  await expect(page.locator('header, #file, #library, #load')).toHaveCount(0);
  expect(await page.locator('aside').evaluate(el => el.scrollHeight <= el.clientHeight + 1)).toBe(true);
  const canvas = await page.locator('canvas').boundingBox(); expect(canvas.y).toBe(0); expect(canvas.height).toBe(720);
  await page.setViewportSize({ width: 390, height: 844 });
  await expect(page.locator('canvas')).toBeVisible();
  expect(await page.locator('#viewport').evaluate(el => el.getBoundingClientRect().left)).toBe(168);
});

test('pose controls transform the model canvas and reset; support is independently visible', async ({ page }) => {
  await load(page);
  await expect(page.locator('#pose-panel')).toBeVisible();
  await expect(page.locator('#joint option')).toHaveCount(18);
  await page.selectOption('#joint', 'jaw');
  const canvas = page.locator('canvas');
  await page.waitForTimeout(500);
  const before = await canvas.screenshot();
  await page.locator('#joint-axes input').evaluate(input => { input.value = '12'; input.dispatchEvent(new Event('input', { bubbles: true })); });
  await page.waitForTimeout(250);
  const after = await canvas.screenshot();
  expect(Buffer.compare(before, after)).not.toBe(0);
  await page.click('#pose-reset');
  await expect(page.locator('#joint-axes input')).toHaveValue('0');
  await page.click('#support-toggle');
  await expect(page.locator('#support-toggle')).toHaveText('지지대 보기');
  await page.click('#support-toggle');
  await expect(page.locator('#support-toggle')).toHaveText('지지대 숨기기');
  await page.click('#side-view'); await page.click('#front-view');
  await expect(page.locator('#status')).toContainText('모델을 불러왔습니다');
});


test('refreshes an old catalog before requesting a versioned model', async ({ page }) => {
  const { readFile } = await import('node:fs/promises');
  const current = JSON.parse(await readFile('dist/models/index.json', 'utf8'));
  let catalogRequests = 0; const modelRequests = [];
  await page.route('**/models/index.json?*', async route => {
    catalogRequests++;
    const data = current.map(entry => ({ ...entry, version: catalogRequests === 1 ? 'old-version' : entry.version }));
    await route.fulfill({ json: data });
  });
  page.on('request', request => { if (request.url().includes('tyrannosaurus-v1.mpd')) modelRequests.push(request.url()); });
  await load(page);
  expect(catalogRequests).toBeGreaterThanOrEqual(2);
  expect(modelRequests.length).toBeGreaterThanOrEqual(1);
  expect(new URL(modelRequests[0]).searchParams.get('v')).toBe(current.find(e => e.designVersion === 1).version);
  await expect(page.locator('#version')).toContainText(current.find(e => e.designVersion === 1).version);
  await expect(page.locator('#models option:checked')).toHaveText('티라노사우루스');
  await expect(page.locator('#versions option:checked')).toHaveText('버전 1');
  expect(current.some(e => e.designVersion === 0)).toBe(true);
});

test('loads integrated v0 with no invented articulation and can return to v1', async ({ page }) => {
  test.setTimeout(600000);
  await load(page);
  await page.selectOption('#versions', { label: '버전 0' });
  await expect(page.locator('#status')).toContainText('버전 0 · 받침대 포함 검토본. 미완성입니다.', { timeout: 180000 });
  await expect(page.locator('#version')).toContainText('tyrannosaurus-v0.mpd');
  await expect(page.locator('#summary')).toContainText('본체·받침대 검토본');
  await expect(page.locator('#summary')).toContainText('본체 초안 2496개');
  await expect(page.locator('#summary')).toContainText('왼쪽 284개 물리 금형 대응 미러');
  await expect(page.locator('#pose-panel')).toBeHidden();
  await page.selectOption('#versions', { label: '버전 1' });
  await expect(page.locator('#status')).toContainText('모델을 불러왔습니다', { timeout: 180000 });
  await expect(page.locator('#joint option')).toHaveCount(18);
});

test('mirrored LDraw meshes retain the same exterior as a symmetric ordinary mesh', async ({ page }, testInfo) => {
  const { createHash } = await import('node:crypto');
  const cube = [
    '0 FILE cube.dat', '0 !LDRAW_ORG Part', '0 BFC CERTIFY CCW',
    '4 16 -20 -20 20 20 -20 20 20 20 20 -20 20 20',
    '4 16 20 -20 -20 -20 -20 -20 -20 20 -20 20 20 -20',
    '4 16 20 -20 20 20 -20 -20 20 20 -20 20 20 20',
    '4 16 -20 -20 -20 -20 -20 20 -20 20 20 -20 20 -20',
    '4 16 -20 20 20 20 20 20 20 20 -20 -20 20 -20',
    '4 16 -20 -20 -20 20 -20 -20 20 -20 20 -20 -20 20',
    '0 NOFILE'
  ].join('\n');
  let body, revision;
  await page.route('**/models/index.json?*', route => route.fulfill({ json: [{ name: 'Mirror check', url: './models/mirror-check.mpd', version: revision }] }));
  await page.route('**/models/mirror-check.mpd?*', route => route.fulfill({ body }));
  const render = async scale => {
    body = `0 FILE mirror-check.ldr\n1 19 0 0 0 ${scale} 0 0 0 1 0 0 0 1 cube.dat\n0 NOFILE\n${cube}`;
    revision = createHash('sha256').update(body).digest('hex').slice(0, 12);
    await page.goto('/');
    await page.selectOption('#models', { label: 'Mirror check' });
    await expect(page.locator('canvas')).toHaveAttribute('data-model-loaded', 'true');
    await page.click('#side-view');
    await page.waitForTimeout(300);
    return page.locator('canvas').screenshot();
  };
  const normal = await render(1), mirrored = await render(-1);
  const { writeFile } = await import('node:fs/promises');
  await writeFile(testInfo.outputPath('normal.png'), normal);
  await writeFile(testInfo.outputPath('mirrored.png'), mirrored);
  await testInfo.attach('normal', { body: normal, contentType: 'image/png' });
  await testInfo.attach('mirrored', { body: mirrored, contentType: 'image/png' });
  const changedFraction = await page.evaluate(async encoded => {
    const pixels = await Promise.all(encoded.map(async value => {
      const image = new Image(); image.src = `data:image/png;base64,${value}`; await image.decode();
      const canvas = document.createElement('canvas'); canvas.width = image.width; canvas.height = image.height;
      const context = canvas.getContext('2d'); context.drawImage(image, 0, 0);
      return context.getImageData(0, 0, canvas.width, canvas.height).data;
    }));
    let changed = 0;
    for (let i = 0; i < pixels[0].length; i += 4) {
      if ([0, 1, 2].some(c => Math.abs(pixels[0][i + c] - pixels[1][i + c]) > 3)) changed++;
    }
    return changed / (pixels[0].length / 4);
  }, [normal.toString('base64'), mirrored.toString('base64')]);
  // Ignore subpixel rasterization differences, but reject missing/reversed faces.
  expect(changedFraction).toBeLessThan(.001);
});


test('loads all integrated review models without missing geometry', async ({ page }, testInfo) => {
  test.setTimeout(600000);
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('/');
  for (const [model, version, file] of [
    ['티라노사우루스', '버전 2', 'tyrannosaurus-v2.mpd'],
    ['티라노사우루스', '버전 0', 'tyrannosaurus-v0.mpd'],
    ['트리케라톱스', '버전 0', 'triceratops-v0.mpd'],
    ['노트르담 대성당', '버전 0', 'notre-dame-v0.mpd'],
    ['호그와트성', '버전 0', 'hogwarts-castle-v0.mpd'],
  ]) {
    await page.selectOption('#models', { label: model });
    await expect(page.locator('#models')).toBeEnabled({ timeout: 180000 });
    await page.selectOption('#versions', { label: version });
    await expect(page.locator('#version')).toContainText(file, { timeout: 180000 });
    console.log('Loaded review model:', file);
    await expect(page.locator('#status')).not.toContainText('완전히 불러오지 못했습니다');
    await expect(page.locator('#summary')).not.toContainText('undefined');
    await expect(page.locator('canvas')).toHaveAttribute('data-model-loaded', 'true');
    await page.screenshot({ path: testInfo.outputPath(file + '.png') });
    if (file === 'tyrannosaurus-v0.mpd') {
      await page.click('#side-view');
      await page.screenshot({ path: testInfo.outputPath('tyrannosaurus-v0-side.png') });
      await page.click('#front-view');
      await page.screenshot({ path: testInfo.outputPath('tyrannosaurus-v0-front.png') });
    }
  }
  expect(errors).toEqual([]);
});


test('keeps the latest version when an earlier model download finishes late', async ({ page }) => {
  const { createHash } = await import('node:crypto');
  const body = color => `0 FILE race.ldr\n1 ${color} 0 0 0 1 0 0 0 1 0 0 0 1 cube.dat\n0 NOFILE\n0 FILE cube.dat\n0 BFC CERTIFY CCW\n3 16 0 0 0 20 0 0 0 20 0\n0 NOFILE\n`;
  const files = { 1: body(4), 2: body(14) };
  const entries = [1, 2].map(v => ({ modelId: 'tyrannosaurus', modelName: '티라노사우루스', name: '티라노사우루스', versionLabel: `버전 ${v}`, designVersion: v, url: `./models/tyrannosaurus-v${v}.mpd`, version: createHash('sha256').update(files[v]).digest('hex').slice(0, 12) }));
  let releaseOld, markRequested;
  const held = new Promise(resolve => { releaseOld = resolve; });
  const requested = new Promise(resolve => { markRequested = resolve; });
  await page.route('**/models/index.json?*', route => route.fulfill({ json: entries }));
  await page.route('**/models/tyrannosaurus-v1.mpd?*', route => route.fulfill({ body: files[1], contentType: 'text/plain' }));
  await page.route('**/models/tyrannosaurus-v2.mpd?*', async route => { markRequested(); await held; await route.fulfill({ body: files[2], contentType: 'text/plain' }); });
  await page.goto('/');
  await page.selectOption('#models', { label: '티라노사우루스' });
  await requested;
  await page.selectOption('#versions', { label: '버전 1' });
  await expect(page.locator('#version')).toContainText('tyrannosaurus-v1.mpd', { timeout: 30000 });
  const oldFinished = page.waitForEvent('requestfinished', request => request.url().includes('tyrannosaurus-v2.mpd'));
  releaseOld();
  await oldFinished;
  await page.waitForLoadState('networkidle');
  await expect(page.locator('#version')).toContainText('tyrannosaurus-v1.mpd');
  await expect(page.locator('#versions option:checked')).toHaveText('버전 1');
});

for (const [slug, title, pieces] of [
  ['hogwarts-clock-tower', '호그와트 시계탑 (75948)', 884],
  ['hogwarts-whomping-willow', '호그와트 커다란 버드나무 (75953)', 719],
  ['hogwarts-great-hall', '호그와트 대연회장 (75954)', 821],
  ['hogwarts-room-of-requirement', '호그와트 필요의 방 (75966)', 169],
  ['hogwarts-astronomy-tower', '호그와트 천문탑 (75969)', 925],
  ['louvre', '루브르 박물관 (21024)', 693],
  ['statue-of-liberty', '자유의 여신상 (21042)', 1683],
  ['big-ben', '빅벤 (10253)', 4166],
  ['dinosaur-7219', '소형 공룡 (7219)', 34],
]) {
  test(`imports CAD version 0: ${slug}`, async ({ page }, testInfo) => {
    test.setTimeout(600000);
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto('/');
    await expect.poll(() => page.locator('#models option').count()).toBeGreaterThan(9);
    await page.selectOption('#models', { label: title });
    await expect(page.locator('#models')).toBeEnabled({ timeout: 300000 });
    await expect(page.locator('#version')).toContainText(`${slug}-v0.mpd`, { timeout: 300000 });
    await expect(page.locator('#versions option')).toHaveText(['버전 선택', '버전 0']);
    await expect(page.locator('#summary')).toContainText(`${pieces}개 부품`);
    await expect(page.locator('#summary')).toContainText('CAD 모델');
    await expect(page.locator('canvas')).toHaveAttribute('data-model-loaded', 'true');
    await expect(page.locator('#pose-panel')).toBeHidden();
    await page.screenshot({ path: testInfo.outputPath(slug + '.png') });
    expect(errors).toEqual([]);
  });
}

test('architectural study selector focuses components and stays separate from part reset', async ({ page }) => {
  const errors = []; page.on('pageerror', error => errors.push(error.message));
  await page.goto('/');
  await expect.poll(() => page.locator('#models option').count()).toBeGreaterThan(9);
  await page.selectOption('#models', 'st-peters-basilica');
  await expect(page.locator('#models')).toBeEnabled({ timeout: 180000 });
  await expect(page.locator('#version')).toContainText('st-peters-basilica-v1.mpd', { timeout: 180000 });
  await expect(page.locator('#study-panel')).toBeVisible();
  await expect(page.locator('#study-view option')).toHaveText(['전체 표본', '돔·드럼', '정면 비교', '본당', '교차부·후진', '직선 회랑', '곡선 회랑']);
  await expect(page.locator('#study-view')).toHaveValue('dome');
  await expect(page.locator('#summary')).toContainText('돔·드럼 설계 표본');
  await expect(page.locator('#summary')).not.toContainText('CNY');
  await page.selectOption('#study-view', 'front');
  await page.click('#fit'); await page.click('#reset');
  await expect(page.locator('#study-view')).toHaveValue('front');
  await expect(page.locator('#summary')).toContainText('정면 비교');
  const box = await page.locator('canvas').boundingBox();
  for (let y = .3; y <= .7; y += .1) {
    for (let x = .2; x <= .8; x += .05) {
      await page.mouse.click(box.x + box.width*x, box.y + box.height*y);
      if (await page.locator('#hide').isEnabled()) break;
    }
    if (await page.locator('#hide').isEnabled()) break;
  }
  await expect(page.locator('#hide')).toBeEnabled();
  await page.click('#hide'); await page.click('#reset');
  await page.selectOption('#study-view', 'all');
  await expect(page.locator('#summary')).toContainText('독립 설계 표본 모음');
  await page.selectOption('#models', 'dinosaur-7219');
  await expect(page.locator('#version')).toContainText('dinosaur-7219-v0.mpd', { timeout: 180000 });
  await expect(page.locator('#study-panel')).toBeHidden();
  expect(errors).toEqual([]);
});
