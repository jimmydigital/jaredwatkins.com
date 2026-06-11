---
title: "Context Window Management for Device-Connected Models"
date: 2026-06-11
lastmod: 2026-06-11
draft: false
description: "How to manage the context window when a local LLM is connected to real network devices — handling long show command output, maintaining troubleshooting state across turns, and the tradeoff between context length and inference speed on Apple Silicon."
tags: ["context-window", "inference", "network-automation", "llm", "kv-cache", "apple-silicon", "ollama"]
categories: ["technology"]
research_area: "local-llm-finetuning/specialist-models"
source_urls:
  - "https://github.com/ktbyers/netmiko"
last_reviewed: 2026-06-11
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Network device show commands can produce large outputs — a full BGP routing table, an OSPF database dump, or `show interfaces detail` on a chassis with dozens of ports can each run to thousands of lines. This creates a practical tension: you want the model to see the full device state, but context windows are finite and long contexts are slow. This entry covers how to measure context usage in the agentic loop, strategies for handling oversized show output, how to maintain troubleshooting state when context must be truncated, and the specific performance impact on Apple Silicon.

## Key Facts

- **8B model with 8192 token context:** fits ~6,000–7,000 words of conversation — adequate for most single-issue troubleshooting sessions
- **Long contexts are exponentially slower:** prefill time scales with O(n²) of context length for standard attention; 8192 tokens takes roughly 4× longer to prefill than 2048
- **Apple Silicon KV cache lives in unified memory:** at 8192 token context, a 7B model with 32 layers and 1024 KV dimension uses ~8 GB for the KV cache (2 × 32 × 8192 × 1024 × 2 bytes); see model-internals for the full formula
- **The most common problem:** `show interfaces detail` or `show ospf database` output that exceeds what fits in context alongside the conversation history
- **Best mitigation:** targeted command selection — ask for specific, narrow show commands rather than broad detailed dumps

---

## Measuring Context Usage

Before building mitigation strategies, you need to know how many tokens your conversations actually use. The simplest approach is to count tokens at the edge of the agentic loop before sending each request:

```python
import requests

def count_tokens_ollama(model: str, messages: list) -> int:
    """
    Estimate token count by running a zero-token generation.
    Ollama returns prompt_eval_count in the response, which is the token count
    of the input (system + all prior messages).
    """
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "num_predict": 1,  # generate only 1 token — we just want the count
        }
    })
    data = response.json()
    return data.get("prompt_eval_count", 0)

# In the agentic loop, check before each LLM call:
token_count = count_tokens_ollama(MODEL, conversation)
context_limit = 8192
headroom = context_limit - token_count - 512  # 512 reserved for the response

if headroom < 500:
    print(f"Warning: context nearly full ({token_count}/{context_limit} tokens used)")
    # trigger context management strategy
```

In practice, a typical troubleshooting session uses:
- System prompt: 400–600 tokens
- Initial user problem description: 50–100 tokens
- Each model response: 150–400 tokens
- Each pasted show command output: 200–2,000+ tokens depending on output

After 10–15 turns including several show outputs, you're typically at 4,000–6,000 tokens. Long outputs — full BGP tables, `show ospf database` — can use 1,000–3,000 tokens each.

---

## Strategy 1: Targeted Command Selection

The most effective strategy is avoiding the problem entirely. The agentic loop can prompt the model to request specific, scoped commands rather than broad dumps:

**Add to your system prompt:**
```
When troubleshooting, prefer targeted show commands over broad output dumps:
- Use "show ospf neighbor X.X.X.X" over "show ospf neighbor detail" for all neighbors
- Use "show route X.X.X.X/Y" over "show route" for the full table
- Use "show interfaces ge-0/0/1.0" over "show interfaces detail" for all interfaces
- Use "show log messages | match <keyword> | last 100" over raw log dumps
- If a broad command is necessary, always pipe through "| count" first to estimate size
```

This reduces the average show output size significantly. `show ospf neighbor 10.10.10.2` is 5–10 lines; `show ospf neighbor detail` for a router with 20+ neighbors is 200+ lines.

---

## Strategy 2: Output Truncation with Metadata Preservation

When a command produces more output than fits in context, truncate it but preserve the key metadata:

```python
def truncate_show_output(output: str, max_tokens: int = 800) -> str:
    """
    Truncate show command output while preserving structure.
    Returns the first and last portions with a count of omitted lines.
    """
    lines = output.strip().split('\n')
    
    # Rough token estimate: ~4 chars per token
    chars_budget = max_tokens * 4
    
    if len(output) <= chars_budget:
        return output
    
    # Keep first 60% and last 10% of budget; middle is usually repetitive data
    first_budget = int(chars_budget * 0.6)
    last_budget = int(chars_budget * 0.1)
    
    first_part = output[:first_budget]
    last_part = output[-last_budget:]
    
    omitted_chars = len(output) - first_budget - last_budget
    omitted_lines_est = omitted_chars // 80  # rough estimate
    
    return (
        first_part
        + f"\n\n[... {omitted_lines_est} lines omitted — output too long for context ...]\n\n"
        + last_part
    )
```

For routing tables and OSPF databases, the header rows contain the most useful information (summary counts, table version, router ID); the middle rows are individual prefixes that are often redundant for diagnosis; the footer may contain error counters or summary lines. Preserving header and footer while truncating the middle works well for these output types.

---

## Strategy 3: Two-Pass Summarization

For outputs that don't compress well with truncation, use the model itself to summarize before adding to conversation history. This uses an extra inference call but dramatically reduces context consumption:

```python
SUMMARIZE_PROMPT = """You are summarizing network device show output for a troubleshooting session.

The current problem: {current_problem}
The command run: {command}
The full output:

{output}

Summarize the key facts from this output relevant to the problem. Include:
- Any error states, down states, or anomalies
- Key counters that indicate problems (errors, drops, resets > 0)
- The overall health summary (X of Y neighbors up, X routes in table)
- Anything that stands out as relevant to the problem

Keep the summary under 200 words. Do not include raw data rows — only relevant facts and anomalies."""

def summarize_show_output(output: str, command: str, current_problem: str) -> str:
    """Use the model to summarize long show output before adding to conversation."""
    token_estimate = len(output) // 4
    
    if token_estimate < 400:  # short enough, don't summarize
        return output
    
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": MODEL,
        "messages": [
            {"role": "user", "content": SUMMARIZE_PROMPT.format(
                current_problem=current_problem,
                command=command,
                output=output[:8000]  # cap the input to summarization call too
            )}
        ],
        "stream": False,
        "options": {"temperature": 0.0, "num_ctx": 8192}
    })
    
    summary = response.json()["message"]["content"]
    return f"[Summarized output of '{command}']:\n{summary}"
```

The summarization call adds latency (1–3 seconds for an 8B model on M3 Pro) but keeps the main conversation context compact. The tradeoff: the model loses raw output details that might be relevant later in the diagnosis. Use summarization for background commands (interface statistics, routing table checks) and keep raw output for the specific output that's actively being analyzed.

---

## Strategy 4: Sliding Window with Progress Injection

For long troubleshooting sessions that grow beyond context capacity, use a sliding window: drop oldest turns but re-inject a summary of the troubleshooting progress:

```python
def trim_conversation(
    conversation: list,
    system_prompt: str,
    context_limit: int = 8192,
    reserved_for_response: int = 512
) -> list:
    """
    Trim conversation history to fit context limit.
    Preserves system prompt, injects a progress summary, keeps recent turns.
    """
    target_tokens = context_limit - reserved_for_response
    
    # Always keep the system prompt
    trimmed = [{"role": "system", "content": system_prompt}]
    
    # Build a progress summary from the trimmed turns
    # Ask the model to summarize what's been found so far
    if len(conversation) > 6:  # only summarize if there's meaningful history
        history_text = "\n".join(
            f"{m['role'].upper()}: {m['content'][:500]}"
            for m in conversation[1:-4]  # exclude system and last 4 turns
        )
        summary_response = requests.post("http://localhost:11434/api/chat", json={
            "model": MODEL,
            "messages": [{
                "role": "user",
                "content": f"Summarize this troubleshooting session progress in 3-4 sentences:\n\n{history_text}"
            }],
            "stream": False,
            "options": {"temperature": 0.0, "num_predict": 200}
        })
        progress_summary = summary_response.json()["message"]["content"]
        
        trimmed.append({
            "role": "user",
            "content": f"[Session context — earlier findings summarized]:\n{progress_summary}"
        })
        trimmed.append({
            "role": "assistant",
            "content": "Understood. Continuing the troubleshooting from where we are."
        })
    
    # Add the most recent turns (keep the last 4 turns minimum)
    recent_turns = conversation[-4:]
    trimmed.extend(recent_turns)
    
    return trimmed
```

**Key risk of sliding windows:** the model loses context on facts established early in the session — what the customer reported initially, what IP addresses belong to what devices, which interfaces are which. Mitigate by including device metadata in the system prompt itself (not just in conversation turns):

```
[In the Modelfile or prepended to every session]:
Device context:
- Hostname: core-rtr-1
- Platform: MX480
- Management IP: 192.168.1.1  
- Role: Core router, OSPF area 0 with 6 neighbors, eBGP to 2 upstreams
```

---

## Performance Impact on Apple Silicon

Context length has a direct impact on inference speed, relevant when using the model interactively on a Mac laptop. The two phases are affected differently:

**Prefill** (processing the prompt): scales approximately linearly with token count for small contexts on Apple Silicon's MLX implementation. Doubling context roughly doubles prefill time. For an 8B model on M4 Pro with 8192 tokens of context, prefill takes 3–6 seconds; at 2048 tokens it takes under 1 second.

**Decode** (generating the response): largely independent of context length for the first few hundred output tokens — the KV cache is already computed. But the KV cache itself consumes memory. At 8192 token context for an 8B model, the KV cache is approximately 8 GB (see model-internals for the formula). On a 16 GB MacBook Pro, that leaves only 8 GB for the model weights (4.5 GB for Q4_K_M 8B model) and the system — tight but workable. On 8 GB unified memory, 8192-token contexts cause paging to NAND, killing performance.

**Practical recommendations by hardware:**

| Hardware | Recommended num_ctx | Notes |
|----------|-------------------|-------|
| M3/M4 Pro 16 GB | 4096–8192 | Fits well; some paging risk at 8192 |
| M3/M4 Pro 24 GB | 8192–16384 | Comfortable at 8192; 16384 OK with Q4 |
| M4 Max 32–64 GB | 16384–32768 | 32K context comfortable with 8B model |
| M4 Max 128 GB | 32768+ | Essentially unconstrained for 8B models |

For the typical network engineer deployment on a 16 GB MacBook, `num_ctx 4096` is the safest setting — it keeps the KV cache under 4 GB and leaves room for the model weights and system. For most troubleshooting sessions (under 30 turns, show outputs kept to targeted commands), 4096 tokens is sufficient. Only extend to 8192 if sessions regularly hit the context limit.

---

## Setting Context Length in Ollama

```
# In Modelfile — set the context window
PARAMETER num_ctx 4096

# Or per-request via API:
options: {
  "num_ctx": 4096,
  "temperature": 0.1
}
```

Ollama defaults to 2048 tokens if `num_ctx` is not specified — well below what a real troubleshooting session needs. Always set it explicitly. The `num_ctx` value allocates the KV cache at model load time, not per-request, so it affects memory from the moment the model starts serving.

## Sources

- [Netmiko documentation](https://github.com/ktbyers/netmiko) — device connectivity layer for capturing show output
