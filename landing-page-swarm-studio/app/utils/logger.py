"""Logs active agent and handoff tool calls."""

from __future__ import annotations

import logging
import re
from typing import Any

_LOG = logging.getLogger("landing_page_swarm")
_TRANSFER_TOOL = re.compile(r"^transfer_to_")


def setup_logging(level: int = logging.INFO) -> None:
    if not _LOG.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        )
        _LOG.addHandler(handler)
    _LOG.setLevel(level)
    logging.captureWarnings(True)


def log_swarm_result(result: dict[str, Any]) -> None:
    active = result.get("active_agent")
    if active:
        _LOG.info("Active agent: %s", active)

    for msg in result.get("messages") or []:
        extra = getattr(msg, "additional_kwargs", None) or {}
        tool_calls = getattr(msg, "tool_calls", None) or extra.get("tool_calls")
        if not tool_calls:
            continue
        for tc in tool_calls:
            name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", None)
            if name and _TRANSFER_TOOL.match(str(name)):
                _LOG.info("Handoff tool invoked: %s", name)
