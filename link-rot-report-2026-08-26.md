# Publication Link-Rot Check — 2026-08-26

**Verdict: everything resolves. No new defects.**

The navigation site is clean live — 39/39 links at HTTP 200, zero Drive links. All 43 Drive
artifacts exist, none trashed, and the 17 that differ in size are exactly the 17 documents on
the re-upload worklist that haven't been done yet. That is the expected baseline established
last week, not rot.

One item carries over unfixed from 08-23: the Drive-folder link in `command-broker/corpus.md`
line 31 still points at an owner-only folder. It is the only live `drive.google.com` link in
any published repo. See §4.

---

## 1. Navigation site — clean

Checked in Chrome at `https://scubanuke.github.io/dba-en-navigation/?cb=2026-08-26`, with a
second random cache-buster on each HEAD request.

| Check | Result | Baseline |
|---|---|---|
| Drive links | **0** | 0 ✓ |
| Unique publications links | **39** (47 anchors) | 39 ✓ |
| HTTP status | **39/39 → 200** | all 200 ✓ |

The 8 non-publications anchors are four in-page fragments (`#electric`, `#gas`, `#oil`,
`#series-intro`) and three sibling-site links — unchanged from last week.

**Served content verified current.** Every one of the 38 linked PDFs returned a
`content-length` matching its MANIFEST row exactly: 0 mismatches, and no linked document
absent from the manifest. The CDN is serving the regenerated files, not pre-5-August copies.

Local `dba-en-navigation` is at `8e733f3`, working tree clean, agreeing with the deployed site.

---

## 2. Mirror vs. Drive — 17 known mismatches, all expected

All 43 rows carrying a `drive_id` checked via the Drive connector.

- **Existence: 43/43 present.** None deleted or trashed. Owner is `scubanuke@gmail.com`
  throughout.
- **Size vs. manifest: 26 match, 17 differ.**
- Four rows (DBA-MA-SMR-FC1, DBA-MA-SMR-FC1-TB1, CB-CT, DBA-VC) have no `drive_id` and were
  not Drive-checked, by design.

### Why 17 is the right number

Since 08-23 the manifest's `bytes` column records the **published repo copy**, not the Drive
artifact. 32 documents had drifted; Tim re-uploaded Groups 1–2 (12 files) on 08-24. So the
expected residue is 32 − 12 − 3 (Group 7, no `drive_id`) = **17**. Observed: 17, and they are
precisely Groups 3–6 of `DRIVE_REUPLOAD_WORKLIST.md`.

| Document | repo / manifest | Drive | Δ | Worklist |
|---|---:|---:|---:|---|
| DBA-ES-GC-FC4_Compressor_Station.pdf | 287,185 | 264,202 | −22,983 | G3 |
| DBA-GAS_Sector_Framework.pdf | 218,449 | 330,217 | +111,768 | G3 |
| DBA-GAS-FC1_Natural_Gas_Transmission.pdf | 309,811 | 338,789 | +28,978 | G3 |
| DBA-GAS-FC2_Natural_Gas_Processing.pdf | 268,748 | 248,632 | −20,116 | G3 |
| DBA-GAS-FC3_Underground_Storage.pdf | 225,193 | 258,690 | +33,497 | G3 |
| DBA-GAS-FC4_Local_Distribution.pdf | 215,519 | 257,097 | +41,578 | G3 |
| DBA-GAS-UC-LNG_LNG_Terminal.pdf | 333,402 | 403,818 | +70,416 | G3 |
| DBA-OIL_Sector_Framework.pdf | 176,290 | 310,056 | +133,766 | G4 |
| DBA-OIL-FC1_Petroleum_Refining.pdf | 146,712 | 236,935 | +90,223 | G4 |
| DBA-OIL-FC2_Offshore_Crude_Production.pdf | 204,145 | 242,033 | +37,888 | G4 |
| DBA-OIL-FC3_Terminals_Storage.pdf | 208,445 | 249,596 | +41,151 | G4 |
| DBA-OIL-FC4_Crude_Product_Transport.pdf | 300,367 | 256,111 | −44,256 | G4 |
| CB-Framework_Cross_Sector.pdf | 112,534 | 110,486 | −2,048 | G5 |
| CB_Implementation_Guide.pdf | 154,083 | 150,355 | −3,728 | G5 |
| CB-IB_Qualification_Standard.pdf | 150,820 | 147,743 | −3,077 | G5 |
| CB-UC-1_BA_Integrated_Interface.pdf | 163,864 | 162,583 | −1,281 | G5 |
| GenAI_Risk_ICS.pdf | 171,642 | 232,763 | +61,121 | G6 |

**Fix:** finish Groups 3–6 in `DRIVE_REUPLOAD_WORKLIST.md` using *Manage versions → Upload new
version*. Do **not** run `scripts/fetch.py` against these — Drive is the stale side here, and
`--force` would revert 17 published documents.

### Groups 1–2 confirmed landed

All 12 files re-uploaded on 08-24 now match the manifest byte-for-byte, and every one retained
its original file ID, parent folder, and title. The version-replace method worked as intended;
nothing to redo.

---

## 3. Cited-and-canonical documents — clean on every axis

| Document | Path | Drive size | Repo | Live | Sharing |
|---|---|---:|---|---|---|
| Tiered Assessment Framework | `awb/` | 177,983 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| ERT Companion Proposal | `awb/` | 402,020 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| SCRM Companion Agent | `awb/` | 228,591 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| BES Asset Nomenclature Specification | `awb/` | 343,603 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| UA Grid Defense (canonical) | `papers/` | 481,245 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| AI Governance Series Overview | top level | 166,824 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |

None of the five NPEC-cited documents appears on the re-upload worklist, so none is affected by
§2. UA Grid Defense resolves to Drive file `1W1lzZWYXGXvKiHhAvODnfuWOYhKXBBbb` in folder
`1sV7Jw…` — the canonical copy, not the Energy-sector duplicate, as intended.

---

## 4. Carried over unfixed — one Drive link in `command-broker/corpus.md`

Still present at line 31 of the **`command-broker` repo** (not `publications`):

> The Proposer–Gate Pattern (v0.1) — not yet on the mirror … [Drive folder](…/1GWWFxu2N-QAGkVEOJxEcNFKBM_iIShDs)

Re-verified this run: that folder's permissions are **owner-only** (`scubanuke@gmail.com`,
no `anyone` entry). Anyone following the link hits a Google sign-in wall.

**Fix (preferred):** repoint to `https://scubanuke.github.io/publications/command-broker/`.
Alternatively drop the link and keep the surrounding "not yet on the mirror" prose. Sharing the
folder publicly would work but re-introduces a Drive dependency in published material — not
recommended.

A sweep of all five repos (`publications`, `ai-governance-course`, `command-broker`,
`dba-en-navigation`, `dba-ma-smr-portal`) found this as the only `drive.google.com` link in
tracked, published content. The four other hits are all in `publications` working notes that
have never been committed — see the caution in §5.

---

## 5. Repo integrity

- **MANIFEST vs. on-disk: 47/47 match.** Zero divergence — last week's reconciliation holds.
- **No stray PDFs.** Every PDF in the repo has a manifest row; every manifest row has a file.
- Last week's fixes to `MANIFEST.csv` and `scripts/fetch.py` are **still uncommitted** in the
  working tree (HEAD is `9763645`), alongside four untracked files — the worklist and three
  dated reports:

```
git add MANIFEST.csv scripts/fetch.py
git commit -m "Reconcile MANIFEST.csv with regenerated PDFs; guard fetch.py against overwrite"
```

Worth committing — the `fetch.py` write guard is the thing standing between a stray `--force`
and 17 reverted documents.

**One caution before committing the notes.** `DRIVE_REUPLOAD_WORKLIST.md` and the
`link-rot-report-*.md` files are currently untracked, which is why §4's sweep can say the
`corpus.md` link is the only Drive link in published content — these four discuss
`drive.google.com` in prose but have never been published. Committing them to a repo served by
Pages would put working notes (including Drive folder IDs) on the public site. Either keep them
untracked, move them to a `notes/` directory excluded from Pages, or add them to `.gitignore`.

---

## Checks not run

None. All three sections of the check completed: the navigation site via Chrome, the Drive
sweep via the Drive connector (43/43 metadata, 6/6 sharing on the cited set plus the Command
Broker folder), and the repo comparison locally. No file, repo, or Drive permission was
modified this run.

---

*Supersedes `link-rot-report-2026-08-23.md` as the current state; that report remains the
reference for why the `bytes` column means what it means.*
