---
title: "Temperature and Sampling"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "What temperature actually is in LLM inference, how it reshapes the probability distribution over next tokens, how it interacts with top-p and top-k sampling, and why the right setting depends entirely on the task."
tags: ["temperature", "sampling", "inference", "llm", "top-p", "top-k", "reasoning"]
categories: ["technology"]
research_area: "local-llm-finetuning/fundamentals"
source_urls:
  - "https://arxiv.org/abs/2002.06440"
last_reviewed: 2026-06-10
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Temperature is a single scalar that controls how deterministic or random a model's output is by reshaping the probability distribution the model produces before sampling the next token. At temperature 0, the model always picks the single most likely token — fully deterministic. At high temperature, unlikely tokens become more probable and the output becomes increasingly random. Between those extremes, temperature is a dial trading predictability against creativity. For a network engineer specialist model, the right temperature depends on the task: near-zero for command generation, moderate for explanatory prose, never high.

## Key Facts

- **Temperature is applied at inference time** — it is not a property of the trained model
- **Range:** 0.0 to theoretically unbounded; practical range is 0.0–1.5; above 2.0 is typically incoherent
- **Temperature 1.0** = use the model's raw output probabilities unchanged
- **Temperature < 1.0** = sharpen the distribution; most likely tokens become more dominant
- **Temperature > 1.0** = flatten the distribution; unlikely tokens become more probable
- **Temperature 0.0** = greedy decoding; always pick the highest-probability token; fully deterministic
- **Interacts with:** top-p (nucleus sampling), top-k, repetition penalty

---

## How It Works Mechanically

Recall from the model internals entry: after all transformer layers run, the model produces a vector of **logits** — one raw score per vocabulary token, 128,000 scores for a Llama 3 model. The logit for each token reflects how much the model "wants" to emit that token next given everything it has processed so far. These logits are not probabilities yet — they're unbounded real numbers, and their relative magnitudes encode the model's preferences.

To turn logits into probabilities, **softmax** is applied:

```
P(token_i) = exp(logit_i) / sum(exp(logit_j) for all j)
```

Softmax is an exponential normalization: high logits get amplified relative to low ones, and the results sum to 1.0.

Temperature enters by dividing every logit by the temperature value *before* applying softmax:

```
P(token_i | temperature T) = exp(logit_i / T) / sum(exp(logit_j / T) for all j)
```

That's the entire mechanism. One division. Everything downstream — the shape of the distribution, how often the model picks surprising tokens — follows from this.

---

## What Different Temperatures Actually Do

Consider a simplified case: the model has just processed "show ospf" and must pick the next token. Imagine the top-5 logit scores look like this:

```
" neighbor"   logit: 8.2
" interface"  logit: 6.1
" database"   logit: 5.4
" route"      logit: 4.8
" summary"    logit: 4.3
```

After dividing by temperature and applying softmax, the resulting probabilities at different temperatures:

| Token | T=0.1 | T=0.5 | T=1.0 | T=1.5 | T=2.0 |
|-------|-------|-------|-------|-------|-------|
| " neighbor" | 99.9% | 92.1% | 67.3% | 48.2% | 37.1% |
| " interface" | ~0.0% | 5.8% | 13.9% | 16.4% | 16.2% |
| " database" | ~0.0% | 1.5% | 7.2% | 11.8% | 13.4% |
| " route" | ~0.0% | 0.4% | 4.1% | 9.2% | 11.8% |
| " summary" | ~0.0% | 0.1% | 2.6% | 7.0% | 10.3% |
| all others | ~0.0% | 0.1% | 4.9% | 7.4% | 11.2% |

*(Approximate values for illustration — real distributions span 128,000 tokens)*

**At T=0.1:** " neighbor" is the overwhelming choice nearly 100% of the time. The model behaves like it has a lookup table — ask for the same completion, get the same answer every time. Useful for CLI commands. Boring for prose.

**At T=0.5:** " neighbor" still wins most of the time but " interface" and " database" occasionally appear. The model's strong preferences are respected but there's some variation. Good for technical explanations where phrasing can vary but facts can't.

**At T=1.0:** The raw distribution. " neighbor" wins two-thirds of the time; the other options are genuinely in play. This is what the model learned during training — the natural uncertainty it had about what comes next. Often reasonable for general conversation.

**At T=1.5:** The distribution is noticeably flatter. " neighbor" is now under 50%, " interface" and " database" are real contenders. You'll see varied and sometimes surprising completions. Useful for brainstorming, creative writing, generating diverse synthetic training data.

**At T=2.0:** Getting incoherent. Tokens the model rated as poor choices (logit 4.3) are nearly as likely as tokens it rated highly (logit 8.2). Output starts mixing in low-probability tokens more frequently, producing text that looks plausible word-by-word but lacks coherent direction.

---

## Temperature and Reasoning

Temperature interacts with reasoning in a less obvious way. Modern models — especially those trained with chain-of-thought reasoning (Phi-4-reasoning, DeepSeek R1 distills, Qwen3 in thinking mode) — produce internal reasoning traces before their final answer. The temperature during this reasoning phase has a different character than during final-answer generation.

**Low temperature during reasoning** causes the model to commit to its first hypothesis quickly and follow it deterministically. This is fast and often correct when the problem is straightforward. But if the initial reasoning path is wrong, low temperature means the model will confidently elaborate on a wrong answer rather than reconsidering.

**Moderate temperature during reasoning** allows the model to explore more of the reasoning space — occasionally taking a less-obvious path that turns out to be correct. This is why some reasoning model deployments use slightly higher temperature (0.3–0.7) during the thinking phase and then collapse to low temperature (0.1) for the final answer extraction. The model "brainstorms" its way to a better answer then commits precisely.

For a network troubleshooting model, this distinction matters. A model diagnosing "OSPF neighbor stuck in EXSTART" with T=0.0 throughout will commit to its first hypothesis (MTU mismatch, the most common cause) and drive toward that conclusion even if subsequent show command output suggests otherwise. A model with slightly higher temperature during its reasoning turns is more likely to consider the second and third possibilities (authentication mismatch, duplicate router ID) before committing.

**Practical approach for the network expert:** Set T=0.1 for the final output token of command-generation tasks. Set T=0.3–0.5 for troubleshooting reasoning steps where the model is interpreting output and forming a hypothesis. This can be implemented by using different temperature settings for different turn types, or by using a model that separates its thinking trace (higher temperature) from its final answer (lower temperature) by design.

---

## Top-p and Top-k: Temperature's Companions

Temperature reshapes the distribution but doesn't limit which tokens are candidates. Two additional parameters do:

**Top-k sampling** restricts the candidate pool to the k highest-probability tokens before sampling. With k=50, only the 50 most likely tokens are considered; everything else gets probability 0. This prevents extremely low-probability tokens from ever being sampled, even at high temperature. A common pairing: T=0.8, top-k=50.

**Top-p (nucleus) sampling** restricts the candidate pool to the smallest set of tokens whose cumulative probability exceeds p. With top-p=0.9, the model selects the minimum set of tokens that together account for 90% of the probability mass, then samples only from that set. The set size varies dynamically: when the model is very confident (one token at 95% probability), nucleus sampling might include just one token. When the model is uncertain, it might include 50. Top-p adapts to the distribution's shape; top-k is a fixed cut.

In practice, top-p=0.9 with temperature 0.1–0.5 is the standard configuration for technical/factual tasks. The top-p limit prevents degenerate outputs at the tail of the distribution; temperature controls how sharply the model prefers its top choices within the nucleus.

**For the network expert model config in Ollama:**

```
# Modelfile settings for config generation (deterministic, exact)
PARAMETER temperature 0.1
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1

# For troubleshooting reasoning (slightly more exploratory)
PARAMETER temperature 0.4
PARAMETER top_p 0.9
PARAMETER top_k 50
PARAMETER repeat_penalty 1.05
```

**Repeat penalty** deserves a brief mention: it reduces the logit score of any token that has already appeared in the recent output, making the model less likely to repeat itself. Values around 1.05–1.15 prevent the model from looping on the same phrase. Setting it too high (>1.3) causes the model to avoid important technical terms it already used, which actively degrades network command output.

---

## The Temperature=0 Special Case

Setting temperature to exactly 0 is called **greedy decoding** — the model always selects the argmax token (highest logit) at every step. This is fully deterministic: the same prompt will always produce exactly the same output.

Greedy decoding sounds ideal for a command-generation tool, but it has a subtle failure mode: once the model starts generating a suboptimal sequence, it cannot escape it. If the highest-probability first token locks the generation into a path where subsequent tokens are less optimal than they would have been with a different start, greedy decoding follows that path to the end. This is the same problem as a greedy algorithm in computer science — locally optimal choices don't always produce globally optimal results.

In practice, T=0.1 (very low but nonzero) often outperforms T=0.0 for technical command generation because the tiny amount of randomness allows occasional recovery from suboptimal token choices early in generation. The difference is small but measurable in output quality evaluations.

## Sources

- [The Curious Case of Neural Text Degeneration (Holtzman et al. 2020)](https://arxiv.org/abs/2002.06440) — introduced nucleus (top-p) sampling; analysis of temperature effects on text quality
