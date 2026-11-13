---
title: "AMD Pensando Pollara 400 AI NIC"
date: 2026-06-07
lastmod: 2026-11-12
draft: false
description: "AMD's 400G AI network interface card for scale-out AI cluster networking, UltraEthernet Consortium (UEC) ready, intended for Instinct MI350 and MI400 infrastructure."
research_area: "ai-accelerators/amd-instinct"
source_urls:
  - "https://www.amd.com/en/products/network-interface-cards/pensando.html"
  - "https://www.amd.com/en/blogs/2025/powering-next-gen-ai-infrastructure--a-new-era-of.html"
  - "https://hc2025.hotchips.org/assets/program/conference/day1/HC%20Pollara%20400%20Final%2020250824.pdf"
last_reviewed: 2026-11-12
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The AMD Pensando Pollara 400 is a 400G AI Network Interface Card designed for scale-out networking in large GPU clusters. AMD describes it as UEC-ready: it implements UEC-style transport features — adding RDMA semantics, lossless transport, and AI-traffic-optimized congestion control on top of standard Ethernet physical layer. It is AMD's answer to NVIDIA's ConnectX/BlueField InfiniBand NICs and is the scale-out fabric component for AMD Instinct MI350 and MI400/Helios clusters. AMD completed its acquisition of Pensando Systems on 26 May 2022 for about \$1.9B; the Pollara product line is the AI-specific output of that acquisition.

## Key Facts

- **Developer:** AMD (Pensando division; acquired 2022 for ~\$1.9B)
- **Speed:** 400 Gbps per NIC
- **Standard:** UEC-ready (AMD wording); UEC AI transport features per the Hot Chips 2025 deck
- **RDMA protocol:** RoCEv2-compatible with UEC features: multipath packet spraying with out-of-order reception, programmable congestion control (NSCC) and selective-ACK loss recovery, without requiring PFC in the switch
- **Silicon:** Programmable P4 pipeline (eight stages, each with four match processing units); PCIe Gen5 x16 host interface; multi-speed MAC rated at 400 Gbps
- **Primary use case:** Scale-out interconnect for GPU clusters (rack-to-rack, cluster-to-cluster)
- **Integration:** PCIe interface to host; RDMA over Ethernet for cluster fabric
- **Deployment:** Shipping since April 2025 (AMD-reported)
- **Successor:** Pensando Vulcano 800G NIC for Helios (announced 2026)
- **Status:** In deployment

## What It Is / How It Works

Large GPU clusters require two distinct networking layers:

1. **Scale-up:** High-bandwidth, low-latency connections *within* a rack or node group — handled by NVLink (NVIDIA) or AMD Infinity Fabric/UALink (AMD Instinct). This is GPU-to-GPU traffic for all-reduce and gradient synchronization within a training job's GPU pool.

2. **Scale-out:** Connections *between* racks and across clusters — handled by the network fabric. This is where the Pollara 400 operates.

InfiniBand has traditionally dominated HPC scale-out because it provides RDMA (Remote Direct Memory Access) — allowing GPU memory to be transferred between nodes without CPU involvement, at low latency. NVIDIA's acquisition of Mellanox (2020) gave it end-to-end control of the dominant InfiniBand stack.

UltraEthernet Consortium (UEC) is the industry response: a set of extensions to standard Ethernet that add RDMA semantics, adaptive routing, and lossless transport optimized for AI collective communication patterns (all-reduce, all-to-all). Because it runs on standard Ethernet switching hardware, it removes the requirement for specialized InfiniBand switches and the associated vendor dependency.

The Pollara 400 implements UEC-style transport features in a programmable P4 pipeline, providing the NIC-side intelligence (RDMA, congestion control, packet retransmission) while allowing operators to use standard 400G Ethernet switches from any vendor.

In the Helios rack architecture, AMD's July 2026 description pairs Pensando Vulcano 800G NICs with MI455X GPUs for scale-out: about 2.4 Tbps of scale-out bandwidth per GPU using three NICs per GPU, across a 72-GPU rack. Within the rack, UALink handles GPU-to-GPU scale-up.

**Performance claims:** AMD's Hot Chips 2025 material claims up to 1.25x performance and roughly 1.25x–1.4x RCCL all-reduce versus RoCEv2 (about 25% average on 4 queue pairs). The test was AMD-internal: 16 MI300X GPUs across two nodes with 16 Pollara NICs and a Broadcom Tomahawk 4 leaf switch, averaged over at least eight runs on 28 April 2025. Other percentage figures in AMD materials are modeled, not measured; treat all as vendor claims.

## Notable Developments

- **2026-07:** AMD details Pensando Vulcano 800G NICs for Helios, MI455X racks (about 2.4 Tbps per GPU, three NICs per GPU).
- **2025-08:** AMD presents the Pollara 400 architecture at Hot Chips 2025.
- **2025-04:** AMD reports Pollara 400 shipments.
- **2022-05:** AMD completes its acquisition of Pensando Systems for about \$1.9B — the DPU/SmartNIC company whose silicon became the Pollara product line.

## Key Organizations

- **AMD (Pensando division)** — designer of Pollara and Vulcano NICs
- **Ultra Ethernet Consortium** — defines the UEC specification
- **UALink Consortium** — defines the scale-up interconnect used inside Helios racks
- **Broadcom** — Tomahawk 4 switch used in AMD's test setup

## Sources

- [AMD Pensando Pollara NIC Product Page](https://www.amd.com/en/products/network-interface-cards/pensando.html)
- [AMD Blog — Scale-out AI infrastructure with Pensando NICs](https://www.amd.com/en/blogs/2025/powering-next-gen-ai-infrastructure--a-new-era-of.html)
- [Hot Chips 2025 — Pollara 400 Architecture Paper](https://hc2025.hotchips.org/assets/program/conference/day1/HC%20Pollara%20400%20Final%2020250824.pdf)
