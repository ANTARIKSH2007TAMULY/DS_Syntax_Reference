#!/usr/bin/env python3
"""Verify responsive/mobile features exist in built HTML."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
HTML = ROOT / "index.html"

REQUIRED = [
    "viewport-fit=cover",
    "mobile-header",
    "menu-btn",
    "nav-overlay",
    "nav-close",
    "back-to-top",
    "table-wrap",
    "max-width: 768px",
    "max-width: 1024px",
    "safe-area-inset",
    "translateX(-100%)",
    "aria-label",
    "closeNav",
    "table-wrap",
]

def main():
    if not HTML.exists():
        print("FAIL: index.html not found. Run: python3 build.py")
        sys.exit(1)

    text = HTML.read_text()
    missing = [k for k in REQUIRED if k not in text]
    nav_links = len(re.findall(r'href="#[^"]+"', text))
    ids = set(re.findall(r'\bid="([^"]+)"', text))
    nav_hrefs = re.findall(r'<nav[^>]*>.*?</nav>', text, re.DOTALL)
    broken = []
    if nav_hrefs:
        for href in re.findall(r'href="#([^"]+)"', nav_hrefs[0]):
            if href not in ids:
                broken.append(href)

    print(f"File: {HTML} ({len(text):,} bytes)")
    print(f"Nav links: {nav_links}")
    if missing:
        print("FAIL missing features:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    if broken:
        print("FAIL broken nav anchors:", broken)
        sys.exit(1)
    if "numpy-section" in text and '<section id="numpy">' not in text:
        print("FAIL: placeholders not replaced — run build.py")
        sys.exit(1)
    print("PASS: mobile/tablet features present")
    print("PASS: all nav anchors resolve")
    print("PASS: content embedded")

if __name__ == "__main__":
    main()
