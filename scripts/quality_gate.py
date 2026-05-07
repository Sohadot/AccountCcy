#!/usr/bin/env python3
"""AccountCcy.com — Sovereign Quality Gate."""
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path
from typing import Optional, Sequence
CHECKS=[['scripts/validate_content.py'],['scripts/validate_assets.py'],['scripts/validate_seo.py'],['scripts/validate_links.py'],['scripts/generate_schema.py'],['scripts/generate_sitemap.py','--strict','--fail-on-warnings','--report']]
def run(root: Path, cmd):
    print('\n'+'='*80); print('Running:', ' '.join(cmd)); print('='*80)
    return subprocess.run([sys.executable]+cmd+['--root',str(root)], cwd=root).returncode
def main(argv: Optional[Sequence[str]]=None) -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default='.'); args=ap.parse_args(argv); root=Path(args.root).resolve(); failures=[]
    for c in CHECKS:
        code=run(root,c)
        if code: failures.append((' '.join(c),code))
    print('\n'+'='*80)
    if failures:
        print('SOVEREIGN QUALITY GATE FAILED')
        for c,code in failures: print(f'- {c}: exit {code}')
        return 1
    print('SOVEREIGN QUALITY GATE PASSED'); return 0
if __name__=='__main__': raise SystemExit(main())
