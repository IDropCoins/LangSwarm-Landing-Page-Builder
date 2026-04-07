"""Developer agent definition."""

from __future__ import annotations

from pathlib import Path

from langchain.agents import create_agent
from langgraph_swarm import create_handoff_tool

_PROMPT = (
    Path(__file__).resolve().parent.parent / "prompts" / "developer.txt"
).read_text(encoding="utf-8")


def create_developer_agent(model: str):
    return create_agent(
        model,
        tools=[
            create_handoff_tool(
                agent_name="Copywriter",
                description="Transfer to Copywriter for wording and CTAs.",
            ),
            create_handoff_tool(
                agent_name="Designer",
                description="Transfer to Designer for visual layout and design system.",
            ),
        ],
        system_prompt=_PROMPT,
        name="Developer",
    )
