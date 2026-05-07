#!/usr/bin/env python3
"""AccountCcy.com — Sovereign Content Validator."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from typing import Any, List, Optional, Sequence

PLACEHOLDERS=[r'\bcoming soon\b',r'\bunder construction\b',r'\blorem ipsum\b',r'\btbd\b',r'\bplaceholder\b',r'\bmore content soon\b',r'\bto be added\b']
REQ_PAGE=['url','type','status','title','meta_description','indexable']
REQ_CONTENT=['h1','intro','primary_section_body']
REQ_TERM=['slug','term','url','status','definition','institutional_context','position_in_chain','why_it_matters','risk_if_misunderstood']

def load(path: Path) -> Any: return json.loads(path.read_text(encoding='utf-8'))
def slug(url: str) -> str: return 'homepage' if url=='/' else url.strip('/').replace('/','__')
def has_placeholder(v: Any) -> bool:
    text=json.dumps(v, ensure_ascii=False).lower()
    return any(re.search(p,text) for p in PLACEHOLDERS)
def candidates(root: Path, url: str) -> List[Path]:
    out=[]
    if url=='/': out.append(root/'main/content/pages/homepage.json')
    out.append(root/'main/content/pages'/f'{slug(url)}.json')
    if url!='/': out.append(root/'main/content/pages'/url.strip('/')/'content.json')
    return out

def validate_json(root: Path) -> List[str]:
    errors=[]
    if not (root/'main').exists(): return ['main/ directory missing']
    for p in (root/'main').rglob('*.json'):
        try: load(p)
        except Exception as e: errors.append(f'{p.relative_to(root)} invalid JSON: {e}')
    return errors

def validate_pages(root: Path) -> List[str]:
    errors=[]; path=root/'main/data/pages.json'
    if not path.exists(): return ['main/data/pages.json missing']
    data=load(path); seen=set()
    for page in data.get('pages',[]):
        u=page.get('url','<unknown>')
        if u in seen: errors.append(f'duplicate page URL: {u}')
        seen.add(u)
        for f in REQ_PAGE:
            if page.get(f) in [None,'']: errors.append(f'{u}: missing {f}')
        if u!='<unknown>' and (not u.startswith('/') or (u!='/' and not u.endswith('/')) or '.html' in u): errors.append(f'{u}: invalid directory-style URL')
        if page.get('status')=='published' and page.get('indexable'):
            found=next((c for c in candidates(root,u) if c.exists()), None)
            html=root/'index.html' if u=='/' else root/u.strip('/')/'index.html'
            if not found and not html.exists(): errors.append(f'{u}: published page has no content JSON and no HTML output')
            if found:
                c=load(found)
                if has_placeholder(c): errors.append(f'{u}: content contains placeholder language')
                if page.get('type') not in {'homepage','acquisition','diagnostic','state'}:
                    for f in REQ_CONTENT:
                        if not c.get(f): errors.append(f'{u}: content missing {f}')
    return errors

def validate_glossary(root: Path) -> List[str]:
    errors=[]; path=root/'main/data/glossary_terms.json'
    if not path.exists(): return ['main/data/glossary_terms.json missing']
    data=load(path); seen=set()
    for term in data.get('terms',[]):
        s=term.get('slug','<unknown>')
        if s in seen: errors.append(f'duplicate glossary slug: {s}')
        seen.add(s)
        if term.get('status')=='published':
            for f in REQ_TERM:
                if not term.get(f): errors.append(f'glossary/{s}: missing {f}')
            if has_placeholder(term): errors.append(f'glossary/{s}: placeholder language')
    return errors

def main(argv: Optional[Sequence[str]]=None) -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default='.'); args=ap.parse_args(argv); root=Path(args.root).resolve()
    errors=validate_json(root)+validate_pages(root)+validate_glossary(root)
    print(f'Content validation errors: {len(errors)}')
    for e in errors: print('ERROR:', e)
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
