---
title: "AMD Instinct"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "AMD's GPU accelerator product line for datacenter AI training and inference, spanning MI300 through the MI400-generation Helios rack-scale system."
tags: ["amd", "gpu", "ai-accelerators", "cdna", "rack-scale", "hpc"]
categories: ["overview"]
research_area: "ai-accelerators/amd-instinct"
last_reviewed: 2026-06-07
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

## Overview

AMD Instinct is AMD's line of GPU accelerators for datacenter AI training, inference, and HPC workloads. Built on successive generations of AMD's CDNA architecture, the line runs from the MI200 series through MI300 (shipping 2023–2024), MI350 (shipping 2H 2025), and the forthcoming MI400 generation anchored by the Helios rack-scale system (target H2 2026). AMD competes directly with NVIDIA's Hopper/Blackwell line and positions on memory capacity advantages and open-standards interconnect.

## Entries

- [AMD Instinct — Overview]({{< relref "amd-instinct-overview.md" >}}) — Architecture generations, competitive positioning, and key facts
- [MI300 Series]({{< relref "mi300-series.md" >}}) — MI300X and MI300A: first AMD APU-style unified CPU+GPU accelerator
- [MI350 Series]({{< relref "mi350-series.md" >}}) — MI350X and MI355X: CDNA 4, 288 GB HBM3e, shipping 2H 2025
- [MI400 Series & Helios]({{< relref "mi400-helios.md" >}}) — MI455X-anchored rack-scale system; 72 GPUs, 31 TB HBM4, H2 2026 target
- [ROCm Software Stack]({{< relref "amd-rocm.md" >}}) — AMD's open-source GPU software platform competing with CUDA
- [AMD Pensando Pollara]({{< relref "amd-pensando-pollara.md" >}}) — 400G AI NIC enabling scale-out networking for Instinct clusters
