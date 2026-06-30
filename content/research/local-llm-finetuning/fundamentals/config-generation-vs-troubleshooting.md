---
title: "Config Generation vs. Troubleshooting: Two Different Models"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "Configuration generation and troubleshooting are fundamentally different tasks with different training data requirements, different interaction patterns, and different quality criteria — and may be better served by two separate fine-tuned models than one."
research_area: "local-llm-finetuning/fundamentals"
source_urls:
  - "https://www.juniper.net/documentation/"
  - "https://www.cisco.com/c/en/us/support/docs/"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Configuration generation and network troubleshooting look like the same domain — both require deep knowledge of JunOS or IOS — but they are fundamentally different tasks at the model level. Config generation is a deterministic translation problem: given a precise outcome description, produce complete, correct, deployable configuration. Troubleshooting is a stochastic reasoning problem: given incomplete and ambiguous symptom information, navigate a diagnostic space toward a root cause. They require different training data shapes, different interaction patterns, different evaluation criteria, and different failure modes. Building one model to do both well is harder than building two focused models.

## Key Facts

- **Config generation:** Input = desired outcome; output = complete, syntactically exact config block; one right answer
- **Troubleshooting:** Input = symptom description + device output; output = next diagnostic step or hypothesis; many valid paths
- **Training data divergence:** Config training is largely static (outcome → config pairs); troubleshooting training requires multi-turn dialog with realistic device output
- **Interaction pattern divergence:** Config generation may need to *ask clarifying questions* before generating; troubleshooting needs to *interpret partial information* and propose next steps
- **Quality divergence:** Config generation fails silently if a command is wrong; troubleshooting fails loudly if the reasoning is wrong
- **Practical recommendation:** Two separate fine-tuned adapters (LoRA), swapped at runtime based on task type, or a single model with a strong task-framing system prompt

---

## Configuration Generation

### What it actually is

Config generation is closer to a **compiler** than to an assistant. The user describes an outcome in English — "add a site-to-site IPsec VPN to peer 203.0.113.5, IKEv2, pre-shared key authentication" — and the model must produce complete, correct, immediately deployable device configuration. No ambiguity is acceptable: a transposed command, a missing `commit`, or the wrong hierarchy level renders the output useless or destructive.

This includes several sub-tasks with distinct characteristics:

**Greenfield / zero-state build:** Start from factory defaults and build complete configuration to achieve a described outcome. "Configure this MX104 as a BGP route reflector for 6 clients in AS 65000. Clients are on loopback addresses 10.0.0.1–10.0.0.6. Use MD5 authentication with key 'rr-secret'." The model must produce the full configuration hierarchy — no assumption about what's already there.

**Incremental addition:** Existing device, add a specific new capability. "Add a new OSPF area 10 on ge-0/0/2.0 as a stub area. Don't touch the existing area 0 config." The model must produce only the additive delta — set-format commands for JunOS, or a targeted config block for IOS — without disturbing what's already there.

**Parameterized templates:** The user knows roughly what they want but needs to fill in specifics. "Add a site-to-site IPsec VPN" — but what's the pre-shared key? What encryption suite? What traffic to protect? This sub-task requires the model to **prompt for parameters before generating** rather than generating immediately.

**Translation:** "Convert this IOS BGP config to JunOS equivalent." Syntactically and semantically correct translation between CLI dialects.

### The parameterized interaction pattern

Parameterized config generation is particularly important and distinct: the model should *not* generate a complete config with placeholder values like `<PSK_HERE>`. It should identify all required parameters, ask for them, and only generate the final config once it has complete information.

This requires training data that explicitly models this interaction:

```
User: Add a site-to-site IKEv2 IPsec VPN to our new branch office.

Model: I'll generate the complete IKEv2 VPN configuration. Before I do, 
       I need a few parameters:

       1. Peer IP address (the branch office's public IP)?
       2. Pre-shared key? (Will not be logged or stored)
       3. Traffic to protect — local subnet(s) and remote subnet(s)?
       4. IKEv2 proposal — or should I use a standard strong default 
          (AES-256-GCM, SHA-384, DH group 20)?
       5. Is this replacing an existing VPN or a new addition?

User: Peer is 203.0.113.45. PSK is [user provides key]. 
      Protect 10.10.0.0/24 local to 192.168.5.0/24 remote.
      Use strong defaults. New addition.

Model: Here is the complete JunOS configuration for this IKEv2 VPN:
       [complete config block follows]
```

Training data for this pattern must include the question-gathering turn — models that skip directly to generating a config with placeholder PSKs are a security risk (they may log the placeholder in ways that suggest the pattern, train users to paste keys into prompts indiscriminately, or produce non-functional configs).

### Training data for config generation

Config generation training is primarily **single-outcome, complete-config pairs**. The conversation is often just two turns: the request and the complete config. What makes it hard is not the interaction complexity but the *precision requirement* — every command must be exactly right.

**Data characteristics:**
- High density of syntactically correct, complete config blocks
- Both JunOS set-format and hierarchical format represented
- Parameterized examples that model the question-gathering interaction
- Coverage of the full configuration surface: routing protocols, VLANs, ACLs, NAT, VPN, QoS, security policies, interface configuration, system parameters
- Platform specificity: the same outcome configured on EX Series vs. QFX vs. MX vs. SRX has different commands even though they all run JunOS

**What's *not* needed:** Long multi-turn reasoning chains. Show command output. Diagnostic interpretation. The model doesn't need to explain *why* a config works — it needs to produce configs that *are* correct.

**Synthetic generation is highly effective here.** A parametric template approach works well: define the outcome space (BGP peering configurations, OSPF area designs, VPN types, VLAN layouts, etc.), parameterize each template (AS numbers, IP addresses, interface names, key material), and generate thousands of valid combinations. A network engineer reviews a sample for correctness rather than reading every example. This is the one area where volume matters more than diversity of source — 10,000 syntactically verified config examples are better than 2,000 varied but unverified ones.

**Validation is the critical quality gate.** Every config example in the training data should be validated against a real device or a validated simulator (GNS3, Juniper vLab, Cisco CML). A wrong config in training teaches the model to produce wrong configs. This is the biggest practical obstacle to building a high-quality config generation dataset — it requires either device access or a validated simulation environment for every training example.

---

## Troubleshooting

### What it actually is

Troubleshooting is fundamentally different: it is **reasoning under uncertainty** toward a diagnosis. The user starts with a symptom, not a complete specification. The model doesn't know what's wrong — neither does the user. The interaction is investigative: propose a diagnostic step, interpret the results, update the hypothesis, propose the next step.

This is closer to a **detective** than a compiler. The model must:
- Maintain a mental model of what's broken based on incomplete evidence
- Prioritize diagnostic steps by information value (what will this tell us that we don't already know?)
- Interpret show command output, log excerpts, and counter values — often ambiguous, often incomplete
- Distinguish between symptoms and causes
- Know when it has enough evidence to commit to a diagnosis vs. when more information is needed
- Recognize patterns: "input errors climbing while output is clean and the interface is a fiber uplink — this is almost certainly a bad SFP or dirty fiber, not a config issue"

### The interaction pattern is intrinsically multi-turn

A troubleshooting session cannot be collapsed to a single turn without destroying the value. The sequential nature — propose, observe, interpret, propose again — is not an implementation detail; it is the essence of the task. Training data that flattens this into "describe the problem → here's the solution" produces a model that guesses at root causes without evidence, which is worse than useless on a production network.

The model must also know what it doesn't know. A good troubleshooting model says "I need to see the output of `show ospf interface ge-0/0/1.0 detail` before I can determine whether this is a timer mismatch or an authentication issue" — not "it's probably a timer mismatch, run this fix." Premature diagnosis on a production network is a service-affecting risk.

### Training data for troubleshooting

Troubleshooting training data has fundamentally different requirements than config generation:

**Realistic show command output is non-negotiable.** The model learns to interpret output by seeing thousands of examples. If the output in training data has wrong field names, wrong indentation, or implausible counter values, the model learns to interpret fake output — which means it misinterprets real output. The Juniper `show bgp summary` output format, the specific field ordering in `show interfaces detail`, the exact wording of `show log messages` OSPF events — these must be exactly right.

**Multi-turn dialog structure is required.** The training example is not "symptom → diagnosis." It is: symptom → diagnostic question + command → realistic device output → interpretation + next question → more output → narrowing → root cause + remediation. Each turn builds on the previous. Collapsing these into single-turn examples produces a model that cannot actually troubleshoot — it can only pattern-match symptoms to common solutions.

**Symptom descriptions must be realistic.** Engineers don't describe problems in complete technical language. They say "users are complaining the VPN keeps dropping" not "the IKEv2 SA lifetime is misconfigured causing phase 2 renegotiation failures." The model must start from the vague user description and drive toward the technical diagnosis through questioning.

**Negative examples matter.** Training should include cases where the initial hypothesis was wrong and the model corrected course after seeing disconfirming evidence. A model that never changes its hypothesis in training will stubbornly stick to wrong diagnoses in deployment.

**Volume and diversity over synthetic precision.** Unlike config generation, troubleshooting training benefits more from diverse real-world scenarios than from synthetically generated perfect examples. A real-world troubleshooting transcript from Reddit, a TAC case summary, or a Packet Pushers podcast discussion that walks through a real problem is worth more than a synthetic example — because real problems have the irregular, incomplete, sometimes-misleading quality that the model needs to learn to handle.

---

## The Case for Two Separate Adapters

Given the divergent training data requirements, the argument for training two separate LoRA adapters (one for config generation, one for troubleshooting) and loading them separately at runtime is strong:

**Training data can be optimized per task.** The config generation adapter trains on dense, syntactically precise, mostly single-turn examples. The troubleshooting adapter trains on multi-turn, ambiguous, symptom-led dialogs with realistic device output. Mixing them in one training run forces the model to serve both patterns from the same weights — which may mean neither is optimally served.

**System prompts can be fully specialized.** The config generation persona is precise and methodical — ask for all parameters before generating, produce complete configs, validate your own output. The troubleshooting persona is investigative and cautious — propose one step at a time, never diagnose without evidence, ask before touching anything. These personas conflict if merged.

**Evaluation criteria are cleanly separated.** Config generation quality is measured by: syntactic correctness, semantic correctness (does it do what was asked), completeness, no extraneous commands. Troubleshooting quality is measured by: correct diagnostic step selection, correct output interpretation, appropriate hypothesis updating, correct identification of root cause. Running separate evals against separate adapters gives clear signal on where each is failing.

**Practical implementation:** LoRA adapters are small files (~50–200 MB for a 7B model at r=16). Swapping them at runtime in Ollama takes a few seconds. A thin routing layer in the agent loop classifies the incoming request as config-generation or troubleshooting and loads the appropriate adapter before inference.

```python
def classify_task(user_input: str) -> str:
    """Simple heuristic classification — replace with a small classifier model
    or a fast LLM call for production use."""
    config_keywords = [
        "configure", "set up", "add a", "create", "generate config",
        "build", "template", "from scratch", "reset", "deploy"
    ]
    troubleshoot_keywords = [
        "not working", "down", "error", "dropped", "can't reach",
        "intermittent", "slow", "flapping", "why is", "what's wrong",
        "troubleshoot", "debug", "investigate"
    ]
    lower = user_input.lower()
    config_score = sum(1 for kw in config_keywords if kw in lower)
    ts_score = sum(1 for kw in troubleshoot_keywords if kw in lower)
    
    if config_score > ts_score:
        return "config"
    elif ts_score > config_score:
        return "troubleshoot"
    else:
        return "troubleshoot"  # default to safer mode when ambiguous

# In the agent loop:
task_type = classify_task(user_input)
model_name = "juniper-config-expert" if task_type == "config" else "juniper-troubleshoot-expert"
response = query_llm(messages, model=model_name)
```

### When one model may be sufficient

Two adapters add operational complexity. A single adapter may be acceptable if:

- The use case is primarily one or the other (a provisioning tool vs. a NOC assistant)
- The model quality bar is "good enough for supervised use" rather than "expert-level autonomous" — with a human reviewing every output, a somewhat confused single model is tolerable
- Training data volume is limited and splitting it would leave both adapters underserved (better to have one well-trained adapter than two mediocre ones)

If going single-adapter, bias the training data toward troubleshooting. Troubleshooting is the harder skill to acquire and the higher-value capability in practice. Config generation can be partially compensated by careful system prompt engineering and strong base model capability; the multi-step diagnostic reasoning in troubleshooting cannot.

---

## Summary: Training Data Requirements Side by Side

| Dimension | Config Generation | Troubleshooting |
|-----------|------------------|-----------------|
| Turn structure | 1–3 turns (optionally: gather params → generate) | 5–15 turns; multi-step investigative dialog |
| Output precision | Exact — one wrong token breaks it | Approximate — reasoning quality matters more than exact wording |
| Show command output | Not needed | Critical; must be syntactically realistic |
| Synthetic data | Highly effective; validate every example | Useful but must be reviewed by domain expert; real examples preferred |
| Negative examples | Low value | High value — models that never course-correct are dangerous |
| Key failure mode | Wrong command / wrong hierarchy | Premature diagnosis / ignoring disconfirming evidence |
| Evaluation method | Automated syntax check + device validation | Human review of reasoning quality |
| Training examples target | 5,000–10,000 (mostly single/double-turn) | 6,000–10,000 (multi-turn; harder to generate) |
| Primary data sources | Vendor docs, GitHub configs, parameterized templates | Real TAC cases, Reddit threads, synthetic dialogs reviewed by engineers |
| Interaction model | User describes → model asks params → model generates | Iterative: user describes symptom → model proposes step → user provides output → repeat |

## Sources

- [Juniper TechLibrary — Configuration guides](https://www.juniper.net/documentation/)
- [Cisco Configuration Professional guides](https://www.cisco.com/c/en/us/support/docs/)
- [GNS3 — Network simulation for config validation](https://www.gns3.com/)
- [Juniper vLab — Virtual Junos environment](https://jlabs.juniper.net/vlabs/)
- [Cisco Modeling Labs (CML)](https://developer.cisco.com/modeling-labs/)
