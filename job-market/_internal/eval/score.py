#!/usr/bin/env python3
"""Unblind an evaluation run and score the two extractions against each other.

Reads manifest.json (which side was A) and grades.json (the verdicts, written
while blind) from the same directory. Per-stratum rates are reweighted by each
stratum's share of the corpus, so the population estimate is not distorted by
the deliberate oversampling of hard cases.

Usage:
  uv run python score.py [--dir .] [--corpus 5743]
"""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--dir", type=Path, default=Path(__file__).resolve().parent)
ap.add_argument("--corpus", type=int, default=5743, help="total jobs the sample represents")
args = ap.parse_args()

manifest = {m["n"]: m for m in json.loads((args.dir / "manifest.json").read_text())}
grades = {g["n"]: g for g in json.loads((args.dir / "grades.json").read_text())["grades"]}

rows = []
for n, g in grades.items():
    m = manifest[n]
    row = {"n": n, "stratum": m["stratum"], "pop": m["stratum_pop"], "title": m["title"],
           "note": g.get("note", "")}
    for side in ("A", "B"):
        row[m[side]] = g[side]          # m["A"] is "new" or "old"
    row["better"] = "tie" if g["better"] == "tie" else m[g["better"]]
    rows.append(row)

print(f"{len(rows)} jobs graded blind\n")

print("=" * 72 + "\nHEAD TO HEAD\n" + "=" * 72)
c = Counter(r["better"] for r in rows)
for k in ("new", "old", "tie"):
    print(f"  {k:<5} preferred on {c[k]:>3} of {len(rows)}")

print("\n" + "=" * 72 + "\nCLASSIFICATION (ai_type)\n" + "=" * 72)
for side in ("old", "new"):
    t = Counter(r[side]["type"] for r in rows)
    print(f"  {side:<4} correct {t['ok']:>3}   defensible {t['weak']:>2}   "
          f"wrong {t['wrong']:>3}   ({t['ok']/len(rows)*100:.0f}% clean)")
print("\n  jobs where exactly one got the type wrong:")
for r in rows:
    if (r["old"]["type"] == "wrong") != (r["new"]["type"] == "wrong"):
        loser = "old" if r["old"]["type"] == "wrong" else "new"
        print(f"    [{loser} wrong] {str(r['title'])[:52]}")

print("\n" + "=" * 72 + "\nSKILL PRECISION - extracted skills the JD never states\n" + "=" * 72)
for side in ("old", "new"):
    tot = sum(r[side]["prec"] for r in rows)
    hit = sum(1 for r in rows if r[side]["prec"])
    print(f"  {side:<4} {tot:>4} invented skills across {hit} of {len(rows)} jobs")
print("\n  worst offenders:")
for r in sorted(rows, key=lambda r: -max(r["old"]["prec"], r["new"]["prec"]))[:5]:
    print(f"    old {r['old']['prec']:>2}  new {r['new']['prec']:>2}   {str(r['title'])[:46]}")

print("\n" + "=" * 72 + "\nSKILL RECALL - stated skills the extraction dropped\n" + "=" * 72)
for side in ("old", "new"):
    tot = sum(r[side]["rec"] for r in rows)
    hit = sum(1 for r in rows if r[side]["rec"])
    print(f"  {side:<4} {tot:>4} missed skills across {hit} of {len(rows)} jobs")

print("\n" + "=" * 72 + "\nBY STRATUM (with corpus weight)\n" + "=" * 72)
by = defaultdict(list)
for r in rows:
    by[r["stratum"]].append(r)
print(f"  {'stratum':<22}{'n':>3}{'corpus':>8}   {'old wrong':>10}{'new wrong':>10}   winner")
for s, rs in sorted(by.items(), key=lambda kv: -kv[1][0]["pop"]):
    ow = sum(1 for r in rs if r["old"]["type"] == "wrong")
    nw = sum(1 for r in rs if r["new"]["type"] == "wrong")
    w = Counter(r["better"] for r in rs)
    win = max(("new", "old", "tie"), key=lambda k: w[k])
    print(f"  {s:<22}{len(rs):>3}{rs[0]['pop']/args.corpus*100:>7.1f}%   "
          f"{ow:>10}{nw:>10}   {win} ({w['new']}/{w['old']}/{w['tie']})")

print("\n" + "=" * 72 +
      "\nPOPULATION ESTIMATE (per-stratum rates reweighted by corpus share)\n" + "=" * 72)
for side in ("old", "new"):
    err = prec = 0.0
    for s, rs in by.items():
        wgt = rs[0]["pop"] / args.corpus
        err += wgt * sum(1 for r in rs if r[side]["type"] == "wrong") / len(rs)
        prec += wgt * sum(r[side]["prec"] for r in rs) / len(rs)
    print(f"  {side:<4} ai_type error {err*100:>5.1f}%    invented skills/job {prec:>4.1f}")
print("\n  Zero observed errors is not a zero error rate: at n=50 the 95% upper")
print("  bound is roughly 6%.")
