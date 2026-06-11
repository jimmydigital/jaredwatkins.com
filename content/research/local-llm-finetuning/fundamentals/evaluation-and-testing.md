---
title: "Evaluating a Fine-Tuned Network Expert Model"
date: 2026-06-11
lastmod: 2026-06-11
draft: false
description: "How to measure whether your fine-tuned network engineer specialist model is actually better than the base model — building an eval set, scoring command accuracy, running regression tests, and deciding when the model is good enough to deploy."
tags: ["evaluation", "testing", "fine-tuning", "llm", "network-engineering", "benchmarking"]
categories: ["technology"]
research_area: "local-llm-finetuning/fundamentals"
source_urls: []
last_reviewed: 2026-06-11
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Standard LLM benchmarks (MMLU, HumanEval, HellaSwag) don't tell you whether your fine-tuned network expert model is accurate on JunOS commands. You need a domain-specific evaluation pipeline: a held-out test set, a scoring method that understands CLI semantics, and a regression suite you run before every adapter update. Without this, you have no way to distinguish a better model from a worse one, and no safety net against catastrophic forgetting eroding general capability while you improve specialist performance.

## Key Facts

- **Build the eval set before training** — if you build it after, you may unconsciously include examples that were in training
- **CLI evaluation requires exact-match or semantic-match scoring** — BLEU score is meaningless for CLI output; one wrong character is a wrong answer
- **Two separate concerns:** domain accuracy (does the model know JunOS?) and general capability retention (did fine-tuning break reasoning?)
- **Hold-out ratio:** 10% of your dataset as test set; stratify across all five competency areas
- **Regression baseline:** always keep the pre-fine-tune base model's eval scores to compare against

---

## Building the Eval Set

Before splitting training data, designate 10% as a held-out test set that never enters training. Stratify by competency area so the test set covers all five capabilities proportionally — if your dataset is 30% config generation, your test set should be too.

**What the eval set must contain:**

The most important category is **examples you didn't write** — cases from vendor documentation, real network engineering forums, or actual device captures that you didn't use to write training data. These test generalization, not memorization.

For each of the five competency areas:

- *Command translation:* 200–300 natural language → CLI pairs not in training
- *Config generation:* 300–500 requirement specs → config blocks
- *Troubleshooting:* 100–200 complete multi-turn dialogs (harder to collect; smaller is OK if they're realistic)
- *Output interpretation:* 200–300 show-command output → interpretation pairs
- *Tool use:* 100–150 examples

**One important anti-pattern:** don't put similar-but-different variations of the same command in both training and eval. If `show bgp summary` is in training and `show bgp summary instance default` is in eval, the eval score flatters you — the model learned the pattern. The eval should contain conceptually distinct scenarios.

---

## Scoring Methods

### Exact match (for commands)

For single-command outputs (command translation, show interpretation), exact string match after normalization works well:

```python
def normalize_command(cmd: str) -> str:
    """Normalize a CLI command for comparison."""
    # Lowercase, collapse whitespace, strip trailing/leading whitespace
    cmd = cmd.strip().lower()
    cmd = " ".join(cmd.split())
    return cmd

def exact_match_score(predictions: list[str], references: list[str]) -> float:
    """Score a list of predicted commands against references."""
    assert len(predictions) == len(references)
    correct = sum(
        normalize_command(p) == normalize_command(r)
        for p, r in zip(predictions, references)
    )
    return correct / len(references)
```

Exact match is strict but appropriate for CLI commands: `set interfaces ge-0/0/0 description uplink` and `set interfaces ge-0/0/0 description  uplink` (double space) are functionally identical but `set interfaces ge-0/0/1 description uplink` (wrong interface) is completely wrong. Normalization handles the former; exact match catches the latter.

### Command presence scoring (for multi-command responses)

When the correct answer contains multiple commands (e.g., a troubleshooting step that proposes three diagnostic commands), check whether the reference commands are present in the model's output rather than requiring exact full-string match:

```python
def command_presence_score(prediction: str, reference_commands: list[str]) -> float:
    """Check what fraction of expected commands appear in the prediction."""
    pred_lower = prediction.lower()
    found = sum(
        normalize_command(cmd) in pred_lower
        for cmd in reference_commands
    )
    return found / len(reference_commands)
```

### Semantic scoring for config blocks

Config generation outputs are longer and have valid syntactic variations — a BGP config can use either set-style or hierarchical notation. Use an LLM judge for these: prompt a capable model (GPT-4, Claude 3.5) with the question, the model's answer, and the reference answer, asking it to score 0–3 on functional equivalence and syntactic correctness. This is slower and more expensive but necessary for config generation evaluation.

```python
JUDGE_PROMPT = """You are evaluating a network engineer AI assistant's response to a configuration task.

Task: {task}

Reference answer (correct):
{reference}

Model answer (to evaluate):
{prediction}

Score the model answer on:
1. Functional correctness (0-3): Does it accomplish the same configuration goal as the reference?
2. Syntax correctness (0-3): Is the syntax valid for the specified platform (JunOS/IOS/etc)?
3. Completeness (0-3): Does it include all necessary components or note what's missing?

Respond with JSON: {{"functional": N, "syntax": N, "completeness": N, "notes": "brief explanation"}}"""
```

### Troubleshooting dialog scoring

For multi-turn troubleshooting, evaluate at the turn level rather than dialog level:

- *Correct next command:* did the model propose the right diagnostic command given the symptom?
- *Correct interpretation:* given the show output, did the model identify the right cause?
- *Resolution accuracy:* for dialogs with known resolutions, did the model reach the correct diagnosis?

Score each turn independently; average across the dialog. A model that proposes the right first command but misinterprets the output is worse than a model that proposes a slightly suboptimal first command but correctly reads what it sees.

---

## General Capability Regression

Fine-tuning on a narrow domain can degrade the model's broader reasoning ability — catastrophic forgetting in practice. Before declaring a fine-tune successful, run a small general capability suite to confirm you haven't broken the base model.

**Minimum regression checks:**

1. **Basic reasoning:** 20–30 questions from a general reasoning test (math word problems, simple logical deductions). The fine-tuned model shouldn't regress more than 5% from the base model.

2. **English prose quality:** Ask the model to write a short explanation of a concept unrelated to networking. Check that it's still coherent, grammatically correct, and appropriately structured.

3. **Instruction following:** Give the model a multi-step instruction ("List three things, then explain the second one") and verify it follows the structure.

4. **Known-bad output detection:** If you had examples of the base model hallucinating commands during your data collection phase, re-run those prompts and verify the fine-tuned model handles them better (or at least not worse).

A simple regression run takes 15–30 minutes and can be automated. If the fine-tune shows >10% regression on general reasoning, the LoRA rank may be too high, the learning rate too aggressive, or the training may have overfit — see finetuning-mechanics for mitigation strategies.

---

## Running the Eval Pipeline

A basic automated evaluation run:

```python
import json
import subprocess
import requests
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/chat"

def query_model(model_name: str, prompt: str, system: str) -> str:
    response = requests.post(OLLAMA_URL, json={
        "model": model_name,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "options": {"temperature": 0.0}  # deterministic for eval
    })
    return response.json()["message"]["content"]

def run_eval(model_name: str, eval_set_path: Path) -> dict:
    eval_set = json.loads(eval_set_path.read_text())
    results = {"exact_match": [], "presence": [], "errors": []}

    for example in eval_set:
        if example["type"] == "command_translation":
            prediction = query_model(
                model_name,
                example["prompt"],
                example["system"]
            )
            score = exact_match_score([prediction], [example["reference"]])
            results["exact_match"].append(score)
        elif example["type"] == "multi_command":
            prediction = query_model(
                model_name,
                example["prompt"],
                example["system"]
            )
            score = command_presence_score(prediction, example["reference_commands"])
            results["presence"].append(score)

    return {
        "model": model_name,
        "exact_match_accuracy": sum(results["exact_match"]) / len(results["exact_match"]),
        "command_presence": sum(results["presence"]) / len(results["presence"]),
        "n_examples": len(eval_set)
    }

# Compare base model vs. fine-tuned
base_results = run_eval("llama3.1:8b", Path("eval_set_juniper.json"))
finetuned_results = run_eval("juniper-expert", Path("eval_set_juniper.json"))

print(f"Base model exact match: {base_results['exact_match_accuracy']:.1%}")
print(f"Fine-tuned exact match: {finetuned_results['exact_match_accuracy']:.1%}")
print(f"Delta: {finetuned_results['exact_match_accuracy'] - base_results['exact_match_accuracy']:+.1%}")
```

Always run eval at **temperature 0.0** — you want deterministic output so results are reproducible. The temperature setting used for production is irrelevant to whether the model knows the correct answer.

---

## What "Good Enough" Looks Like

There's no universal pass/fail threshold, but these are reasonable targets for a network engineer specialist model being deployed for interactive use on real devices:

| Competency | Minimum acceptable | Good | Excellent |
|-----------|-------------------|------|-----------|
| Command translation (exact match) | 70% | 85% | 95%+ |
| Config generation (semantic, 0-9 score) | 6.0/9 | 7.5/9 | 8.5+/9 |
| Troubleshooting (command presence) | 60% | 75% | 90%+ |
| Output interpretation | 65% | 80% | 90%+ |
| General reasoning regression | <10% drop | <5% drop | <2% drop |

The most important number is troubleshooting command presence — this is where the model is most exposed to real device state it's never seen before. A model that scores well on command translation but poorly on troubleshooting has memorized syntax without developing diagnostic reasoning.

For a "dry run" deployment (model proposes commands, engineer decides whether to run them), lower thresholds are acceptable — a 70% exact-match model is still a useful assistant when a human is reviewing every suggestion. For an autonomous mode with pre-approved read-only commands, aim for 90%+ on command translation before enabling.

---

## Tracking Eval Results Over Iterations

As you iterate on training data and hyperparameters, keep a simple results log:

```
| Date       | Model version    | Exact match | Troubleshoot | Regression | Notes                    |
|------------|-----------------|-------------|-------------|------------|--------------------------|
| 2026-06-10 | juniper-v1      | 71%         | 58%         | -3%        | baseline fine-tune       |
| 2026-06-15 | juniper-v2      | 78%         | 63%         | -4%        | +2K troubleshoot examples|
| 2026-06-20 | juniper-v3      | 82%         | 71%         | -2%        | r=32, focused on BGP     |
```

This log is more valuable than any individual eval score — it shows which data investments paid off and whether you're trading general capability for specialist performance.
