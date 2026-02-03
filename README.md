# What this is

This repository is a **lightweight reference architecture** for using Airtable as a control plane for AI-assisted content workflows.

It shows how structured fields, state transitions, and prompt hygiene can turn AI from a “one-shot generator” into a repeatable, debuggable system.

The current focus is a simple pipeline:
**Prompt → Draft → Polish → Final**

This is not a SaaS, SDK, or finished framework. It’s a working pattern.

# What this is not
	•	Not a production-ready platform
	•	Not a “fully automated content machine”
	•	Not optimized for scale

The goal is clarity and operability, not hype.

# Why Airtable

Airtable works well here because it provides:
	•	Explicit state transitions
	•	Human-readable logs
	•	Easy manual overrides when AI output goes wrong

In other words: when something breaks, you can see where and why.

# Demo

Short screen recording showing the full flow:
	•	raw prompt
	•	AI draft
	•	polish pass
	•	final output

[(Video link here)](https://drive.google.com/file/d/1zU5ZIXUa6BiQtdf6obWAqHvE9AckURm8/view?usp=sharing)

# Repo structure
	•	/prompts — prompt templates and variations
	•	/src — placeholder for automation / scripts
	•	/docs — notes on architecture and decisions
	•	/assets — demo media and examples

# Status

Early scaffold. Actively iterating.
Built to be understood, not admired.
