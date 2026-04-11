# Landing Page Swarm Studio

A multi-agent LangGraph Swarm project that turns one landing page request into a staged workflow across copy, design direction, and frontend implementation guidance.

Instead of asking one general-purpose LLM to do everything at once, this project splits the work across specialist agents with explicit handoff routes.

## 🧩 Core Idea

This project uses a simple swarm topology:

`Copywriter -> Designer -> Developer`

Each agent has a focused job:

- Copywriter handles messaging and positioning
- Designer handles layout and visual direction
- Developer handles implementation guidance

Only one agent is active at a time.

When needed, the current agent can use a handoff tool to pass control to the next specialist.

## 🌟 Why This Project Matters

Most single-agent workflows:

- mix strategy, design, and implementation in one response
- blur role boundaries
- make handoff logic implicit
- are harder to inspect and iterate

Landing Page Swarm Studio:

- separates responsibilities clearly
- uses explicit handoff paths
- keeps the workflow inspectable
- persists conversation state across turns
- makes multi-step page planning easier to reason about

This is a practical way to learn how LangGraph Swarm works in a real project.

## 📚 Reference

The core swarm idea and handoff-based multi-agent pattern in this project are based on LangGraph Swarm:

https://reference.langchain.com/python/langgraph-swarm

## 🏗️ Architecture Overview

User Request
  ↓
Copywriter Agent
  ↓ handoff
Designer Agent
  ↓ handoff
Developer Agent
  ↓
Final Response

The swarm is compiled with a checkpointer so the same thread can continue over time.

If SQLite checkpoint support is available, state is stored on disk.
Otherwise, the app falls back to in-memory checkpoints.

## 🧠 Swarm Model

### Copywriter Agent

Responsible for:

- headlines
- subheadlines
- CTAs
- messaging angle
- section-level copy ideas

### Designer Agent

Responsible for:

- section order
- layout direction
- visual hierarchy
- spacing and page structure
- UX-oriented presentation decisions

### Developer Agent

Responsible for:

- React structure guidance
- Tailwind implementation notes
- component breakdown
- responsive behavior guidance
- implementation realism

## ⚙️ Tech Stack

- Python: 3.10+
- Agent framework: LangChain
- Orchestration: LangGraph
- Multi-agent routing: `langgraph-swarm`
- LLM provider: OpenAI
- Config loading: `python-dotenv`

## 🧾 Setup Instructions

```bash
git clone <your-repo-url>
cd landing-page-swarm-studio

python3.11 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-your-openai-key
OPENAI_MODEL=openai:gpt-4o
```

`OPENAI_MODEL` is optional.

If omitted, the project defaults to `openai:gpt-4o`.

## 🚀 Running the Project

From the project root:

```bash
python -m app.main
```

If your environment has import path issues:

```bash
PYTHONPATH=. python -m app.main
```

## 🔄 Expected Flow

Example prompt:

```text
Create a landing page for an AI legal assistant for small law firms
```

The swarm should process the request through:

- Copywriter for messaging
- Designer for structure and visual direction
- Developer for implementation guidance

The app runs as a CLI and keeps using the same internal thread id so the conversation can continue across turns.

## 💾 Persistence

Conversation state is checkpointed through the swarm graph.

Current behavior:

- tries SQLite-backed persistence in `.swarm_state/checkpoints.sqlite`
- falls back to `InMemorySaver()` if SQLite checkpoint support is unavailable
- uses one fixed internal thread id for continued chat

## 🧾 Folder Structure

```text
landing-page-swarm-studio/
├── app/
│   ├── agents/
│   │   ├── copywriter.py
│   │   ├── designer.py
│   │   ├── developer.py
│   │   └── __init__.py
│   ├── prompts/
│   │   ├── copywriter.txt
│   │   ├── designer.txt
│   │   └── developer.txt
│   ├── utils/
│   │   ├── logger.py
│   │   └── prompt_loader.py
│   ├── config.py
│   ├── main.py
│   ├── model.py
│   └── swarm_graph.py
├── examples/
├── .env.example
├── README.md
└── requirements.txt
```

## 📌 Status

- `Done`: multi-agent swarm wiring
- `Done`: one-way handoff topology
- `Done`: CLI chat loop
- `Done`: persisted thread support with checkpoint fallback
- `In Progress`: prompt refinement for cleaner automatic handoffs
- `In Progress`: stronger output formatting and debugging visibility

## 🛠️ What Is Still Necessary

- stronger prompt instructions so agents hand off automatically every time
- corrected `Designer` prompt content so the role is not mixed with `Developer`
- better visibility into which agent is active and when handoffs happen
- more structured final output formatting
- optional tests or smoke checks for swarm setup and CLI flow

Right now, the project is useful as a learning and experimentation setup for LangGraph Swarm, but it still needs prompt cleanup and better observability before it feels production-ready.

## 🪄 License

This project is licensed under the MIT License.

## Author 👤

**Shivay Bajaj**

- GitHub: https://github.com/IDropCoins
