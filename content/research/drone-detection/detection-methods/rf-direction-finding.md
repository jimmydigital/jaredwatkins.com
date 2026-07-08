---
title: "RF Direction Finding (Non-Cooperative)"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "Passive RF detection and triangulation of drone control-link and video-downlink emissions — locates any RF-emitting drone regardless of whether it broadcasts Remote ID or cooperates in any way."
research_area: "drone-detection/detection-methods"
source_urls:
  - "https://www.crfs.com/solutions/drone-detection"
  - "https://www.crfs.com/white-papers/principles-of-geolocation-techniques"
  - "https://sensofusion.com/"
  - "https://www.tronfuture.com/solutions/anti-drone/"
  - "https://aaronia.com/en/solutions/drone-detection"
  - "https://www.dedrone.com/products/drone-detection/rf-sensors/overview"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Non-cooperative RF direction finding detects and locates a drone by passively sensing its control-link and video-downlink emissions — the same 2.4/5.8 GHz signals a drone must transmit to be flown by a human operator — rather than depending on any voluntary identification broadcast. This is the more general and more robust RF detection capability for critical infrastructure protection: it works against non-compliant, modified, unregistered, or even military drones that would be completely invisible to a [Remote ID receiver]({{< relref "rf-detection.md" >}}), because it doesn't require the drone to cooperate at all. **Critical limitation:** like Remote ID monitoring, it is still fundamentally an RF-based method — it has zero capability against drones with no active RF control link (fiber-optic tethered, fully pre-programmed autonomous).

## Key Facts

- **What it detects:** Proprietary control-link and video protocols (DJI OcuSync, DJI Lightbridge, DJI O3, Skydio SPRTN, analog FPV video) and general "signals of interest" (telemetry, video link, payload data) rather than a specific cooperative broadcast
- **Frequency bands:** Primarily 2.4 GHz and 5.8 GHz ISM bands for consumer/FPV control and video; some systems (Aaronia AARTOS, Tron Future T.Sensor) scan much wider ranges (20 MHz–8 GHz and 400 MHz–6 GHz respectively) to also catch GNSS, cellular uplink, and other bands
- **Geolocation techniques:** Angle of Arrival (AoA) from a single directional sensor gives a bearing (line of bearing); three or more networked sensors enable Time Difference of Arrival (TDoA) triangulation to a fix; some systems add Frequency Difference of Arrival (FDoA) and Power of Arrival (PoA) for additional accuracy
- **Detection range:** Typically 2–14 km for commercial-drone control links depending on system and environment; CRFS RFeye claims up to 400 km against military drones under favorable conditions
- **Critical limitation:** Zero effectiveness against fiber-optic tethered drones or pre-programmed autonomous drones with no active RF control link during flight

## How It Works

A directional or omnidirectional wideband receiver (often an SDR-based system) continuously scans its covered frequency range for RF energy matching known drone protocol signatures or, in more advanced systems, generic "signal detector" characteristics of telemetry/video/control traffic that don't require a pre-built library of specific drone models. A single sensor can determine a bearing to the emission source (AoA). Networked deployments of three or more sensors with favorable site geometry triangulate that bearing into a full position fix (TDoA), and some systems add FDoA or PoA to improve accuracy or resolve ambiguity.

Two design philosophies exist in the commercial market:

- **Protocol-library systems** fingerprint specific known drone protocols (DJI OcuSync, Lightbridge, etc.) and identify manufacturer/model where the signature matches — effective against the wide majority of COTS drones but potentially blind to modified or unfamiliar protocols.
- **Signal-detector systems**, exemplified by [CRFS RFeye]({{< relref "../hardware/crfs-rfeye.md" >}}), hunt for the RF *characteristics* of telemetry, video links, or payload data transfer rather than matching a specific drone's signature — CRFS argues this generalizes better to modified, homebuilt, or military drones a library-based system would miss.

Because detection triggers on the RF characteristics of the drone's own control/video link rather than on a voluntary identification message, none of this requires the drone to be Remote-ID compliant, registered, or cooperating in any way — the fundamental distinction from [Remote ID monitoring]({{< relref "rf-detection.md" >}}).

## Threat Vector Analysis: What Non-Cooperative RF Cannot Detect

This is the most important operational constraint for critical infrastructure protection, and it applies to non-cooperative RF detection just as much as to Remote ID reception — because both ultimately depend on the drone emitting RF at all:

**Fiber-optic tethered drones** have no radio link at all. Control signals travel through a thin fiber-optic cable that spools from the ground to the drone. First deployed operationally by Russian forces in Ukraine (~2024), these drones are completely invisible to all passive RF detection, immune to RF jamming, and increasingly available commercially and on the grey market. NATO issued an urgent innovation challenge in April 2025 specifically seeking detection methods for fiber-optic FPV threats.

**Pre-programmed autonomous (waypoint) drones** operate on pre-loaded GPS flight paths with no active command link during flight. They emit no controllable RF link even though the airframe itself may still be flying. Detection requires other modalities — see [Micro-Doppler Radar]({{< relref "micro-doppler-radar.md" >}}), [Acoustic Detection]({{< relref "acoustic-detection.md" >}}), and [Optical/Thermal]({{< relref "optical-thermal-detection.md" >}}).

**RF-silent phases:** Even conventionally RF-controlled drones may go RF-silent for portions of a mission by switching to pre-programmed waypoints with the control link dormant. Any RF-based detection, cooperative or not, only catches actively communicating drones.

## Hardware Available Today

| Product | Vendor | Type | Range | Notes |
|---------|--------|------|-------|-------|
| RF-360 | Dedrone (Axon) | Passive RF, protocol library | ~2 km typical / 5 km ideal | 2.5° AoA; 200+ drone protocols; MIL-STD-810H |
| AARTOS X9 | [Aaronia AG]({{< relref "../hardware/aaronia-aartos.md" >}}) | Passive RF + Remote ID | Up to 14 km | 20 MHz–8 GHz; decodes DJI OcuSync, Mavlink; 360° coverage |
| AARTOS X2 | [Aaronia AG]({{< relref "../hardware/aaronia-aartos.md" >}}) | Portable passive RF | Up to 5 km | Mobile deployment |
| RFeye | [CRFS]({{< relref "../hardware/crfs-rfeye.md" >}}) | Passive RF, signal-detector | Up to 400 km (military, ideal) | Signal-hunting (not signature library); AoA/TDoA/FDoA; integrated into L3Harris/Rafael systems |
| Airfence | [Sensofusion]({{< relref "../hardware/sensofusion-airfence.md" >}}) | Passive RF, protocol library | Not publicly specified | Deployed commercially since 2016; locates drone + pilot |
| T.Sensor | [Tron Future]({{< relref "../hardware/tron-future-tsensor.md" >}}) | Passive RF, protocol library + AI classification | 5 km (commercial); 5–35 km (favorable environment) | 400 MHz–6 GHz; ±2.5° DF accuracy; part of integrated AESA anti-drone stack |

## Regulatory / Legal Context

Passive detection and geolocation of RF emissions is generally permissible for private entities under US law, so long as the system senses RF *patterns* rather than decoding communication *content* (which would implicate the Wiretap Act / Pen-Trap Statute). RF jamming and signal takeover remain restricted to authorized federal agencies; detection-only deployment is the legal baseline for critical infrastructure operators. See [Regulatory Framework]({{< relref "../regulatory-framework.md" >}}) for the full US legal landscape.

## Sources

- [CRFS Drone Detection overview](https://www.crfs.com/solutions/drone-detection)
- [CRFS: Principles of Geolocation Techniques (white paper)](https://www.crfs.com/white-papers/principles-of-geolocation-techniques)
- [Sensofusion Airfence](https://sensofusion.com/)
- [Tron Future Anti-Drone solution overview](https://www.tronfuture.com/solutions/anti-drone/)
- [Aaronia AARTOS drone detection overview](https://aaronia.com/en/solutions/drone-detection)
- [Dedrone RF Sensors overview](https://www.dedrone.com/products/drone-detection/rf-sensors/overview)
