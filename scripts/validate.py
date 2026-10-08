# Copyright 2026 思维刻度 SavorCode
# SPDX-License-Identifier: Apache-2.0
"""Validate all atlas files against their schemas, taxonomies and cross-references.

    python scripts/validate.py

Errors make the script exit with status 1. Warnings (concrete paradigms without a `protocol` block, D-057)
are printed but do not fail the run. Class markers must be a superset of the markers of every active (non-deprecated)
concrete paradigm of the class (D-061, error).
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from atlas import CLASSES_FILE, ROOT, class_id, marker_files, paradigm_files, read_yaml, schemas, terms


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def add(self, path: Path, msg: str) -> None:
        self.errors.append(f"{path.relative_to(ROOT).as_posix()}: {msg}")

    def warn(self, path: Path, msg: str) -> None:
        self.warnings.append(f"{path.relative_to(ROOT).as_posix()}: warning: {msg}")


def validators() -> dict[str, Draft202012Validator]:
    all_schemas = schemas()
    registry = Registry().with_resources(
        [(s["$id"], Resource.from_contents(s)) for s in all_schemas.values()]
        + [(name, Resource.from_contents(s)) for name, s in all_schemas.items()]
    )
    return {name.split(".")[0]: Draft202012Validator(s, registry=registry) for name, s in all_schemas.items()}


def check_schema(v: Draft202012Validator, data, path: Path, rep: Report) -> bool:
    ok = True
    for err in v.iter_errors(data):
        where = "/".join(str(p) for p in err.absolute_path) or "(root)"
        rep.add(path, f"{where}: {err.message}")
        ok = False
    return ok


def load_file(path: Path, rep: Report):
    try:
        return read_yaml(path)
    except yaml.YAMLError as exc:
        rep.add(path, f"invalid YAML ({exc})")
        return None


def main() -> int:
    rep = Report()
    v = validators()
    recording, stimulus = terms("recording_modality"), terms("stimulus_modality")
    families, marker_types = terms("families"), terms("marker_types")

    vocab: dict[str, set[str]] = {}
    for name in ("regions", "constructs"):
        path = ROOT / "knowledge" / f"{name}.yaml"
        data = load_file(path, rep)
        if data is None or not check_schema(v["vocabulary"], data, path, rep):
            vocab[name] = set()
            continue
        ids = [t["id"] for t in data["terms"]]
        for dup in [i for i, n in Counter(ids).items() if n > 1]:
            rep.add(path, f"duplicate id '{dup}'")
        for i in ids:
            if not i.startswith(data["prefix"] + "."):
                rep.add(path, f"'{i}' does not match prefix {data['prefix']}")
        for t in data["terms"]:
            if "parent" in t and t["parent"] not in ids:
                rep.add(path, f"'{t['id']}' has unknown parent '{t['parent']}'")
        vocab[name] = set(ids)

    def check_modalities(path: Path, d: dict) -> None:
        for m in d.get("recording_modality", []):
            if m not in recording:
                rep.add(path, f"unknown recording_modality '{m}'")
        for m in d.get("stimulus_modality", []):
            if m not in stimulus:
                rep.add(path, f"unknown stimulus_modality '{m}'")

    markers: set[str] = set()
    for path in marker_files():
        d = load_file(path, rep)
        if d is None or not check_schema(v["marker"], d, path, rep):
            continue
        if path.stem != d["id"]:
            rep.add(path, f"file name must match id '{d['id']}'")
        if d["id"] in markers:
            rep.add(path, f"duplicate id '{d['id']}'")
        markers.add(d["id"])
        if d["type"] not in marker_types:
            rep.add(path, f"unknown marker type '{d['type']}'")
        check_modalities(path, d)
        for g in d.get("generators", []):
            if g["region"] not in vocab["regions"]:
                rep.add(path, f"unknown region '{g['region']}'")
        for x in d.get("indexes", []):
            if x["construct"] not in vocab["constructs"]:
                rep.add(path, f"unknown construct '{x['construct']}'")

    # Paradigm classes (D-057): paradigms/_classes.yaml
    classes: dict[str, dict] = {}
    data = load_file(CLASSES_FILE, rep) if CLASSES_FILE.exists() else None
    if not CLASSES_FILE.exists():
        rep.add(CLASSES_FILE, "class registry missing")
    elif data is not None and check_schema(v["paradigm_class"], data, CLASSES_FILE, rep):
        for t in data["terms"]:
            cid = t["id"]
            if cid in classes:
                rep.add(CLASSES_FILE, f"duplicate class id '{cid}'")
            classes[cid] = t
            fam = t["family"]
            if fam not in families:
                rep.add(CLASSES_FILE, f"class '{cid}': unknown family '{fam}'")
            elif not cid.startswith(families[fam]["prefix"] + "-"):
                rep.add(CLASSES_FILE, f"class '{cid}' should start with '{families[fam]['prefix']}-'")
            for m in t["markers"]:
                if m not in markers:
                    rep.add(CLASSES_FILE, f"class '{cid}': unknown marker '{m}'")
    instances: Counter = Counter()
    active: Counter = Counter()

    paradigms: set[str] = set()
    for path in paradigm_files():
        d = load_file(path, rep)
        if d is None or not check_schema(v["paradigm"], d, path, rep):
            continue
        pid = d["id"]
        if path.stem != pid:
            rep.add(path, f"file name must match id '{pid}'")
        if pid in paradigms:
            rep.add(path, f"duplicate id '{pid}'")
        paradigms.add(pid)
        fam = d["family"]
        if fam not in families:
            rep.add(path, f"unknown family '{fam}'")
        else:
            if path.parent.name != fam:
                rep.add(path, f"should be placed in paradigms/{fam}/")
            if not pid.startswith(families[fam]["prefix"] + "-"):
                rep.add(path, f"id should start with '{families[fam]['prefix']}-'")
        check_modalities(path, d)
        for m in d["markers"]:
            if m not in markers:
                rep.add(path, f"unknown marker '{m}' (add it under knowledge/markers/)")
        cls = d["class"]
        if cls != class_id(pid):
            rep.add(path, f"class '{cls}' must equal id without the serial suffix ('{class_id(pid)}')")
        if cls not in classes:
            rep.add(path, f"class '{cls}' is not registered in paradigms/_classes.yaml")
        else:
            instances[cls] += 1
            if d["status"] != "deprecated":
                active[cls] += 1
            if classes[cls]["family"] != fam:
                rep.add(path, f"family '{fam}' differs from family of class '{cls}' ('{classes[cls]['family']}')")
            # D-061 (confirmed 2026-10-05): class markers are the union of the markers of its active concrete paradigms
            if d["status"] != "deprecated":
                missing = [m for m in d["markers"] if m not in classes[cls]["markers"]]
                if missing:
                    rep.add(path, f"markers {missing} not in markers of class '{cls}' (class markers must be a superset, D-061)")
        proto = d.get("protocol")
        if proto is None:
            rep.warn(path, "no `protocol` block (D-057; to be defined in sprint 2)")
        elif "n_classes" in proto and "classes" in proto and proto["n_classes"] != len(proto["classes"]):
            rep.add(path, f"protocol.n_classes ({proto['n_classes']}) != number of protocol.classes ({len(proto['classes'])})")

    for cid in classes:
        if not instances[cid]:
            rep.add(CLASSES_FILE, f"class '{cid}' has no concrete paradigm")
        elif not active[cid]:
            rep.add(CLASSES_FILE, f"class '{cid}' has no active (non-deprecated) concrete paradigm")

    for line in rep.warnings:
        print(line)
    for line in rep.errors:
        print(line)
    print(f"{len(paradigms)} paradigms, {len(classes)} classes, {len(markers)} markers, {len(vocab['regions'])} regions, "
          f"{len(vocab['constructs'])} constructs checked; {len(rep.errors)} problem(s), {len(rep.warnings)} warning(s).")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
