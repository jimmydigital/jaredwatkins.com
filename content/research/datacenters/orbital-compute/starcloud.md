---
title: "Starcloud"
date: 2026-04-29
lastmod: 2026-04-29
draft: false
description: "Seattle-area startup building and operating orbital data centers; first to train an LLM in space; YC unicorn at $1.1B valuation after Series A in March 2026."
research_area: "datacenters/orbital-compute"
source_urls:
  - "https://www.starcloud.com/"
  - "https://techcrunch.com/2026/03/30/starcloud-raises-170-million-series-ato-build-data-centers-in-space/"
  - "https://www.cnbc.com/2025/12/10/nvidia-backed-starcloud-trains-first-ai-model-in-space-orbital-data-centers.html"
  - "https://www.geekwire.com/2026/orbital-ai-seattle-area-startup-starcloud-hits-1-1b-valuation-to-build-space-based-data-centers/"
  - "https://blogs.nvidia.com/blog/starcloud/"
  - "https://nvidianews.nvidia.com/news/space-computing"
last_reviewed: 2026-04-29
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Starcloud (formerly Lumen Orbit) is a Redmond, Washington startup building commercial orbital data centers. In November 2025, it launched Starcloud-1 — the first satellite to carry a high-performance GPU (NVIDIA H100 class) — and subsequently became the first company to train a large language model in space. It raised a $170M Series A at a $1.1B valuation in March 2026, becoming the fastest YC company to reach unicorn status (17 months post-YC). Starcloud-2, with multiple Blackwell GPUs and an AWS server blade, is planned for October 2026.

## Key Facts

- **Founded:** January 2024 (as Lumen Orbit); rebranded Starcloud March 2025
- **HQ:** Redmond, WA, USA
- **Type:** Company — orbital data center operator
- **Status:** Active — commercial operations from Starcloud-1; Starcloud-2 planned Oct 2026
- **Funding:** ~$200M total raised; Series A ($170M) led by Benchmark and EQT Ventures, March 2026; seed rounds totaling ~$34M in 2024–2025
- **Valuation:** $1.1B (March 2026)
- **Investors:** Benchmark, EQT Ventures, NFX, Y Combinator, FUSE, Soma Capital, Andreessen Horowitz (scout), Sequoia (scout), NVIDIA (Inception program)
- **Key metric:** First LLM trained in space (Nov 2025); first high-power GPU in orbit (100× more powerful than prior space GPUs)
- **FCC filing:** Feb 2026 proposal for constellation of up to 88,000 orbital data center satellites

## What It Is / How It Works

Starcloud designs, builds, and operates satellites that carry commercial GPU and server hardware in LEO, offering the resulting compute capacity as a cloud service. The founding thesis is that solar power in orbit is abundant, continuous, and free — eliminating the power-purchase and grid-interconnection bottlenecks facing terrestrial AI data centers — while vacuum-based passive thermal management eliminates cooling overhead. Launch costs are the primary economic barrier, which Starcloud bets will fall with Starship scale-up.

Starcloud-1, launched November 2025 aboard a SpaceX Falcon 9, carried an NVIDIA H100-class GPU — described as approximately 100× more capable than any prior GPU flown to space. On-orbit, the satellite ran inference on Google DeepMind's Gemma model (a version of Gemini) and trained nanoGPT (Andrej Karpathy's LLM) on the complete works of Shakespeare, achieving the first in-space LLM training run. The satellite communicates to ground via radio links; optical ISLs are planned for future satellites.

Starcloud-2, targeted for October 2026, adds multiple NVIDIA Blackwell GPUs, an AWS server blade, and a Bitcoin mining computer — the last reflecting the company's multi-workload revenue diversification strategy. The company has also proposed a constellation of up to 88,000 satellites to the FCC, which would substantially exceed current Starlink constellation size.

The company was originally founded as Lumen Orbit. Following a trademark challenge from Lumen Technologies (the fiber network operator), it rebranded to Starcloud in March 2025.

## Notable Developments

- **2026-03:** Raised $170M Series A led by Benchmark and EQT Ventures at $1.1B valuation; fastest YC unicorn (17 months post-program)
- **2026-02:** Filed FCC proposal for constellation of up to 88,000 orbital data center satellites
- **2025-12:** Announced first in-space LLM training (nanoGPT on Shakespeare corpus) and first inference of Gemma on-orbit
- **2025-11:** Launched Starcloud-1 on SpaceX Falcon 9 with NVIDIA H100-class GPU — first high-performance GPU in orbit
- **2025-03:** Rebranded from Lumen Orbit to Starcloud following trademark challenge from Lumen Technologies; raised additional seed funding (total ~$34M)
- **2024-12:** Raised $11M seed round (NFX, YC, FUSE, Soma Capital, a16z scout, Sequoia scout); 200 VCs reportedly competed for allocation
- **2024-10:** Raised initial $10M; announced NVIDIA Inception partnership

## Key People

- **Philip Johnston** — Co-founder and CEO
  - LinkedIn: https://www.linkedin.com/in/philip-johnston-b0b0b0/ — TODO: verify correct slug
  - Previous: McKinsey & Company
- **Adi Oltean** — Co-founder and CTO
  - LinkedIn: https://www.linkedin.com/in/adiaoltean/ — TODO: verify correct slug
  - Previous: SpaceX; Microsoft Azure
  - **⚑ Overlap:** Previously at SpaceX — relevant to SpaceX orbital data center competitive context
- **Ezra Feilden** — Co-founder
  - LinkedIn: not confirmed — TODO: verify
  - Previous: Airbus Defence and Space

### People — Last Reviewed: 2026-04-29

## Claim Verification

### Claim: Starcloud-1 carried the first high-performance GPU in space, "100× more powerful than any prior space GPU"

**Status:** Partially verified

**Supporting sources:**
- [CNBC: Nvidia-backed Starcloud trains first AI model in space](https://www.cnbc.com/2025/12/10/nvidia-backed-starcloud-trains-first-ai-model-in-space-orbital-data-centers.html) — confirms H100-class GPU launch and the 100× claim
- [NVIDIA Newsroom: Space Computing](https://nvidianews.nvidia.com/news/space-computing) — NVIDIA's own framing of the milestone

**Refuting / questioning sources:**
- The "100×" figure is a Starcloud/NVIDIA marketing claim; no independent hardware-level verification published; prior space GPU baselines are not explicitly cited

**Summary:** The Starcloud-1 H100-class GPU is almost certainly the most powerful GPU launched to LEO to date; the exact multiple is unverified and likely a rounded comparison against Jetson/Xavier-class edge GPUs previously flown.

### Claim: First LLM trained in space

**Status:** Verified (with caveats on scope)

**Supporting sources:**
- [CNBC coverage](https://www.cnbc.com/2025/12/10/nvidia-backed-starcloud-trains-first-ai-model-in-space-orbital-data-centers.html) — confirmed nanoGPT training on Shakespeare corpus
- [NVIDIA blog](https://blogs.nvidia.com/blog/starcloud/) — corroborates the training run

**Refuting / questioning sources:**
- nanoGPT on a small corpus is a toy training run, not training a production-scale foundation model; the claim is technically accurate but narrow in scope

**Summary:** Verified as the first in-orbit GPU training run; the LLM itself (nanoGPT on Shakespeare) is a demonstration, not a frontier model.

## Sources

- [Starcloud official site](https://www.starcloud.com/)
- [TechCrunch: Starcloud raises $170M Series A](https://techcrunch.com/2026/03/30/starcloud-raises-170-million-series-ato-build-data-centers-in-space/)
- [CNBC: First LLM trained in space](https://www.cnbc.com/2025/12/10/nvidia-backed-starcloud-trains-first-ai-model-in-space-orbital-data-centers.html)
- [GeekWire: Starcloud unicorn](https://www.geekwire.com/2026/orbital-ai-seattle-area-startup-starcloud-hits-1-1b-valuation-to-build-space-based-data-centers/)
- [NVIDIA Blog: How Starcloud Is Bringing Data Centers to Outer Space](https://blogs.nvidia.com/blog/starcloud/)
- [NVIDIA Newsroom: Space Computing](https://nvidianews.nvidia.com/news/space-computing)
