---
title: "Juniper Networks — PQC Support"
date: 2026-04-15
lastmod: 2026-04-15
draft: false
description: "Post-quantum cryptography implementation status and roadmap for Juniper Networks (acquired by HPE 2024): Junos OS PQC support, IKEv2 integration, and product coverage."
tags: ["post-quantum", "cryptography", "networking", "pqc", "ike-pqc", "ml-kem", "hybrid-pqc", "us", "enterprise"]
categories: ["company"]
research_area: "post-quantum-encryption/networking"
source_urls:
  - "https://www.juniper.net"
  - "https://www.juniper.net/documentation/"
  - "https://www.juniper.net/us/en/research-topics/quantum-safe-networking.html"
last_reviewed: 2026-04-15
stale_after_days: 90
---

## Summary

Juniper Networks, acquired by Hewlett Packard Enterprise in March 2024, produces enterprise routers, switches, firewalls (SRX series), and SD-WAN products running Junos OS. Juniper has published PQC intent as part of its quantum-safe networking posture and has been involved in IETF standardization for IKEv2 PQC extensions. Specific GA-shipping PQC support in Junos, the exact software versions, and the algorithms covered require verification against current Junos release notes. This entry documents the known state as of April 2026 and flags open research questions.

## Key Facts

- **Founded:** 1996
- **Type:** Company (acquired by HPE March 2024; formerly NASDAQ: JNPR)
- **HQ:** Sunnyvale, CA, USA (now HPE division)
- **Parent:** Hewlett Packard Enterprise (NYSE: HPE) — acquisition completed March 2024
- **Key products:** MX Series routers, SRX Series firewalls, EX/QFX switches, Mist AI (cloud-managed networking), SD-WAN
- **Primary OS:** Junos OS (routers, firewalls); Junos Evolved (newer platforms); Mist platform
- **PQC focus area:** IKEv2/IPsec in SRX and MX platforms
- **PQC status:** Roadmap announced; specific GA release details require verification
- **Key PQC protocol:** IKEv2 with RFC 9242/9370 KEM extensions

## What It Is / How It Works

Juniper's PQC effort is concentrated on IPsec VPN and encrypted tunnel infrastructure, where IKEv2 is the key exchange protocol. The company has been a participant in IETF discussions on PQC for IKEv2 (the mechanisms eventually standardized in RFC 9242 and RFC 9370).

**IKEv2 PQC integration:** IKEv2 PQC support works by adding an additional Key Exchange payload to the IKE_SA_INIT and IKE_AUTH exchanges. RFC 9370 allows multiple key exchange rounds — the classical (ECDH) exchange happens first, then a PQC KEM (ML-KEM) exchange in a subsequent round. The combined shared secret is the input to session key derivation, achieving hybrid security. Juniper's implementation, where confirmed, follows this framework.

**Junos OS versioning:** Juniper releases Junos updates quarterly; PQC features are typically gated behind specific release trains. Users should consult the official [Junos release notes](https://www.juniper.net/documentation/) for the current PQC feature set. This entry does not substitute for the official documentation — it provides a research-level summary of what is known from public sources.

**HPE integration implications:** The March 2024 HPE acquisition means Juniper's roadmap is now partly governed by HPE strategy. HPE has its own quantum-safe initiative (HPE has published quantum-safe intent for Aruba networking products). Whether Juniper and Aruba PQC roadmaps will converge under HPE is unclear as of April 2026.

## Notable Developments

- **2024-03:** Juniper Networks acquisition by HPE completed. Juniper now operates as a division of HPE. The JNPR ticker delisted.
- **2024-08:** NIST published FIPS 203/204/205. Juniper's PQC roadmap, if previously aligned to draft Kyber/Dilithium, must be updated to reference the final FIPS standards.
- **2023–2024:** Juniper published documentation on "quantum-safe" networking positioning; specific Junos release with GA PQC IKEv2 support requires verification from release notes.
- **2022–2023:** IETF activity on IKEv2 PQC (RFC 9242 published June 2022; RFC 9370 published May 2023); Juniper was participating in IETF discussions during this period.

<!-- TODO: Identify the specific Junos OS release that first shipped PQC IKEv2 support -->
<!-- TODO: Confirm which algorithms are supported: ML-KEM-768? ML-KEM-1024? Pre-standard Kyber? -->
<!-- TODO: Confirm which product platforms (SRX? MX? All?) support PQC in IKEv2 -->
<!-- TODO: Verify whether Juniper has published FIPS 140-3 validation roadmap for PQC module -->
<!-- TODO: Check HPE Aruba PQC roadmap and note overlap/alignment with Juniper roadmap -->
<!-- TODO: Identify Juniper engineers/architects who have published on PQC (IETF drafts, blogs) -->

## Key People

<!-- TODO: Identify Juniper/HPE security engineering leads for PQC program -->
<!-- TODO: Check IETF draft authors on RFC 9242/9370 for Juniper-affiliated contributors -->

*Research needed: Juniper's internal PQC team and key contacts are not prominently documented from public sources as of April 2026.*

### People — Last Reviewed: 2026-04-15

## Claim Verification

### Claim: Juniper supports post-quantum IKEv2 in Junos OS

**Status:** Partially verified

**Supporting sources:**
- [Juniper quantum-safe networking page](https://www.juniper.net/us/en/research-topics/quantum-safe-networking.html) — Marketing-level description of Juniper's PQC intent; language is positioning rather than specific technical documentation
- IETF RFC 9242 and RFC 9370 provide the technical framework Juniper has referenced; the standards themselves are finalized and verifiable
- Juniper has published technical blog posts referencing PQC readiness (specific posts require URL verification)

**Refuting / questioning sources:**
- Specific Junos OS release notes confirming GA PQC IKEv2 availability have not been confirmed from public sources as of April 2026 — Juniper's documentation portal requires account login for detailed release notes
- "Quantum-safe" and "quantum-ready" language on vendor websites routinely precedes actual shipping support; Juniper's marketing claims have not been independently validated against shipping software

**Summary:** Juniper has publicly committed to PQC IKEv2 support and has the technical framework (IETF RFCs) to implement it; whether the feature is currently GA in a supported Junos release is unconfirmed from public sources.

---

### Claim: Hybrid PQC key exchange (classical + ML-KEM) is the implemented approach

**Status:** Unverified

**Supporting sources:**
- This is the recommended approach per NIST and IETF; consistent with RFC 9370 framework that Juniper has referenced

**Refuting / questioning sources:**
- No specific technical documentation confirming Juniper's current implementation is hybrid (vs. PQC-only or classical-only with a future PQC flag) has been independently reviewed

**Summary:** Hybrid is the expected and recommended approach; Juniper's implementation specifics need confirmation from current Junos release notes.

## Sources

- [Juniper Networks](https://www.juniper.net) — Company website
- [Juniper Documentation Portal](https://www.juniper.net/documentation/) — Official Junos release notes (account required for full access)
- [Juniper Quantum-Safe Networking](https://www.juniper.net/us/en/research-topics/quantum-safe-networking.html) — Public-facing PQC positioning page
- [IETF RFC 9242](https://www.rfc-editor.org/rfc/rfc9242) — Intermediate Exchange in IKEv2
- [IETF RFC 9370](https://www.rfc-editor.org/rfc/rfc9370) — Multiple Key Exchanges in IKEv2
- [NIST FIPS 203 (ML-KEM)](https://csrc.nist.gov/pubs/fips/203/final) — KEM standard referenced in PQC IKEv2 implementations
- [HPE / Juniper acquisition announcement](https://www.hpe.com/us/en/newsroom/press-release/2023/01/hpe-to-acquire-juniper-networks-to-accelerate-ai-driven-networking.html) — Context for corporate structure

<!-- TODO: Add Junos release notes URL for first PQC-capable release once identified -->
<!-- TODO: Add HPE quantum-safe strategy document if publicly available -->
