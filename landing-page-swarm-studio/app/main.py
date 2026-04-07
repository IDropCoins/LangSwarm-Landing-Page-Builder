"""CLI entry point (run the swarm)."""

from __future__ import annotations

import argparse
import sys
import uuid

from app.config import get_settings
from app.model import get_model_id
from app.swarm_graph import create_swarm_app
from app.utils.logger import log_swarm_result, setup_logging


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Landing page swarm (LangGraph Swarm)")
    p.add_argument("-m", "--message", help="Single user message (else REPL)")
    p.add_argument("-t", "--thread-id", default=None, help="Thread id for memory")
    return p.parse_args()


def main() -> None:
    setup_logging()
    settings = get_settings()
    if not settings.openai_api_key:
        print("Set OPENAI_API_KEY in .env", file=sys.stderr)
        sys.exit(1)

    args = _parse_args()
    app = create_swarm_app(model=get_model_id())
    thread_id = args.thread_id or str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    if args.message:
        result = app.invoke(
            {"messages": [{"role": "user", "content": args.message}]},
            config,
        )
        log_swarm_result(result)
        _print_messages(result)
        return

    print(f"Thread id: {thread_id} (use --thread-id to resume)\n")
    while True:
        try:
            line = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            break
        result = app.invoke(
            {"messages": [{"role": "user", "content": line}]},
            config,
        )
        log_swarm_result(result)
        _print_messages(result)


def _print_messages(result: dict) -> None:
    for msg in result.get("messages") or []:
        pretty = getattr(msg, "pretty_print", None)
        if callable(pretty):
            pretty()
        else:
            print(msg)


if __name__ == "__main__":
    main()
