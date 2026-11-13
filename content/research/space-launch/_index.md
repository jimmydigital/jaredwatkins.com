---
title: "Space Launch"
date: 2026-08-13
lastmod: 2026-09-07
draft: false
description: "Orbital launch vehicles, lunar landers, and in-space orbital transfer vehicles — the companies building the hardware that gets payloads from the ground to orbit, the Moon, and beyond."
research_area: "space-launch"
last_reviewed: 2026-09-07
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

{{<steering>}}

## Space Launch — Steering Instructions

**Scope boundaries:** IN — orbital launch vehicle developers, lunar lander developers, and in-space orbital transfer ("space tug") vehicle developers; the companies building and operating this hardware. OUT — planetary-exploration mechanisms/tools suppliers and autonomous orbital defense spacecraft (see [Robotics → Space Robotics]({{< relref "../robotics/space-robotics/_index.md" >}})); satellites purpose-built as orbital data centers (see [Datacenters → Orbital Compute]({{< relref "../datacenters/orbital-compute/_index.md" >}})); stratospheric (non-orbital) platforms (see [HALE / HAPS]({{< relref "../hale-haps/_index.md" >}})); pure satellite-constellation operators with no launch-vehicle or lander hardware of their own. BORDERLINE — a launch/lander company that acquires or builds a notable non-launch product line (e.g., a missile-warning sensor subsidiary, a planetary rover): document the parent here, and cross-link to a full entry elsewhere if the product line's primary business fits another section's scope better (e.g., SciTec is filed under Drone Detection because its core business is missile warning/ISR, not launch).

**Editorial framing:** Per the site's general startup-first priority, standalone entries for large, publicly traded launch companies should only be created when there is a genuinely novel, specific angle to document (a first-of-its-kind mission milestone, a notable acquisition, a distinctive vehicle architecture) — not simply because the company is a known player. Commercial lunar landing is a very new capability (first fully successful commercial soft landing was 2025) and merits close tracking regardless of company size for that reason alone.

**Claim verification flags specific to this topic area:** "Fully successful" landing/mission claims should be checked against the specific failure modes of prior attempts in the same class (e.g., a lander that touches down but tips over, as Intuitive Machines' IM-1 did in February 2024, is a partial success, not a full one — verify which category a given mission claim falls into). Payload-capacity claims (kg to LEO/GTO) for vehicles that have not yet flown are design targets, not flight-demonstrated figures — always check flight-heritage status before citing a capacity number as achieved rather than targeted. National-security launch program claims (NSSL Lane 1/Lane 2, "Golden Dome"-related contracts) should be checked against the relevant Space Force Space Systems Command announcement or SAM.gov/USASpending.gov record where possible, since program ceilings and individual task-order awards are frequently conflated in company press materials.

**Review cadence:** 90 days — fast-moving segment with frequent launch attempts, contract awards, and (for younger companies) failure/anomaly events that materially change the risk picture.

{{</steering>}}

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

This section tracks companies that design, build, and operate orbital launch vehicles, lunar landers, and in-space orbital transfer ("space tug") vehicles — the physical hardware layer that moves payloads from the ground to low Earth orbit, geosynchronous orbit, cislunar space, and the lunar surface. It is distinct from three adjacent sections that are easy to confuse with it: [Robotics → Space Robotics]({{< relref "../robotics/space-robotics/_index.md" >}}) covers planetary-exploration mechanisms/tools suppliers and autonomous orbital defense spacecraft (not launch vehicles or landers); [Datacenters → Orbital Compute]({{< relref "../datacenters/orbital-compute/_index.md" >}}) covers satellites purpose-built as data centers, not the rockets that launch them; [HALE / HAPS]({{< relref "../hale-haps/_index.md" >}}) covers stratospheric (not orbital) platforms. A launch vehicle or lander company that also builds a notable non-launch product (e.g., a lunar rover, a missile-warning sensor subsidiary) is documented here with cross-links out to the entry covering that specific product line where one exists.

## Key Themes

- **Commercial lunar delivery is now a real, if young, market.** NASA's Commercial Lunar Payload Services (CLPS) program has produced the first fully successful commercial soft Moon landings (2025), turning what was purely a national-agency capability into a service multiple private companies sell.
- **Small-lift launch vehicles are consolidating upward.** Several small-lift launch vehicle developers (Firefly's Alpha, Rocket Lab's Electron) are developing or have developed medium-lift successors (Eclipse, Neutron) to compete for larger national-security and constellation-deployment contracts, rather than staying in the small-payload niche where they started.
- **National security launch demand (NSSL Phase 3 Lane 1, Golden Dome-related programs) is a major growth driver** for US launch vehicle developers in 2025–2026, alongside NASA science/exploration contracts and commercial constellation deployment.
- **Vertical integration is common and often defense-driven.** Companies in this section increasingly acquire or build in-house capabilities adjacent to their core launch/lander business — sensing and software (national-security), vision/autonomy navigation, and mechanisms/robotics — rather than relying solely on outside suppliers.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Blue Origin](https://www.blueorigin.com) | Kent, WA | Private ($130B valuation, Jul 2026 round) | Suborbital (New Shepard) and orbital heavy-lift (New Glenn) launch vehicles, Blue Moon lunar landers, Blue Ring orbital tug, and the BE-4/BE-3U/BE-7 engine family; also developing the TeraWave satellite-broadband constellation. |

<!-- TODO: add other pre-IPO/private launch and lander companies (e.g., Stoke Space, Relativity Space, ABL Space Systems, Intuitive Machines if still applicable, ispace) as dedicated entries are researched -->

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [FLY](https://finance.yahoo.com/quote/FLY) | [Firefly Aerospace](https://fireflyspace.com) | Small-to-medium-lift launch vehicles (Alpha, Eclipse), lunar landers (Blue Ghost), and orbital transfer vehicles (Elytra); first commercial company to achieve a fully successful Moon landing (Mar 2025). |

*Fewer than two public companies are currently documented in this section, so the TradingView market-overview widget is omitted per section convention; add it once a second public company entry exists.*

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [NOC](https://finance.yahoo.com/quote/NOC) | [Northrop Grumman](https://www.northropgrumman.com) | Co-developing the Eclipse medium launch vehicle with Firefly Aerospace ($50M investment, May 2025); contributes Antares flight heritage and avionics. |

<!-- TODO: add SpaceX, ULA as dedicated incumbent context entries if a notable, specific angle emerges; SpaceX's orbital-compute initiative is already documented in datacenters/orbital-compute -->

## Supply Chain

| Layer | Key Inputs | Known Companies | Geographic Concentration |
|-------|-----------|------------------|---------------------------|
| Structures | Carbon-fiber composite materials, aluminum-lithium alloys for tanks and airframes | In-house at [Firefly Aerospace]({{< relref "firefly-aerospace.md" >}}) (automated fiber placement, 7-axis robotic powermill at its Briggs, TX "Rocket Ranch") | Not independently documented in this review; flag for future update |
| Propulsion | Liquid rocket engines (tap-off cycle architecture), turbopumps, propellant | In-house at Firefly (Reaver/Lightning engines on Alpha; scaled-up Miranda/Vira engines on Eclipse) | — |
| Avionics / autonomy | Flight avionics, vision-based navigation and autonomous guidance software | Firefly (in-house avionics; acquired Space-ng for vision navigation, 2026); NVIDIA (Jetson edge-compute module for Firefly's Ocula lunar imaging service) | — |
| Mission software / national-security sensing | ISR data fusion, missile-warning, space domain awareness software | [SciTec]({{< relref "../drone-detection/hardware/scitec.md" >}}) (acquired by Firefly Aerospace, ~$855M, closed Nov 2025) | — |
| Mechanisms / robotic payloads | Planetary rovers, robotic arms, drills for lander payloads | [Honeybee Robotics]({{< relref "../robotics/space-robotics/honeybee-robotics.md" >}}) ([Blue Origin]({{< relref "blue-origin.md" >}}) subsidiary) supplying the lunar rover for Firefly's Gruithuisen Domes mission | — |
| Launch site infrastructure | Launch pads, range services, payload processing facilities | Vandenberg Space Force Base (CA), Wallops Island / Mid-Atlantic Regional Spaceport (VA), Cape Canaveral Space Force Station (FL), Esrange Space Center (Sweden, with Swedish Space Corporation) | US government-owned ranges for domestic sites; Esrange is Firefly's first European launch site |
| End customers | NASA (CLPS, JPL science missions), US Space Force / Space Systems Command, defense primes | NASA, US Space Force, Lockheed Martin (multi-launch agreement through 2031), Air Force Research Laboratory | — |

**⚑ Shared partner note:** [Honeybee Robotics]({{< relref "../robotics/space-robotics/honeybee-robotics.md" >}}) (a subsidiary of [Blue Origin]({{< relref "blue-origin.md" >}})) supplies hardware to Firefly Aerospace despite Blue Origin being a competing launch/lander developer — a reminder that supplier relationships in this sector routinely cross competitive lines. [SciTec]({{< relref "../drone-detection/hardware/scitec.md" >}}) is documented in Drone Detection (its primary business is missile warning/ISR, not drones) but is a wholly owned Firefly subsidiary as of November 2025 — see that entry for SciTec-specific detail.

### Supply Chain — Last Reviewed: 2026-09-07
