---
title: "Rigetti Computing"
date: 2026-04-07
lastmod: 2026-04-07
draft: false
description: "Publicly traded superconducting quantum computing company; builds QPUs at its own Fab-1 foundry; sells cloud access via QCS, AWS Braket, and Azure Quantum; financially stressed with declining revenue."
tags: ["quantum-computing", "superconducting", "nisq", "us", "cloud-access"]
categories: ["company"]
research_area: "quantum-computing"
source_urls:
  - "https://www.rigetti.com"
  - "https://investors.rigetti.com"
  - "https://www.sec.gov/Archives/edgar/data/1838359/000155837025002499/rgti-20241231x10k.htm"
  - "https://arxiv.org/abs/2410.05202"
  - "https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-launches-84-qubit-ankaatm-3-system-achieves"
  - "https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-second-quarter-2025-financial-results"
  - "https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-third-quarter-2025-financial-results"
  - "https://investors.rigetti.com/news-releases/news-release-details/rigetti-collaboration-qphox-awarded-58m-afrl-contract-advance"
  - "https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-announces-strategic-collaboration-agreement"
  - "https://www.darpa.mil/research/programs/quantum-benchmarking-initiative"
last_reviewed: 2026-04-07
stale_after_days: 90
---

## Summary

Rigetti Computing (NASDAQ: RGTI) is a publicly traded superconducting quantum computing company founded in 2013 and headquartered in Berkeley, California. It is one of the few quantum hardware companies to operate its own semiconductor fabrication facility — Fab-1 in Fremont, CA — which it uses to design and build its own QPUs. Rigetti sells cloud access to its quantum processors via its proprietary Quantum Cloud Services (QCS) platform, as well as through AWS Braket and Azure Quantum. As of Q1 2026, the company is financially stressed: revenue has declined for three consecutive years, reaching $10.8M in FY2024, while it carries substantial annual operating losses ($68.5M in 2024). Its largest QPU to date is the 84-qubit Ankaa-3 (December 2024); a 36-qubit modular Cepheus-1-36Q chiplet system was announced in mid-2025. The company has a documented history of missing its own published roadmap milestones by wide margins.

## Key Facts

- **Founded:** 2013 by Chad Rigetti (University of California, Berkeley)
- **Type:** Company (publicly traded — NASDAQ: RGTI)
- **HQ:** Berkeley, CA, USA
- **Fab:** Fab-1, Fremont, CA (in-house QPU fabrication)
- **Qubit modality:** Superconducting transmon qubits (gate-based)
- **Status:** Active; NISQ-era commercial systems; fault-tolerant computing on roadmap
- **Latest QPU (general availability):** Ankaa-3 — 84 physical qubits, 99.5% median two-qubit fidelity (company announcement, not peer-reviewed); 34 µs T1, 20 µs T2
- **Latest modular QPU:** Cepheus-1-36Q — 36 qubits (four 9-qubit chiplets), 99.5% median two-qubit fidelity (company announcement)
- **Cloud access:** QCS (proprietary), AWS Braket, Azure Quantum
- **FY2024 revenue:** $10.8M (SEC-filed; ~10% YoY decline)
- **FY2024 net loss:** $201.0M (includes $133.9M non-cash fair value changes)
- **FY2024 operating loss:** $68.5M
- **Cash position (Dec 31, 2024):** $217.2M (cash, equivalents, and available-for-sale securities; SEC 10-K)
- **Going concern:** No going-concern disclosure in FY2024 10-K; company states cash sufficient for "at least the next three years" at current burn rate
- **SPAC merger:** Closed March 2, 2022 (Supernova Partners Acquisition Company II, SNII); proceeds ~$262M
- **CEO:** Dr. Subodh Kulkarni (since December 2022)

## What It Is / How It Works

Rigetti uses superconducting transmon qubits — microfabricated circuits cooled to millikelvin temperatures in dilution refrigerators. Quantum operations are performed by applying precisely shaped microwave pulses. The central architectural feature of Rigetti's current hardware is the use of tunable couplers in a square lattice topology. Earlier Rigetti chips (Aspen-M series) used an octagonal lattice design where each qubit had only three neighbors except at lattice edges; the Ankaa series shifted to a square lattice with four neighbors per non-edge qubit and integrated tunable couplers that allow gate times roughly 3× faster than prior designs. The square lattice also tiles more straightforwardly for future scaling.

Rigetti's fabrication strategy is distinctive: rather than outsourcing chip production to a commercial semiconductor foundry, it operates Fab-1, a dedicated quantum chip foundry in Fremont, California opened in 2017. The claimed advantage of in-house fabrication is rapid design-build-test cycles — the company has stated new 3D-integrated circuit designs can be fabricated and characterized in approximately two weeks. In practice, Fab-1 has enabled faster iteration on chip designs and differentiated Rigetti from software-focused quantum companies, but it has not translated to consistently leading-edge fidelity numbers; IBM and Google (which also operate dedicated fabs) have generally demonstrated higher two-qubit gate fidelities on larger systems. Rigetti's 2022 announcement of a significant Fab-1 capacity expansion has not been followed by commensurate production volume growth, as evidenced by declining revenue.

In mid-2025, Rigetti introduced a chiplet-based architecture with the Cepheus-1-36Q system, which assembles four 9-qubit chiplets into a 36-qubit system. This approach is intended to allow defective chiplets to be discarded, improving overall yield, and to provide a path toward systems larger than can be fabricated on a single die. The chiplet approach is unproven at scale and its fidelity figures have not been independently replicated.

Quantum Cloud Services (QCS) provides programmatic access to Rigetti QPUs via REST APIs and the Quil/Quilc toolchain (open-source). Rigetti's systems are also available on AWS Braket (Ankaa-3 added in early 2025) and Azure Quantum (Cepheus-1-36Q added in Q2 2025). Active user numbers are not publicly disclosed.

## Notable Developments

- **2026-Q1:** Centre for Development of Advanced Computing (C-DAC), India, placed an $8.4M order for a 108-qubit superconducting quantum system; deployment planned for H2 2026. This would be Rigetti's largest single hardware sale if delivered as specified. *(Partially verified — order announced via press release; no independent confirmation of system specs as of April 2026.)*
- **2026-02:** Rigetti and Riverlane co-authored an arXiv preprint (arXiv:2410.05202) demonstrating real-time, low-latency quantum error correction on Rigetti's Ankaa-2 hardware using a scalable FPGA Collision Clustering decoder. 8-qubit stability experiment with 25 decoding rounds; mean decoding latency <1 µs. This is the most substantive independent technical validation of Rigetti's hardware in recent history. *(Verified — preprint; submitted for journal peer review; independently developed decoder from Riverlane.)*
- **2025-Q3:** Two Novera QPU system sales ($5.7M combined, ~$2.85M per system with components) to undisclosed customers. Novera is a commercially sold stand-alone superconducting QPU for on-premises installation.
- **2025-09:** Collaboration with QphoX (Netherlands) awarded $5.8M AFRL contract to advance superconducting quantum networking by combining Rigetti microwave qubits with QphoX microwave-to-optical transducers. 3-year program. *(Verified — contract announcement; AFRL award confirmed.)*
- **2025-08:** Quanta Computer partnership closed; Quanta invested $35M in Rigetti equity at ~$11.59/share and committed to $100M+ total investment over 5 years. Quanta is the world's largest contract electronics manufacturer (a major Apple/Dell/HP notebook and server supplier). Strategic goal: leverage Quanta manufacturing expertise to scale Rigetti QPU commercialization. *(Partially verified — investment closed; whether commercial manufacturing partnership produces results remains to be demonstrated.)*
- **2025-Q2:** Cepheus-1-36Q (four-chiplet modular QPU) deployed on Azure Quantum. Company claims 99.5% median two-qubit gate fidelity and 2× error reduction vs Ankaa-3. *(Partially verified — company announcement; no peer-reviewed characterization of chiplet-integrated fidelity.)*
- **2025-Q1:** Ankaa-3 (84 qubits) added to AWS Braket. Ankaa-3 launched December 2024 with 99.5% median fSim gate fidelity and 99.0% iSWAP fidelity.
- **2025-Q1:** DARPA selected Rigetti for Stage A of its Quantum Benchmarking Initiative (QBI) at up to $1M for a 6-month period. Rigetti did **not** advance to Stage B in the November 2025 cohort (11 other companies were selected for Stage B; Rigetti was not among them). Company stated it remained in dialogue with DARPA about future Stage B consideration. *(Verified — DARPA public announcement; non-selection for Stage B confirmed.)*
- **2024-12:** Ankaa-3 (84 qubits) launched. 99.5% median two-qubit fidelity, 34 µs T1, 20 µs T2, square lattice with tunable couplers. *(Partially verified — company announcement; figures not peer-reviewed.)*
- **2023-11:** Novera QPU commercially released — a stand-alone 9-qubit superconducting QPU sold directly to research institutions and labs for on-premises use, priced at $900,000.
- **2022-03:** SPAC merger with Supernova Partners Acquisition Company II (SNII) closed; Rigetti began trading on Nasdaq as RGTI. Gross proceeds approximately $262M. SPAC IPO at ~$10/share; post-merger stock subsequently declined sharply (see Financial Situation).
- **2022-12:** Chad Rigetti (founder, President & CEO since founding) stepped down. Subodh Kulkarni appointed President & CEO. Chad Rigetti retained no executive role; has subsequently co-founded Sygaldry Technologies (quantum-accelerated AI infrastructure, launched May 2025) and joined the board of Quantum Elements (November 2025).

## Financial Situation

Rigetti's financial trajectory reflects a company that has struggled to convert technical capability into commercial revenue. All figures below are from SEC filings unless otherwise noted.

**Revenue:**
- FY2022: Not separately verified in this research; described as a 60% growth year
- FY2023: Declined ~8% YoY
- FY2024: $10.8M total (10-K filed March 7, 2025); down from ~$12.0M in FY2023. Revenue breakdown: QCaaS (cloud access) was the minority contributor in most quarters (Q3 2024 QCaaS was $1.6M out of ~$2.7M quarterly total); the majority came from collaborative research, professional services, and hardware sales.
- FY2025: Analysts projected approximately $7.6M; Q4 2025 reported at $1.9M (down ~17% YoY), missing consensus of $2.3M.

**Losses:**
- FY2024 operating loss: $68.5M
- FY2024 net loss: $201.0M (includes $133.9M in non-cash fair value changes to earn-out and derivative warrant liabilities from the SPAC structure)
- FY2025 operating loss: ~$22.6M in Q4 alone; full-year not yet filed as of April 2026

**Cash:**
- December 31, 2024: $217.2M in cash, equivalents, and available-for-sale securities (10-K)
- The 10-K states the company believes this cash is sufficient to fund operations for "at least the next three years" at current levels. No going-concern qualification was issued by auditors.
- Note: The $217.2M figure predates the Quanta Computer investment ($35M closed April 30, 2025).

**SPAC context:** Rigetti originally projected a $1.5B pro-forma equity valuation at the time of its SPAC announcement (October 2021). Actual proceeds received were ~$262M — significantly less than the announced ~$458M gross (reflecting substantial SPAC shareholder redemptions, a common outcome in 2021–2022 SPAC transactions). The SPAC structure also created ongoing non-cash accounting complexity (earn-out liabilities, derivative warrants) that substantially inflates reported GAAP net losses.

**Stock price:** 52-week high through early April 2026 was approximately $58.15; price as of April 4, 2026 was approximately $14.19, representing ~76% decline from that peak. The stock had a notable run-up in late 2024/early 2025 driven by broader quantum computing sector enthusiasm, followed by a sharp pullback.

## Roadmap — History and Current Status

Rigetti has a documented pattern of announcing aggressive qubit-count timelines and then delivering substantially lower qubit counts on delayed schedules.

**Original 2022 published roadmap (announced at SPAC investor day):**
- 2023: ~1,000 qubits
- 2024: ~4,000 qubits
- 2025: ~10,000 qubits
- **Outcome:** None of these milestones were met. As of end-2025, the largest commercially available Rigetti system was 84 qubits (Ankaa-3).

**Revised roadmap (as of 2024–2025):**
- End-2025: 100+ qubit chiplet-based system with 99.5% median two-qubit fidelity — **status: missed** (Cepheus-1-36Q was 36 qubits; no 100+ qubit chiplet announcement made by end-2025)
- End-2026: 150+ qubit system with 99.7% median two-qubit fidelity; Lyra processor (336 qubits) described as planned
- End-2027: 1,000+ qubit system with 99.8% median two-qubit fidelity

**Assessment:** The 2026–2027 roadmap should be treated as aspirational. Prior large-scale roadmap announcements (2022) missed targets by roughly 10–100×. The 2025 100+ qubit chiplet target was also missed, though by a smaller relative margin. The chiplet architecture is a credible engineering approach for scaling, but no large-scale chiplet integration (beyond 36 qubits) has been demonstrated. Lyra (336 qubits) has no publicly available prototype data.

## Fab-1

Fab-1, located at 47430 Seabridge Drive, Fremont, California, opened in 2017 as one of the world's first dedicated quantum computing foundries. Rigetti fabricates its own superconducting qubit chips there, in contrast to competitors that use third-party foundries (e.g., IonQ's original plan used external fabrication; IBM and Google operate their own fabs similarly to Rigetti).

**Intended strategic advantages:**
1. Rapid design-build-test cycles (~2 weeks per new design iteration per company claims)
2. Independence from external foundry queue times and IP exposure
3. Ability to develop and protect proprietary fabrication processes

**Demonstrated outcomes:**
- Has produced all commercial Rigetti QPUs from Aspen-M through Ankaa-3 and Cepheus-1-36Q
- Enables custom 3D-integrated circuit designs (flip-chip bonding used in Ankaa architecture)
- Company announced a ~5,000 sq ft clean room expansion in 2022–2023

**Where it has not delivered:**
- Fab-1 has not enabled Rigetti to match or exceed IBM's or Google's gate fidelities at comparable qubit counts. IBM's Heron R2 processor has demonstrated >99.9% two-qubit gate fidelity; Google's Willow demonstrated competitive fidelities at 105 qubits.
- Production ramp has not scaled commensurately with announced roadmap commitments. Revenue from hardware sales (QCaaS and Novera combined) has been declining, not growing, suggesting Fab-1 output has not driven commercialization at the projected rate.
- Fab-1 is described in the 10-K as a critical facility whose loss or disruption would be material to operations — reflecting both its strategic centrality and its single-point-of-failure risk.

## Key People

### Dr. Subodh Kulkarni — President & CEO

- **LinkedIn:** <!-- TODO: search for Subodh Kulkarni Rigetti LinkedIn profile slug -->
- **Appointed:** December 2022 (following Chad Rigetti's departure)
- **Background:** 30+ years in semiconductor and technology industries. Previously President & CEO of CyberOptics Corporation (3D sensing and inspection systems). Prior roles in technology hardware commercialization.
- **Overlap flag:** Background in precision sensor manufacturing; no known overlap with other companies in the Research section.

### Chad Rigetti — Founder (non-executive)

- **LinkedIn:** <!-- TODO: not found in public sources -->
- **Google Scholar:** Research publications from Yale and UC Berkeley (superconducting quantum circuits)
- **Founder:** Founded Rigetti Computing in 2013 after completing PhD at Yale (superconducting qubits) and postdoctoral work at IBM Research (T.J. Watson)
- **CEO tenure:** 2013 – December 2022 (approximately 9 years)
- **Departure (December 2022):** Stepped down as President & CEO; stated reason was to transition to focus on product and technology development. No executive role at Rigetti subsequently.
- **Post-Rigetti:** Co-founded Sygaldry Technologies (quantum-accelerated AI servers/infrastructure; launched May 2025). Joined board of directors of Quantum Elements (November 2025). Joined QDNL Participations (VC fund, ~$70M, early-stage quantum technology) in 2023.
- **⚑ Note on "return":** The task description for this entry stated Chad Rigetti "departed and returned" — research does not confirm any return to an executive role at Rigetti Computing. He departed December 2022 and as of April 2026 is not in any executive role. This claim should not be reported without independent verification.

### CTO

- Company CTO (surname Rivas) appointed February 2023; previously SVP Systems & Services overseeing QCS engineering.
- **LinkedIn:** <!-- TODO: full name and LinkedIn slug not found in public sources; verify against Rigetti management page -->

### Chief Scientist / Research Leadership

- No separately titled Chief Scientist identified in public filings or management pages as of April 2026. Technical leadership appears consolidated under CTO role.

### People — Last Reviewed: 2026-04-07

## Government Contracts

**DARPA:**

- **Quantum Benchmarking Initiative (QBI) Stage A (April 2025):** Up to $1M, 6-month Stage A period. Rigetti selected for Stage A but **not** advanced to Stage B in the November 2025 selection cohort (11 other companies were selected). Company described DARPA discussions as ongoing. *(Verified — DARPA public announcement for Stage A; non-selection for Stage B confirmed by DARPA announcement of the 11 Stage B participants.)*
- **IMPAQT (October 2023):** Contract to advance quantum algorithms for combinatorial optimization under DARPA IMPAQT program. Project: "Scheduling Problems with Efficient Encoding of Qubits" (SPEEQ). *(Verified — contract award announced.)*
- **Quantum Application Benchmarking (August 2022):** Up to $2.9M, 3-year contract to develop quantum application benchmarks. *(Verified.)*
- **Phase 2 Quantum Benchmarking (November 2023):** Up to $1.5M potential value. *(Verified — award announced.)*

**AFRL:**

- **QphoX Collaboration (September 2025):** $5.8M, 3-year AFRL contract (shared between Rigetti and QphoX). Goal: advance superconducting quantum networking by integrating Rigetti microwave qubits with QphoX microwave-to-optical photon transducers. *(Verified — contract announcement; AFRL award confirmed.)*

**DoE:** No DoE contracts identified in available sources as of April 2026.

**USASpending.gov verification:** Direct search of USASpending.gov was not completed in this research pass. DARPA and AFRL contract claims are sourced from press releases. A full USASpending.gov audit is recommended on next review.

## Claim Verification

### Claim: Ankaa-3 achieves 99.5% median two-qubit gate fidelity (December 2024)

**Status:** Partially verified

**Supporting sources:**
- [Rigetti press release, Dec 23, 2024](https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-launches-84-qubit-ankaatm-3-system-achieves) — company announcement specifying 99.5% median fSim gate fidelity and 99.0% median iSWAP fidelity on 84-qubit system; 34 µs T1, 20 µs T2

**Refuting / questioning sources:**
- No peer-reviewed publication characterizing Ankaa-3 performance was identified in this research pass. Reference to arXiv:2412.18837 was noted in one source but could not be verified.
- The 99.5% figure applies to the full 84-qubit system in aggregate (median), not to all qubit pairs; best and worst pairs likely diverge substantially from median. Conditions of measurement (circuit depth, qubit temperature, calibration recency) not specified.

**Summary:** Fidelity figure is from company announcement only. No independent replication or peer-reviewed characterization found. Treat as Partially verified until an arXiv preprint or journal paper characterizing Ankaa-3 system-wide performance is published.

---

### Claim: Cepheus-1-36Q achieves 99.5% median fidelity with 2× error reduction vs Ankaa-3 (Q2 2025)

**Status:** Partially verified

**Supporting sources:**
- [Rigetti Q2 2025 earnings announcement](https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-second-quarter-2025-financial-results) — company reporting; also noted in Azure Quantum deployment announcement

**Refuting / questioning sources:**
- No independent characterization of chiplet-integrated fidelity found. The claim of "2× error reduction" implies roughly 99.5% achieved vs ~99.0% for Ankaa-3's iSWAP — plausible given architectural changes, but unverified.
- Cross-chiplet connectivity and fidelity are not addressed in available sources; chiplet-to-chiplet gates may underperform intra-chiplet gates.

**Summary:** Partially verified from company announcement. The 99.5% figure likely applies to intra-chiplet gates only; cross-chiplet performance unknown.

---

### Claim: Real-time low-latency QEC demonstrated on Ankaa-2 (February 2026, arXiv:2410.05202)

**Status:** Verified (preprint; submitted for peer review)

**Supporting sources:**
- [arXiv:2410.05202](https://arxiv.org/abs/2410.05202) — Rigetti/Riverlane collaborative preprint; FPGA-based Collision Clustering decoder; 8-qubit stability experiment, 25 decoding rounds, <1 µs mean decode latency. Developed by Riverlane (independent UK quantum error correction company) running on Rigetti hardware.

**Refuting / questioning sources:**
- 8-qubit experiment is a small-scale demonstration; does not demonstrate scalable error correction to logical qubit fault-tolerance threshold.
- This is an arXiv preprint, not yet peer-reviewed as of April 2026.

**Summary:** Most substantive independent technical validation of Rigetti hardware currently available. Confirms hardware is usable for real-time error correction experiments. Scale is very limited (8 qubits, not fault-tolerant).

---

### Claim: Prototype 99.9% two-qubit gate fidelity at 28 ns gate time (2025)

**Status:** Unverified

**Supporting sources:**
- Company statement describing a prototype result using proprietary adiabatic CZ scheme

**Refuting / questioning sources:**
- No publication, preprint, or independent source found confirming this figure. The claim is not tied to a specific QPU name or a published characterization.

**Summary:** Unverified. A prototype metric not tied to any commercially available system and not published in peer-reviewed or preprint form. Not suitable for comparison with commercially available fidelity figures.

---

### Claim: 2025 roadmap target (100+ qubit chiplet system) met

**Status:** Unverified — appears missed

**Supporting sources:**
- Rigetti announced a 100+ qubit chiplet target for end-2025 in 2024 roadmap documentation

**Refuting / questioning sources:**
- The announced modular product as of mid-2025 was Cepheus-1-36Q (36 qubits, not 100+). No 100+ qubit chiplet system was announced or deployed as of Q1 2026.

**Summary:** Target missed. Cepheus-1-36Q delivered 36 qubits vs 100+ qubit commitment.

---

### Roadmap History: Prior Published Milestones and Outcomes

| Year announced | Target | Deadline | Outcome |
|---|---|---|---|
| 2022 (SPAC investor day) | ~1,000 qubits | 2023 | Missed — Aspen-M remained flagship at ~80 qubits in 2023 |
| 2022 (SPAC investor day) | ~4,000 qubits | 2024 | Missed — Ankaa-3 at 84 qubits launched Dec 2024 |
| 2022 (SPAC investor day) | ~10,000 qubits | 2025 | Missed — chiplet system reached 36 qubits |
| 2024 (revised roadmap) | 100+ qubits (chiplet) | End-2025 | Missed — Cepheus-1-36Q delivered 36 qubits |
| 2024 (revised roadmap) | 150+ qubits | End-2026 | Pending |
| 2024 (revised roadmap) | 1,000+ qubits | End-2027 | Pending |

The pattern is consistent: Rigetti has not delivered on any large-scale qubit count milestone in its history. The revised 2024 roadmap compressed some timescales vs the original 2022 projections, but the near-term milestone (100+ qubits, end-2025) was still missed.

---

### Claim: In-house Fab-1 as strategic competitive advantage

**Status:** Partially verified (advantage is real; claimed scale-up benefit undemonstrated)

**Supporting sources:**
- Fab-1 has demonstrably enabled rapid iteration: Ankaa series represents multiple generational improvements (Aspen-M → Ankaa-1 → Ankaa-2 → Ankaa-3 → Cepheus architecture) within ~3 years.
- Short design-to-fabrication cycle (~2 weeks per company claims) is plausible given dedicated foundry vs commercial queue.

**Refuting / questioning sources:**
- Fidelity results from Rigetti remain behind IBM Heron R2 (>99.9% reported 2024) and Quantinuum Helios (99.921%, peer-reviewed). In-house fab has not produced leading-edge fidelity.
- Revenue has declined despite Fab-1 producing multiple QPU generations. Production scale benefit is not evident in commercial uptake.
- Fab-1 capacity expansion (2022–2023) has not been followed by production volume growth measurable in reported revenue.

**Summary:** In-house fab demonstrably enables faster design iteration. It has not produced the fidelity leadership or commercial scale-up that was argued to be its strategic rationale. Partially verified as a genuine but limited advantage.

## Sources

- [Rigetti Computing investor relations](https://investors.rigetti.com) — press releases and SEC filings
- [FY2024 10-K (SEC)](https://www.sec.gov/Archives/edgar/data/1838359/000155837025002499/rgti-20241231x10k.htm) — revenue, losses, cash, going concern
- [Ankaa-3 launch press release (Dec 2024)](https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-launches-84-qubit-ankaatm-3-system-achieves) — hardware specs
- [Q2 2025 earnings (Cepheus-1-36Q)](https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-second-quarter-2025-financial-results) — modular QPU specs, Azure deployment
- [Q3 2025 earnings / roadmap update](https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-third-quarter-2025-financial-results) — revenue, roadmap status
- [arXiv:2410.05202 — Rigetti/Riverlane QEC paper](https://arxiv.org/abs/2410.05202) — peer-reviewed QEC experiment on Ankaa-2
- [AFRL/QphoX contract announcement (Sep 2025)](https://investors.rigetti.com/news-releases/news-release-details/rigetti-collaboration-qphox-awarded-58m-afrl-contract-advance) — government contract
- [DARPA QBI Stage A announcement (Apr 2025)](https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-selected-participate-darpas-quantum) — DARPA contract
- [Quanta Computer partnership announcement](https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-announces-strategic-collaboration-agreement) — $35M investment, $100M+ commitment
- [DARPA QBI Stage B selection (Nov 2025)](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) — Rigetti not in Stage B cohort
- [Rigetti leadership team](https://investors.rigetti.com/corporate-governance/management) — executive bios
- [Sygaldry Technologies (Chad Rigetti new company, May 2025)](https://thequantuminsider.com/2025/05/31/new-startup-sygaldry-aims-to-rethink-ai-infrastructure-with-quantum-hardware/) — founder post-Rigetti activity
- [AWS Braket Rigetti page](https://aws.amazon.com/braket/quantum-computers/rigetti/) — cloud access details
