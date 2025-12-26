🚀 DeCodifier — Local Setup (ZIP Download Edition)

Welcome!
This guide assumes you downloaded this repo as a .zip file.

1️⃣ Create a Python environment
cd decodifier-main
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

2️⃣ Install dependencies
pip install --upgrade pip
pip install -e .
pip install openai     # required for the demo client

3️⃣ Start the engine
uvicorn engine.app.main:app --reload


Your local API is now running at:

http://127.0.0.1:8000

🔑 Required Keys (for Demos)
export OPENAI_API_KEY="your-key-here"


⚠️ Usage Charges Warning
Running demos may call external APIs.
You are responsible for any usage fees from providers.
DeCodifier performs no billing or metering.

🧪 Run the OpenAI Todo Demo
python clients/openai_demo/decodifier_openai_demo.py


Expected behavior:

The model inspects the project

Generates a Todo feature

Wires it into the app

🔍 Test the Todo API

With the engine running:

curl http://127.0.0.1:8000/api/todos
curl -X POST http://127.0.0.1:8000/api/todos -H "Content-Type: application/json" -d '{"title":"First task"}'
curl -X PUT http://127.0.0.1:8000/api/todos/1/done

🛡 Troubleshooting
Issue	Fix
KeyError: 'path'	Update to latest / ensure defensive tool adapter applied
ModuleNotFoundError: openai	pip install openai
Address in use	Kill existing uvicorn or use port --port 8001
Windows path issues	Use WSL or GitBash recommended
📁 Data Storage

DeCodifier stores state here:

~/.decodifier


Move or override with:

export DECODIFIER_DATA_DIR=/your/custom/dir

🎉 Next Steps

Connect to other LLMs (Claude, Groq, Gemini)

Try patch-based editing: tools → decodifier_patch_file

Add custom patterns in decodifier_patterns/

DeCodifier turns LLMs into real coding assistants — not autocomplete.
Build something cool. And if you ship a product on top, tell us. We'll cheer you on. 🚀
