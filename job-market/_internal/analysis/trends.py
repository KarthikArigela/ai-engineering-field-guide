#!/usr/bin/env python3
"""Month-over-month trend analysis of AI engineering roles.

Loads the structured job YAMLs grouped by scrape date and reports how the
role itself has changed across the six scrapes (Feb-Jun 2026):
volume, AI-type mix, seniority, and the canonical skill themes.

Focused on the ROLE (not location). Run with:
    uv run python _internal/analysis/trends.py
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

STRUCTURED_DIR = Path(__file__).resolve().parents[2] / "data_structured"
DATES = sorted(d.name for d in STRUCTURED_DIR.iterdir()
               if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name))
LABELS = {d: d[5:] for d in DATES}  # MM-DD


def load_by_date():
    by_date = defaultdict(list)
    for d in DATES:
        for f in (STRUCTURED_DIR / d).glob("*.yaml"):
            try:
                by_date[d].append(yaml.safe_load(f.read_text(encoding="utf-8")))
            except Exception:
                pass
    return by_date


def pct(n, total):
    return 100.0 * n / total if total else 0.0


def skills_of(job):
    return (job.get("position", {}).get("skills") or {})


def has_skill(job, cat, *names):
    lst = [s.lower() for s in (skills_of(job).get(cat) or [])]
    return any(n.lower() in lst for n in names)


# title -> seniority bucket (first match wins)
def seniority(title):
    t = title.lower()
    if re.search(r"\bstaff\b|\bprincipal\b|\bdistinguished\b", t):
        return "Staff+"
    if re.search(r"\bsenior\b|\bsr\.?\b", t):
        return "Senior"
    if re.search(r"\blead\b", t):
        return "Lead"
    if re.search(r"\bmanager\b|\bdirector\b|\bhead\b|\bvp\b|\bchief\b|\bcto\b", t):
        return "Mgmt/Director"
    if re.search(r"\bjunior\b|\bjr\.?\b|\bintern\b|\bentry\b|\bgraduate\b", t):
        return "Junior/Entry"
    if re.search(r"\bengineer\b|\bdeveloper\b|\bscientist\b|\barchitect\b", t):
        return "Mid (unspecified)"
    return "Other"


# GenAI themes: canonical names (post-canonicalization) + grouping
GENAI_THEMES = [
    ("Prompt Engineering", "genai", ["Prompt Engineering"]),
    ("RAG", "genai", ["RAG"]),
    ("LangChain", "genai", ["LangChain"]),
    ("LangGraph", "genai", ["LangGraph"]),
    ("LlamaIndex", "genai", ["LlamaIndex"]),
    ("CrewAI", "genai", ["CrewAI"]),
    ("AutoGen", "genai", ["AutoGen"]),
    ("Agents (any)", "genai", ["AI Agents", "Agentic Workflows", "Multi-Agent Systems"]),
    ("MCP", "genai", ["MCP"]),
    ("Function Calling", "genai", ["Function Calling"]),
    ("OpenAI API", "genai", ["OpenAI API"]),
    ("Anthropic API", "genai", ["Anthropic API"]),
    ("Fine-Tuning", "genai", ["Fine-Tuning", "LoRA"]),
    ("Embeddings", "genai", ["Embeddings"]),
    ("Guardrails", "genai", ["Guardrails"]),
    ("LLM Evaluation", "genai", ["LLM Evaluation"]),
    ("Coding tools (Claude Code/Copilot/Cursor)", "genai",
     ["Claude Code", "GitHub Copilot", "Cursor", "Codeium", "Windsurf", "Codex"]),
]
LANG_TOP = ["Python", "TypeScript", "SQL", "Java", "JavaScript", "Go", "C++", "C#", "Scala", "Rust"]
CLOUD_TOP = ["AWS", "Azure", "GCP", "AWS Bedrock", "Vertex AI", "SageMaker", "Azure OpenAI"]
OPS_TOP = ["Docker", "Kubernetes", "CI/CD", "Terraform", "MLOps", "MLflow", "vLLM", "LangSmith", "Langfuse"]
ML_TOP = ["PyTorch", "TensorFlow", "scikit-learn", "Hugging Face", "CUDA", "RLHF"]


def row(label, fn, by_date):
    cells = []
    for d in DATES:
        jobs = by_date[d]
        n = sum(1 for j in jobs if fn(j))
        cells.append((n, len(jobs)))
    return label, cells


def print_share_table(title, rows, by_date):
    print("\n" + title)
    header = "  theme".ljust(46) + "".join(LABELS[d].rjust(9) for d in DATES)
    print(header)
    for label, cells in rows:
        line = ("  " + label).ljust(46)
        for n, total in cells:
            line += f"{pct(n, total):7.1f}%"
            line += "  "
        print(line)


def main():
    by_date = load_by_date()
    print("Scrapes analyzed:")
    for d in DATES:
        print(f"  {d}: {len(by_date[d])} jobs")
    total_all = sum(len(v) for v in by_date.values())
    print(f"  total: {total_all} job snapshots\n")

    # ---- Volume ----
    print("=" * 78)
    print("VOLUME (jobs captured per scrape)")
    print("  " + "".join(f"{LABELS[d]:>9}" for d in DATES))
    print("  " + "".join(f"{len(by_date[d]):>9}" for d in DATES))

    # ---- AI type mix ----
    aitypes = ["ai-first", "ai-support", "ml-first", "unknown"]
    rows = []
    for t in aitypes:
        rows.append(row(t, lambda j, t=t: j.get("position", {}).get("ai_type", {}).get("type") == t, by_date))
    print_share_table("AI-TYPE MIX (% of jobs)", rows, by_date)

    # ---- Seniority ----
    buckets = ["Staff+", "Senior", "Lead", "Mgmt/Director", "Mid (unspecified)", "Junior/Entry", "Other"]
    rows = [row(b, lambda j, b=b: seniority(j.get("position", {}).get("title", "")) == b, by_date)
            for b in buckets]
    print_share_table("SENIORITY from title (% of jobs)", rows, by_date)

    # ---- GenAI themes ----
    rows = []
    for label, cat, names in GENAI_THEMES:
        rows.append(row(label, lambda j, cat=cat, names=names: has_skill(j, cat, *names), by_date))
    print_share_table("GENAI SKILL THEMES (% of jobs mentioning)", rows, by_date)

    # ---- Languages ----
    rows = [row(l, lambda j, l=l: has_skill(j, "languages", l), by_date) for l in LANG_TOP]
    print_share_table("LANGUAGES (% of jobs mentioning)", rows, by_date)

    # ---- Cloud ----
    rows = [row(l, lambda j, l=l: has_skill(j, "cloud", l), by_date) for l in CLOUD_TOP]
    print_share_table("CLOUD (% of jobs mentioning)", rows, by_date)

    # ---- Ops ----
    rows = [row(l, lambda j, l=l: has_skill(j, "ops", l), by_date) for l in OPS_TOP]
    print_share_table("OPS / INFRA (% of jobs mentioning)", rows, by_date)

    # ---- Traditional ML ----
    rows = [row(l, lambda j, l=l: has_skill(j, "ml", l), by_date) for l in ML_TOP]
    print_share_table("TRADITIONAL ML (% of jobs mentioning)", rows, by_date)

    # ---- Management / customer-facing flags ----
    rows = [
        row("is_management", lambda j: j.get("position", {}).get("is_management"), by_date),
        row("is_customer_facing", lambda j: j.get("position", {}).get("is_customer_facing"), by_date),
    ]
    print_share_table("ROLE FLAGS (% of jobs)", rows, by_date)

    # ---- Largest month-over-month movers among genai themes (first vs last scrape) ----
    print("\n" + "=" * 78)
    print("GENAI THEMES: Feb-04 -> Jun-25 change (percentage points)")
    first, last = DATES[0], DATES[-1]
    movers = []
    for label, cat, names in GENAI_THEMES:
        p0 = pct(sum(1 for j in by_date[first] if has_skill(j, cat, *names)), len(by_date[first]))
        p1 = pct(sum(1 for j in by_date[last] if has_skill(j, cat, *names)), len(by_date[last]))
        movers.append((label, p0, p1, p1 - p0))
    for label, p0, p1, delta in sorted(movers, key=lambda x: x[3], reverse=True):
        print(f"  {label:42s} {p0:5.1f}% -> {p1:5.1f}%  ({delta:+5.1f} pp)")


if __name__ == "__main__":
    main()
