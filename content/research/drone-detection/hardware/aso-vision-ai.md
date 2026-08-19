---
title: "ASO Vision-AI"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Romanian DeepTech startup building a passive, purely-optical edge-AI drone detection system derived from meteor-tracking astronomy research; short-range (~120 m) plug-and-play units for critical infrastructure, launched Aug 2025."
research_area: "drone-detection/hardware"
source_urls:
  - "https://aso-surveillance.com/"
  - "https://www.asodronedetection.com/"
  - "https://www.itiko.de/artikel/2189802/rum-nisches-deeptech-unternehmen-launcht-weltweit-erstes-optisches-drohnenerkennungssystem-mit-edge-ki.html"
last_reviewed: 2026-08-15
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

ASO (marketed as "ASO — Vision-AI Drone Detection") is a Romanian DeepTech company selling a passive, purely optical drone detection system built on edge AI. The company traces its technology to more than a decade of optical object-tracking research originally developed for astronomical meteor detection (dating to 2014), repurposed for airspace surveillance. ASO positions the product against RF- and radar-based competitors on cost and effectiveness at short range against small, low-flying, RF-silent drones.

## Key Facts

- **HQ / Origin:** Romania
- **Type:** Company — DeepTech startup, optical sensor hardware + edge AI software
- **Detection method:** Purely optical/vision-based; edge AI processing (on-device)
- **Detection range:** Up to 120 m altitude (company-stated)
- **Launch:** Publicly launched August 7, 2025; pre-orders opened September 1, 2025 (limited initial availability)
- **Status:** Early commercial stage

## How It Works

ASO's system is vision-only: cameras plus an edge AI inference pipeline detect and classify aerial objects without any RF sensing or radar. The company frames this as a direct answer to the two dominant approaches' weaknesses — RF detection can't see drones that don't transmit a control/video signal (autonomous, pre-programmed, or fiber-optic-tethered drones), and radar struggles to resolve small, slow, low-altitude targets at close range. Because ASO's system is optical-only, it also emits nothing, so it can't be geolocated or jammed via RF countermeasures.

The company describes its data-processing approach as "proprietary and privacy-compliant," likely referring to on-device (edge) processing that avoids transmitting raw video off-site — relevant for sites with privacy or classification concerns. Units are designed to be plug-and-play and are pitched for deployment in numbers ("multiple units can operate economically in parallel") to build wider-area coverage from what is, per-unit, a short-range (120 m) sensor.

## Notable Developments

- **2025-09-01:** Pre-order phase opened, described by the company as limited initial availability.
- **2025-08-07:** Public launch, marketed in press coverage as the "world's first" optical drone detection system built on edge AI — a superlative claim not independently verified (see Claim Verification).

## Key People

Public materials reference a company representative using the LinkedIn handle "Christian H." (self-described "Vision-AI Drone Detection for Industry, Critical Infrastructure & Defense" expert and "6× Tech & Defense Entrepreneur") in connection with ASO. Role/title at ASO could not be independently confirmed from company materials, so it is not stated here as fact.

## Claim Verification

### Claim: "World's first" optical drone detection system with edge AI
**Status:** Unverified / disputed by prior art.
**Supporting sources:** Press coverage ([itiko.de](https://www.itiko.de/artikel/2189802/rum-nisches-deeptech-unternehmen-launcht-weltweit-erstes-optisches-drohnenerkennungssystem-mit-edge-ki.html), syndicated via openpr.de) repeats the company's own "world's first" framing.
**Refuting/questioning sources:** This section already documents other passive-optical C-UAS entries — e.g., [Marduk Technologies]({{< relref "marduk-technologies.md" >}}) (Estonia) — and optical/thermal detection is a long-established C-UAS modality (see [Optical/Thermal Detection]({{< relref "../detection-methods/optical-thermal-detection.md" >}})); AI-assisted inference on optical sensors is not itself novel across the broader market.
**Summary:** "World's first" is standard marketing-press language traceable to a syndicated press release, not an independently substantiated claim; treat as unverified superlative rather than fact.

### Claim: 120 m detection range
**Status:** Unverified.
**Supporting sources:** Company-sourced figure repeated in press coverage (itiko.de); the company's own websites could not be directly fetched for this entry (see Limitations).
**Refuting/questioning sources:** None found.
**Summary:** No independent test data reviewed. 120 m is notably short relative to other entries in this section's hardware table (most claim 1 km+), consistent with an early-stage product optimized for near-perimeter coverage rather than standoff detection.

## Limitations

- **Short range relative to category:** At ~120 m, ASO's stated range is well below most other systems in this hardware section, positioning it as a near-field/perimeter tool rather than a standoff early-warning sensor.
- **Direct site access blocked:** The company's primary websites (aso-surveillance.com, asodronedetection.com, asodefense.de) could not be directly fetched for this entry due to connectivity/robots restrictions; this entry relies on third-party press coverage of the company's own claims, which increases uncertainty about specifics not independently corroborated.
- **Optical dependency:** As with all camera-based systems, performance in darkness, fog, or heavy precipitation is not addressed in available materials.
- **Company disclosure:** No funding, team size, or corporate registration details found in available sources.

## Sources

- [ASO — Vision-AI Drone Detection](https://aso-surveillance.com/)
- [ASO Drone Detection (alternate domain)](https://www.asodronedetection.com/)
- [DeepTech aus Rumänien: ASO launcht weltweit erstes optisches Drohnenerkennungssystem mit Edge-KI — itiko.de](https://www.itiko.de/artikel/2189802/rum-nisches-deeptech-unternehmen-launcht-weltweit-erstes-optisches-drohnenerkennungssystem-mit-edge-ki.html)
