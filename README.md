<p align="center">
  <img src="https://via.placeholder.com/600x140?text=DeCodifier" alt="DeCodifier" />
</p>

<p align="center">
  <b>LLM Execution Layer for Real Code Bases</b><br/>
  Make LLMs read, write, patch, and scaffold projects — safely and locally.
</p>

<p align="center">
  <a href="#">Docs</a> • 
  <a href="#">Roadmap</a> • 
  <a href="#">Quickstart</a> • 
  <a href="#">Contributing</a>
</p>

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](#)
[![Status](https://img.shields.io/badge/Status-Alpha-yellow)](#)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](#)

# DeCodifier v0.1 — Early Access

**DeCodifier is a local AI coding engine** that lets LLMs safely inspect and modify real projects.
It provides the file operations, project registry, and tool-calling required for LLMs to write actual code —
**without uploading repos or sending your code to the cloud**.

---

## 🚀 Quickstart

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e .
uvicorn engine.app.main:app --reload
```

DeCodifier stores project registry & conversations in `~/.decodifier`.

Override location:

```bash
export DECODIFIER_DATA_DIR=/your/path
```

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
from decodifier.tool_registry import DECODIFIER_TOOLS

client = DeCodifierClient("http://127.0.0.1:8000")

tool_result = handle_decodifier_tool_call(
    client,
    "decodifier_read_file",
    {
        "project_id": "my_app",
        "path": "src/main.py",
    }
)

print(tool_result)
```

Works with:  
- GPT Tool Calling  
- Claude Functions  
- Custom agent frameworks

---

## 🧪 Demo: Build a Todo API From Scratch

Run:

```bash
python clients/openai_demo/decodifier_openai_demo.py
```

Example LLM prompt:

> Create a FastAPI Todo service with CRUD and mark-done.  
> Put it in `scratch/todo_service/` and register the router in `main.py`.

Generated structure:

```
scratch/todo_service/
├── api.py
├── models.py
└── storage.py
```

Test it:

```bash
curl http://localhost:8000/todos
curl -X POST http://localhost:8000/todos -H "Content-Type: application/json" -d '{"title": "Task"}'
curl -X PUT http://localhost:8000/todos/1/done
```

---

## 🧱 Architecture

```
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
|-------|---------|
| v0.1  | MVP: file ops, scaffolding, dashboard |
| v0.2  | Patterns — compressed abstractions |
| v0.3  | Built-in test generation & smoke runs |
| v0.4  | Multi-agent iteration & PR drafts |
| v0.5  | SaaS (optional), team mode, cloud sync |

📌 Full roadmap → `ROADMAP.md`

---

## 🧩 Patterns (Optional Module — In Progress)

```
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

| Persona        | Why They Care |
|----------------|----------------|
| Solo Devs      | Build features 2–5× faster |
| Agent Builders | Real execution layer for code agents |
| AI Engineers   | Experiment with model orchestration |
| Startups       | Ship prototypes before hiring a team |
| Researchers    | Study agent reliability limits |

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
