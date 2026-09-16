"""Almasix Web starter kit (Prism + Conduit)."""

from __future__ import annotations

from pathlib import Path

__all__ = ["register", "stub_root"]


def stub_root() -> Path:
    return Path(__file__).resolve().parent / "stubs"


def register():
    """Entry point ``almasix.kits`` → ``web``."""
    from almasix.installer.kits import Kit

    return Kit(
        name="web",
        label="Web (Conduit)",
        description="Prism + Conduit auth, settings, teams, 2FA, notifications shell",
        folder="web",
        kind="web",
        needs_node=False,
        stub_root=stub_root(),
    )
