"""Developer agent definition."""

from __future__ import annotations

from collections.abc import Sequence

from langchain.agents import create_agent

from app.model import get_model_id
from app.utils.prompt_loader import load_prompt


def build_developer_agent(*, tools: Sequence[object], model: str | None = None):
    prompt = load_prompt("developer")
    return create_agent(
        model or get_model_id(),
        tools=list(tools),
        system_prompt=prompt,
        name="developer",
    )


def create_developer_agent(model: str):
    return build_developer_agent(tools=[], model=model)
