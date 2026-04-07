"""create_swarm + handoffs + compile."""

from __future__ import annotations

from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.checkpoint.memory import InMemorySaver
from langgraph_swarm import create_swarm

from app.agents import (
    create_copywriter_agent,
    create_designer_agent,
    create_developer_agent,
)
from app.model import get_model_id


def create_swarm_app(
    model: str | None = None,
    *,
    checkpointer: BaseCheckpointSaver | None = None,
):
    mid = model or get_model_id()
    agents = [
        create_copywriter_agent(mid),
        create_designer_agent(mid),
        create_developer_agent(mid),
    ]
    workflow = create_swarm(agents, default_active_agent="Copywriter")
    return workflow.compile(checkpointer=checkpointer or InMemorySaver())
