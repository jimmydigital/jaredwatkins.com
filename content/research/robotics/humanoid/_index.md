---
title: "Humanoid Robots"
date: 2026-06-19
lastmod: 2026-06-19
draft: false
description: "Overview of the humanoid robot sector: US and non-US companies, autonomy claims, deployment reality, and the specialized vs. humanoid debate."
tags: ["humanoid", "robotics", "industrial", "autonomy"]
categories: ["overview"]
research_area: "robotics/humanoid"
last_reviewed: 2026-06-19
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

{{<steering>}}

## Humanoid Robots Subsection — Steering Instructions

This subsection tracks companies building full-body bipedal humanoid robots. Editorial priority per the parent robotics section applies: component and subsystem suppliers are interesting; platform OEMs provide market context.

**Key editorial posture for this section:**
- Autonomy claims require extra skepticism. The gap between demo performance and real-world autonomous operation is large and poorly disclosed. Every autonomy claim must be accompanied by a Claim Verification section.
- Teleoperation is widespread in demos and early deployments. Note it explicitly. The standard "human-shaped data collection platform" critique is a legitimate research finding, not editorializing.
- Deployment figures must distinguish: units shipped / units in productive commercial operation / units in internal R&D / units under teleoperation.
- Timeline claims (commercial scale by year X, millions of units by year Y) have a poor track record. Document claims with date and source; do not treat them as facts.
- The specialized robot alternative is a genuine engineering trade-off, not a strawman. Document it fairly.

**Chinese-owned companies:** Apply the `chinese-owned: true` frontmatter flag, 🇨🇳 marker in tables, and elevated verification standard per the parent research section rules.

**Review cadence:** 90 days — this is a fast-moving area with frequent funding rounds, deployment updates, and demo cycles.

{{</steering>}}

## Overview

The humanoid robot sector has attracted enormous investment since 2022, driven by the hypothesis that a general-purpose robot in human form can operate in existing human-designed environments without infrastructure modification. As of mid-2026, the gap between this hypothesis and demonstrated capability remains large — most commercial deployments are narrow in task scope, and the line between autonomous operation and teleoperation-assisted data collection is rarely disclosed clearly by companies.

Entries are split into [US Companies]({{< relref "us-companies/_index.md" >}}) and [Non-US Companies]({{< relref "non-us-companies/_index.md" >}}). A standalone [Overview & Critical Analysis]({{< relref "overview-and-critique.md" >}}) entry addresses the autonomy verification problem, the specialized vs. humanoid debate, and investor sentiment.

## Companies

### US — Startups & Growth-Stage

| Company | HQ | Stage | Robot |
|---------|-----|-------|-------|
| [Figure AI](https://figure.ai) | Sunnyvale, CA | Growth / Pre-IPO | Figure 03 — general industrial |
| [Agility Robotics](https://agilityrobotics.com) | Corvallis, OR | Growth (Amazon-backed) | Digit — logistics tote handling |
| [Apptronik](https://apptronik.com) | Austin, TX | Series A ($935M raised) | Apollo — industrial |
| [1X Technologies](https://1x.tech) | Moss, Norway (US ops) | Series B | NEO — consumer/household |
| [Sanctuary AI](https://sanctuary.ai) | Vancouver, BC | Series B | Phoenix — retail/commercial |
| [Robust AI](https://robust.ai) | San Jose, CA | Series B | Carter — logistics AMR (not humanoid) |

### US — Public / Late Stage

| Ticker | Company | Notes |
|--------|---------|-------|
| [TSLA](https://finance.yahoo.com/quote/TSLA) | [Tesla](https://tesla.com) | Optimus — internal R&D / learning mode, no external customers as of Q1 2026 |
| [BDNSA](https://finance.yahoo.com/quote/BDNSA) | [Boston Dynamics](https://bostondynamics.com) | Atlas — Hyundai automotive pilots; primarily R&D stage |

### Non-US Companies

See [Non-US Companies]({{< relref "non-us-companies/_index.md" >}}) for full table. China dominates unit shipments (~90% of 2025 global volume).

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
    "colorTheme": "light",
    "dateRange": "12M",
    "showChart": true,
    "locale": "en",
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "500",
    "tabs": [
      {
        "title": "Humanoid Robots",
        "symbols": [
          {"s": "NASDAQ:TSLA", "d": "Tesla (Optimus)"},
          {"s": "NYSE:HD", "d": "Boston Dynamics (Hyundai — HD)"}
        ],
        "originalTitle": "Humanoid Robots"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

## Key Themes

- **Autonomy gap:** Most robots in 2025–2026 operate under partial or full teleoperation for non-trivial tasks. True closed-loop autonomy for novel physical tasks is a research problem, not a product reality.
- **China's manufacturing lead:** Chinese firms shipped ~90% of global humanoid units in 2025. Price competition is extreme — Unitree R1 at $5,900 vs. US competitors at $100K+.
- **Specialized robot alternative:** For most defined industrial tasks, purpose-built robots (arms, AMRs, conveyors) outperform humanoids on cost, speed, and reliability. The humanoid value proposition is in unstructured, multi-task environments — a much harder problem than the current demos suggest.
- **Battery life bottleneck:** Agility Digit operates ~90 minutes before recharge. An 8-hour factory shift requires either swappable packs or docking infrastructure that undermines the "drop in anywhere" premise.
