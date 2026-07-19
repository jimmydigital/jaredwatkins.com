---
title: "Advanced Protection Systems (APS)"
date: 2026-07-17
lastmod: 2026-07-17
draft: false
description: "Polish counter-drone company building the FIELDctrl family of 3D MIMO radars — purpose-built for LSS (low-slow-small) drone detection, tracking, and AI-based bird/drone classification across four tiers from short-range perimeter security to airport/border-scale coverage."
research_area: "drone-detection/mimo-radar"
source_urls:
  - "https://apsystems.tech/en/our-products/ultra-precise-3d-mimo-radars/"
  - "https://www.unmannedairspace.info/counter-uas-systems-and-policies/advanced-protection-systems-launches-3d-mimo-family-of-radars-for-drone-detection/"
  - "https://www.military.africa/2022/07/aps-supplies-fieldctrl-3d-mimo-c-uas-solution-to-ivorian-special-forces/"
  - "https://www.targikielce.pl/en/about-us/news/premiere-at-mspo-fieldctrl-follow-3d-mimo-radar--a-new-dimension-of-drone-combat,72209"
last_reviewed: 2026-07-17
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Advanced Protection Systems (APS), based in Gdynia, Poland, designs its counter-drone radar hardware entirely in-house, centered on the **FIELDctrl** family of 3D MIMO radars purpose-built for detecting, tracking, and classifying Low-Slow-Small (LSS) targets — the drone category that conventional air-surveillance radar struggles with. Unlike several other companies in this subtopic, APS markets MIMO radar as a finished, fielded C-UAS product rather than a research platform or embedded chip, with deployments reported including Ivorian Special Forces.

## Key Facts

- **HQ:** Gdynia, Poland
- **Type:** Company — in-house designed 3D MIMO radar hardware for C-UAS, perimeter security, and VSHORAD
- **Founders:** Dr. Maciej Klemm and Dr. Radosław Piesiewicz
- **Product family (FIELDctrl):**
  - **FIELDctrl Access** — smallest/most affordable VSHORAD 3D radar tier
  - **FIELDctrl Advance** — adds MIMO, multi-hypothesis tracking (MHT), and micro-Doppler classification; 90° azimuth, 60° elevation, 4 Hz refresh
  - **FIELDctrl Range** — detects nano-UAV from 6 km out to helicopters at 15 km; positioned for ECM/C-UAS, perimeter security, and high-precision VSHORAD
  - **FIELDctrl Ultra** — most advanced tier, for airports, borders, and strategic-facility protection requiring maximum detection range
- **Classification:** AI/ML-based automatic classification distinguishes drones from birds; stated microdrone detection beyond 6 km
- **Reported deployment:** Supplied to Ivorian Special Forces (2022); marketed to military, security, and critical-infrastructure customers internationally

## How It Works

FIELDctrl radars use a MIMO antenna architecture — multiple transmit elements each broadcasting a distinguishable waveform, received across multiple receive elements — to synthesize a virtual aperture larger than the physical array, giving 3D (and for some tiers, higher-refresh 4D-like) target imaging without the bulk of a mechanically-scanned radar. On top of the MIMO-derived 3D track, APS layers micro-Doppler classification (see [Micro-Doppler Radar]({{< relref "../detection-methods/micro-doppler-radar.md" >}})) and multi-hypothesis tracking to discriminate drones from birds and clutter and maintain track continuity across multiple simultaneous targets. The four-tier product structure lets APS address everything from short-range perimeter protection to long-range airport/border surveillance from a common underlying MIMO radar architecture, scaling antenna size, transmit power, and processing rather than changing the core technique.

## Notable Developments

- **2022-07:** APS reported supplying a FIELDctrl 3D MIMO C-UAS solution to Ivorian Special Forces
- **MSPO defense expo (Poland):** "FIELDctrl Follow" 3D MIMO radar premiered, described in trade coverage as "a new dimension of drone combat" — suggesting an on-the-move or tracking-optimized variant beyond the four core tiers
- No confirmed 2026-specific product launch or contract was found in this review beyond the general FIELDctrl family description; verify current-year developments against APS's own newsroom before citing as recent

## Limitations

- **Company-published specifications:** Detection ranges, refresh rates, and classification accuracy figures in "Key Facts" derive from APS marketing material; independent test data was not found in this review
- **Smaller company, less independent press coverage:** Compared to DroneShield, Dedrone, or Fortem elsewhere in this section, APS has comparatively thin independent (non-company, non-trade-show) reporting — treat deployment and performance claims as vendor-stated pending further corroboration
- **MIMO-specific technical detail is limited:** Public material confirms "3D MIMO" branding and general architecture but does not disclose antenna element counts, exact frequency band, or waveform design in detail

## Sources

- [Radary FIELDctrl 3D MIMO — detekcja dronów — APS](https://apsystems.tech/en/our-products/ultra-precise-3d-mimo-radars/)
- [Advanced Protection Systems launches 3D MIMO family of radars for drone detection — Unmanned Airspace](https://www.unmannedairspace.info/counter-uas-systems-and-policies/advanced-protection-systems-launches-3d-mimo-family-of-radars-for-drone-detection/)
- [APS supplies FIELDctrl 3D MIMO C-UAS solution to Ivorian Special Forces — Military Africa](https://www.military.africa/2022/07/aps-supplies-fieldctrl-3d-mimo-c-uas-solution-to-ivorian-special-forces/)
- [Premiere at MSPO: FIELDctrl Follow 3D MIMO Radar](https://www.targikielce.pl/en/about-us/news/premiere-at-mspo-fieldctrl-follow-3d-mimo-radar--a-new-dimension-of-drone-combat,72209)
