# Zenodo Deposit Records — Batch 2: the Always-On Paper Family

Prepared 17 September 2026. Copy-paste source for seven deposit forms. The order follows the DOI Framework:

    reserve DOI → edit cover + citation block → export PDF → upload → publish → record concept DOI

**Status, 17 September 2026:** seven DOIs reserved and recorded in the table below. The stamping pass is done: every master carries the cover citation block with its reserved version DOI, the stale draft dispositions are corrected, and the per-record corrections listed below are applied. Next step is Tim’s: export each master to PDF from Word and upload it to its reserved draft.

These papers go out as the Margins Release run (Release-02 to Release-05), interleaved with the Friday posts. The Release gate requires each paper's DOI to be live **before** the post that introduces it.

---

## Applies to all seven records

- **Creator:** Roxey, Timothy E — ORCID `0009-0002-9482-8679` (no trailing period)
- **Affiliation:** Eclectic Technologies *(free text)*
- **Publisher:** Eclectic Technologies
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Language:** English
- **Visibility:** Public
- **Publication date:** 2026-09
- **Version:** the stamped version, as recorded in the reserved-DOI table below: Gen Mix v0.7, Always-On v0.7, The Asset and the Target v0.12, Keeping the Lights On v0.8, Fuel Cell v0.4, UFLS v0.7, Regulatory Gap v1.7.
- **Related identifiers, all seven:** *is identical to* → the mirror URL given in each record.
- **Related identifiers, family:** each record *references* the others it cites. The references are listed per record. Zenodo does not add the reciprocal automatically, so each one is entered by hand on both records.

---

## 1. Generation Mix Optimization Under Competing Objectives

- **Title:** Generation Mix Optimization Under Competing Objectives: A Parametric Framework for Climate and Resilience Tradeoffs
- **Resource type:** Publication → Working paper
- **Mirror URL:** `https://scubanuke.github.io/publications/papers/GenMix_Optimization_Whitepaper.pdf` (replaces the v0.3 file already served at that path)
- **References:** The Asset and the Target; Keeping the Lights On
- **Keywords:** generation mix; data centers; continuous load; nuclear; firmed LCOE; productive utilization; fuel independence; grid inertia; Pareto frontier; critical infrastructure resilience

**Description:**
An engineering framework for evaluating electricity generation sources against three objectives at once: carbon intensity, capital recovery and physical resilience. It is written for the continuous load that hyperscale data centers place on the bulk electric system. Eight parameters for eight source types feed a climate optimization, a capital-recovery analysis and a resilience vector covering inertia, fuel independence duration and equipment recovery time. The framework finds that nuclear is the only source satisfying all three for this load profile. It carries a qualifier: units that share a dependency can meet every test the framework expresses and still fail together, which the companion paper The Asset and the Target develops. The regulatory pathways for fuel independence and transformer recovery are identified as open questions under Section 215 of the Federal Power Act, not as settled routes.

**Cover corrections before stamping:** none beyond the citation block.

---

## 2. Powering the Always-On Economy

- **Title:** Powering the Always-On Economy: A Plain-Language Guide to Generation Mix Decisions for Continuous Load
- **Resource type:** Publication → Working paper
- **Mirror URL:** `https://scubanuke.github.io/publications/papers/Powering_the_Always_On_Economy.pdf` (replaces v0.4)
- **References:** Generation Mix Optimization; The Asset and the Target
- **Keywords:** data centers; investment; generation mix; nuclear; firmed cost; productive utilization; fuel independence; transformer reserve; shared dependency

**Description:**
The investor-facing presentation of the generation-mix framework, without the derivations. It explains why levelized cost misleads the continuous-load decision, how productive utilization and firmed cost change the comparison, and why fuel independence and equipment recovery time belong in an investment case. It also sets out three regulatory gaps that current adequacy standards do not address. The central finding is stated with its qualifier: nuclear passes every test the framework can express, and shared dependency is a test that the adversarial analysis in The Asset and the Target added.

**Cover corrections before stamping:** strike "Draft for author review." from the audience line.

---

## 3. The Asset and the Target

- **Title:** The Asset and the Target: Concentration, Consequence, and the Generation Mix That Serves Continuous Load
- **Resource type:** Publication → Working paper
- **Mirror URL:** `https://scubanuke.github.io/publications/papers/The_Asset_and_the_Target.pdf` (new)
- **References:** Generation Mix Optimization; Powering the Always-On Economy; Fuel Cell Technologies; Predictive UFLS Ride-Through; Keeping the Lights On
- **Keywords:** adversarial analysis; critical infrastructure protection; common-cause failure; independence classes; effective granularity; small modular reactors; islanding; declared residual; design basis

**Description:**
The adversarial analysis that the generation-mix framework left as forward work. It shows that the defender choosing a portfolio and the adversary choosing a target read the same parameter table and select the same asset for the same reasons. It then adds what the framework could not express: units sharing a control architecture, firmware baseline, switchyard, gas lateral or islanding boundary form one independence class, however many of them there are. The paper works through illustrative portfolios and sets out what adoption asks of a developer. That means a declared dependency set built largely from estimates, independent review of it, a computed count of independence classes, and a declared residual for every class without independent protection. The method is published and site-specific detail is withheld. No utility, facility or site is named.

**Cover corrections before stamping:**
- Strike "Complete draft for author review."
- Replace "a policy and infrastructure-protection treatment is planned separately" with a reference to Keeping the Lights On, which now exists.

**Gate before minting:** this is the family's targeting method, going to a general audience. It needs the same cleared-line review that Bright Line Nos. 4 and 5 received. Claude will run that review during the stamping pass and report anything that goes past method into the particulars of a specific facility.

---

## 4. Keeping the Lights On for Everything That Can't Go Dark

- **Title:** Keeping the Lights On for Everything That Can't Go Dark: Always-On Infrastructure, the Grid It Depends On, and Who Must Act
- **Resource type:** Publication → Working paper
- **Mirror URL:** `https://scubanuke.github.io/publications/papers/Keeping_the_Lights_On.pdf` (new)
- **References:** Generation Mix Optimization; Powering the Always-On Economy; The Asset and the Target; Fuel Cell Technologies; Predictive UFLS Ride-Through; The Regulatory Gap in Commercial Data Center Physical Security
- **Keywords:** critical infrastructure policy; always-on infrastructure; time to harm; large loads; Section 215; Federal Power Act; NERC; FERC; transformer reserve; cross-sector dependency; NIPP

**Description:**
A policy paper for congressional and agency staff, published as a partial draft. It defines always-on infrastructure by time to harm, traces how shared dependencies make many facilities fail together, and shows how large always-on loads have become a source of grid disturbance. Its evidence is the July 2024 and July 2026 load transfer events, the second close to the Eastern Interconnection's largest design contingency. Parts One through Five are written. Part Four sets out seven recommendations, each with its limit. Part Five names the trade-offs. Part Six, which sorts the asks by legal authority, and the Findings and Asks section are held pending a legal reading of Section 215 of the Federal Power Act. The paper divides its ground with The Regulatory Gap in Commercial Data Center Physical Security.

**Cover corrections before stamping:**
- Replace "Draft for author review, not for distribution." with "Partial draft: Part Six and Findings and Asks are held for a legal reading of Section 215."
- In the closing verification paragraph, replace "Seven items must be closed before this draft is distributed." with "Seven items remain open in this draft, and later versions will close them."

---

## 5. Fuel Cell Technologies for Continuous Load Applications

- **Title:** Fuel Cell Technologies for Continuous Load Applications: A Position Paper
- **Resource type:** Publication → Working paper
- **Mirror URL:** `https://scubanuke.github.io/publications/papers/Fuel_Cell_Position_Paper.pdf` (replaces v0.1)
- **References:** Generation Mix Optimization; Powering the Always-On Economy; The Asset and the Target; Keeping the Lights On; Predictive UFLS Ride-Through
- **Keywords:** hydrogen fuel cells; continuous load; data centers; desalination; ride-through; onsite resilience; nuclear electrolysis; backup generation

**Description:**
A position paper placing hydrogen fuel cells as the second tier of a two-tier resilience architecture for continuous load. Primary grid-connected generation forms the first tier, and onsite stored energy measured in days forms the second. The paper examines grey, blue and green hydrogen pathways, the pairing of nuclear generation with electrolysis, and the state of demonstration. It sets out the condition that the two tiers must not share a dependency that can defeat both. It identifies three policy gaps and states that not all of them can be closed under existing authority.

**Cover corrections before stamping:** strike "Draft for author review. Not for distribution until the always-on paper family is aligned."

---

## 6. Predictive UFLS Ride-Through Extension via PMU Wavefront Analysis

- **Title:** Predictive UFLS Ride-Through Extension via PMU Wavefront Analysis: A Gaussian Process Learning Framework for Inertia-Conditioned Protection Coordination
- **Resource type:** Publication → Preprint
- **Mirror URL:** `https://scubanuke.github.io/publications/papers/Predictive_UFLS_Ride_Through.pdf` (new)
- **References:** The Asset and the Target; FD — Foundational Definitions (for FD-LS)
- **Keywords:** under-frequency load shedding; ride-through; PRC-024; phasor measurement units; FWHM; Gaussian process regression; protection coordination; local sovereignty; computational loads

**Description:**
A proposal for extending generator frequency ride-through when a local measurement predicts that an excursion will resolve inside the ride-through window. The paper conjectures that the full width at half maximum of the frequency wavefront at a local phasor measurement unit encodes the duration of the local excursion. It proposes a Gaussian process model that learns that mapping at each location and activates extension only under worst-case posterior uncertainty. The decision is made from local power and local measurement alone. The paper proposes a validation method against the 2008 Flagami event and states that no simulation has been run. It outlines a model-based alternative compliance pathway under NERC PRC-024.

**Cover and text corrections before stamping** (author-only preprint, per Tim's decision of 17 September 2026):
- Strike "Submitted to: IEEE Power and Energy Magazine" and "DRAFT — For reviewer circulation. Not for distribution."
- Recast co-author references in the introduction as the author's own account; Bob Cummings's 2023 IEEE paper stays cited as reference 11, as prior work.
- Section 6.4 "none is in prospect from the authors" becomes "from the author".
- Section 7.4: remove "Bob Cummings is the identified contact for the NERC standards engagement."
- Remove the reviewer questions appendix, which is internal working material that names reviewers and invites co-authorship.

---

## 7. The Regulatory Gap in Commercial Data Center Physical Security

- **Title:** The Regulatory Gap in Commercial Data Center Physical Security: Legislative Argument, Policy Instruments, and the CIKR Logical Predicate
- **Resource type:** Publication → Working paper
- **Mirror URL:** `https://scubanuke.github.io/publications/dba-dc/DBA-DC-POL_Policy_Companion.pdf` (new; series folder dba-dc, beside FC1). Current master: v1.6.
- **References:** Keeping the Lights On; DBA-DC-FC1 Hyperscale Design Basis (published in the mirror, no DOI)
- **Keywords:** data centers; physical security; critical infrastructure; CIKR; legislation; CISA; foreign ownership; NERC CIP comparison; large-load interconnection

**Description:**
The policy companion to the Design Basis Accident — Military Action Data Center and AI Infrastructure Series, document DBA-MA-DC-L2-P-001. It makes the legislative case for mandatory physical security standards at commercial data centers, including those hosting government and military workloads. The argument runs from the federal designation of data centers as critical infrastructure, through the absence of any mandatory standard, audit or enforcement authority, to a three-part offer: executive action within existing authority, congressional authorization, and an industry compact. Its grid interconnection conformance condition requires new statutory direction. The paper divides its ground with Keeping the Lights On for Everything That Can't Go Dark.

**Cover and text corrections before stamping:**
- Strike "UNCLASSIFIED // FOR OFFICIAL ANALYTICAL USE" from the audience line (Tim's decision of 17 September 2026).
- **Both Section 4 items are closed in v1.6 (17 September 2026).** The five findings now cite the public reporting and name DBA-MA-DC-L3-001 as the document that assembles that record rather than as its only source, so a reader holding the DOI can verify each fact from the press. The military AI paragraph no longer asserts that a named vendor's model is in military use: it reports the assertion as the adversary's stated rationale, records that the vendor behind those systems changed during 2026, and rests the argument on the infrastructure.
- **Still open for Tim:** the April strike dates. The document gives 1 March, 1 April and 2 April 2026. Public reporting confirms 1 March and places further strikes in the first days of April, with 1 April as the date of the threat against seventeen named companies. Pin the April dates to a source, or reword to "and again in early April", before minting.

---

## The citation block, as stamped

Each cover now carries three centered lines below the organization line:

    T. Roxey, "<Title>," Version <X.Y>, Eclectic Technologies, September 2026.
    DOI: https://doi.org/10.5281/zenodo.<reserved version DOI>
    Current version: https://scubanuke.github.io/publications/<mirror path>

The DOI Framework's citation block prints a concept DOI on the third line. A concept DOI does not exist until a record is first published, so for a first deposit that line would have to be a placeholder, and a placeholder printed inside a DOI-bearing PDF is the defect the BES record carried in August. The mirror path serves the same purpose: it always resolves to the current file. When each record is published, its concept DOI is recorded in the table below and printed on the third line at the next revision.

## Reserved DOIs — fill in and send back

| # | Document | Reserved version DOI | Concept DOI (after publish) |
|---|---|---|---|
| 1 | Generation Mix Optimization | 10.5281/zenodo.22818157 | 10.5281/zenodo.22818156 |
| 2 | Powering the Always-On Economy | 10.5281/zenodo.22818280 | 10.5281/zenodo.22818279 |
| 3 | The Asset and the Target | 10.5281/zenodo.22818332 | 10.5281/zenodo.22818331 |
| 4 | Keeping the Lights On | 10.5281/zenodo.22818372 | 10.5281/zenodo.22818371 |
| 5 | Fuel Cell Technologies | 10.5281/zenodo.22818385 | 10.5281/zenodo.22818384 |
| 6 | Predictive UFLS Ride-Through | 10.5281/zenodo.22818438 | 10.5281/zenodo.22818437 |
| 7 | Regulatory Gap in Data Center Physical Security | 10.5281/zenodo.22818458 | 10.5281/zenodo.22818457 |

## Sequence after reservation

1. Claude: one pass per paper. Apply the corrections above, stamp the citation block in the Framework's form, bump the version, run the cleared-line review of The Asset and the Target, and commit the masters to Always-On Paper Family and DBA-ES-CL Critical Loads.
2. Tim: export each master to PDF from Word (Acrobat PDFMaker, the house pipeline for the papers series), upload to its reserved draft, set the Version field, publish.
3. Claude: copy the published PDFs into the mirror at the paths above; update MANIFEST.csv, index.html cards and this file; confirm byte-identity against Zenodo.
4. Tim: push from GitHub Desktop.
5. Release-02 can then be drafted against live DOIs.
