---
title: "AMR & Logistics Robotics"
date: 2026-06-19
lastmod: 2026-06-19
draft: false
description: "Autonomous Mobile Robots (AMRs) and logistics automation platforms for warehouse picking, transport, and fulfillment — the commercially mature layer below humanoids."
tags: ["robotics", "amr", "logistics", "warehouse", "fulfillment"]
categories: ["overview"]
research_area: "robotics/amr-and-logistics"
last_reviewed: 2026-06-19
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

## Overview

Autonomous Mobile Robots for warehouse and logistics are the commercially mature tier of mobile robotics — deployed at scale, generating real revenue, and solving defined logistics problems. This is the layer that humanoid companies are competing against and sometimes partnering with.

The AMR warehouse market was valued at $7.1B in 2025 and is projected to reach $91B by 2034 (CAGR 34%). As of 2026, the median new AMR deployment is 35 robots per facility; multi-vendor fleets are common and driving demand for fleet management software (see [Software & Integration]({{< relref "../software-and-integration/_index.md" >}})).

The key commercial distinction from humanoids: AMRs solve defined logistics tasks (move tote A from location B to station C) with high reliability, 24/7 runtime on facility power or fast-swap batteries, and established ROI models. They do not claim general-purpose capability.

## Entries

- [6 River Systems]({{< relref "6-river-systems.md" >}}) — Chuck AMR; originally Shopify-acquired, now independent; goods-to-person picking
- [Locus Robotics]({{< relref "../ground-drones/locus-robotics.md" >}}) — LocusBot; goods-to-person; AI exception handling (in ground-drones section)
- [Fetch Robotics]({{< relref "../ground-drones/fetch-robotics.md" >}}) — Acquired by Zebra Technologies; industrial AMR platform (in ground-drones section)
- [Geek+]({{< relref "../ground-drones/geek-plus.md" >}}) — Chinese AMR leader; goods-to-robot shelving systems (in ground-drones section)

## Companies

### Startups & Growth-Stage

| Company | HQ | Stage | What They Do |
|---------|-----|-------|--------------|
| [6 River Systems](https://6river.com) | Waltham, MA | Growth (independent) | Chuck AMR; collaborative picking with human "associates" |
| [Locus Robotics](https://locusrobotics.com) | Wilmington, MA | Growth | LocusBot; goods-to-person; GenAI exception management |
| [inVia Robotics](https://inviarobotics.com) | Westlake Village, CA | Growth | Goods-to-robot; Robotics-as-a-Service model |

### Public Companies / Acquired

| Company | Parent | Robot |
|---------|--------|-------|
| [Fetch Robotics](https://fetchrobotics.com) | Zebra Technologies (NASDAQ: ZBRA) | Freight series AMRs; industrial transport |
| [Geek+](https://geekplus.com) 🇨🇳 | Private (China) | PopPick, RoboShuttle; shelving automation; 50,000+ deployed |

### Incumbents (integrated WHS/logistics systems)

| Company | Relevance |
|---------|-----------|
| [Daifuku](https://daifuku.com) | Japanese systems integrator; conveyors + sortation + AMR at scale |
| [KION Group / Dematic](https://dematic.com) | German conglomerate; Dematic WES + AMR; owns Linde and STILL forklifts |
| [Körber Supply Chain](https://koerber-supplychain.com) | WMS + robotics control; acquires robotics software |

## VDA 5050 and Multi-Vendor Fleets

The VDA 5050 standard (see [Software & Integration]({{< relref "../software-and-integration/_index.md" >}})) is the key enabler of mixed-vendor AMR fleets. As of 2026, specifying VDA 5050 compliance is standard procurement practice. SVT Robotics and Vecna Pivotal both support VDA 5050 coordination. SYNAOS validated five-vendor fleet management at Mobile Robotics Summit 2025.
