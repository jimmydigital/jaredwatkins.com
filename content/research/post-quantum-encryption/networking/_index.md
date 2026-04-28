---
title: "PQC in Networking"
date: 2026-04-15
lastmod: 2026-04-17
draft: false
description: "Post-quantum cryptography support across networking hardware and software vendors: algorithms, protocol layers, firmware versions, and deployment timelines."
tags: ["post-quantum", "cryptography", "networking", "pqc", "ike-pqc", "tls-pqc"]
categories: ["overview"]
research_area: "post-quantum-encryption/networking"
last_reviewed: 2026-04-17
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


{{< steering >}}

## Networking PQC Section — Steering Instructions

This section tracks post-quantum cryptography adoption across networking hardware vendors, software platforms, and the network protocols they implement. Standard Research section rules and the PQC section steering document both apply here.

---

### Scope

**In scope:**
- Networking hardware vendors (routers, switches, firewalls, VPN concentrators, SD-WAN appliances) that have shipped or roadmapped PQC support
- Network protocol implementations: IKEv2/IPsec PQC (RFC 9242, RFC 9370), TLS 1.3 PQC hybrid extensions, SSH PQC, MACsec PQC
- Dedicated PQC networking security vendors and appliances (e.g., Sitehop)
- Managed security service providers (MSSPs) and cloud security vendors implementing PQC at the network layer

**Out of scope:**
- General application-layer PQC (messaging apps, email encryption, browser TLS) — unless the vendor is primarily a network infrastructure company
- Quantum key distribution (QKD) — a separate technology (hardware photon-based key distribution, not algorithm-based PQC); track separately if warranted
- Post-quantum VPN clients for end-user devices (consumer VPN apps) — unless the client is a managed enterprise product

---

### Protocol Layers Relevant to Networking PQC

Networking PQC adoption is protocol-layer-specific. When documenting vendor support, always specify which protocol layer is covered:

1. **IKEv2/IPsec** — the dominant VPN and site-to-site encryption protocol in enterprise networking. IETF RFC 9242 (Intermediate Exchange) and RFC 9370 (Multiple KE Payloads) provide the framework for adding PQC KEMs to IKEv2 negotiation. This is the most critical layer for most enterprise networking equipment.
2. **TLS 1.3** — used for management interfaces, web UIs, and increasingly for data-plane encryption in SD-WAN and SASE products. IETF has published hybrid key exchange drafts; browser vendors (Chrome, Firefox) have deployed X25519Kyber768 hybrid exchanges since 2023.
3. **SSH** — used for device management (CLI access). OpenSSH 9.0+ supports NTRU Prime hybrid by default; vendors need to update their embedded SSH stack.
4. **MACsec (IEEE 802.1AE)** — Layer 2 link encryption; key exchange managed separately (typically 802.1X/MKA). PQC integration at MACsec layer is nascent.
5. **DTLS** — used in some SD-WAN and wireless protocols; PQC DTLS drafts are in progress at IETF.

---

### Vendor Entry Requirements

Each vendor entry must include:

1. **PQC support status** — clearly state: Not started / Roadmap announced / Beta/Preview / GA available
2. **Supported algorithms** — exact NIST standards (ML-KEM-768, ML-KEM-1024, ML-DSA-65, etc.) or pre-standard names with mapping to FIPS numbers
3. **Protocol layers** — IKEv2, TLS, SSH, MACsec — which layers are covered
4. **Product scope** — which product lines and specific model/software versions
5. **Hybrid vs. PQC-only** — document explicitly
6. **Performance impact** — documented or expected CPU/memory overhead; hardware offload availability
7. **Interoperability** — tested against which other vendors or open-source implementations
8. **FIPS 140-3 / Common Criteria status** — is the PQC implementation certified or in validation?
9. **Key People** — contacts or leads driving the PQC program (public information only)
10. **Claim Verification** — per PQC section steering: decompose "quantum-safe" claims into specifics

---

### Networking PQC — Market Context

As of April 2026, the networking PQC market is in early transition:

- **Standards are finalized** (FIPS 203/204/205 published August 2024) but **vendor implementations lag**. Most major networking vendors have published roadmaps but production-ready, FIPS-validated PQC implementations are limited.
- **IKEv2/IPsec is the leading deployment target** for networking equipment. IETF RFC 9242 and 9370 are the relevant standards; most enterprise router and firewall vendors are working on or have announced IKEv2 PQC support.
- **CNSA 2.0 creates a hard mandate for US government customers.** NSA's Commercial National Security Algorithm Suite 2.0 requires quantum-resistant algorithms for national security systems by 2030 (for most categories). This is pulling forward networking vendor timelines.
- **Interoperability is an open problem.** Different vendors are implementing different algorithm variants, hybrid schemes, and negotiation mechanisms. Multi-vendor PQC IPsec is not reliably plug-and-play as of early 2026.
- **Sitehop** is an outlier: a UK startup focused specifically on high-performance PQC networking, with a different market position than incumbent vendors adding PQC to existing platforms.

---

### Review Cadence

- 90 days for all active vendor entries (PQC roadmaps and firmware releases are moving fast)
- 90 days for this section landing page

---

{{< /steering >}}

## Overview

This section tracks post-quantum cryptography adoption across networking infrastructure: which vendors have shipped PQC-capable products, which algorithms and protocol layers are supported, and what the realistic deployment landscape looks like as of 2026.

The networking layer is particularly critical for PQC migration because it protects in-transit data across enterprise WANs, VPNs, and internet-facing services — the most direct exposure point for the harvest-now-decrypt-later (HNDL) threat. Migration here requires coordination between standards (IKEv2/IPsec RFCs, TLS extensions), hardware capability (some PQC algorithms require crypto accelerator support for line-rate performance), and interoperability between vendor implementations.

**Research status:** Phase 1 — active. Sitehop and Juniper have dedicated entries; Cisco, Palo Alto, Fortinet, Check Point, Nokia, and open-source implementations are covered in the vendor survey. As of April 2026, Fortinet (FortiOS 7.6.1), Palo Alto (PAN-OS 12.1), Check Point (Gaia R82), and Cisco (ASA 9.19 transitional; IOS XE 26 full-stack) all ship GA ML-KEM IKEv2 support.

## Key Themes

- IKEv2/IPsec (RFC 9242/9370) is the primary integration point for enterprise networking equipment
- Most major vendors have PQC on their 2025–2027 roadmaps; production-ready FIPS-validated implementations are limited as of April 2026
- NSA CNSA 2.0 mandates create a hard deadline for US government network infrastructure by 2030
- Interoperability between vendor implementations remains an unsolved operational challenge
- Dedicated PQC networking vendors (Sitehop) offer purpose-built approaches distinct from incumbents' PQC-added-to-existing-platforms

## Vendors

### Dedicated PQC Vendors

| Company | HQ | Stage | Focus |
|---------|-----|-------|-------|
| [Sitehop](https://www.sitehop.io) | Bristol, UK | Private (Series A stage) | Hardware-accelerated PQC networking; FPGA-based PQC IPsec appliances; focus on line-rate PQC without CPU overhead penalty. See [entry]({{< relref "sitehop-pqc-support.md" >}}). |

### Established Networking Vendors

| Company | PQC Status | First GA Release | Primary Layer | Notes |
|---------|-----------|-----------------|---------------|-------|
| [Juniper Networks](https://www.juniper.net) | Roadmap | TBD | IKEv2/IPsec | Now HPE division; Junos GA version unconfirmed; see [entry]({{< relref "juniper-pqc-support.md" >}}). |
| [Cisco Systems](https://www.cisco.com) | **GA (partial/full)** | ASA 9.19 (RFC 9370); IOS XE 26 (full-stack, Apr 2026) | IKEv2/IPsec, SSH, MACsec, TLS | FTD 10.5 with ML-KEM targeted late 2026; see [vendor survey]({{< relref "other-vendors.md" >}}). |
| [Palo Alto Networks](https://www.paloaltonetworks.com) | **GA** | PAN-OS 11.2 (IKEv2); PAN-OS 12.1 Orion (Aug 2025, full) | IKEv2/IPsec, TLS (mgmt + inspect), SASE | Broadest algorithm coverage (FIPS 203/204/205); PA-5500 Gen5 HW accel; see [vendor survey]({{< relref "other-vendors.md" >}}). |
| [Fortinet](https://www.fortinet.com) | **GA** | **FortiOS 7.6.1** (earliest confirmed GA) | IKEv2/IPsec, TLS (7.6.5), Agentless VPN | ML-KEM-512/768/1024; software-only (no FortiASIC offload); see [vendor survey]({{< relref "other-vendors.md" >}}). |
| [Check Point](https://www.checkpoint.com) | **GA** | Gaia R82 | IKEv2/IPsec; TLS (R82.10 EA) | Default ML-KEM-768; API-only config (no GUI); see [vendor survey]({{< relref "other-vendors.md" >}}). |
| [Nokia](https://www.nokia.com) | Roadmap / ANYsec | SR OS 23.10.R1 (ANYsec AES-256 + QKD) | L2/L2.5/L3 (ANYsec), IKEv2 TBC | "Quantum-safe" via AES-256 symmetric + QKD; ML-KEM IKEv2 SR OS version unconfirmed; see [vendor survey]({{< relref "other-vendors.md" >}}). |

<!-- TODO: Add public company table and TradingView widget. Public comparables: Cisco (CSCO), Palo Alto Networks (PANW), Fortinet (FTNT), HPE/Juniper (HPE). -->
