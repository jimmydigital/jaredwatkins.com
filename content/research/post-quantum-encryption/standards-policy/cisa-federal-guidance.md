---
title: "Federal Civilian Agency Guidance (CISA & OMB)"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "CISA and OMB post-quantum cryptography guidance, federal buying directives, and compliance timelines for civilian agencies"
tags: ["cisa", "omb", "federal-agencies", "civilian", "m-23-02", "buying-guidance", "critical-infrastructure"]
categories: ["policy", "guidance"]
research_area: "post-quantum-encryption/standards-policy"
source_urls:
  - "https://www.cisa.gov/pqc"
  - "https://www.whitehouse.gov/wp-content/uploads/2022/11/M-23-02-M-Memo-on-Migrating-to-Post-Quantum-Cryptography.pdf"
  - "https://thequantuminsider.com/2026/01/27/cisa-issues-federal-buying-guidance-for-post-quantum-cryptography/"
last_reviewed: 2026-04-24
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Overview: Two Tracks for Federal Agencies

The U.S. federal government's PQC transition has two parallel tracks:

1. **National Security Systems (NSA → CNSA 2.0)** — Covered in the [NSA CNSA 2.0 entry](nsa-cnsa-2.md)
2. **Civilian Federal Agencies (CISA → OMB M-23-02)** — Covered here

CISA (Cybersecurity and Infrastructure Security Agency) operates under the Department of Homeland Security and leads PQC guidance for civilian agencies, critical infrastructure, and state/local governments. These entities don't necessarily handle classified data but may handle sensitive or critical infrastructure information.

---

## OMB M-23-02: The Federal Mandate (November 18, 2022)

On November 18, 2022, the White House Office of Management and Budget (OMB) issued [Memorandum 23-02 "Migrating to Post-Quantum Cryptography"](https://www.whitehouse.gov/wp-content/uploads/2022/11/M-23-02-M-Memo-on-Migrating-to-Post-Quantum-Cryptography.pdf) to all executive departments, CFO Act agencies, and federal IT organizations.

### Key Requirements of M-23-02

#### 1. Cryptographic System Inventory (Deadline: May 4, 2023; Recurring Annually)

Each agency must submit an **inventory of cryptographic systems** to the Office of the National Cyber Director (ONCD) and CISA, including:

- System name and description
- Cryptographic algorithms used (RSA key sizes, ECDH, ECDSA, etc.)
- Quantum vulnerability assessment
- Implementation status (in-service, planned, decommissioned)
- Data confidentiality requirements (how long must encryption last?)
- Migration feasibility and timeline estimate

**Current status (2026):** Agencies have been submitting annual inventories since 2023. CISA publishes aggregate findings.

#### 2. Transition Planning (Deadline: Ongoing; Plan Due by May 4 each year)

Agencies must develop and update **migration roadmaps** including:
- Prioritization of systems (risk-based)
- Timeline for transition to NIST-standardized PQC algorithms
- Budgeting and resource allocation
- Testing and validation approach
- Vendor engagement plan

#### 3. Funding Estimates (Deadline: Ongoing)

The **preliminary government-wide cost estimate** for PQC migration from 2025–2035 is approximately **$7.1 billion** (in 2024 dollars). Individual agencies must provide budget justification to OMB.

### Compliance Mechanism

- **Non-compliance risk:** OMB can condition IT funding on demonstrated PQC migration progress
- **Reporting:** Annual submission to ONCD/CISA by May 4
- **Enforcement:** OMB Circular A-130 (cybersecurity requirements for federal IT systems) ties compliance to agency funding

---

## CISA PQC Guidance & Roadmap

CISA has issued multiple guidance documents and announcements:

### Executive Order 14306 (June 2025)

The White House issued an executive order directing CISA and DHS to:
1. Identify product categories where PQC-capable solutions are commercially available
2. Publish guidance on procuring only PQC-capable products in those categories by **January 1, 2026**
3. Update the list quarterly as the market matures

**Impact:** This creates **federal procurement requirements** for covered product categories.

### CISA Product Categories for PQC Standards (January 23, 2026)

[Product Categories for Technologies That Use Post-Quantum Cryptography Standards](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards)

Effective January 23, 2026, CISA published an initial list of product categories in which PQC-capable options are widely available. Federal agencies are required to **procure only from PQC-capable vendors** in these categories starting **immediately** (January 2026).

**Examples of covered categories:**
- TLS/HTTPS servers and clients
- VPN products (IKEv2/IPsec support required by RFC 9242/9370)
- Certificate authorities and PKI solutions
- Hardware security modules (HSMs)
- Cloud services (AWS, Azure, Google Cloud PQC support)
- SSH implementations
- Email/messaging encryption

**Update frequency:** CISA will update the list quarterly as:
- Vendors release PQC-capable versions
- New product categories mature
- Market adoption increases

**Implication for 2026:** Agencies procuring IT equipment must now verify PQC capabilities for all covered categories. Non-compliance can invalidate federal IT contracts.

### CISA Migration Roadmap (Ongoing)

CISA publishes recommendations for organizations to develop their own PQC migration roadmaps:

1. **Phase 1 (2024–2025): Assess & Plan**
   - Inventory cryptographic systems
   - Assess quantum vulnerability
   - Identify priority systems for early migration
   - Engage vendors and system owners

2. **Phase 2 (2025–2030): Deploy & Transition**
   - Test NIST-standardized algorithms in pilot systems
   - Deploy hybrid mode (classical + PQC in parallel)
   - Upgrade high-priority systems
   - Monitor vendor support and standards evolution

3. **Phase 3 (2030–2035): Full Migration**
   - Complete transition to PQC-only systems
   - Decommission unsupported legacy systems
   - Validate full compliance with CNSA 2.0 (for NSS) or NIST standards (for civilian systems)

**CISA's emphasis:** Start now (2025–2026); the 10-year window is tight for large organizations with complex infrastructure.

---

## CISA/NSA Joint Advisories for Critical Infrastructure

CISA and NSA have published sector-specific joint guidance for critical infrastructure organizations:

### Covered Sectors

- **Water & Wastewater Systems** — CISA joint advisory on PQC for SCADA/ICS
- **Energy Sector** — Guidance on utility grid cryptography upgrades
- **Finance** — Banking and payment system PQC requirements
- **Communications** — Telecom providers and backbone infrastructure
- **Transportation** — Air traffic control, rail, maritime systems

### Key Message

Critical infrastructure operators must begin PQC migration planning immediately, with priority on systems protecting data with long confidentiality needs (e.g., power grid control algorithms, financial settlement systems).

---

## FedRAMP Implications

[FedRAMP (Federal Risk and Authorization Management Program)](https://www.fedramp.gov/) is the U.S. government's program for certifying cloud services for federal use. As of April 2026, FedRAMP has begun integrating PQC requirements:

### FedRAMP PQC Integration (2025–2026)

**Current status:**
- FedRAMP updates its baseline security requirements (FedRAMP Security Requirements for Cloud Service Providers) to include PQC support
- Cloud service providers (AWS GovCloud, Azure Government, Google Cloud Government) are implementing PQC options

**What this means:**
- New FedRAMP authorizations (starting 2026) must demonstrate PQC-capable TLS/encryption
- Re-authorizations (3-year cycle) will require PQC readiness plans
- By 2028, FedRAMP expects all authorized cloud services to offer PQC options

**Implication:** Federal agencies using cloud services for sensitive data must verify that their cloud providers have achieved PQC-capable certifications by their re-authorization deadlines.

---

## NIST SP 800-175B (Guidance for Federal Cryptography)

[NIST Special Publication 800-175B: Guideline for Using Cryptographic Standards in the Federal Government](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-175b.ipd.pdf) provides federal IT organizations with recommendations for algorithm selection.

### PQC Updates (2025–2026)

- **ML-KEM-768 or ML-KEM-1024** — Recommended for federal systems requiring long-term confidentiality
- **ML-DSA-65 or ML-DSA-87** — Recommended for digital signatures
- **Hybrid mode** — Classical algorithm + PQC algorithm in parallel during transition phase (through ~2030–2033)
- **Transition timeline** — Agencies should support PQC by 2026, prefer it by 2030, use it exclusively by 2035

**Key principle:** SP 800-175B recommends a **risk-based approach** where agencies prioritize systems based on data sensitivity and longevity.

---

## Federal Civilian Agency Compliance Timeline

| Milestone | Date | Scope | Requiring Agency |
|-----------|------|-------|-----------------|
| NSM-10 signed | May 4, 2022 | All federal agencies | White House |
| OMB M-23-02 issued | Nov 18, 2022 | Civilian agencies | OMB |
| First inventory due | May 4, 2023 | Civilian agencies | ONCD/CISA |
| FIPS 203/204/205 finalized | Aug 13, 2024 | All agencies | NIST |
| Executive Order 14306 | June 2025 | Federal procurement | White House |
| CISA product categories published | Jan 23, 2026 | Federal procurement | CISA |
| **PQC procurement mandatory (covered categories)** | **Jan 23, 2026 onwards** | **All civilian agencies** | **CISA** |
| HQC selected by NIST | Mar 11, 2025 | All agencies | NIST |
| TLS RFC expected | 2026–2027 | All organizations | IETF |
| Annual inventory renewal | May 4 (ongoing) | Civilian agencies | ONCD/CISA |

---

## Implementation Guidance for Agencies

### Priority System Categories (Risk-Based Approach)

**Tier 1 (Highest Priority – Migrate by 2027):**
- Systems protecting data with >10 year confidentiality requirements
- Systems processing sensitive personal information (PII, health data)
- Systems protecting critical infrastructure control algorithms
- High-value targets for espionage ("harvest now, decrypt later" risk)

**Tier 2 (Medium Priority – Migrate by 2030):**
- Systems with 5–10 year data sensitivity
- Administrative and financial systems
- General IT infrastructure

**Tier 3 (Lower Priority – Migrate by 2035):**
- Short-lived session data
- Non-sensitive operational systems
- Systems with shorter useful life

### Hybrid Transition Strategy

**Recommended approach for 2026–2030:**
1. Generate dual key pairs (classical + PQC)
2. Encrypt with both algorithms in sequence (classical-then-PQC or via hybrid KEM composition)
3. Receiver can decrypt with either key type, ensuring backward compatibility
4. By 2030, begin enforcing PQC-only mode
5. By 2035, classical-only systems must be decommissioned or upgraded

**Benefits:**
- Backward compatibility with legacy clients
- Provides quantum resistance immediately (via PQC)
- Maintains classical security as fallback
- Smooth transition without forcing overnight cutover

---

## CISA Resources & Support

### CISA PQC Central Hub
[https://www.cisa.gov/pqc](https://www.cisa.gov/pqc) — CISA's main PQC page with:
- Migration planning templates
- Vendor readiness checklists
- Sector-specific guidance
- Training and webinars

### CISA & NSA Joint Guidance (2024–2026)
"Moving to Post-Quantum Cryptography" — A comprehensive guide for organizations on:
- Migration roadmap development
- Hybrid cryptography deployment
- Crypto-agility architecture
- Testing and validation

### NIST PQC Project Page
[https://csrc.nist.gov/projects/post-quantum-cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography) — Official NIST resource with:
- FIPS standards documents
- Implementation guidance
- Cryptanalytic reports
- Algorithm specifications

---

## Cost & Resource Implications

**Government-wide estimate (2025–2035):** ~$7.1 billion (2024 dollars)

**Per-agency breakdown (varies):**
- Small agencies: $5–20 million
- Medium agencies: $50–200 million
- Large agencies (DoD, VA, Treasury): $500 million – $2+ billion each

**Cost drivers:**
1. Hardware upgrades (HSMs, cryptographic accelerators supporting PQC)
2. Software licensing and upgrades
3. Testing, validation, and consulting
4. Staff training and capability development
5. Certificate authority (CA) infrastructure modernization

**Budgeting challenge:** OMB expects agencies to absorb PQC costs within existing cybersecurity budgets or request supplemental appropriations through normal budget cycles.

---

## Cross-Cutting Themes: Federal Guidance vs. NSA CNSA 2.0

| Aspect | CISA / Civilian Agencies | NSA / National Security Systems |
|--------|----------------------|------|
| **Primary driver** | OMB M-23-02, Executive Order 14306 | CNSA 2.0 (NSM-10) |
| **Algorithms** | NIST FIPS 203/204/205 + HQC | CNSA 2.0 (same, but more prescriptive) |
| **Enforcement** | Procurement requirements, OMB funding conditions | Contract compliance (DFARS), audit risk |
| **Timeline** | 2035 full transition (10 years) | 2033 full transition (7 years) + earlier milestone |
| **Hybrid transition** | Strongly recommended through 2030 | Yes, but with tighter intermediate deadlines |
| **Flexibility** | Risk-based prioritization per agency | Strict by system category per NSA guidance |

---

## See Also

- **[NSA CNSA 2.0 & National Security Systems](nsa-cnsa-2.md)** — Stricter timelines for classified/sensitive systems
- **[IETF Protocol Standards](ietf-protocol-standards.md)** — RFC 9242, RFC 9370, draft TLS/SSH standards agencies must implement
- **[NIST FIPS & PQC Standardization](nist-fips-pqc.md)** — Detailed algorithm specifications

---

## References

- [OMB M-23-02 (Nov 18, 2022)](https://www.whitehouse.gov/wp-content/uploads/2022/11/M-23-02-M-Memo-on-Migrating-to-Post-Quantum-Cryptography.pdf)
- [CISA PQC Central](https://www.cisa.gov/pqc)
- [CISA Product Categories (Jan 23, 2026)](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards)
- [Executive Order 14306 (June 2025)](https://thequantuminsider.com/2026/01/27/cisa-issues-federal-buying-guidance-for-post-quantum-cryptography/)
- [NIST SP 800-175B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-175b.ipd.pdf)
- [FedRAMP Updates 2025–2026](https://www.fedramp.gov/)

