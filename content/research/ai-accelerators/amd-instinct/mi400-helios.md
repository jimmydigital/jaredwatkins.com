---
title: "AMD Instinct MI400 Series & Helios Rack"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "AMD's next-generation CDNA 5 GPU accelerators (MI430X, MI440X, MI455X) and Helios rack-scale AI system; 72 GPUs, 31 TB HBM4, 2.9 exaFLOPS FP4; targeting H2 2026."
research_area: "ai-accelerators/amd-instinct"
source_urls:
  - "https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-touts-instinct-mi430x-mi440x-and-mi455x-ai-accelerators-and-helios-rack-scale-ai-architecture-at-ces"
  - "https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199"
  - "https://www.servethehome.com/not-just-for-oreos-and-trailers-amd-helios-next-gen-ai-racks-go-double-wide/"
  - "https://www.techpowerup.com/337987/amd-previews-432-gb-hbm4-instinct-mi400-gpus-and-helios-rack-scale-ai-solution"
  - "https://newsletter.semianalysis.com/p/amd-advancing-ai-mi350x-and-mi400-ualoe72-mi500-ual256"
  - "https://www.datacenterdynamics.com/en/news/amd-unveils-full-mi400-product-lineup-claims-mi500-chips-will-deliver-1000x-increase-in-ai-performance/"
last_reviewed: 2026-06-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The MI400 series is AMD's fifth-generation CDNA accelerator line, announced at CES 2026 with a target production ramp in H2 2026. Three variants cover a range of use cases: MI430X (cost-optimized), MI440X (balanced), and MI455X (flagship). The MI455X anchors AMD's Helios rack-scale system — a double-wide rack housing 72 MI455X GPUs with 31 TB of HBM4 memory and a stated 2.9 exaFLOPS FP4 aggregate throughput. The MI400 generation moves to TSMC 2nm, adopts HBM4, and introduces UALink for scale-up interconnect alongside UltraEthernet for scale-out.

## Key Facts

- **Architecture:** CDNA 5 (5th Gen)
- **Process node:** TSMC 2nm (first GPU family on 2nm)
- **Variants:** MI430X (entry), MI440X (mid), MI455X (flagship)
- **Memory per GPU (MI455X):** 432 GB HBM4; 19.6 TB/s bandwidth
- **Peak compute per GPU (MI455X):** ~40 PFLOPS FP4; ~20 PFLOPS FP8 (AMD stated, not independently verified)
- **Scale-up interconnect:** UALink (AMD, open standard co-developed with industry consortium)
- **Scale-out interconnect:** UltraEthernet (UEC spec), AMD Pensando Pollara NICs
- **Helios rack — GPU count:** 72 MI455X GPUs
- **Helios rack — aggregate memory:** 31 TB HBM4
- **Helios rack — aggregate compute:** 2.9 exaFLOPS FP4; 1.4 exaFLOPS FP8
- **Helios rack — scale-up bandwidth:** 260 TB/s aggregate
- **Helios rack — scale-out bandwidth:** 43 TB/s Ethernet-based
- **Helios rack — form factor:** Double-wide rack (wider than standard 19-inch)
- **Host CPU:** Zen 6-based EPYC Venice processors
- **Status:** Announced; production ramp H2 2026 (Q3 2026 per AMD public statements)
- **Key customer:** OpenAI (disclosed June 2025, described as anchor customer)

## What It Is / How It Works

The Helios system represents AMD's most aggressive move into rack-scale integrated AI infrastructure — analogous to NVIDIA's NVL72/NVL144 GB200 rack systems. Rather than selling individual GPUs and letting OEMs build systems, AMD (with partners) delivers Helios as a complete rack unit with GPUs, networking, cooling, and host CPUs pre-integrated.

**Form factor:** Helios uses a double-wide rack — wider than the standard 600mm 19-inch rack — to accommodate the thermal and electrical requirements of 72 MI455X GPUs. AMD has noted this requires operator planning for physical footprint in advance.

**Scale-up interconnect (UALink):** The MI400 generation transitions from proprietary Infinity Fabric (for scale-up within a rack) to UALink, an open-standard developed under the UALink Consortium. UALink is AMD's answer to NVIDIA's proprietary NVLink/NVSwitch — it achieves comparable bandwidth but under an industry-consortium governance model, theoretically allowing other vendors to implement compatible switches. At rack scale, Helios delivers 260 TB/s of UALink-based scale-up bandwidth for 72 GPUs.

**Scale-out interconnect (UltraEthernet):** Between Helios racks, AMD uses the UltraEthernet Consortium (UEC) standard over AMD Pensando Pollara NICs. UltraEthernet adds RDMA semantics, congestion control, and loss-recovery optimized for AI all-reduce traffic patterns onto standard Ethernet physical layer — again positioned as a CUDA-free, open alternative to InfiniBand.

**HBM4:** The MI455X's 432 GB HBM4 per chip represents roughly 2.25x the memory of the NVIDIA B200 (192 GB). At rack scale, 31 TB of aggregate HBM4 in a single Helios rack is AMD's central capacity argument for very large model deployment.

**Process:** TSMC 2nm is the most advanced commercially available node as of mid-2026, giving AMD a process advantage if production yields are viable.

## Notable Developments

- **2026-06:** AMD and OpenAI announce OpenAI as Helios/MI400 anchor customer; Lisa Su and Sam Altman appear together at AMD Advancing AI event — AMD frames the deal as validation of its rack-scale approach
- **2026-05:** AMD unveils full MI400 product lineup at Advancing AI 2025 event; announces MI500 roadmap with claimed 1000x AI performance improvement over multi-year horizon
- **2026-02:** AMD confirms Helios and MI400 on track for H2 2026 ramp in quarterly investor communications
- **2026-01:** CES 2026 — AMD discloses MI430X, MI440X, MI455X product family and Helios rack architecture with specifications; announces double-wide rack form factor; confirms UALink and UltraEthernet as interconnect standards

## Competitive Context

Helios targets NVIDIA's GB200 NVL72 and NVL144 rack-scale systems directly. The NVL72 packages 72 GB200 GPUs in a liquid-cooled rack; NVIDIA quotes ~1.4 exaFLOPS FP8 per NVL72 rack. AMD claims 1.4 exaFLOPS FP8 and 2.9 exaFLOPS FP4 for Helios — roughly comparable FP8 numbers with an advantage at FP4, though FP4 precision applicability varies by model and workload.

Key competitive differences:
- **Memory:** Helios 31 TB vs. NVL72 approximately 13.5 TB HBM3e — AMD claims a substantial lead here
- **Interconnect:** UALink (open) vs. NVLink (proprietary) — AMD's open-standards argument is relevant for buyers concerned about vendor lock-in
- **Availability:** Helios targets Q3 2026; NVL72/144 B200 systems are already shipping — NVIDIA has a timing lead
- **Software:** CUDA ecosystem vs. ROCm — NVIDIA retains a significant software maturity advantage

## Claim Verification

### Claim: Helios delivers 2.9 exaFLOPS FP4 per rack

**Status:** Unverified — no independent benchmark yet (product not yet shipping as of June 2026)

**Supporting sources:**
- [Tom's Hardware — CES 2026 MI400 announcement](https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-touts-instinct-mi430x-mi440x-and-mi455x-ai-accelerators-and-helios-rack-scale-ai-architecture-at-ces) — AMD stated spec at announcement
- [TechPowerUp — MI400 preview](https://www.techpowerup.com/337987/amd-previews-432-gb-hbm4-instinct-mi400-gpus-and-helios-rack-scale-ai-solution) — corroborates AMD announcement figures

**Refuting / questioning sources:**
- No independent third-party benchmark — product announced but not yet shipping
- Peak FLOPS figures assume FP4 precision with no accuracy degradation guarantees and ideal interconnect conditions

**Summary:** All figures are AMD announcements; independent verification will require post-shipment MLPerf or third-party benchmarks expected late 2026.

### Claim: OpenAI is an anchor customer for Helios

**Status:** Partially verified

**Supporting sources:**
- [CNBC — AMD MI400 OpenAI announcement June 2025](https://www.cnbc.com/2025/06/12/amd-mi400-ai-chips-openai-sam-altman.html) — Lisa Su and Sam Altman appeared together; customer relationship disclosed

**Refuting / questioning sources:**
- Contract volume and deployment timeline not publicly disclosed
- Whether OpenAI is using ROCm or CUDA-compatible software layer not confirmed

**Summary:** Customer relationship publicly confirmed by both companies; commercial terms undisclosed.

## Sources

- [Tom's Hardware — CES 2026 MI400/Helios announcement](https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-touts-instinct-mi430x-mi440x-and-mi455x-ai-accelerators-and-helios-rack-scale-ai-architecture-at-ces)
- [Next Platform — MI400/Helios on track H2 2026](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)
- [ServeTheHome — Helios double-wide rack](https://www.servethehome.com/not-just-for-oreos-and-trailers-amd-helios-next-gen-ai-racks-go-double-wide/)
- [TechPowerUp — MI400 432 GB HBM4 preview](https://www.techpowerup.com/337987/amd-previews-432-gb-hbm4-instinct-mi400-gpus-and-helios-rack-scale-ai-solution)
- [SemiAnalysis — MI350X and MI400](https://newsletter.semianalysis.com/p/amd-advancing-ai-mi350x-and-mi400-ualoe72-mi500-ual256)
- [Data Center Dynamics — MI400 full lineup](https://www.datacenterdynamics.com/en/news/amd-unveils-full-mi400-product-lineup-claims-mi500-chips-will-deliver-1000x-increase-in-ai-performance/)
- [CNBC — AMD MI400/OpenAI June 2025](https://www.cnbc.com/2025/06/12/amd-mi400-ai-chips-openai-sam-altman.html)
