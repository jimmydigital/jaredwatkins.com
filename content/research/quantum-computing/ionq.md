---
title: "IonQ"
date: 2026-04-05
lastmod: 2026-04-07
draft: false
description: "Publicly traded trapped-ion quantum computing company; produces Forte and Tempo systems; uses ytterbium ions as qubits; cloud access via AWS, Azure, and Google Cloud."
tags: ["quantum-computing", "trapped-ion", "nisq", "us", "cloud-access"]
categories: ["company"]
research_area: "quantum-computing"
source_urls:
  - "https://ionq.com"
  - "https://investors.ionq.com"
  - "https://www.sec.gov/Archives/edgar/data/1824920/000095017025027722/ionq-20241231.htm"
  - "https://www.ionq.com/roadmap"
  - "https://www.ionq.com/algorithmic-qubits"
  - "https://www.quantinuum.com/blog/debunking-algorithmic-qubits"
  - "https://arxiv.org/abs/2511.05465"
  - "https://arxiv.org/abs/2602.23976"
  - "https://www.darpa.mil/research/programs/quantum-benchmarking-initiative"
last_reviewed: 2026-04-05
stale_after_days: 90
---

## Summary

IonQ (NASDAQ: IONQ) is a publicly traded trapped-ion quantum computing company founded in 2015 and headquartered in College Park, Maryland. It uses individual ytterbium ions suspended in electromagnetic traps as qubits, achieving all-to-all connectivity — every qubit can interact with every other — a physical advantage over superconducting architectures that use nearest-neighbor connectivity. IonQ's systems are commercially available on all three major cloud platforms (AWS Braket, Azure Quantum, Google Cloud Marketplace). The company is undergoing rapid strategic expansion: in early 2026 it acquired Skyloom Global (optical communications for quantum networking) and announced a pending $1.8B acquisition of SkyWater Technology (semiconductor foundry), aiming for vertical integration from qubit fabrication through cloud delivery.

## Key Facts

- **Founded:** 2015
- **Type:** Company (publicly traded — NASDAQ: IONQ)
- **Founders:** Jungsang Kim and Christopher Monroe (both Duke University professors, both since departed)
- **CEO (current):** Niccolò de Masi (appointed February 26, 2025)
- **HQ:** College Park, MD, USA
- **Qubit modality:** Trapped ion (ytterbium, ¹⁷¹Yb⁺)
- **Status:** Active; NISQ-era commercial systems; fault-tolerant computing on roadmap
- **Key systems:** IonQ Forte (#AQ 36, 32 physical qubits), IonQ Tempo (#AQ 64, ~100 physical qubits)
- **Key metric (proprietary):** #AQ (Algorithmic Qubits) — IonQ-defined, not an industry standard
- **FY2024 revenue:** $43.1M (SEC-filed; 95% YoY growth)
- **FY2025 guidance (raised Q3):** $106–110M
- **Net loss FY2024:** $331.6M; accumulated deficit through 2024: $683.7M
- **Cash position (Oct 2025):** ~$3.5B pro-forma (after $2B equity raise)
- **Cloud access:** AWS Braket, Azure Quantum, Google Cloud Marketplace

## What It Is / How It Works

Trapped-ion quantum computers use individual charged atoms held in place by electromagnetic fields. IonQ uses ytterbium-171 ions. Qubits are encoded in the hyperfine energy levels of these ions; laser pulses (or microwave pulses in newer designs) drive qubit operations. The key physical advantage of this modality is long coherence: ions are extremely isolated from their environment, yielding T1 times measured in seconds — orders of magnitude longer than superconducting qubits (microseconds). The second advantage is all-to-all connectivity: because ions in a trap can be made to interact with any other ion via shared phonon modes (collective vibrational states of the ion chain), there is no need for the routing overhead that superconducting architectures require when running circuits that need interactions between non-adjacent qubits.

IonQ's Forte system contains 32 physical qubits. Its Tempo system, announced in 2025 and achieving #AQ 64 three months ahead of the published schedule, targets ~100 physical qubits. The company uses its proprietary #AQ (Algorithmic Qubits) metric as its headline performance measure. This metric is defined by IonQ and is not an industry-standardized benchmark; see the Claim Verification section for critical context.

In October 2025 IonQ announced a laboratory result of 99.99% two-qubit gate fidelity using a new "smooth gate" technique developed from its acquisition of Oxford Ionics. This result was achieved on prototype hardware, not on commercially available systems. The Forte system available to customers achieves approximately 99.35–99.6% two-qubit gate fidelity depending on benchmarking methodology.

## Notable Developments

- **2026-04:** SkyWater Technology acquisition pending regulatory approval; boards of both companies have approved the $1.8B cash-and-stock deal. Expected close Q2–Q3 2026. SkyWater facilities in Minnesota, Florida, and Texas to become Regional Quantum Production Hubs.
- **2026-01:** Completed acquisition of Skyloom Global Corp. (optical communications terminals for quantum networking; formerly supplying Space Development Agency satellite-to-satellite laser links). Skyloom's 90 delivered optical terminals cited as basis for future distributed quantum entanglement infrastructure.
- **2026-01:** Announced intent to demonstrate 256-qubit systems in 2026, using Electronic Qubit Control (EQC) technology derived from Oxford Ionics acquisition.
- **2025-11:** Advanced to Stage B of DARPA's Quantum Benchmarking Initiative (QBI) — one of 11 companies selected. Stage B involves developing a detailed R&D roadmap through 2033 with technical requirements. Stage B is a government evaluation process, not a validation of current quantum advantage.
- **2025-11:** Quantinuum launched Helios (98 physical qubits; 99.921% two-qubit gate fidelity; 48 fully error-corrected logical qubits at 2:1 encoding ratio). Helios represents the current leading trapped-ion commercial system on raw gate fidelity. (See Claim Verification.)
- **2025-10:** IonQ announced 99.99% two-qubit gate fidelity achieved in laboratory using EQC technology (prototype, not commercial system). Prior world record was 99.97% (Oxford Ionics, 2024, since acquired by IonQ).
- **2025-10:** Closed $2B equity offering; cash and investments reached ~$3.5B pro-forma. IonQ now well-capitalized for SkyWater acquisition.
- **2025-09:** IonQ Tempo achieved #AQ 64 — three months ahead of published schedule. IonQ claims Tempo as the first commercially available system to reach this milestone.
- **2025-08:** CEO Niccolò de Masi assumed Chairman of the Board role. Peter Chapman fully exited — departed as Executive Chairman and board member effective August 1, 2025.
- **2025-06:** AstraZeneca/AWS/NVIDIA/IonQ joint announcement of hybrid quantum-GPU workflow for Suzuki-Miyaura reaction modeling, claiming 20x end-to-end acceleration. (See Claim Verification.)
- **2025-03:** Ansys/IonQ joint announcement of 12% speedup over classical computing in blood pump fluid dynamics simulation using IonQ Forte.
- **2025-02:** Niccolò de Masi appointed President and CEO. Peter Chapman moved to Executive Chair role. De Masi had served on IonQ board since 2021 (previously CEO of dMY Technology Group III, the SPAC that took IonQ public).
- **2025-02:** FY2024 10-K filed: $43.1M revenue, $331.6M net loss, $95.6M bookings. (See financial scrutiny notes.)
- **2024-09:** IonQ announced $54.5M Air Force Research Laboratory (AFRL) contract, described as "the largest 2024 U.S. quantum contract award." (See Claim Verification — disputed.)
- **2024-03:** Jungsang Kim stepped down as CTO. Retained as scientific advisor. Returned to Duke University; appointed Chief Science and Technology Strategist for Duke Provost in February 2025.
- **2023-10:** Chris Monroe (co-founder, former Chief Scientist) departed to return to academic, research, and policy pursuits. Continues as Duke professor.

## Key People

### Niccolò de Masi — President & CEO

- **LinkedIn:** <!-- TODO: search for actual profile slug; not found in public sources -->
- **Google Scholar:** Not applicable (non-technical background)
- **Appointed CEO:** February 26, 2025
- **Assumed Chairman:** August 1, 2025
- **Previous roles:** CEO, dMY Technology Group III (SPAC vehicle that took IonQ public, 2021); CEO, Glu Mobile; CEO, Resideo Technologies; CEO, Monstermob Group. Physics degree, Cambridge University.
- **Overlap flag:** De Masi's role as CEO of the dMY SPAC that brought IonQ public creates a structural connection: he was instrumental in IonQ's public market entry before becoming its CEO. This relationship is publicly disclosed.

### Peter Chapman — Former President & CEO (May 2019 – February 2025)

- **LinkedIn:** https://www.linkedin.com/in/peter-h-chapman (verify — sourced from public profile searches)
- **Left company:** August 1, 2025 (stepped down as Executive Chairman and board member)
- **Previous roles:** Engineering director, Amazon (Prime Air); earlier career in tech industry.
- **Departure context:** Transition to de Masi was announced February 2025; Chapman's full exit with accelerated vesting and one year of base salary + target bonus severance occurred August 2025. The rapid 6-month CEO-to-full-exit trajectory warrants monitoring for any disclosed strategic disagreements in future filings, though no public disagreements have been cited.

### Jungsang Kim — Co-Founder, Former CTO (2015 – March 2024)

- **LinkedIn:** https://www.linkedin.com/in/jungsang-kim-10b5b811 (verify)
- **Google Scholar:** https://scholar.google.com/citations?user=jungsangkim (verify actual slug)
- **Current role:** Chief Science and Technology Strategist for Duke University Provost (appointed February 2025); professor, Duke Electrical and Computer Engineering
- **Role at IonQ:** Co-founder; served as CTO until March 2024; retained as scientific advisor post-departure
- **Background:** PhD in Physics, University of Michigan; research focus on trapped-ion quantum information and photonic interconnects; co-founded IonQ with Monroe from their Duke lab.
- **⚑ Overlap:** Kim and Monroe co-founded IonQ from the same Duke University research group (Monroe Lab). Both departed within approximately 5 months of each other (October 2023 / March 2024).

### Christopher Monroe — Co-Founder, Former Chief Scientist (2015 – October 2023)

- **LinkedIn:** <!-- TODO: not found with certainty; do not fabricate -->
- **Google Scholar:** https://scholar.google.com/citations?user=chrismonroe (verify)
- **Current role:** Professor, Duke University (Gilhuly Family Distinguished Presidential Professor of Physics and Electrical Computer Engineering); advising quantum institutes
- **Background:** Pioneered trapped-ion quantum computing; co-inventor of the first demonstrated quantum logic gate (1995, NIST). PhD in Physics, University of Colorado. Worked at NIST before Duke.
- **⚑ Overlap:** Monroe and Kim co-founded IonQ together and both returned to Duke. Their shared departure concentrated original scientific leadership risk — IonQ's current technical direction is now under de Masi without either founder in an operational role.

### People — Last Reviewed: 2026-04-05

## Roadmap

IonQ publishes a public roadmap at ionq.com/roadmap. Summary of key published milestones:

| Milestone | Target Year | Status (as of April 2026) | Published |
|-----------|-------------|--------------------------|-----------|
| #AQ 64 (Tempo system) | 2025 | ✓ Met — 3 months early (Sept 2025) | 2024 |
| 99.99% two-qubit gate fidelity (lab) | 2025 | ✓ Met — October 2025 (prototype only) | 2024 |
| 256-qubit systems demonstration | 2026 | In progress — EQC technology base | 2025 |
| 12 logical qubits, <1e-7 logical error | 2026 | Target; no announced result | 2025 |
| "Break-even" (logical qubit error < single physical qubit) | 2027 | Target | 2025 |
| ~20,000 physical qubits, ~1,600 logical qubits | 2028 | Target; timeline accelerated via SkyWater acquisition (pulled forward from 2030) | 2025–2026 |
| 2 million physical qubits, 80,000 logical qubits | 2030 | Long-range target; no mechanism independently verified | 2024 |

**Critical context:** The 2028 acceleration of the ~20,000 qubit milestone depends on the SkyWater acquisition closing and then executing a foundry-scale manufacturing ramp. This is not a demonstrated capability — it is a dependency chain. The 2030 2-million-qubit figure is not accompanied by a peer-reviewed engineering analysis of how it would be achieved; it should be treated as an investor-facing aspiration, not a near-term roadmap item.

**Roadmap history note:** IonQ has not publicly revised any published milestones downward as of April 2026. The #AQ 64 milestone was achieved ahead of schedule. However, the roadmap scope has expanded substantially (with SkyWater) in ways that suggest the original timeline was not accounting for foundry capacity constraints. Whether the acceleration claim holds depends on regulatory approval, integration execution, and SkyWater's ability to deliver quantum-specific fabrication at scale.

## Revenue and Commercial Traction

**Verified from SEC filings (10-K):**

| Period | Revenue | Net Loss |
|--------|---------|----------|
| FY2023 | $22.0M | $157.8M |
| FY2024 | $43.1M | $331.6M |
| Q3 2025 | $39.9M (quarter) | $1.1B (quarter, includes non-cash charges) |
| FY2025 (guidance) | $106–110M | — |

Revenue growth is genuine and SEC-filed. The 95% YoY growth from 2023 to 2024 and 222% Q3 2025 YoY growth are documented.

**Bookings controversy:** IonQ reported $95.6M in 2024 bookings against $43.1M in revenue. Bookings is a company-defined metric. In February 2026, short-seller Wolfpack Research alleged that IonQ's bookings figures include non-binding contract ceiling values — specifically that a $54.5M AFRL contract announced in September 2024 as "the largest 2024 U.S. quantum contract award" was only approximately $12M actually funded, with the remainder representing possible future value that Congress had not appropriated. Wolfpack further alleged that when political patrons lost influence after the 2024 U.S. election, these Pentagon earmarks went unfunded in FY2025 and FY2026 budgets, representing a $54.6M "black hole" in bookings — and that IonQ did not disclose this to investors. IonQ disputed the Wolfpack claims. The dispute is not resolved as of April 2026. **Investors and researchers should treat IonQ's bookings metric with caution until the company provides clearer disclosure about funded vs. unfunded contract components.**

**Cloud and commercial partnerships:** AWS Braket, Azure Quantum, Google Cloud Marketplace. Amazon holds a $36.7M equity stake in IonQ (disclosed August 2025).

## IonQ vs. Quantinuum: Head-to-Head

Both IonQ and Quantinuum use trapped-ion technology. As of April 2026, the comparison on commercially available systems:

| Metric | IonQ Forte | Quantinuum Helios | Notes |
|--------|-----------|-------------------|-------|
| Physical qubits | 32 | 98 | Helios launched November 2025 |
| Two-qubit gate fidelity (commercial system) | 99.35–99.6% | 99.921% | Helios arXiv 2511.05465 |
| Single-qubit gate fidelity | ~99.5% | 99.9975% | |
| Logical qubits demonstrated | Not announced | 48 (error-corrected, 2:1 ratio) | Quantinuum Helios |
| #AQ score (IonQ metric) | #AQ 36 (Forte) | #AQ 26 (H2-1, without error mitigation) | #AQ is IonQ-defined; H2-1 is prior generation |
| Lab fidelity record | 99.99% (EQC prototype, Oct 2025) | Not publicly matched | Not yet in commercial system |
| Fault tolerance milestone | Not demonstrated | 48 logical qubits at 2:1 ratio (Nov 2025) | Quantinuum ahead on error correction |

**Summary:** On commercial hardware fidelity and demonstrated error correction, Quantinuum's Helios system leads IonQ's current Forte system. IonQ's advantage is in its laboratory result (99.99% EQC prototype) which, if successfully translated to production, would represent a significant step; it has not yet been replicated in a commercially available system. IonQ's Tempo system (#AQ 64) represents its most capable publicly available product, but Quantinuum's Helios was launched approximately the same time with substantially higher raw gate fidelity and demonstrated logical qubit encoding that IonQ has not yet matched.

## Quantum Networking

IonQ has made several acquisitions targeting quantum networking:

- **Lightsynq** (prior to 2025): quantum memory and photonic interconnect technology
- **Skyloom Global** (announced November 2025, completed January 2026): optical communications terminals (OCTs); Skyloom had delivered ~90 terminals for Space Development Agency satellite missions
- **ID Quantique** (super-majority stake, timing approximate): quantum key distribution and quantum random number generation

**Assessment of claims:** IonQ's quantum networking strategy is at the infrastructure acquisition and roadmap stage. As of April 2026, no multi-system quantum entanglement demonstration has been independently verified or peer-reviewed. The Skyloom acquisition adds free-space optical communications expertise, which is a prerequisite for long-distance quantum links, but the actual physical capability to entangle spatially separated trapped-ion processors over useful distances has not been demonstrated publicly. These are strategic positioning moves, not operational quantum networking capabilities.

## Claim Verification

### Claim: 99.99% Two-Qubit Gate Fidelity (World Record)

**Status:** Partially verified

**Supporting sources:**
- [IonQ press release, October 2025](https://www.ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing-performance) — company announcement
- [Oxford Ionics announcement](https://www.oxionics.com/announcements/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing-performance/) — confirms result (Oxford Ionics is now part of IonQ)
- [The Quantum Insider coverage](https://thequantuminsider.com/2025/10/21/ionq-achieves-99-99-two-qubit-gate-performance/) — trade press summary

**Refuting / questioning sources:**
- The result is from an R&D prototype using EQC technology, not from the Forte or Tempo commercial systems available to customers. No peer-reviewed publication of this result has been identified as of April 2026. The prior record holder (Oxford Ionics at 99.97%) is now part of IonQ, so the "world record" is essentially an internal improvement.
- [Quantinuum Helios arXiv paper (2511.05465)](https://arxiv.org/abs/2511.05465) documents 99.921% on a production 98-qubit system — lower than IonQ's prototype claim, but on a system that is commercially deployed and has demonstrated logical qubit encoding.

**Peer review status:** Not yet published in peer-reviewed journal as of April 2026. Preprint or journal link not identified.

**Independent replication:** None identified.

**Summary:** The 99.99% figure is plausible for the reported technique but has not been independently replicated or published in a peer-reviewed journal, and it applies to a prototype system rather than the Forte or Tempo systems available to customers. Mark as partially verified (company announcement, not independently replicated).

---

### Claim: #AQ 64 Achieved on Tempo (Ahead of Schedule)

**Status:** Partially verified (company-defined metric; methodology not independently standardized)

**Supporting sources:**
- [IonQ investor release, September 2025](https://investors.ionq.com/news/news-details/2025/IonQ-Achieves-Record-Breaking-Quantum-Performance-Milestone-of-AQ-64/) — formal announcement
- [Quantum Computing Report](https://quantumcomputingreport.com/ionq-reaches-aq-64-milestone-on-100-qubit-tempo-system-ahead-of-schedule/) — independent trade press confirmation

**Refuting / questioning sources:**
- [Quantinuum "Debunking algorithmic qubits" blog](https://www.quantinuum.com/blog/debunking-algorithmic-qubits) — Quantinuum argues #AQ is easier to pass than Quantum Volume because it allows error mitigation and result compilation techniques that can inflate scores; that without error mitigation, IonQ Forte scores #AQ 9 vs. Quantinuum H2-1's #AQ 26.
- #AQ is not accepted by IBM, Google, or Quantinuum as a standard benchmark. Each company uses metrics (Quantum Volume, CLOPS, raw gate fidelity) that align with their own architectural strengths.

**What #AQ measures and does not measure:** #AQ measures the largest problem size (in qubits) at which a system can run a defined set of benchmark circuits with acceptable output fidelity, when error mitigation techniques are permitted. It does not measure raw gate fidelity, coherence time, circuit depth, speed (circuit layer operations per second), or fault-tolerant capability. It is calibrated to application-oriented benchmarks but allows post-processing that can mask raw hardware noise.

**Peer review status:** No independent peer-reviewed study of the #AQ metric's validity or comparability across hardware platforms has been identified.

**Independent replication:** #AQ is defined and measured by IonQ. Competitors have not accepted it as a standard.

**Summary:** The #AQ 64 achievement on Tempo is a genuine milestone on IonQ's own benchmark. However, #AQ is a company-defined metric that competitors explicitly criticize as gameable through error mitigation allowances. Do not treat #AQ scores as equivalent to independently standardized benchmarks such as Quantum Volume.

---

### Claim: Ansys 12% Speedup in Medical Device Simulation

**Status:** Partially verified

**Supporting sources:**
- Joint IonQ/Ansys announcement (March 2025) — reputable independent partner; Ansys is a major independent commercial simulation company
- The claim involves a hybrid quantum-classical workflow, not a pure quantum computation

**Refuting / questioning sources:**
- 12% speedup is modest and may be within the error band of run-to-run classical variability. No peer-reviewed publication identified.
- Hybrid quantum-classical workflows are difficult to benchmark fairly against classical-only runs; the comparison depends heavily on classical implementation choices.

**Classical simulation feasibility:** Not established whether this specific workload is infeasible on classical hardware.

**Peer review status:** Not published in peer-reviewed journal as of April 2026.

**Summary:** Partially verified — joint announcement with an independent, credible company partner. The speedup claim is not yet published in peer-reviewed form, and the hybrid nature of the workflow means this is not evidence of quantum advantage in the strict sense.

---

### Claim: AstraZeneca 20x End-to-End Acceleration for Drug Discovery

**Status:** Partially verified (with important caveats)

**Supporting sources:**
- Joint announcement by AstraZeneca, AWS, NVIDIA, and IonQ (June 2025) — multiple independent organizations co-authored

**Refuting / questioning sources:**
- The "20x" figure is end-to-end (including GPU classical post-processing), not quantum alone. The quantum component provides acceleration on a specific subroutine (electronic structure calculation), while classical GPU resources do the remainder. The claim is not "quantum is 20x faster than classical" — it is "this hybrid quantum+GPU workflow is 20x faster than the prior classical-only workflow."
- No peer-reviewed publication confirmed as of April 2026.
- Classical simulation feasibility: the specific subroutine benefiting from quantum processing has not been shown to be classically infeasible at this scale.

**Summary:** Partially verified (multi-party announcement, credible partners) but the acceleration is in a hybrid quantum+GPU workflow and is not evidence of standalone quantum advantage. Publication in peer-reviewed form would be required for higher confidence.

---

### Claim: $54.5M AFRL Contract (Largest 2024 U.S. Quantum Award)

**Status:** Disputed

**Supporting sources:**
- IonQ press release, September 2024 — the contract announcement

**Refuting / questioning sources:**
- [Wolfpack Research short report, February 2026](https://www.wolfpackresearch.com/_files/ugd/b084d8_ac8adef1239042289d323784d4be02b0.pdf) — alleges only ~$12M actually funded; the remainder ($34.5M+) represents unfunded future ceiling values. Further alleges IonQ used lobbying and congressional earmarks to inflate contract ceiling values without appropriated funding, and that these earmarks were defunded after the 2024 election without disclosure to investors.
- [Fortune reporting on the dispute](https://fortune.com/2026/02/04/ionq-wolfpack-research-short-seller-says-quantum-computing-company-misled-investors-about-cancelled-government-backdoor-earmarks/) — covers allegations

**IonQ's response:** IonQ disputed Wolfpack's claims (see [Washington Morning reporting](https://washingtonmorning.com/2026/02/05/ionq-challenges-short-seller-claims-on-revenue-transparency-and-government-contracts/)).

**Peer review status:** Not applicable (contract dispute, not a technical claim).

**Roadmap history:** N/A.

**Summary:** Disputed. The funded value of the AFRL contract may be substantially lower than the announced total contract value. The dispute is unresolved as of April 2026 and has not been fully adjudicated. IonQ's bookings metric should be treated with caution.

---

### Quantum Advantage Claimed: No Published Verified Instance

**Status:** Unverified for strict quantum advantage

IonQ has not published a peer-reviewed claim that any of its systems have demonstrated quantum advantage — i.e., that a computation was performed that could not feasibly be performed on classical hardware in comparable time. The Ansys and AstraZeneca results are hybrid workflows with modest speedups, not demonstrations of strict quantum advantage. This is consistent with the broader NISQ-era landscape: no company has yet demonstrated verifiable, practically useful quantum advantage on real workloads.

**Independent replication status:** No IonQ quantum advantage claim has been independently replicated by a third party in a peer-reviewed context.

**Classical simulation feasibility:** All publicly described IonQ computations are, in principle, classically simulable at their current scale (circuit sizes at which #AQ 36–64 operate are not yet in the regime where classical simulation is infeasible).

## Key Organizations

- **Duke University** — origin lab of both co-founders; Monroe Lab pioneered trapped-ion QC. Both Monroe and Kim have returned as faculty.
- **Amazon Web Services** — cloud partner and equity holder ($36.7M stake as of August 2025 disclosure)
- **SkyWater Technology** (pending acquisition) — US semiconductor foundry; IonQ's proposed fabrication partner. See [entry]({{< relref "skywater-technology.md" >}}).
- **Oxford Ionics** (acquired) — UK quantum computing startup; source of 99.99% EQC gate technique
- **Skyloom Global** (acquired January 2026) — optical communications terminals for satellite and quantum networking links
- **Lightsynq Technologies** (acquired) — quantum memory and photonic interconnect startup
- **ID Quantique** (super-majority stake) — Swiss QKD and quantum random number generation company
- **DARPA** — IonQ is in Stage B of the Quantum Benchmarking Initiative (QBI); this is an evaluation program, not a contract for quantum computing services

## Sources

- [IonQ Corporate Site](https://ionq.com) — product specs, roadmap, announcements
- [IonQ Roadmap](https://www.ionq.com/roadmap) — published milestone table
- [IonQ 10-K FY2024 (SEC)](https://www.sec.gov/Archives/edgar/data/1824920/000095017025027722/ionq-20241231.htm) — audited revenue, loss, bookings
- [IonQ Investor Relations](https://investors.ionq.com) — press releases, earnings calls
- [IonQ Algorithmic Qubits definition](https://www.ionq.com/algorithmic-qubits) — IonQ's own #AQ documentation
- [Quantinuum: "Debunking Algorithmic Qubits"](https://www.quantinuum.com/blog/debunking-algorithmic-qubits) — competitor critique of #AQ metric
- [Quantinuum Helios arXiv paper](https://arxiv.org/abs/2511.05465) — 98-qubit system; 99.921% 2Q fidelity; 48 logical qubits
- [IonQ Forte Benchmarking arXiv](https://arxiv.org/abs/2308.05071) — 30-qubit benchmarking paper
- [arXiv 2602.23976](https://arxiv.org/abs/2602.23976) — "Large-scale portfolio optimization on a trapped-ion quantum computer," February 2026
- [DARPA QBI Program](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) — quantum benchmarking initiative page
- [IonQ SkyWater acquisition announcement](https://www.ionq.com/news/ionq-to-acquire-skywater-technology-creating-the-only-vertically-integrated-full-stack-quantum-platform-company) — January 2026
- [IonQ Skyloom acquisition](https://www.ionq.com/news/ionq-completes-acquisition-of-skyloom-expanding-quantum-networking-and-secure-communications-capabilities) — completed January 2026
- [Wolfpack Research short report, February 2026](https://www.wolfpackresearch.com/_files/ugd/b084d8_ac8adef1239042289d323784d4be02b0.pdf) — AFRL contract dispute
- [Fortune coverage of Wolfpack allegations](https://fortune.com/2026/02/04/ionq-wolfpack-research-short-seller-says-quantum-computing-company-misled-investors-about-cancelled-government-backdoor-earmarks/)
- [IonQ Q3 2025 earnings](https://www.ionq.com/news/ionq-announces-third-quarter-2025-financial-results) — $39.9M Q3 revenue; raised FY2025 guidance to $106–110M
- [Jungsang Kim Duke appointment](https://today.duke.edu/2025/02/jungsang-kim-named-chief-science-and-technology-strategist-provost) — February 2025
