---
title: "US C-UAS Regulatory Framework"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Legal landscape governing counter-UAS detection and interdiction in the United States — who can detect, who can interdict, and which laws constrain private operators."
research_area: "drone-detection"
source_urls:
  - "https://www.hklaw.com/en/insights/publications/2024/07/update-on-us-counter-uas-authorities-and-efforts-to-address-threats"
  - "https://www.faa.gov/sites/faa.gov/files/uas/resources/c_uas/Interagency_Legal_Advisory_on_UAS_Detection_and_Mitigation_Technologies.pdf"
  - "https://www.cisa.gov/news-events/news/cisa-releases-new-guides-safeguard-critical-infrastructure-unmanned-aircraft-systems-threats"
  - "https://www.cisa.gov/sites/default/files/2025-10/DetectionTech_20251030_508.pdf"
  - "https://www.cisa.gov/topics/physical-security/be-air-aware/protect-critical-infrastructure-and-public-gatherings"
  - "https://callmc.com/securing-the-skies-how-the-fy26-ndaa-empowers-your-agency-against-drone-threats/"
  - "https://grabtheaxe.com/c-uas-legalities-corporations-navigating-faa-fcc-rules/"
  - "https://www.route-fifty.com/digital-government/2026/01/defense-law-includes-expanded-counter-drone-authority/410542/"
  - "https://www.congress.gov/bill/118th-congress/senate-bill/473/text"
last_reviewed: 2026-06-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

US counter-UAS (C-UAS) law creates a sharply tiered authority structure: detection and tracking are broadly permissible for private entities, but interdiction — jamming, cyber-takeover, or physical destruction — is reserved exclusively for specific federal agencies. As of FY2026, a limited pathway for trained state and local law enforcement to conduct interdiction under federal authorization has been opened for the first time.

## Key Facts

- **Governing statutes:** FAA Reauthorization Act 2018, FAA Reauthorization Act 2024, FY2024 NDAA (American Security Drone Act), FY2026 NDAA (SAFER SKIES Act)
- **Constraining statutes:** Communications Act of 1934 (47 U.S.C. § 301), Computer Fraud and Abuse Act (CFAA, 18 U.S.C. § 1030), Electronic Communications Privacy Act (Wiretap Act), Pen/Trap Statute
- **Federal interdiction agencies:** DoD, DHS (including TSA), DOJ (including FBI), FAA, Secret Service, Coast Guard (for maritime)
- **Private operator authority:** Detection and tracking only — no jamming, no cyber-takeover, no physical destruction
- **Status:** Rapidly evolving — FY2026 NDAA created first SLTT (state/local/tribal/territorial) pathway in January 2026

## What It Is / How It Works

### The Core Legal Divide: Detection vs. Interdiction

US law draws a hard line between **detection** (passive information-gathering — sensing RF, radar, acoustic, optical) and **interdiction** (taking action to disable, redirect, or destroy a drone). Detection is generally permissible for any entity. Interdiction is tightly restricted.

For private critical infrastructure operators — utilities, water facilities, data centers, emergency shelters — this means the practical toolset is limited to: detect the drone, determine it is suspicious, and call law enforcement. This is not a gap in guidance; it is the intended statutory design. Congress restricted C-UAS interdiction authority because drones are FAA-registered aircraft, and disabling them invokes aviation law, spectrum law, and computer law simultaneously.

### Statutes That Constrain Private Operators

The **Communications Act of 1934** (47 U.S.C. § 301), enforced by the FCC, prohibits any entity from operating a jammer or device that intentionally disrupts radio communications. Because most drone interdiction systems work by RF jamming, GPS spoofing, or signal injection, their use by non-federal entities is a federal crime. The FCC actively enforces this — fines and criminal referrals have been issued to private entities that deployed jammers without authorization.

The **Computer Fraud and Abuse Act** (CFAA, 18 U.S.C. § 1030) makes it illegal to intentionally access a computer system without authorization. Because cyber-takeover C-UAS systems (such as D-Fend EnforceAir) operate by commandeering a drone's control link, using them without explicit federal authorization is a CFAA violation — even if the drone is trespassing.

The **Wiretap Act** and **Pen/Trap Statute** (Electronic Communications Privacy Act) may be implicated by any C-UAS system that intercepts or decodes communications between a drone and its controller. Systems that passively sense RF patterns without decoding content — such as AeroDefense's spectrum sensing approach — are designed specifically to avoid this exposure. Systems that demodulate control signals may require legal review before deployment.

### FAA Reauthorization Act 2018

The FAA Reauthorization Act of 2018 (Section 2207, now codified at 49 U.S.C. § 44810 et seq.) was the first legislation to explicitly authorize C-UAS activities. It granted detection and mitigation authority — including jamming and cyber-takeover — exclusively to the Departments of Defense, Homeland Security, Justice, Transportation (FAA), and the Secret Service. State and local agencies and private entities received no new authority.

### FAA Reauthorization Act 2024

Signed into law in 2024, the reauthorization extended and expanded the 2018 framework through September 30, 2028. Section 904 extended FAA testing authority for counter-UAS operations near airports. Section 935 established authority to request temporary flight restrictions (TFRs) around large public gatherings under a new 49 U.S.C. § 44812. DHS and DOJ interdiction authorities were also extended and clarified under the reauthorization.

### FY2024 NDAA — American Security Drone Act

Signed December 22, 2023, as part of the FY2024 NDAA, the American Security Drone Act prohibits federal agencies from procuring or operating UAS manufactured or assembled by "covered foreign entities" — primarily Chinese manufacturers including DJI, Autel Robotics, and others on the DoD Chinese military company list. Federal contractors, grantees, and cooperative agreement recipients are similarly prohibited. The act does not directly address C-UAS interdiction authority; its primary effect is on procurement.

### FY2026 NDAA — SAFER SKIES Act

The most significant recent development. Signed into law in late 2025 and effective January 2026, the FY2026 NDAA included the SAFER SKIES Act, which created the first statutory pathway for State, Local, Tribal, and Territorial (SLTT) law enforcement and correctional agencies to conduct C-UAS interdiction. Key provisions:

- SLTT agencies may take actions "necessary to mitigate a credible threat" from a drone to safety and security of people, facilities, large public events, critical infrastructure, and correctional institutions
- Agencies must complete a federal training and certification program (developed by DOJ and DHS) before exercising interdiction authority
- Agencies must use systems from a federally authorized technology list
- A 48-hour reporting requirement applies after any mitigation action (Section 8602)
- Section 912 creates Joint Interagency Task Force 401 under the Deputy Secretary of Defense to coordinate C-UAS procurement, strategy, and approved systems lists

### FEMA C-UAS Grant Program

A $500 million FEMA grant program was established to help state and local agencies purchase drone detection equipment. $250 million was available in FY2026, with funding prioritized for jurisdictions hosting National Special Security Events (NSSEs) or SEAR 1 or 2 events such as the FIFA World Cup 2026 and America 250.

## What Private Critical Infrastructure Operators CAN Do

Under current law (as of June 2026), private critical infrastructure operators may:

1. **Detect** drones using any passive sensor — radar, acoustic, optical, thermal
2. **Detect RF signals** using spectrum sensing (without decoding signal content — monitoring patterns only, per Pen/Trap and Wiretap Act constraints)
3. **Receive and process FAA Remote ID broadcasts** — Remote ID is a broadcast signal that any receiver can monitor; no legal barrier
4. **Track** drone location and movement using sensor fusion
5. **Classify** drones as suspicious based on behavior, location, and flight pattern
6. **Report** to law enforcement, providing targeting data for authorized response
7. **Coordinate** with DHS/CISA under established critical infrastructure security frameworks

Private operators may NOT (without explicit federal authorization):
- Jam RF signals (Communications Act violation)
- Spoof GPS signals (Communications Act + CFAA)
- Execute cyber-takeover of a drone (CFAA)
- Physically intercept or destroy a drone in flight (FAA regulations + potential criminal liability)
- Deploy net-capture interceptor drones without authorization

## CISA Guidance for Critical Infrastructure

CISA's **"Be Air Aware"** program, launched through a series of guidance documents in October 2025, provides a framework for critical infrastructure operators to manage UAS risk within their legal authority. The three primary documents are:

- **UAS Detection Technology Guidance** — how to assess risks, select detection tools, and integrate them into existing security operations; explicitly notes that some detection methods monitoring drone-controller communications may implicate federal law, and urges operators to consult legal counsel before deployment
- **Suspicious UAS Activity Guidance** — how to recognize suspicious drone activity indicators, distinguish routine from concerning flights, and determine appropriate response; emphasizes reporting to law enforcement
- **Safe Handling Considerations for Downed UAS** — procedures for physically handling a drone that has landed or crashed on a facility, including safety, evidence preservation, and reporting

CISA's statutory authority for DHS C-UAS activities is grounded in 6 U.S.C. § 124n, which authorizes DHS to detect, identify, monitor, and mitigate UAS threats at designated facilities and assets. DHS can share detection data and coordinate with critical infrastructure owners; the interdiction authority resides with DHS personnel, not with the infrastructure operators themselves.

## State vs. Federal Authority

Pre-FY2026, state and local governments had no C-UAS interdiction authority — only federal agencies named in 49 U.S.C. § 44810 could take action. Several states attempted to pass their own C-UAS laws; federal preemption under aviation law meant those statutes were generally unenforceable for interdiction.

Post-FY2026 NDAA, SLTT agencies can access interdiction authority under the SAFER SKIES pathway, but only after completing federal training and using federally approved systems. This is a new field and training programs were still being developed as of mid-2026.

The division of responsibility for critical infrastructure protection is roughly: **detect → private operators / SLTT**; **interdict → federal agencies or SLTT acting under SAFER SKIES authorization**.

## Notable Developments

- **2026-01:** FY2026 NDAA signed into law; SAFER SKIES Act creates first SLTT C-UAS interdiction pathway; $500M FEMA grant program for detection equipment announced
- **2025-10:** CISA releases three-document "Be Air Aware" guidance package for critical infrastructure operators
- **2024:** FAA Reauthorization Act 2024 extends DHS/DOJ/FAA C-UAS authorities through September 30, 2028; Counter-UAS Authority Security, Safety, and Reauthorization Act passed
- **2023-12:** American Security Drone Act signed as part of FY2024 NDAA; prohibits federal procurement of Chinese-manufactured UAS
- **2018:** FAA Reauthorization Act 2018 — first explicit C-UAS statutory authority for named federal agencies

## Key Organizations

- **CISA (DHS)** — primary civilian federal agency for critical infrastructure C-UAS coordination; "Be Air Aware" program
- **FAA** — airspace authority; Remote ID rulemaking; TFR authority
- **DOJ / FBI** — law enforcement interdiction authority at federal level; co-developing SLTT training program
- **Joint Interagency Task Force 401** (est. FY2026 NDAA) — DoD-led C-UAS coordination body
- **FCC** — enforces Communications Act jammer prohibition against unauthorized C-UAS systems

## Sources

- [Holland & Knight: Update on US Counter-UAS Authorities (2024)](https://www.hklaw.com/en/insights/publications/2024/07/update-on-us-counter-uas-authorities-and-efforts-to-address-threats) — comprehensive legal overview of 2018/2024 authorities
- [FAA Interagency Legal Advisory on UAS Detection and Mitigation](https://www.faa.gov/sites/faa.gov/files/uas/resources/c_uas/Interagency_Legal_Advisory_on_UAS_Detection_and_Mitigation_Technologies.pdf) — authoritative joint advisory on legal constraints
- [CISA: New Guides to Safeguard Critical Infrastructure from UAS Threats](https://www.cisa.gov/news-events/news/cisa-releases-new-guides-safeguard-critical-infrastructure-unmanned-aircraft-systems-threats) — October 2025 guidance announcement
- [CISA: UAS Detection Technology Guidance (Oct 2025 PDF)](https://www.cisa.gov/sites/default/files/2025-10/DetectionTech_20251030_508.pdf) — full detection tech guidance document
- [CISA: Be Air Aware — Protect Critical Infrastructure](https://www.cisa.gov/topics/physical-security/be-air-aware/protect-critical-infrastructure-and-public-gatherings) — program landing page
- [Route Fifty: FY2026 NDAA expanded counter-drone authority](https://www.route-fifty.com/digital-government/2026/01/defense-law-includes-expanded-counter-drone-authority/410542/) — SAFER SKIES Act summary
- [SAFER SKIES Act / FY26 NDAA C-UAS provisions explained](https://callmc.com/securing-the-skies-how-the-fy26-ndaa-empowers-your-agency-against-drone-threats/) — SLTT authority breakdown
- [Grab The Axe: C-UAS Legalities for Corporations](https://grabtheaxe.com/c-uas-legalities-corporations-navigating-faa-fcc-rules/) — FCC and FAA constraints for private entities
- [American Security Drone Act S.473 text (Congress.gov)](https://www.congress.gov/bill/118th-congress/senate-bill/473/text) — statute text
