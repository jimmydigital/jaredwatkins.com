---
title: "Cisco Expert Model"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "Design specification for a fine-tuned Cisco network engineer specialist LLM covering IOS, IOS-XE, NX-OS, and ASA: base model, training data requirements covering multiple OS variants, fine-tuning parameters, and edge deployment."
tags: ["cisco", "ios", "ios-xe", "nx-os", "asa", "specialist-models", "fine-tuning", "network-engineering", "llm"]
categories: ["technology"]
research_area: "local-llm-finetuning/specialist-models"
source_urls:
  - "https://www.cisco.com/c/en/us/support/docs/"
  - "https://developer.cisco.com/docs/"
  - "https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The Cisco expert model covers four meaningfully different operating systems under the "Cisco" umbrella: IOS/IOS-XE (most enterprise routers and switches), NX-OS (Nexus data center switches), IOS-XR (carrier/service provider routers — high-end ASR 9000/NCS), and ASA (legacy and current firewall platform, alongside FTD). This is the primary complexity challenge: training data must represent each OS family distinctly because command syntax differs significantly between them, and the model must track which platform it's operating on.

## Key Facts

- **Base model:** Llama 3.1 8B Instruct — same as Juniper model; two separate fine-tunes
- **Fine-tuning method:** QLoRA (r=16, α=32) — same parameters
- **OS families covered:** IOS/IOS-XE (primary), NX-OS (data center), ASA (firewall), IOS-XR (optional, complex)
- **Training data target:** 15,000–22,000 examples (larger than Juniper due to multi-OS complexity)
- **Critical challenge:** Model must explicitly track which OS it's addressing; cross-OS confusion is the primary failure mode
- **Deployment format:** Same GGUF Q4_K_M via Ollama as Juniper model

## What It Is / How It Works

**The multi-OS complexity problem.** Unlike JunOS (one OS across the Juniper product line with some feature variation), Cisco's device portfolio runs fundamentally different operating systems that share no common CLI syntax for many operations. The model must learn to:
1. Ask for (or infer from context) which Cisco platform it's addressing
2. Apply the correct syntax for that platform
3. Never produce IOS-XE commands in response to an NX-OS device question

This is best handled in the system prompt and in training data by always marking each example with the specific platform:

```
System: You are a senior Cisco network engineer with expertise across IOS/IOS-XE, 
NX-OS (Nexus), and ASA/FTD platforms. When responding, always identify which 
platform applies. If the user hasn't specified, ask before providing commands.
```

**IOS / IOS-XE (primary platform — highest coverage priority).** IOS-XE is the modern variant of IOS running on most current Catalyst switches (9000 series), ISR/ASR routers, and Edge platforms. Command syntax is ~95% identical to classic IOS but with additions: `show platform`, software package management, container support, IOS-XE specific `show` outputs. Training data should default to IOS-XE syntax but note IOS equivalents where they differ.

Key IOS-XE specific competencies:
- Routing: `show ip route`, `show ip bgp summary`, `show ip ospf neighbor` — note these all require `ip` (vs. JunOS which does not)
- ACLs: extended ACLs with named and numbered, permit/deny syntax, `access-list` vs. `ip access-list extended`
- QoS: Modular QoS CLI (MQC) — `class-map`, `policy-map`, `service-policy` — very different from JunOS CoS
- VRFs: `ip vrf <name>` vs NX-OS `vrf context <name>` — key difference
- HSRP/VRRP: Cisco HSRP (`standby` commands) vs JunOS VRRP — different syntax
- MPLS: `mpls ip`, `mpls ldp`, label switching
- Interface configuration: `interface GigabitEthernet0/0/0` (IOS-XE) vs `interface g0/0` (abbreviated shorthand)

**NX-OS (Nexus data center switches — second priority).** NX-OS is a separate OS codebase from IOS with significant syntactic differences. Critical differences that must be in training data:

- Feature model: features must be explicitly enabled (`feature ospf`, `feature bgp`, `feature vpc`) before configuration
- VPC (Virtual Port Channel): Nexus-specific MLAG implementation — `vpc domain`, `vpc peer-link`, `vpc peer-keepalive`
- EVPN/VXLAN: NX-OS EVPN syntax is different from both IOS-XE and JunOS EVPN
- NX-OS VRFs use `vrf context <name>` (not `ip vrf <name>`)
- `show interface status` output format differs from IOS
- `show version` field names differ
- No `enable` password — uses role-based access

**ASA (firewall platform — third priority).** ASA OS has the most distinct syntax of any Cisco platform. Legacy but still very widely deployed. Key concepts:

- Object-based NAT: `object network`, `nat (inside,outside)` syntax — very different from IOS
- Access control: `access-list <name> extended permit/deny` attached with `access-group`
- Security levels: `nameif`, `security-level` — unique to ASA
- VPN: `crypto isakmp policy`, `tunnel-group`, `group-policy` — IKEv1 and IKEv2 configuration syntax
- `show conn`, `show xlate`, `show asp drop` — ASA-specific troubleshooting commands
- FTD (Firepower Threat Defense): Replaces ASA in newer deployments; managed via FMC or FDM; CLI is limited compared to ASA but shares some ASA syntax in the underlying ASA core

**IOS-XR (optional, complex — lowest priority for v1).** IOS-XR is used on carrier-grade ASR 9000, NCS, and CRS series. It has a commit model similar to JunOS (candidate configuration that requires explicit commit), making it the most JunOS-like Cisco platform. Distinct syntax for everything. For a v1 model focused on enterprise use, IOS-XR coverage can be minimal; add in a v2 dataset iteration if the operator manages carrier-grade hardware.

**Training data allocation for Cisco model:**

| Platform | Competency | Examples Target |
|----------|------------|----------------|
| IOS/IOS-XE | Command translation | 2,000 |
| IOS/IOS-XE | Config generation | 3,500 |
| IOS/IOS-XE | Troubleshooting | 4,500 |
| IOS/IOS-XE | Output interpretation | 2,000 |
| NX-OS | Command translation | 1,000 |
| NX-OS | Config generation | 1,500 |
| NX-OS | Troubleshooting | 2,000 |
| ASA | Command translation + config + troubleshoot | 2,500 |
| Tool use (all platforms) | Ping/trace/ARP | 1,000 |
| Platform identification | When to ask vs. infer | 500 |
| **Total** | | **~20,500** |

**Platform tagging in training data.** Every example must explicitly label the platform in either the system prompt context or the conversation itself. Recommended approach: include a short platform line in each user turn for training data:

```json
{
  "messages": [
    {"role": "system", "content": "You are a senior Cisco network engineer..."},
    {"role": "user", "content": "[Platform: Cisco IOS-XE, Catalyst 9300]\nShow me all interfaces and their current state in a compact table"},
    {"role": "assistant", "content": "show interfaces status\n\nThis shows all interfaces with port, name, status, VLAN, duplex, speed, and type in a compact format. Example output on a Cat 9300:\n\nPort         Name       Status       Vlan       Duplex  Speed Type\nGi1/0/1      uplink-sw2 connected    trunk      a-full  a-1G  10/100/1000BaseTX\nGi1/0/2                 notconnect   1            auto   auto  10/100/1000BaseTX\n\nFor just down interfaces: show interfaces status | include err|notconn"}
  ]
}
```

**Cisco-specific troubleshooting scenarios to train.**

Each scenario must specify the platform — troubleshooting steps differ:

IOS/IOS-XE:
- BGP not coming up: `show ip bgp summary`, `show ip bgp neighbors <ip>` (look for `BGP state` and `Last reset`)
- OSPF adjacency stuck in INIT: `debug ip ospf adj` (carefully, on low-traffic link), `show ip ospf interface`
- STP issue: `show spanning-tree vlan <id>`, `show spanning-tree summary`, looking for TCN storms
- HSRP failover not working: `show standby brief`, check preempt settings
- NAT not translating: `show ip nat translations`, `show ip nat statistics`, checking `ip nat inside/outside` on interfaces

NX-OS:
- VPC peer link down: `show vpc`, `show vpc peer-keepalive` — peer-keepalive uses management interface, critical
- Port-channel not forming: `show port-channel summary`, `show lacp neighbor`
- VXLAN tunnel down: `show nve peers`, `show nve vni`, VTEP reachability

ASA:
- Traffic not passing: `packet-tracer input <interface> <proto> <src> <sport> <dst> <dport>` — the most valuable ASA diagnostic command
- NAT debugging: `show nat`, `show conn`, checking xlate table
- VPN tunnel down: `show crypto isakmp sa`, `show crypto ipsec sa`, checking phase 1/2 states

**Evaluation criteria for Cisco model.**

Critical failure modes to test for:
1. Does not use `ip` prefix in IOS routing commands (`show ip route`, `show ip bgp`, `show ip ospf`) — this would indicate JunOS contamination
2. Correctly identifies NX-OS `feature` prerequisites — never writes NX-OS config without checking if the feature is enabled
3. Does not confuse ASA NAT syntax with IOS NAT syntax (completely different)
4. Correctly handles the IOS-XE exec vs. global config mode context in commands
5. Knows `packet-tracer` is ASA-only, not available on IOS
6. Correctly identifies NX-OS vs. IOS output format differences in show commands

## Sources

- [Cisco IOS-XE Configuration Guide](https://www.cisco.com/c/en/us/support/docs/)
- [Cisco NX-OS Configuration Guides](https://www.cisco.com/c/en/us/support/switches/nexus-9000-series-switches/products-installation-and-configuration-guides-list.html)
- [Cisco ASA Configuration Guide](https://www.cisco.com/c/en/us/support/security/asa-5500-series-next-generation-firewalls/products-installation-and-configuration-guides-list.html)
- [Cisco DevNet](https://developer.cisco.com) — automation-focused documentation useful for training data
- [Cisco Community](https://community.cisco.com) — real troubleshooting threads with authentic device output
