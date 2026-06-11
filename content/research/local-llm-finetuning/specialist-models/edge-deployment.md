---
title: "Edge Deployment and Device Integration"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "Deploying a fine-tuned network engineer specialist LLM disconnected on a Mac laptop, connecting it to physical network devices via SSH, and building an agentic command loop that can read device state and propose or execute commands."
tags: ["edge-deployment", "local-inference", "llm-agent", "network-automation", "ssh", "netmiko", "ollama", "macos"]
categories: ["technology"]
research_area: "local-llm-finetuning/specialist-models"
source_urls:
  - "https://ollama.com"
  - "https://github.com/ktbyers/netmiko"
  - "https://llama-cpp-python.readthedocs.io/"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The final step is deploying the fine-tuned model on a Mac laptop, connecting it to physically attached network devices, and building an interaction layer that lets the model query device state and propose or execute commands. The deployment is fully disconnected: no internet required, no API calls, everything runs locally. The core stack is Ollama (model serving), Netmiko (SSH device connectivity), and a thin Python agentic loop that routes between the LLM and the device.

## Key Facts

- **Model serving:** Ollama with the merged GGUF model — local REST API on port 11434
- **Device connectivity:** Netmiko (Python) — SSH sessions to JunOS/IOS devices with platform-aware prompt handling
- **Inference speed (M3/M4 Pro, 7B Q4):** 18–28 tokens/second (fast enough for interactive use)
- **Memory footprint:** ~4.5 GB RAM for 7B Q4_K_M model; comfortably fits in 16 GB laptop
- **Context window used:** 4096–8192 tokens — enough for most troubleshooting dialogs including pasted show output
- **Human-in-the-loop:** All commands proposed, human approves before execution (configurable)

## What It Is / How It Works

**Model serving with Ollama.** Ollama runs the GGUF model as a local REST API server. After the model file is placed and a `Modelfile` is created, the model is available for inference with no internet connection:

```bash
# Create Modelfile for the Juniper expert
cat > ~/models/Modelfile.juniper << 'EOF'
FROM /Users/yourname/models/juniper-expert-v1.gguf

SYSTEM """You are a senior Juniper network engineer with deep expertise in JunOS across the full product line: EX Series switches, QFX Series, MX Series routers, SRX Series firewalls.

Your role is to translate English descriptions into JunOS commands, generate configurations, troubleshoot problems step by step, and interpret show command output. Always use JunOS syntax. If uncertain, say so."""

PARAMETER temperature 0.1
PARAMETER top_p 0.9
PARAMETER num_ctx 8192
PARAMETER repeat_penalty 1.1
EOF

# Register and test
ollama create juniper-expert -f ~/models/Modelfile.juniper
ollama run juniper-expert "Show me the command to check OSPF neighbor state"
```

**Temperature setting.** For a network expert model, use `temperature 0.1`. Network commands are deterministic — there's usually one correct syntax. Higher temperature causes the model to explore alternatives, which for CLI commands means generating plausible-but-wrong variations. Low temperature biases toward the most probable (most-trained) output.

**Connecting to devices with Netmiko.** Netmiko is a Python library that manages SSH sessions to network devices with platform-aware prompt detection and command handling. It knows JunOS needs `>` prompt detection, IOS needs `#`, and handles `More` paging automatically.

```python
from netmiko import ConnectHandler

# Juniper connection profile
juniper_device = {
    "device_type": "juniper_junos",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "your_password",
    # For key-based auth:
    # "use_keys": True,
    # "key_file": "~/.ssh/network_key",
}

# Cisco IOS-XE connection profile
cisco_device = {
    "device_type": "cisco_ios",
    "host": "10.0.0.1",
    "username": "admin",
    "password": "your_password",
    "secret": "enable_password",   # for enable mode
}

# Execute a show command
with ConnectHandler(**juniper_device) as conn:
    output = conn.send_command("show ospf neighbor")
    print(output)

# For config mode commands (JunOS)
with ConnectHandler(**juniper_device) as conn:
    config_commands = [
        "set interfaces ge-0/0/0 description 'uplink-sw2'",
        "commit"
    ]
    output = conn.send_config_set(config_commands)
```

**The agentic interaction loop.** The core pattern is: model proposes an action (a command to run), engineer approves, system executes on the device, output is fed back to the model for interpretation. This is a minimal tool-use agent loop without a complex framework:

```python
import requests
import json
from netmiko import ConnectHandler

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "juniper-expert"

def query_llm(messages: list) -> str:
    """Send conversation history to local Ollama model and get response."""
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "options": {"temperature": 0.1, "num_ctx": 8192}
    })
    return response.json()["message"]["content"]

def run_command_on_device(device_conn, command: str) -> str:
    """Execute a command on the connected network device."""
    return device_conn.send_command(command, read_timeout=30)

def main():
    # Connect to device
    device_config = {
        "device_type": "juniper_junos",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "admin_password",
    }
    
    conversation = []  # maintains full dialog history
    
    print("Juniper Expert — connected to", device_config["host"])
    print("Type your question or describe the problem. Type 'exit' to quit.\n")
    
    with ConnectHandler(**device_config) as conn:
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                break
            
            conversation.append({"role": "user", "content": user_input})
            
            # Get model response
            response = query_llm(conversation)
            print(f"\nExpert: {response}\n")
            conversation.append({"role": "assistant", "content": response})
            
            # Check if model is proposing a command to run
            # Simple heuristic: look for code blocks with CLI commands
            if "```" in response:
                proposed_cmds = extract_commands(response)
                for cmd in proposed_cmds:
                    print(f"  → Proposed command: {cmd}")
                    approval = input("  Run this command? (y/n): ").strip().lower()
                    if approval == "y":
                        output = run_command_on_device(conn, cmd)
                        print(f"\n  Device output:\n{output}\n")
                        # Feed output back into conversation
                        conversation.append({
                            "role": "user",
                            "content": f"Command executed: `{cmd}`\n\nDevice output:\n```\n{output}\n```\n\nWhat does this tell us?"
                        })
                        # Get interpretation
                        interpretation = query_llm(conversation)
                        print(f"Expert: {interpretation}\n")
                        conversation.append({"role": "assistant", "content": interpretation})

def extract_commands(text: str) -> list:
    """Extract commands from code blocks in model response."""
    import re
    # Match content inside ``` blocks (with or without language tag)
    blocks = re.findall(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)
    commands = []
    for block in blocks:
        # Only include lines that look like CLI commands (not config blocks)
        for line in block.strip().split("\n"):
            line = line.strip()
            if line.startswith("show ") or line.startswith("ping ") or line.startswith("traceroute "):
                commands.append(line)
    return commands

if __name__ == "__main__":
    main()
```

**Safety constraints in the agent loop.** The loop above requires human approval for every command. This is the correct default for a network device assistant. Configurable variations:

- *Read-only mode:* Only execute `show` commands automatically; require explicit approval for anything that could change state
- *Dry-run mode:* The model generates commands but never executes them — output is copy-paste for the engineer to run manually. Useful during initial testing of the model's command quality
- *Supervised autonomous mode:* Allow automatic execution of pre-approved command classes (read-only show commands only); queue config commands for batch human approval

For a production deployment on a network management laptop, read-only mode with dry-run for config generation is the recommended starting point. Move to supervised autonomous only after validating the model's command accuracy over several weeks of use.

**Managing conversation context.** Long troubleshooting sessions accumulate context. A 8192-token context window fits approximately 6,000–7,000 words of conversation — roughly 30–50 exchanges including show command outputs. For longer sessions:

- Summarize the troubleshooting progress periodically: "Here's what we've found so far: [summary]. Continue troubleshooting from here."
- Trim old context manually or implement a sliding window
- For the context prompt, always re-inject the current device's hostname, platform, and any known environmental facts (what IP is the upstream peer, what VLAN carries management traffic, etc.) to avoid the model losing context on key facts

**Deployment checklist:**

1. Install Ollama: `brew install ollama` — starts as a launchd service automatically on Mac
2. Place GGUF model file: `~/Library/Application Support/ollama/models/` or use `ollama create`
3. Test inference: `ollama run juniper-expert "show bgp summary"` — should respond with correct JunOS syntax
4. Install Netmiko: `pip install netmiko`
5. Test device connectivity: basic ping and SSH to each device
6. Configure SSH keys on devices (avoid password auth for automated sessions)
7. Run the agent loop: `python network_expert_agent.py`

**SSH key setup on JunOS for keyless access:**
```
# On JunOS device
set system login user admin authentication ssh-rsa "ssh-rsa AAAA... macbook@company"
```

**SSH key setup on Cisco IOS-XE:**
```
ip ssh pubkey-chain
  username admin
    key-string
      AAAA... (paste key content here)
    exit
  exit
```

**Context persistence across sessions.** For an engineer using this daily, it's useful to persist conversation summaries. A simple approach: at session end, ask the model to summarize what was found and what was resolved, save to a timestamped file alongside the device hostname and IP. This creates a lightweight log of AI-assisted troubleshooting sessions.

## Sources

- [Ollama](https://ollama.com) — local model serving with macOS launchd integration
- [Netmiko](https://github.com/ktbyers/netmiko) — SSH to network devices with platform-aware handling
- [llama-cpp-python](https://llama-cpp-python.readthedocs.io/) — alternative to Ollama for direct Python integration
- [Ollama Python library](https://github.com/ollama/ollama-python) — cleaner Python API than raw REST
