---
title: "AMD Pensando Pollara 400 AI NIC"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "AMD's 400G AI network interface card for scale-out AI cluster networking, UltraEthernet Consortium compliant, deployed in Instinct MI350 and MI400 infrastructure."
tags: ["amd", "networking", "nic", "ultraethernet", "rdma", "ai-accelerators", "us"]
categories: ["technology"]
research_area: "ai-accelerators/amd-instinct"
source_urls:
  - "https://www.amd.com/en/products/network-interface-cards/pensando.html"
  - "https://www.amd.com/en/blogs/2025/powering-next-gen-ai-infrastructure--a-new-era-of.html"
  - "https://hc2025.hotchips.org/assets/program/conference/day1/HC%20Pollara%20400%20Final%2020250824.pdf"
last_reviewed: 2026-06-07
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The AMD Pensando Pollara 400 is a 400G AI Network Interface Card designed for scale-out networking in large GPU clusters. It implements the UltraEthernet Consortium (UEC) specification — adding RDMA semantics, lossless transport, and AI-traffic-optimized congestion control on top of standard Ethernet physical layer. It is AMD's answer to NVIDIA's ConnectX/BlueField InfiniBand NICs and is the scale-out fabric component for AMD Instinct MI350 and MI400/Helios clusters. AMD acquired Pensando Systems in 2022 for $1.9B; the Pollara product line is the AI-specific output of that acquisition.

## Key Facts

- **Developer:** AMD (Pensando division; acquired 2022 for ~$1.9B)
- **Speed:** 400 Gbps per NIC
- **Standard:** UltraEthernet Consortium (UEC) compliant
- **RDMA protocol:** RoCEv2-compatible with UEC extensions for AI workloads
- **Primary use case:** Scale-out interconnect for GPU clusters (rack-to-rack, cluster-to-cluster)
- **Integration:** PCIe interface to host; RDMA over Ethernet for cluster fabric
- **Deployment:** First customer shipments to major cloud service providers (timing not publicly confirmed)
- **Status:** Deployment phase (2025)

## What It Is / How It Works

Large GPU clusters require two distinct networking layers:

1. **Scale-up:** High-bandwidth, low-latency connections *within* a rack or node group — handled by NVLink (NVIDIA) or AMD Infinity Fabric/UALink (AMD Instinct). This is GPU-to-GPU traffic for all-reduce and gradient synchronization within a training job's GPU pool.

2. **Scale-out:** Connections *between* racks and across clusters — handled by the network fabric. This is where the Pollara 400 operates.

InfiniBand has traditionally dominated HPC scale-out because it provides RDMA (Remote Direct Memory Access) — allowing GPU memory to be transferred between nodes without CPU involvement, at low latency. NVIDIA's acquisition of Mellanox (2020) gave it end-to-end control of the dominant InfiniBand stack.

UltraEthernet Consortium (UEC) is the industry response: a set of extensions to standard Ethernet that add RDMA semantics, adaptive routing, and lossless transport optimized for AI collective communication patterns (all-reduce, all-to-all). Because it runs on standard Ethernet switching hardware, it removes the requirement for specialized InfiniBand switches and the associated vendor dependency.

The Pollara 400 implements UEC in silicon, providing the NIC-side intelligence (RDMA, congestion control, packet retransmission) while allowing operators to use standard 400G Ethernet switches from any vendor.

In the Helios rack architecture, Pollara 400 NICs handle the 43 TB/s of aggregate scale-out Ethernet bandwidth between racks and to broader cluster fabric. Within the rack, UALink handles GPU-to-GPU scale-up.

## Notable Developments

- **2025-08:** AMD presents Pollara 400 architecture at Hot Chips 2025 (full technical paper published)
- **2025:** Pollara 400G AI NIC enters deployment phase; first shipments to major cloud service providers
- **2025:** AMD blog post frames Pollara as enabling "largest scale-out infrastructure" without dependency on large-buffer InfiniBand switching fabric
- **2022:** AMD acquires Pensando Systems for ~$1.9B — the DPU/SmartNIC company whose silicon became the Pollara product line

## Sources

- [AMD Pensando Pollara NIC Product Page](https://www.amd.com/en/products/network-interface-cards/pensando.html)
- [AMD Blog — Scale-out AI infrastructure with Pensando NICs](https://www.amd.com/en/blogs/2025/powering-next-gen-ai-infrastructure--a-new-era-of.html)
- [Hot Chips 2025 — Pollara 400 Architecture Paper](https://hc2025.hotchips.org/assets/program/conference/day1/HC%20Pollara%20400%20Final%2020250824.pdf)
