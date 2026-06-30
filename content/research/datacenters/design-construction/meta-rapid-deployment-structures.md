---
title: "Meta Rapid Deployment Structures"
date: 2026-06-04
lastmod: 2026-06-04
draft: false
description: "Meta's fabric-and-aluminum tent structures for fast AI compute deployment, enabling hyperscale GPU clusters to go live in months rather than years."
research_area: "datacenters/design-construction"
source_urls:
  - "https://www.fastcompany.com/91369896/meta-is-using-tents-to-build-its-giant-ai-data-centers"
  - "https://www.distilled.earth/p/metas-data-center-strategy-and-the"
  - "https://www.datacenterdynamics.com/en/news/meta-brings-data-centers-in-tents-to-gallatin-tennessee/"
  - "https://cleanview.co/reports/behind-the-meter-data-centers"
  - "https://www.datacenterfrontier.com/hyperscale/article/55310441/ownership-and-power-challenges-in-metas-hyperion-and-prometheus-data-centers"
last_reviewed: 2026-06-04
stale_after_days: 90
related:
  - "datacenters/behind-meter-power/williams-companies-btm.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Meta's "rapid deployment structures" are large fabric-covered buildings — colloquially called tents — used to house GPU clusters outside traditional permanent data centers. Introduced in 2026, the approach cuts time-to-compute roughly in half compared to conventional construction and pairs with dedicated behind-the-meter power plants. Meta had deployed or permitted three tent data centers as of mid-2026: two clusters at its New Albany, Ohio campus (Prometheus) and one at Gallatin, Tennessee.

## Key Facts

- **Operator:** Meta (Facebook parent)
- **Type:** Design pattern / facility entry
- **Status:** Active — deployed at New Albany, Ohio and Gallatin, Tennessee as of June 2026
- **Structure size:** ~125,000 sq ft per tent
- **Units deployed:** Five tents permitted April–June 2026 at New Albany; one at Tennessee (total three sites)
- **Build time:** Weeks to months, vs. 2–3 years for Meta's prior permanent buildings
- **Power pairing:** 400 MW dedicated behind-the-meter gas generation (Williams Companies Socrates project)

## What It Is / How It Works

Rapid deployment structures are long rectangular buildings constructed from puncture- and water-resistant fabric stretched over an aluminum substructure, yielding a mushroom-profile pitched roof. They are not temporary shelters — each unit is approximately 125,000 square feet and houses tens of thousands of AI accelerator chips (primarily NVIDIA GPUs at ~$60,000 per unit). The structures are engineered for the controlled environment requirements of compute hardware: temperature regulation, dust exclusion, and power distribution.

The design rationale is speed. Meta's first five permanent buildings at New Albany took two to three years each to complete. Rapid deployment structures can be permitted, erected, and filled with hardware within months. Satellite imagery reviewed by Cleanview confirms all five Ohio tents were structurally complete within weeks of permitted construction start.

The structures do not replace permanent data centers — they sit adjacent to them on existing campus footprints. Meta is using them to absorb compute demand that cannot wait for permanent construction. The tradeoff is that fabric structures provide less long-term protection, carry higher maintenance risk, and are unlikely to achieve the same operational lifespan as concrete-and-steel buildings.

Because the AI accelerators inside are extremely high-value (billions of dollars across all five Ohio tents at ~$60,000/chip), the environmental and security requirements are substantial despite the temporary-looking form factor.

## Power Infrastructure

Each tent cluster requires dedicated, reliable, high-density power. Meta paired its Ohio rapid deployment structures with a purpose-built 400 MW behind-the-meter gas generation project — two 200 MW plants built by Williams Companies under a 10-year agreement (project name: Socrates). These plants operate entirely off-grid, physically disconnected from the electric power grid, and supply power directly to the adjacent data center campus.

Construction on the Socrates power plants began approximately mid-2025 and was nearing completion as of mid-2026. The Ohio facility alone is expected to exceed 1 GW of total power draw at full buildout.

Meta is applying the same tent-plus-BTM-power pattern at its Gallatin, Tennessee campus, bringing the total to at least three tent data center deployments. Williams Companies is also involved in Tennessee via its existing pipeline infrastructure and Power Innovation program.

## Notable Developments

- **2026-06:** Five Ohio tents confirmed complete via satellite imagery; Tennessee tent deployment underway; total tent count across sites reaches three — source: [Cleanview BTM Report](https://cleanview.co/reports/behind-the-meter-data-centers), [Distilled.earth](https://www.distilled.earth/p/metas-data-center-strategy-and-the)
- **2026-Apr–Jun:** City permits issued for five ~125,000 sq ft rapid deployment structures at New Albany, Ohio — source: [Fast Company](https://www.fastcompany.com/91369896/meta-is-using-tents-to-build-its-giant-ai-data-centers)
- **2026:** Mark Zuckerberg reportedly directed the shift away from traditional data center designs after competitive pressure from OpenAI Stargate and other hyperscaler AI buildouts compressed timelines
- **~2025-Q3:** Williams Companies broke ground on Socrates power plants (two × 200 MW) to serve Meta's New Albany campus under a 10-year BTM agreement — source: [Power Magazine](https://www.powermag.com/new-200-mw-gas-fired-plant-in-ohio-will-power-meta-data-center/)

## Claim Verification

### Claim: Rapid deployment structures cut time to compute in half

**Status:** Partially verified

**Supporting sources:**
- [Fast Company](https://www.fastcompany.com/91369896/meta-is-using-tents-to-build-its-giant-ai-data-centers) — reports Meta's first five permanent buildings took 2–3 years; tents complete in weeks per satellite imagery
- [Distilled.earth / Cleanview](https://www.distilled.earth/p/metas-data-center-strategy-and-the) — confirms satellite imagery showing rapid structure completion; cites city permits as corroboration

**Refuting / questioning sources:**
- No direct third-party construction timeline audit found. The "half the time" figure originates from Meta-adjacent reporting and has not been independently validated by a construction industry source.

**Summary:** The directional claim is credible given the satellite evidence, but the exact "half" figure is not independently verified.

### Claim: Billions of dollars of chips inside the tents

**Status:** Partially verified

**Supporting sources:**
- [Fast Company](https://www.fastcompany.com/91369896/meta-is-using-tents-to-build-its-giant-ai-data-centers) — cites ~$60,000 per chip; five 125,000 sq ft tents implied to house tens of thousands of units each

**Refuting / questioning sources:**
- No public inventory count confirmed. Exact chip count and total asset value are not disclosed by Meta.

**Summary:** The per-chip price figure (~$60,000 for H100/H200-class GPUs) is consistent with publicly known NVIDIA pricing; the aggregate dollar figure is plausible but unverified without a chip count.

## Key Organizations

- **Meta / Sidecat LLC** — operator and developer; Sidecat LLC is the Meta affiliate named in Ohio regulatory filings for power infrastructure
- **Williams Companies** — BTM power provider; 10-year agreement for 400 MW (Socrates project); see <!-- TODO: create entry for datacenters/behind-meter-power/williams-companies-btm.md -->
- **Cleanview** — research firm that published the BTM datacenter capacity report covering this strategy; satellite imagery analysis source

## Sources

- [Fast Company: Meta is using tents to build its giant AI data centers](https://www.fastcompany.com/91369896/meta-is-using-tents-to-build-its-giant-ai-data-centers)
- [Distilled.earth: Meta's Data Center Strategy and the Mad Max Phase of the AI Boom](https://www.distilled.earth/p/metas-data-center-strategy-and-the)
- [Data Center Dynamics: Meta brings data centers in tents to Gallatin, Tennessee](https://www.datacenterdynamics.com/en/news/meta-brings-data-centers-in-tents-to-gallatin-tennessee/)
- [Cleanview: Bypassing the Grid — Behind-the-Meter Data Centers Report](https://cleanview.co/reports/behind-the-meter-data-centers)
- [Data Center Frontier: Ownership and Power Challenges in Meta's Hyperion and Prometheus Data Centers](https://www.datacenterfrontier.com/hyperscale/article/55310441/ownership-and-power-challenges-in-metas-hyperion-and-prometheus-data-centers)
- [Power Magazine: New 200-MW Gas-Fired Plant in Ohio Will Power Meta Data Center](https://www.powermag.com/new-200-mw-gas-fired-plant-in-ohio-will-power-meta-data-center/)
