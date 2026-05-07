# AccountCcy.com UI Components

## Document Status

This document defines the interface component system for AccountCcy.com.

It translates the `FOUNDATION_DOCTRINE.md`, `ASSET_THESIS.md`, `ARCHITECTURE.md`, `CONTENT_GOVERNANCE.md`, `SEO_POLICY.md`, and `DESIGN_SYSTEM.md` into reusable UI structures.

This is not a generic component library.

This is the visual operating system for a sovereign-grade reference asset whose supreme thesis is:

**AccountCcy.com is the chain of custody for monetary truth inside enterprise finance.**

Every component must strengthen that thesis.

No component may exist merely because it is common in modern websites.

Every component must serve meaning, hierarchy, authority, clarity, trust, usability, SEO, or future acquisition value.

---

## 1. Component System Thesis

The AccountCcy.com component system exists to make the asset's conceptual architecture visible and usable.

The interface must not behave like a standard SaaS landing page, a finance blog, a forex site, a crypto page, or a domain sales page.

It must behave like:

- a governed reference institution
- a financial archive
- a ledger doctrine
- a custody map
- a state-control framework
- an enterprise finance reference surface

The components must help users understand how currency moves from market price to accounting truth through custody, state, control, reporting, consolidation, and audit defensibility.

---

## 2. Component Design Principles

All components must follow these principles.

### 2.1 Meaning Before Decoration

A component must express or support a real conceptual function.

Decorative visual blocks are not allowed unless they reinforce custody, ledger, state, audit, reference, or institutional authority.

### 2.2 Restraint Before Noise

Components must be visually calm, structured, and readable.

The asset must not feel busy, promotional, or cluttered.

### 2.3 Hierarchy Before Symmetry

The interface should not force equal visual weight on unequal ideas.

Account Currency, the control point, must receive stronger visual emphasis than surrounding states.

Monetary Truth and Chain of Custody must sit above generic terminology.

### 2.4 Reference Before Conversion

Components must support reference behavior: reading, comparing, defining, tracing, and understanding.

They must not imitate sales-funnel templates unless the component is specifically part of the restrained acquisition layer.

### 2.5 Mobile Authority

Every component must remain institutionally credible on mobile.

No core conceptual component may disappear on mobile.

The Custody Rail, CCY State Chain, and Control Point Panel must become compact, not hidden.

---

## 3. Component Naming Rules

Component names should be conceptual and functional.

Preferred names:

- Custody Rail
- State Card
- Control Point Panel
- Doctrine Block
- Evidence Panel
- Definition Box
- Risk Note
- Audit Reality Badge
- Comparison Matrix
- Diagnostic Maturity Card
- Acquisition Callout

Avoid generic names unless necessary:

- feature box
- card group
- marketing block
- pricing section
- hero widget
- banner ad

The naming system should remind future builders that every UI block belongs to the doctrine.

---

## 4. Visual Token Dependency

All components must use the Custody Archive Palette established in `DESIGN_SYSTEM.md`.

Primary tokens:

- `--color-ink`
- `--color-paper`
- `--color-cream`
- `--color-gold`
- `--color-gold-light`
- `--color-gold-pale`
- `--color-slate`
- `--color-slate-mid`
- `--color-rule`
- `--color-accent-red`
- `--color-verified`

Typography tokens:

- `--font-heading`
- `--font-body`
- `--font-mono`

Spacing, border, and layout tokens should be defined in `assets/css/main.css` before component styles are written.

No component should hard-code colors unless the token does not yet exist and has been approved for addition.

---

## 5. Core Layout Components

### 5.1 Sovereign Masthead

Purpose:

The masthead establishes institutional identity and helps users navigate the reference system.

It must not look like a startup navbar or a domain sales header.

Required elements:

- AccountCcy.com wordmark
- restrained navigation
- no aggressive CTA
- subtle rule line
- high readability
- sticky behavior optional but restrained

Recommended navigation items:

- Doctrine
- Framework
- State Chain
- Account Currency
- CFO Guide
- Glossary
- Diagnostic

Acquisition may appear only as a restrained text link or footer link during early build.

Avoid:

- bright buttons in the masthead
- large sales CTAs
- dropdown clutter
- generic SaaS navigation language
- domain marketplace language

Mobile behavior:

The masthead should collapse cleanly.

If a mobile menu is used, it must remain simple and text-first.

No conceptual navigation should become inaccessible on mobile.

---

### 5.2 Sovereign Footer

Purpose:

The footer closes the page with institutional restraint and reinforces the asset identity.

Required elements:

- AccountCcy.com identity line
- governing thesis or short descriptor
- key page links
- disclaimer link if available
- contact or acquisition inquiry link if appropriate

Recommended footer identity:

**AccountCcy.com — The chain of custody for monetary truth inside enterprise finance.**

Avoid:

- large promotional badges
- social clutter
- domain-for-sale wording
- excessive legal noise
- irrelevant links

---

### 5.3 Page Shell

Purpose:

The page shell provides consistent spacing, width, typography, and section rhythm across all pages.

Rules:

- content must be readable on mobile
- sections must have strong vertical breathing room
- maximum text width must be controlled
- long pages should use clear section anchors
- reference pages should feel like documents, not marketing funnels

Recommended structure:

- masthead
- page hero
- body sections
- related reference links
- restrained footer

---

## 6. Hero Components

### 6.1 Supreme Thesis Hero

Purpose:

The homepage hero introduces the highest thesis of the asset.

It must immediately separate AccountCcy.com from ordinary finance websites.

Primary message:

**The Chain of Custody for Monetary Truth Inside Enterprise Finance**

Supporting message:

Currency does not become truth when it moves. It becomes truth when it is recorded, assigned, reconciled, translated, consolidated, and defended.

Required elements:

- eyebrow label
- H1 thesis
- short explanatory paragraph
- custody-oriented visual or rail
- restrained primary action
- restrained secondary action

Preferred CTAs:

- Explore the Framework
- Trace the State Chain
- Read the Doctrine

Avoid:

- Buy Now
- Make Offer
- Get Started Today
- generic SaaS conversion language
- hype-driven taglines

---

### 6.2 Reference Page Hero

Purpose:

The reference page hero introduces a specific concept without overwhelming the user.

Required elements:

- page category label
- clear H1
- concise thesis paragraph
- optional relationship to CCY State Chain
- optional breadcrumb

Example page categories:

- Doctrine
- Framework
- State Chain
- Definition
- Comparison
- ERP Application
- CFO Guide
- Glossary

---

### 6.3 Acquisition Page Hero

Purpose:

The acquisition page hero communicates selectivity and seriousness.

It must not sound like a domain sale.

Preferred message:

Strategic acquisition may be considered only where institutional alignment exists.

Required tone:

- restrained
- serious
- selective
- non-desperate
- non-promotional

Avoid:

- public pricing
- discount language
- aggressive inquiry language
- domain marketplace phrasing

---

## 7. Doctrine Components

### 7.1 Doctrine Block

Purpose:

A Doctrine Block presents a central principle that governs the asset.

Use cases:

- homepage doctrine statement
- framework page opening
- Chain of Custody page
- acquisition page positioning

Visual behavior:

- strong contrast
- deep ink background or paper surface with gold rule
- concise text
- serif emphasis
- restrained attribution line

Content rules:

Doctrine Blocks should be short, memorable, and defensible.

Example:

**Money does not become accounting truth automatically. It becomes truth through custody.**

Avoid:

- long paragraphs
- hype claims
- decorative quotes without strategic meaning

---

### 7.2 Monetary Truth Statement

Purpose:

A short statement that connects a section back to the supreme thesis.

Use cases:

- section openings
- interstitial breaks
- page summaries

Example:

**Before money becomes a number, it must pass through custody.**

Visual behavior:

- centered or left-aligned
- generous spacing
- strong typographic hierarchy
- no excessive ornament

---

### 7.3 Benchmark Principle Panel

Purpose:

A panel that explains why the asset is not built for ordinary domain resale logic.

Use sparingly.

Best location:

- acquisition page
- internal about or doctrine page

Tone:

Institutional, not boastful.

The panel must express constructed value, not hype.

---

## 8. Custody and State Components

### 8.1 Custody Rail

Purpose:

The Custody Rail is one of the most important visual components of AccountCcy.com.

It shows the passage from market price to audit reality.

States:

1. Quoted Currency
2. Transaction Currency
3. Settlement Currency
4. Account Currency
5. Ledger Currency
6. Reporting Currency
7. Consolidation Currency
8. Audit Reality

Visual behavior:

- horizontal on desktop when space allows
- vertical or stepped on mobile
- Account Currency must be emphasized as the control point
- Audit Reality should feel like the defended terminal state
- gold should highlight control, not decorate every state

Required labels:

- state number
- state name
- short state meaning

Mobile rule:

The Custody Rail must not be hidden on mobile.

It may become a vertical rail, accordion, or compact state list.

---

### 8.2 State Card

Purpose:

A State Card explains one state in the CCY State Chain.

Required elements:

- state number
- state name
- role label
- concise definition
- consequence if misunderstood
- link to full state detail if available

State Card types:

- standard state
- control point state
- terminal audit state
- risk state

Visual distinction:

- standard states use paper or cream surfaces
- Account Currency uses gold accent or ink surface
- Audit Reality may use verified green accent subtly
- risk-related states may use restrained red only when necessary

---

### 8.3 Control Point Panel

Purpose:

This component highlights Account Currency as the critical inflection point.

It is central to the asset.

Required message:

Account Currency is where external monetary movement enters accounting custody.

Required elements:

- strong heading
- control-point explanation
- relationship to previous states
- relationship to downstream states
- gold rule or gold border
- optional shield or custody mark

Use cases:

- homepage
- framework page
- what-is-account-currency page
- CCY State Chain page
- CFO guide

Avoid:

- making the component look like a pricing card
- overusing icons
- making it feel like cybersecurity rather than accounting control

---

### 8.4 Audit Reality Badge

Purpose:

A compact badge that indicates defensible accounting truth.

Use cases:

- diagnostic results
- state cards
- maturity levels
- evidence panels
- CFO guide

Visual behavior:

- restrained verified green or gold
- small, serious, non-gamified
- should not look like a consumer achievement badge

Recommended labels:

- Audit-Defensible
- Reconciled
- Controlled
- Verified State

---

## 9. Reference Components

### 9.1 Definition Box

Purpose:

A Definition Box provides concise professional definitions.

Required elements:

- term
- definition
- role inside the framework
- related terms

Example:

Term: Account Currency

Definition: The currency assigned to an account for recording, maintaining, reconciling, and controlling financial balances inside an accounting or ERP system.

Framework role: State 04 — Control Point.

Visual behavior:

- paper or cream background
- left rule line
- clear term typography
- optional mono label

---

### 9.2 Comparison Matrix

Purpose:

A Comparison Matrix clarifies differences between related currency identities.

Use cases:

- transaction vs account vs reporting currency
- functional vs reporting vs presentation currency
- settlement vs transaction currency

Required rows:

- concept
- where it appears
- what it controls
- risk if confused
- relationship to CCY State Chain

Mobile behavior:

Tables must not break mobile readability.

On mobile, matrices may become stacked comparison cards.

---

### 9.3 Glossary Entry Card

Purpose:

A glossary entry component defines terms while linking them back to the asset framework.

Required elements:

- term
- concise definition
- category
- related states
- related terms
- link to deeper page if available

Glossary entries must not be thin.

Each entry should reinforce AccountCcy.com’s topical authority.

---

### 9.4 Evidence Panel

Purpose:

An Evidence Panel grounds the asset’s original concepts in real institutional context.

Use cases:

- framework page
- ERP page
- functional currency page
- revaluation and translation page

Required behavior:

- distinguish original framework from established terminology
- avoid vendor affiliation implications
- use careful wording
- cite or reference only credible sources when public citations are added

Visual behavior:

- quiet border
- slate text
- no exaggerated proof language

---

### 9.5 Reference Note

Purpose:

A small note that clarifies scope, limitations, or interpretive context.

Use cases:

- legal/accounting disclaimer
- vendor neutrality note
- framework originality note
- educational scope note

Example:

AccountCcy.com provides reference and framework materials. It does not provide accounting, audit, tax, legal, investment, or ERP implementation advice.

---

## 10. Risk and Control Components

### 10.1 Risk Note

Purpose:

A Risk Note explains what may go wrong if a currency identity or state is misunderstood.

Use cases:

- CFO guide
- ERP page
- comparison pages
- revaluation and translation page

Visual behavior:

- restrained red accent
- no alarmist language
- concise professional warning

Avoid:

- fearmongering
- exaggerated risk claims
- compliance panic language

---

### 10.2 Control Note

Purpose:

A Control Note explains how a concept can be governed or clarified.

Visual behavior:

- gold or verified green accent
- structured language
- professional calm

Use cases:

- diagnostic tool
- CFO guide
- framework page
- account currency page

---

### 10.3 Audit Trail Panel

Purpose:

A panel that explains how monetary records become defensible.

Use cases:

- Audit Reality state
- Chain of Custody page
- CFO guide
- diagnostic results

Required language:

- reconciliation
- documentation
- traceability
- defensibility
- review
- audit reality

Avoid:

- legalistic overclaiming
- implying certification

---

## 11. Diagnostic Components

### 11.1 Diagnostic Intro Panel

Purpose:

Introduces the Currency State Diagnostic.

Required message:

The diagnostic assesses maturity across the chain of custody for monetary truth.

Must include disclaimer that the diagnostic is reference-oriented and not professional advice.

---

### 11.2 Diagnostic Question Block

Purpose:

Displays one maturity question.

Required elements:

- question
- state relationship
- answer options
- explanatory help text

Answer options should be professional and restrained.

Avoid gamified language.

---

### 11.3 Maturity Level Card

Purpose:

Displays a maturity level.

Levels:

- Fragmented
- Configured
- Governed
- Controlled
- Audit-Defensible

Visual behavior:

- clear hierarchy
- restrained color
- no consumer-style badges
- professional interpretation

---

### 11.4 Premium Report Callout

Purpose:

Offers a paid diagnostic report after free diagnostic output.

Tone:

Professional, not aggressive.

Allowed language:

- Request the full diagnostic interpretation
- Generate a professional maturity report
- Download the Account Currency Control report

Avoid:

- countdown timers
- exaggerated promises
- cheap pricing emphasis
- “limited time” language

---

## 12. Commercial and Acquisition Components

### 12.1 Strategic Acquisition Callout

Purpose:

A restrained callout indicating that strategic acquisition may be considered.

Use cases:

- homepage footer area
- acquisition page
- about/doctrine page

Required tone:

- selective
- institutional
- quiet
- aligned only

Recommended message:

Strategic acquisition may be considered only where institutional alignment exists across enterprise finance, ERP architecture, financial close, treasury infrastructure, or accounting automation.

Avoid:

- Make Offer
- Buy This Domain
- Premium Domain For Sale
- urgent sales language
- public price language

---

### 12.2 Inquiry Panel

Purpose:

Allows qualified institutional inquiry.

Fields may include:

- name
- organization
- professional email
- area of interest
- acquisition, licensing, partnership, or briefing interest
- message

Required behavior:

- no aggressive sales framing
- no public price anchor
- no low-trust lead funnel behavior

---

### 12.3 Premium Brief Card

Purpose:

Presents a professional paid briefing or white paper.

Required elements:

- title
- short description
- intended audience
- what it covers
- price if public
- disclaimer where necessary

Visual behavior:

- document-like
- not e-commerce flashy
- no discount framing

---

### 12.4 Framework Licensing Panel

Purpose:

Explains that the framework may later be licensed for professional use.

Use cases:

- monetization page
- acquisition page
- professional access page

Tone:

Serious, selective, rights-aware.

---

## 13. Navigation and Wayfinding Components

### 13.1 Breadcrumb Trail

Purpose:

Helps users understand where they are inside the reference system.

Example:

Home → Framework → CCY State Chain → Account Currency

Visual behavior:

- small mono or subdued text
- high readability
- no clutter

---

### 13.2 Related Concepts Block

Purpose:

Encourages conceptual navigation between related terms and pages.

Required elements:

- heading
- 3 to 6 related links
- brief context if useful

Use cases:

- glossary pages
- definitions
- comparison pages
- ERP application pages

---

### 13.3 Next Reference Step

Purpose:

Guides users to the next logical page.

Example:

After reading What Is Account Currency, send users to Transaction Currency vs Account Currency vs Reporting Currency or the CCY State Chain.

Tone:

Reference-oriented, not funnel-driven.

---

## 14. Typography Components

### 14.1 Eyebrow Label

Purpose:

Signals section category.

Style:

- mono font
- uppercase
- tracked letter spacing
- muted gold or slate

Examples:

- Doctrine
- Framework
- State 04
- Control Point
- CFO Guide
- Evidence Discipline

---

### 14.2 Section Header

Purpose:

Introduces major sections with clear hierarchy.

Required elements:

- eyebrow label optional
- strong heading
- explanatory paragraph optional

Rule:

Headings must be meaningful, not decorative.

---

### 14.3 Pull Principle

Purpose:

Highlights a governing principle.

Visual behavior:

- large serif type
- restrained width
- gold rule or ink background

Use sparingly.

---

## 15. Button and Link Components

### 15.1 Primary Button

Purpose:

Leads to core reference actions.

Allowed labels:

- Explore the Framework
- Trace the State Chain
- Read the Doctrine
- Open the Glossary
- Start Diagnostic

Avoid:

- Buy Now
- Get Rich
- Claim Offer
- Make Offer
- Limited Time

---

### 15.2 Secondary Button

Purpose:

Supports lower-priority navigation.

Allowed labels:

- Read the CFO Guide
- Compare Currency Roles
- View Related Terms
- Learn Account Currency

---

### 15.3 Text Link

Purpose:

Used for reference navigation.

Rules:

- links must be descriptive
- no vague “click here”
- no unnecessary link styling
- visited/focus states must remain readable

---

## 16. Tables and Structured Data Components

### 16.1 Reference Table

Purpose:

Displays structured comparisons or definitions.

Rules:

- must be readable on mobile
- should not exceed practical column count
- use stacked mobile fallback where necessary
- no dense spreadsheet-like walls unless needed

---

### 16.2 State Transition Table

Purpose:

Shows how one currency state transitions into the next.

Columns may include:

- From State
- To State
- What Changes
- Risk
- Control Question

Use on framework and CCY State Chain pages.

---

### 16.3 Diagnostic Scoring Table

Purpose:

Shows maturity scoring logic.

Must remain clear, professional, and non-gamified.

---

## 17. Visual Asset Components

### 17.1 Logo Mark

Purpose:

Represents the institutional identity of the asset.

The logo may use symbols of custody, chain, shield, ledger, or audit defensibility.

Rules:

- must remain restrained
- must not feel cartoonish
- must not over-index on cybersecurity
- should support enterprise finance and audit meaning

Current logo concept may be treated as draft identity direction, not final sovereign mark.

Recommended naming for draft:

`assets/img/accountccy-logo-concept.png`

Final mark should not be named `logo-final` until formally approved.

---

### 17.2 Framework Diagram

Purpose:

Visualizes the Currency State Control Framework.

Must prioritize clarity over decoration.

Should show:

- states
- transitions
- control point
- audit destination

---

### 17.3 Social Preview Graphic

Purpose:

Provides a high-quality Open Graph and social sharing visual.

Must include:

- AccountCcy.com
- chain of custody thesis or shorter phrase
- restrained palette
- no cheap promotional language

---

## 18. Accessibility Rules

All components must meet basic accessibility expectations.

Rules:

- text must have sufficient contrast
- interactive elements must have focus states
- buttons and links must be keyboard accessible
- decorative graphics must not block reading
- icons must not carry meaning without text
- mobile touch targets must be usable
- text must remain readable without zooming

No component may sacrifice accessibility for visual drama.

---

## 19. Responsive Rules

Core conceptual components must adapt rather than disappear.

Never hide these completely on mobile:

- Custody Rail
- Control Point Panel
- CCY State Chain summary
- Doctrine Block
- primary reference navigation

Mobile behavior should prefer:

- vertical stacking
- compact cards
- accordions for long state descriptions
- simplified grids
- readable spacing

Avoid:

- horizontal overflow
- tiny tables
- hidden conceptual visuals
- dense multi-column layouts

---

## 20. Prohibited Components

The following components are prohibited unless a future governance decision explicitly approves them:

- countdown timers
- discount banners
- floating sales popups
- ad banners
- forex widgets
- crypto tickers
- aggressive lead magnets
- domain-for-sale cards
- fake urgency bars
- testimonial carousels without substance
- cluttered SaaS feature grids
- stock market chart decorations unrelated to the doctrine
- generic pricing tables before monetization readiness

If a component makes AccountCcy.com feel cheaper, it must not be used.

---

## 21. Component Quality Gate

Before adding a component, ask:

**Does this component strengthen AccountCcy.com as the chain of custody for monetary truth inside enterprise finance?**

If yes, it may proceed.

If no, it must be rejected.

If uncertain, test the component against:

- doctrine alignment
- conceptual clarity
- institutional seriousness
- mobile readability
- accessibility
- SEO usefulness
- acquisition compatibility
- monetization discipline

---

## 22. Initial Component Build List

The first implementation should prioritize these components:

1. Sovereign Masthead
2. Supreme Thesis Hero
3. Custody Rail
4. Control Point Panel
5. Doctrine Block
6. State Card
7. Evidence Panel
8. Definition Box
9. Comparison Matrix
10. Risk Note
11. Related Concepts Block
12. Strategic Acquisition Callout
13. Sovereign Footer

No secondary or commercial component should be built before these are stable.

---

## Final Operating Principle

The AccountCcy.com component system is not a collection of reusable decorations.

It is the interface expression of the asset’s doctrine.

Every component must make the site more precise, more serious, more useful, more authoritative, and more difficult for the right institutional buyer to dismiss.

This is the standard.

This is the component discipline.

This is the line that must not be broken.
