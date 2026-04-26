---
title: "Neousys Technology"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "Taiwan-based rugged embedded computer manufacturer (Advantech subsidiary); SEMIL-2200 and SEMIL-2200GC semi-industrial fanless AI edge servers; wide-temperature GPU inference platforms for transportation, defense, and industrial AI; NVIDIA Jetson and discrete GPU integration."
tags: ["rugged", "edge-compute", "ai-inference", "industrial", "taiwan", "private", "fanless", "gpu-edge"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://www.neousys-tech.com/"
  - "https://www.neousys-tech.com/en/product/application/edge-ai-server"
last_reviewed: 2026-04-25
stale_after_days: 180
---

## Summary

Neousys Technology is a Taiwan-based manufacturer of rugged embedded computers and edge AI inference platforms, operating as a subsidiary of Advantech, the global industrial computing giant. Neousys builds fanless, wide-temperature compute systems that target transportation, surveillance, energy, defense-adjacent, and industrial AI applications where commercial servers cannot survive the environment and VPX military-grade systems are over-engineered and over-priced. The SEMIL-2200 and SEMIL-2200GC Series are Neousys's semi-industrial (fanless, vibration-resistant) AI edge server platforms targeting outdoor and vehicle-side deployments, offering discrete NVIDIA GPU inference in an IP54 or IP65-rated enclosure without fans or other moving parts.

## Key Facts

- **Founded:** 2010
- **HQ:** New Taipei City, Taiwan
- **Parent:** Advantech Co., Ltd. (TWSE: 2395) — acquired Neousys in 2018; Advantech is a major global industrial computing vendor (~$2B annual revenue)
- **Value chain position:** Rugged system integrator and OEM — designs and manufactures embedded compute platforms for integration into customer systems
- **Platform tier:** System/appliance tier — complete fanless edge servers sold to OEMs, integrators, and end users
- **Key certifications:** EN 50155 (railway), E-Mark (automotive/vehicle), MIL-STD-810G (certain models), CE, FCC; IP54/IP65 ingress protection
- **Primary markets:** Transportation (railway, autonomous vehicles), surveillance/ITS, defense-adjacent, energy infrastructure, industrial automation

## Key Products

### SEMIL-2200 Series — Semi-Industrial Fanless AI Edge Server

The SEMIL-2200 is a fanless, semi-industrial AI edge server designed for applications requiring GPU inference in environments unsuitable for fan-cooled commercial hardware — outdoor kiosks, roadside intelligent transportation systems (ITS), vehicle-side deployments, and lightly ruggedized industrial sites. "Semi-industrial" denotes a middle tier between consumer/commercial and full military-grade: dust and splash protection (IP54), wide operating temperature range (-25°C to +60°C or similar), and vibration/shock resistance beyond commercial spec, but not full MIL-STD-810 qualification.

Key specifications:
- **Form factor:** Fanless desktop/wallmount enclosure; rugged aluminum construction
- **Processors:** Intel Core or Xeon E series (generation-dependent)
- **GPU:** NVIDIA discrete GPU (RTX series; specific SKUs vary); full-height/full-length PCIe GPU slot with external power
- **Cooling:** Passive fanless — thermal dissipation through chassis heatsink structure; no moving parts
- **Operating temperature:** Wide-temperature range (varies by SKU; typically -25°C to +60°C)
- **Ingress protection:** IP54 (dust-protected, splash-resistant)
- **Expansion:** PCIe x16 GPU slot; additional PCIe expansion; GbE and optional 10GbE; USB; serial I/O
- **Storage:** M.2 NVMe + 2.5" SATA SSD; no optical drives
- **Use cases:** Roadside AI inference (ITS), outdoor surveillance analytics, transit AI (bus depots, terminals), industrial AI inspection

### SEMIL-2200GC — GPU Compute Variant

The SEMIL-2200GC is the GPU compute-optimized variant of the SEMIL-2200 line, specifically designed to support higher-TDP NVIDIA GPUs (such as RTX 4000/5000-class cards) that exceed the passive thermal budget of the base SEMIL-2200 chassis. The GC variant adds enhanced thermal dissipation structures or limited forced-air supplementation while maintaining the semi-industrial environmental profile. It targets applications requiring more GPU inference throughput — multiple simultaneous HD/4K video analytics streams, real-time object detection and tracking, or inference on larger transformer models — in an IP54 or better enclosure.

Key specifications:
- **GPU:** Higher-TDP NVIDIA GPU than base SEMIL-2200 (e.g., NVIDIA RTX 4070/4090 or data center GPU in select configs)
- **Cooling:** Enhanced passive + optional supplemental cooling; still no external fan exposure
- **TDP budget:** Higher thermal headroom than base SEMIL-2200
- **Use cases:** Multi-camera AI analytics (8–32 camera streams), autonomous vehicle compute offload, edge AI training and fine-tuning, high-throughput inspection

## What It Is / How It Works

Neousys platforms occupy a specific niche between the commodity commercial mini-PC market and the full MIL-spec defense market. The core engineering challenge they solve is thermal management of GPU workloads without fans in environments where fans would fail (dust ingestion, condensation, vibration) or are prohibited (EMI concerns, noise requirements, maintenance minimization).

The fanless design approach uses the chassis as a giant heatsink: aluminum fins, heat pipes, and internal thermal mass conduct GPU and CPU heat to the outer surface, which radiates and convects it to ambient air. This requires custom chassis geometry designed around the specific GPU and CPU TDP — a SEMIL-2200 with an NVIDIA RTX 4070 has a different fin geometry and thermal path than one with an RTX 3060. The constraint is that GPU TDP is bounded by what the chassis thermal structure can dissipate without fans; this is why the GC variant exists — higher-TDP GPUs require more aggressive passive thermal engineering.

**Advantech parentage** matters for two reasons. First, Neousys gets access to Advantech's global distribution channels, component supply relationships, and certifications infrastructure — a startup trying to earn EN 50155 (railway), E-Mark (vehicle), and MIL-STD-810G certifications independently would face years of testing cost and delay. Second, Neousys's products can be bundled into Advantech's broader industrial computing ecosystem, including Advantech's software stacks and management platforms.

**Market position:** Neousys serves OEM customers (companies that integrate Neousys hardware into their own solutions) and direct end users. Typical OEM customers are ITS integrators, smart surveillance vendors, autonomous vehicle platform builders, and defense system integrators who need a certified rugged AI edge server but don't want to build their own. The price point (~$3,000–$12,000 for a SEMIL-class system) is accessible compared to full MIL-spec defense compute ($20,000–$100,000+), making Neousys platforms viable for commercial deployments at scale.

## Market Context

Neousys competes in the semi-industrial edge compute market with peers including Premio (San Jose, CA), ADLINK Technology (also Advantech ecosystem-adjacent), Cincoze, Vecow, and Axiomtek — all Taiwan-based or Taiwan-heritage embedded compute vendors targeting similar markets. The competitive differentiators are GPU TDP handling, operating temperature range, certifications, and PCIe lane count for GPU expansion.

The defense-adjacent demand driver is military's increasing use of commercial or semi-commercial compute platforms for training aids, simulation systems, intelligence analysis workstations, and non-deployed (base/post) AI applications where full MIL-STD-810 is not required. A SEMIL-class Neousys system is often cost-effective for these use cases versus a full Crystal Group or Mercury Systems platform.

## Notable Developments

- **2018:** Acquired by Advantech, becoming part of the largest global industrial computing group; access to global channels and certifications
- **Ongoing:** SEMIL-2200GC platform targets the growing demand for high-TDP GPU inference (RTX 4000/5000 class) in fanless semi-industrial enclosures
- **Ongoing:** DFI Technology is another Taiwan-based peer in this segment; Neousys and DFI have overlapping product categories but distinct customer profiles (Neousys is stronger in transportation/ITS; DFI stronger in gaming/kiosk/industrial display integration)
- **Trend:** Adoption of NVIDIA Jetson Orin-based systems for lower-power fanless AI edge applications (surveillance, robotics); Neousys's POC-400/500 Jetson Orin series addresses this below the SEMIL tier

## Sources

- [Neousys Technology — Official Website](https://www.neousys-tech.com/)
- [Neousys Technology — Edge AI Servers](https://www.neousys-tech.com/en/product/application/edge-ai-server)
- [Advantech Co., Ltd.](https://www.advantech.com/) — parent company
- [Advantech TWSE: 2395](https://finance.yahoo.com/quote/2395.TW/) — public parent; Neousys itself is not separately listed
