---
title: "Semiconductors"
date: 2026-04-15
lastmod: 2026-04-15
draft: false
description: "Semiconductor design, fabrication, and supporting supply chain — chips, equipment, materials, and the companies enabling advanced node manufacturing."
tags: ["semiconductors", "chips", "fabrication", "equipment", "materials"]
categories: ["overview"]
research_area: "semiconductors"
last_reviewed: 2026-04-15
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

{{<steering>}}

## Semiconductors Section — Steering Instructions

This block contains editorial and structural guidelines for AI tools maintaining the Semiconductors section. It is wrapped in `{{</* steering */>}}` shortcode tags and renders nothing on the live site.

---

### Purpose & Editorial Philosophy

The Semiconductors section documents the full stack of semiconductor design and manufacturing — from raw materials and precursor chemicals through wafer fabrication equipment, EDA software, chip design IP, and foundry services. The primary focus is on the enabling technology layer: equipment makers, materials suppliers, and specialized tooling vendors whose products make advanced node manufacturing possible. Chip designers (fabless) and large diversified IDMs (Intel, Samsung) appear in supporting context or when there is something specific and novel to document.

**Editorial priority:**
- Equipment and tooling vendors (lithography, etch, deposition, inspection, metrology)
- Materials and precursor suppliers (photomasks, photoresists, slurries, specialty gases)
- Process technology innovators (new node architectures, packaging, memory)
- Geopolitical and export-control dimensions of the supply chain

**Tone:** Neutral, technically precise, third-person. No hype, no advocacy.
**Depth:** Enough to understand where a company or technology sits in the supply chain, why it matters, and what the key risks and dependencies are.
**Audience:** Technically literate generalist (engineer, analyst, investor, policy researcher).

---

### Directory Structure

```
content/research/semiconductors/
  _index.md                              ← this file (section landing)
  fabrication-equipment/
    _index.md                            ← subtopic landing
    lasertec/
      _index.md                          ← company entry (Lasertec)
    asml/
      _index.md                          ← company entry
  materials/
    _index.md
  chip-design/
    _index.md
```

---

### Semiconductor-Specific Tags

- **Node tier:** `advanced-node` (3nm and below), `leading-edge` (3–7nm), `mature-node` (28nm+)
- **Equipment type:** `lithography`, `etch`, `deposition`, `cvd`, `pvd`, `ald`, `inspection`, `metrology`, `cmp`, `ion-implant`
- **Technology:** `euv`, `duv`, `high-na-euv`, `ebeam`, `actinic`, `photomask`, `wafer`
- **Geography:** `japan`, `netherlands`, `us`, `south-korea`, `taiwan`
- **Strategic:** `export-controls`, `monopoly`, `dual-use`, `wassenaar`

---

### Export Controls and Geopolitical Dimensions

Advanced semiconductor equipment is subject to export control regimes from multiple jurisdictions (US BIS Entity List/FDPR, Japanese METI restrictions, Dutch ASML controls). Every equipment vendor entry should document:

1. Which export control lists, if any, the company's products appear on or are subject to
2. Which geographies are restricted from receiving the equipment
3. The company's historical China revenue exposure (% of revenue) and trajectory
4. Whether the company has received government incentives or strategic partnerships related to export policy

---

### Supply Chain Criticality Flags

When a company holds a near-monopoly or sole-source position for a critical process step, flag it prominently: `**⚑ Supply chain bottleneck:** [Company] is the only qualified supplier for [technology] at [node tier].`

{{</steering>}}

## Overview

The Semiconductors section covers the full enabling stack for advanced chip manufacturing — equipment, materials, and tooling vendors whose products determine what is possible at the leading edge of Moore's Law. The section focuses on the layers below the chip designers themselves: the companies building the machines, chemicals, and inspection tools that make semiconductor fabrication possible.

---

## Subtopics

- [US Domestic Fab Expansion]({{< relref "us-fab-expansion/_index.md" >}}) — CHIPS Act projects, fab construction timelines, and domestic semiconductor manufacturing independence
- [Fabrication Equipment]({{< relref "fabrication-equipment/_index.md" >}}) — Lithography, etch, deposition, inspection, and metrology equipment for wafer fabs
- [Materials & Chemicals]({{< relref "materials/_index.md" >}}) — Silicon wafers, photoresists, specialty gases, CMP slurries, and supply chain concentration analysis
- [Chip Design — EDA & IP]({{< relref "chip-design/_index.md" >}}) — Electronic design automation tools, semiconductor IP licensing, and export controls on design software
