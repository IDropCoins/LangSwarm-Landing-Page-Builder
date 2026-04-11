from __future__ import annotations

import sys
from pathlib import Path

# Allow `python -m main` or `python main.py` from the `app/` directory.
_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from langchain_core.messages import HumanMessage

from app.swarm_graph import build_swarm

THREAD_ID = "landing-page-demo-1"


def main():
    """Run a multi-turn CLI so the same thread can continue over time."""
    graph = build_swarm()
    config = {"configurable": {"thread_id": THREAD_ID}}

    print(f"Thread: {THREAD_ID}")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter your landing page request: ").strip()
        if not user_input:
            print("Please enter a valid request.")
            continue
        if user_input.lower() in {"exit", "quit"}:
            break

        result = graph.invoke(
            {
                "messages": [HumanMessage(content=user_input)],
            },
            config=config,
        )

        messages = result.get("messages", [])
        if not messages:
            print("No response returned.")
            continue

        final_message = messages[-1]
        print("\n=== Final Response ===\n")
        print(final_message.content)
        print()


if __name__ == "__main__":
    main()
