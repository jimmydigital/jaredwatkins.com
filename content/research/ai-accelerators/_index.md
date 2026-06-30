---
title: "AI Accelerators"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "GPU and AI accelerator hardware for datacenter-scale training and inference, including rack-scale systems and interconnect ecosystems."
research_area: "ai-accelerators"
last_reviewed: 2026-06-07
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

{{<steering>}}

## AI Accelerators Section — Steering Instructions

**Scope:** GPU and AI accelerator hardware for datacenter-scale training and inference. In scope: GPU architectures, rack-scale integrated systems, interconnect fabric (scale-up and scale-out), software stacks (CUDA, ROCm, oneAPI), and the companies supplying these components. Out of scope: edge inference chips for mobile/IoT (track separately), cloud software platforms, model development.

**Editorial focus:** The section should document technical differentiation clearly — architecture generations, memory subsystems, interconnect topologies, rack-scale integration — and avoid becoming a product marketing summary. Compare claims against independent benchmarks (MLPerf) where available.

**Key metrics to track per GPU entry:**
- Architecture generation and process node
- Memory capacity and bandwidth (HBM generation and tier)
- Peak FP4/FP8/FP16/BF16 compute (document precision explicitly)
- Scale-up interconnect bandwidth (NVLink, Infinity Fabric, UALink)
- Scale-out interconnect (NVSwitch, UltraEthernet, InfiniBand)
- Rack-scale form factor: GPU count, aggregate memory, aggregate FLOPS
- TDP / power envelope per GPU and per rack

**Software ecosystem** — document alongside hardware: CUDA lock-in is a real competitive factor; ROCm maturity is a critical adoption barrier for AMD; open standards (UltraEthernet Consortium, UALink) vs. proprietary ecosystems matter for buyer lock-in risk.

**Claim verification:** MLPerf benchmark results are the most reliable independent data points — always cite the version and date. Performance claims in press releases should be flagged as unverified until an MLPerf or independent third-party result is cited.

**Review cadence:** 90 days — this is a fast-moving space with quarterly product announcements.

**Tags:**
- Vendor: `amd`, `nvidia`, `intel`, `google`, `amazon`
- Architecture: `cdna`, `hopper`, `blackwell`, `rubin`, `gaudi`
- Form factor: `rack-scale`, `oam-module`, `pcie-card`
- Interconnect: `nvlink`, `infinity-fabric`, `ualink`, `ultraethernet`, `infiniband`

{{</steering>}}

## Overview

The AI accelerator market is dominated by NVIDIA but increasingly contested by AMD, which has built a competitive rack-scale product line around the Instinct GPU family. Intel's Gaudi line competes at the lower end. All three compete on architecture, memory subsystem, software ecosystem maturity, and increasingly on rack-scale integrated systems that package GPUs, networking, and cooling as a unit.

## Companies

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [AMD](https://finance.yahoo.com/quote/AMD) | [Advanced Micro Devices](https://www.amd.com) | CPUs, GPUs, and AI accelerators (EPYC, Instinct, Radeon) |
| [NVDA](https://finance.yahoo.com/quote/NVDA) | [NVIDIA](https://www.nvidia.com) | Dominant GPU/AI accelerator supplier (H100, B200, Vera Rubin) |
| [INTC](https://finance.yahoo.com/quote/INTC) | [Intel](https://www.intel.com) | CPUs and Gaudi AI accelerators |

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
    "colorTheme": "light",
    "dateRange": "12M",
    "showChart": true,
    "locale": "en",
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "500",
    "tabs": [
      {
        "title": "AI Accelerators",
        "symbols": [
          {"s": "NASDAQ:AMD", "d": "Advanced Micro Devices"},
          {"s": "NASDAQ:NVDA", "d": "NVIDIA"},
          {"s": "NASDAQ:INTC", "d": "Intel"}
        ],
        "originalTitle": "AI Accelerators"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

## Topic Areas

- [AMD Instinct]({{< relref "amd-instinct/_index.md" >}}) — AMD's GPU accelerator line for AI training and inference, from MI300 through Helios rack-scale systems
