# Copyright 2026 思维刻度 SavorCode
# SPDX-License-Identifier: Apache-2.0
"""Export the atlas as a knowledge graph (dist/graph.json) and print coverage statistics.

    python scripts/build_graph.py
"""

from __future__ import annotations

import json
from collections import Counter

from atlas import ROOT, load


def main() -> None:
    a = load()
    nodes, edges = [], []

    for rid, t in a.regions.items():
        nodes.append({"id": rid, "kind": "region", "en": t["en"], "zh": t["zh"]})
    for cid, t in a.constructs.items():
        nodes.append({"id": cid, "kind": "construct", "en": t["en"], "zh": t["zh"]})
    for mid, (_, m) in a.markers.items():
        nodes.append({"id": mid, "kind": "marker", "type": m["type"], **m["name"]})
        for g in m.get("generators", []):
            edges.append({"source": g["region"], "target": mid, "relation": "generates", "evidence": g["evidence"]})
        for x in m.get("indexes", []):
            edges.append({"source": mid, "target": x["construct"], "relation": "indexes", "evidence": x["evidence"]})
    for pid, (_, p) in a.paradigms.items():
        nodes.append({"id": pid, "kind": "paradigm", "family": p["family"], **p["name"],
                      "recording_modality": p["recording_modality"], "stimulus_modality": p["stimulus_modality"],
                      "bci_category": p["bci_category"], "status": p["status"]})
        for m in p["markers"]:
            edges.append({"source": pid, "target": m, "relation": "elicits"})

    out = ROOT / "dist" / "graph.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=1), encoding="utf-8")

    ps = [p for _, p in a.paradigms.values()]
    print(f"graph: {len(nodes)} nodes, {len(edges)} edges -> {out.relative_to(ROOT).as_posix()}")
    for label, key in (("recording modality", "recording_modality"), ("stimulus modality", "stimulus_modality"),
                       ("BCI category", "bci_category")):
        c = Counter(v for p in ps for v in p[key])
        print(f"{label}: " + ", ".join(f"{k} {n}" for k, n in c.most_common()))
    print("evidence grades: " + ", ".join(f"{k} {n}" for k, n in
                                          sorted(Counter(e["evidence"] for e in edges if "evidence" in e).items())))
    verified = sum(1 for p in ps if p["status"] == "reviewed")
    print(f"reviewed paradigms: {verified}/{len(ps)}")


if __name__ == "__main__":
    main()
