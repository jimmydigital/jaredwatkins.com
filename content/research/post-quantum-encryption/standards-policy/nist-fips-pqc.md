---
title: "NIST FIPS & PQC Standardization"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "NIST's 8-year post-quantum cryptography standardization process, FIPS 203/204/205 specifications, and status of FIPS 206 and HQC"
tags: ["nist", "fips", "post-quantum", "standards", "ml-kem", "ml-dsa", "slh-dsa", "falcon", "hqc"]
categories: ["standards", "reference"]
research_area: "post-quantum-encryption/standards-policy"
source_urls:
  - "https://csrc.nist.gov/projects/post-quantum-cryptography"
  - "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf"
  - "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf"
  - "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf"
last_reviewed: 2026-04-24
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## The NIST Standardization Timeline

NIST's post-quantum cryptography standardization process took eight years from conception to first finalized standards, reflecting the rigor required for cryptographic algorithms that will protect critical infrastructure for decades.

| Phase | Dates | Key Milestones |
|-------|-------|---|
| **Announcement** | 2016 | NIST calls for submissions of quantum-resistant algorithms |
| **Submission Round** | 2017 | NIST receives 69 submissions from 25+ countries |
| **Evaluation (4 rounds)** | 2017–2022 | Global cryptanalytic community vets algorithms; rounds of elimination |
| **Selection** | July 2022 | NIST announces finalists and alternates |
| **Finalization** | August 2024 | FIPS 203, 204, 205 published; effective August 14, 2024 |
| **FALCON (FIPS 206)** | 2025–2026 | Draft phase; expected finalization 2025–2026 |
| **HQC (5th algorithm)** | March 2025 onwards | Selected March 11, 2025; draft standard expected ~2026, final ~2027 |

---

## Finalized FIPS Standards (August 2024)

### FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)

**Based on:** CRYSTALS-Kyber submission
**Published:** August 13, 2024 | [Federal Register Notice](https://www.federalregister.gov/documents/2024/08/14/2024-17956/)

**What it specifies:**
- Three parameterized variants: ML-KEM-512, ML-KEM-768, ML-KEM-1024
- Key generation, encapsulation, and decapsulation procedures with strict error handling
- Approved parameter sets for different security levels
- Side-channel resistance requirements and implementation guidance
- Random number generation requirements (DRBG compliance)

**Implementation notes:**
- ML-KEM-768 is the general-purpose recommendation
- ML-KEM-1024 is recommended for systems protecting data beyond 2030 or handling high-value national security information
- Larger key sizes: encapsulated keys are 768 or 1088 bytes (vs. ~32 bytes for ECDH)

---

### FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA)

**Based on:** CRYSTALS-Dilithium submission
**Published:** August 13, 2024

**What it specifies:**
- Three variants: ML-DSA-44, ML-DSA-65, ML-DSA-87
- Key generation, signing, and signature verification procedures
- Public key size: ~1312 bytes (ML-DSA-65) vs. ~64 bytes for ECDSA P-256
- Signature size: ~2420 bytes (ML-DSA-65) vs. ~64 bytes for ECDSA
- Deterministic signing to prevent side-channel leakage of private keys
- Batch verification procedures for performance

**Implementation notes:**
- ML-DSA-65 is the recommended general-purpose algorithm
- ML-DSA-87 provides higher security margin for long-term protection
- Certificate size inflation is a known deployment challenge

---

### FIPS 205: Stateless Hash-Based Digital Signature Standard (SLH-DSA)

**Based on:** SPHINCS+ submission
**Published:** August 13, 2024

**What it specifies:**
- SLH-DSA-SHA2-128s, SLH-DSA-SHA2-128f, and corresponding SHA3 variants
- Hash-tree based construction for signature generation
- No secret state required between signatures (unlike older XMSS designs)
- Conservative security margins based on well-understood hash function properties
- Signature size: ~7856 bytes (SLH-DSA-SHA2-128s) with smaller keys (~32 bytes)

**Use cases & implementation notes:**
- Good choice for systems where hash functions are already validated and heavily used
- Larger signature sizes make it less ideal for high-volume signing
- Statelessness eliminates concerns about key reuse or state corruption
- XMSS (an earlier stateful variant) remains useful for firmware signing

---

## In-Progress: FIPS 206 (FALCON / FN-DSA)

**Status as of April 2026:** Draft phase

**What FIPS 206 will specify:**
- FN-DSA (FALCON) algorithm for digital signatures
- FALCON derives security from the hardness of the NTRU lattice problem
- Signatures much smaller than ML-DSA (~660 bytes vs. ~2420 bytes)
- Fast signing and verification

**Timeline:**
- Expected draft FIPS in 2025–2026
- Finalization likely 2026

**Deployment considerations:**
- FALCON was deferred from initial standardization due to implementation complexity and side-channel concerns
- It is now being finalized with careful attention to constant-time implementation
- Strong signatures + smaller size make it attractive for certificates and resource-constrained devices

**Note on FALCON's complexity:** FALCON requires careful implementation to avoid timing attacks that leak the secret key. This has delayed its standardization compared to ML-KEM and ML-DSA, which have simpler constant-time requirements.

---

## HQC: The Fifth Algorithm (Selected March 2025)

**Announcement:** March 11, 2025 | [NIST Press Release](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption)

**Role in NIST suite:**
- Primary role: Backup KEM alongside ML-KEM
- Provides algorithm diversity; based on fundamentally different mathematical problem (code-based cryptography) rather than lattices
- Reduces risk of a single algorithmic weakness affecting both main and backup options

**Timeline:**
- Draft standard expected ~2026
- Final standard expected ~2027

**Why code-based cryptography matters:**
- ML-KEM's security relies on lattice hardness assumptions
- HQC's Hamming Quasi-Cyclic codes offer independent security basis
- This diversity strengthens overall cryptographic resilience

**Key technical properties:**
- Code-based schemes have long history of cryptanalysis (~40 years)
- HQC is based on Hamming codes, which are well-understood
- Larger public keys (~65 KB) compared to ML-KEM (~1 KB), but acceptable for many applications
- Deterministic structure enables formal security proofs

---

## Support Documents & Implementation Guidance

### NIST SP 800-227 (September 2025)
**[Recommendations for Key-Encapsulation Mechanisms](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-227.pdf)**

Comprehensive implementation guidance covering:
- Ephemeral key handling (never reuse ephemeral private keys)
- Hybrid KEM approaches (combining classical + PQC)
- The X-Wing KEM construction (ML-KEM + X25519 hybrid)
- Side-channel resistance guidance
- Error handling and validation procedures

### NIST SP 800-208 (October 2020)
**Stateful Hash-Based Digital Signature Schemes**

Predates FIPS 205 but remains authoritative on hash-based signatures (XMSS, LMS) for firmware signing and other use cases where statelessness is not required.

### NIST IR 8413 (September 2022)
**[Status Report on the Third Round of the NIST Post-Quantum Cryptography Standardization Process](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8545.pdf)**

Explains why candidates were selected, advanced, or eliminated. Documents cryptanalytic insights and implementation considerations.

---

## Key People at NIST

### Dustin Moody — Mathematician & PQC Project Lead

**Background:**
- Ph.D. in Mathematics (University of Washington, 2009)
- B.S. in Mathematics (Brigham Young University)
- Joined NIST in 2010 as a postdoc
- Research focus: Elliptic curves, computational number theory, cryptographic standards

**Role:**
- Heads the NIST Post-Quantum Cryptography project since 2012
- Led the selection, evaluation, and standardization of all three finalized FIPS (203–205)
- Manages the evaluation of HQC and FALCON
- Active in international cryptographic standards communities

**Significance:** Moody's mathematical rigor and careful shepherding of the 8-year process ensured both quality and broad acceptance of NIST's PQC standards globally.

### Lily Chen — Cryptography Group Lead

**Role:**
- Leads the Cryptographic Technology Group within NIST's Computer Security Division
- Oversees all NIST cryptographic standards work, including SHA-3, AES legacy support, and PQC
- Strategic direction for future standards efforts

---

## What's NOT Standardized (and Why)

### Classic McEliece (Code-Based KEM)
- **Status:** Not selected for initial standardization, but widely deployed
- **Why:** Public key sizes too large (~1 MB) for practical Internet use; better suited for resource-unconstrained scenarios or specialized applications
- **Legacy status:** Still considered a valid post-quantum option but not NIST-recommended for general use

### NTRU (Lattice-Based)
- **Status:** Withdrawn from consideration in later rounds
- **Why:** Superseded by ML-KEM and FALCON, which have superior security margins and cleaner mathematical properties
- **Cryptanalytic lessons:** NTRU's history of near-misses (attacks that came close to breaking it) motivated the more conservative approach in ML-KEM and FALCON

### SIKE/SIDH (Isogeny-Based) — The Cautionary Tale

**What happened:** On July 31, 2022, Wouter Castryck and Thomas Decru (KU Leuven) published a devastating key-recovery attack on SIDH (Supersingular Isogeny Diffie-Hellman) that broke the system in polynomial time.

**Attack method:**
- Exploited the torsion point information exchanged during SIDH protocol
- Relied on computing isogenies in higher-dimensional abelian varieties
- Practical: SIKEp434 broken in ~1 hour on a single core; SIKEp751 in ~21 hours

**Immediate impact:**
- NIST promptly removed SIKE from consideration in August 2022
- All public keys generated under SIKE were retroactively compromised
- SIKE was in the final standardization round when the break occurred

**Lesson:** This event underscores the value of cryptographic conservatism:
1. NIST's multi-round evaluation process caught this before finalization
2. Algorithm diversity matters—a single failed lattice scheme wouldn't have derailed standardization
3. Isogeny-based cryptography is fundamentally harder to analyze than lattices, hashes, or codes

**Reference:** [Castryck, W., & Decru, T. (2022). "An efficient key recovery attack on SIDH."](https://eprint.iacr.org/2022/975) IACR ePrint Archive.

---

## NIST's Ongoing Work (2026 Outlook)

1. **FIPS 206 finalization** — Expected 2025–2026 for FALCON
2. **HQC standardization** — Draft ~2026, final ~2027
3. **X.509 certificate extensions** — Guidelines for encoding PQC keys in certificates
4. **Protocol integration** — Coordinating with IETF on TLS 1.3, SSH, and IKEv2 integration
5. **Hardware implementations** — Validating cryptographic modules to FIPS 140-3 with PQC support

---

## Sources & Further Reading

- [NIST Post-Quantum Cryptography Project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [FIPS 203, 204, 205 Announcement](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)
- [HQC Selection Announcement](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption)
- [Federal Register Notice (August 2024)](https://www.federalregister.gov/documents/2024/08/14/2024-17956/)

