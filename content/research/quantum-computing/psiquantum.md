---
title: "PsiQuantum"
date: 2026-04-07
lastmod: 2026-04-07
draft: false
description: "Silicon photonics quantum computing startup pursuing fault-tolerant photonic computing by manufacturing integrated chipsets at GlobalFoundries; the most heavily funded independent quantum hardware company with no publicly demonstrated quantum processor as of early 2026."
tags: ["quantum-computing", "photonic", "fault-tolerant-research", "us", "australia"]
categories: ["company"]
research_area: "quantum-computing"
source_urls:
  - "https://www.psiquantum.com"
  - "https://www.nature.com/articles/s41586-025-08820-7"
  - "https://arxiv.org/abs/2101.09310"
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC9938229/"
  - "https://www.darpa.mil/research/programs/quantum-benchmarking-initiative"
  - "https://www.industry.gov.au/news/leading-quantum-company-chooses-australia-site-its-groundbreaking-utility-scale-quantum-computer"
  - "https://www.anao.gov.au/work/request/investigation-the-investment-psiquantum-announced-the-australian-and-queensland-governments"
  - "https://www.businesswire.com/news/home/20260210565444/en/PsiQuantum-Appoints-Victor-Peng-as-Interim-CEO-Co-Founder-Jeremy-OBrien-to-Become-Executive-Chairman"
last_reviewed: 2026-04-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

PsiQuantum is a private quantum computing company headquartered in Palo Alto, CA, pursuing fault-tolerant photonic quantum computing using silicon photonics manufactured in a commercial semiconductor foundry (GlobalFoundries Fab 8, Malta, NY). Founded in 2016 by four researchers from the University of Bristol and Imperial College London photonics groups, PsiQuantum has raised approximately $2.32 billion in total funding — making it the most heavily funded independent quantum hardware company in the world — while publicly demonstrating no operational quantum processor as of April 2026. The asymmetry between capital raised and demonstrated hardware is a defining fact of the company's history, and readers should weigh it accordingly when evaluating claims about the company's progress.

## Key Facts

- **Founded:** 2016
- **Headquarters:** Palo Alto, CA, USA
- **Type:** Private company
- **Stage:** Late-stage private (~$7B valuation as of September 2025, unverified — private company; no independent audit)
- **Total funding raised:** ~$2.32B across 8 rounds (as of September 2025), including $940M AUD (~$617M USD at time of announcement) from Australian and Queensland governments (April 2024), and $1B Series E (September 2025)
- **Hardware modality:** Photonic (silicon photonics, fusion-based quantum computing, FBQC)
- **Strategy:** Skip NISQ entirely; target fault-tolerant quantum computing (FTQC) at utility scale
- **Key partnership:** GlobalFoundries (Fab 8, 300mm wafers)
- **Key government partnership:** Australian federal government + Queensland state government
- **DARPA status:** Selected for final validation phase of QBI US2QC program (February 2025)
- **Publicly demonstrated quantum processor:** None as of April 2026
- **Status:** Active — Chicago construction begun (September 2025); Brisbane facility delayed

## What It Is / How It Works

PsiQuantum's technical approach centers on linear optical quantum computing (LOQC) — specifically, a variant called fusion-based quantum computing (FBQC) invented by co-founder Terry Rudolph. In FBQC, small constant-size entangled "resource states" are generated and then combined via projective entangling measurements called "fusions" to construct a larger cluster state on which universal quantum computation is performed. Unlike superconducting or trapped-ion approaches, photonic qubits do not need to be persistently stored in a controlled physical environment — photons naturally avoid many thermal noise issues that plague other modalities. This is a genuine theoretical advantage.

The platform uses silicon photonics manufactured on 300mm wafers at GlobalFoundries' Fab 8 facility in Malta, New York. PsiQuantum's Omega chipset — announced February 2025 and described in a peer-reviewed Nature paper (volume 641, 2025) — integrates three key component types on a single chip: single-photon sources (using spontaneous four-wave mixing in silicon nitride resonators), superconducting single-photon detectors (using niobium nitride), and electro-optic switches (using barium titanate, BTO). BTO is an advanced material PsiQuantum manufactures on 300mm wafers at its own California facility, which are then integrated with GlobalFoundries wafers. This hybrid manufacturing flow is unusual and adds supply chain complexity.

GlobalFoundries provides credible high-volume semiconductor manufacturing capability — Fab 8 is a mature 300mm facility with well-established process control. This is a meaningful differentiator from quantum hardware startups that build their own small-scale custom fabs. However, manufacturing the photonic chip to semiconductor-grade yields is only one layer of the full system. What happens after the chip — photon routing, cryogenic operation of superconducting detectors, classical control systems, error correction processing — remains largely unpublished and undemonstrated at system scale. The company's claims about scalability rest on projections from chip-level metrics, not system-level demonstrations.

### Why the "Skip NISQ" Bet Is High Risk

PsiQuantum's thesis is that photonic fault-tolerant quantum computing can leapfrog NISQ-era approaches without needing to demonstrate incremental intermediate-scale utility. The argument has theoretical merit: photonic qubits are well-suited for erasure error correction (photon loss maps cleanly to a known error type, which fault-tolerant codes handle better than depolarizing noise), and the silicon photonics manufacturing thesis — if achievable — would allow production at scales no other modality can match.

The risk is that the technical prerequisites for fault-tolerant operation are severe and none have been demonstrated at the required scale. PsiQuantum's Nature 2025 paper shows chip-level fidelities (99.98% SPAM, 99.22% two-qubit fusion fidelity) that are promising, but these figures are conditional on photon detection — they do not account for photon loss. The loss problem is fundamental: photon loss effectively destroys a qubit. PsiQuantum's June 2025 arXiv study on loss-tolerant FBQC designs found that advanced adaptive schemes can raise loss thresholds to approximately 15–18.8% — but current silicon photonics waveguide loss at the scale required for a million-qubit system has not been demonstrated at these thresholds across a full system. Each chip-to-chip interconnect, each grating coupler, each switch adds loss. For fault tolerance, all of these loss channels must be kept collectively below the threshold.

The physical qubit count required for a fault-tolerant photonic system is also very large. Surface code or FBQC error correction on photons requires generating and routing enormous numbers of physical photons per logical gate — estimates in the literature suggest on the order of 10⁸ photons per second or more at the system level. This resource state generation overhead is a consequence of the probabilistic nature of linear optical gates (unlike superconducting qubits, photons cannot be forced to interact deterministically). No demonstration of resource state generation at the required rate and fidelity exists in the public literature as of April 2026.

## Notable Developments

- **2026-03:** PsiQuantum announced NVIDIA CUDA-Q integration with its Construct simulation platform, enabling GPU-accelerated quantum algorithm simulation (up to 450× vs. CPU). *(Unverified — press release only)*
- **2026-02:** Victor Peng (former President of AMD, former CEO of Xilinx) appointed Interim CEO; Jeremy O'Brien transitions to Executive Chairman. PsiQuantum stated it is conducting a search for a permanent CEO. *(Verified — press release and multiple news sources)*
- **2026-01:** PsiQuantum appointed three new members to its Government Advisory Board. *(Unverified — press release only)*
- **2025-11:** Phase one construction begins on the Chicago IQMP (Illinois Quantum and Microelectronics Park) facility. Phase one includes office space, a data hall, and a cryogenic plant; expected completion 2027. *(Partially verified — multiple news sources, no independent confirmation of construction status)*
- **2025-09:** $1B Series E funding closed, led by BlackRock, Temasek, and Baillie Gifford. Valuation reported at $7B. New investors include NVIDIA (NVentures), Qatar Investment Authority, Macquarie Capital, Ribbit Capital, Counterpoint Global (Morgan Stanley). *(Verified — company announcement and multiple financial news sources)*
- **2025-09:** PsiQuantum broke ground at Chicago IQMP site (September 30, 2025). *(Partially verified — company announcement and Chicago press)*
- **2025-08:** Australian federal government internal audit (McGrathNicol) concluded: "approach and processes were appropriate," though market testing planning "could have been improved." High financial risk noted. *(Verified — DISR public release)*
- **2025-06:** arXiv study on loss-tolerant FBQC designs published, introducing Loss Per Photon Threshold (LPPT) metric. Advanced adaptive methods reach LPPT of ~15–18.8%. *(Partially verified — arXiv preprint, not yet confirmed as peer-reviewed publication)*
- **2025-02:** Nature paper "A manufacturable platform for photonic quantum computing" published (Nature 641, 876–883, 2025). Demonstrates chip-level metrics: 99.98% SPAM fidelity, 99.50% HOM visibility, 99.22% two-qubit fusion fidelity — all conditional on photon detection, not accounting for loss. *(Verified — peer-reviewed, Nature)*
- **2025-02:** DARPA selected PsiQuantum and Microsoft for the final validation phase of the Underexplored Systems for Utility-Scale Quantum Computing (US2QC) program under QBI. *(Verified — DARPA press release)*
- **2025-02:** Omega chipset announced — integrates single-photon sources, superconducting single-photon detectors, and BTO optical switches on a single manufacturable platform. *(Partially verified — company announcement consistent with Nature paper; full system operation not independently confirmed)*
- **2024-04:** Australian federal government and Queensland state government announce A$940M (~$617M USD) joint investment in PsiQuantum, contingent on establishing regional headquarters in Brisbane and operating quantum computer from there. *(Verified — government press releases)*
- **2024-01 (elected):** Newly elected Queensland government announces review of prior funding commitment. Internal audit subsequently cleared the deal process; the investment remained active as of September 2025. *(Verified — multiple Australian news sources)*
- **2023-02:** "Fusion-based quantum computation" published in Nature Communications (Bartolucci et al., 2023) — the foundational architecture paper. *(Verified — peer-reviewed, Nature Communications)*
- **2021-09:** Series D funding (~$450M); valuation reached $3.15B at that time. Earlier investors include Founders Fund, M12 (Microsoft Ventures), Blackbird, Baillie Gifford. *(Partially verified — widely reported, exact figures vary by source)*
- **2021-01:** FBQC preprint first posted to arXiv (arXiv:2101.09310). *(Verified — arXiv)*
- **2016:** Company founded in Palo Alto by Jeremy O'Brien, Terry Rudolph, Pete Shadbolt, and Mark Thompson — all from the Bristol/Imperial College photonics research community.

## Key People

### Jeremy O'Brien — Executive Chairman (Co-Founder)
- **LinkedIn:** [linkedin.com/in/jeremy-o-brien-39482631](https://www.linkedin.com/in/jeremy-o-brien-39482631)
- **Google Scholar / institutional:** [University of Bristol profile archived; Bristol Centre for Quantum Photonics (QET Labs)]
- **Background:** Born 1975, Australia. BS and PhD from University of New South Wales. Postdoctoral research at University of Queensland and University of Toronto. Professor of Physics and Electrical Engineering at University of Bristol (2004–2016); Director, Centre for Quantum Photonics / QET Labs, Bristol. Adjunct Professor at Stanford. Co-founder and CEO of PsiQuantum from 2016; transitioned to Executive Chairman February 2026.
- **Academic record:** ~150 publications, ~40,000 citations (as of publicly stated figures). Demonstrated first photonic two-qubit logic gate; credited with founding integrated quantum photonics as a subfield.
- **⚑ Note:** O'Brien's transition from CEO to Executive Chairman in February 2026, concurrent with a search for a permanent CEO, is a significant governance event. The stated rationale was enabling O'Brien to focus on strategy and partnerships while Peng manages operations.

### Terry Rudolph — Chief Architect (Co-Founder)
- **LinkedIn:** not found via public search
- **Background:** Professor of Quantum Physics at Imperial College London prior to co-founding PsiQuantum. Inventor of fusion-based quantum computing (FBQC). Author or co-author on foundational LOQC and FBQC theory papers. Ph.D. background in quantum foundations and quantum information theory.
- **⚑ Bristol/Imperial overlap:** Rudolph's Imperial College affiliation overlapped with O'Brien's Bristol work through the UK quantum photonics academic community — the four co-founders were collaborators before founding PsiQuantum.

### Pete Shadbolt — Co-Founder and Chief Scientific Officer
- **LinkedIn:** [linkedin.com/in/peteshadbolt](https://www.linkedin.com/in/peteshadbolt) — *Note: URL requires verification; mark as TODO if incorrect*
- **Background:** PhD in experimental photonic quantum computing from the University of Bristol (2014). Postdoctoral researcher at Imperial College London researching photonic quantum computing theory. Co-founder of PsiQuantum from 2016.
- **⚑ Bristol origin:** Direct PhD student in the Bristol photonics group (O'Brien's lab). The four co-founders represent a single Bristol/Imperial academic cluster.

### Mark Thompson — Co-Founder and Chief Technologist
- **LinkedIn:** not found via public search
- **Background:** Over 20 years of experience in photonic and quantum technologies. Formerly at the University of Bristol, where he worked on silicon photonics and quantum photonic devices.
- **⚑ Bristol origin:** Part of the same Bristol photonics group as O'Brien and Shadbolt.

### Victor Peng — Interim CEO (appointed February 2026)
- **LinkedIn:** [linkedin.com/in/victorpeng](https://www.linkedin.com/in/victorpeng) — *TODO: verify exact LinkedIn slug*
- **Background:** More than 40 years of semiconductor industry experience. CEO of Xilinx (2018–2022). President of Advanced Micro Devices, Inc. (AMD) (February 2023–August 2024, retired). Board member at multiple technology companies. Not from the quantum computing field — brings semiconductor manufacturing and operations scaling expertise.
- **⚑ Note:** Peng's appointment is notable because his background is in classical semiconductor manufacturing and operations, not quantum physics. This may signal a shift in PsiQuantum's phase from research-focused to construction/operations-focused, consistent with the Chicago groundbreaking. It may also reflect investor pressure to add experienced operational leadership ahead of large capital deployment.

### People — Last Reviewed: 2026-04-07

## Claim Verification

### Claim: 99.98% state preparation and measurement (SPAM) fidelity for photonic qubits
**Status:** Partially verified

**Supporting sources:**
- [Nature 641, 876–883 (2025)](https://www.nature.com/articles/s41586-025-08820-7) — peer-reviewed publication reporting 99.98% ± 0.01% SPAM fidelity on the Omega chipset manufactured at GlobalFoundries

**Refuting / questioning sources:**
- No independent replication in public literature as of April 2026. The result has not been reproduced by an independent lab.
- The fidelity figure is conditional on photon detection — it does not account for photon loss. A chip with 99.98% conditional SPAM fidelity can still have a low effective fidelity if the photon detection probability is low.

**Summary:** The result is peer-reviewed and credibly demonstrated at the chip level, but not independently replicated, and the loss caveat is material for system-level extrapolation.

---

### Claim: 99.22% two-qubit fusion fidelity
**Status:** Partially verified

**Supporting sources:**
- [Nature 641, 876–883 (2025)](https://www.nature.com/articles/s41586-025-08820-7) — same paper; 99.22% ± 0.12% fidelity on dual-rail fusion, conditional on photon detection

**Refuting / questioning sources:**
- Conditional-on-detection fidelity is not the same as the effective gate fidelity in a full circuit where photon loss can occur. No peer-reviewed independent replication exists.
- For fault-tolerant operation, what matters is the fidelity integrated over the full loss budget of the system — not on a small test circuit with ideal detection efficiency.

**Summary:** Peer-reviewed chip-level result. Conditional caveat is significant and is explicitly noted in the paper itself. No independent replication.

---

### Claim: Silicon photonics manufactured at GlobalFoundries enables "million-qubit scale" quantum computers
**Status:** Unverified

**Supporting sources:**
- [Nature 641, 876–883 (2025)](https://www.nature.com/articles/s41586-025-08820-7) — demonstrates a manufacturable chipset platform; GlobalFoundries involvement confirmed
- [GlobalFoundries press release](https://gf.com/dresden-press-release/psiquantum-and-globalfoundries-build-worlds-first-full-scale-quantum-computer/) — partnership confirmed

**Refuting / questioning sources:**
- No million-qubit-scale system has been built, designed at the full system level in public literature, or demonstrated in any form. The claim is a projection from chip-level manufacturing feasibility.
- The leap from "we can manufacture good photonic chips" to "we can build a million-qubit computer" requires solving photon routing at massive scale, classical control systems, error correction processing at extremely high clock rates, and cryogenic operations for the superconducting detectors — none of which has been demonstrated at relevant scale in the public literature.

**Summary:** Manufacturing partnership is verified. The million-qubit claim is an extrapolation from chip-level results, not a demonstrated capability. State it as an architecture goal, not an achieved milestone.

---

### Claim: Loss per photon thresholds of 15–18.8% achievable with adaptive FBQC schemes
**Status:** Partially verified (company research, not independently replicated)

**Supporting sources:**
- [PsiQuantum arXiv preprint (June 2025)](https://thequantuminsider.com/2025/06/17/psiquantum-study-maps-path-to-loss-tolerant-photonic-quantum-computing/) — theoretical/simulation study evaluating FBQC design space, introducing the LPPT metric

**Refuting / questioning sources:**
- This is a company-authored theoretical study; as of April 2026 it has not been independently reproduced.
- The claimed loss thresholds apply to idealized designs in simulation. Whether real silicon photonics waveguides, switches, and routing at system scale can achieve the required loss budgets has not been demonstrated.
- Traditional photonic NISQ-era approaches without encoding manage LPPT below 1%, indicating how large the engineering gap is.

**Summary:** Theoretical result from company authors, not independently verified. The direction is credible; the specific thresholds are simulation results requiring experimental validation.

---

### Claim: A$940M Australian government investment
**Status:** Verified (as a government commitment; this is not technical validation)

**Supporting sources:**
- [Australian Department of Industry press release (April 2024)](https://www.industry.gov.au/news/leading-quantum-company-chooses-australia-site-its-groundbreaking-utility-scale-quantum-computer) — federal government announcement
- [McGrathNicol audit released August 2025](https://ia.acs.org.au/article/2025/govt-s-psiquantum-deal-given-all-clear-by-internal-audit.html) — confirmed deal process as appropriate

**Refuting / questioning sources:**
- The [Australian National Audit Office (ANAO) investigation](https://www.anao.gov.au/work/request/investigation-the-investment-psiquantum-announced-the-australian-and-queensland-governments) was launched, indicating ongoing scrutiny.
- The newly elected Queensland government ordered its own review of the state's ~A$470M commitment. As of September 2025, the investment remained active, but the review outcome adds uncertainty.
- Brisbane construction had not begun as of late 2025, running up to 12 months behind the originally stated mid-2025 start. No public consultation on the draft development plan had taken place.
- **Government investment is not technical validation.** The deal reflects strategic economic policy (Brisbane as a quantum computing hub), not an independent technical assessment that PsiQuantum's technology works.

**Summary:** The investment commitment is verified. Its current status is uncertain given ongoing reviews and construction delays. It is a government economic bet, not a peer review of PsiQuantum's technology.

---

### Claim: DARPA QBI US2QC selection validates the technical approach
**Status:** Partially verified (selection is verified; it does not constitute validation of the technology)

**Supporting sources:**
- [DARPA press release (February 2025)](https://www.darpa.mil/news/2025/quantum-computing-approaches) — DARPA selected PsiQuantum and Microsoft for the final US2QC validation phase

**Refuting / questioning sources:**
- DARPA selected only two companies (PsiQuantum and Microsoft) for the final stage out of 15 initially evaluated. This is a credible competitive signal.
- However, DARPA's US2QC program is explicitly described as an evaluation and validation program — not a demonstration of achieved results. DARPA's own documentation states it is assessing whether the approaches could reach utility scale, not that they already have.
- The evaluation is ongoing; no result has been published.

**Summary:** DARPA selection is a meaningful signal of technical credibility from a rigorous independent government evaluator. It is not evidence that the technology works at scale. The program's purpose is to determine if these approaches are viable — the answer is not yet known.

---

### Claim: No publicly demonstrated quantum processor as of April 2026
**Status:** Verified

**Supporting sources:**
- Extensive public literature review finds no peer-reviewed report of PsiQuantum operating a multi-qubit quantum processor capable of executing a quantum circuit, as distinct from individual chip-level component characterization.
- The Nature 2025 paper (Omega chipset) demonstrates individual component fidelities in a photonic chip — it is a component characterization paper, not a quantum processor demonstration.
- No public announcement of a multi-qubit programmable quantum computer by PsiQuantum exists in the literature as of April 2026.

**Summary:** PsiQuantum has not publicly demonstrated a quantum processor. It has demonstrated high-quality photonic chip components. The gap between component demonstration and an operational processor is very large and constitutes PsiQuantum's central unsolved engineering challenge.

---

### Roadmap History
PsiQuantum has historically not published detailed public roadmaps with specific milestone dates. Unlike IBM (which publishes explicit qubit-count roadmaps) or Quantinuum (which publishes specific gate fidelity milestones), PsiQuantum's public communications have described capability targets (e.g., "utility-scale fault-tolerant quantum computer") without specifying qubit counts, circuit depths, or timeline dates in technical detail. The claim attributed to PsiQuantum of "utility-scale deployment by February 2026" has not been fulfilled as of this review date (April 7, 2026) — no operational system has been announced. The Chicago IQMP site is under construction; Phase One is not expected to complete until 2027.

**Roadmap claims and dates:**
- *Claim (2024, approximate):* Brisbane site operational "by end of 2027" — flagged as aggressive at time of announcement; Brisbane construction had not begun as of late 2025, placing this milestone at risk.
- *Claim (2025, company communications):* "Utility-scale quantum computers" by February 2026 — not fulfilled as of April 2026.
- *Chicago Phase One:* Construction began September 2025; first phase expected complete 2027. This phase will include a large intermediate-scale test system for DARPA evaluation, not a utility-scale computer.

## Sources

- [PsiQuantum official website](https://www.psiquantum.com) — company profile, Omega chipset announcement, technology overview
- [Nature 641, 876–883 (2025) — "A manufacturable platform for photonic quantum computing"](https://www.nature.com/articles/s41586-025-08820-7) — primary peer-reviewed result; Omega chipset chip-level fidelity metrics
- [PMC full text (open access)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12095036/) — open access version of Nature 2025 paper
- [arXiv:2101.09310 — "Fusion-based quantum computation" (Bartolucci et al., 2021)](https://arxiv.org/abs/2101.09310) — foundational FBQC architecture preprint; published Nature Communications Feb 2023
- [Nature Communications — "Fusion-based quantum computation" (2023)](https://www.nature.com/articles/s41467-023-36493-1) — peer-reviewed FBQC architecture paper
- [DARPA QBI US2QC program](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) — program description and PsiQuantum selection
- [DARPA selects PsiQuantum and Microsoft for final QBI phase (Feb 2025)](https://www.darpa.mil/news/2025/quantum-computing-approaches) — selection announcement
- [Australian Department of Industry — government investment announcement (April 2024)](https://www.industry.gov.au/news/leading-quantum-company-chooses-australia-site-its-groundbreaking-utility-scale-quantum-computer) — A$940M deal
- [ANAO investigation into PsiQuantum investment](https://www.anao.gov.au/work/request/investigation-the-investment-psiquantum-announced-the-australian-and-queensland-governments) — ongoing scrutiny
- [McGrathNicol audit cleared deal process (Aug 2025)](https://ia.acs.org.au/article/2025/govt-s-psiquantum-deal-given-all-clear-by-internal-audit.html) — internal audit result
- [PsiQuantum Brisbane build running very late (Startup Daily)](https://www.startupdaily.net/topic/global-tech/psiquantums-brisbane-build-is-already-running-very-late/) — construction delay reporting
- [PsiQuantum breaks ground Chicago IQMP (Sept 30, 2025)](https://www.psiquantum.com/news-import/psiquantum-breaks-ground-chicago) — groundbreaking announcement
- [Chicago Phase One construction begins (Nov 2025)](https://thequantuminsider.com/2025/11/09/phase-one-construction-begins-on-chicago-quantum-computing-facility/) — construction update
- [Victor Peng Interim CEO announcement (Feb 10, 2026)](https://www.businesswire.com/news/home/20260210565444/en/PsiQuantum-Appoints-Victor-Peng-as-Interim-CEO-Co-Founder-Jeremy-OBrien-to-Become-Executive-Chairman) — leadership change
- [PsiQuantum $1B Series E announcement (Sept 2025)](https://www.psiquantum.com/news-import/psiquantum-1b-fundraise) — funding round details
- [PsiQuantum Series E investors detailed breakdown](https://thequantuminsider.com/2025/09/10/psiquantum-raises-1-billion-to-build-million-qubit-scale-fault-tolerant-quantum-computers/) — investor list
- [Physics World — Australia's A$1bn investment raises eyebrows](https://physicsworld.com/a/australia-raises-eyebrows-by-splashing-a1bn-into-us-quantum-computing-start-up-psiquantum/) — independent academic/scientific press commentary
- [arXiv photonic quantum computing survey (Sept 2024, arXiv:2409.08229)](https://arxiv.org/html/2409.08229v1) — field-level review of photonic quantum computing including PsiQuantum context
- [Jeremy O'Brien LinkedIn](https://www.linkedin.com/in/jeremy-o-brien-39482631) — founder background
