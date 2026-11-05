#!/usr/bin/env python3
"""Build the English and French architecture practice editions."""
import shutil
from pathlib import Path
from architecture_site import build
from brand_assets import build as build_brand_assets
root=Path(__file__).resolve().parents[1]
if (root/'dist').exists():shutil.rmtree(root/'dist')
build()
build_brand_assets()
