---
title: "Sanctuary AI"
date: 2026-06-19
lastmod: 2026-06-19
draft: false
description: "Vancouver-based Physical AI company; pivot to hardware-agnostic AI on existing industrial robots (June 2026); $140M+ raised; Magna International investor; 99.5%+ task success rate at Tier 1 automotive supplier; Geordie Rose and Suzanne Gildert departed Nov 2024; James Wells CEO, Olivia Norton CTO."
tags: ["humanoid", "robotics", "canada", "commercial", "manipulation"]
categories: ["company"]
research_area: "robotics/humanoid"
source_urls:
  - "https://sanctuary.ai"
  - "https://sanctuary.ai/news/sanctuary-ai-expands-physical-ai-strategy-to-industrial-robotics-demonstrating-production-ready-ai-performance/"
  - "https://sanctuary.ai/news/sanctuary-ai-announces-microsoft-collaboration-to-accelerate-ai-development-for-general-purpose-robots/"
  - "https://globalrecognitionawards.org/innovative-companies/sanctuary-ai-phoenix/"
  - "https://techcrunch.com/2023/10/18/sanctuary-ai-series-b/"
last_reviewed: 2026-06-19
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Sanctuary AI is a Vancouver, British Columbia company that pivoted in June 2026 from humanoid-hardware-first to a hardware-agnostic Physical AI strategy — deploying its Carbon AI on existing commercial robotic platforms rather than waiting for humanoid hardware to reach mass production. As of June 2026 the company demonstrated 99.5%+ task success at 2.54-second cycle time on a wire-plugging task at a global Tier 1 automotive supplier. The company raised $140M+ with a distinctive investor mix: Magna International (automotive supplier) is both an investor and a manufacturing partner, and Microsoft provides Azure AI compute for model training. Both original co-founders — Geordie Rose (CEO) and Suzanne Gildert (CTO) — departed in November 2024. James Wells (former Chief Commercial Officer) is now CEO; Olivia Norton (co-founder) is CTO.

## Key Facts

- **Founded:** 2018
- **HQ:** Vancouver, BC, Canada
- **Type:** Company — Platform OEM + AI control system developer
- **Status:** Active; commercial pilots; no disclosed large-scale deployment
- **Employees:** Not publicly disclosed
- **Total funding:** $140M+
- **Valuation:** Not publicly disclosed
- **Robot:** Phoenix (gen-8); ~5'7", ~70 lbs; Carbon AI control system
- **Key feature:** Gen-8 tactile sensors enabling in-hand manipulation and 12-sided dice manipulation
- **Value chain position:** Platform OEM + Carbon AI developer
- **Manufacturing partner:** Magna International

## Funding & Investors

| Round | Date | Amount | Lead / Notable Investors |
|-------|------|--------|--------------------------|
| Series A | 2022 | Undisclosed | Accenture, Bell Canada Enterprises, Evok Innovations, SE Health |
| Series B (initial) | Oct 2022 | ~$58M CAD | Export Development Canada, Verizon Ventures, Workday Ventures |
| Canadian gov. grant | Nov 2022 | $30M CAD | Canadian Strategic Innovation Fund |
| Series B extension | Late 2023 | Undisclosed | Magna International (+ manufacturing agreement), additional investors |
| Microsoft partnership | May 2024 | Undisclosed | Microsoft (investment + Azure AI partnership) |

**Total raised:** $140M+ CAD equivalent across all rounds.

**Magna International:** Magna is the world's third-largest automotive supplier by revenue — stamping, seating, powertrain, mirrors, electronics. Their Sanctuary investment is both financial and strategic: Magna is piloting Phoenix for automotive assembly tasks and serves as a manufacturing scale partner. This is the most concrete supply chain relationship in the humanoid sector — a tier-1 automotive supplier taking a direct role in both capital and manufacturing. Magna's automotive manufacturing expertise (high-reliability, high-volume production to strict tolerance) is exactly the expertise Sanctuary needs to scale beyond pilot quantities.

**Microsoft partnership (May 2024):** Azure AI is training Sanctuary's Carbon AI models. Microsoft's $100M+ investment in OpenAI and participation in Apptronik's round suggests a broader "physical AI" strategy — investing in multiple humanoid companies while providing the AI compute infrastructure all of them need.

**Canadian government support:** $30M from the Canadian Strategic Innovation Fund (November 2022) signals Canadian government interest in anchoring a humanoid company domestically. Export Development Canada participation reflects the same motivation.

**Accenture:** Presence of a professional services firm as an early investor is unusual — Accenture's interest is likely in becoming an integration services provider for enterprise Phoenix deployments, not in the hardware business directly.

## What It Is / How It Works

Sanctuary AI's distinctive architecture is the Carbon AI system — positioned as a general-purpose AI designed to give Phoenix "human-like intelligence" for task planning and execution. Unlike competitors that train task-specific policies via imitation learning from teleoperation data, Carbon is intended as a more generalizable reasoning and planning layer.

**Carbon AI architecture:** Carbon reportedly uses a combination of large language model reasoning (for task planning) and low-level motion policies (for execution). The LLM layer reasons about what to do; the motion policy layer handles how to do it physically. This architecture is theoretically more generalizable than pure imitation learning — a new task can potentially be described in language and executed without retraining. Whether this advantage materializes in practice at commercial scale is not verified.

**Tactile sensing (Phoenix gen-8):** Fingertip sensors provide force and texture feedback. This addresses a fundamental critique of humanoid manipulation — training on visual data misses the proprioceptive and tactile modalities that human dexterity actually relies on. The demonstration of 12-sided dice manipulation (requiring precise tactile control to avoid dropping) is the most technically impressive fine manipulation demo in the sector as of 2025. Commercial relevance of dice manipulation is minimal; it is a proxy for the tactile control precision needed for small parts assembly and electronics work.

**Teleoperation pipeline:** Like other companies, Sanctuary uses teleoperation to generate training data for Carbon. Gen 8 was specifically redesigned (January 2025) to optimize data capture — faster and easier teleoperation sessions that generate higher-quality training data.

**Commercial task breadth:** The 110+ task retail pilot at Mark's (Canadian Tire subsidiary) demonstrates task diversity: folding garments, hanging items, operating store fixtures, moving inventory. This is a deliberately broad scope pilot — testing task generalization rather than performance depth on one task. Autonomy ratio per task is not disclosed.

## Founder Backgrounds

**Geordie Rose** — Co-founder & CEO
- Ph.D., Physics, University of British Columbia
- Co-founder and CEO of D-Wave Quantum (1999–2015) — the first company to sell commercial quantum computers; D-Wave raised $215M+ before Rose departed
- Rose's D-Wave career established a pattern: ambitious claims about the timeline and impact of an emerging technology, sustained through multiple investor cycles before gradual commercialization reality settled in. Observers note similarities between D-Wave's "is it really quantum?" debate and the current "is this really autonomous?" debate in humanoids
- Founded Kindred AI (2014–2017) briefly between D-Wave and Sanctuary — a robot picking company now acquired by Ocado
- LinkedIn: [geordie-rose](https://www.linkedin.com/in/geordie-rose-88a31/)

**Suzanne Gildert** — Co-founder & CTO
- Ph.D., Physics, University of Birmingham (UK)
- Researcher at D-Wave Quantum; world-recognized expert in quantum hardware design and adiabatic quantum computing
- Research interest in the intersection of machine learning and quantum computing led directly to physical AI interests
- Co-founder and head of hardware and AI at Sanctuary from founding
- LinkedIn: search "Suzanne Gildert Sanctuary AI"

**James Wells** — CEO (as of November 2024)
- Former Chief Commercial Officer at Sanctuary AI (5 years)
- Led the commercial pivot to industrial AI deployment
- The GRA 2026 profile identifies Wells as the current CEO

**Olivia Norton** — Co-founder & CTO (current)
- Quoted in the June 2026 press release as CTO
- Background in robotics and Physical AI

**Pattern:** Both original co-founders — Rose and Gildert — departed together in November 2024, a significant leadership discontinuity. The company transitioned from a visionary AGI-oriented narrative (Rose's framing) to a pragmatic commercial execution focus under Wells. The June 2026 hardware-agnostic pivot is the most visible result of this shift: the strategy of deploying Physical AI on existing robots rather than waiting for humanoid hardware at scale is a commercially realistic response to the difficulty of humanoid productionization.

### People — Last Reviewed: 2026-06-19

## Supply Chain & Dependencies

**Actuators:** Not publicly specified. Given the Canadian context and ~70 lbs weight (very light for a humanoid), Phoenix likely uses lighter-duty actuators than industrial platforms. Suppliers not disclosed.

**Manufacturing:** Magna International is the manufacturing scale partner — the most strategically meaningful supply chain relationship of any humanoid company. Magna's tier-1 automotive manufacturing at scale is the path from pilot quantities to thousands of units per year.

**Compute:** Microsoft Azure for training; edge inference hardware not specified.

**Sensors:** Camera-based perception plus tactile fingertip sensors (gen-8). The tactile sensor supplier is not disclosed; likely a custom design given the novelty of full-hand tactile sensing at this resolution.

**Battery:** Not disclosed. ~70 lbs weight suggests either small battery pack or external power tethering for demos.

## Claim Verification

### Claim: Phoenix completed 110+ unique tasks in a commercial setting

**Status:** Partially verified

**Supporting sources:**
- [Global Recognition Awards — Sanctuary AI Phoenix](https://globalrecognitionawards.org/innovative-companies/sanctuary-ai-phoenix/) — documents the Mark's retail pilot
- Canadian Tire Corporation is a named partner, lending credibility to the deployment context

**Qualifying sources:**
- Autonomy ratio for the 110+ tasks is not disclosed — unknown fraction were fully autonomous vs. supervised or teleoperated
- "Commercial setting" is a controlled retail pilot with a friendly partner
- Task diversity (many different tasks) is not the same as task reliability (same task 10,000 times without failure)

**Summary:** Task diversity claim is credible given named commercial partner. Autonomy level per task and production reliability are unknown.

## Sources

- [Sanctuary AI official site](https://sanctuary.ai)
- [Physical AI strategy expansion — Sanctuary AI press release, Jun 2026](https://sanctuary.ai/news/sanctuary-ai-expands-physical-ai-strategy-to-industrial-robotics-demonstrating-production-ready-ai-performance/)
- [Microsoft collaboration — Sanctuary AI press release](https://sanctuary.ai/news/sanctuary-ai-announces-microsoft-collaboration-to-accelerate-ai-development-for-general-purpose-robots/)
- [Sanctuary AI Phoenix — Global Recognition Awards, Feb 2026](https://globalrecognitionawards.org/innovative-companies/sanctuary-ai-phoenix/)
- [Sanctuary AI Series B — TechCrunch, Oct 2023](https://techcrunch.com/2023/10/18/sanctuary-ai-series-b/)
