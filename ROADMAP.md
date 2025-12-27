# DeCodifier Roadmap

## v0.1
- Local alpha - core engine proven
- Tool calling over HTTP
- Safe file operations and audit events

## v0.2
- Diff previews + dry-run
- Compiler hooks
- Expanded examples (Flask, Next.js)

## v0.3 — Spec → Compile → Pip Install

Decodifier v0.3 is focused on one outcome:

🟢 Turn Decodifier into a pip-installable compiler that LLMs can call to safely update software.

This milestone completes the core loop:

🧠 LLM intent → 🧾 Decodifier Spec → 🔧 Compiler → 🧱 Codebase updated

🎯 Core Objectives
Goal	Description
📦 Pip Package	pip install decodifier + basic CLI
🧩 Plugin Architecture	Register custom patterns, compilers, and validators
🛠️ Pattern Runtime v0.3	Runtime to apply patch strategies (append, merge, rewrite, scaffold)
🧪 Static Linting	Preflight validation + rollback on failure
📜 Spec v0.2 Draft	Better schema for multi-file + multi-language projects
🔄 LLM ↔️ Compiler Loop	Reference client for GPT function calling & local LLMs
✳️ New Concepts Planned

These concepts will define the category:

Concept	Why it matters
🔐 Intent Firewall	LLM can propose changes, but compiler confirms & applies
🧱 Pattern Packs	Reusable update/merge behaviors bundled like plugins
🧬 Spec Packs	Declarative templates for common app structures
🔄 Patch Scopes	File-level / module-level / project-level safety boundaries
🥽 Code Execution Layer	Run & test changes without giving the LLM execution access
📌 Anti-Goals (for clarity)

We will not:

❌ Become a code-gen model
❌ Run arbitrary code from LLMs
❌ Replace IDEs
❌ Try to be a one-click app builder

We will:

✅ Become the missing layer between AI and codebases
✅ Enable safe AI development workflows
✅ Define the category of LLM Compilers

🧰 Help Wanted

If you want to contribute, here are good entry points:

Pattern runtime examples

Spec schema design v0.2

Python AST merge utilities

Testing harness for rollback scenarios

CLI interface design

Comment below, open PRs, or DM on X: @ftrouAI

🧭 Version Plan
v0.3 — Pip package + runtime MVP
v0.4 — Plugin architecture + spec packs
v0.5 — Rollbacks, tests, stability → Public Beta

🧩 Add this badge to show we're building in the open
[![Open Roadmap](https://img.shields.io/badge/status-building-yellow.svg)](#)

🚀 If you're reading this:

This is the moment to follow the repo.
Decodifier is the first compiler for AI-generated software.

👉 Star the repo
👉 Watch releases
👉 Join the category early

Discussion Prompt

What’s the single biggest gap in current AI coding workflows?
Reply below — we'll use this to shape v0.3.

End of Issue

Tag: roadmap, v0.3, category-building, help-wanted
