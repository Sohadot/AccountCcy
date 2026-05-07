#!/usr/bin/env python3
"""AccountCcy.com — Sovereign SEO Validator."""
from __future__ import annotations
import argparse, re
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Sequence
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.in_title=False; self.title_parts=[]; self.h1=0; self.meta={}; self.og={}; self.tw={}; self.canonical=None; self.jsonld=0
    def handle_starttag(self, tag, attrs):
        d={k.lower():(v or '') for k,v in attrs}; tag=tag.lower()
        if tag=='title': self.in_title=True
        elif tag=='h1': self.h1+=1
        elif tag=='meta':
            if d.get('name'): self.meta[d['name'].lower()]=d.get('content','')
            if d.get('name','').lower().startswith('twitter:'): self.tw[d['name'].lower()]=d.get('content','')
            if d.get('property','').lower().startswith('og:'): self.og[d['property'].lower()]=d.get('content','')
        elif tag=='link' and 'canonical' in d.get('rel','').lower(): self.canonical=d.get('href')
        elif tag=='script' and d.get('type','').lower()=='application/ld+json': self.jsonld+=1
    def handle_endtag(self, tag):
        if tag.lower()=='title': self.in_title=False
    def handle_data(self, data):
        if self.in_title: self.title_parts.append(data)
    @property
    def title(self): return re.sub(r'\s+',' ',''.join(self.title_parts).strip())
def expected(root: Path, p: Path, base: str) -> str:
    rel=p.relative_to(root).as_posix(); return base.rstrip('/') + ('/' if rel=='index.html' else '/' + rel[:-len('index.html')])
def files(root: Path):
    for p in sorted(root.rglob('index.html')):
        parts={x.lower() for x in p.relative_to(root).parts}
        if parts & {'main','scripts','assets','.git','.github'}: continue
        yield p
def validate(root: Path, p: Path, base: str) -> List[str]:
    e=[]; parser=P(); parser.feed(p.read_text(encoding='utf-8', errors='ignore')); shown=p.relative_to(root)
    if not parser.title: e.append(f'{shown}: missing title')
    elif len(parser.title)>70: e.append(f'{shown}: title longer than 70 chars')
    desc=parser.meta.get('description','')
    if not desc: e.append(f'{shown}: missing meta description')
    elif len(desc)>170: e.append(f'{shown}: meta description longer than 170 chars')
    if parser.canonical != expected(root,p,base): e.append(f'{shown}: canonical mismatch')
    if parser.h1 != 1: e.append(f'{shown}: expected one H1, found {parser.h1}')
    if not parser.meta.get('robots'): e.append(f'{shown}: missing robots meta')
    for k in ['og:title','og:description','og:url','og:image']:
        if k not in parser.og: e.append(f'{shown}: missing {k}')
    for k in ['twitter:title','twitter:description','twitter:image']:
        if k not in parser.tw: e.append(f'{shown}: missing {k}')
    if parser.jsonld<1: e.append(f'{shown}: missing JSON-LD')
    return e
def main(argv: Optional[Sequence[str]]=None) -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default='.'); ap.add_argument('--base-url', default='https://accountccy.com'); args=ap.parse_args(argv); root=Path(args.root).resolve()
    errors=[]
    for p in files(root): errors.extend(validate(root,p,args.base_url))
    print(f'SEO validation errors: {len(errors)}')
    for e in errors: print('ERROR:', e)
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
