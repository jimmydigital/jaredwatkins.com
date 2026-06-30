---
title: "Network Engineering Training Data"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "The specific categories, sources, and volume of training data needed to produce a credible network-engineer expert model for Juniper and Cisco devices — covering command generation, configuration, troubleshooting, and tool interpretation."
research_area: "local-llm-finetuning/training-data"
source_urls:
  - "https://www.juniper.net/documentation/"
  - "https://www.cisco.com/c/en/us/support/docs/"
  - "https://networktocode.com/"
  - "https://github.com/networktocode/ntc-templates"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Building a network-engineer expert model requires training data that covers five distinct competency areas: command translation (English → device command), configuration generation, troubleshooting dialog, show-command output interpretation, and tool use (ping, traceroute, ARP). Each area requires different data sourcing and formatting approaches. The Juniper and Cisco models should be trained separately due to CLI syntax incompatibility — mixing JunOS and IOS examples in one model produces confused output.

## Key Facts

- **Two separate models:** Juniper (JunOS) and Cisco (IOS/IOS-XE/NX-OS/ASA) should not be mixed
- **Target dataset size:** 10,000–20,000 examples per model for strong performance
- **Primary data sources:** Vendor documentation, public configs, synthetic generation, real-world session transcripts
- **Critical quality requirement:** Commands must be syntactically exact — one wrong character in a CLI command is a completely wrong answer
- **Hardest competency to train:** Multi-step troubleshooting that requires interpreting realistic show command output

## The Five Competency Areas

### 1. Command Translation (English → CLI)

The most basic competency: converting a plain-English description of what the engineer wants to see or do into the correct device command.

**What good examples look like:**

```json
{
  "messages": [
    {"role": "system", "content": "You are an expert Juniper network engineer..."},
    {"role": "user", "content": "Show me all OSPF neighbors and their adjacency state"},
    {"role": "assistant", "content": "show ospf neighbor\n\nFor detailed information including interface and area:\nshow ospf neighbor detail\n\nFor a specific router ID:\nshow ospf neighbor 10.0.0.1"}
  ]
}
```

**For Cisco IOS/IOS-XE:**
```json
{
  "messages": [
    {"role": "system", "content": "You are an expert Cisco network engineer..."},
    {"role": "user", "content": "Show me all OSPF neighbors and their adjacency state"},
    {"role": "assistant", "content": "show ip ospf neighbor\n\nFor detailed output:\nshow ip ospf neighbor detail\n\nNote: On NX-OS the command is:\nshow ip ospf neighbors"}
  ]
}
```

**Coverage needed for command translation:**
- All `show` commands for routing protocols: OSPF, BGP, IS-IS, EIGRP (Cisco), static routes
- Interface show commands: physical status, counters, errors, queue stats
- VLAN and switching: show vlan, show mac-address-table, spanning tree status
- Security: show firewall (JunOS), show access-list (IOS), show security policy (SRX/ASA)
- System: show system information, CPU/memory utilization, logging, processes
- Configuration display: show configuration (JunOS), show running-config (IOS)

**Data sourcing for command translation:** Vendor documentation command references are the primary source. Juniper's TechLibrary and Cisco's documentation are comprehensive and authoritative. These can be semi-automatically converted: extract the command syntax and description, then rewrite the description into a natural-language question. Target: 2,000–3,000 command translation examples per model.

---

### 2. Configuration Generation

Translating a network design or requirement into a complete, deployable device configuration block.

**What good examples look like:**

```json
{
  "messages": [
    {"role": "system", "content": "You are an expert Juniper network engineer..."},
    {"role": "user", "content": "Configure a new BGP peer. The peer IP is 192.0.2.1, AS 65001. We're AS 65000. Set the description to 'upstream-provider'. Apply an import policy called 'bgp-import-upstream'."},
    {"role": "assistant", "content": "Here is the JunOS configuration for this BGP peer:\n\n```\nset protocols bgp group external-peers type external\nset protocols bgp group external-peers neighbor 192.0.2.1 description upstream-provider\nset protocols bgp group external-peers neighbor 192.0.2.1 peer-as 65001\nset protocols bgp group external-peers neighbor 192.0.2.1 import bgp-import-upstream\n```\n\nOr in hierarchical form (for a config file or `load merge`):\n\n```\nprotocols {\n    bgp {\n        group external-peers {\n            type external;\n            neighbor 192.0.2.1 {\n                description upstream-provider;\n                peer-as 65001;\n                import bgp-import-upstream;\n            }\n        }\n    }\n}\n```\n\nNote: You'll need a separate `local-as 65000` statement in the BGP group if not already set globally. Also ensure the import policy `bgp-import-upstream` is defined under `policy-options`."}
  ]
}
```

**Coverage needed for configuration generation:**
- BGP: eBGP/iBGP peering, route reflectors, communities, policy attachment
- OSPF: area configuration, interface cost, authentication, stub areas
- VLANs and L2: trunk/access port configuration, STP parameters, LACP/port-channel
- ACLs and firewall filters: JunOS firewall filters vs. Cisco ACLs and ASA ACL syntax
- NAT: static NAT, PAT/masquerade, one-to-many
- QoS: queuing, marking, policing (JunOS CoS vs. Cisco MQC — very different syntax)
- Interface configuration: IP assignment, MTU, duplex/speed, subinterfaces
- VPN: GRE, IPsec (IKEv2 parameters differ significantly between JunOS and IOS)

**Device-specific coverage for Cisco:**
- IOS vs. IOS-XE: most commands identical, some differences in crypto, VRF syntax
- NX-OS: Nexus switches — meaningfully different (feature commands, VPC, FEX)
- ASA: firewall-specific syntax entirely different from IOS; object groups, nat, access-group
- IOS-XR: carrier-grade, different from all others; commit model similar to JunOS

**Data sourcing for configuration:** Public configuration examples from GitHub (network automation repos, Ansible playbooks with Jinja2 templates), NetworkToCode's NTC-Templates, vendor configuration guides, and real-world sanitized configs shared in the network engineering community (Reddit r/networking, Network Chuck, PacketLife). Synthetic generation using GPT-4/Claude to create varied config examples from a seed template is effective for scale. Target: 3,000–5,000 configuration examples per model.

---

### 3. Troubleshooting Dialogs

Multi-turn conversations where the model helps diagnose and resolve a network problem step by step. This is the hardest and most valuable competency to train — and the most time-consuming to generate well.

**The troubleshooting data structure.** Each example is a realistic back-and-forth session:
1. User describes a symptom (not a diagnosis — the model must derive the diagnosis)
2. Model proposes first diagnostic step with the correct command
3. User pastes realistic `show` command output
4. Model interprets the output and identifies the likely cause or next step
5. Repeat until resolution or actionable next steps identified

**Critical requirement: realistic show command output.** The output in step 3 must be syntactically accurate — correct field names, correct indentation, realistic counter values, correct state labels. A model trained on fake or hallucinated show output will learn to interpret fake output, not real output. Sources for realistic output: vendor documentation examples, GitHub repositories with captured network states, the Juniper and Cisco community wikis, and — most valuable — real captured troubleshooting sessions.

**Example troubleshooting dialog (Juniper OSPF):**

```
User: Our OSPF adjacency to 10.10.10.2 dropped about 20 minutes ago. 
      How do I figure out what happened?

Model: Start with the current neighbor state:
       show ospf neighbor 10.10.10.2
       
       If it's not showing, check the interface:
       show ospf interface ge-0/0/0.0
       (replace with your interface to that peer)
       
       Also pull the recent system log for OSPF events:
       show log messages | match OSPF | last 50
       
       What do you see?

User: show ospf neighbor 10.10.10.2 — no output at all. 
      show ospf interface ge-0/0/1.0 shows:
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/1.0          DR      0.0.0.0         10.10.10.1      0.0.0.0          0

Model: The interface is up in OSPF (DR state), but zero neighbors — 
       so the adjacency is completely gone, not just stuck in init/2-way.
       
       The log should tell us why. Show me the output of:
       show log messages | match OSPF | last 100
       
       Also check if the peer is even reachable at L3:
       ping 10.10.10.2 routing-instance default count 5
       
       And check interface physical status:
       show interfaces ge-0/0/1.0 terse

User: Log shows: 
      Jun 10 14:23:41 router1 rpd[1234]: OSPF neighbor 10.10.10.2 
        (ge-0/0/1.0 area 0.0.0.0) state changed from Full to Down 
        due to: Dead timer expired
      Ping is working — 0 packet loss. Interface is up/up.

Model: The dead timer expiry means your router stopped receiving Hello 
       packets from 10.10.10.2 for the full dead interval (typically 40s 
       for point-to-point, or 4x the hello interval).
       
       Since ping is working (L3 reachability is fine), this is almost 
       certainly one of:
       
       1. Hello/Dead timer mismatch — the peer changed its timers and 
          they no longer match yours
       2. Authentication mismatch — if OSPF MD5 auth is configured, a 
          key change on one side drops hellos
       3. Area type mismatch — one side changed stub/NSSA settings
       
       Check your local timers:
       show ospf interface ge-0/0/1.0 detail
       
       Look at the 'Hello interval' and 'Dead interval' fields. If you 
       can access the peer router, run the same command there. 
       Mismatched values prevent adjacency formation.
       
       Also check:
       show ospf interface ge-0/0/1.0 detail | match auth
```

**Troubleshooting scenarios to cover:**
- Routing: BGP session not coming up (various causes), OSPF adjacency failure, route not in table, black holes, asymmetric routing
- Switching: Port not forwarding (STP, LACP, VLAN mismatch), MAC flapping, broadcast storms
- Connectivity: Host can't reach gateway, intermittent packet loss, MTU/fragmentation issues
- Firewall: Policy blocking traffic, NAT not working, VPN tunnel down
- Physical: Interface errors (CRC, input errors, output drops), transceiver issues, duplex mismatch
- Performance: High CPU on routing engine, queue drops, QoS not classifying correctly

**Data sourcing for troubleshooting:** This is the hardest data to source at quality. Best options:
- Real session transcripts with a network engineer (the most valuable; anonymize IPs/hostnames)
- NetworkToCode Slack community logs (with permission)
- Reddit r/networking and r/homelab threads where users post real show output and get expert advice
- Vendor technical assistance center (TAC) case examples (some are publicly documented)
- Synthetic generation with GPT-4/Claude, heavily reviewed by a network engineer
- PacketLife.net, JNCIE study guide forums

Target: 4,000–8,000 multi-turn troubleshooting examples per model. This is where most of the data curation effort goes.

---

### 4. Show Command Output Interpretation

Standalone examples where the model is given a block of show command output and asked to interpret it — without the full troubleshooting conversation context.

**Example:**

```json
{
  "messages": [
    {"role": "system", "content": "You are an expert Cisco network engineer..."},
    {"role": "user", "content": "What does this BGP summary output tell me?\n\nRouter#show ip bgp summary\nBGP router identifier 10.0.0.1, local AS number 65000\nBGP table version is 342, main routing table version 342\n42 network entries using 9744 bytes of memory\n\nNeighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd\n192.168.1.2     4        65001    8432    8428      342    0    0 5d23h       38\n10.10.10.2      4        65002    1203     987      342    0    0 02:14:33     0\n172.16.0.1      4        65003       0       0        0    0    0 never    Active"},
    {"role": "assistant", "content": "This BGP summary shows three configured peers:\n\n**192.168.1.2 (AS 65001)** — Healthy. Session up for ~6 days, 38 prefixes received. No queue backlog.\n\n**10.10.10.2 (AS 65002)** — Up for 2 hours 14 minutes, but receiving 0 prefixes. The session is established (no error state) but the peer is sending nothing. Possible causes: the peer has an outbound policy filtering all routes to you, the peer has no routes matching your inbound filter, or the peer's BGP table is empty. Check with: `show ip bgp neighbors 10.10.10.2 received-routes` to see what they're sending before your import policy.\n\n**172.16.0.1 (AS 65003)** — Never established (Up/Down: never, State: Active). BGP is actively trying to open the session but failing. 0 messages sent/received. Check: Is 172.16.0.1 reachable? Is the peer configured with your router's IP and AS? Is TCP 179 permitted by any ACL? Run: `show ip bgp neighbors 172.16.0.1` for the specific error state and last reset reason."}
  ]
}
```

**Coverage:** One interpretation example per major show command type. 1,000–2,000 examples. This data is relatively fast to generate because you're starting with realistic output templates (from documentation or captured output) and writing the interpretation.

---

### 5. Network Tool Use and Interpretation

Ping, traceroute, ARP, and other standard tools — correct invocation syntax and interpretation of results.

**Example — traceroute interpretation:**

```json
{
  "messages": [
    {"role": "system", "content": "You are an expert Juniper network engineer..."},
    {"role": "user", "content": "What does this traceroute tell me?\n\ntraceroute to 8.8.8.8 from 10.0.1.1\n 1  10.0.1.254  1.2 ms  1.1 ms  1.1 ms\n 2  192.168.100.1  3.4 ms  3.5 ms  3.4 ms\n 3  * * *\n 4  * * *\n 5  72.14.215.198  15.2 ms  15.1 ms  15.2 ms\n 6  8.8.8.8  16.4 ms  16.3 ms  16.3 ms"},
    {"role": "assistant", "content": "The path to 8.8.8.8 is working — you reach it in 6 hops at ~16ms. \n\nHops 3 and 4 show `* * *` (no ICMP TTL-exceeded responses). This is normal — many transit routers are configured to rate-limit or not reply to traceroute probes for the router's own interface (ICMP unreachable deprioritized). It does NOT indicate packet loss since hop 5 responds and hop 6 (the destination) responds. If the destination itself were unreachable, you'd see `* * *` continuing to the end.\n\nPath summary:\n- Hop 1: 10.0.1.254 — your default gateway (1ms, on-LAN)\n- Hop 2: 192.168.100.1 — your ISP or upstream router\n- Hops 3-4: Silent transit routers (normal)\n- Hop 5: Google's edge router (72.14.x is Google's network)\n- Hop 6: 8.8.8.8 — destination reached\n\nIf you were troubleshooting a connectivity issue, the fact that hops 3-4 are silent is not the problem — hops 1, 2, 5, 6 all respond, confirming end-to-end path is intact."}
  ]
}
```

**Tool syntax coverage (per platform):**
- `ping` — basic syntax, extended ping options (IOS), count/size/source parameters (JunOS vs IOS differ)
- `traceroute` — JunOS uses `traceroute`; Cisco IOS uses `traceroute` for IP, extended traceroute for source/VRF
- `show arp` / `show arp table` — ARP table inspection, detecting stale or incorrect entries
- `show route` / `show ip route` — routing table examination, longest-prefix match
- Interpreting MTU problems in ping (using `do-not-fragment` bit and varying packet sizes)
- Interpreting packet loss patterns (consistent vs. random, directional)

**Target:** 500–1,000 tool use examples per model.

---

## Data Sourcing Summary

| Data Type | Primary Sources | Synthetic? | Examples per Model |
|-----------|----------------|------------|-------------------|
| Command translation | Vendor docs, NTC-Templates | OK for augmentation | 2,000–3,000 |
| Config generation | GitHub, vendor guides, NTC | Yes, with review | 3,000–5,000 |
| Troubleshooting dialogs | Real sessions, Reddit, TAC docs | Yes, heavily reviewed | 4,000–8,000 |
| Output interpretation | Vendor docs, captured output | Yes | 1,000–2,000 |
| Tool use | Vendor docs, lab captures | Yes | 500–1,000 |
| **Total** | | | **~10,000–19,000** |

## Synthetic Data Generation Workflow

For data types where real-world examples are scarce, synthetic generation with GPT-4 or Claude 3.5/3.7 Sonnet is effective — with mandatory review by a practicing network engineer. Workflow:

1. Write a detailed generation prompt specifying the target competency, platform (JunOS or IOS), required output format, and examples of good vs. bad outputs
2. Generate in batches of 50–100 examples
3. Have a network engineer review for: command accuracy, realistic output formatting, and whether the troubleshooting logic is correct
4. Discard any example with a command error — do not correct and keep; the model learns from errors too
5. Track rejected examples to identify gaps in your generation prompt

An experienced network engineer can review approximately 100–150 examples per hour for accuracy. Budget 50–100 hours of domain expert review for a 10,000-example dataset — this is the main human cost in the data pipeline.

## Key Quality Checks Before Training

- Run every command in your training data through a JunOS or IOS syntax validator or actual device/simulator if possible
- Check that JunOS and IOS examples are not mixed in either dataset
- Verify show command output formats match actual device output (field names, whitespace, order)
- Confirm the system prompt is consistent across all examples
- Hold out a stratified 10% test set before training (ensure test set covers all five competency areas)
- Check for near-duplicate examples (very similar commands with slightly different parameters) — these cause overfitting

## Sources

- [Juniper TechLibrary](https://www.juniper.net/documentation/) — authoritative JunOS command reference
- [Cisco Documentation](https://www.cisco.com/c/en/us/support/docs/) — IOS/IOS-XE/NX-OS/ASA references
- [NTC-Templates](https://github.com/networktocode/ntc-templates) — TextFSM templates with realistic show command output formats
- [PacketLife Cheat Sheets](https://packetlife.net/library/cheat-sheets/) — quick command reference widely used in training
- [r/networking](https://www.reddit.com/r/networking/) — real troubleshooting threads with authentic show output
- [NANOG mailing list archives](https://www.nanog.org/archives/) — real-world network engineering discussions
