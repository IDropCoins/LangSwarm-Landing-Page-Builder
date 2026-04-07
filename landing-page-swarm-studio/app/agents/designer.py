"""Designer agent definition."""

from __future__ import annotations

from pathlib import Path

from langchain.agents import create_agent
from langgraph_swarm import create_handoff_tool

_PROMPT = (
    Path(__file__).resolve().parent.parent / "prompts" / "designer.txt"
).read_text(encoding="utf-8")


def create_designer_agent(model: str):
    return create_agent(
        model,
        tools=[
            create_handoff_tool(
                agent_name="Copywriter",
                description="Transfer to Copywriter for headlines, copy, and tone.",
            ),
            create_handoff_tool(
                agent_name="Developer",
                description="Transfer to Developer for markup and styling code.",
            ),
        ],
        system_prompt=_PROMPT,
        name="Designer",
    )
