---
title: "Sitehop"
date: 2026-04-15
lastmod: 2026-04-15
draft: false
description: "UK startup building hardware-accelerated post-quantum cryptography networking appliances; FPGA-based PQC IPsec at line rate; spin-out from University of Bristol."
tags: ["post-quantum", "cryptography", "networking", "pqc", "ike-pqc", "ml-kem", "hybrid-pqc", "uk", "emerging"]
categories: ["company"]
research_area: "post-quantum-encryption/networking"
source_urls:
  - "https://www.sitehop.io"
  - "https://www.sitehop.io/technology"
  - "https://www.sitehop.io/products"
last_reviewed: 2026-04-15
stale_after_days: 90
---

## Summary

Sitehop is a Bristol, UK-based startup building hardware-accelerated post-quantum cryptography (PQC) networking appliances. The company's core claim is that PQC algorithms — specifically the lattice-based KEMs now standardized by NIST — impose performance penalties severe enough on software-only implementations that line-rate encryption at scale requires FPGA or dedicated silicon acceleration. Sitehop's approach integrates ML-KEM (Kyber) and related algorithms directly into FPGA-based IPsec appliances, targeting enterprise and government customers concerned about the harvest-now-decrypt-later (HNDL) threat. The company emerged from the University of Bristol's cryptography research community.

## Key Facts

- **Founded:** Circa 2020–2021 (exact date not confirmed from public sources)
- **Type:** Company (private, startup)
- **HQ:** Bristol, UK
- **Origin:** University of Bristol spin-out
- **Stage:** Early-to-growth stage (Series A; exact funding not confirmed from public sources)
- **Focus:** FPGA-accelerated PQC IPsec networking appliances
- **Primary algorithm:** ML-KEM (CRYSTALS-Kyber / FIPS 203); hybrid PQC + classical key exchange
- **Protocol layer:** IKEv2/IPsec; also reportedly TLS
- **Status:** Active; products shipping as of reported timelines (verification needed)
- **Key differentiator:** Hardware acceleration enables PQC at line rate without CPU overhead; contrasts with software-only PQC added to existing platforms by major vendors

## What It Is / How It Works

Sitehop's core architectural argument is that the leading NIST-standardized PQC algorithms (ML-KEM, ML-DSA) have substantially larger computational costs than the ECDH/ECDSA operations they replace. In software implementations on general-purpose CPUs, this cost is manageable for low-throughput connections but degrades performance at high line rates or in environments where many simultaneous IPsec tunnels must be established and rekeyted. Traditional networking vendors adding PQC to existing platforms do so in software, meaning the performance penalty is absorbed by the same CPUs that handle routing, packet forwarding, and other tasks.

Sitehop addresses this by offloading PQC cryptographic operations to FPGAs (Field-Programmable Gate Arrays). An FPGA can execute the matrix multiplication operations at the heart of lattice-based algorithms in hardware, in parallel, without competing with CPU-bound tasks. The result is claimed line-rate PQC IPsec — the encryption and key exchange overhead does not reduce throughput below the physical link capacity.

The company implements IKEv2 with PQC KEM extensions (aligned with IETF RFC 9242 and RFC 9370), supporting hybrid key exchange — classical ECDH combined with ML-KEM so that the session key is secure even if one component is broken. This hybrid approach is the recommended transition path from NIST and IETF.

Sitehop's products are positioned at the network edge and in core infrastructure where dedicated encryption hardware is an established category (similar to hardware security modules or traditional crypto accelerators from vendors like Thales, nCipher, or Intel QAT).

## Notable Developments

- **2024–2025:** Company reportedly shipping early production units to UK government and defence customers; specific contracts and dates not confirmed from public sources — see Claim Verification below.
- **2024-08:** NIST published FIPS 203 (ML-KEM) and FIPS 204 (ML-DSA) as final standards. Sitehop's algorithm implementations are aligned with these finals (previously aligned to pre-standard Kyber/Dilithium drafts).
- **2023–2024:** Demonstrated PQC IPsec performance benchmarks at networking security events; specific figures require verification.
- **~2021:** Founded as University of Bristol spin-out; early UK government research funding reported.

<!-- TODO: Confirm founding date from Companies House (UK) or press records -->
<!-- TODO: Confirm Series A funding amount and investors from Crunchbase or press -->
<!-- TODO: Verify specific FPGA platform used (Xilinx/AMD Versal? Intel Agilex?) -->
<!-- TODO: Verify UK government contract specifics if publicly disclosed -->

## Key People

<!-- TODO: Identify and document founders and key executives from LinkedIn and University of Bristol pages -->
<!-- TODO: Confirm CEO, CTO, and Chief Cryptographer roles and LinkedIn profiles -->

*Research needed: Sitehop's leadership team is not prominently documented in public sources as of April 2026. The company emerged from the University of Bristol cryptography group; likely founders include faculty or PhD alumni from that program.*

### People — Last Reviewed: 2026-04-15

## Claim Verification

### Claim: Line-rate PQC IPsec without CPU performance penalty via FPGA acceleration

**Status:** Partially verified

**Supporting sources:**
- [Sitehop Technology Page](https://www.sitehop.io/technology) — Company description of FPGA-based acceleration architecture; aligns with known FPGA cryptography acceleration approaches used in other sectors
- Academic literature on FPGA ML-KEM/Kyber implementation (multiple groups have demonstrated high-throughput FPGA Kyber; the general claim of FPGA advantage for lattice cryptography is technically well-supported in the research literature)

**Refuting / questioning sources:**
- No independent third-party benchmark of Sitehop hardware against software-only PQC implementations has been identified from public sources as of April 2026
- Software PQC performance has improved significantly with CPU instruction set extensions (AES-NI analogue developments); the gap between software and hardware PQC may narrow as vendor CPU support matures

**Summary:** The general architectural claim (FPGA accelerates lattice-based PQC better than software-only CPU implementation) is technically sound and supported by academic research, but Sitehop-specific performance figures have not been independently verified.

---

### Claim: Products in active deployment with UK government / defence customers

**Status:** Unverified

**Supporting sources:**
- Company website implies active deployment; UK context and University of Bristol pedigree are consistent with NCSC (National Cyber Security Centre) engagement pipelines

**Refuting / questioning sources:**
- No specific UK government contract awards identified in public procurement records as of April 2026; OJEU/Find a Tender records not searched exhaustively

**Summary:** Active UK government deployment is claimed but no independently verifiable contract data has been found. This is common for early-stage UK defence/security vendors given procurement confidentiality norms, but absence of public evidence means the claim remains unverified.

## Sources

- [Sitehop Website](https://www.sitehop.io) — Company overview and product pages
- [Sitehop Technology](https://www.sitehop.io/technology) — Architecture description
- [Sitehop Products](https://www.sitehop.io/products) — Product line overview
- [NIST FIPS 203 (ML-KEM)](https://csrc.nist.gov/pubs/fips/203/final) — Underlying standard for Sitehop's KEM implementation
- [IETF RFC 9242](https://www.rfc-editor.org/rfc/rfc9242) — Intermediate Exchange in IKEv2 (PQC KEM framework)
- [IETF RFC 9370](https://www.rfc-editor.org/rfc/rfc9370) — Multiple Key Exchanges in IKEv2

<!-- TODO: Add University of Bristol spin-out announcement or research group link -->
<!-- TODO: Add Crunchbase profile link once confirmed -->
