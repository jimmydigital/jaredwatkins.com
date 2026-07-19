---
title: "Fraunhofer FHR"
date: 2026-07-17
lastmod: 2026-07-17
draft: false
description: "German research institute (Fraunhofer Institute for High Frequency Physics and Radar Techniques) with a dedicated 'Drone Detection with MIMO Radar' research line and the AKIRA project — a 3D-MIMO ground-radar network concept for monitoring cooperative and non-cooperative drones up to 100m altitude over cities, dual-use for both security and lawful drone-traffic management."
research_area: "drone-detection/mimo-radar"
source_urls:
  - "https://www.fhr.fraunhofer.de/en/sections/Industrial-High-Frequency-Systems-IHS/drone-detection-with-mimo-radar.html"
  - "https://www.izm.fraunhofer.de/en/news_events/tech_news/safer-urban-skies-controlling-drone-aviation-above-german-cities.html"
  - "https://www.fhr.fraunhofer.de/en/sections/Industrial-High-Frequency-Systems-IHS/MINIATURE-MIMO-Radar-SENSORS-FOR-THREE-DIMENSIONAL.html"
  - "https://www.fraunhofer.de/en/research/current-research/defense-against-drones.html"
  - "https://www.fhr.fraunhofer.de/en/sections/Industrial-High-Frequency-Systems-IHS/Detection-of-small-drones-with-millimeter-wave-radar.html"
last_reviewed: 2026-07-17
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Fraunhofer FHR (Fraunhofer Institute for High Frequency Physics and Radar Techniques, Wachtberg, Germany) is a public research institute, not a commercial vendor — included in this subtopic because it runs an explicit "Drone Detection with MIMO Radar" research line and leads **AKIRA**, a project developing a ground-based 3D-MIMO radar network intended to monitor both cooperative and non-cooperative flying objects up to 100 m altitude over German cities. Fraunhofer's framing is genuinely dual-use: the same MIMO radar network proposed for detecting hostile or unauthorized drones (security/defense angle) is pitched equally as the sensing backbone for a lawful drone-traffic-management system, akin to air-traffic control for low-altitude urban drone operations.

## Key Facts

- **Type:** Public research institute (part of the Fraunhofer-Gesellschaft, Germany's applied-research organization)
- **Location:** Wachtberg, Germany
- **Relevant research lines:** "Drone Detection with MIMO Radar," "Miniature MIMO Radar Sensors for Three-Dimensional Visibility in Harsh Environmental Conditions," "Detection of Small Drones with Millimeter-Wave Radar"
- **Flagship project:** AKIRA — ground-based radar platform network for monitoring unmanned aviation over urban airspace
- **Coverage design (AKIRA):** Individual MIMO ground-radar stations covering up to 500 m each; envisioned deployment on public buildings or cellphone towers for city-wide coverage up to 100 m altitude
- **Partners:** esc Aerospace and ESG (IT security/systems partners) reported as collaborators testing economical FMCW radar components for the AKIRA concept

## How It Works

Fraunhofer FHR's core technical argument is that "a MIMO radar system is, so to say, an imaging system" — because the synthesized virtual aperture gives fine enough angular resolution to apply change-detection methods across successive imaging frames, which lets the system pick out a drone hovering in place or creeping slowly along a row of houses, targets that classic single-channel Doppler radar (which relies on translational velocity) would miss entirely. The institute's research pushes this toward miniaturized, geometrically precise 3D-MIMO antennas fabricated on substrates shaped in three dimensions, aiming for compact, low-cost ground-radar nodes rather than large fixed installations. High-precision Doppler-spectrum analysis on top of the MIMO-derived image lets the system estimate rotor count and rotor type, supporting drone classification (see also [Micro-Doppler Radar]({{< relref "../detection-methods/micro-doppler-radar.md" >}})). The AKIRA project's DFRC (Dual Function Radar and Communication) angle additionally investigates using the same radar infrastructure to carry a data-communication network alongside its sensing function.

## Notable Developments

- **AKIRA project (ongoing):** Fraunhofer FHR, together with esc Aerospace and ESG, investigating system concepts for radar sensors and a DFRC communications network aimed at reliably and permanently monitoring cooperative and non-cooperative flying objects up to 100 m altitude in urban airspace
- **Miniaturization research:** Published work on 3D-shaped MIMO antenna substrates intended to reduce radar node size and cost for dense urban deployment
- No specific 2026-dated milestone (e.g., a field trial date or funding announcement) was found in this review; treat the AKIRA project as an active but not obviously time-boxed research effort as of this writing

## Limitations

- **Research institute, not a product vendor:** Unlike the other entries in this subtopic, Fraunhofer FHR's output is research findings and prototype systems, not a purchasable commercial radar — relevant as a leading indicator of where MIMO radar drone-detection technology is headed, not as a fielded solution
- **Dual-use framing complicates threat-model scoping:** Because AKIRA is explicitly positioned for both security and lawful drone-traffic management, its public materials describe a monitoring/tracking capability rather than a security-specific classifier tuned against adversarial evasion (contrast with the threat-model-specific framing in [Micro-Doppler Radar]({{< relref "../detection-methods/micro-doppler-radar.md" >}}))
- **Limited independent verification of specific technical claims:** Coverage figures (500 m per station, 100 m altitude ceiling) are drawn from Fraunhofer's own project descriptions; no independent field-test data was found in this review

## Sources

- [Drone detection with MIMO radar — Fraunhofer FHR](https://www.fhr.fraunhofer.de/en/sections/Industrial-High-Frequency-Systems-IHS/drone-detection-with-mimo-radar.html)
- [Safer urban skies: Controlling drone aviation above German cities — Fraunhofer IZM](https://www.izm.fraunhofer.de/en/news_events/tech_news/safer-urban-skies-controlling-drone-aviation-above-german-cities.html)
- [Miniature MIMO Radar Sensors for Three-Dimensional Visibility — Fraunhofer FHR](https://www.fhr.fraunhofer.de/en/sections/Industrial-High-Frequency-Systems-IHS/MINIATURE-MIMO-Radar-SENSORS-FOR-THREE-DIMENSIONAL.html)
- [Defense against drones — the danger on the radar screen — Fraunhofer](https://www.fraunhofer.de/en/research/current-research/defense-against-drones.html)
- [Detection of small drones with millimeter wave radar — Fraunhofer FHR](https://www.fhr.fraunhofer.de/en/sections/Industrial-High-Frequency-Systems-IHS/Detection-of-small-drones-with-millimeter-wave-radar.html)
