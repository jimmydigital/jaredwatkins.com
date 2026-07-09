---
title: "Base Power"
date: 2026-07-09
lastmod: 2026-07-09
draft: false
description: "Austin, Texas startup deploying large, vertically-integrated home batteries as a distributed grid resource; retail electric provider in ERCOT and utility-partnership VPP operator elsewhere; $4B Series C valuation (Oct 2025), reportedly in talks at $12B (May 2026)."
research_area: "energy/batteries"
source_urls:
  - "https://www.businesswire.com/news/home/20251008106005/en/Base-Power-Raises-$1-Billion-Series-C-to-Build-the-Future-of-American-Power"
  - "https://www.basepowercompany.com/specs"
  - "https://www.basepowercompany.com/specs/core"
  - "https://www.utilitydive.com/news/base-power-partnership-to-mitigate-price-spikes-load-peaks-for-south-texas/818221/"
  - "https://www.canarymedia.com/articles/batteries/base-power-to-launch-100-mw-home-battery-network-for-texas-utility"
  - "https://www.forbes.com/sites/rashishrivastava/2026/05/29/zach-dells-battery-company-is-in-talks-to-raise-funding-at-a-12-billion-valuation/"
  - "https://www.businesswire.com/news/home/20260413969089/en/GVEC-and-Base-Power-Expand-Partnership-to-Full-Service-Territory-Delivering-50-MW-of-Residential-Battery-Capacity"
  - "https://austinenergy.com/about/news/news-releases/2026/Austin-Energy-expands-local-battery-storage-to-support-reliable-affordable-power"
  - "https://www.canarymedia.com/articles/batteries/base-power-cheap-batteries-pjm"
last_reviewed: 2026-07-09
stale_after_days: 90
related:
  - "energy/batteries/_index.md"
  - "energy/grid-markets/ercot-market-design.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **BESS** — Battery Energy Storage System; the general industry term for a battery installation built to store and dispatch grid electricity, whether at residential (Base Power) or utility scale.
- **LFP** — Lithium Iron Phosphate; the battery chemistry Base Power uses, valued for handling frequent charge/discharge cycles well.
- **kWh / MWh** — Kilowatt-hour / megawatt-hour; units of energy. 1 MWh = 1,000 kWh — Base Power's home batteries are sized in kWh (25–50 kWh per unit), while its utility deals are sized in MW/MWh.
- **REP** — Retail Electric Provider; a company licensed to sell electricity directly to customers in a retail-choice market. Base Power operates as one in Texas (Base Texas REP, LLC).
- **ERCOT** — Electric Reliability Council of Texas; the grid operator for most of Texas, and the market Base Power's batteries trade into. See [ERCOT Market Design]({{< relref "../grid-markets/ercot-market-design.md" >}}) for how this works.
- **ADER** — Aggregated Distributed Energy Resource; ERCOT's pilot program that lets a fleet of home batteries like Base Power's bid into wholesale energy and grid-services markets as a single resource.
- **VPP** — Virtual Power Plant; the general term for many small distributed batteries (or other devices) operated together as if they were one power plant.
- **PJM** — PJM Interconnection; the large regional grid operator covering parts of 13 mid-Atlantic and Midwest states (including the Illinois territory Base Power expanded into in 2026) — the non-Texas grid region referenced in this entry.

## Summary

Base Power is an Austin, Texas-based startup (founded 2023) that designs, manufactures, installs, and operates oversized residential battery systems, aggregating them into a distributed grid resource. Unlike Tesla Powerwall or Enphase, which sell batteries through installers, Base owns the hardware and the customer relationship end-to-end: it is a licensed Texas Retail Electric Provider that gives homeowners a large battery for a low upfront fee and small monthly subscription, then dispatches the aggregated fleet into ERCOT's wholesale and ancillary-services markets (and, in regulated-utility territories, sells the aggregated capacity directly to the utility) to recover its costs. It raised $1 billion in Series C funding in October 2025 at a $4 billion valuation and was reportedly in talks as of May 2026 to raise further funding at a $12 billion valuation. Base's model depends heavily on Texas-specific market structure — see [ERCOT Market Design]({{< relref "../grid-markets/ercot-market-design.md" >}}) for the regulatory mechanisms (retail choice, the energy-only market, ERCOT's ADER pilot) that enable it, and for Base's June 2026 expansion into PJM territory as an early test of how portable the model is outside Texas.

## Key Facts

- **Founded:** 2023, Austin, Texas
- **Founders:** Zach Dell (CEO) and Justin Lopas (COO)
- **Type:** Vertically integrated residential battery energy storage system (BESS) manufacturer, installer, and virtual power plant (VPP) operator; also a licensed Texas Retail Electric Provider (Base Texas REP, LLC, PUCT License #10338)
- **Status:** Growth-stage, private; deploying at scale across Texas with early expansion into other utility territories
- **Chemistry:** Lithium Iron Phosphate (LFP)
- **Flagship hardware:** Single ground-mounted system (25 kWh, 11.4 kW instant discharge); double ground-mounted system (50 kWh); Base Core (39.2 kWh total energy per unit, Gen 3 hardware, stackable), designed and manufactured in-house
- **Manufacturing:** "Factory One," the former Austin American-Statesman printing press site in downtown Austin; a second factory is planned
- **Funding:** $1 billion Series C, October 2025, led by Addition, at a $4 billion valuation; reportedly in talks (as of May 29, 2026) to raise roughly $1 billion more at a $12 billion valuation, with Ribbit Capital reported as the lead — unconfirmed by the company as of this review
- **Deployment scale:** More than 100 MWh deployed as of October 2025 (Series C announcement); roughly 300 MWh in operation with an installation pace of 60+ customers per day as of March 2026; reported at more than 500 MWh installed in Texas since its 2024 commercial launch as of June 2026
- **Customer base:** Roughly 10,000 customers as of early 2026, per reporting
- **Geographic expansion:** Launched in ComEd territory (Chicago area, PJM Interconnection) in June 2026 — Base's first market outside Texas, made possible by Illinois retail choice, a state VPP incentive law, and ComEd's battery export-compensation rules rather than an ERCOT-style energy-only market or ADER program

## What It Is / How It Works

Base Power's core product is a large, ground-mounted LFP battery — 25 kWh or 50 kWh in its earlier hardware generation, or the newer 39.2 kWh Base Core unit (marketed as 40 kWh, stackable to roughly 80 kWh) — installed outside a customer's home and wired to provide automatic whole-home backup within 50 milliseconds of a grid outage. Customers pay a heavily discounted upfront installation fee (as low as $695 in Base's direct-to-consumer Texas markets, and far less — $295–$445 — in some utility-partnership deals) plus a small monthly fee (around $19–$29), instead of purchasing a comparable battery outright, which the company says can otherwise cost $15,000–$20,000. Base retains ownership of the hardware and handles all service and maintenance for its lifetime.

The company operates two parallel business models. In Texas's deregulated retail electricity markets (ERCOT), Base is itself a Retail Electric Provider: it sells customers a competitively priced electricity plan (including "Base Energy," a plan launched April 2026 marketed as guaranteed to stay below the market average) alongside the battery, then charges the fleet when wholesale prices are low and discharges — either to the home during outages or back to the grid — when prices are high, recovering costs through energy arbitrage and participation in ERCOT's Aggregated Distributed Energy Resource (ADER) pilot program, which allows aggregated distributed batteries to bid directly into wholesale energy and ancillary-services markets. In municipal utility and cooperative territories where customers cannot choose their retail provider, Base instead sells the aggregated capacity directly to the utility under long-term contracts, paid only for capacity actually delivered. Base's oversized battery packs — roughly double the capacity of a Tesla Powerwall 3 (13.5 kWh) or Enphase IQ 10 (10.1 kWh) — give it more flexibility to shift when it buys and sells power, which the company argues is central to making the economics work at scale. The company also partners with homebuilders (Lennar) to integrate batteries into new construction.

## Notable Developments

- **2026-06-24:** Launched in ComEd's territory in northern Illinois (PJM Interconnection) — Base's first market outside Texas. First 2,000 customers get a 40 kWh battery for $95 upfront (then $295), plus retail electricity at a 25% discount to ComEd's rate, under a 12-year battery agreement; enabled by Illinois retail choice, the state's new Clean and Reliable Grid Affordability Act (VPP incentive law, effective 2026), and ComEd rules compensating batteries for peak exports. Base's head of policy, Travis Kavulla, was tapped the same week to lead the Bonneville Power Administration.
- **2026-05-29 (reported, unconfirmed):** Forbes reported Base was in talks to raise roughly $1 billion at a $12 billion valuation, with Ribbit Capital reported as lead investor; neither Base nor Ribbit confirmed to Forbes.
- **2026-04-13:** Expanded partnership with Guadalupe Valley Electric Cooperative (GVEC) from a 2 MW pilot to 50 MW across GVEC's full South Texas service territory; the aggregation passed ERCOT ADER performance testing on its first attempt.
- **2026-04-08:** Launched "Base Energy," a retail electricity plan (no battery purchase required) guaranteed to stay below the Texas market average rate.
- **2026-04 (council approval):** Austin Energy approved a partnership with Base Power to dispatch up to 40 MW of residential battery capacity for local grid reliability, expected to reach full capacity within about 18 months.
- **2026-03-06:** Launched 100 MW residential storage program with Denton County Electric Cooperative (CoServ, ~330,000 meters) — Base's largest utility deal to date.
- **2026-02-10:** Launched a residential distributed storage pilot with El Paso Electric.
- **2025-10-08:** Raised $1 billion Series C led by Addition at a $4 billion valuation; announced construction of "Factory One" at the former Austin American-Statesman site; disclosed ADER program qualification; reported >100 MWh deployed since 2023 launch.
- **2025 (H2):** Expanded direct-to-consumer operations to Dallas–Fort Worth and Greater Houston, beyond its original Austin-region launch.
- **2024-05:** Commercial launch in the Austin region (initial market).
- **2023:** Company founded by Zach Dell and Justin Lopas.

## Key People

**Zach Dell** — Co-founder and CEO. Previously an investor at Thrive Capital and, before that, in private equity at Blackstone. Son of Dell Technologies founder Michael Dell. Attended the University of Southern California.
- LinkedIn: [linkedin.com/in/zach-dell-a631a554](https://www.linkedin.com/in/zach-dell-a631a554/)
- **⚑ Overlap:** Met co-founder Justin Lopas in late 2022 on a Thrive Capital-related visit to Anduril's Costa Mesa factory, where Lopas then worked.

**Justin Lopas** — Co-founder and COO. Previously Head of Manufacturing at Anduril Industries (2020–2023); before that, a lead manufacturing/Starship engineer at SpaceX (~4 years). B.S. Mechanical Engineering, University of Michigan.
- LinkedIn: [linkedin.com/in/justinlopas](https://www.linkedin.com/in/justinlopas/)
- X: [@JLopas](https://x.com/JLopas)

**Travis Kavulla** — Head of Policy at Base Power through at least June 2026; quoted publicly on the company's Illinois/PJM market-entry strategy. In June 2026 he was named Administrator of the Bonneville Power Administration, a federal power marketing agency, suggesting a departure from Base Power around that time — his status at Base as of this review is unconfirmed.
- LinkedIn: not found (not searched in this session — TODO: verify)

### Key People — Last Reviewed: 2026-07-09

## Supply Chain Position

Base Power operates at the **Pack Assembly and OEM/End-Use** layers of the battery value chain, distinct from the utility-scale BESS integrators (Tesla Megapack, Sungrow, Fluence, etc.) documented elsewhere in this section: its product is a residential-scale, ground-mounted system rather than a grid-scale container, and its go-to-market is direct-to-homeowner (and direct-to-utility for aggregated capacity) rather than project-based utility or IPP sales. Base has stated its Gen 3 hardware ("Base Core") is fully designed and manufactured in-house at its Austin factory, indicating vertical integration from cell-pack assembly through installation and software-based dispatch — but the company has not publicly disclosed its LFP cell supplier(s). No shared-supplier relationship with other companies documented in this section has been confirmed.

## Claim Verification

### Claim: Base Power deployed more than 100 MWh of residential battery capacity within less than two years of founding

**Status:** Verified

**Supporting sources:**
- [Base Power Series C press release, Business Wire, Oct 8, 2025](https://www.businesswire.com/news/home/20251008106005/en/Base-Power-Raises-$1-Billion-Series-C-to-Build-the-Future-of-American-Power) — company states "more than 100 MWh of residential battery capacity" deployed since its 2023 founding

**Summary:** Company-reported figure from an official press release; no independent third-party audit of deployed capacity was found.

---

### Claim: Base Power's Series C valued the company at $4 billion; a subsequent round is being discussed at $12 billion

**Status:** Partially verified

**Supporting sources:**
- [Canary Media, March 11, 2026](https://www.canarymedia.com/articles/batteries/base-power-to-launch-100-mw-home-battery-network-for-texas-utility) — references the "$4 billion valuation" tied to the October 2025 Series C
- [Forbes, May 29, 2026](https://www.forbes.com/sites/rashishrivastava/2026/05/29/zach-dells-battery-company-is-in-talks-to-raise-funding-at-a-12-billion-valuation/) — reports the $12B figure as from "four sources familiar with the matter"; explicitly states Base Power and Ribbit Capital did not respond to comment requests

**Summary:** The $4B Series C valuation is corroborated by multiple outlets citing the October 2025 round. The $12B figure is sourced only to unnamed parties as of this review and has not been confirmed by Base Power; treat as reported-but-unconfirmed.

---

### Claim: Base's battery packs offer roughly double the capacity of comparable residential systems (Tesla Powerwall 3, Enphase IQ 10)

**Status:** Verified

**Supporting sources:**
- [Utility Dive, April 22, 2026](https://www.utilitydive.com/news/base-power-partnership-to-mitigate-price-spikes-load-peaks-for-south-texas/818221/) — cites Tesla Powerwall 3 official datasheet (13.5 kWh) and Enphase IQ 10 product page (10.1 kWh) against Base's 25-kWh single unit
- [Base Power specs page](https://www.basepowercompany.com/specs) — confirms 25 kWh / 50 kWh capacities for Base's ground-mounted systems

**Summary:** Verified by direct comparison of publicly listed specifications from all three vendors.

## Sources

- [Base Power Raises $1 Billion Series C to Build the Future of American Power (Business Wire, Oct 8, 2025)](https://www.businesswire.com/news/home/20251008106005/en/Base-Power-Raises-$1-Billion-Series-C-to-Build-the-Future-of-American-Power)
- [Base Power Battery Specifications](https://www.basepowercompany.com/specs)
- [Base Core System Specifications](https://www.basepowercompany.com/specs/core)
- [Base Power partnership to mitigate price spikes, load peaks for South Texas co-op, CEO says (Utility Dive, Apr 22, 2026)](https://www.utilitydive.com/news/base-power-partnership-to-mitigate-price-spikes-load-peaks-for-south-texas/818221/)
- [Base Power to launch 100-MW home battery network for Texas utility (Canary Media, Mar 11, 2026)](https://www.canarymedia.com/articles/batteries/base-power-to-launch-100-mw-home-battery-network-for-texas-utility)
- [Zach Dell's Battery Company Is In Talks To Raise Funding At A $12 Billion Valuation (Forbes, May 29, 2026)](https://www.forbes.com/sites/rashishrivastava/2026/05/29/zach-dells-battery-company-is-in-talks-to-raise-funding-at-a-12-billion-valuation/)
- [GVEC and Base Power Expand Partnership to Full Service Territory, Delivering 50 MW of Residential Battery Capacity (Business Wire, Apr 13, 2026)](https://www.businesswire.com/news/home/20260413969089/en/GVEC-and-Base-Power-Expand-Partnership-to-Full-Service-Territory-Delivering-50-MW-of-Residential-Battery-Capacity)
- [Austin Energy expands local battery storage to support reliable, affordable power (Austin Energy, 2026)](https://austinenergy.com/about/news/news-releases/2026/Austin-Energy-expands-local-battery-storage-to-support-reliable-affordable-power)
- [Base Power brings cheap batteries to residents in power-starved PJM (Canary Media, Jun 24, 2026)](https://www.canarymedia.com/articles/batteries/base-power-cheap-batteries-pjm)
