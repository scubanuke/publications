# Publication Link-Rot Check — 2026-09-09

**Verdict: no new defects. Nothing changed since last week.**

The navigation site is clean — 39/39 links at HTTP 200, zero Drive links. All 43 Drive files
exist, none trashed. Sharing is intact on all six publicly-readable files. The 18 size
mismatches are exactly the 18 from the 09-02 check: the 17-file re-upload backlog plus the
BES Asset Nomenclature drift. Neither has moved.

Two carry-over items remain open and unchanged: the **BES v1.0/v1.1 Drive drift** (reported
09-02, still the only cited-document defect) and the **`corpus.md` Drive-folder link** (reported
08-23). Both fixes are described below.

---

## 1. Navigation site — clean

Checked in Chrome at `https://scubanuke.github.io/dba-en-navigation/?cb=2026-09-09`.

| Check | Result | Baseline |
|---|---|---|
| Drive links | **0** | 0 ✓ |
| Unique publications links | **39** (47 anchors) | 39 ✓ |
| HTTP status | **39/39 → 200** | all 200 ✓ |
| Content-length vs manifest | **38/38 PDFs match exactly** | match ✓ |

The 39 unique links are 38 PDFs plus the `/publications/` index. The 47 anchors comprise
3 nav links to sibling sites, 4 in-page section anchors, and one duplicated href. The
`dba-en-navigation` repo's `index.html` contains zero occurrences of `drive.google.com` in the
local working copy as well. No Drive link has been reintroduced.

Last commit to the navigation repo is still `8e733f3` (2026-08-07) — the site has not been
touched since, which is consistent with the unchanged link set.

## 2. Mirror vs Drive — 43 files, 25 match, 18 differ

All 43 Drive files resolve; none deleted or trashed. Every one of the 18 mismatches reports
exactly the size recorded last week, so nothing has drifted further.

| Group | Files | Status |
|---|---|---|
| 1 — Series introductions | 3 | ✅ matching |
| 2 — Electric sector (DBA-ES) | 9 | ✅ matching |
| 3 — Gas sector + compressor | 7 | ☐ pending, still at "old size" |
| 4 — Oil sector | 5 | ☐ pending, still at "old size" |
| 5 — Command Broker | 4 | ☐ pending, still at "old size" |
| 6 — Papers (GenAI Risk ICS) | 1 | ☐ pending, still at "old size" |
| — BES Asset Nomenclature | 1 | ⚠ carry-over drift from 09-02 |

Also verified matching and outside any backlog: DBA-GAS-POL Deterrence, DBA-MA ONG Series
Introduction, DBA-DC-FC1, both DBA-UxS documents, GenMix, Powering the Always-On Economy,
Fuel Cell Position Paper, and the six public `awb/`, `papers/` and top-level files.

The 12 manifest rows without a `drive_id` are repo-only by design and outside the Drive check.
All 12 exist locally at their manifest byte counts. This now includes `DBA-MA-CDB`, published to
the mirror on 2026-09-01 (`3229aa3`); it is correctly listed with no `drive_id` and its local
size matches the manifest.

## 3. Carry-over — BES Asset Nomenclature Specification

Unchanged from the 09-02 report. Repeated here because it is one of the four NPEC-cited
documents and has a circulating public share link.

| | |
|---|---|
| Drive file | `15gHhHNU5ZqLCRw-i98ID1vEnXwnTY1eF` — `BES_Asset_Nomenclature_Specification_v1_0.pdf` |
| Drive size / modified | 343,603 · 2026-08-08 (unchanged) |
| Repo + manifest + Pages | 343,633 · v1.1 · published 2026-08-30 (`e195b10`) |
| Sharing | anyone-with-link reader ✓ |

**The repo is ahead; Drive is behind.** The Pages mirror serves the correct v1.1 at 200 — public
readers are fine. What is stale is the Drive copy that the share link points at.

**Fix:** in Drive, right-click the file → **Manage versions → Upload new version** → pick
`C:\Users\scuba\OneDrive\Documents\GitHub\publications\awb\BES_Asset_Nomenclature_Specification.pdf`.
Confirm the size then reads 343,633. Add a Group 8 row to `DRIVE_REUPLOAD_WORKLIST.md`.

**Do not run `scripts/fetch.py` for this** — fetch pulls Drive → repo and would overwrite the
published v1.1 with the superseded v1.0.

## 4. Cited-and-canonical documents — all intact

| Document | Location | Drive bytes | Sharing |
|---|---|---|---|
| Tiered Assessment Framework | `awb/` | 177,983 ✓ | anyone / reader ✓ |
| ERT Companion Proposal | `awb/` | 402,020 ✓ | anyone / reader ✓ |
| SCRM Companion Agent | `awb/` | 228,591 ✓ | anyone / reader ✓ |
| BES Asset Nomenclature Specification | `awb/` | 343,603 ⚠ | anyone / reader ✓ |
| UA Grid Defense (canonical) | `papers/` | 481,245 ✓ | anyone / reader ✓ |
| AI Governance Series Overview | top level | 166,824 ✓ | anyone / reader ✓ |

UA Grid Defense still resolves to `1W1lzZWYXGXvKiHhAvODnfuWOYhKXBBbb` in folder `1sV7Jw…` — the
canonical copy, not the Energy-sector duplicate. No sharing regressions: all six remain
`anyone` / `reader`.

Cosmetic-only, no action needed: the Drive **titles** of BES (`v1_0`) and Tiered Assessment
Framework (`v2_5`) lag their manifest versions. Tiered's bytes match exactly, so it is
title-only. The manifest matches on ID, not filename.

## 5. Carry-over — `corpus.md` Drive-folder link

`corpus.md` line 31 in the **scubanuke/command-broker** repo still links to the Command Broker
Drive folder `1GWWFxu2N-QAGkVEOJxEcNFKBM_iIShDs`, which is owner-only. Confirmed present today
in both the raw GitHub copy and the local working copy. It is on the Proposer–Gate Pattern
bullet, the one document in that list not yet on the mirror. It does not appear in the rendered
`https://scubanuke.github.io/command-broker/` page, but the raw markdown is publicly readable.
Still the only live `drive.google.com` link in any published repo.

**Correction to last week's report:** it stated this file could not be edited from a Cowork
session because the command-broker repo was not a connected folder. It *is* connected this
session (`C:\Users\scuba\OneDrive\Documents\GitHub\command-broker`), so the fix is now
actionable locally — it was simply not made, per this task's report-only scope.

Preferred fix unchanged: point it at `https://scubanuke.github.io/publications/command-broker/`,
or drop the link and keep the surrounding "not yet on the mirror" prose.

## 6. Checks not run

- `scripts/fetch.py` round-trip verification — deliberately not attempted. It requires public
  read on all 43 Drive files; 37 are owner-only by design. See "When you're done" in
  `DRIVE_REUPLOAD_WORKLIST.md`.
- Byte-level content comparison of Drive originals against repo copies — the Drive connector
  exposes size and metadata, not checksums. Size equality is the available proxy.
- Sharing was read for the six known-public files only. The other 37 were confirmed to exist
  but their permissions were not re-enumerated; the 08-24 audit established they are owner-only
  by design and nothing this week suggests otherwise.

---

*Report only; no file, repo, or Drive permission was modified. Nothing was committed.*
