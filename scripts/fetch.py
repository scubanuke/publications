#!/usr/bin/env python3
"""Fetch the published PDFs from Google Drive into the repo tree.

Run once, on a machine that can reach Drive:

    python3 scripts/fetch.py

Reads MANIFEST.csv. For each row it downloads the Drive file into
<series>/<file> and checks the size against the manifest. A size mismatch
means the Drive copy has changed since 13 July 2026 and is reported, not
silently accepted.

Requires: pip install requests
"""
import csv, os, sys, requests

MANIFEST = os.path.join(os.path.dirname(__file__), '..', 'MANIFEST.csv')
ROOT = os.path.join(os.path.dirname(__file__), '..')
URL = 'https://drive.google.com/uc?export=download&id={}'

ok = mismatch = failed = 0
with open(MANIFEST, newline='') as fh:
    for r in csv.DictReader(fh):
        dest = os.path.join(ROOT, r['series'], r['file'])
        try:
            s = requests.Session()
            resp = s.get(URL.format(r['drive_id']), timeout=60)
            # Drive interstitial for larger files: re-request with the confirm token
            if b'%PDF' not in resp.content[:1024]:
                token = next((v for k, v in s.cookies.items()
                              if k.startswith('download_warning')), None)
                if token:
                    resp = s.get(URL.format(r['drive_id']),
                                 params={'confirm': token}, timeout=60)
            if b'%PDF' not in resp.content[:1024]:
                print('FAILED   {} — not a PDF (sharing may have changed)'.format(r['file']))
                failed += 1
                continue
            open(dest, 'wb').write(resp.content)
            got, want = len(resp.content), int(r['bytes'])
            if got != want:
                print('MISMATCH {} — expected {} bytes, got {}'.format(r['file'], want, got))
                mismatch += 1
            else:
                print('ok       {}'.format(r['file']))
                ok += 1
        except Exception as e:
            print('FAILED   {} — {}'.format(r['file'], e))
            failed += 1

print('\n{} ok, {} size mismatches, {} failed'.format(ok, mismatch, failed))
if mismatch or failed:
    print('Resolve mismatches before committing. A mismatch means the Drive artifact')
    print('is not the one this manifest was built against.')
    sys.exit(1)
