"""Almasix API starter kit (Signet personal access tokens)."""

from __future__ import annotations

from pathlib import Path

__all__ = ["register", "stub_root"]


def stub_root() -> Path:
    return Path(__file__).resolve().parent / "stubs"


def register():
    """Entry point ``almasix.kits`` → ``api``."""
    from almasix.installer.kits import Kit

    return Kit(
        name="api",
        label="API (Signet)",
        description="JSON API polarity + Signet personal access tokens (no session UI)",
        folder="api",
        kind="api",
        force_stack="none",
        stub_root=stub_root(),
    )
