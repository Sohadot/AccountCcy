# AccountCcy.com Sovereign Indexing System

## Purpose

This is not a basic sitemap generator.

It is a **Sovereign Indexing Gate** for AccountCcy.com.

It generates `sitemap.xml` and audits whether public pages are safe, canonical, indexable, internally coherent, and technically ready for search engines.

## Critical note

The correct sitemap file is:

`sitemap.xml`

not:

`Sitemap.xls`

`.xls` is an Excel spreadsheet format. Search engines read XML sitemap files.

## Files

Place the script here:

`scripts/generate_sitemap.py`

## Core command

```bash
python scripts/generate_sitemap.py --strict --report
```

## Recommended command before every commit

```bash
python scripts/generate_sitemap.py --strict --fail-on-warnings --report
```

## Create or update robots.txt

```bash
python scripts/generate_sitemap.py --write-robots --strict --report
```

## What it includes

The system includes only canonical public directory pages:

- `index.html` -> `/`
- `framework/index.html` -> `/framework/`
- `ccy-state-chain/index.html` -> `/ccy-state-chain/`

It does not include non-canonical files such as:

- `page.html`

The canonical standard is directory-style URL architecture.

## What it excludes

The script excludes:

- governance `.md` files
- `assets/`
- `scripts/`
- `main/data/`
- `templates/`
- drafts
- internal pages
- private files
- images
- CSS
- JavaScript
- old sitemap files
- robots.txt
- non-indexable files

## What it validates

For every public HTML page, it checks:

- `<title>` exists
- meta description exists
- canonical link exists
- canonical URL matches expected public URL
- exactly one H1 exists
- page is not marked `noindex`
- internal links are not broken
- local CSS/images/scripts referenced by the page exist
- internal `.html` links are warned against
- robots.txt references the sitemap

## Overrides

Optional overrides may be placed in:

`main/data/sitemap_overrides.json`

Example:

```json
{
  "/framework/": {
    "priority": "0.9",
    "changefreq": "monthly"
  },
  "/internal-test/": {
    "exclude": true
  }
}
```

## GitHub Actions recommendation

```yaml
name: Sovereign Indexing Gate

on:
  push:
    branches: [main]
  pull_request:

jobs:
  indexing-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python scripts/generate_sitemap.py --strict --fail-on-warnings --report
```

## Publication rule

No public page should be merged or deployed unless it passes this indexing gate.

The goal is not merely to create a sitemap.

The goal is to prevent weak, broken, duplicate, non-canonical, or untrustworthy pages from entering the public architecture.
