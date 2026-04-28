---
title: "SES AI Corporation"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "Boston-based lithium-metal hybrid battery company; AI-based cell management for dendrite detection; OEM partnerships with GM, Hyundai, Honda; Apollo cell (417 Wh/kg, 107 Ah); A-sample and B-sample JDAs ongoing; Ui-Wang, South Korea B-sample facility announced; SPAC IPO 2022; ~$390M liquidity end-2022."
tags: ["batteries", "lithium-metal", "hybrid", "ai", "us", "public", "ev"]
categories: ["company"]
research_area: "energy/batteries"
source_urls:
  - "https://www.ses.ai"
  - "https://ses.ai/dr-qichao-hu/"
  - "https://electrek.co/2026/03/25/battery-company-ai-pivot-ses/"
  - "https://news.metal.com/newscontent/101730957/After-General-Motors-and-Hyundai-Honda-announced-the-joint-development-of-lithium-metal-battery-with-SES/"
  - "https://www.businesswire.com/news/home/20211103005931/en/SES-Unveils-Worlds-First-100-Plus-Ah-Li-Metal-Battery-Announces-New-Gigafactory-at-First-SES-Battery-World"
  - "https://www.businesswire.com/news/home/20230301006034/en/SES-Provides-an-Update-on-Cash-Position-as-of-End-of-2022-and-Status-of-Annual-Report-on-Form-10-K"
last_reviewed: 2026-04-24
stale_after_days: 90
related:
  - "energy/batteries/lithium-metal.md"
  - "energy/batteries/solid-state-batteries.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

SES AI Corporation (NYSE: SES) is a Boston-based lithium-metal battery company founded in 2012 by MIT researchers. The company has taken a distinctive approach to the dendrite problem by combining a lithium-metal hybrid cell architecture (liquid electrolyte with engineered protective layers) with AI-powered battery management software that detects and responds to dendrite formation in real time. SES has secured strategic investment and partnerships from General Motors, Hyundai Motor Company, and Honda, and is the only lithium-metal company with three major OEM joint development agreements (A-sample, B-sample) signed simultaneously. The Apollo cell (417 Wh/kg, 107 Ah) was demonstrated in 2021 as the world's first 100+ Ah lithium-metal cell. As of end-2022, the company held ~$390M in liquidity. B-sample development facility in Ui-Wang, South Korea announced (2025); mass production targeted early 2030s.

## Key Facts

- **Founded:** 2012 (in basement of MIT)
- **HQ:** Boston, MA, USA
- **Type:** Public (NYSE: SES; SPAC merger Dec 2022 with Ivanhoe Capital Acquisition Corp.)
- **Founder & CEO:** Dr. Qichao Hu (MIT BS Physics, Harvard PhD Applied Physics, MIT postdoc 2009–2013)
- **Key investors:** General Motors (strategic investor + PIPE participant), Hyundai Motor Company, Honda, A123 Systems (initial institutional investor)
- **Technology:** Lithium-metal hybrid cell with liquid electrolyte + engineered protective layers + AI-based electrochemical monitoring and management system
- **Apollo cell specs (demonstrated 2021):** 107 Ah capacity; 417 Wh/kg energy density; 935 Wh/L volumetric; tested at C/10, C/3, and 1C discharge rates; ~60% higher energy density than best conventional Li-ion cells (260 Wh/kg)
- **OEM partnerships:** General Motors (A-sample JDA; B-sample in progress), Hyundai Motor Company and Kia (A-sample and B-sample JDAs; dedicated facility Ui-Wang, South Korea), Honda (A-sample JDA announced 2026)
- **B-sample facility:** Ui-Wang, South Korea; SES AI building and operating one of the largest capacity lithium-metal lines in the world (announced 2025)
- **Mass production timeline:** Targeting early-to-mid 2030s (dependent on OEM qualification and facility scaling)
- **Financial position (end-2022):** ~$390M liquidity; $61M annual cash burn (2022, below $75–85M guidance); $51M net loss (2022); $145.3M accumulated deficit
- **Differentiation:** AI-based real-time electrochemical monitoring; claims to detect and suppress dendrite formation before it causes shorts

## Technology Overview

### The Hybrid Approach

SES AI does not pursue a fully solid-state architecture. Instead, the company uses a **lithium-metal hybrid** design: a liquid electrolyte (which is easier to manufacture and more processable than solid electrolytes) combined with an engineered protective layer and separator system designed to suppress dendrite formation, plus an AI-based battery management system.

**Why hybrid instead of solid-state?**

1. **Manufacturing simplicity:** Liquid electrolytes are compatible with existing lithium-ion manufacturing equipment (estimated 70–80% compatibility); solid ceramics require new equipment and processes.
2. **Faster time-to-market:** Proven manufacturing pathway reduces learning curve for OEMs.
3. **Energy density above solid-state, below full optimization:** The hybrid design delivers 417 Wh/kg (Apollo), roughly 60% higher than conventional NMC (260 Wh/kg), but potentially 15–25% lower than a fully optimized all-solid-state cell.
4. **Lower first-pass manufacturing risk:** OEMs can integrate hybrid cells with known processes; solid-state requires new assembly methods, thermal management, BMS software.

### AI Differentiation: Electrochemical Monitoring

SES's distinctive competitive claim is its AI-based electrochemical monitoring system. Rather than trying to engineer away dendrites entirely, SES uses machine learning to:

1. **Monitor electrochemical signatures in real-time** during charge/discharge — monitoring cell impedance, voltage curves, current distribution, and other electrochemical parameters
2. **Detect early signs of dendrite formation** — dendrites have characteristic electrochemical signatures that appear before they cause short circuits
3. **Respond dynamically** — adjust charging profile, current limits, or cell management in real-time to suppress or slow dendrite growth

This is a fundamentally different approach: rather than relying purely on material science to prevent dendrites, SES uses **algorithmic control** to detect and suppress them.

**Advantages:**
- Adds a software-based layer of safety that works across a range of operating conditions
- Can be updated and improved through software; doesn't require new cell manufacturing
- Complements any electrolyte or separator chemistry

**Challenges:**
- Requires integration with vehicle BMS (battery management system) and onboard computing
- Effectiveness depends on the quality of the AI models and training data
- Independent validation of AI performance in real vehicles is limited as of Q2 2026

### Apollo Cell Specifications

| Specification | Value | Context |
|---------------|-------|---------|
| **Capacity** | 107 Ah | Large-format automotive cell |
| **Gravimetric energy density** | 417 Wh/kg | Tested at multiple discharge rates (C/10, C/3, 1C) |
| **Volumetric energy density** | 935 Wh/L | Volume-normalized energy |
| **Relative to conventional Li-ion** | ~60% higher | vs. 260 Wh/kg NMC baseline |
| **Discharge rate testing** | C/10, C/3, 1C | Consistently high across three test rates |
| **Status (as of 2026)** | Demonstrated; in OEM testing phase | Not yet in production |

**Note:** Apollo was demonstrated in 2021; subsequent cell development and OEM-specific variants may differ. Current status of Apollo vs. next-generation designs (as of Q2 2026) not publicly detailed.

## Business Model

SES has three simultaneous OEM pathways, each at different development stages:

### General Motors (Primary Partnership)

- **Status:** A-sample JDA (active); B-sample JDA in progress
- **Timeline:** B-sample development leading to prototype vehicle integration by 2027–2028
- **Scale:** GM investment and PIPE participation signals high confidence

### Hyundai Motor Company and Kia

- **Status:** A-sample and B-sample JDAs signed; dedicated B-sample facility Ui-Wang, South Korea announced (2025)
- **Scale:** SES AI "building and operating one of the largest capacity Li-Metal lines in the world" (company language suggests GWh-scale ambition by 2027–2028)
- **Timeline:** B-sample development in South Korea facility; prototype vehicle integration planned for late 2020s

### Honda

- **Status:** A-sample JDA announced (2026)
- **Timeline:** Early-stage compared to GM and Hyundai-Kia
- **Significance:** Marks Honda's formal commitment to lithium-metal battery development alongside its traditional nickel-metal-hydride and early solid-state research

**Unique position:** SES is the only lithium-metal company with three major OEM partnerships all active simultaneously (as of April 2026).

## Notable Developments

- **2026:** Honda announces A-sample JDA with SES AI for joint development of lithium-metal batteries.
- **2026 (Q1):** MIT Technology Review publishes feature on SES's AI pivot; CEO Hu discusses electrochemical diagnostics strategy.
- **2025:** Hyundai and Kia advance to B-sample phase; Ui-Wang, South Korea facility announced for largest capacity lithium-metal production line (SES language).
- **2025 (Jan):** SES AI wins two new OEM partners as Hyundai and Kia enter B-sample joint development contracts. Hyundai-Kia facility planned in South Korea.
- **2022 (Dec):** SPAC merger closes; SES AI lists on NYSE (SES). Raises $275M PIPE from GM, Hyundai, Honda, and others.
- **2022 (year-end):** Cash position $390M; annual cash burn $61M; no revenue yet from battery sales (pre-commercial).
- **2021 (Nov):** Apollo cell unveiled (107 Ah, 417 Wh/kg); first 100+ Ah lithium-metal cell demonstrated. Gigafactory plans announced.
- **2012:** Founded by Qichao Hu in MIT basement.

## Key People

### Dr. Qichao Hu — Founder, Chairman, and CEO
- **LinkedIn:** Profile not separately listed; company leadership page: [ses.ai/dr-qichao-hu](https://ses.ai/dr-qichao-hu/)
- **Role:** Founder (2012); CEO throughout; oversees technology development, OEM relationships, and fundraising
- **Education:** Massachusetts Institute of Technology (BS Physics) → Harvard University (PhD Applied Physics)
- **Career (reverse-chronological):**
  - SES AI (2012–present): Founder, CEO, and Chairman; founded in MIT basement with goal of commercializing lithium-metal batteries
  - MIT Energy Postdoctoral Fellow (2009–2013): Conducted research on electrochemistry and battery materials
  - **Recognition:** Forbes 30 Under 30; MIT Technology Review Innovators Under 35; board member MIT Enterprise Forum Cambridge
- **Notes:** Hu's entire career has been in battery science and commercialization; he is both the technical founder (electrochemistry expertise) and CEO. This differs from QuantumScape (tech founder → manufacturing specialist CEO transition) — at SES, the original technologist remains in charge, suggesting a technology-first strategy.

### Other Leadership
- Company leadership page identifies executive team; additional details not extensively published as of Q2 2026.

## Supply Chain Position

SES operates primarily at the **Cell Manufacturing** layer, producing hybrid lithium-metal cells for automotive testing and eventual OEM supply. The company has no disclosed upstream partnership for electrolyte or separator materials (unlike QuantumScape's Murata partnership), suggesting in-house synthesis.

**Upstream dependencies:**
- **Lithium metal anode:** Sourced from specialized suppliers; not disclosed
- **Electrolyte and separator materials:** Proprietary, synthesized in-house or via undisclosed partners
- **Cathode materials:** Standard NMC or proprietary variants; not detailed publicly

**Downstream:**
- **OEM customers:** GM, Hyundai-Kia, Honda (JDAs; no commercial supply yet)
- **No disclosed secondary markets** (unlike QuantumScape's defense/drone expansion)

**⚑ No disclosed supply chain partners at scale,** suggesting SES is attempting a more vertically integrated approach than QuantumScape, or is relying on confidential supplier relationships.

## Competitive Position

SES's hybrid lithium-metal approach with AI management occupies a middle ground in the competitive landscape:

| Aspect | SES AI | QuantumScape | Factorial | Solid Power |
|--------|--------|--------------|-----------|------------|
| **Electrolyte** | Liquid (hybrid) | Solid sulfide | Quasi-solid gel | Solid sulfide |
| **Manufacturing** | ~70–80% Li-ion compatible | Bespoke Cobra process | ~80% Li-ion compatible | Supplied by partners (Samsung SDI) |
| **Differentiation** | AI monitoring | Anode-free + ceramic | Semi-solid simplicity | Electrolyte IP licensing |
| **Energy density** | 417 Wh/kg (Apollo) | 301 Wh/kg (QSE-5) | 375–450 Wh/kg (FEST® / Solstice) | ~300–350 Wh/kg (target) |
| **Safety** | Liquid (fire risk mitigated by AI control) | Solid (inherent safety) | Semi-solid (reduced fire risk) | Solid (inherent safety) |
| **Time to OEM validation** | 2027–2028 (GM, Hyundai) | 2027–2028 (PowerCo, others) | 2026–2027 (Stellantis, Mercedes) | 2027–2028 (BMW i7) |

**SES's strategic positioning:** The hybrid + AI approach trades off the safety margin of fully solid-state designs for faster manufacturing integration and a second layer of algorithmic control. If the AI system works reliably across real-world conditions, SES could reach commercialization faster than fully solid-state competitors. If the AI fails or proves insufficient in cold climates or extreme charge rates, the inherent fire risk of liquid electrolyte becomes the liability.

## Claim Verification

### Claim: Apollo Cell — 417 Wh/kg, 107 Ah
**Status:** Demonstrated (2021); verified by company disclosure

**Supporting sources:**
- [SES Unveils World's First 100 Plus Ah Li-Metal Battery — Business Wire (Nov 2021)](https://www.businesswire.com/news/home/20211103005931/en/SES-Unveils-Worlds-First-100-Plus-Ah-Li-Metal-Battery-Announces-New-Gigafactory-at-First-SES-Battery-World)
- [SES Launches 107Ah Lithium-Metal Battery — Electrek (Nov 2021)](https://electrek.co/2021/11/03/ses-shares-plans-for-worlds-largest-lithium-metal-facility-to-build-107-amp-hour-ev-batteries/)

**Status:**
- Disclosed in 2021; no refutation identified
- Tested at multiple discharge rates (C/10, C/3, 1C) with consistent performance
- ~60% higher than conventional NMC (260 Wh/kg baseline)

**Summary:** Energy density claim is verified at disclosed test conditions. Real-world automotive validation (via GM, Hyundai, Honda JDAs) ongoing as of Q2 2026; independent OEM test results not yet published.

---

### Claim: AI Detects and Suppresses Dendrites in Real-Time
**Status:** Claimed; independent validation pending

**Supporting sources:**
- [MIT Technology Review — "Why this battery company is pivoting to AI" (Mar 2026)](https://www.technologyreview.com/2026/03/25/1134657/battery-company-ai-pivot-ses/)
- SES corporate communications and investor materials

**Questions:**
- The specific electrochemical signatures being monitored are not disclosed
- No published peer-reviewed validation of the AI algorithm's effectiveness
- Real-world effectiveness depends on integration with OEM BMS, which is still in development (2025–2026)

**Summary:** AI-based monitoring is a credible and novel approach, but effectiveness claims remain unverified independently. OEM validation via GM, Hyundai, Honda will be the decisive test in 2027–2028.

---

### Claim: "Only Li-Metal Company With Three Major OEM Partnerships"
**Status:** Verified (as of April 2026)

**Supporting sources:**
- Multiple press releases confirming GM, Hyundai-Kia, and Honda JDAs

**Context:** This is a genuine competitive differentiator; no other lithium-metal company (QuantumScape, Solid Power, Factorial) has secured simultaneous A-sample and B-sample JDAs with three Tier-1 OEMs.

**Summary:** Verified and strategically significant. Reflects broad automotive industry confidence in lithium-metal batteries despite remaining commercialization challenges.

## Sources

**Company & Technology:**
- [SES AI — Corporate Website](https://www.ses.ai)
- [Dr. Qichao Hu — SES AI Founder/CEO Profile](https://ses.ai/dr-qichao-hu/)
- [SES AI Unveils World's First 100+ Ah Li-Metal Battery — Business Wire (Nov 2021)](https://www.businesswire.com/news/home/20211103005931/en/SES-Unveils-Worlds-First-100-Plus-Ah-Li-Metal-Battery-Announces-New-Gigafactory-at-First-SES-Battery-World)

**OEM Partnerships & News:**
- [Honda Joins GM and Hyundai with A-Sample JDA — SMM (2026)](https://news.metal.com/newscontent/101730957/After-General-Motors-and-Hyundai-Honda-announced-the-joint-development-of-lithium-metal-battery-with-SES/)
- [Hyundai-Kia B-Sample Development Agreement — SES AI (Jan 2025)](https://www.electrive.com/2025/01/27/ses-ai-wins-two-car-manufacturers-as-partners/)
- [SES AI and Hyundai Advance Li-Metal Battery Tech — Investing.com](https://www.investing.com/news/company-news/ses-ai-and-hyundai-motor-advance-li-metal-battery-tech-93CH-3401194)

**AI & Strategy:**
- [Why This Battery Company is Pivoting to AI — MIT Technology Review (Mar 2026)](https://www.technologyreview.com/2026/03/25/1134657/battery-company-ai-pivot-ses/)

**Financial:**
- [SES AI Cash Position Update — Business Wire (Mar 2023)](https://www.businesswire.com/news/home/20230301006034/en/SES-Provides-an-Update-on-Cash-Position-as-of-End-of-2022-and-Status-of-Annual-Report-on-Form-10-K)
- [SES AI Investor Relations — Annual Reports & SEC Filings](https://investors.ses.ai/overview/default.aspx)
