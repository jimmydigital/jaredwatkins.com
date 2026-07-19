---
title: "Span"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "San Francisco smart-electrical-panel and grid-edge technology company (founder Arch Rao, ex-Tesla Energy); pivoted from home electrification toward utility infrastructure with SPAN Edge, and in April 2026 launched XFRA — a distributed, residentially-sited data center product built with NVIDIA to add AI inference capacity using existing grid headroom."
research_area: "datacenters/distributed-compute"
source_urls:
  - "https://www.span.io/blog/span-announces-xfra-a-distributed-data-center-solution-to-close-the-speed-to-power-gap-for-ai-compute-demand"
  - "https://www.span.io/blog/b2-funding"
  - "https://www.latitudemedia.com/news/span-is-raising-a-176-million-series-c/"
  - "https://www.span.io/news"
last_reviewed: 2026-07-18
stale_after_days: 90
related:
  - "datacenters/distributed-compute/_index.md"
  - "datacenters/distributed-compute/akash-network.md"
  - "energy/batteries/base-power.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **SPAN Panel** — The company's original product: a smart electrical panel that meters and controls individual circuits in a home, enabling software-managed load shedding and prioritization (e.g., for battery backup).
- **SPAN Edge** — An "at-the-meter" grid device (launched March 2025) sold to utilities, positioned as an alternative to costly service upgrades for managing new home loads (EVs, heat pumps, batteries).
- **XFRA** — Span's distributed data center product (announced April 2026): compute nodes hosted in homes and small commercial spaces, using Span's power-orchestration technology to unlock unused electrical headroom to run GPU-based AI inference.
- **Speed-to-power gap** — Span's framing for the multi-year lag between when a hyperscaler wants new datacenter capacity and when the grid can actually deliver the power for it, due to interconnection queues and transmission buildout timelines.
- **Grid headroom** — Unused capacity within an existing electrical connection (e.g., a home's service panel) that can be tapped for a new load without requiring a utility service upgrade.

## Summary

Span is a San Francisco home-electrification technology company, founded by former Tesla Energy product lead Arch Rao, best known for its smart electrical panel. Since 2025 the company has pivoted a significant part of its business toward utilities (via the at-the-meter "SPAN Edge" device) and, as of April 2026, toward AI infrastructure: XFRA, a distributed data center product that places liquid-cooled NVIDIA GPU server nodes in homes and small commercial sites to sell inference compute capacity to hyperscalers and AI cloud providers, using power headroom in the existing grid rather than new dedicated generation or transmission.

## Key Facts

- **Founded:** 2018, San Francisco, California
- **Founder:** Arch Rao (CEO); previously Head of Products, Application & Sales Engineering for Tesla Energy (2013–2018), where he worked on Powerwall, Powerpack, and Solar Roof
- **Type:** Home electrification hardware/software company; grid-edge and (as of 2026) distributed-compute infrastructure vendor
- **Status:** Growth-stage, private; ~220+ employees as of April 2023 disclosure
- **Funding:** $231 million raised through Series B2 (April 2023, led by Wellington Management); a further Series C of roughly $176 million (per SEC filing, $163M in equity sold as of the filing) was reported in progress as of February 2026 — bringing total disclosed funding above $200M pre-Series C; the exact post-Series C total was not confirmed by a fetched primary source as of this review
- **Core products:** SPAN Panel (from 2020), SPAN Drive EV charger (from 2022), SPAN Edge at-the-meter device (from March 2025), XFRA distributed data center (announced April 2026)
- **XFRA hardware:** Liquid-cooled NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs
- **XFRA launch partners:** NVIDIA (compute hardware/go-to-market); PulteGroup (homebuilder, for new-construction rollout)

## What It Is / How It Works

Span's foundational product is a smart electrical panel that replaces a home's standard breaker panel with a metered, software-controlled version — giving homeowners circuit-level visibility and enabling automatic load management (for example, shedding non-essential circuits to extend battery backup runtime during an outage). Since 2025, the company has extended this power-orchestration technology outward from the home to the grid itself: SPAN Edge is an at-the-meter device, developed with metering partner Landis+Gyr, that gives utilities visibility and control over new home loads (EVs, heat pumps, batteries) without a full service upgrade — pitched as a cheaper alternative to utilities building new poles, wires, and transformers to accommodate load growth. Span has piloted this utility-facing model with PG&E, coordinating roughly 400 smart panels and 1,500 Sunrun-managed residential batteries in a virtual-power-plant-style capacity program (results not yet publicly disclosed as of this review).

XFRA, announced April 13, 2026, applies the same core idea — unlocking unused headroom in existing electrical connections — to AI compute rather than home appliances. Instead of a data center operator waiting years for new grid interconnection, XFRA sites liquid-cooled NVIDIA GPU server nodes directly in homes and small commercial spaces, using Span's power controls to draw on grid capacity that already exists but is underused. Span frames XFRA as additive rather than a replacement for centralized data centers, aimed specifically at inference and cloud-gaming workloads (which Span/NVIDIA argue benefit from proximity to end users and can tolerate distributed, smaller-node deployment, unlike large synchronized training runs). The company is working with homebuilder PulteGroup to integrate XFRA into new-construction homes alongside SPAN Panels and battery backup, and describes a three-way value proposition: hyperscalers/"neoscalers" get fast, flexible inference capacity; homeowners get a subsidized panel, battery, and discounted electricity/internet; utilities get better peak-demand management without new capital spending.

## Notable Developments

- **2026-04-13:** Announced XFRA, a distributed data center product for AI inference and cloud gaming, built with launch partner NVIDIA (liquid-cooled RTX PRO 6000 Blackwell Server Edition GPUs) and homebuilder PulteGroup; initial deployments slated for "later this year" (2026) with a stated goal of gigawatt-scale capacity by 2027. Company states a technical white paper is available at XFRA.ai (not independently reviewed for this entry).
- **2026-03-10:** Joined a campaign with Carrier, Tesla, and others aimed at unlocking underused grid capacity to lower electricity costs.
- **2026-02-02:** Reported (via SEC filing, first covered by Axios and Latitude Media) to be raising a Series C of approximately $176 million, with $163 million in equity sold as of the filing; prior disclosed total funding exceeded $200 million.
- **2025-03:** Launched SPAN Edge, an at-the-meter grid device for utilities, building on a 2024 partnership with metering vendor Landis+Gyr.
- **2025:** Participated in a PG&E virtual power plant pilot coordinating ~400 smart panels and 1,500 Sunrun-managed batteries (results undisclosed as of this review).
- **2023-04-24:** Closed $96 million Series B2 (led by Wellington Management; Congruent Ventures, Capricorn Investment Group, Qualcomm Ventures, Fifth Wall, Munich Re Ventures, Amazon's Alexa Fund among participants), bringing total funding to $231 million.
- **2022-03:** Closed $90 million Series B round.
- **2020:** Began selling the original SPAN Panel.
- **2018:** Company founded by Arch Rao.

## Key People

**Arch Rao** — Founder and CEO. Previously Head of Products, Application & Sales Engineering for Tesla Energy (2013–2018), where he worked on Powerwall, Powerpack, and Solar Roof. M.S. Mechanical Engineering, Stanford University (2004–2006).
- LinkedIn: [linkedin.com/in/arch-rao](https://www.linkedin.com/in/arch-rao)
- **⚑ Overlap:** Tesla Energy alumnus — a cluster worth cross-referencing against other Tesla Energy/Powerwall-adjacent people documented elsewhere in this knowledge base (e.g., in energy storage and VPP entries) as they are added.

Other Span co-founders or executive team members were not independently confirmed via a current-dated source as of this review; TODO — verify full founding team and current executive roster.

### Key People — Last Reviewed: 2026-07-18

## Supply Chain Position

Span sits at the **integrator / systems-and-software layer** for this section: it does not manufacture GPUs (NVIDIA supplies the RTX PRO 6000 Blackwell hardware for XFRA) or build conventional datacenter shells: its differentiation is the power-orchestration hardware/software (the panel and at-the-meter device) that lets a distributed compute node draw on existing residential/commercial electrical capacity. This makes Span's role for XFRA analogous to a siting-and-power-integration layer, distinct from Akash Network's role as a marketplace/coordination-software layer in the same [Distributed & Decentralized Compute]({{< relref "_index.md" >}}) subsection. **⚑ Shared theme:** Span's XFRA and [Base Power]({{< relref "../../energy/batteries/base-power.md" >}}) both monetize distributed, residentially-sited electrical infrastructure, but for different end uses — Span for on-site AI compute, Base Power for grid-services/backup battery capacity; no shared corporate or supplier relationship between the two has been confirmed.

## Claim Verification

### Claim: XFRA can deliver "gigawatts of new compute capacity" and reach "gigawatt scale in 2027"

**Status:** Unverified

**Supporting sources:**
- [SPAN Announces XFRA (Span blog/press release, April 13, 2026)](https://www.span.io/blog/span-announces-xfra-a-distributed-data-center-solution-to-close-the-speed-to-power-gap-for-ai-compute-demand) — company states "a pipeline of deployment capacity to achieve gigawatt scale in 2027"

**Refuting / questioning sources:**
- None found; but as of this review no independent reporting on actual XFRA deployments, site counts, or measured capacity was located, and the announcement itself states deployments were only "beginning later this year" (2026) at the time of writing.

**Summary:** This is a forward-looking company projection made at product launch, not a demonstrated or independently verified capacity figure. Treat the gigawatt-scale claim as aspirational/pipeline-stage until deployment data is published.

### Claim: XFRA "meets the specific power and latency requirements of modern inference workloads" (NVIDIA endorsement)

**Status:** Partially verified

**Supporting sources:**
- [SPAN Announces XFRA](https://www.span.io/blog/span-announces-xfra-a-distributed-data-center-solution-to-close-the-speed-to-power-gap-for-ai-compute-demand) — quotes Marc Spieler, NVIDIA Senior Managing Director of Global Energy Industry, endorsing the approach; NVIDIA is a named launch partner and hardware supplier

**Refuting / questioning sources:**
- None found; NVIDIA's endorsement is credible as a partner statement (NVIDIA has a commercial stake in RTX PRO 6000 sales through this channel) but is not the same as independent, third-party latency/performance benchmarking of an actual XFRA deployment.

**Summary:** NVIDIA's participation as a named launch partner supplying real hardware lends more weight than a typical unaffiliated endorsement, but NVIDIA is also a commercially interested party (GPU sales), and no independent benchmark of a live XFRA node's latency or throughput has been published as of this review.

### Claim: Span's total funding and Series C amount

**Status:** Partially verified

**Supporting sources:**
- [SPAN Series B2 Announcement](https://www.span.io/blog/b2-funding) — company-confirmed $231M total funding as of April 2023
- [Span is raising a $176 million Series C (Latitude Media, Feb 2, 2026)](https://www.latitudemedia.com/news/span-is-raising-a-176-million-series-c/) — cites an SEC Form D filing showing ~$176M target, $163M sold to date, first reported by Axios

**Refuting / questioning sources:**
- None found; but no Span-issued press release confirming the closed Series C amount or new post-money total was located as of this review — the SEC filing and secondary reporting are the only sources.

**Summary:** The $231M figure through Series B2 is company-confirmed. The Series C figures come from an SEC filing and secondary press coverage rather than a Span press release, so the round should be treated as "in progress / reported" rather than a confirmed closed and announced amount.

## Sources

- [SPAN Announces XFRA, a Distributed Data Center Solution to Close the Speed-to-Power Gap for AI Compute Demand (Span blog, Apr 13, 2026)](https://www.span.io/blog/span-announces-xfra-a-distributed-data-center-solution-to-close-the-speed-to-power-gap-for-ai-compute-demand)
- [SPAN secures $96.5M in Series B2 funding (Span blog, Apr 24, 2023)](https://www.span.io/blog/b2-funding)
- [Span is raising a $176 million Series C (Latitude Media, Feb 2, 2026)](https://www.latitudemedia.com/news/span-is-raising-a-176-million-series-c/)
- [SPAN News (Span blog index)](https://www.span.io/news)
