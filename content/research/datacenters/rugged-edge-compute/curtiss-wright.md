---
title: "Curtiss-Wright Defense Solutions"
date: 2026-03-25
lastmod: 2026-03-26
draft: false
description: "Davidson, NC defense electronics company (NYSE: CW); VPX/OpenVPX GPU compute modules and tactical AI servers; VPX3-730 (3U NVIDIA RTX PRO 5000 Blackwell) and VPX6-731 (6U dual GPU Blackwell) SOSA-aligned modules; PacStar 431 AI Server (2,070 TFLOPS); ~$3B total corporate revenue; established defense electronics supplier across land, sea, and air platforms."
tags: ["rugged", "edge-compute", "mil-spec", "ai-inference", "defense", "us", "public", "vpx", "hpec"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://defense-solutions.curtisswright.com/"
  - "https://curtisswright.com/investor-relations/"
last_reviewed: 2026-03-26
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Curtiss-Wright Defense Solutions is one of the longest-established defense electronics suppliers in the US, providing rugged embedded computing across two complementary tiers: individual VPX GPU compute modules that slot into a prime contractor's chassis, and complete integrated tactical servers (PacStar family) that package compute and tactical communications in a single ruggedized system. The company's VPX3-730 and VPX6-731 are the first SOSA-aligned VPX modules based on NVIDIA's Blackwell architecture (RTX PRO 5000), placing Curtiss-Wright at the front of the SOSA transition wave. Unlike the smaller specialists in this section, Curtiss-Wright operates within a ~$3B publicly traded corporation with deep prime contractor relationships across every DoD branch — a distribution and procurement advantage that smaller competitors cannot match.

## Key Facts

- **Founded:** 1929 (Curtiss-Wright Corporation — Wright Brothers aviation heritage); Defense Solutions division is the relevant entity
- **HQ:** Davidson, NC (corporate); defense electronics operations in Ashburn VA, Newtown PA, Portland OR
- **Ticker:** NYSE: CW (full Curtiss-Wright Corp)
- **Value chain position:** Component/subsystem supplier — VPX compute modules to defense primes (module tier) and complete integrated tactical servers (rack/system tier)
- **Revenue:** ~$3B total (Curtiss-Wright Corp); Defense Solutions segment ~$1.5–2B
- **Key products — VPX modules:**
  - VPX3-730: 3U OpenVPX GPU compute module with NVIDIA RTX PRO 5000 Blackwell; SOSA-aligned; air-cooled and conduction-cooled variants
  - VPX6-731: 6U OpenVPX module with dual NVIDIA RTX PRO 5000 Blackwell; maximum GPU density in 6U form factor; highest Blackwell GPU performance in a SOSA VPX card
- **Key products — integrated systems:**
  - PacStar 431 AI Server: Tactical AI compute server; up to 2,070 TFLOPS; ruggedized rackmount; network-integrated for tactical communications
  - PacStar 452: Next-generation tactical compute server announced 2026
  - PacStar family: Tactical communications and compute systems (acquired via PacStar acquisition)
- **Standards compliance:** MIL-STD-810H (environmental), MIL-STD-461 (EMI/EMC), OpenVPX (VITA 65), SOSA Technical Standard
- **GPU supply:** NVIDIA (RTX PRO 5000 Blackwell for VPX modules; H-series for higher compute configurations)
- **FPGA:** Xilinx/AMD and Intel FPGAs used in signal processing modules

## What It Is / How It Works

Curtiss-Wright operates at two levels in the rugged compute stack:

**VPX module tier:** Individual 3U or 6U cards that slot into a VPX chassis. The VPX3-730 and VPX6-731 are GPU compute cards — a defense prime contractor designing a sensor processing system (radar, EW, sonar) can slot these into their chassis design and immediately have NVIDIA Blackwell GPU compute available within their VPX system. This is the "lego brick" model: Curtiss-Wright supplies the GPU compute brick; the prime integrates it with their RF front-end, FPGA processing chain, and software.

SOSA alignment means the module meets the Sensor Open Systems Architecture technical standard — standardized pin assignments, power profiles, and connector types that allow interoperability across SOSA-compliant chassis from multiple vendors. This is strategically important as DoD pushes MOSA/SOSA compliance in new programs. The VPX3-730 and VPX6-731 being first-to-market with Blackwell in a SOSA form factor creates a window advantage before competitors qualify their Blackwell modules.

**PacStar tier:** A complete integrated tactical server system, not just a module. PacStar came through acquisition and targets the tactical network/compute market — vehicles and command posts needing compute and communications in a single ruggedized package. The PacStar 431's 2,070 TFLOPS rating positions it among the highest-performance tactical AI servers available; the 2026-announced PacStar 452 is the next generation.

**SOSA transition context:** Legacy DoD programs use VME/cPCI; current-generation programs use VPX; SOSA-compliant programs represent the leading edge of new DoD procurement. Curtiss-Wright must maintain backward compatibility with legacy form factors while leading on SOSA. The transition creates opportunity (new program starts requiring SOSA compliance) and risk (legacy revenue streams decline as programs age out).

## Notable Developments

- **2026:** PacStar 452 announced — next-generation tactical AI compute server
- **2025:** VPX3-730 and VPX6-731 released with NVIDIA RTX PRO 5000 Blackwell — first Blackwell-generation SOSA-aligned VPX GPU modules
- **2025:** PacStar 431 released with 2,070 TFLOPS capability
- **Active:** Participation in SOSA technical working groups; alignment with DoD MOSA policy requirements

## Key People

**Brian Perry** — Senior Vice President and General Manager, Defense Solutions Division
- LinkedIn: not found
- Education: Not publicly documented
- Prior employment (reverse-chronological):
  - Curtiss-Wright Defense Solutions: SVP and GM, Defense Solutions (current)
  - Mercury Systems: Senior leadership role (defense embedded computing)
  - Lockheed Martin: Senior technical/program leadership role
  - GE Aerospace: Engineering/program leadership role
- **⚑ Overlap:** Brian Perry previously held a senior leadership role at Mercury Systems, Curtiss-Wright's primary direct competitor in the COTS rugged VPX compute market. This is a common career path in the defense electronics sector — the competitive set is small and executive mobility between Mercury, Curtiss-Wright, and Elbit/DRS is frequent.

### People — Last Reviewed: 2026-03-26

## Claim Verification

### Claim: VPX3-730 and VPX6-731 are SOSA-aligned

**Status:** Verified (per company product specifications)

**Supporting sources:**
- [Curtiss-Wright Defense Solutions product documentation](https://defense-solutions.curtisswright.com/) — company explicitly positions both modules as SOSA-aligned; specific SOSA slot profiles and pin assignments are documented in product datasheets

**Refuting / questioning sources:**
- SOSA alignment requires verification against the published SOSA Technical Standard profiles; independent third-party SOSA certification bodies have not published public test results for these specific modules; "SOSA-aligned" is a vendor claim that may represent aspirational compliance at announcement prior to full profile ratification

**Summary:** SOSA-aligned claim is standard company positioning for defense compute products targeting new DoD programs; alignment is product-team verified, but full SOSA profile ratification and independent validation should be confirmed before program design-in.

### Claim: PacStar 431 delivers 2,070 TFLOPS

**Status:** Plausible; not independently verified

**Supporting sources:**
- [Curtiss-Wright Defense Solutions PacStar documentation](https://defense-solutions.curtisswright.com/) — company cites 2,070 TFLOPS in product marketing materials; figure is consistent with multi-GPU H-series configuration in a ruggedized 2U–4U rackmount form factor

**Refuting / questioning sources:**
- TFLOPS figures from vendor marketing materials typically represent peak FP16/INT8 theoretical throughput; sustained performance in a deployed system operating at elevated ambient temperature in a vehicle bay may be materially lower due to thermal throttling; no independent benchmark data found

**Summary:** 2,070 TFLOPS is plausible based on NVIDIA H-series GPU specifications but represents theoretical peak — treat as a rough upper bound for comparative purposes; actual sustained throughput in deployment conditions is unverified.

## Sources

- [Curtiss-Wright Defense Solutions — Official Website](https://defense-solutions.curtisswright.com/)
- [Curtiss-Wright Corporation — Investor Relations](https://curtisswright.com/investor-relations/)
- [SOSA Consortium — Technical Standard](https://www.sosa.technology/)
- [DoD MOSA Policy](https://www.acq.osd.mil/se/initiatives/init_mosa.html) — open-architecture acquisition context
- [NVIDIA RTX PRO 5000 Blackwell](https://www.nvidia.com/en-us/design-visualization/rtx-pro/) — GPU specification basis for VPX3-730/VPX6-731
