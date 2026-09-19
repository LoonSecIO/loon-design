"""Generate CSS and a deterministic source bundle from the versioned foundations."""
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]


def build():
    data = json.loads((ROOT / 'tokens/design.json').read_text())
    out = ROOT / 'dist'
    out.mkdir(exist_ok=True)
    lines = ['/* Generated from tokens/design.json; do not edit. */', ':root {']
    for group in ('brand', 'space', 'radius', 'font'):
        lines += [f'  --loon-{group}-{key}: {value};' for key, value in data[group].items()]
    lines += [f'  --loon-{key}: {value};' for key, value in data['themes']['light'].items()]
    lines += ['}', '[data-loon-theme="dark"] {']
    lines += [f'  --loon-{key}: {value};' for key, value in data['themes']['dark'].items()]
    lines += ['}', '']
    (out / 'tokens.css').write_text('\n'.join(lines))
    files = [p for folder in ('assets', 'guide', 'tokens') for p in (ROOT / folder).rglob('*') if p.is_file()]
    files += [ROOT / p for p in ('README.md', 'LICENSE', 'BRAND-USAGE.md', 'ASSETS.md', 'CHANGELOG.md', 'sources.json')]
    files += [out / 'tokens.css']
    with ZipFile(out / f"loon-design-{data['version']}.zip", 'w') as bundle:
        for p in sorted(files):
            name = 'tokens/tokens.css' if p.parent == out else p.relative_to(ROOT).as_posix()
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, p.read_bytes())
    return out


if __name__ == '__main__':
    print(build())
