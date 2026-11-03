import { cp, mkdir, readdir, readFile, writeFile, rm } from 'node:fs/promises';
import { createHash } from 'node:crypto';
const root = new URL('../../', import.meta.url);
const publicRoot = new URL('../public/', import.meta.url);
await rm(new URL('parts-library/', publicRoot), { recursive: true, force: true });
await cp(new URL('assets/', root), new URL('parts-library/', publicRoot), { recursive: true });
await rm(new URL('models/', publicRoot), { recursive: true, force: true });
await mkdir(new URL('models/', publicRoot), { recursive: true });
const entries = [];
for (const name of (await readdir(new URL('models/', root))).filter(name => name.endsWith('.mpd')).sort((a, b) => a.localeCompare(b, 'en', { numeric: true }))) {
  const data = await readFile(new URL('models/' + name, root));
  await writeFile(new URL('models/' + name, publicRoot), data);
  const stem = name.replace(/\.mpd$/i, '');
  const match = stem.match(/^(.*)-v(\d+)$/);
  const modelName = match ? match[1] : stem;
  const title = ({ tyrannosaurus: '티라노사우루스', triceratops: '트리케라톱스' })[modelName] || modelName.replaceAll('-', ' ');
  entries.push({ name: title + (match ? ' · v' + match[2] : ''), designVersion: match ? Number(match[2]) : null, url: './models/' + name, version: createHash('sha256').update(data).digest('hex').slice(0, 12) });
}
await writeFile(new URL('models/index.json', publicRoot), JSON.stringify(entries, null, 2) + '\n');
