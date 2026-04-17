---
title: "Ethereum — Post-Quantum Cryptography Exposure and Migration"
date: 2026-04-17
lastmod: 2026-04-17
draft: false
description: "Analysis of Ethereum's quantum vulnerability across execution and consensus layers, EIP migration proposals, leanSig/leanXMSS attestation research, and Vitalik Buterin's 2026–2029 Strawmap roadmap."
tags: ["post-quantum", "cryptography", "ethereum", "cryptocurrency", "blockchain", "pqc", "ml-dsa", "fn-dsa", "slh-dsa", "hndl"]
categories: ["company"]
research_area: "post-quantum-encryption/cryptocurrencies"
source_urls:
  - "https://pq.ethereum.org/"
  - "https://ethereum.org/roadmap/future-proofing/"
  - "https://blog.projecteleven.com/posts/quantum-attack-vectors-in-ethereum"
last_reviewed: 2026-04-17
stale_after_days: 90
---

## Summary

Ethereum's quantum exposure is more uniform than Bitcoin's: because Ethereum uses an account model, **any account that has ever sent a transaction has already revealed its ECDSA public key**. Unlike Bitcoin's UTXO model where unspent, never-spent addresses retain some hash-based protection, a large fraction of actively-used Ethereum accounts are immediately quantum-vulnerable. The consensus layer (validators using BLS12-381 signatures) and the data availability layer (KZG commitments in EIP-4844) are also quantum-vulnerable.

The Ethereum Foundation response has been the most organized of any major blockchain: a dedicated Post-Quantum Security team was established in January 2026, [pq.ethereum.org](https://pq.ethereum.org/) launched in March 2026, and Vitalik Buterin's "Strawmap" (February 2026) targets full L1 quantum upgrade by approximately 2029 across a series of ~7 hard forks.

## Quantum Vulnerability — Exposure by Layer

### Execution Layer (User Accounts / EOAs)

Ethereum EOAs (Externally Owned Accounts) use **ECDSA secp256k1** for transaction signing — fully quantum-vulnerable via Shor's algorithm. Any account that has signed and broadcast a transaction has exposed its public key in the transaction signature. In Ethereum's account model, this includes the vast majority of active wallets.

**Estimated exposure:** Project Eleven analysis found the 1,000 highest-value Ethereum accounts held approximately 20.5M ETH and could theoretically be compromised in under 9 days under Google's March 2026 model assumptions. A CCN analysis estimated approximately 90M ETH across all address types at some level of quantum exposure.

**Contrast with Bitcoin:** Bitcoin's UTXO model provides some address-level protection for never-spent outputs. Ethereum's account model does not — once a wallet sends any transaction, it is permanently quantum-vulnerable until migrated to a PQC account type.

### Consensus Layer (Validators)

Ethereum validators use **BLS12-381** (BLS signatures) for attestations and block proposals. BLS12-381 is based on elliptic curve pairings over the BLS12-381 curve — quantum-vulnerable via Shor's algorithm applied to the elliptic curve discrete logarithm problem.

**Scale challenge:** Over 500,000 active validators each produce BLS signatures every epoch (~6.4 minutes). BLS has highly efficient signature aggregation — a core reason it was chosen. No current PQC scheme aggregates as efficiently as BLS, making consensus-layer PQC a harder engineering problem than execution-layer migration.

### Data Availability Layer

**KZG commitments** (used in EIP-4844 blob transactions) rely on elliptic curve pairings (BLS12-381) — quantum-vulnerable. Migrating from KZG to STARK-based polynomial commitments is a major undertaking affecting the entire rollup and data availability ecosystem.

### ZK Proof Systems

**SNARKs** (used in many ZK-rollup provers) rely on elliptic curve cryptography — quantum-vulnerable. **STARKs** (hash-based, used by StarkWare and others) are already quantum-resistant. The Ethereum roadmap relies heavily on STARK-based aggregation for the quantum transition.

---

## Governance Proposals and EIPs

### EIP-7701 — Native Account Abstraction (EOF-based)

Foundational EIP enabling smart-contract-based validation logic, which is the "EVM migration path" for moving accounts off ECDSA without a protocol-wide signature scheme cutover. Considered for the Glamsterdam fork (H1 2026).

### EIP-8141 — Frame Transactions (Native Account Abstraction)

- **Authors:** Vitalik Buterin et al.
- **Status:** Considered for Inclusion (CFI) for Hegota fork (H2 2026); client teams from Nethermind and Besu flagged complexity concerns; risk of delaying the entire Hegota upgrade
- **Vitalik's statement:** "Will ship within a year" (early 2026)

**Design:** Introduces "frames" — a programmable sequence of validation and execution steps that fully decouples a transaction's signature scheme from the protocol. Under EIP-8141, any wallet can adopt any PQC signature scheme without requiring a network-wide cutover. The signing algorithm becomes a wallet implementation detail rather than a protocol constant.

**Significance for PQC:** EIP-8141 is the primary mechanism enabling the execution layer quantum migration. It allows sophisticated users and wallets to migrate to PQC accounts immediately upon availability, without waiting for a mandatory network-wide switch.

**Gas cost problem:** ECDSA verification costs ~3,000 gas. PQC signature verification (ML-DSA, Falcon) may cost ~200,000 gas or more. EIP-8141's design relies on recursive STARK aggregation to compress many PQC signatures into a single proof, amortizing verification costs across many transactions.

### Emergency Quantum Path in Glamsterdam

Vitalik's Glamsterdam design includes a contingency "Quantum Emergency" path: if a CRQC threat materializes imminently, users can migrate to lattice-based addresses via ZK proofs of their current private key — converting classical accounts to PQC-secured accounts without revealing the classical private key on-chain.

---

## PQC Algorithm Candidates

### Consensus Layer: leanSig / leanXMSS

The most novel element of Ethereum's PQC roadmap is the **leanSig** scheme, designed specifically for the validator attestation aggregation problem:

- **Type:** Custom XMSS-style scheme (stateful hash-based), combined with STARK-based aggregation ("leanMultisig" / zkVM)
- **Innovation:** STARK-based recursive proofs achieve approximately 250x compression of attestation data — critical for managing 500,000+ validator signatures per epoch
- **Implementation:** Open-source; leanSpec (Python), leanSig (Rust)
- **Status:** Research prototype; active interoperability devnets underway

### Execution Layer: NIST-Standard PQC

For user transaction signatures via EIP-8141, all three NIST standards are under consideration:

- **ML-DSA (Dilithium, FIPS 204)** — Likely primary candidate for execution layer precompiles; simpler implementation than Falcon
- **FN-DSA (Falcon, FIPS 206)** — Smaller signatures; more complex implementation
- **SLH-DSA (SPHINCS+, FIPS 205)** — Hash-based; conservative security assumptions; large signatures; potential role as high-assurance fallback

---

## The Strawmap and Ethereum's PQC Roadmap

Vitalik Buterin's "Strawmap" (February 2026) is a 4-year Ethereum development plan targeting approximately 7 hard forks through ~2029, with full L1 post-quantum as a primary goal.

**Ethereum Foundation Post-Quantum roadmap milestones:**

| Milestone | Focus |
|-----------|-------|
| **I\*** | Post-quantum key registry (consensus layer) |
| **J\*** | Post-quantum signature precompiles (execution layer) |
| **L\*** | Post-quantum attestations with leanVM aggregation (consensus + data) |
| **M\*** | Full post-quantum aggregation + blob handling (execution + data) |

**Timeline:**

- **January 2026:** Ethereum Foundation establishes dedicated Post-Quantum Security team
- **March 2026:** [pq.ethereum.org](https://pq.ethereum.org/) launched; 10+ client teams running interoperability devnets (4 devnets shipped by March 2026)
- **H1 2026:** Glamsterdam fork — quantum emergency contingency path included
- **H2 2026:** Hegota fork — EIP-8141 frame transactions targeted (CFI status); FOCIL confirmed as headliner
- **~2029:** Full L1 post-quantum consensus targeted

**Vitalik's stated threat estimate:** "~20% chance" a CRQC arrives before 2030.

---

## Key Technical Challenges

**Validator signature aggregation:** BLS aggregation is uniquely efficient — aggregating N validator signatures produces one compact combined signature. No PQC scheme achieves comparable aggregation natively. leanSig's STARK-based compression is the proposed solution but is more complex than BLS aggregation.

**EVM gas costs:** PQC signature verification is 20–100x more expensive than ECDSA. New precompiles and gas repricing are required. EIP-8141's recursive STARK aggregation approach aims to amortize costs.

**KZG replacement:** EIP-4844's blob data architecture uses KZG polynomial commitments (quantum-vulnerable). Migrating to STARK-based polynomial commitments affects the entire rollup ecosystem.

**Layer 2 implications:** ZK-rollups using SNARK-based provers inherit quantum vulnerability from the underlying proof system. ZK-rollup teams using SNARK provers (Polygon zkEVM, zkSync Era) will need to migrate to STARK-based provers. STARK-based rollups (StarkNet) are already quantum-resistant at the proof layer.

**Scale:** Ethereum's ecosystem is substantially larger than Bitcoin's in terms of active applications, rollups, and developer infrastructure. A signature scheme migration has cascading effects across the entire DeFi, NFT, and L2 ecosystem.

---

## Notable Developments

- **2026-01:** Ethereum Foundation establishes Post-Quantum Security team
- **2026-02-26:** Vitalik Buterin publishes Strawmap with full L1 quantum upgrade targeted ~2029 ([CoinDesk coverage](https://www.coindesk.com/tech/2026/02/26/vitalik-buterin-unveils-ethereum-roadmap-to-counter-quantum-computing-threat))
- **2026-03-25:** [pq.ethereum.org](https://pq.ethereum.org/) launched; 4 interoperability devnets active ([CoinDesk](https://www.coindesk.com/tech/2026/03/25/ethereum-foundation-prepares-for-quantum-threat-with-new-cryptography-roadmap))
- **2026-03-31:** Google Quantum AI paper reduces CRQC resource estimates; sets 2029 migration target — accelerates Ethereum urgency
- **2026-04:** EIP-8141 debated for Hegota fork inclusion; complexity concerns raised by Nethermind and Besu teams

<!-- TODO: Track EIP-8141 decision — included or deferred from Hegota? -->
<!-- TODO: Track leanSig devnet results; look for published benchmarks on STARK compression ratios vs. BLS -->
<!-- TODO: Monitor specific PQC precompile proposals for execution layer (ML-DSA? Falcon?) -->

---

## Key People

- **Vitalik Buterin** — Primary PQC roadmap architect; authored Strawmap; backs EIP-8141; stated ~20% pre-2030 CRQC threat probability
- **Justin Drake** (Ethereum Foundation researcher) — Consensus-layer PQC lead; called recent quantum research "a momentous day"; advisory board member at Coinbase
- **Ethereum Foundation Post-Quantum Team** — Established January 2026; coordinates 10+ client teams on weekly PQC interoperability devnets

---

## Claim Verification

### Claim: ~90M ETH is at some level of quantum exposure

**Status:** Partially verified

**Supporting sources:**
- CCN analysis of Ethereum addresses: approximately 90M ETH across all address types at some quantum exposure level
- Project Eleven: 1,000 highest-value accounts hold ~20.5M ETH and could theoretically be targeted within 9 days under Google's 2026 paper assumptions

**Refuting / questioning sources:**
- "Some level of quantum exposure" conflates immediate vulnerability (accounts that have sent transactions, pubkey exposed) with conditional vulnerability (accounts that have not yet sent transactions, pubkey hashed)
- The actual immediately vulnerable pool is accounts that have signed at least one transaction — a large fraction of active accounts but not all ETH holders

**Summary:** ~90M ETH represents a directionally credible upper bound on quantum-exposed holdings; the immediately-attackable subset is accounts that have revealed public keys via transaction signatures.

---

### Claim: Full L1 quantum upgrade targeted for ~2029

**Status:** Verified (as a target; not a commitment)

**Supporting sources:**
- [pq.ethereum.org](https://pq.ethereum.org/) roadmap milestones
- Vitalik's Strawmap (February 2026) — ~7 hard forks targeting 2029 completion
- [Ethereum.org future-proofing roadmap](https://ethereum.org/roadmap/future-proofing/)

**Refuting / questioning sources:**
- Ethereum has historically slipped major upgrades; The Merge took years longer than initial estimates
- EIP-8141 is already facing complexity concerns that could delay the Hegota fork
- 2029 is an aspiration, not a shipped schedule

**Summary:** 2029 is the Ethereum Foundation's published target; historical precedent suggests it may slip.

---

## Sources

- [pq.ethereum.org — Post-Quantum Ethereum Hub](https://pq.ethereum.org/)
- [Ethereum.org: Future-Proofing Roadmap](https://ethereum.org/roadmap/future-proofing/)
- [CoinDesk: Vitalik Buterin unveils Ethereum quantum roadmap (February 26, 2026)](https://www.coindesk.com/tech/2026/02/26/vitalik-buterin-unveils-ethereum-roadmap-to-counter-quantum-computing-threat)
- [CoinDesk: Ethereum Foundation prepares for quantum threat (March 25, 2026)](https://www.coindesk.com/tech/2026/03/25/ethereum-foundation-prepares-for-quantum-threat-with-new-cryptography-roadmap)
- [KuCoin: Vitalik outlines Ethereum quantum resistance strategy 2026–2030](https://www.kucoin.com/news/flash/vitalik-buterin-outlines-ethereum-s-quantum-resistance-strategy-for-2026-2030)
- [BTQ: Ethereum's roadmap for post-quantum cryptography](https://www.btq.com/blog/ethereums-roadmap-post-quantum-cryptography)
- [Cryptonews: Ethereum Strawmap — 7 hard forks](https://cryptonews.com/news/ethereum-strawmap-quantum-hard-forks/)
- [Ethereum Foundation sets 2029 target (CoinPaprika)](https://coinpaprika.com/news/ethereum-foundation-sets-2029-target-l1-quantum-upgrade/)
- [EIP-8141 and native account abstraction (CCN)](https://www.ccn.com/education/crypto/ethereum-eip8141-native-account-abstraction-frame-transactions/)
- [ethresear.ch: Road to PQ Ethereum via account abstraction](https://ethresear.ch/t/the-road-to-post-quantum-ethereum-transaction-is-paved-with-account-abstraction-aa/21783)
- [Project Eleven: Quantum attack vectors in Ethereum](https://blog.projecteleven.com/posts/quantum-attack-vectors-in-ethereum)
- [CCN: 6M BTC, 90M ETH exposed to quantum threats](https://www.ccn.com/news/crypto/crypto-token-quantum-risk-btc-eth-exposed-threat/)
- [Google Quantum AI: Safeguarding cryptocurrency (March 31, 2026)](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/)
- [Federal Reserve Staff Paper 2025-093: HNDL and DLT Networks](https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm)
- [Citi Institute: Trillion-Dollar Security Race (January 2026)](https://www.citigroup.com/rcs/citigpa/storage/public/Citi_Institute_Quantum_Threat.pdf)
