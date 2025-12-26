<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#"><img src="https://img.shields.io/badge/Status-Alpha-yellow" alt="Project Status"></a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#"><img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python Version"></a>
</p>

<br/>

<!--
Optional banner:
- Put a real image at: docs/decodifier_banner.png
- Or change the src to any hosted image you want.
-->
<p align="center">
  <img src="docs/decodifier_banner.png" alt="DeCodifier" width="700" />
</p>

<p align="center">
  <b>LLM Execution Layer for Real Code Bases</b><br/>
  Make LLMs read, write, patch, and scaffold projects — safely and locally.
</p>

<p align="center">
  <a href="https://github.com/ftrou/Decodifier/tree/main/docs"><b>Docs</b></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/ftrou/Decodifier/blob/main/ROADMAP.md"><b>Roadmap</b></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/ftrou/Decodifier/blob/main/GET_STARTED.md"><b>Quickstart</b></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/ftrou/Decodifier/blob/main/CONTRIBUTING.md"><b>Contributing</b></a>
</p>

<br/>

# DeCodifier v0.1 — Early Access

**DeCodifier is a local AI coding engine** that lets LLMs safely inspect and modify real projects.  
It provides file operations, a project registry, and tool-calling — so models can write real code **without uploading repos or sending your code to the cloud**.

---

## 🚀 Quickstart

```bash
pip install decodifier   # (coming soon)

python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -e .
uvicorn engine.app.main:app --reload
```

> 💡 **Try it live in ~20 seconds** (Provider Keys must be exported first)
```bash
python examples/openai_demo/decodifier_openai_demo.py
```

---

## 📂 Data Storage

DeCodifier stores project registry & conversations in:

```text
~/.decodifier
```

Override location:

```bash
export DECODIFIER_DATA_DIR=/your/path
```

---

## 🎬 Demo

Run the OpenAI demo client:

```bash
python clients/openai_demo/decodifier_openai_demo.py
```

What the model does automatically:

| Action | Where |
|--------|------|
| Inspect file tree | `decodifier/` |
| Scaffold feature | `scratch/todo_service/` |
| Create API + models | `api.py`, `models.py`, `storage.py` |
| Patch router | `engine/app/main.py` |
| Serve live feature | `http://127.0.0.1:8000` |

**No copy/paste. No hallucinated paths. No manual wiring.**

---

### 3️⃣ Hit the Endpoints

Create a todo:

```bash
curl -X POST "http://127.0.0.1:8000/api/todos" \
  -H "Content-Type: application/json" \
  -d '{"title":"Task"}'
```

List todos:

```bash
curl "http://127.0.0.1:8000/api/todos"
```

Mark done:

```bash
curl -X PUT "http://127.0.0.1:8000/api/todos/1/done"
```

Expected:

```json
{"id":1,"title":"Task","done":true}
```

🧠 **This proves:** DeCodifier isn’t code generation — it’s executable development.

---

## 🔑 Provider Keys (Required for Demos)

```bash
export OPENAI_API_KEY=your_key_here
# Anthropic / Groq support coming soon
```

⚠️ **Charges Warning**  
You are responsible for any model provider usage fees.  
DeCodifier performs **no metering or billing** on your behalf.

---

## 📦 Include DeCodifier in an LLM App

```python
from decodifier.client import DeCodifierClient, handle_decodifier_tool_call

client = DeCodifierClient("http://127.0.0.1:8000")

tool_result = handle_decodifier_tool_call(
    client,
    "decodifier_read_file",
    {
        "project_id": "my_app",
        "path": "src/main.py",
    },
)

print(tool_result)
```

Works with:
- GPT Tool Calling
- Claude Functions
- Custom agent frameworks

---

## 🩹 Patch Compatibility (Codex, GPT, Claude, Copilot)

DeCodifier accepts multiple patch formats and normalizes them automatically — so most LLMs “just work” out of the box.

Supported formats:

| Patch Style | Example Trigger | Status |
|-------------|-----------------|--------|
| Codex-style blocks | `*** Begin Patch` / `*** Update File:` | ✅ Auto-converted |
| Unified diff | `@@` context patches | ⚙️ Native |
| Inline replacements | `- old` / `+ new` | ⚙️ Normalized |
| Partial context edits | Missing full context | 🔍 Heuristic merge |
| Mixed output | Multiple formats in one response | 🧩 Best-fit parse |

Example accepted patches:

```diff
*** Begin Patch
*** Update File: app/main.py
@@
-print("Hello")
+print("Hello, World!")
```

```diff
--- a/app/main.py
+++ b/app/main.py
@@ -1,3 +1,3 @@
-print("Hello")
+print("Hello, World!")
```

If a patch fails, DeCodifier returns structured diagnostic output:

```json
{
  "error": "patch_mismatch",
  "missing_context": ["def process_user()"],
  "suggestion": "Retry with full file or rebase",
  "severity": "recoverable"
}
```

---

## 🧱 Architecture

```text
         LLM
          |
 (tool calls + JSON args)
          ↓
┌──────────────────────────────┐
│        DeCodifier API        │
├──────────────────────────────┤
│ file ops | search | patches  │
│ scaffolds | patterns (soon)  │
└──────────┬──────────┬────────┘
           |          |
      Projects     Registry
```

- Local-only by default  
- No repo uploads  
- Vendor neutral  

---

## 🧠 Roadmap Snapshot

| Stage | Target |
|-------|--------|
| v0.1  | MVP: file ops, scaffolding, dashboard |
| v0.2  | Patterns — compressed abstractions |
| v0.3  | Built-in test generation & smoke runs |
| v0.4  | Multi-agent iteration & PR drafts |
| v0.5  | SaaS (optional), team mode, cloud sync |

📌 Full roadmap → `ROADMAP.md`

---

## 🧩 Patterns (Optional Module — In Progress)

```text
decodifier_patterns/
├── fastapi/
│   ├── rest_resource.py
│   ├── auth_jwt.py
│   ├── sqlite_model.py
├── ml/
│   ├── inference_runner.py
│   ├── dataset_iterator.py
│   └── training_loop.py
```

Example usage:

```python
from decodifier_patterns.fastapi import rest_resource

user_api = rest_resource("User", fields=["name:str", "email:str"])
```

---

## 🎯 Who Is This For?

| Persona | Why They Care |
|---------|---------------|
| Solo Devs | Build features 2–5× faster |
| Agent Builders | Real execution layer for code agents |
| AI Engineers | Experiment with model orchestration |
| Startups | Ship prototypes before hiring a team |
| Researchers | Study agent reliability limits |

---

## ❌ Limitations (Important)

DeCodifier is **not**:
- a compiler  
- a linter  
- a static analyzer  
- a deployment tool  
- a hosted SaaS (yet)

It does **not guarantee correctness** — it accelerates development.  
**You still own your code.**

---

## 📜 License

MIT — Use freely.  
If you build a business on this, tell us — we’ll cheer you on.

---

## 🤝 Contributing

DeCodifier is early; rough edges expected. Contributions welcome.

**Help Wanted:**
- Patterns PRs
- Test coverage
- Windows env improvements
- Tutorials & videos
- Model provider adapters

---

## ⭐️ One-Sentence Summary

**DeCodifier gives LLMs the tools they need to code like developers — not autocomplete.**
