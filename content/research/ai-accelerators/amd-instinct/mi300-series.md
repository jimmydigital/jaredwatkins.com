---
title: "AMD Instinct MI300 Series"
date: 2026-06-07
lastmod: 2026-11-12
draft: false
description: "MI300X and MI300A: AMD's CDNA 3 generation GPU accelerators featuring 192 GB HBM3 memory; the fastest-ramping product in AMD history."
research_area: "ai-accelerators/amd-instinct"
source_urls:
  - "https://www.amd.com/en/products/accelerators/instinct/mi300.html"
  - "https://newsroom.amd.com/news/amd-reports-fourth-quarter-and-full-year-2024-fina/"
last_reviewed: 2026-11-12
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The MI300 series is AMD's third-generation CDNA accelerator line, released in late 2023. The MI300X (pure GPU) and MI300A (CPU+GPU APU) were the first commercially significant Instinct products to gain meaningful hyperscale adoption. The MI300X set a memory capacity record at launch (192 GB HBM3) and AMD reported more than \$5B of total Instinct accelerator revenue in 2024. It has since been followed by the MI350 series (MI355X) and the MI400 family (MI455X).

## Key Facts

- **Architecture:** CDNA 3 (3rd Gen)
- **Process node:** TSMC 5nm (GPU dies) + 6nm (CPU dies for MI300A)
- **Variants:** MI300X (GPU only), MI300A (CPU+GPU APU)
- **Memory (MI300X):** 192 GB HBM3, 5.3 TB/s bandwidth
- **Memory (MI300A):** 128 GB HBM3
- **Peak compute (MI300X):** ~1.3 PFLOPS FP16; ~2.6 PFLOPS FP8
- **TDP:** 750W (MI300X)
- **Form factor:** OAM (OCP Accelerator Module)
- **Status:** Shipping since late 2023; succeeded by the MI350/MI355X and MI400/MI455X generations
- **Revenue:** AMD reported more than \$5B of total Instinct accelerator revenue in 2024 (the figure covers the Instinct line, not MI300X alone)

## What It Is / How It Works

The MI300X is a pure GPU accelerator using AMD's CDNA 3 architecture. It uses a chiplet design with multiple GPU Complex Dies (GCDs) and High Bandwidth Memory (HBM3) stacks interposer-mounted together. The 192 GB memory capacity at launch significantly exceeded the NVIDIA H100's 80 GB, making the MI300X competitive for large-language-model inference where model size is the primary constraint — larger memory allows serving larger models without tensor parallelism across multiple GPUs.

The MI300A variant integrates AMD EPYC CPU cores alongside GPU compute dies in a single package — a unified memory architecture (UMA) where CPU and GPU share the same HBM pool. This design reduces CPU-GPU memory copy overhead for HPC workloads but is less suited to pure GPU-intensive AI training.

Both variants use the OAM form factor, allowing system integrators (Supermicro, Dell, HPE, and others) to build 8-GPU nodes. Infinity Fabric provides inter-GPU connectivity within the node.

## Notable Developments

- **2026 (H2):** AMD plans production of the Helios rack built around MI455X, the successor generation.
- **2025-Q4:** AMD reported MI308 shipments to China of about \$390M (reported figure; source not re-fetched).
- **2025-02:** AMD reported record Q4 and full-year 2024 results; Instinct revenue exceeded \$5B for 2024.
- **2025-02:** AMD's FY2024 release names IBM (IBM Cloud) and Vultr as MI300X customers.
- **2023-Q4:** MI300X and MI300A ship to first customers

## Key Organizations

- **AMD** — designer of the Instinct line (CDNA 3)
- **TSMC** — fabricates the GPU and CPU dies
- **IBM, Vultr** — cloud providers announcing MI300X deployments
- **Supermicro, Dell, HPE** — system integrators building OAM-based nodes

## Sources

- [AMD Instinct MI300 Series Product Page](https://www.amd.com/en/products/accelerators/instinct/mi300.html)
- [AMD Reports Fourth Quarter and Full Year 2024 Financial Results](https://newsroom.amd.com/news/amd-reports-fourth-quarter-and-full-year-2024-fina/) — Instinct revenue and MI300X customers
