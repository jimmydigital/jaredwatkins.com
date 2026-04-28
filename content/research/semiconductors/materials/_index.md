---
title: "Materials & Chemicals"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "Supply chain analysis for semiconductor fabrication materials: silicon wafers, photoresists, specialty gases, CMP slurries, photomask blanks, and advanced packaging materials."
tags: ["semiconductors", "materials", "photoresist", "specialty-gases", "wafer", "supply-chain", "japan-concentration"]
categories: ["overview"]
research_area: "semiconductors/materials"
source_urls:
  - "https://asia.nikkei.com/Business/Business-deals/Japan-state-backed-fund-looks-to-buy-top-photoresist-maker-JSR"
  - "https://www.entegris.com/en/home/brands/cmc-materials-july-2022.html"
  - "https://www.semiconductors.org/chip-supply-chain-investments/"
last_reviewed: 2026-04-24
stale_after_days: 180
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


{{< steering >}}

**Scope:** Companies supplying raw materials, specialty chemicals, gases, and substrates consumed in wafer fabrication. Includes silicon wafers, photoresists (ArF, EUV), specialty process gases (NF3, WF6, silane), CMP slurries, photomask blanks, and advanced packaging materials (underfills, solder, adhesives). Out of scope: fabrication equipment (see fabrication-equipment/ section); wafer testing and packaging equipment.

**Japan Concentration Risk - CRITICAL:** The materials layer exhibits severe geographic concentration risk, particularly in photoresists and photomask blanks. Japan controls 70%+ of global photoresist production and near-monopoly on EUV photomask blanks (Hoya). This concentration is independent of US fab construction: even if US builds domestic TSMC Arizona and Intel Ohio fabs, photoresists and photomask blanks must come from Japan or Europe. Disruption in Japan (earthquake, export control, geopolitical event) would halt US fab production immediately. This is a strategic vulnerability that CHIPS Act fab construction does not address and requires parallel supply chain investments.

**Strategic Flags:**
- ⚑ Flag every near-monopoly or high-concentration supply (>50% in one country/company).
- ⚑ Japan concentration: photoresists, photomask blanks, CMP slurries, process chemicals.
- ⚑ Government involvement: JSR acquisition by Japan Investment Corporation (2023) signals government recognition of supply chain risk.

**Export Controls:** Some specialty gases (NF3, WF6, silane) are dual-use and subject to export controls from US and Netherlands. Document relevant control regimes.

**Key People:** For major suppliers, document executive leadership, career background, and any government/board connections.

**Review Cadence:** 180 days. Materials supply is slower-moving than fab construction, but geopolitical disruptions and M&A activity warrant semi-annual review.

{{< /steering >}}

## Strategic Vulnerability: Japan Concentration in Critical Materials

The US fab expansion initiatives (TSMC Arizona, Intel Ohio, Samsung Taylor, etc.) address physical chip manufacturing capacity but do **not** address supply chain vulnerability in semiconductor materials and chemicals.

**Critical Insight:** Even if the US builds all planned fabs to domestic manufacturing, the daily operations of these fabs depend on continuous supply of:

- **Photoresists (ArF, EUV):** ~75% global production in Japan (JSR 30%, Tokyo Ohka Kogyo 20%, Fujifilm 15%, others 10%).
- **Photomask Blanks (EUV):** Near-monopoly: Hoya Corporation (Japan), ~90% market share.
- **CMP Slurries:** Entegris (US, via CMC Materials acquisition), Cabot (via Entegris), Fujimi (Japan).
- **Specialty Gases:** Air Liquide (France), Linde (US), Air Products (US), Japan Gases (~30% combined).
- **Silicon Wafers:** Shin-Etsu Chemical (Japan, ~28% global, leading position), SUMCO (Japan, ~20%), Siltronic (Germany, ~15%).

**Risk Scenario:** An earthquake in Japan (e.g., in Kyushu where photoresist and precursor chemical plants operate) would disrupt EUV photoresist supply within days and halt US fab operations within 2–4 weeks due to material inventory depletion. No amount of domestic fab capacity matters if fabs cannot obtain inputs.

**Policy Gap:** US CHIPS Act prioritizes fab construction ($39B). Materials and chemical supply chain resilience received only ~$2B in funding and has not received equivalent policy attention.

---

## Materials Supply: Three-Tier Vendor Landscape

### Tier 1: Strategic Monopolies / Near-Monopolies (⚑ High Risk)

| Supplier | Country | Product | Market Share | Status |
|----------|---------|---------|--------------|--------|
| Shin-Etsu Chemical | Japan | Silicon wafers (300mm, 200mm) | ~28% global | ⚑ Largest wafer supplier; integrated photoresist capacity |
| Hoya Corporation | Japan | EUV photomask blanks | ~90% global | ⚑ Sole source risk for EUV mask blanks |
| JSR Corporation | Japan | ArF/EUV photoresists | ~30% advanced nodes | ⚑ Now government-backed (Japan IC Manuf. Corp.) |
| Tokyo Ohka Kogyo (TOK) | Japan | ArF/EUV photoresists | ~20% | Part of Japan photoresist oligopoly |

### Tier 2: Concentrated but Competitive (⚑ Moderate Risk)

| Supplier | Country | Product | Market Position | Notes |
|----------|---------|---------|-----------------|-------|
| SUMCO | Japan | Silicon wafers | #2 global (~20%) | Duopoly with Shin-Etsu |
| Siltronic | Germany | Silicon wafers | #3 global (~15%) | EU-based alternative |
| Merck KGaA | Germany | Electronic materials (photoresists, slurries, precursors) | Top 5 globally | AZ Electronic Materials acquisition broadened portfolio |
| Entegris | USA | CMP slurries, filtration, specialty materials | #1 CMP after CMC acquisition | US-based, controls key planarization supply |
| Air Liquide | France | Specialty gases (N2, F2, NF3, WF6) | Major regional supplier | EU/France-based; diversifies from Japan |
| Linde | USA/EU | Specialty gases (NF3, WF6, silane) | Global leader in industrial gases | US/German company |
| Fujifilm | Japan | Photoresists, materials | Top 5 photoresists | Diversified materials company |

### Tier 3: Specialty & Emerging (Fractured, Competitive)

- Photoresist developers, adhesion promoters, anti-reflective coatings.
- Underfills, solder materials, packaging substrates.
- Thermal interface materials, encapsulants.

---

## Key Company Profiles

Detailed profiles for strategically significant suppliers:

- [**JSR Corporation**](materials-jsr.md) — Photoresist leader; government acquisition (Japan IC Manuf. Corp. 2023); strategic nationalization story; ArF/EUV resist dominance
- [**Entegris**](materials-entegris.md) — US-based; CMP slurries, filtration, specialty materials; CMC Materials acquisition (2022); plays in CHIPS Act supply chain resilience
- [**Shin-Etsu Chemical**](materials-shin-etsu.md) — Japan; silicon wafer and photoresist duopoly; vertically integrated; ~28% wafer market share + 20% photoresist share

---

## Materials Supply Chain Resilience Initiatives

### Japan-Based Supply Chain Diversification

**Objective:** Reduce dependency on Japan for critical materials without displacing existing suppliers (goal is redundancy, not replacement).

**Actions Underway:**
- **Photoresists:** Merck (Germany), Samsung SDI (South Korea) expanding capacity. Asahi Kasei and other Japanese makers expanding non-Japan production.
- **Photomask Blanks:** Hoya dominates; no credible alternative supplier. Mitsubishi Materials exploring mask blank production but not at commercial scale.
- **CMP Slurries:** Entegris (US) after CMC acquisition; Fujimi (Japan) as secondary source; Cabot (legacy) now integrated into Entegris.
- **Specialty Gases:** Linde (US), Air Liquide (France), Air Products (US) provide redundancy for NF3, WF6, silane. Japan Gases remaining as supplement.

### US-Based Onshoring Initiatives

**CHIPS Act Materials Component (~$2B):**
- Entegris received grant for US filtration and CMP slurry capacity expansion.
- Air Products and Linde received loans/grants for US specialty gas production (notably for NF3, crucial for cleaning EUV masks).

**Gaps:** No credible plan to domesticate EUV photomask blank production (Hoya monopoly) or domesticate photoresist production (Japan concentrated; US photoresist industry largely dormant since 1990s).

---

## Export Controls on Materials

Some specialty materials fall under export control regimes:

| Material | Control Regime | Key Restriction | Rationale |
|----------|----------------|-----------------|-----------|
| NF3 (nitrogen trifluoride) | US Export Control | Controlled to China (not comprehensive ban but license required) | Dual-use; used in semiconductor cleaning and other industrial processes; controlled to prevent advanced chip development |
| WF6 (tungsten hexafluoride) | Limited control | Not strictly controlled, but precursor chemicals may be | Dual-use; used in tungsten deposition |
| Photoresists (EUV, advanced DUV) | US ECRA (proposed) | Not fully implemented but proposed restrictions to China | Dual-use; EUV resists specific to advanced chip nodes |
| Photomask blanks (EUV) | Dutch/US coordination | Restriction to China (Hoya, ASML coordination) | Critical input for advanced node fabs; geo-political vulnerability |

---

## Market Dynamics & Consolidation (2024–2026)

### Recent M&A Activity

- **Synopsys Acquisition of ANSYS (2024–2025):** EDA tools, not direct materials, but indicates consolidation in chip design ecosystem (related section).
- **JSR Acquisition by Japan IC Manuf. Corp. (2023–2024):** Government-backed Japanese fund acquired photoresist leader. Signals Japan government recognition of photoresist supply chain risk. Completed acquisition; JSR now private subsidiary of JIC.
- **Entegris CMC Materials Acquisition (2022):** Consolidation of CMP slurry supply. Entegris now controls ~40% of global CMP market.

### Pricing & Margin Environment

- **Wafers:** Tight supply post-COVID; pricing stable to rising for 300mm wafers. Shin-Etsu and SUMCO supply-constrained.
- **Photoresists:** Extreme concentration; price power with JSR, TOK, Fujifilm for advanced nodes. Margins compressed for commodity DUV resists.
- **CMP Slurries:** Post-Entegris-CMC consolidation, pricing and supply stable but margins controlled by Entegris.
- **Specialty Gases:** Competitive; margins declining due to new capacity (Linde, Air Liquide expansion). Long-term contracts lock in prices.

---

## Geopolitical & Climate Risks

### Japan Earthquake / Natural Disaster Risk

Japan's semiconductor materials industry clusters in specific regions (Kyushu for photoresists and precursor chemicals, Tokyo area for wafers). Earthquake or major disruption could affect 30–40% of global photoresist supply for 2–3 months.

### China Trade / Export Control Escalation

If US or Netherlands impose comprehensive restrictions on materials exports to China (similar to current ASML EUV scanner restrictions), Chinese fabs may enter into bilateral agreements with Japan/Europe for supply alternatives, creating global supply chain tension.

### Climate & Environmental

- **Water Stress:** Wafer fabrication and photoresist manufacturing are water-intensive. Japan faces water stress in certain regions. US fabs (Arizona, Ohio) will require major water infrastructure investment.
- **Carbon Pricing:** EU carbon border adjustment mechanism (CBAM) may affect European materials suppliers' pricing and competitiveness.

---

## Sourcing Strategies for US Fab Operators

For TSMC Arizona, Intel Ohio, Samsung Taylor, and other US fabs:

| Material | Strategy | Status |
|----------|----------|--------|
| Photoresists | Source from JSR (Japan), TOK (Japan), Merck (Germany) with long-term contracts | Established; multi-source contracts in place |
| Photomask Blanks | 100% from Hoya (Japan); no alternative | Accepted single-source risk; Hoya pricing negotiated |
| CMP Slurries | Entegris (US) primary, Fujimi (Japan) secondary | Established; Entegris capacity expanding for US demand |
| Silicon Wafers | TSMC Arizona uses Shin-Etsu (Japan); Intel uses Shin-Etsu/SUMCO mix | Established; wafer supply confirmed |
| Specialty Gases | Mix of Linde (US), Air Liquide (France), Air Products (US) | Established; US-based suppliers prioritized when equivalent quality available |

---

## Sources

- [Nikkei Asia - Japan State-Backed Fund JSR Acquisition](https://asia.nikkei.com/Business/Business-deals/Japan-state-backed-fund-looks-to-buy-top-photoresist-maker-JSR)
- [Entegris CMC Materials Acquisition](https://www.entegris.com/en/home/brands/cmc-materials-july-2022.html)
- [SIA Chip Supply Chain Report](https://www.semiconductors.org/chip-supply-chain-investments/)
- [Photoresist Market Analysis - Future Market Insights](https://www.futuremarketinsights.com/reports/photoresist-chemicals-market)
- [Hoya Photomask Blank Dominance Research](https://www.semiconductor-today.com/news_items/hoya-photomask-blanks)
