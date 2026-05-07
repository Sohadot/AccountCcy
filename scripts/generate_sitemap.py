#!/usr/bin/env python3
"""
AccountCcy.com — Sovereign Indexing Gate
File: scripts/generate_sitemap.py

Purpose:
Generate a high-integrity sitemap.xml and prevent indexing mistakes before publication.

This is not a basic sitemap generator.

It is a sovereign indexing gate designed for a reference-grade digital asset that may grow
to hundreds or thousands of canonical, high-quality pages.

It verifies:
- public canonical pages
- directory-style URLs
- canonical URL consistency
- robots/noindex discipline
- title and meta description presence
- H1 integrity
- internal link integrity
- local asset integrity
- sitemap validity
- robots.txt sitemap reference
- exclusion of governance/source/draft/internal files

Output:
- sitemap.xml
- optional sitemap-index.xml when very large
- optional main/reports/indexing-report.json
- optional robots.txt update/check

Important:
- Search engines use sitemap.xml, not Sitemap.xls.
- This script includes only public, canonical, indexable HTML pages.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple
from urllib.parse import quote, unquote, urljoin, urlparse
from xml.sax.saxutils import escape


DEFAULT_BASE_URL = "https://accountccy.com"
DEFAULT_OUTPUT = "sitemap.xml"
SITEMAP_NAMESPACE = "https://www.sitemaps.org/schemas/sitemap/0.9"
MAX_URLS_PER_SITEMAP = 50000

PUBLIC_INDEX_FILENAME = "index.html"


# ---------------------------------------------------------------------------
# Exclusion policy
# ---------------------------------------------------------------------------

EXCLUDED_DIR_NAMES = {
    ".git",
    ".github",
    ".vscode",
    ".idea",
    "__pycache__",
    "node_modules",
    ".next",
    "dist",
    "build",
    "tmp",
    "temp",
    "cache",
    ".cache",
    "scripts",
    "main",
    "data",
    "templates",
    "drafts",
    "draft",
    "notes",
    "private",
    "internal",
    "governance",
    "archive",
    "archives",
    "tests",
    "test",
    "coverage",
    "vendor",
    "assets",
}

EXCLUDED_FILE_NAMES = {
    "README.md",
    "FOUNDATION_DOCTRINE.md",
    "ASSET_THESIS.md",
    "ARCHITECTURE.md",
    "CONTENT_GOVERNANCE.md",
    "SEO_POLICY.md",
    "MONETIZATION_PRINCIPLES.md",
    "ACQUISITION_POSTURE.md",
    "QUALITY_GATE.md",
    "DECISION_LOG.md",
    "DESIGN_SYSTEM.md",
    "UI_COMPONENTS.md",
    "HOMEPAGE_WIREFRAME.md",
    "domain-dossier.md",
    "CNAME",
    "robots.txt",
    "sitemap.xml",
    "sitemap-index.xml",
    "llms.txt",
    "LICENSE",
    ".nojekyll",
}

DRAFT_MARKERS = {
    "draft",
    "_draft",
    "private",
    "_private",
    "internal",
    "_internal",
    "test",
    "_test",
    "sample",
    "_sample",
    "placeholder",
}


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class PageAudit:
    source_path: str
    url_path: str
    loc: str
    title: Optional[str] = None
    meta_description: Optional[str] = None
    canonical: Optional[str] = None
    robots: Optional[str] = None
    h1_count: int = 0
    excluded: bool = False
    exclusion_reason: Optional[str] = None
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    internal_links: List[str] = field(default_factory=list)
    local_assets: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class SitemapEntry:
    loc: str
    lastmod: str
    changefreq: str
    priority: str
    source_path: str


@dataclass
class HTMLMetadata:
    title: Optional[str] = None
    meta_description: Optional[str] = None
    robots: Optional[str] = None
    canonical: Optional[str] = None
    h1_count: int = 0
    anchors: List[str] = field(default_factory=list)
    assets: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# HTML parser
# ---------------------------------------------------------------------------

class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.meta = HTMLMetadata()
        self._in_title = False
        self._title_parts: List[str] = []
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        tag = tag.lower()
        attr = {k.lower(): (v or "") for k, v in attrs}

        if tag == "title":
            self._in_title = True

        if tag == "h1":
            self.meta.h1_count += 1
            self._in_h1 = True

        if tag == "meta":
            name = attr.get("name", "").lower()
            content = attr.get("content", "")
            if name == "description":
                self.meta.meta_description = content.strip()
            elif name == "robots":
                self.meta.robots = content.strip()

        if tag == "link":
            rel = attr.get("rel", "").lower()
            href = attr.get("href", "").strip()
            if "canonical" in rel and href:
                self.meta.canonical = href
            if href and rel in {"stylesheet", "icon", "preload", "modulepreload"}:
                self.meta.assets.append(href)

        if tag == "a":
            href = attr.get("href", "").strip()
            if href:
                self.meta.anchors.append(href)

        if tag in {"img", "script", "source", "video", "audio", "iframe"}:
            src = attr.get("src", "").strip()
            if src:
                self.meta.assets.append(src)

        if tag == "img":
            srcset = attr.get("srcset", "").strip()
            if srcset:
                for item in srcset.split(","):
                    candidate = item.strip().split(" ")[0]
                    if candidate:
                        self.meta.assets.append(candidate)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
            title = "".join(self._title_parts).strip()
            self.meta.title = re.sub(r"\s+", " ", title) if title else None
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def normalize_base_url(base_url: str) -> str:
    base_url = base_url.strip()
    if not base_url:
        raise ValueError("Base URL cannot be empty.")
    if not base_url.startswith(("https://", "http://")):
        raise ValueError("Base URL must start with https:// or http://")
    return base_url.rstrip("/")


def load_json(path: Path) -> Dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def load_site_config(root: Path) -> Dict:
    candidates = [
        root / "main" / "data" / "site.json",
        root / "data" / "site.json",
        root / "site.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return load_json(candidate)
    return {}


def load_overrides(root: Path) -> Dict[str, Dict]:
    candidates = [
        root / "main" / "data" / "sitemap_overrides.json",
        root / "data" / "sitemap_overrides.json",
        root / "sitemap_overrides.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            data = load_json(candidate)
            if not isinstance(data, dict):
                raise ValueError(f"{candidate} must contain a JSON object.")
            return data
    return {}


def is_hidden_path(path: Path) -> bool:
    return any(part.startswith(".") and part not in {".well-known"} for part in path.parts)


def has_excluded_dir(path: Path) -> bool:
    return bool({part.lower() for part in path.parts} & EXCLUDED_DIR_NAMES)


def has_draft_marker(path: Path) -> bool:
    return bool({part.lower() for part in path.parts} & DRAFT_MARKERS)


def should_exclude_html(root: Path, file_path: Path) -> Tuple[bool, Optional[str]]:
    rel = file_path.relative_to(root)

    if is_hidden_path(rel):
        return True, "hidden path"

    if has_excluded_dir(rel.parent):
        return True, "excluded directory"

    if has_draft_marker(rel):
        return True, "draft/internal/test marker"

    if file_path.name in EXCLUDED_FILE_NAMES:
        return True, "excluded governance or system file"

    if file_path.suffix.lower() != ".html":
        return True, "not html"

    if file_path.name.lower() != PUBLIC_INDEX_FILENAME:
        return True, "non-canonical html file; use directory/index.html"

    return False, None


def file_to_url_path(root: Path, file_path: Path) -> str:
    rel = file_path.relative_to(root).as_posix()
    if rel == PUBLIC_INDEX_FILENAME:
        return "/"
    if rel.endswith("/" + PUBLIC_INDEX_FILENAME):
        return "/" + rel[: -len(PUBLIC_INDEX_FILENAME)]
    return "/" + rel.strip("/") + "/"


def quote_url_path(url_path: str) -> str:
    return quote(url_path, safe="/-._~")


def canonical_loc(base_url: str, url_path: str) -> str:
    return base_url + quote_url_path(url_path)


def read_metadata(file_path: Path) -> HTMLMetadata:
    parser = MetadataParser()
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    parser.feed(content)
    return parser.meta


def has_noindex(meta: HTMLMetadata) -> bool:
    robots = (meta.robots or "").lower()
    tokens = {token.strip() for token in robots.split(",")}
    return "noindex" in tokens


def get_git_lastmod(root: Path, file_path: Path) -> Optional[str]:
    try:
        rel = str(file_path.relative_to(root))
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", rel],
            cwd=str(root),
            capture_output=True,
            text=True,
            check=False,
        )
    except (OSError, ValueError):
        return None

    stamp = result.stdout.strip()
    if not stamp:
        return None

    try:
        dt = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        return dt.date().isoformat()
    except ValueError:
        return None


def get_file_lastmod(file_path: Path) -> str:
    return datetime.fromtimestamp(file_path.stat().st_mtime, tz=timezone.utc).date().isoformat()


def determine_lastmod(root: Path, file_path: Path) -> str:
    return get_git_lastmod(root, file_path) or get_file_lastmod(file_path)


def classify_url(url_path: str) -> Tuple[str, str]:
    if url_path == "/":
        return "weekly", "1.0"

    high_value = {
        "/monetary-truth-chain-of-custody/",
        "/framework/",
        "/ccy-state-chain/",
        "/what-is-account-currency/",
        "/cfo-guide/",
    }
    if url_path in high_value:
        return "monthly", "0.9"

    if url_path in {"/glossary/", "/currency-state-diagnostic/", "/account-currency-in-erp/"}:
        return "monthly", "0.8"

    if url_path.startswith("/glossary/"):
        return "monthly", "0.7"

    if url_path.startswith("/articles/") or url_path.startswith("/briefings/"):
        return "monthly", "0.6"

    if url_path.startswith("/acquisition/"):
        return "monthly", "0.5"

    return "monthly", "0.7"


def apply_overrides(url_path: str, entry: Dict, overrides: Dict[str, Dict]) -> Dict:
    override = overrides.get(url_path) or overrides.get(url_path.rstrip("/") + "/")
    if not override:
        return entry
    if override.get("exclude") is True:
        entry["exclude"] = True
    for key in ("priority", "changefreq", "lastmod"):
        if key in override:
            entry[key] = str(override[key])
    return entry


def is_external_url(href: str, base_url: str) -> bool:
    parsed = urlparse(href)
    if parsed.scheme in {"mailto", "tel", "sms", "javascript", "data"}:
        return True
    if parsed.scheme in {"http", "https"}:
        return not href.startswith(base_url)
    return False


def normalize_internal_href(current_url_path: str, href: str, base_url: str) -> Optional[str]:
    href = href.strip()
    if not href or href.startswith("#"):
        return None

    parsed = urlparse(href)
    if parsed.scheme in {"mailto", "tel", "sms", "javascript", "data"}:
        return None

    if parsed.scheme in {"http", "https"}:
        if not href.startswith(base_url):
            return None
        relative = href[len(base_url):] or "/"
    else:
        relative = href

    relative = relative.split("#", 1)[0].split("?", 1)[0]
    if not relative:
        return None

    if relative.startswith("/"):
        path = relative
    else:
        base_dir = current_url_path if current_url_path.endswith("/") else current_url_path.rsplit("/", 1)[0] + "/"
        joined = urljoin(base_dir, relative)
        path = urlparse(joined).path

    path = unquote(path)

    if path.endswith(".html"):
        return path

    if not path.endswith("/"):
        path += "/"

    return path


def url_path_to_file(root: Path, url_path: str) -> Path:
    if url_path == "/":
        return root / PUBLIC_INDEX_FILENAME

    path = url_path.strip("/")
    if path.endswith(".html"):
        return root / path

    return root / path / PUBLIC_INDEX_FILENAME


def normalize_asset_path(current_file: Path, root: Path, src: str, base_url: str) -> Optional[Path]:
    src = src.strip()
    if not src or src.startswith("#"):
        return None

    parsed = urlparse(src)
    if parsed.scheme in {"http", "https", "data", "mailto", "tel", "javascript"}:
        return None

    clean = src.split("#", 1)[0].split("?", 1)[0]
    if not clean:
        return None

    if clean.startswith("/"):
        return root / clean.lstrip("/")

    return (current_file.parent / clean).resolve()


def audit_page(root: Path, base_url: str, file_path: Path, overrides: Dict[str, Dict]) -> Tuple[Optional[SitemapEntry], PageAudit]:
    url_path = quote_url_path(file_to_url_path(root, file_path))
    loc = canonical_loc(base_url, url_path)
    audit = PageAudit(
        source_path=file_path.relative_to(root).as_posix(),
        url_path=url_path,
        loc=loc,
    )

    meta = read_metadata(file_path)
    audit.title = meta.title
    audit.meta_description = meta.meta_description
    audit.canonical = meta.canonical
    audit.robots = meta.robots
    audit.h1_count = meta.h1_count

    if has_noindex(meta):
        audit.excluded = True
        audit.exclusion_reason = "meta robots noindex"
        return None, audit

    # Required metadata.
    if not meta.title:
        audit.errors.append("Missing <title>.")
    elif len(meta.title) > 70:
        audit.warnings.append(f"Title is long ({len(meta.title)} characters).")

    if not meta.meta_description:
        audit.errors.append("Missing meta description.")
    elif len(meta.meta_description) > 170:
        audit.warnings.append(f"Meta description is long ({len(meta.meta_description)} characters).")

    if not meta.canonical:
        audit.errors.append("Missing canonical link.")
    elif meta.canonical.rstrip("/") + "/" != loc.rstrip("/") + "/":
        audit.errors.append(f"Canonical mismatch. Expected {loc}, found {meta.canonical}.")

    if meta.h1_count != 1:
        audit.errors.append(f"Expected exactly one H1, found {meta.h1_count}.")

    # Internal links.
    for href in meta.anchors:
        normalized = normalize_internal_href(url_path, href, base_url)
        if not normalized:
            continue
        audit.internal_links.append(normalized)

        if normalized.endswith(".html"):
            audit.warnings.append(f"Internal link uses .html style instead of directory URL: {href}")

        target = url_path_to_file(root, normalized)
        if not target.exists():
            audit.errors.append(f"Broken internal link: {href} -> {normalized}")

    # Local assets.
    for src in meta.assets:
        asset_path = normalize_asset_path(file_path, root, src, base_url)
        if not asset_path:
            continue
        try:
            rel = asset_path.relative_to(root)
        except ValueError:
            audit.errors.append(f"Local asset resolves outside site root: {src}")
            continue

        audit.local_assets.append(rel.as_posix())

        if not asset_path.exists():
            audit.errors.append(f"Missing local asset: {src} -> {rel.as_posix()}")

    changefreq, priority = classify_url(url_path)
    entry_dict = {
        "lastmod": determine_lastmod(root, file_path),
        "changefreq": changefreq,
        "priority": priority,
        "exclude": False,
    }
    entry_dict = apply_overrides(url_path, entry_dict, overrides)

    if entry_dict.get("exclude"):
        audit.excluded = True
        audit.exclusion_reason = "excluded by sitemap_overrides.json"
        return None, audit

    entry = SitemapEntry(
        loc=loc,
        lastmod=entry_dict["lastmod"],
        changefreq=entry_dict["changefreq"],
        priority=entry_dict["priority"],
        source_path=file_path.relative_to(root).as_posix(),
    )
    return entry, audit


def discover(root: Path, base_url: str, overrides: Dict[str, Dict]) -> Tuple[List[SitemapEntry], List[PageAudit]]:
    entries: List[SitemapEntry] = []
    audits: List[PageAudit] = []

    for file_path in sorted(root.rglob("*.html")):
        excluded, reason = should_exclude_html(root, file_path)
        if excluded:
            continue

        entry, audit = audit_page(root, base_url, file_path, overrides)
        audits.append(audit)

        if entry is not None:
            entries.append(entry)

    entries.sort(key=lambda e: (0 if e.loc == f"{base_url}/" else 1, e.loc))
    return entries, audits


def validate_sitemap_entries(entries: Sequence[SitemapEntry]) -> List[str]:
    errors: List[str] = []
    seen: Set[str] = set()

    for entry in entries:
        if entry.loc in seen:
            errors.append(f"Duplicate URL: {entry.loc}")
        seen.add(entry.loc)

        if " " in entry.loc:
            errors.append(f"URL contains raw space: {entry.loc}")

        if not entry.loc.startswith(("https://", "http://")):
            errors.append(f"Invalid URL scheme: {entry.loc}")

        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", entry.lastmod):
            errors.append(f"Invalid lastmod for {entry.loc}: {entry.lastmod}")

        try:
            priority = float(entry.priority)
            if priority < 0.0 or priority > 1.0:
                errors.append(f"Priority out of range for {entry.loc}: {entry.priority}")
        except ValueError:
            errors.append(f"Invalid priority for {entry.loc}: {entry.priority}")

        if entry.changefreq not in {"always", "hourly", "daily", "weekly", "monthly", "yearly", "never"}:
            errors.append(f"Invalid changefreq for {entry.loc}: {entry.changefreq}")

    return errors


def validate_robots(root: Path, base_url: str, write_robots: bool = False) -> List[str]:
    warnings: List[str] = []
    robots_path = root / "robots.txt"
    expected_sitemap = f"Sitemap: {base_url}/sitemap.xml"

    if write_robots:
        robots_path.write_text(f"User-agent: *\nAllow: /\n\n{expected_sitemap}\n", encoding="utf-8")
        return warnings

    if not robots_path.exists():
        warnings.append("robots.txt is missing.")
        return warnings

    content = robots_path.read_text(encoding="utf-8", errors="ignore")
    if expected_sitemap not in content:
        warnings.append(f"robots.txt does not reference expected sitemap: {expected_sitemap}")

    return warnings


def render_urlset(entries: Sequence[SitemapEntry]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<urlset xmlns="{SITEMAP_NAMESPACE}">',
    ]
    for entry in entries:
        lines.extend([
            "  <url>",
            f"    <loc>{escape(entry.loc)}</loc>",
            f"    <lastmod>{escape(entry.lastmod)}</lastmod>",
            f"    <changefreq>{escape(entry.changefreq)}</changefreq>",
            f"    <priority>{escape(entry.priority)}</priority>",
            "  </url>",
        ])
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def render_sitemap_index(base_url: str, sitemap_files: Sequence[str], today: str) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<sitemapindex xmlns="{SITEMAP_NAMESPACE}">',
    ]
    for file_name in sitemap_files:
        lines.extend([
            "  <sitemap>",
            f"    <loc>{escape(base_url + '/' + file_name)}</loc>",
            f"    <lastmod>{escape(today)}</lastmod>",
            "  </sitemap>",
        ])
    lines.append("</sitemapindex>")
    return "\n".join(lines) + "\n"


def write_sitemaps(root: Path, output: Path, base_url: str, entries: Sequence[SitemapEntry]) -> List[Path]:
    output = output if output.is_absolute() else root / output
    output_paths: List[Path] = []

    if len(entries) <= MAX_URLS_PER_SITEMAP:
        output.write_text(render_urlset(entries), encoding="utf-8")
        output_paths.append(output)
        return output_paths

    stem = output.stem
    suffix = output.suffix or ".xml"
    sitemap_files: List[str] = []

    for idx in range(0, len(entries), MAX_URLS_PER_SITEMAP):
        chunk = entries[idx: idx + MAX_URLS_PER_SITEMAP]
        file_name = f"{stem}-{(idx // MAX_URLS_PER_SITEMAP) + 1}{suffix}"
        path = output.parent / file_name
        path.write_text(render_urlset(chunk), encoding="utf-8")
        output_paths.append(path)
        sitemap_files.append(file_name)

    index_path = output.parent / "sitemap-index.xml"
    today = datetime.now(timezone.utc).date().isoformat()
    index_path.write_text(render_sitemap_index(base_url, sitemap_files, today), encoding="utf-8")
    output_paths.append(index_path)
    return output_paths


def write_report(root: Path, base_url: str, entries: Sequence[SitemapEntry], audits: Sequence[PageAudit], global_errors: Sequence[str], global_warnings: Sequence[str]) -> Path:
    report_dir = root / "main" / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "indexing-report.json"

    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "base_url": base_url,
        "url_count": len(entries),
        "global_errors": list(global_errors),
        "global_warnings": list(global_warnings),
        "entries": [asdict(entry) for entry in entries],
        "page_audits": [asdict(audit) for audit in audits],
    }
    report_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report_path


def summarize_failures(audits: Sequence[PageAudit], global_errors: Sequence[str], global_warnings: Sequence[str]) -> Tuple[int, int]:
    error_count = len(global_errors) + sum(len(a.errors) for a in audits)
    warning_count = len(global_warnings) + sum(len(a.warnings) for a in audits)
    return error_count, warning_count


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate and validate AccountCcy.com sitemap.xml.")
    parser.add_argument("--root", default=".", help="Site root directory. Default: current directory.")
    parser.add_argument("--base-url", default=None, help="Canonical base URL. Default: site.json or https://accountccy.com.")
    parser.add_argument("--output", default="sitemap.xml", help="Output sitemap path. Default: sitemap.xml.")
    parser.add_argument("--strict", action="store_true", help="Fail if any errors are found.")
    parser.add_argument("--fail-on-warnings", action="store_true", help="Fail if warnings are found.")
    parser.add_argument("--report", action="store_true", help="Write main/reports/indexing-report.json.")
    parser.add_argument("--write-robots", action="store_true", help="Create/update robots.txt with sitemap reference.")
    parser.add_argument("--verbose", action="store_true", help="Print page-level audit details.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()

    if not root.exists():
        print(f"ERROR: Root does not exist: {root}", file=sys.stderr)
        return 2

    config = load_site_config(root)
    base_url = args.base_url or config.get("canonical_url") or config.get("base_url") or DEFAULT_BASE_URL
    base_url = normalize_base_url(base_url)

    overrides = load_overrides(root)
    entries, audits = discover(root, base_url, overrides)

    global_errors = validate_sitemap_entries(entries)
    global_warnings = validate_robots(root, base_url, write_robots=args.write_robots)

    output_paths = write_sitemaps(root, Path(args.output), base_url, entries)

    report_path = None
    if args.report:
        report_path = write_report(root, base_url, entries, audits, global_errors, global_warnings)

    error_count, warning_count = summarize_failures(audits, global_errors, global_warnings)

    print(f"Generated sovereign sitemap for {base_url}")
    print(f"URLs included: {len(entries)}")
    print(f"Errors: {error_count}")
    print(f"Warnings: {warning_count}")

    for path in output_paths:
        try:
            shown = path.relative_to(root)
        except ValueError:
            shown = path
        print(f"Wrote: {shown}")

    if report_path:
        print(f"Report: {report_path.relative_to(root)}")

    if args.verbose or error_count or warning_count:
        if global_errors:
            print("\nGlobal errors:")
            for item in global_errors:
                print(f"- {item}")
        if global_warnings:
            print("\nGlobal warnings:")
            for item in global_warnings:
                print(f"- {item}")

        for audit in audits:
            if args.verbose or audit.errors or audit.warnings:
                print(f"\nPage: {audit.source_path} -> {audit.loc}")
                if audit.excluded:
                    print(f"  Excluded: {audit.exclusion_reason}")
                for err in audit.errors:
                    print(f"  ERROR: {err}")
                for warn in audit.warnings:
                    print(f"  WARNING: {warn}")

    if args.strict and error_count:
        print("\nSTRICT MODE FAILED: resolve errors before publication.", file=sys.stderr)
        return 1

    if args.fail_on_warnings and warning_count:
        print("\nWARNING GATE FAILED: resolve warnings before publication.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
