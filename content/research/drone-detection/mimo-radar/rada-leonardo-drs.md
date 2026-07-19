---
title: "RADA / Leonardo DRS"
date: 2026-07-17
lastmod: 2026-07-17
draft: false
description: "Israeli-origin radar maker (RADA Electronic Industries), now DRS RADA Technologies within Leonardo DRS; its Multi-Mission Hemispheric Radar (MHR) family uses a digital MIMO radar architecture for 4D AESA pulse-Doppler detection, with variants (RPS-42, RPS-82) integrated into third-party C-UAS products including DroneShield's DroneSentry."
research_area: "drone-detection/mimo-radar"
source_urls:
  - "https://www.drsrada.com/missions/shorad-c-uas"
  - "https://www.leonardodrs.com/what-we-do/products-and-services/multi-mission-hemispheric-radar/"
  - "https://www.drsrada.com/products/nmhr"
  - "https://www.leonardodrs.com/what-we-do/products-and-services/improved-and-enhanced-multi-mission-hemispheric-radar/"
  - "https://www.radartutorial.eu/19.kartei/05.perimeter/karte007.en.html"
  - "https://www.airforce-technology.com/news/newsrada-to-supply-rps-42-aerial-surveillance-radar-systems-to-undisclosed-asian-country-4989931/"
last_reviewed: 2026-07-17
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

RADA Electronic Industries, an Israeli radar maker, is now DRS RADA Technologies, a segment of Leonardo DRS (NYSE: DRS). Its **Multi-Mission Hemispheric Radar (MHR)** family — including the RPS-42 and RPS-82 variants — is a non-rotating, solid-state, software-defined 4D AESA pulse-Doppler radar line built on a digital MIMO radar architecture: multiple transmitters broadcasting distinguishable waveforms and multiple receivers correlating them into virtual radar channels for high-resolution 4D (azimuth, elevation, range, velocity) imaging. This entry is distinct from a dedicated C-UAS product vendor like [Advanced Protection Systems]({{< relref "advanced-protection-systems.md" >}}): RADA/Leonardo DRS radar is frequently sold as a sensor component integrated into other companies' systems — most notably, an RPS-82 variant is the AESA radar DroneShield integrated into its DroneSentry fixed-site C-UAS system (see [DroneShield]({{< relref "../hardware/droneshield.md" >}})).

## Key Facts

- **HQ:** Netanya, Israel (RADA); parent Leonardo DRS is US/Italy-linked (NYSE: DRS)
- **Type:** Company — radar hardware, now a Leonardo DRS business segment
- **Product family:** Multi-Mission Hemispheric Radar (MHR), including RPS-42, RPS-82, and next-generation variants (nMHR, ieMHR, exMHR)
- **Architecture:** Software-defined, 4D AESA (active electronically scanned array) pulse-Doppler radar using GaN (gallium nitride) amplifiers and a digital MIMO radar architecture (per patent filings: multiple transmit waveforms, multiple receivers, virtual-channel correlation)
- **Stated detection range:** ~3.5 km for smallest ("nano") UAV class (RPS-42)
- **Mission set:** Detects, classifies, and tracks all aerial vehicle classes — fighters, helicopters, UAVs, transport aircraft — plus counter-UAS and short-range air defense (SHORAD) roles
- **Known integration:** RPS-82 variant integrated into DroneShield's DroneSentry fixed-site C-UAS system (2025)
- **Export activity:** Reported supply of RPS-42 aerial surveillance radar systems to an undisclosed Asian country

## How It Works

MHR-family radars use a planar, non-rotating AESA antenna with direct RF sampling and digital beamforming, built on what Leonardo DRS's own patent filings describe as a flexible MIMO radar architecture — multiple transmitters each carrying distinguishable waveforms, multiple receivers, and signal processing that correlates transmit/receive pairs into a larger set of virtual radar channels than the physical antenna count would otherwise support. This is what enables the "4D" claim (azimuth, elevation, range, and Doppler/velocity) in a compact, software-defined, Modular Open System Architecture (MOSA) package that can be reconfigured for different missions (search, track-while-scan, fire control) without new hardware. Because the radar is software-defined and modular, Leonardo DRS positions it as a component other integrators — vehicle platforms, fixed-site C-UAS vendors like DroneShield — can embed into a larger system rather than only selling it as a standalone end-user product.

## Notable Developments

- **2025:** DroneShield integrates an RPS-82 AESA radar (RADA/Leonardo DRS lineage) into its DroneSentry fixed-site C-UAS suite, improving detection range and 4D tracking capability
- **Ongoing:** Leonardo DRS continues to expand the MHR family with next-generation variants (nMHR, ieMHR, exMHR) emphasizing wideband operation, direct RF sampling, and planar transmit/receive architecture
- **Export:** RPS-42 systems reportedly supplied to an undisclosed Asian country for aerial surveillance

## Limitations

- **Component supplier, not always visible to end users:** Like [Echodyne]({{< relref "../hardware/echodyne.md" >}}) elsewhere in this section, much of RADA/Leonardo DRS's reach into the drone-detection market comes through integration into other vendors' branded products (e.g., DroneShield), which can make independent, deployment-specific performance verification harder
- **MIMO branding is technical/patent-level, not consumer marketing:** Leonardo DRS markets these radars primarily as "4D AESA" or "software-defined" rather than leading with "MIMO" in customer-facing material; the MIMO architecture claim in this entry is drawn from patent filings and technical descriptions rather than product brochures
- **Large defense-contractor structure:** As a Leonardo DRS segment, contract values, customer lists, and technical specifications are less transparent than for smaller venture-backed peers in this section

## Sources

- [Air Defense Radars — DRS RADA Technologies](https://www.drsrada.com/missions/shorad-c-uas)
- [Multi-Mission Hemispheric Radar (MHR) — Leonardo DRS](https://www.leonardodrs.com/what-we-do/products-and-services/multi-mission-hemispheric-radar/)
- [Next-Gen Multi-Mission Hemispheric Radar (nMHR) — DRS RADA Technologies](https://www.drsrada.com/products/nmhr)
- [Improved and Enhanced Multi-Mission Hemispheric Radar (ieMHR) — Leonardo DRS](https://www.leonardodrs.com/what-we-do/products-and-services/improved-and-enhanced-multi-mission-hemispheric-radar/)
- [RPS-42 — Radartutorial](https://www.radartutorial.eu/19.kartei/05.perimeter/karte007.en.html)
- [RADA to supply RPS-42 aerial surveillance radar systems to undisclosed Asian country — Airforce Technology](https://www.airforce-technology.com/news/newsrada-to-supply-rps-42-aerial-surveillance-radar-systems-to-undisclosed-asian-country-4989931/)
