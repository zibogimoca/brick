import { readFile, writeFile, readdir } from 'node:fs/promises';
const dist = new URL('../dist/', import.meta.url);
const entries = {};
async function walk(folder, prefix = '') {
  for (const entry of await readdir(folder, { withFileTypes: true })) {
    if (entry.name === 'assets' && !prefix) continue;
    const path = prefix + entry.name;
    if (entry.isDirectory()) await walk(new URL(entry.name + '/', folder), path + '/');
    else if (entry.name !== 'index.html' && !entry.name.endsWith('-offline.html')) entries[path] = (await readFile(new URL(entry.name, folder))).toString('base64');
  }
}
await walk(dist);
let html = await readFile(new URL('index.html', dist), 'utf8');
const scriptPath = html.match(/<script type="module"[^>]*src="([^"]+)"[^>]*><\/script>/)[1];
const cssPath = html.match(/<link rel="stylesheet"[^>]*href="([^"]+)"[^>]*>/)[1];
const js = await readFile(new URL(scriptPath, dist), 'utf8');
const css = await readFile(new URL(cssPath, dist), 'utf8');
const bootstrap = `const embedded=${JSON.stringify(entries)};const originalFetch=window.fetch.bind(window);window.fetch=async(input,init)=>{const u=new URL(typeof input==='string'?input:input.url,location.href);const path=decodeURIComponent(u.pathname);const key=Object.keys(embedded).find(k=>path.endsWith('/'+k));if(key){const bytes=Uint8Array.from(atob(embedded[key]),c=>c.charCodeAt(0));return new Response(bytes,{status:200,headers:{'Content-Type':key.endsWith('.json')?'application/json':'text/plain'}});}return originalFetch(input,init);};`;
html = html.replace(/<script type="module"[^>]*src="[^"]+"[^>]*><\/script>/, () => '<script>' + bootstrap.replaceAll('</script', '<\\/script') + '</script><script type="module">' + js.replaceAll('</script', '<\\/script') + '</script>');
html = html.replace(/<link rel="stylesheet"[^>]*href="[^"]+"[^>]*>/, () => '<style>' + css + '</style>');
await writeFile(new URL('brick-viewer-offline.html', dist), html);
console.log('Built portable offline viewer with embedded models, reference geometry and licenses.');
