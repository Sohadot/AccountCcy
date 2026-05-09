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
