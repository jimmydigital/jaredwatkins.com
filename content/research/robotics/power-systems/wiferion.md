---
title: "Wiferion"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "Freiburg Germany inductive wireless charging system developer for AMRs and AGVs; etaLINK system delivers up to 3.3kW at 93% efficiency; acquired by Tesla in 2023 then sold to PULS GmbH (Munich power supply company), now operating as PULS Wireless business unit."
tags: ["robotics", "power-systems", "eu", "wireless-charging"]
categories: ["company"]
research_area: "robotics/power-systems"
source_urls:
  - "https://www.therobotreport.com/puls-acquires-wiferions-wireless-charging-business/"
  - "https://www.wiferion.com/us/products/etalink-3000-inductive-charging-with-3-kw/"
  - "https://www.automation.com/en-us/articles/october-2023/wiferion-wireless-charging-business-acquired-puls"
last_reviewed: 2026-03-31
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Wiferion is a Freiburg im Breisgau, Germany developer of inductive wireless charging systems for industrial autonomous mobile robots (AMRs) and automated guided vehicles (AGVs). Founded in 2016, the company commercialized an "etaLINK" floor-embedded or pad-mounted inductive charging architecture that allows AMR fleets to charge automatically during natural pauses in operation ("opportunity charging") without operator intervention. The company's ownership history is unusual: Wiferion was acquired by Tesla in June 2023 for an undisclosed amount, then sold by Tesla to PULS GmbH (a Munich-based DIN rail power supply manufacturer, part of the PULS Group) on October 1, 2023. Wiferion's engineers remained at Tesla; only the business, brand, technology rights, and patents transferred to PULS. It now operates as the PULS Wireless business unit, with its operational team based in Freiburg. **Note:** The task briefing for this entry stated Wiferion was "Acquired by Würth Elektronik (Würth Group subsidiary) in 2022" — research found the actual acquirer was PULS GmbH in 2023, with Tesla as an intermediary owner.

## Key Facts

- **Founded:** 2016 (Freiburg im Breisgau, Germany)
- **HQ:** Freiburg im Breisgau, Germany (PULS Wireless business unit)
- **Type:** Business unit of PULS GmbH (private, Munich)
- **Ownership:** PULS GmbH since October 1, 2023; previously Tesla (June–October 2023); previously independent startup
- **Prior funding:** $6.8M over 2 rounds pre-acquisition
- **Key products:** etaLINK 3000 (3.3 kW max, 93% efficiency, inductive floor/pad charging for AMR/AGV); compatible with industrial LFP and Li-Ion battery management systems
- **Current leadership:** Julian Seume (former CSO of Wiferion) and Matthieu Ebert co-manage the PULS Wireless business unit
- **Deployed in:** 20+ countries

## What It Is / How It Works

Wiferion's etaLINK system uses resonant inductive power transfer between a floor-embedded or pad-mounted transmitter coil and a receiver coil installed on the underside of the AMR or AGV. When a robot drives over or parks near the transmitter, the charging process begins automatically within one second of coil proximity — no operator contact required. This enables "opportunity charging": rather than fully depleting a battery and then charging at a dedicated station for 30–60 minutes, robots can charge opportunistically during brief pauses (loading/unloading, queue waiting, elevator holds) throughout their shift. With frequent small charge top-ups, a fleet can run continuously across multi-shift operations without removing robots from service.

The etaLINK 3000 delivers up to 3.3 kW at maximum output current of 60A, with system efficiency of up to 93% — competitive with high-quality wired charging systems. Efficiency of 93% means 7% of power is lost as heat in the inductive transfer; for a 3kW system operating at full load, this is approximately 210W of heat dissipation, acceptable in industrial environments. The system is rated IP65/IP68 (fully dust-tight and water-resistant), allowing floor embedding in wash-down environments and outdoor applications. The transmitter coil connects to the factory floor power infrastructure, and the receiver coil is permanently installed on the vehicle underside.

The autonomous charging initiation (within one second of positioning) is achieved through the coil geometry and resonant circuit design: as long as the receiver coil is within the operating range of the transmitter, power transfer begins without any software handshake or communication step. This "always-on" behavior is simpler and more reliable than plug-in systems that require mechanical alignment and wear-prone electrical contacts.

For AMR fleet operators, the economic case for opportunity charging is: higher robot utilization (less downtime at charging stations), longer battery life (shallow discharge cycles are better for Li-Ion chemistry than deep discharge/full-charge cycles), and simplified fleet management (no manual battery swap, no human operator involvement in charging logistics). The 20+ country deployment footprint indicates commercial validation across European automotive, logistics, and industrial manufacturing applications.

Tesla's acquisition of Wiferion in June 2023 and rapid divestiture to PULS in October 2023 is unexplained in public statements. The separation of Wiferion's engineers (retained by Tesla) from its business and IP assets (sold to PULS) is atypical and suggests Tesla acquired Wiferion primarily for the engineering talent (possibly for its own wireless charging research programs), while the Wiferion-branded industrial charging business was not strategically aligned with Tesla's core operations.

## Notable Developments

- **2023-10:** PULS GmbH completes acquisition of Wiferion business, IP, and brand from Tesla; Wiferion becomes PULS Wireless business unit; Julian Seume and Matthieu Ebert lead the unit from Freiburg. ([The Robot Report](https://www.therobotreport.com/puls-acquires-wiferions-wireless-charging-business/); [Automation.com](https://www.automation.com/en-us/articles/october-2023/wiferion-wireless-charging-business-acquired-puls))
- **2023-06:** Tesla acquires Wiferion for undisclosed consideration; Wiferion engineers stay at Tesla. ([electrive.com](https://www.electrive.com/2023/10/11/tesla-sells-wireless-charging-business-wiferion/))
- **2016:** Wiferion founded by Florian Reiners, Johannes Mayers, Benriah Goeldi, and Johannes Tritschler in Freiburg; $6.8M raised pre-acquisition.

## Key People

### Julian Seume — Business Unit Manager, PULS Wireless (former Wiferion CSO)
- **LinkedIn:** Not found (no confirmed public profile)
- **Background:** Former Chief Sales Officer (CSO) of Wiferion; retained post-acquisition as co-lead of the PULS Wireless business unit alongside Matthieu Ebert
- **Notes:** Seume and Ebert represent operational continuity from the original Wiferion team despite the two-step Tesla → PULS ownership transition.

### Florian Reiners — Co-Founder (not with PULS)
- **LinkedIn:** Not found (no confirmed public profile)
- **Education:** Electrical engineering background
- **Notes:** Co-founded Wiferion in 2016; left with the engineering team to Tesla in 2023. Not part of the current PULS Wireless unit.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

Wiferion (PULS Wireless) operates at the **Subsystem Supplier** layer, selling charging infrastructure to AMR/AGV OEMs for integration into robot designs and to end-user logistics facilities as aftermarket installations. The coil design and resonant circuit IP transferred to PULS; hardware manufacturing is German/European industrial supply chain. **⚑ Competitive overlap:** WiBotic (Seattle) and Wiferion are the two most prominent wireless charging specialists for robotics globally; WiBotic has stronger drone and lightweight robot market position; Wiferion has stronger penetration in European automotive-grade heavy AMR and AGV markets. PULS brings distribution infrastructure and power electronics manufacturing credibility that should help Wiferion's OEM integration into industrial automation.

## Claim Verification

### Claim: etaLINK system achieves up to 93% charging efficiency — "comparable to very good wired charging systems"
**Status:** Partially verified

**Supporting sources:**
- [etaLINK FAQ — Wiferion](https://www.wiferion.com/en/faq/faq-etalink/) — Company specification; 93% efficiency at rated conditions
- [Direct Industry product listing](https://www.directindustry.com/prod/wiferion/product-239276-2402857.html) — Third-party listing confirms the 93% efficiency figure from Wiferion datasheets
- Context: High-quality wired industrial battery chargers typically achieve 92–96% efficiency at full load; 93% for inductive transfer is plausible and technologically consistent with published research on resonant inductive coupling at this power level

**Refuting / questioning sources:**
- Efficiency in real-world installations varies with coil alignment tolerance, ambient temperature, and partial-load operation; the 93% figure is likely measured at optimal alignment and full rated power; efficiency at partial load or with moderate misalignment would be lower

**Summary:** The 93% efficiency claim is plausible and supported by the company's published datasheets; real-world efficiency will vary with installation conditions, but the claim is consistent with the physics of high-quality resonant inductive transfer.

## Sources

- [PULS Acquires Wiferion — The Robot Report (Oct 2023)](https://www.therobotreport.com/puls-acquires-wiferions-wireless-charging-business/)
- [Wiferion Wireless Charging Acquired by PULS — Automation.com (Oct 2023)](https://www.automation.com/en-us/articles/october-2023/wiferion-wireless-charging-business-acquired-puls)
- [Tesla Sells Wiferion — electrive.com (Oct 2023)](https://www.electrive.com/2023/10/11/tesla-sells-wireless-charging-business-wiferion/)
- [etaLINK 3000 Product Page — Wiferion](https://www.wiferion.com/us/products/etalink-3000-inductive-charging-with-3-kw/)
- [etaLINK FAQ — Wiferion](https://www.wiferion.com/en/faq/faq-etalink/)
- [Wiferion Company Profile — Tracxn](https://tracxn.com/d/companies/wiferion/__ToUeN7HN8fJFPOrQUiO5EzYmxADb0RSDyRxahevKd-g)
