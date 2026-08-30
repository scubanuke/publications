#!/usr/bin/env python3
"""Fetch the published PDFs from Google Drive into the repo tree.

Run once, on a machine that can reach Drive:

    python3 scripts/fetch.py

Reads MANIFEST.csv. For each row it downloads the Drive file and compares the
size against the manifest. A size mismatch means the Drive copy has changed
since the manifest was written, and is reported, not silently accepted.

WRITE GUARD
-----------
The download is compared to the manifest BEFORE anything touches the working
tree. A file is only overwritten when the download matches the manifest byte
for byte. This matters because the repo's PDFs are not always straight copies
of the Drive artifacts: on 2026-08-05 commit 5920687 regenerated 34 of them
from conformed sources and added the governing-instruments footer. An earlier
version of this script wrote the download first and compared afterwards, so a
run at that point would have reverted every regenerated document while still
reporting success. Do not reorder the check below the write.

If a download disagrees with the manifest, resolve it deliberately:
  * the Drive artifact is the new truth -> update MANIFEST.csv, then --force
  * the repo copy is the new truth      -> re-upload to Drive, or leave it be

Requires: pip install requests
"""
import csv, os, sys, requests

MANIFEST = os.path.join(os.path.dirname(__file__), '..', 'MANIFEST.csv')
ROOT = os.path.join(os.path.dirname(__file__), '..')
URL = 'https://drive.google.com/uc?export=download&id={}'
FORCE = '--force' in sys.argv

ok = mismatch = failed = skipped = 0
with open(MANIFEST, newline='') as fh:
    for r in csv.DictReader(fh):
        dest = os.path.join(ROOT, r['series'], r['file'])
        if not r['drive_id'].strip():
            print('skip     {} — no drive_id in manifest'.format(r['file']))
            skipped += 1
            continue
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

            got, want = len(resp.content), int(r['bytes'])
            on_disk = os.path.getsize(dest) if os.path.exists(dest) else None

            if got != want:
                # Never clobber on a mismatch. Say plainly what is at stake.
                print('MISMATCH {} — manifest {} bytes, Drive {} bytes'
                      .format(r['file'], want, got))
                if on_disk is not None:
                    print('         repo copy is {} bytes and was NOT overwritten.'
                          .format(on_disk))
                    if on_disk == want:
                        print('         The repo copy is the one the manifest describes;')
                        print('         overwriting would replace a published document.')
                if FORCE:
                    open(dest, 'wb').write(resp.content)
                    print('         --force given: overwritten anyway.')
                mismatch += 1
                continue

            open(dest, 'wb').write(resp.content)
            print('ok       {}'.format(r['file']))
            ok += 1
        except Exception as e:
            print('FAILED   {} — {}'.format(r['file'], e))
            failed += 1

print('\n{} ok, {} size mismatches, {} failed, {} skipped'
      .format(ok, mismatch, failed, skipped))
if mismatch or failed:
    print('Resolve mismatches before committing. A mismatch means the Drive artifact')
    print('is not the one this manifest was built against. Nothing was overwritten')
    print('for those rows unless --force was given.')
    sys.exit(1)
