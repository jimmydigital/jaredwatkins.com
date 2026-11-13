---
title: "Sentinel Automata"
date: 2026-11-11
lastmod: 2026-11-11
draft: false
description: "STUB — US-based, pre-release maker of ISAP-D45 and ISAP-D30 backdrivable two-stage planetary integrated joint modules (EtherCAT, 48 V) for legged-robot hips and knees, arms, and gimbals; specs are design targets, dev kits ship Q1 2027. All information is company-sourced."
research_area: "robotics/actuators"
source_urls:
  - "https://automata.llc/"
  - "https://www.linkedin.com/in/iandaily/"
  - "https://www.linkedin.com/company/sentinel-automata/about/"
last_reviewed: 2026-11-11
stale_after_days: 90
related:
  - "robotics/actuators/_index.md"
  - "robotics/ethercat/protocol-guide.md"
  - "robotics/humanoid/_index.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Sentinel Automata (Sentinel Automata Inc., founded 2026) is a US-based, pre-release startup, run as one company with three programs: integrated actuators, embedded compute (symbolic-regression coprocessors), and an open robot interoperability standard. The actuator line is the first to reach hardware: integrated robot joint modules — motor, planetary gearbox, dual encoders, and EtherCAT drive in one housing — for the hips and knees of legged robots, as well as arms, gimbals, and similar uses. Its two announced products, the ISAP-D45 and ISAP-D30, are described as backdrivable two-stage planetary joints. The company markets them as "Designed for U.S. production" with NDAA-provenance sourcing, positioning them as a domestic alternative in a category dominated by Chinese and European suppliers. No hardware has been independently tested, and all published figures are design targets. All available information comes from the company's own website; no independent coverage was found.

## Key Facts

- **Founder:** Ian Daily
- **HQ:** Long Beach, California, USA (inferred from the founder's LinkedIn location; the company site states only "Built in America" and "USA")
- **Founded:** 2026
- **Type:** Private, pre-release startup; 2–10 employees (LinkedIn); founded by Ian Daily (not named on the company website); no funding amounts disclosed; pursuing non-dilutive defense funding
- **Programs:** Actuation (US-sourced servo/joint systems), Compute (embedded symbolic-regression coprocessors), Standard (open mechanical/electrical/protocol/certification layer for robot parts)
- **Positioning:** US-sourced, "ITAR-clean from day one," dual-use with a defense-first approach; stated aim to be OEM actuator supplier to global robotics companies
- **Affiliated project:** [OpenTree]({{< relref "opentree.md" >}}) — a company-run directory and public map of US-based robot-parts makers, tied to the new FCC robot rule
- **Business model:** Component supplier — joint modules sold per unit through lot reservations, dev kits, and volume pricing
- **Value Chain Layer:** Integrated actuator module (layer 6 in the [Actuators supply chain]({{< relref "_index.md" >}}))
- **Credentials listed by company:** NVIDIA Inception member; OIST-Lifetime Startup Elevate 2026 program; SAM registration (CAGE 267S5)
- **Status:** Specs are targets until dyno testing; measured datasheet to be published after first articles pass

## Key People

### Ian Daily — Founder

- **Role:** Founder (LinkedIn headline: Founder, Sentinel Automata; "Autonomous Recovery & Actuation")
- **LinkedIn:** [linkedin.com/in/iandaily](https://www.linkedin.com/in/iandaily/) — Long Beach, California; ~1,800 followers
- **Education:** UCLA School of Law (JD)
- **Background (self-reported):** Four years in the US Marines, mostly on Okinawa, then a Marine maintenance manager responsible for \$25M in equipment and 250 people; later an M&A and regulatory attorney and operator who scaled regulated-industry ventures past \$100M in revenue
- **Stated progress (a few months in):** lead actuator at detailed design and physical mockup; open standard and reference code drafted; first channel and design partners signed
- **Hiring:** chief-engineer seat open (precision gear design for manufacture; "can sit in Japan"), plus a low-volume gearset and housing manufacturer and robotics integrators to bench early units

### People — Last Reviewed: 2026-11-11

## Recent Company Activity

- **2026-11-06:** Poster at OIST-Lifetime Startup Elevate 2026 (Deeptech Day, Okinawa); the company site also lists the OIST program. The company pitch there describes integrated joint actuators for robots going where people shouldn't, with a founding team that includes former Marines whose unit supported the 2011 Fukushima recovery.
- **Late Oct–Nov 2026:** Company posts focus on the FCC robot rule and Buy American definitions (components of unknown origin treated as foreign) and a bill-of-materials sourcing worksheet; launched the opentree US robot-parts map.


## Products (Design Targets)

| | ISAP-D45 | ISAP-D30 |
|---|---|---|
| Continuous torque | 45 N·m | 30 N·m |
| Peak torque | 139 N·m | 88 N·m |
| Max speed | 191 rpm | 306 rpm |
| Gear ratio | 22.5:1 | 14.3:1 |

**Shared platform:** ~75 mm hollow-bore motor; mass ≤1.2 kg; 48 V; EtherCAT (CiA 402); absolute encoders on motor and output; backlash ≤15 arcmin; unpowered backdrive torque ≤1.5 N·m. D45 efficiency target ≥75% at 45 N·m, 120 rpm.

## Pricing and Availability (Company-Stated)

- **Production Lot 1:** \$2,500 per joint (1,000-joint lot); reservations free, with a 20% refundable deposit due when the lot opens
- **Dev kit:** \$9,500 per joint, pre-order, shipping Q1 2027
- **Evaluation pair** (one D45, one D30): \$14,500
- **Volume:** from \$1,300 per joint at 5,000+ units per year

## Manufacturing and Sourcing

The company says the joints are designed for US production. NDAA provenance compliance is described as verified only at the first production build, so domestic manufacturing and supply-chain claims should be treated as intent rather than demonstrated capability. Like all BLDC-based joints, the design still depends on the NdFeB magnet supply chain described in the [Actuators overview]({{< relref "_index.md" >}}).

## Claim Verification

### Claim: Joint specifications (torque, speed, efficiency, backlash, mass)

**Status:** Unverified (design targets; no dyno data published)

**Supporting sources:**
- [Sentinel Automata — Home](https://automata.llc/)

### Claim: US-manufactured with NDAA-compliant sourcing

**Status:** Unverified (company states design for US production; compliance to be verified at first production build)

**Supporting sources:**
- [Sentinel Automata — Home](https://automata.llc/)

### Claim: Ian Daily is the founder

**Status:** Verified (founder's own LinkedIn profile and the company LinkedIn page; not named on the company website)

**Supporting sources:**
- Direct correspondence
- [Ian Daily — LinkedIn](https://www.linkedin.com/in/iandaily/)
- [Sentinel Automata — LinkedIn](https://www.linkedin.com/company/sentinel-automata/about/)

## Sources

- [Sentinel Automata — Home](https://automata.llc/)
- [Ian Daily — LinkedIn (public profile)](https://www.linkedin.com/in/iandaily/)
- [Sentinel Automata — LinkedIn (company page)](https://www.linkedin.com/company/sentinel-automata/about/)
