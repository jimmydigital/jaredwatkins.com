---
title: "PAL Robotics"
date: 2026-06-19
lastmod: 2026-06-19
draft: false
description: "Barcelona-based humanoid and mobile robot company; 2004 founding; TALOS bipedal research platform; KANGAROO lower-body system; TIAGo mobile manipulator; primary market European research institutions; now part of UNITY Robotics Group."
research_area: "robotics/humanoid"
source_urls:
  - "https://pal-robotics.com"
  - "https://blog.robozaps.com/b/humanoid-robot-companies"
  - "https://ec.europa.eu/research/participants/portal/"
last_reviewed: 2026-06-19
stale_after_days: 365
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

PAL Robotics is a Barcelona-based company, one of the few European humanoid and bipedal robot developers, and the oldest with a continuous commercial product line. Founded 2004, it predates the current humanoid boom by nearly two decades. Its TALOS platform is a research bipedal used by European university labs; TIAGo is a widely deployed research mobile manipulator; KANGAROO is a bipedal lower-body system for custom integrations. PAL is not competing for industrial deployment at scale — its niche is supplying capable, well-documented research platforms to the European academic community and EU-funded projects. PAL Robotics is now part of the UNITY Robotics Group, a Spanish robotics holding company.

## Key Facts

- **Founded:** 2004 (Barcelona, Spain)
- **HQ:** Barcelona, Catalonia, Spain
- **Parent:** UNITY Robotics Group (Spanish holding company)
- **Type:** Company — Platform OEM (research market)
- **Status:** Active — commercial research platforms; ongoing EU project participation
- **Ownership:** Private; Spanish/European
- **Total funding:** Not publicly disclosed; mix of private equity and EU R&D grants
- **Employees:** ~80–100 (estimated from company size descriptions; not publicly disclosed)
- **Key robots:** TALOS (full bipedal humanoid, research), KANGAROO (bipedal lower body), TIAGo (mobile manipulator), TIAGo++ (dual-arm), ARI (social/humanoid service robot)
- **Primary market:** European research institutions, EU-funded Horizon projects
- **Value chain position:** Platform OEM (research market)

## Funding & Context

PAL Robotics' funding structure reflects its research-market orientation:
- EU Horizon Europe grants (participant or prime contractor in multiple projects)
- Private equity from UNITY Robotics Group parent
- Revenue from TALOS and TIAGo system sales to universities (~€200K–€400K per TALOS system; ~€100K per TIAGo)

**UNITY Robotics Group:** Spanish holding company that has consolidated several European robotics and automation companies. PAL's integration into a holding structure provides access to capital and cross-portfolio opportunities without VC pressure to achieve US-startup-style growth.

**EU research funding:** PAL is a participant in numerous Horizon Europe and H2020 projects covering humanoid locomotion, manipulation, and human-robot interaction. This gives the company recurring project revenue and collaborative relationships with European robotics research labs (LAAS-CNRS, IIT, DLR, Fraunhofer).

## What It Is / How It Works

PAL Robotics builds research-grade platforms sold primarily to European universities and research institutes. The business model is hardware + ROS/ROS 2 integration + technical support, not robotics-as-a-service or industrial deployment.

**TALOS:** 1.75m, ~95 kg full bipedal humanoid with high-torque electric joints. Open-source software stack (ROS/ROS 2 compatible). Used for manipulation and locomotion research, not commercial deployment. TALOS is notable as the European alternative to US research platforms (Atlas for research-grade capability, Agility Cassie for locomotion focus).

**TIAGo:** Mobile manipulator (wheeled base + single arm, or dual-arm TIAGo++). Most commercially successful PAL product; deployed at 100+ research institutions globally. TIAGo was used in RoboCup@Home competition and numerous EU projects. Its success demonstrates PAL's ability to build commercially viable research products.

**KANGAROO:** Bipedal lower body system — legs and pelvis — designed to be integrated with custom upper bodies. This "KANGAROO + custom upper" approach is targeted at research groups wanting to build their own humanoid without designing legs. Positions PAL as a subsystem supplier as well as a full platform provider.

**ARI:** Social robot — humanoid upper body on wheeled base for interaction research and front-desk applications. Targets hospitality and healthcare interaction research markets.

**ROS ecosystem:** PAL Robotics has been a major contributor to the ROS (Robot Operating System) ecosystem. Their deep integration with ROS 2 makes their platforms the default choice for European roboticists who use ROS.

## Founder Background

**Francesco Ferro** — Co-founder & CEO
- Background in mechanical engineering and robotics; University of Catania (Italy)
- Co-founded PAL Robotics 2004 in Barcelona
- Led the company through 20+ years of European research market development
- LinkedIn: [francescoferro](https://www.linkedin.com/in/francescoferro/)

**Luca Marchionni** — Co-founder & CTO
- Background in electrical engineering and robotics
- Technical lead on TALOS, TIAGo hardware and software architecture
- LinkedIn: [lucamarchionni](https://www.linkedin.com/in/lucamarchionni/)

**Pattern:** PAL's 20-year survival in the European research robotics market — a segment not known for generating venture returns — is evidence of disciplined market focus and sustainable business model. Ferro and Marchionni chose a defensible niche over attempting to compete directly with US and Chinese industrial humanoid OEMs.

### People — Last Reviewed: 2026-06-19

## Supply Chain & Dependencies

**Actuators:** High-torque electric drives for TALOS joints; motion control electronics from European suppliers (Elmo Motion Control, Advanced Motion Controls). TALOS joints are custom-designed.

**Compute:** ROS 2-compatible control computer; NVIDIA Jetson for AI inference on TALOS and TIAGo platforms.

**Manufacturing:** Barcelona; small-batch production appropriate for research market volume (tens of systems per year).

**EU supply chain:** European components where possible (given EU procurement norms for research institution customers); some Asian-sourced electronics.

## Competitive Position

PAL occupies a niche that large humanoid OEMs have no incentive to serve: the research institution market needs thoroughly documented, open-source-compatible platforms with strong ROS integration and local support — not optimized-for-cost production robots. This protects PAL from direct competition with Unitree (which is too opaque for European research procurement) or US industrial humanoids (which are too expensive and not research-oriented).

Risk: If Agility or other US companies produce research-licensed versions of their hardware (as Agility did with Cassie), or if Chinese manufacturers improve documentation and ROS support, PAL's differentiation narrows.

## Sources

- [PAL Robotics official site](https://pal-robotics.com)
- [30+ humanoid robot companies ranked — Robozaps 2026](https://blog.robozaps.com/b/humanoid-robot-companies)
- [EU Horizon Research participant portal](https://ec.europa.eu/research/participants/portal/)
