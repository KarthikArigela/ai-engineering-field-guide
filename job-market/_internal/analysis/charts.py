#!/usr/bin/env python3
"""Render trend charts as PNGs into job-market/images/.

Reuses computations from deep_trends2.py (deterministic k-means seed=7).
Run:  uv run python _internal/analysis/charts.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from deep_trends2 import (  # noqa: E402
    ALL, BD, DATES, LAB, FEATURES, aitype, build_features, has, kmeans,
)

IMG = Path(__file__).resolve().parents[2] / "images"
IMG.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 150, "savefig.bbox": "tight"})


def series(fn, base=None):
    src = base if base is not None else BD
    return [100.0 * sum(1 for j in src[d] if fn(j)) / len(src[d]) for d in DATES]


X = list(LAB.values())


# --------------------------------------------------------------------------- #
# 1. Integrator vs trainer
# --------------------------------------------------------------------------- #
def chart_integrator_trainer():
    aif = {d: [j for j in BD[d] if aitype(j) == "ai-first"] for d in DATES}
    trainer = lambda j: has(j, "ml", "PyTorch", "TensorFlow", "scikit-learn", "CUDA", "RLHF") or has(j, "genai", "Fine-Tuning", "LoRA")
    integrator = lambda j: has(j, "genai", "RAG", "LangChain", "LangGraph", "CrewAI", "AutoGen", "MCP", "OpenAI API", "Anthropic API", "Function Calling", "AI Agents", "Agentic Workflows", "Multi-Agent Systems")
    pure_int = lambda j: integrator(j) and not trainer(j)
    pure_tr = lambda j: trainer(j) and not integrator(j)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(X, [series(trainer, aif)[i] for i in range(len(DATES))], "o-", label="Trainer stack (PyTorch/TF/Fine-Tune/CUDA)", color="#d62728")
    ax.plot(X, [series(integrator, aif)[i] for i in range(len(DATES))], "o-", label="Integrator stack (RAG/agents/APIs)", color="#2ca02c")
    ax.plot(X, series(pure_int, aif), "o--", label="Pure integrator (no training)", color="#2ca02c", alpha=0.5)
    ax.plot(X, series(pure_tr, aif), "o--", label="Pure trainer (no integration)", color="#d62728", alpha=0.5)
    ax.set_title("The integrator-vs-trainer shift within ai-first roles")
    ax.set_ylabel("% of ai-first jobs")
    ax.set_ylim(0, 90)
    ax.legend(fontsize=9, loc="center right")
    fig.savefig(IMG / "integrator-vs-trainer.png")
    plt.close(fig)


# --------------------------------------------------------------------------- #
# 2. Skill trajectories (risers / decliners)
# --------------------------------------------------------------------------- #
def chart_trajectories():
    risers = [("SQL", "languages", "SQL"), ("Prompt Engineering", "genai", "Prompt Engineering"),
              ("CI/CD", "ops", "CI/CD"), ("Coding tools", "genai", "Claude Code"),
              ("MCP", "genai", "MCP"), ("LangGraph", "genai", "LangGraph")]
    decliners = [("PyTorch", "ml", "PyTorch"), ("Fine-Tuning", "genai", "Fine-Tuning"),
                 ("RLHF", "ml", "RLHF"), ("TensorFlow", "ml", "TensorFlow")]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    for label, cat, name in risers:
        a1.plot(X, series(lambda j, cat=cat, name=name: has(j, cat, name)), "o-", label=label)
    a1.set_title("Rising skills")
    a1.set_ylabel("% of jobs")
    a1.legend(fontsize=9)
    for label, cat, name in decliners:
        a2.plot(X, series(lambda j, cat=cat, name=name: has(j, cat, name)), "o-", label=label)
    a2.set_title("Declining skills")
    a2.set_ylabel("% of jobs")
    a2.legend(fontsize=9)
    fig.suptitle("Skill trajectories across the six scrapes", y=1.02)
    fig.savefig(IMG / "skill-trajectories.png")
    plt.close(fig)


# --------------------------------------------------------------------------- #
# 3. Role archetypes heatmap
# --------------------------------------------------------------------------- #
def name_cluster(freq):
    def f(name):
        return freq[IDX[name]]
    if f("React/Frontend") > 0.5:
        return "Full-stack AI"
    if f("Vector DB") > 0.5 or f("RAG") > 0.6:
        return "RAG app builder"
    if f("Agents") > 0.6:
        return "Agent builder"
    if f("Terraform") > 0.2 and f("RAG") < 0.4:
        return "DevOps / infra"
    if f("PyTorch/TF") > 0.5 and f("RAG") < 0.5:
        return "ML trainer / researcher"
    return "Cloud / ML platform"


def chart_archetypes():
    Xf = build_features(ALL)
    mask = Xf.sum(axis=1) > 0
    Xc = Xf[mask]
    jobs_c = [j for j, m in zip(ALL, mask) if m]
    labels = kmeans(Xc, k=6)
    cols = ["RAG", "Agents", "LangChain", "LangGraph", "Vector DB", "PyTorch/TF",
            "MLOps", "Kubernetes", "Terraform", "React/Frontend", "OpenAI/Anthropic API"]
    fname_to_i = {f[0]: i for i, f in enumerate(FEATURES)}
    col_idx = [fname_to_i[c] for c in cols]
    named = {}
    for c in range(6):
        members = labels == c
        freq = Xc[members].mean(axis=0)
        size = int(members.sum())
        named[name_cluster(freq)] = (freq, size)
    order = ["RAG app builder", "Cloud / ML platform", "Agent builder", "DevOps / infra",
             "ML trainer / researcher", "Full-stack AI"]
    order = [n for n in order if n in named]
    matrix = np.array([[named[n][0][i] * 100 for i in col_idx] for n in order])
    sizes = [named[n][1] for n in order]
    fig, ax = plt.subplots(figsize=(12, 5.5))
    im = ax.imshow(matrix, aspect="auto", cmap="YlGnBu", vmin=0, vmax=100)
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels(cols, rotation=40, ha="right")
    rowlabels = [f"{n}\n({s}, {100*s/len(ALL):.1f}%)" for n, s in zip(order, sizes)]
    ax.set_yticks(range(len(order)))
    ax.set_yticklabels(rowlabels)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            v = matrix[i, j]
            ax.text(j, i, f"{v:.0f}", ha="center", va="center",
                    color="white" if v > 55 else "black", fontsize=9)
    fig.colorbar(im, ax=ax, label="% of cluster with this skill")
    ax.set_title("Six role archetypes and their skill signatures (k-means, k=6)")
    fig.savefig(IMG / "role-archetypes.png")
    plt.close(fig)


# --------------------------------------------------------------------------- #
# 4. Use-case themes
# --------------------------------------------------------------------------- #
def chart_usecases():
    import re
    themes = {
        "Automation / workflow": r"automat|workflow|back[- ]office|process autom",
        "Agents / autonomous": r"\bagent|multi-agent|autonomous|agentic",
        "RAG / Q&A": r"\brag\b|retrieval-augmented|question answer|\bqa\b",
        "Search / retrieval": r"search|retrieval|knowledge management",
        "Copilot / dev tools": r"copilot|code assist|developer tool|software develop",
        "Recommend / personalize": r"recommend|personaliz",
    }
    def utext(j):
        return " ".join(j.get("position", {}).get("use_cases") or []).lower()
    fig, ax = plt.subplots(figsize=(9, 5))
    for name, pat in themes.items():
        rx = re.compile(pat)
        ax.plot(X, series(lambda j, rx=rx: bool(rx.search(utext(j)))), "o-", label=name)
    ax.set_title("What companies build with AI (use-case themes)")
    ax.set_ylabel("% of jobs")
    ax.legend(fontsize=9)
    fig.savefig(IMG / "use-case-themes.png")
    plt.close(fig)


# --------------------------------------------------------------------------- #
# 5. Skill slopes (diverging bar)
# --------------------------------------------------------------------------- #
def chart_slopes():
    items = [("SQL", "languages", "SQL"), ("Prompt Engineering", "genai", "Prompt Engineering"),
             ("CI/CD", "ops", "CI/CD"), ("Coding tools", "genai", "Claude Code"),
             ("Docker", "ops", "Docker"), ("MCP", "genai", "MCP"), ("LangGraph", "genai", "LangGraph"),
             ("RAG", "genai", "RAG"), ("Embeddings", "genai", "Embeddings"),
             ("TensorFlow", "ml", "TensorFlow"), ("RLHF", "ml", "RLHF"),
             ("Fine-Tuning", "genai", "Fine-Tuning"), ("PyTorch", "ml", "PyTorch"),
             ("Function Calling", "genai", "Function Calling"), ("Guardrails", "genai", "Guardrails")]
    x = np.arange(len(DATES))
    rows = []
    for label, cat, name in items:
        cells = series(lambda j, cat=cat, name=name: has(j, cat, name))
        slope = float(np.polyfit(x, cells, 1)[0])
        rows.append((label, slope))
    rows.sort(key=lambda r: r[1])
    labels = [r[0] for r in rows]
    slopes = [r[1] for r in rows]
    colors = ["#d62728" if s < 0 else "#2ca02c" for s in slopes]
    fig, ax = plt.subplots(figsize=(9, 6))
    y = np.arange(len(labels))
    ax.barh(y, slopes, color=colors)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("change in % of jobs per scrape (percentage points)")
    ax.set_title("Skill momentum: risers (green) vs decliners (red)")
    fig.savefig(IMG / "skill-momentum.png")
    plt.close(fig)


FEATURES_IDX = {f[0]: i for i, f in enumerate(FEATURES)}
IDX = FEATURES_IDX


def main():
    chart_integrator_trainer()
    chart_trajectories()
    chart_archetypes()
    chart_usecases()
    chart_slopes()
    print("Charts written to", IMG)
    for p in sorted(IMG.glob("*.png")):
        print(" ", p.name, f"{p.stat().st_size//1024} KB")


if __name__ == "__main__":
    main()
