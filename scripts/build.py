#!/usr/bin/env python3
"""Build the English and French static editions."""
import runpy,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[1]
if (root/'dist').exists(): shutil.rmtree(root/'dist')
runpy.run_path(str(root/'scripts/build_fr.py'))
from global_site import build
build()
