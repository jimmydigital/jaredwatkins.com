---
title: "Fabrication Equipment"
date: 2026-04-15
lastmod: 2026-04-15
draft: false
description: "Semiconductor wafer fabrication equipment — lithography, etch, deposition, inspection, and metrology systems enabling advanced node manufacturing."
tags: ["semiconductors", "fabrication-equipment", "lithography", "inspection", "metrology", "euv"]
categories: ["overview"]
research_area: "semiconductors/fabrication-equipment"
last_reviewed: 2026-04-15
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Semiconductor wafer fabrication equipment (WFE) encompasses all the tools used to pattern, etch, deposit, and inspect materials on silicon wafers during chip manufacturing. As nodes advance below 5nm, the equipment landscape is dominated by a small number of specialized vendors — many holding near-monopoly positions for specific process steps. Equipment procurement decisions are strategic, multi-year commitments; changing suppliers at advanced nodes is effectively impossible once a process is qualified.

The most strategically significant equipment category at the leading edge is extreme ultraviolet (EUV) lithography, which requires a tightly coupled ecosystem of complementary tools: EUV scanners (ASML), EUV photomasks (Photronics, Hoya, Toppan), EUV pellicles, and — critically — EUV mask inspection systems.

---

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Mynaric](https://mynaric.com) | Germany | Public (F-listed) | Free-space optical communications terminals for satellite and airborne networks |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [TSE:6920](https://finance.yahoo.com/quote/6920.T) | [Lasertec](https://www.lasertec.co.jp/en/) | EUV photomask and mask blank inspection systems; near-monopoly in actinic EUV inspection |
| [NASDAQ:ASML](https://finance.yahoo.com/quote/ASML) | [ASML](https://www.asml.com) | EUV and DUV lithography scanners; sole supplier of EUV systems globally |
| [NASDAQ:KLAC](https://finance.yahoo.com/quote/KLAC) | [KLA Corporation](https://www.kla.com) | Broad-based semiconductor process control, metrology, and yield management |
| [NASDAQ:AMAT](https://finance.yahoo.com/quote/AMAT) | [Applied Materials](https://www.appliedmaterials.com) | Etch, deposition (CVD/PVD/ALD), CMP, and ion implant systems; largest WFE vendor by revenue |
| [NASDAQ:LRCX](https://finance.yahoo.com/quote/LRCX) | [Lam Research](https://www.lamresearch.com) | Etch and deposition (ALD, CVD) systems; leading edge in high-aspect-ratio etch for NAND |
| [NASDAQ:ONTO](https://finance.yahoo.com/quote/ONTO) | [Onto Innovation](https://www.ontoinnovation.com) | Advanced process control, metrology, and inspection for leading-edge nodes |

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
        "title": "Fabrication Equipment",
        "symbols": [
          {"s": "TSE:6920", "d": "Lasertec"},
          {"s": "NASDAQ:ASML", "d": "ASML"},
          {"s": "NASDAQ:KLAC", "d": "KLA Corporation"},
          {"s": "NASDAQ:AMAT", "d": "Applied Materials"},
          {"s": "NASDAQ:LRCX", "d": "Lam Research"},
          {"s": "NASDAQ:ONTO", "d": "Onto Innovation"}
        ],
        "originalTitle": "Fabrication Equipment"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [TYO:7735](https://finance.yahoo.com/quote/7735.T) | [Screen Semiconductor Solutions](https://www.screen.co.jp/eng/) | Wafer cleaning, thermal processing; major WFE vendor in Japan |
| [TYO:6857](https://finance.yahoo.com/quote/6857.T) | [Advantest](https://www.advantest.com) | Semiconductor test systems (ATE); dominant in memory and SoC test |

---

## Supply Chain Position

| Layer | Key Inputs / Outputs | Key Companies | Concentration Risk |
|-------|---------------------|--------------|-------------------|
| **Raw silicon wafers** | Polished silicon substrates (300mm, 200mm) | Shin-Etsu Chemical, SUMCO, Siltronic, SK Siltron | Japan/Korea/Germany dominant |
| **Photomasks** | Patterned quartz reticles used in lithography | Photronics, Hoya, Toppan, DNP | Mask blanks: HOYA near-monopoly for EUV |
| **Photoresists** | Light-sensitive chemicals for pattern transfer | JSR, TOK, Shin-Etsu, Merck KGaA | Japan: >90% of advanced EUV resist supply |
| **Lithography** | EUV and DUV scanners patterning wafer layers | ASML (EUV sole supplier), Nikon, Canon | ASML holds 100% of EUV scanner market |
| **Inspection & metrology** | Defect detection, pattern measurement, overlay | Lasertec (EUV mask inspection monopoly), KLA, Onto | Lasertec: ~90%+ EUV mask inspection share |
| **Etch & deposition** | Material removal and thin-film layer formation | Lam Research, Applied Materials, Tokyo Electron | US and Japan dominate |
| **CMP** | Chemical mechanical planarization (surface flattening) | Applied Materials, Ebara, Entegris | US/Japan dominant; slurries: Cabot, CMC |
| **Assembly & packaging** | Dicing, bonding, advanced packaging (HBM, CoWoS) | ASE Group, Amkor, TSMC CoWoS | Advanced packaging: TSMC near-monopoly for CoWoS |

---

## Entries

- [ASML]({{< relref "asml.md" >}}) — ⚑ Sole supplier of EUV lithography systems globally; TWINSCAN EXE:5200B High-NA leadership; CEO Christophe Fouquet; export controls; Euronext: ASML
- [Applied Materials]({{< relref "applied-materials.md" >}}) — Largest WFE vendor by revenue (~$27–30B); etch, deposition (CVD/PVD/ALD), CMP, ion implant; CEO Gary Dickerson; NASDAQ: AMAT
- [Tokyo Electron]({{< relref "tokyo-electron.md" >}}) — Third-largest WFE vendor; etch, CVD, thermal, track systems; Japan-based; strong fab relationships; Tokyo Stock Exchange: 8035
- [Lasertec]({{< relref "/research/semiconductors/fabrication-equipment/lasertec" >}}) — EUV photomask and mask blank inspection; near-monopoly in actinic EUV inspection; Tokyo Stock Exchange: 6920
