---
title: Antennas
date: 2026-07-15
lastmod: 2026-07-15
draft: false
description: Directional and auto-tracking antenna systems for long-range drone command-and-control and video/data links — the ground-station and airborne antenna hardware layer distinct from the radio modules it carries.
research_area: "robotics/antennas"
last_reviewed: 2026-07-15
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

Long-range drone command-and-control and video/data links depend on directional antenna hardware — often mounted on an automatic tracking positioner that keeps a high-gain beam pointed at a moving aircraft — to achieve range and reliability well beyond what a fixed omnidirectional antenna can provide. This subsection covers the antenna and tracking-positioner hardware layer specifically, distinct from the [Communications]({{< relref "../communications/_index.md" >}}) section's coverage of the radio modules and waveforms those antennas carry, and distinct from [Flight Controllers / Autopilot Hardware]({{< relref "../flight-controllers/_index.md" >}}), which covers the onboard computer rather than the RF link hardware.

## Key Themes

- Auto-tracking ground antennas (mechanically steered high-gain directional antennas that follow the aircraft) are what extend practical UAS command-and-control range from tens of kilometers to 60+ km, and are a distinct hardware category from the radio/waveform layer that rides on top of them.
- Radio-agnostic tracking antenna platforms — supporting COFDM, OFDM, CDL, and MIMO/MANET waveforms interchangeably — are a deliberate design choice among defense-market suppliers, letting customers swap radio modules without replacing the antenna and tracking mechanism.
- Both named companies in this entry emphasize operation in GPS-denied and RF-contested (jamming) environments as a core design requirement, reflecting the shift toward electronic-warfare-resilient design driven by recent conflict experience (echoing themes already noted in [Flight Controllers]({{< relref "../flight-controllers/_index.md" >}}) regarding Ukraine-driven procurement shifts).
- Platform OEMs (e.g., AeroVironment) that build their own tracking antennas for their own aircraft (e.g., Puma AE) differ in value-chain position from independent tracking-antenna specialists (e.g., Troll Systems) that sell radio-agnostic ground equipment across multiple aircraft platforms and customers.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Troll Systems Corporation](https://trollsystems.com) | Valencia, CA, USA | Private | Radio-agnostic auto-tracking directional antennas and transceivers (AX3000, MTX series, SkyLink) for UAS, law enforcement, and broadcast; ITAR-free, US-manufactured. |

### Public Companies

| Ticker | Company | Relevance |
|--------|---------|-----------|
| NASDAQ: AVAV | AeroVironment | Builds its own Long-Range Tracking Antenna (LRTA) and Extended Range Antenna (ERA) ground systems for its Puma AE and related UAS platforms; see full company entry at [AeroVironment]({{< relref "../aerial-drones/aeroviroment.md" >}}). |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Antenna/RF hardware design** | Directional antenna elements, radomes, pan/tilt tracking positioners | [Troll Systems](https://trollsystems.com), AeroVironment (in-house for its own platforms) | US-concentrated for both named suppliers |
| **2. Tracking and acquisition software/electronics** | Auto-alignment, calibration, acquisition, and tracking algorithms; embedded INS/dual-GPS positioning | [Troll Systems](https://trollsystems.com) (patented RF acquisition/tracking software) | Proprietary, vendor-specific — not a shared/commodity toolchain |
| **3. Radio/waveform layer** | COFDM, OFDM, CDL, MIMO/MANET transceivers riding on the antenna hardware | See [Communications]({{< relref "../communications/_index.md" >}}) | N/A — adjacent layer, not duplicated here |
| **4. Aircraft/ground-station integration** | Complete C2/video link between aircraft and operator | [AeroVironment]({{< relref "../aerial-drones/aeroviroment.md" >}}) (platform OEM, vertically integrated); Troll Systems customers (integrator/platform-agnostic model) | N/A — integration layer |

### Key Supply Chain Notes

**Platform OEM vertical integration vs. independent tracking-antenna specialist:** AeroVironment builds its LRTA and ERA tracking antennas specifically for its own Puma AE and related aircraft, a vertically integrated model similar to patterns seen elsewhere in this research area (e.g., DJI's closed gimbal-camera-drone bundle, see [Gimbals & Camera Stabilization]({{< relref "../gimbals/_index.md" >}})). Troll Systems instead sells radio-agnostic tracking antennas across multiple aircraft platforms and customer types (UAS, law enforcement, broadcast), a model closer to Gremsy's independent-supplier position in the gimbal market.

**GPS-denied operation as a shared design requirement:** Both named companies explicitly market GPS-denial resilience (embedded INS, dual-GPS, auto-calibration without relying solely on satellite positioning) as a core capability — a direct response to the same electronic-warfare and jamming environment that has driven procurement changes noted in [Flight Controllers]({{< relref "../flight-controllers/_index.md" >}}) (Blue UAS Framework) and broader defense-market UAS trends.

### Supply Chain — Last Reviewed: 2026-07-15
