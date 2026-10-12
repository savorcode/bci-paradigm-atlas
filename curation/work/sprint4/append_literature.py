"""Append sprint-4 knowledge-layer sources (markers, regions, constructs) to curation/literature.csv.
Existing DOIs are not duplicated. Vancouver citations are split into authors / title / venue heuristically."""
import csv, glob, re, yaml
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
LIT = ROOT / "curation" / "literature.csv"
rows = list(csv.DictReader(open(LIT, encoding="utf-8-sig")))
fields = list(rows[0].keys())
have = {r["doi"].lower(): r["ref_id"] for r in rows if r["doi"]}
nxt = max(int(r["ref_id"][1:]) for r in rows) + 1
src = {}  # key -> (source, set of users)
def add(s, user):
    key = (s.get("doi") or "").lower() or s["citation"]
    src.setdefault(key, [s, set()])[1].add(user)
for p in sorted(glob.glob(str(ROOT / "knowledge/markers/*.yaml"))):
    d = yaml.safe_load(open(p, encoding="utf-8"))
    for k in ("generators", "indexes"):
        for x in d.get(k) or []:
            for s in x["sources"]:
                add(s, d["id"])
for f in ("regions", "constructs"):
    for t in yaml.safe_load(open(ROOT / f"knowledge/{f}.yaml", encoding="utf-8"))["terms"]:
        for s in t.get("sources") or []:
            add(s, t["id"])
new, reused = [], 0
for key, (s, users) in sorted(src.items(), key=lambda kv: kv[0]):
    doi = (s.get("doi") or "").lower()
    if doi and doi in have:
        reused += 1
        continue
    c = s["citation"].strip()
    parts = [x.strip() for x in re.split(r"\.\s+", c)]
    authors = parts[0] if len(parts) > 2 else ""
    title = parts[1] if len(parts) > 2 else c
    venue = ". ".join(parts[2:]).rstrip(".") if len(parts) > 2 else ""
    rid = f"R{nxt:04d}"; nxt += 1
    if doi: have[doi] = rid
    new.append({**{k: "" for k in fields}, "ref_id": rid, "authors": authors, "year": str(s.get("year", "")),
                "title": title, "venue": venue, "doi": s.get("doi", ""), "pmid": str(s.get("pmid", "") or ""),
                "url": f"https://doi.org/{s['doi']}" if s.get("doi") else "",
                "found_via": "curator_search_s4", "source_page": "knowledge: " + ";".join(sorted(users)),
                "verified": "false", "qa_flag": "" if doi else "no_doi"})
with open(LIT, "a", encoding="utf-8", newline="") as fh:
    csv.DictWriter(fh, fieldnames=fields).writerows(new)
print(f"sources {len(src)}; already in literature.csv {reused}; appended {len(new)} ({new[0]['ref_id']}-{new[-1]['ref_id']}); no DOI {sum(1 for r in new if not r['doi'])}")
