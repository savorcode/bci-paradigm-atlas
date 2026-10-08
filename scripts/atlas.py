# Copyright 2026 思维刻度 SavorCode
# SPDX-License-Identifier: Apache-2.0
"""Shared loading utilities for the BCI Paradigm Atlas."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CLASSES_FILE = ROOT / "paradigms" / "_classes.yaml"


def read_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def terms(name: str) -> dict[str, dict]:
    return {t["id"]: t for t in read_yaml(ROOT / "taxonomy" / f"{name}.yaml")["terms"]}


def schemas() -> dict[str, dict]:
    return {p.name: json.loads(p.read_text(encoding="utf-8")) for p in (ROOT / "schema").glob("*.schema.json")}


@dataclass
class Atlas:
    paradigms: dict[str, tuple[Path, dict]] = field(default_factory=dict)
    classes: dict[str, dict] = field(default_factory=dict)
    markers: dict[str, tuple[Path, dict]] = field(default_factory=dict)
    regions: dict[str, dict] = field(default_factory=dict)
    constructs: dict[str, dict] = field(default_factory=dict)


def paradigm_files() -> list[Path]:
    return sorted(p for p in (ROOT / "paradigms").rglob("*.yaml") if not p.name.startswith("_"))


def marker_files() -> list[Path]:
    return sorted(p for p in (ROOT / "knowledge" / "markers").glob("*.yaml") if not p.name.startswith("_"))


def class_id(paradigm_id: str) -> str:
    """Paradigm class of a concrete paradigm id: MOT-MI-001 -> MOT-MI (D-057)."""
    return paradigm_id.rsplit("-", 1)[0]


def load() -> Atlas:
    atlas = Atlas()
    if CLASSES_FILE.exists():
        atlas.classes = {t["id"]: t for t in (read_yaml(CLASSES_FILE) or {}).get("terms", [])}
    for p in paradigm_files():
        d = read_yaml(p)
        atlas.paradigms[d["id"]] = (p, d)
    for p in marker_files():
        d = read_yaml(p)
        atlas.markers[d["id"]] = (p, d)
    atlas.regions = {t["id"]: t for t in read_yaml(ROOT / "knowledge" / "regions.yaml")["terms"]}
    atlas.constructs = {t["id"]: t for t in read_yaml(ROOT / "knowledge" / "constructs.yaml")["terms"]}
    return atlas
