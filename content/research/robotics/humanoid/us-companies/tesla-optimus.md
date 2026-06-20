---
title: "Tesla Optimus"
date: 2026-06-19
lastmod: 2026-06-19
draft: false
description: "Tesla's internally-developed humanoid program; 1,000+ units in learning/data-collection mode inside Tesla factories; $20B 2026 capex across all programs; zero external customers; full vertical integration strategy; Milan Kovac VP Engineering."
tags: ["humanoid", "robotics", "us", "industrial", "tesla"]
categories: ["company"]
research_area: "robotics/humanoid"
source_urls:
  - "https://standardbots.com/blog/tesla-robot"
  - "https://newmarketpitch.com/blogs/news/humanoid-robotics-optimus-deployment-tracker"
  - "https://ir.tesla.com/sec-filings/annual-reports"
  - "https://newmarketpitch.com/blogs/news/humanoid-robotics-figure-vs-tesla"
last_reviewed: 2026-06-19
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Tesla's Optimus program is one of the most publicized humanoid robot programs globally, driven by CEO Elon Musk's recurring and repeatedly revised timeline claims. As of Q1 2026, Tesla has deployed over 1,000 Optimus units inside its own factories, but explicitly in "learning and data collection" mode — not productive operation. Musk stated in the Q4 2025 earnings call that Optimus units are "primarily for learning and data collection, not productive tasks." Tesla has zero external paying customers for Optimus. The program is self-funded through Tesla's capital, with $20B in capex committed for 2026 across all Tesla programs including Optimus.

## Key Facts

- **Program origin:** 2021 (announced Tesla AI Day)
- **Developer:** Tesla, Inc. (NASDAQ: TSLA) — internal program
- **Type:** Internal OEM; self-funded
- **Status:** Internal R&D / data collection mode; no external commercial deployment
- **Capital commitment:** $20B capex for 2026 (all Tesla programs including Optimus, AI compute, vehicles)
- **Employees on Optimus:** Not disclosed; part of Tesla's ~140,000 total headcount
- **Units deployed:** 1,000+ inside Tesla factories (Q1 2026; learning/data-collection mode)
- **External customers:** Zero as of Q1 2026
- **Robot:** Optimus Gen 2 — bipedal, ~5'8", ~125 lbs; 28 degrees of freedom (hands: 11 DoF each)
- **Value chain position:** Fully vertically integrated OEM (designs, manufactures, and deploys internally)

## Capital Commitment

Optimus is funded through Tesla's corporate balance sheet rather than external venture rounds:

| Year | Capital Event | Optimus Relevance |
|------|---------------|-------------------|
| 2021 | AI Day announcement | Concept revealed; initial engineering allocated |
| 2023 | $1B+ raised in equity | Used for Gigafactory expansion and AI/compute |
| 2025 | $20B capex announced for 2026 | Covers Optimus manufacturing, AI datacenter (Cortex), vehicle production |
| 2026 | Fremont Model S line converted | Dedicated Optimus manufacturing line |

**Self-funding advantage:** Tesla's ability to self-fund means Optimus isn't subject to the startup funding cycle (raise → deploy → prove → raise again). This allows longer-horizon development without investor pressure. Disadvantage: Optimus must compete with vehicle production, Megapack, and FSD for engineering resources and capital allocation — all businesses with near-term revenue.

## What It Is / How It Works

Optimus is a bipedal humanoid standing ~5'8", weighing ~125 lbs, with 28 degrees of freedom and an estimated 11 DoF per hand (the most capable hand design in the sector). Tesla designs its own actuators, sensors (using the same FSD vision system from vehicles), battery pack, and AI stack — full vertical integration mirroring Tesla's vehicle design philosophy.

**Actuators:** Tesla designs custom rotary and linear actuators for Optimus in-house. The actuator design team came from SpaceX (propulsion actuators) and Tesla Vehicle (powertrain motors). Specific actuator architecture (SEA vs. QDD vs. direct drive) is not publicly detailed but appears to be a custom hybrid. Tesla claims manufacturing cost advantage from integrated production alongside vehicle powertrains.

**AI and perception:** Optimus uses Tesla's FSD (Full Self-Driving) neural network architecture and training infrastructure. The same Dojo supercomputer cluster that trains the vehicle AI trains Optimus policies. Teleoperation data from human operators inside Tesla factories is the primary training signal. Tesla's scale advantage in AI training compute (Dojo) is potentially significant — Optimus has access to far more training compute than any startup competitor.

**Training pipeline:** 1,000+ internal units running inside Tesla factories generate continuous operational data even in "learning mode." A robot "failing to perform a task" still generates useful trajectory and environmental data. The sheer volume of hardware deployed for data collection is unprecedented in the sector.

**Battery:** In-house LiPo/NMC pack, manufactured with expertise from Tesla vehicle battery production. Runtime not publicly specified but likely 2+ hours given Tesla's battery density expertise.

**FSD transfer:** Tesla's Autopilot/FSD team has solved related problems (visual scene understanding, obstacle avoidance, behavioral planning) that directly apply to humanoid robot navigation. This transfer is Optimus's key AI advantage over startups building perception stacks from scratch.

## Founder / Key People

**Elon Musk** — CEO, Tesla; Optimus program champion
- Vision owner; responsible for public timeline claims; drives resource allocation decisions
- Notable: Musk's track record of aggressive timelines that ultimately prove achievable (SpaceX Falcon Heavy, Model 3 production) but later than stated has defined the Optimus narrative

**Milan Kovac** — Former VP of Engineering, Optimus *(departed June 2025)*
- Former SpaceX engineer (propulsion systems)
- Led Optimus hardware and systems engineering from 2022 until departing June 2025

**Ashok Elluswamy** — Director, Autopilot/AI; took over Optimus program leadership June 2025
- Oversees the neural network and AI training stack shared between FSD and Optimus
- PhD from CMU Robotics Institute
- The leadership transition signals tighter integration between FSD AI and the Optimus program

**Lars Moravy** — VP of Vehicle Engineering
- Oversees actuator and powertrain components that share manufacturing with Optimus

### People — Last Reviewed: 2026-06-19

## Supply Chain & Dependencies

**Actuators (40–60% of BoM):** In-house design and manufacturing. Tesla's servo motor expertise from electric vehicle powertrain (PMSM motors) directly applies. Tesla manufactures its own motor windings, which is a competitive advantage for volume cost reduction. Custom rotary actuators for joints, linear actuators for torso. No external actuator vendor dependency — the clearest vertical integration in the sector.

**Compute:** Tesla FSD chip (custom silicon, designed in-house, manufactured by Samsung/TSMC). Dojo supercomputer for training. The FSD chip running in Tesla vehicles is the same silicon architecture used in Optimus — massive volume leverage on chip design costs. This is Figure AI's stated goal but Tesla is already here.

**Sensors:** Camera-only vision system (no LiDAR), consistent with FSD philosophy. Uses same camera modules as Tesla vehicles — volume leverage on sensor costs. No depth sensors or LiDAR in current design; neural networks handle depth estimation from stereo camera pairs.

**Battery:** Tesla 4680 cells (in-house manufacturing, Gigafactory Nevada/Texas). Battery cost leverage from vehicle production scale is among the strongest in the industry. However, critical minerals (lithium, cobalt, nickel) remain supply-chain dependencies regardless of pack design.

**Manufacturing:** Converting Fremont's Model S line to Optimus production in 2026. Gigafactory infrastructure (casting, machining, assembly) already in place. Scale-up path is cleaner than any startup competitor — Tesla has experience running high-volume precision manufacturing at Gigafactories.

**Rare earth dependency:** NdFeB permanent magnets for all PMSM motors depend on Chinese rare-earth production (~90% of global processing). Tesla reduced cobalt in vehicle batteries (LFP adoption) but magnet supply from China is harder to diversify. This is a systemic dependency shared with all motor-based humanoids.

## Notable Developments

| Date | Event |
|------|-------|
| 2021 | Tesla AI Day: "Tesla Bot" announced; Musk predicted 1M units "in a few years" |
| 2022 | First Optimus prototype shown; could barely walk; dressed in spandex suit with human inside in initial teaser |
| 2023 | Optimus Gen 1 demonstrated folding laundry — later revealed to be heavily scripted, non-generalizable; Tesla acknowledged limited scope on questioning |
| 2024 | Optimus Gen 2: improved hand dexterity (11 DoF/hand), faster walking speed, lighter weight |
| Jun 2025 | Milan Kovac (Optimus program lead since 2022) departs Tesla; Ashok Elluswamy (FSD/Autopilot head) takes over Optimus, signaling tighter AI integration |
| Jul 2025 | Q2 2025 earnings: Musk admits only hundreds of units built vs. 5,000-unit target — >90% miss |
| Oct 2025 | Kung fu demo confirmed fully AI-driven (not teleoperated) — first verified proof of complex autonomous movement |
| Dec 2025 | Optimus running video goes viral; significant locomotion improvement over walking-only demos |
| Jan 2026 | Q4 2025 earnings: units "primarily for learning and data collection, not productive tasks"; Fremont Model S/X lines announced for discontinuation, converting to Optimus production |
| Jan 2026 | Gen 3 hand production starts at Fremont pilot line — 22 DOF, 50 actuators |
| Mar 2026 | Musk confirms Gen 3 "walking around" inside Tesla facilities; Q1 2026 public unveil delayed for "finishing touches" |
| Apr 2026 | Optimus program lead Konstantinos Laskaris keynotes ETH Zurich, reveals Gen 3 silhouette; four design pillars: usefulness, safety, reliability, mass-manufacturability |

## Claim Verification

### Claim: Tesla will produce 1 million Optimus units "in a few years" (stated 2021–2023)

**Status:** Not on track (as of 2026)

**Supporting sources:**
- Tesla's Fremont factory conversion and $20B capex indicate intent to scale
- Internal deployment of 1,000+ units is real hardware at real scale (more than any other company)

**Refuting / qualifying sources:**
- [Optimus deployment tracker — New Market Pitch, 2026](https://newmarketpitch.com/blogs/news/humanoid-robotics-optimus-deployment-tracker) — actual vs. announced timeline comparison; internal learning-mode units ≠ commercial production
- Q4 2025 earnings: "primarily learning and data collection" contradicts commercial scale narrative
- 1,000 internal units across Tesla's global manufacturing is not "1 million units"

**Summary:** Repeated timeline slippage; current state is internal data collection. The 1M unit prediction from 2021 was wildly optimistic; but Tesla is further along on physical hardware quantity than any startup competitor.

### Claim: Optimus will be Tesla's most important and valuable product

**Status:** Speculative

**Supporting sources:**
- Morgan Stanley: if Optimus achieves mass deployment, optionality value could exceed vehicle business
- Tesla's AI training infrastructure (Dojo) and FSD transfer give Optimus a credible path competitors lack

**Refuting / qualifying sources:**
- Zero revenue from Optimus as of Q1 2026
- FSD itself has been "one year from release" since 2016 — Tesla's AI timeline credibility is impaired
- The "most important product" framing sets up every quarterly miss as a narrative failure

**Summary:** Long-term speculative thesis with a credible technical pathway; near-term commercial timeline remains undefined.

## Sources

- [Tesla robot specs and pricing — Standard Bots, 2026](https://standardbots.com/blog/tesla-robot)
- [Tesla Optimus deployment tracker — New Market Pitch, Apr 2026](https://newmarketpitch.com/blogs/news/humanoid-robotics-optimus-deployment-tracker)
- [Figure vs. Tesla comparison — New Market Pitch](https://newmarketpitch.com/blogs/news/humanoid-robotics-figure-vs-tesla)
- [Tesla investor relations / annual reports](https://ir.tesla.com/sec-filings/annual-reports)
