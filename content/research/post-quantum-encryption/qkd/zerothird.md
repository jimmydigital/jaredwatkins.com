---
title: "zerothird"
date: 2026-06-02
lastmod: 2026-06-02
draft: false
description: "Austrian startup commercializing entanglement-based Quantum Key Distribution (eQKD) for enterprise and critical infrastructure, founded by alumni of Anton Zeilinger's Nobel Prize-winning quantum lab at IQOQI Vienna."
tags: ["qkd", "quantum-security", "cryptography", "photonics", "eu", "austria", "startup", "emerging"]
categories: ["company"]
research_area: "post-quantum-encryption/qkd"
source_urls:
  - "https://zerothird.com"
  - "https://zerothird.com/about-us"
  - "https://zerothird.com/technology/zerothird-differentiators"
  - "https://zerothird.com/products/quantum-key-distribution"
  - "https://zerothird.com/news/verbund-x-ventures-invests-in-zerothird"
  - "https://zerothird.com/news/zerothird-implements-pilot-with-erste-group-and-a1-telekom-austria-ag"
last_reviewed: 2026-06-02
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

zerothird (legal entity: Quantum Industries GmbH) is a Vienna-based startup commercializing entanglement-based Quantum Key Distribution (eQKD) systems for enterprise and critical infrastructure. The company was founded by researchers from Anton Zeilinger's Nobel Prize-winning quantum lab at the Institute for Quantum Optics and Quantum Information (IQOQI Vienna), and positions its technology as physics-guaranteed cryptographic security immune to both classical and quantum attacks.

## Key Facts

- **Founded:** 2024 (GmbH transition completed February 2026 per company announcement)
- **Headquarters:** Vienna, Austria
- **Type:** Private company (startup)
- **Stage:** Seed+ (VERBUND X Ventures lead investor, March 2026)
- **Technology:** Entanglement-based QKD (eQKD), BBM92 protocol-inspired
- **Key range:** Up to 350 km without trusted relay nodes (claimed)
- **Products:** S10 photon source, D11 photon receiver, Key-as-a-Service (KaaS), lab equipment
- **Use cases:** Metro eQKD, long-distance eQKD, fully connected networks
- **Supported by:** Austrian federal funding ("Seedfinancing – Deep Tech," BMAW and BMK, managed by aws)

## What It Is / How It Works

zerothird builds hardware and managed services around entanglement-based QKD, specifically an architecture inspired by the BBM92 protocol. In standard prepare-and-measure QKD (e.g., BB84), a transmitter sends encoded photons to a receiver — which requires trust in the photon source, since a compromised source could allow interception without disturbing quantum states. The BBM92 entanglement-based approach avoids this: a central source generates polarization-entangled photon pairs, delivering one photon of each pair to each endpoint. Each party measures its photon independently; the correlated outcomes yield a shared key without the key ever being transmitted. Because entanglement correlations are intrinsic to the quantum state, there is no "source" the adversary can subvert.

The company's hardware consists of the **S10** photon source (produces entangled pairs) and the **D11** receiver (detects incoming photons using superconducting nanowire single-photon detectors, or SNSPDs). The use of superconducting detectors is a claimed differentiator — they offer higher detection efficiency and lower noise than conventional avalanche photodiode-based detectors, supporting longer-distance key distribution.

zerothird offers three commercial deployment configurations: **Metro eQKD** for intra-city multi-building deployments; **Long-Distance eQKD** for inter-city fiber links; and **Fully Connected Networks**, where a single photon source distributes entangled pairs to multiple endpoints, creating a star topology with one key pair per communication link. The **Key-as-a-Service (KaaS)** model delivers quantum keys as a managed service over the customer's existing fiber infrastructure with minimal operational overhead from the customer side.

The technology is described as resistant to harvest-now-decrypt-later (HNDL) attacks by design: QKD-distributed keys are symmetric and ephemeral, so there is no public-key math for a future quantum computer to break retroactively.

## Notable Developments

- **2026-03:** VERBUND X Ventures announced as lead investor in Seed+ funding round.
- **2026-02:** zerothird GmbH incorporation formalized (prior entity was Quantum Industries GmbH).
- **2026-02:** Announced quantum-secure banking pilot with Erste Group and A1 Telekom Austria AG; described as an inter-organizational eQKD deployment over A1's fiber network.
- **2026-01:** Pilot received international media attention as a notable early commercial eQKD deployment.
- **2025-12:** Hosted open house event week in Vienna.
- **2025-11:** Hosted "QUANTUM-SECURE NOW" event in Linz, Austria.
- **2026-05:** Attended CDL Super Session 2026 (Toronto Tech Week) and Cisco Live Las Vegas (May–June 2026).
- **2026-06:** Participated in QSNP Industry Hub Day 2026 (Paris).

## Key People

- **Felix Tiefenbacher** — Co-Founder and CEO. Previously CEO and founder of HELIOVIS (solar energy startup, ~15 years). Prior to that, led a quantum cryptography startup with Nobel laureate Prof. Anton Zeilinger; postdoctoral researcher at IQOQI Vienna. LinkedIn: [felix-tiefenbacher](https://www.linkedin.com/in/felix-tiefenbacher/) — *verify URL*
- **Rupert Ursin** — Co-Founder and CEO of qtlabs (zerothird's sister entity focused on space-based quantum communication). Senior Group Leader and former Deputy Director at IQOQI Vienna. Leading quantum scientist; background in long-distance quantum communication experiments. LinkedIn: not found in public search.
- **Thomas Scheidl** — Co-Founder, Senior Advisor. CEO and Co-Founder of qtlabs alongside Ursin. 8+ years at IQOQI Vienna; contributed to Quantum Experiments at Space Scale (QUESS/Micius satellite) project. LinkedIn: not found in public search.
- **Thomas Heine** — Co-Founder, Head of Product Development and Production. 9 years leading R&D and production at XARION (laser acoustics); 11 years at TOPTICA Photonics developing miniaturized lasers for quantum technology applications. **⚑ Overlap:** TOPTICA Photonics is a Munich-based laser company that supplies equipment to multiple quantum technology labs and companies across Europe — potential shared supplier relationship with other documented quantum sector entries.
- **Christoph Thaler** — CFO. Background in M&A and corporate finance advisory for private equity and technology companies. CFA charterholder; master's in international business.
- **Lukas Helm** — Head of Sales.

### People — Last Reviewed: 2026-06-02

## Claim Verification

### Claim: QKD key distribution up to 350 km without trusted relay nodes

**Status:** Partially verified

**Supporting sources:**
- [zerothird Differentiators page](https://zerothird.com/technology/zerothird-differentiators) — company claims 350 km range with superconducting detectors and entanglement-based architecture eliminating relay nodes.
- Entanglement-based QKD over fiber at 100–300 km range has been demonstrated academically (e.g., IQOQI Vienna group published long-distance entanglement distribution results). zerothird's founders were core members of this group, providing scientific lineage for the claim.

**Refuting / questioning sources:**
- No independent third-party lab verification of zerothird's specific hardware achieving 350 km was found in public sources as of June 2026.
- Practical fiber QKD at 350 km requires extremely low-loss fiber and high-efficiency SNSPD detectors cooled to millikelvin temperatures — significant operational complexity not addressed in public marketing materials.

**Summary:** The 350 km claim is scientifically plausible based on published academic work from the founders' prior research group; no independent product validation found as of this writing.

---

### Claim: Erste Group / A1 Telekom Austria banking pilot

**Status:** Partially verified

**Supporting sources:**
- [zerothird news release, February 2026](https://zerothird.com/news/zerothird-implements-pilot-with-erste-group-and-a1-telekom-austria-ag) — company announcement of the pilot.
- [Media coverage announcement, March 2026](https://zerothird.com/news/media-cover-breakthrough) — references "major media" covering the pilot; specific outlets not named on the zerothird page.

**Refuting / questioning sources:**
- No independent published results, transaction volumes, or technical specifications from Erste Group or A1 Telekom were found in public sources. The announcement is currently company-issued only.

**Summary:** Pilot existence is confirmed by company announcement and referenced media attention; technical performance or operational scope not independently verifiable.

## Sources

- [zerothird.com](https://zerothird.com) — company website, product descriptions, use cases
- [About Us](https://zerothird.com/about-us) — founder and team backgrounds
- [zerothird Differentiators](https://zerothird.com/technology/zerothird-differentiators) — technical architecture claims, 350 km range, BBM92/SNSPD approach
- [VERBUND X Ventures Seed+ Investment](https://zerothird.com/news/verbund-x-ventures-invests-in-zerothird) — most recent funding round
- [Erste Group / A1 Pilot Announcement](https://zerothird.com/news/zerothird-implements-pilot-with-erste-group-and-a1-telekom-austria-ag) — first named commercial pilot
