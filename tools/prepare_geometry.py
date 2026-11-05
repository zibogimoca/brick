"""공식 LDraw ZIP의 지정 부품과 의존 형상을 추가한다. 기존 파일은 덮어쓰거나 삭제하지 않는다.
실행: python3 tools/prepare_geometry.py /tmp/complete.zip --parts 64179 30504
모든 의존성과 기존 해시를 확인한 뒤 저장하며 원본 저자·라이선스 주석을 유지한다.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

START = '<!-- asset-manifest:start -->\n```json\n'
END = '\n```\n<!-- asset-manifest:end -->'

def digest(data):
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def add_geometry(archive, requested, root=Path('assets')):
    policy = root / 'policy.md'
    before, rest = policy.read_text().split(START, 1)
    body, after = rest.split(END, 1)
    manifest = json.loads(body)
    files = manifest['files']
    for rel, entry in files.items():
        data = (root / rel).read_bytes()
        if any(digest(data)[key] != entry[key] for key in ('sha256', 'bytes')):
            raise ValueError('Existing asset integrity mismatch: ' + rel)
    requested = sorted(set(p.lower().removesuffix('.dat') for p in requested))
    if not requested or any(not re.fullmatch(r'[a-z0-9_-]+', p) for p in requested):
        raise ValueError('Supply explicit part numbers with --parts')
    pending = {}
    visited = set()
    with zipfile.ZipFile(archive) as z:
        members = {n.lower(): n for n in z.namelist()}
        def resolve(name):
            name = name.replace('\\', '/').lower()
            if name.startswith('/') or '..' in name.split('/'):
                raise ValueError('Unsafe reference: ' + name)
            for rel in (name, 'parts/' + name, 'p/' + name):
                if 'ldraw/' + rel in members:
                    return rel
            raise ValueError('Missing ZIP dependency: ' + name)
        def local(rel):
            if rel.startswith('parts/s/'):
                return rel.replace('parts/s/', 'parts/subparts/', 1)
            if rel.startswith('p/48/'):
                choices = ['primitives/48/' + rel[5:], 'primitives/high-resolution/' + rel[5:]]
                return next((p for p in choices if (root / p).exists()), choices[0])
            return rel.replace('p/', 'primitives/', 1) if rel.startswith('p/') else rel
        def check_existing(path):
            if path in visited:
                return
            visited.add(path)
            data = (root / path).read_bytes()
            if path not in files:
                raise ValueError('Unregistered existing asset: ' + path)
            for line in data.decode('utf-8-sig').splitlines():
                fields = line.split(maxsplit=14)
                if len(fields) == 15 and fields[0] == '1':
                    child = fields[14].replace('\\', '/').lower()
                    match = next((p for p in (child, 'parts/' + child, 'primitives/' + child) if (root / p).is_file()), None)
                    if match is None:
                        raise ValueError('Broken existing dependency: ' + child)
                    check_existing(match)
        def collect(rel):
            path = local(rel)
            if (root / path).exists():
                check_existing(path)
                return
            if path in pending:
                return
            data = z.read(members['ldraw/' + rel])
            pending[path] = b''  # Guard recursive dependency cycles.
            lines = []
            for line in data.decode('utf-8-sig').splitlines(keepends=True):
                fields = line.split(maxsplit=14)
                if len(fields) == 15 and fields[0] == '1':
                    child = resolve(fields[14].strip())
                    collect(child)
                    ending = '\r\n' if line.endswith('\r\n') else '\n' if line.endswith('\n') else ''
                    line = ' '.join(fields[:14]) + ' ' + local(child) + ending
                lines.append(line)
            pending[path] = ''.join(lines).encode('utf-8')
        for part in requested:
            # Existing roots may belong to an older archive; preserve them verbatim.
            path = 'parts/' + part + '.dat'
            if (root / path).exists():
                check_existing(path)
            else:
                collect(resolve(path))
        if not (root / 'LDConfig.ldr').exists():
            pending['LDConfig.ldr'] = z.read(members['ldraw/ldconfig.ldr'])
    # Nothing above mutates assets: missing dependencies leave the repository untouched.
    for path, data in pending.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        files[path] = digest(data)
    manifest['parts'] = sorted(set(manifest.get('parts', [])) | set(requested))
    policy.write_text(before + START + json.dumps(manifest, ensure_ascii=False, indent=2) + END + after)
    print('Added', len(pending), 'files; preserved', len(files) - len(pending), 'existing files. No geometry deleted or replaced.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('--parts', nargs='+', required=True)
    args = parser.parse_args()
    add_geometry(args.archive, args.parts)
