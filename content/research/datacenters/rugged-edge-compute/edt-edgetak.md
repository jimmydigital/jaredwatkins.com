---
title: "EDT / EDGETAK"
date: 2026-03-25
lastmod: 2026-10-23
draft: false
description: "Hillsboro, OR defense electronics company (HEICO subsidiary, NYSE: HEI); EDGETAK man-wearable tactical edge AI computer announced April 16, 2025; NVIDIA Jetson Orin NX 16GB with a vendor-stated 100 TOPS; passively cooled, battery-powered, designed to fit alongside radio and magazine pouches; SDR version (30 MHz–8 GHz) announced as coming in summer 2025; no MIL-STD qualification claims on the product page."
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://edt.com/"
  - "https://edt.com/edgetak/"
  - "https://edt.com/product/edgetak/"
  - "https://edt.com/edgetak-press-release/"
  - "https://www.sec.gov/Archives/edgar/data/0000046619/000004661926000018/a07312026ex991earningsrele.htm"
last_reviewed: 2026-10-23
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Engineering Design Team (EDT) is a Hillsboro, Oregon electronics company and a subsidiary of HEICO Corporation. Its EDGETAK, announced April 16, 2025, is a man-wearable edge computer built on an NVIDIA Jetson Orin NX that runs AI and data-processing applications on the body without network connectivity. EDT says it is passively cooled, battery-powered, open (no proprietary software or licenses) and designed to fit alongside existing radio and magazine pouches. The launch release also announced a summer 2025 version with an integrated software-defined radio covering 30 MHz to 8 GHz; no later release confirming shipment was found. EDT publishes no weight, dimensions, battery life or MIL-STD qualification for EDGETAK in the sources reviewed.

## Key Facts

- **Full company name:** Engineering Design Team, Inc. (EDT)
- **HQ:** Hillsboro, OR (3423 NE John Olsen Avenue)
- **Parent:** HEICO Corporation (NYSE: HEI). EDT's site says it has operated "for over 35 years"; it gives no acquisition date.
- **Product:** EDGETAK wearable tactical edge compute; announced 2025-04-16
- **Compute:** NVIDIA Jetson Orin NX 16GB; EDT states 100 TOPS (AI inference rating; not a measured field figure)
- **Storage and I/O:** up to 8TB NVMe; two USB-C ports; RJ45 Ethernet; Wi-Fi/Bluetooth; GPS; DC input 9–16 V
- **Form factor:** wearable, "optimized for size, wearable and thermal management"; no dimensions or weight published
- **Cooling and power:** passive cooling; battery-powered; battery life not stated
- **Software:** open platform; EDT's product page says the unit can host ATAK (Android Team Awareness Kit)
- **SDR version:** 30 MHz–8 GHz with up to 80 MHz instantaneous bandwidth, aimed at spectrum monitoring and signals collection; announced as a summer 2025 release
- **Standards claims:** none made on the EDGETAK product page
- **Value chain position:** end-system supplier in the man-portable tier

## What It Is / How It Works

EDGETAK sits in the smallest platform tier in this section. A rack or vehicle system can draw hundreds of watts; a dismounted operator carries batteries and a few pouches. EDT's answer is a Jetson Orin NX module in a small semi-rugged enclosure that runs inference locally, which matters in disconnected or degraded communications where a cloud service is unreachable.

**Open stack.** EDT says there is no proprietary software or licensing, so users load their own application stack. Its product page says the unit can host ATAK, the Android-based situational-awareness app used across US forces; the press release does not mention ATAK, so the depth of integration is not documented.

**Thermal approach.** Passive cooling avoids fans, which add power draw, noise and a failure point. It also limits sustained compute: a fanless enclosure of this size will throttle under continuous load, and EDT publishes no thermal data.

**SDR version.** The launch release announced an enhanced EDGETAK with an integrated software-defined radio from 30 MHz to 8 GHz, targeting spectrum monitoring and signals collection. The release said "summer" and was dated April 2025. The product pages reviewed (last modified April and May 2026) do not describe an RF variant.

## Notable Developments

- **2026-07:** HEICO reports record Q3 FY2026 net sales of $1,413.1M; its Electronic Technologies Group (the segment containing EDT) reports $483.5M. The release does not mention EDT or EDGETAK. ([HEICO](https://www.sec.gov/Archives/edgar/data/0000046619/000004661926000018/a07312026ex991earningsrele.htm))
- **2025-04-16:** EDGETAK announced for procurement teams, integrators and partners, with a demonstration at SOF Week 2025; SDR version flagged for summer. ([EDT press release](https://edt.com/edgetak-press-release/))

## Key People

### Cameron Kidd — President, EDT
- **LinkedIn:** not found
- **Role:** quoted as President of EDT in the April 2025 release ([EDT](https://edt.com/edgetak-press-release/))

### Jay Soles — VP of Business Development, EDT
- **LinkedIn:** not found
- **Role:** quoted in the April 2025 release

### HEICO leadership
- Eric A. Mendelson and Victor H. Mendelson are Co-Chairmen and Co-CEOs of HEICO per its July 2026 earnings release.

Prior employers were not confirmed from fetched sources.

### People — Last Reviewed: 2026-10-23

## Claim Verification

### Claim: Wearable form factor that fits alongside radio and magazine pouches

**Status:** Unverified

**Supporting sources:**
- [EDT press release](https://edt.com/edgetak-press-release/) and [EDT EDGETAK page](https://edt.com/edgetak/) — state the unit is designed to fit on the body alongside existing radio and magazine pouches

**Refuting / questioning sources:**
- No dimensions, weight or battery size are published, so fit cannot be checked.

**Summary:** A design intent without published dimensions.

### Claim: 100 TOPS

**Status:** Unverified

**Supporting sources:**
- [EDT product page](https://edt.com/product/edgetak/) — states 100 TOPS with a Jetson Orin NX 16GB

**Refuting / questioning sources:**
- TOPS is a peak AI rating for the module, not sustained throughput in a fanless enclosure; no thermal or benchmark data is published.

**Summary:** A module-level rating, not an EDGETAK measurement.

### Claim: SDR version covering 30 MHz–8 GHz

**Status:** Unverified

**Supporting sources:**
- [EDT press release](https://edt.com/edgetak-press-release/) — announced the SDR version with up to 80 MHz instantaneous bandwidth for summer release

**Refuting / questioning sources:**
- No product page, datasheet or customer announcement confirming the variant shipped, and no sensitivity or dynamic-range figures.

**Summary:** An announced capability with no confirmed availability.

### Claim: Rugged or MIL-STD qualified

**Status:** Unverified

**Supporting sources:**
- None. The product page calls the enclosure semi-rugged and makes no MIL-STD claim.

**Refuting / questioning sources:**
- The absence of qualification data means suitability for field use is undocumented.

**Summary:** No environmental qualification is published.

## Sources

- [EDT](https://edt.com/)
- [EDT — EDGETAK](https://edt.com/edgetak/)
- [EDT — EDGETAK product page](https://edt.com/product/edgetak/)
- [EDT — EDGETAK press release (Apr 2025)](https://edt.com/edgetak-press-release/)
- [HEICO — Q3 FY2026 earnings release](https://www.sec.gov/Archives/edgar/data/0000046619/000004661926000018/a07312026ex991earningsrele.htm)
