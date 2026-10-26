---
title: "Curtiss-Wright Defense Solutions"
date: 2026-03-25
lastmod: 2026-10-23
draft: false
description: "Defense electronics division of Curtiss-Wright (NYSE: CW), Ashburn, VA; SOSA-aligned 3U VPX3-730 (RTX PRO 5000 Blackwell, July 2025) and 6U VPX6-731 (one or two GPUs, October 2025) modules; PacStar 431 compact edge AI module on NVIDIA IGX Thor (2,070 TFLOPS vendor rating); Q2 2026 Defense Electronics sales $246M; CEO succession announced September 2026."
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://defense-solutions.curtisswright.com/"
  - "https://militaryaerospace.com/computers/article/55305932/curtiss-wright-defense-solutions-sosa-aligned-imbedded-computing-module-for-artificial-intelligence-ai"
  - "https://www.eejournal.com/industry_news/curtiss-wright-expands-nvidia-accelerated-gpu-family-with-6u-vpx-module-for-ai-at-the-edge"
  - "https://www.eejournal.com/industry_news/curtiss-wright-introduces-new-pacstar-431-edge-ai-module-accelerated-by-nvidia-igx-thor"
  - "https://www.businesswire.com/news/home/20260805430638/en/Curtiss-Wright-Reports-Second-Quarter-2026-Financial-Results-and-Raises-Full-Year-2026-Guidance"
  - "https://www.sec.gov/Archives/edgar/data/0000026324/000162828026062997/ex991_ceosuccession.htm"
  - "https://www.curtisswrightds.com/company/leadership.html"
last_reviewed: 2026-10-23
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Curtiss-Wright Defense Solutions, based in Ashburn, Virginia, is the defense computing arm of Curtiss-Wright Corporation (NYSE: CW). It sells rugged compute at two tiers: OpenVPX GPU modules that defense primes slot into their own chassis, and compact PacStar edge computers. The VPX3-730 (3U, announced 2025-07-29) and VPX6-731 (6U, announced 2025-10-28) use NVIDIA RTX PRO 5000 Blackwell GPUs and are described as SOSA-aligned. In the same October 2025 announcement cycle it introduced the PacStar 431, built on NVIDIA IGX Thor. The parent reported Q2 2026 sales of $924M, of which Defense Electronics was $246M (down 3%), and on 2026-09-22 announced that COO Kevin Rayment will succeed CEO Lynn Bamford on 2027-01-01.

## Key Facts

- **Parent:** Curtiss-Wright Corporation, NYSE: CW; CEO Lynn M. Bamford (to 2026-12-31); Kevin M. Rayment becomes President and CEO 2027-01-01, with Bamford as Executive Chair
- **Division location:** Ashburn, VA (per product announcements)
- **Parent financials (Q2 2026):** sales $924M (+5%); Defense Electronics $246M (−3% from $253M), 28.0% operating margin; FY2026 sales guidance raised to $3,768–3,813M
- **Value chain position:** component/subsystem supplier at the VPX module tier and the compact edge-system tier
- **VPX3-730:** 3U OpenVPX GPU module; NVIDIA RTX PRO 5000 Blackwell; up to 50 TFLOPS peak; 100 GbE via ConnectX-7 over PCIe Gen5; SOSA-aligned (announced 2025-07-29)
- **VPX6-731:** 6U OpenVPX; one or two RTX PRO 5000 Blackwell GPUs; up to 100 TFLOPS peak and 48 GB GDDR7; conduction-cooled, liquid flow-through and air flow-through options; designed for SOSA-aligned systems (announced 2025-10-28)
- **PacStar 431:** NVIDIA IGX Thor with Blackwell GPU (IGX T5000); up to 2,070 TFLOPS AI performance (vendor rating); 14-core Arm Neoverse V3AE CPU; 128GB DDR5X; 25 GbE interfaces; enclosure 5.3" × 7.1" × 1.7" (announced 2025-10-28)
- **Standards:** OpenVPX (VITA 65) and the SOSA Technical Standard for the VPX modules

## What It Is / How It Works

**VPX module tier.** The VPX3-730 and VPX6-731 are cards a prime contractor adds to its own chassis, next to RF front-ends and FPGA processing. The company's stated targets are radar, display and sensor-fusion systems that need deep-learning inference. SOSA alignment means the module is designed to the Sensor Open Systems Architecture technical standard so cards from different vendors can interoperate in aligned chassis.

**PacStar tier.** PacStar began as a tactical-communications line. The PacStar 431 is a compact enclosure rather than a rackmount server: a Blackwell-based IGX Thor module with 128GB of memory aimed at real-time inference, sensor fusion and autonomous processing at the edge. The 2,070 TFLOPS figure is the NVIDIA-platform AI rating cited by the vendor; the numeric precision behind it (and whether it assumes sparsity) is not stated in the sources reviewed.

**SOSA context.** DoD policy favors open, re-competable architectures. For a module vendor this opens new program starts but weakens proprietary lock-in; see the [Mercury Systems]({{< relref "mercury-systems.md" >}}) entry for the same dynamic.

## Notable Developments

- **2026-09-22:** CEO succession announced: Kevin Rayment (COO) becomes President and CEO on 2027-01-01; Lynn Bamford becomes Executive Chair. ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000026324/000162828026062997/ex991_ceosuccession.htm))
- **2026-08-05:** Q2 2026 results: Defense Electronics sales $246M; management cites record defense electronics orders and embedded computing demand from fighter and UAV programs; full-year guidance raised. ([Business Wire](https://www.businesswire.com/news/home/20260805430638/en/Curtiss-Wright-Reports-Second-Quarter-2026-Financial-Results-and-Raises-Full-Year-2026-Guidance))
- **2025-10-28:** VPX6-731 (6U) and PacStar 431 (IGX Thor) announced. ([EE Journal — VPX6-731](https://www.eejournal.com/industry_news/curtiss-wright-expands-nvidia-accelerated-gpu-family-with-6u-vpx-module-for-ai-at-the-edge), [EE Journal — PacStar 431](https://www.eejournal.com/industry_news/curtiss-wright-introduces-new-pacstar-431-edge-ai-module-accelerated-by-nvidia-igx-thor))
- **2025-07-29:** VPX3-730 3U SOSA-aligned GPU module announced with NVIDIA RTX PRO 5000 Blackwell. ([Military & Aerospace Electronics](https://militaryaerospace.com/computers/article/55305932/curtiss-wright-defense-solutions-sosa-aligned-imbedded-computing-module-for-artificial-intelligence-ai))

## Key People

### Brian Perry — Senior Vice President and General Manager, Defense Solutions Division
- **LinkedIn:** not found
- **Role:** named as head of the Defense Solutions division on Curtiss-Wright's leadership page ([Curtiss-Wright](https://www.curtisswrightds.com/company/leadership.html))

### Lynn M. Bamford — Chair and CEO (CEO through 2026-12-31)
- **LinkedIn:** not found
- **Role:** becomes Executive Chair on 2027-01-01

### Kevin M. Rayment — EVP and COO; incoming President and CEO (2027-01-01)
- **LinkedIn:** not found

Prior employers were not confirmed from fetched sources.

### People — Last Reviewed: 2026-10-23

## Claim Verification

### Claim: First SOSA-aligned Blackwell VPX modules

**Status:** Unverified

**Supporting sources:**
- [Military & Aerospace Electronics](https://militaryaerospace.com/computers/article/55305932/curtiss-wright-defense-solutions-sosa-aligned-imbedded-computing-module-for-artificial-intelligence-ai) — describes the VPX3-730 as a rugged, SOSA-aligned 3U GPU module with an RTX PRO 5000 Blackwell
- [EE Journal](https://www.eejournal.com/industry_news/curtiss-wright-expands-nvidia-accelerated-gpu-family-with-6u-vpx-module-for-ai-at-the-edge) — VPX6-731 designed for systems aligned with the SOSA standard

**Refuting / questioning sources:**
- "Aligned" is a vendor term, not an independent conformance certification. Competing SOSA-aligned 6U GPU cards from other vendors appear in trade coverage, so "first" was not confirmed.

**Summary:** Alignment is a vendor assertion; priority over competitors is unconfirmed.

### Claim: PacStar 431 delivers 2,070 TFLOPS

**Status:** Partially verified

**Supporting sources:**
- [EE Journal](https://www.eejournal.com/industry_news/curtiss-wright-introduces-new-pacstar-431-edge-ai-module-accelerated-by-nvidia-igx-thor) — "up to 2070 TFLOPS of AI performance," described as 8x the prior IGX Orin 500

**Refuting / questioning sources:**
- Precision (for example FP4) and sparsity assumptions are not stated, so the number is not comparable with FP16 or INT8 figures; no sustained thermal data for the 5.3" × 7.1" × 1.7" enclosure.

**Summary:** A vendor peak AI rating, not a sustained throughput.

## Sources

- [Curtiss-Wright Defense Solutions](https://defense-solutions.curtisswright.com/)
- [VPX3-730 — Military & Aerospace Electronics (Jul 2025)](https://militaryaerospace.com/computers/article/55305932/curtiss-wright-defense-solutions-sosa-aligned-imbedded-computing-module-for-artificial-intelligence-ai)
- [VPX6-731 — EE Journal (Oct 2025)](https://www.eejournal.com/industry_news/curtiss-wright-expands-nvidia-accelerated-gpu-family-with-6u-vpx-module-for-ai-at-the-edge)
- [PacStar 431 — EE Journal (Oct 2025)](https://www.eejournal.com/industry_news/curtiss-wright-introduces-new-pacstar-431-edge-ai-module-accelerated-by-nvidia-igx-thor)
- [Q2 2026 results — Business Wire](https://www.businesswire.com/news/home/20260805430638/en/Curtiss-Wright-Reports-Second-Quarter-2026-Financial-Results-and-Raises-Full-Year-2026-Guidance)
- [CEO succession 8-K (Sep 2026)](https://www.sec.gov/Archives/edgar/data/0000026324/000162828026062997/ex991_ceosuccession.htm)
- [Defense Solutions leadership](https://www.curtisswrightds.com/company/leadership.html)
