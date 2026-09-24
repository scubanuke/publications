# Zenodo Deposit Records — Batch 3: the DBA-MA International Ladder

Prepared 24 September 2026. Copy-paste source for four deposit forms. The order follows the DOI Framework:

    reserve DOI → edit cover + citation block → export PDF → upload → publish → record concept DOI

**Status, 24 September 2026: PUBLISHED.** All four records are live. Files verified byte-identical to the mirror for L1, L2 and L3 by MD5 from the live record pages (L4 page unread, rate-limited). Concept DOIs recorded below follow Zenodo's first-deposit pattern (version DOI minus one), to be confirmed by Tim against each record's "Cite all versions" line before this commit is pushed. Index cards added under "DBA-MA international ladder"; MANIFEST rows added.

All four are **first deposits**, not New Versions. None of these documents has a Zenodo record or a file in the mirror today.

These four go together because they cite one another. The parent (L1) defines the framework, the six threat categories and the seven engineering principles. L2 states the accident and its design requirements, L3 the trigger framework, and L4 the monitoring that feeds the triggers. Depositing the parent alone would publish a document whose §10 and §11 point at three children no reader could obtain, which is the defect the FD August 2026 Edition was minted to close.

---

## Applies to all four records

- **Creator:** Roxey, Timothy E — ORCID 0009-0002-9482-8679 (type the digits only, no backticks, label or URL) (no trailing period)
- **Affiliation:** Eclectic Technologies *(free text)*
- **Publisher:** Eclectic Technologies
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Language:** English
- **Visibility:** Public
- **Resource type:** Publication → Report
- **Publication date:** 2026-09
- **Version:** L1 `v2.0`; L2, L3 and L4 `v3.0`. Type the leading "v" and check the field after saving: the BES draft showed "a1.1" in August.
- **Related works, all four:** one row, relation *Is identical to*, scheme URL, the mirror URL given in each record. Enter these under **Related works**, not the free-text **References** box, which prints on the public record as typed and should stay empty.
- **Related works, family:** each record *references* the others it cites, listed per record. Zenodo does not add the reciprocal, so each is entered by hand on both records once all four DOIs exist.
- **Series folder in the mirror:** `dba-ma/`, beside DBA-MA-CDB and the DBA-MA Introduction. Filenames carry identity, not version.

**A caution that applies to the titles and descriptions.** The filenames and running headers of this ladder use "IAEA" as a level designation, meaning the international, jurisdiction-neutral tier above the national children. On Zenodo that word could be read as authorship. None of the titles below uses it, and every description states that the document is an independent proposal written in the vocabulary of the IAEA standards, not an IAEA publication. Keep it that way in any field you edit.

---

## 1. DBA-MA International Framework (L1)

- **Title:** Expanding the Design Basis for Nuclear Power Plants to Address Military Action Against Nuclear Facilities: An International Framework
- **Version:** v2.0 (first final version)
- **Mirror URL:** `https://scubanuke.github.io/publications/dba-ma/L1_DBA-MA_IAEA_Framework.pdf` (new)
- **Related works (References):** now — DOI 10.5281/zenodo.21430410 (DBA-MA-SMR-FC1); after all four DOIs exist — L2, L3, L4
- **Keywords:** nuclear safety; military action; design basis; design extension condition; Zaporizhzhia; Autonomous Safe Shutdown Condition; local sovereignty; uncrewed aerial systems; geopolitical siting; critical infrastructure

**Description:**
The parent framework of the DBA-MA series. It proposes bringing military action against nuclear facilities into the design basis of nuclear power plants, drawing on the Russia–Ukraine conflict and the IAEA's findings at the Zaporizhzhia Nuclear Power Plant, where the Director General reported all seven pillars of nuclear safety and security compromised at once. The framework argues that military action falls between the IAEA's safety standards and its security guidance and should be addressed as a safety design problem: the facility cannot defeat the military threat, so it must survive the conditions the threat creates. It sets out six threat categories and seven engineering principles, defines the Autonomous Safe Shutdown Condition as a new plant state, describes a three-tier trigger framework with the plant's standing authority to shut down, adds a geopolitical stability dimension to siting, and places military action in the IAEA hierarchy as a design extension condition analysed with the discipline of the design basis. It is an independent proposal written in the vocabulary of the IAEA standards; it is not an IAEA publication.

---

## 2. DBA-MA L2 — Formal Accident Description and Design Requirements

- **Title:** Design Basis Accident: Military Action Against Nuclear Facilities — Formal Accident Description and Design Requirements
- **Version:** v3.0 (first final version)
- **Mirror URL:** `https://scubanuke.github.io/publications/dba-ma/L2_DBA-MA_IAEA_Accident_Description.pdf` (new)
- **Related works (References):** now — DOI 10.5281/zenodo.21430410 (DBA-MA-SMR-FC1); after all four DOIs exist — L1, L3, L4
- **Keywords:** design basis accident; military action; nuclear power plant; Autonomous Safe Shutdown Condition; acceptance criteria; decay heat removal; spent fuel pool; hardening; post-occupation recovery

**Description:**
The formal accident description for military action against nuclear power facilities, issued under the DBA-MA International Framework. It postulates military operations by a hostile state and describes the accident as four phases: preparation, transition, sustained operation in the Autonomous Safe Shutdown Condition, and recovery, including the reassessment of a plant after hostile occupation. It defines the Autonomous Safe Shutdown Condition and its required characteristics, sets design-basis durations by facility class (not less than two years for large light-water reactors; a 72-hour class floor for near-term integral light-water small modular reactors), states the acceptance criteria, and gives the seven governing engineering principles with the categories of specific engineering requirements they generate. It is an independent proposal written in the vocabulary of the IAEA standards; it is not an IAEA publication.

---

## 3. DBA-MA L3 — Trigger Framework

- **Title:** Trigger Framework for Military Action Design Basis Accident: Observable Indicators and Decision Criteria for Transition to Autonomous Safe Shutdown Condition
- **Version:** v3.0 (first final version)
- **Mirror URL:** `https://scubanuke.github.io/publications/dba-ma/L3_DBA-MA_IAEA_Trigger_Framework.pdf` (new)
- **Related works (References):** after all four DOIs exist — L1, L2, L4
- **Keywords:** trigger framework; military action; nuclear power plant; observable indicators; shutdown decision; decision authority; local sovereignty; uncrewed aerial systems; grid coordination

**Description:**
The trigger framework for the DBA-MA accident. It resolves the dilemma of a plant that may be needed for national defense and civilian supply yet must not be operating when it is attacked, by replacing judgment under pressure with pre-defined observable criteria. Three tiers, strategic warning, elevated threat and imminent threat, each carry observable indicators, including drone activity, and required actions ending in mandatory transition to the Autonomous Safe Shutdown Condition. The framework gives plant management standing authority to act on its own indicators at every tier, a floor that national direction may add to but never precondition, and holds that grid reliability cannot override the Tier 3 shutdown. It is an independent proposal written in the vocabulary of the IAEA standards; it is not an IAEA publication.

---

## 4. DBA-MA L4 — Monitoring Sources and Data-Sharing Guidance

- **Title:** Monitoring Sources and Data-Sharing Guidance for DBA-MA Trigger Observables
- **Version:** v3.0 (first final version)
- **Mirror URL:** `https://scubanuke.github.io/publications/dba-ma/L4_DBA-MA_IAEA_Monitoring_Guidance.pdf` (new)
- **Related works (References):** after all four DOIs exist — L1, L2, L3
- **Keywords:** threat monitoring; information sharing; ISAC; nuclear power plant; asset owner/operator; security clearance; readiness assessment; uncrewed systems; review cycle

**Description:**
Implementation guidance for asset owners and operators on the monitoring sources and data-sharing agreements needed to observe the DBA-MA trigger indicators before a crisis rather than during one. For each strategic-warning indicator it identifies internal monitoring, external government sources, required agreements and commercial supplements, and it provides an agreement and relationship readiness assessment for self-assessment. It sets out immediate, near-term and industry-level actions, including a proposed coordination protocol between military, intelligence and regulatory authorities and nuclear operators; the operational mechanics of the review cycle for the uncrewed-systems threat characterization; and post-strike inspection and restoration of passive kinetic barriers. It is jurisdiction-neutral; national programs are named in the national child documents. It is an independent proposal written in the vocabulary of the IAEA standards; it is not an IAEA publication.

---

## The citation block, to be stamped

The four masters currently carry a provisional "Suggested citation" paragraph at the head of the first body page, with placeholders for the concept and version DOIs. The stamping pass replaces it with the Framework's form, as used in Batch 2: three centered lines on the cover, below the organization line.

    T. Roxey, "<Title>," Version <X.Y>, Eclectic Technologies, September 2026.
    DOI: https://doi.org/10.5281/zenodo.<reserved version DOI>
    Current version: https://scubanuke.github.io/publications/dba-ma/<mirror file>

A concept DOI does not exist until a record is first published, so it is not printed; the mirror path serves the same purpose. The provisional paragraph is deleted, not left beside the stamped block.

**Render pipeline.** The `dba-ma/` and `dba-ma-smr/` mirror PDFs are LibreOffice renders (Liberation Serif, no Producer string), not Acrobat PDFMaker exports; the DBA-MA-SMR-FC1 v0.9 deposit of 12 September followed that rule. The house-faithful render for this batch is therefore `soffice --headless --convert-to pdf`, which Claude runs. The Acrobat-from-Word rule belongs to the `awb/` and `papers/` series.

---

## Reserved DOIs — fill in and send back

| # | Document | Reserved version DOI | Concept DOI (after publish) |
|---|---|---|---|
| 1 | L1 — DBA-MA International Framework v2.0 | 10.5281/zenodo.22944855 | 10.5281/zenodo.22944854 |
| 2 | L2 — Formal Accident Description and Design Requirements v3.0 | 10.5281/zenodo.22945300 | 10.5281/zenodo.22945299 |
| 3 | L3 — Trigger Framework v3.0 | 10.5281/zenodo.22945421 | 10.5281/zenodo.22945420 |
| 4 | L4 — Monitoring Sources and Data-Sharing Guidance v3.0 | 10.5281/zenodo.22945520 | 10.5281/zenodo.22945519 |

## Sequence after reservation

1. Tim: create four new uploads (New upload, not New version), fill the fields above, reserve a DOI on each, save as draft, and send the four version DOIs.
2. Claude: stamp each master's cover with its citation block, delete the provisional paragraph, render the four PDFs with LibreOffice, check fonts and page counts, and place them in the mirror at the paths above.
3. Tim: upload each PDF to its reserved draft, check the Version field, and publish.
4. Claude: add the family *references* rows once all four DOIs are live; record the concept DOIs in the table above; update MANIFEST.csv and the index.html cards; confirm byte-identity against Zenodo.
5. Tim: push from GitHub Desktop.
6. Afterward: the NPEC paper for Henry Sokolski replaces its DBA-MA reference with the L1 DOI.
