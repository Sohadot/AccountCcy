# AccountCcy.com Sovereign Publishing Engine

## Purpose

This engine connects the AccountCcy.com data layer, templates, and public pages.

It is intentionally conservative.

It refuses to generate weak placeholder pages, refuses to publish draft pages, and refuses to link published pages to unpublished pages.

## Files

Place these files in the repository:

```text
main/templates/tool_page.html
scripts/generate_pages.py
```

The updated `tool_page.html` removes the static-hosting anti-pattern:

```html
<form action="#" method="post">
```

and replaces it with:

```html
<div class="ccy-tool-surface" role="form">
```

This avoids invalid POST behavior on GitHub Pages.

## Run

Dry-run first:

```bash
python scripts/generate_pages.py --dry-run
```

Generate without overwriting existing hand-authored pages:

```bash
python scripts/generate_pages.py
```

Overwrite existing generated pages only when certain:

```bash
python scripts/generate_pages.py --overwrite
```

## Publication Rule

The generator writes only pages with:

```text
status = published
indexable = true
```

It blocks publication if a published page links to a draft or unregistered page.

It refuses to create reference/state pages unless content data exists or the existing hand-authored file is preserved.

This protects AccountCcy.com from placeholder pages, broken links, and low-grade mass generation.
