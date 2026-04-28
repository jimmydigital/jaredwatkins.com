---
title: "NSA CNSA 2.0 & National Security Systems"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "NSA's Commercial National Security Algorithm Suite 2.0 (CNSA 2.0) specifications, migration timelines for national security systems, and compliance requirements"
tags: ["nsa", "cnsa", "national-security", "ml-kem", "ml-dsa", "migration", "timeline", "compliance"]
categories: ["standards", "policy"]
research_area: "post-quantum-encryption/standards-policy"
source_urls:
  - "https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF"
  - "https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2022/05/04/national-security-memorandum-on-promoting-united-states-leadership-in-quantum-computing-while-mitigating-risks-to-vulnerable-cryptographic-systems/"
last_reviewed: 2026-04-24
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Overview: NSM-10 and CNSA 2.0 Relationship

On May 4, 2022, the White House issued [National Security Memorandum 10 (NSM-10)](https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2022/05/04/national-security-memorandum-on-promoting-united-states-leadership-in-quantum-computing-while-mitigating-risks-to-vulnerable-cryptographic-systems/), directing all U.S. federal agencies to begin planning and executing a transition to quantum-resistant cryptography. This memorandum set a policy mandate.

Four months later, in September 2022, the NSA published [CNSA 2.0 (Commercial National Security Algorithm Suite 2.0)](https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF)—the technical specification that implements NSM-10's policy direction for **National Security Systems (NSS)**. CNSA 2.0 is binding for DoD, Intelligence Community (IC) contractors, and all other entities handling classified or sensitive national security information.

**Key distinction:**
- **NSM-10** = Policy mandate for all federal agencies
- **CNSA 2.0** = Technical algorithm requirements + timelines for NSS (national security systems)
- **OMB M-23-02** (November 2022) = Implementation guidance for civilian agencies without NSS systems

---

## CNSA 2.0 Approved Algorithm Suite

### Key Encapsulation (Replacing RSA, ECDH)
- **ML-KEM-1024** (FIPS 203) — Primary for long-term protection
- **ML-KEM-768** (FIPS 203) — Acceptable where 128-bit security suffices
- **HQC** (future NIST standard, ~2027) — Backup/diversity algorithm

### Digital Signatures (Replacing ECDSA, RSA)
- **ML-DSA-87** (FIPS 204) — Primary for long-term protection; higher security margin
- **ML-DSA-65** (FIPS 204) — Acceptable where 128-bit security suffices
- **SLH-DSA** (FIPS 205) — Stateless hash-based alternative
- **XMSS/LMS** (NIST SP 800-208) — For firmware and software signing

### Symmetric & Hash Algorithms (Unchanged)
- **AES-256** — Encryption (no quantum attack threat)
- **SHA-384, SHA-512** — Hashing (no quantum attack threat; SHAKE-256 also acceptable)

### Legacy Algorithms (Being Deprecated)
- **RSA** — Key establishment; deprecation begins immediately in priority systems
- **ECDH, ECDSA** — Key exchange & signatures; phase-out per timeline below
- **SHA-256** — May be used but SHA-384/512 preferred

---

## CNSA 2.0 Migration Timeline: By System Category

NSA's migration strategy is phased by **system type**, not by a single agency-wide deadline. Different systems have different risk profiles and implementation complexity.

| System Category | 2025 Target | 2026–2030 Window | 2030 Deadline | 2033 Deadline |
|---|---|---|---|---|
| **Software/Firmware Signing** | CNSA 2.0 *preferred* | — | **Exclusive use** | — |
| **Network Equipment (VPN, routers)** | Support + *prefer* CNSA 2.0 | Deploy CNSA 2.0 | **Prefer exclusive** | — |
| **Web Browsers & Servers** | Support CNSA 2.0 | Deploy where feasible | *Preferred* | **Exclusive use** |
| **Operating Systems** | Support CNSA 2.0 | Deploy widely | *Preferred* | **Exclusive use** |
| **Enterprise & Legacy Systems** | Assess & plan | Execute migration | *Support* CNSA 2.0 | **Exclusive use** |
| **Highly Constrained Devices** | Assess feasibility | Limited deployment | Assess upgrade path | — |

### Detailed Timeline by System Type

#### 1. Software & Firmware Code Signing (2025 deadline)

**Immediate action required:** This is the earliest transition point.

- **2025 (NOW):** All software and firmware signatures must support CNSA 2.0 (ML-DSA-87 or XMSS/LMS for firmware)
- **2030:** Exclusive use of CNSA 2.0 required
- **Why first:** Code signing is relatively low-complexity and high-impact; securing the supply chain is foundational

**Implementation approach:**
- Dual-sign initial releases (classical + CNSA 2.0)
- Deprecate classical-only signatures by 2028
- Enforce signature validation against CNSA 2.0

**Standards:** NIST SP 800-208 (XMSS/LMS for stateful firmware signing)

---

#### 2. Network Equipment (VPNs, Routers, Firewalls) (2026–2030)

**Timelines:**
- **2026:** Vendors must offer support for CNSA 2.0 in IKEv2/IPsec
- **2030:** NSA expects exclusive use of CNSA 2.0 for key establishment
- **Pressure point:** Enterprises with 5–10 year hardware refresh cycles must begin procurement NOW

**Implementation approach:**
- Use RFC 9242 (IKEv2 intermediate exchange for large keys) and RFC 9370 (hybrid KEMs in IKEv2)
- Deploy hybrid mode: classical ECDH + ML-KEM-1024 in parallel
- Phase out pure classical by 2028–2029

**Responsible parties:** Juniper, Cisco, Palo Alto Networks, Check Point, and other NSA-validated vendors must support CNSA 2.0 by 2026

---

#### 3. Web Browsers, Servers, TLS (2026–2033)

**Timelines:**
- **2025–2026:** TLS implementations must support CNSA 2.0 (via IETF drafts or RFC once finalized)
- **2033:** Exclusive use required

**Current status (April 2026):**
- Google Chrome and Cloudflare have been running X25519Kyber768 (hybrid) TLS experiments since August 2023
- Draft RFCs (draft-ietf-tls-mlkem, draft-ietf-tls-ecdhe-mlkem) are approaching finalization
- Major CDNs (Cloudflare, Akamai, AWS CloudFront) expected to offer CNSA 2.0 TLS by 2026

**Implementation challenge:** Certificate chain inflation. ML-DSA-87 public keys (~2592 bytes) are much larger than ECDSA P-256 (~64 bytes), affecting:
- Certificate storage in HSMs
- Network latency (more bytes in ServerHello)
- Mobile clients with constrained bandwidth

---

#### 4. Operating Systems (2027–2033)

**Timeline:**
- **2027:** Major OS vendors (Microsoft, Apple, Linux distributions) expected to ship with CNSA 2.0 support
- **2033:** Exclusive use required

**What this means:**
- Windows Server, macOS, Linux kernels must support ML-KEM, ML-DSA in TLS, SSH, certificate validation
- Cryptographic libraries (OpenSSL, BoringSSL) must have hardened, tested PQC implementations
- User-facing apps (browsers, email clients) must validate CNSA 2.0 certificates

---

#### 5. Enterprise & Legacy Systems (2026–2033)

**Timeline:**
- **2026:** Inventory of legacy cryptographic systems due to NSA
- **2030:** Majority of upgradeable systems should support CNSA 2.0
- **2033:** All systems must use CNSA 2.0 (exception: certified-obsolete hardware beyond repair)

**Challenge:** Large enterprises may have 20–30 year lifespans for some systems (industrial control, banking mainframes). NSA allows phased migration but no hard exemptions after 2033.

---

## Scope: What is a "National Security System"?

**NSA defines NSS as:** Systems that process classified information or handle sensitive national security data, including:

1. **DoD Systems** — All Department of Defense networks, weapons systems, command & control
2. **Intelligence Community** — CIA, NSA, NRO, DIA systems
3. **Cleared Contractors** — Companies processing classified information under DFARS (Defense Federal Acquisition Regulation Supplement) contracts
4. **Critical Infrastructure** — Some DHS-designated critical infrastructure with NSS designation
5. **Unclassified but Sensitive Systems** — Systems handling CUI (Controlled Unclassified Information) marked as "NATIONAL SECURITY"

**Scope exclusions:** Systems processing only unclassified, non-sensitive data may transition at their own pace (but should still follow federal guidance).

---

## Cleared Contractor Compliance Chain

Defense contractors and cleared organizations must comply with CNSA 2.0 through contractual mechanisms:

### DFARS Flow-Down Requirements
- **DFARS 252.204-7012** — Contract clause requiring cybersecurity compliance
- **NIST SP 800-171** — Standard security requirements for CUI; being updated with PQC expectations
- **CMMC 2.0** — Cybersecurity Maturity Model Certification; PQC alignment expected in 2026 updates

### Compliance Verification
- DoD CISO audits contractor systems
- Self-assessment via CMMC Level 2 certification
- Supply chain risk management reviews

### Timeline Implications
- Contractors must begin migration 2025–2026 to show progress by 2027 audits
- Failure to demonstrate CNSA 2.0 planning can result in contract suspension

---

## Key People & Leadership

### Robert (Rob) Joyce — Former NSA Cybersecurity Director

**Career:**
- Joined NSA in 1990
- Led NSA Cybersecurity Collaboration Center
- Served as NSA Cybersecurity Director (2021–March 2024)
- Signed the CNSA 2.0 announcement (September 2022) as Cybersecurity Director

**Post-NSA (2024–present):**
- Founded Joyce Cyber LLC providing cybersecurity consulting
- Joined OpenAI Safety & Security Committee
- Advises Microsoft, PwC, and other firms on PQC adoption

**Significance:** Joyce's cybersecurity leadership at NSA ensured CNSA 2.0 reflected operational realities of U.S. national security systems and was achievable within stated timelines.

### Anne Neuberger — Deputy National Security Advisor (During NSM-10 Era)

**Career:**
- Served as Deputy National Security Advisor for Cyber and Emerging Technology under the Biden administration (2021–January 2025)
- Coordinated NSM-10 policy across agencies
- Acted as liaison between NSA, NIST, CISA, and White House during early PQC transition planning

**Post-government (2025–present):**
- Senior Advisor at Andreessen Horowitz (venture capital)
- Payne Lecturer at Stanford University
- Distinguished Fellow, Royal United Services Institute

**Significance:** Neuberger was instrumental in framing PQC migration as a national security priority and securing presidential authority (NSM-10) to mandate federal agency participation.

---

## Critical Timeline Pressure Points (2026–2030)

### Now (April 2026): Firmware Signing & Early Procurement
- Organizations should be completing firmware signing transition planning
- Network equipment procurement should account for CNSA 2.0 delivery dates
- Large enterprise TLS certificate renewal cycles should plan for larger ML-DSA certificates

### 2026 (This Year)
- IETF TLS drafts expected to advance toward RFC (finalization likely 2026–2027)
- Major TLS implementations (OpenSSL, BoringSSL) shipping with stable ML-KEM support
- CISA expects federal agencies to have CNSA 2.0 procurement plans in place
- First FedRAMP authorizations with PQC support expected

### 2027–2028: The Crunch Years
- Operating systems should ship with native CNSA 2.0 support
- Large enterprises must transition network infrastructure
- TLS certificate deployment reaches critical mass
- Hardware HSM vendors must certify PQC implementations

### 2030 (Firmware & Network Equipment Exclusive)
- Firmware must be signed exclusively with CNSA 2.0
- Network equipment must support CNSA 2.0 as primary mode
- Organizations without credible progress toward 2033 deadline face compliance pressure

### 2033 (Exclusive Use Deadline)
- All NSS systems must use CNSA 2.0 exclusively
- RSA and ECDH officially deprecated for all new protocols
- Late-stage migrations become high-risk and high-cost

---

## Implementation Challenges

1. **Certificate size inflation:** ML-DSA-87 certificates (~4–6 KB) vs. ECDSA P-256 (~1 KB) create network latency and storage pressure
2. **Hardware constraints:** Cryptographic accelerators and HSMs must support ML-KEM, ML-DSA; many legacy devices cannot
3. **Backward compatibility:** Dual-algorithm support (classical + CNSA 2.0) extends implementation timelines
4. **Testing & validation:** FIPS 140-3 cryptographic module validation for new algorithms is time-consuming
5. **Enterprise entropy:** Enterprise RNG (random number generation) must scale to support higher-entropy ML-KEM key generation

---

## References & Primary Sources

- [CNSA 2.0 Algorithm Document (May 2025)](https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF)
- [NSM-10 (May 4, 2022)](https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2022/05/04/national-security-memorandum-on-promoting-united-states-leadership-in-quantum-computing-while-mitigating-risks-to-vulnerable-cryptographic-systems/)
- [NIST FIPS 203, 204, 205 (August 2024)](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [RFC 9242: IKEv2 Intermediate Exchange](https://datatracker.ietf.org/doc/rfc9242/)
- [RFC 9370: Multiple Key Exchanges in IKEv2](https://datatracker.ietf.org/doc/rfc9370/)

