---
title: "Post-Quantum Encryption"
date: 2026-04-15
lastmod: 2026-04-17
draft: false
description: "Research on post-quantum cryptography (PQC): NIST-standardized algorithms, vendor implementation timelines, and adoption across networking and cryptocurrency infrastructure."
tags: ["post-quantum", "cryptography", "security", "pqc", "nist"]
categories: ["overview"]
research_area: "post-quantum-encryption"
last_reviewed: 2026-04-17
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

{{< steering >}}

## Post-Quantum Encryption Section — Steering Instructions

This section tracks the transition to post-quantum cryptography (PQC): the standardization of quantum-resistant algorithms, vendor and protocol adoption timelines, and deployment progress across networking hardware and cryptocurrency/blockchain platforms. Standard Research section rules apply. The following PQC-specific rules extend and override global defaults where noted.

---

### Why This Section Exists

Classical public-key cryptography (RSA, ECDSA, Diffie-Hellman) relies on mathematical problems — integer factorization and discrete logarithm — that a sufficiently powerful quantum computer running Shor's algorithm could solve efficiently. The timeline for a "cryptographically relevant quantum computer" (CRQC) is uncertain, but NIST has treated it as a concrete engineering risk since at least 2016. The primary threat is "harvest now, decrypt later" (HNDL): adversaries can intercept and store encrypted traffic today and decrypt it retroactively once a CRQC is available. For data with long secrecy lifetimes (classified government comms, medical records, long-dated financial contracts), the migration clock is already running.

---

### Editorial Priority

**Research focus:** Depth over breadth. PQC adoption is uneven across the technology stack. Prioritize entries that track:

1. **Network vendors and protocol stacks** — which products have shipped PQC support, which algorithms, in which software/firmware versions, and under what constraints (e.g., performance penalty, key size impact, hardware offload requirements).
2. **Cryptocurrency and blockchain platforms** — which are exposed to quantum attack (signature scheme), which have published migration plans, and what the realistic upgrade path looks like for a decentralized protocol.
3. **Standards bodies and working groups** — NIST, IETF (TLS 1.3 PQC extensions), IEEE, ETSI — track active drafts and finalized specs.

Do not create entries for quantum computing hardware companies in this section — they belong in `research/quantum-computing/`. Cross-reference where relevant.

---

### NIST PQC Standardization — Background

The NIST PQC standardization process (started 2016) produced its first finalized standards in August 2024:

- **FIPS 203** — ML-KEM (Module Lattice-Based Key Encapsulation Mechanism), derived from CRYSTALS-Kyber. The primary standard for key establishment / key exchange.
- **FIPS 204** — ML-DSA (Module Lattice-Based Digital Signature Algorithm), derived from CRYSTALS-Dilithium. The primary standard for digital signatures.
- **FIPS 205** — SLH-DSA (Stateless Hash-Based Digital Signature Algorithm), derived from SPHINCS+. A hash-based signature alternative with different security assumptions.

Additional standards in progress:
- **FIPS 206** — FN-DSA, derived from FALCON (lattice-based signatures; smaller signature size than Dilithium but more complex implementation).
- **HQC** (code-based KEM) — selected as a fourth KEM standard in March 2025 for algorithm diversity; final standard pending.

**Pre-standard algorithms still in wide use:** CRYSTALS-Kyber (pre-FIPS), CRYSTALS-Dilithium (pre-FIPS), Classic McEliece (code-based, not selected by NIST but used in some deployments). Treat these as transitional — document their use but note they are predecessor implementations of the final standards.

**Hybrid approaches:** Many current deployments use hybrid key exchange — classical ECDH combined with a PQC KEM — so that the session key is secure even if one component is broken. This is the recommended transition approach. IETF has published hybrid key exchange specifications for TLS 1.3 (RFC 8773 and successors). Document whether a product's PQC support is hybrid or PQC-only.

---

### Key Terminology

- **CRQC (Cryptographically Relevant Quantum Computer):** A quantum computer with sufficient fault-tolerant qubits to run Shor's algorithm against RSA-2048 or ECDSA-256 at practical speed. No CRQC exists as of April 2026; estimates for when one might range from 2030–2050+ with high uncertainty.
- **HNDL (Harvest Now, Decrypt Later):** Threat model in which adversaries collect encrypted traffic today to decrypt after a CRQC becomes available. Relevant for any data with secrecy lifetime > CRQC arrival estimate.
- **KEM (Key Encapsulation Mechanism):** The mechanism used to establish a shared secret between two parties; replaces classical Diffie-Hellman in PQC deployments. ML-KEM (Kyber) is the NIST standard.
- **Lattice-based cryptography:** The dominant PQC approach. Security relies on the hardness of problems in high-dimensional lattices (Learning With Errors, NTRU). Basis of ML-KEM, ML-DSA, FN-DSA (FALCON).
- **Hash-based signatures:** Security relies only on the collision resistance of hash functions — considered the most conservative PQC choice from a security assumptions standpoint. SLH-DSA (SPHINCS+) is the NIST standard. Larger signatures and slower signing than lattice schemes.
- **Code-based cryptography:** Security relies on the hardness of decoding random linear codes. Classic McEliece and HQC are the leading schemes. Large public keys.
- **Hybrid key exchange:** A session key established by combining a classical KEM (ECDH) and a PQC KEM so that security holds as long as either component is unbroken.
- **Perfect Forward Secrecy (PFS):** Session keys are ephemeral; compromise of long-term keys does not retroactively expose recorded sessions. PQC key exchange must preserve PFS — most PQC KEM deployments are designed to do so.
- **IKEv2 / IPsec PQC:** IETF extensions to IKEv2 (the key exchange protocol in IPsec VPNs) to support PQC KEMs. RFC 9242 and RFC 9370 define the framework. Relevant to networking section entries.
- **TLS 1.3 PQC:** Hybrid PQC extensions for TLS 1.3, primarily standardized via IETF draft-ietf-tls-hybrid-design and related drafts. Relevant to web/application-layer encryption.
- **PQXDH:** Signal Protocol extension for PQC; used in Signal and WhatsApp (as of 2023–2024). Not directly relevant to networking hardware but a useful deployment precedent.

---

### Research Phases

- **Phase 1 (current):** Networking vendors — which hardware and software products support NIST-standard PQC algorithms, under what conditions, with what performance impact.
- **Phase 2 (planned):** Cryptocurrency and blockchain platforms — exposure analysis and migration roadmaps.
- **Phase 3 (future):** Standards and policy — NIST, CISA, NSA guidance; CNSA 2.0 timeline mandates; IETF protocol standards.

---

### Claim Verification Flags for PQC Entries

When a vendor claims PQC support, document:

1. **Specific algorithms supported** — ML-KEM? ML-DSA? Pre-standard Kyber/Dilithium? Hybrid? Name the exact FIPS standard or draft version.
2. **Product scope** — which product lines, which software/firmware versions. "PQC support" that applies only to one CLI-configured lab feature is different from GA shipping support.
3. **Protocol layer** — IKEv2/IPsec? TLS? SSH? MACsec? The answer determines applicability to different traffic types.
4. **Hybrid vs. PQC-only** — document explicitly.
5. **Performance impact** — PQC algorithms, especially lattice-based KEMs, impose higher CPU/memory costs and larger key/ciphertext sizes than classical equivalents. Document any published benchmarks or vendor-disclosed performance deltas.
6. **Hardware offload** — some vendors require dedicated crypto accelerators for performant PQC; note whether PQC is software-only or hardware-offloaded.
7. **FIPS/Common Criteria validation** — is the implementation validated by an accredited lab? FIPS 140-3 and Common Criteria certifications for PQC modules are nascent; document status.

Do not accept "PQC-ready" or "quantum-safe" marketing language without decomposing it into the above specifics. These terms are undefined and frequently used without substance.

---

### PQC-Specific Tags

In addition to global tags:
- Algorithm: `ml-kem`, `ml-dsa`, `slh-dsa`, `fn-dsa`, `kyber`, `dilithium`, `sphincs-plus`, `classic-mceliece`, `hqc`
- Approach: `hybrid-pqc`, `pqc-only`, `pre-standard-pqc`
- Protocol layer: `ike-pqc`, `tls-pqc`, `ssh-pqc`, `macsec-pqc`
- Standard status: `nist-final`, `nist-draft`, `ietf-rfc`, `ietf-draft`
- Sector: `networking`, `cryptocurrency`, `blockchain`, `enterprise`
- Threat model: `hndl`

---

### Review Cadence

- **90 days** — vendor entries in networking and crypto sections (PQC roadmaps are moving fast; NIST and IETF standards activity is ongoing)
- **90 days** — section landing pages (this section is in active development)
- **180 days** — standards reference entries (once a standard is finalized, it changes slowly)

---

{{< /steering >}}

## Overview

Post-quantum cryptography (PQC) addresses the long-term security threat posed by quantum computers capable of running Shor's algorithm, which can break the public-key cryptographic systems — RSA, ECDSA, Diffie-Hellman — that secure nearly all internet traffic and financial infrastructure today.

NIST finalized its first three PQC standards in August 2024 (FIPS 203, 204, 205), ending nearly a decade of evaluation. The U.S. government has mandated federal agencies migrate to these standards, with NSA's CNSA 2.0 suite setting 2030–2033 deadlines for most national security systems. The private sector and standards bodies (IETF, IEEE) are actively integrating PQC algorithms into protocols including TLS, IKEv2/IPsec, and SSH.

The primary near-term threat is **harvest now, decrypt later (HNDL)**: adversaries collecting today's encrypted traffic for future decryption. This makes the migration timeline relevant now even though no cryptographically relevant quantum computer (CRQC) exists yet.

**Editorial note:** This section tracks implementation facts, not future speculation. "PQC-ready," "quantum-safe," and similar marketing terms are examined against specific algorithm support, protocol integration, software version availability, and FIPS validation status. Vendor claims are documented with verification status.

## Key Themes

- NIST finalized ML-KEM (Kyber), ML-DSA (Dilithium), and SLH-DSA (SPHINCS+) as FIPS 203/204/205 in August 2024; these are the authoritative standards for migration planning
- The recommended migration path is hybrid key exchange — combining classical ECDH with a PQC KEM — to preserve security even if one component is broken
- Networking hardware vendors are at varying stages of PQC integration; most have published roadmaps but production-ready, standards-conformant implementations are limited as of early 2026
- Cryptocurrency platforms face a deeper challenge: signature scheme migration in decentralized networks requires broad ecosystem consensus and may involve hard forks
- The HNDL threat model means the migration clock is already running for long-lived sensitive data, even without an operational CRQC

## Research Phases

| Phase | Focus | Status |
|-------|-------|--------|
| Phase 1 | Networking vendors (Sitehop, Juniper, Cisco, Palo Alto, Fortinet, Check Point, Nokia) | In progress |
| Phase 2 | Cryptocurrency platforms (Bitcoin, Ethereum, Solana, Cardano, Algorand, QRL) | In progress |
| Phase 3 | Standards and policy (NIST FIPS, NSA CNSA 2.0, IETF) | Planned |

## Topic Areas

- [Networking]({{< relref "networking/_index.md" >}}) — PQC support across networking hardware and software vendors
- [Cryptocurrencies]({{< relref "cryptocurrencies/_index.md" >}}) — Blockchain platform exposure and migration plans *(Phase 2 — planned)*
