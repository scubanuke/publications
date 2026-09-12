# Publication Link-Rot Check — 2026-09-02

**Verdict: one new defect. BES Asset Nomenclature Specification has drifted between the repo
and Drive, and it is one of the four NPEC-cited documents.**

The navigation site is clean — 39/39 links at HTTP 200, zero Drive links. Sharing is intact on
all six publicly-readable files. The 17 known size mismatches are still exactly the 17 documents
on the re-upload worklist, unchanged.

The new item: on 2026-08-30, commit `e195b10` published **BES v1.1** to the repo and the Pages
mirror. The Drive original was never re-uploaded, so Drive still serves **v1.0**. As of the
08-26 check both sides read 343,603 and matched; they no longer do. This is the silent-drift
case, and it is on a document with a circulating public share link.

---

## 1. Navigation site — clean

Checked in Chrome at `https://scubanuke.github.io/dba-en-navigation/?cb=2026-09-02`.

| Check | Result | Baseline |
|---|---|---|
| Drive links | **0** | 0 ✓ |
| Unique publications links | **39** (47 anchors) | 39 ✓ |
| HTTP status | **39/39 → 200** | all 200 ✓ |
| Content-length vs manifest | **38/38 PDFs match** | match ✓ |

The 39 unique links are 38 PDFs plus the `/publications/` index. The 47 anchors include 3 nav
links to sibling sites, 4 in-page anchors, and one duplicated href. No Drive link has been
reintroduced.

## 2. New defect — BES Asset Nomenclature Specification

| | |
|---|---|
| Document | BES Asset Nomenclature Specification (`awb/`) |
| Drive file | `15gHhHNU5ZqLCRw-i98ID1vEnXwnTY1eF` — `BES_Asset_Nomenclature_Specification_v1_0.pdf` |
| Drive size / modified | 343,603 · 2026-08-08 |
| Repo + manifest + Pages | 343,633 · v1.1 · published 2026-08-30 (`e195b10`) |
| Sharing | anyone-with-link reader ✓ (intact) |

**Direction of drift: the repo is ahead, Drive is behind.** The Pages mirror is correct and is
serving v1.1 at 200. What is stale is the Drive copy.

**Fix:** in Drive, right-click the file → **Manage versions → Upload new version**, and pick
`C:\Users\scuba\OneDrive\Documents\GitHub\publications\awb\BES_Asset_Nomenclature_Specification.pdf`.
Confirm the size afterwards reads 343,633. Add a Group 8 row to `DRIVE_REUPLOAD_WORKLIST.md`
recording it.

**Do not run `scripts/fetch.py` for this.** Fetch pulls Drive → repo, which here would overwrite
the published v1.1 with the superseded v1.0. (It would fail anyway on the other 37 owner-only
files, as documented in the worklist.)

Worth noting while the file is open: the Drive **title** still says `v1_0`. Retitling to `v1_1`
is cosmetic — the manifest matches on ID, not filename — but it is what made this easy to miss.
The same cosmetic lag exists on Tiered Assessment Framework, whose Drive title reads `v2_5`
while the manifest says v2.6; its bytes match exactly (177,983), so that one is title-only and
needs no upload.

## 3. Mirror vs Drive — 43 files, 25 match, 18 differ

All 43 Drive files exist; none deleted or trashed. Of the 18 size mismatches, 17 are the
outstanding re-upload backlog and 1 is the BES item above.

| Group | Files | Status |
|---|---|---|
| 1 — Series introductions | 3 | ✅ verified matching |
| 2 — Electric sector (DBA-ES) | 9 | ✅ verified matching |
| 3 — Gas sector + compressor | 7 | ☐ pending, sizes still at "old size" |
| 4 — Oil sector | 5 | ☐ pending, sizes still at "old size" |
| 5 — Command Broker | 4 | ☐ pending, sizes still at "old size" |
| 6 — Papers (GenAI Risk ICS) | 1 | ☐ pending, sizes still at "old size" |
| — BES Asset Nomenclature | 1 | ⚠ **new drift, not yet on worklist** |

Every one of the 17 pending files still reports exactly the "old size" recorded in
`DRIVE_REUPLOAD_WORKLIST.md`, so nothing in that backlog has moved or degraded since 08-24.

The 12 rows without a `drive_id` (Group 7 plus `DBA-MA-SMR-FC1-TB1`, the FD set, and
`DBA-MA-CDB`) are repo-only by design and outside the Drive check. All 12 exist locally at their
manifest byte counts.

## 4. Cited-and-canonical documents — sharing intact

| Document | Location | Drive bytes | Sharing |
|---|---|---|---|
| Tiered Assessment Framework | `awb/` | 177,983 ✓ | anyone-with-link reader ✓ |
| ERT Companion Proposal | `awb/` | 402,020 ✓ | anyone-with-link reader ✓ |
| SCRM Companion Agent | `awb/` | 228,591 ✓ | anyone-with-link reader ✓ |
| BES Asset Nomenclature Specification | `awb/` | 343,603 ⚠ | anyone-with-link reader ✓ |
| UA Grid Defense (canonical) | `papers/` | 481,245 ✓ | anyone-with-link reader ✓ |
| AI Governance Series Overview | top level | 166,824 ✓ | anyone-with-link reader ✓ |

UA Grid Defense resolves to `1W1lzZWYXGXvKiHhAvODnfuWOYhKXBBbb` in folder `1sV7Jw…` — the
canonical copy, not the Energy-sector duplicate, as intended. No sharing regressions anywhere:
all six are still `anyone` / `reader`.

## 5. Carry-over — unfixed since 08-23

`corpus.md` in the **scubanuke/command-broker** repo still links to the Command Broker Drive
folder `1GWWFxu2N-QAGkVEOJxEcNFKBM_iIShDs`, which is owner-only. Confirmed still present in the
raw file today. It does not appear in the rendered
`https://scubanuke.github.io/command-broker/` HTML, so a casual visitor will not hit it, but the
raw markdown is publicly readable on GitHub. Still the only live `drive.google.com` link in any
published repo.

Preferred fix unchanged: point it at `https://scubanuke.github.io/publications/command-broker/`.

Note this file lives in the command-broker repo, which is not among the connected local folders —
it was inspected read-only over HTTP and cannot be edited from this session.

## 6. Checks not run

- `scripts/fetch.py` round-trip verification — deliberately not attempted. It requires public
  read on all 43 Drive files; 37 are owner-only by design. See "When you're done" in
  `DRIVE_REUPLOAD_WORKLIST.md`.
- Byte-level content comparison of Drive originals against repo copies — the Drive connector
  exposes size and metadata, not checksums. Size equality is the available proxy.

---

*Report only; no file, repo, or Drive permission was modified. Nothing was committed.*
