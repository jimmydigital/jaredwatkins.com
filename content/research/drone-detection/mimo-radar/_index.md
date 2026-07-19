---
title: "MIMO Radar Projects"
date: 2026-07-17
lastmod: 2026-07-17
draft: false
description: "Multiple-Input Multiple-Output (MIMO) radar architectures for drone detection — digital antenna-array radar that forms a large virtual aperture from few physical elements, enabling high-resolution 3D/4D imaging and classification at lower size, weight, power, and cost than mechanically-scanned or single-channel radar."
research_area: "drone-detection/mimo-radar"
last_reviewed: 2026-07-17
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.7
  disable: false
---

# MIMO Radar Projects

MIMO (Multiple-Input Multiple-Output) radar uses multiple transmit and multiple receive antenna elements, each carrying a distinguishable waveform, so that the receiver can resolve signals from every transmit/receive antenna pair. Combining those pairs synthesizes a much larger **virtual array** than the number of physical antennas actually present — the standard way modern digital radar achieves high angular resolution and 3D/4D (azimuth, elevation, range, and often velocity) imaging without the size, weight, power, and cost of a large mechanically-scanned or fully-populated phased array.

**Relationship to other entries in this section:** MIMO is an antenna/waveform architecture, not a detection algorithm — it is usually paired with [micro-Doppler processing]({{< relref "../detection-methods/micro-doppler-radar.md" >}}) for the actual drone-vs-bird classification step once the MIMO array has localized a target. It's also a distinct approach from the metamaterial-based electronically-scanned-array (MESA) radar used by [Echodyne]({{< relref "../hardware/echodyne.md" >}}) — both are digital, software-defined radar architectures aimed at similar SWaP-C goals, but MIMO's virtual-aperture technique and MESA's beam-steering metamaterial antenna are different ways of getting there. Several vendors described elsewhere in this section (e.g., [DroneShield's RPS-82]({{< relref "../hardware/droneshield.md" >}}), sourced from RADA/Leonardo DRS) use radar built on MIMO-related digital array techniques without necessarily branding the product "MIMO" — this subtopic collects the companies and research projects that build or explicitly market the underlying MIMO radar technology itself.

## Entries

- [Advanced Protection Systems (APS)]({{< relref "advanced-protection-systems.md" >}}) — Polish FIELDctrl 3D MIMO radar family, purpose-built for C-UAS; Access/Advance/Range/Ultra tiers from short-range perimeter to airport/border-scale detection
- [RADA / Leonardo DRS]({{< relref "rada-leonardo-drs.md" >}}) — Israeli-origin, now Leonardo DRS-owned; Multi-Mission Hemispheric Radar (MHR) family uses a digital MIMO radar architecture for 4D AESA pulse-Doppler detection; RPS-42/RPS-82 variants integrated into third-party C-UAS products including DroneShield
- [Fraunhofer FHR]({{< relref "fraunhofer-fhr.md" >}}) — German research institute; dedicated "Drone Detection with MIMO Radar" research line and the AKIRA project building a 3D-MIMO ground-radar network for urban drone traffic monitoring up to 100m altitude
- [Vayyar Imaging]({{< relref "vayyar-imaging.md" >}}) — Israeli radar-on-chip maker; XRR single-chip MIMO RFIC (48 transceivers) built for automotive 4D imaging, marketed into public-safety/security screening — a dual-use MIMO chip platform, not a fielded C-UAS product
- [Uhnder]({{< relref "uhnder.md" >}}) — Austin, Texas digital MIMO radar-on-chip maker (S-series, up to 96 MIMO channels); automotive ADAS-focused today, included here as the enabling chip technology behind the low-cost 4D imaging radar trend relevant to future small/cheap counter-drone sensors

## Why MIMO Matters for Drone Detection

Small drones present a hard radar problem: low radar cross-section, low/zero translational velocity when hovering, and a need for angular precision (not just detection) to hand off accurate track data to a classifier or an effector. A MIMO array's synthesized virtual aperture gives more independent look angles from fewer physical antennas than a conventional array, which is what lets several of the systems in this subtopic claim 3D (and in some cases 4D, adding a velocity/Doppler dimension) target imaging in a compact, relatively low-cost, solid-state package — the same SWaP-C pressure driving [Echodyne's MESA]({{< relref "../hardware/echodyne.md" >}}) and the miniaturized designs in [Fraunhofer FHR's work](#entries). Fraunhofer's AKIRA project is a useful illustration of where this is headed beyond pure security: the same MIMO ground-radar network concept proposed for detecting hostile or unauthorized drones is also being pitched as the sensing backbone for lawful, cooperative drone-traffic management in cities — a genuinely dual-use architecture.

## Companies & Research Institutes

| Organization | HQ | Type | Mission |
|---|---|---|---|
| [Advanced Protection Systems](https://apsystems.tech) | Poland | Private | FIELDctrl 3D MIMO radar family for C-UAS, perimeter security, VSHORAD |
| [Leonardo DRS (RADA)](https://www.drsrada.com) | Israel / USA | Public (Leonardo DRS, NYSE: DRS) | Multi-Mission Hemispheric Radar (MHR) family; digital MIMO 4D AESA pulse-Doppler radar |
| [Fraunhofer FHR](https://www.fhr.fraunhofer.de) | Germany | Research institute | MIMO radar research for drone detection and urban drone-traffic monitoring (AKIRA) |
| [Vayyar Imaging](https://vayyar.com) | Israel | Private | XRR single-chip MIMO RFIC (48 transceivers); 4D imaging radar for automotive and public-safety/security screening |
| [Uhnder](https://www.uhnder.com) | USA (Austin, TX) | Private | Digital Code Modulation MIMO radar-on-chip (S-series); automotive 4D imaging radar |

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
        "title": "MIMO Radar",
        "symbols": [
          {"s": "NYSE:DRS", "d": "Leonardo DRS"}
        ],
        "originalTitle": "MIMO Radar"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->
