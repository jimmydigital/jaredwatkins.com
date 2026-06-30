---
title: "Dataset Formats for Fine-Tuning"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "The three standard dataset formats used for LLM instruction fine-tuning — Alpaca, ShareGPT, and ChatML — with examples and guidance on when to use each."
research_area: "local-llm-finetuning/training-data"
source_urls:
  - "https://github.com/tatsu-lab/stanford_alpaca"
  - "https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered"
  - "https://github.com/openai/openai-cookbook"
last_reviewed: 2026-06-10
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Fine-tuning requires a dataset formatted to match the model's expected input structure. Three formats dominate open-source practice: Alpaca (simple instruction-response pairs), ShareGPT (multi-turn conversations), and ChatML (the format used by OpenAI-style models and most modern open-source fine-tuning frameworks). For a network-engineer specialist model, ShareGPT/ChatML is strongly preferred because network troubleshooting is inherently multi-turn.

## Key Facts

- **Alpaca:** Single-turn; instruction + optional input + output; easiest to generate
- **ShareGPT:** Multi-turn; conversation history; natural for dialog-style interaction
- **ChatML:** OpenAI's internal format; used by Llama 3.1, Mistral, and most 2024+ models
- **File format:** JSONL (one JSON object per line) for all three
- **Recommended for network expert:** ChatML with multi-turn examples

## What It Is / How It Works

**Alpaca format.** The simplest structure: each example has three fields: `instruction` (the task), `input` (optional context), and `output` (the expected response). Introduced by Stanford Alpaca (2023). Good for single-turn question-answering tasks where each example is self-contained.

```json
{
  "instruction": "Convert this plain English description to a Juniper JunOS CLI command",
  "input": "Show all BGP neighbors and their current state",
  "output": "show bgp neighbor"
}
```

**Limitations of Alpaca for networking.** Real network troubleshooting involves back-and-forth: the model proposes a diagnostic step, the engineer runs it and reports output, the model interprets the output and proposes the next step. Single-turn format cannot represent this. Every multi-step troubleshooting workflow must be artificially collapsed into one example, which destroys the reasoning chain that makes the response useful.

**ShareGPT format.** Represents a full conversation as a list of turns with speaker roles (`human` and `gpt`). Each example is one conversation. This maps naturally to interactive network troubleshooting sessions.

```json
{
  "conversations": [
    {
      "from": "human",
      "value": "My Juniper EX switch is showing some interfaces as 'down' but they're physically connected. Where do I start?"
    },
    {
      "from": "gpt",
      "value": "Start by checking the interface status in detail. Run:\n\n```\nshow interfaces et-0/0/0 detail\n```\n\nReplace `et-0/0/0` with the specific interface name. Look for: (1) Physical link status vs. protocol status — if physical is down, check the cable and transceiver; (2) Error counters under 'Input errors' and 'Output errors'; (3) 'Link-mode' to confirm auto-negotiation settings.\n\nWhat does the output show?"
    },
    {
      "from": "human",
      "value": "Physical link is up, protocol is down. No input errors. Output shows 'inet, MTU 1500'."
    },
    {
      "from": "gpt",
      "value": "Physical up / protocol down on Juniper typically means a Layer 2 or Layer 3 configuration issue, not a hardware problem. Since the interface has `inet` family assigned, check:\n\n1. Is the interface in a routing instance or the default instance? Run: `show interfaces et-0/0/0 routing-instance`\n2. Is there an active family inet address? Run: `show interfaces et-0/0/0 terse`\n3. Check for any filters or policers that might be preventing the protocol from coming up: `show interfaces et-0/0/0 detail | match filter`\n\nAlso check: is this interface supposed to be a trunk port or access port? If it's expected to carry VLANs, confirm `family ethernet-switching` is configured instead of `family inet`."
    }
  ]
}
```

**ChatML format.** The format used internally by OpenAI and adopted by Llama 3.1, Mistral Instruct v3, and most 2024+ open-source models. Uses special role tokens in the tokenizer. In raw form:

```
<|im_start|>system
You are an expert Juniper network engineer. You translate English descriptions into JunOS commands and help troubleshoot Juniper devices.<|im_end|>
<|im_start|>user
Show me the BGP summary on this router<|im_end|>
<|im_start|>assistant
show bgp summary<|im_end|>
```

In JSONL format for training frameworks like Axolotl or Unsloth:

```json
{
  "messages": [
    {"role": "system", "content": "You are an expert Juniper network engineer..."},
    {"role": "user", "content": "Show me the BGP summary on this router"},
    {"role": "assistant", "content": "show bgp summary"}
  ]
}
```

**System prompt role.** The system message sets the model's persona and behavior for the entire conversation. For a network expert model, a well-crafted system prompt is part of the training data: every example should include the same (or similar) system prompt so the model learns to activate the expert persona when that prompt is present. Example:

```
You are a network engineer expert specializing in Juniper Networks devices (JunOS). You translate plain English descriptions of network outcomes into specific JunOS commands and configurations. You troubleshoot network problems step by step, interpret show command output and log files, and use standard network diagnostic tools (ping, traceroute, arp). When you provide commands, you include the correct JunOS syntax with necessary context. You acknowledge when you're uncertain rather than providing incorrect commands.
```

**Format selection guidance:**
- Use Alpaca for simple command lookup tasks (English → command) where no context is needed
- Use ShareGPT/ChatML for all troubleshooting, multi-step configuration, and interpretive tasks
- For a network expert model, target 80%+ of examples in multi-turn ShareGPT/ChatML format; single-turn Alpaca for the command reference subset

**Quality criteria for individual examples:**
- Commands must be syntactically correct and platform-specific (JunOS ≠ IOS — never mix them)
- Show command output in examples should look realistic (actual counter formats, correct field names)
- Assistant responses should explain the *why* not just the *what* — this is what makes the model useful vs. a simple lookup tool
- Each example should reflect what an experienced engineer would actually say, not a documentation excerpt
- Length: 200–1000 tokens per turn is typical; avoid very short responses (no depth) and very long ones (hard to learn from)

**Dataset size targets:**
- Minimum viable: 1,000–2,000 high-quality multi-turn examples
- Good coverage: 5,000–10,000 examples
- Comprehensive specialist: 15,000–30,000 examples
- Quality matters far more than quantity: 2,000 well-crafted examples consistently outperform 10,000 noisy ones

## Sources

- [Stanford Alpaca (Taori et al. 2023)](https://github.com/tatsu-lab/stanford_alpaca) — introduced the Alpaca format
- [ShareGPT dataset (Vicuna)](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) — reference implementation
- [ChatML format documentation](https://github.com/openai/openai-python/blob/main/chatml.md) — OpenAI's ChatML spec
- [Axolotl dataset format docs](https://github.com/OpenAccess-AI-Collective/axolotl#dataset) — practical reference for format handling in training
