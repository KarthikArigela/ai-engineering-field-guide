#!/usr/bin/env python3
"""Check the fields the blind eval never covered, against the job text.

is_management and is_customer_facing have no definition anywhere in the prompt
- they are bare booleans with a False default - and company_stage is only
"extract if mentioned". All three moved sharply in the re-extraction, so this
measures which version the text actually supports.

Management and stage can be checked objectively enough without a judge:
a title containing Manager/Director/Head/VP is management by any definition,
and a stage is either named in the description or it is not.
"""
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

import argparse

HERE = Path(__file__).resolve().parent
JM = HERE.parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("--current", type=Path, default=JM / "data_structured")
ap.add_argument("--baseline", type=Path, required=True,
                help="second extraction to compare against")
ap.add_argument("--raw", type=Path, default=JM / "data_raw")
_a = ap.parse_args()
NEW, OLD, RAW = _a.current, _a.baseline, _a.raw

# Unambiguous people-management titles. "Lead" and "Principal" are excluded:
# both are routinely individual-contributor titles.
MGMT_TITLE = re.compile(
    r"\b(engineering manager|manager|director|head of|vp\b|vice president|chief|cto)\b", re.I)
# Phrases that mean line management rather than technical leadership.
MGMT_BODY = re.compile(
    r"direct reports|manage a team of|people manage|hiring and (?:firing|retention)"
    r"|performance review|headcount|grow(?:ing)? the team|team of \d+ engineers"
    r"|managing engineers", re.I)
IC_HINT = re.compile(r"individual contributor|\bIC\b role|hands.on contributor", re.I)

STAGE = re.compile(
    r"\b(pre-?seed|seed(?:-stage)?|series [a-f]\b|bootstrapp?ed|publicly traded"
    r"|nasdaq|nyse|fortune \d+|ipo|post-ipo|profitable)\b", re.I)


def load(root, d, name):
    p = root / d / name
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else None


def raw_text(d, name):
    f = RAW / d / name
    if not f.exists():
        return "", ""
    j = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    return str(j.get("title", "")), str(j.get("description", ""))


rows = []
for d in sorted(x.name for x in NEW.iterdir() if x.is_dir()):
    for f in sorted((NEW / d).glob("*.yaml")):
        new = load(NEW, d, f.name)
        old = load(OLD, d, f.name)
        if old is None:
            continue
        title, desc = raw_text(d, f.name)
        rows.append({
            "title": title, "desc": desc,
            "new_m": bool((new.get("position") or {}).get("is_management")),
            "old_m": bool((old.get("position") or {}).get("is_management")),
            "new_c": bool((new.get("position") or {}).get("is_customer_facing")),
            "old_c": bool((old.get("position") or {}).get("is_customer_facing")),
            "new_s": ((new.get("company") or {}).get("stage") or "").strip(),
            "old_s": ((old.get("company") or {}).get("stage") or "").strip(),
        })
n = len(rows)
print(f"{n} jobs\n")

print("=" * 70)
print("IS_MANAGEMENT")
print("=" * 70)
for side in ("old", "new"):
    k = sum(r[f"{side}_m"] for r in rows)
    print(f"  {side} says management: {k} ({k/n*100:.1f}%)")

mgmt_title = [r for r in rows if MGMT_TITLE.search(r["title"])]
mgmt_body = [r for r in rows if MGMT_BODY.search(r["desc"])]
print(f"\n  jobs whose TITLE is unambiguously management: {len(mgmt_title)} "
      f"({len(mgmt_title)/n*100:.1f}%)")
for side in ("old", "new"):
    hit = sum(1 for r in mgmt_title if r[f"{side}_m"])
    print(f"    {side} recall on those: {hit}/{len(mgmt_title)} "
          f"({hit/len(mgmt_title)*100:.1f}%)")

print(f"\n  jobs whose BODY describes line management: {len(mgmt_body)} "
      f"({len(mgmt_body)/n*100:.1f}%)")
for side in ("old", "new"):
    hit = sum(1 for r in mgmt_body if r[f"{side}_m"])
    print(f"    {side} recall on those: {hit}/{len(mgmt_body)} "
          f"({hit/len(mgmt_body)*100:.1f}%)")

neither = [r for r in rows
           if not MGMT_TITLE.search(r["title"]) and not MGMT_BODY.search(r["desc"])]
print(f"\n  precision - flagged management with no title or body evidence:")
for side in ("old", "new"):
    fp = sum(1 for r in neither if r[f"{side}_m"])
    flagged = sum(1 for r in rows if r[f"{side}_m"])
    print(f"    {side}: {fp} of {flagged} flagged ({fp/max(1,flagged)*100:.1f}% unsupported)")

print("\n" + "=" * 70)
print("COMPANY_STAGE")
print("=" * 70)
for side in ("old", "new"):
    k = sum(1 for r in rows if r[f"{side}_s"])
    print(f"  {side} states a stage: {k} ({k/n*100:.1f}%)")

has_stage = [r for r in rows if STAGE.search(r["desc"])]
print(f"\n  jobs whose description actually names a stage: {len(has_stage)} "
      f"({len(has_stage)/n*100:.1f}%)")
for side in ("old", "new"):
    hit = sum(1 for r in has_stage if r[f"{side}_s"])
    print(f"    {side} recall on those: {hit}/{len(has_stage)} "
          f"({hit/len(has_stage)*100:.1f}%)")
no_stage = [r for r in rows if not STAGE.search(r["desc"])]
print(f"\n  precision - stage recorded where the text names none:")
for side in ("old", "new"):
    fp = sum(1 for r in no_stage if r[f"{side}_s"])
    got = sum(1 for r in rows if r[f"{side}_s"])
    print(f"    {side}: {fp} of {got} ({fp/max(1,got)*100:.1f}% unsupported)")
    ex = Counter(r[f"{side}_s"] for r in no_stage if r[f"{side}_s"])
    print(f"      most common invented values: {[v for v, _ in ex.most_common(5)]}")

print("\n" + "=" * 70)
print("IS_CUSTOMER_FACING (no objective probe - reporting drift only)")
print("=" * 70)
for side in ("old", "new"):
    k = sum(1 for r in rows if r[f"{side}_c"])
    print(f"  {side}: {k} ({k/n*100:.1f}%)")
agree = sum(1 for r in rows if r["old_c"] == r["new_c"])
print(f"  agreement between the two: {agree/n*100:.1f}%")
