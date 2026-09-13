# Zenodo Deposit Records — Batch 1

Copy-paste source for the five deposit forms. Create each as a draft, **reserve the DOI**, then paste
the reserved DOI into the table at the bottom and send it to me. The cover/citation edits happen after
that, so each document is exported exactly once.

> **Reconciliation update (August 2026).** The FD-BL corpus reconciliation conformed the corpus to the
> governing stack — **FD-BL** (definition), **FD-LD**, and the determinations **FD-BL-D1** (mode of
> discharge), **FD-BL-D2** (indication integrity), and **FD-EV** (envelope). Of the five records below,
> only **#1 Tiered Assessment Framework** changed as a result (an FD-BL by-reference conformance);
> **#2–#5 are unchanged** by the reconciliation. One deposit **outside this batch — the SMR Facility-Class
> Design Basis (DBA-MA-SMR-FC1)** — also changed and needs a new version; it is recorded in
> *Reconciliation re-versions* below. The published PDFs for the changed documents have been
> regenerated from the conformed sources.

**Applies to all five records:**

- **Creator:** Roxey, Timothy E. — ORCID `0009-0002-9482-8679`
- **Affiliation:** Eclectic Technologies *(free text)*
- **Publisher:** Eclectic Technologies
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Language:** English
- **Visibility:** Public

---

## 1. Tiered Assessment Framework

- **Title:** Tiered Assessment Framework for Cognitive Errors in Generative AI Systems: A Quality Assurance Methodology for Industrial Control Systems
- **Resource type:** Publication → Report
- **Version:** v2.8
- **Publication date:** 2026-09
- **Reconciliation status:** **Done** — conformed to FD-BL by reference; re-versioned and published as v2.6 (version DOI `10.5281/zenodo.21813691`, 5 Aug 2026), superseding v2.5 (`10.5281/zenodo.21363866`).
- **v2.7**, version DOI `10.5281/zenodo.22726006`, published 12 September 2026, superseding v2.6. It repairs the determinism/placement fusion at §2.4, qualifies the Mid band at six sites, reconciles the band definitions on the maloperation and loss-of-service entry routes, and carries an erratum notice naming both DOI-bearing predecessors. Its own revision history is defective: it holds no entry for v2.6 and its v2.7 entry retains an unremoved drafting sentence. Both are corrected by the successor and neither is edited in place.
- **Current version:** **v2.8**, version DOI `10.5281/zenodo.22726480`, published 12 September 2026, superseding v2.7. It conforms the error-axis vocabulary at thirty sites including five section headings, restoring the terms the Critical Infrastructure variant has carried since February 2026; removes the last use of *tier* on the application axis at §2.2; writes the missing v2.6 revision entry and records when the §2.2 bridging clause entered the lineage; and repairs a sentence fragment in the fourth objective proposed to NIST at §11.1. It carries a second erratum notice naming the revision-history defects of v2.7. **No published record is edited**: a version DOI names a fixed text, and the successor's notice is the remedy for a fixed text that is wrong.
- **Related identifiers:**
  - *is identical to* → `https://scubanuke.github.io/publications/awb/Tiered_Assessment_Framework.pdf`
- **Keywords:** generative AI; industrial control systems; quality assurance; cognitive error; critical infrastructure; NQA-1; IEC 61508; ISA/IEC 62443; NIST AI RMF; Bright Line; FD-BL

**Description:**
A quality assurance methodology for cognitive errors in generative AI systems deployed in industrial
control environments. Establishes a tiered criticality model, testing methodology, and statistical
acceptance criteria. It is the cognitive-error layer of a two-layer hybrid quality assurance
architecture, paired with formal verification for deterministic infrastructure components. Written
against ASME NQA-1, NRC Regulatory Guides, NERC CIP, IEEE 1012, IEC 61508, ISA/IEC 62443, and the
NIST AI Risk Management Framework, with the intent of converting framework content into enforceable
standards. Placement of the Bright Line is governed by FD-BL (consequence, per action), with the
criticality-tier framing an application of that definition.

---

## 2. BES Asset Nomenclature Specification

- **Title:** BES Asset Nomenclature Specification: A Comprehensive Framework for Bulk Electric System Asset Identification
- **Resource type:** Publication → Report
- **Version:** v1.1
- **Publication date:** 2026-08
- **Reconciliation status:** Unchanged by the FD-BL pass. Separately re-versioned to v1.1 (TOC removed) and published 30 Aug 2026 — version DOI `10.5281/zenodo.22178898`, superseding v1.0 (`10.5281/zenodo.21365015`). Mirror, Zenodo file and master are the same artifact.
- **Related identifiers:**
  - *is identical to* → `https://scubanuke.github.io/publications/awb/BES_Asset_Nomenclature_Specification.pdf`
- **Keywords:** bulk electric system; asset identification; nomenclature; control systems; protection systems; NERC; critical infrastructure

**Description:**
An identification framework for Bulk Electric System assets. Specifies human-comprehensible identifiers
that encode hierarchical relationships, spanning control system, computing platform, network
infrastructure, protection, and communication assets. Provides the common naming convention that
downstream assessment and supply-chain instruments assume.

---

## 3. UA Grid Defense: Cyber-Kinetic

- **Title:** UA Grid Defense: Cyber-Kinetic
- **Resource type:** Publication → Report
- **Version:** v1.0
- **Publication date:** 2026-06
- **Reconciliation status:** Unchanged.
- **Related identifiers:**
  - *is identical to* → `https://scubanuke.github.io/publications/papers/UA_Grid_Defense_Cyber_Kinetic.pdf`
- **Keywords:** Ukraine; grid defense; cyber-kinetic attack; electric infrastructure; design basis; military action

**Description:**
Analysis of Ukrainian grid defense under combined cyber and kinetic attack. Serves as the primary
evidentiary anchor for kinetic attack scenarios throughout the DBA-ES electric sector series.

*Note: the only document in the corpus carrying no DRAFT marker, and the most heavily cited.*

---

## 4. ERT Companion Proposal

- **Title:** ERT Companion Proposal: AI-Enhanced Evidence Request Tool — NERC CIP Compliance Automation Initiative
- **Resource type:** Publication → Preprint *(alternatively: Working paper)*
- **Version:** v5.3
- **Publication date:** 2026-03
- **Reconciliation status:** Unchanged.
- **Related identifiers:**
  - *is identical to* → `https://scubanuke.github.io/publications/awb/ERT_Companion_Proposal.pdf`
- **Keywords:** NERC CIP; compliance audit; evidence request tool; generative AI; regulatory automation; electric utilities

**Description:**
A pilot proposal for an AI-enhanced Evidence Request Tool supporting NERC CIP compliance audits. The
system automates population of the ERO Enterprise CIP ERT workbook rather than replacing it, providing
automated data extraction, traceable evidence packages, natural-language querying, and human-reviewed
narrative responses. The pilot uses a mock-audit approach with volunteer utility and Regional Entity
auditors before production deployment.

*Typed as a preprint: the proposal describes a pilot that has not yet run.*

---

## 5. SCRM Companion Agent

- **Title:** SCRM Companion Agent: AI-Enhanced Supply Chain Risk Management for Critical Infrastructure Protection
- **Resource type:** Publication → Preprint *(alternatively: Working paper)*
- **Version:** v1.0
- **Publication date:** 2026-03
- **Reconciliation status:** Unchanged.
- **Related identifiers:**
  - *is identical to* → `https://scubanuke.github.io/publications/awb/SCRM_Companion_Agent.pdf`
- **Keywords:** supply chain risk management; SBOM; HBOM; bulk power system; generative AI; multi-agent systems; procurement; vulnerability assessment

**Description:**
A multi-agent architecture for supply chain risk management in the bulk power system. Six specialized
generative AI agents integrate with existing procurement, inventory control, configuration management,
and operations/maintenance platforms to provide continuous hardware and software bill-of-materials
visibility across operational technology environments, reducing vulnerability assessment time from
weeks to minutes. Includes operational use cases, pilot structure, and governance framework.

*Typed as a preprint: describes a proposed deployment, not a delivered system.*

---

## 6. FD — Foundational Definitions, August 2026 Edition

- **Title:** FD — Foundational Definitions, August 2026 Edition
- **Resource type:** Publication → Report
- **Version:** August 2026 Edition
- **Publication date:** 2026-08-30
- **Version DOI:** `10.5281/zenodo.22181029` · **Concept DOI:** `10.5281/zenodo.22181028`
- **Status:** **PUBLISHED** 30 Aug 2026. Seven files; MD5s verified byte-identical to the mirror at
  `fd/` and to the production masters.
- **Related identifiers:**
  - *is referenced by* → `10.5281/zenodo.21813691` (TAF v2.6)
  - *is referenced by* → `10.5281/zenodo.21814883` (DBA-MA-SMR-FC1 v0.5)
  - Reciprocal *references* → `10.5281/zenodo.22181029` added to both of those records
    (metadata-only edit; no new version minted).
- **Keywords:** Bright Line; foundational definition; command broker; determinism; critical
  infrastructure; AI governance; ICS/OT

**Contents (six instruments plus front matter):**

| File | Instrument | Version |
|---|---|---|
| `00_FD_Foundational_Definitions_August_2026_Edition.pdf` | Front matter | August 2026 Edition |
| `01_FD-BL_The_Bright_Line_v0_3.pdf` | FD-BL — The Bright Line | v0.3 |
| `02_FD-LD_Layer_Decomposition_and_Determinism_v0_1.pdf` | FD-LD — Layer Decomposition and Determinism | v0.1 |
| `03_FD-EV_The_Envelope_v0_1.pdf` | FD-EV — The Envelope | v0.1 |
| `04_FD-BR_The_Broker_v0_1.pdf` | FD-BR — The Broker | v0.1 |
| `05_FD-BL-D1_Mode_of_Discharge_v0_3.pdf` | FD-BL-D1 — Mode of Discharge | v0.3 |
| `06_FD-BL-D2_Indication_Integrity_v0_2.pdf` | FD-BL-D2 — Indication Integrity | v0.2 |

**Note on the *is identical to* convention.** The five Batch 1 records each carry one
*is identical to* → mirror-URL row. That convention does not transfer to this record: it holds seven
files, so nothing is byte-identical to a single URL. The file-to-mirror mapping is carried in
`MANIFEST.csv` (series `fd`) instead.

**Which DOI to propagate.** The **version DOI** (`…22181029`) is the dated coherence claim — it is
what the citation block inside each of the seven PDFs prints, and what a conformed document should
cite when the claim is "reconciled against the August 2026 edition." The **concept DOI**
(`…22181028`) always resolves to the current edition and is what the publications index and
narrative references use.

---

## Reconciliation re-versions (post-conformance)

These deposits carry content the reconciliation **changed**, so each needs a **new version** published
under its **existing concept DOI** (the concept DOI is stable; Zenodo mints a fresh version DOI on upload).
The regenerated PDFs are already in the `publications` repo at the paths below.

| Document | Existing concept DOI | Prior version DOI | Status | PDF |
|---|---|---|---|---|
| Tiered Assessment Framework → **v2.6** | `10.5281/zenodo.21363865` | `10.5281/zenodo.21363866` | **DONE** — published, version DOI `10.5281/zenodo.21813691` | `awb/Tiered_Assessment_Framework.pdf` |
| Tiered Assessment Framework → **v2.7** | `10.5281/zenodo.21363865` | `10.5281/zenodo.21813691` | **DONE** — published, version DOI `10.5281/zenodo.22726006` | `awb/Tiered_Assessment_Framework.pdf` |
| Tiered Assessment Framework → **v2.8** | `10.5281/zenodo.21363865` | `10.5281/zenodo.22726006` | **DONE** — published 12 September 2026, version DOI `10.5281/zenodo.22726480`; vocabulary conformance and revision-history repair | `awb/Tiered_Assessment_Framework.pdf` |
| SMR Facility-Class Design Basis — DBA-MA-SMR-FC1 → **v0.5** | `10.5281/zenodo.21430410` | `10.5281/zenodo.21430411` | **DONE** — published, version DOI `10.5281/zenodo.21814883` | `dba-ma-smr/DBA-MA-SMR-FC1_SMR_Facility_Class_Design_Basis.pdf` |
| SMR Facility-Class Design Basis — DBA-MA-SMR-FC1 → **v0.9** | `10.5281/zenodo.21430410` | `10.5281/zenodo.21814883` | **DONE** — published 12 September 2026, version DOI `10.5281/zenodo.22730040`; carries the 3 September placement correction to the published layer. Versions 0.6–0.8 were working revisions and were not deposited. | `dba-ma-smr/DBA-MA-SMR-FC1_SMR_Facility_Class_Design_Basis.pdf` |
| BES Asset Nomenclature Specification → **v1.1** | `10.5281/zenodo.21365014` | `10.5281/zenodo.21365015` | **DONE** — published 30 Aug 2026, version DOI `10.5281/zenodo.22178898`; TOC removed, placeholder replaced with the real DOI | `awb/BES_Asset_Nomenclature_Specification.pdf` |

**Per-version steps (Zenodo UI — manual):** open the concept DOI → **New version** → reserve the version
DOI → confirm the citation block in the source reflects the reserved DOI → upload the regenerated PDF →
publish. Record the new version DOI in the table below.

---

## Reserved DOIs — fill in and return

| Document | Reserved version DOI | Concept DOI (after publish) |
|---|---|---|
| Tiered Assessment Framework v2.5 | 10.5281/zenodo.21363866 | 10.5281/zenodo.21363865 |
| BES Asset Nomenclature Specification v1.0 | 10.5281/zenodo.21365015 | 10.5281/zenodo.21365014 |
| UA Grid Defense: Cyber-Kinetic v1.0 | 10.5281/zenodo.21365171 | 10.5281/zenodo.21365170 |
| ERT Companion Proposal v5.3 | 10.5281/zenodo.21365218 | 10.5281/zenodo.21365217 |
| SCRM Companion Agent v1.0 | 10.5281/zenodo.21365262 | 10.5281/zenodo.21365261 |
| **TAF v2.6 — reconciliation re-version** | 10.5281/zenodo.21813691 | 10.5281/zenodo.21363865 |
| **DBA-MA-SMR-FC1 v0.5 — reconciliation re-version** | 10.5281/zenodo.21814883 | 10.5281/zenodo.21430410 |
| **BES v1.1 — TOC-removal re-version** | 10.5281/zenodo.22178898 | 10.5281/zenodo.21365014 |
| **TAF v2.7 — placement/derivation re-version** | 10.5281/zenodo.22726006 | 10.5281/zenodo.21363865 |
| **TAF v2.8 — vocabulary and revision-history re-version** | 10.5281/zenodo.22726480 | 10.5281/zenodo.21363865 |

Once the version DOIs are reserved, the citation block goes into each Word source, the PDFs are
exported once, uploaded to the reserved deposits, and published.
