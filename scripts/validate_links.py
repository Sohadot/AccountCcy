#!/usr/bin/env python3
"""AccountCcy.com — Sovereign Link Validator."""
from __future__ import annotations
import argparse, json
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Optional, Sequence
from urllib.parse import urljoin, urlparse, unquote
BASE_URL='https://accountccy.com'
class AParser(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.hrefs=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower()=='a':
            d={k.lower():(v or '') for k,v in attrs}; h=d.get('href','').strip()
            if h: self.hrefs.append(h)
def load(p: Path): return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
def url_for(root: Path, p: Path) -> str:
    rel=p.relative_to(root).as_posix(); return '/' if rel=='index.html' else '/' + rel[:-len('index.html')]
def target(root: Path, current: str, href: str) -> Optional[Path]:
    if not href or href.startswith('#'): return None
    pr=urlparse(href)
    if pr.scheme in {'mailto','tel','sms','javascript','data'}: return None
    if pr.scheme in {'http','https'}:
        if not href.startswith(BASE_URL): return None
        path=href[len(BASE_URL):] or '/'
    else: path=href.split('#',1)[0].split('?',1)[0]
    if not path: return None
    if not path.startswith('/'):
        base=current if current.endswith('/') else current.rsplit('/',1)[0]+'/'; path=urlparse(urljoin(base,path)).path
    path=unquote(path)
    if path.endswith('.html'): return root/path.lstrip('/')
    return root/'index.html' if path=='/' else root/path.strip('/')/'index.html'
def html_files(root: Path):
    for p in sorted(root.rglob('index.html')):
        parts={x.lower() for x in p.relative_to(root).parts}
        if parts & {'main','scripts','assets','.git','.github'}: continue
        yield p
def validate_html(root: Path) -> List[str]:
    errors=[]
    for p in html_files(root):
        cur=url_for(root,p); parser=AParser(); parser.feed(p.read_text(encoding='utf-8', errors='ignore'))
        for href in parser.hrefs:
            if '.html' in href and not href.startswith(('http://','https://')): errors.append(f'{p.relative_to(root)}: .html public link {href}')
            t=target(root,cur,href)
            if t and not t.exists(): errors.append(f'{p.relative_to(root)}: broken link {href}')
    return errors
def validate_data(root: Path) -> List[str]:
    errors=[]; pages=load(root/'main/data/pages.json').get('pages',[]); glossary=load(root/'main/data/glossary_terms.json').get('terms',[]); tools=load(root/'main/data/tools.json').get('tools',[])
    pub={p['url'] for p in pages if p.get('status')=='published' and p.get('indexable')}; pub|={t['url'] for t in glossary if t.get('status')=='published'}; pub|={(x.get('public_url') or x['url']) for x in tools if x.get('status')=='published'}; pub.add('/')
    for p in pages:
        if p.get('status')=='published' and p.get('indexable'):
            for l in p.get('required_links',[]):
                if l not in pub: errors.append(f"{p['url']}: unpublished required link {l}")
    for t in glossary:
        if t.get('status')=='published':
            for l in t.get('related_pages',[]):
                if l not in pub: errors.append(f"{t['url']}: unpublished related page {l}")
    return errors
def main(argv: Optional[Sequence[str]]=None) -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default='.'); args=ap.parse_args(argv); root=Path(args.root).resolve()
    errors=validate_data(root)+validate_html(root); print(f'Link validation errors: {len(errors)}')
    for e in errors: print('ERROR:', e)
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
