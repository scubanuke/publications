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
- **Version:** v2.5
- **Publication date:** 2026-02
- **Reconciliation status:** **Changed** — conformed to FD-BL by reference (placement is consequence, per action; the tier framing is an application of it). Re-export the regenerated PDF; publish as a **new version** under the existing concept DOI.
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
- **Version:** v1.0
- **Publication date:** 2026-02
- **Reconciliation status:** Unchanged.
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

## Reconciliation re-versions (post-conformance)

These deposits carry content the reconciliation **changed**, so each needs a **new version** published
under its **existing concept DOI** (the concept DOI is stable; Zenodo mints a fresh version DOI on upload).
The regenerated PDFs are already in the `publications` repo at the paths below.

| Document | Existing concept DOI | Prior version DOI | Action | Regenerated PDF |
|---|---|---|---|---|
| Tiered Assessment Framework (v2.5, conformed) | `10.5281/zenodo.21363865` | `10.5281/zenodo.21363866` | New version → reserve DOI, upload regenerated PDF, publish | `awb/Tiered_Assessment_Framework.pdf` |
| SMR Facility-Class Design Basis — DBA-MA-SMR-FC1 (v0.4, conformed) | `10.5281/zenodo.21430410` | `10.5281/zenodo.21430411` | New version → reserve DOI, upload regenerated PDF, publish | `dba-ma-smr/DBA-MA-SMR-FC1_SMR_Facility_Class_Design_Basis.pdf` |

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
| **TAF — reconciliation re-version** | *(reserve on New version)* | 10.5281/zenodo.21363865 |
| **DBA-MA-SMR-FC1 — reconciliation re-version** | *(reserve on New version)* | 10.5281/zenodo.21430410 |

Once the version DOIs are reserved, the citation block goes into each Word source, the PDFs are
exported once, uploaded to the reserved deposits, and published.
