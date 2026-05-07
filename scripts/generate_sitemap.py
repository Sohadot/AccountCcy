#!/usr/bin/env python3
"""AccountCcy.com — Sovereign Sitemap Generator and Indexing Gate."""
from __future__ import annotations
import argparse, json, re, subprocess, sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Optional, Sequence, Tuple
from urllib.parse import quote, unquote, urljoin, urlparse
from xml.sax.saxutils import escape
BASE_URL='https://accountccy.com'; NS='https://www.sitemaps.org/schemas/sitemap/0.9'
EXCL={'main','scripts','assets','.git','.github','draft','drafts','private','internal','templates','data','tests','test','archive','archives'}
@dataclass
class Audit:
    source_path:str; url_path:str; loc:str; title:Optional[str]=None; description:Optional[str]=None; canonical:Optional[str]=None; robots:Optional[str]=None; h1_count:int=0; errors:List[str]=field(default_factory=list); warnings:List[str]=field(default_factory=list)
@dataclass(frozen=True)
class Entry:
    loc:str; lastmod:str; changefreq:str; priority:str; source_path:str
class P(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.in_title=False; self.title_parts=[]; self.description=None; self.canonical=None; self.robots=None; self.h1=0; self.links=[]; self.assets=[]
    def handle_starttag(self, tag, attrs):
        d={k.lower():(v or '') for k,v in attrs}; tag=tag.lower()
        if tag=='title': self.in_title=True
        elif tag=='h1': self.h1+=1
        elif tag=='meta':
            if d.get('name','').lower()=='description': self.description=d.get('content','').strip()
            if d.get('name','').lower()=='robots': self.robots=d.get('content','').strip()
            if d.get('property','').lower()=='og:image' and d.get('content'): self.assets.append(d['content'])
            if d.get('name','').lower()=='twitter:image' and d.get('content'): self.assets.append(d['content'])
        elif tag=='link':
            if 'canonical' in d.get('rel','').lower(): self.canonical=d.get('href')
            if d.get('href') and any(x in d.get('rel','').lower() for x in ['stylesheet','icon','preload']): self.assets.append(d['href'])
        elif tag=='a' and d.get('href'): self.links.append(d['href'].strip())
        elif tag in {'img','script','source','video','audio'} and d.get('src'): self.assets.append(d['src'])
    def handle_endtag(self, tag):
        if tag.lower()=='title': self.in_title=False
    def handle_data(self, data):
        if self.in_title: self.title_parts.append(data)
    @property
    def title(self): return re.sub(r'\s+',' ',''.join(self.title_parts).strip()) or None

def base(b: str) -> str:
    if not b.startswith(('https://','http://')): raise ValueError('base-url must start with http(s)')
    return b.rstrip('/')
def skip(root: Path, p: Path) -> bool:
    if p.name.lower()!='index.html': return True
    parts={x.lower() for x in p.relative_to(root).parts}
    return bool(parts & EXCL) or any(x.startswith('.') for x in p.relative_to(root).parts)
def url(root: Path, p: Path) -> str:
    rel=p.relative_to(root).as_posix(); return '/' if rel=='index.html' else '/' + rel[:-len('index.html')]
def loc(base_url: str, u: str) -> str: return base_url + quote(u, safe='/-._~')
def noindex(robots: Optional[str]) -> bool: return 'noindex' in {x.strip().lower() for x in (robots or '').split(',')}
def parse(p: Path) -> P: parser=P(); parser.feed(p.read_text(encoding='utf-8', errors='ignore')); return parser
def lastmod(root: Path, p: Path) -> str:
    try:
        r=subprocess.run(['git','log','-1','--format=%cI','--',str(p.relative_to(root))], cwd=root, capture_output=True, text=True, check=False)
        if r.stdout.strip(): return datetime.fromisoformat(r.stdout.strip().replace('Z','+00:00')).date().isoformat()
    except Exception: pass
    return datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).date().isoformat()
def classify(u: str) -> Tuple[str,str]:
    if u=='/': return 'weekly','1.0'
    if u in {'/framework/','/ccy-state-chain/','/what-is-account-currency/','/monetary-truth-chain-of-custody/'}: return 'monthly','0.9'
    if u.startswith('/glossary/'): return 'monthly','0.7'
    if u.startswith('/states/'): return 'monthly','0.75'
    if u.startswith('/currency-state-diagnostic/'): return 'monthly','0.8'
    return 'monthly','0.6'
def target(root: Path, current: str, href: str, base_url: str) -> Optional[Path]:
    if not href or href.startswith('#'): return None
    pr=urlparse(href)
    if pr.scheme in {'mailto','tel','sms','javascript','data'}: return None
    if pr.scheme in {'http','https'}:
        if not href.startswith(base_url): return None
        path=href[len(base_url):] or '/'
    else: path=href.split('#',1)[0].split('?',1)[0]
    if not path: return None
    if not path.startswith('/'):
        basep=current if current.endswith('/') else current.rsplit('/',1)[0]+'/'; path=urlparse(urljoin(basep,path)).path
    path=unquote(path)
    if path.endswith('.html'): return root/path.lstrip('/')
    return root/'index.html' if path=='/' else root/path.strip('/')/'index.html'
def asset(root: Path, cur: Path, src: str, base_url: str) -> Optional[Path]:
    pr=urlparse(src)
    if pr.scheme in {'http','https','data','mailto','tel'}:
        if pr.netloc=='accountccy.com': return root/pr.path.lstrip('/')
        return None
    clean=src.split('#',1)[0].split('?',1)[0]
    if not clean: return None
    return root/clean.lstrip('/') if clean.startswith('/') else (cur.parent/clean).resolve()
def discover(root: Path, base_url: str):
    entries=[]; audits=[]
    for p in sorted(root.rglob('index.html')):
        if skip(root,p): continue
        u=url(root,p); l=loc(base_url,u); h=parse(p); a=Audit(p.relative_to(root).as_posix(),u,l,h.title,h.description,h.canonical,h.robots,h.h1)
        if noindex(h.robots): audits.append(a); continue
        if not h.title: a.errors.append('Missing title')
        if not h.description: a.errors.append('Missing meta description')
        elif len(h.description)>170: a.warnings.append('Meta description longer than 170 characters')
        if h.canonical!=l: a.errors.append(f'Canonical mismatch. Expected {l}, found {h.canonical}')
        if h.h1!=1: a.errors.append(f'Expected one H1, found {h.h1}')
        for href in h.links:
            t=target(root,u,href,base_url)
            if t and not t.exists(): a.errors.append(f'Broken internal link: {href}')
        for src in h.assets:
            t=asset(root,p,src,base_url)
            if t and not t.exists(): a.errors.append(f'Missing local asset: {src}')
        cf,pri=classify(u); entries.append(Entry(l,lastmod(root,p),cf,pri,p.relative_to(root).as_posix())); audits.append(a)
    return entries,audits
def render(entries):
    lines=['<?xml version="1.0" encoding="UTF-8"?>',f'<urlset xmlns="{NS}">']
    for e in entries: lines += ['  <url>',f'    <loc>{escape(e.loc)}</loc>',f'    <lastmod>{escape(e.lastmod)}</lastmod>',f'    <changefreq>{escape(e.changefreq)}</changefreq>',f'    <priority>{escape(e.priority)}</priority>','  </url>']
    return '\n'.join(lines)+"\n</urlset>\n" if False else '\n'.join(lines+['</urlset>'])+'\n'
def robots(root: Path, base_url: str, write: bool):
    p=root/'robots.txt'; expected=f'Sitemap: {base_url}/sitemap.xml'
    if write: p.write_text(f'User-agent: *\nAllow: /\n\n{expected}\n', encoding='utf-8'); return []
    if not p.exists(): return ['robots.txt missing']
    return [] if expected in p.read_text(encoding='utf-8', errors='ignore') else [f'robots.txt missing expected sitemap reference: {expected}']
def main(argv: Optional[Sequence[str]]=None) -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default='.'); ap.add_argument('--base-url', default=BASE_URL); ap.add_argument('--strict', action='store_true'); ap.add_argument('--fail-on-warnings', action='store_true'); ap.add_argument('--report', action='store_true'); ap.add_argument('--write-robots', action='store_true'); args=ap.parse_args(argv)
    root=Path(args.root).resolve(); b=base(args.base_url); entries,audits=discover(root,b); entries.sort(key=lambda e:(0 if e.loc==b+'/' else 1,e.loc))
    errors=[]; warnings=robots(root,b,args.write_robots); seen=set()
    for e in entries:
        if e.loc in seen: errors.append(f'Duplicate URL: {e.loc}')
        seen.add(e.loc)
    for a in audits: errors += [f'{a.source_path}: {x}' for x in a.errors]; warnings += [f'{a.source_path}: {x}' for x in a.warnings]
    (root/'sitemap.xml').write_text(render(entries), encoding='utf-8')
    if args.report:
        rp=root/'main/reports/indexing-report.json'; rp.parent.mkdir(parents=True, exist_ok=True); rp.write_text(json.dumps({'generated_at':datetime.now(timezone.utc).isoformat(),'url_count':len(entries),'errors':errors,'warnings':warnings,'audits':[asdict(a) for a in audits]}, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(f'Generated sitemap.xml with {len(entries)} URLs.'); print(f'Errors: {len(errors)}'); print(f'Warnings: {len(warnings)}')
    for e in errors: print('ERROR:', e)
    for w in warnings: print('WARNING:', w)
    if args.strict and errors: return 1
    if args.fail_on_warnings and warnings: return 1
    return 0
if __name__=='__main__': raise SystemExit(main())
