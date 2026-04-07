---
title: "SkyWater Technology"
date: 2026-04-07
lastmod: 2026-04-07
last_reviewed: 2026-04-07
draft: false
description: "U.S. pure-play semiconductor foundry serving defense, commercial, and quantum computing customers; pending acquisition by IonQ; fabricates superconducting qubits for D-Wave, photonic chips for PsiQuantum (prior to GlobalFoundries transition), and cryogenic control electronics."
tags: ["semiconductor-foundry", "us-foundry", "quantum-manufacturing", "partnership", "us"]
categories: ["company"]
research_area: "quantum-computing"
source_urls:
  - "https://www.skywatertechnology.com"
  - "https://ir.skywatertechnology.com"
  - "https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/default.aspx"
  - "https://www.skywatertechnology.com/ionq-to-acquire-skywater/"
  - "https://www.skywatertechnology.com/skywater-completes-acquisition-of-fab-25/"
  - "https://www.skywatertechnology.com/skywater-technology-and-quamcore-announce-collaboration-to-fabricate-digital-superconducting-controller-for-scalable-quantum-computing/"
  - "https://www.skywatertechnology.com/skywater-technology-and-silicon-quantum-computing-team-to-advance-hybrid-quantum-classical-computing/"
  - "https://www.skywatertechnology.com/skywaters-commercially-fabricated-qubits-power-d-waves-landmark-achievement-in-quantum-supremacy/"
  - "https://ir.skywatertechnology.com/news/news-details/2023/PsiQuantum-Expands-Development-Engagement-and-Plan-for-Production-Ramp-of-Quantum-Computing-Technology-at-SkyWaters-Minnesota-Fab/default.aspx"
  - "https://www.skywatertechnology.com/enabling-the-quantum-revolution-with-skywaters-advanced-manufacturing/"
  - "https://www.skywatertechnology.com/sky130-open-source-pdk/"
  - "https://www.businesswire.com/news/home/20250630358336/en/SkyWater-Completes-Acquisition-of-Fab-25-Expanding-U.S.-Pure-Play-Foundry-Capacity-for-Critical-Semiconductor-Technologies"
  - "https://www.science.org/doi/10.1126/science.ado6285"
  - "https://en.wikipedia.org/wiki/SkyWater_Technology"
  - "https://www.acq.osd.mil/asds/dmea/tapo/docs/tp/AccreditedSuppliers-03NOV2025.pdf"
stale_after_days: 180
---

## Summary

SkyWater Technology (NASDAQ: SKYT) is a U.S.-based pure-play semiconductor foundry headquartered in Bloomington, Minnesota. Originally the Cypress Semiconductor wafer fabrication facility, it was acquired by private equity in 2017 and went public in 2021. SkyWater holds U.S. Department of Defense Trusted Foundry status and specializes in mature nodes (130nm–65nm) for defense, aerospace, automotive, and increasingly quantum computing customers. As of early 2026, the company is the subject of a pending $1.8 billion acquisition by quantum computing company IonQ (NASDAQ: IONQ), which, if completed, would make SkyWater IonQ's in-house fabrication platform for trapped-ion quantum hardware.

## Key Facts

- **Founded/Formed:** 2017 (acquisition of Cypress Semiconductor's Bloomington, MN fab by Oxbow Industries; fab itself dates to pre-2017 Cypress Semiconductor era)
- **Incorporated:** 2016
- **Type:** Company (publicly traded — NASDAQ: SKYT)
- **CEO:** Thomas Sonderman
- **HQ:** Bloomington, Minnesota, USA
- **Facilities:** Fab 1 (Bloomington, MN, 200mm); NeoCity (Osceola, FL, acquired 2021); Fab 25 (Austin, TX, acquired June 30, 2025 from Infineon for ~$93M)
- **DOD Status:** Trusted Foundry ([DoD-certified for secure manufacturing of classified and sensitive defense semiconductors](https://www.acq.osd.mil/asds/dmea/tapo/docs/tp/AccreditedSuppliers-03NOV2025.pdf))
- **FY2025 Revenue:** $442.1M (reported; record year; 29% YoY growth)
- **FY2025 Adjusted EBITDA:** $53.2M (record; +57% YoY)
- **Employees:** Approximately 1,000 added via Fab 25 acquisition in mid-2025
- **Process nodes (standard):** 130nm (SKY130), 65nm, down to 55nm; 200mm wafer platform
- **Quantum-specific:** Niobium-based superconducting process integrations; cryogenic CMOS; photonics structures; SFQ (Single Flux Quantum) process development
- **Pending acquisition:** IonQ, $1.8B cash-and-stock deal announced January 26, 2026; shareholder vote scheduled May 8, 2026; expected close Q2–Q3 2026

## What It Is / How It Works

SkyWater operates as a pure-play merchant foundry — it does not design or sell its own chips but manufactures silicon devices for external customers. The company's core business is mature-node fabrication (not cutting-edge process nodes like 3nm or 7nm), which is structurally differentiated from TSMC, Samsung, or Intel Foundry, whose competitive moat lies in leading-edge processes. SkyWater's differentiation is in three areas: domestic (U.S.-only) manufacturing with DoD Trusted Foundry certification; specialized process development for non-standard materials and device architectures; and customer-funded technology development services (Advanced Technology Services, or ATS), where SkyWater co-develops fabrication processes with customers for novel device types.

The company operates 200mm wafer fabs (as opposed to 300mm, which is standard for high-volume leading-edge production). 200mm fabs have lower throughput but are more flexible and capital-efficient for specialty processes. Three fabs as of July 2025: Bloomington, MN (flagship, ~170,000 wafer starts/year); Osceola, FL (NeoCity, acquired from University of Central Florida in 2021); and Austin, TX (Fab 25, formerly Infineon's facility, acquired June 30, 2025, adding ~400,000 wafer starts/year capacity on 65–130nm nodes).

For quantum computing specifically, SkyWater has invested in process capabilities that go beyond standard CMOS. Superconducting quantum devices require custom materials deposition (notably niobium for Josephson junction qubits, which are the physical basis of superconducting qubit systems used by D-Wave, IBM, Google, and others), specialized device patterning at micrometer scales, and integration of layers that must maintain extreme purity to limit qubit energy loss. SkyWater has built this capability over approximately a decade, beginning with its partnership with D-Wave to fabricate annealing qubit processors. Separately, the company developed photonic integration capabilities — high-performance waveguide structures and photonics process modules — that it used to support PsiQuantum's silicon photonic qubit chip development starting around 2022–2023 at the Bloomington fab. PsiQuantum later moved its primary production relationship to GlobalFoundries Fab 8 (New York), but the SkyWater engagement established SkyWater's photonics credibility.

The open-source SKY130 process design kit (PDK), released in 2020 in collaboration with Google, is a 130nm CMOS process with full open-source design rules and models. It has been used primarily by researchers, universities, and startups for low-cost ASIC prototyping rather than quantum computing directly, but it established SkyWater as the first foundry to offer a fully open-source production PDK and expanded its visibility in the academic and open-hardware communities.

SkyWater's IonQ acquisition rationale is straightforward: IonQ uses trapped-ion technology, which does not require the niobium Josephson junction processes used by superconducting qubit companies. Trapped-ion systems require precision photonics (for laser-based qubit control), ion trap microstructures (etched or microfabricated electrode arrays), and standard CMOS for control electronics. SkyWater's photonics and custom process capabilities, combined with its domestic supply chain status, make it a credible manufacturing partner. IonQ has described plans to use SkyWater's facilities as "Regional Quantum Production Hubs" once the acquisition closes.

## Notable Developments

- **2026-01-26:** IonQ announced agreement to acquire SkyWater Technology for $35.00 per share ($15.00 cash + $20.00 in IonQ stock, subject to exchange ratio collar), implying ~$1.8B total equity value. Both boards unanimously approved. SkyWater shareholder vote scheduled for May 8, 2026; deal expected to close Q2–Q3 2026. SkyWater would operate as a wholly owned subsidiary under its existing name and CEO.
- **2026-04:** SkyWater reported FY2025 full year revenue of $442.1M (record; +29% YoY) and Adjusted EBITDA of $53.2M (+57% YoY). Record performance attributed to Fab 25 contribution and growing quantum ATS revenue.
- **2025-11-20:** SkyWater and Silicon Quantum Computing (SQC, the Australian government-backed silicon spin qubit company) announced a joint program to advance hybrid quantum-classical computing. SQC will supply atomically-engineered QPUs; SkyWater will provide superconducting resonators and tailored silicon wafers from its secure production line.
- **2025-11-06:** SkyWater and QuamCore announced a multi-million-dollar collaboration to co-engineer Single Flux Quantum (SFQ) digital control circuits for superconducting qubit systems. SFQ technology operates natively at cryogenic temperatures (~10mK) and is claimed to reduce cabling by up to 1,000x compared to conventional approaches. Development milestones targeting 12–18 months including test-vehicle fabrication.
- **2025-07 (Q3 record reported):** SkyWater reported record Q3 2025 results, noting over 30% growth in quantum-related ATS revenues in FY2025, with four new quantum customers signed since Q2 2025.
- **2025-06-30:** SkyWater completed acquisition of Infineon's Fab 25 in Austin, Texas (~$93M total consideration). Fab 25 adds ~400,000 wafer starts/year capacity in 65–130nm nodes; approximately 1,000 Infineon employees transferred to SkyWater. Infineon retains a long-term supply agreement.
- **2025-03-12:** D-Wave and SkyWater announced that SkyWater-fabricated qubits powered D-Wave's Advantage2™ prototype result, published in *Science* (doi: 10.1126/science.ado6285). The paper claims computational supremacy over classical simulation in a quantum spin glass simulation problem. (See Claim Verification.)
- **2023-05:** PsiQuantum expanded its development agreement with SkyWater at the Bloomington, MN fab, extending a silicon photonic chip development program using 200mm wafers. PsiQuantum subsequently selected GlobalFoundries Fab 8 for its primary production ramp.
- **2021-04:** SkyWater Technology went public on NASDAQ under ticker SKYT.
- **2021:** SkyWater acquired the NeoCity fab in Osceola, Florida (formerly University of Central Florida research facility).
- **2020:** SkyWater and Google released the SKY130 open-source Process Design Kit (PDK), the first fully open-source production-grade foundry PDK, enabling low-cost ASIC prototyping at 130nm.
- **2017:** Oxbow Industries (private equity) acquired the Cypress Semiconductor wafer fab in Bloomington, MN for ~$30M and formed SkyWater Technology. The underlying fab dates to Cypress Semiconductor's earlier operations.

## Key People

### Thomas Sonderman — President & CEO

- **LinkedIn:** https://www.linkedin.com/in/thomas-sonderman (verify)
- **Background:** Long career in semiconductor manufacturing and foundry operations. Named President & CEO of SkyWater; has been the public face of the company through its IPO, Fab 25 acquisition, and IonQ deal.
- **Role in IonQ transaction:** Sonderman will continue as CEO of SkyWater as a wholly owned IonQ subsidiary, per the acquisition announcement. He is a member of the merger proxy recommendation committee.

## Claim Verification

### Claim: SkyWater-Fabricated Qubits Power D-Wave "Quantum Supremacy" (Science, March 2025)

**Status:** Disputed

**Supporting sources:**
- [D-Wave/SkyWater press release, March 12, 2025](https://www.skywatertechnology.com/skywaters-commercially-fabricated-qubits-power-d-waves-landmark-achievement-in-quantum-supremacy/) — joint company announcement
- [*Science*, doi: 10.1126/science.ado6285](https://www.science.org/doi/10.1126/science.ado6285) — peer-reviewed publication in *Science* (AAAS); the D-Wave Advantage2™ annealing processor outperformed classical supercomputer (Frontier, Oak Ridge) on a quantum spin glass simulation problem in wall-clock time

**Refuting / questioning sources:**
- [SiliconANGLE coverage of challenges](https://siliconangle.com/2025/03/12/d-wave-claims-achieved-quantum-supremacy-last-others-disagree/) — documents two independent teams disputing the claim; one team (led by Dries Sels, NYU) reported simulating the same problem on a laptop in approximately two hours using classical methods, suggesting D-Wave's specific quantum simulation was not classically infeasible
- [phys.org coverage](https://phys.org/news/2025-03-d-quantum-problem-scientific-relevance.html) — notes ongoing dispute about whether classical algorithms were fully optimized in D-Wave's comparison

**Critical context for SkyWater specifically:**
- The peer-reviewed publication validates that SkyWater can fabricate superconducting annealing qubits at commercial scale — that is, the manufacturing capability is substantiated
- The "quantum supremacy" characterization of the D-Wave computational result is disputed; the fabrication quality claim (SkyWater made manufacturable superconducting qubits that function in a commercial quantum processor) is more robust
- D-Wave's annealing approach is a distinct computational model from gate-based quantum computing and its "supremacy" claims apply to a narrow class of problems

**Peer review status:** Published in *Science* (peer-reviewed). However, independent replication challenges have been raised post-publication; the specific classical simulation feasibility question is contested.

**Fabrication claim assessment:** Partially verified — SkyWater's decade-long role in D-Wave qubit fabrication is well-documented and the production of functioning qubits in a commercial processor is substantiated. The "supremacy" framing is disputed.

---

### Claim: SFQ Control Reduces Cabling by "Up to 1,000x" (QuamCore Collaboration, November 2025)

**Status:** Unverified (early-stage development claim)

**Supporting sources:**
- [SkyWater/QuamCore press release, November 6, 2025](https://www.skywatertechnology.com/skywater-technology-and-quamcore-announce-collaboration-to-fabricate-digital-superconducting-controller-for-scalable-quantum-computing/) — company announcement
- SFQ technology is a known research area; claims about cabling reduction are consistent with published SFQ architecture literature in general

**Refuting / questioning sources:**
- No independent peer-reviewed publication confirming the specific "1,000x" cabling reduction claim for SkyWater/QuamCore's joint process
- The partnership is at the co-engineering and test-vehicle stage (12–18 month development timeline announced November 2025); no fabricated prototype has been demonstrated or independently verified

**Status detail:** SFQ (Single Flux Quantum) digital logic operating at cryogenic temperatures is a legitimate research area with a real theoretical basis for the cabling reduction claim in quantum control systems. However, the 1,000x figure is an architectural projection from the press release, not a measured result from a fabricated device. Mark as unverified until test-vehicle results are published.

---

### Claim: 30%+ Growth in Quantum ATS Revenue (FY2025)

**Status:** Partially verified

**Supporting sources:**
- [SkyWater Q3 2025 results](https://ir.skywatertechnology.com/news/news-details/2025/SkyWater-Technology-Reports-Record-Third-Quarter-2025-Results/default.aspx) — company financial report; stated ATS quantum revenue growth >30% for FY2025
- FY2025 full-year revenue of $442.1M confirmed via financial reporting (record year)

**Critical context:** ATS (Advanced Technology Services) revenue is customer-funded R&D and process development. Growth in ATS quantum revenue means more quantum companies are paying SkyWater to develop fabrication processes, not that SkyWater is producing high-volume quantum chips. High-volume quantum chip production remains speculative pending IonQ acquisition and the broader maturation of the quantum hardware market.

**Mark:** Partially verified — revenue growth figure is from SkyWater's own reported financials (not yet independently audited in full-year 10-K context at time of writing); the 30%+ ATS growth claim is company-stated, not independently confirmed.

---

### Claim: IonQ Foundry Acquisition Enables "200,000-qubit QPUs by 2028"

**Status:** Unverified (roadmap projection, multiple dependencies)

**Supporting sources:**
- [IonQ/SkyWater acquisition announcement](https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/default.aspx) — IonQ investor relations; describes 200,000-qubit target for 2028 enabled by acquisition

**Critical context:**
- The 200,000-qubit figure is IonQ's investor-facing roadmap projection, not a technical specification supported by peer-reviewed engineering analysis
- The claim depends on: (a) regulatory approval and closing of the acquisition; (b) SkyWater successfully developing trapped-ion-specific fabrication processes at scale (IonQ's trapped-ion technology does not currently use SkyWater's existing superconducting qubit processes — it requires photonics and precision ion trap microstructures); (c) IonQ's Electronic Qubit Control (EQC) technology scaling as projected; and (d) quantum error correction milestones being achieved on schedule
- IonQ's FY2025 guidance was $106–110M in revenue; a company at that revenue scale acquiring a $442M-revenue foundry and directing significant capex toward novel fabrication is a substantial organizational and engineering challenge

**Mark:** Unverified — aspirational roadmap claim with multiple unresolved technical and business dependencies. Document with date made (January 2026) for future tracking.

---

### Claim: PsiQuantum Production at SkyWater's Minnesota Fab

**Status:** Superseded / no longer accurate

**Note:** As of 2023, PsiQuantum's primary production ramp agreement shifted to GlobalFoundries Fab 8 in Malta, New York. SkyWater's engagement with PsiQuantum was a development-phase collaboration that concluded or transitioned before PsiQuantum's Australian government deal and GlobalFoundries production ramp were announced. SkyWater's role in PsiQuantum's commercialization path appears to have been early-stage only. This does not negate SkyWater's photonic process development capabilities, but the PsiQuantum partnership should not be cited as evidence of ongoing production-scale photonic quantum chip manufacturing by SkyWater.

## Key Organizations

- **IonQ (NASDAQ: IONQ)** — pending acquirer; $1.8B acquisition announced January 2026; shareholder vote May 8, 2026. See [entry]({{< relref "ionq.md" >}}).
- **D-Wave Quantum (NASDAQ: QBTS)** — decade-long foundry customer; SkyWater fabricates D-Wave's superconducting annealing qubit processors (Advantage2™ prototype qubits confirmed). See [entry for D-Wave](https://finance.yahoo.com/quote/QBTS/).
- **Silicon Quantum Computing (SQC)** — Australian government-backed silicon spin qubit company; SkyWater partnership announced November 2025 for hybrid quantum-classical compute stack.
- **QuamCore** — quantum computing startup targeting superconducting SFQ control circuits; SkyWater collaboration for SFQ fabrication process announced November 2025.
- **PsiQuantum** — prior photonic chip development partnership (2022–2023); PsiQuantum subsequently moved primary production to GlobalFoundries.
- **Infineon Technologies** — sold Fab 25 (Austin, TX) to SkyWater in June 2025; retains long-term supply agreement as foundry customer.
- **Google** — co-released open-source SKY130 PDK (2020); partner in open-source ASIC manufacturing initiative.
- **Oxbow Industries** — private equity firm that formed SkyWater in 2017 via Cypress Semiconductor fab acquisition; retains majority ownership stake.
- **U.S. Department of Defense** — SkyWater holds [Trusted Foundry status](https://www.acq.osd.mil/asds/dmea/tapo/docs/tp/AccreditedSuppliers-03NOV2025.pdf), enabling it to manufacture secure, classified semiconductors for defense programs.

## Sources

- [SkyWater Technology Corporate Site](https://www.skywatertechnology.com)
- [SkyWater Investor Relations](https://ir.skywatertechnology.com)
- [IonQ/SkyWater acquisition announcement (IonQ)](https://investors.ionq.com/news/news-details/2026/IonQ-to-Acquire-SkyWater-Technology-Creating-the-Only-Vertically-Integrated-Full-Stack-Quantum-Platform-Company/default.aspx)
- [IonQ/SkyWater acquisition announcement (SkyWater)](https://www.skywatertechnology.com/ionq-to-acquire-skywater/)
- [SkyWater Fab 25 acquisition completed](https://www.skywatertechnology.com/skywater-completes-acquisition-of-fab-25/)
- [SkyWater Q3 2025 Record Results](https://ir.skywatertechnology.com/news/news-details/2025/SkyWater-Technology-Reports-Record-Third-Quarter-2025-Results/default.aspx)
- [QuamCore SFQ collaboration announcement](https://www.skywatertechnology.com/skywater-technology-and-quamcore-announce-collaboration-to-fabricate-digital-superconducting-controller-for-scalable-quantum-computing/)
- [Silicon Quantum Computing partnership announcement](https://www.skywatertechnology.com/skywater-technology-and-silicon-quantum-computing-team-to-advance-hybrid-quantum-classical-computing/)
- [D-Wave / SkyWater quantum supremacy announcement](https://www.skywatertechnology.com/skywaters-commercially-fabricated-qubits-power-d-waves-landmark-achievement-in-quantum-supremacy/)
- [PsiQuantum expands engagement at SkyWater MN fab (2023)](https://ir.skywatertechnology.com/news/news-details/2023/PsiQuantum-Expands-Development-Engagement-and-Plan-for-Production-Ramp-of-Quantum-Computing-Technology-at-SkyWaters-Minnesota-Fab/default.aspx)
- [SkyWater quantum manufacturing overview](https://www.skywatertechnology.com/enabling-the-quantum-revolution-with-skywaters-advanced-manufacturing/)
- [SKY130 open source PDK](https://www.skywatertechnology.com/sky130-open-source-pdk/)
- [D-Wave *Science* paper (peer-reviewed)](https://www.science.org/doi/10.1126/science.ado6285)
- [SiliconANGLE — challenges to D-Wave supremacy claim](https://siliconangle.com/2025/03/12/d-wave-claims-achieved-quantum-supremacy-last-others-disagree/)
- [Wikipedia: SkyWater Technology](https://en.wikipedia.org/wiki/SkyWater_Technology)
- [Manufacturing Dive: IonQ/SkyWater deal overview](https://www.manufacturingdive.com/news/ionq-spend-nearly-2-billion-chips-maker-skywater-us-quantum-computing/810601/)
