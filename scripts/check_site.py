#!/usr/bin/env python3
"""Check local site destinations, metadata, headings and XML before publication."""
import os
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree

ROOT=Path(__file__).resolve().parents[1]/'dist'
BASE=os.environ.get('SITE_BASE_PATH','').rstrip('/')
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.h1=0; self.ids=set(); self.title=False; self.description=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        self.h1+=tag=='h1'
        if tag=='title': self.title=True
        if tag=='meta' and a.get('name')=='description': self.description=True
        if 'id' in a:
            if a['id'] in self.ids: raise AssertionError('Duplicate ID: '+a['id'])
            self.ids.add(a['id'])
        for key in ['href','src']:
            if key in a: self.links.append(a[key])

errors=[]; pages={}
for file in ROOT.rglob('*.html'):
    page=Page();page.feed(file.read_text());pages[file]=page
    if page.h1!=1: errors.append(f'{file}: expected one h1, got {page.h1}')
    if not page.title or not page.description: errors.append(f'{file}: missing title/description')
for file,page in pages.items():
    for target in page.links:
        u=urlsplit(target)
        if u.scheme or u.netloc: continue
        path=unquote(u.path)
        if BASE and (path==BASE or path.startswith(BASE+'/')): path=path[len(BASE):]
        dest=(ROOT/path.lstrip('/')) if path.startswith('/') else (file.parent/path)
        if not path: dest=file
        if dest.is_dir(): dest=dest/'index.html'
        if not dest.exists(): errors.append(f'{file.relative_to(ROOT)}: missing {target}')
        elif u.fragment and dest in pages and u.fragment not in pages[dest].ids: errors.append(f'{file}: missing anchor {target}')
for path in ['sitemap.xml','feed.xml']: ElementTree.parse(ROOT/path)
assert not errors, '\n'.join(errors)
print(f'Checked {len(pages)} HTML files, internal destinations, metadata and XML successfully.')
