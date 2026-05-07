#!/usr/bin/env python3
"""AccountCcy.com — Sovereign Build Orchestrator."""
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path
from typing import Optional, Sequence
def run(root: Path, cmd):
    print('\n$', ' '.join([sys.executable]+cmd)); return subprocess.run([sys.executable]+cmd, cwd=root).returncode
def main(argv: Optional[Sequence[str]]=None) -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default='.'); ap.add_argument('--overwrite', action='store_true'); ap.add_argument('--skip-quality-gate', action='store_true'); args=ap.parse_args(argv); root=Path(args.root).resolve()
    gen=['scripts/generate_pages.py','--root',str(root)]
    if args.overwrite: gen.append('--overwrite')
    steps=[gen, ['scripts/generate_sitemap.py','--root',str(root),'--write-robots','--strict','--report']]
    if not args.skip_quality_gate: steps.append(['scripts/quality_gate.py','--root',str(root)])
    for s in steps:
        code=run(root,s)
        if code: print('BUILD FAILED at:', ' '.join(s), file=sys.stderr); return code
    print('\nAccountCcy sovereign build complete.'); return 0
if __name__=='__main__': raise SystemExit(main())
