---
title: "Bitcoin — Post-Quantum Cryptography Exposure and Migration"
date: 2026-04-17
lastmod: 2026-04-17
draft: false
description: "Analysis of Bitcoin's quantum vulnerability exposure by address type, BIP-360 and BIP-361 governance proposals, PQC algorithm candidates, and timeline estimates for migration."
tags: ["post-quantum", "cryptography", "bitcoin", "cryptocurrency", "blockchain", "pqc", "ml-dsa", "fn-dsa", "slh-dsa", "hndl"]
categories: ["company"]
research_area: "post-quantum-encryption/cryptocurrencies"
source_urls:
  - "https://bitcoinops.org/en/topics/quantum-resistance/"
  - "https://bip360.org/bip360.html"
  - "https://blog.projecteleven.com/posts/quantum-vulnerability-of-bitcoin-addresses"
  - "https://www.projecteleven.com/bitcoin-risq-list"
last_reviewed: 2026-04-17
stale_after_days: 90
---

## Summary

Bitcoin uses ECDSA secp256k1 (legacy addresses) and Schnorr/BIP-340 (Taproot) for transaction signing — both fully quantum-vulnerable via Shor's algorithm. The mining/consensus layer (SHA-256 proof-of-work) has only a quadratic quantum speedup via Grover's algorithm, a far lesser and more distant concern. The primary threat is to transaction signing and — critically — to the large fraction of existing UTXOs whose public keys are already visible on-chain.

As of April 2026, Bitcoin has two significant governance proposals in motion: **BIP-360** (a soft-fork infrastructure change to enable quantum-resistant output types) and **BIP-361** (a controversial phased sunset of legacy signature types). A working testnet exists, but no mainnet timeline has been set, and core developer estimates put the full migration timeline at 5–10 years from activation.

## Quantum Vulnerability — Exposure by Address Type

Bitcoin's UTXO model creates heterogeneous quantum exposure. Vulnerability is determined by whether the public key is visible on-chain:

### Long-Exposure (public key already on-chain — immediately attackable by a CRQC)

| Address Type | Format | Vulnerability Trigger | Estimated BTC at Risk |
|---|---|---|---|
| **P2PK** | `OP_PUSHDATA <pubkey> OP_CHECKSIG` | Immediate on receipt — pubkey in locking script | ~1.7M BTC (largely Satoshi-era, likely lost) |
| **P2PKH (reused)** | `1...` addresses | Pubkey exposed on any spend; reused addresses have exposed pubkeys | Part of ~5.2M BTC pool |
| **P2WPKH (reused)** | `bc1q...` addresses | Same as P2PKH — pubkey exposed on spend | Part of ~5.2M BTC pool |
| **P2TR (Taproot)** | `bc1p...` addresses | Immediate on receipt — x-only pubkey is encoded directly in address; **no hash protection** | Part of ~5.2M BTC pool (~5% of UTXOs) |

### Short-Exposure (pubkey hidden until spend — attacker must act within ~10 minutes)

All Bitcoin address types are vulnerable during the mempool broadcast window before block confirmation. An attacker with a CRQC fast enough to derive a private key in <10 minutes could steal any in-flight transaction. This is currently considered a more distant threat than the long-exposure problem.

### Aggregate Exposure Estimates

- **~6.2–6.9M BTC (28–32% of total supply)** sit in long-exposure quantum-vulnerable addresses where the public key is already visible on-chain, per Project Eleven analysis.
- A March 2026 Ark Invest / Unchained Capital report placed ~35% of outstanding supply in theoretically vulnerable types.
- Citi Institute (January 2026) estimated ~$648B+ in digital assets at quantum risk across all chains.
- CoinShares research ("Quantum vulnerability in Bitcoin: A Manageable Risk") offers a more conservative view, noting most vulnerable P2PK coins are likely lost/inactive, but acknowledges the structural exposure.

**Project Eleven** maintains the [Bitcoin Risq List](https://www.projecteleven.com/bitcoin-risq-list), an open-source, weekly-updated database tracking all quantum-vulnerable addresses by type and balance.

### Taproot's Double-Edged Nature

Taproot (BIP-340/341/342, activated 2021) offers privacy benefits by making all spends look alike at the script level. However, it encodes a 32-byte x-only public key directly into the output address — providing **no hash protection**. Any coins sent to a P2TR address are immediately quantum-vulnerable on receipt, unlike P2PKH/P2WPKH addresses that are protected until first spend. This makes the urgency of quantum migration more acute for Taproot users than for holders of legacy address types.

---

## Governance Proposals

### BIP-360 — Pay-to-Merkle-Root (P2MR)

- **Authors:** Hunter Beast (lead), Ethan Heilman, Isabel Foxen Duke
- **Assigned:** December 18, 2024; last updated February 2026
- **Status:** Draft (soft fork)
- **GitHub:** [bitcoin/bips PR #1670](https://github.com/bitcoin/bips/pull/1670)
- **Full text:** [bip360.org](https://bip360.org/bip360.html)

**Design:** BIP-360 introduces a new output type — Pay-to-Quantum-Resistant-Hash (P2QRH) — that mirrors P2TR structurally but eliminates the key-path spend entirely. Instead of encoding a public key, the output commits only to a Merkle root of scripts. This removes the on-receipt public key exposure that makes P2TR immediately quantum-vulnerable.

**What BIP-360 does not do:** It does not specify a PQC signature algorithm. It is infrastructure for quantum-resistant output types; algorithm selection is a separate (and more contentious) decision.

**Implementation status:** BTQ Technologies deployed the first working BIP-360 implementation on a Bitcoin Quantum Testnet (v0.3.0) in March 2026, with 50+ miners and 100,000+ blocks processed.

---

### BIP-361 — Post-Quantum Migration and Legacy Signature Sunset

- **Authors:** Jameson Lopp (Casa CTO, lead), Christian Papathanasiou, Ian Smith, Joe Ross, Steve Vaile, Pierre-Luc Dallaire-Demers
- **Formally assigned:** February 11, 2026
- **Status:** Informational draft — no immediate protocol action required
- **Coverage:** [news.bitcoin.com](https://news.bitcoin.com/bitcoin-developers-propose-freezing-coins-that-skip-quantum-safe-migration-under-bip-361/) | [cointelegraph.com](https://cointelegraph.com/news/bitcoin-devs-and-researchers-propose-freezing-quantum-vulnerable-coins-bip-361)

**Design:** A three-phase soft fork timeline building on BIP-360 activation:

- **Phase A** (~3 years after BIP-360 activation): No new funds may be sent to legacy quantum-vulnerable address types (P2PK, P2PKH, P2WPKH, P2TR).
- **Phase B** (~5 years after BIP-360 activation): All legacy ECDSA/Schnorr spends invalidated at consensus layer; non-migrated coins effectively frozen.
- **Phase C** (optional, separate BIP; requires a hard fork): Recovery of frozen coins via zero-knowledge proof of BIP-39 seed phrase ownership, enabling quantum-secure access proof without exposing the classical private key.

**Controversy:** BIP-361 directly targets approximately 5.6M dormant/potentially lost coins, including Satoshi Nakamoto's known holdings (~1.1M BTC in early P2PK UTXOs). **Adam Back** (Blockstream CEO) is a prominent opponent of mandatory freezing, advocating instead for optional upgrade paths. His position (stated April 16, 2026 per CoinDesk): "optional, not forced" — coin owners should have the choice to migrate without the protocol invalidating their assets.

---

## PQC Algorithm Candidates

Bitcoin's block size limit (~2–4 MB) makes signature size a critical constraint. Candidate algorithms, ranked by practical fitness for Bitcoin:

| Algorithm | Standard | Signature Size | Public Key | Notes |
|---|---|---|---|---|
| **FN-DSA (Falcon-512)** | NIST FIPS 206 (draft) | ~655 bytes | ~897 bytes | Best size-to-security ratio; favored by BIP-360 authors and BTQ. Complex implementation (requires floating-point arithmetic). |
| **ML-DSA (Dilithium2)** | NIST FIPS 204 | ~2,420 bytes | ~1,312 bytes | Simpler implementation than Falcon; larger signatures. Roughly 37x Schnorr signature size. |
| **SLH-DSA (SPHINCS+-128s)** | NIST FIPS 205 | ~7,856 bytes | 32 bytes | Hash-based; most conservative security assumptions. Signature size is impractical for high-volume Bitcoin use. |
| **Hash-based via OP_CAT** | — | Variable | — | Winternitz/hash-based signatures implementable in Bitcoin Script if OP_CAT is activated. Conservative security assumptions; script-level solution without consensus changes beyond OP_CAT. |
| **Lamport** | — | ~10s of KB | — | Theoretically possible; impractical for Bitcoin at current block size limits. |
| **XMSS** | NIST SP 800-208 | ~2,500 bytes | 64 bytes | Stateful; key state management complexity is prohibitive for Bitcoin's UTXO model. |

For comparison: Schnorr (BIP-340) signatures are 64 bytes. Falcon-512 at ~655 bytes represents approximately a 10x overhead — reducing transactions-per-block by roughly 10x at current throughput without accompanying block size changes.

Academic analysis: A November 2025 paper by Mikhail Kudinov and Jonas Nick (Blockstream) — "[Hash-based Signature Schemes for Bitcoin](https://eprint.iacr.org/2025/2203.pdf)" (IACR ePrint 2025/2203) — specifically analyzes compact hash-based options for Bitcoin's constraints.

---

## Key Technical Challenges

**Block space pressure:** PQC signatures impose significant per-transaction overhead. Falcon-512 (~655 bytes) vs. Schnorr (64 bytes) is approximately 10x; ML-DSA (~2,420 bytes) is approximately 37x. Without block size increases (politically contentious in Bitcoin), PQC migration would severely constrain transaction throughput.

**Lightning Network:** Lightning channels require participants to exchange public keys. There is no hash protection available — Lightning is structurally more vulnerable than on-chain Bitcoin. A full Lightning PQC migration requires entirely new channel types and may effectively reset the network.

**Soft fork vs. hard fork requirements:** BIP-360 achieves quantum-resistant address infrastructure via soft fork. BIP-361 Phase B (freezing old signatures) and Phase C (ZK-proof recovery) each require a hard fork — substantially raising the political bar for full migration.

**Satoshi coins:** Any freeze proposal must contend with approximately 1.1M BTC in P2PK outputs associated with Satoshi's early mining activity. These coins have never moved. Freezing them would be perceived by many as a property rights violation and a precedent-setting attack on Bitcoin's fixed-supply guarantee.

**Upgrade lead time:** Bitcoin's conservative governance process means 5–10 years from activation to broad ecosystem adoption is a realistic estimate, per core developers (per CoinDesk, December 2025). BIP-360 must still achieve miner signaling, full node adoption, and wallet ecosystem support before activation.

**Google's March 2026 threat paper:** Google Quantum AI published a paper on March 31, 2026 reducing estimates for CRQC resource requirements — under optimistic error rate assumptions, fewer than 500,000 physical qubits might suffice to break ECDLP-256. The paper set 2029 as a migration target. This raised urgency across the cryptocurrency ecosystem.

---

## Notable Developments

- **2024-12:** BIP-360 draft published.
- **2026-02-11:** BIP-361 formally assigned.
- **2026-03:** BTQ Technologies deploys BIP-360 on Bitcoin Quantum Testnet v0.3.0 (50+ miners, 100,000+ blocks).
- **2026-03-31:** Google Quantum AI paper reduces CRQC resource estimates; sets 2029 migration target.
- **2026-04:** Active community debate on coin freeze provisions (Lopp vs. Back). CoinDesk coverage: "[Bitcoin's $1.3T Security Race](https://www.coindesk.com/tech/2026/04/04/bitcoin-s-usd1-3-trillion-security-race-key-initiatives-aimed-at-quantum-proofing-the-world-s-largest-blockchain)" (April 4, 2026); "[Bitcoin's Quantum Debate Splits](https://www.coindesk.com/tech/2026/04/16/bitcoin-s-quantum-debate-splits-as-adam-back-pushes-optional-upgrades-over-forced-freeze)" (April 16, 2026).

<!-- TODO: Monitor BIP-360 miner signaling status; track if a specific algorithm is formally proposed as companion BIP -->
<!-- TODO: Track Phase C (ZK-proof recovery) development — which ZK proof system is proposed? -->
<!-- TODO: Follow Adam Back / Blockstream's alternative proposal once published -->

---

## Key People

- **Hunter Beast** — Lead BIP-360 author; primary architect of P2QRH/P2MR approach.
- **Ethan Heilman** — Co-author BIP-360; cryptography researcher; co-author of the Taproot Annex BIP.
- **Jameson Lopp** (Casa CTO) — Lead BIP-361 co-author; advocates mandatory freeze and migration timeline; prominent Bitcoin security researcher.
- **Adam Back** (Blockstream CEO) — Vocal opponent of mandatory coin freeze; advocates optional phased upgrade path; co-inventor of Hashcash (Bitcoin's PoW basis).
- **Jonas Nick** (Blockstream) — Co-author of hash-based signatures for Bitcoin research (with Kudinov, IACR 2025).
- **Project Eleven team** — Maintains the Bitcoin Risq List; quantitative exposure analysis and testnet implementation.
- **BTQ Technologies** — Deployed BIP-360 testnet; active in Bitcoin PQC standardization.

---

## Claim Verification

### Claim: ~28–35% of Bitcoin supply is in quantum-vulnerable addresses

**Status:** Broadly verified (range, not a single number)

**Supporting sources:**
- Project Eleven Bitcoin Risq List (open-source, weekly-updated exposure database)
- Ark Invest / Unchained Capital analysis (March 2026): ~35% of outstanding supply
- CCN analysis: ~6M BTC at elevated quantum risk

**Refuting / questioning sources:**
- CoinShares research ("Quantum Vulnerability in Bitcoin: A Manageable Risk") argues most vulnerable P2PK coins (largely Satoshi-era) are likely permanently lost and will never be spent, reducing the practical threat

**Summary:** The range (~28–35%) reflects different methodologies and assumptions about lost coins. The directional finding — a substantial fraction of supply is in long-exposure quantum-vulnerable state — is well-supported across independent analyses.

---

### Claim: Bitcoin migration timeline is 5–10 years from activation

**Status:** Editorial judgment / consensus estimate

**Supporting sources:**
- Core developer statements cited in CoinDesk (December 2025)
- Historical precedent: SegWit (proposed 2015, activated August 2017 — ~2 years) and Taproot (proposed 2018, activated November 2021 — ~3 years), both less controversial than a signature scheme migration
- BIP-360 has not yet achieved miner signaling; BIP-361 is informational only

**Summary:** 5–10 years is a reasonable estimate for full ecosystem migration, given that the most analogous upgrades took 2–3 years just for activation, and adoption of new address types continues to lag years after activation.

---

## Sources

- [Bitcoin Optech: Quantum Resistance](https://bitcoinops.org/en/topics/quantum-resistance/)
- [BIP-360 full text at bip360.org](https://bip360.org/bip360.html)
- [BIP-361 — Bitcoin.com coverage](https://news.bitcoin.com/bitcoin-developers-propose-freezing-coins-that-skip-quantum-safe-migration-under-bip-361/)
- [BIP-361 — CoinTelegraph coverage](https://cointelegraph.com/news/bitcoin-devs-and-researchers-propose-freezing-quantum-vulnerable-coins-bip-361)
- [CoinDesk: Bitcoin's $1.3T Security Race (April 4, 2026)](https://www.coindesk.com/tech/2026/04/04/bitcoin-s-usd1-3-trillion-security-race-key-initiatives-aimed-at-quantum-proofing-the-world-s-largest-blockchain)
- [CoinDesk: Bitcoin's Quantum Debate Splits (April 16, 2026)](https://www.coindesk.com/tech/2026/04/16/bitcoin-s-quantum-debate-splits-as-adam-back-pushes-optional-upgrades-over-forced-freeze)
- [CoinDesk: Bitcoin Developers and Frozen Coins (April 15, 2026)](https://www.coindesk.com/tech/2026/04/15/bitcoin-developers-are-trying-to-build-quantum-defenses-your-coins-could-pay-the-price)
- [BTQ Technologies: BIP-360 Testnet v0.3.0 (March 2026)](https://www.prnewswire.com/news-releases/btq-technologies-announces-first-deployment-of-bip-360-on-bitcoin-quantum-testnet-v0-3-0--302718592.html)
- [Project Eleven: Quantum vulnerability of Bitcoin addresses](https://blog.projecteleven.com/posts/quantum-vulnerability-of-bitcoin-addresses)
- [Project Eleven: Bitcoin Risq List](https://www.projecteleven.com/bitcoin-risq-list)
- [Onramp Bitcoin: Address types and quantum exposure tiers](https://onrampbitcoin.com/knowledge-center/which-bitcoin-is-vulnerable-to-quantum-computing-address-types-exposure-tiers-and-what-you-can-do)
- [CoinShares: Quantum vulnerability in Bitcoin — a manageable risk](https://coinshares.com/insights/research-data/quantum-vulnerability-in-bitcoin-a-manageable-risk/)
- [Google Quantum AI: Safeguarding cryptocurrency (March 31, 2026)](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/)
- [Bloomberg: Google paper warns crypto of quantum risk, 2029 timeline (March 31, 2026)](https://www.bloomberg.com/news/articles/2026-03-31/google-paper-warns-crypto-on-quantum-risk-ahead-of-2029-timeline)
- [Federal Reserve Staff Paper 2025-093: HNDL and DLT Networks](https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm)
- [Citi Institute: Trillion-Dollar Security Race (January 2026)](https://www.citigroup.com/rcs/citigpa/storage/public/Citi_Institute_Quantum_Threat.pdf)
- [IACR ePrint 2025/2203: Hash-based Signature Schemes for Bitcoin (Kudinov, Nick)](https://eprint.iacr.org/2025/2203.pdf)
- [Preprints.org: Hybrid PQC Signatures for Bitcoin and Ethereum (September 2025)](https://www.preprints.org/manuscript/202509.2079)
- [CCN: 6M BTC exposed to quantum threats](https://www.ccn.com/news/crypto/crypto-token-quantum-risk-btc-eth-exposed-threat/)
- [Chainalysis: Quantum Computing and Cryptocurrency](https://www.chainalysis.com/blog/quantum-computing-crypto-security/)
- [QBIP.org — companion Bitcoin PQC tracking site](https://qbip.org/)
