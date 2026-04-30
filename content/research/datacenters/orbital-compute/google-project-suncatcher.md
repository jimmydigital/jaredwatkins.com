---
title: "Google Project Suncatcher"
date: 2026-04-29
lastmod: 2026-04-29
draft: false
description: "Google research initiative to deploy TPU-equipped solar-powered satellite clusters in LEO as a scalable alternative to terrestrial AI data centers."
tags: ["orbital-compute", "space", "ai-datacenter", "tpu", "us", "research-initiative"]
categories: ["technology"]
research_area: "datacenters/orbital-compute"
source_urls:
  - "https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/"
  - "https://blog.google/technology/research/google-project-suncatcher/"
  - "https://www.datacenterdynamics.com/en/news/project-suncatcher-google-to-launch-tpus-into-orbit-with-planet-labs-envisions-1km-arrays-of-81-satellite-compute-clusters/"
  - "https://spacenews.com/planet-bets-on-orbital-data-centers-in-partnership-with-google/"
  - "https://satnews.com/2026/01/19/google-addresses-orbital-debris-risks-for-project-suncatcher-ai-constellation/"
last_reviewed: 2026-04-29
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Project Suncatcher is a Google Research moonshot studying the feasibility of solar-powered, TPU-equipped satellite constellations in low Earth orbit as a long-run alternative to terrestrial AI data centers. A peer-reviewed pre-print published in November 2025 documented radiation testing of Trillium TPUs, inter-satellite optical link designs, formation flight dynamics for an 81-satellite 1 km-radius cluster, and a launch cost analysis projecting economic viability at ~$200/kg to LEO. The first prototype mission — two satellites built with Planet Labs — is targeted for early 2027.

## Key Facts

- **Initiated by:** Google / Alphabet
- **Type:** Research initiative / technology moonshot
- **Status:** Active — pre-print published Nov 2025; prototype mission with Planet Labs targeting early 2027
- **Prototype partner:** Planet Labs (PBC; NYSE: PL)
- **Compute hardware:** Google Trillium (v6e) Cloud TPU
- **Target orbit:** Dawn-dusk sun-synchronous LEO, ~650 km altitude
- **Cluster design:** 81 satellites in a 1 km radius planar formation
- **ISL bandwidth demonstrated:** 1.6 Tbps bidirectional (bench-scale demonstrator)
- **TPU radiation survival:** No hard failures to 15 krad(Si) TID; HBM showed anomalies at 2 krad (2.7× 5-year mission requirement of 750 rad)
- **Key paper authors:** Blaise Agüera y Arcas, Travis Beals, Maria Biggs, Jessica V. Bloom, Thomas Fischbacher, Konstantin Gromov, Urs Köster, Rishiraj Pravahan, James Manyika

## What It Is / How It Works

Project Suncatcher works backwards from a long-run hypothesis: that AI compute demand will grow faster than terrestrial energy supply can accommodate, and that the most scalable long-term solution is to tap solar energy directly in space. The Sun delivers ~1,361 W/m² in LEO — roughly 8× the annual energy yield of a mid-latitude ground panel once weather and day/night losses are included. A dawn-dusk sun-synchronous orbit maximizes continuous illumination.

Rather than transmitting power back to Earth (the traditional space-based solar power concept, which faces beam-forming and atmospheric-loss challenges), Suncatcher proposes doing the compute in orbit and communicating results to ground stations via optical or radio links. Thermal management in vacuum is handled passively via heat pipes and radiators — eliminating the cooling water overhead (WUE) and most of the PUE overhead of terrestrial data centers.

The core technical challenges addressed in the November 2025 paper are: (1) inter-satellite communication at ML cluster bandwidths; (2) formation flight stability for tightly clustered satellites; (3) radiation tolerance of commercial AI accelerators; and (4) launch cost economics.

For inter-satellite links (ISLs), the key insight is that received optical power scales inversely with the square of distance. By flying satellites in close formation (hundreds of meters to low hundreds of km), COTS dense wavelength-division multiplexing (DWDM) transceivers — the same equipment used in terrestrial data centers — can achieve the multi-Tbps aggregate bandwidths required for ML cluster interconnects. A bench demonstrator achieved 1.6 Tbps bidirectional over a short free-space path using 800G commercial transceivers. Spatial multiplexing at very short ranges (<10 km) enables further bandwidth scaling.

Formation flight for an 81-satellite constellation at 1 km cluster radius was analyzed using Hill-Clohessy-Wiltshire orbital mechanics plus J2 oblateness corrections. The analysis found that a planar constellation can maintain stable nearest-neighbor relationships with modest delta-v requirements beyond normal station-keeping, with the J2 drift compensated by a slight axis-ratio adjustment (2:1.0037 vs. 2:1 for pure Keplerian orbits). The constellation shape cycles twice per orbit.

Radiation testing of Google's Trillium (v6e) TPU — the first published radiation results for a high-performance ML accelerator — used a 67 MeV proton beam at UC Davis Crocker Nuclear Laboratory. The TPU survived to 15 krad(Si) TID with no hard failures, well above the 750 rad 5-year mission requirement for shielded LEO. High Bandwidth Memory (HBM) was the most sensitive subsystem: uncorrectable ECC errors (UECCs) began at ~44 rad/event, yielding ~1 failure per 10 million inferences at the expected 150 rad/year orbital dose. Training workloads require further study. CPU and RAM showed single-event functional interrupts (SEFIs) at ~400–450 rad per event.

The launch cost analysis projects a path to <$200/kg to LEO via SpaceX Starship learning-curve extrapolation by the mid-2030s, contingent on ~180 Starship launches/year. At $200/kg, annualized launched power cost for a Starlink v2-class satellite is modeled at ~$810/kW/year — comparable to the $570–3,000/kW/year range for terrestrial AI data center power spend.

## Notable Developments

- **2026-01:** Google published a response to orbital debris concerns raised by the Suncatcher constellation concept, noting debris avoidance is a design requirement.
- **2025-11:** Google published peer-reviewed pre-print on Suncatcher; announced Planet Labs as prototype mission partner targeting early 2027.
- **2025-11:** Trillium TPU radiation test results disclosed — first published radiation data for a high-performance ML accelerator; survived 15 krad(Si) with no hard TPU failures.
- **2025-11:** Bench-scale ISL demonstrator validated 1.6 Tbps bidirectional free-space optical transmission using COTS components.

## Key People

- **Blaise Agüera y Arcas** — Google; project originator; ML researcher and VP
  - LinkedIn: https://www.linkedin.com/in/blaise-aguera-y-arcas/
  - Previous: Microsoft Research (principal researcher, 2006–2014)
- **Jessica V. Bloom** — Google; led launch cost analysis and manuscript preparation
  - LinkedIn: not confirmed — TODO: verify
- **Thomas Fischbacher** — Google; orbital dynamics and formation flight work
  - LinkedIn: not confirmed — TODO: verify
- **Urs Köster** — Google; inter-satellite link analysis and radiation testing
  - LinkedIn: not confirmed — TODO: verify
- **James Manyika** — Google (SVP, Technology & Society); overall supervision
  - LinkedIn: https://www.linkedin.com/in/james-manyika/
  - Previous: McKinsey Global Institute (Director, 1996–2022)

### People — Last Reviewed: 2026-04-29

## Claim Verification

### Claim: Trillium TPU survives 5-year LEO mission radiation dose without hard failures

**Status:** Verified (by Google internal testing; no independent third-party replication published)

**Supporting sources:**
- [Google Research Blog — Project Suncatcher](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/) — documents TID survival to 15 krad(Si), 20× the 5-year mission requirement of 750 rad
- Pre-print arXiv paper (Agüera y Arcas et al., 2025) — full methodology at UC Davis Crocker Nuclear Laboratory with 67 MeV proton beam

**Refuting / questioning sources:**
- No independent third-party replication published as of April 2026
- HBM UECC rate (~1 event per 50 rad) requires system-level mitigation for training workloads; paper explicitly notes this requires further study
- Silent data corruption (SDC) rate of ~1 per 107 rad in one test run requires more data to solidify

**Summary:** TPU core logic radiation survival claim is internally verified and technically credible; HBM memory sensitivity is real and acknowledged; training workload implications remain unquantified.

### Claim: Launch costs reach <$200/kg to LEO by mid-2030s

**Status:** Partially verified — plausible projection with significant execution risk

**Supporting sources:**
- [Suncatcher pre-print](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/) — 20% learning rate extrapolation from SpaceX historical data; Starship 4 cost modeling at 10–100× reuse
- SpaceX Starship stated targets consistent with sub-$200/kg at high reuse rates

**Refuting / questioning sources:**
- Requires ~180 Starship launches/year average — well below stated SpaceX targets but still a substantial operational ramp
- SpaceX's own IPO S-1 filing described orbital AI data centers as "unproven technologies" that "may not achieve commercial viability"
- Deutsche Bank estimates orbital compute cost parity with terrestrial is "well into the 2030s"

**Summary:** Projection is analytically grounded but depends on SpaceX achieving reuse and launch-rate targets that have no historical precedent at this scale.

## Sources

- [Google Research Blog: Exploring a space-based, scalable AI infrastructure system design](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/) — primary research summary
- [Google Blog: Project Suncatcher](https://blog.google/technology/research/google-project-suncatcher/) — announcement and overview
- [Data Center Dynamics: Project Suncatcher coverage](https://www.datacenterdynamics.com/en/news/project-suncatcher-google-to-launch-tpus-into-orbit-with-planet-labs-envisions-1km-arrays-of-81-satellite-compute-clusters/) — Planet Labs partnership and 2027 launch timeline
- [SpaceNews: Planet Labs bets on orbital data centers](https://spacenews.com/planet-bets-on-orbital-data-centers-in-partnership-with-google/) — Planet Labs strategic context
- [SatNews: Google addresses orbital debris risks](https://satnews.com/2026/01/19/google-addresses-orbital-debris-risks-for-project-suncatcher-ai-constellation/) — January 2026 debris response
