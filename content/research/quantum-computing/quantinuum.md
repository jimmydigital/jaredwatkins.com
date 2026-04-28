---
title: "Quantinuum"
date: 2026-04-05
lastmod: 2026-04-05
draft: false
description: "Privately held trapped-ion quantum computing company formed by the 2021 merger of Honeywell Quantum Solutions and Cambridge Quantum; produces the H-series (H1, H2) and Helios systems; holds the highest publicly demonstrated two-qubit gate fidelity of any commercial system."
tags: ["quantum-computing", "trapped-ion", "nisq", "fault-tolerant-research", "us", "uk"]
categories: ["company"]
research_area: "quantum-computing"
source_urls:
  - "https://www.quantinuum.com"
  - "https://arxiv.org/abs/2511.05465"
  - "https://arxiv.org/abs/2305.03828"
  - "https://arxiv.org/abs/2602.22211"
  - "https://arxiv.org/abs/2603.04584"
  - "https://www.nature.com/articles/s41586-025-08737-1"
  - "https://www.honeywell.com/us/en/press/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale"
  - "https://docs.quantinuum.com/systems/data_sheets/Quantinuum%20H2%20Product%20Data%20Sheet.pdf"
last_reviewed: 2026-04-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Quantinuum is a privately held quantum computing company formed on November 30, 2021 by the merger of Honeywell Quantum Solutions and Cambridge Quantum Computing (CQC). Headquartered in Broomfield, Colorado and Cambridge, UK, it produces the H-series trapped-ion quantum computers (H1, H2, and the 2025-generation Helios system) and develops quantum software including the TKET open-source compiler and InQuanto computational chemistry platform. Quantinuum's commercially available systems hold the highest publicly demonstrated two-qubit gate fidelity of any gate-based quantum computing platform; this claim is from company-authored preprints, though supported by independent benchmarking studies. As of early 2026, the company is approaching an IPO and is pursuing a roadmap toward fault-tolerant quantum computing by 2029–2030.

## Key Facts

- **Founded:** November 30, 2021 (via merger of Honeywell Quantum Solutions + Cambridge Quantum Computing)
- **Type:** Company (private; joint ownership — Honeywell ~54%, Cambridge Quantum Holdings ~36%, other investors ~10%)
- **HQ:** Broomfield, CO, USA and Cambridge, UK
- **Qubit modality:** Trapped ion (¹³⁷Ba⁺ barium ions on Helios; ⁷¹Yb⁺ ytterbium on H1/H2)
- **Status:** Active; commercial NISQ systems available; advanced fault-tolerant research underway
- **Key systems:** System Model H1 (20 qubits), System Model H2 (56 qubits), Helios (98 qubits, launched November 2025)
- **Key metric:** Two-qubit gate fidelity — Helios: 99.921% (7.9×10⁻⁴ infidelity); H2: >99.9% (company claim); both from company-authored papers
- **Valuation:** ~$10 billion pre-money (September 2025 funding round — unverified; private company, no public filing)
- **Total external funding raised:** ~$900M+ (January 2024: $300M round; September 2025: $600M round)
- **Key investors:** Honeywell, JPMorgan Chase, Mitsui, Amgen, Quanta Computer, NVentures (NVIDIA VC arm), QED Investors
- **Software:** TKET (open-source compiler), InQuanto (quantum chemistry), Quantum Origin (quantum-enhanced cryptographic RNG)
- **IPO status:** Planned; Honeywell CEO stated potential IPO as early as 2027

## What It Is / How It Works

Quantinuum uses the quantum charge-coupled device (QCCD) trapped-ion architecture. In this design, ions are held in a chip-scale electromagnetic trap and shuttled between zones for different operations: laser-cooled storage areas, high-fidelity gate zones, and mid-circuit measurement zones. This architecture enables all-to-all connectivity — any qubit can interact with any other — without the routing overhead that limits superconducting architectures, which are restricted to nearest-neighbor interactions.

The H1 system uses ytterbium-171 ions (¹⁷¹Yb⁺) with 20 qubits. The H2 (System Model H2) advanced to 56 qubits, also using ytterbium, in a racetrack-shaped ion trap with periodic boundary conditions. The Helios system, launched in November 2025, switches to barium-137 ions (¹³⁷Ba⁺) and uses a rotatable ion storage ring connecting two quantum operation regions via a junction. This architectural change enables 98 fully connected qubits with parallelized operations and real-time compilation of dynamic programs — key prerequisites for executing quantum error correction circuits that require mid-circuit measurement and qubit reuse.

The key physical advantage of trapped-ion systems is long coherence: trapped ions are extremely well-isolated from environmental noise, yielding T1 and T2 coherence times measured in seconds — orders of magnitude longer than superconducting qubits. The trade-off is gate speed: trapped-ion two-qubit gates are typically 1–2 orders of magnitude slower than superconducting gates, which can execute millions of operations per second. This places trapped-ion systems at a disadvantage for any application requiring high circuit throughput.

Quantinuum's software heritage derives primarily from Cambridge Quantum Computing (CQC), founded in 2014. CQC developed TKET as a hardware-agnostic quantum compiler beginning around 2018–2019, made it open source in 2021, and built the InQuanto chemistry platform on top of it. TKET handles circuit optimization and transpilation across multiple hardware backends, including IBM, Google, IonQ, and Quantinuum's own systems. The combination of a high-fidelity hardware platform with a mature, hardware-agnostic software stack is a meaningful competitive differentiation from pure hardware vendors.

## Notable Developments

- **2026-03:** Quantinuum preprint arXiv:2603.04584 (March 4, 2026) by Ruslan Shaydulin et al. (JPMorgan Chase + Quantinuum) demonstrated fault-tolerant execution of the QAOA algorithm (5–12 logical qubits) and HHL algorithm using the [[7,1,3]] Steane code on H2 and Helios systems. First demonstration of end-to-end fault-tolerant algorithm execution on real hardware. (arXiv preprint only; not yet peer-reviewed.)
- **2026-02:** Quantinuum preprint arXiv:2602.22211 demonstrated computations with up to 94 logical qubits (iceberg error detecting codes) and up to 48 logical qubits (concatenated error correcting codes) on Helios, achieving "beyond break-even" performance — encoded qubits outperforming unprotected physical qubits across multiple benchmarks. (arXiv preprint; not yet peer-reviewed.)
- **2025-11:** Launched Helios system — 98 qubits (¹³⁷Ba⁺), 99.921% two-qubit gate fidelity (7.9×10⁻⁴ infidelity averaged over all qubit pairs), 99.9975% single-qubit gate fidelity. Preprint: arXiv:2511.05465. Not yet in a peer-reviewed journal as of April 2026. Quantinuum also demonstrated 48 logical error-corrected qubits at launch using concatenated iceberg codes.
- **2025-09:** Honeywell announced a $600M equity capital raise at a $10B pre-money valuation. New investors include Quanta Computer, NVentures (NVIDIA), and Korea Investment Partners. Existing investors JPMorgan, Mitsui, Amgen, CQC Holdings, and Honeywell all reinvested.
- **2025-09:** H-series systems reached Quantum Volume of 2²⁵ (33,554,432) — a benchmark defined by IBM, measuring combined qubit count, connectivity, and fidelity.
- **2025-03:** Quantinuum H2-1, with JPMorgan Chase, Argonne National Laboratory, Oak Ridge National Laboratory, and UT Austin, published a peer-reviewed result in Nature (March 2025) demonstrating certified quantum randomness generation — 71,313 bits of entropy certified using exascale classical verification. This is among the strongest peer-reviewed "beyond-classical" demonstrations to date from any quantum hardware provider.
- **2024-09:** Microsoft and Quantinuum demonstrated 12 logical qubits using qubit virtualization on H2, with an end-to-end hybrid quantum-classical chemistry simulation. Published as arXiv preprint; peer review status not confirmed as of April 2026.
- **2024-04:** Quantinuum reported 99.9% two-qubit gate fidelity on its H2 system across all qubit pairs — crossing a threshold widely viewed as necessary for practical quantum error correction. Reported in a company blog post; the underlying H2 characterization paper (arXiv:2305.03828) was published peer-reviewed in *Physical Review X*, Vol. 13, article 041052 (2023), with an earlier ~1.84×10⁻³ infidelity figure; subsequent fidelity improvements were announced as company releases, not via additional peer-reviewed publications as of April 2026.
- **2023-05:** Published H2 system characterization in *Physical Review X* (PRX) — the racetrack QCCD architecture paper (arXiv:2305.03828). Peer-reviewed; two-qubit gate infidelity measured at 1.84(5)×10⁻³ on the initial system (32 qubits at launch, later upgraded to 56).
- **2023-02:** Rajeeb (Raj) Hazra appointed CEO; Ilyas Khan moved to Chief Product Officer and Vice-Chairman.
- **2023-11:** Tony Uttley stepped away from his role as President & COO.
- **2021-11:** Quantinuum officially formed via merger of Honeywell Quantum Solutions and Cambridge Quantum Computing.
- **2021:** TKET made fully open source (source code released on GitHub); prior versions had been released as a Python package since ~2019.

## Key People

### Rajeeb (Raj) Hazra — President & CEO

- **LinkedIn:** [https://www.linkedin.com/in/rhazra/](https://www.linkedin.com/in/rhazra/)
- **Google Scholar:** Not applicable (industry executive, non-research background)
- **Appointed CEO:** February 14, 2023 (effective immediately)
- **Previous roles:** SVP and GM, Compute and Networking Business Unit, Micron Technology (responsibility for >$12B annual P&L); 25 years at Intel Corporation (Enterprise and Government Group, Technical Computing Group, Supercomputer Architecture and Planning, Systems Technology Research); earlier career with Lockheed Corporation at NASA Langley Research Center.
- **Education:** PhD and MS in Computer Science, College of William and Mary; BS in Computer Science, Jadavpur University, Kolkata, India. Holds 16 patents.
- **Context:** Hazra is a semiconductor and HPC industry executive, not a quantum physicist. His appointment alongside Ilyas Khan's shift to CPO signals a maturation of Quantinuum toward commercial and operational scale rather than research leadership.

### Ilyas Khan — Founder, Chief Product Officer & Vice-Chairman

- **LinkedIn:** [https://uk.linkedin.com/in/ilyas-khan-ksg-2a899453](https://uk.linkedin.com/in/ilyas-khan-ksg-2a899453)
- **Google Scholar:** Not applicable (non-research background)
- **Role:** Founder of Cambridge Quantum Computing (2014); served as CEO of CQC through the 2021 Quantinuum merger; served as CEO of Quantinuum until February 2023; transitioned to Chief Product Officer and Vice-Chairman upon Hazra's appointment.
- **Background:** Financier and technology entrepreneur. Founded CQC using personal capital in 2014 as a commercial software company focused on quantum computation. Holds Knight Commander of the Order of the Star of Ghana (KSG) honor. Not a quantum physicist — assembled technical leadership from academia.
- **Context:** Khan's shift from CEO to CPO/Vice-Chairman while retaining significant equity stake (via Cambridge Quantum Holdings) means he remains the largest non-Honeywell controlling shareholder and a strategic voice in product direction.
- **⚑ Conflict of interest flag:** As both CPO and major shareholder through CQC Holdings (~36% of the company), Khan has interests that may not always align with outside investors. This is publicly disclosed.

### Tony Uttley — Former President & COO

- **LinkedIn:** [https://www.linkedin.com/in/tony-uttley-8597667](https://www.linkedin.com/in/tony-uttley-8597667)
- **Departed:** November 2023 (announced step-away; full departure confirmed)
- **Previous role at Quantinuum:** President and Chief Operating Officer from company's founding (2021) through his departure
- **Background prior to Quantinuum:** President, Honeywell Quantum Solutions (the predecessor to Quantinuum's hardware division); previously Operations Manager at NASA. Uttley was the founding senior executive of Honeywell's quantum program and the primary architect of merging it with CQC.
- **Post-Quantinuum:** CEO, Enginuity Power Systems (per public records)
- **Context:** Uttley's departure eliminated the last Honeywell-side operational founder. His role was absorbed by Hazra and Khan.

### People — Last Reviewed: 2026-04-05

## Roadmap

Quantinuum unveiled a formal roadmap to universal, fully fault-tolerant quantum computing in September 2024 and has updated it as of November 2025. The roadmap names successive hardware generations by celestial body.

| System | Physical Qubits (approx.) | Target Year | Status (April 2026) | First Published |
|--------|--------------------------|-------------|---------------------|-----------------|
| Helios | 98 | 2025 | ✓ Launched November 2025 | September 2024 roadmap |
| Sol | "hundreds" (2D grid) | 2027 | Target; not yet announced as released | November 2025 |
| Apollo | "thousands" | 2029 | Target; described as first fully fault-tolerant universal system | September 2024 roadmap |

**Fault-tolerant capability milestones (from company roadmap, published September 2024 and November 2025):**

| Milestone | Target Year | Status (April 2026) | Notes |
|-----------|-------------|---------------------|-------|
| Demonstrate logical qubit benchmark | 2025 | Partially met — 48 logical qubits shown (Helios, November 2025) | Demonstrated at launch; error-correcting codes at 2:1 encoding ratio |
| Beyond break-even logical qubits | 2025–2026 | Met — arXiv:2602.22211 (February 2026) | 94 logical qubits outperform unencoded; preprint only |
| Fault-tolerant algorithm execution | 2026 | Met — arXiv:2603.04584 (March 2026) | QAOA and HHL on Steane code; preprint only; modest circuit sizes |
| Small error-corrected circuit | 2027 | Target | Sol-class system prerequisite |
| Full fault-tolerant subsystem | ~2029–2030 | Target | Apollo-class system |
| "Millions of gate" deep circuits on hundreds of logical qubits | ~2029–2030 | Target | Apollo commercial claim |

**Roadmap history and skepticism notes:**
- The September 2024 roadmap set 2030 as the target for universal FTQC. A later November 2025 blog post titled "Quantinuum overcomes last major hurdle to deliver scalable universal fault-tolerant quantum computers by 2029" pulled the Apollo target forward to 2029. This represents the first instance of the target date shifting in the published roadmap — notably in an optimistic direction. Treat the 2029 target with caution: the 2029 claim is in a company blog post, not a peer-reviewed engineering analysis of the prerequisites.
- Sol (2027) is a new architectural departure from Helios — a 2D-grid-based QCCD system rather than the current linear/racetrack design. The transition to 2D grid adds architectural complexity that has not been publicly characterized in detail. Delays in Sol would cascade to Apollo.
- Prior to September 2024, Quantinuum did not publish a named roadmap with specific year targets. The 2024 roadmap was the first such public commitment; there is therefore no multi-year track record of milestone adherence or slippage to assess.

## Honeywell Relationship and Ownership

Honeywell owned approximately 54% of Quantinuum as of September 2025 (post-$600M raise), down from an estimated 55%+ at founding. Cambridge Quantum Holdings (controlled by Ilyas Khan) holds approximately 36%. The remainder is held by external investors including JPMorgan Chase, Mitsui, Amgen, Quanta Computer, NVentures, and others.

Honeywell is undergoing a major restructuring, splitting its core Automation, Aerospace, and Advanced Materials businesses into three independent public companies by late 2026. Quantinuum is not part of this split but is being positioned for an eventual IPO — Honeywell's CEO stated this could occur as early as 2027. Honeywell's investment in Quantinuum flows through its P&L as roughly $250M in annual spending; an IPO would separate this cost and allow Quantinuum to access public capital markets.

**Independence assessment:** Quantinuum operates with meaningful operational independence — it sets its own research agenda, sells to customers across the competitive landscape (including parties Honeywell may compete with in industrial automation), and has attracted non-Honeywell investors who would resist purely strategic subordination. However, Honeywell's majority ownership means board control and capital allocation decisions ultimately require Honeywell's agreement. The $600M September 2025 raise was announced by Honeywell, not Quantinuum, and the press release was from Honeywell's IR function. Strategic alignment with Honeywell's industrial customer base (aerospace, building automation, industrial sensing) exists but appears limited: Quantinuum's primary commercial customer segments are finance, pharmaceuticals, and chemistry — areas where Honeywell has little overlap. No evidence found of Quantinuum being steered toward Honeywell's industrial customer base as a primary market.

**Financial transparency:** Quantinuum is private and files no public financials. Revenue, profitability, and cost structure are unverified. The $10B pre-money valuation is from an investor press release; it cannot be independently confirmed. The company has disclosed aggregate external capital raises but no operating figures.

## Cambridge Quantum Software Heritage

Cambridge Quantum Computing (CQC) was founded in 2014 as a software-only quantum computing company. Its primary product was TKET (originally "t|ket⟩"), a quantum circuit compiler and optimization toolkit designed for hardware agnosticism. CQC's key insight was that quantum computers in the NISQ era would be highly heterogeneous — different qubit modalities, different gate sets, different noise profiles — and that a hardware-agnostic compiler could provide lasting value regardless of which hardware platform "won."

TKET was released as a Python package (pytket) and made fully open source in 2021, shortly before the Quantinuum merger. As of 2026, TKET is available on GitHub (github.com/CQCL/tket) and PyPI, and is used by researchers running circuits on IBM, Google, IonQ, Rigetti, and Quantinuum systems. The package has thousands of users and is cited in academic publications as the compilation backend. For the Helios system's new software stack, TKET serves as the compiler/optimizer for Guppy programs (a higher-level quantum programming language being developed by Quantinuum).

**Durable moat assessment:** TKET's open-source status is a double-edged sword. It maximizes adoption and reduces friction for developers, which creates network effects and community-driven improvement — a genuine strategic advantage. However, it reduces direct monetization leverage; users of TKET on IBM hardware are not Quantinuum customers in any direct sense. The moat from TKET is primarily ecosystem stickiness: developers familiar with TKET are more likely to choose Quantinuum hardware for serious workloads, especially as Quantinuum hardware leads on fidelity. InQuanto (the computational chemistry platform) is the primary proprietary software product and is sold commercially to pharmaceutical and materials companies. Independent academic use of InQuanto has been documented in publications from partner institutions. The true moat durability depends on whether Quantinuum's hardware fidelity lead is maintained; if other platforms close the gap, the software heritage becomes less defensible as a differentiator.

## Claim Verification

### Claim: Highest Two-Qubit Gate Fidelity of Any Publicly Demonstrated Commercial System (Helios: 99.921%)

**Status:** Partially verified (company-authored preprint; not yet independently replicated; figures are system-averaged, not cherry-picked)

**Supporting sources:**
- [arXiv:2511.05465](https://arxiv.org/abs/2511.05465) — Quantinuum-authored preprint (November 2025); reports 7.9(2)×10⁻⁴ average two-qubit gate infidelity (99.921% fidelity) averaged over all operational zones of the 98-qubit Helios system. The "averaged over all qubit pairs" scope is important: the figure is not reported for a subset of qubits, which is a meaningful methodological strength.
- [HPCwire, April 2024](https://www.hpcwire.com/2024/04/16/quantinuum-reports-99-9-2-qubit-gate-fidelity-caps-eventful-2-months/) — independent trade press coverage of the earlier H2 99.9% result; confirms the milestone was communicated publicly.
- [Forschungszentrum Jülich / Purdue benchmarking study](https://docs.quantinuum.com/systems/user_guide/hardware_user_guide/benchmarks/system_benchmarks.html) — independent benchmarking (academic institutions) placed Quantinuum H2-1 at the top of a comparative evaluation; partial independent support.

**Refuting / questioning sources:**
- The 99.921% figure appears only in the Quantinuum-authored arXiv:2511.05465 (November 2025 preprint). As of April 2026, no peer-reviewed journal publication of this result has been identified. No independent lab has yet reproduced the measurement on Helios.
- The prior H2 peer-reviewed result (PRX, 2023, arXiv:2305.03828) reported a 1.84(5)×10⁻³ infidelity (98.16% fidelity) on the initial 32-qubit H2 configuration. Subsequent fidelity improvements — including crossing the 99.9% threshold — were announced via company blog posts, not peer-reviewed publications. The gap between the PRX paper and the current 99.921% claim is a sequence of company-released improvements, not a chain of independently verified measurements.
- IonQ claimed 99.99% two-qubit gate fidelity in October 2025 (EQC prototype), but on a research prototype rather than a commercially deployed system. If validated, this would exceed Helios — but it also remains unpublished in peer-reviewed form.

**Independent replication status:** None identified for the Helios 99.921% figure. The prior H2 ~99.9% figure has partial independent support from the Jülich/Purdue benchmarking study.

**Classical simulation feasibility:** Not applicable to a gate fidelity measurement.

**Peer review status:** Partially. The underlying H2 architecture was published peer-reviewed in PRX (2023). The specific Helios fidelity figures are from an arXiv preprint (2511.05465, November 2025) not yet in a peer-reviewed journal.

**System-level or subset?** The reported figures are averaged over all operational zones and qubit pairs in the system — an important distinction from subset-optimized benchmarks. This methodological choice supports the credibility of the claim.

**Summary:** The claim of "highest publicly demonstrated two-qubit gate fidelity" is consistent with all published data and not contradicted by any independent measurement. However, it rests on company-authored preprints, not peer-reviewed publications. The claim should be treated as Partially Verified: plausible, internally consistent, architecturally sourced, but not independently replicated.

---

### Claim: 48 Logical Qubits Demonstrated at Helios Launch (Concatenated Error Correcting Codes)

**Status:** Partially verified (same preprint as above; demonstrations of fault-tolerant primitives, not fault-tolerant computation)

**Supporting sources:**
- [arXiv:2511.05465](https://arxiv.org/abs/2511.05465) — Helios launch preprint; documents 48 logical qubits using concatenated iceberg codes with a 2:1 encoding ratio.
- [MIT Technology Review, November 2025](https://www.technologyreview.com/2025/11/05/1127659/a-new-ion-based-quantum-computer-makes-error-correction-simpler/) — independent mainstream technology press coverage; confirms the demonstration was real and noteworthy.
- [IEEE Spectrum](https://spectrum.ieee.org/quantinuum-fault-tolerant-quantum-computing) — covered the fault-tolerant milestones.

**Refuting / questioning sources:**
- **Critical precision:** 48 logical qubits at a 2:1 encoding ratio means 48 logical qubits encoded in ~96 physical qubits. This is not the same as a fully fault-tolerant quantum computer with independently error-corrected logical qubits capable of arbitrarily deep circuits. The iceberg code used is a low-rate code that trades computational capacity for error protection at modest overhead — appropriate for the current qubit count, but not the surface code approach typically discussed for large-scale fault tolerance.
- "Fault-tolerant primitives" (mid-circuit measurement, feedforward, logical gates) have been demonstrated. "A fault-tolerant quantum computer" has not been demonstrated. These are different claims at different levels of the engineering stack.
- The encoding at 2:1 ratio and the iceberg code's distance-4 structure means the logical qubit error suppression is real but limited; deep circuits with millions of gates (the Apollo goal) would require much higher encoding ratios and lower physical error rates than current systems provide.

**Peer review status:** Not peer-reviewed (arXiv preprint, November 2025).

**Independent replication:** None identified.

**Summary:** The demonstration of 48 logical qubits with genuine error suppression (beyond break-even) is a real milestone — among the most advanced demonstrated by any quantum hardware provider. It is not, however, evidence of a fault-tolerant quantum computer capable of arbitrary-depth computation. Partially Verified (company preprint, physically plausible, consistent with hardware parameters, but unreviewed and not independently replicated).

---

### Claim: 94 Logical Qubits Beyond Break-Even (arXiv:2602.22211, February 2026)

**Status:** Partially verified (Quantinuum-authored arXiv preprint; not peer-reviewed; physically consistent with Helios specifications)

**Supporting sources:**
- [arXiv:2602.22211](https://arxiv.org/abs/2602.22211) — "Computing with many encoded logical qubits beyond break-even" (February 25, 2026); demonstrates logical gate error rates ~10–100× below physical error rates across multiple benchmarks on Helios.
- [Quantum Computing Report coverage](https://quantumcomputingreport.com/quantinuum-implements-high-rate-iceberg-codes-on-helios-processor/) — independent trade press.
- [The Quantum Insider](https://thequantuminsider.com/2026/03/10/quantinuum-researchers-demonstrates-quantum-computations-with-dozens-of-protected-logical-qubits/) — March 2026 trade coverage.

**Refuting / questioning sources:**
- This is a Quantinuum-authored preprint with 45 authors, not independently replicated. Authors are affiliated with Quantinuum; no external research institution co-authored the measurement.
- "Beyond break-even" means logical error rates lower than physical error rates — a necessary but not sufficient condition for fault-tolerant computation. At 94 logical qubits with the iceberg code, the actual logical error suppression is real but the circuits remain shallow. Deeper circuits with more logical gates would accumulate errors faster.
- The iceberg code is a high-rate code that provides error detection (not full error correction in the Steane/surface code sense) at the 94-qubit end of the demonstration. Error correction is demonstrated separately with 48 logical qubits. This distinction matters: detection codes catch errors but cannot correct them; correction codes can.

**Peer review status:** Not peer-reviewed (arXiv preprint, February 2026).

**Independent replication:** None.

**Summary:** Partially Verified. The result is consistent with published Helios hardware specifications and represents a genuine advance in high-rate encoded computation. Key caveat: detection vs. correction code distinction, Quantinuum-only authorship, no independent replication.

---

### Claim: Fault-Tolerant Algorithm Execution (arXiv:2603.04584, March 2026)

**Status:** Partially verified (JPMorgan Chase co-authorship adds independent weight; still arXiv preprint; circuit sizes are small)

**Supporting sources:**
- [arXiv:2603.04584](https://arxiv.org/abs/2603.04584) — Ruslan Shaydulin (JPMorgan Chase) corresponding author; demonstrates QAOA (5–12 logical qubits, Steane code [[7,1,3]]) and HHL (Poisson equation) on H2 and Helios. JPMorgan Chase researchers co-authoring provides meaningful independence.

**Refuting / questioning sources:**
- Circuit sizes remain small (5–12 logical qubits; algorithms chosen for toy instances, not commercially relevant workloads). "Near-break-even performance" on larger QAOA circuits suggests the fault-tolerant overhead is still penalizing at scale.
- HHL applied to the Poisson equation is a toy problem (structured, classical-simulation feasible). No claim of quantum advantage over classical compute is made.
- Steane code [[7,1,3]] uses 7 physical qubits per logical qubit — a significant overhead that limits the usable logical qubit count at current hardware scales.

**Peer review status:** Not peer-reviewed (arXiv, March 2026).

**Independent replication:** JPMorgan Chase co-authorship is meaningful but not independent replication in the full sense.

**Summary:** Partially verified. The first demonstration of end-to-end fault-tolerant algorithm execution on real hardware is a genuine milestone. JPMorgan Chase's co-authorship adds credibility beyond a purely internal Quantinuum result. Caveats: small circuit sizes, toy problem instances, not yet peer-reviewed.

---

### Claim: Certified Quantum Randomness (Nature, March 2025)

**Status:** Verified (peer-reviewed in Nature; multi-institutional authorship; exascale classical verification)

**Supporting sources:**
- [Nature, March 2025](https://www.nature.com/articles/s41586-025-08737-1) — peer-reviewed publication; JPMorgan Chase, Quantinuum, Argonne National Laboratory, Oak Ridge National Laboratory, and UT Austin as co-authors.
- [arXiv:2503.20498](https://arxiv.org/abs/2503.20498) — preprint version.
- [OLCF coverage](https://www.olcf.ornl.gov/2025/05/05/quantum-computing-experiment-realizes-verifiably-random-number/) — Oak Ridge confirmation.

**Refuting / questioning sources:**
- "Certified randomness" is a specific cryptographic property, not a demonstration of general quantum advantage for computation. The result demonstrates a quantum computer can generate verifiable random numbers faster than a classical computer could fake them (given assumptions about the adversary). This is a real result but a narrow application domain.
- The certified entropy (71,313 bits) required enormous classical verification resources (~1.1×10¹⁸ FLOP/s across multiple supercomputers). The practical deployment of this protocol at scale would require similar verification infrastructure.

**Classical simulation feasibility:** The randomness certified relies on the computational hardness of random circuit sampling — the same complexity-theoretic assumption underlying Google's 2019 Sycamore claim. Whether this assumption holds for all adversary models is an open theoretical question.

**Summary:** Verified (peer-reviewed, multi-institutional). The strongest independently validated "beyond-classical" result from Quantinuum to date. Caveat: it is a specific, narrow application (certified randomness), not general quantum computational advantage.

---

### Claim: H2 System Two-Qubit Gate Fidelity >99.9% (System-Level, All Qubit Pairs)

**Status:** Partially verified (underlying architecture peer-reviewed in PRX; the specific 99.9%+ claim was made via company blog post in April 2024, not via peer-reviewed publication)

**Supporting sources:**
- [Physical Review X, Vol. 13, No. 041052 (2023)](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.041052) — peer-reviewed publication of the H2 racetrack QCCD architecture (arXiv:2305.03828); reports 1.84(5)×10⁻³ infidelity (98.16% fidelity) on the initial 32-qubit configuration in 2023.
- [Quantinuum blog, April 2024](https://www.quantinuum.com/blog/quantinuum-extends-its-significant-lead-in-quantum-computing-achieving-historic-milestones-for-hardware-fidelity-and-quantum-volume) — reports crossing the 99.9% threshold for the 56-qubit H2 system. Company blog post, not peer-reviewed.
- Forschungszentrum Jülich/Purdue independent benchmark — placed H2-1 first in a comparative evaluation; partial independent corroboration.

**Refuting / questioning sources:**
- The journey from 98.16% (PRX 2023) to >99.9% (company blog 2024) is a significant improvement unaccompanied by an equivalent peer-reviewed characterization paper. The improvements are described in company releases but not in publications with the methodological detail of the original PRX paper.

**Peer review status:** Partially. The architecture and initial fidelity are peer-reviewed (PRX 2023). The >99.9% specific figure is from company releases.

**Summary:** Partially Verified. The H2 architecture and initial performance are peer-reviewed. The specific claim of >99.9% two-qubit fidelity for the 56-qubit configuration relies on company announcements without an equivalent characterization paper; independent benchmarking partially corroborates.

## Key Organizations

- **Honeywell International** — majority owner (~54%); provided the original hardware division (Honeywell Quantum Solutions); key to Quantinuum's capital position; planning IPO by 2027.
- **Cambridge Quantum Computing Holdings** (Ilyas Khan) — ~36% owner; contributed TKET, InQuanto, Quantum Origin software assets; ongoing software leadership.
- **JPMorgan Chase** — equity investor and major research partner; co-authored the certified randomness Nature paper and the fault-tolerant algorithm arXiv paper; among the most credible commercial partners in Quantinuum's portfolio.
- **Microsoft** — collaborated on logical qubit demonstrations on H2 (2024); Microsoft's qubit virtualization system combined with Quantinuum hardware for error correction experiments. Note: Microsoft develops its own topological qubit approach and is also a commercial quantum competitor; this is a research collaboration, not a commercial partnership implying exclusive alignment.
- **Mitsui** — Japanese equity investor; Quantinuum has a Japanese subsidiary with active expansion.

## Sources

- [Quantinuum Corporate Site](https://www.quantinuum.com) — products, press releases, blog posts
- [Helios arXiv preprint (2511.05465)](https://arxiv.org/abs/2511.05465) — 98-qubit system characterization; 99.921% two-qubit fidelity; 48 logical qubits
- [H2 racetrack QCCD paper, PRX 2023 (arXiv:2305.03828)](https://arxiv.org/abs/2305.03828) — peer-reviewed H2 architecture characterization; Physical Review X Vol. 13, 041052
- [arXiv:2602.22211 — "Computing with many encoded logical qubits beyond break-even"](https://arxiv.org/abs/2602.22211) — February 2026; 94 logical qubits on Helios; preprint
- [arXiv:2603.04584 — Fault-tolerant execution of error-corrected quantum algorithms](https://arxiv.org/abs/2603.04584) — March 2026; QAOA/HHL on Steane code; JPMorgan Chase + Quantinuum; preprint
- [Nature: Certified Randomness (arXiv:2503.20498)](https://www.nature.com/articles/s41586-025-08737-1) — peer-reviewed; March 2025; multi-institutional; 56-qubit H2-1
- [Honeywell $600M Capital Raise Press Release, September 2025](https://www.honeywell.com/us/en/press/2025/09/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale) — $10B valuation claim; investor details
- [Honeywell $300M Round Press Release, January 2024](https://www.quantinuum.com/press-releases/honeywell-announces-the-closing-of-300-million-equity-investment-round-for-quantinuum-at-5b-pre-money-valuation) — $5B pre-money valuation at prior round
- [Quantinuum Accelerated Roadmap Press Release, September 2024](https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030) — formal roadmap; Apollo 2030 target
- [HPCwire: Helios and Roadmap to Apollo, November 2025](https://www.hpcwire.com/2025/11/05/quantinuum-introduces-helios-quantum-system-as-roadmap-advances-toward-apollo/) — Sol (2027) and Apollo (2029/2030) milestone coverage
- [Quantinuum: "Overcomes last major hurdle," blog post claiming 2029 Apollo target](https://www.quantinuum.com/blog/quantinuum-overcomes-last-major-hurdle-to-deliver-scalable-universal-fault-tolerant-quantum-computers-by-2029) — revised 2029 date (company blog; treat with caution)
- [Rajeeb Hazra CEO appointment, February 2023](https://www.quantinuum.com/press-releases/quantinuum-names-rajeeb-raj-hazra-chief-executive-officer) — leadership transition details
- [Tony Uttley departure, November 2023](https://thequantuminsider.com/2023/11/16/tony-uttley-to-step-away-from-quantinuum/) — COO step-away announcement
- [TKET open source announcement](https://www.quantinuum.com/blog/just-the-tket-quantum-software-tool-now-open-source) — TKET open-sourcing
- [Quantinuum H2 Product Data Sheet](https://docs.quantinuum.com/systems/data_sheets/Quantinuum%20H2%20Product%20Data%20Sheet.pdf) — official system specifications
- [MIT Technology Review: Helios review, November 2025](https://www.technologyreview.com/2025/11/05/1127659/a-new-ion-based-quantum-computer-makes-error-correction-simpler/) — independent assessment of Helios launch
- [Quantinuum Wikipedia](https://en.wikipedia.org/wiki/Quantinuum) — general background, merger history
