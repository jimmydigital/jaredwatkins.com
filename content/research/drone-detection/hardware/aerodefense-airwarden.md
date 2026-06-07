---
title: "AeroDefense AirWarden"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "US-made RF spectrum sensing drone detection system targeting correctional facilities and critical infrastructure; detects both Remote ID-broadcasting and non-broadcasting drones without violating federal surveillance laws."
tags: ["rf-detection", "remote-id", "us", "critical-infrastructure", "commercial-legal", "fixed-site", "mobile"]
categories: ["company"]
research_area: "drone-detection"
source_urls:
  - "https://aerodefense.tech/"
  - "https://aerodefense.tech/rf-drone-detection-system-airwarden-spectrum-overview/"
  - "https://aerodefense.tech/rf-drone-detection-specs-airwarden/"
  - "https://aerodefense.tech/drone-detection-system-products/"
  - "https://aerodefense.tech/correctional-facilities-drone-detection/"
  - "https://aerodefense.tech/drone-detection-system-products/drone-detection-system-price/"
  - "https://dronelife.com/2026/02/19/aerodefense-launches-no-cost-drone-detection-access-program-for-law-enforcement/"
  - "https://uasweekly.com/2023/04/24/aerodefense-introduces-low-cost-remote-id-receiver-for-existing-drone-detection-systems/"
last_reviewed: 2026-06-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

AeroDefense is a US company based in Oceanport, NJ, that builds the AirWarden drone detection system — an RF spectrum sensing platform that detects and locates both the drone and its pilot simultaneously. The system is designed specifically for deployment by non-federal entities (correctional facilities, critical infrastructure operators, campuses, stadiums) and operates without requiring a legal waiver by avoiding demodulation of RF signal content.

## Key Facts

- **Founded:** Operational deployment since 2017 (earliest documented)
- **Headquarters:** Oceanport, NJ (1000 Sanger Ave, Suite 18)
- **Type:** Private company
- **Status:** Active; expanding product line
- **Core technology:** Passive RF spectrum sensing (not signature database; not demodulation)
- **Key differentiator:** Detects both Remote ID-broadcasting drones AND non-broadcasting drones; locates pilot simultaneously with drone
- **Legal status:** Designed to be compliant with Communications Act and federal surveillance law without waivers
- **Pricing:** AirWarden Essentials from $9,987/year; Spectrum system pricing on request
- **DHS SAFETY Act:** AiroDefense holds DHS SAFETY Act Designation, providing liability protection

## What It Is / How It Works

### Detection Approach: Spectrum Sensing

AirWarden uses a patented RF spectrum sensing approach that differs from most competing RF detection systems. Most RF detection systems maintain a database of known drone RF signatures (specific frequencies, modulation schemes, or protocol patterns for DJI, Parrot, etc.) and match incoming signals against that library. AirWarden instead continuously scans the RF environment and uses machine learning algorithms to identify patterns of RF emissions that are "out of the norm" — anomalous signals that match the behavioral characteristics of drone RF activity, without decoding or demodulating the signal content.

This approach has two advantages: it can detect custom "kit" drones and DIY drones that don't appear in any commercial signature library, and it avoids the legal exposure of the Wiretap Act and Pen/Trap Statute — statutes that may be implicated by systems that intercept and decode the control communications between a drone and its operator. AeroDefense explicitly positions this legal compliance as a core product feature.

### Simultaneous Drone and Pilot Detection

A notable capability: AirWarden detects and locates both the drone and its human operator (pilot) simultaneously, by sensing both the drone's return signal and the controller's uplink signal. This is operationally significant — knowing the pilot's location enables law enforcement to respond to the person, not just the aircraft. The system provides drone make, model, location, altitude, speed, and serial number when available, plus pilot location.

### Product Line

**AirWarden Essentials:** A cloud-connected, wide-area monitoring solution launched January 2025. Subscription-based at $9,987/year starting price. Covers up to 20 square miles per deployment. Designed as a scalable, lower-cost entry point for smaller organizations.

**AirWarden Spectrum (Classic):** The full-featured fixed or mobile deployment system. Fixed sensors mount permanently to framing or C-strut. Mobile units deploy from a carrying case and tripod in approximately 15 minutes by a single operator. Dimensions of mobile spectrum sensor: 10" × 8.25" × 3.25". Exact detection range specifications are available via spec sheet request (not published publicly). Pricing is tailored to site layout and use case.

**AirWarden Remote ID Receiver:** A dedicated low-cost receiver for monitoring FAA-mandated Remote ID broadcasts from compliant drones. Introduced April 2023 as a standalone add-on compatible with existing AirWarden deployments or as a standalone system for organizations with limited budgets. Detects Remote ID broadcasts but does not detect non-broadcasting drones.

**AirWarden Direction Finder Module:** An add-on module that provides directional bearing to detected drone and pilot signals, enhancing situational awareness for response teams.

### Law Enforcement Access Program

In February 2026, AeroDefense launched a no-cost drone detection access program for law enforcement agencies, providing access to AirWarden Essentials at no cost under qualifying conditions. This aligns with the FY2026 NDAA SAFER SKIES Act framework and the $500M FEMA grant program for drone detection equipment, which increased law enforcement procurement capacity.

## Deployment Approach

**Correctional Facilities:** AeroDefense's primary established market. Fixed Spectrum sensors mount around facility perimeter. The system's simultaneous drone + pilot detection capability is particularly valuable in correctional settings — it enables staff to not only identify a contraband delivery attempt but to locate the person making the delivery for arrest. At a Georgia State Prison deployment (operational since fall 2017), AirWarden contributed to the interception of over $500,000 in contraband and multiple suspect arrests.

**Critical Infrastructure:** Power facilities, water treatment plants, data centers, government buildings. Fixed sensor arrays provide perimeter monitoring. Integration with existing physical security operations centers (SOCs) via API.

**Event Security:** Stadiums, large public gatherings, National Special Security Events (NSSEs). Mobile units deploy rapidly for temporary coverage.

**Campus Security:** Universities, corporate campuses, healthcare facilities.

## Customer Base

Documented customer segments: US correctional facilities (stated primary market since 2017), colleges and universities, government entities (state and local), law enforcement agencies. AeroDefense does not publicly disclose named enterprise customers. The Georgia State Prison deployment is the only named operational case study in public materials.

## Notable Developments

- **2026-02:** Launched no-cost drone detection access program for law enforcement, aligned with FY2026 NDAA funding availability
- **2025-01:** Launched AirWarden Essentials — $9,987/year entry-level subscription; covers 20 square miles; designed to scale to full Spectrum deployment
- **2023-04:** Introduced standalone AirWarden Remote ID Receiver for existing deployments and low-budget customers
- **2017:** First operational deployment at Georgia State Prison; established correctional market leadership

## Key People

- Executive team and founding details not publicly available on AeroDefense website or in findable press coverage as of this review.
<!-- TODO: search LinkedIn for AeroDefense founders and leadership team -->

### People — Last Reviewed: 2026-06-05

## Claim Verification

### Claim: Detects non-broadcasting (non-Remote ID) drones

**Status:** Partially verified

**Supporting sources:**
- [AeroDefense AirWarden Spectrum page](https://aerodefense.tech/rf-drone-detection-system-airwarden-spectrum-overview/) — company states the Spectrum sensors detect "drones NOT broadcasting Remote ID information including custom 'kit' or Do It Yourself (DIY drones)"
- [Legality page](https://aerodefense.tech/drone-detection-system-products/airwarden-legal-drone-detection/) — explains spectrum sensing mechanism that identifies RF patterns without demodulation

**Refuting / questioning sources:**
- No independent third-party technical evaluation found in public sources. The claim is self-reported.
- Note: Spectrum sensing can detect any drone with an active RF control link; it cannot detect fiber-optic FPV or pre-programmed autonomous drones (no RF emissions). AeroDefense's marketing states this limitation implicitly by focusing on RF control links.

**Summary:** The claim is plausible and technically consistent with the spectrum sensing approach described, but no independent validation exists in public literature. The system cannot detect RF-dark drones (fiber-optic or pre-programmed autonomous).

### Claim: Detects pilot location simultaneously with drone

**Status:** Partially verified

**Supporting sources:**
- Multiple AeroDefense product pages describe simultaneous drone + pilot detection as a core feature
- The mechanism is technically plausible: the controller's RF uplink to the drone is a detectable signal from the pilot's location

**Refuting / questioning sources:**
- No independent evaluation of localization accuracy or range published. Accuracy depends heavily on RF multipath environment (buildings, terrain, RF noise)

**Summary:** Technically plausible; self-reported capability; no independent accuracy verification in public domain.

## Sources

- [AeroDefense company website](https://aerodefense.tech/) — product overview and use cases
- [AirWarden Spectrum Overview](https://aerodefense.tech/rf-drone-detection-system-airwarden-spectrum-overview/) — system capabilities
- [AirWarden Spectrum Sensor Spec Sheet page](https://aerodefense.tech/rf-drone-detection-specs-airwarden/) — specs (spec sheet download gated)
- [AirWarden product suite](https://aerodefense.tech/drone-detection-system-products/) — full product line
- [Correctional Facilities use case](https://aerodefense.tech/correctional-facilities-drone-detection/) — Georgia State Prison case study
- [Pricing page](https://aerodefense.tech/drone-detection-system-products/drone-detection-system-price/) — Essentials $9,987/year; Spectrum by quote
- [DroneLife: AeroDefense no-cost LE access program (Feb 2026)](https://dronelife.com/2026/02/19/aerodefense-launches-no-cost-drone-detection-access-program-for-law-enforcement/)
- [UAS Weekly: Remote ID Receiver launch (Apr 2023)](https://uasweekly.com/2023/04/24/aerodefense-introduces-low-cost-remote-id-receiver-for-existing-drone-detection-systems/)
