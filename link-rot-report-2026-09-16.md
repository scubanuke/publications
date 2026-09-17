# Publication Link-Rot Check — 2026-09-16

**Verdict: no new defects, and one carry-over resolved.**

The navigation site is clean — 39/39 links at HTTP 200, zero Drive links, every served PDF
byte-identical to the manifest. All 43 Drive files exist, none trashed. Sharing is intact on all
six publicly-readable files.

**Resolved this week:** the **Tiered Assessment Framework** Drive original was re-uploaded on
2026-09-12 and now matches the published v2.8 exactly. The file ID and its anyone-with-link
reader permission both survived the version replace, which is what the worklist method is for.

The 18 size mismatches are the same 18 as last week, at exactly the same byte counts — the
17-file re-upload backlog plus the BES Asset Nomenclature drift. Nothing moved.

One carry-over remains open: the **`corpus.md` Drive-folder link** (first reported 08-23), plus
the BES drift (09-02). Both fixes are restated below.

---

## 1. Navigation site — clean

Checked in Chrome at `https://scubanuke.github.io/dba-en-navigation/?cb=2026-09-16`.

| Check | Result | Baseline |
|---|---|---|
| Drive links | **0** | 0 ✓ |
| Unique publications links | **39** (47 anchors) | 39 ✓ |
| HTTP status | **39/39 → 200** | all 200 ✓ |
| Content-length vs manifest | **38/38 PDFs match exactly** | match ✓ |
| Off-site links | **0** | — |

The 39 unique links are 38 PDFs plus the `/publications/` index. Sizes were compared against
`MANIFEST.csv` as served from Pages, so this is a live end-to-end check rather than a local one.

Last commit to the navigation repo is still `8e733f3` (2026-08-07); its `index.html` contains
zero occurrences of `drive.google.com` in the local working copy. No Drive link has been
reintroduced anywhere in the `publications` repo either.

## 2. Mirror vs Drive — 43 files, 25 match, 18 differ

All 43 Drive files resolve; none deleted or trashed. Every one of the 18 mismatches reports
**exactly the "old size" recorded in `DRIVE_REUPLOAD_WORKLIST.md`**, so nothing has drifted
further in either direction.

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
All 12 exist locally at their manifest byte counts.

## 3. Resolved — Tiered Assessment Framework

| | |
|---|---|
| Document | Tiered Assessment Framework (`awb/`) — NPEC-cited |
| Drive file | `1K039vZxQU7JrMLio4RW1iW_vNxo5KptC` |
| Drive size / modified | **308,120** · 2026-09-12 |
| Repo + manifest + Pages | 308,120 · v2.8 · published 2026-09-12 (`b07b70f`) |
| Sharing | anyone-with-link reader ✓ (survived the version replace) |

The repo moved v2.7 → v2.8 on 09-12 (`7618fb7`, then `b07b70f`) and the Drive original was
re-uploaded the same day. Both sides read 308,120 and Pages serves that byte count live. The
cosmetic version-in-title lag noted on 09-02 is also gone — the Drive title is now plain
`Tiered_Assessment_Framework.pdf`, carrying no version string to go stale.

Nothing to do here. Recorded so the change is not mistaken for drift next week.

## 4. Carry-over — BES Asset Nomenclature Specification

| | |
|---|---|
| Document | BES Asset Nomenclature Specification (`awb/`) — NPEC-cited |
| Drive file | `15gHhHNU5ZqLCRw-i98ID1vEnXwnTY1eF` — `BES_Asset_Nomenclature_Specification_v1_0.pdf` |
| Drive size / modified | 343,603 · 2026-08-08 (unchanged) |
| Repo + manifest + Pages | 343,633 · v1.1 · published 2026-08-30 (`e195b10`) |
| Sharing | anyone-with-link reader ✓ (intact) |

Direction of drift is unchanged: **the repo is ahead, Drive is behind.** Pages serves the correct
v1.1 at 200. What is stale is the Drive copy, which still carries a circulating public share link.

**Fix:** in Drive, right-click → **Manage versions → Upload new version**, pick
`C:\Users\scuba\OneDrive\Documents\GitHub\publications\awb\BES_Asset_Nomenclature_Specification.pdf`,
and confirm the size then reads 343,633. Add a Group 8 row to `DRIVE_REUPLOAD_WORKLIST.md`.
This is the same operation that just worked on the Tiered Assessment Framework.

**Do not run `scripts/fetch.py` for this.** Fetch pulls Drive → repo, which here would overwrite
the published v1.1 with the superseded v1.0.

## 5. Carry-over — Drive link in `command-broker/corpus.md`

Line 31 of `corpus.md` in the **scubanuke/command-broker** repo still links to the Command
Broker Drive folder `1GWWFxu2N-QAGkVEOJxEcNFKBM_iIShDs`, which is owner-only. Confirmed present
again today in the local working copy. It sits on the Proposer–Gate Pattern bullet, the one
document in that list not yet on the mirror. It does not appear in the rendered
`https://scubanuke.github.io/command-broker/` page, but the raw markdown is publicly readable.

Still the only live `drive.google.com` link in any published repo.

**Fix:** point it at `https://scubanuke.github.io/publications/command-broker/`, or drop the link
and keep the surrounding "not yet on the mirror" prose. The `command-broker` repo is a connected
folder this session, so this is editable locally — not done here, per this task's report-only scope.

## 6. Minor — stale size in the Group 7 worklist

`DRIVE_REUPLOAD_WORKLIST.md` Group 7 lists
`dba-ma-smr/DBA-MA-SMR-FC1_SMR_Facility_Class_Design_Basis.pdf` at **249,852 bytes**. That row
predates the v0.9 publication on 2026-09-12 (`437fd27`); the file is now **433,917 bytes**, which
is what the manifest and the local copy both read.

No defect — the document is repo-only and correct everywhere it is actually served. But if the
Group 7 fresh-upload is ever done, the size sanity-check in that row would fail against a
correct file. Worth updating the number when the worklist is next touched.

## 7. Checks not run

- `scripts/fetch.py` round-trip verification — deliberately not attempted. It requires public
  read on all 43 Drive files; 37 are owner-only by design. See "When you're done" in
  `DRIVE_REUPLOAD_WORKLIST.md`.
- Byte-level content comparison of Drive originals against repo copies — the Drive connector
  exposes size and metadata, not checksums. Size equality is the available proxy, and it cannot
  detect a revision that happens to preserve byte count.
- Sharing was read for the six known-public files only. The other 37 were confirmed to exist but
  their permissions were not re-enumerated; the 08-24 audit established they are owner-only by
  design and nothing this week suggests otherwise.

---

*Report only; no file, repo, or Drive permission was modified. Nothing was committed.*
