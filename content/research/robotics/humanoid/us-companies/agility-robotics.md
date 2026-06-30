---
title: "Agility Robotics"
date: 2026-06-19
lastmod: 2026-06-19
draft: false
description: "Albany, OR humanoid robotics company; Digit bipedal robot; commercial deployment leader among US humanoids; ~$180M raised; DCVC/Playground/Amazon investors; customers include Amazon, GXO, Toyota."
research_area: "robotics/humanoid"
source_urls:
  - "https://agilityrobotics.com"
  - "https://www.agilityrobotics.com/content/agility-robotics-announces-commercial-agreement-with-toyota-motor-manufacturing-canada"
  - "https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics"
  - "https://www.agilityrobotics.com/content/mercado-libre-and-agility-robotics-announce-commercial-agreement"
  - "https://www.agilityrobotics.com/content/agility-robotics-announces-strategic-investment-and-agreement-with-motion-technology-company-schaeffler-group"
  - "https://newmarketpitch.com/blogs/news/humanoid-robotics-optimus-deployment-tracker"
last_reviewed: 2026-06-19
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Agility Robotics is the commercial deployment leader among US humanoid robot companies — Digit is operating in real warehouses at Amazon, GXO, and Toyota facilities, making Agility the only US humanoid company with verifiable multi-customer production deployments as of mid-2026. The company originated as a Carnegie Mellon/Oregon State robotics lab spinout; Digit evolved from the ATRIAS and Cassie research platforms developed over 15+ years of bipedal locomotion research. With ~$180M raised across six rounds and investors including Amazon's Industrial Innovation Fund and Schaeffler, Agility has real strategic backing — but a fraction of Figure AI's valuation, consistent with the market rewarding potential over current revenue.

## Key Facts

- **Founded:** 2015 (OSU spinout of DARPA-funded bipedal research)
- **HQ:** Albany, OR (manufacturing/production); Corvallis, OR (R&D)
- **Type:** Company — Platform OEM
- **Status:** Commercial; multi-customer deployments
- **Employees:** ~85 (2023); doubling plan underway
- **Total funding:** ~$180M across 6 rounds, 18+ investors
- **Robot:** Digit — bipedal humanoid; ~5'9", ~140 lbs; 90-minute battery runtime
- **Value chain position:** Platform OEM; Series Elastic Actuator (SEA) design
- **Customers:** Amazon (AMZN), GXO Logistics (GXO), Toyota Motor Manufacturing Canada (Feb 2026 commercial agreement), Schaeffler (SDVXF), Mercado Libre (Dec 2025 commercial agreement)
- **Commercial model:** Robotics-as-a-Service (RaaS) — per-hour/shift pricing, not capital sales

## Funding & Investors

| Round | Date | Amount | Lead / Notable Investors |
|-------|------|--------|--------------------------|
| Pre-seed | 2015–2019 | Undisclosed | DCVC, Playground Global (early) |
| Series A | 2021 | ~$20M | DCVC (lead), Playground Global |
| Series B | 2022 | $150M | DCVC (lead), Playground Global, Amazon Industrial Innovation Fund, Sony, TDK Ventures, Schaeffler |
| Additional | 2023–2024 | ~$10M+ | ABICO Holdings, SoftBank Group (additional participation noted) |

**Total raised:** ~$180M. 18+ investors across 6 rounds.

**Amazon AIIF note:** Amazon's Industrial Innovation Fund investment in the Series B (2022) came alongside the announcement of Digit pilots at Amazon fulfillment centers. Amazon is simultaneously an investor and a paying customer — a structure that aligns incentives but also raises questions about whether commercial pricing reflects market rates. Amazon separately acquired Kiva (AMR) and iRobot (home), suggesting a serial strategy of investing then acquiring; Agility could follow this path.

**Schaeffler investment:** Schaeffler is a German precision bearing and motion technology manufacturer (harmonic drives, bearings, gearboxes). Their Series B participation is a strategic bet on becoming a component supplier as Digit scales — not a purely financial investment.

**Playground Global:** Peter Barrett's deep-tech VC has been involved since earliest rounds; one of the few VCs with robotics manufacturing expertise on staff.

## What It Is / How It Works

Digit is a bipedal humanoid robot designed for logistics environments — specifically "the last foot" problem: moving totes between conveyors, shelves, and pick stations. Agility deliberately limits Digit's task scope rather than claiming general-purpose capability. This tradeoff (narrow task, high reliability) is validated by its status as the only US humanoid with real multi-customer commercial deployment.

**Actuator technology — Series Elastic Actuators (SEA):** Digit uses Series Elastic Actuators throughout. SEAs insert a compliant spring element between the motor gearbox and the output joint. The spring absorbs shock loads (protecting motors and gearboxes), enables torque sensing from spring deflection without dedicated torque sensors at every joint, and makes contact with the environment inherently gentle. SEA-based robots handle physical interaction with humans and unplanned contact more safely than stiff direct-drive or harmonic-drive systems — a meaningful advantage in co-working warehouse environments.

Trade-off: SEAs sacrifice some speed and peak stiffness compared to Quasi-Direct Drive (QDD) systems like Unitree's. Digit walks at ~1.5 m/s and manipulates at moderate speed — optimized for safe co-working over agility. At ~300 boxes/hour in Amazon testing, Digit reaches ~70% of a human picker's rate — but can operate 24/7 across shifts, theoretically outperforming human throughput over an 8-hour cycle.

**Battery constraint:** 90-minute runtime per charge is the deployment's dominant limitation. In Amazon facilities, Digit operates in ~30-minute windows with swap or charge cycles. Until fast-swap battery or inductive charging is deployed, 24/7 operation requires 3+ Digit units per operational "slot" to cover charging downtime.

**Training pipeline:** Teleoperation data collection feeds imitation learning. Digit's arms are teleoperated by human operators to demonstrate manipulation tasks; those demonstrations train motion policies. Claimed independence level in Amazon tote operations is "minimal supervision" as of Q2 2026 — not independently verified.

## Founder Backgrounds

**Jonathan Hurst** — Co-founder & Chief Robot Officer
- Ph.D., Carnegie Mellon University, Robotics Institute; dissertation on energy-efficient bipedal locomotion
- Professor, Oregon State University, Mechanical Engineering (joint appointment in Computer Science)
- Developed ATRIAS biped at OSU — first robot to demonstrate human-comparable walking energy efficiency
- DARPA funding: led the $1M grant that produced Cassie in 16 months (2016–2017) — a product-speed execution from an academic lab, signaling commercial orientation
- Research focus: passive dynamic walking, spring-mass biomechanics, applying animal locomotion principles to robot design
- LinkedIn: [jonathan-hurst](https://www.linkedin.com/in/jonathan-hurst-b1b3604/)

**Damion Shelton** — Co-founder & CEO
- Ph.D., Carnegie Mellon University, Robotics Institute (met Hurst as PhD classmate at CMU)
- Background: robotics perception, systems integration, commercial translation of research
- Prior: Caterpillar Technology & Solutions; robotics consulting before OSU spinout
- LinkedIn: [damionshelton](https://www.linkedin.com/in/damionshelton/)

**Mikhail Jones** — Co-founder
- M.S., Oregon State University (worked in Hurst's Dynamic Robotics Lab)
- Contributed to early Cassie and Digit development

**Pattern:** Classic academic spinout with unusual commercial discipline. Hurst invested 15+ years in fundamental bipedal locomotion research before commercializing. The Cassie DARPA execution (16 months from grant to hardware) demonstrated the team can move fast. Agility's current commercial lead over better-funded competitors suggests that depth of foundational research translates to deployable products better than speed-to-prototype.

### People — Last Reviewed: 2026-06-19

## Robot Development History

| Platform | Year | Significance |
|----------|------|--------------|
| ATRIAS | 2012 | OSU biped; first to demonstrate human-comparable walking energy efficiency |
| Cassie | 2017 | Spring-mass bipedal legs; DARPA-funded; 16-month development; commercially licensed to 23+ universities |
| Digit v1 | 2019 | Added torso + arms to Cassie legs; first humanoid configuration |
| Digit v2–v3 | 2021–2023 | Improved arm payload, perception, battery runtime |
| Digit (current) | 2024+ | Production version; RaaS deployments at Amazon, GXO, Toyota |

Cassie (legs only) was separately licensed to 23+ universities as a research platform. This academic distribution is an unusual asset — Agility has more third-party researchers working on their locomotion platform than any other humanoid company, generating a pipeline of talent familiar with the hardware.

## Supply Chain & Dependencies

**Actuators:** SEA design is Agility's proprietary IP, but components (electric motors, springs, bearings, gearboxes) are sourced. Unlike Figure AI, Agility does not claim full vertical integration. Schaeffler's investment is likely tied to potential bearing and precision drive supply. Specific motor vendors not publicly disclosed.

**Sensors:** Custom head unit with cameras and depth sensors. Suppliers not disclosed. Likely Luxonis/Orbbec class RGB-D sensors given Intel RealSense discontinuation.

**Compute:** Not publicly disclosed per joint. Likely NVIDIA Jetson Orin for perception stack; embedded microcontrollers for actuator control loops.

**Battery:** 90-minute LiPo/NMC pack. Fast-swap battery development underway for shift-continuous operation. Cell sourcing not disclosed — likely Asian supply chain (Samsung SDI, LG Energy, or CATL).

**Manufacturing scale constraint:** No equivalent of Figure's BotQ. Production volume for Digit is small (dozens to low hundreds of units). Manufacturing capacity is the binding constraint on commercial scaling — a problem that Amazon's investment presumably helps address if they choose to scale.

## Claim Verification

### Claim: Digit operational in customer warehouses doing real productive work

**Status:** Verified (more than any other US humanoid company)

**Supporting sources:**
- Amazon, GXO, Toyota, and Schaeffler are all named customers with announced deployments
- Agility CEO stated "hundreds of thousands of tote operations" completed at Amazon facilities
- [Automate.org](https://www.automate.org/industry-insights/humanoid-robots-are-evolving) acknowledges Agility's deployment lead

**Qualifying sources:**
- Autonomy level during tote operations (supervised vs. autonomous) not independently confirmed
- Amazon described the deployment as a "pilot" — scale unknown
- No independent third-party throughput audit

**Summary:** The most substantiated deployment claim in US humanoid robotics. Real customers, real hardware, real task completion — at limited scale and unverified autonomy level.

## Sources

- [Agility Robotics official site](https://agilityrobotics.com)
- [Toyota commercial agreement — Agility Robotics press release, Feb 2026](https://www.agilityrobotics.com/content/agility-robotics-announces-commercial-agreement-with-toyota-motor-manufacturing-canada)
- [GXO multi-year agreement — Agility Robotics press release, Jun 2024](https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics)
- [Mercado Libre commercial agreement — Agility Robotics press release, Dec 2025](https://www.agilityrobotics.com/content/mercado-libre-and-agility-robotics-announce-commercial-agreement)
- [Schaeffler investment — Agility Robotics press release, Nov 2024](https://www.agilityrobotics.com/content/agility-robotics-announces-strategic-investment-and-agreement-with-motion-technology-company-schaeffler-group)
- [Agility vs. Tesla Optimus deployment comparison — New Market Pitch, Apr 2026](https://newmarketpitch.com/blogs/news/humanoid-robotics-optimus-deployment-tracker)
