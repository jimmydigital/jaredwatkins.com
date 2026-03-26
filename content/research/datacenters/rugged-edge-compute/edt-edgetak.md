---
title: "EDT / EDGETAK"
date: 2026-03-25
lastmod: 2026-03-26
draft: false
description: "Hillsboro, OR defense electronics company (HEICO subsidiary, NYSE: HEI); EDGETAK man-portable wearable tactical AI compute platform (launched April 2025); NVIDIA Jetson Orin NX-based; battery-powered; passive thermal management; ATAK-compatible; fits in standard radio or ammunition pouch; EDGETAK RF SDR integration (30MHz–8GHz) announced Summer 2026; targets dismounted soldiers and SOCOM operators."
tags: ["rugged", "edge-compute", "mil-spec", "ai-inference", "defense", "us", "man-portable"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://edt.com/"
  - "https://edt.com/product/edgetak/"
last_reviewed: 2026-03-26
stale_after_days: 90
---

## Summary

Engineering Design Team, Inc. (EDT) is a Hillsboro, Oregon defense electronics company that has been a HEICO Corporation subsidiary since November 2005. Its EDGETAK platform, officially launched April 16, 2025, addresses the most extreme end of the SWaP constraint in rugged compute: a wearable AI inference system that fits in a standard radio pouch and is powered by soldier batteries. Built on the NVIDIA Jetson Orin NX, EDGETAK brings GPU-accelerated AI inference to dismounted soldiers and special operations operators who cannot carry rack-mounted compute. Integration with ATAK — the DoD's primary soldier situational awareness platform — makes EDGETAK's AI outputs immediately actionable in the field. The Summer 2026 EDGETAK RF variant adds 30MHz–8GHz software-defined radio capability, expanding the platform from pure AI inference to tactical SIGINT.

## Key Facts

- **Full company name:** Engineering Design Team, Inc. (EDT)
- **Founded:** Not publicly documented; HEICO subsidiary since November 2005
- **HQ:** Hillsboro, OR
- **Parent company:** HEICO Corporation (NYSE: HEI) — aerospace/defense component manufacturer; ~$3.8B revenue FY2024
- **Value chain position:** End-system supplier — complete man-portable tactical compute platform to special operations and dismounted infantry units
- **Product:** EDGETAK — wearable tactical AI inference platform; officially launched April 16, 2025
- **Compute:** NVIDIA Jetson Orin NX — compact AI compute module; approximately 70–100 TOPS INT8 inference throughput; 10–25W power draw
- **Form factor:** Wearable/man-portable — designed to fit in a standard radio pouch or ammunition magazine pouch; body-worn by dismounted operators
- **Power:** Battery-powered; passive thermal management (no active cooling fans)
- **Software integration:** ATAK (Android Team Awareness Kit) compatible — integrates with DoD primary soldier situational awareness and blue force tracking app
- **EDGETAK RF (Summer 2026):** Software-defined radio variant with 30MHz–8GHz coverage — adds tactical SIGINT capability to the base inference platform
- **Target users:** Dismounted soldiers, SOCOM operators, reconnaissance teams
- **Standards:** MIL-STD-810 environmental compliance (implied by wearable defense form factor; specific MIL-spec qualification documentation not publicly listed)

## What It Is / How It Works

EDGETAK addresses the most extreme SWaP constraint in this research section: a soldier on foot cannot carry a rack-mounted server. The platform takes NVIDIA's Jetson Orin NX — a compact, low-power AI compute module — and integrates it into a form factor that can be worn or carried with a soldier's existing kit.

The Jetson Orin NX delivers meaningful AI inference capability at approximately 70–100 TOPS INT8 in a package consuming 10–25W, enabling real-time computer vision (identifying objects, vehicles, or personnel from a camera feed), signals processing, and sensor fusion — all without radio transmission to a backend cloud or datacenter. This is crucial for operations in denied, disrupted, or intermittent communications (DDIL) environments where connectivity to a cloud inference service cannot be guaranteed.

**ATAK integration** is the key operational software connection. ATAK is the Android-based app that US military and allied forces use for blue force tracking, shared situational awareness, and mission coordination. EDGETAK's AI inference outputs — object detections, signal intercepts, sensor fusion data — feed directly into the ATAK display, making AI results immediately actionable without requiring a separate display device or data link back to a command post.

**Passive thermal management** is a critical design constraint that distinguishes EDGETAK from commercial edge AI modules: active cooling (fans) creates acoustic signature, draws additional power, and introduces mechanical failure modes in field conditions. EDGETAK's passive thermal design means no moving parts in the cooling system — important for reliability, stealth, and maintenance in austere environments.

**EDGETAK RF (Summer 2026)** represents a significant capability expansion: combining AI inference with software-defined radio (30MHz–8GHz coverage) means EDGETAK can perform signals intelligence tasks — identifying, classifying, and geolocating radio emissions — that previously required specialized, separately carried equipment. The SDR+AI combination on a single wearable platform is a meaningful capability increase for individual operators.

## Notable Developments

- **Summer 2026:** EDGETAK RF announced — software-defined radio variant with 30MHz–8GHz coverage; adds SIGINT capability to base EDGETAK inference platform
- **2026-04-16:** EDGETAK officially launched — man-portable wearable tactical AI compute platform
- **Active:** ATAK compatibility established — integration with DoD tactical situational awareness platform
- **HEICO parent (NYSE: HEI):** Provides manufacturing scale and existing DoD procurement relationships that smooth EDGETAK's acquisition pathway through defense channels

## Key People

**HEICO Corporation (Parent Company)**

**Laurans Mendes** — Chairman, HEICO Corporation
- LinkedIn: not found
- Co-founded HEICO with sons Eric and Victor Mendes

**Eric Mendes** — President & CEO, HEICO Corporation
- LinkedIn: not found
- Son of Laurans Mendes; leads HEICO's day-to-day operations

**EDT Division Leadership:** EDT operates as a technical product division within HEICO's Electronic Technologies Group. Division-level leadership is not prominently public-facing; no named individuals confirmed as of last review.

### People — Last Reviewed: 2026-03-26

## Claim Verification

### Claim: Fits in standard radio/ammunition pouch

**Status:** Plausible; specific dimensions not independently verified

**Supporting sources:**
- [EDT EDGETAK product page](https://edt.com/product/edgetak/) — company markets EDGETAK explicitly as fitting in standard radio and ammunition pouches
- NVIDIA Jetson Orin NX production module dimensions are 69.6mm × 45mm — small enough for pouch integration with appropriate housing

**Refuting / questioning sources:**
- The Jetson Orin NX compute module itself is compact, but the complete EDGETAK system includes housing, battery, connectors, and thermal management structure — the combined package dimensions and weight are not independently published; "fits in a radio pouch" may refer to a specific pouch size that differs from standard MOLLE radio/mag pouches in practice

**Summary:** The core Jetson Orin NX module is genuinely small enough for wearable integration; the complete EDGETAK system dimensions and weight have not been independently confirmed but are consistent with company marketing claims given the Jetson module baseline.

### Claim: EDGETAK RF covers 30MHz–8GHz

**Status:** Unverified; source is company announcement only

**Supporting sources:**
- EDT product announcement materials (Summer 2026) cite 30MHz–8GHz coverage for the EDGETAK RF variant

**Refuting / questioning sources:**
- No independent technical specification or third-party RF performance data found; SDR frequency range claims are difficult to assess without access to insertion loss, sensitivity (NF), and dynamic range specifications across the full claimed band; 8GHz upper limit is technically plausible for modern SDR chipsets but represents the demanding end of wideband SDR performance in a compact form factor

**Summary:** 30MHz–8GHz is a plausible SDR specification for current compact SDR chipsets; no independent verification available; treat as company-stated specification until confirmed by independent test data.

## Sources

- [EDT — Official Website](https://edt.com/)
- [EDT EDGETAK Product Page](https://edt.com/product/edgetak/)
- [HEICO Corporation — Investor Relations](https://ir.heico.com/)
- [NVIDIA Jetson Orin NX — Product Brief](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/) — compute module baseline for EDGETAK
- [ATAK — Android Team Awareness Kit](https://www.tak.gov/) — software integration context
