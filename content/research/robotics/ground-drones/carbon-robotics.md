---
title: "Carbon Robotics"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "Seattle, WA agricultural robotics company; LaserWeeder uses 30 CO₂ lasers to eliminate weeds with millimeter precision without herbicides; LaserWeeder G2 launched 2024; $70M raised; peer-reviewed 2024 study confirms effectiveness comparable to herbicides in vegetable crops."
tags: ["robotics", "agricultural", "ugv", "us", "commercial"]
categories: ["company"]
research_area: "robotics/ground-drones"
source_urls:
  - "https://carbonrobotics.com/laserweeder"
  - "https://carbonrobotics.com/laserweeder-g2"
  - "https://www.agriculturedive.com/news/carbon-robotics-raises-70m-for-its-ai-powered-laserweeder/730725/"
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC12268811/"
  - "https://wga.s3.us-west-1.amazonaws.com/cit/2024/cit_case-study_carbon-robotics.pdf"
last_reviewed: 2026-03-31
stale_after_days: 90
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Carbon Robotics (Seattle, WA) develops the LaserWeeder — a tractor-pulled implement that uses AI-guided CO₂ lasers to eliminate weeds in specialty vegetable crops without herbicides or soil disturbance. Founded in 2018 by Paul Mikesell (serial entrepreneur, ex-Isilon Systems co-founder), the company has raised $70M+ in funding. The LaserWeeder G2, launched in 2024, offers double the operating speed of the original and supports widths from 6.6 to 60 feet with 30 lasers. A 2024 peer-reviewed study confirmed that laser weeding reduced weed biomass by ≥97% — comparable to conventional herbicide applications.

## Key Facts

- **Founded:** 2018
- **HQ:** Seattle, WA
- **Type:** Private
- **Key backers:** Sozo Ventures (Series C lead), Anthos Capital, Fuse VC, Ignition Partners, Liquid2, Voyager Capital; $70M+ raised (Agriculture Dive, April 2024)
- **Key products:** LaserWeeder G2 (tractor-pulled, 30 CO₂ lasers, 6.6–60 ft width, 4,250 lb minimum); LaserWeeder (original, legacy)
- **Revenue / valuation:** Private; not disclosed
- **Series C:** $30M (April 2023); subsequent $70M+ round (Agriculture Dive reports $70M in 2024)

## What It Is / How It Works

The LaserWeeder is a large tractor-pulled implement that uses an array of high-powered CO₂ lasers to destroy weeds at the meristem — the growing point at the base of the plant — with millimeter-level precision. Computer vision and deep learning models identify weeds in real time as the implement moves through the field; the laser fires only at confirmed weed meristems, leaving crop plants undisturbed. The process eliminates the need for herbicide application in the treated zone.

The key technical challenge is the computer vision task: distinguishing weeds from crops in real time, across variable soil conditions, at the speed needed for commercial field operations. Carbon Robotics built what it calls a "large plant model" — a deep learning system trained on millions of plant images that can classify plants quickly enough to fire the laser accurately at field speeds. The 2025 GeekWire article noted Carbon Robotics was developing a new "AI robot" product (undisclosed specifications) suggesting expansion beyond the tractor-pull LaserWeeder format.

The LaserWeeder G2 (launched February 2024) is 2x faster than the original, weighing from 4,250 lbs, with modularity supporting variable widths from 6.6 ft (for tight row crops) to 60 ft (for broad field applications). The 30 CO₂ lasers provide high throughput — up to 200,000 weeds per hour per company claims.

Independent validation came in 2024 from two sources: a peer-reviewed PMC/Wiley study in three vegetable production systems (beet, spinach, pea) found laser weeding reduced weed biomass by ≥97% — comparable to or better than herbicide benchmarks; and a Western Growers case study found farms in the Salinas Valley cut weeding costs from $900/acre to $268/acre (70% reduction). These represent meaningful independent corroboration of the core technology claims.

Competitive context: John Deere's See & Spray (acquired from Blue River Technology) uses herbicide spot-spraying guided by computer vision rather than lasers — lower capital cost but still involves chemical inputs. FarmWise/Trimble uses mechanical weeding. Carbon Robotics is the only commercial pure-laser-weeding system in the market.

## Notable Developments

- **2025-06:** Named to CNBC Disruptor 50 list. ([CNBC](https://www.cnbc.com/2025/06/10/carbon-robotics-cnbc-disruptor-50.html))
- **2025-04:** Carbon Robotics raises $20M and announces new "AI robot" product in development. ([GeekWire](https://www.geekwire.com/2025/carbon-robotics-raises-20m-as-laserweeder-maker-plans-secretive-new-ai-robot-for-farms/))
- **2024:** Peer-reviewed study (PMC, Wiley Open Access) confirms LaserWeeder effectiveness ≥97% weed biomass reduction in vegetable crops, comparable to herbicides. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12268811/))
- **2024-02:** LaserWeeder G2 launched — 2x faster, lighter (4,250 lb base), modular widths 6.6–60 ft, 30 CO₂ lasers. ([Carbon Robotics](https://carbonrobotics.com/laserweeder-g2))
- **2024:** Agriculture Dive reports $70M funding round. ([Agriculture Dive](https://www.agriculturedive.com/news/carbon-robotics-raises-70m-for-its-ai-powered-laserweeder/730725/))
- **2024-03:** Western Growers case study documents 70% weeding cost reduction at Salinas Valley farms. ([Western Growers](https://wga.s3.us-west-1.amazonaws.com/cit/2024/cit_case-study_carbon-robotics.pdf))
- **2023-04:** $30M Series C (Sozo Ventures lead). ([Business Wire](https://www.businesswire.com/news/home/20230411005018/en/Carbon-Robotics-Raises-30-Million-in-Funding-to-Scale-AI-Powered-LaserWeeder-Platform))
- **2018:** Founded by Paul Mikesell in Seattle, WA.

## Key People

### Paul Mikesell — Founder and CEO
- **LinkedIn:** not found
- **Education:** Not publicly disclosed in available sources
- **Career (reverse-chronological):**
  - Carbon Robotics (2018–present): Founder and CEO
  - Isilon Systems: Co-founder; company went public 2006, acquired by EMC for $2.5B in 2010
- **Notes:** Serial entrepreneur with a prior successful hardware+software company exit. Isilon Systems built distributed storage systems — a background in large-scale data management systems that translates to Carbon Robotics' AI inference workloads.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

Carbon Robotics is a **Platform OEM** at the agricultural robotics layer. The LaserWeeder is designed and manufactured in Seattle. CO₂ laser sources are commercial industrial laser components (supplier not disclosed); computer vision runs on embedded GPU compute (NVIDIA Jetson or equivalent). The implement is powered by the tractor's PTO (power take-off), not a self-contained power source. **⚑ Rare earth dependency:** If servo or stepper motors are used for laser beam steering or implement positioning, NdFeB magnets apply; the primary CO₂ laser mechanism itself does not require rare earth materials.

## Claim Verification

### Claim: LaserWeeder eliminates 200,000 weeds per hour at 99% efficiency
**Status:** Partially verified

**Supporting sources:**
- [Carbon Robotics LaserWeeder page](https://carbonrobotics.com/laserweeder) — Company-stated: "eliminate more than 200,000 weeds per hour"; "up to 99% efficiency in weed death"
- [PMC peer-reviewed study (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12268811/) — Independent academic study confirms ≥97% weed biomass reduction across three vegetable crop types; this is close to the 99% claim and provides genuine academic validation
- [Western Growers case study (Mar 2024)](https://wga.s3.us-west-1.amazonaws.com/cit/2024/cit_case-study_carbon-robotics.pdf) — Farm-level cost reduction data corroborates practical effectiveness

**Refuting / questioning sources:**
- "200,000 weeds per hour" depends heavily on weed density per acre, operating speed, and field conditions; this is a throughput maximum under favorable conditions, not a consistent field average
- 99% efficiency claim is slightly higher than the 97% in the peer-reviewed study; the gap is small but the peer-reviewed figure is more credible
- Performance in different crop types (vs. the vegetable crops studied) has not been independently verified

**Summary:** The peer-reviewed 2024 study provides strong independent validation that laser weeding is as effective as herbicides in vegetable crops; the specific 200,000 weeds/hour and 99% efficiency figures are company-stated maximums, with independent science supporting the general effectiveness claim at a similar level.

## Sources

- [LaserWeeder — Carbon Robotics](https://carbonrobotics.com/laserweeder)
- [LaserWeeder G2 — Carbon Robotics](https://carbonrobotics.com/laserweeder-g2)
- [Carbon Robotics $70M Raise — Agriculture Dive](https://www.agriculturedive.com/news/carbon-robotics-raises-70m-for-its-ai-powered-laserweeder/730725/)
- [Peer-Reviewed Laser Weeding Study — PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12268811/)
- [Western Growers Case Study (Mar 2024)](https://wga.s3.us-west-1.amazonaws.com/cit/2024/cit_case-study_carbon-robotics.pdf)
- [Carbon Robotics $20M Raise + New AI Robot — GeekWire (Apr 2025)](https://www.geekwire.com/2025/carbon-robotics-raises-20m-as-laserweeder-maker-plans-secretive-new-ai-robot-for-farms/)
- [Series C $30M — Business Wire (Apr 2023)](https://www.businesswire.com/news/home/20230411005018/en/Carbon-Robotics-Raises-30-Million-in-Funding-to-Scale-AI-Powered-LaserWeeder-Platform)
