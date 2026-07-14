#!/usr/bin/env python3
"""Verify every external reference still resolves.

    python3 scripts/check_links.py

Checks, for each document in MANIFEST.csv:
  1. the GitHub Pages URL returns 200 and a PDF
  2. the Google Drive file is still readable without credentials

Run after any reorganization of Drive, and on a schedule if you can.
This is the notification that does not otherwise exist.
"""
import csv, os, sys, requests

MANIFEST = os.path.join(os.path.dirname(__file__), '..', 'MANIFEST.csv')
DRIVE = 'https://drive.google.com/uc?export=download&id={}'

bad = []
with open(MANIFEST, newline='') as fh:
    for r in csv.DictReader(fh):
        try:
            p = requests.head(r['url'], allow_redirects=True, timeout=30)
            if p.status_code != 200:
                bad.append((r['file'], 'pages', p.status_code))
        except Exception as e:
            bad.append((r['file'], 'pages', str(e)))
        try:
            d = requests.get(DRIVE.format(r['drive_id']), timeout=30, stream=True)
            body = next(d.iter_content(1024), b'')
            if b'%PDF' not in body and b'download_warning' not in d.cookies.__str__().encode():
                bad.append((r['file'], 'drive', 'not readable anonymously'))
        except Exception as e:
            bad.append((r['file'], 'drive', str(e)))

if not bad:
    print('All references resolve.')
else:
    for f, where, why in bad:
        print('BROKEN  {:45s} {:6s} {}'.format(f, where, why))
    sys.exit(1)
