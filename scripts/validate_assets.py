#!/usr/bin/env python3
"""AccountCcy.com — Sovereign Asset Validator."""
from __future__ import annotations
import argparse
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Optional, Sequence
from urllib.parse import urlparse
REQ = [
    'assets/css/main.css',
    'assets/icons/favicon.webp',
    'assets/img/social-preview.webp',
    'assets/img/logo-accountccy.webp',
]
class AP(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.assets=[]
    def handle_starttag(self, tag, attrs):
        d={k.lower():(v or '') for k,v in attrs}; tag=tag.lower()
        if tag=='link' and d.get('href') and any(x in d.get('rel','').lower() for x in ['stylesheet','icon','apple-touch-icon','preload']): self.assets.append(d['href'])
        if tag in {'img','script','source','video','audio'} and d.get('src'): self.assets.append(d['src'])
        if tag=='meta' and d.get('property','').lower()=='og:image' and d.get('content'): self.assets.append(d['content'])
        if tag=='meta' and d.get('name','').lower()=='twitter:image' and d.get('content'): self.assets.append(d['content'])
def local(root: Path, current: Path, asset: str) -> Optional[Path]:
    pr=urlparse(asset)
    if pr.scheme in {'http','https','data','mailto','tel'}:
        if pr.netloc=='accountccy.com': return root/pr.path.lstrip('/')
        return None
    clean=asset.split('#',1)[0].split('?',1)[0]
    if not clean: return None
    return root/clean.lstrip('/') if clean.startswith('/') else (current.parent/clean).resolve()
def files(root: Path):
    for p in sorted(root.rglob('index.html')):
        parts={x.lower() for x in p.relative_to(root).parts}
        if parts & {'main','scripts','assets','.git','.github'}: continue
        yield p
def main(argv: Optional[Sequence[str]]=None) -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default='.'); args=ap.parse_args(argv); root=Path(args.root).resolve(); errors=[]
    for a in REQ:
        if not (root/a).exists(): errors.append(f'required asset missing: {a}')
    for p in files(root):
        parser=AP(); parser.feed(p.read_text(encoding='utf-8', errors='ignore'))
        for a in parser.assets:
            t=local(root,p,a)
            if t and not t.exists():
                try: shown=t.relative_to(root)
                except ValueError: shown=t
                errors.append(f'{p.relative_to(root)}: missing asset {a} -> {shown}')
    print(f'Asset validation errors: {len(errors)}')
    for e in errors: print('ERROR:', e)
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
