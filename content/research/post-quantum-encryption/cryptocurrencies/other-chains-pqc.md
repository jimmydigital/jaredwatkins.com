---
title: "PQC in Other Blockchain Platforms — Solana, Cardano, Algorand, QRL"
date: 2026-04-17
lastmod: 2026-04-17
draft: false
description: "Post-quantum cryptography exposure and migration status for Solana (Ed25519, testnet with Dilithium), Cardano (Project Nightstream), Algorand (Falcon live on mainnet), and QRL (purpose-built PQC blockchain)."
tags: ["post-quantum", "cryptography", "solana", "cardano", "algorand", "qrl", "cryptocurrency", "blockchain", "pqc", "fn-dsa", "ml-dsa", "slh-dsa"]
categories: ["overview"]
research_area: "post-quantum-encryption/cryptocurrencies"
source_urls:
  - "https://algorand.co/technology/post-quantum"
  - "https://blog.projecteleven.com/posts/project-eleven-to-advance-post-quantum-security-for-the-solana-network"
  - "https://www.theqrl.org/"
last_reviewed: 2026-04-17
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Overview

This entry surveys PQC exposure and migration plans for Solana, Cardano, Algorand, and QRL. Algorand is the standout: it executed the world's first post-quantum transaction on a public blockchain mainnet in November 2025, using Falcon (FN-DSA) signatures natively in the AVM. Solana and Cardano are in research/testnet phases. QRL is a purpose-built quantum-resistant chain that predates the NIST standards.

---

## Solana

### Signature Scheme and Quantum Vulnerability

Solana uses **Ed25519** for all transaction signing. Ed25519 is an elliptic curve signature scheme (Curve25519) — fully quantum-vulnerable via Shor's algorithm. Because any account that has signed a transaction has exposed its public key, the vast majority of active Solana accounts are in quantum-vulnerable state.

Solana's high-throughput architecture (50,000+ TPS target) makes the performance impact of PQC migration a particularly acute concern. PQC signatures are 20–40x larger than Ed25519 (64 bytes → ~2,500 bytes for ML-DSA-65, ~655 bytes for Falcon-512) — directly affecting bandwidth, validator storage, and turbine block propagation.

### Governance and Research Status

- **No formal SIP (Solana Improvement Proposal) assigned** as of April 2026.
- [Quantum-Resistant Research Proposal for Solana](https://forum.solana.com/t/quantum-resistant-research-proposal-for-solana/4665) — posted to Solana Developer Forums; community discussion ongoing.
- **Solana Foundation + Project Eleven Partnership** (announced December 2025): Formal quantum threat assessment conducted; testnet deployed with ML-DSA (CRYSTALS-Dilithium) signatures sustaining 3,000 TPS (matching mainnet throughput in the test environment).

### PQC Algorithms Under Consideration

- **ML-DSA (CRYSTALS-Dilithium, FIPS 204)** — Primary candidate; used in the December 2025 testnet.
- **FN-DSA (Falcon, FIPS 206 draft)** — Also under consideration; already integrated in Solana developer builds for Phantom and Ledger hardware wallet testing.
- **Crypto-agility** is Solana's stated design philosophy: building systems capable of algorithm substitution without complete protocol overhaul.

### Key Technical Challenges

**Signature size overhead:** ML-DSA-65 signatures are ~2,500 bytes vs. 64 bytes for Ed25519 — approximately 39x larger. Falcon-512 (~655 bytes) is more manageable but still roughly 10x Ed25519. This directly impacts:
- **Turbine block propagation:** Solana's peer-to-peer block propagation protocol is sensitive to message sizes; larger signatures could degrade propagation speed and increase re-transmission rates.
- **Validator storage:** Higher per-transaction data storage requirements at validator nodes.
- **Network bandwidth:** Substantially increased bandwidth requirements across the validator network.

**Firedancer:** Jump Crypto's Firedancer validator client (targeting 2026 launch) is designed with multiple signature backend support — viewed as a key technical enabler for the migration, as it allows signature scheme flexibility without forking the primary validator client.

### Timeline

- **December 2025:** Solana Foundation + Project Eleven testnet deployment with ML-DSA sustaining 3,000 TPS.
- **2026:** Firedancer validator client expected to ship with multi-signature backend support.
- **No mainnet migration date set.** Still in research and testnet phase.

### Key People

- **Solana Foundation** — Official sponsor of quantum readiness effort.
- **Project Eleven** — Security firm conducting threat assessment and testnet implementation.

<!-- TODO: Monitor Solana Developer Forums for formal SIP filing on PQC migration -->
<!-- TODO: Track Firedancer multi-signature backend implementation specifics -->
<!-- TODO: Follow up on Phantom/Ledger developer build testing results for Falcon -->

---

## Cardano

### Signature Scheme and Quantum Vulnerability

Cardano uses **Ed25519 (extended variant)** for spending keys and staking keys. The extended variant adds a 32-byte scalar but the underlying elliptic curve operations remain identical — fully quantum-vulnerable via Shor's algorithm.

Cardano's Extended UTXO (eUTXO) model provides some structural similarity to Bitcoin: unspent outputs at never-spent addresses retain hash-based protection until first spend. However, any address that has been used to sign transactions has exposed its public key.

### Project Nightstream

**Announced:** February 13, 2026 at Consensus Hong Kong by Charles Hoskinson (IOG founder).

Project Nightstream is Cardano's formal post-quantum security initiative:
- Backed by researchers linked to **Google Cloud** and **Microsoft Research**.
- Built on advanced lattice-based cryptography (specific algorithm not yet fully publicly specified; described as lattice-based).
- Includes an independent **"proof chain"** as a verification layer for historical transaction integrity.
- Google Quantum AI recognized Cardano as the "second-most quantum-ready blockchain" (after Algorand) in its 2025 assessment.

### Mithril

**Mithril** is already live on Cardano mainnet and uses PQC-signed certificate checkpoints securing historical ledger data. Viewed as a first-phase quantum protection layer for the ledger's historical record — not for individual transaction signatures.

### PQC Algorithms

- **Lattice-based (ML-DSA/Dilithium, FIPS 204)** — Hoskinson's stated preference (December 2025); aligned with NIST standards.
- **Nightstream** — Not yet fully specified publicly; described as "advanced lattice-based cryptography" optimized for AI hardware acceleration.

### Key Technical Challenges

**10x performance degradation risk:** Hoskinson explicitly warned (Decrypt interview) that a naive PQC implementation without hardware acceleration could reduce Cardano's network throughput by 10x. The Nightstream approach specifically targets avoiding this through hardware-accelerated lattice operations.

**Staged migration necessity:** Cardano's approach emphasizes resilience without sacrificing scalability; phased transition required. Hard fork necessary for full signature scheme migration.

**Plutus smart contracts:** Cardano's Plutus script language (and the upcoming Plinth/Aiken ecosystem) needs updates to handle new signature verification types and to verify PQC signatures in on-chain validation logic.

**No formal CIP assigned:** No Cardano Improvement Proposal number exists for PQC migration as of April 2026. Nightstream is an IOG initiative, not yet a governance proposal.

### Timeline

- **February 2026:** Project Nightstream announced; Google/Microsoft research collaboration confirmed.
- **2026–2027:** Historical ledger data protection via Mithril PQC-signed checkpoints (near-term deliverable).
- **No mainnet PQC transaction date announced.** Still at research and specification phase.

### Key People

- **Charles Hoskinson** (IOG founder) — Primary Cardano PQC advocate; leads strategic framing, warns of performance trade-offs.
- **IOG Research Team** — Academic research pipeline; 24 peer-reviewed papers published in 2025 across 20 research streams, with quantum security a stated priority.
- **Google Cloud / Microsoft Research** — Nightstream collaborators (identity of specific researchers not publicly disclosed).

<!-- TODO: Track Nightstream specification publication — which algorithm exactly? -->
<!-- TODO: Monitor for formal CIP filing on PQC migration -->
<!-- TODO: Follow up on proof chain architecture — which ZK proof system? -->

---

## Algorand

**Algorand is the most advanced major blockchain in PQC implementation.** It executed the world's first post-quantum transaction on a public blockchain mainnet on November 3, 2025, using Falcon (FN-DSA) signatures natively in the Algorand Virtual Machine.

### Signature Scheme and Quantum Vulnerability (Current State)

- **Regular transaction signatures:** Ed25519 — still quantum-vulnerable for ordinary transactions.
- **State Proofs:** Falcon (FN-DSA) — post-quantum secure since 2022.
- **User accounts via `falcon_verify`:** Migration path to quantum-resistant accounts now available.

### What's Live

**State Proofs (since 2022):** Compact, Falcon-signed certificates attesting to 256-block ledger segments. State Proofs are used primarily for cross-chain light client verification — allowing external blockchains and bridges to verify Algorand ledger state without trusting an intermediary. The Falcon signatures in State Proofs have been live for several years.

**`falcon_verify` AVM opcode (since September 2024, consensus upgrade v4.3.0):** Exposes Falcon signature verification as a native opcode in the Algorand Virtual Machine (AVM v12), available in both stateless and stateful smart contracts. This means developers can build accounts, applications, and wallets that use Falcon signatures for spending control rather than Ed25519.

**First PQC mainnet transaction (November 3, 2025):** Algorand executed a live Falcon-signed transaction on mainnet, representing the first post-quantum digital asset protection on any public blockchain.

**Google Quantum AI recognition:** Algorand was identified as the "most quantum-ready blockchain" in Google Quantum AI's 2025 assessment.

### PQC Algorithm: FN-DSA (Falcon, FIPS 206 draft)

- **Algorithm:** NTRU lattice-based digital signature (Falcon-512)
- **Standard:** NIST FIPS 206 — Initial Public Draft (IPD); final standard expected approximately 2027
- **Signature size:** ~666–1,280 bytes depending on parameter set
- **Public key size:** ~897–1,793 bytes
- **SumHash512:** Used in State Proof Merkle trees; provides hash-based security for the proof structure

**Standardization caveat:** FIPS 206 is still in Initial Public Draft stage as of April 2026. Algorand's Falcon implementation follows the draft standard; there is some standardization risk for early adopters if the final standard introduces changes. However, the underlying NTRU lattice mathematics are well-established.

### Outstanding Vulnerability: VRF

Algorand's **Verifiable Random Function (VRF)**, used for leader election in the Pure Proof-of-Stake consensus protocol, remains quantum-vulnerable. This is the primary remaining quantum-vulnerable component in Algorand's protocol. Active research is ongoing for a post-quantum VRF replacement, but no timeline has been publicly specified.

### Timeline

| Date | Milestone |
|------|-----------|
| 2022 | State Proofs with Falcon introduced (cross-chain verification) |
| September 2024 | `falcon_verify` AVM opcode deployed (v4.3.0) |
| November 3, 2025 | First post-quantum transaction on any public blockchain mainnet |
| 2026 (ongoing) | R&D on VRF replacement and broader PQC integration |

<!-- TODO: Track VRF replacement research — any candidate post-quantum VRF published? -->
<!-- TODO: Monitor for adoption metrics on falcon_verify usage in deployed contracts -->
<!-- TODO: Track FIPS 206 final standard timeline (expected ~2027) and any implications for Algorand's implementation -->

---

## QRL (Quantum Resistant Ledger)

QRL is unique: it was purpose-built for quantum resistance from its 2018 mainnet launch. It uses no elliptic curve cryptography anywhere in the protocol.

### QRL v1 (Current Mainnet)

- **Signature scheme:** XMSS (eXtended Merkle Signature Scheme) — NIST-recognized stateful hash-based signature scheme (NIST SP 800-208).
- **Consensus:** Proof-of-Work.
- **Status:** First blockchain to launch with a NIST-approved post-quantum signature scheme.

**XMSS limitations:** XMSS requires tracking One-Time Signature (OTS) indices — each signing key can only be used a fixed number of times. This creates operational complexity: users must not reuse OTS keys; exchanges and staking pools must maintain key state; smart contracts have limited compatibility. These are the primary motivations for the migration to stateless PQC schemes in QRL v2.

### Project Zond (QRL 2.0)

**Testnet V2 launched: March 31, 2026.**

QRL 2.0 is a complete protocol overhaul targeting stateless PQC signatures, Proof-of-Stake consensus, and EVM compatibility:

- **Signature schemes:** ML-DSA-87 (Dilithium, FIPS 204) as primary; SLH-DSA (SPHINCS+, FIPS 205) for additional resilience. Both are stateless — eliminating XMSS's key-state management complexity.
- **Smart contracts:** **Hyperion** (Solidity-derived language) + **QRVM** (Quantum Resistant Virtual Machine, EVM fork). Valid Solidity code is largely valid Hyperion.
- **Consensus:** Proof-of-Stake replacing Proof-of-Work.
- **Roadmap:** Security audits following testnet; mainnet launch targeted in 2026.

### PQC Algorithm Details

| Algorithm | Type | Standard | Role in QRL 2.0 |
|---|---|---|---|
| ML-DSA-87 (Dilithium) | Lattice | FIPS 204 | Primary transaction signing |
| SLH-DSA (SPHINCS+) | Hash-based, stateless | FIPS 205 | Backup/resilience option |
| XMSS | Hash-based, stateful | NIST SP 800-208 | QRL v1 only |

**SLH-DSA note:** SPHINCS+ signatures are large (8–41 KB depending on parameters), but for QRL — a dedicated PQC chain where security is the primary value proposition — the overhead is acceptable. QRL v2 uses the faster parameter sets.

### Key Technical Challenges and Market Position

**Adoption is the primary challenge.** QRL is a correctly-designed quantum-resistant chain that predates the NIST standards and has now upgraded to use them. Its challenge is not technical — it is achieving network effects against established chains with vastly larger ecosystems. The quantum-resistant positioning must become a market-relevant differentiator before a CRQC arrives.

**EVM compatibility (Zond):** QRL v2's EVM-compatible smart contract platform aims to lower the barrier for Solidity developers to deploy on QRL. The Hyperion language and QRVM architecture provide the technical bridge.

### Timeline

| Date | Milestone |
|------|-----------|
| 2018 | QRL mainnet v1 launch (XMSS, PoW) — first NIST-approved PQC blockchain |
| 2022 | NIST recommends XMSS and LMS as post-quantum standards |
| 2024–2025 | Zond beta testnet |
| March 31, 2026 | Testnet V2 launch (EVM + PQC + PoS) |
| 2026 (target) | Security audits → mainnet launch |

<!-- TODO: Track QRL Zond audit completion and mainnet launch -->
<!-- TODO: Monitor Hyperion smart contract ecosystem growth post-mainnet -->

---

## Cross-Chain Comparison Summary

| Chain | Current Sig Scheme | PQC Status | Primary Candidate | Hard Fork Required | Notable |
|-------|---|---|---|---|---|
| Bitcoin | ECDSA secp256k1 / Schnorr | BIP-360 testnet; BIP-361 draft | FN-DSA (Falcon) | Phase B/C of BIP-361 | ~28–35% supply in long-exposure state |
| Ethereum | ECDSA secp256k1 (exec) / BLS12-381 (consensus) | Devnets active; EIP-8141 proposed | ML-DSA + leanSig | Multiple hard forks (~7) | Most organized response; 2029 target |
| Solana | Ed25519 | Testnet (Dec 2025) | ML-DSA | Protocol upgrade | 3,000 TPS sustained in testnet |
| Cardano | Ed25519 extended | Project Nightstream announced | ML-DSA (lattice) | Hard fork | Google/Microsoft collaboration |
| Algorand | Ed25519 (regular) / Falcon (State Proofs, user accounts) | **Falcon live on mainnet** | FN-DSA (Falcon) | N/A (opcode live) | Most advanced; VRF still vulnerable |
| QRL | XMSS (v1) / ML-DSA (v2) | **Fully PQC since 2018**; v2 testnet March 2026 | ML-DSA-87, SLH-DSA | N/A (purpose-built) | Purpose-built; adoption is the challenge |

---

## Exchange and Wallet Readiness

### Coinbase

Established an **Independent Advisory Board on Quantum Computing and Blockchain** in January 2026.

**Members:** Prof. Scott Aaronson (UT Austin), Prof. Dan Boneh (Stanford), Justin Drake (Ethereum Foundation), Prof. Sreeram Kannan (EigenLayer), Prof. Yehuda Lindell (Coinbase Head of Cryptography), Prof. Dahlia Malkhi (UCSB).

Position paper in development; near-term product updates and long-term cryptographic research roadmap planned. [Coinbase blog announcement](https://www.coinbase.com/blog/coinbase-establishes-independent-advisory-board-on-quantum-computing-and-blockchain).

**Binance, Kraken:** No public PQC readiness statements as of April 2026.

### Hardware Wallets

**Trezor Safe 7** — Released 2025; described as the "first quantum-ready hardware wallet." COO Danny Sanders: device is "technically capable of receiving post-quantum updates when the time comes." TROPIC01 chip and firmware are open-source/independently verifiable. Developer builds with dual keypairs (Ed25519 + Dilithium) available in testing.

**Ledger:** No quantum-ready hardware announced as of April 2026. Ledger Donjon (internal security research) published detailed PQC hardware analysis in early 2026 concluding that ML-DSA, Falcon, and SLH-DSA require significantly more RAM and produce larger signatures — "difficult" on constrained secure elements. No public PQC migration path announced for Ledger's proprietary secure elements (ST33/ST33G1M2).

---

## Key Academic and Regulatory Context

- **Google Quantum AI (March 31, 2026):** Reduced CRQC resource estimates; under optimistic error rate assumptions, <500,000 physical qubits might suffice to break ECDLP-256. Set 2029 as a migration target. [Research blog](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/).
- **Federal Reserve Staff Paper 2025-093:** "Harvest Now, Decrypt Later: Examining Post-Quantum Cryptography and the Data Privacy Risks for Distributed Ledger Networks." Warns that blockchain's permanent public transaction history makes all historical data permanently harvestable. [federalreserve.gov](https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm).
- **Citi Institute (January 2026):** "The Trillion-Dollar Security Race Is On: Quantum Threat" — estimates ~$648B+ in digital assets at quantum risk. [PDF](https://www.citigroup.com/rcs/citigpa/storage/public/Citi_Institute_Quantum_Threat.pdf).

---

## Sources

- [Algorand: Post-Quantum Technology](https://algorand.co/technology/post-quantum)
- [Algorand: Technical brief — Falcon signatures](https://algorand.co/blog/technical-brief-quantum-resistant-transactions-on-algorand-with-falcon-signatures)
- [Algorand: 2025 Roadmap Progress](https://algorand.co/blog/2025-on-algorand-roadmap-progress)
- [Hacken: FN-DSA/Falcon for Web3](https://hacken.io/discover/falcon-post-quantum-signature-algorithm/)
- [Project Eleven + Solana Foundation partnership (Tekedia)](https://www.tekedia.com/solana-foundation-partners-with-project-eleven-on-quantum-resistance/)
- [Project Eleven: Post-quantum security for Solana](https://blog.projecteleven.com/posts/project-eleven-to-advance-post-quantum-security-for-the-solana-network)
- [CoinDesk: Solana quantum trade-off — security vs. speed (April 4, 2026)](https://www.coindesk.com/tech/2026/04/04/solana-s-quantum-threat-readiness-reveals-harsh-tradeoff-security-vs-speed)
- [Helius: What Solana needs to become quantum-ready](https://www.helius.dev/blog/solana-post-quantum-cryptography)
- [Sanctum: Solana quantum computing guide 2026](https://sanctum.so/blog/quantum-computing-solana-2026-guide)
- [Cardano: Project Nightstream announcement (CoinAlertNews, February 2026)](https://coinalertnews.com/news/2026/02/14/cardano-google-microsoft-post-quantum-security)
- [Hoskinson: Bitcoin's quantum fix is a hard fork (CoinDesk, April 16, 2026)](https://www.coindesk.com/tech/2026/04/16/cardano-s-hoskinson-says-bitcoin-s-quantum-fix-is-a-hard-fork-that-can-t-save-satoshi-s-coins)
- [Hoskinson: Post-quantum requires trade-offs (Decrypt)](https://decrypt.co/353161/cardano-hoskinson-warns-crypto-becoming-post-quantum-require-trade-offs)
- [QRL Official Site](https://www.theqrl.org/)
- [QRL Roadmap](https://www.theqrl.org/roadmap/)
- [QRL Testnet V2 Launch (March 31, 2026)](https://www.theqrl.org/press/qrl-launches-testnet-v2-for-its-postquantum-evmfriendly-blockchain/)
- [Coinbase quantum advisory board (Quantum Zeitgeist)](https://quantumzeitgeist.com/coinbase-quantum-computing-quantum-advisory-board/)
- [Trezor Safe 7 / Ledger comparison 2026 (CryptoValleyJournal)](https://cryptovalleyjournal.com/focus/background/hardware-wallet-comparison-2026-ledger-vs-trezor-new-models-new-risks/)
- [Ledger Donjon: Quantum computing threat to blockchain](https://www.ledger.com/blog-quantum-computing-threat-to-blockchain)
- [Google Quantum AI: Safeguarding cryptocurrency (March 31, 2026)](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/)
- [Federal Reserve Staff Paper 2025-093](https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm)
- [Citi Institute: Trillion-Dollar Security Race (January 2026)](https://www.citigroup.com/rcs/citigpa/storage/public/Citi_Institute_Quantum_Threat.pdf)
