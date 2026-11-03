import { cp, mkdir, readdir, readFile, writeFile, rm } from 'node:fs/promises';
import { createHash } from 'node:crypto';
const root = new URL('../../', import.meta.url);
const publicRoot = new URL('../public/', import.meta.url);
await rm(new URL('parts-library/', publicRoot), { recursive: true, force: true });
await cp(new URL('assets/ldraw/', root), new URL('parts-library/', publicRoot), { recursive: true });
await rm(new URL('models/', publicRoot), { recursive: true, force: true });
await mkdir(new URL('models/', publicRoot), { recursive: true });
const entries = [];
for (const name of (await readdir(new URL('models/', root))).filter(name => name.endsWith('.mpd')).sort()) {
  const data = await readFile(new URL('models/' + name, root));
  await writeFile(new URL('models/' + name, publicRoot), data);
  entries.push({ name: name.replace('.mpd', '').replaceAll('-', ' '), url: './models/' + name, version: createHash('sha256').update(data).digest('hex').slice(0, 12) });
}
await writeFile(new URL('models/index.json', publicRoot), JSON.stringify(entries, null, 2) + '\n');
