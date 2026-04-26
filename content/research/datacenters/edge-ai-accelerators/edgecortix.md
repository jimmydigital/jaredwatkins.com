---
title: "EdgeCortix"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "Tokyo-based fabless AI chip startup; SAKURA-I and SAKURA-II edge AI accelerator chips and PCIe/M.2 modules; Dynamic Neural Accelerator (DNA) CGRA architecture; 15–40+ TOPS at 10–25W targeting defense, autonomous vehicles, robotics, and industrial AI inference; TSMC 12nm fabrication."
tags: ["edge-compute", "ai-inference", "npu", "accelerator", "m2", "pcie", "japan", "private", "fabless", "defense"]
categories: ["company"]
research_area: "datacenters/edge-ai-accelerators"
source_urls:
  - "https://www.edgecortix.com/"
  - "https://www.edgecortix.com/en/products"
last_reviewed: 2026-04-25
stale_after_days: 180
---

## Summary

EdgeCortix is a Tokyo-headquartered (with US presence in Santa Clara) fabless semiconductor startup developing dedicated AI inference accelerator chips and add-in modules for edge deployments. The company's flagship product line is the SAKURA series — PCIe and M.2 AI accelerator cards built on its proprietary Dynamic Neural Accelerator (DNA) chip architecture. EdgeCortix targets applications where GPU-class inference performance is needed but GPU power consumption and size are prohibitive: defense embedded compute, unmanned systems, autonomous vehicles, robotics, and industrial AI. The company has positioned SAKURA specifically for defense and security markets, with a US DoD / NATO ally customer focus.

## Key Facts

- **Founded:** 2019
- **HQ:** Tokyo, Japan (US office: Santa Clara, CA)
- **Funding stage:** Private; Series B funding completed (total raised approximately $30M+; investors include SBI Investment, AIST Solutions, and defense/industrial VCs)
- **Founders:** Hassan Inoue (CEO) — prior experience at academic AI research (University of Toronto); Sakyasingha Dasgupta (CTO) — prior at RIKEN Brain Science Institute
- **Value chain position:** Fabless chip designer; sells chips and accelerator modules to OEMs and system integrators
- **Fabrication:** TSMC 12nm FinFET
- **Primary markets:** Defense/intelligence (ISR, drone onboard AI, tactical C4ISR), autonomous vehicles, robotics, industrial AI inspection
- **Key differentiator:** Dynamic Neural Accelerator (DNA) architecture — CGRA (Coarse-Grained Reconfigurable Array) based; claims superior performance-per-watt vs. conventional fixed-dataflow NPUs for diverse neural network topologies

## Key Products

### SAKURA-I — First Generation CGRA Accelerator

The SAKURA-I was EdgeCortix's first-generation production accelerator chip, implemented in TSMC 12nm FinFET. SAKURA-I is available in PCIe card and M.2 module form factors, targeting embedded computers, industrial PCs, and network appliances with free PCIe or M.2 slots.

Key specifications:
- **Architecture:** DNA (Dynamic Neural Accelerator) CGRA
- **Performance:** ~15 TOPS at INT8 precision
- **Power:** ~10W TDP (PCIe card); ~5W M.2 variant
- **Form factor:** PCIe x4 half-height half-length card; M.2 2280 module
- **Memory:** On-chip SRAM + external LPDDR
- **Interface:** PCIe Gen3 x4
- **Software:** EdgeCortix MERA compiler/SDK; ONNX, PyTorch, TensorFlow frontend support

### SAKURA-II — Second Generation, Defense-Optimized

SAKURA-II is the second-generation EdgeCortix accelerator, representing a significant performance step over SAKURA-I. EdgeCortix has positioned SAKURA-II explicitly for defense and security applications, citing deployments in military ISR, drone payload processing, and tactical AI at the edge.

Key specifications:
- **Architecture:** DNA (second generation, enhanced CGRA)
- **Performance:** 40+ TOPS at INT8 precision (company-cited figure)
- **Power:** <25W (PCIe card); M.2 variant with lower TDP
- **Form factor:** PCIe x8 full-height half-length; M.2 2280 (lower-power variant)
- **Interface:** PCIe Gen4 x8
- **Memory:** Higher-bandwidth external memory vs. SAKURA-I
- **Software:** MERA 2.x compiler with expanded model support and quantization-aware training integration

### MERA Software Stack

The MERA (Model Efficiency and Run-time Architecture) SDK is EdgeCortix's compiler and runtime software that maps neural networks from standard ML frameworks (ONNX, TensorFlow, PyTorch) onto SAKURA silicon. MERA performs graph optimization, operator fusion, quantization (INT8/FP16), and hardware-specific kernel compilation.

MERA's design philosophy addresses a key pain point with proprietary NPU hardware: portability. Many edge NPU vendors require customers to rewrite models for the specific chip's operator set. MERA accepts standard ONNX models and handles the hardware translation — reducing the engineering burden for deploying existing trained models onto SAKURA hardware.

## What It Is / How It Works

### DNA Architecture — CGRA vs. Fixed Dataflow

Most edge AI accelerators (including early Hailo designs and Google's Edge TPU) use fixed dataflow architectures: the chip's internal data movement paths are hardwired for specific layer types (convolution, attention, etc.). This achieves maximum efficiency for workloads that match the fixed topology but degrades for workloads that don't.

EdgeCortix's DNA architecture is a Coarse-Grained Reconfigurable Array (CGRA): the compute fabric's internal connectivity and data routing are programmable (reconfigurable) at inference time. This means the hardware can dynamically adapt its internal computation graph to match the specific structure of whatever neural network is being run — convnets, transformers, graph neural networks, and hybrid architectures all map efficiently rather than only one class of network.

The claimed benefit is versatility across diverse model types with less performance degradation for non-standard architectures. The practical implication for defense customers is that SAKURA hardware can run a wider range of AI models (object detection, target classification, signals intelligence CNNs, multi-modal fusion models) with consistent performance rather than peaking on one topology and degrading on others.

### Defense Focus

EdgeCortix has made defense and intelligence a primary target market. The rationale is alignment between SAKURA's properties and defense requirements:

- **SWaP:** Defense tactical systems face strict size, weight, and power constraints. SAKURA's M.2 form factor at 5–10W is viable in platforms where a 75W GPU is not.
- **Model diversity:** Military AI applications span object detection (visual ISR), radar waveform classification (SIGINT), acoustic classification (sonar/ACINT), and sensor fusion — diverse model architectures that benefit from CGRA flexibility.
- **Onboard vs. cloud:** US DoD policy pushes for contested environment operation without cloud connectivity; onboard inference on SAKURA hardware eliminates that dependency.
- **Supply chain:** Japan-based company with TSMC fabrication — outside the Chinese supplier restrictions of NDAA Section 889; eligible for US government procurement.

EdgeCortix has reported engagement with US DoD programs and NATO ally defense customers, though specific contract details are not publicly disclosed as of April 2026.

## Claim Verification

### Claim: 40+ TOPS at <25W for SAKURA-II

**Status:** Partially verified

**Supporting sources:**
- [EdgeCortix product documentation](https://www.edgecortix.com/en/products) — company publishes SAKURA-II performance figures; TSMC 12nm fabrication baseline is consistent with competitive NPU performance in this range

**Refuting / questioning sources:**
- No independent third-party benchmark of SAKURA-II has been identified from public sources; figure is from EdgeCortix marketing materials
- CGRA architecture performance advantage over fixed dataflow NPUs is a theoretical claim dependent on workload; benchmarks on standard vision models (ImageNet, COCO) versus specialized military AI models may differ

**Summary:** The 40+ TOPS figure is plausible for a 12nm CGRA at this power level; the architecture versatility claim is theoretically well-founded but no public head-to-head benchmark against Hailo-15 or Intel NPU has been found.

## Sources

- [EdgeCortix — Official Website](https://www.edgecortix.com/)
- [EdgeCortix — Products (SAKURA)](https://www.edgecortix.com/en/products)
- [EdgeCortix MERA SDK](https://www.edgecortix.com/en/mera) — compiler and runtime documentation
- [TSMC 12nm Process](https://www.tsmc.com/) — fabrication node context
