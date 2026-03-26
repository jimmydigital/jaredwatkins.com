---
title: "Submer ADA — Autonomous Datacenter Assistant"
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: "Submer's ADA robot automates server insertion and removal from single-phase immersion tanks. Revealed at OCP Summit October 2021; commercial release targeting Q3 2025. Addresses the core friction point of immersion-cooled datacenters: vertical lift for server servicing rather than horizontal rack-slide."
tags: ["datacenters", "robotics-automation", "immersion-cooling", "cooling"]
categories: ["product"]
research_area: "datacenters/robotics-automation"
source_urls:
  - "https://submer.com/videos/product-demos/ada-the-autonomous-datacenter-assistant/"
  - "https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-to-release-autonomous-robot/"
last_reviewed: 2026-03-24
stale_after_days: 90
related:
  - "datacenters/cooling/submer.md"
  - "datacenters/robotics-automation/_index.md"
  - "datacenters/cooling/_index.md"
---

## Summary

ADA (Autonomous Datacenter Assistant) is Submer's robotic platform for automating server installation and removal inside single-phase immersion cooling tanks. Submer revealed ADA at OCP Summit in October 2021; commercial availability was targeted for around Q3 2025. ADA directly addresses the key operational friction of immersion-cooled datacenters: unlike traditional air-cooled racks where servers slide in horizontally, immersion tank servers must be lifted out vertically — a physically demanding task that requires PPE (to handle dielectric fluid) and, at scale, some form of mechanical lifting assistance. ADA replaces the crane or manual jig currently used for this with an autonomous robotic system that can also perform environmental monitoring, commissioning, and decommissioning. ADA represents the "build robots for existing infrastructure" philosophy — robots adapted to the physical realities of tanks — as distinct from SoftBank's approach of redesigning the infrastructure for robots (see `softbank-robot-rack.md`). The two approaches are not directly competitive since they target different cooling architectures.

## Key Facts

- **Product:** ADA — Autonomous Datacenter Assistant
- **Developer:** Submer Technologies (Barcelona, Spain)
- **First revealed:** October 2021, OCP Global Summit 21 (via Submer Labs R&D unit)
- **Commercial target:** ~Q3 2025 (as stated in a 2025 Data Center Dynamics report; exact status unconfirmed as of this writing)
- **Primary function:** Automated vertical lift for inserting and removing servers from single-phase immersion cooling tanks
- **Secondary functions:** Environmental monitoring inside tanks; commissioning and decommissioning workflows; human-robot collaborative operation
- **Coolant compatibility:** Designed for Submer SmartCoolant (proprietary single-phase dielectric fluid); likely compatible with similar low-viscosity single-phase fluids
- **Fleet coordination:** Stated to support collaborative environments with other robots and humans; over-the-air software updates
- **Status (Q1 2026):** Pre-commercial / late development; no independent third-party deployment report confirmed as of last review

## What It Is / How It Works

Immersion cooling tanks submerge servers in a bath of dielectric fluid — a liquid that conducts heat but not electricity. In Submer's single-phase system, the fluid is SmartCoolant, a proprietary biodegradable synthetic. Servers are positioned inside a tank horizontally (lying flat in a bath), but must be lifted vertically out of the fluid to be serviced, replaced, or decommissioned.

At small scale this is done manually with PPE and care; at AI datacenter scale (tanks handling 100 kW+ of compute density), servicing frequency and tank depth make manual lifting impractical and physically demanding. Submer currently offers a crane option, but a crane requires overhead clearance and trained operation.

ADA's design addresses this with a purpose-built robotic "crash cart" — a mobile robotic arm or gantry system that can:

1. **Navigate to a specific tank** within the datacenter floor
2. **Identify the target server** using onboard sensors
3. **Engage the server** and perform a controlled vertical lift out of the fluid bath
4. **Hold the server** for inspection, replacement, or relocation
5. **Reinsert the server** (or a replacement unit) back into the designated tank slot
6. **Monitor tank conditions** (fluid temperature, fluid level, particle contamination indicators) during the operation

The fluid management aspect is significant: lifting a server from a tank causes dielectric fluid to drain off the hardware. ADA is designed to manage this process — minimizing fluid loss and contamination — rather than requiring a human technician to handle fluid-wet hardware.

ADA was developed through Submer Labs, Submer's internal R&D program, which the company uses to prototype hardware and software beyond its core tank and coolant product line.

**Design tension with robot-friendly rack approaches:** ADA exists because immersion tanks are inherently difficult to robotically service. The alternative philosophy (SoftBank's cable-less rack) avoids the immersion complexity entirely by keeping servers in standard rack form factors with blind-mate connections — but sacrifices the PUE and cooling density advantages of immersion. As AI accelerator power density increases past ~100 kW/rack, direct-to-chip or immersion approaches become thermodynamically necessary, making ADA-type solutions more relevant at the highest density tier.

## Notable Developments

- **2025 (~Q3):** Submer targets commercial release of ADA robot; described by Data Center Dynamics as a "robotic crash cart." Exact launch status unconfirmed as of Q1 2026. ([Data Center Dynamics](https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-to-release-autonomous-robot/))
- **2021-10:** ADA unveiled at OCP Global Summit 21 as Submer Labs concept; demonstrated vertical lift capability for immersion tank server servicing. ([Submer / X (formerly Twitter)](https://x.com/submertech/status/1458404816095428617))

## Key People

No individuals specifically associated with ADA's engineering or product development have been named publicly. Product development sits within the Submer Labs R&D unit. See `submer.md` for Submer's company leadership including CEO Patrick Smets and co-founders Daniel Pope and Pol Valls Soler.

### People — Last Reviewed: 2026-03-24

## Supply Chain Position

ADA is a finished robotic product from Submer. Its upstream components (robotic arms, actuators, sensors, computer vision hardware) are not disclosed. As a pre-commercial product, supply chain details are not yet meaningful to document.

**⚑ Immersion vs. robot-servicing design incompatibility:** ADA is Submer's own solution to the immersion tank servicing problem — the same design tension flagged in `cooling/_index.md`. SoftBank-style cable-less rack designs solve the robot servicing problem at the cost of immersion cooling advantages. ADA attempts to solve the robot servicing problem while preserving immersion cooling. These two approaches will likely coexist in different deployment contexts: ADA for ultra-high-density AI compute (where immersion is thermodynamically necessary), cable-less racks for moderate density workloads where air or direct-to-chip cooling is sufficient.

## Claim Verification

### Claim: ADA can "autonomously" insert and remove servers from immersion tanks
**Status:** Demonstrated in concept (OCP Summit 2021 demonstration); commercial readiness not independently confirmed

**Supporting:**
- OCP Summit demonstration shows a working prototype performing vertical lift
- Submer has continued to reference ADA as an active product development program through 2025
- The mechanical task (controlled vertical lift with fluid management) is simpler than the cable-routing tasks required in traditional rack automation — ADA's design has a narrower scope

**Refuting / questioning:**
- Four years elapsed between the OCP Summit 2021 reveal and the Q3 2025 commercial target — longer than typical product development timelines suggest
- "Autonomous" in datacenter robotics is on a spectrum; whether ADA operates fully autonomously (no human oversight per operation) or semi-autonomously (human authorizes each lift) is not specified in public materials
- No customer deployment case study has been published; commercial adoption is unverified

**Summary:** ADA is a real development program addressing a real operational problem. The concept is sound and the demonstration was functional. The timeline slippage from 2021 to 2025 reflects the difficulty of building reliable industrial robotics for wet environments. Commercial status as of Q1 2026 should be re-verified directly with Submer.

## Sources

- [ADA: The Autonomous Datacenter Assistant — Submer Labs (product page)](https://submer.com/videos/product-demos/ada-the-autonomous-datacenter-assistant/)
- [Immersion Cooling Firm Submer to Release Autonomous Robot — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-to-release-autonomous-robot/)
- [Submer unveils ADA at OCP Summit 21 — Submer on X (Oct 2021)](https://x.com/submertech/status/1458404816095428617)
