---
title: "Quantum Key Distribution"
date: 2026-06-02
lastmod: 2026-06-02
draft: false
description: "Companies and technologies in Quantum Key Distribution (QKD): physics-based key exchange using entangled photons and quantum channels."
research_area: "post-quantum-encryption/qkd"
last_reviewed: 2026-06-02
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

Quantum Key Distribution (QKD) is a method for establishing cryptographic keys whose security is guaranteed by the laws of physics rather than computational hardness assumptions. Unlike post-quantum cryptography (PQC), which replaces classical algorithms with quantum-resistant math, QKD physically distributes symmetric key material via quantum channels — typically fiber optic links carrying single photons or entangled photon pairs. Any eavesdropping attempt disturbs the quantum states, making interception detectable in principle.

The dominant commercial approach is entanglement-based QKD (eQKD), derived from the BBM92 protocol. A central photon source generates polarization-entangled pairs; each endpoint measures its photon, and the correlated measurement outcomes yield a shared key without transmitting the key itself. This eliminates trust assumptions around the photon source and removes the need for trusted relay nodes for inter-city distances.

QKD is complementary to PQC rather than a direct substitute. PQC secures software and protocols; QKD secures key exchange on dedicated fiber infrastructure. Governments and critical infrastructure operators with long secrecy requirements (finance, defense, telecoms backhaul) are the primary market.

## Key Themes

- Entanglement-based QKD removes the "trusted relay node" requirement that limits prepare-and-measure QKD to shorter hops
- Commercial viability depends on reducing cost, size, and operational complexity of photon source and detector hardware
- European vendors (Austria, UK) lead early commercialization; China has deployed QKD at national scale (Beijing-Shanghai backbone) but as state infrastructure
- Hybrid deployments combining QKD-distributed keys with conventional AES encryption are the most practical near-term architecture

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|----|-------|---------|
| [zerothird](https://zerothird.com) | Vienna, Austria | Seed+ | Entanglement-based QKD systems and Key-as-a-Service for enterprise and critical infrastructure |
| [Toshiba Quantum](https://www.toshiba.eu/pages/eu/Cambridge-Research-Laboratory/quantum-information/) | Cambridge, UK | Growth | QKD hardware and quantum networks, spun out of Toshiba Research Cambridge |
| [ID Quantique](https://www.idquantique.com) | Geneva, Switzerland | Growth | QKD systems, quantum random number generators; one of the earliest commercial QKD vendors |
