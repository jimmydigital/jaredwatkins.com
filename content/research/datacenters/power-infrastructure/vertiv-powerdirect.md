---
title: "Vertiv™ PowerDirect"
date: 2026-07-28
lastmod: 2026-07-28
draft: false
description: "Vertiv's DC power distribution product family for AI racks, spanning the PowerDirect Rack/3000 in-rack 50 VDC power shelf (33 kW/1U, dual AC/800 VDC input) and the PowerDirect 5000, an 800 VDC 'sidecar' — a standalone power center bundled next to the IT rack (400–900 kW over busbar) that lets operators keep legacy AC infrastructure while introducing high-voltage DC at the rack; portfolio commercialization begins H2 2026, timed ahead of NVIDIA Rubin Ultra/Kyber deployments in 2027."
research_area: "datacenters/power-infrastructure"
source_urls:
  - "https://www.vertiv.com/en-us/insights/articles/blog-posts/from-rack-to-data-hall-the-practical-path-to-800-vdc/"
  - "https://www.vertiv.com/en-us/insights/articles/blog-posts/vertiv-powerdirect-rack-33kw--a-new-standard-in-modern-data-center-power/"
  - "https://www.vertiv.com/en-us/products-catalog/critical-power/dc-power-systems/powerdirect-3000-33kW/"
  - "https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/"
  - "https://www.prnewswire.com/news-releases/vertiv-accelerates-ai-infrastructure-evolution-in-alignment-with-nvidia-800-vdc-power-architecture-announcement-302458599.html"
last_reviewed: 2026-07-28
stale_after_days: 60
related:
  - "datacenters/power-infrastructure/vertiv.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Vertiv™ PowerDirect is Vertiv's brand for DC power distribution hardware aimed at high-density AI racks, and it now spans two distinct product tiers. The PowerDirect Rack (also sold as the PowerDirect 3000) is an in-rack 50 VDC power shelf delivering 33 kW per 1U, stackable to 132 kW per rack, that accepts either standard AC or an emerging 800 VDC facility feed. The newer PowerDirect 5000 is an 800 VDC "sidecar" — a standalone power center installed next to, rather than inside, the IT rack — delivering 400–900 kW over a busbar directly to a GPU rack. The sidecar is Vertiv's near-term answer to the industry-wide shift to 800 VDC power architecture: it returns the 8–16 rack units historically consumed by power conversion back to compute, while letting operators keep most of their existing AC infrastructure upstream. That combination — high-voltage DC at the rack without a facility-wide rebuild — is explicitly pitched as a bridge for brownfield and legacy datacenters preparing for next-generation, megawatt-class compute density.

## Key Facts

- **Brand family:** Vertiv™ PowerDirect — spans 48/50 VDC in-rack shelves and the newer 800 VDC sidecar line
- **PowerDirect Rack / PowerDirect 3000:** 1U power shelf, 33 kW (660A at 50 VDC) per shelf, stackable to 132 kW/rack; 97.5% peak conversion efficiency; hot-pluggable 5.5 kW power modules; dual input — accepts 400/230–480/277 VAC three-phase *or* an 800 VDC-class DC source (190–410 VDC range), output fixed at 50 VDC to the IT load; OCP Open Rack V3 HPR compliant
- **PowerDirect 5000 (800 VDC sidecar):** Standalone 800 VDC power center bundled alongside the IT rack; delivers 400–900 kW over a busbar tied to the GPU rack; frees 8–16 rack units of space inside the 42U enclosure previously occupied by power conversion hardware
- **Type:** Product line (DC power distribution hardware), not a standalone company — made by Vertiv Holdings (NYSE: VRT); see [Vertiv entry]({{< relref "vertiv.md" >}})
- **Status:** PowerDirect Rack/3000 — shipping (commercially available, referenced in Vertiv product catalog); PowerDirect 5000 sidecar — in customer lab validation as of mid-2026, portfolio commercialization targeted for H2 2026, customer pilots and deployment ramp through 2027
- **Target platform alignment:** Timed ahead of NVIDIA Rubin Ultra and Kyber rack-scale platforms (2027 rollout); NVIDIA itself demonstrated an 800V sidecar powering 576 Rubin Ultra GPUs in a single Kyber rack at GTC 2025
- **Key differentiator vs. facility-wide DC conversion:** Sidecar architecture contains the initial 800 VDC transition to the rack/pod level, preserving upstream AC infrastructure — positioned explicitly as a practical bridge for existing (brownfield) datacenters rather than a forced facility rebuild

## What It Is / How It Works

Rack power delivery for AI compute is running into a physical wall. Vertiv frames it around 350–400 kW per rack: beyond that point, the copper and connector volume needed to carry enough current at conventional 48/54 VDC in-rack distribution starts competing directly with compute for physical space — Vertiv cites 8 to 16 rack units of a 42U enclosure being consumed by power shelves alone as racks scale from 72 to 576 GPUs. The industry-wide response, backed by NVIDIA and a broad silicon and power-systems ecosystem (Eaton, Schneider Electric, Delta, Infineon, Navitas, and others), is to move to 800 VDC distribution: higher voltage means lower current for the same power, which reduces both conductor size and resistive losses.

PowerDirect is Vertiv's product expression of that shift, and it currently covers two different points on the transition path. The **PowerDirect Rack (PowerDirect 3000)** is the more mature, already-shipping product: a 1U, 33 kW power shelf that converts either standard three-phase AC or (looking ahead) an 800 VDC-class facility feed down to 50 VDC for the IT load. Because its input stage already accepts a DC source in the 190–410 VDC range in addition to AC, it functions as a stepping-stone product — datacenters can deploy it today on conventional AC power and later feed it from a higher-voltage DC bus without swapping the rack-level hardware.

The **PowerDirect 5000** is the more consequential product for the 800 VDC transition itself. Rather than trying to fit an 800 VDC power stage inside the rack, Vertiv (and the industry more broadly, per NVIDIA's own Kyber sidecar reference design shown at GTC 2025) is pulling power conversion out of the rack entirely into an adjacent "sidecar" enclosure. The sidecar is a dedicated 800 VDC power center that sits next to the IT rack and feeds it 400–900 kW over a busbar. Scott Armul, Vertiv's Chief Product and Technology Officer, described the shift at Vertiv's May 2026 investor conference as "a story of DC power in the rack moving to DC power in the pod."

The strategic significance for legacy datacenters — the specific angle relevant here — is what the sidecar architecture *doesn't* require. Vertiv is explicit that adopting 800 VDC via the sidecar does not force an operator to rebuild upstream AC infrastructure: the sidecar contains the initial DC transition to the space immediately around the rack, so an existing facility can bring 800 VDC-capable racks online without redesigning switchgear, UPS, or busway further upstream. Vertiv describes this as an "optionality bridge" — operators can adopt higher-voltage DC at the rack while the rest of the facility remains on its existing AC power train, and extend DC further upstream (to the pod, then to a centralized, medium-voltage-connected DC architecture) only when it makes sense for a given site or generation of compute. That two-stage roadmap — rack-adjacent sidecar now, pod-level and centralized facility DC later (2028–2029 and beyond) — mirrors the pattern of prior high-density retrofits (rear-door heat exchangers before full direct-liquid-cooling conversions) where a bolt-on intermediate step lets existing buildings absorb a step-change in density without full reconstruction.

Vertiv describes two parallel paths for the eventual centralized-DC end state: an MV DC UPS (a transformer paired with a rectifier converting medium-voltage AC directly to facility-wide 800 VDC, which Vertiv says has higher technology readiness today) and a solid-state transformer approach (better efficiency and footprint, but a less mature supply chain). Both are in active development. To validate the complete sidecar-to-rack system under real load, Vertiv is standing up a dedicated infrastructure test lab built around a 1.5 MW AI pod and thermal test vehicles up to 600 kW.

## Notable Developments

- **2026-07:** Vertiv publishes "From rack to data hall: The practical path to 800 VDC," detailing the PowerDirect 5000 sidecar (400–900 kW, rack-adjacent), the phased roadmap to pod- and facility-level DC, and confirming H2 2026 portfolio commercialization with customer pilots through 2027. ([Vertiv](https://www.vertiv.com/en-us/insights/articles/blog-posts/from-rack-to-data-hall-the-practical-path-to-800-vdc/))
- **2026-05:** At Vertiv's Investor Conference, CPTO Scott Armul frames the transition as "DC power in the rack moving to DC power in the pod" and confirms the 800 VDC roadmap is tied to specific, named (but undisclosed) customer engagements.
- **2025-11:** Vertiv publishes the third in a blog series on rack-level DC power, spotlighting the shipping PowerDirect Rack 33kW (PowerDirect 3000): 33 kW/1U, 132 kW/rack stacked, 97.5% peak efficiency, dual AC/800 VDC-class input, OCP ORV3 HPR compliant. ([Vertiv](https://www.vertiv.com/en-us/insights/articles/blog-posts/vertiv-powerdirect-rack-33kw--a-new-standard-in-modern-data-center-power/))
- **2025 (late):** Vertiv confirms its 800 VDC portfolio — centralized rectifiers, DC busways, rack-level DC-DC converters, DC-compatible backup — is planned for a 2026 release, timed to NVIDIA's Rubin Ultra rollout. ([PR Newswire](https://www.prnewswire.com/news-releases/vertiv-accelerates-ai-infrastructure-evolution-in-alignment-with-nvidia-800-vdc-power-architecture-announcement-302458599.html))
- **2025-05:** NVIDIA publishes its 800 VDC architecture initiative naming Vertiv (alongside Eaton and Schneider Electric) as a data center power systems partner; NVIDIA cites up to 5% end-to-end efficiency improvement, 45% copper reduction, and up to 30% TCO reduction from the industry-wide 800 VDC shift. NVIDIA demonstrates an 800V sidecar powering 576 Rubin Ultra GPUs in a Kyber rack at GTC 2025. ([NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/))

## Claim Verification

### Claim: PowerDirect 5000 sidecar delivers 400–900 kW over a busbar to a GPU rack
**Status:** Company-stated; product is in customer lab validation as of the source publication date (July 2026), with commercialization not yet begun

**Supporting:**
- The figure comes from Vertiv's own technical blog post describing the architecture, not a marketing one-liner, and includes specifics (busbar delivery, rack-adjacent placement) consistent with how NVIDIA's own Kyber sidecar reference design works
- Vertiv states engineering validation is "well advanced" with a named (but undisclosed) customer on their intended GPU rack, and that power conversion, IT, and power distribution are being validated together as one system

**Refuting / questioning:**
- No commercial shipments or third-party benchmarks exist yet; portfolio commercialization is targeted for H2 2026 with pilots continuing through 2027, so the 400–900 kW range is a design target rather than a field-proven figure
- "Several large-scale AI factory projects" cited as early adopters (per Vertiv's broader 800 VDC messaging) have not been named, making independent verification of real-world performance impossible at this stage

**Summary:** Technically consistent with the broader NVIDIA-led 800 VDC ecosystem and Vertiv's stated engineering progress, but unverified in commercial deployment — this is a pre-launch product spec, not a field-measured result.

### Claim: PowerDirect Rack (33kW/PowerDirect 3000) achieves 97.5% peak conversion efficiency
**Status:** Company-published product specification (Vertiv product catalog and blog)

**Supporting:**
- Figure appears consistently across both Vertiv's blog post and its official product catalog page for the PowerDirect 3000, suggesting it is a tested/rated specification rather than a one-off marketing claim
- 97%+ efficiency is broadly consistent with modern bulk AC-to-50VDC rectifier efficiency figures published by competing vendors (Eaton, Schneider Electric) for similar rack-power-shelf products

**Refuting / questioning:**
- "Peak" efficiency figures characteristically represent the best-case operating point (near-optimal load); Vertiv's own blog notes that traditional embedded server power supplies suffer efficiency loss at partial load due to N+1 redundancy — the same caveat likely applies at the low end of PowerDirect's loading range, though Vertiv claims parallel-shelf operation mitigates this
- No independent lab measurement has been published to confirm the 97.5% figure under real mixed-load conditions

**Summary:** Plausible and consistent with comparable industry products, but sourced entirely to Vertiv's own specification sheet — treat as a rated maximum rather than a guaranteed field efficiency.

### Claim: 800 VDC sidecar architecture "frees 8 to 16 rack units" of space for compute
**Status:** Company-stated; physically plausible given typical power-shelf rack-unit consumption, but the exact figure is Vertiv's own estimate

**Supporting:**
- Basic arithmetic supports the range: existing in-rack power shelves (including Vertiv's own PowerDirect Rack, at 1U per 33 kW) commonly occupy multiple rack units in dense configurations; moving that hardware to an external sidecar mechanically returns that space
- NVIDIA's own 800 VDC technical blog independently corroborates the underlying problem — describing up to 64U of rack space consumed by power shelves for a Kyber-class MW-scale rack under legacy 54 VDC distribution — which supports the directional claim even though the specific "8–16" figure is Vertiv's own

**Refuting / questioning:**
- The exact rack-unit savings will vary by GPU generation, rack density, and how much redundancy the operator's power design requires; "8 to 16" is presented as a range without a specific reference configuration
- Since the sidecar itself still requires floor space adjacent to the rack, the net facility-level space savings (not just intra-rack space) has not been quantified by Vertiv

**Summary:** Directionally well-supported by both Vertiv's and NVIDIA's own technical material, but the specific numeric range should be read as an estimate pending real deployment data.

## Sources

- [From rack to data hall: The practical path to 800 VDC — Vertiv](https://www.vertiv.com/en-us/insights/articles/blog-posts/from-rack-to-data-hall-the-practical-path-to-800-vdc/)
- [Vertiv™ PowerDirect Rack 33kW – A new standard in modern data center power — Vertiv](https://www.vertiv.com/en-us/insights/articles/blog-posts/vertiv-powerdirect-rack-33kw--a-new-standard-in-modern-data-center-power/)
- [Vertiv™ PowerDirect 3000 33kW — Product Catalog](https://www.vertiv.com/en-us/products-catalog/critical-power/dc-power-systems/powerdirect-3000-33kW/)
- [NVIDIA 800 VDC Architecture Will Power the Next Generation of AI Factories — NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- [Vertiv Accelerates AI Infrastructure Evolution in Alignment with NVIDIA 800 VDC Power Architecture Announcement — PR Newswire](https://www.prnewswire.com/news-releases/vertiv-accelerates-ai-infrastructure-evolution-in-alignment-with-nvidia-800-vdc-power-architecture-announcement-302458599.html)
