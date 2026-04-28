---
title: "Google Quantum AI"
date: 2026-04-19
lastmod: 2026-04-19
draft: false
description: "Google's superconducting quantum computing program; Sycamore 2019 supremacy claim (contested), Willow 2024 below-threshold error correction (partially verified), dual-modality expansion to neutral atoms (March 2026); targeting useful fault-tolerant quantum computer by 2029."
tags: ["quantum-computing", "superconducting", "nisq", "fault-tolerant-research", "us", "incumbent"]
categories: ["company"]
research_area: "quantum-computing"
source_urls:
  - "https://quantumai.google/"
  - "https://quantumai.google/roadmap"
  - "https://www.nature.com/articles/s41586-019-1666-5"
  - "https://www.nature.com/articles/s41586-024-08449-y"
  - "https://blog.google/technology/research/google-willow-quantum-chip/"
  - "https://research.google/blog/a-verifiable-quantum-advantage/"
  - "https://arxiv.org/abs/2511.09124"
  - "https://arxiv.org/abs/2410.00917"
  - "https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf"
  - "https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/"
last_reviewed: 2026-04-19
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Google Quantum AI is Google's internal quantum computing research and hardware program, founded in 2012 by Hartmut Neven at NASA Ames Research Center in partnership with NASA and the Universities Space Research Association (USRA). The program manufactures superconducting transmon qubits in-house and has produced four generations of processors: Foxtail (2017, 22 qubits), Bristlecone (2018, 72 qubits), Sycamore (2019, 53 qubits), and Willow (2024, 105 qubits). Google has made two high-profile claims of quantum advantage: the 2019 "quantum supremacy" demonstration on Sycamore and the 2024 "below-threshold" error correction and RCS benchmark on Willow. Both claims are contested. In March 2026 Google expanded its hardware program to include neutral atom qubits as a second modality.

## Key Facts

- **Parent Company:** Alphabet / Google (NASDAQ: GOOGL)
- **Business Unit:** Google Quantum AI (part of Google Research)
- **Founded:** 2012 (Quantum AI Lab at NASA Ames; manufacturing moved in-house 2014)
- **VP of Engineering / Founder:** Hartmut Neven
- **HQ:** Santa Barbara, CA, USA (hardware fabrication and research); also Boulder, CO (neutral atom program, 2026)
- **Qubit Modality (primary):** Superconducting (transmon qubits)
- **Qubit Modality (new):** Neutral atom (program launched March 2026; no operational system yet)
- **Current Generation Hardware:** Willow (105 qubits, 2024)
- **Status:** Active; NISQ-era systems deployed; fault-tolerant research in progress
- **Public Cloud Access:** Google Cloud Quantum Computing Service (early access program); hardware also accessible via partnership arrangements (no broad public free tier as of April 2026)
- **Stated Goal:** "Useful, error-corrected quantum computer" by 2029 (Sundar Pichai, Google I/O 2021; reaffirmed)

## Processor Lineage

| Processor | Year | Physical Qubits | Key Specs | Notable For |
|-----------|------|-----------------|-----------|-------------|
| Foxtail | 2017 | 22 | Xmon qubit design; 2.5D fabrication; passive capacitive coupling | First generation; proof-of-concept |
| Bristlecone | 2018 | 72 | Passive capacitive coupling; improved coherence over Foxtail | First large-scale prototype; Julian Kelly lead designer |
| Sycamore | 2019 | 53 (54 fabricated; 1 inoperable) | T1 ~20 µs; active adjustable couplers; 1Q gate fidelity ~99.6%, 2Q gate fidelity ~99.4%, readout ~99.4% | "Quantum supremacy" claim (contested) |
| Willow | 2024 | 105 | T1 ~100 µs (~5× improvement over Sycamore); 1Q gate fidelity 99.97%, 2Q gate fidelity 99.88% (entangling), readout 99.5%; square grid, avg. connectivity 3.47; distance-7 logical qubit T1 291±6 µs | Below-threshold error correction claim (partially verified); new RCS benchmark |

**Source note on Willow specs:** Single-qubit fidelity (99.97%), two-qubit entangling gate fidelity (99.88%), and readout fidelity (99.5%) are from Google's company spec sheet (December 9, 2024) and the Nature paper (Acharya et al., 2024). T1 ~100 µs and logical qubit coherence (291 µs) are from the same publication. These figures are company-reported and peer-reviewed but not yet independently replicated on third-party hardware.

## What It Is / How It Works

Google Quantum AI uses superconducting transmon qubits fabricated in-house. Transmon qubits are anharmonic LC oscillators formed using Josephson junctions. Two-qubit gates are implemented by activating tunable couplers between adjacent qubits — an architectural improvement over the passive capacitive coupling used in Bristlecone and earlier chips, which reduced unwanted cross-talk and improved gate fidelity. Gate operations occur in nanoseconds; circuit depth is thus limited by coherence times (T1/T2), which reached ~100 µs average in Willow compared to ~20 µs in Sycamore.

**Quantum error correction approach:** Google uses the surface code — a 2D lattice-based error correction scheme where logical information is encoded redundantly across many physical qubits. Data qubits carry the logical information; ancilla (measurement) qubits are periodically measured to detect errors without collapsing the logical state. At Willow's scale, Google tests code distances (the side length of the logical qubit patch) of 3, 5, and 7, using (2d²−1) physical qubits per distance-d code (e.g., distance-7 uses 97 qubits).

The "below threshold" result means that as Google increases code distance, the logical error rate decreases rather than increases — meaning the error correction overhead is actually improving qubit quality. This is a necessary (but not sufficient) precondition for fault-tolerant quantum computing. It does not mean fault tolerance has been demonstrated; it demonstrates that the engineering approach can in principle scale toward it.

## Notable Developments

- **2026-04:** Google publishes paper "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities" (arXiv:2603.28846), co-authored with UC Berkeley, Stanford, and the Ethereum Foundation — among the first Google Quantum AI work with named financial security implications.
- **2026-03:** Google Quantum AI announces expansion into neutral atom quantum computing, hiring Dr. Adam Kaufman (atomic/molecular/optical physics) to lead a new program from Boulder, CO. Strategy frames superconducting (circuit depth) and neutral atoms (qubit count scalability up to ~10,000 qubits, any-to-any connectivity, millisecond gate cycles) as complementary. No operational neutral atom system announced.
- **2025-11:** Ryan Babbush and colleagues publish "The Grand Challenge of Quantum Applications" (arXiv:2511.09124), a perspective outlining a five-stage framework from theoretical quantum advantage discovery to production deployment; acknowledges that two critical middle stages — identifying hard concrete problem instances and connecting them to real-world use cases — remain under-resourced.
- **2025-10:** Google publishes "Quantum Echoes" result in *Nature* (vol. 646, pp. 825–830): the OTOC(2) (second-order out-of-time-order correlator) experiment on 65-qubit Willow achieves a claimed 13,000× speedup over Frontier supercomputer for this task. Peer-reviewed; claims "verifiable quantum advantage." Independent critics dispute the "real-world problem" framing (see Claim Verification below).
- **2025-02:** Sundar Pichai (Bloomberg interview) characterizes practical quantum computing as "5 to 10 years away" — a softer framing than the 2021 "by 2029" target.
- **2024-12:** Willow chip unveiled. 105 qubits. *Nature* paper (Acharya et al.) demonstrates below-threshold error correction for the first time. Simultaneous RCS benchmark claims 10²⁵-year classical simulation time. Google spec sheet released publicly.
- **2023:** First experimental demonstration of scalable quantum error correction at Google — below-threshold NOT yet demonstrated (that came with Willow); 2023 result showed error suppression on a single logical qubit, counting as Milestone 2 on Google's roadmap.
- **2021:** Sundar Pichai announces at Google I/O that Google will build a "useful, error-corrected quantum computer" by 2029.
- **2019-10:** Sycamore quantum supremacy paper published in *Nature* (Arute et al., vol. 574). Google claims Sycamore completed a random circuit sampling task in 200 seconds that would take a classical supercomputer 10,000 years. IBM challenges the claim within days.

## Key People

### Hartmut Neven — VP of Engineering, Founder of Google Quantum AI

- **LinkedIn:** https://www.linkedin.com/in/hartmut-neven-b4097a7 (verify — may need update)
- **Google Scholar:** https://research.google/people/hartmutneven/
- **Current Role:** Vice President of Engineering at Google; leads Google Quantum AI (founded the lab 2012)
- **Background:** PhD 1996, focus on autonomous mobile robots. Co-founded Eyematic (face recognition, CTO) and Neven Vision (CEO; acquired by Google 2006, enabling initial hire). Coinventor of "Neven's Law" (doubly exponential improvement rate claim for quantum hardware, not widely accepted as empirically validated).
- **Recognition:** Named to TIME's 100 Most Influential People in AI (2025).
- **Overlap:** No documented overlaps with other Research section companies as of April 2026.

### Julian Kelly — Senior Director, Hardware

- **LinkedIn:** https://www.linkedin.com/in/julianskelly/
- **Google Scholar:** https://scholar.google.com/citations?user=oEiC6dgAAAAJ&hl=en
- **Current Role:** Senior Director of Quantum Hardware at Google Quantum AI
- **Background:** PhD, University of California, Santa Barbara (superconducting qubits research). Joined Google Quantum AI following collaboration between Google and John Martinis's UCSB group (2014). Lead designer of Bristlecone (72-qubit, 2018). Developed "optimus," the automated calibration framework underpinning Google's quantum processor operations. Led hardware team for 2019 quantum supremacy and 2022/2023 error correction demonstrations. 
- **Overlap:** UCSB group origin — shared background with researchers at other superconducting qubit groups that spun out or collaborated with Google. No documented crossover with other specific Research section companies as of April 2026.

### Ryan Babbush — Director, Quantum Algorithms and Applications

- **LinkedIn:** https://www.linkedin.com/in/ryanbabbush/
- **Google Scholar:** https://scholar.google.com/citations?user=6I7jyygAAAAJ&hl=en
- **Current Role:** Director of Research, Quantum Algorithms and Applications, Google Quantum AI
- **Background:** PhD in Chemical Physics, Harvard University (2015). Began collaborating with Google Quantum AI while completing his doctorate; joined full-time 2015. Best known for developing quantum chemistry simulation algorithms (quantum phase estimation approaches to molecular simulation, applications in drug design and materials science). Lead author on "The Grand Challenge of Quantum Applications" (2025).
- **Overlap:** No documented overlaps with other Research section companies as of April 2026.

### Adam Kaufman — Director, Neutral Atom Program (new, 2026)

- **LinkedIn:** Not found as of April 2026; search TODO.
- **Current Role:** Director of neutral atom quantum computing program, Google Quantum AI, Boulder, CO. Announced March 2026.
- **Background:** Researcher in atomic, molecular and optical physics. Recruited externally by Neven in 2026 to lead Google's neutral atom expansion.
- **Prior Affiliation:** Not fully documented in public sources as of April 2026 — likely academic (TODO: verify institutional background).

### People — Last Reviewed: 2026-04-19

## Roadmap

Google's roadmap is published at quantumai.google/roadmap. The company uses named milestones rather than published annual hardware targets.

| Milestone | Description | Status (April 2026) | Date Claimed / Achieved |
|-----------|-------------|---------------------|------------------------|
| Milestone 1 | Beyond-classical quantum computation (quantum supremacy) | Claimed achieved (2019, Sycamore, RCS) | October 2019 — contested (see Claim Verification) |
| Milestone 2 | Logical qubit prototype: error correction demonstrated (errors suppress as code scales) | Claimed achieved | 2023 (first demonstration); Willow 2024 (below threshold) |
| Milestone 3 (implied) | Below-threshold quantum error correction | Claimed achieved | December 2024 (Willow) — "tickling the tail of fault-tolerance" (Aaronson) |
| Future milestone | Large-scale fault-tolerant quantum computer | Not achieved | Target: "by 2029" (Pichai, Google I/O 2021); reframed as "5–10 years" by Pichai in Feb 2025 |

**Timeline credibility notes:**

- The 2029 target was announced in 2021 and has not been formally retracted, but Sundar Pichai's February 2025 restatement as "5 to 10 years away" effectively softens the prior commitment without canceling it. This creates ambiguity: the 2029 target is still cited by Google materials but the CEO is publicly hedging on it.
- Google estimates ~1 million physical qubits may be required for a genuinely useful fault-tolerant machine. Willow has 105 physical qubits. The gap between current hardware and the 2029 target is approximately 4 orders of magnitude in qubit count, plus the requirement for below-threshold gate operations (not yet demonstrated — Willow shows below-threshold *memory*, not below-threshold *gates*).
- Unlike IBM (which publishes named future processor generations with qubit counts and target dates), Google has not published a public hardware roadmap naming future chips or qubit counts beyond current Willow generation. This makes year-by-year milestone tracking impossible from public sources.

**Historical timeline for the 2029 goal:**

| Claim | Date Made | Target |
|-------|-----------|--------|
| "Build useful, error-corrected quantum computer by 2029" | Google I/O 2021 | 2029 |
| "Practical quantum computing 5 to 10 years away" | Sundar Pichai, Bloomberg, Feb 2025 | 2030–2035 |
| "By decade's end" (neutral atom roadmap) | Hartmut Neven, March 2026 blog post | ~2029–2030 |

## Practical Applications

As of April 2026, no Google Quantum AI demonstration has been independently verified as outperforming classical computers on a real-world problem with direct economic or scientific utility. The following is a factual accounting of what has and has not been demonstrated:

**Demonstrated (physics experiments, not production applications):**

- Random circuit sampling (RCS): Sycamore (2019) and Willow (2024) benchmarks. Synthetic benchmark with no known real-world application. Classical simulation feasibility is actively debated (see Claim Verification).
- Quantum echoes / OTOC(2) (2025): Second-order out-of-time-order correlator measurement using 65-qubit Willow. Claimed 13,000× speedup over Frontier. A proof-of-principle NMR molecular ruler application was demonstrated with 15 qubits, but the initial NMR spectroscopy application does not yet exceed classical performance. Peer-reviewed in *Nature*.
- Wormhole dynamics simulation (2022, Sycamore): Simulated toy model of wormhole behavior; demonstration was of a highly compressed model, not a physical simulation of significance.
- Time crystal (2021, Sycamore, 20 qubits): First observation of a discrete time crystal phase — a genuine physics result but not a computation-over-classical-hardware advantage.
- Chemical simulation (2020, Sycamore, 12 qubits): Hartree-Fock approximation calculation — the smallest scale of chemistry simulation; classical computers handle this easily.

**Not yet demonstrated:**
- Quantum chemistry simulation outperforming classical hardware on a practically relevant molecule
- Materials discovery or drug design calculation with verified quantum advantage
- Optimization problem with verified quantum advantage over best classical solvers
- Any commercial customer deploying Google quantum hardware to solve a real production workload faster than classical compute

## Claim Verification

---

### Claim: Google demonstrated "quantum supremacy" in 2019 (Sycamore, Nature)

**Status:** Disputed

**Supporting sources:**
- [Arute et al., *Nature* 574, 505–510 (2019)](https://www.nature.com/articles/s41586-019-1666-5) — Original peer-reviewed paper. Sycamore (53 active qubits) completed a random circuit sampling task in 200 seconds; Google estimated 10,000 years for Summit supercomputer under assumptions stated in the paper. Peer-reviewed.

**Refuting / questioning sources:**
- [IBM Quantum Blog, "On Quantum Supremacy" (October 2019)](https://www.ibm.com/quantum/blog/on-quantum-supremacy) — IBM argued the same task could be performed on a classical system in 2.5 days using secondary storage, challenging the 10,000-year estimate at the time of the announcement.
- [Frontier supercomputer, 2024 retrospective](https://en.wikipedia.org/wiki/Quantum_supremacy) — Google's own team acknowledged that, given improvements in classical tensor network algorithms and Frontier's exascale capacity, simulating the 53-qubit Sycamore circuit would now take approximately 6 seconds on Frontier (compared to the original 200-second quantum runtime). This means the 2019 RCS demonstration has been effectively matched and exceeded classically, approximately 4–5 years after the claim.
- Gil Kalai (Hebrew University) maintains a long-standing critique that Google's claimed advantage figures are systematically overstated by approximately 10 orders of magnitude, and that the relevant benchmarks are not rigorous evidence of quantum advantage even at the time of the claim. See his blog for extended technical arguments.

**Independent replication:** The RCS computation itself has not been independently run by a third-party quantum computer at comparable scale. Classical simulation has exceeded it.

**Classical simulation feasibility:** Yes, as of 2024, classical hardware can simulate the original 2019 Sycamore RCS task in approximately 6 seconds on Frontier.

**Peer review status:** The original 2019 paper is peer-reviewed in *Nature*. IBM's rebuttal was published as a blog post (not peer-reviewed). Subsequent classical simulation work is primarily published in preprints and academic papers.

**Summary:** The 2019 supremacy claim was the first of its kind and was genuine within its stated conditions at the time. However, improved classical algorithms have since matched or surpassed it, demonstrating that "quantum supremacy" based on RCS is a moving target, not a permanent condition. The computation had no real-world utility; it was designed to be hard to simulate classically, not useful. **Status: Disputed** — was arguably valid at the time of publication; no longer holds as of 2024 due to classical simulation advances.

---

### Claim: Willow (2024) achieved "below threshold" quantum error correction (Nature)

**Status:** Partially Verified

**Supporting sources:**
- [Acharya et al., *Nature* (December 9, 2024)](https://www.nature.com/articles/s41586-024-08449-y) — Full peer-reviewed paper. Key result: increasing code distance from 3 to 5 to 7 reduces the logical error rate exponentially; error suppression factor 2.14 ± 0.02 per unit increase in code distance. Distance-7 logical qubit achieves 0.143% ± 0.003 error per cycle. Logical qubit coherence time 291±6 µs vs. best physical qubit 119 µs — logical outperforms physical.
- [Scott Aaronson blog, "The Google Willow thing" (December 2024)](https://scottaaronson.blog/?p=8525) — Independent expert endorses the below-threshold result as a genuine and significant milestone; characterizes it as "tickling the tail of the dragon of quantum fault-tolerance."
- [AAAS *Science* news coverage (December 2024)](https://www.science.org/content/article/google-passes-milestone-road-error-free-quantum-computer) — Describes result as "truly remarkable."

**Refuting / questioning sources:**
- Sabine Hossenfelder (physicist, public critic): The result is scientifically impressive but has zero near-term practical impact; ~1 million qubits are needed for practically useful applications; the current 105-qubit demonstration is far from that threshold.
- Multiple experts quoted in CNBC and industry press: The 0.143% logical error rate per cycle remains orders of magnitude above the ~10⁻⁶ target believed necessary for running meaningful large-scale quantum algorithms. Below threshold in memory ≠ below threshold in gates.
- Scott Aaronson (despite endorsing the result): Google demonstrated a *single* encoded logical qubit; no gate operations were performed on it. A fault-tolerant computer requires many logical qubits on which gates can be applied, not just a single preserved memory element.

**What "below threshold" technically means vs. press coverage:**
- **Technical meaning:** Physical error rates in Willow's surface code implementation are below the fault-tolerance threshold for *quantum memory* — meaning logical qubit lifetime improves as the code is made larger. This is the first experimental demonstration of this property at Google and is a necessary precondition for fault-tolerant computing.
- **What it is NOT:** Below-threshold gate operations (applying logical gates with error rates that also suppress as the code scales) have not been demonstrated. Universal fault-tolerant quantum computation requires below-threshold gate performance, not just memory. Willow's 0.143% logical error rate per cycle is approximately 1,000× above where Google aims to be.
- **Press coverage gap:** Many press reports described the result as Google having achieved "fault-tolerant quantum computing" or being near practical usefulness. This is inaccurate. The result is a necessary first step on a long path, not proof of useful quantum computation.

**Independent replication:** Not yet independently replicated on third-party hardware as of April 2026. Result is peer-reviewed and the theoretical framework is sound.

**Peer review status:** Published in *Nature* (Acharya et al., 2024). Full peer review completed.

**Summary:** The below-threshold error correction result is peer-reviewed, genuine, and a meaningful milestone in quantum hardware engineering. It does not demonstrate fault-tolerant computation, universal logical gate operations, or practical utility. The gap between Willow's current performance and a genuinely fault-tolerant system is large (approximately ~10,000:1 in physical qubits and ~1,000× in logical gate error rates). **Status: Partially Verified** — the specific error-suppression-below-threshold claim in quantum memory is verified; broader claims about proximity to fault-tolerant computing are not.

---

### Claim: Willow's 2024 RCS benchmark requires 10²⁵ years of classical simulation

**Status:** Unverified / Partially Disputed

**Supporting sources:**
- [Google Willow announcement blog (December 2024)](https://blog.google/technology/research/google-willow-quantum-chip/) — Company statement; the 10²⁵-year figure is for the specific Willow RCS circuit, not the 2019 Sycamore circuit.
- [Scott Aaronson blog](https://scottaaronson.blog/?p=8525) — Accepts the 10²⁵-year figure as correct for the stated circuit complexity; notes that classical algorithms could in principle improve over time.

**Refuting / questioning sources:**
- Scott Aaronson (accepting the numbers but noting the problem): The RCS benchmark is specifically designed to be hard to simulate classically. It is "quantum verifiable" only in the sense that results can be cross-checked against smaller circuits extrapolated up — it cannot be directly verified because verification would take as long as simulation (10²⁵ years). The benchmark is not a useful task.
- Gil Kalai: Claims the advantage is overstated by ~10 orders of magnitude; technical argument relates to extrapolation methodology and noise models.
- Hossenfelder and CNBC-quoted experts: The benchmark has no practical application; even if the 10²⁵-year figure is correct, it is not evidence of quantum utility.
- Historical pattern: The analogous 10,000-year figure for Sycamore (2019) was reduced to ~6 seconds on Frontier (~5 years later). The 10²⁵-year figure for Willow uses a more complex circuit that would be harder to classically simulate, but the same pattern of improving classical algorithms and hardware could erode the advantage over time.

**Classical simulation feasibility:** Not currently feasible for the specific Willow RCS circuit. Unlike 2019 Sycamore (which has since been classically matched), no classical simulation matching the Willow RCS benchmark has been published as of April 2026. The problem may remain classically hard for many years due to the larger circuit complexity.

**Summary:** The 10²⁵-year figure is accepted by leading independent experts as plausible given the circuit complexity, but the benchmark is a synthetic task with no known real-world utility. Direct classical verification is impossible. Historical precedent from 2019 suggests the figure may be reduced by future classical algorithm improvements, though the Willow circuit is substantially harder than Sycamore. **Status: Unverified** (the scale claim is plausible but cannot be independently confirmed; benchmark is not a practical problem).

---

### Claim: Quantum Echoes / OTOC(2) (2025) demonstrates "verifiable quantum advantage" on a real-world problem

**Status:** Partially Verified — peer-reviewed physics result; real-world application not yet demonstrated at quantum advantage

**Supporting sources:**
- [Google Research blog, "A verifiable quantum advantage"](https://research.google/blog/a-verifiable-quantum-advantage/) — Google's claim framing
- Published in *Nature* (vol. 646, pp. 825–830, October 2025) — peer-reviewed
- 13,000× speedup over Frontier claimed for the OTOC(2) measurement at the tested circuit scale (65-qubit Willow)
- "Verifiable" in the sense that results can be checked against other quantum computers of comparable quality (cross-benchmarkable), unlike RCS

**Refuting / questioning sources:**
- [Dries Sels (NYU), Nature news coverage](https://www.nature.com/articles/d41586-025-03300-4) — Argues the burden of proof has not been met; proving the impossibility of a more efficient classical algorithm is inherently difficult; historical precedent shows classical algorithms improving to match earlier claims
- James Whitfield (Dartmouth): Technically impressive but "a stretch" to envision near-term economically viable applications
- The UC Berkeley NMR spectroscopy proof-of-principle used 15 qubits and the molecular results do not yet exceed classical performance — Google itself acknowledges the NMR application is pre-advantage at current scale
- Gil Kalai: Claims Google's advantage estimates are inflated by ~10 orders of magnitude
- The experiment required ~1 trillion measurements to extract OTOC signals from noise — the quantum advantage margin is narrow, and classical algorithms could potentially improve to close it

**Independent replication:** Not yet independently replicated on a third-party quantum computer as of April 2026 (though the result is described as "cross-benchmarkable" in principle).

**Peer review status:** Published in *Nature* (October 2025). Full peer review completed.

**Practical application status:** OTOC measurements are relevant to quantum chaos, information scrambling, and molecular structure analysis. The NMR molecular ruler application is a plausible near-term direction but is not yet at the quantum advantage scale. No commercially deployed or independently verified real-world application exists.

**Summary:** The OTOC(2) result is peer-reviewed and represents a more physically meaningful measurement than RCS, as its results are interpretable (not just random bitstrings). The claimed 13,000× speedup is specific to this physics experiment. The "verifiable" framing is more honest than the 2019 and 2024 benchmarks, but independent verification has not yet occurred, and the path from this result to practical applications requires several additional steps. **Status: Partially Verified** — peer-reviewed physics result; "verifiable quantum advantage on a real-world problem" claim is overstated relative to demonstrated evidence.

---

## Sources

- [Quantum supremacy using a programmable superconducting processor, *Nature* 574 (Arute et al., 2019)](https://www.nature.com/articles/s41586-019-1666-5) — Original 2019 supremacy paper
- [IBM Quantum Blog: On "quantum supremacy" (October 2019)](https://www.ibm.com/quantum/blog/on-quantum-supremacy) — IBM's rebuttal to 2019 claim
- [Quantum error correction below the surface code threshold, *Nature* (Acharya et al., 2024)](https://www.nature.com/articles/s41586-024-08449-y) — Willow below-threshold paper
- [Meet Willow, our state-of-the-art quantum chip (Google Blog, December 2024)](https://blog.google/technology/research/google-willow-quantum-chip/) — Company announcement
- [Willow Spec Sheet (Google Quantum AI, December 2024)](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf) — Technical specs
- [The Google Willow thing (Scott Aaronson, December 2024)](https://scottaaronson.blog/?p=8525) — Independent expert assessment
- [Google claims quantum computing milestone — but the tech can't solve real-world problems yet (CNBC, December 2024)](https://www.cnbc.com/2024/12/10/google-claims-quantum-milestone-but-cant-solve-real-world-problems-.html) — Critical coverage
- [A verifiable quantum advantage (Google Research Blog, October 2025)](https://research.google/blog/a-verifiable-quantum-advantage/) — Quantum Echoes announcement
- [Observation of constructive interference at the edge of quantum ergodicity, *Nature* 646, 825–830 (October 2025)](https://www.nature.com/articles/s41586-025-09101-x) — Quantum Echoes paper (OTOC(2))
- [Google claims 'quantum advantage' again — but researchers are sceptical (*Nature* news, 2025)](https://www.nature.com/articles/d41586-025-03300-4) — Expert skepticism on Quantum Echoes
- [The Grand Challenge of Quantum Applications, arXiv:2511.09124 (Babbush et al., November 2025)](https://arxiv.org/abs/2511.09124) — Google's five-stage framework; candid assessment of gaps
- [Google Quantum AI's Quest for Error-Corrected Quantum Computers, arXiv:2410.00917 (2024)](https://arxiv.org/abs/2410.00917) — Program overview
- [Google Paves a Two-Lane Quantum Roadmap by Adding Neutral Atom Systems (The Quantum Insider, March 2026)](https://thequantuminsider.com/2026/03/24/google-paves-a-two-lane-quantum-roadmap-by-adding-neutral-atom-systems/) — Neutral atom expansion
- [Google Quantum AI to include neutral atom computing (Google Blog, March 2026)](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) — Neven announcement
- [Google CEO Sees 'Useful' Quantum Computers 5 to 10 Years Away (Bloomberg, February 2025)](https://www.bloomberg.com/news/articles/2025-02-12/google-ceo-sees-useful-quantum-computers-5-to-10-years-away) — Pichai timeline
- [Hartmut Neven, Research at Google](https://research.google/people/hartmutneven/) — Leadership bio
- [Julian Kelly, Google Quantum AI](https://www.linkedin.com/in/julianskelly/) — Hardware director
- [Ryan Babbush, Research at Google](https://research.google/people/ryanbabbush/) — Algorithms director
