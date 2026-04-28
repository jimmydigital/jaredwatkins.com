---
title: "Research Section Changelog"
date: 2026-04-04
lastmod: 2026-04-28
draft: false
description: "Timestamped log of additions and modifications to the Research knowledge base."
tags: ["changelog", "research"]
categories: ["overview"]
research_area: "research"
last_reviewed: 2026-04-04
stale_after_days: 90
outputs:
  - HTML
  - ResearchChangelog
sitemap:
  changefreq: "monthly"
  priority: 0.7
  disable: false
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Overview

[Subscribe via RSS](/research/changelog/index.xml)

This page tracks important additions and modifications to the Research knowledge base. Log entries include:
- **New entry creation** (new company, technology, person, or research page)
- **Major content revisions** (rewrite of What It Is / How It Works, significant corrections to claims)
- **Supply chain discoveries** (new shared supplier flags, strategic relationships)
- **Mass updates** (bulk changes across multiple pages)

Do not log trivial changes: flag additions, minor formatting, small frontmatter tweaks, or routine fact-checking updates are not logged here.

Each entry is a one-line timestamped summary.

## Changelog

- **2026-04-28:** Expanded [Wärtsilä]({{< relref "datacenters/behind-meter-power/wartsila-btm.md" >}}) — added BESS (Quantum3, 19+ GWh deployed, Eraring 3.1 GWh AU), marine propulsion (cruise, container, island grids), Caribbean projects (USVI, Bahamas, BVI, Bonaire, Cayman), and TAM sizing (marine ~$25.6B; stationary recip ~$64-79B).
- **2026-04-25:** Created [VITA 48 REDI thermal standards]({{< relref "datacenters/rugged-edge-compute/vita-48-thermal-standards.md" >}}) + 5 entries: [GMS]({{< relref "datacenters/rugged-edge-compute/general-micro-systems.md" >}}) (X7 RAPTOR 1"×4" RuggedCool +75°C <$10K), [Annapolis Micro Systems]({{< relref "datacenters/rugged-edge-compute/annapolis-micro-systems.md" >}}) (WILD100 SOSA VPX; WC34D0 VITA 48.4 LFT), [Core Systems]({{< relref "datacenters/rugged-edge-compute/core-systems.md" >}}) (ATMOS stackable nodes; +60°C GPU), [LCR Embedded Systems]({{< relref "datacenters/rugged-edge-compute/lcr-embedded-systems.md" >}}) (35yr defense chassis integrator; open-source VITA 46.11 manager), [7Starlake LFT ATR]({{< relref "datacenters/rugged-edge-compute/seven-starlake-liquid-atr.md" >}}) (7SL-3500 500W closed-loop VITA 48.4). Updated [half-rack overview]({{< relref "datacenters/rugged-edge-compute/half-rack-embedded-compute.md" >}}) with power/ruggedization specs; [rugged-edge-compute index]({{< relref "datacenters/rugged-edge-compute/_index.md" >}}) supply chain liquid cooling flag.
- **2026-04-25:** Created [MicroTCA standard overview]({{< relref "datacenters/rugged-edge-compute/microtca-standard.md" >}}) + 3 entries: [VadaTech]({{< relref "datacenters/rugged-edge-compute/vadatech.md" >}}) (Henderson NV; MCH+chassis+AMC; MTCA.0/1/3/4), [N.A.T. GmbH]({{< relref "datacenters/rugged-edge-compute/nat-europe.md" >}}) (Hennef DE; NAT-MCH-G4; CERN/DESY/PSI), [MicroTCA in 5G RAN]({{< relref "datacenters/rugged-edge-compute/microtca-in-5g-ran.md" >}}) (O-RAN DU; PTP/SyncE; 100 GbE fronthaul).
- **2026-04-25:** Created [half-rack embedded compute form factor]({{< relref "datacenters/rugged-edge-compute/half-rack-embedded-compute.md" >}}) + 4 platform entries: [Neousys SEMIL-1300]({{< relref "datacenters/rugged-edge-compute/neousys-semil-1300.md" >}}) (2U fanless IP67, -40°C), [ASUS RUC-1000]({{< relref "datacenters/rugged-edge-compute/asus-ruc-1000.md" >}}) (600W GPU 2U; half-rack fanless), [Galleon XSR]({{< relref "datacenters/rugged-edge-compute/galleon-xsr-half-rack.md" >}}) (3U NAS 80TB 100 Gbps US-owned), [7Starlake THOR200-U8-D]({{< relref "datacenters/rugged-edge-compute/seven-starlake-thor200-u8-d.md" >}}) (2.5U NAS 64TB Xeon D MIL-STD-810).
- **2026-04-25:** Created new [edge-ai-accelerators]({{< relref "datacenters/edge-ai-accelerators/_index.md" >}}) subsection with entries for [Hailo]({{< relref "datacenters/edge-ai-accelerators/hailo.md" >}}) (Hailo-8 26 TOPS/2.5W M.2/PCIe, Hailo-15 TSMC 5nm, Raspberry Pi AI HAT+) and [EdgeCortix]({{< relref "datacenters/edge-ai-accelerators/edgecortix.md" >}}) (SAKURA-I/II CGRA architecture, 40+ TOPS, defense/ISR focus, Tokyo HQ). Created 5 new rugged/semi-industrial edge compute entries: [Crystal Group]({{< relref "datacenters/rugged-edge-compute/crystal-group.md" >}}) (Cedar Rapids IA; RE4100 shipboard MIL-STD-901D, RE1900M vehicle-mount), [Neousys Technology]({{< relref "datacenters/rugged-edge-compute/neousys.md" >}}) (Advantech subsidiary; SEMIL-2200/2200GC fanless GPU AI servers), [Premio]({{< relref "datacenters/rugged-edge-compute/premio.md" >}}) (JCO-6000-ORN/JCO-3000-ORN Jetson Orin; RCO + EDGEBoost modular I/O), [ADLINK Technology]({{< relref "datacenters/rugged-edge-compute/adlink.md" >}}) (AXE/DLAP rugged GPU servers; SOSA-aligned OpenVPX; TWSE:6166), [DFI]({{< relref "datacenters/rugged-edge-compute/dfi.md" >}}) (Taiwan industrial fanless computers + GPU AI systems). Updated [rugged-edge-compute index]({{< relref "datacenters/rugged-edge-compute/_index.md" >}}) overview and tracker table.
- **2026-04-25:** Created [datacenter-opposition]({{< relref "datacenter-opposition/_index.md" >}}) section — regulatory, NIMBY, and grid-impact controversies around datacenter expansion; linked entries for environmental justice advocates, case studies (Mesa AZ water fights, Oregon permitting freezes), and incumbent utility opposition to behind-meter SMR/renewables power models.
- **2026-04-25:** Created 4 missing BTM power company profiles for [behind-meter-power]({{< relref "datacenters/behind-meter-power/_index.md" >}}) section: [TerraPower Natrium]({{< relref "datacenters/behind-meter-power/terrapower-btm.md" >}}) (345 MW SMR + molten-salt storage, Meta 2.76 GW contract), [Radiant Kaleidos]({{< relref "datacenters/behind-meter-power/radiant-nuclear.md" >}}) (1.2 MWe microreactor, Equinix 20-unit preorder), [Caterpillar Solar Turbines]({{< relref "datacenters/behind-meter-power/caterpillar-solar-turbines.md" >}}) (1–39 MW gas turbines, Vertiv partnership Nov 2025), [Siemens Energy]({{< relref "datacenters/behind-meter-power/siemens-energy-btm.md" >}}) (SGT series 40–200 MW heavy-frame turbines, modular 500 MW plants with Eaton). Resolved 5 Hugo REF_NOT_FOUND errors in _index.md.
- **2026-04-19:** Created [Google Quantum AI]({{< relref "quantum-computing/google-quantum-ai.md" >}}) — Willow 105-qubit (2024); below-threshold error correction (partially verified, Nature); 2019 supremacy claim classically matched (Frontier ~6 sec); dual-modality expansion to neutral atoms (Mar 2026).
- **2026-04-17:** Created [Bitcoin PQC]({{< relref "post-quantum-encryption/cryptocurrencies/bitcoin-pqc.md" >}}) — BIP-360 (P2MR soft fork, BTQ testnet Mar 2026) and BIP-361 (coin freeze, Lopp vs. Back debate); ~28–35% BTC supply in long-exposure quantum-vulnerable state; Falcon/FN-DSA primary algorithm candidate; 5–10 year migration timeline estimate.
- **2026-04-17:** Created [Ethereum PQC]({{< relref "post-quantum-encryption/cryptocurrencies/ethereum-pqc.md" >}}) — EIP-8141 frame transactions (CFI Hegota H2 2026); leanSig/leanXMSS for validator attestation aggregation; pq.ethereum.org devnets active (Mar 2026); Strawmap targets full L1 PQC by ~2029; ~90M ETH at quantum exposure.
- **2026-04-17:** Created [Other Chains PQC]({{< relref "post-quantum-encryption/cryptocurrencies/other-chains-pqc.md" >}}) — Algorand (Falcon live on mainnet Nov 2025, first PQC mainnet tx); Solana (ML-DSA testnet 3,000 TPS Dec 2025); Cardano (Project Nightstream, Google/Microsoft collaboration Feb 2026); QRL (purpose-built XMSS→ML-DSA; Testnet V2 Mar 2026); exchange and wallet readiness (Coinbase advisory board; Trezor Safe 7).
- **2026-04-17:** Updated [Cryptocurrencies PQC index]({{< relref "post-quantum-encryption/cryptocurrencies/_index.md" >}}) — Phase 2 now active; platform status summary table; Google March 2026 paper context.
- **2026-04-17:** Updated [Networking PQC vendor survey]({{< relref "post-quantum-encryption/networking/other-vendors.md" >}}) — Added confirmed GA release versions: Fortinet FortiOS 7.6.1 (earliest GA), Palo Alto PAN-OS 12.1 Orion (Aug 2025, broadest coverage), Check Point Gaia R82 (API-only), Cisco IOS XE 26 (full-stack Apr 2026) + ASA 9.19/FTD roadmap; OpenSSL 3.5 (ML-KEM default TLS); strongSwan 6.0.0; WireGuard PSK workaround; Cloudflare One (Feb 2026); Nokia ANYsec/QKD distinction; draft-ietf-ipsecme-ikev2-mlkem-05 IANA gap noted.
- **2026-04-17:** Updated [Networking PQC index]({{< relref "post-quantum-encryption/networking/_index.md" >}}) — Vendor table updated with confirmed GA release versions; research status updated.
- **2026-04-17:** Updated [Post-Quantum Encryption section index]({{< relref "post-quantum-encryption/_index.md" >}}) — Phase 2 marked in progress; research phases table expanded.
- **2026-04-15:** Created [Lasertec]({{< relref "semiconductors/fabrication-equipment/lasertec/_index.md" >}}) — EUV mask inspection monopoly; TSE:6920; actinic inspection sole supplier; Japan export controls; FY2025 ¥251.5B revenue.
- **2026-04-15:** Created [Semiconductors section]({{< relref "semiconductors/_index.md" >}}) and [Fabrication Equipment subsection]({{< relref "semiconductors/fabrication-equipment/_index.md" >}}) — supply chain table, public company index with TradingView widget, steering guide for equipment and export controls.
- **2026-04-15:** Created [Post-Quantum Encryption section]({{< relref "post-quantum-encryption/_index.md" >}}) — Phase 1 (networking): Sitehop, Juniper, and multi-vendor survey; Phase 2 (crypto) placeholder; full steering document with NIST FIPS 203/204/205 background.
- **2026-04-15:** Created [Sitehop]({{< relref "post-quantum-encryption/networking/sitehop-pqc-support.md" >}}) — UK PQC networking startup; FPGA-accelerated ML-KEM IPsec; University of Bristol spin-out; claim verification: line-rate PQC partially verified, govt contracts unverified.
- **2026-04-15:** Created [Juniper PQC Support]({{< relref "post-quantum-encryption/networking/juniper-pqc-support.md" >}}) — Juniper (now HPE division) IKEv2/IPsec PQC roadmap; Junos OS status; GA release unconfirmed from public sources.
- **2026-04-14:** Created [D-Wave Quantum]({{< relref "quantum-computing/d-wave.md" >}}) — quantum annealer (not gate-based); Advantage2 4,400+ qubits; 2025 Science supremacy claim actively disputed; $550M QCI acquisition for gate-model entry.
- **2026-04-07:** Created [Rigetti]({{< relref "quantum-computing/rigetti.md" >}}) — Rigetti Computing (NASDAQ: RGTI) superconducting QPU vendor; Ankaa-3 84-qubit system; Fab-1 in-house foundry; FY2024 revenue $10.8M; documented 2022 roadmap miss.
- **2026-04-07:** Created [SkyWater Technology]({{< relref "quantum-computing/skywater-technology.md" >}}) — U.S. DOD Trusted Foundry; pending $1.8B IonQ acquisition (shareholder vote May 8, 2026); FY2025 revenue $442.1M. Updated IonQ entry and section index.
- **2026-04-07:** Created [PsiQuantum]({{< relref "quantum-computing/psiquantum.md" >}}) — silicon photonics FTQC startup; $2.32B raised; DARPA QBI US2QC final phase selected; Victor Peng Interim CEO (Feb 2026).
- **2026-04-06:** Created [IBM Quantum]({{< relref "quantum-computing/ibm-quantum.md" >}}) — superconducting QPU; qLDPC error correction progress; 2029/2033 FTQC roadmap; Qiskit cloud platform.
- **2026-04-05:** Created [quantum-computing section]({{< relref "quantum-computing/_index.md" >}}) with initial entries: [IonQ]({{< relref "quantum-computing/ionq.md" >}}), [Quantinuum]({{< relref "quantum-computing/quantinuum.md" >}}), [Xanadu]({{< relref "quantum-computing/xanadu.md" >}}).
- **2026-04-05:** Created [Xanadu]({{< relref "quantum-computing/xanadu.md" >}}) — photonic QC; Borealis Nature 2022 advantage claim; Aurora 12-qubit system; March 2026 IPO (XNDU); $250M+ raised.
- **2026-04-05:** Created [Quantinuum]({{< relref "quantum-computing/quantinuum.md" >}}) — trapped-ion; Helios 98 qubits, 99.921% 2Q fidelity; 94 logical qubits milestone; Honeywell ~54% ownership.
- **2026-04-05:** Created [IonQ]({{< relref "quantum-computing/ionq.md" >}}) — trapped-ion; Forte/Tempo hardware; FY2024/2025 revenue from SEC filings; Skyloom/SkyWater acquisitions; all-founder departures.
- **2026-04-04:** Reorganized [energy/batteries]({{< relref "energy/batteries/_index.md" >}}) by value-chain layers; added cross-cutting insights and Q1 2026 updates across 12+ companies including tariff and supply chain impacts.
- **2026-04-04:** Created [HyperStrong]({{< relref "energy/batteries/hyperstrong.md" >}}) — top-5 global BESS integrator; added to Systems Integrators table.
- **2026-04-04:** Created [CNTE]({{< relref "energy/batteries/cnte.md" >}}) — Contemporary Nebula Technology Energy battery entry.
