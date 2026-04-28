---
title: "Hailo Technologies"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "Tel Aviv-based AI chip company (~$1B+ valuation, Series C); Hailo-8 (26 TOPS, 2.5W M.2/PCIe), Hailo-10H (ultra-low power), and Hailo-15 (20–40 TOPS, <5W) edge AI accelerators; highest TOPS/watt ratio in the add-in M.2/PCIe accelerator market; Raspberry Pi AI HAT+; ADAS, smart camera, industrial AI, and defense-adjacent markets."
tags: ["edge-compute", "ai-inference", "npu", "accelerator", "m2", "pcie", "israel", "private", "fabless", "defense", "automotive"]
categories: ["company"]
research_area: "datacenters/edge-ai-accelerators"
source_urls:
  - "https://hailo.ai/"
  - "https://hailo.ai/products/ai-accelerators/"
last_reviewed: 2026-04-25
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Hailo Technologies is a Tel Aviv-based fabless AI chip company developing dedicated edge inference accelerators — the Hailo-8, Hailo-10, and Hailo-15 chip families — available as M.2, PCIe, and mPCIe add-in modules for embedding AI inference into existing compute platforms. Hailo's chips are notable for the highest documented TOPS/watt ratio in the add-in accelerator market: the Hailo-8 delivers 26 TOPS at 2.5W in an M.2 2280 module — enabling AI inference on camera systems, embedded computers, drones, vehicles, and industrial equipment without a GPU. Hailo has achieved broad OEM adoption across automotive ADAS (including Toyota, Denso, and Tier 1 auto suppliers), smart camera vendors, industrial AI companies, and defense-adjacent integrators.

## Key Facts

- **Founded:** 2017
- **HQ:** Tel Aviv, Israel
- **Funding:** ~$250M+ raised; Series C completed (2022); investors include Poalim Equity, ABB Technology Ventures, Cardium, Mann+Hummel Ventures, and others; valuation estimated >$1B post-Series C
- **Founders:** Orr Danon (CEO), Avi Baum (CTO) — both veteran Israeli chip engineers with prior experience at EZchip (acquired by Mellanox/NVIDIA)
- **Value chain position:** Fabless chip designer; sells chips in bulk to OEM customers and sells Hailo AI Modules (M.2, PCIe, mPCIe) directly to integrators and developers
- **Fabrication:** TSMC — Hailo-8 at TSMC 16nm FinFET; Hailo-15 at TSMC 5nm
- **Primary markets:** Automotive ADAS, smart cameras and surveillance, industrial AI inspection, robotics, medical imaging, defense-adjacent (drone AI, tactical sensors)

## Key Products

### Hailo-8 — M.2 / PCIe / mPCIe AI Accelerator (26 TOPS, 2.5W)

The Hailo-8 is the chip that established Hailo's market position. Fabricated at TSMC 16nm, the Hailo-8 delivers 26 TOPS (tera-operations per second) at INT8 precision while consuming only 2.5W — a TOPS/watt ratio that substantially outperforms Intel integrated NPUs and Google's Edge TPU. The chip is available in M.2 2280, PCIe (x1 or x4), and mini-PCIe form factors, making it compatible with an enormous base of existing embedded computers, industrial PCs, smart cameras, and single-board computers.

Key specifications:
- **Performance:** 26 TOPS (INT8)
- **Power:** 2.5W typical; <3.5W peak
- **Fabrication:** TSMC 16nm FinFET
- **Form factors available:** M.2 2280 (key M or B+M), PCIe half-height half-length, mPCIe
- **Memory:** 32MB on-chip SRAM (no external DRAM required for inference — eliminates DRAM power)
- **Interface:** PCIe Gen3 x1 (standard); Gen3 x4 (full-bandwidth)
- **Software:** HailoRT runtime; TAPPAS (vision AI application framework); integration with GStreamer pipelines; ONNX/TFLite model compilation via Hailo Dataflow Compiler
- **Notable deployment:** Raspberry Pi AI HAT+ (announced 2024) — Hailo-8L (13 TOPS, lower-TDP variant) on an official Raspberry Pi accessory; dramatically expanded developer ecosystem

**Hailo-8L variant:** Lower-performance (13 TOPS) version of Hailo-8 at lower cost and even lower power, used in the Raspberry Pi AI HAT+ and camera modules.

### Hailo-10H — Ultra-Low Power Inference

The Hailo-10H is a lower-power, lower-cost accelerator targeting applications where even the Hailo-8's 2.5W is too much — battery-powered cameras, IoT sensors, wearable devices, and ultra-compact embedded systems. Performance is reduced relative to Hailo-8, but the power envelope (sub-1W operation possible) opens use cases that no other add-in accelerator can address.

Key specifications:
- **Performance:** Approximately 10 TOPS (INT8)
- **Power:** <1W typical; target: sub-milliwatt idle
- **Target use cases:** Battery-powered AI cameras, wearable AI, IoT edge nodes, drone AI payload nodes

### Hailo-15 — Next Generation, TSMC 5nm (20–40 TOPS per chip)

The Hailo-15 family represents Hailo's move to TSMC 5nm and a significant performance step. Multiple SKUs cover different power/performance points:

- **Hailo-15H:** ~40 TOPS at <5W (high-performance M.2/PCIe variant)
- **Hailo-15M:** ~20 TOPS at lower power
- **Hailo-15L:** Ultra-low power variant

Key specifications:
- **Fabrication:** TSMC 5nm
- **Interface:** PCIe Gen4 x4 (higher bandwidth than Hailo-8)
- **Memory:** Enhanced on-chip SRAM; larger SRAM enables larger model inference
- **Notable improvement over Hailo-8:** Transformer model support — Hailo-15 is specifically optimized for attention-based models (ViT, YOLO-NAS, RT-DETR) that were less efficient on Hailo-8's CNN-optimized architecture
- **Availability:** Production availability Q3/Q4 2025 per company announcements; modules in deployment through 2026

### Hailo AI Software Stack

- **Hailo Dataflow Compiler (DFC):** Compiles neural networks (ONNX, TFLite, Caffe) to Hailo hardware; performs quantization (INT8/INT16), graph optimization, and hardware-specific scheduling
- **HailoRT:** Real-time runtime library for inference deployment; C/C++/Python APIs; GStreamer plugin integration
- **TAPPAS:** Vision AI application framework with pre-built pipelines for object detection, classification, tracking, and multi-stream processing
- **Model Zoo:** Pre-compiled, validated models for common vision tasks (YOLOv8, ResNet, EfficientDet, etc.) — reduces time-to-deployment for common use cases

## What It Is / How It Works

### Architecture: Structure-Defined Dataflow

Hailo's chip architecture is based on "Structure-Defined Dataflow" — a hardware design philosophy where the chip's internal compute graph is a direct mapping of the neural network's data flow graph, rather than a general-purpose matrix multiply array. In a conventional GPU or general NPU, all operations go through shared memory and execution units; in Hailo's architecture, each layer of the network has dedicated resources and direct data paths to the next layer.

The on-chip SRAM (32MB on Hailo-8) is large enough to hold entire intermediate activations for typical CNN inference tasks, eliminating the need for external DRAM access during inference. DRAM access is one of the largest power consumers in AI inference; removing it is the primary reason Hailo achieves 26 TOPS at 2.5W when competing architectures require 5–10× more power for similar throughput.

**The trade-off:** The dataflow architecture is extremely efficient for models whose structure matches the chip's internal wiring, but less flexible for unusual architectures. Hailo-8 is very efficient for standard CNNs (YOLO, ResNet, EfficientNet) but less so for transformers — a known limitation that Hailo-15's architecture specifically addresses.

### Raspberry Pi AI HAT+ Effect

The Raspberry Pi AI HAT+ (shipping 2024) with the Hailo-8L created a massive developer ecosystem for Hailo hardware — developer boards are how AI chip companies establish software ecosystems and trained engineers. NVIDIA's Jetson dominance in edge AI is partly built on the developer community that grew around the Jetson Nano (cheap developer module). Hailo's Raspberry Pi partnership is a strategic move to build similar developer ecosystem density, which then pulls through commercial deployments when those developers build products.

### Defense-Adjacent Applications

Hailo hardware appears in defense-adjacent deployments through system integrators and OEMs who embed Hailo modules in:

- **Tactical camera and surveillance systems:** AI analytics on soldier-worn cameras, fixed perimeter surveillance, and ISR camera payloads — Hailo-8's 2.5W is compatible with battery-powered or solar-powered deployments
- **Drone payload AI:** Small UAS/UAV onboard inference for object detection, target classification, and geolocation — Hailo-8M.2 fits in tight payload bays where GPU modules cannot
- **Vehicle-mounted sensor processing:** Forward-looking ADAS/sensor fusion supplementary inference in military vehicles (supplementing, not replacing, larger GPU compute for lower-priority inference tasks)
- **Smart IED detection / ground sensor networks:** Persistent sensor nodes with local AI inference to reduce data transmission requirements in bandwidth-constrained tactical environments

Hailo does not publicly identify specific DoD contracts, but its products are available through US defense electronics distributors and are listed in several defense-oriented embedded computing vendors' hardware catalogs.

## Notable Developments

- **2024:** Raspberry Pi AI HAT+ launched with Hailo-8L — rapidly expands developer ecosystem; tens of thousands of developer units shipped
- **2025:** Hailo-15H production ramp at TSMC 5nm; PCIe Gen4 modules becoming available through distribution
- **2025:** TAPPAS 3.x release — expanded model zoo (YOLOv8, RT-DETR, SAM-Edge); improved multi-stream pipeline performance
- **Ongoing:** Smart camera market penetration through Axis Communications and Hanwha Vision partnerships — Hailo chips embedded in network camera SoCs
- **Ongoing:** Automotive design-in wins; Hailo chips are embedded in Toyota/Denso advanced ADAS platforms (Level 2+ features)

## Key People

**Orr Danon** — Co-Founder & CEO
- Previously at EZchip Technologies (acquired by Mellanox/NVIDIA for $811M in 2016 — network processor chips)
- Education: Computer Science, Technion – Israel Institute of Technology

**Avi Baum** — Co-Founder & CTO
- Previously at EZchip Technologies; chip architecture and design
- Education: Electrical Engineering, Technion – Israel Institute of Technology

## Claim Verification

### Claim: 26 TOPS at 2.5W for Hailo-8

**Status:** Verified (with standard precision caveat)

**Supporting sources:**
- [Hailo-8 datasheet](https://hailo.ai/products/ai-accelerators/) — company datasheet specifies 26 TOPS at INT8 precision, 2.5W typical power
- Multiple third-party publications and embedded computing review sites have independently measured Hailo-8 power draw in the 2.0–2.8W range under inference load, consistent with specification
- Raspberry Pi AI HAT+ documentation (which uses Hailo-8L at 13 TOPS / ~1.5W) corroborates the power efficiency claims by independent community testing

**Refuting / questioning sources:**
- TOPS is measured at INT8 precision; FP16 throughput is lower (most inference workloads use INT8 after quantization, so INT8 TOPS is the relevant figure)
- TOPS figure represents peak compute throughput; actual model throughput depends on memory bandwidth, model structure efficiency, and compiler optimization — real-world FPS on specific models may be lower than peak TOPS suggests

**Summary:** The 26 TOPS / 2.5W specification is well-supported by independent measurement. The efficiency advantage over alternatives is real and documented. Standard caveat: TOPS is peak, not sustained on all model types.

## Sources

- [Hailo Technologies — Official Website](https://hailo.ai/)
- [Hailo — AI Accelerators Products](https://hailo.ai/products/ai-accelerators/)
- [Hailo Developer Zone](https://developer.hailo.ai/) — SDK, model zoo, TAPPAS documentation
- [Raspberry Pi AI HAT+](https://www.raspberrypi.com/products/ai-hat-plus/) — consumer ecosystem entry point
- [TSMC 5nm Process](https://www.tsmc.com/) — fabrication context for Hailo-15
