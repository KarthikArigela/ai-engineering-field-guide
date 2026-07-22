#!/usr/bin/env python3
"""Comprehensive deep-dive analyses for AI engineering roles.

Covers: latent role clustering, company-stage x archetype, AI-infra role
emergence, responsibilities verb evolution, eval/LLMOps maturity, skill
half-life (risers vs decliners), title->stack mapping, and FDE-in-AI.
k-means is implemented in numpy (no sklearn dependency).
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import yaml

STRUCTURED_DIR = Path(__file__).resolve().parents[2] / "data_structured"
DATES = sorted(d.name for d in STRUCTURED_DIR.iterdir()
               if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name))
LAB = {d: d[5:] for d in DATES}


def load():
    bd = defaultdict(list)
    for d in DATES:
        for f in (STRUCTURED_DIR / d).glob("*.yaml"):
            try:
                bd[d].append(yaml.safe_load(f.read_text(encoding="utf-8")))
            except Exception:
                pass
    return bd


BD = load()
ALL = [j for js in BD.values() for j in js]
N = len(ALL)


def sk(j):
    return (j.get("position", {}).get("skills") or {})


def has(j, cat, *names):
    lst = [s.lower() for s in (sk(j).get(cat) or [])]
    return any(n.lower() in lst for n in names)


def aitype(j):
    return j.get("position", {}).get("ai_type", {}).get("type")


def title(j):
    return (j.get("position", {}).get("title", "") or "").lower()


def stage_bucket(j):
    s = (j.get("company", {}).get("stage") or "").lower()
    if any(k in s for k in ["seed", "series a", "early", "startup", "pre-seed"]):
        return "Early (Seed-Series A)"
    if any(k in s for k in ["series b", "series c", "series d", "series e", "series f", "growth"]):
        return "Growth (Series B-F)"
    if any(k in s for k in ["public", "established", "private"]):
        return "Public/Late"
    return "Unknown"


def trend(label, fn, base=None):
    src = base if base is not None else BD
    cells = []
    for d in DATES:
        jobs = src[d] if isinstance(src, dict) else src
        cells.append(100.0 * sum(1 for j in jobs if fn(j)) / len(jobs))
        if not isinstance(src, dict):
            break
    return label, cells


def ptable(title_, rows):
    print("\n" + title_)
    print("  " + "".join(LAB[d].rjust(9) for d in DATES))
    for label, cells in rows:
        print("  " + label.ljust(38) + "".join(f"{c:7.1f}%  " for c in cells))


# --------------------------------------------------------------------------- #
# 1. LATENT ROLE CLUSTERING (spherical k-means on skill signatures)
# --------------------------------------------------------------------------- #
FEATURES = [
    ("RAG", "genai", ["RAG"]),
    ("Agents", "genai", ["AI Agents", "Agentic Workflows", "Multi-Agent Systems"]),
    ("LangChain", "genai", ["LangChain"]),
    ("LangGraph", "genai", ["LangGraph"]),
    ("MCP", "genai", ["MCP"]),
    ("Fine-Tuning", "genai", ["Fine-Tuning", "LoRA"]),
    ("OpenAI/Anthropic API", "genai", ["OpenAI API", "Anthropic API"]),
    ("Function Calling", "genai", ["Function Calling"]),
    ("Prompt Engineering", "genai", ["Prompt Engineering"]),
    ("Coding tools", "genai", ["Claude Code", "GitHub Copilot", "Cursor", "Codex"]),
    ("PyTorch/TF", "ml", ["PyTorch", "TensorFlow"]),
    ("Hugging Face", "ml", ["Hugging Face"]),
    ("RLHF", "ml", ["RLHF"]),
    ("React/Frontend", "web", ["React", "Vue", "Next.js"]),
    ("FastAPI/Flask", "web", ["FastAPI", "Flask"]),
    ("Node.js", "web", ["Node.js"]),
    ("AWS", "cloud", ["AWS"]),
    ("Azure", "cloud", ["Azure"]),
    ("GCP", "cloud", ["GCP"]),
    ("AI cloud svc", "cloud", ["AWS Bedrock", "Vertex AI", "SageMaker", "Azure OpenAI"]),
    ("Docker", "ops", ["Docker"]),
    ("Kubernetes", "ops", ["Kubernetes"]),
    ("CI/CD", "ops", ["CI/CD"]),
    ("Terraform", "ops", ["Terraform"]),
    ("MLOps", "ops", ["MLOps", "MLflow", "Kubeflow"]),
    ("Inference/serving", "ops", ["vLLM", "Triton", "TensorRT", "Model Deployment"]),
    ("Eval/observability", "ops", ["LangSmith", "Langfuse", "Weights & Biases"]),
    ("Vector DB", "databases", ["Vector Databases", "Pinecone", "Weaviate", "pgvector", "Milvus", "Qdrant", "Chroma"]),
    ("Spark/Databricks", "data", ["Spark", "Databricks", "PySpark"]),
    ("Kafka/Airflow", "data", ["Kafka", "Airflow"]),
    ("SQL", "languages", ["SQL"]),
]


def build_features(jobs):
    X = np.zeros((len(jobs), len(FEATURES)), dtype=float)
    for i, j in enumerate(jobs):
        for k, (_, cat, names) in enumerate(FEATURES):
            X[i, k] = 1.0 if has(j, cat, *names) else 0.0
    return X


def kmeans(X, k, seed=7, restarts=25):
    rng = np.random.default_rng(seed)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms[norms == 0] = 1
    Xn = X / norms
    best_labels, best_inertia = None, np.inf
    for _ in range(restarts):
        # k-means++ init
        centers = [Xn[rng.integers(len(Xn))]]
        for _ in range(1, k):
            d2 = np.min([np.sum((Xn - c) ** 2, axis=1) for c in centers], axis=0)
            probs = d2 / d2.sum() if d2.sum() else None
            centers.append(Xn[rng.choice(len(Xn), p=probs)])
        C = np.array(centers)
        for _ in range(60):
            D = 1 - Xn @ C.T  # cosine distance
            labels = np.argmin(D, axis=1)
            newC = np.zeros_like(C)
            for c in range(k):
                members = Xn[labels == c]
                if len(members):
                    v = members.mean(axis=0)
                    newC[c] = v / (np.linalg.norm(v) or 1)
                else:
                    newC[c] = C[c]
            if np.allclose(newC, C):
                C = newC
                break
            C = newC
        inertia = np.sum((Xn - C[labels]) ** 2)
        if inertia < best_inertia:
            best_inertia, best_labels = inertia, labels.copy()
    return best_labels


def cluster_analysis():
    print("=" * 80)
    print("1. LATENT ROLE ARCHETYPES (spherical k-means, k=6, on 31 skill features)")
    X = build_features(ALL)
    # drop jobs with zero features (can't cluster meaningfully)
    mask = X.sum(axis=1) > 0
    Xc = X[mask]
    jobs_c = [j for j, m in zip(ALL, mask) if m]
    labels = kmeans(Xc, k=6)
    overall = Xc.mean(axis=0)
    order = np.argsort([-(labels == c).sum() for c in range(6)])
    for idx, c in enumerate(order):
        members = labels == c
        size = int(members.sum())
        freq = Xc[members].mean(axis=0)
        lift = np.where(overall > 0, freq / overall, 0)
        top = np.argsort(-(lift * (freq > 0.20)))  # distinctive + present
        feats = [(FEATURES[i][0], freq[i], lift[i]) for i in top if freq[i] > 0.20][:7]
        cj = [jobs_c[i] for i in range(len(jobs_c)) if labels[i] == c]
        ai = Counter(aitype(j) for j in cj)
        cf = 100.0 * sum(1 for j in cj if j.get("position", {}).get("is_customer_facing")) / size
        ai1 = ai.get("ai-first", 0)
        print(f"\n  Cluster {idx+1}  (n={size}, {100*size/N:.1f}% of all jobs)  "
              f"ai-first {100*ai1/size:.0f}%  customer-facing {cf:.0f}%")
        print("    signature: " + ", ".join(f"{n} {f*100:.0f}%(x{l:.1f})" for n, f, l in feats))


# --------------------------------------------------------------------------- #
# 2. COMPANY STAGE x ARCHETYPE
# --------------------------------------------------------------------------- #
def stage_analysis():
    print("\n" + "=" * 80)
    print("2. COMPANY STAGE x ARCHETYPE (over/under-index vs all-jobs baseline)")
    buckets = ["Early (Seed-Series A)", "Growth (Series B-F)", "Public/Late", "Unknown"]
    fns = {
        "ai-first": lambda j: aitype(j) == "ai-first",
        "RAG": lambda j: has(j, "genai", "RAG"),
        "Agents": lambda j: has(j, "genai", "AI Agents", "Agentic Workflows", "Multi-Agent Systems"),
        "Fine-Tuning": lambda j: has(j, "genai", "Fine-Tuning", "LoRA"),
        "Coding tools": lambda j: has(j, "genai", "Claude Code", "GitHub Copilot", "Cursor", "Codex"),
        "PyTorch/TF": lambda j: has(j, "ml", "PyTorch", "TensorFlow"),
        "AWS": lambda j: has(j, "cloud", "AWS"),
        "Docker/K8s": lambda j: has(j, "ops", "Docker", "Kubernetes"),
    }
    base = {k: 100.0 * sum(1 for j in ALL if fn(j)) / N for k, fn in fns.items()}
    print(f"  baseline (all jobs): " + ", ".join(f"{k} {v:.1f}%" for k, v in base.items()))
    for b in buckets:
        bj = [j for j in ALL if stage_bucket(j) == b]
        if not bj:
            continue
        print(f"\n  {b} (n={len(bj)}):")
        for k, fn in fns.items():
            v = 100.0 * sum(1 for j in bj if fn(j)) / len(bj)
            idx = v / base[k] if base[k] else 1
            flag = "  " if 0.9 <= idx <= 1.1 else ("↑" if idx > 1.1 else "↓")
            print(f"    {k:14s} {v:5.1f}%  (x{idx:.2f}) {flag}")


# --------------------------------------------------------------------------- #
# 3. AI-INFRA / INFERENCE ROLE EMERGENCE
# --------------------------------------------------------------------------- #
def infra_analysis():
    print("\n" + "=" * 80)
    print("3. AI-INFRA / INFERENCE ROLE EMERGENCE (% of ai-first jobs)")
    aif = {d: [j for j in BD[d] if aitype(j) == "ai-first"] for d in DATES}
    ptable("", [
        trend("vLLM", lambda j: has(j, "ops", "vLLM"), aif),
        trend("Triton", lambda j: has(j, "ops", "Triton"), aif),
        trend("TensorRT", lambda j: has(j, "ops", "TensorRT"), aif),
        trend("Model Deployment", lambda j: has(j, "ops", "Model Deployment"), aif),
        trend("CUDA", lambda j: has(j, "ml", "CUDA"), aif),
        trend("ANY inference/serving", lambda j: has(j, "ops", "vLLM", "Triton", "TensorRT", "Model Deployment") or has(j, "ml", "CUDA"), aif),
        trend("Kubernetes (infra proxy)", lambda j: has(j, "ops", "Kubernetes"), aif),
    ])


# --------------------------------------------------------------------------- #
# 4. RESPONSIBILITIES VERB EVOLUTION
# --------------------------------------------------------------------------- #
def resp_analysis():
    print("\n" + "=" * 80)
    print("4. RESPONSIBILITIES VERB EVOLUTION (% of jobs whose responsibilities match)")
    groups = {
        "train/research/optimize": r"train|research|optimiz|fine-tun|fine tun|experiment|tune model",
        "ship/deploy/integrate": r"\bship|deploy|integrat|productioniz|roll out|launch|put into production",
        "design/architect": r"\bdesign|architect",
        "build/develop": r"\bbuild|develop|implement|engineer",
        "collaborate/partner": r"collaborat|partner|stakeholder|cross-functional|work with",
        "scale/performance": r"scale|performance|latency|throughput|efficient",
        "evaluate/test": r"evaluat|test|monitor|benchmark|qa",
    }

    def text(j):
        return " ".join(j.get("position", {}).get("responsibilities") or []).lower()

    rows = []
    for name, pat in groups.items():
        rx = re.compile(pat)
        rows.append(trend(name, lambda j, rx=rx: bool(rx.search(text(j)))))
    ptable("", rows)


# --------------------------------------------------------------------------- #
# 5. EVAL / LLMOps MATURITY
# --------------------------------------------------------------------------- #
def eval_analysis():
    print("\n" + "=" * 80)
    print("5. EVAL / LLMOps MATURITY (% of jobs mentioning)")
    ptable("", [
        trend("LangSmith", lambda j: has(j, "ops", "LangSmith")),
        trend("Langfuse", lambda j: has(j, "ops", "Langfuse")),
        trend("Guardrails", lambda j: has(j, "genai", "Guardrails")),
        trend("LLM Evaluation", lambda j: has(j, "genai", "LLM Evaluation")),
        trend("LLM-specific eval (any)", lambda j: has(j, "ops", "LangSmith", "Langfuse") or has(j, "genai", "Guardrails", "LLM Evaluation")),
        trend("MLOps (MLflow/Kubeflow)", lambda j: has(j, "ops", "MLOps", "MLflow", "Kubeflow")),
        trend("W&B", lambda j: has(j, "ops", "Weights & Biases")),
        trend("Infra monitoring (any)", lambda j: has(j, "ops", "Datadog", "Prometheus", "Grafana", "OpenTelemetry")),
    ])


# --------------------------------------------------------------------------- #
# 6. SKILL HALF-LIFE (risers vs decliners)
# --------------------------------------------------------------------------- #
def slope(cells):
    x = np.arange(len(cells))
    return float(np.polyfit(x, cells, 1)[0])  # pp per scrape


def halflife_analysis():
    print("\n" + "=" * 80)
    print("6. SKILL TRAJECTORIES (first -> last %, slope in pp/scrape)")
    items = [
        ("MCP", "genai", "MCP"), ("Coding tools", "genai", "Claude Code"),
        ("Prompt Engineering", "genai", "Prompt Engineering"), ("LangGraph", "genai", "LangGraph"),
        ("LLM Evaluation", "genai", "LLM Evaluation"), ("SQL", "languages", "SQL"),
        ("RAG", "genai", "RAG"), ("Agents", "genai", "AI Agents"),
        ("PyTorch", "ml", "PyTorch"), ("TensorFlow", "ml", "TensorFlow"),
        ("Fine-Tuning", "genai", "Fine-Tuning"), ("RLHF", "ml", "RLHF"),
        ("Function Calling", "genai", "Function Calling"), ("Guardrails", "genai", "Guardrails"),
        ("AWS Bedrock", "cloud", "AWS Bedrock"), ("Docker", "ops", "Docker"),
        ("CI/CD", "ops", "CI/CD"), ("Kubernetes", "ops", "Kubernetes"),
        ("Embeddings", "genai", "Embeddings"),
    ]
    rows = []
    for label, cat, name in items:
        _, cells = trend(label, lambda j, cat=cat, name=name: has(j, cat, name))
        rows.append((label, cells[0], cells[-1], slope(cells)))
    risers = sorted(rows, key=lambda r: r[3], reverse=True)
    decliners = sorted(rows, key=lambda r: r[3])
    print("  RISERS:")
    for l, a, b, s in risers[:8]:
        print(f"    {l:22s} {a:5.1f}% -> {b:5.1f}%  ({s:+.2f} pp/scrape)")
    print("  DECLINERS:")
    for l, a, b, s in decliners[:8]:
        print(f"    {l:22s} {a:5.1f}% -> {b:5.1f}%  ({s:+.2f} pp/scrape)")


# --------------------------------------------------------------------------- #
# 7. TITLE -> STACK MAPPING
# --------------------------------------------------------------------------- #
def title_stack():
    print("\n" + "=" * 80)
    print("7. TITLE -> STACK MAPPING")
    groups = {
        '"ai engineer"': lambda t: "ai engineer" in t,
        '"software/backend engineer"': lambda t: ("software engineer" in t or "backend" in t or "full stack" in t or "full-stack" in t) and "ai engineer" not in t,
        '"ml engineer/scientist"': lambda t: "ml engineer" in t or "machine learning engineer" in t or "scientist" in t,
        '"applied/forward deployed"': lambda t: "applied" in t or "forward deploy" in t or "fde" in t,
        '"platform/infra/devops"': lambda t: any(k in t for k in ["platform", "infrastructure", "infra", "devops", "mlops", "sre"]),
        '"data engineer"': lambda t: "data engineer" in t,
    }
    metrics = {
        "ai-first%": lambda js: 100 * sum(aitype(j) == "ai-first" for j in js) / len(js),
        "cust-facing%": lambda js: 100 * sum(j.get("position", {}).get("is_customer_facing") for j in js) / len(js),
        "RAG%": lambda js: 100 * sum(has(j, "genai", "RAG") for j in js) / len(js),
        "Agents%": lambda js: 100 * sum(has(j, "genai", "AI Agents", "Agentic Workflows", "Multi-Agent Systems") for j in js) / len(js),
        "PyTorch/TF%": lambda js: 100 * sum(has(j, "ml", "PyTorch", "TensorFlow") for j in js) / len(js),
        "Fine-Tune%": lambda js: 100 * sum(has(j, "genai", "Fine-Tuning", "LoRA") for j in js) / len(js),
        "K8s%": lambda js: 100 * sum(has(j, "ops", "Kubernetes") for j in js) / len(js),
        "Python%": lambda js: 100 * sum(has(j, "languages", "Python") for j in js) / len(js),
    }
    header = "  group".ljust(30) + "".join(m.rjust(11) for m in metrics)
    print(header)
    for gname, fn in groups.items():
        js = [j for j in ALL if fn(title(j))]
        if not js:
            continue
        line = (gname + f" (n={len(js)})").ljust(30)
        for mname, mfn in metrics.items():
            line += f"{mfn(js):10.0f}% "
        print(line)


# --------------------------------------------------------------------------- #
# 8. FDE IN AI
# --------------------------------------------------------------------------- #
def fde_analysis():
    print("\n" + "=" * 80)
    print("8. FORWARD DEPLOYED ENGINEER (FDE) IN AI")
    is_fde = lambda j: bool(re.search(r"forward deploy|fde|forward-deployed", title(j)))
    fdes = [j for j in ALL if is_fde(j)]
    nonfde_aif = [j for j in ALL if not is_fde(j) and aitype(j) == "ai-first"]
    print(f"  FDE postings: {len(fdes)} of {N} ({100*len(fdes)/N:.1f}%)")
    print("  FDE monthly count / share:")
    print("  " + "".join(LAB[d].rjust(9) for d in DATES))
    counts = [sum(1 for j in BD[d] if is_fde(j)) for d in DATES]
    shares = [100 * sum(1 for j in BD[d] if is_fde(j)) / len(BD[d]) for d in DATES]
    print("  count: " + "".join(f"{c:>9}" for c in counts))
    print("  share: " + "".join(f"{s:8.1f}%" for s in shares))

    def col(js, fn):
        return 100 * sum(1 for j in js if fn(j)) / len(js) if js else 0

    rows = [
        ("ai-first%", lambda j: aitype(j) == "ai-first"),
        ("ai-support%", lambda j: aitype(j) == "ai-support"),
        ("customer-facing%", lambda j: j.get("position", {}).get("is_customer_facing")),
        ("RAG%", lambda j: has(j, "genai", "RAG")),
        ("Agents%", lambda j: has(j, "genai", "AI Agents", "Agentic Workflows", "Multi-Agent Systems")),
        ("PyTorch/TF%", lambda j: has(j, "ml", "PyTorch", "TensorFlow")),
        ("Fine-Tune%", lambda j: has(j, "genai", "Fine-Tuning", "LoRA")),
        ("Python%", lambda j: has(j, "languages", "Python")),
        ("AWS%", lambda j: has(j, "cloud", "AWS")),
    ]
    print("\n  FDE vs other ai-first roles:")
    print("    " + "".join(n.rjust(18) for n in ["metric", "FDE", "other ai-first"]))
    for name, fn in rows:
        print(f"    {name:16s}{col(fdes, fn):17.0f}%{col(nonfde_aif, fn):11.0f}%")
    # top use cases for FDE
    uc = Counter()
    for j in fdes:
        for u in (j.get("position", {}).get("use_cases") or []):
            for w in re.findall(r"[a-z]+", u.lower()):
                if w not in {"ai", "for", "and", "the", "to", "of", "with", "in", "into", "data", "system", "systems", "model", "models", "customer", "customers"}:
                    uc[w] += 1
    print("\n  FDE use-case keywords: " + ", ".join(f"{w}({n})" for w, n in uc.most_common(15)))


def main():
    cluster_analysis()
    stage_analysis()
    infra_analysis()
    resp_analysis()
    eval_analysis()
    halflife_analysis()
    title_stack()
    fde_analysis()


if __name__ == "__main__":
    main()
