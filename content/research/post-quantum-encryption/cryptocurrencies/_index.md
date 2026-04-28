---
title: "PQC in Cryptocurrencies"
date: 2026-04-15
lastmod: 2026-04-17
draft: false
description: "Post-quantum cryptography exposure analysis and migration plans for major cryptocurrency and blockchain platforms — Phase 2 research, now active."
tags: ["post-quantum", "cryptography", "cryptocurrency", "bitcoin", "ethereum", "blockchain", "pqc"]
categories: ["overview"]
research_area: "post-quantum-encryption/cryptocurrencies"
last_reviewed: 2026-04-17
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.7
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


{{< steering >}}

## Cryptocurrencies PQC Section — Steering Instructions

This section documents the post-quantum cryptography exposure of major cryptocurrency and blockchain networks, the migration mechanisms proposed or under development, and the governance challenges involved in transitioning decentralized protocols to quantum-resistant cryptography.

**Phase 2 is now active.** Initial entries exist for Bitcoin, Ethereum, and a multi-platform survey covering Solana, Cardano, Algorand, and QRL.

---

### Why This Section Is Different

Cryptocurrency PQC migration is fundamentally more complex than enterprise networking vendor upgrades for several reasons:

1. **Decentralized governance:** There is no single vendor who can ship a firmware update. Bitcoin, Ethereum, and similar networks require broad ecosystem consensus — miners, validators, node operators, wallet developers, exchanges — to adopt protocol changes. The social coordination cost is as significant as the technical cost.

2. **Signature scheme exposure:** Most proof-of-work and proof-of-stake networks use ECDSA (secp256k1 or P-256) or EdDSA (Ed25519) for transaction signing. An operational CRQC running Shor's algorithm could derive private keys from public keys that have been exposed on-chain. Bitcoin addresses that have never spent UTXOs expose only a hash of the public key — which requires a preimage attack and is more resistant. But any reused address, or any UTXO whose public key is exposed in the scriptPubKey (including all P2PK outputs and any spent P2PKH address), is directly vulnerable.

3. **Long migration horizon:** Migrating a cryptocurrency's signature scheme requires a hard fork (or a carefully staged soft fork). Historical precedent (SegWit, Taproot) suggests 2–5 year timelines from proposal to majority adoption for major Bitcoin changes. Ethereum's account model introduces different migration dynamics.

4. **Key burning risk:** If a CRQC becomes operational before a cryptocurrency completes migration, quantum-vulnerable holdings may be at risk of theft. The mitigation is proactive migration to quantum-resistant addresses — but this requires user action, which is historically poor for security upgrades.

---

### Research Questions — Ongoing

For each platform, ongoing research should address:

1. **Exposure analysis updates:** What fraction of total value is in quantum-vulnerable state? Track this as address adoption patterns change.
2. **Governance proposal status:** BIP/EIP/SIP/CIP proposal numbers, activation status, miner/validator signaling.
3. **Algorithm selection finalization:** Which specific PQC signature scheme is formally adopted? Track changes as FIPS 206 (Falcon) finalizes and HQC standardization progresses.
4. **Timeline reassessment:** Has Google's March 2026 paper changed developer urgency and timelines?
5. **Layer 2 implications:** Lightning Network PQC, Ethereum rollup prover migration.
6. **Wallet and exchange readiness:** Trezor, Ledger, Coinbase, Binance developments.

---

### Editorial Notes

- Apply the same skepticism standard as the main PQC section: decompose "quantum-safe" or "quantum-resistant" claims into specific algorithm names, implementation status, and governance stage.
- Distinguish between academic proposals (BIP/EIP drafts), protocol-level activation, and actual ecosystem adoption. A BIP that has no miner signaling is different from a BIP that has achieved lock-in.
- Document the major voices in the debate — cryptographers, core developers, large holders — and their stated positions. This is a governance question as much as a technical one.
- The timeline for a CRQC is the key unknown. Be transparent about the range of expert estimates and do not anchor to a single date. Google's March 2026 paper is the most recent credible reduction in resource estimates.

---

{{< /steering >}}

## Overview

**Phase 2 — Now Active**

This section documents the post-quantum cryptography exposure of major cryptocurrency and blockchain networks, the migration mechanisms proposed or under development, and the governance challenges involved in transitioning decentralized protocols to quantum-resistant cryptography.

Unlike enterprise networking, where a vendor can ship a firmware update, cryptocurrency PQC migration requires decentralized consensus across miners, validators, developers, exchanges, and end users. The technical challenge is significant; the social coordination challenge may be greater.

The urgency accelerated in late 2025 and early 2026. Google Quantum AI published a paper on March 31, 2026 reducing CRQC resource estimates — under optimistic error rate assumptions, fewer than 500,000 physical qubits might suffice to break ECDLP-256, with a 2029 migration target. The Federal Reserve published a staff paper analyzing harvest-now-decrypt-later risks for distributed ledgers. Citi Institute estimated ~$648B in digital assets at quantum risk.

## Key Context: Google's March 2026 Paper

Google Quantum AI's March 31, 2026 paper ("Safeguarding Cryptocurrency by Disclosing Quantum Vulnerabilities Responsibly") materially reduced estimated resource requirements for a cryptographically relevant quantum computer:

- Fewer than **500,000 physical qubits** under optimistic error rate assumptions (previous estimates were in the millions)
- Under **1,200 logical qubits** + 90M Toffoli gates theoretically sufficient for ECDLP-256
- Sets **2029 as a migration target** — consistent with NSA CNSA 2.0 timelines

This has accelerated urgency across the cryptocurrency ecosystem, with Ethereum, Bitcoin, Solana, and Cardano all intensifying PQC research and roadmap activity in Q1 2026.

## Platform Status Summary

| Platform | Signature Scheme | PQC Status | Primary Candidate | Hard Fork | Notable |
|---|---|---|---|---|---|
| Bitcoin | ECDSA secp256k1 / Schnorr | BIP-360 testnet (Mar 2026); BIP-361 draft | FN-DSA (Falcon) | Phases B/C of BIP-361 | ~28–35% supply long-exposure vulnerable |
| Ethereum | ECDSA secp256k1 / BLS12-381 | Devnets active; EIP-8141 proposed; 2029 target | ML-DSA + leanSig | ~7 hard forks | Most organized response; dedicated PQ team |
| Solana | Ed25519 | Testnet (Dec 2025), 3,000 TPS Dilithium | ML-DSA | Protocol upgrade | Firedancer multi-sig backend key enabler |
| Cardano | Ed25519 extended | Project Nightstream (Feb 2026) | ML-DSA (lattice) | Hard fork | Google/Microsoft collaboration |
| Algorand | Ed25519 / Falcon (State Proofs + accounts) | **Falcon live on mainnet (Nov 2025)** | FN-DSA (Falcon) | N/A — live | Most advanced; VRF still vulnerable |
| QRL | XMSS → ML-DSA/SLH-DSA | **Fully PQC**; v2 testnet (Mar 2026) | ML-DSA-87 | N/A — purpose-built | First PQC blockchain (2018) |

## Entries

- [Bitcoin PQC]({{< relref "bitcoin-pqc.md" >}}) — UTXO exposure analysis, BIP-360/BIP-361 proposals, algorithm candidates, Lopp vs. Back governance debate
- [Ethereum PQC]({{< relref "ethereum-pqc.md" >}}) — Account model exposure, EIP-8141 frame transactions, leanSig/leanXMSS, Strawmap 2029 roadmap
- [Other Chains]({{< relref "other-chains-pqc.md" >}}) — Solana, Cardano (Nightstream), Algorand (Falcon live), QRL (purpose-built PQC), exchange and wallet readiness
