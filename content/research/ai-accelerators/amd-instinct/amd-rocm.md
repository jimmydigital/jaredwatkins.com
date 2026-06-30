---
title: "ROCm — AMD GPU Software Platform"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "AMD's open-source GPU software stack for AI and HPC workloads, competing with CUDA. Includes HIP (CUDA compatibility layer), ROCm runtime, and AI libraries."
research_area: "ai-accelerators/amd-instinct"
source_urls:
  - "https://www.amd.com/en/products/software/rocm.html"
  - "https://www.storagereview.com/news/amd-instinct-mi355x-achieves-mlperf-inference-v6-0-gains-with-over-1-million-tokens-per-second-and-supports-scalable-rocm-stack"
  - "https://www.amd.com/en/newsroom/press-releases/2025-6-12-amd-unveils-vision-for-an-open-ai-ecosystem-detai.html"
last_reviewed: 2026-06-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

ROCm (Radeon Open Compute) is AMD's open-source software platform for GPU computing on Instinct accelerators. It is AMD's primary competitive response to NVIDIA's CUDA ecosystem — the dominant and deeply entrenched GPU computing stack. ROCm includes HIP (Heterogeneous Interface for Portability), a CUDA-compatible API layer that allows CUDA code to be ported to AMD GPUs with minimal modification. Ecosystem maturity relative to CUDA remains AMD's single biggest adoption barrier, though ROCm 7 (2025) substantially narrowed the gap for AI workloads.

## Key Facts

- **Developer:** AMD (open-source; GitHub: ROCm/ROCm)
- **License:** Open-source (mixed: Apache 2.0, MIT, others per component)
- **Current version:** ROCm 7 (released 2025)
- **Primary language:** C++, HIP (C++ dialect)
- **CUDA compatibility:** HIP API — CUDA code can be "hipified" to run on AMD GPUs
- **Framework support:** PyTorch (primary), TensorFlow, JAX, ONNX Runtime
- **Key libraries:** rocBLAS (BLAS), MIOpen (deep learning), hipBLAS, rocRAND, rocFFT
- **Supported hardware:** Instinct MI200, MI300, MI350 series; limited Radeon support
- **Inference stack:** vLLM (AMD-optimized fork), TGI (Text Generation Inference), Triton
- **Status:** Active development; production-ready for major AI training frameworks

## What It Is / How It Works

ROCm is a full software stack from GPU driver to high-level AI libraries. Its architecture roughly mirrors CUDA:

- **Driver layer:** AMD GPU kernel drivers (amdgpu) integrated into the Linux kernel
- **Runtime layer:** HIP runtime — provides CUDA-like API semantics for kernel launches, memory management, and device queries
- **Math libraries:** rocBLAS, rocSPARSE, rocFFT — AMD implementations of standard HPC linear algebra primitives
- **AI libraries:** MIOpen (analogous to cuDNN) — provides convolutions, attention mechanisms, and activation functions optimized for AMD hardware
- **Inference server:** AMD maintains an optimized vLLM fork supporting MI300/MI350 and provides container-based deployment via AMD's AI software distribution

**HIP (Heterogeneous Interface for Portability):** HIP is AMD's CUDA compatibility layer. CUDA source files can be converted with the `hipify` tool, replacing CUDA-specific APIs with HIP equivalents. For many PyTorch and standard AI training workloads, hipification is straightforward. The gap appears in CUDA-specific extensions, custom kernels, and PTX (NVIDIA's parallel thread execution IR) — these require AMD-specific rewrites.

**ROCm 7 (2025) improvements:** ROCm 7 added support for FP6 and FP4 data types (required for MI350/MI400 inference workloads), improved distributed inference via open-source framework support, and enhanced enterprise tooling for MLOps orchestration and endpoint management.

## Ecosystem Gap vs. CUDA

CUDA's competitive moat is its depth of ecosystem, not its underlying technical architecture. CUDA has been the dominant GPU computing platform for over 15 years; it has:

- Wider ISV and library support (cuDNN, cuBLAS, NCCL, Thrust, thousands of CUDA-native applications)
- More extensive documentation and community knowledge base
- Tighter integration with popular ML frameworks (PyTorch, JAX — both developed with CUDA as the primary target)
- More custom CUDA kernels written by AI labs — these require porting effort to run on ROCm

For standard training workloads using PyTorch with off-the-shelf models, ROCm maturity is now sufficient for production use. For frontier model training with custom CUDA kernels (common at major AI labs), the porting burden remains a real cost. AMD's OpenAI partnership is partly a signal that at least one frontier lab has committed resources to ROCm compatibility.

## Notable Developments

- **2026-05:** MI355X achieves >1M tokens/second in MLPerf Inference 6.0 using ROCm stack — demonstrates production-quality inference performance
- **2026-06:** AMD unveils "open AI ecosystem" strategy at Advancing AI 2025; positions ROCm and open interconnect standards (UALink, UltraEthernet) as unified alternative to NVIDIA's proprietary stack
- **2025:** ROCm 7 released with FP4/FP6 support, improved framework compatibility, and expanded inference tooling
- **2025:** AMD MI355X listed as generally available on Oracle Cloud Infrastructure — first major public cloud with MI355X-based ROCm instances

## Sources

- [AMD ROCm Product Page](https://www.amd.com/en/products/software/rocm.html)
- [AMD Advancing AI 2025 — Open Ecosystem Announcement](https://www.amd.com/en/newsroom/press-releases/2025-6-12-amd-unveils-vision-for-an-open-ai-ecosystem-detai.html)
- [StorageReview — MI355X MLPerf ROCm stack](https://www.storagereview.com/news/amd-instinct-mi355x-achieves-mlperf-inference-v6-0-gains-with-over-1-million-tokens-per-second-and-supports-scalable-rocm-stack)
