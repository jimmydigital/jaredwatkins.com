---
title: "Xanadu"
date: 2026-04-05
lastmod: 2026-04-05
draft: false
description: "Toronto-based photonic quantum computing company; developed Borealis quantum advantage system and PennyLane open-source SDK; recently went public via SPAC merger; building Aurora modular fault-tolerant platform targeting 2028–2029 deployment."
tags: ["quantum-computing", "photonic", "nisq", "canada", "cloud-access", "fault-tolerant-research"]
categories: ["company"]
research_area: "quantum-computing"
source_urls:
  - "https://www.xanadu.ai"
  - "https://www.xanadu.ai/about/"
  - "https://www.xanadu.ai/products/pennylane/"
  - "https://github.com/XanaduAI"
  - "https://www.nature.com/articles/s41586-022-04725-x"
  - "https://www.sec.gov/cgi-bin/browse-edgar?company=xanadu&owner=exclude&action=getcompany"
  - "https://www.prnewswire.com/news-releases/xanadu-and-disco-announce-collaboration-on-advanced-wafer-processing-for-photonic-quantum-computing-302526516.html"
  - "https://arxiv.org/abs/2212.14703"
last_reviewed: 2026-04-05
stale_after_days: 90
---

## Summary

Xanadu Quantum Technologies is a Toronto-headquartered photonic quantum computing company founded in 2016 and led by CEO Christian Weedbrook. It became the first pure-play photonic quantum computing company to go public, completing a SPAC merger with Crane Harbor Acquisition Corp in March 2026 under the ticker "XNDU" (Nasdaq/TSX). The company operates Borealis, a 216-squeezed-mode photonic system that claimed quantum computational advantage in a 2022 *Nature* publication. Xanadu is currently developing Aurora, a modular 12-qubit photonic quantum computer with modular, networked architecture, and has published a detailed technical blueprint for scaling photonic quantum computing to fault-tolerant regime by 2028–2029. The company maintains PennyLane, a widely adopted open-source quantum machine learning library. Total funding to date: approximately $250M across 8 rounds; post-IPO valuation as of November 2025: $3B.

## Key Facts

- **Founded:** 2016
- **Type:** Company (now publicly traded — Nasdaq: XNDU; TSX: XNDU)
- **Founder/CEO:** Christian Weedbrook
- **HQ:** Toronto, Canada
- **Qubit modality:** Photonic (squeezed light, linear optics)
- **Status:** NISQ-era commercial systems; fault-tolerant architecture under development
- **Key systems:** Borealis (216 squeezed modes, claim of quantum advantage), Aurora (12-qubit modular system, 4 photonically-interconnected racks with 35 photonic chips, 13km fiber optics)
- **Cloud access:** Amazon Braket, accessible for public experiments
- **Recent IPO:** March 2026 via SPAC merger; ~$302M raised in transaction
- **Valuation (Nov 2025):** $3B (private)
- **Headquarters:** Toronto, Canada; R&D and manufacturing facility expansion in 2024–2025

## What It Is / How It Works

Photonic quantum computing uses individual photons (particles of light) as qubits. Xanadu's approach centers on **squeezed light** — quantum states where uncertainty is concentrated in one observable at the expense of another — combined with **Gaussian boson sampling** (GBS) and linear optics. This differs fundamentally from superconducting and trapped-ion approaches.

### Photonic Hardware Specifics

**Borealis (2022):**
- 216 independent quantum systems (squeezed light modes)
- Time-multiplexed, photon-number-resolving architecture
- Operates at room temperature (key claimed advantage over cryogenic systems)
- Photon loss remains the primary scalability challenge
- Peer-reviewed result (Nature, 2022); not independently replicated as of April 2026

**Aurora (2025):**
- 12-qubit universal photonic quantum computer (modular design)
- 4 photonically-interconnected removable server racks
- 35 photonic chips, 13km of fiber optics
- Gottesman-Kitaev-Preskill (GKP) bosonic qubits with squeezed states
- Cluster-state architecture with one temporal and two spatial dimensions
- Represents architectural template for scaling to thousands of racks (theoretical: 1M+ physical qubits)
- In operational development as of April 2026

**Operating Temperature:** Room temperature operation is cited as a significant advantage versus cryogenic superconducting (millikelvin) and trapped-ion (near-room-temperature but laser-cooling dependent) systems. However, photon loss — fundamental to photonics — remains unsolved at scale.

### Photonic-Specific Metrics

Photonic systems do not use the "qubit count" framing of superconducting or trapped-ion architectures effectively, because:
1. Squeezed modes are continuous-variable quantum states, not discrete qubits
2. Photon loss causes statistical rather than deterministic errors
3. GBS is inherently probabilistic — successful outcomes require post-selection

Xanadu instead reports squeezed mode counts and computational samples produced. This is not standardized across the industry and should not be directly compared to other qubit modalities.

## Notable Developments

### 2026 (Most Recent)

- **2026-03:** Completed SPAC merger with Crane Harbor Acquisition Corp; went public on Nasdaq (XNDU) and Toronto Stock Exchange (XNDU). Business combination raised approximately $302M total (SPAC investor commitment ~$275M plus $27M in financing).
- **2026-03:** Partnership with University of Toronto and National Research Council of Canada announced for lithium-ion battery simulation quantum algorithms.
- **2026-03:** Announced Stage B advancement in DARPA's Quantum Benchmarking Initiative (QBI). Stage B represents government evaluation process, not technical validation of claimed advantage.
- **2026-01:** ETRI (Electronics and Telecommunications Research Institute, South Korea) partnership announced to accelerate fault-tolerant quantum algorithm design using PennyLane.

### 2025 (Major Momentum)

- **2025-11:** Aurora system operational; showcased 12-qubit modular photonic quantum computer architecture. Represents leap in scalability compared to Borealis.
- **2025-08:** Partnership with DISCO Corp. (Japan) announced for advanced wafer processing and photonic chip packaging. DISCO's dicing, grinding, and polishing technologies (Kiru, Kezuru, Migaku) aim to reduce optical loss in silicon-photonic integration. Expected to accelerate fault-tolerant timeline to ~2028.
- **2025-06:** Generated error-resistant photonic GKP qubits on integrated silicon-nitride photonic chip (first on-chip integration of GKP qubits). Marks significant progress toward fault-tolerant error correction.
- **2025-03:** Published breakthrough in quantum error-correction protocol for photonic GKP qubits.
- **2025-06:** Photonic packaging facility (Toronto, $10M investment) operational; developing large-scale assembly and packaging methods.

### 2024

- **2024-09:** Strategic timeline guidance issued: fault-tolerant photonic quantum data center targeted for 2029, with scaling efforts beginning 2028. This followed earlier claims of 2028 target in some communications.
- **2024-05:** CEO Christian Weedbrook publicly stated company was seeking $200M in all-Canadian funding round. This supported pre-IPO capital needs.

### 2022 (Quantum Advantage Claim)

- **2022-06:** Published "Quantum Computational Advantage with a Programmable Photonic Processor" in *Nature* (Madsen et al.). Claims 216-mode GBS would take >9,000 years for best available classical algorithms on supercomputers to replicate; Borealis produces samples in 36 microseconds. Borealis made available publicly on Amazon Braket.

## Claim Verification: Gaussian Boson Sampling and Quantum Advantage

### The 2022 Borealis Nature Claim

**What was claimed:** Gaussian boson sampling (GBS) — a specific quantum sampling distribution — cannot be efficiently simulated classically. Borealis output distribution matches theoretical prediction; the claim is that classical simulation would require >9,000 years of supercomputer time.

**Peer review status:** ✓ **Verified (peer-reviewed)** — Published in *Nature*, peer-reviewed, authors include Xanadu researchers and external co-authors.

**Independent replication:** ✗ **Unverified (no independent replication reported as of April 2026).** This is a critical gap. The paper was published 4 years ago; no independent group has reproduced the exact GBS sampling distribution on Borealis or equivalent photonic hardware.

**Classical simulation feasibility — CRITICAL CONTEXT:** This is where the skepticism standard applies heavily.

1. **GBS is a synthetic benchmark, not a practical computation.** It was designed to be hard to simulate but not to solve real problems. This is important context for interpreting "advantage."

2. **Classical simulation algorithms have improved substantially since 2022.** Multiple research groups have published faster classical GBS simulation algorithms in 2023–2024. While the full 216-mode GBS may still require classical resources beyond certain timeframes, the gap has narrowed. Notably:
   - Improved classical heuristics for GBS sampling published in peer-reviewed venues
   - No independent group has attempted to fully replicate Borealis's 216-mode sampling on equivalent classical hardware as of April 2026, so the exact comparison is unverified
   - One research group (Shao et al.) has published `BosonSupremacy` software for simulating GBS on supercomputers, showing classical methods can approach Borealis-scale problems

3. **Photon loss poses credibility challenges.** Borealis operates at room temperature but photon loss is non-negligible. Some critics have argued that the loss characteristics make GBS harder to spoof (positive for the claim) but also mean the "hardness" is partly a consequence of noise, not purely quantum advantage (negative for the claim). The paper addresses spoofing explicitly; the loss-hardness entanglement remains debated.

**Summary:** The 2022 *Nature* publication is legitimate peer-reviewed science, but the claim of quantum advantage in Borealis GBS remains **Partially verified** — the paper is solid, but independent replication is absent, and faster classical algorithms since publication have narrowed (though not eliminated) the claimed advantage.

### Roadmap and Timeline Claims

**Fault-tolerant quantum data center by 2028–2029:**
- **First published:** 2022 (in the blueprint paper; see below)
- **Reaffirmed:** 2024–2025, with refinement: 2028 for scaling initiation, 2029 for operational data center
- **Mechanism:** Networked modular photonic processors (thousands of racks) combining 1M+ physical qubits encoded in GKP bosonic states
- **Status:** In development; Aurora represents architectural proof-of-concept; no technical demonstration of full error correction yet
- **Credibility assessment:** **Partially verified (blueprint exists, architecture progresses, but full demonstration of fault tolerance remains outstanding).** The technical roadmap is published and detailed; manufacturing partnerships (DISCO) suggest serious execution, but photonics faces known scaling challenges (photon loss, integration density). This timeline is credible relative to industry claims but must be monitored for slip.

**Manufacturing acceleration via DISCO partnership (claimed ~2028 fault-tolerant deployment):**
- **Mechanism:** Advanced wafer dicing and polishing to reduce optical loss
- **Status:** Partnership announced August 2025; early-stage collaboration
- **Risk:** Depends on silicon-photonics fabrication maturing in parallel; DISCO partnership is necessary but not sufficient

## PennyLane: Adoption and Ecosystem

PennyLane is Xanadu's flagship open-source quantum machine learning library, providing a differentiable programming interface for quantum circuits across multiple hardware backends.

### Adoption Metrics

**GitHub:** Main repository (XanaduAI/pennylane) has substantial community engagement. Specific star counts were not retrieved in April 2026 search, but the library has been active and updated since 2018.

**PyPI / Downloads:** PennyLane is actively maintained with recent versions:
- v0.44.1 (March 10, 2026)
- v0.44.0 (January 13, 2026)
- v0.43.3 (March 11, 2026)
Active release cadence indicates ongoing development and user engagement.

**Backend Support:** PennyLane supports quantum hardware and simulators beyond Xanadu:
- Xanadu devices (Strawberry Fields, Borealis on AWS Braket)
- Cirq (Google)
- Qiskit (IBM)
- PennyLane-Lightning (GPU-accelerated simulation)
- Multiple third-party plugins (Rigetti, IonQ, D-Wave, others)

This multi-platform support differentiates PennyLane from single-vendor SDKs and increases adoption potential.

### Adoption Assessment

**Verified:** PennyLane is actively maintained, widely integrated across quantum computing platforms, and has consistent release velocity. It is one of the most broadly compatible quantum machine learning frameworks.

**Unverified (company claims):** Xanadu has not published official download statistics or academic citation counts. Adoption metrics should be verified via GitHub activity, PyPI downloads (available on PyPI Stats sites), and academic search (Google Scholar) for independent assessment.

### Academic Citations and Research Use

Estimated as substantial (based on active research community using PennyLane for published work), but specific citation counts were not retrieved in April 2026 searches. Recommend checking Google Scholar for current citation impact.

## Key People

### Christian Weedbrook — Founder & CEO

- **Current role:** Founder, Chief Executive Officer (since 2016)
- **Education:**
  - PhD in Quantum Information Theory, University of Queensland (2005–2009)
  - B.Sc. Honours Physics, Australian National University (2004)
  - B.Sc. Mathematics and Physics, University of Queensland (2000–2003)
- **Academic background:** Postdoctoral researcher at MIT and University of Toronto following PhD
- **Career transition:** Moved from academic quantum information to founding Xanadu in 2016
- **Leadership role:** Led Xanadu through funding rounds and public market entry (March 2026)
- **Overlap flag:** Weedbrook is the primary technical and strategic leader; his departure would represent significant organizational risk

### Nathan Killoran — Chief Technology Officer, Software

- **Current role:** CTO for software and quantum machine learning
- **Background:** Author and key contributor to Strawberry Fields (photonic quantum simulation platform)
- **Research focus:** Quantum chemistry applications, PennyLane architecture and differentiable quantum computing
- **LinkedIn:** Not located in public sources with certainty

### Nicolás Quesada — Researcher / Principal Scientist

- **Role:** Primary researcher/developer on Strawberry Fields and photonic quantum algorithms
- **Background:** Published work on Gaussian boson sampling, photonic quantum computing theory
- **Academic overlap:** Collaboration with University of Toronto; strong theoretical quantum optics background
- **LinkedIn:** Not located with certainty in searches

### People — Last Reviewed: 2026-04-05

Note: Xanadu is still a relatively small company (private/post-IPO startup stage). Leadership team depth in peer-reviewed quantum research is concentrated among founders and early research hires. No significant leadership departures have been announced as of April 2026.

## Roadmap: Fault-Tolerant Quantum Computing

Xanadu publishes roadmap targets for scaling photonic quantum computing. Key milestones:

| Milestone | Target Year | Status (as of April 2026) | Publication Date | Credibility Note |
|-----------|-------------|--------------------------|------------------|-----------------|
| Photonic GKP qubits on integrated chip | 2025 | ✓ Achieved (June 2025, silicon-nitride) | 2022 Blueprint | On track; peer-reviewed fabrication |
| Aurora 12-qubit modular system operational | 2025–2026 | ✓ Operational (Nov 2025) | 2024–2025 | Achieved on schedule |
| Scaling to thousands of modular racks | 2027–2028 | In progress | 2022 Blueprint | Depends on manufacturing partnerships (DISCO) and photon loss reduction |
| Fault-tolerant quantum data center demonstration | 2028–2029 | Targeted | 2022 Blueprint | Ambitious; photonics faces known loss challenges; no peer-reviewed FT error correction demonstration yet |
| 1M+ physical qubits, error-corrected operation | 2029+ | Long-range target | 2022 Blueprint | Depends on photon loss reduction and integration density scaling |

**Roadmap history:** Xanadu has not publicly revised its 2028–2029 fault-tolerant target downward. Aurora's achievement ahead of or on schedule (2025) suggests execution capability. However, the transition from NISQ systems to demonstrated fault tolerance remains unverified across all quantum modalities; photonics has not yet demonstrated logical qubit error suppression at scale.

## Manufacturing and Partnerships

### DISCO Partnership (2025)

- **Announced:** August 2025
- **Scope:** Advanced wafer processing (dicing, grinding, polishing) for silicon-photonic integrated circuits
- **Technology:** DISCO's Kiru, Kezuru, and Migaku platform for ultra-low-loss photonic chip preparation
- **Impact claim:** Expected to accelerate Xanadu's fault-tolerant quantum computer deployment to ~2028
- **Maturity:** Early collaboration; technology integration in progress as of April 2026
- **Assessment:** **Necessary but not sufficient** for claimed 2028 timeline; photon loss reduction remains the core bottleneck

### Other Partnerships

- **Amazon Braket:** Borealis available on AWS Braket for public cloud access
- **University of Toronto:** Collaborative research on quantum algorithms
- **National Research Council of Canada:** Battery simulation algorithms (2026)
- **ETRI (South Korea):** Fault-tolerant quantum algorithm development (2026)
- **Mitsubishi Chemical Group, Volkswagen, Toyota Research Institute:** Strategic partnerships in development (detailed announcements pending)
- **DARPA Quantum Benchmarking Initiative:** Stage B advancement with up to $15M in funding

## Funding and Valuation

| Milestone | Amount | Year | Notes |
|-----------|--------|------|-------|
| Series A–E (cumulative) | ~$150M | 2018–2022 | Multiple rounds led by Georgian, Bessemer Venture Partners, others |
| Series F (approximate) | $100M+ | 2022 | Georgian Partners led; valued company at $1B+ |
| Pre-IPO capital raise | $200M target | 2024 | CEO Weedbrook sought all-Canadian investment; partially achieved |
| SPAC merger (IPO) | $302M | 2026 | Combined with Crane Harbor Acquisition Corp; raised capital for scaling |
| **Valuation (Nov 2025)** | **$3B** | Private | Pre-IPO valuation; post-IPO valuation TBD |
| **Total funding** | **~$250M+** | 2016–2026 | 8 rounds from 26 investors (Tracxn data) |

**Assessment:** Funding is substantial and reflects investor confidence in photonic quantum computing. However, note that funding rounds do not validate technical claims; many quantum companies have raised similarly large amounts on future promises.

## Photonics vs. Other Modalities: Strategic Positioning

Xanadu's photonic approach has distinct advantages and challenges compared to superconducting (IBM, Google, Rigetti) and trapped-ion (IonQ, Quantinuum) systems:

### Advantages

1. **Room-temperature operation:** No cryogenic infrastructure required (advantage for practical deployment)
2. **Long coherence times (potentially):** Photons decohere on timescales of nanoseconds to microseconds in transmission, but stored in matter qubits can achieve seconds
3. **All-photonic integration:** Modularity via fiber interconnection offers scalability pathway
4. **Gaussian boson sampling** demonstrates a specific quantum computing application (though of limited practical use currently)

### Challenges

1. **Photon loss:** Fundamental to photonics; loss causes probabilistic failure and error. No photonic quantum computer has demonstrated error correction reducing logical error below physical error (the core requirement for fault tolerance)
2. **Probabilistic gates:** Many photonic gates are inherently probabilistic, requiring post-selection and reducing circuit depth
3. **Scaling integration:** Integrating thousands of photonic chips with minimal loss is unsolved; silicon-photonics fabrication at quantum-grade quality is not yet mature (DISCO partnership aims to address this)
4. **No demonstrated quantum advantage for practical problems:** Borealis's GBS is a synthetic benchmark; no photonic system has demonstrated advantage for real computation (optimization, chemistry, machine learning) vs. classical

### Market Position

Xanadu is currently the only public pure-play photonic quantum company. PsiQuantum (private, silicon-photonics approach with GlobalFoundries) and others are pursuing similar paths but remain private. Xanadu's IPO and public roadmap position it as the most transparent representative of the photonic modality.

## Notable Research Publications (Last 90 Days)

As of April 2026, Xanadu has published or announced:

1. **Nonadiabatic Molecular Dynamics on Quantum Computers** (2025–2026, arXiv preprint):
   - Novel algorithm for pre-Born-Oppenheimer molecular dynamics
   - Demonstrated order-of-magnitude reduction in Toffoli gate costs vs. prior methods
   - Application: ammonia + boron trifluoride reaction modeling
   - Status: Peer-reviewed publication pathway expected

2. **Photodynamic Cancer Therapy Optimization** (December 2025, arXiv preprint):
   - Quantum computational framework for photosensitizer discovery
   - Application to cancer treatment modalities
   - Status: Early-stage research; implications for pharmaceutical workflows under investigation

3. **Lithium-Ion Battery Simulation Algorithms** (March 2026, collaborative announcement):
   - Joint publication with University of Toronto and NRC Canada
   - Quantum algorithms for battery chemistry simulation
   - Status: Under peer review or recent publication

**Publication velocity:** Xanadu maintains active research publication pace, primarily on arXiv with subsequent peer review. Most recent publications target chemistry and optimization applications rather than fundamental photonics improvements, suggesting strategic shift toward demonstrating practical quantum advantage.

## Risk Factors and Monitoring Items

1. **Borealis advantage claim independence:** As of April 2026, no independent group has replicated Borealis's GBS sampling distribution. This 4-year gap is unusual for claimed quantum advantage. Monitor for independent validation or challenges.

2. **Photon loss roadmap:** Xanadu claims DISCO partnership will accelerate fault-tolerant deployment to ~2028. This is credible but depends on silicon-photonics manufacturing maturity and photon loss reduction. Any slip in this partnership or photon loss progress should trigger timeline revision.

3. **Aurora scaling:** Aurora is a proof-of-concept modular system. Scaling from 12 qubits to 1M+ physical qubits while maintaining low photon loss is exponentially harder. Monitor for technical breakthroughs in loss reduction or manufacturing.

4. **Public market execution:** Post-IPO (March 2026), Xanadu must balance investor expectations with technical development timelines. History of quantum companies suggests pressure to announce milestones; assess announcements against independent technical criteria.

5. **PennyLane adoption as business driver:** PennyLane is valuable intellectual property, but adoption does not require customers to use Xanadu hardware. Revenue diversification (cloud services, software licensing, research partnerships) is important for sustainability.

## Conclusion

Xanadu is a credible photonic quantum computing company with published peer-reviewed research (Borealis advantage claim), a detailed technical roadmap (fault-tolerant photonics blueprint), and active engineering progress (Aurora system, DISCO partnership). However, the field operates under heightened skepticism: the Borealis advantage claim lacks independent replication, the fault-tolerant roadmap remains undemonstrated, and photonics faces fundamental scalability challenges (photon loss) not yet solved. The March 2026 IPO brings financial resources and transparency but also investor-pressure dynamics to monitor. As of April 2026, Xanadu represents the most transparent public representative of the photonic quantum computing modality, but technical validation remains outstanding at the scale required for practical quantum advantage.

## Sources

- [Xanadu Official Website](https://www.xanadu.ai)
- [Xanadu About Page](https://www.xanadu.ai/about/)
- [PennyLane Product Page](https://www.xanadu.ai/products/pennylane/)
- [Xanadu GitHub Organization](https://github.com/XanaduAI)
- [Nature 2022: Quantum Computational Advantage with a Programmable Photonic Processor](https://www.nature.com/articles/s41586-022-04725-x)
- [Xanadu IPO Announcement](https://www.xanadu.ai/press/xanadu-becomes-first-pure-play-photonic-quantum-computing-company-to-go-public)
- [DISCO Partnership Press Release](https://www.prnewswire.com/news-releases/xanadu-and-disco-announce-collaboration-on-advanced-wafer-processing-for-photonic-quantum-computing-302526516.html)
- [Aurora System Announcement](https://phys.org/news/2025-01-world-scalable-photonic-quantum-prototype.html)
- [Xanadu Funding History](https://www.clay.com/dossier/xanadu-funding)
- [PennyLane PyPI Package](https://pypi.org/project/pennylane/)
- [AWS Quantum Blog: Exploring Xanadu's Borealis Device](https://aws.amazon.com/blogs/quantum-computing/explore-quantum-computational-advantage-with-xanadus-borealis-device-on-amazon-braket/)
- [Xanadu DARPA QBI Stage B Announcement](https://thequantuminsider.com/2026/03/12/xanadu-etri-fault-tolerant-quantum-algorithm-pennylane/)
- [Xanadu Lithium-Ion Battery Research](https://www.globenewswire.com/news-release/2026/03/18/3258581/0/en/Xanadu-the-University-of-Toronto-and-the-National-Research-Council-of-Canada-Unveil-Quantum-Algorithms-for-Lithium-ion-Battery-Simulations.html)

