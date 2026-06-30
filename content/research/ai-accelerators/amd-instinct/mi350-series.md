---
title: "AMD Instinct MI350 Series"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "MI350X and MI355X: AMD's CDNA 4 generation GPU accelerators with 288 GB HBM3e and MXFP4 support, shipping 2H 2025."
research_area: "ai-accelerators/amd-instinct"
source_urls:
  - "https://www.amd.com/en/products/accelerators/instinct/mi350.html"
  - "https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html"
  - "https://www.amd.com/en/blogs/2025/amd-instinct-mi350-series-and-beyond-accelerating-the-future-of-ai-and-hpc.html"
  - "https://www.servethehome.com/amd-dives-deep-on-cdna-4-architecture-and-mi350-accelerator-at-hot-chips-2025/"
  - "https://blogs.oracle.com/cloud-infrastructure/amd-instinct-mi355x-on-oci-performance-technical-details"
  - "https://www.storagereview.com/news/amd-instinct-mi355x-achieves-mlperf-inference-v6-0-gains-with-over-1-million-tokens-per-second-and-supports-scalable-rocm-stack"
last_reviewed: 2026-06-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The MI350 series (MI350X and MI355X) is AMD's fourth-generation CDNA accelerator, introduced in 2H 2025. Built on CDNA 4, it expands memory to 288 GB HBM3e per chip and adds MXFP4 and MXFP6 data type support, which AMD states enables up to 4x improvement in inference throughput versus the MI300X. The MI355X is the flagship variant for AI inference; the MI350X targets training workloads. Oracle Cloud was an early hyperscale deployment partner.

## Key Facts

- **Architecture:** CDNA 4 (4th Gen)
- **Variants:** MI350X (training focus), MI355X (inference focus)
- **Memory:** 288 GB HBM3e per GPU; 8 TB/s bandwidth
- **Chiplet design:** 8 XCDs (Accelerator Complex Dies) per package
- **New data types:** MXFP4, MXFP6 (in addition to FP8, FP16, BF16)
- **Peak compute (MI355X):** AMD claims up to 4x peak vs. MI300X at FP4 — approximately 10+ PFLOPS FP4 (exact figure not independently confirmed)
- **Scale-up interconnect:** 4th Gen AMD Infinity Fabric; 400 Gbps front-end network (4x prior gen)
- **TDP:** Not publicly confirmed at time of writing
- **Form factor:** OAM (OCP Accelerator Module); 8-GPU OCP platform trays
- **Rack configuration:** Liquid-cooled racks supporting up to 64 GPUs per rack; 2.3 TB aggregate HBM3e per 8-GPU tray
- **Status:** Shipping to hyperscalers 2H 2025; broadly available 2026
- **MLPerf 6.0:** MI355X achieved >1 million tokens/second inference throughput (submitted May 2026)

## What It Is / How It Works

CDNA 4 is the architectural generation underlying the MI350 series. AMD maintained the chiplet approach from MI300 — 8 XCDs (GPU compute dies) with HBM3e stacks on a common interposer — but moved to a denser process node and added new numerical formats.

The MXFP4 and MXFP6 microscaling formats (from the OCP Microscaling Formats specification) allow neural network weights to be stored and computed at lower precision without the accuracy degradation typical of traditional INT4 quantization. This is the primary source of AMD's claimed inference throughput gains: running quantized models at MXFP4 precision yields higher token throughput per GPU at lower power.

The 4th Gen Infinity Fabric scale-up interconnect operates at 400 Gbps per link — four times the prior generation — enabling faster all-reduce operations across multi-GPU nodes. For scale-out (rack-to-rack), the MI350 platform integrates with the AMD Pensando Pollara 400G AI NIC over UltraEthernet-compliant fabric.

Supermicro, Dell, and HPE build 8U systems with 8 MI350X GPUs and 4U liquid-cooled systems with 8 MI355X GPUs for hyperscale deployment. Oracle Cloud Infrastructure (OCI) was among the first to offer general-availability MI355X instances.

## Notable Developments

- **2026-05:** MI355X achieves >1M tokens/second in MLPerf Inference 6.0 — first publicly submitted result at this scale for AMD Instinct
- **2026 (early):** OCI announces general availability of MI355X GPU instances for AI training and inference
- **2025-08:** AMD presents CDNA 4 architecture at Hot Chips 2025 with detailed chiplet design and memory subsystem disclosures
- **2025-H2:** MI350X and MI355X begin shipping to hyperscale partners and cloud providers

## Claim Verification

### Claim: MI355X achieves 4x peak performance over MI300X

**Status:** Partially verified

**Supporting sources:**
- [AMD MI350 product page](https://www.amd.com/en/products/accelerators/instinct/mi350.html) — AMD states "up to 4x" but compares FP4 throughput to MI300X FP8 baseline
- [MLPerf Inference 6.0 — StorageReview](https://www.storagereview.com/news/amd-instinct-mi355x-achieves-mlperf-inference-v6-0-gains-with-over-1-million-tokens-per-second-and-supports-scalable-rocm-stack) — confirms material throughput gain, does not precisely quantify vs. MI300X

**Refuting / questioning sources:**
- The comparison baseline uses MI300X at FP8; an FP4-to-FP4 comparison has not been independently published

**Summary:** The headline 4x claim mixes precision levels; real-world inference gains are likely 2–3x depending on model and quantization approach.

## Sources

- [AMD MI350 Series Product Page](https://www.amd.com/en/products/accelerators/instinct/mi350.html)
- [AMD MI355X Product Page](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html)
- [AMD MI350 Blog — 2025](https://www.amd.com/en/blogs/2025/amd-instinct-mi350-series-and-beyond-accelerating-the-future-of-ai-and-hpc.html)
- [ServeTheHome — CDNA 4 Hot Chips 2025 Deep Dive](https://www.servethehome.com/amd-dives-deep-on-cdna-4-architecture-and-mi350-accelerator-at-hot-chips-2025/)
- [Oracle Cloud — MI355X OCI Performance Details](https://blogs.oracle.com/cloud-infrastructure/amd-instinct-mi355x-on-oci-performance-technical-details)
- [StorageReview — MLPerf 6.0 MI355X](https://www.storagereview.com/news/amd-instinct-mi355x-achieves-mlperf-inference-v6-0-gains-with-over-1-million-tokens-per-second-and-supports-scalable-rocm-stack)
