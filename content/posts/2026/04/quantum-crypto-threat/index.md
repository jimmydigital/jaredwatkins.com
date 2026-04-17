---
title: "The Clock Is Already Running on Quantum Crypto Risk"
date: 2026-04-17
draft: false
description: "Quantum computers will eventually break most of the encryption protecting the internet, financial systems, and crypto assets. Here's where that stands, what it'll cost to fix, and why the timeline might be shorter than anyone comfortable."
tags: ["quantum", "cryptography", "security", "cryptocurrency", "post-quantum", "bitcoin", "networking"]
categories: ["Computing and Tech"]
---

On March 31, Google Quantum AI published a paper that got quiet but serious attention from the security world. The upshot: under optimistic error rate assumptions, you might need fewer than 500,000 physical qubits to break the elliptic curve cryptography that underpins almost everything on the internet. Previous estimates were in the millions. Their suggested migration target is 2029.

That's not "quantum computers are coming someday." That's three years.

<!--more-->

To understand why this matters, you need to know what "break" means here. RSA, ECDSA, and Diffie-Hellman, the signature and key exchange algorithms that secure HTTPS, VPNs, SSH, email, banking, and a substantial fraction of the world's financial infrastructure, rely on mathematical problems (integer factorization and discrete logarithm) that are hard for classical computers. In 1994, Peter Shor showed that a quantum computer could solve these problems efficiently. We've been slowly accepting that this would eventually be a real problem ever since. "Eventually" keeps getting closer.

The threat isn't only about what a quantum computer breaks in real-time. There's a second threat model called "harvest now, decrypt later" (HNDL), and it's already happening. Nation-state adversaries are almost certainly collecting encrypted traffic today (VPN sessions, TLS connections, classified communications) with the explicit intent to decrypt it retroactively once a CRQC (a cryptographically relevant quantum computer) becomes available. If your data needs to stay secret for more than 5 to 10 years, the security clock is already running, not starting when a CRQC is built.

## Why now?

The NIST post-quantum cryptography standardization process has been grinding along since 2016, and in August 2024 it finally produced real standards: FIPS 203, 204, and 205. These are the CRYSTALS-Kyber and Dilithium-derived algorithms that are going to replace RSA and ECDH everywhere. The standards are done. The problem is that "done" at NIST and "deployed everywhere" are separated by a gap that historically takes a decade or more to close.

And Google's paper just compressed the urgency. Prior estimates suggesting we had until the mid-2030s to get our act together were already making people uncomfortable; a plausible path to CRQC by 2029 is a different conversation entirely.

## Network infrastructure

For enterprise networking, the migration path exists but it's not plug-and-play. IKEv2/IPsec (the protocol behind most enterprise VPNs) has IETF extensions for PQC KEMs (RFC 9242, RFC 9370). TLS 1.3 has hybrid key exchange drafts; Chrome and Firefox have been running X25519Kyber768 in some configurations since 2023. The standards are real and the protocol work is largely done.

The vendor picture is messier. Fortinet, Palo Alto, Check Point, and Cisco all ship or are shipping ML-KEM IKEv2 support in recent software versions. But "ships support" and "deployed in production at scale across heterogeneous environments" are not the same thing. Most of these implementations are software-only right now, with meaningful CPU overhead. A lot of networking hardware doesn't have the crypto acceleration to run post-quantum algorithms at line rate. Interoperability between vendor implementations is still an open problem. And then there's the long tail of embedded devices, industrial systems, and legacy infrastructure that nobody's going to upgrade on a 3-year timeline regardless of how urgent the threat becomes.

The cost to upgrade just the identifiable enterprise network perimeter globally (firewalls, VPN concentrators, core routing infrastructure) is probably in the low hundreds of billions of dollars when you account for hardware refresh cycles, migration labor, and the operational disruption of replacing cryptographic algorithms end-to-end. That's before touching government classified systems (which have hard mandates under NSA's CNSA 2.0 by 2030) or financial sector infrastructure. The Fed and CISA have both been clear that the financial sector needs to treat this as a critical infrastructure priority, but the actual upgrade spend is still largely ahead of us.

## Cryptocurrency is a much harder problem

Enterprise networking is hard because of scale and operational inertia. Cryptocurrency is hard for a different and more fundamental reason: there's no one in charge.

Bitcoin uses ECDSA secp256k1 and Schnorr signatures for transaction authorization. Both are fully quantum-vulnerable via Shor's algorithm. Approximately 28 to 35% of the total Bitcoin supply sits in addresses where the public key is already visible on-chain, meaning a CRQC could derive the private key directly without the owner doing anything. That's somewhere in the neighborhood of 6 to 7 million BTC, including most of Satoshi's known holdings (around 1.1M BTC in early P2PK outputs). At current prices that's over a trillion dollars in directly attackable assets across the crypto ecosystem.

Migrating Bitcoin requires the whole ecosystem to agree on a new signature scheme, ship it as a consensus change (probably a soft fork for the address infrastructure, definitely a hard fork for phasing out old signature types), and then get every wallet, exchange, node operator, and user to actually do the migration. The historical precedent here is not encouraging. SegWit took about two years from proposal to activation, and a significant portion of the network still doesn't use it. Taproot activated in 2021 and most wallets still default to legacy address types. Core developers are estimating 5 to 10 years for full Bitcoin PQC migration from the point a change is activated. That's a best case.

There's an active governance debate happening right now. BIP-360 proposes quantum-resistant output infrastructure, and BIP-361 proposes a controversial phased sunset of legacy signature types that would effectively freeze coins in old address formats that don't migrate. Jameson Lopp (Casa CTO) is driving the more aggressive approach. Adam Back is publicly against mandatory freezing. The fact that this is still being debated at the conceptual level, with no miner signaling, no algorithm formally selected, and a testnet that's only a few weeks old, is not reassuring given the 2029 migration target that Google just put on the table.

Ethereum is in a similar position but with a more organized response. They have a dedicated post-quantum team, an active proposal (EIP-8141), and devnets running. Their self-imposed 2029 migration deadline implies roughly seven hard forks in the remaining time. It's ambitious but at least there's an organized program.

Some chains are further along. Algorand has Falcon-based signatures live on mainnet for state proofs as of November 2025. QRL was built from the ground up as a quantum-resistant blockchain in 2018. But the assets most at risk are on Bitcoin and Ethereum, which have the most value, the most decentralized governance, and therefore the hardest migration paths.

## The broader picture

Beyond networks and crypto, there's everything else. HTTPS certificates that secure web browsing. S/MIME email encryption. Code signing certificates that verify software updates. Document signing. The PKI underpinning most of the internet's trust model. Healthcare record confidentiality, where HNDL is particularly concerning given how long medical data retains sensitivity. Financial records. Legal contracts. Smart grid infrastructure. Every layer of the stack that relies on public-key cryptography has to migrate, in some cases multiple times (signing and key exchange often use different algorithms).

Early estimates for migrating federal government systems put the number well north of $7 billion and the better part of this decade to complete. The private sector is an order of magnitude larger. The total cost of global crypto infrastructure migration, done properly, is probably in the trillions when you account for hardware, software, labor, testing, and the inevitable disruption to systems that can't be taken offline cleanly.

The realistic outcome isn't that we migrate everything in time. It's that we prioritize the highest-sensitivity, highest-value assets and connections, get those migrated first, and accept that long-tail infrastructure will remain vulnerable for years longer than is comfortable. That means some HNDL-harvested traffic will eventually be decrypted. Some legacy embedded systems will get cracked once a CRQC is operational. The question is whether the critical stuff (financial clearing, classified communications, critical infrastructure control) is protected before the window closes.

The standards exist. The vendor implementations are starting to arrive. The governance debates in decentralized systems are happening, if contentiously. Whether 2029 proves out as the actual CRQC timeline or the real date turns out to be 2032 or 2035, the direction is clear and the work is late. The difference between treating this as a three-year problem versus a fifteen-year problem is whether we're actually going to be ready.

I've been tracking this closely in the [research section](/research/post-quantum-encryption/). There's more depth there on specific vendor implementations, the cryptocurrency exposure numbers, and the NIST standards themselves, if you want to go further.
