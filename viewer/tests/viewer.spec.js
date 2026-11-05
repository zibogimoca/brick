import { test, expect } from '@playwright/test';
async function load(page) {
  await page.goto('/');
  await expect.poll(() => page.locator('#models option').count()).toBeGreaterThan(1);
  await page.selectOption('#models', { label: '티라노사우루스' });
  await expect(page.locator('#versions')).toBeEnabled();
  await expect(page.locator('#status')).toContainText('모델을 불러왔습니다', { timeout: 30000 });
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
  await expect(page.locator('#status')).toContainText('버전 0 · 작업 중. 펼침 배치', { timeout: 30000 });
  await expect(page.locator('#version')).toContainText('triceratops-v0.mpd');
  await page.selectOption('#models', { label: '티라노사우루스' });
  await expect(page.locator('#versions option')).toHaveText(['버전 선택', '버전 1', '버전 0']);
  await expect(page.locator('#versions')).toHaveValue(/\d+/);
  await page.selectOption('#versions', { label: '버전 0' });
  await expect(page.locator('#status')).toContainText('버전 0 · 받침대 포함 검토본. 미완성입니다.', { timeout: 30000 });
  await page.selectOption('#models', { label: '노트르담 대성당' });
  await expect(page.locator('#versions option')).toHaveText(['버전 선택', '버전 0']);
  await expect(page.locator('#version')).toContainText('notre-dame-v0.mpd');
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
  await expect(page.locator('#status')).toContainText('완전히 불러오지 못했습니다', { timeout: 30000 });
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
  expect(modelRequests).toHaveLength(1);
  expect(new URL(modelRequests[0]).searchParams.get('v')).toBe(current.find(e => e.designVersion === 1).version);
  await expect(page.locator('#version')).toContainText(current.find(e => e.designVersion === 1).version);
  await expect(page.locator('#models option:checked')).toHaveText('티라노사우루스');
  await expect(page.locator('#versions option:checked')).toHaveText('버전 1');
  expect(current.some(e => e.designVersion === 0)).toBe(true);
});

test('loads integrated v0 with no invented articulation and can return to v1', async ({ page }) => {
  test.setTimeout(60000);
  await load(page);
  await page.selectOption('#versions', { label: '버전 0' });
  await expect(page.locator('#status')).toContainText('버전 0 · 받침대 포함 검토본. 미완성입니다.', { timeout: 30000 });
  await expect(page.locator('#version')).toContainText('tyrannosaurus-v0.mpd');
  await expect(page.locator('#summary')).toContainText('본체·받침대 통합 검토본');
  await expect(page.locator('#summary')).toContainText('본체 초안 2488개');
  await expect(page.locator('#summary')).toContainText('두 번째 다리 비대칭 보행 후보');
  await expect(page.locator('#pose-panel')).toBeHidden();
  await page.selectOption('#versions', { label: '버전 1' });
  await expect(page.locator('#status')).toContainText('모델을 불러왔습니다', { timeout: 30000 });
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
