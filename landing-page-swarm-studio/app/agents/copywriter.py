"""Copywriter agent definition."""

from __future__ import annotations

from pathlib import Path

from langchain.agents import create_agent
from langgraph_swarm import create_handoff_tool

_PROMPT = (
    Path(__file__).resolve().parent.parent / "prompts" / "copywriter.txt"
).read_text(encoding="utf-8")


def create_copywriter_agent(model: str):
    return create_agent(
        model,
        tools=[
            create_handoff_tool(
                agent_name="Designer",
                description="Transfer to Designer for layout, hierarchy, and UX.",
            ),
            create_handoff_tool(
                agent_name="Developer",
                description="Transfer to Developer for HTML/CSS/React implementation.",
            ),
        ],
        system_prompt=_PROMPT,
        name="Copywriter",
    )
