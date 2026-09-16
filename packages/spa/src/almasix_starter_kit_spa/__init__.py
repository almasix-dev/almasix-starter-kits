"""Almasix SPA starter kits (Inertia — React / Vue / Svelte)."""

from __future__ import annotations

from pathlib import Path

__all__ = ["react", "vue", "svelte", "stub_root"]


def stub_root() -> Path:
    return Path(__file__).resolve().parent / "stubs"


def _spa(name: str, label: str, frontend: str, inertia_pkg: str):
    from almasix.installer.kits import Kit

    return Kit(
        name=name,
        label=label,
        description=f"Official {inertia_pkg} client, same product surface as Web",
        folder=f"spa/{frontend}",
        kind="spa",
        frontend=frontend,
        force_stack="tailwind",
        needs_node=True,
        stub_root=stub_root(),
    )


def react():
    """Entry point ``almasix.kits`` → ``react``."""
    return _spa("react", "SPA — React + Inertia", "react", "@inertiajs/react")


def vue():
    """Entry point ``almasix.kits`` → ``vue``."""
    return _spa("vue", "SPA — Vue + Inertia", "vue", "@inertiajs/vue3")


def svelte():
    """Entry point ``almasix.kits`` → ``svelte``."""
    return _spa("svelte", "SPA — Svelte + Inertia", "svelte", "@inertiajs/svelte")
