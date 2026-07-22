#!/usr/bin/env python3
"""Deep, non-obvious trend analyses for AI engineering roles.

Goes beyond single-skill tables: stack indices, framework churn, skill
co-occurrence (lift), use-case themes, and the build-vs-buy split.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import yaml

STRUCTURED_DIR = Path(__file__).resolve().parents[2] / "data_structured"
DATES = sorted(d.name for d in STRUCTURED_DIR.iterdir()
               if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name))
LABELS = {d: d[5:] for d in DATES}


def load_by_date():
    bd = defaultdict(list)
    for d in DATES:
        for f in (STRUCTURED_DIR / d).glob("*.yaml"):
            try:
                bd[d].append(yaml.safe_load(f.read_text(encoding="utf-8")))
            except Exception:
                pass
    return bd


def pct(n, t):
    return 100.0 * n / t if t else 0.0


def sk(job):
    return (job.get("position", {}).get("skills") or {})


def has(job, cat, *names):
    lst = [s.lower() for s in (sk(job).get(cat) or [])]
    return any(n.lower() in lst for n in names)


def aitype(job):
    return job.get("position", {}).get("ai_type", {}).get("type")


def trend_row(label, jobs_by_date, fn):
    return label, [pct(sum(1 for j in jobs if fn(j)), len(jobs)) for d, jobs in jobs_by_date.items()]


def print_table(title, rows):
    print("\n" + title)
    print("  " + "".join(LABELS[d].rjust(9) for d in DATES))
    for label, cells in rows:
        print("  " + label.ljust(40) + "".join(f"{c:7.1f}%  " for c in cells))


def main():
    bd = load_by_date()
    ai_first = {d: [j for j in jobs if aitype(j) == "ai-first"] for d, jobs in bd.items()}

    # ---- 1. Integrator vs Trainer ----
    trainer = lambda j: has(j, "ml", "PyTorch", "TensorFlow", "scikit-learn", "CUDA", "RLHF") \
        or has(j, "genai", "Fine-Tuning", "LoRA")
    integrator = lambda j: has(j, "genai", "RAG", "LangChain", "LangGraph", "CrewAI", "AutoGen",
                               "MCP", "OpenAI API", "Anthropic API", "Function Calling") \
        or has(j, "genai", "AI Agents", "Agentic Workflows", "Multi-Agent Systems")
    pure_integrator = lambda j: integrator(j) and not trainer(j)
    pure_trainer = lambda j: trainer(j) and not integrator(j)
    print("=" * 78)
    print("1. THE INTEGRATOR-vs-TRAINER SHIFT (within ai-first jobs)")
    print_table("% of ai-first jobs", [
        trend_row("Trainer stack (PyTorch/TF/FT/CUDA)", ai_first, trainer),
        trend_row("Integrator stack (RAG/agents/APIs)", ai_first, integrator),
        trend_row("Pure integrator (no training)", ai_first, pure_integrator),
        trend_row("Pure trainer (no integration)", ai_first, pure_trainer),
        trend_row("Neither (apis/infra only?)", ai_first,
                  lambda j: not trainer(j) and not integrator(j)),
    ])

    # ---- 2. Framework churn (share within framework users) ----
    fw_names = ["LangChain", "LangGraph", "LlamaIndex", "CrewAI", "AutoGen", "Semantic Kernel", "DSPy"]
    print("\n" + "=" * 78)
    print("2. AGENT-FRAMEWORK CHURN (share among jobs using ANY framework)")
    rows = []
    for fw in fw_names:
        rows.append(trend_row(fw, bd, lambda j, fw=fw: has(j, "genai", fw)))
    # normalize by framework-user base each month
    print("  raw % of all jobs:")
    print_table("", rows)
    print("  share among framework-users (denominator = jobs using >=1 framework):")
    fw_share = []
    for fw in fw_names:
        cells = []
        for d in DATES:
            users = [j for j in bd[d] if any(has(j, "genai", f) for f in fw_names)]
            cells.append(pct(sum(1 for j in users if has(j, "genai", fw)), len(users)))
        fw_share.append((fw, cells))
    print("  " + "".join(LABELS[d].rjust(9) for d in DATES))
    for label, cells in fw_share:
        print("  " + label.ljust(40) + "".join(f"{c:7.1f}%  " for c in cells))

    # ---- 3. Skill co-occurrence lift (all jobs) ----
    anchors = {
        "RAG": ("genai", ["RAG"]),
        "Agents (any)": ("genai", ["AI Agents", "Agentic Workflows", "Multi-Agent Systems"]),
        "LangChain": ("genai", ["LangChain"]),
        "OpenAI API": ("genai", ["OpenAI API"]),
        "PyTorch": ("ml", ["PyTorch"]),
        "Fine-Tuning": ("genai", ["Fine-Tuning"]),
        "MCP": ("genai", ["MCP"]),
        "Docker": ("ops", ["Docker"]),
    }
    candidates = {
        "Vector DB": ("databases", ["Pinecone", "Weaviate", "Milvus", "Qdrant", "Chroma", "pgvector", "Vector Databases", "FAISS"]),
        "Embeddings": ("genai", ["Embeddings"]),
        "FastAPI": ("web", ["FastAPI"]),
        "LangGraph": ("genai", ["LangGraph"]),
        "Function Calling": ("genai", ["Function Calling"]),
        "Kubernetes": ("ops", ["Kubernetes"]),
        "Python": ("languages", ["Python"]),
        "Prompt Engineering": ("genai", ["Prompt Engineering"]),
        "AWS": ("cloud", ["AWS"]),
        "MLOps": ("ops", ["MLOps"]),
    }
    alljobs = [j for jobs in bd.values() for j in jobs]
    N = len(alljobs)
    base = {k: pct(sum(1 for j in alljobs if has(j, v[0], *v[1])), N) for k, v in candidates.items()}
    print("\n" + "=" * 78)
    print(f"3. SKILL CO-OCCURRENCE (lift = P(B|A)/P(B), across all {N} jobs; >1 means B over-represented given A)")
    for aname, (acat, anames) in anchors.items():
        A = [j for j in alljobs if has(j, acat, *anames)]
        if not A:
            continue
        lifts = []
        for cname, (ccat, cnames) in candidates.items():
            if cname == aname:
                continue
            pa = len(A)
            pab = sum(1 for j in A if has(j, ccat, *cnames))
            cond = pct(pab, pa)
            lift = cond / base[cname] if base[cname] else 0
            lifts.append((cname, cond, lift))
        lifts.sort(key=lambda x: x[2], reverse=True)
        top = ", ".join(f"{n} {c:.0f}%(x{l:.1f})" for n, c, l in lifts[:5])
        print(f"  {aname:14s} (n={pa:4d}) -> {top}")

    # ---- 4. Use-case themes over time ----
    themes = {
        "Chatbot/assistant": r"chatbot|chat bot|conversational|virtual assistant|assistant",
        "Search/retrieval": r"search|retrieval|knowledge management",
        "Customer support": r"customer support|customer service|support agent|help ?desk",
        "Copilot/dev tools": r"copilot|code assist|developer tool|ide|software develop",
        "Document/extract": r"document|ocr|invoice|contract|pdf|extract",
        "Automation/workflow": r"automat|workflow|back[- ]office|process autom",
        "Recommend/personalize": r"recommend|personaliz",
        "Analytics/BI": r"data analysis|analytics|insight|reporting|\bbi\b",
        "Agents/autonomous": r"\bagent|multi-agent|autonomous|agentic",
        "RAG/Q&A": r"\brag\b|retrieval-augmented|question answer|\bqa\b",
    }
    def use_text(job):
        uc = job.get("position", {}).get("use_cases") or []
        return " ".join(uc).lower()
    print("\n" + "=" * 78)
    print("4. USE-CASE THEMES (% of jobs whose use_cases match)")
    rows = []
    for name, pat in themes.items():
        rx = re.compile(pat)
        rows.append(trend_row(name, bd, lambda j, rx=rx: bool(rx.search(use_text(j)))))
    print_table("", rows)

    # ---- 5. Coding tools by ai-type & seniority ----
    code_tools = ["Claude Code", "GitHub Copilot", "Cursor", "Codeium", "Windsurf", "Codex"]
    print("\n" + "=" * 78)
    print("5. AI-CODING-TOOLS AS A SKILL (Claude Code/Copilot/Cursor/Codex)")
    print_table("% of jobs mentioning any coding tool", [
        trend_row("all jobs", bd, lambda j: has(j, "genai", *code_tools) or has(j, "other", *code_tools)),
    ])
    by_type = []
    for t in ["ai-first", "ai-support"]:
        by_type.append(trend_row(t, bd, lambda j, t=t: aitype(j) == t and (has(j, "genai", *code_tools) or has(j, "other", *code_tools))))
    print_table("% by ai-type", by_type)

    # ---- 6. ai-first sub-archetypes ----
    rag = lambda j: has(j, "genai", "RAG")
    agents = lambda j: has(j, "genai", "AI Agents", "Agentic Workflows", "Multi-Agent Systems")
    finetune = lambda j: has(j, "genai", "Fine-Tuning", "LoRA") or has(j, "ml", "Fine-Tuning", "LoRA")
    inference = lambda j: has(j, "ops", "vLLM", "Triton", "TensorRT", "Model Deployment") or has(j, "ml", "CUDA")
    print("\n" + "=" * 78)
    print("6. ai-first SUB-ARCHETYPES (% of ai-first jobs)")
    print_table("", [
        trend_row("RAG builder", ai_first, rag),
        trend_row("Agent builder", ai_first, agents),
        trend_row("Fine-tuner", ai_first, finetune),
        trend_row("Inference/serving", ai_first, inference),
        trend_row("RAG AND agents", ai_first, lambda j: rag(j) and agents(j)),
        trend_row("agents but NOT rag", ai_first, lambda j: agents(j) and not rag(j)),
    ])


if __name__ == "__main__":
    main()
