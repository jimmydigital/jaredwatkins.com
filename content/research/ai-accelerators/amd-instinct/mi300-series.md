---
title: "AMD Instinct MI300 Series"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "MI300X and MI300A: AMD's CDNA 3 generation GPU accelerators featuring 192 GB HBM3 memory; the fastest-ramping product in AMD history."
research_area: "ai-accelerators/amd-instinct"
source_urls:
  - "https://www.amd.com/en/products/accelerators/instinct/mi300.html"
  - "https://www.datacenterdynamics.com/en/news/amds-mi300-ai-accelerator-sales-drive-80-percent-growth-in-data-center-segment/"
last_reviewed: 2026-06-07
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The MI300 series is AMD's third-generation CDNA accelerator line, released in late 2023. The MI300X (pure GPU) and MI300A (CPU+GPU APU) were the first commercially significant Instinct products to gain meaningful hyperscale adoption. The MI300X set a memory capacity record at launch (192 GB HBM3) and became the fastest-ramping product in AMD history, with sales exceeding $5B in 2024.

## Key Facts

- **Architecture:** CDNA 3 (3rd Gen)
- **Process node:** TSMC 5nm (GPU dies) + 6nm (CPU dies for MI300A)
- **Variants:** MI300X (GPU only), MI300A (CPU+GPU APU)
- **Memory (MI300X):** 192 GB HBM3, 5.3 TB/s bandwidth
- **Memory (MI300A):** 128 GB HBM3
- **Peak compute (MI300X):** ~1.3 PFLOPS FP16; ~2.6 PFLOPS FP8
- **TDP:** 750W (MI300X)
- **Form factor:** OAM (OCP Accelerator Module)
- **Status:** In production; being succeeded by MI350 series
- **Revenue:** >$5B in 2024 (AMD-reported; fastest-ramping product in company history)

## What It Is / How It Works

The MI300X is a pure GPU accelerator using AMD's CDNA 3 architecture. It uses a chiplet design with multiple GPU Complex Dies (GCDs) and High Bandwidth Memory (HBM3) stacks interposer-mounted together. The 192 GB memory capacity at launch significantly exceeded the NVIDIA H100's 80 GB, making the MI300X competitive for large-language-model inference where model size is the primary constraint — larger memory allows serving larger models without tensor parallelism across multiple GPUs.

The MI300A variant integrates AMD EPYC CPU cores alongside GPU compute dies in a single package — a unified memory architecture (UMA) where CPU and GPU share the same HBM pool. This design reduces CPU-GPU memory copy overhead for HPC workloads but is less suited to pure GPU-intensive AI training.

Both variants use the OAM form factor, allowing system integrators (Supermicro, Dell, HPE, and others) to build 8-GPU nodes. Infinity Fabric provides inter-GPU connectivity within the node.

## Notable Developments

- **2024:** AMD revises MI300 revenue guidance four times upward; ends year "more than $5B" — fastest product ramp in AMD history
- **2024:** More than 100 enterprise and AI customers reported actively developing or deploying MI300X
- **2024-Q1:** Oracle Cloud (OCI) among first hyperscalers to offer MI300X instances commercially
- **2023-Q4:** MI300X and MI300A ship to first customers

## Sources

- [AMD Instinct MI300 Series Product Page](https://www.amd.com/en/products/accelerators/instinct/mi300.html)
- [Data Center Dynamics — MI300 revenue growth](https://www.datacenterdynamics.com/en/news/amds-mi300-ai-accelerator-sales-drive-80-percent-growth-in-data-center-segment/)
