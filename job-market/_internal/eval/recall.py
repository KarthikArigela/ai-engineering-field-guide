#!/usr/bin/env python3
"""Corpus-wide recall probe: when a JD names a tool, did we extract it?

Only tools whose name is a distinctive string are probed, so a text match is
strong evidence the skill is genuinely stated. This needs no judge and no
hand-labelling, so unlike the 50-job blind eval it can run over the whole
corpus every time the extractor changes.

It measures recall only. Precision (skills extracted that the text never
states) still needs a reader, because "the string is absent" is not the same
as "the skill is unsupported" - a JD can require containers without writing
the word Docker.

Usage:
  uv run python recall.py [--baseline /tmp/base] [--sample 700]
"""
import argparse
import random
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
JM = HERE.parent.parent
sys.path.insert(0, str(HERE.parent / "analysis"))
from common import flat_skills  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--current", type=Path, default=JM / "data_structured")
ap.add_argument("--baseline", type=Path, help="optional second extraction to compare against")
ap.add_argument("--raw", type=Path, default=JM / "data_raw")
ap.add_argument("--sample", type=int, default=700, help="0 for the whole corpus")
ap.add_argument("--seed", type=int, default=3)
args = ap.parse_args()

PROBES = [
    ("docker", r"\bdocker\b"),
    ("kubernetes", r"\bkubernetes\b|\bk8s\b"),
    ("python", r"\bpython\b"),
    ("sql", r"\bsql\b"),
    ("terraform", r"\bterraform\b"),
    ("langchain", r"\blangchain\b"),
    ("pytorch", r"\bpytorch\b"),
    ("fastapi", r"\bfastapi\b"),
    ("react", r"\breact(\.js)?\b"),
    ("kafka", r"\bkafka\b"),
    ("snowflake", r"\bsnowflake\b"),
    ("mcp", r"model context protocol|\bmcp\b"),
]


def raw_text(date, name):
    f = args.raw / date / name
    if not f.exists():
        return None
    d = yaml.safe_load(f.read_text(encoding="utf-8"))
    return " ".join(str(v) for v in d.values() if isinstance(v, str)).lower()


files = sorted(args.current.rglob("*.yaml"))
if args.sample:
    files = random.Random(args.seed).sample(files, min(args.sample, len(files)))

stats = {k: {"stated": 0, "new": 0, "old": 0} for k, _ in PROBES}
n = 0
for f in files:
    txt = raw_text(f.parent.name, f.name)
    if txt is None:
        continue
    n += 1
    new_s = flat_skills(yaml.safe_load(f.read_text(encoding="utf-8")), umbrella=True)
    old_s = set()
    if args.baseline:
        o = args.baseline / f.parent.name / f.name
        if o.exists():
            old_s = flat_skills(yaml.safe_load(o.read_text(encoding="utf-8")), umbrella=True)
    for key, pat in PROBES:
        if re.search(pat, txt):
            stats[key]["stated"] += 1
            stats[key]["new"] += key in new_s
            stats[key]["old"] += key in old_s

print(f"{n} jobs sampled\n")
head = f"{'skill':<14}{'stated':>8}{'new recall':>12}"
print(head + (f"{'old recall':>12}" if args.baseline else ""))
tot = {"stated": 0, "new": 0, "old": 0}
for key, _ in PROBES:
    s = stats[key]
    if not s["stated"]:
        continue
    for k in tot:
        tot[k] += s[k]
    line = f"{key:<14}{s['stated']:>8}{s['new']/s['stated']*100:11.1f}%"
    if args.baseline:
        line += f"{s['old']/s['stated']*100:11.1f}%"
    print(line)
line = f"\n{'overall':<14}{tot['stated']:>8}{tot['new']/tot['stated']*100:11.1f}%"
if args.baseline:
    line += f"{tot['old']/tot['stated']*100:11.1f}%"
print(line)
