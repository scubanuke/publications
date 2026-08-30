# Publication Link-Rot Check — 2026-08-13

**Verdict: everything resolves. No defects found.** No action required.

## 1. Navigation site (dba-en-navigation)

Checked live via Chrome at `https://scubanuke.github.io/dba-en-navigation/?cb=2026-08-13`.

- **Drive links: 0** — no `drive.google.com` anchors present. The public site remains fully decoupled from the personal Drive.
- **Publications links: 39 unique, all HTTP 200** — 38 document PDFs plus the `publications/` index. Every link re-checked with a cache-buster returned 200.

Minor note (not a defect): the nav presents 38 distinct document PDF links rather than 39; the "39" baseline is reached only when the `publications/` index link is counted. All resolve, so nothing to fix.

## 2. Mirror vs. Drive (MANIFEST.csv, 43 mapped documents)

All 43 rows with a `drive_id` checked via the Drive connector.

- **Existence: 43/43 present**, none deleted or trashed.
- **Byte counts: 43/43 match** the manifest exactly. No silent size drift — the mirror is not stale.
- Four manifest rows (DBA-MA-SMR-FC1, DBA-MA-SMR-FC1-TB1, CB-CT, DBA-VC) have no `drive_id` and were not Drive-checked by design.

Observation (not a defect): several Drive artifacts carry recent `modifiedTime` stamps — the `awb/` set and UA Grid Defense on 2026-08-08, the Command-Broker set on 2026-07-31 — yet their byte counts still match the manifest, so the mirror is current. If any of these are re-exported in future, a size mismatch would appear here.

## 3. Cited-and-canonical documents (special attention)

| Document | Path | Bytes (manifest = Drive) | Sharing |
|---|---|---|---|
| Tiered Assessment Framework | awb/ | 177,983 ✓ | anyone-with-link reader ✓ |
| ERT Companion Proposal | awb/ | 402,020 ✓ | anyone-with-link reader ✓ |
| SCRM Companion Agent | awb/ | 228,591 ✓ | anyone-with-link reader ✓ |
| BES Asset Nomenclature Specification | awb/ | 343,603 ✓ | anyone-with-link reader ✓ |
| UA Grid Defense (canonical) | papers/ | 481,245 ✓ | anyone-with-link reader ✓ |

All five exist, match on bytes, and remain publicly readable.

## Checks not run

- **Sharing permissions were verified only for the five cited/canonical documents.** `get_file_metadata` does not surface sharing status, so a permissions check for the other 38 files was not performed this run. All five checked returned `anyone` reader.
- The bash sandbox cannot reach `scubanuke.github.io` or `drive.google.com`; all HTTP checks used Chrome and all Drive checks used the Drive connector, as required.
