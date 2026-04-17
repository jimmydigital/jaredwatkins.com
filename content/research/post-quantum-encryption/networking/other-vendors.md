---
title: "Networking PQC — Vendor Survey"
date: 2026-04-15
lastmod: 2026-04-17
draft: false
description: "Survey of post-quantum cryptography support and roadmaps across major networking vendors: Cisco (IOS XE 26, ASA, FTD), Palo Alto Networks (PAN-OS 12.1 Orion), Fortinet (FortiOS 7.6.x), Check Point (Gaia R82), Nokia (ANYsec/SR OS), Aruba/HPE, and open-source implementations."
tags: ["post-quantum", "cryptography", "networking", "pqc", "ike-pqc", "ml-kem", "hybrid-pqc", "enterprise"]
categories: ["overview"]
research_area: "post-quantum-encryption/networking"
source_urls:
  - "https://docs.fortinet.com/document/fortigate/7.6.0/new-features/229631/enhancing-security-with-post-quantum-cryptography-for-ipsec-key-exchange-7-6-1"
  - "https://docs.paloaltonetworks.com/network-security/quantum-security/administration/quantum-security-concepts/support-for-quantum-features"
  - "https://blogs.cisco.com/security/preparing-for-post-quantum-cryptography-the-secure-firewall-roadmap"
  - "https://sc1.checkpoint.com/documents/R82/WebAdminGuides/EN/CP_R82_SitetoSiteVPN_AdminGuide/Content/Topics-VPNSG/Quantum-Safe-Key-Exchange.htm"
  - "https://strongswan.org/blog/2024/12/03/strongswan-6.0.0-released.html"
last_reviewed: 2026-04-17
stale_after_days: 90
---

## Summary

This entry surveys post-quantum cryptography support across major networking vendors. As of April 2026, the market has matured significantly since this section was initially established: **Fortinet FortiOS 7.6.1 (GA), Palo Alto PAN-OS 11.2/12.1 (GA), Check Point Gaia R82 (GA), and Cisco ASA 9.19 (transitional GA)** all ship production ML-KEM IKEv2 support. Cisco's full-stack IOS XE 26 platform was announced at Cisco Live Amsterdam in April 2026. The critical pending standard is **draft-ietf-ipsecme-ikev2-mlkem**, which has not yet been published as an RFC — meaning current vendor implementations use pre-RFC algorithm identifiers.

**Key finding:** Fortinet is the earliest shipping GA vendor for native ML-KEM IKEv2 in a commercial firewall OS. Palo Alto has the broadest algorithm coverage. Cisco has the most comprehensive architectural narrative. No major vendor has FIPS 140-3 CMVP validation for PQC modules. No vendor other than Palo Alto (Gen5 PA-5500 Series) has announced dedicated silicon acceleration for lattice-based PQC.

---

## IETF Standards Context (Updated April 2026)

| Document | Status | Subject |
|---|---|---|
| RFC 8784 | Published (2020) | PPK (post-quantum PSK) mixing in IKEv2 — transitional measure |
| RFC 9242 | Published (2022) | IKE_INTERMEDIATE exchange for additional key exchanges |
| RFC 9370 | Published (2023) | Multiple Key Exchanges in IKEv2 — primary PQC IKEv2 vehicle |
| RFC 9794 | Published (June 2025) | Terminology for PQC/Traditional Hybrid Schemes |
| **draft-ietf-ipsecme-ikev2-mlkem-05** | **Publication requested March 24, 2026** | **ML-KEM in IKEv2 — defines IANA codepoints for ML-KEM-512/768/1024** |
| draft-ietf-tls-hybrid-design-16 | Active draft (Sep 2025) | Hybrid key exchange in TLS 1.3 |
| draft-guthrie-cnsa2-ipsec-profile | Active draft | CNSA 2.0 IPsec profile for US government customers |

**Critical gap:** `draft-ietf-ipsecme-ikev2-mlkem` defines the specific IANA algorithm identifiers for ML-KEM in IKEv2. As of April 2026, it is at version -05 with publication requested but not yet an RFC. All current vendor ML-KEM IKEv2 implementations use pre-RFC identifiers that may need updating when the RFC finalizes. Multi-vendor interoperability is not reliably plug-and-play as a result.

---

## Cisco Systems

### IOS XE — Full-Stack PQC (IOS XE 26, April 2026)

**Announced:** Cisco Live Amsterdam, April 2026. Positioned as "the first enterprise platform delivering full-stack Quantum Defense."

**IOS XE 26 PQC coverage:**
- **Secure Boot / image integrity:** PQC-based attestation chain on Catalyst 9000 Smart Switches
- **IPsec/IKEv2:** RFC 9242 + RFC 9370 hybrid key exchange with ML-KEM
- **MACsec:** Line-rate PQC-ready MACsec on Catalyst 8000/9000 hardware (Catalyst 9000 Smart Switches claim line-rate without CPU overhead)
- **SSH:** ML-KEM-1024 hybrid (SSHv2)
- **Management TLS:** IOS XE 26 target

**Earlier partial support:** IOS XE 17.15.x (March 2026 release) included ML-KEM-1024 for SSHv2 and partial PQC for the Cisco 8300 Series Secure Routers. RFC 8784 PPK (post-quantum preshared key mixing) has been available across IOS XE 17.x as a transitional measure.

**Hybrid vs. PQC-only:** Hybrid (classical DH + ML-KEM in parallel), per NIST/NSA/BSI/ANSSI guidance.

**CNSA 2.0 alignment:** Cisco has explicitly aligned the IOS XE roadmap to NSA CNSA 2.0 requirements. Site-to-site VPN CNSA 2.0 profile follows `draft-guthrie-cnsa2-ipsec-profile`.

**FIPS 140-3:** No CMVP PQC module validation published. FIPS 140-2 sunset is September 2026.

**Sources:**
- [Cisco: Why full-stack PQC cannot wait](https://blogs.cisco.com/networking/why-full-stack-post-quantum-cryptography-cannot-wait)
- [Cisco: Post-Quantum MACsec in Cisco Switches](https://blogs.cisco.com/security/post-quantum-macsec-in-cisco-switches)
- [Cisco Campus PQC analysis (Pinglabz)](https://www.pinglabz.com/post-quantum-crypto-in-cisco-campus-networks-what-operators-need-to-know/)

---

### Cisco Secure Firewall (ASA and FTD)

**Transitional GA (current):**
- **ASA 9.18:** RFC 8784 PPK for IKEv2 (GA)
- **ASA 9.19:** RFC 9242 + RFC 9370 hybrid multiple key exchange (GA)

**Upcoming GA:**
- **FTD 10.5 / ASA 9.25** — Target: late 2026
  - ML-KEM (FIPS 203) for IKEv2/IPsec VPN
  - TLS decryption with PQC algorithm support
  - SKIP (Secure Key Integration Protocol) for dynamic PPK management
- **FTD/ASA 11.0** — Target: H2 2027
  - ML-DSA (FIPS 204), SLH-DSA (FIPS 205) for digital signatures
  - QUIC decryption with PQC
  - Remote Access VPN (TLS/DTLS) with ML-KEM + ML-DSA
  - PQC metadata logging

**Source:** [Cisco Secure Firewall PQC Roadmap blog](https://blogs.cisco.com/security/preparing-for-post-quantum-cryptography-the-secure-firewall-roadmap)

### Cisco Meraki

**Status:** No GA PQC VPN support. The Cisco 8455-G2-MX hardware is described as "AI/ML and Post Quantum Cryptography (PQC) ready" — hardware readiness without a software GA date. Cloud-managed architecture creates dependency on centralized firmware deployment. No public timeline confirmed.

**Source:** [Cisco Meraki community announcement](https://community.meraki.com/t5/Feature-Announcements/Introducing-the-Cisco-8455-G2-MX-Secure-Router/ba-p/286660)

<!-- TODO: Track FTD 10.5 GA date (target late 2026) and confirm ML-KEM algorithm variants (768 or 1024 default?) -->
<!-- TODO: Monitor FIPS 140-3 validation filings for Cisco IOS XE PQC module -->
<!-- TODO: Verify IOS XE 17.15.x release notes for 8300 Series PQC specifics -->

---

## Palo Alto Networks

### PAN-OS 12.1 "Orion" — Full PQC Suite

**GA announcement:** PAN-OS 12.1 Orion launched August 19, 2025.

**Quantum-Safe Security solution GA:** January 30, 2026 (broader platform integration including Prisma SASE).

**PQC features by OS version:**

| Version | PQC Feature |
|---|---|
| PAN-OS 11.1 | RFC 8784 PPK for IKEv2 (transitional) |
| PAN-OS 11.2 | Site-to-site VPN hybrid PQC (RFC 9242/9370) |
| **PAN-OS 12.1 (Aug 2025)** | **Full PQC suite — all NIST FIPS 203/204/205 + experimental algorithms** |

**Algorithms confirmed (PAN-OS 12.1):**
- ML-KEM (FIPS 203) — all parameter sets (512/768/1024) supported
- ML-DSA (FIPS 204) — confirmed
- SLH-DSA (FIPS 205) — confirmed
- Experimental/pre-standard: HQC, Classic McEliece, BIKE, FrodoKEM

**Protocol layers:**
- IKEv2/IPsec site-to-site VPN — PAN-OS 11.2+
- TLS (management plane) — PAN-OS 12.1 (SSL service profiles now offer ML-KEM)
- TLS deep inspection / dataplane decryption — PAN-OS 12.1
- RFC standards: RFC 8784, RFC 9242, RFC 9370, ETSI GS QKD 014

**GlobalProtect VPN (remote access):** Not explicitly confirmed for GA in available documentation. Site-to-site VPN is the primary confirmed use case for PAN-OS 12.1.

**Prisma SASE (January 30, 2026 GA):**
- **Quantum Readiness Dashboard** — telemetry from PAN-OS NGFW + Prisma Access
- **Cipher Translation Proxy** — re-encrypts classical traffic to PQC in real-time at network edge; enables PQC protection for traffic to/from legacy endpoints
- **Active Drift Detection** — alerts on cipher suite regression

**Hardware platforms with quantum-optimized processing:**
- PA-5500 Series (Gen 5, data center) — quantum-optimized hardware acceleration for PQC traffic inspection. **Only major networking vendor other than Sitehop to announce dedicated PQC hardware acceleration.**
- PA-455R-5G (Gen 5, ruggedized industrial)
- Also supported (software-based PQC): PA-400, PA-1400, PA-3400, PA-5400 Series, VM-Series (Gen 4)

**Hybrid vs. PQC-only:** Both hybrid and pure PQC modes supported; hybrid recommended for transition.

**FIPS 140-3:** FIPS 140-3 compliance referenced in governance tooling; no specific CMVP module validation for PQC algorithms published.

**Sources:**
- [PAN-OS Support for Post-Quantum Features (official docs)](https://docs.paloaltonetworks.com/network-security/quantum-security/administration/quantum-security-concepts/support-for-quantum-features)
- [PAN-OS 12.1 Orion announcement](https://live.paloaltonetworks.com/t5/community-blogs/palo-alto-networks-introduces-pan-os-12-1-orion/ba-p/1237575)
- [Palo Alto: Securing the Quantum Age (August 2025)](https://www.paloaltonetworks.com/blog/2025/08/securing-the-quantum-age/)
- [Palo Alto: Introducing Quantum-Safe Security (January 2026)](https://www.paloaltonetworks.com/blog/2026/01/introducing-quantum-safe-security/)
- [Post-Quantum TLS for PAN-OS management plane (docs)](https://docs.paloaltonetworks.com/content/techdocs/en_US/whats-new/new-features/august-2025/post-quantum-ssl-support-for-pan-os-management)
- [Quantum Computing Report: PAN-OS 12.1](https://quantumcomputingreport.com/palo-alto-networks-introduces-pan-os-12-1-orion-with-post-quantum-cryptography-features/)

<!-- TODO: Confirm GlobalProtect VPN PQC GA status in PAN-OS 12.x or later -->
<!-- TODO: Identify PA-5500 Gen5 hardware PQC acceleration specifics — which algorithms offloaded? -->

---

## Fortinet

### FortiOS 7.6.x — First Commercial Firewall GA

**Fortinet is the earliest confirmed GA vendor for native ML-KEM IKEv2 support in a commercial firewall OS.**

**PQC feature rollout by FortiOS version:**

| Version | Feature |
|---|---|
| 7.4.x | QKD integration support (initial; no ML-KEM KEM) |
| **7.6.1** | **ML-KEM IPsec IKEv2 (RFC 9242/9370 hybrid) — first GA** |
| 7.6.3 | QKD + ML-DSA digital signature support; hybrid QKD+PQC+DH key mixing |
| 7.6.5 | PQC for Agentless (clientless) VPN; TLS 1.3 hybrid PQC SSL deep inspection (flow mode) |
| 7.6.6 | Latest current release; all above features present |

**Algorithms — IKEv2 (official documentation confirmed):**

*FIPS 203 standardized:*
- ML-KEM-512 (keyword: `kyber512`)
- ML-KEM-768 (keyword: `kyber768`)
- ML-KEM-1024 (keyword: `kyber1024`)

*Additional non-FIPS / pre-standard:*
- BIKE
- HQC
- FrodoKEM

**Implementation details:** RFC 9370 (Multiple Key Exchanges in IKEv2) with RFC 9242 (IKE_INTERMEDIATE). Up to 7 additional key exchange rounds (ADDKE1–ADDKE7), up to 3 KE groups per round. CLI: `set addke1 <option>` in Phase 1/2 config.

**Protocol layers:**
- IKEv2/IPsec (site-to-site, dial-up) — 7.6.1 GA
- IPsec Agentless VPN — 7.6.5
- TLS 1.3 deep inspection (flow mode) with hybrid PQC — 7.6.5
- Digital signatures (ML-DSA via FIPS 204 KAT) — 7.6.3
- QKD integration — 7.6.3+

**Hybrid vs. PQC-only:** Hybrid mode is the default. Pure PQC mode configurable via CLI in 7.6.5 Agentless VPN feature.

**FortiASIC hardware acceleration:** No public documentation confirms FortiASIC (NP7/NP6/CP9) hardware offload for lattice-based PQC operations. FortiASIC documentation covers traditional RSA/DH/AES acceleration. PQC is currently software-only on FortiGate CPUs.

**FortiClient VPN PQC:** Not explicitly confirmed for FortiClient as a client-side feature. Agentless VPN PQC (7.6.5) covers clientless SSL VPN only.

**FIPS 140-3:** Fortinet documentation confirms FIPS 203 algorithm compliance and FIPS 204 KAT testing. No CMVP FIPS 140-3 module validation certificate for FortiOS PQC module confirmed in public records.

**Sources:**
- [FortiOS 7.6.0 New Features: PQC for IPsec Key Exchange 7.6.1 (official docs)](https://docs.fortinet.com/document/fortigate/7.6.0/new-features/229631/enhancing-security-with-post-quantum-cryptography-for-ipsec-key-exchange-7-6-1)
- [FortiOS 7.6.6 Administration Guide: PQC for IPsec Key Exchange](https://docs.fortinet.com/document/fortigate/7.6.6/administration-guide/229631/post-quantum-cryptography-for-ipsec-key-exchange)
- [FortiOS 7.6.3: QKD and ML-DSA Support](https://docs.fortinet.com/document/fortigate/7.6.0/new-features/249519/support-quantum-key-distribution-and-digital-signature-algorithm-post-quantum-cryptography-7-6-3)
- [FortiOS 7.6.5: PQC for Agentless VPN](https://docs.fortinet.com/document/fortigate/7.6.0/new-features/43632/post-quantum-cryptography-for-agentless-vpn-7-6-5)
- [FortiOS 7.6.5: Hybrid PQC SSL Deep Inspection](https://docs.fortinet.com/document/fortigate/7.6.0/new-features/90507/hybrid-post-quantum-cryptography-in-ssl-deep-inspection-in-flow-mode-7-6-5)
- [Security Brief: Fortinet adds quantum-safe encryption to FortiOS 7.6](https://securitybrief.com.au/story/fortinet-adds-quantum-safe-encryption-to-fortios-7-6-update)

<!-- TODO: Confirm whether FortiASIC NP7/NP6 roadmap includes lattice-based PQC offload -->
<!-- TODO: Track FortiClient client-side PQC VPN timeline -->
<!-- TODO: Check NIST CMVP for FortiOS PQC module validation filings -->

---

## Check Point

### Gaia OS R82 — GA with API-Only Configuration

**Status:** R82 is GA. R82.10 was in Early Availability (EA) for TLS inspection as of late 2025.

**Algorithms (confirmed, official documentation):**
- ML-KEM-768 (Kyber768) — default; paired with DH Group 15 (3072-bit) in default proposals
- ML-KEM-512 (Kyber512) — available via API
- ML-KEM-1024 (Kyber1024) — available via API

**Protocol layers:**
- IKEv2 site-to-site VPN — R82 GA (RFC 9242 + RFC 9370 hybrid key exchange)
- TLS/HTTPS inspection — R82.10 EA: handles `X25519MLKEM768` cipher suites
- Remote Access VPN — Roadmap item; not yet GA

**Implementation:** Hybrid key exchange combining classical Diffie-Hellman with ML-KEM. Automatic fallback to classical algorithms if remote peer does not support PQC.

**Configuration:** API-based configuration for PQC VPN settings. **No GUI support confirmed** — this is a meaningful operational barrier for organizations without API automation workflows.

**SMB / Quantum Spark appliances:** No confirmed PQC timeline for the Quantum Spark (SMB) lineup. (Note: Check Point's firewall line is called "Quantum Security Gateway" — unrelated to quantum computing — creating potential search confusion.)

**Performance:** CPU overhead concentrated at IKE handshake/rekey. ML-KEM-768 public key + ciphertext ~1 KB may require IKEv2 fragmentation. Steady-state per-packet symmetric crypto cost unchanged. CoreXL multithreaded IKE processing handles load.

**FIPS 140-3:** Not confirmed for R82 PQC module.

**Sources:**
- [Check Point: Quantum-Safe Cybersecurity — Current Capabilities and Road Ahead](https://blog.checkpoint.com/innovation/quantum-safe-cyber-security-current-capabilities-and-the-road-ahead/)
- [Check Point R82 Admin Guide: Quantum-Safe Key Exchange](https://sc1.checkpoint.com/documents/R82/WebAdminGuides/EN/CP_R82_SitetoSiteVPN_AdminGuide/Content/Topics-VPNSG/Quantum-Safe-Key-Exchange.htm)
- [Check Point CheckMates community: PQC for IPsec VPN questions](https://community.checkpoint.com/t5/Security-Gateways/Questions-about-Post-Quantum-Cryptography-PQC-for-IPsec-VPN/td-p/262570)
- [Qtonic Score: Check Point R82 PQ VPN](https://qtonicquantum.com/lab/solutions/checkpoint-r82-pq-vpn)

<!-- TODO: Track R82 GUI support for PQC VPN configuration -->
<!-- TODO: Track Remote Access VPN PQC timeline for Gaia OS -->
<!-- TODO: Confirm Quantum Spark (SMB) PQC roadmap -->

---

## Nokia

### SR OS — ANYsec Layer-2.5 Encryption

**ANYsec (Nokia's proprietary layer-agnostic encryption):**
- **Introduced:** SR OS 23.10.R1 (requires FP5 silicon)
- **Latest confirmed version:** SR-SIM 25.7.R1

**Technical architecture:** ANYsec is built on MACsec standards foundation, extended to encrypt Layer 2, 2.5 (MPLS), and Layer 3 simultaneously. Cipher suite: GCM-AES-XPN-128 / GCM-AES-XPN-256. Key exchange via MACsec Key Agreement (MKA) over UDP.

**Important distinction:** Nokia's "quantum-safe" claim for ANYsec rests primarily on **AES-256 symmetric encryption** being resistant to Grover's algorithm (which halves key strength, leaving AES-256 at an effective 128-bit quantum security level — still considered secure). This is a valid claim, but it is different from deploying ML-KEM (FIPS 203) in the key exchange — the key exchange in ANYsec/MKA uses classical DH, not a post-quantum KEM.

**Built-in QKD:** Nokia has announced a built-in Quantum Key Distribution (QKD) board insertable into NetEngine 8000E series routers — providing truly quantum-random key injection for AES-256 session keys. This is a QKD approach (hardware photon-based key distribution), distinct from algorithm-based PQC.

**ML-KEM IKEv2 for SR OS IPsec:** Nokia published a blog post in January 2026 addressing quantum-resistant IPsec using RFC 8784/RFC 9370 hybrid approaches. However, a specific SR OS version number confirming GA ML-KEM IKEv2 support has not been identified in available public documentation as of April 2026. Nokia's primary quantum positioning is ANYsec + QKD for the service provider market.

**Research:** Nokia Bell Labs published in MDPI Future Internet (2026): "Towards Quantum-Safe O-RAN: Experimental Evaluation of ML-KEM-Based IPsec on the E2 Interface" — confirming active ML-KEM IPsec research.

**FIPS 140-3:** Not confirmed.

**Sources:**
- [Nokia ANYsec Quantum-Safe Network Cryptography (white paper)](https://www.nokia.com/asset/i/210676/)
- [Nokia: Road to Quantum-Safe Networks (white paper)](https://www.nokia.com/asset/i/214685/)
- [SReXplore: Enable Quantum-Safe Network Transport with ANYsec](https://srexplore.srexperts.net/nos/sros/beginner/41-ANYsec/)
- [MDPI Future Internet: Towards Quantum-Safe O-RAN (2026)](https://www.mdpi.com/1999-5903/18/4/188)

<!-- TODO: Identify specific SR OS release with GA ML-KEM IKEv2 if published -->
<!-- TODO: Distinguish Nokia's QKD board commercial availability from lab demonstration -->

---

## Aruba Networks (HPE)

**Status:** No GA PQC implementation confirmed in available public documentation for ArubaOS (wireless) or AOS-CX (switching) as of April 2026.

**EdgeConnect SD-WAN:** EdgeConnect uses a patented "IKE-less" IPsec key exchange architecture for the data plane. No confirmed GA PQC feature in available sources.

**HPE / Juniper alignment:** Both Aruba and Juniper are now HPE divisions following the March 2024 Juniper acquisition. Whether their PQC roadmaps will be harmonized under HPE has not been publicly detailed as of April 2026.

**Assessment:** Aruba/HPE networking appears behind the leaders (Palo Alto, Fortinet, Cisco) in PQC GA deployments. Likely on roadmap for 2026–2027.

<!-- TODO: Monitor HPE unified networking roadmap for Aruba/Juniper PQC convergence -->

---

## Ericsson

**Focus:** 5G core network and radio access network (RAN) management interfaces — not traditional enterprise networking.

**Known activity:** Ericsson has contributed to 3GPP standards discussions on quantum-safe security for 5G. PQC for 5G authentication and key agreement is a longer-horizon standardization effort at 3GPP. Ericsson has published quantum security intent aligned with ETSI and ENISA guidance.

<!-- TODO: Expand if Ericsson enterprise networking PQC becomes more directly relevant to this section's scope -->

---

## Huawei

**Status:** Xinghe Intelligent Traffic-Encryption Integration Solution announced at MWC Barcelona, March 2026.

**Xinghe capabilities (per announcement):**
- Three quantum-resistance methods: PQC algorithms, external QKD, and built-in QKD board
- Built-in QKD board insertable into **NetEngine 8000E series routers** — described as an industry first
- Xinghe AI Full-Scope Security Campus Solution: end-to-end MACsec + PQC algorithms
- VRP OS version numbers for PQC features not disclosed in public sources

**Geopolitical context:** Huawei equipment is restricted or banned in many Western markets (US, UK, EU telecoms core networks). PQC claims are technically relevant but cannot be independently verified via Western lab testing or US FIPS certification processes.

**Sources:**
- [Huawei Xinghe launch at MWC (March 2026)](https://e.huawei.com/en/news/2026/solutions/enterprise-network/xinghe-intelligent-traffic-encryption)
- [Huawei Xinghe at MWC (SDxCentral)](https://www.sdxcentral.com/news/huawei-pitches-xinghe-quantum-secure-wan-platform-at-mwc/)

---

## Vendors Without Confirmed PQC Support

The following vendors have no confirmed GA PQC support as of April 2026:

- **SonicWall (SonicOS):** No public announcement of ML-KEM or RFC 9370 hybrid key exchange. No roadmap statements identified.
- **Zyxel (ZyWALL/USG/ATP):** IKEv2 and AES-GCM support present; no quantum-safe extensions documented.
- **Extreme Networks:** No public PQC roadmap or GA announcement identified.

---

## Open-Source and Protocol Reference Implementations

### strongSwan 6.0.x — Reference IKEv2 ML-KEM Implementation

**strongSwan is the de facto open-source reference implementation for ML-KEM IKEv2, used by Cloudflare and others for interoperability testing.**

- **First GA ML-KEM release:** strongSwan 6.0.0 (released December 3, 2024)
- **strongSwan 6.0.2** (released July 14, 2025): Added ML-KEM via OpenSSL 3.5+ backend

**Algorithms supported:**
- ML-KEM-512 (keyword: `mlkem512`, NIST category 1)
- ML-KEM-768 (keyword: `mlkem768`, category 3) — NIST recommended default
- ML-KEM-1024 (keyword: `mlkem1024`, category 5)

**Cryptographic library backends:**
- Botan 3.6.0+
- wolfSSL 5.7.4+
- AWS-LC 1.37.0+
- OpenSSL 3.5+ (added in 6.0.2)
- Built-in `ml` plugin

**IKEv2:** Full RFC 9370 + RFC 9242 support. Up to 7 additional key exchanges (`ke1_` through `ke7_` prefixes). Example config: `x25519-ke1_mlkem768` for hybrid X25519 + ML-KEM-768.

**Sources:**
- [strongSwan 6.0.0 release blog](https://strongswan.org/blog/2024/12/03/strongswan-6.0.0-released.html)
- [strongSwan 6.0.2 release blog](https://www.strongswan.net/blog/2025/07/14/strongswan-6.0.2-released.html)
- [Cloudflare: Standardizing Post-Quantum IPsec (InfoQ, March 2026)](https://www.infoq.com/news/2026/03/cloudflare-post-quantum-ipsec/)

---

### OpenSSL 3.5 — ML-KEM as TLS 1.3 Default

**Release date:** April 8, 2025 (LTS; supported until April 8, 2030).

**PQC algorithms natively in mainline (no provider plugin required):**
- ML-KEM-512, ML-KEM-768, ML-KEM-1024 (FIPS 203)
- ML-DSA-44, ML-DSA-65, ML-DSA-87 (FIPS 204)
- SLH-DSA multiple parameter sets (FIPS 205)

**TLS 1.3 default change:** Default keyshares are now **X25519MLKEM768** and X25519. Hybrid PQC is the new default for any server/client built on OpenSSL 3.5. This cascades across all Linux-based network device management planes using OpenSSL.

**oqs-provider:** For pre-standard algorithms (BIKE, HQC, Classic McEliece, FrodoKEM), the Open Quantum Safe project's `oqs-provider` plugin remains available.

**Sources:**
- [OpenSSL 3.5.0 final release (April 8, 2025)](https://openssl-library.org/post/2025-04-08-openssl-35-final-release/)
- [Help Net Security: OpenSSL 3.5.0 released](https://www.helpnetsecurity.com/2025/04/09/openssl-3-5-0-released/)

---

### WireGuard — PSK Injection as Quantum Workaround

WireGuard intentionally has no cryptographic agility — it fixes Curve25519 + ChaCha20-Poly1305 in the core protocol. Native in-protocol ML-KEM is not possible without forking the protocol.

**Production quantum-resistance approach (PSK injection):**
WireGuard's existing optional PSK (pre-shared key) feature can be used to inject a quantum-safe symmetric key. PSK is mixed into the handshake KDF, providing quantum resistance to the key exchange as long as the PSK is delivered via a separate PQC-secured channel. Major deployments:

- **NordVPN (NordLynx/WireGuard):** Full cross-platform PQC deployment completed early 2025 (Linux September 2024, then Windows, macOS, iOS, Android, tvOS). ML-KEM-derived PSKs delivered over a TLS 1.3/ML-KEM control channel.
- **Tailscale:** Similar PSK injection; ML-KEM hybrid via separate control channel.
- **ExpressVPN:** Hybrid ML-KEM TLS 1.3 for key delivery + WireGuard PSK injection; reported 15–20ms additional connection establishment time; no steady-state throughput impact.

**Assessment:** WireGuard quantum resistance in production is achieved through a workaround, not a native protocol change. A formal PQ-WireGuard protocol extension remains an open research question.

**Sources:**
- [Tailscale: Post-Quantum Cryptography documentation](https://tailscale.com/kb/1460/post-quantum-cryptography)

---

## Cloudflare

**Cloudflare One:** First SASE with modern PQC deployed, February 2026.
- Cloudflare One Appliance — added ML-KEM hybrid (X25519MLKEM768) PQC encryption on February 11, 2026 ([changelog](https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/))
- Cloudflare's internal infrastructure has been running hybrid ML-KEM TLS since 2023

**Sources:**
- [Cloudflare One: First SASE with Modern PQC (February 2026)](https://blog.cloudflare.com/post-quantum-sase/)
- [Cloudflare One Appliance PQC Changelog](https://developers.cloudflare.com/changelog/post/2026-02-11-appliance-post-quantum-encryption/)

---

## Vendor Comparison Summary

| Vendor | Product | First GA PQC Release | Algorithms (FIPS names) | Protocols | Hybrid | HW Accel | FIPS 140-3 |
|---|---|---|---|---|---|---|---|
| Sitehop | Proprietary FPGA | GA (claimed) | ML-KEM (FIPS 203) | IKEv2/IPsec | Yes | FPGA | Not confirmed |
| Juniper (HPE) | Junos OS | Roadmap | ML-KEM (TBD) | IKEv2/IPsec | Yes (planned) | No | Not confirmed |
| Cisco | IOS XE 26 (Apr 2026) | Full-stack | ML-KEM-1024 | IPsec, SSH, MACsec, TLS | Yes | Catalyst 9000 | Pending |
| Cisco | ASA 9.19 (transitional) | RFC 9370 hybrid | ML-KEM (variant TBC) | IKEv2/IPsec | Yes | No | Not confirmed |
| Cisco | FTD 10.5 (late 2026) | Not yet GA | ML-KEM (FIPS 203) | IKEv2, TLS | Yes | No | Not confirmed |
| **Palo Alto** | **PAN-OS 12.1 (Aug 2025)** | **All FIPS 203/204/205** | ML-KEM/ML-DSA/SLH-DSA + experimental | IPsec, TLS (mgmt + inspect), SASE | Both | PA-5500 Gen5 | Referenced, not validated |
| **Fortinet** | **FortiOS 7.6.1** | **ML-KEM-512/768/1024 (FIPS 203)** | + BIKE, HQC, FrodoKEM | IPsec, TLS (7.6.5), Agentless VPN | Yes | No | FIPS 203 compliance; no CMVP module |
| **Check Point** | **Gaia R82** | **ML-KEM-512/768/1024 (default: 768)** | ML-KEM only (R82); ML-DSA TBD | IKEv2/IPsec; TLS (R82.10 EA) | Yes (mandatory) | No | Not confirmed |
| Nokia | SR OS 23.10.R1 (ANYsec) | AES-256 + QKD | ANYsec: AES-256; ML-KEM IKEv2 version TBC | L2/L2.5/L3 (ANYsec) | N/A | FP5 silicon (ANYsec) | Not confirmed |
| Aruba/HPE | ArubaOS / EdgeConnect | Not GA | None confirmed | N/A | N/A | N/A | N/A |
| SonicWall | SonicOS | Not GA | None confirmed | N/A | N/A | N/A | N/A |
| Huawei | VRP / Xinghe | MWC Mar 2026 (announced) | PQC + QKD (specs undisclosed) | MACsec, IPsec | Yes | Built-in QKD board | N/A |
| strongSwan | 6.0.0 (Dec 2024) | ML-KEM-512/768/1024 | IKEv2/IPsec | Both | No | N/A (OSS) |
| OpenSSL | 3.5 (Apr 2025) | ML-KEM/ML-DSA/SLH-DSA | TLS 1.3 (default hybrid) | Default hybrid | No | N/A (library) |
| WireGuard | PSK workaround only | ML-KEM (via external PSK) | WireGuard tunnel | Yes (PSK hybrid) | No | N/A |
| Cloudflare One | Feb 2026 | X25519MLKEM768 | SASE/TLS | Yes | No | N/A |

*All status assessments are based on public documentation as of April 2026 and are subject to change. Verify against current vendor release notes before making procurement decisions.*

## Sources

- [NIST PQC Standards (FIPS 203/204/205)](https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization)
- [IETF RFC 9370: Multiple Key Exchanges in IKEv2](https://www.rfc-editor.org/rfc/rfc9370)
- [RFC 9794: Terminology for PQC/Traditional Hybrid Schemes](https://www.rfc-editor.org/rfc/rfc9794.html)
- [draft-ietf-ipsecme-ikev2-mlkem-05 (IETF datatracker)](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/)
- [draft-ietf-tls-hybrid-design-16 (IETF datatracker)](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/16/)
- [NSA CNSA 2.0](https://media.defense.gov/2022/Sep/07/2003071834/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS_.PDF)
- [CISA PQC Migration Guidance](https://www.cisa.gov/quantum)
- [Open Quantum Safe (OQS) Project](https://openquantumsafe.org)
- [IETF PQUIP: State of Protocols and PQC](https://github.com/ietf-wg-pquip/state-of-protocols-and-pqc)
- [2025 in Review: FIPS 140-3, PQC, Crypto-Agility (SafeLogic)](https://www.safelogic.com/blog/2025-in-review-fips-140-3-post-quantum-readiness-crypto-agility)
