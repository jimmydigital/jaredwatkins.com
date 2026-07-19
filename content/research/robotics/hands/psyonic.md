---
title: "PSYONIC"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "San Diego prosthetics-to-robotics company founded 2015 by Dr. Aadeel Akhtar; FDA-approved, Medicare-covered Ability Hand myoelectric prosthetic (300+ patients); partnered with ABB Robotics (Jun 2026) to apply human-prosthetic touch/force data to industrial and humanoid dexterous manipulation via the GoFa cobot."
research_area: "robotics/hands"
source_urls:
  - "https://www.therobotreport.com/psyonic-abb-robotics-partner-apply-human-touch-data-robot-dexterity/"
  - "https://www.psyonic.io"
last_reviewed: 2026-07-18
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

PSYONIC, based in San Diego, California, was founded in 2015 by Dr. Aadeel Akhtar to develop affordable, advanced prosthetic hands. Its Ability Hand is FDA-approved, covered by Medicare in the US, and in use by 300+ patients; Meta was an early purchaser after PSYONIC's nationwide release. In June 2026, PSYONIC announced a partnership with ABB Robotics (majority-owned by SoftBank since an October 2025 $5.3B sale) to combine the Ability Hand with ABB's GoFa collaborative robot, applying touch and motion data captured from human prosthetic users to train industrial and humanoid dexterous-manipulation systems. The company represents a distinctive technology-transfer path in the dexterous-hand sector: rather than adapting industrial actuator technology for prosthetic use, PSYONIC is repurposing a medical device — and the real-world human-contact data it generates — for robotics.

## Key Facts

- **Founded:** 2015
- **HQ:** San Diego, CA, USA
- **Type:** Private company — Component/Subsystem Supplier (originating in medical devices)
- **Status:** Active; FDA-approved prosthetic in commercial use; new industrial/robotics partnership (ABB, Jun 2026) in early evaluation phase
- **Key product:** Ability Hand — five-finger myoelectric prosthetic hand with integrated touch sensing and vibration feedback; also sold in a robotics/gripper configuration
- **Regulatory status:** FDA-approved; covered by Medicare (US)
- **Patients using the prosthetic version:** 300+ as of mid-2026
- **Value chain position:** Component/Subsystem Supplier — dexterous end effector and human-derived manipulation training data, sold/partnered into both prosthetics and robotics channels
- **Key partner (2026):** ABB Robotics (GoFa cobot; owned by SoftBank since Oct 2025 $5.3B sale from ABB Group)

## What It Is / How It Works

The Ability Hand combines myoelectric control (reading electrical signals from a user's residual muscles), touch sensing, and compliant mechanics in a lightweight, multi-articulating design. Pressure sensors and a vibration feedback system let prosthetic users detect contact, grip force, and release, while flexible fingers conform naturally to irregular and deformable objects — capabilities originally engineered to restore function and sensation for amputees, not for industrial automation.

**From prosthetics to robotics:** According to founder and CEO Dr. Aadeel Akhtar, PSYONIC's business emphasis shifted substantially toward the robotics side over the year prior to mid-2026, as "physical AI" investment accelerated. The company argues the same problems it solved for prosthetics — robustness, consistency, and tactile feedback for high-mix, low-volume object handling — map directly onto both industrial pick-and-place and home tasks like washing dishes or folding laundry, where suction and parallel-jaw grippers struggle with deformable or irregular objects.

**ABB Robotics partnership (announced June 16, 2026):** ABB Robotics and PSYONIC are combining the GoFa force- and power-limited collaborative robot with the Ability Hand to explore whether touch and motion data from human prosthetic users can train robots to perform manipulation tasks that have been difficult to automate. ABB frames this within its "Autonomous Versatile Robotics" (AVR) strategy — robots that sense, reason, move, and precisely handle objects in dynamic environments. The partnership is explicitly a data-and-training collaboration, not (yet) a product: the companies state they are assessing over a 6–12 month window how to reach greater than 99% grasping reliability, starting with automotive and warehouse pick-and-place, with laboratory automation (handling beakers and test tubes) called out as a particularly large target market.

**Why tactile data matters more than teleoperation, per PSYONIC:** Dr. Akhtar argues that most manipulation training today comes from teleoperation (gloves, VR) or video analysis, both of which capture only position information — where a hand is — not how much force a human applies to avoid crushing a raspberry or dropping a coffee mug. Because the same Ability Hand is used on both human prosthetic patients and robots, PSYONIC can capture high-fidelity contact, grip-force, and torque data from real human use (including synchronized with multimodal data such as Meta Ray-Ban camera footage) and apply it directly to robot training — a claim that models need less data when trained on this kind of high-quality, multimodal tactile data than on teleoperation or video alone.

**Cross-embodiment ambition:** PSYONIC states its next-generation hand, while retaining a human-inspired form factor, is being designed to work across embodiments — cobots and industrial automation as well as wheeled and legged robots, including humanoids — rather than being built as a single-platform-exclusive component.

**AI stack:** PSYONIC is working with both ABB's R&D team and NVIDIA's Isaac Lab and GR00T platforms to train vision-language-action (VLA) and world models on its captured data.

## Notable Developments

- **2026-06-16:** Announced partnership with ABB Robotics combining the GoFa cobot with the Ability Hand to apply human-prosthetic touch/motion data to industrial and humanoid dexterous manipulation; targeting automotive, warehouse, aerospace, packaging, logistics, and laboratory-automation use cases.
- **2025-10:** ABB Group sold ABB Robotics to SoftBank for $5.3B, making PSYONIC's 2026 robotics partner a SoftBank-owned entity.
- **Ongoing (as of 2026):** 300+ patients using the FDA-approved, Medicare-covered Ability Hand prosthetic; Meta cited as an early purchaser following nationwide release.
- **2015:** PSYONIC founded by Dr. Aadeel Akhtar.

## Key People

**Dr. Aadeel Akhtar** — Founder & CEO
- Began focusing on prosthetics as a child after meeting a same-age amputee in Pakistan with limited healthcare access
- As a University of Illinois graduate student, fit a 3D-printed bionic hand prototype on a patient in Ecuador (2014) via the Range of Motion Project, which motivated commercializing the technology as PSYONIC
- Named to MIT Technology Review's "35 Innovators Under 35"
- LinkedIn: [aadeelakhtar](https://www.linkedin.com/in/aadeelakhtar/)
- Personal site: [aadeelakhtar.com](https://www.aadeelakhtar.com/)

### People — Last Reviewed: 2026-07-18

## Supply Chain Position

PSYONIC operates at the **Tactile & Force Sensing** and **Integrated Hand Assembly** layers of the [Robotic Hands & Dexterous Manipulation]({{< relref "_index.md" >}}) supply chain, with a distinctive additional position as a **human-derived training-data source** — the same physical device (Ability Hand) generates commercial prosthetic revenue and proprietary tactile/force datasets used to train robot manipulation models.

**⚑ Shared AI stack:** PSYONIC's use of NVIDIA Isaac Lab/GR00T for VLA model training is shared with multiple humanoid platform OEMs documented elsewhere in this knowledge base (e.g., 1X Technologies' GR00T-based NEO stack — see [1X Technologies]({{< relref "../humanoid/us-companies/1x-technologies.md" >}})), underscoring NVIDIA's position as a common dependency across otherwise-unrelated humanoid and end-effector companies.

## Claim Verification

### Claim: Models trained on PSYONIC's human-prosthetic tactile data need less data than teleoperation- or video-based training

**Status:** Unverified (company claim, made by the founder in an interview, not an independent benchmark)

**Supporting sources:**
- Dr. Akhtar's stated rationale is mechanistically plausible: teleoperation gloves and video capture position but not force/pressure, which is relevant to tasks requiring delicate or variable grip force
- The ABB partnership is explicitly structured to test this hypothesis over a 6–12 month evaluation window, targeting a defined reliability bar (>99%)

**Refuting / questioning sources:**
- No published, independent benchmark compares PSYONIC's tactile-data training approach against teleoperation- or video-only approaches on a standardized manipulation task set
- The claim originates from a single interview with the company's own founder/CEO, not a peer-reviewed or third-party study

**Summary:** A plausible and testable hypothesis with a concrete evaluation window (ABB partnership, 6–12 months), but currently a company claim rather than a verified result.

### Claim: ABB Robotics + PSYONIC will reach >99% grasping reliability for pick-and-place tasks

**Status:** Unverified (forward-looking target)

**Supporting sources:**
- Explicitly stated as the goal of the joint 6–12 month evaluation program by both companies

**Refuting / questioning sources:**
- No interim results have been published as of this review; the timeline had not yet elapsed as of July 2026

**Summary:** A stated target, not yet a result. Revisit at or after the 6–12 month evaluation window (approximately Q4 2026–Q2 2027).

## Sources

- [PSYONIC partners with ABB Robotics to apply human touch to robot dexterity — The Robot Report, Jun 16 2026](https://www.therobotreport.com/psyonic-abb-robotics-partner-apply-human-touch-data-robot-dexterity/)
- [PSYONIC official site](https://www.psyonic.io)
