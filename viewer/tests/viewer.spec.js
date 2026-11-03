import { test, expect } from '@playwright/test';
async function load(page) {
  await page.goto('/');
  await expect(page.locator('#models option')).toHaveCount(2);
  await page.selectOption('#models', '0');
  await expect(page.locator('#status')).toContainText('모델을 불러왔습니다', { timeout: 30000 });
}
test('renders the actual full Tyrannosaurus MPD with local geometry and colors; selects and hides a part', async ({ page }) => {
  const errors = []; page.on('pageerror', error => errors.push(error.message));
  await load(page);
  await expect(page.locator('#empty')).toBeHidden();
  await expect(page.locator('#version')).toContainText('tyrannosaurus');
  const canvas = page.locator('canvas'); const box = await canvas.boundingBox();
  let selected = false;
  for (let y = .35; y <= .65 && !selected; y += .05) for (let x = .25; x <= .75 && !selected; x += .05) {
    await page.mouse.click(box.x + box.width * x, box.y + box.height * y);
    selected = await page.locator('#hide').isEnabled();
  }
  expect(selected).toBe(true); await page.click('#hide');
  await expect(page.locator('#selection')).toContainText('숨겼습니다');
  await page.click('#reset'); await page.click('#fit');
  expect(errors).toEqual([]);
});
test('rejects incomplete models while preserving the previously loaded model', async ({ page }) => {
  await load(page); const revision = await page.locator('#version').textContent();
  await page.locator('#file').setInputFiles({ name: 'missing.mpd', mimeType: 'text/plain', buffer: Buffer.from('0 FILE missing.ldr\n1 16 0 0 0 1 0 0 0 1 0 0 0 1 no-such-part.dat\n0 NOFILE\n') });
  await expect(page.locator('#status')).toContainText('완전히 불러오지 못했습니다', { timeout: 30000 });
  await expect(page.locator('#version')).toHaveText(revision);
});
test('opens local MPD without uploading and works at mobile size', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  const posts = []; page.on('request', request => { if (request.method() === 'POST') posts.push(request.url()); });
  await page.goto('/');
  await page.locator('#file').setInputFiles('../models/tyrannosaurus.mpd');
  await expect(page.locator('#status')).toContainText('모델을 불러왔습니다', { timeout: 30000 });
  expect(posts).toEqual([]); await expect(page.locator('canvas')).toBeVisible();
});
