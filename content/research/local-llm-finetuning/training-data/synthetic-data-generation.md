---
title: "Synthetic Training Data Generation"
date: 2026-06-11
lastmod: 2026-06-11
draft: false
description: "How to generate synthetic training data for a network engineer specialist model at scale — using a capable LLM as a data generator, writing effective generation prompts, estimating the domain expert review cost, and maintaining quality across large datasets."
tags: ["training-data", "synthetic-data", "data-generation", "llm", "network-engineering", "fine-tuning"]
categories: ["technology"]
research_area: "local-llm-finetuning/training-data"
source_urls:
  - "https://arxiv.org/abs/2212.10560"
last_reviewed: 2026-06-11
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Getting 10,000–20,000 high-quality network engineering training examples from real sources alone is not feasible for most individuals. Real troubleshooting session transcripts are scarce, vendor documentation examples cover only common cases, and manually writing training examples is slow. The practical path is to use a large capable model (GPT-4.1, Claude Sonnet 4.5, Llama 3.1 70B) as a data generator — seeding it with your requirements, generating at scale, then having a domain expert review and filter the output before it enters training. This section covers how to set up that pipeline, what makes a good generation prompt, how to estimate review effort, and how to catch systematic errors before they contaminate the training set.

## Key Facts

- **A large model generates; a small model trains** — use the most capable available LLM to generate data; train your specialist on the filtered output
- **Domain expert review is non-negotiable for CLI commands** — LLMs hallucinate plausible-but-wrong syntax; a network engineer can spot this at a glance
- **Estimate ~100–150 examples reviewed per hour** by a working network engineer
- **Generate diverse, not just voluminous** — 2,000 varied examples beat 10,000 near-duplicates
- **Reject, don't correct** — a corrected-but-uncertain example teaches the model the original wrong pattern too; discard it
- **Seed data matters** — the quality of your generation prompt directly caps the quality ceiling of the output

---

## The Generation Architecture

The pipeline has three stages: generation, review, and ingest.

```
[Seed templates + generation prompt]
         ↓
[Large LLM: GPT-4.1 / Claude Sonnet 4.5 / Llama 3.1 70B]
         ↓
[Raw synthetic examples: JSONL batches of 50–100]
         ↓
[Domain expert review: accept / reject / flag for rewrite]
         ↓
[Validated dataset: deduplicated, split train/eval]
         ↓
[Fine-tuning run]
```

The critical insight is that the large generator model doesn't need to be the model you're fine-tuning — in fact it shouldn't be. You're using its broader knowledge and instruction-following capability to create data that teaches a smaller model to specialize. GPT-4.1 generating 10,000 JunOS training examples, reviewed and filtered to 8,000 by a network engineer, then used to fine-tune Llama 3.1 8B, is a form of knowledge distillation — you're extracting the large model's network engineering knowledge into a smaller, faster, offline model.

---

## Writing Effective Generation Prompts

The generation prompt is a meta-instruction to the large LLM: "generate N training examples that look like this." The quality ceiling of your dataset is determined by how well this prompt specifies what you want. A weak generation prompt produces fluent but repetitive or inaccurate examples; a strong one produces diverse, syntactically accurate, well-structured examples.

**Structure of a good generation prompt:**

```
You are creating training data for a Juniper JunOS specialist AI assistant.

Generate {N} training examples as a JSON array. Each example must follow this exact format:
{
  "messages": [
    {"role": "system", "content": "<SYSTEM_PROMPT>"},
    {"role": "user", "content": "<user question or request>"},
    {"role": "assistant", "content": "<ideal expert response>"}
  ],
  "competency": "<command_translation|config_generation|troubleshooting|interpretation|tool_use>",
  "platform": "junos",
  "difficulty": "<basic|intermediate|advanced>"
}

Target competency: {COMPETENCY}
Target difficulty distribution: 40% basic, 40% intermediate, 20% advanced
Target topics to cover (generate examples across all of these, not just the first):
{TOPIC_LIST}

Requirements for responses:
- All JunOS commands must be syntactically correct for JunOS 21.x and later
- Commands must appear in fenced code blocks with the "junos" language tag
- Troubleshooting responses must propose a diagnostic command before interpreting output
- Configuration examples must include brief commentary noting any prerequisite config
- Avoid repeating the same command in multiple examples — vary the scenarios

Here are two examples of high-quality outputs:
{FEW_SHOT_EXAMPLES}

Generate the examples now as valid JSON.
```

**Key elements:**

*Topic lists prevent clustering.* Without an explicit topic list, the generator will weight toward common topics and underrepresent edge cases. For JunOS command translation, specify the full coverage list explicitly: OSPF, BGP, IS-IS, static routes, interfaces, VLANs, firewall filters, NAT, QoS, system, spanning tree. The generator will then distribute examples across topics proportionally.

*Difficulty distribution matters.* 40/40/20 basic/intermediate/advanced matches realistic usage: most queries are about standard operations, some are complex, a few involve deep edge cases. A dataset that's 80% basic produces a model that handles common queries well but fails on less common ones.

*Language tag in code blocks.* Specifying `junos` as the language tag in the generation prompt means the model will include it in generated examples — and since you're also using it as the system prompt format specification during fine-tuning, the training data will be consistent with the deployment format.

*Explicit prohibitions on repetition.* Without this, generators will produce many variations of the same 5–10 most common commands. The instruction to avoid repeating commands shifts the distribution toward broader coverage.

---

## Competency-Specific Generation Prompts

Each competency area needs a different topic list and different example requirements.

### Command translation

Topic list to include verbatim in the generation prompt:

```
Topics (generate examples across ALL of these):
Routing protocols: show ospf neighbor, show ospf route, show ospf interface detail,
  show bgp summary, show bgp neighbor X.X.X.X, show route, show route protocol bgp,
  show isis adjacency, show isis route
Interface operations: show interfaces terse, show interfaces ge-0/0/0 detail,
  show interfaces queue, show interfaces statistics, show lacp interfaces
Switching: show ethernet-switching table, show spanning-tree bridge, show lldp neighbors,
  show vlan, show vlans extensive
Security: show firewall, show security policies, show security nat source summary,
  show security ike security-associations, show security ipsec security-associations
System: show system uptime, show system processes, show chassis hardware,
  show chassis alarms, show version, show log messages
BGP: show bgp summary, show route receive-protocol bgp, show route advertising-protocol bgp,
  show bgp group, show bgp neighbor X.X.X.X advertised-routes
```

### Troubleshooting dialogs

For multi-turn dialogs, provide a scenario seed list rather than a topic list:

```
Generate {N} multi-turn troubleshooting dialogs. Each dialog must:
- Start with a symptom description (not a diagnosis)
- Have 3–5 turns minimum
- Include realistic JunOS show command output (not placeholder text)
- Reach a specific conclusion: identified root cause, or clear next steps

Scenario seeds (generate dialogs for varied scenarios across this list):
- BGP peer stuck in Active state
- OSPF neighbor not forming (various causes: MTU, auth, area type, timer mismatch)
- Route not being redistributed into BGP
- Interface flapping (with log output showing the events)
- Firewall filter blocking unexpected traffic
- VLAN not passing traffic between access ports
- IPsec tunnel down (phase 1 vs phase 2 failures)
- Duplicate IP address causing intermittent connectivity
- STP topology change causing brief outage
- High CPU on routing engine (different causes)
- QoS not classifying traffic correctly
```

**Critical for troubleshooting generation:** explicitly require realistic show command output. LLMs tend to abbreviate or simplify show output unless instructed otherwise. Include in the prompt:

```
IMPORTANT: Show command output in user turns must be:
- Syntactically correct JunOS output format (correct field names, column widths, indentation)
- Contain realistic counter values (not all zeros, not round numbers like 1000)
- Show the specific anomaly being diagnosed (e.g., if the scenario is "dead timer expiry",
  the log output must show the dead timer expired message in correct JunOS log format)
```

### Configuration generation

```
Generate {N} configuration generation examples. Each must:
- Start with a plain-English description of the network requirement (not a command request)
- Provide both set-format and hierarchical format where applicable
- Include brief commentary on prerequisites or dependencies
- Cover varied scenarios from this list:
  BGP peering (eBGP and iBGP), OSPF area configuration, interface IP assignment and
  subinterfaces, VLAN configuration on EX switches, firewall filter with multiple terms,
  NAT source and static NAT, IPsec IKEv2 VPN, QoS class-of-service configuration,
  LACP port aggregation, VRRP redundancy, routing policy with match conditions and actions,
  route reflection, BGP communities, IS-IS configuration
```

---

## Estimating Review Effort

For a 10,000-example dataset:

| Competency | Examples | Review rate | Hours |
|-----------|---------|------------|-------|
| Command translation | 2,500 | 150/hr | 17 |
| Config generation | 4,000 | 80/hr | 50 |
| Troubleshooting | 2,500 | 50/hr | 50 |
| Output interpretation | 750 | 120/hr | 6 |
| Tool use | 250 | 150/hr | 2 |
| **Total** | 10,000 | | **~125 hours** |

Troubleshooting dialogs take longest to review because each turn must be checked: is the command right? Is the show output realistic? Is the diagnosis correct? Config generation is slower than command translation for the same reason — a config block has many lines, each of which can be wrong.

**Reducing review cost:** Run an automated pre-filter before human review. A second LLM call asking "does this example contain any JunOS command errors? Respond yes/no with confidence" can flag the bottom 20–30% of generated examples for automatic rejection, reducing human review volume. Don't use the same model that generated the data — it will tend to validate its own output.

---

## Common Generation Failures

**Hallucinated command options.** LLMs frequently generate `show ospf neighbor detail all` (no such option) or `set interfaces ge-0/0/0 link-mode full-duplex` (wrong keyword — should be `full-duplex` under `ether-options`, not `link-mode`). These pass a casual read but fail on a device. Reviewers should mentally execute each command.

**Simplified show output.** The generator uses placeholder-style output: `show ospf neighbor` output with exactly two neighbors, counters all at zero, state always Full. Real output has messy counters, varied states, and formatting quirks specific to the platform version. Add a few real captured show outputs as examples in your generation prompt to improve realism.

**Scope creep to Cisco.** When asking for troubleshooting scenarios, LLMs often drift toward IOS syntax mid-dialog, especially for protocols where Cisco is more commonly represented in training data (BGP, for instance). Add an explicit instruction: "Every command in this dialog must be JunOS syntax. If you find yourself writing `show ip route`, stop and rewrite as JunOS."

**Over-hedging.** Generated examples include qualifications like "Note: Exact syntax may vary by JunOS version" on nearly every response. This is appropriate occasionally but if it appears in every training example, the fine-tuned model will hedge constantly — including on questions where a network engineer would answer directly. Add to the generation prompt: "Do not include disclaimers about version differences unless the specific command actually changed significantly between versions."

**Repetitive structure.** The first 50 generated troubleshooting examples all follow the same 3-turn pattern: symptom → one command → diagnosis. Real troubleshooting requires more turns with more back-and-forth. Specify: "Dialogs must be 3–8 turns. At least 30% should require 5 or more turns to reach resolution."

---

## Deduplication

A 10,000-example dataset generated in batches will contain near-duplicates. An example for "show BGP summary" and an example for "show me the BGP neighbor table" may produce nearly identical assistant responses — the model learns redundantly from both. Deduplication before training reduces effective dataset size but improves training efficiency.

```python
from sentence_transformers import SentenceTransformer
import numpy as np

def deduplicate_examples(examples: list, threshold: float = 0.95) -> list:
    """Remove near-duplicate examples based on user prompt similarity."""
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    # Embed all user prompts
    prompts = [ex["messages"][1]["content"] for ex in examples]
    embeddings = model.encode(prompts, normalize_embeddings=True)
    
    # Greedy deduplication: keep an example if its max similarity to any 
    # already-kept example is below threshold
    kept_indices = [0]
    kept_embeddings = [embeddings[0]]
    
    for i in range(1, len(embeddings)):
        similarities = np.dot(kept_embeddings, embeddings[i])
        if similarities.max() < threshold:
            kept_indices.append(i)
            kept_embeddings.append(embeddings[i])
    
    print(f"Kept {len(kept_indices)}/{len(examples)} examples after deduplication")
    return [examples[i] for i in kept_indices]
```

Run deduplication per competency area, not across the whole dataset — you don't want to remove a command translation example because a similar prompt appeared in a troubleshooting dialog.

---

## Sources

- [Self-Instruct: Aligning Language Models with Self-Generated Instructions (Wang et al. 2022)](https://arxiv.org/abs/2212.10560) — foundational paper on using LLMs to generate their own training data
