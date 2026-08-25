#!/usr/bin/env python3
"""Build a blind A/B evaluation set comparing two extractions of the same jobs.

A uniform random sample spends most of its budget on jobs both extractions get
right, so the sample is stratified instead. Each stratum targets a place the
two disagree or a place either one is known to be shaky, plus a random baseline
that keeps the set anchored to the ordinary case. Every stratum records how
much of the corpus it represents, so `score.py` can reweight per-stratum rates
back to a population estimate instead of reading the raw counts as headline
numbers.

The two extractions print as "A" and "B" in a per-job random order so the
grader cannot tell which is which while scoring. The mapping lives only in
manifest.json, which is not meant to be read until the grades are written.

Usage:
  # materialise the baseline extraction from git, then build
  git archive <ref> job-market/data_structured | tar -x -C /tmp/base --strip-components=2
  uv run python build_eval.py --baseline /tmp/base --out ./run1

Grade by reading run1/batch_*.md and writing a grades.json alongside (see the
committed grades.json for the shape), then run score.py.
"""
import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
JM = HERE.parent.parent
sys.path.insert(0, str(HERE.parent / "analysis"))
from common import is_umbrella  # noqa: E402

ap = argparse.ArgumentParser(description=__doc__,
                             formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--baseline", type=Path, required=True,
                help="directory holding the extraction to compare against "
                     "(dated subdirs, same layout as data_structured)")
ap.add_argument("--current", type=Path, default=JM / "data_structured")
ap.add_argument("--raw", type=Path, default=JM / "data_raw")
ap.add_argument("--out", type=Path, default=HERE / "run")
ap.add_argument("--seed", type=int, default=2026)
ap.add_argument("--batch", type=int, default=10)
args = ap.parse_args()

NEW, OLD, RAW = args.current, args.baseline, args.raw
args.out.mkdir(parents=True, exist_ok=True)
for stale in args.out.glob("batch_*.md"):
    stale.unlink()

CORE = {"python", "docker", "sql", "kubernetes", "aws"}
GAINED = {"llm evaluation", "guardrails", "function calling", "model evaluation"}


def flat(job):
    out = set()
    for cat, lst in ((job.get("position") or {}).get("skills") or {}).items():
        if isinstance(lst, list):
            out |= {s.lower() for s in lst if not is_umbrella(s)}
    return out


def at(job):
    if job is None:
        return None
    return ((job.get("position") or {}).get("ai_type") or {}).get("type", "unknown")


print("loading both extractions ...", flush=True)
rows = []
for d in sorted(x.name for x in NEW.iterdir() if x.is_dir()):
    for f in sorted((NEW / d).glob("*.yaml")):
        o = OLD / d / f.name
        rows.append({
            "date": d, "file": f.name,
            "new": yaml.safe_load(f.read_text(encoding="utf-8")),
            "old": yaml.safe_load(o.read_text(encoding="utf-8")) if o.exists() else None,
        })
print(f"  {len(rows)} jobs", flush=True)

n_new = {r["file"]: flat(r["new"]) for r in rows}
n_old = {r["file"]: (flat(r["old"]) if r["old"] else set()) for r in rows}
sizes = sorted(len(v) for v in n_new.values())
lo, hi = sizes[int(len(sizes) * 0.05)], sizes[int(len(sizes) * 0.95)]

# A job lands in the first stratum it qualifies for, so the narrow diagnostic
# strata get first pick and the baseline mops up whatever is left.
STRATA = [
    ("recovered_or_unknown", 4,
     lambda r: r["old"] is None or "unknown" in (at(r["new"]), at(r["old"]))),
    ("aitype_disagree", 8,
     lambda r: r["old"] is not None and at(r["new"]) != at(r["old"])),
    ("ml_vs_ai_boundary", 5,
     lambda r: "ml-first" in (at(r["new"]), at(r["old"]))),
    ("support_boundary", 5,
     lambda r: at(r["new"]) == "ai-support"
     and bool([s for s in ((r["new"].get("position") or {}).get("skills") or {}).get("genai", [])
               if not is_umbrella(s)])),
    ("lost_core_skill", 6,
     lambda r: bool((n_old[r["file"]] & CORE) - n_new[r["file"]])),
    ("gained_eval_skill", 6,
     lambda r: bool((n_new[r["file"]] & GAINED) - n_old[r["file"]])),
    ("sparse_or_dense", 4,
     lambda r: len(n_new[r["file"]]) <= lo or len(n_new[r["file"]]) >= hi),
    ("baseline_random", 12, lambda r: True),
]

rng = random.Random(args.seed)
pools = {name: [] for name, _, _ in STRATA}
for r in rows:
    for name, _, pred in STRATA:
        if pred(r):
            pools[name].append(r)
            break

picked = []
for name, target, _ in STRATA:
    take = rng.sample(pools[name], min(target, len(pools[name])))
    for r in take:
        r["stratum"], r["stratum_pop"] = name, len(pools[name])
    picked += take
    print(f"  {name:<22} pool {len(pools[name]):>5} "
          f"({len(pools[name])/len(rows)*100:5.1f}% of corpus)  sampled {len(take)}")
rng.shuffle(picked)


def clean(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;?", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def render(job):
    if job is None:
        return ["(no extraction - this job was dropped entirely)"]
    p = job.get("position") or {}
    a = p.get("ai_type") or {}
    flat_ = [f"{s}{'*' if is_umbrella(s) else ''} ({cat})"
             for cat, lst in (p.get("skills") or {}).items() if isinstance(lst, list)
             for s in lst]
    return [f"ai_type: {a.get('type')}", f"reasoning: {a.get('reasoning')}",
            f"skills ({len(flat_)}): " + "; ".join(flat_)]


manifest = []
for bi in range(0, len(picked), args.batch):
    chunk = picked[bi:bi + args.batch]
    lines = [f"# Eval batch {bi // args.batch + 1} "
             f"(jobs {bi + 1}-{bi + len(chunk)} of {len(picked)})", "",
             "Two extractions per job, labelled A and B in a random order. Skills",
             "marked with * are umbrella terms (field names, not capabilities).", ""]
    for n, r in enumerate(chunk, start=bi + 1):
        raw = yaml.safe_load((RAW / r["date"] / r["file"]).read_text(encoding="utf-8"))
        p = r["new"].get("position") or {}
        a_is_new = rng.random() < 0.5
        a, b = (r["new"], r["old"]) if a_is_new else (r["old"], r["new"])
        lines += [
            f"## JOB {n} - {r['file']}", f"title: {p.get('title')}",
            f"company: {(r['new'].get('company') or {}).get('name')}  |  scrape: {r['date']}",
            "", "### description", clean(str(raw.get("description", "")))[:9000], "",
            "### extraction A", *render(a), "",
            "### extraction B", *render(b), "", "---", "",
        ]
        manifest.append({
            "n": n, "file": r["file"], "date": r["date"], "title": p.get("title"),
            "stratum": r["stratum"], "stratum_pop": r["stratum_pop"],
            "A": "new" if a_is_new else "old", "B": "old" if a_is_new else "new",
            "new_ai_type": at(r["new"]), "old_ai_type": at(r["old"]),
        })
    (args.out / f"batch_{bi // args.batch + 1}.md").write_text("\n".join(lines),
                                                               encoding="utf-8")

(args.out / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
print(f"\n{len(picked)} jobs -> {args.out}")
print("new ai_type mix:", dict(Counter(m["new_ai_type"] for m in manifest)))
print("old ai_type mix:", dict(Counter(m["old_ai_type"] for m in manifest)))
print("A is new in", sum(1 for m in manifest if m["A"] == "new"), f"of {len(manifest)}")
