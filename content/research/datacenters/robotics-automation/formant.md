---
title: "Formant"
date: 2026-03-24
lastmod: 2026-10-20
draft: false
description: "San Francisco robot-operations software company (Software/AI layer): fleet management, teleoperation and analytics, plus the F3 generative-AI platform launched 2025-06-30. $21M round led by BMW i Ventures (2023-10-11). Named customers include SoftBank and BP; no datacenter deployment found. No funding or major announcement found since mid-2025 in a 2026-10-20 search."
research_area: "datacenters/robotics-automation"
source_urls:
  - "https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops"
  - "https://www.press.bmwgroup.com/usa/article/detail/T0437645EN_US/bmw-i-ventures-leads-investment-in-robotics-data-and-operations-platform-formant"
  - "https://www.therobotreport.com/tag/formant/"
  - "https://formant.io/"
  - "https://www.robotics247.com/article/formant_using_latest_funding_hires_experts_secure_cloud_robotics_platform"
  - "https://www.intelcapital.com/investing-in-formant-navigating-the-path-to-mass-adoption/"
  - "https://www.signalfire.com/blog/formant-robotics-investor"
last_reviewed: 2026-10-20
stale_after_days: 60
related:
  - "datacenters/robotics-automation/_index.md"
  - "datacenters/robotics-automation/softbank-robot-rack.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

**Value-chain position: Software/AI layer** (robot operations software; Formant builds no hardware). Formant is a San Francisco cloud robotics platform founded in 2018 by Jeff Linnell and a team of alumni from Google Robotics, Savioke, and Redwood Robotics. The company provides a software layer above individual robots — handling fleet management, teleoperation, mission tasking, incident management, and AI-driven analytics across heterogeneous robot deployments. It is not a robot manufacturer; it is the orchestration and observability platform that sits between robots on the floor and the operations teams monitoring them. SoftBank Robotics America is a named customer. Formant has raised $45M through a Series B in October 2023, led by BMW i Ventures with participation from Intel Capital. Its relevance to datacenter robotics automation is as the likely software layer for any multi-robot datacenter servicing program — if SoftBank (or others) deploy AMRs for server handling at Tomakomai or similar facilities, Formant-class platforms are the natural fleet management solution.

## Key Facts

- **Founded:** 2018
- **HQ:** San Francisco, CA
- **Type:** Private
- **CEO / Founder:** Jeff Linnell (former Google Robotics group lead)
- **Founding team:** Ex-Google Robotics, Savioke, Redwood Robotics engineers and product managers
- **Funding:** $21M round announced 2023-10-11; no later round found (total raised not stated in sources reviewed)
- **Latest round (2023-10-11):** $21M led by BMW i Ventures; Intel Capital and GS Futures joined; returning investors include SignalFire, Hillsven, Goodyear Ventures, Pelion Ventures, Holman, Ericsson, PICUS Capital and Thursday Ventures ([BMW Group](https://www.press.bmwgroup.com/usa/article/detail/T0437645EN_US/bmw-i-ventures-leads-investment-in-robotics-data-and-operations-platform-formant)); the sources fetched do not name the round (previous review called it Series B)
- **Business model:** SaaS; pricing not public
- **Named customers (company release, June 2025):** SoftBank and BP; the release says Formant has also worked with Google, John Deere, Shell and Westinghouse ([Business Wire](https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops)); SoftBank Robotics cleaning-robot data platform announced December 2023 ([The Robot Report](https://www.therobotreport.com/tag/formant/))
- **Core products:** Formant platform (fleet management, teleoperation, mission control, incident resolution, analytics); **F3** (launched 2025-06-30): voice/text command interface, AI insights (anomaly and failure prediction, incident summaries), smart knowledge base and deep-research agents
- **Robot compatibility:** heterogeneous fleets; earlier coverage shows Spot, Kinova Gen 3 and ROS-based integrations (2019-2022)

## What It Is / How It Works

Formant operates at the **Robot Operations** layer — the software infrastructure that enables human operators to manage robot fleets at scale without requiring individual attention to each unit. This is analogous to a network operations center (NOC) for robots: Formant provides the observability, control, and workflow tooling that makes it operationally tractable to run dozens or hundreds of robots across one or more facilities.

**Fleet management and teleoperation:** Operators can view live telemetry from all robots in a fleet (position, battery state, sensor feeds, error conditions) and intervene with remote teleoperation when a robot gets stuck or needs human guidance. This is the baseline capability of any commercial robot fleet platform.

**Mission Control and Tasking:** Operators can define, assign, and monitor tasks across the fleet — scheduling server inspection routes, queuing maintenance operations, or responding to on-demand service requests from a DCIM (datacenter infrastructure management) system.

**Incident Management:** When a robot encounters an error condition — obstacle, battery failure, mechanical fault — Formant surfaces the incident to the operations team with context (what the robot was doing, relevant sensor data, similar past incidents). The F3 AI Engine adds automated root cause analysis, recommending whether the issue requires human intervention or can be resolved by the robot fleet autonomously.

**Performance Analytics:** Fleet utilization metrics, task completion rates, downtime analysis, and capacity planning data. For datacenter operators evaluating ROI on robot deployments, this layer is what produces the business case metrics.

**Datacenter relevance:** No Formant datacenter deployment was found in this review. The platform is generic to robot fleets; any datacenter role is an inference from its architecture, not a reported engagement. Its named customer SoftBank is also the operator behind the robot-friendly rack work tracked in [SoftBank robot rack]({{< relref "softbank-robot-rack.md" >}}), but no connection between Formant and that program is reported.

**F3:** Announced 2025-06-30 as an "AI-native" robotics management platform built on generative AI and agentic reasoning, positioned as the orchestration layer of a "Physical AI" strategy (Brain, Body, Context). Features per the company: voice/text commands that return live visualizations and control robots, an always-on insights layer, a knowledge base answering from PDFs and SOPs with citations, and autonomous multi-step investigation agents ([Business Wire](https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops)).

## Notable Developments

No Formant funding, acquisition or product announcement dated after June 2025 was found in searches on 2026-10-20 (company site, Business Wire, The Robot Report, PitchBook and Tracxn listings); absence of news is not confirmation that nothing happened.

- **2025-06-30:** F3 platform launched (generative AI, agentic reasoning). ([Business Wire](https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops))
- **2024-10-11:** Partnership with Slalom debuted at RoboBusiness 2024. ([The Robot Report](https://www.therobotreport.com/tag/formant/))
- **2023-12-21:** Formant Analytics launched; Formant data platform announced for SoftBank's cleaning robots. ([The Robot Report](https://www.therobotreport.com/tag/formant/))
- **2023-10-11:** $21M round led by BMW i Ventures. ([BMW Group](https://www.press.bmwgroup.com/usa/article/detail/T0437645EN_US/bmw-i-ventures-leads-investment-in-robotics-data-and-operations-platform-formant), [Robotics 24/7](https://www.robotics247.com/article/formant_using_latest_funding_hires_experts_secure_cloud_robotics_platform))
- **2022-06:** Freemium Formant Studio (ROS) launched. ([The Robot Report](https://www.therobotreport.com/tag/formant/))
- **2019-08:** Cloud fleet-monitoring platform launched. ([The Robot Report](https://www.therobotreport.com/tag/formant/))

## Key People

### Jeff Linnell — CEO and Founder
- **LinkedIn:** not found (unverified profile URL removed)
- **Role:** Founder and CEO (per the June 2025 company release)
- **Background:** Led Google's robotics group before founding Formant; identified the lack of a generalized robot data and operations platform as the key missing layer for commercial robotics deployment
- **Education:** Not confirmed in public sources reviewed
- **Career (reverse-chronological):**
  - Formant (2018–present): Co-founder, CEO
  - Google: Robotics group lead (role predating Formant)
  - Savioke / Redwood Robotics: (other founding team members had these backgrounds; Linnell's specific earlier roles outside Google not confirmed)

Biographical details are as of the previous review and were not re-verified.

### People — Last Reviewed: 2026-10-20

## Supply Chain Position

Formant is a software company with no hardware supply chain dependency. Its position in the datacenter robotics stack:

| Layer | Detail |
|-------|--------|
| **Below Formant** | Robot hardware (AMRs, arms, AGFs from Boston Dynamics, Locus, custom OEM); cloud infrastructure (AWS, GCP, Azure) |
| **Formant's layer** | Fleet orchestration, teleoperation, analytics, AI engine — SaaS |
| **Above Formant** | DCIM systems, datacenter operator dashboards, human facilities teams |

**Integration risk:** Formant's value depends on broad robot hardware compatibility. If a datacenter operator deploys a robot fleet from a vendor with a closed ecosystem (Boston Dynamics Spot has a proprietary API; DJI drones operate within DJI's ecosystem), integration complexity increases. Formant's stated support for heterogeneous fleets is a direct response to this risk.

**⚑ SoftBank overlap:** SoftBank is a named Formant customer. SoftBank Corp. builds the robot-friendly datacenter rack program; whether Formant is used there is not reported.

## Claim Verification

### Claim: Formant customers see "60% less downtime," "8x utilization," "72% faster rollout"
**Status:** Unverified (marketing claim not found in sources fetched this review)

**Supporting:** None found in the June 2025 release or BMW release.

**Refuting / questioning:** No methodology, customer or measurement period was found.

**Summary:** Removed from the Key Facts as unverified; treat any such figures as marketing.

### Claim: Formant is relevant to datacenter robot fleets
**Status:** Inference, not reported

**Supporting:** SoftBank is a named customer; the platform is robot-agnostic.

**Refuting / questioning:** No datacenter customer, pilot or partnership was found.

**Summary:** Keep as a watch item only.

## Sources

- [Business Wire — Formant F3 (2025-06-30)](https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops)
- [BMW Group — BMW i Ventures leads investment in Formant (2023-10-11)](https://www.press.bmwgroup.com/usa/article/detail/T0437645EN_US/bmw-i-ventures-leads-investment-in-robotics-data-and-operations-platform-formant)
- [The Robot Report — Formant archive](https://www.therobotreport.com/tag/formant/)
- [Formant Platform — Formant.io](https://formant.io/)
- [Formant to Use Latest Funding to Hire Experts — Robotics 24/7 (Oct 2023)](https://www.robotics247.com/article/formant_using_latest_funding_hires_experts_secure_cloud_robotics_platform)
- [Investing in Formant — Intel Capital](https://www.intelcapital.com/investing-in-formant-navigating-the-path-to-mass-adoption/)
- [Formant and the Coming-of-Age Moment for Robotics Software — SignalFire](https://www.signalfire.com/blog/formant-robotics-investor)
- [Formant Crunchbase Profile](https://www.crunchbase.com/organization/formant)
