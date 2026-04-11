"""Prompt loading utilities with safe overrides and clear errors."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

_DEFAULT_PROMPT_DIR = Path(__file__).resolve().parent.parent / "prompts"


def _prompt_dir() -> Path:
    override = os.getenv("APP_PROMPT_DIR", "").strip()
    if not override:
        return _DEFAULT_PROMPT_DIR
    return Path(override).expanduser()


@lru_cache(maxsize=None)
def load_prompt(name: str) -> str:
    prompt_name = name.strip()
    if not prompt_name:
        raise ValueError("Prompt name cannot be empty.")

    specific_var = f"{prompt_name.upper()}_PROMPT_PATH"
    specific_path = os.getenv(specific_var, "").strip()
    prompt_path = (
        Path(specific_path).expanduser()
        if specific_path
        else _prompt_dir() / f"{prompt_name}.txt"
    )

    try:
        return prompt_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"Prompt file not found for '{prompt_name}' at '{prompt_path}'. "
            f"Set {specific_var} or APP_PROMPT_DIR to override."
        ) from exc
    except OSError as exc:
        raise RuntimeError(
            f"Failed to read prompt '{prompt_name}' from '{prompt_path}': {exc}"
        ) from exc
