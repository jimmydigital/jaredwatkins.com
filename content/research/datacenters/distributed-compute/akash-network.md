---
title: "Akash Network"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "Blockchain-coordinated decentralized GPU compute marketplace (built by Overclock Labs) matching idle GPU capacity — data-center providers and, via the new Homenode product, home gaming rigs — with AI developers through a reverse-auction model."
research_area: "datacenters/distributed-compute"
source_urls:
  - "https://homenode.akash.network/"
  - "https://akash.network/"
  - "https://ovrclk.com/about"
last_reviewed: 2026-07-18
stale_after_days: 90
related:
  - "datacenters/distributed-compute/_index.md"
  - "datacenters/distributed-compute/span.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **AKT** — Akash Network's native token; used for staking (network security) and as a settlement currency in the compute marketplace (other IBC-enabled currencies are also configurable via governance).
- **Reverse auction** — Akash's price-discovery mechanism: a renter posts required resources (GPU model, region, max price) and independent providers submit competitive bids, rather than the renter paying a fixed rate set by the provider.
- **SDL** — Stack Definition Language; the YAML-based config file format used to specify a deployment's resource requirements on Akash.
- **Homenode** — A 2026 Akash Core initiative (not yet publicly launched as of this review) that packages provider software for individual GPU owners — gamers, 3D artists — so they can list idle consumer GPUs (RTX 30/40/50-series) on the Akash marketplace without needing Kubernetes or Linux administration expertise.
- **Supercloud** — Akash's own branding for its aggregate network of independent compute providers, positioned as a decentralized alternative to hyperscaler cloud.

## Summary

Akash Network is a blockchain-based decentralized compute marketplace built by Overclock Labs (founded 2015 as "Ovrclk Inc.") that lets GPU and CPU owners list spare capacity for rent and lets developers deploy containerized workloads (Docker-native) onto that capacity via a reverse-auction pricing model. Originally a general-purpose "open cloud" project dating to 2018, Akash has repositioned around AI compute since adding GPU deployment support in 2023, and in 2026 announced Homenode, a simplified onboarding product aimed at bringing individual consumer GPU owners — not just datacenter-scale providers — onto the network as a way of tapping distributed, already-idle hardware to address the AI compute shortage.

## Key Facts

- **Founded:** Work on the underlying technology began in 2014 (Greg Osuri and Adam Bozanich); the company, Overclock Labs (originally "Ovrclk Inc."), was registered in Delaware in June 2015; Akash Mainnet 1 (token generation event) launched September 2020
- **Founders:** Greg Osuri (CEO) and Adam Bozanich (CTO)
- **Type:** Decentralized compute marketplace protocol (Cosmos SDK / Tendermint-based blockchain) plus supporting products (Akash Console, AkashML, Homenode)
- **Status:** Live mainnet (Mainnet 15 / v1.1.0 as of November 2025); Homenode in waitlist/early-access as of this review — no public launch date confirmed
- **Network scale (per akash.network live counter, checked 2026-07-18):** 60 active providers, ~10,000 vCPUs, 249 GPUs, 68 TB memory, 805 TB storage — a real-time figure, not a static claim, and likely to change between visits
- **GPU deployment support:** Added August 2023 (Mainnet 6, v.24)

## What It Is / How It Works

Akash operates as a two-sided marketplace coordinated by a public blockchain rather than a centralized cloud operator. On one side, "providers" — anyone from datacenter operators to (via Homenode) individual gamers — run Akash's provider software to list available compute (GPU model, CPU, memory, storage) on the network. On the other side, developers submit a deployment request (an SDL file specifying required resources, region, and a maximum price) to an on-chain marketplace; providers meeting the spec submit competitive bids in real time, and the developer accepts a bid to open a lease. Akash markets the pricing mechanism — a reverse auction rather than a fixed hyperscaler rate card — as the source of its cost advantage, citing figures like H100 instances at $1.33/hr versus a claimed $3.93/hr on AWS.

The Homenode initiative, announced via a dedicated waitlist site in 2026, extends this model to individual consumer hardware. Rather than requiring a Kubernetes-savvy operator, Homenode packages the provider software for direct installation on a gaming PC or workstation, targeting owners of NVIDIA RTX 30-, 40-, and 50-series cards. Akash's own marketing materials frame this explicitly as a response to datacenter power constraints: "Centralized data centers have hit an energy wall... Akash Network bypasses the energy bottleneck by tapping into the dispersed power and hardware already running in homes." The company's illustrative earnings estimate for an RTX 5090 node is $3,066/year at 50% utilization and a $0.70/hr market rate — enough, per Akash's own figures, to cover the card's ~$2,500 retail cost in under a year.

Akash cites a case study with Razer, which integrated its AIKit platform with Akash to scale an AI image-generation campaign, reporting $0.01 per generated image, a 3.24-second average end-to-end response time, and a claimed 15x lower inference cost versus centralized APIs.

## Notable Developments

- **2026 (waitlist open, no public launch date confirmed):** Akash Homenode announced — simplified provider onboarding for individual consumer GPU owners, explicitly positioned as tapping "dispersed power and hardware already running in homes" to address AI compute/energy constraints.
- **2025-11:** Mainnet 15 (v1.1.0) — bug-fix release resolving overdrawn escrow accounts blocking deployment closure.
- **2025-10:** Mainnet 14 (v1.0) — Cosmos SDK v0.53 upgrade, multi-depositor escrow accounts (AEP-75), lease termination reasons (AEP-39).
- **2023-11:** Mainnet 8 (v.32) — introduced `ResourcesOffer`, letting providers respond to wildcard GPU-model requests with a specific model.
- **2023-08:** Mainnet 6 (v.24) — GPU deployment support added; also enabled settlement in non-AKT, IBC-enabled currencies.
- **2022-04:** Mainnet 3 — added persistent storage.
- **2021-03:** Mainnet 2 — added the marketplace functionality (bidding/leasing) that defines Akash today.
- **2020-09:** Mainnet 1 — staking and the AKT Token Generation Event.
- **2015-06:** Overclock Labs (as "Ovrclk Inc.") registered in Delaware; raised its first financing round (led by Tuesday Capital, with Auren Hoffman, Kevin Lin, and People Fund participating) in February 2016.

## Key People

**Greg Osuri** — Founder and CEO of Overclock Labs / Akash Network. Previously worked as an engineer at IBM and founded AngelHack, a large hackathon organizer, before starting Overclock Labs.
- LinkedIn: [linkedin.com/in/gosuri](https://www.linkedin.com/in/gosuri)
- [GitHub](https://www.github.com/gosuri)
- [X](https://www.twitter.com/GregOsuri)

**Adam Bozanich** — Co-founder and Chief Technology Officer.
- LinkedIn: [linkedin.com/in/abozanich](https://www.linkedin.com/in/abozanich)
- [GitHub](https://www.github.com/boz)
- [X](https://www.twitter.com/abozanich)

**Cheng Wang** — Chief Financial Officer.
- LinkedIn: [linkedin.com/in/cheng-wang-10900621](https://www.linkedin.com/in/cheng-wang-10900621)
- [X](https://www.twitter.com/LeChenghiskhan)

### Key People — Last Reviewed: 2026-07-18

## Supply Chain Position

Akash does not manufacture hardware; it is a coordination/marketplace layer sitting above hardware owned by third-party providers (datacenter operators and, via Homenode, individual consumers). Its position is analogous to a software/AI layer in the value chain described elsewhere in this knowledge base's Robotics steering, but for cloud compute rather than robots: Akash supplies the protocol and marketplace software, not the GPUs, servers, or power infrastructure underneath them. No shared-supplier or shared-infrastructure relationship with other companies in this section has been confirmed.

## Claim Verification

### Claim: Akash pricing is significantly cheaper than hyperscaler cloud (e.g., "$1.33/hr H100 vs. $3.93/hr AWS")

**Status:** Partially verified

**Supporting sources:**
- [Akash Network homepage](https://akash.network/) — company-published comparison figures and live pricing widget

**Refuting / questioning sources:**
- None found; but the comparison is company-published and depends on which AWS instance/commitment type is used as the baseline — on-demand vs. reserved vs. spot pricing differ substantially and the exact AWS SKU being compared was not specified on the page.

**Summary:** The reverse-auction pricing mechanism itself is real and observable on Akash's own live console, but the specific headline comparison figures are self-published without a specified, apples-to-apples AWS baseline. Directionally plausible (decentralized spare-capacity marketplaces are generally cheaper than on-demand hyperscaler rates) but not independently verified.

### Claim: Razer's AIKit/Akash integration achieved "15x lower inference costs than centralized APIs"

**Status:** Unverified

**Supporting sources:**
- [Akash Network homepage, Razer case study summary](https://akash.network/) — cites $0.01/image, 3.24s average response time, 15x cost reduction

**Refuting / questioning sources:**
- None found; the case study is hosted and promoted by Akash itself, and the comparison baseline ("centralized APIs") is not named.

**Summary:** Single-source company case study without a named baseline provider or independent audit. Treat as a marketing figure pending independent confirmation.

### Claim: Homenode lets a consumer RTX 5090 node "cover 123% of hardware cost annually" ($3,066/year at 50% utilization)

**Status:** Unverified

**Supporting sources:**
- [Akash Homenode](https://homenode.akash.network/) — company-published estimate, explicitly modeled on a 50% utilization assumption at a "conservative $0.70/hr market rate"

**Refuting / questioning sources:**
- None found; but Homenode has not publicly launched, so no real-world utilization or payout data exists yet to test the assumption. 50% utilization is a planning assumption, not an observed figure.

**Summary:** This is a pre-launch marketing projection built on an assumed utilization rate, not a demonstrated result. Actual demand for consumer-grade RTX cards on the network (vs. enterprise H100/H200/A100 supply) is unproven at this stage.

## Sources

- [Akash Homenode](https://homenode.akash.network/)
- [Akash Network — homepage](https://akash.network/)
- [Overclock Labs — About](https://ovrclk.com/about)
