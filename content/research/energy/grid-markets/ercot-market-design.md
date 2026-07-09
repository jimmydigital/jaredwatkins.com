---
title: "ERCOT Market Design: Why Texas Enables Distributed Energy Innovation"
date: 2026-07-09
lastmod: 2026-07-09
draft: false
description: "How ERCOT's energy-only market, FERC exemption, retail electric choice, and fast interconnection combine to enable companies like Base Power — and which of these mechanisms are portable to other U.S. grid regions."
research_area: "energy/grid-markets"
source_urls:
  - "https://www.ferc.gov/industries-data/electric/electric-power-markets/ercot"
  - "https://eta-publications.lbl.gov/sites/default/files/2025-12/queued_up_2025_edition_12.15.2025.pdf"
  - "https://www.canarymedia.com/articles/batteries/base-power-cheap-batteries-pjm"
  - "https://www.ercot.com/mktrules/pilots/ader"
  - "https://www.utilitydive.com/news/texas-regulators-move-virtual-power-plant-pilot-development-to-ercot/740304/"
  - "https://www.utilitydive.com/news/base-power-partnership-to-mitigate-price-spikes-load-peaks-for-south-texas/818221/"
  - "https://comptroller.texas.gov/economy/fiscal-notes/archive/2021/oct/winter-storm-reform.php"
  - "https://capitol.texas.gov/billlookup/BillSummary.aspx?LegSess=87R&Bill=SB3"
last_reviewed: 2026-07-09
stale_after_days: 90
related:
  - "energy/grid-markets/_index.md"
  - "energy/batteries/base-power.md"
  - "energy/grid-markets/winter-storm-uri.md"
  - "energy/grid-markets/griddy.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **ERCOT** — Electric Reliability Council of Texas; the independent grid operator for most of Texas.
- **ISO / RTO** — Independent System Operator / Regional Transmission Organization; the entity that runs a regional grid and wholesale electricity market. PJM, MISO, CAISO, SPP, NYISO, and ISO-NE are the other major ones referenced here.
- **PUCT** — Public Utility Commission of Texas; regulates ERCOT and Texas retail electricity.
- **FERC** — Federal Energy Regulatory Commission; the federal regulator with jurisdiction over interstate transmission and wholesale rates almost everywhere except ERCOT.
- **Federal Power Act (sections 203/205/206)** — The federal law provisions that normally give FERC authority over transmission and wholesale rates; ERCOT is exempt because its grid has no synchronous tie to the rest of the country.
- **Energy-only market** — A wholesale design where generators are paid only for energy actually delivered, relying on price spikes ("scarcity pricing") rather than separate availability payments to attract investment. ERCOT and SPP are the only two U.S. ISOs built this way.
- **Capacity market** — The alternative design (PJM, MISO, NYISO, ISO-NE) where generators are also paid just to be available, independent of whether they ever run.
- **Retail choice / REP** — A system letting customers pick their electricity supplier from competing Retail Electric Providers (REPs) rather than a single regulated utility. Base Power's ability to sell electricity directly to homeowners depends on this.
- **DER** — Distributed Energy Resource; a small, customer-sited asset like a home battery, as opposed to a utility-scale power plant.
- **VPP** — Virtual Power Plant; many DERs aggregated and dispatched together as a single resource.
- **ADER** — Aggregated Distributed Energy Resource; ERCOT's pilot program letting VPPs bid into its wholesale energy and ancillary-services markets.
- **FERC Order 2222** — A federal rule requiring RTOs/ISOs (PJM, MISO, etc.) to let DER aggregations participate in their wholesale markets — the non-Texas equivalent of ERCOT's ADER pathway.
- **NEM** — Net Energy Metering; the billing framework (mainly used in California/CAISO) that credits customers for power their solar panels or batteries export to the grid.
- **Interconnection queue** — The waitlist and technical review process a new generator or battery must go through before it's allowed to connect to the grid.
- **Behind-the-meter** — Equipment (like a home battery) installed on the customer's side of the utility meter, as opposed to connected directly to the grid — often lets a resource skip the interconnection queue.
- **MW / MWh** — Megawatt (a unit of power, i.e. rate of electricity delivery) and megawatt-hour (a unit of energy, i.e. power delivered over an hour). A useful rule of thumb: 1 MW can power roughly 200 average U.S. homes at a given moment.

## Summary

Texas's ERCOT grid is structurally different from every other major U.S. grid region in three compounding ways: it runs an energy-only wholesale market with no capacity payments, it sits entirely outside FERC's jurisdiction because it isn't synchronously tied to the rest of the country, and it has offered full retail electric choice since 2002. None of these exist to encourage battery startups — they predate companies like Base Power by decades — but together they lower the barriers that would otherwise stop a hardware company from becoming its own power retailer, monetizing distributed batteries in wholesale markets, and connecting new distributed capacity in months rather than years. Base Power's 2026 expansion into PJM territory via Illinois retail choice is the first real-world test of which of these mechanisms can be replicated elsewhere and which are Texas-specific.

## Key Facts

- **Grid operator:** Electric Reliability Council of Texas (ERCOT), an independent system operator (ISO) serving roughly 90% of Texas's electric load and about 24 million customers over more than 46,000 miles of transmission lines
- **Market design:** Energy-only market (no capacity market) — ERCOT and the Southwest Power Pool (SPP) are the only two U.S. ISOs/RTOs structured this way; generators are paid only for energy delivered, with scarcity pricing (not capacity payments) relied on to incentivize new investment
- **Regulatory jurisdiction:** ERCOT's transmission grid lies entirely within Texas and has no synchronous AC connection to the Eastern or Western Interconnection; as a result, transmission occurring wholly within ERCOT is not subject to FERC jurisdiction under Federal Power Act sections 203, 205, or 206 — oversight instead rests with the Public Utility Commission of Texas (PUCT) and the Texas Legislature
- **Retail choice:** Enacted by Senate Bill 7 (passed by the Texas Legislature in 1999, effective January 1, 2002), which required investor-owned utilities to divest generation and created a competitive retail market; ERCOT reports administering retail switching for roughly 7 million premises in competitive-choice areas
- **Interconnection speed:** Per Lawrence Berkeley National Laboratory's "Queued Up" 2025/2026 data, the national average interconnection queue wait is roughly 25 months; ERCOT's average is roughly 20 months versus roughly 40 months in PJM. Within ERCOT, gas projects average about 17 months, storage about 23 months, and renewables about 27 months — though projects in data-center load-growth zones wait 36–48 months in both ERCOT and PJM
- **Distributed-resource market access:** ERCOT's Aggregated Distributed Energy Resource (ADER) pilot, established by the ERCOT Board in October 2022 under PUCT direction (PUCT Project No. 53911), allows aggregations of residential/small distributed resources to bid into ERCOT's wholesale energy and ancillary-services markets; management was shifted from PUCT to the ERCOT stakeholder process in February 2025
- **Stress-tested by crisis:** Winter Storm Uri (February 13–17, 2021) forced roughly 20,000 MW of manually controlled rolling blackouts — the largest such event in U.S. history — and triggered Senate Bill 3 (signed June 8, 2021), which mandated weatherization of generation, transmission, and gas facilities under PUCT enforcement

## How It Works

**Energy-only market, no capacity market.** Most U.S. ISOs (PJM, MISO, NYISO, ISO-NE) run a capacity market: generators are paid to simply be available, on top of what they earn selling actual energy. ERCOT and SPP don't — ERCOT generators are compensated purely for energy delivered, and the market instead depends on scarcity pricing (prices spiking when supply is tight) to signal new investment. This has two consequences relevant to distributed energy: it makes real-time and day-ahead price volatility a bigger part of the Texas market's DNA than elsewhere, which is exactly the kind of volatility a dispatchable home battery fleet like Base Power's is built to exploit; and it means new capacity — including distributed capacity — doesn't have to clear a capacity-market auction to get paid, it just has to be available when prices spike.

**No FERC jurisdiction.** Because ERCOT's grid has no synchronous AC tie to the Eastern or Western Interconnection, transmission occurring entirely within ERCOT falls outside the Federal Power Act's sections 203, 205, and 206 — the provisions that give FERC jurisdiction over interstate transmission and wholesale rates elsewhere. That leaves the PUCT and the Texas Legislature as ERCOT's sole regulators, which is why Texas has historically been able to move faster on market redesigns (deregulation, ADER, real-time co-optimization) than ISOs that need FERC sign-off on tariff changes. This is the one piece of the Texas model that is structurally non-portable: it depends on Texas's physical grid isolation, which no other state can replicate by policy choice alone.

**Retail electric choice.** Since 2002, most of Texas has allowed customers to choose their electricity supplier from competing Retail Electric Providers (REPs), rather than buying from a single regulated utility. This is the mechanism that lets Base Power operate as Base Texas REP, LLC (PUCT License #10338) — selling electricity directly to homeowners at a competitive rate, then using its battery fleet to buy power cheap and sell it expensive, capturing the arbitrage itself instead of splitting it with a utility middleman. Retail choice is not unique to Texas — Ohio, Illinois, Pennsylvania, and roughly a dozen other states plus D.C. offer some form of residential choice — which is what made Illinois (inside PJM) a viable first expansion market for Base Power in 2026, even without ERCOT's other structural advantages.

**Fast interconnection for distributed, behind-the-meter resources.** ERCOT's average generator interconnection queue is roughly half of PJM's (about 20 months versus about 40 months, per LBNL). But the more important mechanism for a company like Base Power is that behind-the-meter residential batteries mostly sidestep the queue altogether: as Base Power CEO Zach Dell put it regarding the company's Illinois move, "we are deploying capacity behind the meter at the residential home, where an interconnection already exists, so we don't wait in the interconnection queue." This is a general feature of behind-the-meter distributed resources, not an ERCOT-specific rule — but ERCOT's overall faster queue culture, plus the ADER pathway to wholesale market participation, gives distributed resources in Texas more ways to get paid once installed.

**The ADER pilot as a market-access bridge.** The ADER pilot lets aggregations of many small distributed resources (like a fleet of home batteries) register as a single resource that can bid into ERCOT's wholesale energy and ancillary-services markets — the same markets utility-scale batteries participate in. Launched in 2022 with a target of 80 MW, the pilot has grown slowly: as of February 2025, only three virtual power plants were registered, providing about 25.5 MW of energy and almost 20 MW of other reserve services — well short of the original target, which PUCT and ERCOT staff attributed partly to initial limits on program size discouraging participation. Base Power's GVEC aggregation passed ERCOT's ADER performance testing on its first attempt in 2026. Management of the pilot moved from PUCT to the ERCOT stakeholder process in February 2025 specifically so it could "engage with a larger community of ERCOT market participants," per PUCT Chairman Thomas Gleeson.

## Comparison to Other U.S. Grid Markets

| Feature | ERCOT (Texas) | PJM (Mid-Atlantic/Midwest) | MISO | CAISO (California) |
|---------|---------------|----------------------------|------|---------------------|
| Market design | Energy-only (no capacity market) | Capacity market (annual base residual auction) | Capacity market (resource adequacy construct) | No formal capacity market; resource adequacy program |
| FERC jurisdiction | Exempt (no synchronous interconnection to rest of U.S. grid) | Full FERC jurisdiction | Full FERC jurisdiction | Full FERC jurisdiction |
| Retail choice | Yes, since 2002 (most of the state) | Varies by state — Illinois, Pennsylvania, Ohio, New Jersey, Maryland, others offer choice; some PJM states do not | Limited — mostly regulated utility monopolies | No — California is a regulated-utility state (net metering/NEM is the closest analog to retail choice for DERs) |
| Avg. interconnection queue wait (LBNL, ~2025) | ~20 months | ~40 months | Data not isolated in sources reviewed for this entry | Data not isolated in sources reviewed for this entry |
| Distributed-resource wholesale market access | ADER pilot (since 2022; slow uptake, ~25.5 MW as of Feb 2025) | FERC Order 2222 implementation underway; first DER capacity auction (for 2028–2029 delivery) expected mid-2026 | Order 2222 implementation ongoing | NEM 3.0 (2023) reduced compensation for exported solar/storage relative to prior NEM 2.0 |
| Recent stress event | [Winter Storm Uri]({{< relref "winter-storm-uri.md" >}}) (Feb 2021) — SB3 weatherization mandate | Rising capacity prices; some governors have discussed exiting PJM over cost allocation to data centers | — | — |

**What's portable and what isn't.** Retail choice, ADER-style aggregation rules, and utility policies that compensate batteries for exporting power at the right times are all things a state legislature or a single accommodating utility can adopt without needing Texas's physical grid isolation. Illinois did exactly this: the state already had retail choice, and its 2026 Clean and Reliable Grid Affordability Act created a rebate for battery customers who agree to discharge during summer peak hours, while ComEd (the local utility) had already revised its net-metering rules to compensate standalone batteries — not just solar — for exporting at market rates. That combination was enough for Base Power to enter PJM territory without needing an ERCOT-style energy-only market or ADER program; per Base Power's head of policy Travis Kavulla, "if you're a state in PJM, this is something that you can kind of cause your utilities to do." What is not portable is ERCOT's FERC exemption, which depends on Texas's grid being physically unconnected to the rest of the country — no other state can adopt that by legislation. The practical implication is that other states can capture much of the "distributed battery as retail arbitrage + grid service" model without becoming another Texas; they just need retail choice (already present in roughly a dozen states) plus a utility or legislature willing to pay distributed batteries a fair price for flexibility.

## Notable Developments

- **2026-06-24:** Base Power launched in Illinois (ComEd/PJM territory) — its first expansion outside Texas — using retail choice, a state VPP incentive law, and ComEd's battery export-compensation rules, explicitly bypassing the interconnection queue via behind-the-meter deployment.
- **2026-04-13:** Base Power's GVEC aggregation passed ERCOT ADER performance testing on its first attempt, as part of a 50 MW territory-wide expansion.
- **2025-10-08:** Base Power disclosed it had qualified for ERCOT's ADER pilot program as part of its $1B Series C announcement.
- **2025-02-19:** PUCT transferred day-to-day management of the ADER pilot to the ERCOT stakeholder process; program had reached only ~25.5 MW energy / ~20 MW reserves against an original 80 MW target.
- **2023-08-22:** ADER pilot participation formally began.
- **2022-10-18:** ERCOT Board of Directors established the ADER pilot project under PUCT direction, targeting 80 MW of aggregated distributed resources.
- **2021-08-30:** Texas AG finalized a settlement releasing [Griddy]({{< relref "griddy.md" >}}) customers from outstanding storm-related bills — the clearest case study of what happens to a wholesale-pass-through retail model with no consumer-side circuit breaker.
- **2021-06-08:** Texas Senate Bill 3 signed, mandating weatherization of generation, transmission, and gas facilities in response to [Winter Storm Uri]({{< relref "winter-storm-uri.md" >}}); PUCT adopted implementing rule (16 TAC §25.55) on October 21, 2021, with a December 1, 2021 compliance deadline.
- **2021-02-13 to 2021-02-17:** [Winter Storm Uri]({{< relref "winter-storm-uri.md" >}}) forces roughly 20,000 MW of manually controlled rolling blackouts across Texas — the largest such load-shed event in U.S. history — exposing the energy-only market's resource-adequacy tradeoffs under extreme weather.
- **2002-01-01:** Texas retail electric choice takes effect statewide under Senate Bill 7 (passed 1999).

## Why This Is Worth Tracking

The Base Power case makes visible something usually invisible in energy policy: market structure, not just technology cost curves, determines where distributed energy innovation happens first. A company with Base Power's exact business model — vertically integrated, oversized home batteries monetized through retail arbitrage plus grid services — is very hard to build in a state without retail choice, because there's no legal path for a hardware company to also be the electricity seller. It's also easier to reach commercial speed in ERCOT specifically, because the energy-only market rewards exactly the kind of price-timing behavior a battery fleet is good at, and the ADER pathway (however slow-growing) gives a route into wholesale ancillary-services revenue that most other ISOs are still building via FERC Order 2222. The open question — being tested in real time by Base Power's Illinois launch — is how much of the Texas outcome depends on ERCOT's specific market design versus how much is simply "retail choice plus one cooperative utility," which is a far more replicable recipe. If Illinois works, it suggests the Texas story is less about Texas exceptionalism and more about a checklist of adoptable policies; if it struggles, that would point back toward ERCOT's energy-only design and FERC exemption as doing more of the real work.

## Claim Verification

### Claim: ERCOT is exempt from FERC jurisdiction because it has no synchronous interconnection to the rest of the U.S. grid

**Status:** Verified

**Supporting sources:**
- [FERC, "ERCOT" official page](https://www.ferc.gov/industries-data/electric/electric-power-markets/ercot) — "The transmission grid that the ERCOT independent system operator administers is located solely within the state of Texas and is not synchronously interconnected to the rest of the United States. The transmission of electric energy occurring wholly within ERCOT is not subject to the Commission's jurisdiction under sections 203, 205, or 206 of the Federal Power Act."

**Summary:** Confirmed directly from FERC's own website; this is an uncontested structural/legal fact, not a disputed claim.

---

### Claim: ERCOT's average interconnection queue wait time is roughly half of PJM's

**Status:** Partially verified

**Supporting sources:**
- Lawrence Berkeley National Laboratory, "Queued Up: 2025 Edition" (referenced via search; full PDF at [eta-publications.lbl.gov](https://eta-publications.lbl.gov/sites/default/files/2025-12/queued_up_2025_edition_12.15.2025.pdf)) — cited figures of ~25 months national average, ~20 months ERCOT, ~40 months PJM

**Summary:** These figures were surfaced via web search summarizing the LBNL report rather than direct extraction from the PDF itself in this session; the general direction (ERCOT meaningfully faster than PJM) is consistent with multiple secondary sources on interconnection queues, but the exact month figures should be treated as approximate until independently re-verified against the primary LBNL dataset.

---

### Claim: Base Power's Illinois/PJM expansion proves the Texas model is portable to other grid regions

**Status:** Unverified (too early)

**Supporting sources:**
- [Canary Media, June 24, 2026](https://www.canarymedia.com/articles/batteries/base-power-cheap-batteries-pjm) — describes the Illinois launch and the specific state/utility policies that made it possible, but the article itself frames this as an open test ("the question had remained whether this model would work outside the particularities of the Texas market")

**Summary:** The Illinois launch is real and underway, but as of this review it is a newly launched pilot with no performance track record yet. Whether it succeeds commercially is a distinct question from whether it was legally/structurally possible — this entry can confirm the latter but not yet the former.

## Sources

- [FERC — ERCOT](https://www.ferc.gov/industries-data/electric/electric-power-markets/ercot)
- [Lawrence Berkeley National Laboratory — Queued Up: 2025 Edition](https://eta-publications.lbl.gov/sites/default/files/2025-12/queued_up_2025_edition_12.15.2025.pdf)
- [Base Power brings cheap batteries to residents in power-starved PJM (Canary Media, June 24, 2026)](https://www.canarymedia.com/articles/batteries/base-power-cheap-batteries-pjm)
- [ERCOT — Aggregate Distributed Energy Resource (ADER) Pilot Project](https://www.ercot.com/mktrules/pilots/ader)
- [Texas regulators move virtual power plant pilot development to ERCOT (Utility Dive, Feb 19, 2025)](https://www.utilitydive.com/news/texas-regulators-move-virtual-power-plant-pilot-development-to-ercot/740304/)
- [Base Power partnership to mitigate price spikes, load peaks for South Texas co-op (Utility Dive, Apr 22, 2026)](https://www.utilitydive.com/news/base-power-partnership-to-mitigate-price-spikes-load-peaks-for-south-texas/818221/)
- [Texas Comptroller — Winter Storm Reform](https://comptroller.texas.gov/economy/fiscal-notes/archive/2021/oct/winter-storm-reform.php)
- [Texas Legislature — SB3 (87th Regular Session) Bill Summary](https://capitol.texas.gov/billlookup/BillSummary.aspx?LegSess=87R&Bill=SB3)
