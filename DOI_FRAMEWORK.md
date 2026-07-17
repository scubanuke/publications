# DOI Framework — Eclectic Technologies Publications

Status: agreed 14 July 2026. Governs how documents in this mirror receive permanent identifiers.

## Why

Every public citation of this work currently resolves to a URL — either a Google Drive file ID in a
personal Gmail account, or (since 14 July 2026) a GitHub Pages URL in this repository. Both are
addresses that depend on an account continuing to exist. A DOI does not. It is the only layer in the
stack that survives the author.

The mirror solved *link stability*. The DOI solves *durability and citability*.

## The unit is the document, not the repository

Zenodo's GitHub integration mints one DOI per repository release. That is the wrong granularity here:
citations in Paul Stockton's NPEC study, in the AI Governance course, and in Behr's forthcoming column
point at individual documents. Each document therefore gets its own Zenodo record.

## Two DOIs per document

| | What it is | Where it goes |
|---|---|---|
| **Version DOI** | Pins one exact file. Never changes, never re-points. | Printed in the PDF's own citation block. A reader holding v2.5 gets v2.5. |
| **Concept DOI** | Always resolves to the newest version of that document. | The README index, the DBA-EN site, the course Notes — anywhere "the current document" is meant. |

This mirrors the discipline already in force: filenames carry identity, cover pages carry version.

**Ordering matters.** Zenodo lets you *reserve* a version DOI on a draft deposit before uploading any
file, specifically so the identifier can be printed inside the document. That is what makes a single
export pass possible:

    reserve DOI → edit cover + citation block → export PDF → upload → publish → record concept DOI

Do it in any other order and every document gets exported twice.

## Batch 1 — the cited set

These five are cited in published or forthcoming work. They are the batch.

| Document | Version | Resource type | Rationale |
|---|---|---|---|
| Tiered Assessment Framework | v2.5 | Report | Anchor methodology; cited; standards-track intent. |
| BES Asset Nomenclature Specification | v1.0 | Report | A specification. Stable by nature. |
| UA Grid Defense: Cyber-Kinetic | v1.0 | Report | Evidentiary analysis; the only document in the corpus with no DRAFT marker. |
| ERT Companion Proposal | v5.3 | Preprint / working paper | Genuinely proposal-stage: proposes a pilot that has not run. |
| SCRM Companion Agent | v1.0 | Preprint / working paper | Same — pilot structure, not a delivered system. |

Everything else in the mirror stays as it is for now, publicly readable at a stable Pages URL, without
a DOI. Nothing is blocked by that.

## Prerequisite — cover corrections

A DOI is permanent. These five documents must not contradict their own DOI. Before minting:

| Document | Correction |
|---|---|
| Tiered Assessment Framework | Strike `(unpublished)` from the citation block. Replace `Status: Draft for Review and Comment`. |
| ERT Companion Proposal | Strike `(unpublished)`. |
| SCRM Companion Agent | Strike `(unpublished)`. |
| BES Asset Nomenclature Specification | Strike `(unpublished)`. |
| UA Grid Defense | None. Already clean. |

`(unpublished)` printed inside a document that carries a public DOI is self-refuting. It is the single
most important thing to fix, and it is the reason the DOIs must be reserved before the export.

Separately, and outside this batch: the **Command Broker Implementation Guide** cover reads
"DRAFT for Internal Review" while being served publicly. Not in the DOI batch, but it should be
corrected on the same pass.

## Citation block to print in each PDF

Replacing the current "(unpublished)" form:

> T. Roxey, "<Title>," Version <X.X>, Eclectic Technologies, <Month> 2026.
> DOI: https://doi.org/10.5281/zenodo.<reserved>
> Current version: https://doi.org/10.5281/zenodo.<concept>

The version DOI is what the reader is holding. The concept DOI is how they find out it has been superseded.

## Record metadata — applied to all five

- **Creator:** Timothy E. Roxey — ORCID [0009-0002-9482-8679](https://orcid.org/0009-0002-9482-8679).
- **Affiliation:** Eclectic Technologies (free-text field; ET is not a registered ROR entity).
- **Publisher:** Eclectic Technologies.
- **Publication date:** the document's cover date, not the upload date.
- **Version:** as printed on the cover (v2.5, v1.0, v5.3).
- **License:** CC BY 4.0 — already elected.
- **Related identifiers:**
  - `is identical to` → the document's GitHub Pages URL in this mirror.
  - `is part of` → the series, once a series record exists.
  - `references` → other documents in the corpus that the text actually cites.
- **Keywords:** critical infrastructure, industrial control systems, design basis, AI governance,
  bulk electric system, NERC CIP — plus per-document terms.

## ORCID

**0009-0002-9482-8679** — registered 14 July 2026. Checksum validated.

The author-side equivalent of what the DOI does for the documents: a permanent identifier that binds
this body of work to a person rather than to an email address. Log in to Zenodo *via* ORCID rather than
with an email and password — published records then bind to the iD automatically.

Eclectic Technologies is carried as a free-text affiliation. It is not a ROR-registered entity, which
has no effect on the DOIs.

## Versioning policy

A revision to any document with a DOI is published as a **new version** of the existing Zenodo record —
never as a new record. This preserves the concept DOI and keeps every prior version permanently
retrievable. It is the same rule as `Manage versions` in Drive and same-path replacement in this
mirror: one document, one identity, many versions.

## Sequence

1. ~~Register ORCID.~~ **Done — 0009-0002-9482-8679.**
2. Create Zenodo account, log in via ORCID. *(Tim)*
3. Create five draft deposits; reserve a version DOI on each; record them. *(Tim — I can prepare the metadata.)*
4. Correct covers and citation blocks in the Word sources; export PDFs. *(Claude, given access to the sources.)*
5. Upload PDFs to the reserved deposits; publish. *(Tim.)*
6. Refresh Drive copies via Manage versions — preserves file IDs. *(Tim.)*
7. Re-run `scripts/fetch.py`, refresh MANIFEST byte counts, commit. *(Claude.)*
8. Add concept DOIs to the README index and the DBA-EN site cards. *(Claude.)*

Steps 2, 3, 5 and 6 require an account holder's hands. The rest is mechanical.
