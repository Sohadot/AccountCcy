# AccountCcy.com Sovereign Scripts Suite

This suite implements the publication pipeline agreed for AccountCcy.com:

Doctrine → Registry → Content → Templates → Generator → Quality Gate → Sitemap → Publication

## Files

```text
scripts/
├── build.py
├── generate_pages.py
├── generate_sitemap.py
├── generate_schema.py
├── validate_content.py
├── validate_links.py
├── validate_seo.py
├── validate_assets.py
└── quality_gate.py
```

## Recommended use

Dry-run page generation first:

```bash
python scripts/generate_pages.py --dry-run
```

Build everything:

```bash
python scripts/build.py
```

Strict quality gate only:

```bash
python scripts/quality_gate.py
```

## Publication rule

No public page should be treated as ready unless `quality_gate.py` passes.

## Important operating principle

The generator does not create placeholder pages. A page is generated only when it is registered, published, indexable, content-backed, and link-safe.
