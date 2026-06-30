---
title: "Unitree Robotics"
date: 2026-06-19
lastmod: 2026-06-19
draft: false
description: "Hangzhou-based Chinese robotics company; global volume leader in humanoid units shipped; ~700M yuan Series C (June 2025); 12B yuan valuation; Wang Xingxing founder; G1 at $16K and R1 at $5,900 are the most price-competitive humanoids globally; IPO planned."
research_area: "robotics/humanoid"
chinese-owned: true
source_urls:
  - "https://unitree.com"
  - "https://www.eweek.com/news/unitree-20000-humanoid-robots-2026-china/"
  - "https://newsletter.semianalysis.com/p/chinas-unitree-will-dominate-global"
  - "https://www.techtimes.com/articles/318641/20260618/humanoid-robots-china-ships-90-global-units-now-leads-ai-benchmarks.htm"
  - "https://www.reuters.com/technology/unitree-raises-funds-series-c-2025-06/"
last_reviewed: 2026-06-19
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Unitree Robotics 🇨🇳 is the global volume leader in humanoid robot shipments. Headquartered in Hangzhou, China, the company shipped ~5,500 humanoid units in 2025 and is targeting 20,000 in 2026 — orders of magnitude above any US competitor. Its price points ($5,900 for R1, $16,000 for G1) are the lowest in the global market, driven by vertical integration of actuator design and China's manufacturing ecosystem. Unitree reported revenue exceeding 1 billion yuan (~$140M) in 2025 and is pursuing an IPO. It is the closest thing the humanoid sector has to a proven commercial business as of mid-2026 — though Chinese government demand, subsidized domestic sales, and national policy goals make Western comparisons difficult.

## Key Facts

- **Founded:** 2016 (Hangzhou, Zhejiang)
- **HQ:** Hangzhou, Zhejiang, China
- **Type:** Company — Platform OEM; vertically integrated
- **Status:** Active — commercial shipments; IPO preparation announced
- **Ownership:** Private; Chinese domestic
- **Employees:** Not publicly disclosed
- **Total funding:** ~700M yuan (~$96M) in June 2025 Series C; prior rounds undisclosed
- **Valuation:** ~12B yuan (~$1.65B) post Series C
- **Revenue:** >1 billion yuan (~$140M) in 2025
- **Units shipped (humanoid):** ~5,500 in 2025; targeting 20,000 in 2026
- **Key robots:** H1 ($90K industrial), G1 ($16K), R1 ($5,900 entry-level)
- **Value chain position:** Platform OEM; designs own Quasi-Direct Drive (QDD) actuators
- **Chinese-owned:** Yes

## Funding & Investors

| Round | Date | Amount | Lead / Notable Investors |
|-------|------|--------|--------------------------|
| Early rounds | 2019–2022 | Undisclosed | Meituan, Sequoia Capital China (HongShan), Shunwei Capital, Matrix Partners China |
| Pre-Series C | 2023 | Undisclosed | Undisclosed |
| Series C | Jun 2025 | ~700M yuan (~$96M) | China Mobile, Tencent, Jinqiu, Alibaba, Ant Group, Geely Capital |

**Total raised:** ~700M+ yuan declared; likely higher including earlier rounds.

**Investor analysis:**
- **China Mobile:** State-owned telco; interest in robot connectivity and 5G/edge compute market
- **Tencent:** Internet/gaming giant; AI model interest; previous investments in industrial AI
- **Alibaba / Ant Group:** E-commerce logistics automation interest (Alibaba operates major logistics networks)
- **Geely Capital:** Geely is one of China's largest automakers (owns Volvo, Lotus, Zeekr); direct deployment interest
- **Sequoia Capital China (early):** HongShan's early bet was well-timed; Unitree went from unknown to $1.65B valuation

**IPO:** Announced August 2025, targeting Chinese domestic exchange (A-share). Timeline and status as of mid-2026 not confirmed.

## What It Is / How It Works

Unitree's strategy is aggressive cost reduction through vertical integration and manufacturing volume. The company designs and manufactures its own Quasi-Direct Drive (QDD) actuators — the key innovation that enables its price competitiveness.

**QDD actuators ("DJI playbook"):** Unitree's QDD design uses low-ratio gearboxes (~5:1 to ~10:1) with large-diameter back-drivable motors. Compared to high-ratio harmonic drive gearboxes ($2,000–$5,000 each), QDD is cheaper to manufacture, easier to repair, and back-drivable (meaning external forces can move the joint without jamming — a safety feature). Trade-off: less torque multiplication means larger/heavier motors for the same output torque. Wang Xingxing explicitly adopted the "DJI playbook" — DJI dominated drone markets by manufacturing critical components in-house at Chinese volume scale and undercutting Western competitors by 60–80%.

**Robot line:**
- **H1** ($90K): Industrial humanoid; research and deployment-grade; 47 cm/s max speed, 18 kg payload
- **G1** ($16K): Research/commercial humanoid; fastest in Unitree's line; 2.0 m/s walking, 43 DoF; most widely adopted research humanoid globally
- **R1** ($5,900): Entry-level humanoid; limited DoF; targeted at developer and educational markets; sets global price floor

**Autonomy:** Shipped units are used for a mix of teleoperation data collection (by academic and commercial AI teams) and limited autonomous task execution. Unitree does not publish autonomy benchmarks. Factory deployments (predominantly with Chinese automotive OEMs) have not released independent productivity data.

## Founder Background

**Wang Xingxing** — Founder & CEO
- Born in Ningbo, Zhejiang province
- B.S./M.S. in Mechanical Engineering, Shanghai University (2010–2015)
- While a student (2013–2015): built "XDog" — an early quadruped robot in the university workshop; attracted early attention from robotics community
- 2015: Briefly joined DJI (world's largest drone manufacturer, Shenzhen) — exposed to DJI's vertical integration model and cost-competitive manufacturing philosophy
- 2016: Left DJI to found Unitree in Hangzhou (August 2016), at age ~26
- Explicitly applied DJI's model to legged robotics: design actuators in-house, manufacture at volume, price below Western competitors
- Net worth: ~6.7B yuan (~$920M) as of 2025 estimates (based on ~5% equity in 12B yuan company)
- LinkedIn: limited public presence (consistent with Chinese tech founder norms)

**Note:** Wang Xingxing is one of the youngest founders of a billion-dollar robotics company globally. His background is hardware engineering rather than AI research — Unitree's competitiveness is in actuator design and manufacturing, not AI innovation.

### People — Last Reviewed: 2026-06-19

## Supply Chain & Dependencies

**Actuators (40–60% of BoM):** In-house QDD design and manufacturing in Hangzhou. Permanent magnets (NdFeB) from Chinese rare earth supply chain. China controls ~85% of rare earth mining and ~90% of processing globally — domestic supply chain for Unitree's magnets is entirely within China, with no external dependency risk for the company itself. Creates import/export risk for Western customers purchasing Unitree robots.

**Compute:** Not disclosed per unit. Likely Qualcomm-class SoC or domestic Chinese AI chips (Cambricon, Biren) for edge inference, given US chip export restrictions. NVIDIA Jetson Orin is subject to export controls; Unitree cannot easily use NVIDIA edge chips.

**Sensors:** Cameras and IMU. Depth sensors likely from Chinese domestic suppliers (Orbbec, Mech-Mind). LiDAR if included would be Hesai or Robosense (see Sensors section).

**Battery:** Domestic Chinese LiPo/LFP cells from CATL, Lishen, or equivalent. China dominates battery supply chain — no supply risk.

**Manufacturing:** All Hangzhou-based. China's manufacturing cost advantage (labor, tooling, supply chain proximity) allows costs ~1/3 of equivalent Western production at matched volume.

**US/EU customer risk:** Purchasing Unitree robots creates:
1. Geopolitical risk: Chinese hardware with cellular/WiFi connectivity may face procurement restrictions
2. Data risk: Robot telemetry, map data, and operational patterns routed through Chinese-controlled hardware
3. Supply continuity risk: Tariff escalation or export restrictions could interrupt supply

## Claim Verification

### Claim: Targeting 20,000 humanoid units in 2026

**Status:** Unverified (forward-looking)

**Supporting sources:**
- [eWeek, 2026](https://www.eweek.com/news/unitree-20000-humanoid-robots-2026-china/) — reports Unitree's stated target and fourfold capacity increase
- Chinese domestic automotive demand (BYD, Geely, SAIC) provides plausible pull demand

**Refuting / qualifying sources:**
- 5,500 to 20,000 requires 3.6× growth in one year; achievable but not guaranteed
- Chinese humanoid "deployment" numbers may include partially assembled units, R&D units, and government-subsidized institutional purchases

**Summary:** Ambitious but plausible given manufacturing capacity and domestic demand. Verify against actual shipping data.

### Claim: Revenue >1B yuan (~$140M) in 2025

**Status:** Company-reported; unaudited

**Supporting sources:**
- [Reuters, 2025](https://www.reuters.com/technology/unitree-raises-funds-series-c-2025-06/) — reports revenue figure in context of Series C

**Refuting / qualifying sources:**
- No independent audit; Chinese private company reporting not required to meet Western accounting standards
- Revenue includes quadruped (Go series) and component sales alongside humanoids

**Summary:** Directionally credible given unit volume; breakdown between humanoid and quadruped revenue unknown.

## Sources

- [Unitree official site](https://unitree.com)
- [Unitree targets 20,000 humanoid robots — eWeek 2026](https://www.eweek.com/news/unitree-20000-humanoid-robots-2026-china/)
- [China's Unitree will dominate global robotics — SemiAnalysis](https://newsletter.semianalysis.com/p/chinas-unitree-will-dominate-global)
- [China ships 90% of global humanoid units — TechTimes, June 2026](https://www.techtimes.com/articles/318641/20260618/humanoid-robots-china-ships-90-global-units-now-leads-ai-benchmarks.htm)
- [Unitree Series C — Reuters](https://www.reuters.com/technology/unitree-raises-funds-series-c-2025-06/)
