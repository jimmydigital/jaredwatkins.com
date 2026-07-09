---
title: "Winter Storm Uri (February 2021): The ERCOT Grid Failure"
date: 2026-07-09
lastmod: 2026-07-09
draft: false
description: "Case study of the February 2021 Texas grid failure — root causes, the extended $9,000/MWh price cap, the human and financial toll, and the regulatory response that shaped ERCOT's current market design."
research_area: "energy/grid-markets"
source_urls:
  - "https://comptroller.texas.gov/economy/fiscal-notes/archive/2021/oct/winter-storm-impact.php"
  - "https://texasstandard.org/stories/texas-freeze-winter-storm-2021-death-count/"
  - "https://www.texastribune.org/2021/03/16/griddy-bankruptcy-electricity-bills/"
  - "https://www.cbsnews.com/news/griddy-energy-charged-9000-power-bills-settles-with-texas/"
  - "https://comptroller.texas.gov/economy/fiscal-notes/archive/2021/oct/winter-storm-reform.php"
  - "https://capitol.texas.gov/billlookup/BillSummary.aspx?LegSess=87R&Bill=SB3"
last_reviewed: 2026-07-09
stale_after_days: 180
related:
  - "energy/grid-markets/ercot-market-design.md"
  - "energy/grid-markets/griddy.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **ERCOT** — Electric Reliability Council of Texas; the grid operator whose service area covers about 90% of the state.
- **PUCT** — Public Utility Commission of Texas; sets ERCOT's market rules, including the wholesale price cap referenced throughout this entry.
- **Rolling blackouts** — Planned, short, rotating power cuts across different neighborhoods, used to reduce total grid demand without cutting everyone off at once; intended as temporary, they stretched into multi-day outages for some Texans during Uri.
- **Black start** — The process of restoring a power grid completely from a total, uncontrolled collapse. Far slower and more damaging than a managed rolling-blackout event; ERCOT narrowly avoided needing one.
- **Price cap** — The maximum dollar-per-megawatt-hour price regulators allow in the wholesale market; ERCOT's cap was $9,000/MWh during Uri, versus a typical average of about $35/MWh.
- **Weatherization** — Insulating and protecting power plants, gas wells, and pipelines against extreme cold (or heat) so they keep operating; Senate Bill 3 made this mandatory in Texas after Uri.
- **Excess mortality** — A statistical method that estimates disaster deaths by comparing actual deaths in a period to the number that would normally be expected, rather than relying only on death certificates that explicitly cite the disaster as a cause.
- **MW / MWh** — Megawatt (a unit of power) and megawatt-hour (a unit of energy delivered over an hour) — the units used for the ~20,000 MW of blackouts and the $9,000/MWh price cap described in this entry.

## Summary

Winter Storm Uri (February 13–17, 2021) is the failure case study for ERCOT's market design: a multi-day arctic blast that knocked out generation across every fuel source simultaneously, forced roughly 20,000 MW of manually controlled rolling blackouts — the largest such event in U.S. history — and left the grid, per a University of Texas at Austin analysis, narrowly short of a total, weeks-long collapse. Texas's official death count stands at 246, but independent excess-mortality studies place the true toll several times higher. The storm also produced a second, self-inflicted disaster: ERCOT held the wholesale price at its $9,000/MWh cap for roughly 32 hours longer than an independent market monitor said conditions justified, adding an estimated $16 billion in overbilling on top of an already catastrophic event. The event forced out ERCOT's CEO and the entire Public Utility Commission of Texas, and produced Senate Bill 3's weatherization mandate — the regulatory backbone that still governs ERCOT's resource adequacy approach today.

## Key Facts

- **Event dates:** February 13–17, 2021 (impacts and grid stress continued through February 19)
- **Scale of outage:** Blackouts spanned most of Texas from February 15–18; a University of Houston Hobby School survey found 69% of Texans lost power at some point during February 14–20, with an average outage of about 42 hours (31 of those consecutive)
- **Grid dependency:** More than 26 million Texans (about 90% of the state's population) rely on ERCOT
- **Generation mix at the time (February 2021):** Natural gas ~51%, wind ~24.8%, coal ~13.4%, nuclear ~4.9%, solar ~3.8%, storage ~0.2% of ERCOT's generating capacity
- **Official death toll:** 246 (Texas Department of State Health Services, finalized report dated December 30, 2021); an earlier running count stood at 210 as of an October 2021 state report
- **Independent excess-mortality estimates:** BuzzFeed News (May 2021) estimated 426–978 deaths (mean ~702); a separate excess-mortality analysis by researcher Ariel Karlinsky (a member of the WHO's technical advisory group on COVID-19 mortality) estimated 814 — both several times the official count
- **Estimated economic toll:** $80 billion to $130 billion, per sources cited by the Federal Reserve Bank of Dallas (April 2021)
- **Price cap:** The Public Utility Commission of Texas (PUCT) raised the wholesale price to its $9,000/MWh cap (versus an average of about $35/MWh) to incentivize generation; an independent market monitor found ERCOT kept the price at that cap for roughly 32 hours longer than conditions warranted, resulting in an estimated $16 billion in overbilling to power companies system-wide
- **Corporate/financial fallout:** Brazos Electric Power Cooperative, Texas's largest electric cooperative, filed for bankruptcy after incurring $2.1 billion in ERCOT charges; retail electric provider Griddy was forced out of the market and filed bankruptcy (see [Griddy]({{< relref "griddy.md" >}}))
- **Governance fallout:** ERCOT's CEO was fired; all three sitting PUCT commissioners resigned; several ERCOT board members (including some living outside Texas) also resigned amid public criticism
- **Legislative response:** Senate Bill 3, signed June 8, 2021, mandated weatherization of generation, transmission, and natural gas facilities, with PUCT-enforced fines and inspections

## What Happened

**The setup.** A UT-Austin post-event analysis found that Winter Storm Uri, while not the most severe winter storm on Texas record, caused the most electricity loss of any storm in ERCOT history. Multiple compounding failures were responsible: ERCOT's demand forecast underestimated the actual peak by nearly 14%, weather forecasts misjudged both the severity and timing of the cold, and generator outages — while nominally within the range anticipated in ERCOT's seasonal planning — were unusually concentrated and hit every major fuel source at once. Frozen natural gas wellheads curtailed gas production and processing before it could reach power plants; a nuclear plant tripped offline; coal piles froze; and wind turbines iced over. Rolling blackouts, designed as a short-term "last line of defense" to protect the grid from a full collapse, stretched into multi-day outages for many Texans because there was not enough surviving generation to safely restore power in rotation.

**The near-catastrophe.** Per the UT-Austin report, the grid did not fully stabilize until February 19, having "narrowly missed a catastrophic failure" — industry shorthand for an uncontrolled, cascading blackout that would have required a black start (rebuilding the grid from zero) potentially taking weeks and causing far more extensive damage to transmission and generation equipment than the managed rolling blackouts that did occur.

**The pricing scandal within the crisis.** Separate from the physical failure, the PUCT's decision to hold wholesale prices at the $9,000/MWh cap became its own controversy. According to reporting on findings from an independent market monitor, ERCOT was expected to let the price fall back toward market-clearing levels once emergency conditions eased, but instead kept it at the cap for roughly 32 additional hours — adding an estimated $16 billion in charges across the market on top of the already-extreme storm costs. This is a distinct failure from the physical grid emergency: it was a pricing-administration decision, not a supply shortage, and it directly set up downstream failures like Griddy's collapse and Brazos Electric's bankruptcy, since both were exposed to ERCOT's real-time wholesale price.

**Human cost and the undercounting problem.** Texas's official death toll — 246, as finalized by the state health department in a December 2021 report — counts only deaths where a medical examiner or coroner explicitly attributed a role to the storm. Researchers who study excess mortality (deaths above the statistically expected baseline) argue this significantly undercounts the true toll: a BuzzFeed News analysis estimated 426–978 deaths, and a separate excess-mortality study by a WHO-affiliated researcher put the figure at 814. Both approaches found the excess-mortality signal was concentrated in Texas and not present in neighboring states that had similarly severe weather but did not lose power — evidence, researchers argue, that the deaths tracked the blackout rather than the cold alone. The gap between the official count and these estimates remains a live methodological and political dispute, not a resolved question.

## Notable Developments

- **2021-08-30:** Texas Attorney General finalized a settlement with Griddy Energy releasing customers from outstanding storm-related bills (see [Griddy]({{< relref "griddy.md" >}}) for details).
- **2021-06-08:** Senate Bill 3 signed, mandating weatherization of generation, transmission, and gas facilities; PUCT adopted implementing rule (16 TAC §25.55) on October 21, 2021, with a December 1, 2021 compliance deadline.
- **2021-05:** BuzzFeed News published an excess-mortality analysis estimating 426–978 storm-related deaths, several times the state's contemporaneous count.
- **2021-03-15:** Griddy filed for Chapter 11 bankruptcy after being ejected from the ERCOT market.
- **2021-03 (spring legislative session):** ERCOT's CEO was fired; all three PUCT commissioners resigned; the governor appointed new commissioners and a new ERCOT CEO.
- **2021-02-19:** Grid conditions normalized; UT-Austin's later analysis found the system had narrowly avoided a full cascading collapse.
- **2021-02-15 to 2021-02-18:** Manually controlled rolling blackouts spread across most of Texas.
- **2021-02-13 to 2021-02-14:** Generator outages begin; ERCOT issues a public conservation appeal as generation cannot meet demand.
- **2021-02-12:** Texas Governor Greg Abbott issues a state of emergency declaration ahead of the storm.
- **2021-12-30:** Texas Department of State Health Services finalizes its official mortality surveillance report at 246 deaths.

## Why This Is Worth Tracking

Uri is the reference event for every claim made about ERCOT's resilience, and it directly shapes the current [ERCOT market design]({{< relref "ercot-market-design.md" >}}): the weatherization mandates (SB3), the governance overhaul (new PUCT commissioners, new ERCOT leadership), and the political memory that makes both regulators and companies like Base Power emphasize backup power and grid resilience in their marketing are all downstream of this event. It's also a caution against treating "energy-only market" and "retail choice" as unambiguously good things without qualification: the same market structure that lets a well-capitalized, vertically integrated company like Base Power thrive on price volatility is the one that let an under-capitalized wholesale-pass-through retailer like Griddy expose ordinary customers to five-figure bills with no circuit breaker. Evaluating any Texas grid-market innovation should include asking what happens to it — and to the people relying on it — the next time an extreme event pushes prices to the cap for days rather than hours.

## Claim Verification

### Claim: Texas's official Winter Storm Uri death toll is undercounted, and the true toll is several times higher

**Status:** Disputed (methodologically, not politically resolved)

**Supporting sources:**
- [Texas Standard, Aug 5, 2022](https://texasstandard.org/stories/texas-freeze-winter-storm-2021-death-count/) — reports the official DSHS count of 246, alongside a WHO-affiliated researcher's excess-mortality estimate of 814 and a BuzzFeed News estimate of 426–978 (mean ~702); notes the excess-mortality signal was unique to Texas relative to neighboring states with similarly bad weather but no comparable outages

**Refuting/questioning sources:**
- The Texas Department of State Health Services has stated its published count reflects only deaths where a medical examiner or coroner explicitly attributed a causal role to the storm, and describes its number as a count rather than a statistical estimate — implying the two figures are answering different questions rather than one being simply "wrong"

**Summary:** The official count (246) and the excess-mortality estimates (roughly 700–800+) are not directly reconcilable because they use fundamentally different methodologies (causal attribution by a coroner vs. statistical deviation from expected baseline mortality). Independent researchers argue the excess-mortality approach is more complete; the state's position is that its count reflects verified causal attribution. Both figures should be reported together rather than treating either as the single correct number.

---

### Claim: ERCOT kept the wholesale price at its $9,000/MWh cap for roughly 32 hours longer than conditions warranted, adding $16 billion in overbilling

**Status:** Partially verified

**Supporting sources:**
- [Texas Tribune, Mar 16, 2021](https://www.texastribune.org/2021/03/16/griddy-bankruptcy-electricity-bills/) — reports the finding, attributed to "an independent market monitor," that ERCOT should have let prices fall the day after the storm's peak but instead held them at the cap for 32 additional hours, "overbilling power companies by $16 billion"

**Summary:** This entry relies on a single news source's characterization of the market monitor's finding rather than the market monitor's report itself, which was not directly fetched in this session. The core fact pattern (extended price-cap period, an official finding of overbilling, subsequent legislative action to address it) is corroborated by the broader contemporaneous reporting on the Texas Senate's rapid response bill referenced in the same article, but the exact $16 billion figure should be treated as a media-reported characterization pending direct verification against the original market monitor report.

## Sources

- [Texas Comptroller — Winter Storm Uri 2021: The Economic Impact of the Storm](https://comptroller.texas.gov/economy/fiscal-notes/archive/2021/oct/winter-storm-impact.php)
- [Texas has an official death count from the 2021 blackout. The true toll may never be known. (Texas Standard, Aug 5, 2022)](https://texasstandard.org/stories/texas-freeze-winter-storm-2021-death-count/)
- [Griddy Energy customers may be off the hook for exorbitant energy bills after company files bankruptcy (Texas Tribune, Mar 16, 2021)](https://www.texastribune.org/2021/03/16/griddy-bankruptcy-electricity-bills/)
- [Griddy Energy settles with Texas, releasing customers from $9,000 power bills during freeze (CBS News, Aug 31, 2021)](https://www.cbsnews.com/news/griddy-energy-charged-9000-power-bills-settles-with-texas/)
- [Texas Comptroller — The 87th Legislature Takes On Electricity Reform](https://comptroller.texas.gov/economy/fiscal-notes/archive/2021/oct/winter-storm-reform.php)
- [Texas Legislature — SB3 (87th Regular Session) Bill Summary](https://capitol.texas.gov/billlookup/BillSummary.aspx?LegSess=87R&Bill=SB3)
