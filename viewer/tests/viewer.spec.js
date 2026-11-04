import { test, expect } from '@playwright/test';
async function load(page) {
  await page.goto('/');
  await expect.poll(() => page.locator('#models option').count()).toBeGreaterThan(1);
  await page.selectOption('#models', { label: '티라노사우루스 · 버전 1' });
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
  await page.selectOption('#models', { label: '티라노사우루스 · 버전 1' });
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
  await expect(page.locator('#models option:checked')).toHaveText(current.find(e => e.designVersion === 1).name);
  expect(current.some(e => e.designVersion === 0)).toBe(true);
});

test('loads current v0 workbench with no invented articulation and can return to v1', async ({ page }) => {
  await load(page);
  await page.selectOption('#models', { label: '티라노사우루스 · 버전 0' });
  await expect(page.locator('#status')).toContainText('버전 0 · 작업 중', { timeout: 30000 });
  await expect(page.locator('#version')).toContainText('tyrannosaurus-v0.mpd');
  await expect(page.locator('#summary')).toContainText('원래 조립 위치 아님');
  await expect(page.locator('#summary')).toContainText('본체 초안 152개');
  await expect(page.locator('#pose-panel')).toBeHidden();
  await page.selectOption('#models', { label: '티라노사우루스 · 버전 1' });
  await expect(page.locator('#status')).toContainText('모델을 불러왔습니다', { timeout: 30000 });
  await expect(page.locator('#joint option')).toHaveCount(18);
});
