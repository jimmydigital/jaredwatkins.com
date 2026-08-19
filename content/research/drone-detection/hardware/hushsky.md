---
title: "HushSky"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Passive, RF-silent optical drone detection system from Capablanca.ai using multi-camera 3D voxel triangulation and wavelet-based noise filtering; currently TRL-2, not yet fielded."
research_area: "drone-detection/hardware"
source_urls:
  - "https://hushsky.net/"
last_reviewed: 2026-08-15
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

HushSky is a passive, RF-silent optical drone/aircraft detection system developed by Capablanca.ai, a self-described "Deep Tech venture." It uses multi-camera computer vision — wavelet-based noise filtering, 3D motion voxel triangulation, and AI-based tracking — to detect and localize aerial targets without emitting any signal, which the company argues makes it immune to jamming and spectrum-denial countermeasures that defeat RF- and radar-based systems. The technology is early-stage (company-stated TRL-2) with no fielded deployments documented.

## Key Facts

- **Developer:** Capablanca.ai (parent company, described as a "Deep Tech venture")
- **Type:** Company — passive optical sensor hardware + AI software
- **Detection method:** Multi-camera computer vision; fully passive, zero RF emissions
- **Status:** TRL-2 (early concept/lab validation); pre-operational
- **Target range:** Up to 2 km (company-stated target, unverified)

## How It Works

HushSky's core pitch is passivity: because the system emits nothing, it can't be jammed or geolocated by an adversary's RF sensors — a limitation shared by radar and by any system that depends on detecting a drone's own RF control/video link. The company describes several proprietary processing stages: stationary wavelet filters (it names U-DT-CWT and BM4D specifically) to strip atmospheric noise from camera feeds; "3D Motion Voxel Projection," which intersects rays from multiple synchronized cameras to triangulate a target's 3D position; a coarse-to-fine "pyramid processing" scheme claimed to cut compute load by 90%; and a secondary tracking stage combining spectral clustering with a deep-learning model.

The product is described in three deployment tiers rather than named hardware SKUs: a Near-Field Protection stage for close-range perimeter security, an Early Far-Field Detection tier for extended-range warning, and a Strategic Interception Field for wide-area coverage against faster targets. The company says the camera-array approach scales from 2 to 64 cameras per node and runs at 30–60 Hz on edge GPU/CPU hardware.

## Notable Developments

- **2026 (as of page review):** Company site states TRL-2 status with a roadmap toward a TRL-6 operational prototype, NATO C2 compliance (SAPIENT, ASTERIX standards), and at least four system integrations — these are forward-looking goals, not completed milestones.

## Claim Verification

### Claim: 99.5% detection accuracy with <0.5% false alarm rate; centimeter-level 3D accuracy at 2 km range
**Status:** Unverified.
**Supporting sources:** Company website (hushsky.net) only — self-reported target specifications.
**Refuting/questioning sources:** None found; no independent test data, government evaluation, or third-party review located.
**Summary:** These are stated as targets by a company that identifies itself as TRL-2 (early lab-scale technology). At this readiness level, published performance figures are typically simulation- or bench-test-derived rather than field-validated. Treat as aspirational until independent test results are published.

### Claim: "Jam-proof" / immune to spectrum denial
**Status:** Partially verified by physical principle, unverified in practice.
**Supporting sources:** The underlying premise — a purely passive optical system cannot be RF-jammed — is sound and consistent with other passive-optical entries in this section (see [Marduk Technologies]({{< relref "marduk-technologies.md" >}})).
**Refuting/questioning sources:** None found. Note that optical systems have their own vulnerabilities not addressed by the "jam-proof" framing — daylight/weather dependence, laser dazzling, and smoke/fog obscuration — which the company's public materials do not discuss.
**Summary:** The RF-immunity claim is directionally credible for any passive-optical design, but "jam-proof" elides optical-specific countermeasures and weather/visibility limitations.

## Limitations

- **TRL-2:** Not a fielded or commercially available product as of this writing; no known deployments, pilot programs, or government contracts documented.
- **Optical dependency:** As a camera-based system, performance in darkness, fog, heavy rain, or smoke is not addressed in the company's public materials — a known weak point relative to RF/radar detection methods elsewhere in this section.
- **Limited independent information:** No funding, team, or founding-date information is publicly disclosed; company registration and leadership could not be independently verified from the source page.

## Sources

- [HushSky](https://hushsky.net/)
