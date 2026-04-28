---
title: "Lasertec"
date: 2026-04-15
lastmod: 2026-04-15
draft: false
description: "Yokohama-based semiconductor inspection equipment maker; founded 1960; holds a near-monopoly in EUV photomask and mask blank inspection systems; sole developer of actinic (13.5nm wavelength) inspection technology essential for 7nm-and-below chip manufacturing."
tags: ["semiconductors", "fabrication-equipment", "inspection", "metrology", "euv", "photomask", "japan", "monopoly", "export-controls"]
categories: ["company"]
research_area: "semiconductors/fabrication-equipment"
source_urls:
  - "https://www.lasertec.co.jp/en/"
  - "https://www.lasertec.co.jp/en/ir/individuals/euv.html"
  - "https://finance.yahoo.com/quote/6920.T"
  - "https://fortune.com/asia/2024/03/21/lasertec-chip-stock-asia-future-japan-semiconductors-testing-shares/"
  - "https://semiconductorinsight.com/blog/next-gen-euv-photomask-inspection-tools-reshape-chip-manufacturing-amid-2-28-billion-market-boom-by-2032/"
last_reviewed: 2026-04-15
stale_after_days: 90
related:
  - "semiconductors/fabrication-equipment/_index.md"
  - "semiconductors/_index.md"
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Summary

Lasertec Corporation is a Yokohama, Japan-based manufacturer of inspection and measurement equipment for the semiconductor industry, founded in 1960 and listed on the Tokyo Stock Exchange (TSE: 6920). The company holds a near-monopoly position — estimated at 90% or higher global market share — in EUV (extreme ultraviolet) photomask inspection, including the world's only commercially available actinic inspection system, which uses the same 13.5nm wavelength as EUV lithography itself to detect defects at resolutions impossible with conventional optical tools. This technological position makes Lasertec a critical single point of dependency in the EUV supply chain: without qualified mask inspection, chipmakers cannot verify the photomasks required for manufacturing chips at 7nm and below — the nodes used for advanced AI processors, mobile SoCs, and HPC chips.

Lasertec's financial performance reflects this monopoly position. The company reported FY2025 (ended June 2025) consolidated net sales of 251.5 billion yen (+17.8% YoY) with operating income of 122.8 billion yen (+51.0% YoY) and a net profit margin of approximately 33.7%. Its stock rose approximately 1,800% between 2019 and 2024, driven by the EUV adoption wave and AI chip demand surge. The company is subject to Japanese export control regulations enacted in July 2023 that restrict shipment of advanced semiconductor equipment — including Lasertec's inspection systems — to certain geographies, most significantly China.

**⚑ Supply chain bottleneck:** Lasertec is the only qualified supplier of actinic EUV photomask inspection systems. No alternative supplier exists. TSMC, Samsung, and Intel's EUV production lines depend on Lasertec equipment to verify mask quality before wafer exposure.

## Key Facts

- **Founded:** 1960 (as Tokyo ITV Laboratory; incorporated 1962 as NJS Corporation; rebranded Lasertec 1986)
- **HQ:** Yokohama, Kanagawa, Japan
- **Type:** Public — Tokyo Stock Exchange (TSE: 6920); OTC US trading as LSRCF / LSRCY
- **Market cap (April 2026):** ~3.36 trillion JPY (~$22B USD)
- **Core technology:** Actinic EUV photomask inspection (13.5nm wavelength); confocal and DUV optics; interferometry
- **Key product lines:** ACTIS (actinic pattern mask inspection), ABICS (actinic blank inspection and cleaning), PELMIS (pellicle inspection)
- **Key differentiator:** Only commercially available actinic EUV inspection — inspects masks using the actual EUV wavelength, enabling detection of defects invisible to DUV-based tools
- **Market share:** ~90%+ in EUV mask inspection; near-100% for actinic inspection at 5nm and below
- **Development stage:** Mature, market-leading product line; active product extension into High-NA EUV inspection
- **Business model:** Fabless (outsources manufacturing); revenue from equipment sales plus service contracts
- **Nikkei 225:** Added to index in 2023
- **FY2025 revenue:** 251.5 billion yen; operating margin ~48.8%; net margin ~33.7%
- **CEO (as of July 2024):** Tetsuya Sendoda

## What It Is / How It Works

**The photomask problem in EUV lithography:** EUV lithography — the process used to pattern chip features at 7nm and below — uses 13.5nm wavelength light (versus 193nm for conventional deep ultraviolet). At these scales, even sub-nanometer defects in the photomask (the patterned quartz reticle used to transfer circuit designs onto silicon wafers) can cause catastrophic yield losses. A single defective mask, if undetected, will print bad patterns across thousands of wafers before the problem is identified — destroying hundreds of millions of dollars in work-in-process material.

**Why conventional inspection fails:** Traditional photomask inspection tools use DUV light (typically 193nm or 257nm wavelengths) to scan masks for defects. These wavelengths are too long to reliably detect the smallest defect types relevant to EUV masks, which must be inspected at or near the resolution limit of the printing wavelength itself. At EUV nodes, a DUV-based tool may miss defects that are nonetheless printable. The industry term for using the same wavelength as the printing tool is "actinic" inspection — and until Lasertec's systems, no commercial actinic EUV inspection capability existed.

**Lasertec's actinic approach:** Lasertec's ACTIS series inspection systems use 13.5nm EUV illumination to scan photomasks, providing inspection sensitivity matched to the actual printing wavelength. This allows the system to identify defects that would be printed as circuit errors, while ignoring sub-critical defects that the scanner would not resolve. Additionally, Lasertec's ABICS series inspects EUV mask blanks (the raw substrates before circuit patterns are applied) for buried multilayer defects — a prerequisite for maskmakers receiving blanks from suppliers like HOYA before committing them to expensive patterning steps.

**Pellicle inspection:** EUV pellicles — ultra-thin membranes stretched across photomasks to protect them from particle contamination during scanner exposure — add a new inspection challenge. Lasertec's PELMIS series inspects pellicles for particle contamination from both front and back sides, with classification of defect type and location. This product line, launched in December 2024, addresses a critical yield control step as EUV pellicle adoption expands.

**High-NA EUV extension:** The next generation of EUV lithography (ASML's High-NA EUV, EXE:5000 series) requires new photomask formats (8% transmission) and tighter defect specifications. Lasertec has confirmed active development of ACTIS A200HiT systems (launched October 2025) specifically designed to support High-NA EUV optics, extending the product roadmap through the late 2020s.

**Technology foundation:** Lasertec's systems integrate applied optics, confocal optics (enabling depth-resolved inspection), DUV and EUV optics, and interferometry. The company's long history (since 1960) in precision optical systems underpins its technical competence in handling EUV-range optics, which require ultra-high vacuum environments and specialized reflective (rather than transmissive) optical components.

## Notable Developments

- **2025-10:** Launched ACTIS A200HiT series — enhanced photomask and mask blank inspection specifically supporting High-NA EUV lithography (next-generation ASML EXE:5000 scanners)
- **2025-07:** Released PELMIS EPM200, supporting Carbon Nanotube (CNT) pellicles — the leading pellicle material candidate for EUV production
- **2025-05:** Released ECCS B520 (Electro-Chemical Reaction Visualizing Confocal System) — inspection tool for semiconductor process chemistry monitoring
- **2025-04:** Received Intel EPIC Supplier Award for outstanding supply chain performance
- **2025-01:** Released OPTELICS IR infrared confocal microscope
- **2024-12:** Released ABICS E320 — next-generation actinic EUV mask blank inspection system with high-magnification Schwarzschild objective
- **2024-12:** Released PELMIS Series — EUV pellicle particle inspection system with front/back side defect classification
- **2024-07:** CEO transition — Tetsuya Sendoda appointed President and CEO (succeeding prior leadership)
- **2024:** FY2024 (ended June 2024) net sales 213.5 billion yen (+39.7% YoY); semiconductor products 181.7 billion yen
- **2023:** Added to Nikkei 225 index, reflecting strategic importance to Japan's technology sector
- **2023-07:** Japan METI export controls take effect covering 23 categories of advanced semiconductor equipment, including Lasertec's inspection systems; all exports to restricted countries now require METI license
- **2022:** Announced Lasertec Innovation Park development in Yokohama — new R&D center to support product development acceleration
- **2021:** Published mid-term business plan targeting 6–18 month lead time reduction and maximum sales growth through 2030
- **2019:** Launched world's first commercial actinic EUV photomask inspection system (ACTIS series), establishing monopoly position in the segment

## Key People

### Tetsuya Sendoda — President & CEO
- **LinkedIn:** Search "Tetsuya Sendoda Lasertec"
- **Born:** April 26, 1977
- **Joined Lasertec:** January 2008
- **Career at Lasertec:**
  - General Manager, Technology Department 2 (June 2020)
  - Sales Officer (July 2022)
  - Executive Officer (September 2022)
  - Chief Sales Officer (2022–2024)
  - President and CEO (July 1, 2024)
- **Background:** Career Lasertec executive with background in technology and sales leadership; appointed CEO in a planned succession in 2024. Educational background not publicly detailed.
- **Source:** [Lasertec officer profile](https://www.lasertec.co.jp/en/company/officer/sendoda.html)

<!-- TODO: find LinkedIn profiles and additional biography for other Lasertec board members; Lasertec's public IR does not extensively detail individual biographies beyond the CEO -->

### People — Last Reviewed: 2026-04-15

## Supply Chain Position

| Layer | Detail |
|-------|--------|
| **EUV mask blanks** | Reflective multi-layer substrates (Mo/Si multilayer on ultra-low expansion glass); HOYA is near-monopoly supplier; Lasertec's ABICS systems inspect blanks upon receipt at maskmakers |
| **Photomask fabrication** | Maskmakers (Photronics, Hoya, Toppan, DNP) pattern EUV masks; Lasertec's ACTIS systems inspect finished masks before shipment to fabs |
| **Pellicles** | Ultra-thin EUV pellicles (CNT, polysilicon); Lasertec's PELMIS systems inspect for particle contamination |
| **EUV scanners** | ASML EUV (NXE/NXi/EXE series) exposes wafers using verified masks; Lasertec inspection is prerequisite to scanner use |
| **Chipmaker fabs** | TSMC, Samsung, Intel purchase Lasertec systems directly or receive inspection services from maskmakers using them |
| **End markets** | AI accelerators (NVIDIA, AMD, Google TPU), mobile SoCs (Apple A-series, Qualcomm), HPC — all require EUV-manufactured chips |

**⚑ Sole-source dependency:** No qualified alternative to Lasertec exists for actinic EUV mask inspection. Maskmakers and chipmakers cannot qualify EUV masks without it.

**⚑ Export control exposure:** Japan's July 2023 METI regulations require export licenses for Lasertec equipment sold to non-Wassenaar Arrangement countries. The 42 Wassenaar member countries (US, South Korea, Taiwan, EU) receive streamlined licensing. China — historically a growing market for Lasertec — faces significant restriction. The US government's FDPR (Foreign Direct Product Rule) provides an additional lever: equipment incorporating US-origin technology (software, process equipment used in Lasertec's own supply chain) can potentially be controlled by Washington regardless of where it is manufactured.

**⚑ Japan's strategic position:** Lasertec, along with Tokyo Electron and Shin-Etsu, places Japan as an irreplaceable node in the semiconductor equipment supply chain. This creates both leverage (Japan can restrict exports as part of coordinated US-Japan-Netherlands policy) and vulnerability (any disruption to Japan's industrial base affects global advanced node production).

## Research Relevance

Lasertec is the archetype of a hidden monopolist in the semiconductor supply chain — a company with essentially no consumer brand recognition that holds decisive chokehold over the most advanced chip manufacturing processes on the planet. Understanding Lasertec is relevant for several reasons:

**EUV ecosystem completeness:** The EUV lithography ecosystem is often discussed exclusively in terms of ASML, but the mask supply chain — masks, blanks, resists, inspection — is equally critical. Lasertec occupies the inspection bottleneck in that chain. Without Lasertec, EUV lithography cannot function at scale.

**AI chip production dependency:** Every advanced AI accelerator — NVIDIA H100/H200/B200, AMD MI300X, Google TPU — is manufactured on TSMC's 3nm or 5nm node, both of which use EUV. Lasertec's inspection systems are therefore a dependency for the entire AI hardware supply chain.

**Geopolitical leverage mapping:** The US-Japan-Netherlands semiconductor export control regime (US BIS restrictions, Dutch ASML export controls, Japanese METI regulations) creates a tripartite chokepoint on advanced chip manufacturing. Lasertec is the Japanese contribution to the inspection segment of that chokepoint. Tracking Lasertec's export policy evolution and China exposure provides a leading indicator for how tightly the control regime is being enforced.

**Near-monopoly valuation dynamics:** Lasertec's ~90% gross margins and 45%+ operating margins reflect pricing power from monopoly position in a market where customers have no alternatives. This makes it an interesting case study in how technological moats in deep supply chain positions translate to financial outcomes — and how those moats can be disrupted (primarily by the entrance of a second qualified inspection system supplier, which has not materialized despite years of industry need).

**High-NA EUV transition:** As the industry migrates to High-NA EUV (ASML EXE:5000) through 2026–2030, Lasertec must extend its inspection capability to new mask formats and tighter defect specifications. The company's ability to maintain monopoly across this transition — or the potential for a competitor to enter if Lasertec stumbles — is a key strategic question for the next five years.

## Claim Verification

### Claim: "Lasertec holds ~90% global market share in EUV photomask inspection"
**Status:** Partially verified

**Supporting sources:**
- [Oreate AI — Lasertec monopoly analysis](https://www.oreateai.com/blog/lasertec-the-global-monopoly-in-euv-photomask-inspection/981a881b59881e5650513914c59b6694) — describes Lasertec as "the global monopoly" with dominant share in EUV mask inspection
- [MatrixBCG competitive landscape](https://matrixbcg.com/blogs/competitors/lasertec) — lists competitors (KLA, Onto Innovation, Camtek) but confirms Lasertec's leadership in the EUV-specific segment
- Industry analyst consensus (Semiconductor Insight, EUV market reports) regularly describes Lasertec as the dominant or sole supplier in actinic EUV inspection

**Refuting / questioning sources:**
- KLA Corporation serves the broader photomask inspection market (DUV and some EUV segments) and may hold share in non-actinic EUV inspection — the 90% figure likely refers specifically to actinic EUV, not all mask inspection tools
- No independent audited market share data is publicly available; figures are from analyst estimates and secondary sources

**Summary:** The near-monopoly claim is directionally accurate for actinic EUV mask inspection; KLA and others compete in adjacent DUV and non-actinic EUV inspection segments but no qualified competitor exists for Lasertec's core actinic inspection capability.

---

### Claim: "Lasertec launched the world's first actinic EUV photomask inspection system in 2019"
**Status:** Verified

**Supporting sources:**
- [Lasertec EUV IR page](https://www.lasertec.co.jp/en/ir/individuals/euv.html) — company confirms first actinic inspection system launch
- [Semiconductor Insight — EUV inspection market](https://semiconductorinsight.com/blog/next-gen-euv-photomask-inspection-tools-reshape-chip-manufacturing-amid-2-28-billion-market-boom-by-2032/) — confirms Lasertec's first-mover position and 2019 timeline
- Fortune Asia reporting (March 2024) confirms the product launch timeline and commercial significance

**Refuting / questioning sources:**
- None found; no competing vendor has publicly claimed a prior or simultaneous actinic EUV inspection system launch

**Summary:** Verified — Lasertec introduced the first commercial actinic EUV photomask inspection system in 2019. This was a genuine industry first with no documented competing commercial product at that time.

---

### Claim: "Japan's July 2023 METI export controls cover Lasertec's inspection systems"
**Status:** Verified

**Supporting sources:**
- [TechWireAsia — Japan chip export restrictions (2023)](https://techwireasia.com/2023/03/japan-joins-the-us-by-restricting-chipmaking-gear-exports-to-china/) — confirms Japan's METI regulations covering 23 categories of advanced semiconductor manufacturing equipment effective July 23, 2023
- [AJOT — US-Japan semiconductor leverage](https://www.ajot.com/news/us-gets-new-levers-from-japan-to-curb-chinaas-chip-ambitions) — confirms scope of controls and Wassenaar streamlined licensing pathway
- [South China Morning Post — Japan export controls](https://www.scmp.com/news/asia/east-asia/article/3215505/japan-restricts-chipmaking-equipment-exports-as-us-seeks-to-contain-china) — confirms China-focused impact of restrictions

**Refuting / questioning sources:**
- The specific enumeration of which Lasertec product lines fall under which control category is not publicly detailed at the item level in English-language sources; the broad coverage of "advanced inspection systems" is confirmed but SKU-level mapping requires METI classification review
- Lasertec has not published detailed statements on specific product export control classifications

**Summary:** Verified that Japan's 2023 METI regulations cover Lasertec's category of equipment (advanced semiconductor inspection systems). The practical effect is that Lasertec requires METI export licenses for shipments to non-Wassenaar countries, most importantly China.

## Sources

- [Lasertec Corporate Site](https://www.lasertec.co.jp/en/) — official corporate and IR information
- [Lasertec EUV IR Page](https://www.lasertec.co.jp/en/ir/individuals/euv.html) — EUV product line overview and technology background
- [Lasertec Officer Profiles](https://www.lasertec.co.jp/en/company/officer/sendoda.html) — executive bios
- [TSE: 6920 on Yahoo Finance](https://finance.yahoo.com/quote/6920.T) — stock data and financials
- [Fortune Asia — Lasertec profile (March 2024)](https://fortune.com/asia/2024/03/21/lasertec-chip-stock-asia-future-japan-semiconductors-testing-shares/) — business overview and AI boom context
- [Semiconductor Insight — EUV inspection market and High-NA](https://semiconductorinsight.com/blog/next-gen-euv-photomask-inspection-tools-reshape-chip-manufacturing-amid-2-28-billion-market-boom-by-2032/) — market sizing and product pipeline
- [Semiconductor Insight — ABICS E320 launch (Dec 2024)](https://semiconductorinsight.com/blog/lasertec-launches-abics-e320-enhancing-actinic-euv-mask-blank-defect-detection/) — product announcement details
- [Oreate AI — Lasertec monopoly analysis](https://www.oreateai.com/blog/lasertec-the-global-monopoly-in-euv-photomask-inspection/981a881b59881e5650513914c59b6694) — competitive positioning analysis
- [MatrixBCG — Lasertec competitive landscape](https://matrixbcg.com/blogs/competitors/lasertec) — competitor mapping
- [TechWireAsia — Japan export restrictions (2023)](https://techwireasia.com/2023/03/japan-joins-the-us-by-restricting-chipmaking-gear-exports-to-china/) — METI export control details
- [AJOT — US-Japan semiconductor leverage](https://www.ajot.com/news/us-gets-new-levers-from-japan-to-curb-chinaas-chip-ambitions) — geopolitical context
- [Seeking Alpha — FY2026 Q1 earnings (2025)](https://seekingalpha.com/article/4839744-lasertec-corporation-2026-q1-results-earnings-call-presentation) — quarterly financials
- [Bloomberg — Tetsuya Sendoda profile](https://www.bloomberg.com/profile/person/23049056) — CEO background
- [Wikipedia — Lasertec Corporation](https://en.wikipedia.org/wiki/Lasertec_Corporation) — company history and founding timeline
