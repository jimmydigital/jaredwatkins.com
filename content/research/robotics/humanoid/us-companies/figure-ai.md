---
title: "Figure AI"
date: 2026-06-19
lastmod: 2026-06-19
draft: false
description: "Sunnyvale, CA humanoid robot startup; highest private valuation in the sector at $39B; ~$1.9B raised; Figure 03 general-purpose industrial robot; BotQ manufacturing facility; 619 employees."
research_area: "robotics/humanoid"
source_urls:
  - "https://figure.ai"
  - "https://techmarketbriefs.com/pre-ipo/figure-ai/"
  - "https://www.therobotreport.com/figure-ai-raises-675m-to-commercialize-humanoids/"
  - "https://www.therobotreport.com/figure-ai-unveils-botq-high-volume-humanoid-manufacturing-facility/"
  - "https://www.bloomberg.com/news/videos/2026-05-15/figure-ceo-says-humanoid-robot-test-had-no-outside-aid-video"
  - "https://sacra.com/c/figure-ai/"
  - "https://en.wikipedia.org/wiki/Brett_Adcock"
last_reviewed: 2026-06-19
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Figure AI is the highest-valued private humanoid robotics company as of mid-2026, at a reported $39 billion valuation on ~$1.9 billion in total funding. The company is developing the Figure 03 general-purpose humanoid for industrial deployment. Its BotQ manufacturing facility in Sunnyvale achieved one robot per hour production rate by early 2026. Figure's valuation already exceeds Goldman Sachs' entire projected global humanoid market for 2035 — a disparity that investors and analysts cite as a key risk.

## Key Facts

- **Founded:** 2022
- **HQ:** Sunnyvale, CA
- **Type:** Company — Platform OEM
- **Status:** Active; commercial production ramping
- **Employees:** ~619 (as of April 2026)
- **Total funding:** ~$1.9B across all rounds
- **Valuation:** $39B (September 2025, Series C)
- **Robot:** Figure 03 — general-purpose bipedal humanoid
- **Manufacturing:** BotQ facility, San Jose; 12,000 units/year design capacity; scaling to 100,000/year target
- **Production rate:** ~1 robot/hour as of early 2026 (up from 1/day in January 2026)
- **Value chain position:** Platform OEM; vertically integrated (actuators, sensors, batteries all in-house)

## Funding & Investors

| Round | Date | Amount | Lead / Notable Investors |
|-------|------|--------|--------------------------|
| Seed | 2022 | $100M | Brett Adcock (founder self-funded) |
| Series A | 2023 | $70M | Undisclosed |
| Series B | Feb 2024 | $675M | Microsoft, OpenAI Startup Fund, NVIDIA, Jeff Bezos (Bezos Expeditions), Intel Capital, LG Technology Ventures, Samsung Ventures; $2.6B post-money |
| Series C | Sep 2025 | >$1B | Parkway Venture Capital (lead), Brookfield Asset Management, NVIDIA, Intel Capital, Microsoft, OpenAI Startup Fund, Bezos Expeditions; $39B post-money |

**Total raised:** ~$1.9B. The Series C represents a 15× valuation increase in 18 months from the Series B.

**Notable investor signal:** NVIDIA participation across both Series B and C is significant — NVIDIA is supplying compute (Jetson Orin / Blackwell chips) and has a strategic interest in humanoid adoption as a GPU-intensive inference workload.

## What It Is / How It Works

Figure AI was founded by Brett Adcock with the stated goal of building a general-purpose humanoid robot capable of operating in any environment humans work in. The Figure 03 is a full-size bipedal platform at roughly human dimensions and weight class.

**Vertical integration strategy:** Unlike most competitors that source actuators from Maxon, Nabtesco, or Chinese suppliers, Figure designs and manufactures its own actuators, battery packs, sensors, and electronics entirely in-house. The BotQ facility has produced 9,000 actuators across 10 distinct SKUs with >80% first-pass yield. The stated supply chain goal is to source 3 million actuators internally — equivalent to 200,000+ robots at 15 actuators each. Adcock stated a target of full supply chain decoupling from China by summer 2026.

**AI training approach:** Figure uses teleoperation data collection paired with imitation learning to train task policies. The BMW pilot (2024) generated training data; ongoing internal deployments continue to build the dataset. Figure 03 is claimed to run fully onboard inference without cloud dependency.

**Figure 03 battery:** 5-hour runtime; 2.3 kWh pack; wireless inductive charging. This is among the longest stated runtimes in the sector and positions Figure 03 favorably against Digit's 90-minute pack.

**BotQ facility:** Located in San Jose; unveiled 2025; initially producing 12,000 units/year with a stated scale plan to 100,000/year over four years. As of early 2026 the rate was one robot per hour — 8,760/year annualized if sustained 24/7. BMW Spartanburg has 40 Figure 03 units deployed, completing 90,000+ parts across 1,250+ operational hours.

## Founder Background

**Brett Adcock** — Founder & CEO
- Born April 6, 1986, Moweaqua, Illinois
- B.S. Finance & Real Estate, University of Florida (~2008)
- **Vettery (2013–2018):** Co-founded AI-driven recruiting marketplace; scaled to hundreds of employees and 30,000 company network; sold to Adecco Group for $100M in 2018
- **Archer Aviation (2018–2022):** Co-founded eVTOL aircraft company; led through SPAC merger at $3.8B valuation in 2021; signed $1.5B deal with United Airlines; oversaw 5 generations of aircraft with in-house actuation, flight software, and electric motor development — directly transferable experience to Figure's vertical integration approach
- **Figure AI (2022–present):** Self-funded initial $100M seed; recruited engineering team from aerospace, automotive, and robotics backgrounds
- LinkedIn: [brettadcock](https://www.linkedin.com/in/brettadcock/)
- Net worth: estimated at $19 billion as of early 2026 (Forbes, NYT), primarily from Figure AI equity at the $39B Series C valuation

**Pattern:** Adcock is a serial hardware entrepreneur who explicitly applies lessons from Archer Aviation's vertical integration to Figure — own the actuators, own the supply chain, do not depend on third-party component vendors who may not be able to scale with you.

### People — Last Reviewed: 2026-06-19

## Supply Chain & Dependencies

**Actuators (40–60% of BoM):** Self-developed; BotQ produces all actuators in-house. This is Figure's key differentiation — most competitors buy actuators from Maxon (Swiss), Nabtesco (Japanese), or Chinese vendors. In-house production eliminates supply dependency but concentrates manufacturing risk.

**Compute:** NVIDIA chips (Jetson Orin class / Blackwell inference); NVIDIA is both investor and supplier — a dependency worth flagging. If NVIDIA supply tightens (as it did 2023–2024 for GPU chips), Figure's production could be constrained.

**Sensors:** Cameras and depth sensors; suppliers not publicly disclosed. RGB-D sensor supply chain is currently dominated by Intel RealSense (exiting), Microsoft Azure Kinect (discontinued), and emerging alternatives from Luxonis and Chinese vendors.

**Battery:** In-house pack design; cell sourcing not disclosed. Likely LFP or NMC cells from Asian suppliers — the same supply chain dependency that affects EV manufacturers.

**China decoupling:** Adcock's stated goal of full supply chain decoupling from China by summer 2026 is ambitious given that precision bearings, rare-earth permanent magnets (NdFeB for motors), and many passive components are >80% China-sourced globally. Independent verification of decoupling completion is not available.

## Claim Verification

### Claim: Figure 03 capable of "fully autonomous 24/7 operation without human supervision"

**Status:** Unverified

**Supporting sources:**
- [Figure AI news — introducing Figure 03](https://www.figure.ai/news/introducing-figure-03) — company asserts full autonomy
- [Bloomberg, May 2026](https://www.bloomberg.com/news/videos/2026-05-15/figure-ceo-says-humanoid-robot-test-had-no-outside-aid-video) — CEO states no teleoperation in testing

**Refuting / questioning sources:**
- No external paying customer has publicly confirmed Figure 03 doing sustained autonomous productive work at commercial scale
- Figure has zero external commercial customers as of Q1 2026 — all deployment is internal or in controlled pilots with BMW

**Summary:** Company-asserted; no independent third-party verification. The BMW pilot generated media coverage but no independent productivity verification.

### Claim: $39B valuation is justified

**Status:** Disputed

**Supporting sources:**
- Morgan Stanley projects $5T humanoid market by 2050 — at that scale, current valuation is defensible
- NVIDIA, Microsoft, and Bezos participation signals conviction from technically sophisticated investors

**Refuting / questioning sources:**
- [Goldman Sachs](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035) — entire global humanoid market projected at $38B by 2035; Figure's single-company valuation already equals this
- [Humanoid Robot Bubble — Talking Logistics, Jan 2026](https://talkinglogistics.com/2026/01/12/the-humanoid-robot-bubble-is-getting-hard-to-ignore/) — zero external revenue, zero external customers

**Summary:** Requires Morgan Stanley's scenario to be correct. Goldman's numbers make the valuation indefensible at the conservative estimate.

## Sources

- [Figure AI official site](https://figure.ai)
- [Figure AI IPO analysis — Tech Market Briefs](https://techmarketbriefs.com/pre-ipo/figure-ai/)
- [Figure AI raises $675M Series B — The Robot Report](https://www.therobotreport.com/figure-ai-raises-675m-to-commercialize-humanoids/)
- [BotQ manufacturing facility — The Robot Report](https://www.therobotreport.com/figure-ai-unveils-botq-high-volume-humanoid-manufacturing-facility/)
- [Figure CEO no outside aid — Bloomberg, May 2026](https://www.bloomberg.com/news/videos/2026-05-15/figure-ceo-says-humanoid-robot-test-had-no-outside-aid-video)
- [Figure AI funding and valuation — Sacra](https://sacra.com/c/figure-ai/)
- [Brett Adcock — Wikipedia](https://en.wikipedia.org/wiki/Brett_Adcock)
- [Goldman Sachs $38B market projection](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035)
- [Humanoid robot supply chain — McKinsey](https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins)
