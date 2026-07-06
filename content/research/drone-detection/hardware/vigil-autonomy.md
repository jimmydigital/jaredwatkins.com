---
title: "Vigil Autonomy"
date: 2026-07-03
lastmod: 2026-07-03
draft: false
description: "Austin, TX startup (founded Aug 2025) building benchmark and perception infrastructure for counter-UAS systems — the CommonDefense multi-spectral training dataset, Jetson-based field collection hardware, and model baselines for C-UAS computer vision teams."
research_area: "drone-detection/hardware"
source_urls:
  - "https://www.vigilautonomy.com/"
  - "https://www.vigilautonomy.com/company/about"
  - "https://www.vigilautonomy.com/newsroom"
  - "https://www.vigilautonomy.com/careers"
  - "https://www.vigilautonomy.com/partner-with-us"
  - "https://www.goodmattg.xyz/"
  - "https://x.com/goodmattg"
  - "https://github.com/goodmattg"
last_reviewed: 2026-07-03
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Vigil Autonomy is an Austin, Texas startup, founded August 2025, that builds benchmark and perception infrastructure for counter-UAS (C-UAS) teams — not a detection or interceptor product itself, but the data, hardware, and evaluation layer that other C-UAS companies use to train and validate their perception models before fielding them. Its flagship offering, **CommonDefense**, is a multi-spectral (RGB/LWIR/MWIR) counter-UAS training and benchmark dataset with RTK-grade ground-truth positioning.

## Key Facts

- **HQ:** Austin, Texas
- **Founded:** August 2025
- **Founder & CEO:** Matt Goodman (also styled "Founder & Principal" on his personal site)
- **Type:** Perception/data infrastructure and benchmarking provider — supplies tooling to C-UAS integrators rather than selling an end-user detection or interception product
- **Flagship product:** CommonDefense — multi-spectral C-UAS training/benchmark dataset (v3.2 as of April 2026)
- **Funding:** Not publicly disclosed as of this review; no verified funding announcement found
- **Status:** Early-stage, active; partner program opened June 2026

## What It Is

Vigil Autonomy positions itself as the "shared perception layer" for the C-UAS industry rather than a competitor to detection hardware or interceptor vendors. The company's stated thesis is that adversary drones cost roughly $500 while the kill chains built to stop them cost millions, and that the bottleneck limiting cheaper, faster C-UAS response is perception infrastructure — training data, evaluation, and model baselines — rather than hardware.

Its product line has three parts:

- **Field Data (CommonDefense):** Real-world drone capture data with calibrated timing, RTK position, and scenario metadata across RGB, LWIR (long-wave infrared), and MWIR (mid-wave infrared) imagery, intended for training and evaluating detection/tracking/segmentation models.
- **Latency Benchmarks:** Measurement of detection timing and continuity against deployment constraints, not just raw detection accuracy — the company argues "toy demos" of detection quality alone are not a reliable indicator of real-world performance.
- **Model Baselines:** Reference computer-vision models and failure reports showing performance against the CommonDefense corpus, plus fine-tuning services using edge-collected data specific to a customer's deployment region.

Vigil also offers its own field collection hardware — a Jetson-based "Ground Station" platform (camera, RTK positioning, and collection rig) — for customers who want synchronized data collection before their own production hardware is finalized. Benchmarks are designed to run offline on a customer's own Linux-based compute/perception stack, including NVIDIA Jetson edge hardware.

## Notable Developments

- **2026-06:** Opened its partner program — data licensing, model evaluation, and custom collection programs for prime contractors, system integrators, government agencies, and research institutions.
- **2026-04:** Released CommonDefense v3.2, expanding multi-spectral (RGB/LWIR/MWIR) annotation coverage with RTK-grade positioning and full camera intrinsics per annotation.
- **2026-01:** Ground Station (Jetson-based field collection platform) entered active field collection in the Texas Hill Country.
- **2025-08:** Vigil Autonomy founded in Austin, TX by Matt Goodman.

## Key People

**Matt Goodman** — Founder & CEO
- LinkedIn: [linkedin.com/in/matt-goodman-89b76989](https://www.linkedin.com/in/matt-goodman-89b76989/)
- [X](https://x.com/goodmattg) · [GitHub](https://github.com/goodmattg) · [Personal site](https://www.goodmattg.xyz/) — handle `goodmattg` consistent across all three; GitHub profile explicitly cross-links the X account and personal site, confirming same person.
- Previously: Staff Software Engineer, Setpoint (2023– ); Head of Engineering, Cercle AI (2022–2023); Computer Vision Research Engineer, ByteDance AI Lab Computer Vision Group (2021–2023)
- Education: M.S. Computer Science (computer vision), University of Pennsylvania (2019–2021), including research in the UPenn GRASP Lab Computer Vision Group; B.S. with honors in Electrical Engineering, University of Pennsylvania
- Per Vigil Autonomy's own About page, Goodman founded the company "after consulting on computer vision for C-UAS companies based in Austin, TX" — no specific prior C-UAS employer named.

### People — Last Reviewed: 2026-07-03

## Claim Verification

### Claim: 94.2% mAP@0.5 model baseline performance
**Status:** Unverified.
**Supporting sources:** Stated on Vigil Autonomy's own homepage as a headline metric; no test set, methodology, or third-party benchmark disclosed.
**Summary:** Self-reported figure with no independent corroboration or documented evaluation protocol.

### Claim: 500K+ annotations in field dataset; 12+ latency/timing metrics tracked
**Status:** Unverified.
**Supporting sources:** Company homepage only.
**Summary:** No independent source confirms dataset size or benchmark metric count.

### Claim: "$500 average adversary drone cost" / "$3M+ average interceptor cost" / "400% increase in UAS incidents, 2019–2024" / "1B+ consumer drones produced annually"
**Status:** Unverified as company-specific research; directionally consistent with cost-asymmetry figures cited elsewhere in this knowledge base (e.g., Allen Control Systems' ~$10-per-kill claim), but Vigil does not cite primary sources for these industry-wide statistics on its site.
**Summary:** Treat as marketing context rather than sourced statistics pending an independently cited methodology.

## Sources

- [Vigil Autonomy — homepage](https://www.vigilautonomy.com/)
- [Vigil Autonomy — About](https://www.vigilautonomy.com/company/about)
- [Vigil Autonomy — Newsroom](https://www.vigilautonomy.com/newsroom)
- [Vigil Autonomy — Careers](https://www.vigilautonomy.com/careers)
- [Vigil Autonomy — Partner With Us](https://www.vigilautonomy.com/partner-with-us)
- [Matt Goodman — personal site](https://www.goodmattg.xyz/)
- [Matt Goodman — X (@goodmattg)](https://x.com/goodmattg)
- [Matt Goodman — GitHub](https://github.com/goodmattg)
