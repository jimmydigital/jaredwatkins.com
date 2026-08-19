---
title: "Salad"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Utah-based consumer-GPU marketplace (SaladCloud) that pays gamers and other 'everyday' PC owners for idle GPU cycles via a desktop client, then auto-schedules AI inference and batch workloads onto that residential hardware using a proprietary trust-rating system — the most literal 'local AI compute' marketplace in this section, sourcing supply from individual home machines rather than data centers or professional miners."
research_area: "compute-marketplaces"
source_urls:
  - "https://salad.com/about"
  - "https://salad.com/"
  - "https://community.salad.com/sell-gpu-power/"
  - "https://www.prnewswire.com/news-releases/saladcom-announces-17-million-series-a-funding-round-to-pioneer-affordable-decentralized-cloud-computing-services-301529132.html"
  - "https://www.originventures.com/blog/why-we-invested-in-salad-technologies-inc"
last_reviewed: 2026-08-15
stale_after_days: 90
related:
  - "compute-marketplaces/openrouter.md"
  - "datacenters/distributed-compute/akash-network.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Salad (operated by Salad Technologies, doing business as SaladCloud) is a Utah-based company that pays gamers and other consumer PC owners for spare GPU cycles through a desktop application, then resells that pooled capacity as a low-cost cloud for AI inference, rendering, and other batch/parallel workloads. It is the section's clearest example of a marketplace sourcing "local" compute in the literal sense — residential gaming rigs rather than data-center or crypto-mining-grade hardware — automatically matched to jobs via a trust-rating system rather than a posted-price or on-chain-auction mechanism.

## Key Facts

- Founded: March 27, 2018; headquartered in the US (Utah-incorporated, per its seed investors)
- Founder/CEO: Bob Miles
- Type: Company — consumer-GPU compute marketplace (SaladCloud)
- Status: Private, growth-stage
- Funding: Seed (Kickstart Seed Fund, Royal Street Ventures) → Seed Plus, $3.2M → Series A, $17M, announced April 20, 2022, co-led by Left Lane Capital and Origin Ventures with Kickstart Seed Fund, Royal Street Ventures, and Carthona Capital participating
- Reported scale: 60,000+ daily active GPUs, 450,000+ worldwide earning nodes, presence in 191 countries, 100,000+ monthly active "Chef" (supplier) accounts, $7M+ paid out to GPU contributors to date (self-reported; not independently audited)

## What It Is / How It Works

Salad's supply side runs on a desktop client ("Salad") that individual PC owners — predominantly gamers, per the company's own framing — install to share idle GPU cycles, storage, and bandwidth in exchange for cash or gift-card rewards ("Chefs" earning "Salad Bucks"). This is structurally the same "aggregate idle third-party hardware" model as Akash Network, but sourced explicitly from consumer/residential machines rather than data-center or crypto-mining capacity, and coordinated by Salad's own centralized backend rather than an on-chain auction.

On the demand side, SaladCloud offers usage-based GPU rental starting around $0.02/hour with no prepaid contracts, marketed at up to 90% savings versus hyperscaler pricing. Job placement runs through what Salad describes as a "proprietary trust rating system" that indexes each node's historical performance, forecasts its likely availability, and selects a suitable hardware configuration for a given deployment — the closest analogue in this marketplace to OpenRouter's provider-ranking algorithm or io.net's proof-of-work-verified supplier ranking, though Salad has not published the algorithm's internals. Because consumer nodes can go offline at any time (a user closing their laptop, for instance), Salad automatically reallocates interrupted workloads to other nodes, an approach the company itself compares to cloud spot-instance interruption handling; published cold-start times are correspondingly longer than a traditional cloud, and the network tops out at 24GB VRAM per node, so Salad explicitly advises against workloads needing very low latency or large-model VRAM. Security is handled via SOC 2 certification and isolated per-job container environments, addressing the obvious trust concern of running arbitrary customer workloads on untrusted consumer hardware.

Compared to the other marketplace models in this section, Salad is notable for being demand-side centralized (Salad's own platform makes the routing decision, unlike Akash's on-chain auction) while being supply-side maximally decentralized down to the individual home PC — a middle position between OpenRouter (professional inference providers, posted-price routing) and the P2P swarm model used by Petals/Hivemind-style projects.

## Notable Developments

- **2022-04-20:** Closed $17M Series A co-led by Left Lane Capital and Origin Ventures, with existing seed investors Kickstart Seed Fund and Royal Street Ventures participating alongside new investor Carthona Capital; announced via PR Newswire.
- **2018-03-27:** Company founded.

## Key People

**Bob Miles** — Founder and CEO.
- LinkedIn: [linkedin.com/in/milesbob](https://www.linkedin.com/in/milesbob/)

### People — Last Reviewed: 2026-08-15

## Sources

- [Salad — About](https://salad.com/about) — founding date, mission, funding history, scale figures
- [Salad — homepage](https://salad.com/) — current pricing, scale metrics, trust-rating/scheduling description, latency/VRAM limitations
- [Salad Chef Community — How to Sell GPU Power](https://community.salad.com/sell-gpu-power/) — supplier-side ("Chef") mechanics
- [PR Newswire — Salad.com Announces $17 Million Series A Funding Round](https://www.prnewswire.com/news-releases/saladcom-announces-17-million-series-a-funding-round-to-pioneer-affordable-decentralized-cloud-computing-services-301529132.html) — funding amount, date, lead investors, founder/CEO name
- [Origin Ventures — Chopping Up Compute: Why We Invested in Salad Technologies](https://www.originventures.com/blog/why-we-invested-in-salad-technologies-inc) — investor rationale
