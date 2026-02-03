# Airtable AI Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Status](https://img.shields.io/badge/status-early%20scaffold-yellowgreen)](#status)

Minimal Airtable → OpenAI pipeline to turn prompts into repeatable, auditable content workflows.

What this is
- A lightweight reference architecture for using Airtable as a control plane for AI-assisted content workflows.
- Shows how structured fields, state transitions, and prompt hygiene can turn AI from a “one-shot generator” into a repeatable, debuggable system.
- Current flow: Prompt → Draft → Polish → Final

What this is not
- Not a production-ready platform
- Not a “fully automated content machine”
- Not optimized for scale

The goal is clarity and operability, not hype.

Quick links
- Demo: see the Demo section below
- Prompts: /prompts
- Code: /src
- Docs: /docs
- Assets & examples: /assets and /examples

Table of contents
1. Quickstart
2. Demo & Example output
3. Repo structure
4. Environment variables
5. Contributing & contact
6. License

Quickstart (get running in <10 minutes)
1) Clone:
   git clone https://github.com/gabrieldcpaiva/airtable-ai-pipeline.git
   cd airtable-ai-pipeline

2) Copy env and add your keys:
   cp .env.example .env
   # edit .env and add your AIRTABLE/OPENAI keys

3) Install & run — pick the section that matches your environment:

- Python (if pipeline is Python)
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python src/run_pipeline.py

- Node (if pipeline is JS/TS)
  npm install
  npm run start
  # or: node src/index.js

- Docker (optional)
  docker build -t airtable-ai-pipeline .
  docker run --env-file .env airtable-ai-pipeline

Note: Replace the commands above with the actual run command if different. If you want, I can detect the runtime and tailor these commands.

Demo
Short recording showing the full flow:
- raw prompt → AI draft → polish pass → final output

![Demo GIF placeholder](assets/demo.gif)
Video link: https://drive.google.com/file/d/1zU5ZIXUa6BiQtdf6obWAqHvE9AckURm8/view?usp=drive_link

Example output (paste a real example from your demo)
- Raw prompt:
  "Write a LinkedIn intro announcing I'm offering no-code Airtable consultations for SMBs."

- Final output:
  "Excited to offer no-code Airtable consultations to small businesses — I help teams organize data, automate repetitive work, and ship workflows that actually get used. DM me if you want a short audit & sample automation."

Repo structure
- /prompts — prompt templates and variations
- /src — automation scripts and runner
- /docs — notes on architecture and decisions
- /assets — demo media and examples
- /examples — sample Airtable CSV / input records (recommended)

.env.example
AIRTABLE_API_KEY=your_airtable_api_key
AIRTABLE_BASE_ID=your_base_id
AIRTABLE_TABLE_NAME=Table1
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
LOG_LEVEL=info

Status
Early scaffold. Actively iterating. Built to be understood, not admired.

Why Airtable
Airtable provides:
- Explicit state transitions
- Human-readable logs
- Easy manual overrides when AI output goes wrong

In other words: when something breaks, you can see where and why.

Recommended quick additions
- Add demo GIF in /assets and link it at top.
- Add a short example record in /examples so people can import and try.
- Add CONTRIBUTING.md (1 paragraph) + CODE_OF_CONDUCT.md.
- Add .github/ISSUE_TEMPLATE/bug_report.md and feature_request.md and PULL_REQUEST_TEMPLATE.md.
- Add a .env.example file (included above) and commit it.
- Add a basic GitHub Actions workflow to run lint/tests and show a CI badge.

Contributing & contact
Open issues or PRs. For quick questions or consulting, DM me on LinkedIn.

License
MIT — see LICENSE file.

CHANGELOG / Releases
Consider adding CHANGELOG.md or using GitHub Releases for notable updates.