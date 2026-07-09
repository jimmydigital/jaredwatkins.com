---
title: "Grid Markets & Policy"
date: 2026-07-09
lastmod: 2026-07-09
draft: false
description: "How electricity market design and regulatory structure — using ERCOT/Texas as the leading case study — enable or constrain distributed energy innovation."
research_area: "energy/grid-markets"
last_reviewed: 2026-07-09
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Glossary

- **ERCOT** — Electric Reliability Council of Texas; the independent grid operator for most of Texas.
- **ISO / RTO** — Independent System Operator / Regional Transmission Organization; a nonprofit entity that operates a regional electric grid and wholesale market (ERCOT, PJM, MISO, CAISO, etc. are all ISOs or RTOs).
- **PUCT** — Public Utility Commission of Texas; the state regulator overseeing ERCOT and retail electricity in Texas.
- **FERC** — Federal Energy Regulatory Commission; regulates interstate electricity transmission and wholesale rates. Does not have jurisdiction over ERCOT (see [ERCOT Market Design]({{< relref "ercot-market-design.md" >}})).
- **Retail choice / REP** — A market structure where customers pick their electricity supplier from competing Retail Electric Providers (REPs), rather than buying from one regulated utility.
- **Energy-only market** — A wholesale market design (used by ERCOT and SPP) where generators are paid only for the electricity they actually deliver, with no separate payment for simply being available.
- **Capacity market** — The alternative design (used by PJM, MISO, and others) where generators are also paid to be available, on top of energy sales.
- **DER** — Distributed Energy Resource; a small, customer-sited energy asset (like a home battery or rooftop solar) as opposed to a large power plant.
- **VPP** — Virtual Power Plant; many DERs (e.g., thousands of home batteries) aggregated and operated together as if they were a single power plant.
- **ADER** — Aggregated Distributed Energy Resource; ERCOT's specific pilot program letting VPPs bid into its wholesale markets.
- **kWh / MWh** — Kilowatt-hour / megawatt-hour; units of energy. 1 MWh = 1,000 kWh — roughly a day's electricity use for 30–40 typical U.S. homes.

## Overview

Tracks the market design, regulatory structure, and policy mechanisms that determine which grid regions become fertile ground for distributed energy innovation — virtual power plants, residential batteries, fast-interconnecting distributed generation — and which stay bottlenecked. The lead case study is ERCOT (Texas), whose energy-only market, retail electric choice, and exemption from FERC jurisdiction have together produced a distinctly fast-moving environment for companies like [Base Power]({{< relref "../batteries/base-power.md" >}}). Entries compare ERCOT's structure against other U.S. ISOs/RTOs (PJM, MISO, CAISO, SPP, ISO-NE, NYISO) to separate what is genuinely portable policy from what depends on Texas-specific circumstances (its physical grid isolation) that cannot be replicated elsewhere. This section also documents failure cases — [Winter Storm Uri]({{< relref "winter-storm-uri.md" >}}) and [Griddy]({{< relref "griddy.md" >}}) — because the same market structure that enables fast-moving distributed energy innovation is also the one that exposed ordinary customers to catastrophic bills and left millions without power for days. Evaluating this market honestly requires both stories. Two entries — [FERC]({{< relref "ferc.md" >}}) and [PUCT]({{< relref "puct.md" >}}) — document the regulatory bodies themselves and who currently sits on them, since commission composition and leadership priorities are a direct input into every other entry in this section.

## Key Themes

- **Energy-only market design** (no capacity market) — ERCOT and SPP are the only two U.S. ISOs that rely solely on scarcity pricing rather than paying generators for availability
- **FERC jurisdictional exemption** — ERCOT's lack of synchronous interconnection to the Eastern or Western Interconnections keeps its market design outside Federal Power Act sections 203/205/206, leaving the [Public Utility Commission of Texas (PUCT)]({{< relref "puct.md" >}}) as the sole regulator — a structural feature unique to Texas among the mainland ISOs. See [FERC]({{< relref "ferc.md" >}}) and [PUCT]({{< relref "puct.md" >}}) for who sits on each body.
- **Retail electric choice** — Texas deregulated retail electricity in 2002 (Senate Bill 7, 1999); this licensing model is what lets a hardware company like Base Power become its own retail electric provider (REP) and directly capture the value of its batteries, rather than selling through a utility or third-party aggregator
- **Interconnection queue speed** — Berkeley Lab's Queued Up data shows ERCOT's average interconnection wait is roughly half of PJM's, and behind-the-meter distributed resources can often bypass the queue entirely
- **Portability testing in progress** — Base Power's 2026 expansion into PJM territory (via Illinois retail choice, not an ERCOT-style ADER program) is an active, real-time test of which pieces of the Texas model travel and which don't
- **What can go wrong** — [Winter Storm Uri]({{< relref "winter-storm-uri.md" >}}) (Feb 2021) is the reference failure event for ERCOT's resource adequacy under extreme weather; [Griddy]({{< relref "griddy.md" >}}) is the reference failure event for what a wholesale-pass-through retail model does to customers with no circuit breaker when prices are held at the cap for days
- **Who's regulating** — [FERC]({{< relref "ferc.md" >}}) (federal, everywhere except ERCOT) and [PUCT]({{< relref "puct.md" >}}) (Texas state-level, ERCOT's actual regulator) are tracked as standing entries with current commissioner rosters and backgrounds, since both bodies' decisions directly shape distributed-energy market access
