---
title: "Echodyne"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "US electronically-scanned-array (ESA) radar maker whose miniaturized MESA radars (EchoShield, EchoGuard) are widely embedded in third-party counter-drone systems; selected for a $490M USAF counter-drone program and integrated into Axon/Dedrone."
research_area: "drone-detection/hardware"
source_urls:
  - "https://www.echodyne.com/applications/government/counter-drone-radar/"
  - "https://www.defensenews.com/industry/2026/07/02/in-red-hot-counter-drone-market-echodyne-ceo-sees-radar-demand-boom/"
  - "https://uasmagazine.com/articles/echodyne-selected-as-radar-provider-for-air-force-counter-drone-program"
  - "https://www.echodyne.com/newsroom/echodyne-expands-public-safety-radar-applications-through-partnership-with-axon"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Echodyne (Kirkland, Washington) makes miniaturized electronically-scanned-array (ESA) radar — branded MESA — that has become a common radar component embedded inside other vendors' counter-drone systems rather than being sold primarily as a standalone end-user product. This is a useful distinction for this section: Echodyne is less a competitor to [Dedrone]({{< relref "dedrone.md" >}}) or [DroneShield]({{< relref "droneshield.md" >}}) and more the radar supplier several of them (and defense integrators) build on top of. In 2026 the counter-drone radar market has been described by Echodyne's own CEO as "red hot," with demand potentially growing tenfold by 2030. **Limitation:** as a radar (not RF/Remote ID) sensor, Echodyne detects any airborne object with sufficient radar cross-section regardless of RF emission — but like all radar, it still requires careful tuning to discriminate drones from birds and other clutter, and does not by itself identify a drone's operator or protocol.

## Key Facts

- **HQ:** Kirkland, Washington, USA
- **Type:** Company — radar hardware (ESA/MESA radar family) + EchoWare mission software
- **Product line:** EchoShield (medium-range, advanced threat discrimination), EchoGuard (short-range, ultra-low SWaP for urban settings), EchoFlight (tethered-drone-mounted radar for temporary elevated coverage), MESA (core radar technology), EchoWare (meshed radar management / fusion software)
- **Stated detection ranges (EchoShield):** ~1.5 km for very small UAS, ~3 km for small quadcopters, ~5.3 km for larger multirotor drones, ~7.9 km for small fixed-wing drones
- **Major contract:** Selected in 2026 as primary radar for Trust Automation's Small-Unmanned Air Defense System (SUADS) under a $490M US Air Force IDIQ contract (awarded August 2025)
- **Integration breadth:** Radars integrated into offerings from at least 29 exhibitors at Eurosatory 2026; used on high-powered microwave systems (Epirus, ThinKom) and laser-based systems (AeroVironment, Electro Optic Systems)
- **Status:** Active; rapidly scaling production — opened a new facility in mid-2026 intended to lift production capacity roughly tenfold at full rate

## How It Works

Echodyne's MESA radars are solid-state electronically-scanned-array radars, engineered to be small, light, and power-efficient enough to mount on fixed towers, vehicles, tethered drones, or man-portable kits, unlike traditional mechanically-scanned military radar. They detect and track airborne objects by radar cross-section and kinematics rather than by RF emission — meaning they work identically well against RF-silent, non-cooperative, or Remote-ID-noncompliant drones, closing a gap that both [FAA Remote ID monitoring]({{< relref "../detection-methods/rf-detection.md" >}}) and [non-cooperative RF direction finding]({{< relref "../detection-methods/rf-direction-finding.md" >}}) cannot: an object with no active RF control link at all (fiber-optic tethered, fully autonomous waypoint flight) is still visible to radar if it has enough radar cross-section, which is why this section treats [micro-Doppler radar]({{< relref "../detection-methods/micro-doppler-radar.md" >}}) as the primary detection method rather than RF.

AI/ML classification distinguishes drone, fixed-wing, multi-rotor, vehicle, vessel, human, bird, and clutter categories to reduce false alarms in cluttered environments. EchoWare software meshes multiple radar units and provides a single fusion/C2 interface with an open architecture designed to integrate into third-party command-and-control systems — which is largely how Echodyne reaches end users: as the radar layer inside someone else's C-UAS product. Notably, **Axon announced in May 2026 that it would integrate Echodyne radar into its Axon Air and Dedrone platforms**, directly linking this entry to [Dedrone]({{< relref "dedrone.md" >}}) elsewhere in this section.

## Notable Developments

- **2026-07:** Defense News reports Echodyne CEO describing "red hot" counter-drone radar demand, with short-range radar demand potentially growing tenfold by 2030; company opens new production facility to scale roughly 10x
- **2026-05-27:** Axon announces integration of Echodyne radar into Axon Air and Dedrone platforms
- **2026-04:** Echodyne selected as radar provider for Trust Automation's SUADS program under a $490M US Air Force IDIQ counter-drone contract (originally awarded August 2025)
- **2026 (Eurosatory):** At least 29 exhibitor stands displayed Echodyne radars integrated into their own counter-UAS offerings

## Limitations

- **Radar-only, not identification:** Detects and tracks by radar signature; does not itself decode Remote ID, identify drone manufacturer/model, or locate an operator — typically paired with RF, optical, or Remote ID sensors in a fused system (see [Multi-Sensor Fusion]({{< relref "../detection-methods/multi-sensor-fusion.md" >}}))
- **Primarily a component supplier:** Most end users encounter Echodyne radar embedded inside another vendor's product rather than purchasing directly, which can make independent performance verification harder for a given deployment
- **Classification accuracy in dense clutter:** Like all radar-based systems, drone-vs-bird and drone-vs-vehicle discrimination in busy or urban airspace depends on tuning and AI/ML model quality, not guaranteed by hardware alone

## Key People

- **Eben Frankenberg** — Co-founder (2014), President and CEO; previously COO of Intellectual Ventures (grew from 50 to 550 people, $250M to $5B+ under management, incubated Evolv Technologies and Kymeta); earlier spent 9 years at Onyx Software in sales/marketing leadership. Bachelor's in geophysics from Harvard, MS in geophysics from Stanford
- Series A ($15M) led by Bill Gates and Madrona Venture Group

### People — Last Reviewed: 2026-07-07

## Claim Verification

### Claim: $490M USAF SUADS contract
**Status:** Verified via multiple independent trade press outlets.
**Supporting sources:** [UAS Magazine](https://uasmagazine.com/articles/echodyne-selected-as-radar-provider-for-air-force-counter-drone-program), [The Defense Post](https://thedefensepost.com/2026/04/21/echodyne-radar-counter-drone/), [UASweekly.com](https://uasweekly.com/2026/04/23/echodyne-radar-selected-for-trust-automations-490m-u-s-air-force-counter-uas-contract/) all report consistent figures.
**Summary:** Well-corroborated across independent defense trade publications.

### Claim: EchoShield detection ranges (~1.5 km very small UAS, ~3 km small quadcopters, ~5.3 km larger multirotor, ~7.9 km small fixed-wing)
**Status:** Unverified independently — company-stated figures from Echodyne's own site.
**Supporting sources:** [Echodyne Counter-Drone Radar page](https://www.echodyne.com/applications/government/counter-drone-radar/).
**Refuting/questioning sources:** None found.
**Summary:** Plausible given the radar class and stated use cases, but treat as vendor-published figures pending independent test data.

## Sources

- [Echodyne Counter-Drone Radar overview](https://www.echodyne.com/applications/government/counter-drone-radar/)
- [In 'red hot' counter-drone market, Echodyne CEO sees radar demand boom — Defense News](https://www.defensenews.com/industry/2026/07/02/in-red-hot-counter-drone-market-echodyne-ceo-sees-radar-demand-boom/)
- [Echodyne selected as radar provider for Air Force counter-drone program — UAS Magazine](https://uasmagazine.com/articles/echodyne-selected-as-radar-provider-for-air-force-counter-drone-program)
- [Echodyne expands public safety radar applications through partnership with Axon](https://www.echodyne.com/newsroom/echodyne-expands-public-safety-radar-applications-through-partnership-with-axon)
