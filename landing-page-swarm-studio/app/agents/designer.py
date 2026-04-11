"""Designer agent definition."""

from __future__ import annotations

from collections.abc import Sequence

from langchain.agents import create_agent

from app.model import get_model_id
from app.utils.prompt_loader import load_prompt


def build_designer_agent(*, tools: Sequence[object], model: str | None = None):
    prompt = load_prompt("designer")
    return create_agent(
        model or get_model_id(),
        tools=list(tools),
        system_prompt=prompt,
        name="designer",
    )


def create_designer_agent(model: str):
    return build_designer_agent(tools=[], model=model)
