---
title: "RF / Remote ID Monitoring"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Radio frequency detection of drone control links and FAA Remote ID broadcasts — effective against compliant US drones; fundamentally unable to detect fiber-optic or pre-programmed autonomous drones."
tags: ["rf-detection", "remote-id", "drone-detection", "faa", "spectrum-monitoring"]
categories: ["technology"]
research_area: "drone-detection/detection-methods"
source_urls:
  - "https://www.faa.gov/uas/getting_started/remote_id"
  - "https://advexure.com/blogs/news/top-5-remote-id-detection-systems"
  - "https://aerodefense.tech/airwarden-remote-id-receiver/"
  - "https://www.dronetag.com/products/bs"
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10490811/"
  - "https://www.airsight.com/blog/end-of-jamming-tethered-waypoint-drones"
last_reviewed: 2026-06-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

RF detection monitors the radio frequency emissions of drone control links (2.4 GHz, 5.8 GHz) and video downlinks to detect and identify commercial drones. FAA Remote ID (broadcast over Wi-Fi NAN and Bluetooth 5 long-range) provides standardized identification telemetry for compliant US drones. RF monitoring is the fastest path to operator identification and location for compliant drones but is completely ineffective against fiber-optic tethered or fully autonomous pre-programmed drones that emit no RF whatsoever.

## Key Facts

- **FAA Remote ID enforcement:** Active as of 2023; as of 2025 local law enforcement can use Remote ID apps to identify non-compliant operators
- **RF control link frequencies:** 2.4 GHz and 5.8 GHz ISM bands (DJI Ocusync, Lightbridge, Wi-Fi); FPV systems often on 5.8 GHz video
- **Remote ID broadcast protocols:** Wi-Fi NAN (802.11) and Bluetooth 5 Long Range (ASTM F3411-22a standard)
- **Detection range:** Up to 5 km for passive RF sensors in ideal conditions; ~1.3–3.7 km for Remote ID depending on drone model
- **Critical limitation:** Zero effectiveness against fiber-optic tethered drones or pre-programmed autonomous drones with no active RF transmissions

## What It Is / How It Works

**Passive RF detection** uses wideband software-defined radio (SDR) receivers to scan the spectrum for drone control link emissions. Many drones use proprietary protocols (DJI OcuSync, DJI O3, Skydio SPRTN) that can be fingerprinted. Directional antennas combined with angle-of-arrival (AoA) processing allow triangulation of both drone and operator positions. Systems like Dedrone RF-360 and Aaronia AARTOS operate on this principle, with detection ranges up to 5 km in ideal conditions and protocol libraries covering 200+ drone types.

**FAA Remote ID** (ASTM F3411 / 14 CFR Part 89) mandates that US-registered drones manufactured after 2022 broadcast identification messages every second including: drone ID, takeoff location, current position, altitude, velocity, and operator location. These broadcasts use:
- **Broadcast Remote ID (BRI):** Direct RF broadcast from drone (Wi-Fi NAN, Bluetooth 5 LR) — receivable with off-the-shelf hardware within ~300m–3.7 km depending on protocol and environment
- **Network Remote ID:** Drone sends data to a USS (UAS Service Supplier) via cellular uplink — requires network access by the drone

Receivers built to the ASTM standard (Dronetag BS, AeroDefense AirWarden, OpenDroneID receiver apps) can decode BRI and display operator identity, position, and flight path.

**Research-grade RF identification** work (Svanström et al., 2023) demonstrates decoding Remote ID telemetry from DJI drones at up to 3.7 km and reconstructing 2D position and altitude in real time from the encoded GPS data.

## Threat Vector Analysis: What RF Cannot Detect

This is the most important operational constraint for critical infrastructure protection:

**Fiber-optic tethered drones** have no radio link at all. Control signals travel through a thin fiber-optic cable that spools from the ground to the drone. First deployed operationally by Russian forces in Ukraine (~2024), these drones are:
- Completely invisible to all passive RF detection
- Immune to RF jamming
- Increasingly available commercially and on the grey market
- NATO issued an urgent innovation challenge in April 2025 specifically seeking detection for fiber-optic FPV threats

**Pre-programmed autonomous (waypoint) drones** operate on pre-loaded GPS flight paths with no active command link during flight. They may transmit Remote ID (if compliant) but emit no controllable RF link. Detection requires other modalities (radar, acoustic, optical).

**RF-silent phases:** Even conventionally RF-controlled drones may go RF-silent for portions of a mission by using pre-programmed waypoints with the control link dormant. RF detection only catches actively communicating drones.

## Hardware Available Today

| Product | Vendor | Type | Range | Notes |
|---------|--------|------|-------|-------|
| RF-360 | Dedrone (Axon) | Passive RF | ~2 km typical / 5 km ideal | 2.5° AoA; 200+ drone protocols; MIL-STD-810H |
| AARTOS X9 | Aaronia AG | Passive RF + Remote ID | Up to 14 km | 20 MHz–8 GHz; decodes DJI OcuSync, Mavlink; 360° coverage |
| AARTOS X2 | Aaronia AG | Portable passive RF | Up to 5 km | Mobile deployment |
| AirWarden | AeroDefense | Remote ID receiver | ~300 m–1 km | Small form factor; low maintenance; FAA BRI compatible |
| Dronetag BS | Dronetag | Remote ID base station | ~3–5 km | Fixed outdoor receiver; feeds UTM/app |
| Dronetag RIDER | Dronetag | Portable Remote ID | ~3 mi radius | IP54; 6–10 hr battery; patrol use |

## Regulatory / Legal Context

RF jamming and signal takeover (cyber/GPS spoofing) of drones is **illegal for private entities** under US federal law (Communications Act, Computer Fraud and Abuse Act). Detection-only is permissible. Only authorized federal agencies (DoD, DHS, DOJ, FAA, Secret Service) may legally employ jamming or cyber countermeasures. State and local law enforcement have limited authority under the FAA Reauthorization Acts of 2018 and 2024.

## Sources

- [FAA Remote ID overview](https://www.faa.gov/uas/getting_started/remote_id)
- [Top 5 Remote ID Detection Systems — Advexure 2025](https://advexure.com/blogs/news/top-5-remote-id-detection-systems)
- [AeroDefense AirWarden Remote ID Receiver](https://aerodefense.tech/airwarden-remote-id-receiver/)
- [Dronetag BS product](https://www.dronetag.com/products/bs)
- [Drone Detection and Tracking Using RF Identification Signals — PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10490811/) — Remote ID decoding at 3.7 km
- [The End of Jamming: Tethered Drones & Waypoint Autonomy — AirSight](https://www.airsight.com/blog/end-of-jamming-tethered-waypoint-drones)
- [Fiber-Optic Drones: Posing a Significant C-UAS Challenge — US Army](https://www.army.mil/article/287737/fiber_optic_drones_posing_a_significant_c_uas_challenge)
