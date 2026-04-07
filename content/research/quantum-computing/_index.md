---
title: Quantum Computing Research
date: 2026-04-05
lastmod: 2026-04-07
draft: false
description: Research on quantum computing hardware, software, and the companies and researchers building toward practical quantum advantage.
tags: ["quantum-computing"]
categories: ["overview"]
research_area: "quantum-computing"
last_reviewed: 2026-04-07
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

{{< steering >}}

## Quantum Computing Section — Steering Instructions

This section tracks companies and technologies in the quantum computing stack. Standard Research section rules apply. The following quantum-specific rules extend and override global defaults where noted.

---

### Editorial Priority

Unlike most research areas, the major incumbents (IBM, Google, Microsoft) are primary subjects here — their roadmaps and claimed milestones directly define the state of the field and cannot be treated as background context only. Smaller hardware companies (IonQ, Quantinuum, Rigetti, D-Wave, Xanadu, PsiQuantum) are first-tier entries. Software/cloud access layers and academic spinouts are second-tier. Pure quantum software companies without a hardware program are out of scope unless they have a distinctive technical approach.

---

### Mandatory Skepticism Standard

**This section operates under heightened skepticism compared to the rest of the Research knowledge base.** Quantum computing is a field with a long history of extraordinary claims, aggressive roadmap promises, and hype cycles that have repeatedly outrun demonstrated results. Apply the following rules consistently:

1. **Never report claimed qubit counts at face value.** Distinguish between: physical qubits, logical qubits, and error-corrected logical qubits. These are not interchangeable. A system with 1,000 physical qubits but no demonstrated error correction is fundamentally different from one with even a single fault-tolerant logical qubit. Always state which type is being claimed.

2. **Quantum advantage claims require extraordinary sourcing.** "Quantum supremacy" or "quantum advantage" claims must be sourced to peer-reviewed publications, not company press releases. If a claim is based only on a company's own announcement, mark it `Unverified` and note the absence of independent replication. Document whether independent researchers have attempted to replicate or refute the result (e.g., IBM's classical simulation responses to Google's 2019 Sycamore result).

3. **Commercial timeline claims are almost always optimistic.** Quantum hardware development has a decade-long track record of slippage. When a company projects "fault-tolerant quantum computing by 20XX," document the claim with the date it was made, the mechanism by which they claim to achieve it, and the history of prior timeline projections from the same source. Do not repeat timelines without this context.

4. **"Quantum useful" ≠ "fault-tolerant."** Some companies frame near-term NISQ (Noisy Intermediate-Scale Quantum) applications as commercially relevant. Assess these claims by asking: has any customer demonstrated a verified advantage over classical compute for a real workload? If not, say so.

5. **Error rate and coherence time claims require experimental sourcing.** Gate fidelity, T1/T2 coherence times, and two-qubit gate error rates all degrade at system scale. Quoted figures for small test circuits often do not reflect system-level performance. Note the circuit size and conditions under which figures were measured.

6. **Funding and valuation are not technical validation.** Quantum companies have raised billions on the strength of future promises. Large funding rounds or high valuations should be documented as business facts, not as evidence of technical progress.

7. **Apply the "classical simulation" test.** If a claimed quantum computation has not been shown to be infeasible on classical hardware, it is not evidence of quantum advantage. Note whether any claimed demonstrations have been matched or exceeded by classical simulation after the fact.

8. **DoD Trusted Foundry / Trusted Supplier status claims.** When companies claim or are described as holding [DoD Trusted Foundry or Trusted Supplier status](https://www.acq.osd.mil/asds/dmea/tapo/docs/tp/AccreditedSuppliers-03NOV2025.pdf), link to the official accreditation list (current as of November 3, 2025). Verify the company name appears on that list rather than relying on company self-description. This status is a real regulatory credential that affects market access and national security supply chain confidence; it is not a technical performance claim but should be verified for accuracy.

---

### Key Terminology to Document in Relevant Entries

- **Qubit:** Fundamental unit of quantum information. Physical vs. logical distinction is critical — see above.
- **NISQ (Noisy Intermediate-Scale Quantum):** The current era: 50–1000+ physical qubits, significant noise, no full error correction. NISQ devices can run limited circuits but are not fault-tolerant.
- **Fault-tolerant quantum computing (FTQC):** The long-term goal: logical qubits with error rates low enough for deep circuit execution. Requires error correction codes (surface code, etc.) and a very large physical-to-logical qubit overhead (often estimated at 1,000:1 or more).
- **Error correction / surface code:** Methods for protecting logical qubit state by encoding it across many physical qubits. Surface code is the leading approach; requires ~1,000 physical qubits per logical qubit at practical fidelities.
- **Gate fidelity:** Probability that a quantum gate operation produces the correct result. Two-qubit gate fidelity below ~99.9% is generally insufficient for fault-tolerant circuits.
- **Coherence time (T1, T2):** T1 = energy relaxation time; T2 = dephasing time. Limits circuit depth before errors dominate.
- **Qubit modalities:** Superconducting (IBM, Google, Rigetti), trapped ion (IonQ, Quantinuum), photonic (Xanadu, PsiQuantum), neutral atom (QuEra, Atom Computing), topological (Microsoft). Each has distinct fidelity, speed, connectivity, and scalability trade-offs.
- **Quantum volume (QV):** IBM metric combining qubit count, connectivity, and fidelity into a single benchmark. Disputed by competitors; not universally accepted.
- **CLOPS (Circuit Layer Operations Per Second):** IBM metric for circuit execution speed. Context-dependent — compare only within the same metric framework.
- **#AQ (Algorithmic Qubits):** IonQ metric for effective quantum circuit size. Company-defined; not independently standardized.
- **Analog quantum simulation:** A distinct mode from gate-based quantum computing. D-Wave's annealing approach falls here. Claims of quantum advantage in this mode are contested.

---

### Hardware Modality Tags

Tag every hardware company entry with its primary qubit modality:
- `superconducting` — IBM, Google, Rigetti
- `trapped-ion` — IonQ, Quantinuum
- `photonic` — Xanadu, PsiQuantum
- `topological` — Microsoft (research stage)
- `neutral-atom` — QuEra, Atom Computing (out of initial scope but track as emerging)
- `annealing` — D-Wave (note: not gate-based; distinct computational model)

---

### Claim Verification Additions for Quantum Computing

In addition to the standard Claim Verification section, every quantum computing entry must address:

- **Independent replication status:** Has the claim been independently reproduced? By whom?
- **Classical simulation feasibility:** Has the computation been simulated classically at comparable or better performance?
- **Peer review status:** Is the underlying result published in a peer-reviewed journal? If only a preprint, note it.
- **Roadmap history:** List prior published timelines for the same milestone and whether they were met.

---

### Quantum-Specific Tags

In addition to global tags:
- Modality: `superconducting`, `trapped-ion`, `photonic`, `topological`, `neutral-atom`, `annealing`
- Stage: `nisq`, `fault-tolerant-research`, `fault-tolerant-demonstrated` (use the last only when peer-reviewed evidence exists)
- Application focus: `optimization`, `simulation`, `cryptography`, `machine-learning`, `chemistry`
- Market: `cloud-access`, `hardware-vendor`, `software-layer`, `hybrid-classical-quantum`

---

### Review Cadence

- 90 days for all active hardware companies (roadmap announcements and paper publications move fast)
- 180 days for software/access layer companies
- 365 days for stable reference/overview entries

---

{{< /steering >}}

## Overview

Tracks the development of quantum computing hardware, software, and the race toward practical quantum advantage. The field spans multiple competing hardware modalities — superconducting circuits, trapped ions, photonics, and neutral atoms — each with distinct technical profiles and roadmap trajectories. Progress is real but slow relative to the projections routinely made by companies seeking funding and press coverage.

**Editorial note:** This section applies a higher skepticism standard than the rest of the Research knowledge base. Quantum computing is a field with a long history of aggressive roadmap claims, shifting definitions of success, and hype that has repeatedly outpaced demonstrated results. Claims about qubit counts, quantum advantage, and commercial timelines are documented with source dates and independent verification status.

## Key Themes

- Physical qubit counts are growing but error correction — the prerequisite for practical fault-tolerant computing — remains undemonstrated at useful scale
- The gap between "quantum supremacy" demonstrations and commercial utility remains large; no real-world workload has shown verified advantage over optimized classical compute
- Hardware modalities are diverging rather than converging: superconducting, trapped ion, photonic, and neutral atom approaches each have credible advocates and distinct engineering trade-offs
- Microsoft's topological qubit program has produced extraordinary claims but limited peer-reviewed validation
- D-Wave occupies a distinct position as a quantum annealer, not a gate-based computer — its "quantum advantage" claims apply to a narrow problem class
- Timeline compression is the norm in company communications; most published milestones have slipped by years

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Rigetti Computing](https://www.rigetti.com) | Berkeley, CA, USA | Public (RGTI) | Superconducting gate-based QPUs; Ankaa-3 (84 qubits, 99.5% median 2Q fidelity, company claim); Fab-1 in-house foundry (Fremont CA); cloud access via QCS, AWS Braket, Azure Quantum; financially stressed (revenue declining, $10.8M FY2024). See [entry]({{< relref "rigetti.md" >}}). |
| [Xanadu](https://www.xanadu.ai) | Toronto, Canada | Public (XNDU, Nasdaq/TSX; IPO Mar 2026) | Photonic quantum computing; Borealis quantum advantage system; PennyLane open-source SDK; developing Aurora modular fault-tolerant platform; targeting 2028–2029 fault-tolerant data center. See [entry]({{< relref "xanadu.md" >}}). |
| [PsiQuantum](https://www.psiquantum.com) | Palo Alto, CA, USA | Private (~$7B val.; $2.32B raised) | Silicon photonics fault-tolerant approach (FBQC); Omega chipset manufactured at GlobalFoundries Fab 8; A$940M AUD Australian government deal; $1B Series E (Sept 2025); Chicago site under construction; no operational quantum processor publicly demonstrated as of April 2026; DARPA QBI US2QC final phase selected (Feb 2025). See [entry]({{< relref "psiquantum.md" >}}). |
| [Quantinuum](https://www.quantinuum.com) | Broomfield, CO, USA + Cambridge, UK | Private (~54% Honeywell; IPO targeted 2027) | Trapped-ion hardware (H1, H2, Helios 98-qubit); highest two-qubit gate fidelity publicly demonstrated (99.921% on Helios); TKET open-source compiler; InQuanto chemistry; advanced fault-tolerant research. See [entry]({{< relref "quantinuum.md" >}}). |
| [D-Wave Systems](https://www.dwavesys.com) | Burnaby, Canada | Public (QBTS) | Quantum annealing (not gate-based); Advantage2 processor; narrowly applicable to combinatorial optimization. |
| [IonQ](https://ionq.com) | College Park, MD, USA | Public (IONQ) | Trapped-ion gate-based systems; Forte and Forte Enterprise systems; #AQ metric contested. See [entry]({{< relref "ionq.md" >}}). |
| [SkyWater Technology](https://www.skywatertechnology.com) | Bloomington, MN, USA | Public (SKYT; pending IonQ acquisition) | U.S. pure-play semiconductor foundry; DOD Trusted Foundry; fabricates superconducting qubits (D-Wave), photonics; pending $1.8B IonQ acquisition (expected Q2–Q3 2026). See [entry]({{< relref "skywater-technology.md" >}}). |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [XNDU](https://finance.yahoo.com/quote/XNDU) | [Xanadu](https://www.xanadu.ai) | Photonic quantum computing hardware; Borealis quantum advantage system; Aurora modular fault-tolerant platform; PennyLane open-source SDK. See [entry]({{< relref "xanadu.md" >}}). |
| [IONQ](https://finance.yahoo.com/quote/IONQ) | [IonQ](https://ionq.com) | Trapped-ion quantum computing hardware and cloud access; Forte (#AQ 36) and Tempo (#AQ 64) systems; pending SkyWater foundry acquisition. See [entry]({{< relref "ionq.md" >}}). |
| [SKYT](https://finance.yahoo.com/quote/SKYT) | [SkyWater Technology](https://www.skywatertechnology.com) | U.S. pure-play semiconductor foundry; DOD Trusted Foundry; quantum chip fabrication (superconducting, photonic, cryogenic CMOS); pending IonQ acquisition. See [entry]({{< relref "skywater-technology.md" >}}). |
| [QBTS](https://finance.yahoo.com/quote/QBTS) | [D-Wave Quantum](https://www.dwavesys.com) | Quantum annealing systems and hybrid classical-quantum solvers. |
| [RGTI](https://finance.yahoo.com/quote/RGTI) | [Rigetti Computing](https://www.rigetti.com) | Superconducting gate-based QPUs manufactured at Fab-1 (Fremont, CA); Ankaa-3 84-qubit system (99.5% median 2Q fidelity, company claim); cloud access via QCS, AWS Braket, Azure Quantum; FY2024 revenue $10.8M (declining); $217M cash (Dec 2024); DARPA QBI Stage A (not Stage B). See [entry]({{< relref "rigetti.md" >}}). |

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
    "colorTheme": "light",
    "dateRange": "12M",
    "showChart": true,
    "locale": "en",
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "500",
    "tabs": [
      {
        "title": "Quantum Computing",
        "symbols": [
          {"s": "NASDAQ:IONQ", "d": "IonQ"},
          {"s": "NYSE:QBTS", "d": "D-Wave Quantum"},
          {"s": "NASDAQ:RGTI", "d": "Rigetti Computing"}
        ],
        "originalTitle": "Quantum Computing"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [IBM](https://finance.yahoo.com/quote/IBM) | [IBM Quantum](https://www.ibm.com/quantum) | Largest publicly accessible quantum fleet; superconducting QPUs (Eagle, Heron, Nighthawk, Loon); qLDPC error correction research; 2029 Starling and 2033 Blue Jay fault-tolerant roadmap. See [entry]({{< relref "ibm-quantum.md" >}}). |
| [MSFT](https://finance.yahoo.com/quote/MSFT) | [Microsoft Azure Quantum](https://azure.microsoft.com/en-us/products/quantum) | Topological qubit research (majorana); Azure Quantum cloud platform; claims disputed. |
| [GOOGL](https://finance.yahoo.com/quote/GOOGL) | [Google Quantum AI](https://quantumai.google) | Sycamore/Willow superconducting processors; 2019 and 2024 supremacy claims; Brisbanefablab. |
