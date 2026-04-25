---
title: "Standards & Policy"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "NIST FIPS standardization, NSA CNSA 2.0 mandates, federal agency directives, and IETF protocol integration for post-quantum cryptography migration"
tags: ["post-quantum", "cryptography", "nist", "policy", "standards", "cnsa", "ietf", "fips", "nsm-10", "omb"]
categories: ["standards"]
research_area: "post-quantum-encryption/standards-policy"
source_urls:
  - "https://csrc.nist.gov/projects/post-quantum-cryptography"
  - "https://www.nsa.gov/CNSA/"
  - "https://www.cisa.gov/pqc"
  - "https://datatracker.ietf.org"
last_reviewed: 2026-04-24
stale_after_days: 180
---

{{< steering >}}
**Scope:** This section covers authoritative standards documents, government mandates and compliance timelines, protocol-level integration specifications, and international equivalents. It does NOT re-explain algorithm cryptographic details—those are covered in the main post-quantum-encryption section steering. Focus is on policy, mandates, regulatory timelines, and how standards are being implemented in practice.

**Key sources to monitor:**
- NIST PQC Project: https://csrc.nist.gov/projects/post-quantum-cryptography
- NSA CNSA 2.0 advisories: https://www.nsa.gov/CNSA/
- CISA PQC guidance: https://www.cisa.gov/pqc
- IETF datatracker: https://datatracker.ietf.org
- ETSI TC CYBER: https://www.etsi.org/committee/cyber

**Claim verification:** Always link to the primary source document: FIPS publication number, RFC or draft-name, NSA advisory URL, OMB or CISA guidance link. Do not accept secondary sources alone for regulatory timelines or compliance deadlines.

**Staleness policy:** 180 days for finalized standards (they don't change often); 90 days for pending standards, draft RFCs, and compliance deadlines (these evolve).
{{< /steering >}}

## Overview

The U.S. government's post-quantum cryptography migration is driven by three interlocking mandates: NSM-10 (National Security Memorandum 10, signed May 4, 2022), NIST's FIPS publications (FIPS 203–205 finalized August 2024), and NSA's CNSA 2.0 suite (announced September 2022). Together they establish what systems must be protected, which algorithms are approved, and by when. The private sector transition is being propelled by IETF protocol standards (RFC 9242, RFC 9370, and emerging TLS/SSH drafts) and by industry-specific regulators following NIST guidance.

As of April 2026, the standards landscape has solidified: three FIPS are finalized, a fourth (FIPS 206 for FALCON) is in draft, and NIST selected a fifth algorithm (HQC) in March 2025 for future standardization. The migration clock is ticking—CNSA 2.0 mandates full deprecation of RSA and ECDH by 2033 for national security systems, and civilian federal agencies face inventory and planning deadlines under OMB M-23-02.

---

## Standards Reference Table

| Document | Body | Status | Subject | Finalized/Released |
|----------|------|--------|---------|------------------|
| [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) | NIST | **Final** | ML-KEM (Module-Lattice-Based KEM) | August 13, 2024 |
| [FIPS 204](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf) | NIST | **Final** | ML-DSA (Module-Lattice-Based Digital Signature) | August 13, 2024 |
| [FIPS 205](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf) | NIST | **Final** | SLH-DSA (Stateless Hash-Based Digital Signature) | August 13, 2024 |
| FIPS 206 | NIST | *Draft* | FN-DSA (FALCON) | Expected 2025–2026 |
| HQC Standard | NIST | *In Progress* | HQC (Hamming Quasi-Cyclic) as 5th backup KEM | Draft ~2026; final ~2027 |
| [SP 800-227](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-227.pdf) | NIST | **Final** | Recommendations for Key-Encapsulation Mechanisms | September 2025 |
| [SP 800-208](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-208.pdf) | NIST | **Final** | Stateful Hash-Based Digital Signature Schemes | October 2020 |
| [NSM-10](https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2022/05/04/national-security-memorandum-on-promoting-united-states-leadership-in-quantum-computing-while-mitigating-risks-to-vulnerable-cryptographic-systems/) | White House | **In Force** | Federal PQC migration directive & quantum computing leadership | May 4, 2022 |
| [OMB M-23-02](https://www.whitehouse.gov/wp-content/uploads/2022/11/M-23-02-M-Memo-on-Migrating-to-Post-Quantum-Cryptography.pdf) | OMB | **In Force** | Federal agency cryptographic inventory & migration planning | November 18, 2022 |
| [CNSA 2.0](https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF) | NSA | **In Force** | National security systems algorithm suite & timeline | September 2022 |
| [RFC 9242](https://datatracker.ietf.org/doc/rfc9242/) | IETF | **Final** | IKEv2 intermediate exchange for large PQC keys | May 2022 |
| [RFC 9370](https://datatracker.ietf.org/doc/rfc9370/) | IETF | **Final** | Multiple Key Exchanges in IKEv2 (hybrid PQC mechanism) | May 2023 |
| [RFC 8784](https://datatracker.ietf.org/doc/rfc8784/) | IETF | **Final** | Mixing preshared keys in IKEv2 | July 2020 |
| [draft-ietf-tls-mlkem](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/) | IETF | *Active Draft* | ML-KEM for TLS 1.3 (v07, expires Aug 2026) | — |
| [draft-ietf-tls-ecdhe-mlkem](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/) | IETF | *Active Draft* | Hybrid ECDH+ML-KEM for TLS 1.3 (v04, expires Aug 2026) | — |
| draft-ietf-sshm-ssh-pq-hybrid | IETF | *Active Draft* | PQC key exchange for SSH | — |
| [ETSI TR 103 616](https://www.etsi.org/deliver/etsi_tr/103600_103699/103616/01.01.01_60/tr_103616v010101p.pdf) | ETSI | **Final** | Overview of post-quantum digital signature algorithms | September 2021 |
| [ETSI TS 104 015](https://www.etsi.org/deliver/etsi_ts/104000_104099/104015/) | ETSI | **Final** | Quantum-safe hybrid key establishment (Covercrypt) | February 2025 |

---

## Topic Areas

- **[NIST FIPS & PQC Standardization](nist-fips-pqc.md)** — The 8-year standardization process, FIPS 203/204/205 scope and implementation requirements, status of FIPS 206 (FALCON) and HQC selection, and the SIKE/SIDH cautionary tale.

- **[NSA CNSA 2.0 & National Security Systems](nsa-cnsa-2.md)** — CNSA 2.0 algorithm specifications, migration timelines by system category (software/firmware, network equipment, operating systems), NSM-10 relationship, and cleared contractor compliance obligations.

- **[Federal Civilian Agency Guidance (CISA & OMB)](cisa-federal-guidance.md)** — OMB M-23-02 requirements, CISA PQC roadmap, federal buying guidance (January 2026), FedRAMP PQC implications, and sector-specific critical infrastructure advisories.

- **[IETF Protocol Standards](ietf-protocol-standards.md)** — IKEv2/IPsec (RFC 9242, RFC 9370), TLS 1.3 hybrid key exchange (draft-ietf-tls-mlkem, draft-ietf-tls-ecdhe-mlkem), SSH, X.509 certificates, and the Google/Cloudflare X25519Kyber768 production experiment.

- **[International Standards Bodies](international-standards.md)** — ETSI (Europe), BSI (Germany), NCSC (UK), ANSSI (France), ISO/IEC JTC 1/SC 27, and China's divergent OSCCA PQC initiative—convergence vs. fragmentation analysis.

---

## Quick Timeline

| Event | Date | Significance |
|-------|------|-------------|
| NSM-10 signed | May 4, 2022 | U.S. Government PQC migration mandate begins |
| CNSA 2.0 announced | September 2022 | NSA specifies algorithms & timelines for national security systems |
| OMB M-23-02 issued | November 18, 2022 | Civilian agencies required to inventory & plan migration |
| FIPS 203/204/205 finalized | August 13, 2024 | ML-KEM, ML-DSA, SLH-DSA standards published |
| Google Chrome X25519Kyber | August 2023–present | Large-scale TLS experiment in production |
| HQC selected by NIST | March 11, 2025 | Fifth algorithm chosen; draft standard expected ~2026, final ~2027 |
| NIST SP 800-227 published | September 2025 | KEM implementation & deployment guidance |
| CISA federal buying guidance | January 23, 2026 | Agencies required to procure PQC-capable products in identified categories |
| **Key deadline pressure window** | **2026–2030** | CNSA 2.0 firmware signing (by 2030), network equipment (by 2030) |
| **Full deprecation deadline** | **2033** | CNSA 2.0 requires exclusive use of PQC for all NSS systems |

---

## Notes for Researchers

1. **"Harvest Now, Decrypt Later" risk** — Adversaries may collect encrypted data today for decryption after quantum computers arrive. This retroactive threat makes the migration timeline critical even for data with long confidentiality requirements.

2. **Certificate size impact** — ML-DSA-87 public keys are ~2592 bytes vs. ECDSA P-256 at 64 bytes. This affects HSM storage, certificate chains, and PKI infrastructure planning.

3. **Hybrid transitional period** — Most deployments will run classical algorithms + PQC in parallel ("hybrid") for several years before full migration, to ensure backward compatibility and provide dual protection.

4. **Geopolitical divergence** — China's OSCCA is developing independent PQC standards. Europe (ETSI, BSI) is largely aligning with NIST. This fragmentation complicates global deployments.

5. **Clock is tight for enterprises** — Large organizations typically require 5–10 years to migrate cryptographic infrastructure. The 2030–2033 deadlines for national security systems and 2035 for civilian agencies are aggressive.

---

## See Also

- **[Main PQC Section](../)** — Algorithm details, cryptographic properties, deployment considerations
- **[Networking & Vendor Implementation](../networking/)** — Which vendors (Juniper, Sitehop, Palo Alto) support RFC 9242, RFC 9370, etc.

