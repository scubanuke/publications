# Drive Re-upload Worklist — 32 documents

> **Status — 2026-08-24**
> **Groups 1 and 2 are done and verified (12/12).** Correct sizes, original file IDs, folders
> and titles all preserved. Remaining: Groups 3–6 (17 files) and Group 7 (3 files).
>
> **The goal changed after a sharing audit — read "When you're done" before continuing.**
> `scripts/fetch.py` cannot verify this work, and trying to make it able to would undo the
> decoupling of the public site from your Drive account. The re-uploads are still worth
> finishing, but for archive fidelity, not for a round-trip check.

Goal: bring the Google Drive originals back in line with the regenerated PDFs that are
actually published, so the Drive copy of each document is the same artifact readers receive.

**Source of truth is the repo.** Every file listed below is at
`C:\Users\scuba\OneDrive\Documents\GitHub\publications\<path>`. Upload that exact file.

---

## Read this first — how to upload

Use **Manage versions → Upload new version** on the existing Drive file. Do **not** delete
the old file and upload a fresh one.

Deleting and re-uploading mints a **new file ID**, which would:

- break the `drive_id` in MANIFEST.csv for that row,
- invalidate any existing share link already circulated, and
- reset sharing to private, silently breaking public access.

Replacing the version keeps the ID, the link, and the anyone-with-link reader permission.

**Right-click the file → Manage versions → Upload new version → pick the repo copy.**

Sanity check after each one: reopen the file's details and confirm the size matches the
"new size" column. If it doesn't, the wrong file was picked.

---

## ~~Group 1 — Series introductions~~ *(3 files)* ✅ DONE

Drive folder ID `19FPs8jFiMbQKf-2YXbXx1A3kBEEWhn79` — verified 2026-08-24, all sizes confirmed.

| ☑ | Repo file | Drive file name | new size | old size |
|---|---|---|---:|---:|
| ☑ | `dba-en/DBA-EN_Series_Introduction.pdf` | DBA-EN_Series_Introduction_v0_1.pdf | 182,826 | 243,950 |
| ☑ | `dba-en/DBA-EN-SF_Energy_Sector_Framework.pdf` | DBA-EN-SF_Energy_Sector_Framework_v0_3.pdf | 286,854 | 274,276 |
| ☑ | `dba-ma/DBA-MA_Introduction.pdf` | DBA-MA_Introduction_v1_9.pdf | 123,145 | 230,261 |

## ~~Group 2 — Electric sector (DBA-ES)~~ *(9 files)* ✅ DONE

Drive folder ID `1tlhQYKWjqVgynKjmrwIk-VKJpLrvRMf6` — verified 2026-08-24, all sizes confirmed.

| ☑ | Repo file | Drive file name | new size | old size |
|---|---|---|---:|---:|
| ☑ | `dba-en/DBA-ES_Sector_Framework.pdf` | DBA-ES-Sector_Framework_v0_8.pdf | 251,791 | 306,671 |
| ☑ | `dba-en/DBA-ES-HY-FC1_Hydroelectric_Storage.pdf` | DBA-ES-HY-FC1_v0_4.pdf | 263,235 | 359,105 |
| ☑ | `dba-en/DBA-ES-TX-FC2_EHV_Substation.pdf` | DBA-ES-TX-FC2_EHV_Substation_v0_1.pdf | 205,075 | 266,339 |
| ☑ | `dba-en/DBA-ES-TX-FC3_HVDC_Interconnect.pdf` | DBA-ES-TX-FC3_HVDC_Interconnect_v0_1.pdf | 213,400 | 261,504 |
| ☑ | `dba-en/DBA-ES-DI-FC5_Distribution_Edge_Generation.pdf` | DBA-ES-DI-FC5_Distribution_Edge_Generation_v0_1.pdf | 170,523 | 232,508 |
| ☑ | `dba-en/DBA-ES-CntlCo_Control_Company.pdf` | DBA-ES-CntlCo_v0_1.pdf | 225,713 | 219,373 |
| ☑ | `dba-en/DBA-ES-GN-FC6_Coal_Generation.pdf` | DBA-ES-GN-FC6_Coal_Generation_v0_1.pdf | 174,185 | 250,214 |
| ☑ | `dba-en/DBA-ES-GN-FC7_Oil_Fired_Generation.pdf` | DBA-ES-GN-FC7_Oil_Fired_Generation_v0_1.pdf | 178,816 | 254,927 |
| ☑ | `dba-en/DBA-ES-GN-FC8_Renewable_Generation_BESS.pdf` | DBA-ES-GN-FC8_Renewable_Generation_BESS_v0_1.pdf | 197,367 | 262,594 |

The version-replace method worked exactly as intended: every file kept its original ID,
folder, and title. Use the same method for the rest.

## Group 3 — Gas sector + compressor station *(7 files)*

Drive folder ID `1-d_Bw6tCfOdyC0FOefhkMZYn0vgZjYWm`

| ☐ | Repo file | Drive file name | new size | old size |
|---|---|---|---:|---:|
| ☐ | `dba-en/DBA-ES-GC-FC4_Compressor_Station.pdf` | DBA-ES-GC-FC4_Compressor_Station_v0_2.pdf | 287,185 | 264,202 |
| ☐ | `dba-en/DBA-GAS_Sector_Framework.pdf` | DBA-GAS-Sector_Framework_v1_6.pdf | 218,449 | 330,217 |
| ☐ | `dba-en/DBA-GAS-FC1_Natural_Gas_Transmission.pdf` | DBA-GAS-FC1_Natural_Gas_Transmission_v1_5.pdf | 309,811 | 338,789 |
| ☐ | `dba-en/DBA-GAS-FC2_Natural_Gas_Processing.pdf` | DBA-GAS-FC2_Natural_Gas_Processing_v0_1.pdf | 268,748 | 248,632 |
| ☐ | `dba-en/DBA-GAS-FC3_Underground_Storage.pdf` | DBA-GAS-FC3_Underground_Storage_v0_1.pdf | 225,193 | 258,690 |
| ☐ | `dba-en/DBA-GAS-FC4_Local_Distribution.pdf` | DBA-GAS-FC4_Local_Distribution_v0_1.pdf | 215,519 | 257,097 |
| ☐ | `dba-en/DBA-GAS-UC-LNG_LNG_Terminal.pdf` | DBA-GAS-UC-LNG_v1_1.pdf | 333,402 | 403,818 |

Note: `DBA-GAS-POL_Deterrence.pdf` lives in this folder but is **not** on the list — it already matches.

## Group 4 — Oil sector *(5 files)*

Drive folder ID `1iO_lOV49poqhjYPc0NvV1BsXEeV3tnOh`

| ☐ | Repo file | Drive file name | new size | old size |
|---|---|---|---:|---:|
| ☐ | `dba-en/DBA-OIL_Sector_Framework.pdf` | DBA-OIL-Sector_Framework_v1_6.pdf | 176,290 | 310,056 |
| ☐ | `dba-en/DBA-OIL-FC1_Petroleum_Refining.pdf` | DBA-OIL-FC1_Petroleum_Refining_v1_2.pdf | 146,712 | 236,935 |
| ☐ | `dba-en/DBA-OIL-FC2_Offshore_Crude_Production.pdf` | DBA-OIL-FC2_Offshore_Crude_Production_v0_1.pdf | 204,145 | 242,033 |
| ☐ | `dba-en/DBA-OIL-FC3_Terminals_Storage.pdf` | DBA-OIL-FC3_Terminals_Storage_v0_1.pdf | 208,445 | 249,596 |
| ☐ | `dba-en/DBA-OIL-FC4_Crude_Product_Transport.pdf` | DBA-OIL-FC4_Crude_Product_Transport_v0_1.pdf | 300,367 | 256,111 |

This whole group is one Drive folder and all five are small — a good place to start if you
want an easy win first.

## Group 5 — Command Broker *(4 files)*

Drive folder ID `1GWWFxu2N-QAGkVEOJxEcNFKBM_iIShDs`

| ☐ | Repo file | Drive file name | new size | old size |
|---|---|---|---:|---:|
| ☐ | `command-broker/CB-Framework_Cross_Sector.pdf` | CB-Framework_Cross_Sector_v0_1.pdf | 112,534 | 110,486 |
| ☐ | `command-broker/CB_Implementation_Guide.pdf` | Command_Broker_Implementation_Guide_V0_1.pdf | 154,083 | 150,355 |
| ☐ | `command-broker/CB-IB_Qualification_Standard.pdf` | CB-IB_Qualification_Standard_v0_1.pdf | 150,820 | 147,743 |
| ☐ | `command-broker/CB-UC-1_BA_Integrated_Interface.pdf` | CB-UC-1_BA_Integrated_Interface_v0_1.pdf | 163,864 | 162,583 |

Note the repo and Drive names differ for the Implementation Guide — match on content, not filename.

## Group 6 — Papers *(1 file)*

Drive folder ID `1nRblIv9XJFC4BGWS-AjNZX5QE5Ihmrqo`

| ☐ | Repo file | Drive file name | new size | old size |
|---|---|---|---:|---:|
| ☐ | `papers/GenAI_Risk_ICS.pdf` | GenAI_Risk_ICS_V29.pdf | 171,642 | 232,763 |

---

## Group 7 — Not in Drive at all *(3 files, different job)*

These three changed in the repo but have **no `drive_id`** in the manifest — they have never
been mirrored from Drive. They need a *fresh upload*, not a version replace, and then some
follow-up.

| ☐ | Repo file | size |
|---|---|---:|
| ☐ | `dba-ma-smr/DBA-MA-SMR-FC1_SMR_Facility_Class_Design_Basis.pdf` | 249,852 |
| ☐ | `command-broker/CB-CT_Commissioning_and_Joint_Training.pdf` | 118,734 |
| ☐ | `command-broker/DBA-VC_Vendor_Companion.pdf` | 263,708 |

For each: upload to the matching Drive folder, set sharing to **anyone with the link → Viewer**,
copy the new file ID out of the URL, and paste it into the `drive_id` column of the
corresponding MANIFEST.csv row. Leave them out of Drive entirely if you'd rather — they work
fine as repo-only documents, they just stay outside the Drive round-trip check.

A fourth no-`drive_id` row, `DBA-MA-SMR-FC1-TB1`, is unchanged and needs nothing.

---

## When you're done — revised 2026-08-24

**Do not expect `scripts/fetch.py` to verify this work. It can't, and that's not fixable
without a tradeoff you probably don't want.**

A sharing audit of all 43 Drive files found that only **6 are publicly readable**:

| Publicly readable (`anyone` / reader) | Location |
|---|---|
| Tiered Assessment Framework | `awb/` |
| ERT Companion Proposal | `awb/` |
| SCRM Companion Agent | `awb/` |
| BES Asset Nomenclature Specification | `awb/` |
| UA Grid Defense (canonical) | `papers/` |
| AI Governance Series Overview | top level |

The other **37 are owner-only**, as are all parent folders. This is long-standing, not
something the re-uploads caused — files never touched are in the same state. The set of 6
maps exactly onto the documents that needed citable public links (the four NPEC-cited
documents, UA Grid Defense, and the series overview), which suggests it was deliberate.

Confirmed empirically: opening a non-public file's Drive link in a signed-out browser
redirects to a Google sign-in wall rather than rendering.

### Why this breaks the round-trip check

`fetch.py` downloads with unauthenticated `requests` against
`drive.google.com/uc?export=download`. That only succeeds on publicly-shared files. Run it
today and you get roughly `6 ok, 37 FAILED — not a PDF (sharing may have changed)`. The
failures are the sign-in HTML page being correctly rejected, not a problem with your uploads.

Making it pass would require setting anyone-with-link on all 43 — which re-couples the
published corpus to a personal Gmail account, the precise thing the GitHub Pages
architecture was built to avoid. **Not recommended.**

### So what is the re-upload for?

Archive fidelity. It keeps Drive an accurate origin copy of what's actually published, so the
two never silently drift again. That's worth having on its own. It just isn't machine-verifiable
from outside, and doesn't need to be — GitHub Pages is the delivery path, and the weekly
link-rot check already validates it live.

### Verification that does work

- **Per-file, as you go:** reopen the file's details in Drive and confirm the size matches the
  "new size" column. That's what confirmed Groups 1 and 2.
- **Whole-set:** ask for a Drive metadata sweep in a session with the Drive connector — it reads
  authenticated and sees all 43 regardless of sharing.

Partial progress is safe. The `fetch.py` write guard means a half-finished state can't corrupt
anything, and this list stays accurate for whatever's left.

---

## Separate issue found during the audit

`command-broker/corpus.md` line 31 links to the Command Broker **Drive folder**
(`1GWWFxu2N-QAGkVEOJxEcNFKBM_iIShDs`). That folder is owner-only, so anyone following the link
hits a sign-in wall. It's the only live `drive.google.com` link anywhere in the published repos —
the navigation site itself has zero.

Options, in order of preference:

1. **Point it at the Pages mirror instead** — `https://scubanuke.github.io/publications/command-broker/`.
   Consistent with the decoupling, nothing to maintain.
2. **Drop the link**, keeping the surrounding "not yet on the mirror" prose.
3. **Share the folder** anyone-with-link reader — works, but re-introduces a Drive dependency
   in published material.
