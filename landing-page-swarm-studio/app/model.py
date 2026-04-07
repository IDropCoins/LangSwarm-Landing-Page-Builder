"""LLM setup (OpenAI / LangChain)."""

from __future__ import annotations

from app.config import Settings, get_settings


def get_model_id(settings: Settings | None = None) -> str:
    """Model id for `langchain.agents.create_agent` (e.g. `openai:gpt-4o`)."""
    s = settings or get_settings()
    return s.openai_model
