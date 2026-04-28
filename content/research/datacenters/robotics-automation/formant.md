---
title: "Formant"
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: "San Francisco cloud robotics platform; founded by ex-Google Robotics engineers; $45M raised through Series B (Oct 2023, BMW i Ventures lead); fleet management, teleoperation, AI-driven incident management and analytics for multi-robot deployments. SoftBank Robotics America is a named customer. Relevant to datacenter robot fleet orchestration as the servicing-robot layer matures."
tags: ["datacenters", "robotics-automation", "software", "fleet-management", "us", "startup"]
categories: ["company"]
research_area: "datacenters/robotics-automation"
source_urls:
  - "https://formant.io/"
  - "https://www.robotics247.com/article/formant_using_latest_funding_hires_experts_secure_cloud_robotics_platform"
  - "https://www.intelcapital.com/investing-in-formant-navigating-the-path-to-mass-adoption/"
  - "https://www.signalfire.com/blog/formant-robotics-investor"
last_reviewed: 2026-03-24
stale_after_days: 90
related:
  - "datacenters/robotics-automation/_index.md"
  - "datacenters/robotics-automation/softbank-robot-rack.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Formant is a San Francisco cloud robotics platform founded in 2018 by Jeff Linnell and a team of alumni from Google Robotics, Savioke, and Redwood Robotics. The company provides a software layer above individual robots — handling fleet management, teleoperation, mission tasking, incident management, and AI-driven analytics across heterogeneous robot deployments. It is not a robot manufacturer; it is the orchestration and observability platform that sits between robots on the floor and the operations teams monitoring them. SoftBank Robotics America is a named customer. Formant has raised $45M through a Series B in October 2023, led by BMW i Ventures with participation from Intel Capital. Its relevance to datacenter robotics automation is as the likely software layer for any multi-robot datacenter servicing program — if SoftBank (or others) deploy AMRs for server handling at Tomakomai or similar facilities, Formant-class platforms are the natural fleet management solution.

## Key Facts

- **Founded:** 2018
- **HQ:** San Francisco, CA
- **Type:** Private
- **CEO / Founder:** Jeff Linnell (former Google Robotics group lead)
- **Founding team:** Ex-Google Robotics, Savioke, Redwood Robotics engineers and product managers
- **Total funding:** $45M across 3 rounds
- **Series B:** $21M, October 2023; led by BMW i Ventures; participants include Intel Capital, GS Futures, SignalFire, Hillsven, Pelion Ventures, Ericsson, Goodyear Ventures, PICUS Capital
- **Business model:** SaaS subscription; per-robot or per-fleet pricing (specifics not public)
- **Named customers:** SoftBank Robotics America (Brady Watkins, President of SoftBank Robotics America, quoted in customer materials)
- **Core products:** Formant Platform (fleet management, teleoperation, mission tasking, incident management, performance analytics); F3 AI Engine (voice commands, predictive insights, automated root cause analysis)
- **Robot compatibility:** Broad heterogeneous fleet support; publishes a supported robot database; integrates via ROS, custom SDKs

## What It Is / How It Works

Formant operates at the **Robot Operations** layer — the software infrastructure that enables human operators to manage robot fleets at scale without requiring individual attention to each unit. This is analogous to a network operations center (NOC) for robots: Formant provides the observability, control, and workflow tooling that makes it operationally tractable to run dozens or hundreds of robots across one or more facilities.

**Fleet management and teleoperation:** Operators can view live telemetry from all robots in a fleet (position, battery state, sensor feeds, error conditions) and intervene with remote teleoperation when a robot gets stuck or needs human guidance. This is the baseline capability of any commercial robot fleet platform.

**Mission Control and Tasking:** Operators can define, assign, and monitor tasks across the fleet — scheduling server inspection routes, queuing maintenance operations, or responding to on-demand service requests from a DCIM (datacenter infrastructure management) system.

**Incident Management:** When a robot encounters an error condition — obstacle, battery failure, mechanical fault — Formant surfaces the incident to the operations team with context (what the robot was doing, relevant sensor data, similar past incidents). The F3 AI Engine adds automated root cause analysis, recommending whether the issue requires human intervention or can be resolved by the robot fleet autonomously.

**Performance Analytics:** Fleet utilization metrics, task completion rates, downtime analysis, and capacity planning data. For datacenter operators evaluating ROI on robot deployments, this layer is what produces the business case metrics.

**Formant's datacenter relevance:** Formant itself does not operate in the datacenter automation space today — its current customers are in enterprise warehouse, logistics, security, and industrial settings. However, its architecture is directly applicable: as SoftBank, Submer, or other operators deploy AMRs for server handling or immersion tank servicing, they will need exactly this class of platform. Formant's SoftBank Robotics America relationship is a direct link to the SoftBank datacenter automation program.

**F3 AI Engine:** Formant's newer AI-layer product (announced 2024–2025) adds voice-command interaction ("show me all robots with battery below 20%"), predictive analytics (flagging robots likely to fail before they do), and a knowledge base for troubleshooting. This positions Formant as an AI-native platform rather than a traditional SCADA-style control system — relevant for the complexity of multi-vendor robot fleets in a datacenter environment.

## Notable Developments

- **2023-10:** Series B — $21M led by BMW i Ventures; Intel Capital and GS Futures join as new investors; proceeds directed at hiring security and platform engineers. ([Robotics 24/7](https://www.robotics247.com/article/formant_using_latest_funding_hires_experts_secure_cloud_robotics_platform))
- **~2022–2023:** F3 AI Engine introduced; adds voice commands and AI-native analytics layer to the platform
- **2021:** Series A funding; SignalFire publishes investment thesis citing Formant as infrastructure play for the coming robotics deployment wave
- **2018:** Founded by Jeff Linnell and team; early focus on ROS-compatible fleet management for heterogeneous robots

## Key People

### Jeff Linnell — CEO and Founder
- **LinkedIn:** [linkedin.com/in/jefflinnell](https://www.linkedin.com/in/jefflinnell/) *(verify — common profile pattern)*
- **Role:** Co-founder and CEO
- **Background:** Led Google's robotics group before founding Formant; identified the lack of a generalized robot data and operations platform as the key missing layer for commercial robotics deployment
- **Education:** Not confirmed in public sources reviewed
- **Career (reverse-chronological):**
  - Formant (2018–present): Co-founder, CEO
  - Google: Robotics group lead (role predating Formant)
  - Savioke / Redwood Robotics: (other founding team members had these backgrounds; Linnell's specific earlier roles outside Google not confirmed)

### People — Last Reviewed: 2026-03-24

## Supply Chain Position

Formant is a software company with no hardware supply chain dependency. Its position in the datacenter robotics stack:

| Layer | Detail |
|-------|--------|
| **Below Formant** | Robot hardware (AMRs, arms, AGFs from Boston Dynamics, Locus, custom OEM); cloud infrastructure (AWS, GCP, Azure) |
| **Formant's layer** | Fleet orchestration, teleoperation, analytics, AI engine — SaaS |
| **Above Formant** | DCIM systems, datacenter operator dashboards, human facilities teams |

**Integration risk:** Formant's value depends on broad robot hardware compatibility. If a datacenter operator deploys a robot fleet from a vendor with a closed ecosystem (Boston Dynamics Spot has a proprietary API; DJI drones operate within DJI's ecosystem), integration complexity increases. Formant's stated support for heterogeneous fleets is a direct response to this risk.

**⚑ SoftBank Robotics connection:** SoftBank Robotics America is a named Formant customer. SoftBank Corp. (the parent, different entity) is building the Tomakomai robot-friendly datacenter. The connection between SoftBank Robotics (humanoid and service robots) and SoftBank Corp.'s datacenter program is not confirmed, but the organizational adjacency is worth monitoring. If Formant is embedded in SoftBank Robotics' platform, it may be positioned to serve SoftBank Corp.'s datacenter fleet as well.

## Claim Verification

### Claim: "60% reduction in downtime," "8x increase in utilization," "72% faster rollout"
**Status:** Customer-reported metrics; not independently audited

**Supporting:**
- These are characteristic performance improvement figures for fleet management software in warehouse/logistics robotics — plausible directionally
- Series B investors including BMW i Ventures (automotive/industrial robotics focus) and Intel Capital conducted due diligence before investing

**Refuting / questioning:**
- No third-party study or customer case study methodology is published; figures appear in marketing materials without attribution to specific customers or defined measurement periods
- "8x increase in utilization" is an unusually high figure that likely reflects a baseline with very poor utilization (common in early-stage robot deployments without fleet management software)

**Summary:** Treat as directionally illustrative rather than precisely accurate. The order of magnitude of improvement is consistent with industry experience in fleet management software, but the specific numbers are unverified marketing claims.

## Sources

- [Formant Platform — Formant.io](https://formant.io/)
- [Formant to Use Latest Funding to Hire Experts — Robotics 24/7 (Oct 2023)](https://www.robotics247.com/article/formant_using_latest_funding_hires_experts_secure_cloud_robotics_platform)
- [Investing in Formant — Intel Capital](https://www.intelcapital.com/investing-in-formant-navigating-the-path-to-mass-adoption/)
- [Formant and the Coming-of-Age Moment for Robotics Software — SignalFire](https://www.signalfire.com/blog/formant-robotics-investor)
- [Formant Crunchbase Profile](https://www.crunchbase.com/organization/formant)
