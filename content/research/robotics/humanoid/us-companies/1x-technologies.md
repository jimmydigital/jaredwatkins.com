---
title: "1X Technologies"
date: 2026-06-19
lastmod: 2026-07-18
draft: false
description: "Norwegian-founded, US-operated humanoid startup; $136.5M raised; OpenAI and EQT Ventures backed; NEO consumer robot open for pre-order at $20,000 (or $499/month) since Oct 2025, 22-DoF five-finger hands, Redwood AI + NVIDIA Jetson Thor Cortex compute; ~60–70% autonomy with 'Expert Mode' teleoperation for remainder; Bernt Børnich founder."
research_area: "robotics/humanoid"
source_urls:
  - "https://1x.tech"
  - "https://techcrunch.com/2023/03/23/1x-technologies-raises-23-5m-series-a-from-openai/"
  - "https://techcrunch.com/2024/01/08/1x-technologies-series-b/"
  - "https://medium.com/@mehul.chourasia28/the-truth-about-humanoid-robots-in-2026-3ae82e9061b1"
  - "https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"
  - "https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/"
  - "https://www.1x.tech/discover/neo-home-robot"
last_reviewed: 2026-07-18
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

1X Technologies is a Norwegian-founded startup with US operations, backed by OpenAI and EQT Ventures. Its NEO robot is marketed as the "world's first consumer-ready home humanoid." 1X opened consumer pre-orders for NEO on October 30, 2025 — Early Access costs $20,000 (with a $200 deposit) or $499/month, with first deliveries to US homes beginning in 2026 and expansion to other markets from 2027. NEO ships with a feature called "Expert Mode"/scheduled teleoperation — human teleoperators at 1X control the robot remotely for tasks it cannot handle autonomously. Independent estimates place NEO's autonomous task completion at ~60–70%, meaning roughly a third of operations involve remote human control. This is the most clearly disclosed example of the teleoperation-as-a-service model that critics argue is pervasive but largely undisclosed across the humanoid sector. 1X also separately deploys a wheeled industrial robot (EVE/Android) in commercial settings.

## Key Facts

- **Founded:** 2021 (Moss, Norway)
- **HQ:** Norway (founding / engineering); Santa Clara, CA (US operations)
- **Type:** Company — Platform OEM + teleoperation service provider
- **Status:** Active; NEO pre-orders open since Oct 30, 2025; first US home deliveries in 2026, other markets from 2027; EVE commercial deployments ongoing
- **Employees:** 100+ (2023 figure; likely higher by 2026)
- **Total funding:** $136.5M across 3 rounds
- **Robots:** NEO (bipedal, consumer); EVE/Android (wheeled, industrial)
- **NEO price:** $20,000 Early Access ($200 deposit) or $499/month subscription
- **NEO specs:** 66 lb (29.9 kg); lifts up to 154 lb (69.8 kg); carries 55 lb (24.9 kg); 22-DoF five-finger hands (44 DoF across both); soft 3D-lattice polymer body; patented Tendon Drive actuation; NVIDIA Jetson Thor-based "Cortex" compute; Wi-Fi/Bluetooth/5G
- **Autonomy level (NEO):** ~60–70% autonomous at launch; ~30–40% via "Expert Mode" teleoperation
- **Value chain position:** Platform OEM + AI/teleoperation service

## Funding & Investors

| Round | Date | Amount | Lead / Notable Investors |
|-------|------|--------|--------------------------|
| Series A | Mar 2023 | $23.5M | OpenAI Startup Fund (lead); Tiger Global, Sandwater, Alliance Ventures, Skagerak Capital |
| Series B | Jan 2024 | $100M | EQT Ventures (lead); Samsung NEXT, Nistad Group; OpenAI Startup Fund follow-on |
| Additional | 2024–2025 | ~$13M | Undisclosed |

**Total raised:** $136.5M across approximately 3 rounds.

**OpenAI Startup Fund:** OpenAI's direct investment in the Series A (the only robotics company in OpenAI's initial startup fund portfolio) signals that 1X is OpenAI's hardware partner hypothesis — if OpenAI's language and vision models become the AI backbone for humanoids, 1X is the early bet on that future.

**EQT Ventures:** Scandinavian growth equity fund; investment makes sense given 1X's Norwegian origins and EQT's interest in European deep tech.

**Tiger Global:** Presence of a large growth equity fund in a 2023 Series A signals confidence in 1X's potential scale; Tiger Global has been burned on late-stage bets in other sectors but continues to participate in AI-adjacent hardware.

**Note on valuation:** 1X has not publicly disclosed a post-money valuation for either round. At $136.5M total, 1X is substantially smaller than Figure AI ($1.9B) or Apptronik ($935M) — consistent with its position as a company that made an early autonomy disclosure tradeoff rather than raising on maximum ambition.

## What It Is / How It Works

1X Technologies was founded by Bernt Øivind Børnich with a distinct design philosophy: a soft-bodied robot with compliant, fabric-covered limbs designed for safety around humans in home environments. The company partnered with NVIDIA and uses the GR00T N1 foundation model as a base for task policies.

**NEO design philosophy:** Unlike the metal exoskeleton design of most industrial humanoids, NEO's soft body is deliberately optimized for consumer environments where a robot damaging furniture or injuring a family member is an existential product risk. The soft exterior also has compliance benefits — unplanned contact is less dangerous than with rigid structures. NEO's actuation is built on 1X's patented Tendon Drive system, which the company describes as using some of the highest torque-density motors available to drive cable/tendon transmissions rather than rigid gearboxes — intended to produce compliant, low-energy movement safe around people.

**Hands:** NEO ships with 22-degree-of-freedom five-fingered hands (44 DoF across both hands), among the highest hand-DoF counts publicly disclosed for a shipping (rather than lab-only) humanoid platform as of mid-2026, positioning dexterous manipulation — folding laundry, handling dishes, opening doors — as a core NEO capability rather than a research afterthought.

**Expert Mode (teleoperation service):** NEO ships with a household membership that includes access to remote human operators who take control when NEO encounters tasks it cannot handle autonomously. 1X frames Expert Mode as: (a) a safety net for customers, and (b) a data generation pipeline — every teleoperated session produces labeled training data that improves autonomous policies. This is the most honest public disclosure of the teleoperation-backstop model in the industry. 1X is unique in having made this a public product feature rather than hiding it.

**Implication:** Buyers of NEO at launch are purchasing a service that is partly a remote human labor service. The ~$30–50K price point (estimated; not publicly set) includes ongoing access to Expert Mode operators.

**EVE/Android industrial platform:** 1X separately operates EVE, a wheeled-base humanoid-upper-body robot deployed in commercial security and facility monitoring. EVE generates revenue and real-world operational data while NEO is being deployed to consumers. EVE deployments at US commercial facilities are the company's closest thing to current commercial traction.

**December 2025 announcement:** 1X announced a deal to also send NEO units to factories and warehouses (TechCrunch December 2025) — expanding from consumer-only to dual-market, suggesting the home market timeline may be slipping or the factory market opportunity is more near-term.

## Notable Developments

- **2025-10-30:** Opened consumer pre-orders for NEO — $20,000 Early Access ($200 deposit) or $499/month; first US home deliveries targeted for 2026, other markets from 2027.
- **2025-12:** Announced expansion of NEO deployment to factories and warehouses in addition to the original consumer/home focus.
- **2024-08:** Unveiled NEO Beta and announced the pivot to focus solely on the in-home consumer market.

## Founder Background

**Bernt Øivind Børnich** — Founder & CEO
- Norwegian entrepreneur; based in Moss, Norway
- Background in computer science and engineering
- Founded 1X (originally Halodi Robotics, rebranded 2023) in 2021
- Prior: product and engineering leadership at Norwegian tech companies
- Unusual in the humanoid sector for being the only founder without a US research institution or MIT/CMU/Stanford pedigree
- LinkedIn: [berntboirnich](https://www.linkedin.com/in/berntb%C3%B8irnich/)

**Note on founder background:** Børnich's background is lighter on academic robotics credentials than founders at Agility, Apptronik, or Sanctuary AI. 1X compensates by hiring NVIDIA engineers and using GR00T as the foundation model rather than developing AI from scratch — a systems integration strategy rather than a first-principles research approach.

### People — Last Reviewed: 2026-07-18

## Supply Chain & Dependencies

**Actuators:** Soft-body design uses lower-force actuation than hard industrial humanoids; compliant joints and cable-driven or pneumatic elements. Specific vendors not disclosed.

**Compute:** NVIDIA GR00T N1 foundation model integration implies NVIDIA Jetson Orin or successor for edge inference. NVIDIA is both compute supplier and strategic partner.

**Sensors:** Cameras (visual AI). OpenAI and NVIDIA vision models are the perception backbone.

**Battery:** Consumer home use implies longer runtime target; not publicly specified.

**Manufacturing:** Not disclosed. Norwegian manufacturing for prototypes; production scaling not addressed publicly.

**Teleoperation infrastructure:** Expert Mode requires significant human labor investment and latency-tolerant VR teleoperation infrastructure. This is an ongoing operating cost, not a capital cost — 1X's unit economics depend on reducing Expert Mode dependency (increasing autonomous fraction) to avoid scaling a human workforce proportional to robot fleet size.

## Claim Verification

### Claim: NEO is the "world's first consumer-ready home humanoid robot"

**Status:** Partially verified / Marketing

**Supporting sources:**
- 1X opened consumer pre-orders with confirmed 2026 delivery — no other company had shipped a consumer humanoid to households before this

**Refuting / qualifying sources:**
- "Consumer-ready" overstates autonomy given ~30–40% Expert Mode dependency
- No independent third-party household reviews available — all demonstrations are company-controlled or conference settings
- December 2025 factory announcement suggests consumer market may not be the primary deployment path

**Summary:** Technically first to consumer market by delivery date. "Ready" is misleading given Expert Mode dependency.

### Claim: ~60–70% autonomous task completion at launch

**Status:** Unverified (third-party analyst estimate; not company-published)

**Supporting sources:**
- [Winn Solutions, 2026](https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/) — independent analysis using 60–70% figure

**Refuting / qualifying sources:**
- 1X has not published autonomy benchmarks on a standardized test
- The figure is not a controlled measurement

**Summary:** Reasonable estimate consistent with sector norms; not independently verified.

## Sources

- [1X Technologies official site](https://1x.tech)
- [1X raises $23.5M Series A from OpenAI — TechCrunch, Mar 2023](https://techcrunch.com/2023/03/23/1x-technologies-raises-23-5m-series-a-from-openai/)
- [1X raises $100M Series B — TechCrunch, Jan 2024](https://techcrunch.com/2024/01/08/1x-technologies-series-b/)
- [The Truth About Humanoid Robots in 2026 — Medium](https://medium.com/@mehul.chourasia28/the-truth-about-humanoid-robots-in-2026-3ae82e9061b1)
- [Humanoid Robots 2025–2026: Reality or Hype? — Winn Solutions](https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/)
- [NEO humanoid designed for household use, available for preorder — The Robot Report, Oct 30 2025](https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/)
- [1X NEO Home Robot — Order page](https://www.1x.tech/discover/neo-home-robot)
