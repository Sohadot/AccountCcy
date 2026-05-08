#!/usr/bin/env python3
"""AccountCcy.com — Sovereign Page Generator."""
from __future__ import annotations
import argparse, html, json, re, sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set
try:
    from generate_schema import schema_for_registered_page, schema_for_glossary_term
except ImportError:
    from scripts.generate_schema import schema_for_registered_page, schema_for_glossary_term

BASE_URL='https://accountccy.com'; PUBLISHED='published'
class GenerationError(RuntimeError): pass
@dataclass(frozen=True)
class Page:
    url:str; type:str; template:str; status:str; title:str; meta_description:str; required_links:List[str]; schema_types:List[str]; indexable:bool; raw:Dict[str,Any]

def esc(v: Any) -> str: return html.escape(str(v or ''), quote=True)
def raw(v: Any) -> str: return str(v or '')
def load(path: Path, required=True):
    if not path.exists():
        if required: raise GenerationError(f'Missing JSON: {path}')
        return {}
    try: return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e: raise GenerationError(f'Invalid JSON {path}: {e}') from e

def tmpl(root: Path, name: str) -> str:
    p=root/'main/templates'/name
    if not p.exists(): raise GenerationError(f'Missing template: main/templates/{name}')
    return p.read_text(encoding='utf-8')

def repl(template: str, values: Dict[str,Any]) -> str:
    out=template
    for k,v in values.items(): out=out.replace('{{'+k+'}}', str(v))
    unresolved=sorted(set(re.findall(r'{{[A-Z0-9_]+}}', out)))
    if unresolved: raise GenerationError('Unresolved template tokens: '+', '.join(unresolved))
    return out

def norm(url: str) -> str:
    if not url.startswith('/'): raise GenerationError(f'URL must start /: {url}')
    if url!='/' and (not url.endswith('/') or '.html' in url): raise GenerationError(f'Invalid public URL: {url}')
    return url

def canon(url: str) -> str: return BASE_URL.rstrip('/') + ('/' if url=='/' else norm(url))
def outpath(root: Path, url: str) -> Path: return root/'index.html' if url=='/' else root/url.strip('/')/'index.html'
def slug(url: str) -> str: return 'homepage' if url=='/' else url.strip('/').replace('/','__')

def records(pages_json: Dict[str,Any]) -> Dict[str,Page]:
    d={}
    for i in pages_json.get('pages', []):
        u=norm(i['url'])
        if u in d: raise GenerationError(f'Duplicate page URL: {u}')
        d[u]=Page(u,i.get('type','reference'),i.get('template',''),i.get('status',''),i.get('title',''),i.get('meta_description',''),list(i.get('required_links',[])),list(i.get('schema_types',[])),bool(i.get('indexable',False)),i)
    return d

def published(records: Dict[str,Page], glossary: Dict[str,Any], tools: Dict[str,Any]) -> Set[str]:
    s={u for u,p in records.items() if p.status==PUBLISHED and p.indexable}; s.add('/')
    s |= {norm(t['url']) for t in glossary.get('terms', []) if t.get('status')==PUBLISHED}
    s |= {norm(tool.get('public_url') or tool['url']) for tool in tools.get('tools', []) if tool.get('status')==PUBLISHED}
    return s

def link_safety(records: Dict[str,Page], glossary: Dict[str,Any], tools: Dict[str,Any]) -> None:
    allowed=published(records, glossary, tools)
    for p in records.values():
        if p.status==PUBLISHED and p.indexable:
            bad=[l for l in p.required_links if norm(l) not in allowed]
            if bad: raise GenerationError(f'{p.url} links to unpublished/unregistered pages: '+', '.join(bad))
    for t in glossary.get('terms', []):
        if t.get('status')==PUBLISHED:
            bad=[l for l in t.get('related_pages', []) if norm(l) not in allowed]
            if bad: raise GenerationError(f"{t['url']} links to unpublished pages: "+', '.join(bad))

def content(root: Path, p: Page) -> Dict[str,Any]:
    cands=[]
    if p.url=='/': cands.append(root/'main/content/pages/homepage.json')
    cands += [root/'main/content/pages'/f'{slug(p.url)}.json']
    if p.url!='/': cands.append(root/'main/content/pages'/p.url.strip('/')/'content.json')
    for c in cands:
        if c.exists(): return load(c)
    # Preserve hand-authored HTML if it exists; no placeholder generation.
    if outpath(root,p.url).exists(): return {'__preserve_existing__': True}
    raise GenerationError(f'Missing content JSON for {p.url}. Expected one of: '+', '.join(str(c.relative_to(root)) for c in cands))

def paras(v: Any) -> str:
    if isinstance(v,str): return f'<p class="ccy-body">{esc(v)}</p>'
    return '\n'.join(f'<p class="ccy-body">{esc(x)}</p>' for x in (v or []))

def cards(items: Sequence[Dict[str,Any]], cls='ccy-state-card') -> str:
    return '\n'.join(f'<article class="{esc(cls)}"><p class="ccy-eyebrow">{esc(i.get("label","Reference"))}</p><h3 class="ccy-section-title">{esc(i.get("title",""))}</h3><p class="ccy-small">{esc(i.get("body",""))}</p></article>' for i in (items or []))

def rail(items: Sequence[Any], active: Optional[str]=None) -> str:
    out=[]
    for it in items or []:
        name=it if isinstance(it,str) else it.get('name','')
        desc='' if isinstance(it,str) else it.get('description','')
        u='' if isinstance(it,str) else it.get('url','')
        ac=' is-control' if active and active.lower() in name.lower() else ''
        h=f'<a href="{esc(u)}">{esc(name)}</a>' if u else esc(name)
        out.append(f'<div class="ccy-custody-state{ac}" role="listitem"><div class="ccy-state-dot" aria-hidden="true"></div><div class="ccy-state-body"><h3 class="ccy-state-name">{h}</h3><p class="ccy-state-desc">{esc(desc)}</p></div></div>')
    return '\n'.join(out)

def template_for(p: Page) -> str:
    if p.template: return p.template
    if p.url=='/': return 'homepage.html'
    if p.type in {'diagnostic','tool'}: return 'diagnostic.html'
    if p.type=='acquisition': return 'acquisition.html'
    if p.type=='state': return 'state_page.html'
    return 'reference-page.html'

def breadcrumb(p: Page) -> str:
    if p.url=='/': return ''
    parts=p.url.strip('/').split('/'); items=['<li><a href="/" style="color: var(--ccy-color-gold); text-decoration:none;">Home</a></li>']; path_acc=''
    for idx, part in enumerate(parts):
        path_acc += f'/{part}/'
        label=p.title if idx==len(parts)-1 else part.replace('-',' ').title()
        items.append('<li aria-hidden="true" style="color: var(--ccy-color-rule-dark);">→</li>')
        if idx==len(parts)-1:
            items.append(f'<li aria-current="page" style="color: var(--ccy-color-slate-mid);">{esc(label)}</li>')
        else:
            href = '/ccy-state-chain/' if parts[0]=='states' and idx==0 else path_acc
            items.append(f'<li><a href="{esc(href)}" style="color: var(--ccy-color-gold); text-decoration:none;">{esc(label)}</a></li>')
    return '<div class="ccy-container" style="padding-top: var(--ccy-space-6); padding-bottom: 0;"><nav aria-label="Breadcrumb"><ol style="display:flex; flex-wrap:wrap; gap: var(--ccy-space-2); list-style:none; margin:0; padding:0; font-family: var(--ccy-font-mono); font-size: var(--ccy-font-size-2xs); letter-spacing: var(--ccy-letter-wide); color: var(--ccy-color-slate-soft);">'+''.join(items)+'</ol></nav></div>'

def related(p: Page, records: Dict[str,Page], glossary: Dict[str,Any]) -> str:
    titles={norm(t['url']):t['term'] for t in glossary.get('terms', [])}
    blocks=[]
    for l in p.required_links:
        title=records[l].title if l in records else titles.get(l,l)
        blocks.append(f'<div class="ccy-nav-link-item"><span class="ccy-nav-link-label">Reference</span><a class="ccy-nav-link-title" href="{esc(l)}">{esc(title)}</a></div>')
    return '' if not blocks else '<section class="ccy-section" aria-labelledby="related-title"><div class="ccy-container"><p class="ccy-eyebrow" id="related-title">Continue Reading</p><div class="ccy-nav-links">'+''.join(blocks)+'</div></div></section>'

def render_reference(root: Path, p: Page, c: Dict[str,Any]) -> str:
    name='reference-page.html' if (root/'main/templates/reference-page.html').exists() else 'reference_page.html'
    return repl(tmpl(root,name), {
        'PAGE_EYEBROW':esc(c.get('page_eyebrow',p.type.title())),'H1':esc(c.get('h1',p.title.replace(' — AccountCcy.com',''))),'INTRO':esc(c.get('intro',p.meta_description)),
        'DOCTRINE_EYEBROW':esc(c.get('doctrine_eyebrow','AccountCcy Doctrine')),'DOCTRINE_STATEMENT':raw(c.get('doctrine_statement','Money becomes accounting truth through custody.')),'DOCTRINE_ATTRIBUTION':esc(c.get('doctrine_attribution','The Currency State Control Framework · AccountCcy.com')),
        'PRIMARY_SECTION_EYEBROW':esc(c.get('primary_section_eyebrow','Reference')),'PRIMARY_SECTION_TITLE':esc(c.get('primary_section_title',p.title)),'PRIMARY_SECTION_BODY':paras(c.get('primary_section_body',[])),
        'GRAPH_EYEBROW':esc(c.get('graph_eyebrow',c.get('grid_eyebrow','Reference Graph'))),'GRAPH_TITLE':esc(c.get('graph_title',c.get('grid_title','Reference graph position'))),'GRAPH_INTRO':esc(c.get('graph_intro',c.get('grid_intro',''))),'CARD_GRID_HTML':cards(c.get('cards',[])),
        'CONTROL_LABEL':esc(c.get('control_label','Control Discipline')),'CONTROL_TITLE':esc(c.get('control_title','Control logic')),'CONTROL_BODY':esc(c.get('control_body','')),
        'RISK_LABEL':esc(c.get('risk_label','Risk Discipline')),'RISK_TITLE':esc(c.get('risk_title','Risk if weak')),'RISK_BODY':esc(c.get('risk_body',''))})

def render_home(root: Path, p: Page, c: Dict[str,Any]) -> str:
    return repl(tmpl(root,'homepage.html'), {
        'HOMEPAGE_EYEBROW':esc(c.get('homepage_eyebrow','Monetary Truth Custody')),'HOMEPAGE_H1':esc(c.get('h1','The Chain of Custody for Monetary Truth')),'HOMEPAGE_INTRO':esc(c.get('intro',p.meta_description)),'HOMEPAGE_THESIS_QUOTE':esc(c.get('thesis_quote','Money does not become accounting truth automatically. It becomes truth through custody.')),
        'HOMEPAGE_STATE_RAIL_HTML':rail(c.get('state_rail',[]),'Account Currency'),'PROBLEM_EYEBROW':esc(c.get('problem_eyebrow','The Hidden Problem')),'PROBLEM_TITLE':esc(c.get('problem_title','Enterprise finance suffers from monetary truth fragmentation.')),'PROBLEM_BODY_HTML':paras(c.get('problem_body',[])),'PROBLEM_CARDS_HTML':cards(c.get('problem_cards',[])),
        'CONTROL_POINT_TITLE':esc(c.get('control_point_title','Account currency is where monetary movement enters accounting custody.')),'CONTROL_POINT_BODY':esc(c.get('control_point_body','')),'ACCOUNT_CURRENCY_DEFINITION':esc(c.get('account_currency_definition','')),'HOMEPAGE_DOCTRINE':raw(c.get('homepage_doctrine','Currency is not only exchanged. It is recorded, assigned, reconciled, translated, consolidated, reported, and audited.')),
        'AUDIENCE_TITLE':esc(c.get('audience_title','Built for professionals who live inside the financial system.')),'AUDIENCE_INTRO':esc(c.get('audience_intro','')),'AUDIENCE_CARDS_HTML':cards(c.get('audience_cards',[]),'ccy-evidence-panel'),'ACQUISITION_PREVIEW_TITLE':esc(c.get('acquisition_preview_title','A category-grade reference asset may be considered for strategic acquisition where institutional alignment exists.')),'ACQUISITION_PREVIEW_BODY':esc(c.get('acquisition_preview_body',''))})

def render_diag(root: Path, p: Page, c: Dict[str,Any]) -> str:
    levels='\n'.join(f'<span class="ccy-badge ccy-badge-gold">{esc(x)}</span>' for x in c.get('maturity_levels',['Fragmented','Configured','Governed','Controlled','Audit-Defensible']))
    return repl(tmpl(root,'diagnostic.html'), {'DIAGNOSTIC_TYPE':esc(c.get('diagnostic_type','Maturity Assessment')),'DIAGNOSTIC_NAME':esc(c.get('h1',p.title)),'DIAGNOSTIC_SUMMARY':esc(c.get('intro',p.meta_description)),'DIAGNOSTIC_PURPOSE_TITLE':esc(c.get('purpose_title','What this diagnostic is designed to assess.')),'DIAGNOSTIC_PURPOSE_BODY':esc(c.get('purpose_body','')),'DIAGNOSTIC_DISCLAIMER':esc(c.get('disclaimer','Reference diagnostic only. Not professional advice.')),'ASSESSMENT_TITLE':esc(c.get('assessment_title','Structured self-assessment')),'ASSESSMENT_INTRO':esc(c.get('assessment_intro','')),'DIAGNOSTIC_SLUG':esc(slug(p.url)),'DIAGNOSTIC_QUESTIONS_HTML':raw(c.get('questions_html','<p class="ccy-body">This diagnostic is local-first. No data is submitted by default.</p>')),'MATURITY_TITLE':esc(c.get('maturity_title','Currency-state maturity levels')),'MATURITY_INTRO':esc(c.get('maturity_intro','')),'MATURITY_LEVELS_HTML':levels,'REPORT_TITLE':esc(c.get('report_title','Professional report layer')),'REPORT_BODY':esc(c.get('report_body',''))})

def render_acq(root: Path, p: Page, c: Dict[str,Any]) -> str:
    return repl(tmpl(root,'acquisition.html'), {'ACQUISITION_H1':esc(c.get('h1',p.title)),'ACQUISITION_INTRO':esc(c.get('intro',p.meta_description)),'ACQUISITION_DOCTRINE':raw(c.get('acquisition_doctrine','This is not a commodity domain sale. It is a strategic asset transfer.')),'ASSET_INCLUDED_TITLE':esc(c.get('asset_included_title','What the asset includes.')),'ASSET_INCLUDED_BODY_HTML':paras(c.get('asset_included_body',[])),'ASSET_INCLUDED_CARDS_HTML':cards(c.get('asset_included_cards',[])),'BUYER_TITLE':esc(c.get('buyer_title','Aligned institutional buyers.')),'BUYER_INTRO':esc(c.get('buyer_intro','')),'BUYER_CARDS_HTML':cards(c.get('buyer_cards',[]),'ccy-evidence-panel'),'INQUIRY_TITLE':esc(c.get('inquiry_title','Institutional inquiry only.')),'INQUIRY_BODY':esc(c.get('inquiry_body',''))})

def render_state(root: Path, p: Page, c: Dict[str,Any]) -> str:
    return repl(tmpl(root,'state_page.html'), {'STATE_NUMBER':esc(c.get('state_number','')),'STATE_NAME':esc(c.get('state_name',c.get('h1',p.title))),'STATE_SUMMARY':esc(c.get('state_summary',c.get('intro',''))),'STATE_ROLE_LABEL':esc(c.get('state_role_label','State Role')),'STATE_ROLE_TITLE':esc(c.get('state_role_title','')),'STATE_ROLE_BODY':esc(c.get('state_role_body','')),'CUSTODY_QUESTION':esc(c.get('custody_question','')),'CHAIN_POSITION_BODY':esc(c.get('chain_position_body','')),'STATE_RAIL_HTML':rail(c.get('state_rail',[]),c.get('state_name')),'STATE_RISK_TITLE':esc(c.get('state_risk_title','')),'STATE_RISK_BODY':esc(c.get('state_risk_body','')),'STATE_CONTROL_TITLE':esc(c.get('state_control_title','')),'STATE_CONTROL_BODY':esc(c.get('state_control_body','')),'RECEIVES_FROM':esc(c.get('receives_from','')),'PASSES_TO':esc(c.get('passes_to',''))})

def render_base(root: Path, p: Page, c: Dict[str,Any], main: str, rel: str) -> str:
    return repl(tmpl(root,'base.html'), {'PAGE_TITLE':esc(p.title),'META_DESCRIPTION':esc(p.meta_description),'ROBOTS_DIRECTIVE':'index, follow' if p.indexable else 'noindex, follow','CANONICAL_URL':canon(p.url),'OG_TYPE':'website' if p.type=='homepage' else 'article','OG_TITLE':esc(p.title),'OG_DESCRIPTION':esc(p.meta_description),'JSON_LD':schema_for_registered_page(p.raw,c,BASE_URL),'BODY_CLASS':esc('page-'+p.type),'TEMPLATE_NAME':esc(template_for(p)),'PAGE_TYPE':esc(p.type),'BREADCRUMB_HTML':breadcrumb(p),'MAIN_CONTENT':main,'RELATED_LINKS_HTML':rel})

def render_page(root: Path, p: Page, recs: Dict[str,Page], glossary: Dict[str,Any]) -> Optional[str]:
    c=content(root,p)
    if c.get('__preserve_existing__'): return None
    t=template_for(p)
    if t=='homepage.html': main=render_home(root,p,c)
    elif t=='diagnostic.html': main=render_diag(root,p,c)
    elif t=='acquisition.html': main=render_acq(root,p,c)
    elif t=='state_page.html': main=render_state(root,p,c)
    else: main=render_reference(root,p,c)
    return render_base(root,p,c,main,related(p,recs,glossary))

def render_term(root: Path, term: Dict[str,Any], recs: Dict[str,Page], glossary: Dict[str,Any]) -> str:
    related_terms='\n'.join(f'<span class="ccy-badge ccy-badge-gold">{esc(str(x).replace("-"," ").title())}</span>' for x in term.get('related_terms', []))
    main=repl(tmpl(root,'glossary_term.html'), {'TERM_CATEGORY':esc(term.get('ccy_state_name','Reference Term')),'TERM':esc(term['term']),'DEFINITION':esc(term['definition']),'INSTITUTIONAL_CONTEXT':esc(term.get('institutional_context','')),'POSITION_IN_CHAIN':esc(term.get('position_in_chain','')),'WHY_IT_MATTERS':esc(term.get('why_it_matters','')),'RISK_IF_MISUNDERSTOOD':esc(term.get('risk_if_misunderstood','')),'RELATED_TERMS_HTML':related_terms})
    pseudo=Page(norm(term['url']),'glossary-term','glossary_term.html',PUBLISHED,f"{term['term']} — AccountCcy.com Glossary",term['definition'][:155],list(term.get('related_pages',[])),['DefinedTerm'],True,term)
    return repl(tmpl(root,'base.html'), {'PAGE_TITLE':esc(pseudo.title),'META_DESCRIPTION':esc(pseudo.meta_description),'ROBOTS_DIRECTIVE':'index, follow','CANONICAL_URL':canon(pseudo.url),'OG_TYPE':'article','OG_TITLE':esc(pseudo.title),'OG_DESCRIPTION':esc(pseudo.meta_description),'JSON_LD':schema_for_glossary_term(term,BASE_URL),'BODY_CLASS':'page-glossary-term','TEMPLATE_NAME':'glossary_term.html','PAGE_TYPE':'glossary-term','BREADCRUMB_HTML':breadcrumb(pseudo),'MAIN_CONTENT':main,'RELATED_LINKS_HTML':related(pseudo,recs,glossary)})

def write(root: Path, url: str, doc: str, overwrite: bool) -> str:
    p=outpath(root,url); p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not overwrite: return f'preserved existing {p.relative_to(root)}'
    p.write_text(doc, encoding='utf-8'); return f'wrote {p.relative_to(root)}'

def main(argv: Optional[Sequence[str]]=None) -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default='.'); ap.add_argument('--overwrite', action='store_true'); ap.add_argument('--dry-run', action='store_true'); args=ap.parse_args(argv)
    root=Path(args.root).resolve()
    try:
        pages=load(root/'main/data/pages.json'); glossary=load(root/'main/data/glossary_terms.json'); tools=load(root/'main/data/tools.json'); load(root/'main/data/link_graph.json')
        recs=records(pages); link_safety(recs, glossary, tools); actions=[]
        for p in recs.values():
            if p.status!=PUBLISHED or not p.indexable: continue
            doc=render_page(root,p,recs,glossary)
            actions.append(('would generate '+p.url) if args.dry_run else ('preserved existing '+str(outpath(root,p.url).relative_to(root)) if doc is None else write(root,p.url,doc,args.overwrite)))
        for term in glossary.get('terms', []):
            if term.get('status')!=PUBLISHED: continue
            doc=render_term(root,term,recs,glossary); actions.append(('would generate '+term['url']) if args.dry_run else write(root,norm(term['url']),doc,args.overwrite))
        print('AccountCcy sovereign page generation complete.'); [print('- '+a) for a in actions]; return 0
    except GenerationError as e:
        print('GENERATION BLOCKED:', e, file=sys.stderr); return 1
if __name__=='__main__': raise SystemExit(main())
