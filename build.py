#!/usr/bin/env python3
"""Assemble fragment files into a single self-contained HTML reference."""
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = (ROOT / "template.html").read_text()
PLACEHOLDERS = {
    "numpy-section": "numpy.html",
    "pandas-section": "pandas.html",
    "viz-section": "viz.html",
    "stats-ml-section": "stats-ml.html",
}

html = TEMPLATE
for div_id, fname in PLACEHOLDERS.items():
    content = (ROOT / fname).read_text()
    html = html.replace(f'<div id="{div_id}"></div>', content)

# Write to both entry points
for out_name in ("index.html", "ds-syntax-reference.html"):
    out = ROOT / out_name
    out.write_text(html)
    print(f"Built {out} ({len(html):,} bytes)")
