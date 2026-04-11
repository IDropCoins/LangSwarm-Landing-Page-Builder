"""Swarm graph assembly and handoff topology."""

from __future__ import annotations

from pathlib import Path

from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.checkpoint.memory import InMemorySaver
from langgraph_swarm import create_handoff_tool, create_swarm

from app.agents.copywriter import build_copywriter_agent
from app.agents.designer import build_designer_agent
from app.agents.developer import build_developer_agent
from app.model import get_model_id


def _default_checkpointer() -> BaseCheckpointSaver:
    """Use SQLite-backed checkpoints when available; fallback to in-memory."""
    try:
        from langgraph.checkpoint.sqlite import SqliteSaver

        db_dir = Path(__file__).resolve().parent.parent / ".swarm_state"
        db_dir.mkdir(parents=True, exist_ok=True)
        db_path = db_dir / "checkpoints.sqlite"
        return SqliteSaver.from_conn_string(str(db_path))
    except Exception:
        return InMemorySaver()


def build_swarm(
    model: str | None = None,
    *,
    checkpointer: BaseCheckpointSaver | None = None,
):
    """Build and compile the three-agent swarm with designer/developer handoffs."""
    mid = model or get_model_id()

    handoff_to_designer = create_handoff_tool(
        agent_name="designer",
        description=(
            "Hand off to the Designer Agent for layout, visual direction, and UX structure."
        ),
    )

    handoff_to_developer = create_handoff_tool(
        agent_name="developer",
        description=(
            "Hand off to the Developer Agent for React structure, Tailwind notes, "
            "and implementation guidance."
        ),
    )

    copywriter = build_copywriter_agent(tools=[handoff_to_designer], model=mid)
    designer = build_designer_agent(tools=[handoff_to_developer], model=mid)
    developer = build_developer_agent(tools=[], model=mid)

    swarm = create_swarm(
        agents=[copywriter, designer, developer],
        default_active_agent="copywriter",
    )
    return swarm.compile(checkpointer=checkpointer or _default_checkpointer())


def create_swarm_app(
    model: str | None = None,
    *,
    checkpointer: BaseCheckpointSaver | None = None,
):
    """Build the compiled swarm graph; forwards to ``build_swarm`` with the same arguments."""
    return build_swarm(model=model, checkpointer=checkpointer)
