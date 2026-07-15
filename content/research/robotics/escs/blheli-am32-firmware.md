---
title: "ESC Firmware: BLHeli / BLHeli_32 / AM32"
date: 2026-07-15
lastmod: 2026-07-15
draft: false
description: "The dominant ESC firmware lineage for FPV and small drones — from Steffen Skaug's open-source BLHeli through the closed-source, since-discontinued BLHeli_32, to the open-source AM32 replacement."
research_area: "robotics/escs"
source_urls:
  - "https://oscarliang.com/am32-esc-firmware-an-open-source-alternative-to-blheli32/"
last_reviewed: 2026-07-15
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

BLHeli, BLHeli_32, and AM32 are the successive generations of firmware that run on most FPV and small commercial drone electronic speed controllers, controlling brushless motor commutation. The lineage is a documented case study in firmware single-vendor risk: the closed-source, licensing-fee-based BLHeli_32 became the industry default, then its Norwegian developer abruptly ceased operations in June 2024, leaving the open-source AM32 firmware as the community's replacement path.

## Key Facts

- Type: Firmware/technology (not a company)
- Origin: BLHeli created by Steffen Skaug (Norway) in the early 2010s, open-sourced under GPLv3
- Status: BLHeli and BLHeli_S remain open-source; BLHeli_32 (closed-source, licensing-fee-based) was discontinued when its developer, BLHeli AS, ceased operations in June 2024; AM32 (open-source, created by Peter Smith/"AlkaMotors") is the active replacement
- Key metric(s): AM32 supports Betaflight passthrough flashing, DShot300/600, bi-directional DShot, and KISS telemetry; hardware support spans STSPIN32F0, STM32F051, STM32G071, GD32E230, AT32F415, and AT32F421 MCUs

## What It Is / How It Works

An ESC firmware governs how an electronic speed controller commutates a brushless motor — timing the phase switching that converts DC battery current into motor rotation — and exposes control protocols (PWM, DShot, bi-directional DShot, CAN) and telemetry back to the flight controller. BLHeli progressed through three generations: the original BLHeli (assembly code for 8-bit Atmel/Silabs MCUs, three motor-type variants, GPLv3 open source), BLHeli_S (assembly for Silabs 8-bit MCUs, multirotor-focused, also open source), and BLHeli_32 (rewritten for 32-bit MCUs, closed-source, requiring ESC manufacturers to pay a licensing fee passed through to consumers).

BLHeli_32 became the de facto standard for FPV racing and small commercial drone ESCs on the strength of its reliability and feature set, despite the licensing cost. In June 2024, BLHeli AS abruptly announced it was ceasing operations, halting all firmware updates and support with no announced transition plan — leaving every ESC manufacturer and end user who had built products around BLHeli_32 without a forward path from the original vendor.

AM32, created by Peter Smith under the "AlkaMotors" name, is an open-source firmware alternative for modern ARM-based ESCs that predates the BLHeli_32 shutdown (available since at least 2023) but became the primary migration target afterward. Because it is open-source and royalty-free, ESC manufacturers avoid the licensing fee previously built into BLHeli_32 pricing, and the firmware is under active community development rather than being dependent on a single company's continued operation. Existing BLHeli_32 ESCs can, in many cases, be reflashed to AM32 (a one-way transition, according to community documentation), and new ESC hardware increasingly ships with AM32 pre-installed.

## Notable Developments

- **2024-06:** BLHeli AS (Norway) ceases operations, halting all updates and support for BLHeli_32 with no transition plan — a live single-vendor firmware collapse affecting a large share of the FPV/drone ESC installed base.
- **2023 (by):** AM32 firmware, created by Peter Smith/AlkaMotors, is established as an open-source, royalty-free alternative to BLHeli_32, supporting a growing list of ARM-based ESC hardware.

## Claim Verification

### Claim: BLHeli AS ceased operations in June 2024, discontinuing BLHeli_32 support
**Status:** Partially verified

**Supporting sources:**
- [AM32 ESC Firmware - An Open Source Alternative to BLHeli32 | Oscar Liang](https://oscarliang.com/am32-esc-firmware-an-open-source-alternative-to-blheli32/) — a June 2024-dated reader comment on this article references "the non-continuation of BLHeli" as recent news, and the article's own July 2024 update timestamp is consistent with the discontinuation timeframe.

**Refuting / questioning sources:**
- None found; no source disputing the discontinuation was located, but the primary confirmation in this session comes from a secondary trade blog and a reader comment rather than a direct BLHeli AS company statement, which could not be located and fetched in this session.

**Summary:** The discontinuation is corroborated by secondary sources and is widely referenced in the FPV community, but a primary BLHeli AS statement was not independently fetched and read in this session; treat the exact date as approximate pending direct confirmation.

## Sources

- [AM32 ESC Firmware - An Open Source Alternative to BLHeli32 | Oscar Liang](https://oscarliang.com/am32-esc-firmware-an-open-source-alternative-to-blheli32/) — BLHeli_32 licensing model, AM32 origin and features, hardware compatibility list, migration guidance
