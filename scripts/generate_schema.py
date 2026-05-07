#!/usr/bin/env python3
"""AccountCcy.com — Sovereign Schema Generator."""
from __future__ import annotations
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

BASE_URL = "https://accountccy.com"

def canonical(url: str, base_url: str = BASE_URL) -> str:
    if not url.startswith('/'):
        raise ValueError(f"URL must start with /: {url}")
    if url != '/' and (not url.endswith('/') or '.html' in url):
        raise ValueError(f"URL must be directory-style and must not contain .html: {url}")
    return base_url.rstrip('/') + ('/' if url == '/' else url)

def webpage(page: Dict[str, Any], content: Dict[str, Any], base_url: str) -> Dict[str, Any]:
    return {
        '@type': 'WebPage',
        '@id': canonical(page['url'], base_url),
        'url': canonical(page['url'], base_url),
        'name': page.get('title') or content.get('h1') or 'AccountCcy.com',
        'description': page.get('meta_description') or content.get('intro') or '',
        'isPartOf': {'@type': 'WebSite', 'name': 'AccountCcy.com', 'url': base_url.rstrip('/') + '/'},
        'about': {'@type': 'Thing', 'name': 'Account Currency Control'},
        'inLanguage': 'en'
    }

def article(page: Dict[str, Any], content: Dict[str, Any], base_url: str) -> Dict[str, Any]:
    node = {
        '@type': 'Article',
        'headline': (content.get('h1') or page.get('title') or '').replace(' — AccountCcy.com',''),
        'description': page.get('meta_description') or content.get('intro') or '',
        'mainEntityOfPage': {'@type': 'WebPage', '@id': canonical(page['url'], base_url)},
        'author': {'@type': 'Organization', 'name': 'AccountCcy.com', 'url': base_url.rstrip('/') + '/'},
        'publisher': {'@type': 'Organization', 'name': 'AccountCcy.com', 'url': base_url.rstrip('/') + '/'},
        'inLanguage': 'en'
    }
    if content.get('last_updated'):
        node['dateModified'] = content['last_updated']
    return node

def breadcrumb(url: str, title: str, base_url: str) -> Dict[str, Any]:
    parts = [] if url == '/' else [p for p in url.strip('/').split('/') if p]
    items = [{'@type':'ListItem','position':1,'name':'Home','item':canonical('/', base_url)}]
    path = ''
    for i, part in enumerate(parts, start=2):
        path += f'/{part}/'
        items.append({'@type':'ListItem','position':i,'name': title if i == len(parts)+1 else part.replace('-',' ').title(),'item':canonical(path, base_url)})
    return {'@type':'BreadcrumbList','itemListElement':items}

def faq(items: Sequence[Dict[str, str]]) -> Optional[Dict[str, Any]]:
    main = []
    for item in items or []:
        q, a = str(item.get('question','')).strip(), str(item.get('answer','')).strip()
        if q and a:
            main.append({'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}})
    return {'@type':'FAQPage','mainEntity':main} if main else None

def defined_term(term: Dict[str, Any], base_url: str) -> Dict[str, Any]:
    return {'@type':'DefinedTerm','name':term['term'],'description':term['definition'],'url':canonical(term['url'], base_url),'inDefinedTermSet':{'@type':'DefinedTermSet','name':'AccountCcy.com Glossary','url':canonical('/glossary/', base_url)}}

def graph(nodes: Sequence[Optional[Dict[str, Any]]]) -> str:
    return json.dumps({'@context':'https://schema.org','@graph':[n for n in nodes if n]}, indent=4, ensure_ascii=False)

def schema_for_registered_page(page: Dict[str, Any], content: Optional[Dict[str, Any]]=None, base_url: str=BASE_URL) -> str:
    content = content or {}
    nodes: List[Optional[Dict[str, Any]]] = [webpage(page, content, base_url), breadcrumb(page['url'], page.get('title') or content.get('h1') or 'AccountCcy.com', base_url)]
    schema_types = set(page.get('schema_types', []))
    if 'Article' in schema_types or page.get('type') in {'pillar','reference','cfo','risk','erp','comparison','acquisition'}:
        nodes.append(article(page, content, base_url))
    if 'FAQPage' in schema_types or content.get('faq'):
        nodes.append(faq(content.get('faq', [])))
    return graph(nodes)

def schema_for_glossary_term(term: Dict[str, Any], base_url: str=BASE_URL) -> str:
    pseudo = {'url':term['url'],'title':f"{term['term']} — AccountCcy.com Glossary",'meta_description':term['definition'][:155], 'type':'glossary-term'}
    return graph([defined_term(term, base_url), webpage(pseudo, {}, base_url), breadcrumb(term['url'], term['term'], base_url)])

def validate_jsonld(raw: str) -> List[str]:
    try: data = json.loads(raw)
    except json.JSONDecodeError as e: return [f'Invalid JSON-LD: {e}']
    errors = []
    if data.get('@context') != 'https://schema.org': errors.append('Missing schema.org context')
    if not isinstance(data.get('@graph'), list) or not data.get('@graph'): errors.append('Missing non-empty @graph')
    return errors

def load(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}

def main(argv: Optional[Sequence[str]]=None) -> int:
    p = argparse.ArgumentParser(); p.add_argument('--root', default='.'); p.add_argument('--base-url', default=BASE_URL); args = p.parse_args(argv)
    root = Path(args.root).resolve(); pages = load(root/'main/data/pages.json'); glossary = load(root/'main/data/glossary_terms.json')
    report = {'generated_at':datetime.now(timezone.utc).isoformat(),'errors':[],'page_count':0,'term_count':0}
    for page in pages.get('pages', []):
        if page.get('status') == 'published' and page.get('indexable'):
            errs = validate_jsonld(schema_for_registered_page(page, base_url=args.base_url)); report['errors'] += [f"{page['url']}: {e}" for e in errs]; report['page_count'] += 1
    for term in glossary.get('terms', []):
        if term.get('status') == 'published':
            errs = validate_jsonld(schema_for_glossary_term(term, args.base_url)); report['errors'] += [f"{term['url']}: {e}" for e in errs]; report['term_count'] += 1
    out = root/'main/reports/schema-report.json'; out.parent.mkdir(parents=True, exist_ok=True); out.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(f"Schema report: {out.relative_to(root)} | Errors: {len(report['errors'])}")
    for e in report['errors']: print('ERROR:', e)
    return 1 if report['errors'] else 0
if __name__ == '__main__': raise SystemExit(main())
