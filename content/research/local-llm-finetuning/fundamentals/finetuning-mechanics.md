---
title: "Fine-Tuning Mechanics"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "What fine-tuning actually modifies in a base model, how instruction tuning differs from domain adaptation, the risk of catastrophic forgetting, and how to evaluate whether a fine-tuned model actually improved."
tags: ["fine-tuning", "instruction-tuning", "domain-adaptation", "catastrophic-forgetting", "sft", "llm"]
categories: ["technology"]
research_area: "local-llm-finetuning/fundamentals"
source_urls:
  - "https://arxiv.org/abs/2109.01652"
  - "https://arxiv.org/abs/2210.11610"
  - "https://huggingface.co/blog/rlhf"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Fine-tuning is continued training of a pretrained model on a smaller, curated dataset. It adjusts existing weights rather than learning from scratch, making it fast and hardware-accessible. Understanding what fine-tuning changes — and what it cannot — is essential for setting realistic expectations when building a specialist model.

## Key Facts

- **Input:** A pretrained base or instruction-tuned model + a curated training dataset
- **Process:** Same gradient descent as pretraining, but on far fewer tokens (thousands to millions vs. trillions)
- **Output:** A model with modified weights that responds differently to the target domain
- **Risk:** Catastrophic forgetting — aggressively fine-tuned models can lose general capability
- **Key methods:** Full fine-tune, LoRA/QLoRA (parameter-efficient), DPO (preference alignment)

## What It Is / How It Works

**What fine-tuning modifies.** A neural network's "knowledge" is entirely encoded in its weight matrices. Fine-tuning runs the same backpropagation loop as pretraining but on a small domain-specific dataset, updating some or all weights to reduce loss on that new data. The model doesn't "add" knowledge like appending to a database — it redistributes and reshapes the statistical patterns in its weights. Concepts that appear frequently in fine-tuning data become more strongly associated. Formats that match fine-tuning examples become more likely to be reproduced.

**Three types of fine-tuning, distinguished by goal:**

*Instruction tuning (SFT)* teaches a base model to follow a specific input-output format — typically prompt/response pairs. This is what converts a raw base model into an assistant. Open-source instruction-tuned models (Llama 3.1 8B Instruct, Mistral 7B Instruct) have already undergone this step. For a specialist model built on top of an Instruct variant, you're doing the second type instead.

*Domain adaptation* teaches an already-instruction-tuned model the vocabulary, facts, commands, and reasoning patterns of a specific domain. This is the relevant type for a network-engineer expert: you start from Llama 3.1 8B Instruct (which already knows how to be an assistant) and fine-tune it on networking content so it knows Juniper JunOS syntax, OSPF troubleshooting flows, BGP state machines, etc. The model already knows how to answer questions; you're teaching it what to say about your specific domain.

*Preference alignment (RLHF, DPO)* adjusts the model's behavior toward preferred outputs — not just correct facts but correct tone, safety, format. DPO (Direct Preference Optimization) is the practical approach for small-scale use: provide pairs of (preferred response, rejected response) and the model learns the difference. For a network expert model this matters for outputs like preferring to show complete working configs over partial snippets, or prefering to explain what each command does rather than just providing a command list.

**Catastrophic forgetting.** When a model is fine-tuned too aggressively on a narrow domain, it can "forget" general capabilities — language fluency, reasoning, knowledge outside the training data. This is most severe with full fine-tuning (all weights updated) on small datasets (a few thousand examples). Practical effects: a network-expert model fine-tuned only on Cisco IOS examples might refuse or fail to handle Cisco ASA or Nexus commands even though the base model knew them. Mitigation strategies: use LoRA/QLoRA (fewer weights updated), include some general-purpose examples mixed with domain data, keep the dataset large and diverse enough to cover the target domain comprehensively, and avoid training for too many epochs.

**Epochs and overfitting.** An epoch is one full pass through the training dataset. With small datasets (under 10,000 examples), the model can overfit after just 1–3 epochs — memorizing training examples rather than generalizing. Signs: perfect training loss but poor performance on held-out test prompts; the model reproduces training examples verbatim. For domain fine-tuning, 1–3 epochs is typical. Monitor validation loss during training and stop when it stops improving.

**What fine-tuning cannot do.** Fine-tuning cannot reliably inject information that contradicts the base model's strongly-encoded priors. It cannot expand the model's context window. It cannot fix systematic reasoning failures baked in at pretraining scale. If a 7B base model consistently fails at multi-hop network troubleshooting scenarios, fine-tuning on more examples of the same type will improve performance somewhat but will not close the gap to a 70B model. Fine-tuning amplifies what the base model can already do — it does not add fundamentally new capabilities.

**Evaluating whether fine-tuning worked.** Evaluation for specialist models requires domain-specific test sets created before training. Hold out 10–15% of your curated data as a test set; do not train on it. Build evaluation prompts that test: (1) command accuracy — does the model produce syntactically correct, semantically correct device commands? (2) troubleshooting flow — given specific show command output, does the model correctly identify the problem and next diagnostic step? (3) format compliance — does the output match expected config structure? (4) refusal accuracy — does it correctly say "I don't know" rather than hallucinating a plausible-sounding but wrong command? Human review of 100–200 representative prompts by a network engineer is more reliable than automated metrics for this use case.

## Notable Developments

- **2023:** DPO (Rafailov et al.) — simplified preference alignment without a separate reward model; widely adopted for open-source fine-tuning
- **2022:** InstructGPT (OpenAI) — demonstrated that SFT + RLHF reliably produces helpful, instruction-following behavior; motivation for all subsequent open-source instruction tuning
- **2022:** FLAN (Wei et al.) — showed that instruction tuning on many diverse tasks improved zero-shot generalization
- **2021:** LoRA (Hu et al.) — parameter-efficient fine-tuning that made specialist fine-tuning practical on consumer hardware

## Sources

- [Finetuned Language Models Are Zero-Shot Learners (Wei et al. 2021)](https://arxiv.org/abs/2109.01652) — FLAN instruction tuning
- [InstructGPT: Training language models to follow instructions (Ouyang et al. 2022)](https://arxiv.org/abs/2203.02155) — canonical SFT + RLHF paper
- [Direct Preference Optimization (Rafailov et al. 2023)](https://arxiv.org/abs/2305.18290) — DPO method
- [Hugging Face RLHF explainer](https://huggingface.co/blog/rlhf) — accessible overview of the alignment pipeline
