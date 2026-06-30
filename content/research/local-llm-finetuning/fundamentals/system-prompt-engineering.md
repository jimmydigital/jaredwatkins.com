---
title: "System Prompt Engineering for Specialist Models"
date: 2026-06-11
lastmod: 2026-06-11
draft: false
description: "How to write the system prompt for a fine-tuned network engineer specialist model — role definition, constraint specification, output format anchoring, few-shot examples, and the interaction between system prompt design and training data quality."
research_area: "local-llm-finetuning/fundamentals"
source_urls: []
last_reviewed: 2026-06-11
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The system prompt is the first thing a fine-tuned specialist model reads on every inference call. It sets the role, constraints, output format, and behavioral expectations for everything that follows. A poorly written system prompt can degrade a well-trained model; a well-written one can compensate for training gaps. For a network engineer specialist, the system prompt must be consistent between training and inference — if your training data used one system prompt and your Ollama Modelfile uses a different one, the model's behavior will be inconsistent and harder to predict.

## Key Facts

- **Training-inference consistency is mandatory:** the system prompt in training data must exactly match the system prompt at inference
- **System prompts are part of the context window** — they consume tokens on every call; keep them tight
- **The system prompt cannot override what the model learned in training** — it can guide and remind, but not reprogram
- **Few-shot examples in the system prompt are powerful** — 2–3 examples of perfect output anchor the format more reliably than prose instructions
- **Platform specificity is critical** — a model serving both Juniper and Cisco needs the system prompt to specify the active platform; ambiguity produces mixed-syntax output

---

## The Anatomy of an Effective Specialist System Prompt

A network engineer specialist system prompt has four components: role definition, platform scope, behavioral constraints, and output format. All four are necessary; weak performance in any area degrades overall output quality.

### 1. Role Definition

Tell the model what it is, not what it should do. "You are a senior Juniper network engineer" is more effective than "You should answer questions about Juniper networking." The former activates the model's learned representation of what a senior network engineer knows and does; the latter frames the task as a Q&A exercise.

Be specific about depth: "senior Juniper network engineer with 10+ years of production experience" signals that the model should not hedge unnecessarily on common questions. A model that describes itself as a "helpful assistant" will hedge more, qualify more, and suggest consulting documentation more frequently than one that has internalized the role of a confident domain expert.

### 2. Platform Scope

Explicitly list the platforms the model covers. This prevents the model from generating IOS commands in response to JunOS questions (a common failure mode when the base model has more IOS training data than JunOS).

For the Juniper model:
```
You have deep expertise in JunOS across the full Juniper product line:
- EX Series (campus switches, EX2300, EX3400, EX4300, EX4600, EX9200)
- QFX Series (data center switching, QFX5110, QFX5120, QFX10000)
- MX Series (service/edge routing, MX204, MX480, MX960)
- SRX Series (security/firewalls, SRX300, SRX1500, SRX4600)
- Juniper Apstra (intent-based networking, data center fabric management)

Always use JunOS syntax. Never generate Cisco IOS, NX-OS, or other vendor syntax unless explicitly asked to compare.
```

For the Cisco model, the platform list is more complex:
```
You have deep expertise across the Cisco product line:
- IOS-XE: ASR 1000, CSR 1000v, Catalyst 8000 Series, ISR 4000
- NX-OS: Nexus 9000, 7000, 5000 (note: meaningfully different from IOS)
- ASA: ASA 5500-X, Firepower 1000/2100/4100 (note: ASA syntax differs from IOS)
- IOS-XR: ASR 9000, NCS Series (note: uses commit model similar to JunOS)

When generating configuration, always identify which platform you're targeting. If not specified, assume IOS-XE. Always clarify when NX-OS or ASA syntax differs from IOS-XE.
```

### 3. Behavioral Constraints

These instructions define what the model should and should not do. For a network device assistant:

```
Behavioral guidelines:
- For configuration commands: provide the exact CLI syntax, ready to paste into a device
- For troubleshooting: propose one step at a time; wait for the output before the next step
- When uncertain about platform version differences: note the uncertainty and give the most common case
- Never generate configuration for actions that are destructive without an explicit warning (e.g., "clear ip route *", "delete chassis-cluster", "commit confirmed")
- If a question is ambiguous between platforms (e.g., "how do I check OSPF?"), ask which platform before answering
- Do not hallucinate command syntax. If you don't know the exact syntax, say so rather than generating a plausible-sounding but incorrect command.
```

The last constraint — explicitly telling the model not to hallucinate — is worth including even though it won't fully prevent hallucination. It does reduce hallucination frequency for fine-tuned specialist models, because it activates a learned behavior from the training data (examples where the model appropriately expressed uncertainty).

### 4. Output Format

Specify how commands and configurations should be formatted. This is especially important for code block formatting — whether commands appear in backtick-delimited code blocks affects the agentic loop's ability to parse them for execution approval.

```
Output format:
- Single commands: present in a code block with the platform identifier
  ```junos
  show ospf neighbor detail
  ```
- Multi-command sequences: number each step and put each command in its own code block
- Configuration blocks: use set-format (one command per line, starting with "set") unless hierarchical format is explicitly requested
- When interpreting show command output: structure the response as (1) what the output shows, (2) what is normal, (3) what is anomalous or concerning
```

---

## The Training Data — System Prompt Relationship

Every example in your training dataset should use the identical system prompt text that appears in your Modelfile. This is not a best practice — it's a requirement. The model learns to produce good network engineering responses *conditional on* the system prompt it was trained with. A different system prompt at inference shifts the conditional and the model's behavior becomes less predictable.

**Practical implications:**

Finalize your system prompt *before* generating training data. Changes to the system prompt after training has started mean re-generating (or at minimum re-verifying) your training data. A common mistake is to write a rough system prompt for data generation, then "improve" it for the Modelfile — the two diverge and the model behaves strangely.

Version your system prompt alongside your training data and adapter files. A simple naming convention:

```
juniper-expert-v1/
  system_prompt.txt        ← exact text used in all v1 training examples
  train_set_v1.jsonl
  eval_set_v1.jsonl
  adapter/                 ← LoRA adapter trained on train_set_v1
  Modelfile.juniper-v1     ← references system_prompt.txt verbatim
```

**What happens when they diverge:** The model produces output that's structurally correct (it knows JunOS commands) but behaviorally inconsistent — it may ignore format instructions, over-hedge on questions it handled confidently during eval, or produce responses structured differently than the training examples. These symptoms are subtle and can be misattributed to training quality problems when the real issue is prompt-training mismatch.

---

## Few-Shot Examples in the System Prompt

Two or three worked examples placed in the system prompt are often more effective than prose instructions for format compliance. The model treats them as a template — the output format of those examples anchors subsequent responses more reliably than "format commands in code blocks."

Example of a system prompt with inline few-shot examples:

```
You are a senior Juniper network engineer with expertise across the full JunOS product line.

[...]role and constraints as above[...]

Here are examples of ideal responses:

---
User: How do I check OSPF neighbor state?
Assistant: To view all OSPF neighbors and their adjacency state:

```junos
show ospf neighbor
```

For detailed output including interface, area, and timer information:

```junos
show ospf neighbor detail
```

To check a specific neighbor by router ID:

```junos
show ospf neighbor 10.0.0.1
```

---
User: The OSPF adjacency to 10.10.10.2 just dropped. Where do I start?
Assistant: Start with the current neighbor state and the interface it was on:

```junos
show ospf neighbor
show ospf interface detail
```

Then check the log for the reason it dropped:

```junos
show log messages | match OSPF | last 50
```

The log will show whether it was a dead timer expiry, authentication failure, or interface event. Paste the output and I can tell you what to look for.
---
```

The two examples above establish the response pattern: commands in labelled code blocks, brief prose explaining what each command shows, and for troubleshooting — propose commands and ask for output before diagnosing.

**System prompt token cost.** A system prompt like the above (role, platform scope, constraints, two examples) is approximately 400–600 tokens. At 8192 token context, that leaves ~7,600 tokens for conversation — adequate for most troubleshooting sessions. If the system prompt grows beyond ~800 tokens, consider whether some content is better expressed through training data than through runtime instructions.

---

## Testing the System Prompt

Before using a system prompt for training data generation, test it directly against the base model:

1. Give the base model the system prompt and a representative set of 20–30 test prompts
2. Review: does it respond in the right format? Does it stay on platform? Does it handle "I don't know" cases correctly?
3. Iterate the system prompt based on failures before generating training data

Common failures and fixes:

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Model generates IOS when asked JunOS | Platform scope too vague | Add explicit "never use IOS syntax" constraint |
| Model puts commands in prose, not code blocks | Format instructions missing | Add output format section with example |
| Model hedges on basic questions ("you should consult documentation") | Role definition too weak | Strengthen role: "10+ years production experience" |
| Model ignores multi-step troubleshooting format | No troubleshooting examples | Add a troubleshooting few-shot example |
| Model generates destructive commands without warning | Missing constraint | Add explicit constraint for dangerous command classes |

---

## Updating the System Prompt

If you change the system prompt after training, you have two options:

**Minor wording tweaks** (same intent, different phrasing): usually safe at inference; the model's trained behavior is robust to small prompt changes.

**Structural changes** (new sections, different format examples, different constraints): re-generate and re-label affected training data, then retrain. The cost is worth it — a mismatched system prompt is a hidden source of quality degradation that's hard to diagnose.

Keep the system prompt in version control alongside the adapter and training data. A three-file bundle — `system_prompt.txt`, `train_set.jsonl`, `adapter/` — makes it possible to reproduce any previous version exactly.
