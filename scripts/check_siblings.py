# Copyright 2026 思维刻度 SavorCode
# SPDX-License-Identifier: Apache-2.0
"""Check that the concrete paradigms of each class differ on at least one numbering criterion (D-057).

The four criteria are compared on the `protocol` block:
  1 class/condition set   -> n_classes + normalised `classes`
  2 stimulus / cue type   -> normalised `cue` + `stimulus_coding`
  3 trial structure       -> `paradigm_timing`
  4 feedback mode         -> `feedback`

Two levels are reported for every pair of siblings:
  DUPLICATE  identical on all four criteria (all fields equal after normalisation) -> error
  REVIEW     structured fields equal (n_classes, stimulus_coding, paradigm_timing, feedback); the pair
             differs only in free text (`classes` and/or `cue`), so a human must confirm that the
             difference is a real criterion-1/2 change and not a rewording -> listed, not an error

Usage: python3 scripts/check_siblings.py [--markdown]   (exit status 1 if a DUPLICATE is found)
"""

from __future__ import annotations

import itertools
import re
import sys
from collections import defaultdict

from atlas import load


def norm(s) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


def crit(d: dict) -> dict:
    p = d.get("protocol") or {}
    classes = tuple(sorted(norm(c) for c in p.get("classes") or []))
    return {
        "1": (p.get("n_classes") or len(classes) or None, classes),
        "2": (norm(p.get("cue")), norm(p.get("stimulus_coding"))),
        "3": p.get("paradigm_timing"),
        "4": p.get("feedback"),
        "struct": (p.get("n_classes"), norm(p.get("stimulus_coding")), p.get("paradigm_timing"), p.get("feedback")),
    }


def main() -> int:
    md = "--markdown" in sys.argv
    atlas = load()
    by_class: dict[str, list[str]] = defaultdict(list)
    for pid, (_, d) in atlas.paradigms.items():
        if d["status"] == "deprecated":  # merged entries keep their file but are not siblings (D-058)
            continue
        by_class[d["class"]].append(pid)
    dups, review = [], []
    n_pairs = 0
    for cid, ids in sorted(by_class.items()):
        for a, b in itertools.combinations(sorted(ids), 2):
            n_pairs += 1
            ca, cb = crit(atlas.paradigms[a][1]), crit(atlas.paradigms[b][1])
            same = [k for k in "1234" if ca[k] == cb[k]]
            if len(same) == 4:
                dups.append((cid, a, b))
            elif ca["struct"] == cb["struct"]:
                diff = [k for k in "12" if ca[k] != cb[k]]
                review.append((cid, a, b, ",".join(diff)))
    multi = sum(1 for ids in by_class.values() if len(ids) > 1)
    if md:
        print(f"Classes: {len(by_class)}; classes with >1 concrete paradigm: {multi}; sibling pairs: {n_pairs}\n")
        print(f"DUPLICATE (identical on criteria 1-4): {len(dups)}\n")
        for c, a, b in dups:
            print(f"- {c}: {a} = {b}")
        print(f"\nREVIEW (structured fields equal; differ only in free-text criterion): {len(review)}\n")
        print("| class | pair | differs in criterion |\n|---|---|---|")
        for c, a, b, k in review:
            print(f"| {c} | {a} / {b} | {k} |")
    else:
        for c, a, b in dups:
            print(f"DUPLICATE {c}: {a} and {b} are identical on criteria 1-4")
        for c, a, b, k in review:
            print(f"REVIEW    {c}: {a} / {b} differ only in free text of criterion {k}")
        print(f"{len(by_class)} classes ({multi} with siblings), {n_pairs} sibling pairs; "
              f"{len(dups)} duplicate(s), {len(review)} pair(s) to review.")
    return 1 if dups else 0


if __name__ == "__main__":
    sys.exit(main())
