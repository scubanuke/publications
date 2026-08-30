# Publication Link-Rot Check — 2026-08-23

**Verdict: one significant defect found and fixed during this run. Everything now resolves.**

The navigation site is fully clean live (39/39 links, HTTP 200, zero Drive links). All 43
Drive artifacts exist and are unchanged. The defect was in the *bookkeeping*: MANIFEST.csv
had silently stopped describing what is actually published, and `scripts/fetch.py` would
have reverted 32 live documents while reporting success. Both are corrected below.

**Read §5 and §6 before the next run.** The meaning of the `bytes` column has changed, so next
week's Drive comparison will behave differently. And a follow-up sharing audit (§6) found that
only 6 of 43 Drive files are publicly readable — long-standing and harmless to readers, but it
means `scripts/fetch.py` cannot verify the Drive mirror and shouldn't be expected to.

---

## 1. The defect — manifest described Drive, not the mirror *(fixed)*

Every `bytes` value in MANIFEST.csv matched its Drive artifact exactly (43/43). What no
longer matched was the **repo**: 32 of 47 mirrored PDFs differed in size from the manifest
row describing them.

Not Drive rot — the reverse of the failure mode this check was built to catch. The history:

| Commit | Date | Effect |
|---|---|---|
| `5920687` | 2026-08-05 | "Regenerate published PDFs from conformed sources; add footer" — rewrote **34 PDFs in place**. MANIFEST.csv *not* updated. |
| `0cc792b` | 2026-08-07 | Republished TAF v2.6, BES, SMR-FC1. Manifest not updated. |
| `9763645` | 2026-08-08 | "Refresh mirror for six revised documents" — re-fetched 6 files from Drive **and** updated their 6 manifest rows. |

The manifest was brought current only for the six documents that came back *from Drive*. The
32 regenerated *locally* on 5 August kept their pre-regeneration Drive byte counts.

### Why this mattered more than a dead link

`scripts/fetch.py` wrote each download to disk **and then** compared sizes — the write on
line 39 preceded the check on line 40. Run against the pre-fix manifest it would have:

1. **Overwritten all 32 regenerated PDFs** with older Drive copies, discarding the conformed
   sources and the governing-instruments footer, on documents that are live and cited.
2. **Reported complete success** — `43 ok, 0 size mismatches`, exit 0 — because Drive matched
   the manifest. The reversion would have left no trace in the output.

A stale citation is worse than a dead one; a silent reversion of a citation target is worse
still.

### Which copy was canonical — settled by evidence, not assumption

The live HEAD checks in §4 returned a `content-length` for every document. Those lengths match
the **regenerated on-disk sizes**, not the manifest's old Drive sizes:

| Document | old manifest | served by Pages | on disk |
|---|---:|---:|---:|
| DBA-EN_Series_Introduction.pdf | 243,950 | **182,826** | 182,826 |
| DBA-MA_Introduction.pdf | 230,261 | **123,145** | 123,145 |
| DBA-ES_Sector_Framework.pdf | 306,671 | **251,791** | 251,791 |

The regenerated PDFs are what readers and citers actually receive. They are canonical.

### What was changed

**`MANIFEST.csv`** — `bytes` updated to the on-disk size for the 32 divergent rows. Verified
mechanically that nothing else moved: `32 lines changed, 0 touched anything other than the
bytes field`. Manifest-vs-repo divergence is now **0 of 47**.

**`scripts/fetch.py`** — the write-before-check bug fixed. The download is now compared to the
manifest *before* anything touches the working tree, and a mismatching download is never
written; the script reports the mismatch, states the repo copy's size, and warns when the repo
copy is the one the manifest describes. Also added: `--force` for deliberate refreshes, an
explicit skip for the 4 rows with no `drive_id`, and a comment block recording the 5920687
history so the check is not reordered below the write again.

Both changes are staged in the working tree, uncommitted:

```
git add MANIFEST.csv scripts/fetch.py
git commit -m "Reconcile MANIFEST.csv with regenerated PDFs; guard fetch.py against overwrite"
```

---

## 2. Mirror vs. Drive — clean

All 43 rows carrying a `drive_id` checked via the Drive connector.

- **Existence: 43/43 present.** None deleted or trashed.
- **Byte counts vs. Drive: 43/43 matched** the manifest *as it stood at the start of this run*.
  No Drive-side revision has occurred. (This is no longer true of the corrected manifest — see §5.)
- Four rows (DBA-MA-SMR-FC1, DBA-MA-SMR-FC1-TB1, CB-CT, DBA-VC) have no `drive_id` and were not
  Drive-checked, by design. `fetch.py` now skips them explicitly rather than attempting a fetch.

---

## 3. Cited-and-canonical documents — clean on every axis

| Document | Path | Drive | Repo | Live | Sharing |
|---|---|---|---|---|---|
| Tiered Assessment Framework | awb/ | 177,983 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| ERT Companion Proposal | awb/ | 402,020 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| SCRM Companion Agent | awb/ | 228,591 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| BES Asset Nomenclature Specification | awb/ | 343,603 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |
| UA Grid Defense (canonical) | papers/ | 481,245 ✓ | ✓ | 200 ✓ | anyone-with-link reader ✓ |

All five exist, agree across Drive and repo, serve 200, and remain publicly readable with owner
`scubanuke@gmail.com`. These are among the six refreshed by `9763645`, which is why their rows
were already current while the other 32 were not — and why the five documents Stockton's NPEC
study cites were never at risk. They would have been exposed to the same reversion after any
future local regeneration; the `fetch.py` guard closes that.

---

## 4. Navigation site — verified live

Checked in Chrome at `https://scubanuke.github.io/dba-en-navigation/?cb=2026-08-23`, with a
second random cache-buster on each HEAD request to defeat CDN caching.

- **Drive links: 0.** No `drive.google.com` anchor anywhere. The public site remains decoupled
  from the personal Drive account.
- **Publications links: 39 unique** (47 anchors total), matching the expected baseline.
- **HTTP status: 39/39 returned 200.** No redirects, no 404s.
- Remaining anchors: four in-page fragments (`#electric`, `#gas`, `#oil`, `#series-intro`) and
  three sibling-site links (`ai-governance-course`, `command-broker`, `dba-en-navigation`).
- Deployed content confirmed current: served `content-length` values match the regenerated
  files on disk, so the CDN is not serving pre-5-August copies.

The local `dba-en-navigation` working copy (`HEAD` = `8e733f3`, 2026-08-07, clean) agrees with
the deployed site.

---

## 5. Note for the next run — the `bytes` column has changed meaning

Until today, `bytes` recorded **the size of the Drive artifact**, and `fetch.py`'s docstring
described it that way. As corrected, it records **the size of the published repo copy**. For
the 15 rows where Drive and repo agree these are the same number; for the other 32 they are not.

Consequences to expect:

1. **The Drive-vs-manifest comparison will report 32 mismatches next week.** That is the new
   expected baseline, not a regression. What would be a genuine finding is a mismatch on one of
   the *15* rows that currently agree, or any change in the set of 32.
2. **`fetch.py` will now report those 32 as MISMATCH and refuse to write them.** That is the
   guard working as intended. Use `--force` only after deciding Drive is the newer truth.

Two options to remove the ambiguity permanently, in order of preference:

- **Re-upload the 32 regenerated PDFs to Drive.** Origin and mirror realign, all 47 rows agree
  on a single number again, and `fetch.py` becomes a true round-trip check. Cleanest.
- **Split the column** into `bytes` (repo) and `drive_bytes` (origin), and have `fetch.py`
  compare against `drive_bytes`. Preserves both facts but adds a field to maintain.

Until one is done, this report's §2 and §1 measure different things and both are needed.

---

## 6. Sharing audit — all 43 files *(added 2026-08-24)*

A full `get_file_permissions` sweep was run after Tim re-uploaded Groups 1–2 of the Drive
worklist. Result: **only 6 of 43 Drive files are publicly readable.**

| Publicly readable (`anyone` / reader) | Location |
|---|---|
| Tiered Assessment Framework | `awb/` |
| ERT Companion Proposal | `awb/` |
| SCRM Companion Agent | `awb/` |
| BES Asset Nomenclature Specification | `awb/` |
| UA Grid Defense (canonical) | `papers/` |
| AI Governance Series Overview | top level |

The other 37 are owner-only, as are all five parent folders checked. Confirmed empirically:
a signed-out browser hitting `DBA-OIL_Sector_Framework`'s Drive link is redirected to a
Google sign-in wall rather than rendering the PDF.

**This is long-standing, not new, and not caused by the re-uploads.** Files never touched —
`DBA-GAS-POL_Deterrence`, `DBA-OIL_Sector_Framework` — are in the same state. The set of 6
maps exactly onto the documents needing citable public links, so it reads as deliberate:
Drive sharing was granted per-document where a citation required it, and public delivery for
everything else goes through GitHub Pages.

**Reader impact: none.** The navigation site carries zero Drive links and served 39/39 at 200
(§4). All five NPEC-cited documents are in the still-public set.

### Consequence for `scripts/fetch.py`

`fetch.py` downloads with unauthenticated `requests` against
`drive.google.com/uc?export=download`, which only succeeds on publicly-shared files. It can
therefore only ever have worked for those 6; the other 37 return Google's sign-in HTML, which
the script correctly rejects as `FAILED — not a PDF (sharing may have changed)`.

Making it pass for all 43 would require anyone-with-link on the whole corpus, re-coupling
published material to a personal Gmail account — the precise dependency the Pages architecture
removed. **Not recommended.** The Drive re-uploads remain worthwhile for archive fidelity;
they simply aren't verifiable by that script, and don't need to be.

This also revises §5's first option: re-uploading to Drive realigns the artifacts, but does not
make `fetch.py` a working round-trip check. Splitting the column, or accepting that `bytes`
describes the repo, remain the live options.

### One dead link found

`command-broker/corpus.md` line 31 links to the Command Broker Drive folder
(`1GWWFxu2N-QAGkVEOJxEcNFKBM_iIShDs`), which is owner-only — anyone following it hits a
sign-in wall. It is the only live `drive.google.com` link in any published repo. Fix by
pointing it at `https://scubanuke.github.io/publications/command-broker/` instead.

---

## Checks not run

Nothing outstanding. The sharing sweep deferred in the original run was completed on 08-24
and is recorded in §6 above.

---

*Changes made this run: `MANIFEST.csv` (32 byte values) and `scripts/fetch.py` (write guard),
both at Tim's explicit direction and both uncommitted pending review. No Drive file or
permission was modified. Supersedes `link-rot-report-2026-08-19.md`, which was misdated and
predates the fix.*
