---
title: "Anduril Industries"
date: 2026-03-25
lastmod: 2026-03-26
draft: false
description: "Costa Mesa, CA defense technology prime (private, ~$28–30B valuation, Series G); Lattice OS autonomous C2 software platform; Menace-T/X rugged edge C4 systems built on Klas Voyager compute; $20B US Army Lattice enterprise contract (March 2026, 10-year term); Golden Dome missile defense software (with Palantir); ExoAnalytic Solutions acquisition (March 2026); ~$6.84B total funding."
tags: ["rugged", "edge-compute", "ai-inference", "defense", "us", "private", "autonomous-systems", "c2"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://www.anduril.com/"
  - "https://www.anduril.com/article/army-lattice-enterprise-contract/"
last_reviewed: 2026-03-26
stale_after_days: 90
---

## Summary

Anduril Industries is the most significant new entrant to the defense prime market in a generation — a pure software/AI-first defense company that builds complete autonomous weapon and sensor systems, with Lattice OS as the AI command-and-control software layer running across its platforms. In the context of this research section, Anduril is relevant primarily through its Menace-T and Menace-X tactical edge C4 systems, which are the highest-integration-level rugged compute offerings in this section: not bare compute modules (Mercury, Curtiss-Wright) or compute servers (OSS), but complete deployable C4 systems with compute, networking, and AI software in a package deployable by a single operator. The $20B US Army enterprise contract awarded March 2026 for Lattice as the Army's open AI battlefield network is the single largest signal of where DoD AI-at-the-edge investment is heading. Anduril's March 2026 acquisition of ExoAnalytic Solutions extends Lattice's sensor fusion reach to space domain awareness.

## Key Facts

- **Founded:** 2017
- **HQ:** Costa Mesa, CA (Orange County)
- **Status:** Private; total funding ~$6.84B (through Series G)
- **Valuation:** ~$28–30B post-Series G (June 2025); reported $4B fundraise targeting $60B valuation (March 2026, Andreessen Horowitz and Thrive Capital leading)
- **CEO:** Brian Schimpf (Co-Founder)
- **Founder / CTO:** Palmer Luckey (Co-Founder; previously founder of Oculus VR, sold to Meta 2014)
- **Employees:** ~2,200+ globally
- **Value chain position:** Defense prime — builds complete autonomous systems, AI-enabled weapons platforms, and C2 software; sells directly to DoD and allied governments; vertically integrated from rugged compute hardware (Klas Voyager) to software (Lattice OS) to airframe/munition manufacturing
- **Flagship software:** Lattice OS — AI-powered command-and-control platform fusing sensor data from drones, radars, and satellites into a shared operational picture; open-architecture SDK for third-party integration
- **Key rugged compute products:**
  - Menace-T: Two-case C4 system deployable by single operator; runs Lattice Mesh on Klas Voyager ruggedized compute and networking hardware; supports third-party software including Palantir's Edge
  - Menace-X: Vehicle-mounted expeditionary C4 predecessor to Menace-T; higher weight/power for command post environments
- **Klas Voyager:** Ruggedized compute and networking hardware (acquired ~2025) — the underlying hardware backbone for Menace-T and Menace-X
- **Major contract:** $20B US Army enterprise contract to deploy Lattice as the AI-driven open-architecture battlefield network; awarded March 13–14, 2026; 10-year term; awarded at Aberdeen Proving Ground
- **Other programs:** US Space Force surveillance network (Lattice, 2024); Golden Dome missile defense software (with Palantir, 2026); USSOCOM; multiple allied Ministry of Defence contracts
- **Manufacturing:** $1B manufacturing facility in Pickaway County, Ohio (announced January 2025) for aerial and maritime drones; first new US solid rocket motor production facility in 50 years operational August 2025

## What It Is / How It Works

Anduril is structurally different from every other company in this section. Mercury, OSS, and Curtiss-Wright are component and subsystem suppliers — they make the rugged compute building blocks that defense primes integrate into platforms. Anduril is itself a defense prime: it builds complete autonomous weapon and sensor systems from the ground up, with Lattice OS as the differentiating software layer.

**Lattice OS / Lattice Mesh** is the software core. It ingests data from heterogeneous sensors — Anduril's own drones, third-party radars, satellite feeds, space surveillance systems — and processes it through AI/ML algorithms to produce a fused 3D common operating picture. Lattice then supports autonomous decision-making: identifying and classifying threats, prioritizing targets, and coordinating responses across a network of autonomous systems. The $20B Army enterprise contract positions Lattice as an open-architecture AI backbone for the Army battlefield network — other vendors can interoperate through Lattice's SDK, which means Anduril is building toward an OS-layer monopoly analogous to how commercial cloud platforms captured developer ecosystems.

**Menace-T** (launched May 2025) is the product most directly relevant to this research section: a two-case C4 system deployable by a single operator in minutes. It runs Lattice Mesh software on Klas Voyager ruggedized compute and networking hardware. Anduril acquired Klas specifically to control this hardware layer rather than depending on a third-party supplier. Menace-T can run third-party software stacks including Palantir's Edge — making it a general-purpose tactical edge compute platform, not just an Anduril-only node. Edge AI inference for sensor processing, threat classification, and communications management are core use cases.

**Menace-X** is the vehicle-mounted C4 predecessor: a heavier expeditionary system designed for commanders operating in denied, disrupted, or intermittent communications (DDIL) environments. Menace-T is the man-portable, individual-operator version.

**Vertical integration strategy:** By acquiring Klas (ruggedized compute), building its own SRM production, and owning airframe manufacturing (Ohio facility), Anduril is systematically removing external suppliers from its value chain. This is strategically opposite to Mercury, OSS, and Curtiss-Wright, who depend on DoD primes choosing their components. Anduril competes for the entire program, not just the compute component.

## Notable Developments

- **2026-03:** ExoAnalytic Solutions acquisition — space domain awareness company; extends Lattice's sensor fusion to satellite tracking and space situational awareness
- **2026-03:** $20B US Army Lattice enterprise contract awarded (Aberdeen Proving Ground, 10-year term) — positions Lattice as open AI backbone for Army-wide C2
- **2026-03:** Anduril and Palantir reported as software developers for Golden Dome missile defense system ($185B program); with Aalyria, Scale AI, and Swoop Technologies
- **2026-03:** Reported $4B fundraise targeting $60B valuation (Andreessen Horowitz, Thrive Capital)
- **2025-08:** First new US solid rocket motor production facility in 50 years operational
- **2025-06:** $2.5B Series G funding (Founders Fund leading)
- **2025-05:** Menace-T launched — compact two-case C4 system for single-operator tactical edge deployment; built on Klas Voyager hardware
- **2025-05:** Anduril Menace systems become preferred hardware for Palantir's Edge software
- **2025-01:** $1B Ohio manufacturing facility announced for aerial and maritime drones
- **2024-12:** Japan operations launched for local manufacturing and supply chain partnerships
- **2024:** US Space Force selected Lattice for surveillance network operations

## Key People

**Brian Schimpf** — Co-Founder & CEO
- LinkedIn: [linkedin.com/in/bschimpf](https://www.linkedin.com/in/bschimpf/)
- Education: Not publicly documented
- Prior employment (reverse-chronological):
  - Anduril Industries: Co-Founder & CEO (2017–present)
  - Palantir Technologies: Senior engineer/leadership role — core team member before founding Anduril

**Palmer Luckey** — Co-Founder & CTO
- LinkedIn: [linkedin.com/in/palmer-luckey-21a16959](https://www.linkedin.com/in/palmer-luckey-21a16959/)
- Education: Self-taught; California State University Long Beach (partial enrollment)
- Prior employment (reverse-chronological):
  - Anduril Industries: Co-Founder & CTO (2017–present)
  - Facebook / Meta: VP of VR (2014–2017) — post-Oculus acquisition; departed 2017
  - Oculus VR: Founder (2012–2014) — created Oculus Rift VR headset; sold to Facebook for ~$2B (2014)

**Trae Stephens** — Co-Founder & Executive Chairman
- LinkedIn: [linkedin.com/in/trae-stephens-485a811](https://www.linkedin.com/in/trae-stephens-485a811/)
- Prior employment (reverse-chronological):
  - Anduril Industries: Co-Founder & Executive Chairman (2017–present)
  - Founders Fund: Partner (2016–present) — primary investor role; Founders Fund is Anduril's lead investor
  - Palantir Technologies: Business development and government affairs roles

**Christian Brose** — President & Chief Strategy Officer
- LinkedIn: [linkedin.com/in/christian-brose-50b026ab](https://www.linkedin.com/in/christian-brose-50b026ab/)
- Prior employment (reverse-chronological):
  - Anduril Industries: President & CSO (joined ~2019)
  - US Senate Armed Services Committee: Staff Director (under Senator John McCain) — shaped US defense modernization policy; authored "The Kill Chain" (2020), articulating the DoD's need for AI-enabled networked warfare — the intellectual framework Anduril is executing against
  - US Department of State: Policy roles
- **⚑ Overlap:** Christian Brose's "The Kill Chain" thesis — that the US must shift from expensive exquisite platforms to AI-networked affordable autonomous systems — is the policy foundation for Anduril's $20B Army Lattice contract. Brose is both an architect of the policy and the commercial beneficiary executing against it.

**Matt Grimm** — Co-Founder & COO
- LinkedIn: not found
- Prior: Palantir Technologies (early team)

**Babak Siavoshy** — CFO
- LinkedIn: not found
- Details not publicly documented

### People — Last Reviewed: 2026-03-26

## Claim Verification

### Claim: $20B Army contract makes Lattice the DoD-wide AI battlefield network

**Status:** Partially accurate — contract is real; framing is oversimplified

**Supporting sources:**
- [US Army / DoD announcements (March 13–14, 2026)](https://www.anduril.com/article/army-lattice-enterprise-contract/) — Army enterprise contract awarded to Anduril for Lattice; confirmed at Aberdeen Proving Ground
- [Anduril press release](https://www.anduril.com/) — details open-architecture nature and 10-year term

**Refuting / questioning sources:**
- "Enterprise contract" means a procurement vehicle that enables task orders, not a guaranteed $20B payment — actual spend depends on program execution, congressional appropriations, and task order awards over 10 years
- "Open architecture" framing means other vendors can interoperate with Lattice; Anduril is not the sole platform for all Army AI; the contract creates Lattice as a preferred platform, not a mandated monopoly
- No independent DoD budget document confirming the full $20B commitment found; ceiling value versus obligated value distinction is important

**Summary:** The Army enterprise contract is real, significant, and positions Lattice as the Army's preferred open-architecture AI C2 platform. The $20B ceiling is the maximum contract value over 10 years, not a guaranteed payout; actual spend will depend on appropriations and program execution. Treating Lattice as the de facto Army AI network is directionally accurate but overstated as a certain outcome.

### Claim: First new US solid rocket motor production facility in 50 years

**Status:** Reported as accurate (August 2025)

**Supporting sources:**
- Multiple US defense publications reported this as accurate at the August 2025 facility opening; the US SRM industrial base has been a documented DoD concern with only Northrop Grumman and L3Harris as prior producers

**Refuting / questioning sources:**
- "First in 50 years" framing has not been independently verified against the full history of US SRM production facilities; there may be smaller-scale SRM production not counted in this claim; framing may reflect production scale rather than absolute first-ever

**Summary:** Broadly accurate based on defense publication reporting and DoD concerns about SRM industrial base concentration; specific "50 years" framing should be verified against DoD industrial base assessments before citing.

### Claim: ExoAnalytic Solutions acquisition extends Lattice to space domain awareness

**Status:** Verified (March 2026)

**Supporting sources:**
- Multiple defense technology publications confirmed the ExoAnalytic Solutions acquisition in March 2026; ExoAnalytic operates a commercial network of optical telescopes for satellite tracking

**Summary:** Acquisition confirmed; strategic logic is coherent — ExoAnalytic's satellite tracking data integrates with Lattice's multi-domain sensor fusion architecture, extending Lattice's common operating picture from ground/air domains to space.

## Sources

- [Anduril Industries — Official Website](https://www.anduril.com/)
- [Anduril — Army Lattice Enterprise Contract](https://www.anduril.com/article/army-lattice-enterprise-contract/)
- [Klas Government — Voyager Tactical Edge Compute](https://www.klasgov.com/) — hardware backbone for Menace-T/X
- [Palantir — Edge Software / Menace Integration](https://www.palantir.com/platforms/apollo/) — software partner context
- Christian Brose, "The Kill Chain" (2020) — policy framework context for Lattice strategy
- [NVIDIA Jetson Orin — Embedded AI Platform](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/) — edge inference silicon used in Anduril autonomous systems
