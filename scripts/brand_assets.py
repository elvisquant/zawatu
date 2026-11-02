"""Publish content-versioned brand assets with browser and sharing fallbacks."""
import hashlib
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
ASSETS = ROOT / 'assets'
NAMES = ['logo.svg', 'logo-white.svg', 'favicon.svg', 'browser-icon.png',
         'apple-touch-icon.png', 'favicon-32.png', 'favicon.ico']


def build():
    versions = {}
    for name in NAMES:
        source = ASSETS / name
        digest = hashlib.sha256(source.read_bytes()).hexdigest()[:12]
        versions[name] = f'{source.stem}.{digest}{source.suffix}'
        for directory in [OUT / 'assets', OUT / 'fr/assets']:
            shutil.copyfile(source, directory / versions[name])
    # Conventional URLs used by saved shortcuts and older browser discovery.
    shutil.copyfile(ASSETS / 'favicon.ico', OUT / 'favicon.ico')
    shutil.copyfile(ASSETS / 'apple-touch-icon.png', OUT / 'apple-touch-icon.png')
    base = os.environ.get('SITE_BASE_PATH', '').rstrip('/')
    origin = os.environ.get('SITE_URL', 'https://zawatu.com').rstrip('/')
    for page in OUT.rglob('*.html'):
        text = page.read_text()
        for name in ['logo.svg', 'logo-white.svg', 'favicon.svg']:
            text = text.replace('assets/' + name, 'assets/' + versions[name])
        icon = re.search(r'<link rel="icon"[^>]*href="([^"]+)"[^>]*>', text)
        if not icon:
            raise ValueError(f'Missing SVG favicon in {page}')
        directory = icon.group(1).rsplit('/', 1)[0] + '/'
        fallbacks = (f'<link rel="icon" type="image/x-icon" href="{directory}{versions["favicon.ico"]}" sizes="any">'
                     f'<link rel="icon" type="image/png" href="{directory}{versions["favicon-32.png"]}" sizes="32x32">')
        text = text.replace(icon.group(0), fallbacks + icon.group(0), 1)
        share = origin + base + '/assets/' + versions['browser-icon.png']
        metadata = (f'<link rel="apple-touch-icon" sizes="180x180" href="{directory}{versions["apple-touch-icon.png"]}">'
                    f'<meta property="og:image" content="{share}">'
                    '<meta property="og:image:width" content="512">'
                    '<meta property="og:image:height" content="512">'
                    '<meta property="og:image:alt" content="Zawatu symbol">'
                    '<meta name="twitter:card" content="summary">'
                    f'<meta name="twitter:image" content="{share}">')
        text = text.replace('</head>', metadata + '</head>')
        page.write_text(text)
    print('Published versioned logos, SVG/PNG/ICO favicons and sharing metadata.')
