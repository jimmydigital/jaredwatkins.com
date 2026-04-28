---
title: "D-Wave Quantum"
date: 2026-04-14
lastmod: 2026-04-14
draft: false
description: "D-Wave (NYSE: QBTS) makes quantum annealers — not gate-based quantum computers. Its Advantage2 processor uses analog optimization for combinatorial problems. Quantum advantage claims are actively disputed by independent researchers."
tags: ["quantum-computing", "annealing", "optimization", "canada", "cloud-access", "hybrid-classical-quantum"]
categories: ["company"]
research_area: "quantum-computing"
source_urls:
  - "https://www.dwavequantum.com"
  - "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001907982&type=10-K"
  - "https://www.nature.com/articles/s41586-023-05867-2"
  - "https://www.science.org/doi/10.1126/science.ado6285"
  - "https://arxiv.org/abs/2403.00910"
  - "https://arxiv.org/abs/2603.18825"
  - "https://arxiv.org/html/2503.08247"
  - "https://quantumcomputingreport.com/d-wave-launches-advantage2-quantum-system-with-4400-qubits-and-higher-coherence/"
  - "https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-fourth-quarter-and-year-end-2025-results/"
last_reviewed: 2026-04-14
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


> **⚠ Critical framing:** D-Wave builds **quantum annealers**, not gate-based quantum computers. Quantum annealing is an analog optimization technique fundamentally different from the gate-based approaches used by IBM, Google, IonQ, and Quantinuum. D-Wave's physical qubit counts are not comparable to gate-based qubit counts — they measure something else entirely. This distinction must be kept in mind throughout this entry.

## Summary

D-Wave Quantum (NYSE: QBTS) is the oldest commercial quantum computing company, founded in 1999 and headquartered in Burnaby, British Columbia, Canada. It designs, manufactures, and sells quantum annealing systems and hybrid classical-quantum solvers, primarily targeting combinatorial optimization problems. D-Wave's Advantage2 system entered general availability in November 2024 with 4,400+ qubits in Zephyr topology. The company went public via SPAC in August 2022 and in January 2026 announced the acquisition of Quantum Circuits Inc. for $550 million to accelerate entry into the gate-based market.

D-Wave's quantum advantage claims — most recently a March 2025 paper in *Science* — are among the most contested in the quantum computing field. Multiple independent research groups have produced classical simulations partially replicating D-Wave's results, and the scope and generality of the claimed advantage remain actively disputed.

## Key Facts

- **Founded:** 1999
- **Headquarters:** Burnaby, British Columbia, Canada
- **Stock:** NYSE: QBTS (public since August 5, 2022, via SPAC merger with DPCM Capital)
- **Type:** Company — quantum annealing hardware and hybrid solver cloud service
- **Status:** Active, publicly traded, pre-profitability
- **Modality:** Quantum annealing — **not gate-based quantum computing**
- **Current system:** Advantage2 (4,400+ qubits, Zephyr topology; GA November 2024)
- **FY2025 adjusted EBITDA loss:** ~$71.8M (from company reports; see Financial section)
- **Cash position:** $884.5M (December 2025, after capital raises)
- **Key metric caveat:** Physical qubit counts in a D-Wave annealer are not comparable to qubit counts in gate-based systems — see "What It Is / How It Works" section

## What It Is / How It Works

### Quantum Annealing vs. Gate-Based Quantum Computing

The most important thing to understand about D-Wave is what it is *not*. IBM, Google, IonQ, and Quantinuum build **gate-based quantum computers** — universal-ish machines that apply discrete quantum logic gates to qubits, in principle capable of running any quantum algorithm. D-Wave builds **quantum annealers**, which are a fundamentally different type of machine.

A quantum annealer is an analog device designed to find low-energy states of a physical system called an Ising model. This process naturally maps onto certain combinatorial optimization problems — where the goal is to find the best configuration among many possibilities. The annealer exploits quantum tunneling and quantum fluctuations to explore the solution space, potentially escaping local minima more efficiently than purely classical approaches.

**Why qubit counts are not comparable:** In a D-Wave annealer, a physical qubit is a superconducting flux qubit that participates in an analog energy minimization process. The qubit count tells you the size of problems the annealer can represent directly. In a gate-based quantum computer, a physical qubit is a two-state quantum system that must be manipulated with high fidelity through discrete gate operations. Gate-based qubit counts are limited by the need for very high gate fidelity and coherence. D-Wave can have 4,400+ physical qubits precisely *because* it doesn't need to maintain the extreme fidelity required for gate operations — but this also means those qubits cannot execute Shor's algorithm, run quantum chemistry simulations in the standard sense, or do anything outside the optimization problem class the architecture was designed for.

Comparing D-Wave's 4,400+ physical qubits to IBM's 1,000+ physical qubits and concluding D-Wave is "more powerful" is a category error. They are solving different classes of problems with different methods.

### The Advantage2 System

D-Wave's current production system, the Advantage2, entered general availability in November 2024. It features:

- **4,400+ physical qubits** in the new **Zephyr topology**
- **Zephyr connectivity:** Each qubit connects to up to 20 other qubits (up from 15 in the prior Advantage/Pegasus system)
- **40,000+ couplers**
- **40% higher energy scale** than the prior Advantage system, which reduces the effect of thermal noise
- **Longer coherence times and lower flux noise** than Advantage
- **Operating temperature:** ~18 millikelvin, achieved by dilution refrigerator cooling

The prior Advantage system (5th generation, still available) used the Pegasus topology with 5,640 qubits and 15-way connectivity. The smaller qubit count in Advantage2 versus Advantage is intentional — Zephyr topology offers better connectivity per qubit and higher coherence, which in practice means more effective embedding of real optimization problems.

An earlier Advantage2 **prototype** was demonstrated with claims of ~7,000 physical qubits; the production system settled at 4,400+. The prototype specification should not be cited as the current production system.

### Hybrid Classical-Quantum Solvers

D-Wave's most commercially relevant product is its **hybrid solver service** on the Leap cloud platform, not the bare quantum annealer. Hybrid solvers decompose large optimization problems into subproblems, solve appropriate pieces on the quantum annealer, and integrate the results with classical algorithms. This approach handles problems much larger than the annealer can address directly and is where most customer use cases live. D-Wave describes this as a key commercial differentiator over purely gate-based approaches for near-term optimization workloads.

### The Leap Cloud Platform

D-Wave's cloud service, **Leap**, provides access to both bare quantum annealing hardware and hybrid solvers. It integrates with AWS Marketplace and supports Python-based problem formulation via the **Ocean SDK**. As of late 2024, D-Wave reported 200+ million customer jobs processed since Leap's launch.

## Notable Developments

- **2026-01:** D-Wave announced the acquisition of **Quantum Circuits Inc. (QCI)** for $550 million ($300M stock + $250M cash), signaling a major pivot to also pursuing gate-based quantum computing. QCI's technology uses dual-rail superconducting qubits with built-in error detection. D-Wave's stated roadmap from the acquisition: 17-qubit system in 2026, 49-qubit in 2027, 181-qubit in 2028. D-Wave also claimed an "industry-first" demonstration of scalable on-chip cryogenic control for gate-model qubits. *Verification status: company press release; acquisition close and technical claims not yet independently replicated.* (Partially verified)

- **2025-03:** D-Wave published a paper in *Science* (King et al., 61+ co-authors, 11 institutions) claiming quantum supremacy for simulation of magnetic material dynamics — specifically, that a D-Wave annealer solved the problem in minutes while claiming a classical supercomputer would require ~1 million years. Within days, independent teams published rebuttals (see Claim Verification section). (Disputed)

- **2024-11:** Advantage2 entered **general availability** with 4,400+ qubits in Zephyr topology. 314% usage growth reported for Advantage2 over the prior year as of January 2026. (Partially verified — usage growth from company report)

- **2023-05:** King et al. published "Quantum critical dynamics in a 5,000-qubit programmable spin glass" in *Nature* (vol. 617, pp. 61–66; DOI: 10.1038/s41586-023-05867-2), demonstrating coherent quantum dynamics on 5,000+ qubits and extracting critical exponents differentiating quantum annealing from classical Monte Carlo. This was a quantum simulation result, not an optimization result, and came before the Advantage2 production launch. (Peer-reviewed; interpretation of advantage scope is debated)

- **2022-08:** D-Wave went public on NYSE as QBTS via SPAC merger with DPCM Capital, Inc. (announced February 2022). Transaction valued the combined company at $1.6 billion; gross proceeds ~$340 million including $40M PIPE from Goldman Sachs Asset Management, PSP Investments, NEC Corporation, and others.

- **2022-10:** Advantage2 prototype demonstrated publicly. The prototype specification (~7,000 qubits) is distinct from the production system.

## Quantum Advantage Claims — The Controversy

**This section requires careful reading.** D-Wave has published multiple papers claiming quantum advantage or quantum supremacy. These claims are contested to varying degrees.

### The 2023 Nature Paper

King et al. (2023) reported coherent quantum dynamics in a D-Wave Advantage system emulating frustrated quantum magnets. The paper demonstrated that the annealer could track quantum dynamics of a spin system in ways distinguishable from classical Monte Carlo simulation — specifically, it reproduced the correct quantum critical exponents while classical methods required significant approximation. This paper was peer-reviewed and published in *Nature*, making it one of the more credible D-Wave publications.

However, the scope is important: this was a **quantum simulation** result, not an optimization result. The demonstration was on a specific class of magnetic phase transition problems, not on general optimization. The quantum advantage shown was specifically in simulating quantum dynamics, not in solving practical optimization problems faster.

### The 2025 Science Paper and Immediate Controversy

King et al. (2025), in *Science* vol. 388, pp. 199–204 (DOI: 10.1126/science.ado6285; arXiv: 2403.00910), claimed "beyond-classical computation in quantum simulation" — that a D-Wave annealer solved a magnetic material simulation problem in minutes where a classical supercomputer would take ~1 million years. The paper involved 61+ co-authors and 11 institutions, and represents D-Wave's strongest "quantum supremacy" claim to date.

Within days of the March 2025 publication, independent research groups published direct rebuttals:

1. **NYU (Dries Sels) tensor network method:** Sels' group at New York University reported replicating D-Wave's calculations on a regular laptop in approximately 2 hours using tensor network methods (arXiv: 2603.18825). The argument was that D-Wave's problem, while quantum mechanical in nature, could be tackled without quantum entanglement using efficient classical mathematical representations.

2. **EPFL and Flatiron Institute GPU method:** Using variational Monte Carlo (t-VMC) with Jastrow-Feenberg ansatz on classical computers, this team solved the same class of problems using 4 GPUs over 3 days (arXiv: 2503.08247). The classical approach had limitations — it worked for systems up to approximately 54 qubits, smaller than the full D-Wave problem scale.

3. **D-Wave's response:** Senior Distinguished Scientist Andrew King disputed both rebuttals, stating that critics "didn't do all the problems that we did, they didn't do all the sizes we did, they didn't do all the observables we did." King reported scaling D-Wave's quantum calculations to 3,200+ qubits to refute the criticisms. D-Wave's position is that leading approximate methods (tensor networks, neural networks) cannot achieve D-Wave's accuracy across the full problem range in reasonable time frames.

**Current status:** The controversy remains unresolved as of April 2026. The debate is not "D-Wave is wrong" vs. "D-Wave is right" — it is more nuanced. The key question is the **scaling behavior**: classical methods appear to work on smaller instances; D-Wave's claim rests on classical methods failing at large problem sizes. Neither side has definitively closed this argument. The "1 million years" figure specifically has not been validated by independent parties.

## Claim Verification

### Claim: Advantage2 has 4,400+ physical qubits in Zephyr topology

**Status:** Partially verified

**Supporting sources:**
- [Quantum Computing Report — Advantage2 Launch](https://quantumcomputingreport.com/d-wave-launches-advantage2-quantum-system-with-4400-qubits-and-higher-coherence/) — reports GA launch with 4,400+ qubits and Zephyr topology
- [HPCWire — Advantage2 Ready](https://www.hpcwire.com/2024/11/06/d-wave-readies-4400-plus-qubit-advantage2-system-for-use/) — corroborates GA announcement and specs
- [D-Wave product documentation](https://www.dwavequantum.com/solutions-and-products/systems/) — company source

**Refuting / questioning sources:**
- None found disputing the qubit count itself; however, the prototype (~7,000 qubit claims) was widely cited before GA and should not be confused with production specs

**Summary:** Qubit count and topology appear consistent across multiple independent trade sources; labeled Partially verified (no peer-reviewed independent benchmarking of the production Advantage2 specs found as of this writing).

---

### Claim: 2025 *Science* paper demonstrates quantum supremacy (classical would take ~1 million years)

**Status:** Disputed

**Supporting sources:**
- [King et al. (2025), *Science* 388:199–204](https://www.science.org/doi/10.1126/science.ado6285) — peer-reviewed, 11 institutions, 61+ co-authors; specific problem class is simulation of quantum magnetic dynamics (Transverse-field Ising model dynamics); classical figure derives from D-Wave's extrapolation of classical DMRG scaling

**Refuting / questioning sources:**
- [Sels et al. (2025), arXiv:2603.18825](https://arxiv.org/abs/2603.18825) — NYU tensor network approach solves D-Wave's problems on a laptop in ~2 hours; claims quantum entanglement not required
- [EPFL/Flatiron t-VMC paper, arXiv:2503.08247](https://arxiv.org/html/2503.08247) — 4 GPUs, 3 days for same problem class; limited to ~54 qubit problem sizes
- [Physics World coverage](https://physicsworld.com/a/d-wave-systems-claims-quantum-advantage-but-some-physicists-are-not-convinced/) — summarizes independent skepticism
- [SiliconANGLE, March 2025](https://siliconangle.com/2025/03/12/d-wave-claims-achieved-quantum-supremacy-last-others-disagree/) — covers immediate controversy following publication

**Classical simulation feasibility:** Demonstrated partially — classical methods work at smaller scales, and the full-scale case remains actively contested. The "1 million years" extrapolation has not been independently validated.

**Independent replication status:** The quantum advantage claim has not been independently replicated. The refutations are peer-reviewed or peer-reviewed preprints; the debate is active.

**Roadmap history:** N/A for this specific claim.

**Summary:** A legitimate peer-reviewed paper in a top journal with contested scope — the classical simulation rebuttals are credible and partially successful, but the full-scale comparison remains unsettled. Do not treat the "1 million years" figure as established.

---

### Claim: 2023 *Nature* paper demonstrates coherent quantum dynamics

**Status:** Partially verified

**Supporting sources:**
- [King et al. (2023), *Nature* 617:61–66](https://www.nature.com/articles/s41586-023-05867-2) — peer-reviewed; demonstrated correct quantum critical exponents in D-Wave Advantage spin glass simulation; co-authored with Boston University researchers (not solely D-Wave)
- PubMed indexed: PMID 37076625

**Refuting / questioning sources:**
- Independent replication of the specific quantum critical dynamics result is limited; the result is narrowly scoped to quantum phase transition simulation, not general optimization

**Classical simulation feasibility:** The quantum critical exponents demonstrated differ from what classical Monte Carlo produces — this is the basis of the advantage claim. Classical replication of the *full* quantum dynamics has not been demonstrated for the problem sizes studied.

**Summary:** Stronger and less contested than the 2025 Science paper, but scoped to quantum simulation of specific magnetic systems — not a general optimization advantage.

---

### Claim: Acquisition of Quantum Circuits Inc. for $550M (January 2026)

**Status:** Partially verified

**Supporting sources:**
- [D-Wave press release](https://www.dwavequantum.com/company/newsroom/press-release/d-wave-to-acquire-quantum-circuits/) — company announcement; $300M stock + $250M cash
- [Data Center Dynamics coverage](https://www.datacenterdynamics.com/en/news/d-wave-acquires-quantum-circuits-inc-for-550m/) — trade press corroboration
- [Next Platform coverage](https://www.nextplatform.com/2026/01/07/d-wave-makes-gate-model-power-move-with-quantum-circuits-buy/) — technical context

**Refuting / questioning sources:**
- Gate-model roadmap claims (17 → 49 → 181 dual-rail qubits, 2026–2028) are unverified company targets; no independent assessment of whether QCI's dual-rail qubit approach is technically superior to competing methods

**Summary:** Acquisition announcement is credible from multiple sources; technical roadmap claims are company-stage projections, not demonstrated results.

---

### Claim: Revenue growth and commercial traction

**Status:** Partially verified

**Supporting sources:**
- SEC 10-K filing (FY2024): [EDGAR filing](https://www.sec.gov/Archives/edgar/data/1907982/000190798225000060/qbts-20241231.htm) — FY2024 QCaaS revenue $5.4M; GAAP net loss $143.9M; adjusted net loss $75.6M (excluding $68.3M non-cash warrant charge)
- [D-Wave Q4 FY2025 press release](https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-fourth-quarter-and-year-end-2025-results/) — Q4 2025 commercial revenue doubled to $3.7M vs $1.8M Q4 2024; cash $884.5M as of Dec 2025; FY2025 adjusted EBITDA loss $71.8M
- 76 commercial customers in trailing 12 months (Q3 2024 10-Q); 28 Fortune 500 customers — company claim from earnings, not independently audited customer list

**Refuting / questioning sources:**
- Revenue remains small relative to operating losses; the path to profitability is not established from public filings
- "Fortune 500" customer count is a company-claimed figure; which companies, whether they are paying customers vs. trial users, is not fully disclosed in public filings

**Summary:** Revenue figures are verifiable from SEC filings; customer names and counts are partially verified from earnings reports. Revenue is growing but extremely small in absolute terms relative to losses.

## Financial Overview

*All figures from SEC filings or D-Wave earnings press releases unless noted. Company uses calendar year.*

**Revenue (QCaaS — cloud quantum computing as a service):**
- FY2024: $5.4M total
- Q4 FY2025: $3.7M (vs. $1.8M Q4 FY2024; ~106% YoY growth)
- FY2025 full year: Not yet disclosed in available filings as of this writing; Q4 indicates strong growth trajectory

**Losses:**
- FY2024 GAAP net loss: $143.9M (includes $68.3M non-cash warrant remeasurement)
- FY2024 adjusted net loss (ex-warrant): $75.6M
- FY2025 adjusted EBITDA loss: $71.8M

**Cash:**
- December 2025: $884.5M in consolidated cash and marketable securities (following significant stock issuances in 2024–2025)

**Context:** D-Wave has funded operations through repeated equity raises, not revenue. The $884.5M cash position provides runway, but the company remains firmly pre-profitability with annual adjusted losses in the $70–75M range.

## Gate-Based Program

In January 2026, D-Wave announced the acquisition of **Quantum Circuits Inc. (QCI)** for $550 million, pivoting D-Wave from a pure-play annealing company to a dual-platform approach. QCI's technology centers on **dual-rail superconducting qubits** — an architecture where each logical qubit is encoded across two physical qubits, enabling built-in error detection without a full surface code overhead.

D-Wave's stated gate-model roadmap (from acquisition announcement):
- **2026:** 17 dual-rail qubit system (general availability claimed)
- **2027:** 49 dual-rail qubit system
- **2028:** 181 dual-rail qubit system

D-Wave also separately claimed an "industry-first" demonstration of scalable on-chip cryogenic control for gate-model qubits in January 2026.

**Verification status:** These are roadmap claims from a company press release. The gate-model program is at the hardware-prototype/roadmap stage. The acquisition close itself is verifiable; the technical roadmap milestones are unverified company projections. The dual-rail approach is a genuine academic research direction (not a fabrication), but claimed commercial delivery timelines for quantum hardware have a long history of slippage.

## Key People

### Alan Baratz — President & CEO
- **Tenure at D-Wave:** CEO since 2020; previously Chief Product Officer and EVP R&D at D-Wave
- **LinkedIn:** [linkedin.com/in/alan-baratz](https://www.linkedin.com/in/alan-baratz/)
- **Prior roles (reverse chronological):**
  - Managing Director, Warburg Pincus LLC
  - Executive roles at Symphony, Avaya, Cisco, IBM
  - CEO/President, Versata; CEO/President, Zaplet; CEO/President, NeoPath Networks
  - First President, JavaSoft at Sun Microsystems (grew Java platform to 80% Fortune 1000 adoption)
- **Education:** Ph.D. Computer Science, MIT; B.S. Computer Science, UCLA
- **Overlap flags:** None identified with other documented Research section entries as of this writing.

### Mark W. Johnson — SVP, Quantum Technologies and Systems Products
- **Tenure at D-Wave:** Joined 2005 as experimental physicist and superconducting circuit design engineer; one of the longest-serving technical executives
- **LinkedIn:** [ca.linkedin.com/in/mark-w-johnson-phd](https://ca.linkedin.com/in/mark-w-johnson-phd)
- **Google Scholar:** [scholar.google.ca/citations?user=12nh5TcAAAAJ](https://scholar.google.ca/citations?user=12nh5TcAAAAJ&hl=en)
- **Role note:** Johnson's title is SVP, Quantum Technologies and Systems Products — sometimes referenced externally as "Chief Quantum Officer" but the official title per D-Wave leadership page is SVP.
- **Education:** Ph.D. Physics, University of Rochester (1996)
- **Overlap flags:** None identified with other documented Research section entries.

### John Markovich — Chief Financial Officer
- **LinkedIn:** Not found with confidence; search returned ambiguous results. <!-- TODO: verify LinkedIn URL for John Markovich, D-Wave CFO -->
- **Prior roles:** Not fully established from public sources

### Stan Black — Chief Information Security Officer (CISO)
- **Appointed:** September 2025
- **Prior roles:** 20+ years cybersecurity leadership at Dell/EMC/RSA/VMware, Citrix, Nuance, Delinea
- **LinkedIn:** Not found with confidence <!-- TODO: verify LinkedIn URL for Stan Black, D-Wave CISO -->

### People — Last Reviewed: 2026-04-14

## SPAC Merger History

D-Wave went public via a merger with **DPCM Capital, Inc.** (a blank-check SPAC) announced February 8, 2022, and completed August 5, 2022. The transaction valued the combined company at approximately $1.6 billion. Gross proceeds were approximately $340 million, including a $40M PIPE from Goldman Sachs Asset Management, PSP Investments, NEC Corporation, Yorkville Advisors, and Aegis Group Partners.

D-Wave had been a private company for over 20 years before the SPAC listing, making it by far the oldest quantum computing company to reach public markets. The stock now trades as NYSE: QBTS.

## Sources

- [D-Wave Corporate Site](https://www.dwavequantum.com) — company product and leadership information
- [D-Wave SEC EDGAR filings (CIK 1907982)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001907982&type=10-K) — authoritative financial data
- [King et al. (2023), *Nature* 617:61–66](https://www.nature.com/articles/s41586-023-05867-2) — peer-reviewed quantum simulation result (DOI: 10.1038/s41586-023-05867-2)
- [King et al. (2025), *Science* 388:199–204](https://www.science.org/doi/10.1126/science.ado6285) — disputed quantum supremacy claim (arXiv: 2403.00910)
- [Sels et al. (2025), arXiv:2603.18825](https://arxiv.org/abs/2603.18825) — NYU tensor network rebuttal of 2025 Science paper
- [EPFL/Flatiron rebuttal, arXiv:2503.08247](https://arxiv.org/html/2503.08247) — GPU-based classical challenge to 2025 Science paper
- [Quantum Computing Report — Advantage2 GA](https://quantumcomputingreport.com/d-wave-launches-advantage2-quantum-system-with-4400-qubits-and-higher-coherence/) — independent trade coverage of hardware launch
- [HPCWire — March 2025 controversy coverage](https://www.hpcwire.com/2025/03/13/d-wave-reports-quantum-supremacy-stirs-immediate-challenge-and-rebuttal/) — contemporaneous controversy reporting
- [Physics World — skeptical coverage](https://physicsworld.com/a/d-wave-systems-claims-quantum-advantage-but-some-physicists-are-not-convinced/) — independent physicist commentary
- [D-Wave Q4 FY2025 press release](https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-fourth-quarter-and-year-end-2025-results/) — most recent available financial summary
- [Quantum Computing Report — QCI acquisition](https://quantumcomputingreport.com/d-wave-quantum-to-acquire-quantum-circuits-inc-to-accelerate-error-corrected-gate-model-roadmap/) — independent analysis of gate-model acquisition
- [D-Wave Advantage2 support documentation](https://support.dwavesys.com/hc/en-us/articles/32105885880087-D-Wave-s-Advantage2-Quantum-Computer-Now-Generally-Available) — technical specs
- [D-Wave topologies documentation](https://docs.dwavequantum.com/en/latest/quantum_research/topologies.html) — Zephyr and Pegasus topology details
