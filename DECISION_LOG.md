# AccountCcy.com Decision Log

## Purpose

This file records major strategic, architectural, conceptual, commercial, technical, and governance decisions for AccountCcy.com.

The decision log exists to preserve institutional memory.

It prevents future drift.

It ensures that the asset remains consistent with its sovereign-grade doctrine, strategic thesis, and long-horizon value construction logic.

Every major decision should be recorded here.

---

## Decision Log Rules

Each entry should include:

- date
- decision
- strategic meaning
- implications
- next action if relevant

The decision log should not record minor edits.

It should record decisions that affect the asset’s meaning, structure, monetization, acquisition posture, public positioning, quality discipline, or build direction.

---

## 2026-05-09 — Audit Evidence & Close Control Cluster Published

Published the third controlled reference cluster for AccountCcy.com, extending the Currency State Control Framework from ERP and ledger control into audit evidence, period-end close discipline, control exceptions, FX control evidence, monetary truth governance, and currency-state audit trails.

The cluster added six indexable reference pages:

- /audit-evidence-for-currency-state-control/
- /period-end-currency-close-control/
- /currency-control-exceptions/
- /fx-control-evidence/
- /monetary-truth-close-discipline/
- /currency-state-audit-trail/

The pages use the existing reference-page.html rendering path through render_reference and introduce no new template, renderer, unsupported JSON fields, tool, calculator, diagnostic workflow, acquisition page, ERP implementation guide, or vendor-specific advice.

This cluster strengthens AccountCcy.com by showing how currency-state control becomes audit-defensible evidence at period-end. It reinforces the asset thesis that AccountCcy.com is the chain of custody for monetary truth inside enterprise finance.

Validation completed successfully:

- Generated pages through the existing pipeline.
- Sitemap increased from 67 to 73 URLs.
- Sovereign Quality Gate passed.
- Production verification passed for all six Cluster 03 routes.
- sitemap.xml returned 73 <loc> entries and includes all six Cluster 03 routes.
- Commit: 2338357 — feat(site): audit evidence close control cluster.

---

## 2026-05-09 — ERP Ledger Control Layer Cluster Published

Published the second controlled reference cluster for AccountCcy.com, extending the Currency State Control Framework from conceptual currency-state distinctions into ERP, ledger, reconciliation, FX revaluation, and institutional control behavior.

The cluster added six indexable reference pages:

- /erp-currency-configuration-control/
- /ledger-currency-control/
- /account-currency-control-point/
- /multi-currency-reconciliation-control/
- /fx-revaluation-control/
- /currency-state-control-risk/

The pages use the existing reference-page.html rendering path through render_reference and introduce no new template, renderer, unsupported JSON fields, ERP implementation guide, diagnostic tool, calculator, acquisition page, or vendor-specific advice.

This cluster strengthens AccountCcy.com by showing how monetary identity becomes governed system behavior inside enterprise finance. It reinforces the asset thesis that AccountCcy.com is the chain of custody for monetary truth inside enterprise finance.

Validation completed successfully:

- Generated pages through the existing pipeline.
- Sitemap increased from 61 to 67 URLs.
- Sovereign Quality Gate passed.
- Commit: 12adbf0 — feat(site): erp ledger control layer cluster.

---

## 2026-05-08 — Core Reference Architecture Locked

### Decision

The foundational AccountCcy.com reference architecture is **locked** after the reinforcement sequence completed across the glossary hub, doctrine pillar, framework pillar, CCY State Chain pillar, primary definitional entry, canonical State 04 page, homepage sovereign pathway, and CFO decision layer.

### Strategic Meaning

The public surface now reads as a single governed reference system—not a loose collection of articles. Visitors can follow an explicit custody vocabulary pathway from definition through state mechanics, operational framework layers, doctrinal thesis, and lexicon authority.

### Published Spine (Authoritative)

| Layer | Path | Role |
|-------|------|------|
| Glossary Authority Map | `/glossary/` | Controlled vocabulary grouped into conceptual clusters—not a flat dictionary index. |
| Doctrine Pillar | `/monetary-truth-chain-of-custody/` | Core thesis: AccountCcy.com is the chain of custody for monetary truth inside enterprise finance. |
| Framework Pillar | `/framework/` | Operational control framing for currency states, ledger treatment, FX revaluation, translation, reporting, and audit evidence. |
| State Model Pillar | `/ccy-state-chain/` | Currency as a sequence of enterprise finance states—not a static ISO code. |
| Primary Entry | `/what-is-account-currency/` | Accessible definition and SEO entry point into custody language. |
| Canonical State 04 | `/states/account-currency/` | Account-level monetary state inside the CCY State Chain. |
| Sovereign Pathway | Homepage (`/` → `#sovereign-pathway`) | Reading path: Definition → Account Currency State → CCY State Chain → Framework → Monetary Truth Custody → Glossary. |
| CFO Decision Layer | `/cfo-guide/` | Executive translation: reporting integrity, FX discipline, ERP control, audit reconstruction, monetary truth governance. |

### Technical State (Verified)

- **Sitemap:** 31 published URLs at lock.
- **Quality discipline:** sovereign quality gate passed after the reinforcement sequence (`scripts/quality_gate.py`).
- **Link safety:** internal URLs remain constrained through `required_links` registry alignment and published-URL validation during generation.

### Expansion Posture

The spine is ready for **controlled expansion**—additional glossary clusters, state-depth pages, executive-facing guides, or audit/evidence layers—provided each increment preserves doctrine alignment, `link_safety`, strict sitemap discipline, and institutional tone.

---

## 2026-05-08 — Glossary Term Pages Cluster 02 Published

### Decision

AccountCcy.com published the second glossary term cluster focused on conceptual control terminology.

The cluster covers monetary truth, chain of custody, currency state, the Currency State Control Framework, account currency control, functional currency, FX revaluation, and currency translation.

### Strategic Meaning

This cluster strengthens the conceptual vocabulary beneath the AccountCcy doctrine and connects the glossary layer to the framework, the completed CCY State Chain, the CFO guide, and future comparison, ERP, and diagnostic content.

### Technical Changes

- Existing published glossary terms were preserved rather than duplicated.
- Invalid related-term slugs were corrected.
- Glossary term pages were regenerated.
- Sitemap expanded to 55 URLs.
- The sovereign quality gate passed.

### Governance Implication

Glossary term relationships must reference only published or valid glossary slugs. Related-term arrays are part of the reference graph and must remain honest, controlled, and non-placeholder.

---

## 2026-05-08 — Audit Evidence Control Layer Integrated

### Decision

**Glossary Cluster 03 — Audit, Evidence & Control Discipline** is **complete** as eight published terms, grouped on `/glossary/` under the **Audit, Evidence & Control Discipline** authority section; that vocabulary is **integrated** into doctrine, framework, state-sequence, State 04, CFO guidance, and the primary definition entry so audit reconstruction and evidence discipline operate as an explicit conceptual layer—not an implicit footnote.

### Published Terms (Cluster 03)

| Term | Path |
|------|------|
| Audit trail | `/glossary/audit-trail/` |
| Control evidence | `/glossary/control-evidence/` |
| Evidence trail | `/glossary/evidence-trail/` |
| Monetary reconstruction | `/glossary/monetary-reconstruction/` |
| State ownership | `/glossary/state-ownership/` |
| Reporting integrity | `/glossary/reporting-integrity/` |
| Audit defensibility | `/glossary/audit-defensibility/` |
| Monetary ambiguity | `/glossary/monetary-ambiguity/` |

### Strategic Meaning

The lexicon now names **monetary defensibility** in institutional language: reconstructable trails, governed **control evidence**, accountable **state ownership**, **reporting integrity** across translation boundaries, explicit **audit defensibility**, and the custody risk of **monetary ambiguity**. Integration into core pillars tightens the thesis that monetary truth must survive independent replay—without turning pillars into glossary inventories.

### Integration Surface (Verified)

| Surface | Path |
|---------|------|
| Doctrine | `/monetary-truth-chain-of-custody/` |
| Framework | `/framework/` |
| State sequence | `/ccy-state-chain/` |
| State 04 | `/states/account-currency/` |
| Executive layer | `/cfo-guide/` |
| Definition entry | `/what-is-account-currency/` |

### Technical State (Verified)

- **Glossary hub:** **24** published defined terms; Cluster 03 fills the audit/evidence/control discipline authority cluster alongside existing doctrine, architecture, accounting-control, and visibility clusters.
- **Sitemap:** **39** published URLs after Cluster 03 publication and pillar integration pass.
- **Quality discipline:** sovereign quality gate passed after integration (`scripts/quality_gate.py`).
- **Link safety:** unchanged—`required_links` alignment and published-URL validation during generation.

---

## 2026-05-08 — FX Reporting Mechanics Layer Integrated

### Decision

**Glossary Cluster 04 — FX, Translation & Reporting Mechanics** is **complete** as eight published terms, grouped on `/glossary/` under the **FX, Translation & Reporting Mechanics** authority cluster; that vocabulary is **integrated** into the framework pillar, CCY State Chain, CFO decision layer, canonical State 04, primary definition entry, and doctrine pillar so FX mechanics operate as an explicit reference layer—not implicit jargon scattered across ERP commentary.

### Published Terms (Cluster 04)

| Term | Path |
|------|------|
| Remeasurement | `/glossary/remeasurement/` |
| Realized FX | `/glossary/realized-fx/` |
| Unrealized FX | `/glossary/unrealized-fx/` |
| Exchange rate source | `/glossary/exchange-rate-source/` |
| Period-end revaluation | `/glossary/period-end-revaluation/` |
| Translation adjustment | `/glossary/translation-adjustment/` |
| Consolidation adjustment | `/glossary/consolidation-adjustment/` |
| Currency exposure | `/glossary/currency-exposure/` |

### Strategic Meaning

The lexicon now names **operational FX and reporting transformation** in institutional language: how balances **remeasure**, how **realized** versus **unrealized** FX separates settlement economics from mark-to-model drift, why **exchange rate source** and **period-end revaluation** discipline anchor defensible closes, how **translation** and **consolidation adjustments** preserve group reporting integrity, and how **currency exposure** must be read against custody—not headline FX noise. Pillar integration keeps these mechanics adjacent to state progression and monetary-truth custody without converting core pages into glossary inventories.

### Integration Surface (Verified)

| Surface | Path |
|---------|------|
| Framework pillar | `/framework/` |
| State sequence | `/ccy-state-chain/` |
| CFO decision layer | `/cfo-guide/` |
| State 04 | `/states/account-currency/` |
| Definition entry | `/what-is-account-currency/` |
| Doctrine pillar | `/monetary-truth-chain-of-custody/` |

### Custody Consequences Strengthened

- FX revaluation discipline and **remeasurement** logic
- **Realized** versus **unrealized** FX distinction at period boundaries
- **Exchange rate source** governance and **period-end** control
- **Translation adjustment** and **consolidation adjustment** clarity for group reporting paths
- **Currency exposure** interpretation tied to account and consolidation context
- Reinforcement of **reporting integrity** and **audit defensibility** where mechanics meet custody

### Technical State (Verified)

- **Glossary hub:** **32** published defined terms across **five** authority clusters on `/glossary/`.
- **Sitemap:** **47** published URLs after Cluster 04 publication and pillar integration pass.
- **Quality discipline:** sovereign quality gate passed after integration (`scripts/quality_gate.py`).
- **Link safety:** unchanged—`required_links` alignment and published-URL validation during generation.

---

## 2026-05-08 — ERP Ledger Control Layer Integrated

### Decision

**Glossary Cluster 05 — ERP, Ledger & System Control** is **complete** as eight published terms, grouped on `/glossary/` under the **ERP, Ledger & System Control** authority cluster; that vocabulary is **integrated** into the framework pillar, CCY State Chain, CFO decision layer, canonical State 04, primary definition entry, and doctrine pillar so enterprise finance architecture—systems of record, source lineage, ledger accountability, posting mechanics, master data, mapping, and ERP currency configuration—reads as an explicit control layer alongside doctrine and FX mechanics.

### Published Terms (Cluster 05)

| Term | Path |
|------|------|
| System of record | `/glossary/system-of-record/` |
| Source system | `/glossary/source-system/` |
| Subledger | `/glossary/subledger/` |
| General ledger | `/glossary/general-ledger/` |
| Posting logic | `/glossary/posting-logic/` |
| Currency master data | `/glossary/currency-master-data/` |
| Account mapping | `/glossary/account-mapping/` |
| ERP currency configuration | `/glossary/erp-currency-configuration/` |

### Strategic Meaning

The lexicon now names **where monetary truth is instantiated inside applications**: which **source system** captured the obligation, which **system of record** owns replay-grade postings, how **subledger** detail rolls into **general ledger** measurement under governed **posting logic** and **account mapping**, how **currency master data** constrains numeric engines, and how **ERP currency configuration** operationalizes State 04–06 behavior. Integration keeps pillars readable—referencing architecture vocabulary where custody demands system-path reconstruction, not vendor blogging.

### Integration Surface (Verified)

| Surface | Path |
|---------|------|
| Framework pillar | `/framework/` |
| State sequence | `/ccy-state-chain/` |
| CFO decision layer | `/cfo-guide/` |
| State 04 | `/states/account-currency/` |
| Definition entry | `/what-is-account-currency/` |
| Doctrine pillar | `/monetary-truth-chain-of-custody/` |

### System-Control Consequences Strengthened

- **System-of-record** discipline and **source-system** traceability
- **Subledger** to **general ledger** continuity under explicit **posting logic**
- **Currency master data** governance and **account mapping** defensibility
- **ERP currency configuration** alignment with custody and close evidence
- **Monetary reconstruction** across identifiable application paths—not dashboards alone

### Technical State (Verified)

- **Glossary hub:** **40** published defined terms across **six** authority clusters on `/glossary/`.
- **Sitemap:** **55** published URLs after Cluster 05 publication, pillar integration pass, and registry alignment.
- **Quality discipline:** sovereign quality gate passed after integration (`scripts/quality_gate.py`).
- **Link safety:** unchanged—`required_links` alignment and published-URL validation during generation.

---

## 2026-05-08 — Royal Institutional Masthead Adopted

### Decision

AccountCcy.com adopted a responsive royal institutional masthead system.

The masthead now uses a deep royal navy background, the AccountCcy visual mark as the primary identity element, and responsive behavior across desktop, tablet, and mobile screens.

### Strategic Meaning

The masthead establishes the asset’s sovereign visual identity at the top of the interface.

The logo is no longer treated as page imagery inside the hero section. It functions as the official identity mark of the asset.

### Technical Changes

- The hero logo block was removed.
- The masthead now contains the AccountCcy logo image only.
- Legacy masthead CSS conflicts were removed.
- A responsive masthead system was added at the end of `assets/css/main.css`.
- Navigation remains available on larger screens and is hidden on smaller screens to preserve visual discipline.

### Governance Implication

The masthead is now part of the asset’s institutional identity layer and should not be changed casually.

---

## 2026-05-08 — Foundation Publication Cluster 02 (Glossary & CFO Guide)

### Decision

AccountCcy.com published two additional sovereign reference pillars:

- `/glossary/` — a terminology constitution anchoring AccountCcy language (hub page; term URLs staged later).
- `/cfo-guide/` — **The CFO Guide to Hidden Account Currency Risk**, addressing fragmentation of monetary truth across currency states for executive governance audiences.

### Strategic Meaning

Temporary removal of masthead links to unpublished targets was replaced by publishing real pages — not reintroducing broken navigation.

The glossary owns lexical discipline; the CFO guide bridges conceptual doctrine to high-value institutional buyers without reducing content to thin SEO filler.

### Technical Changes

- Added `main/content/pages/glossary.json` and `main/content/pages/cfo-guide.json`.
- Set both URLs to `published` / indexable in `main/data/pages.json` with `required_links` constrained to the published graph only.
- Restored `CFO Guide` and `Glossary` entries in `main/templates/base.html` primary navigation after generation readiness.
- Regenerated HTML outputs, `sitemap.xml`, `robots.txt`, and indexing/schema reports; **sovereign quality gate passed**.

### Governance Implication

Reference navigation must never point to non-existent URLs; expanding the graph requires publishing or withholding links until `link_safety` and strict sitemap audits succeed.

---

## 2026-05-08 — Foundation Publication Cluster 03 (Core CCY State Pages)

### Decision

AccountCcy.com published five sovereign state pages along the CCY State Chain:

- `/states/account-currency/` (State 04 — critical control point)
- `/states/ledger-currency/` (State 05)
- `/states/reporting-currency/` (State 06)
- `/states/consolidation-currency/` (State 07)
- `/states/audit-reality/` (State 08 — terminal custody)

States 01–03 remain text-only in on-page rails until their dedicated pages publish; the hub pillar `/ccy-state-chain/` deep-links to the five published states.

### Strategic Meaning

The asset gains navigable depth beyond pillar summaries — aligning ERP, reporting, consolidation, and audit audiences with custody language grounded in published URLs.

### Technical Changes

- Added JSON corpus files under `main/content/pages/` using the `states__*.json` slug convention consumed by `generate_pages.py`.
- Promoted the five URLs in `main/data/pages.json` with `required_links` constrained to the published graph only.
- Expanded `/ccy-state-chain/` and `/what-is-account-currency/` related-link registries to surface State 04.
- Adjusted `breadcrumb()` in `scripts/generate_pages.py` so intermediate `states/` segments resolve to `/ccy-state-chain/` (avoiding a non-existent `/states/` index).
- Shortened State 04 registry meta description to satisfy SEO length discipline.
- Regenerated HTML, `sitemap.xml`, and reports — **sovereign quality gate passed**.

### Governance Implication

State rails must not hyperlink unpublished targets; expanding the chain requires publishing upstream states or keeping rail entries text-only until URLs exist.

---

## 2026-05-08 — Foundation Publication Cluster 04 (Eight-State Chain Complete)

### Decision

AccountCcy.com published the three upstream CCY State Chain pages so the public reference chain runs continuously from State 01 through State 08:

- `/states/quoted-currency/` (State 01)
- `/states/transaction-currency/` (State 02)
- `/states/settlement-currency/` (State 03)

The hub pillar `/ccy-state-chain/` now requires links to all eight state URLs. Every state content file’s `state_rail` carries working URLs for all eight positions.

### Strategic Meaning

The site exposes a complete, sequenced custody narrative — improving internal linking, glossary alignment, and future diagnostic tooling without fragmenting the chain mid-stream.

### Technical Changes

- Added `states__quoted-currency.json`, `states__transaction-currency.json`, and `states__settlement-currency.json` under `main/content/pages/`.
- Promoted the three registry rows in `main/data/pages.json` to `published` with `required_links` limited to already-published targets (no individual glossary term URLs).
- Expanded `/ccy-state-chain/` `required_links` to enumerate States 01–08; added `/states/settlement-currency/` to State 04’s registry links for upstream continuity.
- Updated `state_rail` entries across all eight state JSON files so earlier positions resolve to live URLs.
- Regenerated HTML, `sitemap.xml`, and reports — **sovereign quality gate passed**.

### Governance Implication

The eight-state chain is now the canonical navigable spine for currency-state doctrine; further clusters (e.g. glossary term pages) must preserve `link_safety` and strict sitemap discipline.

---

## 2026-05-08 — WebP Identity Assets Integrated

### Decision

AccountCcy.com adopted WebP-based identity assets for the public site.

The following assets were added and integrated:

- `assets/icons/favicon.webp`
- `assets/icons/favicon-192.webp`
- `assets/img/logo-accountccy.webp`
- `assets/img/social-preview.webp`
- `assets/img/social-preview-square.webp`

### Strategic Meaning

The asset now has a visual identity layer aligned with the AccountCcy doctrine: monetary truth, chain of custody, control, and audit defensibility.

The logo is treated as a sovereign visual mark, not as decorative branding.

### Technical Changes

- `index.html` now references `favicon.webp` and `social-preview.webp`.
- `main/templates/base.html` now references `favicon.webp` and `social-preview.webp`.
- `assets/css/main.css` now includes hero logo layout rules.
- `validate_assets.py` now validates WebP identity assets.
- `apple-touch-icon` was removed until a dedicated icon file exists.
- generated reports were moved out of `main/data` into `main/reports`.

### Governance Implication

`main/data` remains reserved for governing registries only.

Reports belong in `main/reports`.

Scripts remain executable-only except where root-level documentation is explicitly maintained.

---

## 2026-05-07 — Foundation Doctrine Adopted

### Decision

AccountCcy.com adopted `FOUNDATION_DOCTRINE.md` as the governing constitutional document for the asset.

### Strategic Meaning

The asset is no longer treated as a raw domain, landing page, generic finance website, or speculative domain listing.

It is now governed as a sovereign-grade strategic digital asset built around the thesis:

**AccountCcy.com is the chain of custody for monetary truth inside enterprise finance.**

### Implications

All future architecture, content, design, SEO, monetization, tooling, and acquisition posture must serve this doctrine.

The asset must not be developed as:

- a currency converter
- a forex site
- a generic finance blog
- a domain-for-sale page
- a low-grade SEO property
- a cheap affiliate site

### Next Action

Create the operating governance files required for sovereign-grade development.

---

## 2026-05-07 — Previous Index HTML Rejected as Build Base

### Decision

The earlier `index.html` concept was rejected as the foundation for the final AccountCcy.com build.

### Strategic Meaning

The page contained useful conceptual elements, including:

- currency as state
- CCY State Chain
- account currency as control point
- institutional visual language
- acquisition framing

However, it was not accepted as the final architectural base.

### Implications

The asset will be rebuilt from doctrine, architecture, content governance, and system design rather than from a visual landing page.

The strongest elements may be retained conceptually, but the build must restart from sovereign methodology.

### Next Action

Use the governance files to guide the eventual site architecture and design system.

---

## 2026-05-07 — Supreme Thesis Confirmed

### Decision

The supreme thesis of the asset was confirmed:

**AccountCcy.com is the chain of custody for monetary truth inside enterprise finance.**

### Strategic Meaning

This sentence became the highest conceptual layer of the asset.

It reframes AccountCcy.com from a domain about account currency into a reference system about how monetary movement becomes accounting truth.

### Implications

All future pages, tools, products, design, monetization, SEO, and acquisition posture must be evaluated against this thesis.

### Next Action

Embed this thesis into all governance files, page architecture, public positioning, and quality review.

---

## 2026-05-07 — Conceptual Hierarchy Adopted

### Decision

The asset adopted the following hierarchy:

**Monetary Truth**<br>
↓<br>
**Chain of Custody**<br>
↓<br>
**Currency State Control Framework**<br>
↓<br>
**CCY State Chain**<br>
↓<br>
**Account Currency Control**<br>
↓<br>
**ERP / CFO / Treasury / Reporting / Audit Application**

### Strategic Meaning

This hierarchy defines the order of meaning for the asset.

It prevents the site from becoming merely a glossary, SEO property, ERP guide, or domain landing page.

### Implications

Architecture, content, internal linking, SEO targeting, monetization, and acquisition language must follow this hierarchy.

### Next Action

Use this hierarchy inside all future page briefs and public positioning.

---

## 2026-05-07 — Governance File Set Initiated

### Decision

The AccountCcy.com project initiated the following governance file set:

- `ASSET_THESIS.md`
- `ARCHITECTURE.md`
- `CONTENT_GOVERNANCE.md`
- `SEO_POLICY.md`
- `MONETIZATION_PRINCIPLES.md`
- `ACQUISITION_POSTURE.md`
- `QUALITY_GATE.md`
- `DECISION_LOG.md`

### Strategic Meaning

The asset is being built through governance before design.

This follows the sovereign asset principle that doctrine precedes architecture, architecture precedes content, content precedes design, and design precedes monetization.

### Implications

No final website build should begin until governance files are in place.

### Next Action

Complete governance files, then begin page briefs and build architecture.

---

## 2026-05-07 — Monetization Discipline Adopted

### Decision

AccountCcy.com adopted monetization principles that allow revenue only when it preserves or increases institutional authority.

### Strategic Meaning

The asset may generate income before eventual acquisition, but it must not become a low-trust monetized website.

Revenue is acceptable only if it strengthens the asset as a reference-grade institutional surface.

### Implications

Allowed monetization may include:

- diagnostic reports
- enterprise finance briefings
- professional white papers
- framework licensing
- practitioner subscriptions
- selective institutional partnerships

Prohibited monetization includes:

- display advertising
- generic affiliate offers
- retail forex promotions
- crypto hype
- spam lead generation
- public domain-sale positioning

### Next Action

Develop the Currency State Diagnostic concept after the reference architecture is established.

---

## 2026-05-07 — Acquisition Posture Adopted

### Decision

AccountCcy.com adopted a restrained strategic acquisition posture.

### Strategic Meaning

The asset will not be positioned as a commodity domain sale.

It may only be considered for strategic acquisition by aligned institutional actors.

### Implications

The future buyer is expected to be a strategic institutional actor, potentially from:

- financial close
- consolidation software
- account reconciliation
- ERP platforms
- enterprise accounting
- treasury systems
- CFO advisory
- accounting automation
- professional finance training

The asset should be built so that a future buyer asks:

**What is included in the asset?**

not merely:

**How much for the domain?**

### Next Action

Build visible authority before any outreach or price disclosure.

---

## 2026-05-07 — Quality Gate Adopted

### Decision

AccountCcy.com adopted a sovereign quality gate covering doctrine, concept integrity, institutional seriousness, evidence, content, SEO, design, technical quality, mobile readability, monetization, acquisition, and governance traceability.

### Strategic Meaning

The quality gate protects the asset from dilution, weak content, unsupported claims, poor design, broken implementation, and premature commercialization.

### Implications

No public page, tool, monetization layer, or acquisition posture should be published unless it passes the relevant quality gates.

### Next Action

Use `QUALITY_GATE.md` as the review standard before publishing any future page.

---

## 2026-05-07 — Logo Concept Classified as Draft Identity Direction

### Decision

The current AccountCcy logo concept was classified as a draft identity direction, not a final sovereign mark.

### Strategic Meaning

The logo contains useful conceptual symbols:

- chain for custody
- shield for audit defensibility
- institutional mark structure
- blue and gold financial seriousness

However, the final identity should be more restrained, more geometric, more system-oriented, and more institutionally refined.

### Implications

The logo may be stored as a concept asset, but should not yet be treated as final.

Suggested file naming:

`assets/img/accountccy-logo-concept.png`

not:

`assets/img/logo-final.png`

### Next Action

Develop final visual identity after design doctrine and site architecture are stabilized.

---

## 2026-05-07 — No Final Build Before Page Briefs

### Decision

The project will not proceed directly into full website code after governance.

### Strategic Meaning

A sovereign-grade asset requires page briefs before final implementation.

Each page must have:

- purpose
- thesis
- audience
- SEO intent
- relationship to doctrine
- internal links
- content requirements
- evidence discipline
- quality gate expectations

### Implications

The next phase after governance is Page Briefs, not final HTML.

### Next Action

Create page briefs for the initial sovereign build, starting with Homepage, Chain of Custody, Framework, CCY State Chain, and What Is Account Currency.

---

## Additional Operating Rule — Governed Build Logging

Every substantive governed build change must be recorded in this file before the phase is considered complete.

This includes page publication, template changes, diagnostic behavior, ontology changes, evidence maps, control artifacts, sitemap/indexing changes, monetization posture, acquisition posture, quality-gate decisions, security decisions, link-safety decisions, and any detail that affects the asset's meaning, structure, public surface, or future buyer interpretation.

Typographical noise does not need a separate entry. Any change that affects meaning, structure, behavior, publication status, SEO surface, buyer logic, governance, or technical trust must be logged.

---

## 2026-06-23 — Asset Intelligence Factory Plan, Diagnostic, and Acquisition Posture Published

### Decision

Published the first AccountCcy.com Category Intelligence Factory layer.

The phase added or changed:

- `ASSET_INTELLIGENCE_FACTORY_PLAN.md`
- `/currency-state-diagnostic/`
- `/acquisition/`
- `main/content/pages/currency-state-diagnostic.json`
- `main/content/pages/acquisition.json`
- `main/data/pages.json`
- `main/data/tools.json`
- `scripts/generate_pages.py`
- `assets/css/main.css`
- `sitemap.xml`
- indexing and schema reports

### Strategic Meaning

The asset moved from reference surface toward governed category infrastructure.

The Currency State Diagnostic creates practical output from the thesis. The Strategic Acquisition Posture frames AccountCcy.com as a governed reference asset, not commodity domain inventory. The Asset Intelligence Factory Plan defines the operating model for domain thesis, category language, ontology, standard, protocol, engine, reference layer, governance, interface thesis, monetization, and buyer logic.

### Technical and Governance Details

The diagnostic was implemented as a local-first browser assessment:

- no POST form
- no external data collection endpoint
- no certification claim
- no accounting, audit, tax, legal, treasury, investment, or ERP implementation advice
- explicit non-advisory disclaimer

The generator was extended so diagnostic questions are structured data rather than hand-authored HTML.

The acquisition page was published with restrained language:

- no price
- no urgency
- no marketplace framing
- no domain-sale posture
- institutional inquiry only

### Validation

Sovereign build and quality gate passed after publication:

- content validation errors: 0
- asset validation errors: 0
- SEO validation errors: 0
- link validation errors: 0
- schema errors: 0
- sitemap errors: 0
- sitemap warnings: 0

### Next Action

Deepen the ontology and make the diagnostic report path more credible without weakening professional trust.

---

## 2026-06-23 — Ontology, Evidence Maps, Diagnostic Output, Homepage, and Reference Expansion Published

### Decision

Published the second governed Category Intelligence Factory expansion.

The phase added or changed:

- evidence maps for all eight Currency State pages
- control artifacts for all eight Currency State pages
- deeper diagnostic output showing overall maturity, weakest custody area, and strongest custody area
- `main/templates/state_page.html`
- `main/templates/homepage.html`
- `main/content/pages/homepage.json`
- `scripts/generate_pages.py`
- `assets/css/main.css`
- five new high-quality reference pages:
  - `/account-currency-in-erp/`
  - `/functional-currency-explained/`
  - `/revaluation-and-translation/`
  - `/risks/account-currency-misconfiguration/`
  - `/compare/account-currency-vs-reporting-currency/`
- corresponding content JSON files
- registry publication status for the five pages
- sitemap, indexing report, and schema report

### Strategic Meaning

The ontology now has reviewable evidence depth. Each state is no longer only a conceptual description; it has artifacts, owners, and proof expectations.

The diagnostic now produces a more buyer-relevant output because it identifies maturity and custody weak spots. The homepage now presents the asset as a Category Intelligence Factory with direct pathways into framework, state chain, diagnostic, and acquisition posture.

The five new reference pages strengthen professional SEO while staying inside the AccountCcy thesis:

- ERP account currency control
- functional currency boundaries
- revaluation versus translation
- account currency misconfiguration risk
- account currency versus reporting currency

### Technical and Governance Details

The generator was extended to support:

- `evidence_map`
- `control_artifacts`
- local diagnostic detail output
- breadcrumb behavior that avoids broken intermediate links for `/risks/` and `/compare/`

The homepage was moved into governed JSON content so future builds do not preserve stale hand-authored HTML.

Published page descriptions were shortened to satisfy SEO warning thresholds.

No new external scripts, data collection endpoints, third-party tracking, POST forms, or professional-advice claims were introduced.

### Validation

Sovereign build and quality gate passed after publication:

- generated sitemap URLs: 80
- content validation errors: 0
- asset validation errors: 0
- SEO validation errors: 0
- link validation errors: 0
- schema errors: 0
- sitemap errors: 0
- sitemap warnings: 0

### Next Action

Future monetization should focus on a governed diagnostic report layer, with explicit evidence maps, non-advisory boundaries, and high-trust report language before any paid workflow is exposed publicly.

---

## 2026-06-23 — Decision Log Discipline Tightened

### Decision

AccountCcy.com will treat `DECISION_LOG.md` as the mandatory record for every substantive governed build change.

### Strategic Meaning

The asset is being developed as category infrastructure, not a casual website. A strict decision record protects institutional memory, prevents hidden drift, and gives a future strategic buyer a clear trail of why the asset evolved as it did.

### Implications

Every future governed implementation phase must log:

- published or unpublished pages
- template and renderer changes
- diagnostic logic changes
- ontology, evidence-map, or control-artifact changes
- sitemap and indexing changes
- monetization or acquisition posture changes
- validation results
- security, link-safety, or technical-quality decisions

Minor copy spelling fixes may remain outside the log, but any change that alters meaning, structure, behavior, publication status, SEO surface, buyer logic, or governance must be recorded.

### Next Action

Before final delivery of each build phase, update this file with the changes made and the validation result.

---

## 2026-06-23 — Trust Hardening Sprint Started

### Decision

Started a trust-hardening phase and paused broad public page expansion.

This phase added:

- `METHODOLOGY.md`
- `SOURCE_BOUNDARY_POLICY.md`
- `CLAIM_BOUNDARY_MATRIX.md`
- `FRAMEWORK_VERSIONING.md`
- `PUBLIC_CHANGELOG.md`
- `EXTERNAL_EVIDENCE_REGISTRY.md`

It also updated:

- `ASSET_INTELLIGENCE_FACTORY_PLAN.md`

### Strategic Meaning

AccountCcy.com already has a strong internal reference system, but market inevitability requires trust layers beyond page count.

The purpose of this sprint is to prevent the asset from looking like fast content expansion and to make its governance harder to imitate. The asset now has explicit methodology, source boundaries, claim boundaries, versioning discipline, public changelog discipline, and a registry for verified external evidence.

### Implications

No new comparison cluster or broad SEO expansion should be added before this trust layer is stable.

Future authority should be built through:

- source discipline
- methodology clarity
- framework versioning
- claim restraint
- verified external evidence
- diagnostic usage signals
- qualified professional references

### Technical and Governance Details

The trust-hardening files are governance files, not new public HTML pages.

They do not increase sitemap URL count and do not add public routes.

The external evidence registry starts empty by design. AccountCcy.com should not claim external authority before external authority exists.

### Validation

Sovereign quality gate must be run after this entry.

Expected technical impact:

- no new indexable URLs
- no new external scripts
- no data collection endpoints
- no professional-advice expansion
- no acquisition language escalation

### Next Action

Run the quality gate and keep the next build phase focused on trust signals rather than page volume.

---

## 2026-06-23 - Public Methodology Surface Published

### Decision

Published `/methodology/` as the single public methodology surface for AccountCcy.com.

The page explains how the framework is governed, what it covers, what it does not claim, how source boundaries are handled, and how publication discipline is maintained.

### Strategic Meaning

This creates a public trust layer without exposing raw internal governance files.

The methodology surface strengthens credibility for buyers, advisors, auditors, ERP vendors, financial close platforms, and acquisition reviewers by showing that AccountCcy.com is governed by a disciplined framework rather than loose content expansion.

### Technical Changes

- Confirmed `main/content/pages/methodology.json` as the public methodology content source.
- Registered `/methodology/` as a published, indexable page in `main/data/pages.json`.
- Added targeted inbound methodology links from `/`, `/framework/`, `/monetary-truth-chain-of-custody/`, `/glossary/`, `/cfo-guide/`, and `/acquisition/`.
- Kept the methodology page connected to `/currency-state-diagnostic/` and `/acquisition/` because both routes are currently published.
- Shortened two existing meta descriptions that blocked a warning-free strict sitemap run.
- Regenerated HTML, sitemap, robots output, and indexing reports.

### Governance Implication

Future public expansion should remain consistent with the methodology page, source boundary policy, claim boundary discipline, versioning discipline, and quality gate requirements.

No unsupported market claim, vendor advice, accounting advice, or external validation claim should be added unless it is supported by the governance artifacts and evidence registry.

### Validation

Executed:

- `py scripts\generate_pages.py --root . --overwrite`
- `py scripts\generate_sitemap.py --root . --write-robots --strict --report`
- `py scripts\quality_gate.py --root .`

Results:

- sitemap URL count: 81
- sitemap errors: 0
- sitemap warnings: 0
- sovereign quality gate: passed

Suggested commit message:

`feat(site): publish public methodology trust surface`

---

## 2026-06-23 - SEO Strengthening Sprint for Existing Comparison Pages

### Decision

Strengthened the existing comparison-page set for professional search intent without creating a new comparison cluster or adding a new URL.

The sprint covered:

- `/account-currency-vs-transaction-currency/`
- `/account-currency-vs-settlement-currency/`
- `/account-currency-vs-ledger-currency/`
- `/functional-currency-vs-reporting-currency/`
- `/ledger-currency-vs-reporting-currency/`
- `/reporting-currency-vs-consolidation-currency/`
- `/compare/account-currency-vs-reporting-currency/`

### Strategic Meaning

The comparison pages now answer high-intent professional searches more directly while preserving AccountCcy.com's framework discipline.

The sprint strengthens discoverability, comprehension, and internal trust flow without diluting the site through broad page-volume expansion.

### Technical Changes

- Reworked each targeted comparison page opening around clear search intent.
- Added a one-sentence governing distinction to each page.
- Added structured side-by-side comparison sections.
- Added explicit currency-state positioning for each compared concept.
- Added ERP, close, reconciliation, and reporting consequence sections.
- Added risk-boundary sections explaining where confusion creates control risk.
- Added custody questions for each concept.
- Added related glossary links, related state links, and a controlled `/methodology/` trust-boundary link.
- Added FAQ-style question sections inside the existing reference-page rendering model.
- Updated `main/data/pages.json` so the targeted comparison pages include `/methodology/` as a required trust-boundary link.

### Governance Implication

No new page was created during this sprint.

The optional `/account-currency-vs-functional-currency/` page was intentionally not created because the existing comparison set could be strengthened first.

The added content remains reference and educational framework material only. It does not claim official standard status and does not provide accounting, audit, tax, legal, treasury, investment, or ERP implementation advice.

### Validation

Executed:

- `py scripts\generate_pages.py --root . --dry-run`
- `py scripts\generate_pages.py --root . --overwrite`
- `py scripts\generate_sitemap.py --root . --write-robots --strict --report`
- `py scripts\quality_gate.py --root .`

Results:

- sitemap URL count: 81
- sitemap errors: 0
- sitemap warnings: 0
- content validation errors: 0
- asset validation errors: 0
- SEO validation errors: 0
- link validation errors: 0
- schema errors: 0
- sovereign quality gate: passed

Suggested commit message:

`feat(seo): strengthen comparison pages for professional search intent`

---

## 2026-06-23 - Strategic Narrative Elevation Sprint

### Decision

Elevated the core AccountCcy.com narrative across existing public surfaces without creating new URLs or expanding the sitemap.

Updated surfaces:

- `/`
- `/monetary-truth-chain-of-custody/`
- `/framework/`
- `/acquisition/`
- `/methodology/`

### Strategic Meaning

The public story now centers more directly on monetary truth custody:

> In enterprise finance, money does not become truth when it moves. It becomes truth when its currency state can be traced, controlled, reconciled, reported, consolidated, and defended.

The homepage now presents the big story in the first screen, frames the eight currency states as a narrative custody chain, and distinguishes AccountCcy from currency conversion. The doctrine page has been strengthened as the philosophical anchor. The framework page connects the thesis to bounded control architecture across ERP, accounts, ledger, reporting, consolidation, and audit evidence. The acquisition page speaks more clearly to strategic buyers while preserving restrained institutional posture.

### Governance Implication

No new URLs were created.

No vendor-specific targeting, public comparison narratives, market leadership claims, official-standard language, price anchoring, urgency language, or professional advice language was introduced.

The methodology page remains a trust layer and includes only a light thesis-binding sentence.

Suggested commit message:

`feat(strategy): elevate monetary truth custody narrative`

---

## Future Decisions

Future entries should record major decisions related to:

- site architecture
- design system
- content publication
- diagnostic tool
- monetization launch
- acquisition posture
- outreach readiness
- SEO expansion
- framework licensing
- public positioning
- technical implementation
- validation scripts
- visual identity
- page publication
