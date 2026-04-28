---
title: "International Standards Bodies & Divergence"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "ETSI, BSI, NCSC, ANSSI, ISO/IEC, and China OSCCA post-quantum cryptography standards and convergence analysis"
tags: ["international", "etsi", "bsi", "ncsc", "anssi", "iso", "china", "oscca", "standards-divergence"]
categories: ["standards", "international"]
research_area: "post-quantum-encryption/standards-policy"
source_urls:
  - "https://www.etsi.org/committee/cyber"
  - "https://www.bsi.bund.de"
  - "https://www.ncsc.gov.uk"
  - "https://www.anssi.gouv.fr"
  - "https://www.iso.org"
last_reviewed: 2026-04-24
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Overview: Global Standards Divergence & Alignment

As of April 2026, the post-quantum cryptography standardization landscape is **largely converging** on NIST's FIPS algorithms at the technical level, but significant **geopolitical and strategic divergence** exists at the policy and national sovereignty level. Europe is largely harmonizing with NIST; the UK is aligned; China is charting an independent course.

---

## Europe: ETSI (European Telecommunications Standards Institute)

### ETSI TC CYBER — Quantum-Safe Cryptography Working Group

ETSI, based in France, is Europe's primary standards body for telecommunications and IT. Its Technical Committee CYBER has an active PQC working group.

#### ETSI TR 103 616: Quantum-Safe Signatures (September 2021)

**Status:** ✅ **PUBLISHED** | [ETSI Deliverable](https://www.etsi.org/deliver/etsi_tr/103600_103699/103616/01.01.01_60/tr_103616v010101p.pdf)

**Scope:** Overview and comparison of post-quantum digital signature algorithms.

**Coverage:**
- CRYSTALS-Dilithium (now ML-DSA) — Recommended
- CRYSTALS-Kyber (now ML-KEM) — Covered, recommended for KEMs
- SPHINCS+ (now SLH-DSA) — Covered, recommended
- FALCON — Covered, noted for smaller signatures
- Rainbow, GeMSS, PICNIC — Analyzed; not recommended (security margin concerns)

**Key contribution:** Provides unified notation and terminology across PQC schemes, facilitating understanding and comparison. Non-prescriptive but aligns with NIST selections.

#### ETSI TS 104 015: Quantum-Safe Hybrid Key Establishment (February 2025)

**Status:** ✅ **PUBLISHED** (February 2025) | Official ETSI Technical Specification

**Title:** "Efficient Quantum-Safe Hybrid Key Exchanges with Hidden Access Policies"

**Core innovation:** Covercrypt — a Key Encapsulation Mechanism with Access Control (KEMAC).

**What it specifies:**
- **Hybrid KEM design:** Combines classical (ECDH) + post-quantum (ML-KEM) in a unified framework
- **Access control:** Cryptographic enforcement of access policies (e.g., decrypt only if authorized)
- **Pre- and post-quantum security:** Achieves quantum resistance + classical confidentiality simultaneously

**Difference from IETF approach:**
- IETF (RFC 9370): Concatenates two independent KEMs (ECDH || ML-KEM)
- ETSI TS 104 015: Integrates access control layer into hybrid KEM itself

**Deployment:** Conceptual framework; industry adoption TBD. More research-oriented than operational.

#### ETSI Relationship to NIST Standards

**Alignment:** 🟢 **STRONG**

- ETSI has explicitly adopted NIST FIPS 203, 204, 205 as the basis for European deployment recommendations
- ETSI TR 103 616 and TS 104 015 are **complementary**, not competitive, to NIST standards
- European organizations follow NIST algorithm recommendations; ETSI provides additional implementation guidance and European-specific context

**Why alignment:** ETSI members include major European vendors (Ericsson, Nokia, Siemens, Orange) who need interoperability with global standards. Full divergence would fragment the market.

---

## Germany: BSI (Bundesamt für Sicherheit in der Informationstechnik)

### BSI Technical Guidelines TR-02102 Series

Germany's Federal Office for Information Security (BSI) publishes **TR-02102: Cryptographic Methods: Recommendations and Key Lengths**, updated annually since 2013.

#### TR-02102-1 (January 2026 Update)

**Key PQC Recommendations:**

**Recommended KEMs (Key Encapsulation):**
- **ML-KEM** (NIST FIPS 203) — Primary recommendation (finalized August 2024)
  - ML-KEM-768 for 128-bit security
  - ML-KEM-1024 for 192-bit security and beyond
  - Recommended for deployment in German government, critical infrastructure, and enterprise systems
  
- **FrodoKEM** — Alternative (code-based)
  - Based on Frodo learning-with-errors scheme
  - Larger keys/ciphertexts than ML-KEM but independently evaluated
  - Recommended as diversity mechanism
  
- **Classic McEliece** — Alternative (code-based)
  - Long history of cryptanalysis
  - Large public keys (~1 MB) limit practical use
  - Viable for archival/long-term security where size not critical

**Recommended Digital Signatures:**
- **ML-DSA** (NIST FIPS 204) — Primary (finalized August 2024)
  - ML-DSA-65 for 128-bit security
  - ML-DSA-87 for 192-bit security
  
- **XMSS** (SP 800-208) — Stateful hash-based signatures
  - Good for firmware/code signing
  - Simpler than stateless alternatives
  
- **SLH-DSA** (NIST FIPS 205) — Stateless hash-based signatures
  - Conservative security margin
  - No state management risk

#### BSI Hybrid Cryptography Requirement

**Critical policy:** Post-quantum schemes should **only be deployed in hybrid mode** (paired with classical algorithms) "if possible" per BSI guidelines.

**Rationale:**
1. If PQC algorithm is broken, classical algorithm provides fallback security
2. Dual protection eliminates risk of single-algorithm failure
3. Smooth transition without flashover to unproven algorithms

**Hybrid deployment model BSI endorses:**
```
Encrypted_data = ClassicalEncrypt(data) || PQCEncrypt(data)
Verification = ClassicalVerify() AND PQCVerify()
```

**Implementation guideline:** Use composite KEMs or sequential application of multiple algorithms. Ensure both succeed to proceed.

#### BSI Alignment with NIST

**Alignment:** 🟢 **STRONG**

BSI explicitly references NIST FIPS standards and recommends their adoption for German organizations. However, BSI adds the **requirement for hybrid deployment**, which is stronger than NIST's (NIST recommends but doesn't mandate hybrid for all use cases).

**Difference in philosophy:**
- **NIST:** Recommends PQC-only deployment once algorithms mature
- **BSI:** Mandates hybrid during transition; hybrid may remain indefinitely for highest-assurance systems

---

## United Kingdom: NCSC (National Cyber Security Centre)

### NCSC Post-Quantum Cryptography Migration Guidance (March 2025)

The UK National Cyber Security Centre published comprehensive PQC guidance in March 2025, establishing a **three-phase migration roadmap** for organizations.

#### NCSC Recommended Algorithms

- **ML-KEM-768, ML-KEM-1024** — NIST FIPS 203 endorsed
- **ML-DSA-65, ML-DSA-87** — NIST FIPS 204 endorsed
- **SLH-DSA** — NIST FIPS 205 endorsed
- **XMSS/LMS** — For firmware/code signing

#### NCSC Three-Phase Timeline

| Phase | Years | Actions | Deadline |
|-------|-------|---------|----------|
| **Phase 1** | 2024–2028 | Identify systems needing PQC upgrade; build migration plans; test PQC in pilot systems | — |
| **Phase 2** | 2028–2031 | Deploy high-priority upgrades; achieve hybrid PQC support across infrastructure; refine rollout strategy | — |
| **Phase 3** | 2031–2035 | Complete migration to PQC for all systems, services, and products; deprecate classical algorithms | **2035 (full PQC)** |

**Key difference from U.S. timelines:**
- NCSC allows 10 years (2025–2035) for full migration
- U.S. NSA/CNSA 2.0 sets 2033 deadline for NSS (8 years)
- U.S. civilian agencies (CISA) target 2035 (similar to NCSC)

#### NCSC 2025–2026 Expectations

- **Cryptographic hardware** (HSMs, secure boots) using NIST standards expected to become available in **late 2025**
- **FIPS 140-3 validations** for cryptographic modules with PQC support expected by **late 2025–2026**
- Organizations should begin **pilot deployments** in 2026

#### NCSC Alignment with NIST

**Alignment:** 🟢 **VERY STRONG**

NCSC has explicitly endorsed NIST FIPS 203, 204, 205 as the basis for UK government and critical infrastructure migration. No divergence; NCSC provides additional planning and implementation guidance on top of NIST standards.

---

## France: ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information)

### ANSSI Post-Quantum Cryptography Guidance (Status: 2025–2026)

France's cybersecurity agency (ANSSI) has issued early PQC recommendations, broadly aligned with NIST and ETSI.

**Key points:**
- Endorses NIST FIPS 203, 204, 205 for government and critical infrastructure
- Recommends hybrid deployment during transition (similar to BSI)
- French critical infrastructure (energy, finance, healthcare) following ANSSI guidance

**Unique French element:** Active monitoring of **European cryptographic sovereignty**—ensuring Europe is not dependent on U.S. algorithms (though no current ANSSI proposal diverges from NIST).

#### ANSSI Alignment

**Alignment:** 🟢 **STRONG** with emphasis on European digital sovereignty

---

## ISO/IEC JTC 1/SC 27: International Standardization

The International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC) jointly maintain IT security standards through **JTC 1 (Information Technology) Subcommittee 27 (Security)**.

### ISO/IEC 18033-x: Encryption Algorithms

**Current status (2026):**
- ISO/IEC 18033-2: Public-key encryption — Being updated to include ML-KEM, FALCON, and other NIST-standardized PQC KEMs
- ISO/IEC 18033-3: Digital signatures — Being updated to include ML-DSA, SLH-DSA, XMSS/LMS

**Timeline:**
- Draft standards in development; expected publication **2026–2027**
- Will formally adopt NIST FIPS algorithms with ISO/IEC numbering and OIDs

**Effect:** Once ISO standards are published, global enterprises using ISO/IEC frameworks will have official certification path for PQC compliance.

---

## China: OSCCA (Office of State Commercial Cryptography Administration) — Divergence

### China's Independent PQC Initiative (February 2025)

China is **NOT adopting NIST PQC standards** at the national level. Instead, the Institute of Commercial Cryptography Standards (ICCS), under OSCCA, announced in **February 2025** a global call for quantum-resistant algorithm proposals.

#### Why the Divergence?

1. **Cryptographic sovereignty:** China has maintained independent cryptographic standards (SM2, SM3, SM4) for decades; fully adopting NIST algorithms conflicts with this doctrine
2. **Geopolitical tension:** Post-quantum standards carry strategic weight; U.S. dominance in PQC standardization is seen as technological hegemony
3. **Supply chain security:** China seeks domestic control over cryptographic infrastructure
4. **National champion algorithms:** OSCCA wants home-grown PQC alternatives

#### China's Current Quantum Key Distribution Standards

China HAS published standards for quantum key distribution (QKD):
- **GB/T 42829-2023** — Quantum key distribution protocol requirements
- **GB/T 43692-2024** — Quantum key distribution network security requirements
- **YD/T 3834.1-2021** — Telecom QKD standards
- **GM/T 0108-2021** — QKD for commercial cryptography

**Important distinction:** QKD ≠ PQC. China's QKD standards are for quantum-secured key exchange using quantum mechanics (not yet post-quantum cryptography). QKD is orthogonal to NIST PQC.

#### OSCCA 2025 PQC Proposal Call

In February 2025, ICCS issued a **global solicitation for post-quantum cryptographic algorithm proposals** across multiple categories:

- **Public-key encryption/key exchange (KEMs)**
- **Digital signatures**
- **Quantum-resistant hash functions**
- **Quantum-resistant block ciphers**

**Timeline:** Proposals accepted through **late 2025**; evaluation and standardization process **2025–2027**.

**Strategic implication:** If China develops its own PQC standards, organizations operating in China (or serving Chinese customers) will face **dual-standards compliance** requirements: NIST PQC for international markets, OSCCA PQC for China.

#### Competitive Landscape

| Region | Standard | Algorithms | Adoption Rate |
|--------|----------|-----------|--------------|
| **U.S. & Allies** | NIST FIPS 203/204/205 | ML-KEM, ML-DSA, SLH-DSA | 80%+ of global tech companies |
| **Europe** | ETSI/ISO (aligned w/ NIST) | Same as NIST | ~70% of EU organizations |
| **China** | OSCCA (under development) | TBD; proposed 2025–2027 | —, ~0% globally as of 2026 |

---

## Convergence vs. Divergence Summary (April 2026)

### Convergence Drivers

1. **Internet standards (IETF):** Global protocols (TLS, SSH, IKEv2) must be algorithm-agnostic; NIST FIPS chosen to minimize fragmentation
2. **Market economics:** Vendors (Palo Alto, Juniper, OpenSSL) implement NIST PQC once; multiple Chinese/European standards would multiply cost
3. **Interoperability:** Government agencies worldwide need to communicate with allies; divergent standards break secure channels
4. **Technical quality:** NIST's 8-year vetting process produced high-quality algorithms; competitors have lower confidence bar

### Divergence Drivers

1. **National sovereignty:** China, potentially others, seek independent cryptographic infrastructure
2. **Geopolitical hedging:** If NIST algorithms broken, backup standards from independent sources reduce single-point failure
3. **Ideological (non-technical):** Western-developed standards perceived as politically motivated; independent development seen as assertion of autonomy

---

## Implications for Global Organizations (2026)

### For Western Enterprises
- **Action:** Deploy NIST PQC standards (ML-KEM, ML-DSA); expect global interoperability with ETSI, ISO, NCSC, BSI, ANSSI alignment
- **Timeline:** 2026–2027 major deployments; hybrid mode through 2030
- **Risk:** Geopolitical breakdown could fragment standards post-2027; monitor China's OSCCA progress

### For Chinese Organizations
- **Action:** Monitor OSCCA proposal submissions (2025); prepare for potential dual-standards compliance
- **Timeline:** OSCCA standards expected 2026–2027; deployment likely 2027–2030
- **Risk:** Delay in adopting proven NIST PQC if OSCCA timeline slips

### For Multinational Corporations
- **Action:** Plan dual-stack cryptography
  - Primary: NIST PQC for international/Western markets
  - Secondary: Monitor OSCCA PQC for China market (likely needed by 2028–2030)
- **Timeline:** Start OSCCA monitoring in 2026; begin dual-support planning 2027
- **Procurement:** Specify crypto-agility in vendor contracts to ease algorithm swaps

---

## Future Divergence Risk Assessment

**Low-medium risk (2026–2027):** ETSI, BSI, NCSC, ISO remain tightly aligned with NIST; no divergence expected.

**Medium-high risk (2027–2030):** China's OSCCA standards mature; Chinese regulation may mandate OSCCA PQC for national systems. Creates **de facto dual-standards world** for companies serving both markets.

**Potential breakpoint:** If NIST algorithms face significant cryptanalysis weakness, divergence would accelerate as nations seek alternatives. Current confidence in NIST FIPS 203/204/205 is high; risk of such a break ~5–10%.

---

## See Also

- **[NIST FIPS & PQC Standardization](nist-fips-pqc.md)** — Technical algorithm specifications
- **[CISA Federal Guidance](cisa-federal-guidance.md)** — U.S. civilian agency requirements
- **[IETF Protocol Standards](ietf-protocol-standards.md)** — Global protocol integration

---

## References

- [ETSI Committee CYBER](https://www.etsi.org/committee/cyber)
- [ETSI TR 103 616](https://www.etsi.org/deliver/etsi_tr/103600_103699/103616/01.01.01_60/tr_103616v010101p.pdf)
- [ETSI TS 104 015](https://www.etsi.org/deliver/etsi_ts/104000_104099/104015/)
- [BSI TR-02102-1 (Jan 2026)](https://www.bsi.bund.de)
- [NCSC PQC Migration Guidance (March 2025)](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines)
- [ANSSI Cyber Security Agency](https://www.anssi.gouv.fr)
- [ISO/IEC JTC 1/SC 27](https://www.iso.org)
- [China OSCCA PQC Initiative (Feb 2025)](https://thequantuminsider.com/2025/02/18/china-launches-its-own-quantum-resistant-encryption-standards-bypassing-us-efforts/)

