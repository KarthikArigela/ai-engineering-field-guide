#!/usr/bin/env python3
"""Self-consistency: do near-identical job descriptions get the same label?

Some employers post the same description many times with one detail swapped -
G2i's RLHF posting appears once per programming language. Those groups are free
ground truth for consistency: whatever the right label is, it has to be the
same across the group. No judge and no hand-labelling required, which makes
this cheap enough to run over the whole corpus on every extraction change.

Groups are formed on the description with numbers and language names stripped,
so "3+ years in C" and "3+ years in Java" collapse together.

Usage:
  uv run python consistency.py [--baseline /tmp/base]
"""
import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
JM = HERE.parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("--current", type=Path, default=JM / "data_structured")
ap.add_argument("--baseline", type=Path, help="optional second extraction to compare against")
ap.add_argument("--raw", type=Path, default=JM / "data_raw")
ap.add_argument("--min-chars", type=int, default=400)
args = ap.parse_args()

SIDES = [("new", args.current)] + ([("old", args.baseline)] if args.baseline else [])
LANGS = (r"\b(c\+\+|c#|golang|go|java|javascript|typescript|python|ruby|rust"
         r"|scala|kotlin|swift|php|perl|r)\b")


def norm(text):
    t = re.sub(r"<[^>]+>", " ", str(text)).lower()
    t = re.sub(LANGS, "<lang>", t)
    t = re.sub(r"\d+", "<n>", t)
    return " ".join(re.sub(r"[^a-z<>]+", " ", t).split())


def at(job):
    return ((job.get("position") or {}).get("ai_type") or {}).get("type", "unknown")


groups = defaultdict(list)
for d in sorted(x.name for x in args.raw.iterdir() if x.is_dir()):
    for f in sorted((args.raw / d).glob("*.yaml")):
        raw = yaml.safe_load(f.read_text(encoding="utf-8"))
        desc = str(raw.get("description", ""))
        if len(desc) >= args.min_chars:      # too short to be a meaningful duplicate
            groups[norm(desc)].append((d, f.name))

dupes = {k: v for k, v in groups.items() if len(v) > 1}
print(f"{len(dupes)} near-duplicate description groups, "
      f"{sum(len(v) for v in dupes.values())} postings\n")

stats = {s: [0, 0] for s, _ in SIDES}
split_by_new = []
examples = []
for members in dupes.values():
    labels = {s: [] for s, _ in SIDES}
    for d, name in members:
        for side, root in SIDES:
            p = root / d / name
            if p.exists():
                labels[side].append(at(yaml.safe_load(p.read_text(encoding="utf-8"))))
    for side, _ in SIDES:
        if len(labels[side]) > 1:
            stats[side][1] += 1
            stats[side][0] += len(set(labels[side])) == 1
    title = yaml.safe_load((args.raw / members[0][0] / members[0][1])
                           .read_text(encoding="utf-8")).get("title")
    if len(set(labels["new"])) > 1:
        split_by_new.append((title, len(members), Counter(labels["new"])))
    if (args.baseline and len(set(labels.get("old", []))) > 1
            and len(set(labels["new"])) == 1 and len(examples) < 8):
        examples.append((title, len(members), Counter(labels["old"]), labels["new"][0]))

print("group-level label consistency (same text -> same label):")
for side, _ in SIDES:
    ok, tot = stats[side]
    print(f"  {side:<4} {ok}/{tot} groups internally consistent ({ok/tot*100:.1f}%)")

if examples:
    print("\ngroups the baseline split and the current extraction did not:")
    for title, n, old_c, new_l in examples:
        print(f"  {str(title)[:50]:<50} {n} postings")
        print(f"    old: {dict(old_c)}   new: all {new_l}")

print(f"\ngroups the CURRENT extraction still splits ({len(split_by_new)}) - "
      "these are the remaining error candidates:")
for title, n, c in split_by_new[:15]:
    print(f"  {str(title)[:50]:<50} {n} postings  {dict(c)}")
