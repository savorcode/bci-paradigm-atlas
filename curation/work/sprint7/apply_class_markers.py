"""Apply class marker additions/removals to paradigms/_classes.yaml, rewriting only the affected class blocks."""
import csv, re, sys
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[3]
p = ROOT / "paradigms" / "_classes.yaml"
s = p.read_text(encoding="utf-8")
terms = yaml.safe_load(s)["terms"]
starts = [m.start() for m in re.finditer(r"^- id: ", s, re.M)] + [len(s)]
upd = {}
for path in sys.argv[1:]:
    for r in csv.DictReader(open(path, encoding="utf-8")):
        u = upd.setdefault(r["class_id"], [set(), set()])
        u[0] |= {x.strip() for x in r["add"].split(";") if x.strip()}
        u[1] |= {x.strip() for x in r["remove"].split(";") if x.strip()}
for i in sorted((i for i, t in enumerate(terms) if t["id"] in upd), reverse=True):
    t = terms[i]; add, rem = upd[t["id"]]
    t["markers"] = [m for m in t.get("markers") or [] if m not in rem] + [m for m in sorted(add) if m not in (t.get("markers") or [])]
    s = s[:starts[i]] + yaml.safe_dump([t], allow_unicode=True, sort_keys=False, width=120) + s[starts[i + 1]:]
p.write_text(s, encoding="utf-8")
print("updated", sorted(upd))
