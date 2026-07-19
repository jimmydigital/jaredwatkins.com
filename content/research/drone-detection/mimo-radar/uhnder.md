---
title: "Uhnder"
date: 2026-07-17
lastmod: 2026-07-17
draft: false
description: "Austin, Texas maker of digital Code Modulation MIMO radar-on-chip (S-series, up to 96 MIMO channels); automotive ADAS-focused today, included here as the enabling low-cost 4D imaging radar chip technology relevant to future small/cheap counter-drone sensors rather than a current C-UAS product."
research_area: "drone-detection/mimo-radar"
source_urls:
  - "https://www.uhnder.com/"
  - "https://www.globenewswire.com/news-release/2024/04/23/2867698/0/en/Uhnder-Releases-New-4D-Digital-Imaging-Radar-Chip-to-Bolster-ADAS-Applications-for-Mass-Market-Automobiles.html"
  - "https://www.globenewswire.com/news-release/2024/02/21/2832691/0/en/Uhnder-raises-50-million-in-Series-D-funding-to-accelerate-growth.html"
  - "https://www.prnewswire.com/news-releases/uhnder-strengthens-executive-leadership-team-with-coo-and-cfo-appointments-301278390.html"
  - "https://www.microwavejournal.com/articles/41844-uhnder-releases-new-4d-digital-imaging-radar-chip"
  - "https://tdk-ventures.com/uhnder/"
  - "https://www.tributearchive.com/obituaries/24392571/curtis-alfred-davis"
  - "https://www.legacy.com/us/obituaries/stltoday/name/curtis-davis-obituary?id=52263896"
  - "https://theabj.com.au/2026/03/20/morse-micro-appoints-joe-bedewi-cfo/"
last_reviewed: 2026-07-17
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Uhnder (Austin, Texas; founded 2015) makes what it markets as the first fully digital automotive radar, using Digital Code Modulation (DCM) — a PMCW (phase-modulated continuous-wave)-based digital waveform — rather than traditional analog FMCW (frequency-modulated continuous wave). Its S81 chip is a single-chip, 77 GHz, 4D imaging Radar-on-Chip (RoC) supporting up to 96 MIMO channels, automotive-qualified for safety applications like automatic emergency braking, lane-keep assist, adaptive cruise control, and blind-spot detection, with Magna as its first production customer (Icon Radar, unveiled at the 2018 Detroit Auto Show). Like [Vayyar Imaging]({{< relref "vayyar-imaging.md" >}}), Uhnder has no confirmed drone-detection or counter-UAS product; it is included in this subtopic because digital MIMO radar-on-chip technology at automotive price points and power budgets is a plausible enabling technology for future low-cost, small-footprint drone-detection sensors — the SWaP-C direction the whole subtopic is trending toward. Note also that Uhnder's leadership has changed substantially since founding, including the 2023 death of cofounder/CTO Curtis Davis and the 2026 departure of its CFO — see Key People and Limitations below for what remains unconfirmed.

## Key Facts

- **HQ:** Austin, Texas, USA
- **Founded:** 2015, by Dr. Manju Hegde and Curtis Davis
- **Type:** Company — digital radar-on-chip semiconductor maker
- **Core technology:** Digital Code Modulation (DCM) — a fully digital, PMCW-based radar waveform, as opposed to conventional analog FMCW radar
- **Flagship chip:** S81 — 77 GHz, single-chip 4D Imaging Radar-on-Chip; supports up to 96 MIMO channels (reported elsewhere, not confirmed via a primary source in this review, as a 12-transmit/8-receive antenna configuration); detects/tracks objects with High Contrast Resolution (HCR) at 50+ fps
- **Certified applications:** Automotive AEB, lane-keep assist, adaptive cruise control, blind-spot detection; company materials also reference industrial and defense-sector customer engagements without naming specific programs
- **First production customer:** Magna, whose Icon Radar (built on Uhnder's digital RoC) was unveiled at the 2018 Detroit Auto Show
- **Shipments (company-stated):** More than 200,000 digital radar chips shipped to customers as of February 2024
- **Funding:** $50 million Series D closed February 21, 2024, led by ACME Capital, with participation from Magna, Qualcomm Ventures, El Camino Capital, Monta Vista Capital, Sagitta Ventures, and HT Capital; earlier rounds included a Series C (closed 2020) and investment from TDK Ventures; total funding to date reported as ~$145 million by third-party aggregators (not confirmed via a primary source in this review)

## How It Works

Uhnder's Digital Code Modulation approach replaces the analog FMCW chirp used by most automotive and security radar with a fully digital, phase/code-modulated waveform, which the company says reduces mutual interference between multiple radars operating in the same environment (a growing problem as radar density increases) and improves resistance to spoofing, since each transmit channel's code is digitally distinguishable and difficult for an external actor to replicate. Combined with support for up to 96 MIMO channels on a single chip — synthesizing a large virtual array from a smaller physical transmit/receive antenna count, in the manner described in the [subtopic overview]({{< relref "_index.md" >}}) — this enables 4D imaging (range, azimuth, elevation, velocity) at a cost and power profile suited to mass-market vehicles rather than only premium or defense-grade systems. That is the same cost/power trajectory that would need to be reached for MIMO radar to become a truly ubiquitous, cheap sensor layer for drone detection, rather than the current specialized (and comparatively expensive) systems from vendors like [Advanced Protection Systems]({{< relref "advanced-protection-systems.md" >}}) or [RADA/Leonardo DRS]({{< relref "rada-leonardo-drs.md" >}}).

## Notable Developments

- **2026-03 (reported):** Joe Bedewi, Uhnder's CFO since 2021, is appointed Chief Financial Officer of Morse Micro; no Uhnder press release announcing a replacement CFO was found in this review
- **2024-04-23:** Uhnder announces general commercial availability of the S81 single-chip 4D digital imaging radar (up to 96 MIMO channels, DCM waveform, automotive-qualified), targeted at mass-market ADAS
- **2024-02-21:** Uhnder closes a $50 million Series D round led by ACME Capital, with Magna, Qualcomm Ventures, El Camino Capital, Monta Vista Capital, Sagitta Ventures, and HT Capital participating; company states it has shipped over 200,000 radar chips to date with "dozens of customer engagements in the automotive, industrial and defense sectors"
- **2023-06-14:** Cofounder and Chief Technology Officer Curtis Davis dies of glioblastoma at age 54, roughly a year after diagnosis
- **2021-04-28:** Uhnder appoints Sandeep Chennakeshu as Chief Operating Officer and Joe Bedewi as Chief Financial Officer, both brought on to scale operations and financial rigor as the company grew
- **2018:** Magna unveils Icon Radar at the Detroit Auto Show — Uhnder's technology in its first production automotive customer deployment
- **2015:** Uhnder founded in Austin, Texas by Manju Hegde and Curtis Davis

## Key People

- **Dr. Manju Hegde** — CEO and Cofounder (since 2015). LinkedIn: [manju-hegde-80b7141b](https://www.linkedin.com/in/manju-hegde-80b7141b/). Previously cofounded and served as CEO of Ageia Technologies (2002–2008, acquired by Nvidia in 2008) and cofounded Celox Networks (1999–2002); also held roles as Corporate Vice President at AMD and Vice President at Nvidia. Confirmed as CEO via Uhnder's own April 2024 press release (quoted directly); note that at least one third-party aggregator (CorporationWiki) labels him "Previous CEO" without a corroborating primary source found in this review — treat any claim of a post-2024 CEO transition as unconfirmed pending a direct Uhnder announcement.
- **Curtis Davis** — Cofounder and Chief Technology Officer (2015 until his death on June 14, 2023, from glioblastoma, diagnosed roughly a year earlier). LinkedIn profile has been memorialized: [curtis-davis-95765](https://www.linkedin.com/in/curtis-davis-95765/). Previously COO of MulticoreWare, VP of PhysX engineering at Nvidia, and — notably — cofounder and President of Ageia Technologies and cofounder/principal VLSI architect of Celox Networks, the same two prior companies as Hegde. **⚑ Shared background:** Hegde and Davis were a repeat cofounding partnership across three consecutive companies (Celox Networks → Ageia Technologies → Uhnder), not a one-time team-up. Uhnder's own public team page, fetched during this review, still lists Davis as active CTO/Cofounder with no note of his 2023 death — a sign the company website is not being actively maintained and should not be treated as current without independent cross-checking.
- **Sandeep Chennakeshu** — Chief Operating Officer (since April 2021). LinkedIn: [sandeep-chennakeshu-351187111](https://www.linkedin.com/in/sandeep-chennakeshu-351187111/). Previously EVP at AMD, President of BlackBerry Technology Solutions, SVP of Freescale Semiconductor, President of Ericsson Mobile Platforms, and CTO of Ericsson and Sony Ericsson; IEEE Fellow and named inventor on 180 granted patents; holds a Doctorate in electrical engineering from Southern Methodist University. **⚑ Overlap:** Chennakeshu (EVP, AMD) and Hegde (Corporate VP, AMD) both held executive positions at AMD prior to Uhnder — exact tenure overlap was not confirmed in this review.
- **Joe Bedewi** — Chief Financial Officer from April 2021 until his departure in March 2026 to become CFO of Morse Micro (per independent Australian trade press). LinkedIn: [joe-bedewi-3148584](https://www.linkedin.com/in/joe-bedewi-3148584/). Previously CFO of Altium (grew market cap to over $3B during his tenure) and CFO of Lattice Semiconductor (led two acquisitions, Silicon Image in 2015 and Silicon Blue in 2012), plus 15+ years at Intel in finance/manufacturing roles; BS from Arizona State University. **No Uhnder-published announcement of his successor was found in this review — current CFO status is unconfirmed.**

### People — Last Reviewed: 2026-07-17

## Claim Verification

### Claim: S81 supports "up to 96 MIMO channels," 4D digital imaging radar-on-chip using Digital Code Modulation
**Status:** Verified.
**Supporting sources:** [Uhnder's own GlobeNewswire press release](https://www.globenewswire.com/news-release/2024/04/23/2867698/0/en/Uhnder-Releases-New-4D-Digital-Imaging-Radar-Chip-to-Bolster-ADAS-Applications-for-Mass-Market-Automobiles.html) (April 23, 2024) states the 96-MIMO-channel figure and DCM technology directly; independently corroborated in trade coverage from [Microwave Journal](https://www.microwavejournal.com/articles/41844-uhnder-releases-new-4d-digital-imaging-radar-chip).
**Summary:** Well-sourced to the company's own release plus independent trade press; the underlying 12-transmit/8-receive antenna breakdown reported by some secondary outlets was not independently fetched/confirmed in this session.

### Claim: $50 million Series D, led by ACME Capital (February 2024)
**Status:** Verified.
**Supporting sources:** [Uhnder's own GlobeNewswire press release](https://www.globenewswire.com/news-release/2024/02/21/2832691/0/en/Uhnder-raises-50-million-in-Series-D-funding-to-accelerate-growth.html) names ACME Capital as lead, lists Magna, Qualcomm Ventures, El Camino Capital, Monta Vista Capital, Sagitta Ventures, and HT Capital as participants, and quotes ACME's Hany Nada and Magna's Boris Shulkin directly.
**Summary:** Verified via the company's own primary press release.

### Claim: Total funding to date ~$145 million
**Status:** Unverified.
**Supporting sources:** Figure surfaced via secondary/aggregator search summaries (Crunchbase-derived); not confirmed via a primary Uhnder or investor source fetched in this session.
**Summary:** Treat as a third-party estimate only.

### Claim: Over 200,000 radar chips shipped to customers (as of February 2024)
**Status:** Partially verified.
**Supporting sources:** Stated directly in [Uhnder's own Series D press release](https://www.globenewswire.com/news-release/2024/02/21/2832691/0/en/Uhnder-raises-50-million-in-Series-D-funding-to-accelerate-growth.html).
**Refuting/questioning sources:** None found; but no independent (non-company) shipment audit or customer-disclosed unit count was found either.
**Summary:** Company-stated figure with no independent corroboration found — plausible given the Magna production relationship, but not third-party verified.

### Claim: Current executive leadership (CEO Hegde, CTO Davis, COO Chennakeshu, CFO Bedewi)
**Status:** Disputed / stale as published.
**Supporting sources:** Uhnder's own team page (fetched during this review) lists all four in these roles.
**Refuting/questioning sources:** Independent obituary sources ([Tribute Archive](https://www.tributearchive.com/obituaries/24392571/curtis-alfred-davis), [St. Louis Post-Dispatch via Legacy.com](https://www.legacy.com/us/obituaries/stltoday/name/curtis-davis-obituary?id=52263896)) confirm Curtis Davis died June 14, 2023; independent Australian trade press ([The Australian Business Journal](https://theabj.com.au/2026/03/20/morse-micro-appoints-joe-bedewi-cfo/)) confirms Joe Bedewi moved to Morse Micro as CFO in March 2026.
**Summary:** Uhnder's public-facing team page is materially out of date — it does not reflect Davis's 2023 death or Bedewi's 2026 departure. Any claim about current Uhnder leadership beyond CEO Hegde (last directly confirmed via an April 2024 company press release) should be treated as unconfirmed until verified against a more current company source.

## Limitations

- **No confirmed drone/C-UAS product:** This entry documents adjacent, enabling MIMO radar-on-chip technology, not a fielded or marketed counter-drone system — treat any drone-detection application as speculative/architectural rather than a current Uhnder offering
- **Automotive-first public track record:** Nearly all independently verifiable deployments, certifications, and customer relationships found in this review relate to automotive safety systems; the company's own materials mention unspecified "industrial and defense" engagements without naming programs
- **Company website leadership page is stale:** As detailed in Key People and Claim Verification above, Uhnder's own team page does not reflect a cofounder's 2023 death or a 2026 CFO departure — a concrete example of why company-published "current team" pages cannot be treated as current without independent cross-checking, per this knowledge base's general sourcing rules
- **Total funding and current CEO status are both unconfirmed:** Specific dollar figures beyond the sourced Series D, and any post-2024 CEO transition, should be verified directly with the company before being relied upon

## Sources

- [Uhnder — The First Digital Automotive Radar](https://www.uhnder.com/)
- [Uhnder Releases New 4D Digital Imaging Radar Chip — GlobeNewswire](https://www.globenewswire.com/news-release/2024/04/23/2867698/0/en/Uhnder-Releases-New-4D-Digital-Imaging-Radar-Chip-to-Bolster-ADAS-Applications-for-Mass-Market-Automobiles.html)
- [Uhnder raises $50 million in Series D funding to accelerate growth — GlobeNewswire](https://www.globenewswire.com/news-release/2024/02/21/2832691/0/en/Uhnder-raises-50-million-in-Series-D-funding-to-accelerate-growth.html)
- [Uhnder Strengthens Executive Leadership Team with COO and CFO Appointments — PRNewswire](https://www.prnewswire.com/news-releases/uhnder-strengthens-executive-leadership-team-with-coo-and-cfo-appointments-301278390.html)
- [Uhnder Releases New 4D Digital Imaging Radar Chip — Microwave Journal](https://www.microwavejournal.com/articles/41844-uhnder-releases-new-4d-digital-imaging-radar-chip)
- [TDK Ventures invests in digital imaging radar-on-chip — TDK Ventures](https://tdk-ventures.com/uhnder/)
- [Curtis Alfred Davis obituary — Tribute Archive](https://www.tributearchive.com/obituaries/24392571/curtis-alfred-davis)
- [Curtis Davis obituary (1968–2023) — St. Louis Post-Dispatch via Legacy.com](https://www.legacy.com/us/obituaries/stltoday/name/curtis-davis-obituary?id=52263896)
- [Morse Micro Appoints Joe Bedewi as Chief Financial Officer — The Australian Business Journal](https://theabj.com.au/2026/03/20/morse-micro-appoints-joe-bedewi-cfo/)
