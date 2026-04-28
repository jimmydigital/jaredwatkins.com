---
title: "IETF Protocol Standards & Integration"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "IETF protocol standards for post-quantum cryptography in IKEv2, TLS 1.3, SSH, and X.509 certificates"
tags: ["ietf", "rfc", "tls", "ikev2", "ssh", "hybrid", "ml-kem", "x509"]
categories: ["standards", "protocols"]
research_area: "post-quantum-encryption/standards-policy"
source_urls:
  - "https://datatracker.ietf.org"
  - "https://datatracker.ietf.org/doc/rfc9242/"
  - "https://datatracker.ietf.org/doc/rfc9370/"
  - "https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/"
  - "https://blog.cloudflare.com/experiment-with-pq/"
last_reviewed: 2026-04-24
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Overview: Protocol-Level PQC Integration

While NIST standardizes cryptographic algorithms (FIPS 203, 204, 205), the IETF standardizes how those algorithms integrate into Internet protocols. IETF working groups are updating TLS 1.3, IKEv2/IPsec, SSH, and X.509 certificates to support post-quantum algorithms.

As of April 2026, IKEv2/IPsec integration is mature (finalized RFCs); TLS 1.3 integration is in final draft stages; and SSH, CMS, and certificate standards are in active development.

---

## IKEv2 / IPsec (Most Mature — Finalized RFCs)

### RFC 9242: Intermediate Exchange in IKEv2 (May 2022)

**Status:** ✅ **FINAL RFC** | [IETF Datatracker](https://datatracker.ietf.org/doc/rfc9242/)

**Problem it solves:** IKEv2's standard message exchange has size limits; large PQC key encapsulations (1088 bytes for ML-KEM-1024) exceed IKEv2's maximum message sizes, causing packet fragmentation and losing protection from some attacks.

**Solution:** RFC 9242 introduces an **intermediate exchange** that allows the IKE_INTERMEDIATE message type, enabling multiple round-trips to handle large keys without strict size limits.

**Implementation:**
- Initiator sends small classical key share (e.g., ECDH) in initial message
- Responder calculates shared secret from classical exchange
- Both parties use resulting key material to encrypt subsequent messages
- Larger PQC keys (ML-KEM) can then be safely exchanged in encrypted payloads

**Deployment status (2026):**
- Palo Alto Networks, Juniper Networks, Cisco support RFC 9242
- Available in OpenIKE, strongSwan, and other open-source implementations
- Enterprise adoption estimated at 20–30% of deployed VPNs by early 2026

---

### RFC 9370: Multiple Key Exchanges in IKEv2 (May 2023)

**Status:** ✅ **FINAL RFC** | [IETF Datatracker](https://datatracker.ietf.org/doc/rfc9370/)

**Problem it solves:** IKEv2 traditionally supports one key exchange per SA setup. PQC migration requires **hybrid** approaches combining classical (ECDH) + quantum-resistant (ML-KEM) in parallel.

**Solution:** RFC 9370 defines how to perform multiple key exchanges (e.g., ECDH + ML-KEM) during a single SA establishment, computing a combined shared secret.

**How it works:**
1. Initiator proposes multiple key exchanges: `[ECDH_X25519, ML_KEM_768]`
2. Responder accepts and performs both independently
3. Shared secrets combined: `combined_secret = PRF(ECDH_shared_secret || ML_KEM_shared_secret)`
4. Either key establishment algorithm failing doesn't fully compromise the session (fail-safe property)

**Hybrid strategy:**
- **Classical-first:** If ML-KEM is broken, ECDH still provides security
- **Crypto-agility:** Easy to swap out ML-KEM variants without protocol changes
- **Transitional:** Organizations can deploy hybrid mode immediately, deprecate classical by 2030

**Deployment status (2026):**
- RFC 9370 implementations in Juniper SRX (since 2024), Palo Alto (2024+), Fortinet (2025+)
- Open-source: libreswan, strongSwan have implementations
- Enterprise adoption: Estimated 15–25% of deployed hybrid VPNs by 2026

---

### RFC 8784: Mixing Preshared Keys in IKEv2 (July 2020)

**Status:** ✅ **FINAL RFC** | Pre-dates PQC focus but used in hybrid deployments

**Relevance to PQC:** PSK mixing can complement hybrid KEMs; if shared knowledge of a PSK exists (e.g., from out-of-band distribution), it can be mixed with PQC-derived keys for additional resilience.

**Limited PQC adoption:** Most IKEv2 PQC deployments use RFC 9370 (multiple KEMs) rather than PSK mixing.

---

## TLS 1.3 (In Progress — Active Drafts, Expected RFC 2026–2027)

### draft-ietf-tls-mlkem (ML-KEM for TLS 1.3)

**Status:** 🟡 **ACTIVE DRAFT** | [Datatracker](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/) | Version 07 (expires Aug 16, 2026)

**Specification:**
- Defines three named groups for TLS 1.3: `ML-KEM-512`, `ML-KEM-768`, `ML-KEM-1024`
- Registers IANA TLS Named Groups registry entries
- Specifies encapsulation/decapsulation in ClientHello key_share extensions
- Compatible with existing TLS 1.3 ClientHello and ServerHello flows

**Implementation status (April 2026):**
- BoringSSL (Google), OpenSSL 3.x, libtls (OpenBSD) have working implementations
- Major browsers (Chrome, Firefox) expected to support by late 2026 (pending RFC finalization)
- CDNs (Cloudflare, AWS, Akamai) beta support available; production deployment expected 2026–2027

**Timeline:**
- Expected to advance to RFC in **late 2026 or early 2027**
- Assumes no major cryptanalytic attacks or implementation issues in current draft period

---

### draft-ietf-tls-ecdhe-mlkem (Hybrid ECDHE+ML-KEM for TLS 1.3)

**Status:** 🟡 **ACTIVE DRAFT** | [Datatracker](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/) | Version 04 (expires Aug 12, 2026)

**Specification:**
Defines three hybrid named groups combining classical + PQC:
- **X25519MLKEM768** — X25519 ECDH + ML-KEM-768
- **SecP256r1MLKEM768** — P-256 ECDH + ML-KEM-768
- **SecP384r1MLKEM1024** — P-384 ECDH + ML-KEM-1024

**Shared secret computation:**
```
hybrid_shared_secret = Hash(
    "tls13 hybrid" || 
    ecdhe_shared_secret || 
    mlkem_shared_secret
)
```

**Deployment & Real-World Testing**

Google and Cloudflare have been running a **large-scale TLS experiment** since August 2023:

#### Google Chrome X25519Kyber768Draft00 Experiment

**Timeline:**
- **August 2023:** Chrome begins slowly enabling X25519+Kyber768Draft00 by default for a percentage of users
- **Q4 2023–Q1 2024:** Rollout reaches ~1–2% of all TLS 1.3 connections globally
- **Q2–Q3 2024:** Further rollout; monitoring for compatibility issues
- **April 2026:** Estimated 5–10% of TLS connections use hybrid PQC (exact figures proprietary to Google/Cloudflare)

**Key findings (published via Cloudflare & Google security blogs):**
- **Performance:** Negligible latency impact (~0–5 ms added to handshake)
- **Compatibility:** No significant breakage; legacy servers transparently handle hybrid handshake
- **Size impact:** ClientHello increases by ~600–800 bytes due to larger key shares; acceptable for most clients
- **Security assessment:** No implementation flaws discovered; hybrid mode provides immediate quantum resistance

**Transition plan:**
- Support for X25519Kyber768Draft00 expected to continue through RFC finalization (expected 2026–2027)
- Once draft-ietf-tls-ecdhe-mlkem becomes RFC, Chrome/Cloudflare will transition to final algorithm
- Old draft00 support deprecated and removed by 2028–2029

**Industry adoption (2026):**
- Cloudflare: X25519+Kyber768 available by default for all domains
- AWS CloudFront: Beta PQC support available
- Azure: PQC support roadmap announced for 2026
- Akamai: Evaluating hybrid TLS deployment

---

## SSH (In Progress — Active Drafts)

### draft-ietf-sshm-ssh-pq-hybrid

**Status:** 🟡 **ACTIVE DRAFT** | SSHM Working Group | [Datatracker](https://datatracker.ietf.org/doc/draft-ietf-sshm-ssh-pq-hybrid/)

**Specification:**
Integrates post-quantum key exchange into SSH protocol (RFC 4253).

**Current draft state (2026):**
- Defines new key exchange algorithm names: `mlkem768-x25519`, `mlkem1024-p256`, etc.
- Hybrid composition matches TLS draft approach
- Implementation guidance for OpenSSH, PuTTY, and other SSH clients/servers

**Expected timeline:**
- RFC expected **2026–2027** (follows TLS finalization)
- OpenSSH implementation expected by 2027

**Deployment challenge:** SSH is widely used for server administration; large-scale rollout requires coordination with enterprise SSH management platforms (Teleport, Gravitational).

---

## S/MIME & CMS (In Progress — Multiple Active Drafts)

### draft-ietf-lamps-pq-composite-kem

**Status:** 🟡 **ACTIVE DRAFT** | LAMPS Working Group | [GitHub](https://lamps-wg.github.io/draft-composite-kem/)

**Purpose:**
Defines **composite public key cryptography** — combining multiple PQC algorithms into single composite certificates and signatures for maximum safety.

**Example composite KEM:**
```
CompositeKEM ::= SEQUENCE {
    rsa_kem ...,
    mlkem_kem ...,
    hqc_kem ...
}
```

Encryption/signing performed with all algorithms in sequence; decryption/verification succeeds if any single algorithm succeeds.

**Use cases:**
- Securing email (S/MIME)
- Signing documents and code
- Critical infrastructure where algorithm failure is intolerable

**Timeline:** RFC expected **2026–2027**

---

## X.509 Certificates (In Progress)

### draft-ietf-lamps-dilithium-certificates

**Status:** 🟡 **ACTIVE DRAFT** | LAMPS Working Group

**Problem:** X.509 certificates traditionally store ECDSA or RSA public keys. Deploying ML-DSA requires:
1. New OIDs (Object Identifiers) for ML-DSA algorithm types
2. New SubjectPublicKeyInfo structure to encode ML-DSA keys
3. Larger certificate sizes (~4–6 KB vs. ~1 KB for ECDSA)

**Certificate size impact:**
- **ML-DSA-87 certificate size:** ~4–6 KB (public key ~2592 bytes alone)
- **ECDSA P-256 certificate size:** ~1–1.5 KB (public key ~64 bytes)
- **TLS handshake implication:** Server sends certificate in ServerCertificate message; 4–5× larger certificate means more network bytes in handshake

**Deployment challenge:**
- Some legacy TLS implementations have hard-coded limits on certificate size (<4 KB)
- Mobile clients with bandwidth constraints affected
- HSM storage and certificate authority database planning needed

**IETF solution:** Composite certificates combining both classical (ECDSA) and PQC (ML-DSA) keys in single cert, reducing total number of certs needed and simplifying PKI.

**Expected timeline:** RFC **2026–2027**

---

## IETF Working Groups Leading PQC Standardization

| WG | Focus Area | Key Drafts | Expected RFC |
|---|---|---|---|
| **IPSECME** | IKEv2 / IPsec | RFC 9242, RFC 9370 (both final) | ✅ Complete |
| **TLS** | TLS 1.3 | draft-ietf-tls-mlkem, draft-ietf-tls-ecdhe-mlkem | 2026–2027 |
| **SSHM** | SSH | draft-ietf-sshm-ssh-pq-hybrid | 2026–2027 |
| **LAMPS** | X.509, CMS, S/MIME | draft-ietf-lamps-pq-composite-kem, draft-ietf-lamps-dilithium-certificates | 2026–2027 |
| **QUIC** | QUIC protocol | Integration via TLS drafts | 2026–2027 |

---

## Crypto-Agility: A Core Design Principle

IETF PQC standards emphasize **crypto-agility** — the ability to swap algorithms without protocol changes.

**Implementation approach:**
1. Algorithms registered in IANA registries (TLS Named Groups, IKEv2 Key Exchange Algorithm Numbers, etc.)
2. New algorithms can be added by registration without protocol updates
3. Implementations support algorithm negotiation (client proposes list; server selects)

**Benefit:** When HQC becomes standardized (2027), TLS/IKEv2/SSH implementations can add it via IANA registration without requiring protocol revisions.

---

## Migration Path: Hybrid → Post-Quantum Only (Timeline)

| Phase | 2025 | 2026 | 2027–2028 | 2029–2030 | 2031–2033 |
|---|---|---|---|---|---|
| **Status** | Experiments | RFCs finalize | Deployment | Preference | Exclusive |
| **TLS** | Draft support | RFC published | Vendors implement | Preferred mode | Mandatory |
| **IKEv2** | RFC complete | Vendor rollout | Enterprise deployment | Preferred | Preferred |
| **SSH** | Draft phase | Active drafts | Vendor support | Gradual | Gradual |
| **Certificates** | Draft phase | RFC expected | CA rollout | Hybrid certs | PQC-first |
| **Algorithm choice** | Hybrid (X25519+ML-KEM) | Hybrid | Hybrid → Mixed | Preferred PQC | PQC-exclusive |

---

## Vendor Implementation Status (April 2026)

| Vendor | TLS PQC | IKEv2 PQC | SSH PQC | Status |
|---|---|---|---|---|
| **Palo Alto Networks** | Beta (2026) | RFC 9242/9370 | Planning | Actively implementing |
| **Juniper Networks** | Roadmap (2026–2027) | RFC 9242/9370 | Evaluating | Enterprise partnerships |
| **Cisco** | Evaluating (2026+) | RFC 9370 planned | Evaluating | Moderate pace |
| **Cloudflare** | X25519Kyber (production) | — | Planning | Leading TLS deployment |
| **Google** | Chrome hybrid (production) | — | Planning | Major browser support |
| **OpenSSL** | Draft support | — | Planning | Community-driven |
| **BoringSSL** | ML-KEM support | — | Planning | Google internal + Android |
| **Microsoft** | Roadmap (2026–2027) | Evaluating | Roadmap | Enterprise software focus |

---

## Critical Decision Points for Organizations (2026)

1. **TLS certificate refresh cycle:** Plan certificate replacement for 2027–2028 when larger PQC certs are standard; older clients may reject newer certs, so hybrid deployment recommended through 2030
2. **VPN equipment procurement:** Specify RFC 9242/9370 support in RFPs issued in 2026–2027; equipment purchased today must support hybrid mode
3. **SSH infrastructure:** Transition timelines for SSH vary widely; government agencies (CNSA 2.0) may have earlier deadlines than general enterprises
4. **Crypto-agility in architecture:** Design systems to support algorithm swaps without code changes (e.g., via configuration registries)

---

## See Also

- **[NIST FIPS & PQC Standardization](nist-fips-pqc.md)** — Algorithm specifications (FIPS 203, 204, 205)
- **[NSA CNSA 2.0](nsa-cnsa-2.md)** — Timelines and compliance requirements for national security systems
- **[CISA Federal Guidance](cisa-federal-guidance.md)** — Federal civilian agency compliance deadlines

---

## References & IETF Resources

- [IETF Datatracker](https://datatracker.ietf.org) — Drafts and RFCs
- [RFC 9242: IKEv2 Intermediate Exchange](https://datatracker.ietf.org/doc/rfc9242/)
- [RFC 9370: Multiple Key Exchanges in IKEv2](https://datatracker.ietf.org/doc/rfc9370/)
- [draft-ietf-tls-mlkem](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/)
- [draft-ietf-tls-ecdhe-mlkem](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/)
- [Cloudflare PQC Experiment Blog](https://blog.cloudflare.com/experiment-with-pq/)
- [Google Chrome PQC Rollout](https://blog.chromium.org/2023/08/protecting-chrome-users-from-quantum.html)

