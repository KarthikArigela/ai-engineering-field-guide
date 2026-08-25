#!/usr/bin/env python3
"""Canonicalize skill names in structured job YAMLs.

Collapses the many casing / acronym / synonym variants the LLM extractor
emits (e.g. "RAG"/"rag"/"RAG pipelines", "MCP"/"MCP (Model Context Protocol)",
"agents"/"AI agents"/"Agentic AI") into one canonical form per concept, and
dedupes within each category.

Reuses the exact YAML formatting of the extractor (flow-style skill lists,
literal-block long text) so files whose skills are unchanged stay byte-identical.

Usage:
    uv run python canonicalize_skills.py --dry-run     # show impact, write nothing
    uv run python canonicalize_skills.py --check        # round-trip check (no skill changes)
    uv run python canonicalize_skills.py                # apply
"""
from __future__ import annotations

import argparse
import re
import sys
import textwrap
from collections import Counter
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
INTERNAL_ROOT = SCRIPT_DIR.parent
STRUCTURED_DIR = INTERNAL_ROOT.parent / "data_structured"


# --------------------------------------------------------------------------- #
# Canonical skill vocabulary
# --------------------------------------------------------------------------- #
# Each entry: (canonical display name, [aliases]) -- aliases are matched
# case-insensitively after normalization. The canonical name's own normalized
# form is included automatically. Keep these conservative: only merge names
# that refer to the same concept.
CANON = {
    "genai": [
        ("RAG", ["rag pipelines", "rag pipeline", "rag architectures", "rag architecture",
                 "rag (retrieval-augmented generation)", "retrieval-augmented generation",
                 "retrieval augmented generation", "advanced rag", "rag systems",
                 "rag frameworks", "rag implementation", "rag pipelines"]),
        ("Prompt Engineering", ["prompt design", "prompt tuning", "prompt optimization",
                                "prompt patterns", "prompt crafting"]),
        ("LangChain", ["langchain", "lang chain", "lang-chain"]),
        ("LangGraph", ["langgraph", "lang graph"]),
        ("LlamaIndex", ["llamaindex", "llama index", "lama index"]),
        ("CrewAI", ["crewai", "crew ai"]),
        ("AutoGen", ["autogen", "auto-gen", "autogen studio"]),
        ("Semantic Kernel", ["semantic kernel"]),
        ("DSPy", ["dspy"]),
        ("Haystack", ["haystack", "haystack ai", "deepset haystack"]),
        ("Phidata", ["phidata"]),
        ("Instructor", ["instructor"]),
        ("Marvin", ["marvin"]),
        ("MCP", ["mcp (model context protocol)", "model context protocol",
                 "model context protocol (mcp)", "model context protocol(mcp)"]),
        ("OpenAI API", ["openai apis", "openai api", "openai"]),
        ("Anthropic API", ["anthropic apis", "anthropic api", "anthropic",
                           "claude api", "anthropic claude", "claude"]),
        ("Gemini", ["gemini", "google gemini", "gemini api"]),
        ("LLMs", ["llm", "large language models", "large language model",
                  "llm apis", "llm integration", "llm orchestration", "llm orchestration frameworks"]),
        ("Generative AI", ["generative artificial intelligence", "genai", "gen ai", "generative-ai"]),
        ("AI Agents", ["agents", "agent", "ai agent", "agentic ai", "agentic"]),
        ("Agentic Workflows", ["agent orchestration", "agent frameworks", "agentic systems",
                               "agentic orchestration", "multi-agent orchestration"]),
        ("Multi-Agent Systems", ["multi-agent", "multi-agent frameworks"]),
        ("Function Calling", ["tool use", "tool calling", "tool-use", "function-calling", "tool calls"]),
        ("Embeddings", ["embedding", "embedding models", "text embeddings", "vector embeddings"]),
        ("Fine-Tuning", ["fine tuning", "llm fine-tuning", "model fine-tuning"]),
        ("LoRA", ["peft", "qlora", "low-rank adaptation"]),
        ("Guardrails", ["nemo guardrails", "guardrails ai", "neuronal guardrails", "nemo"]),
        ("LLM Evaluation", ["llm eval", "evaluation frameworks", "eval frameworks", "llm evaluations"]),
        ("Structured Outputs", ["structured output", "json schema outputs", "structured generation"]),
        ("Claude Code", ["claude code"]),
        ("GitHub Copilot", ["copilot", "github copilot ai"]),
        ("Cursor", ["cursor ide", "cursor editor"]),
        ("Codeium", ["codeium"]),
        ("Windsurf", ["windsurf"]),
        ("Codex", ["openai codex"]),
        ("Bedrock", []),
    ],
    "ml": [
        ("PyTorch", ["py torch"]),
        ("TensorFlow", ["tensor flow", "tf"]),
        ("scikit-learn", ["sklearn", "scikit learn"]),
        ("Keras", []),
        ("JAX", []),
        ("XGBoost", []),
        ("LightGBM", []),
        ("Hugging Face", ["huggingface", "hugging face transformers", "hf transformers",
                          "huggingface transformers"]),
        ("CUDA", []),
        ("Deep Learning", ["deep neural networks"]),
        ("Machine Learning", ["ml"]),
        ("Reinforcement Learning", ["rl"]),
        ("NLP", ["natural language processing"]),
        ("Model Training", ["training models", "training"]),
        ("Model Evaluation", ["model eval"]),
        ("Fine-Tuning", ["model fine-tuning"]),
        ("RLHF", ["reinforcement learning from human feedback"]),
        ("LoRA", ["peft", "qlora"]),
        ("Quantization", ["model quantization"]),
        ("Embeddings", ["embedding models", "embedding"]),
        ("NumPy", []),
        ("Pandas", []),
        ("Transformers", ["transformer architectures", "transformer models", "transformer models"]),
        ("ONNX", []),
        ("spaCy", []),
        ("Feature Engineering", []),
        ("OpenCV", []),
        ("CNNs", ["convolutional neural networks"]),
        ("RNNs", ["recurrent neural networks"]),
        ("GANs", ["generative adversarial networks"]),
        ("BERT", []),
        ("Anomaly Detection", []),
        ("Neural Networks", ["neural nets"]),
        ("Llama", ["llama 2", "llama 3", "meta llama"]),
        ("Diffusion Models", ["diffusion", "stable diffusion"]),
    ],
    "web": [
        ("REST APIs", ["rest api", "restful apis", "restful api", "restful", "rest api design"]),
        ("React", ["react.js", "reactjs", "react js"]),
        ("FastAPI", ["fast api"]),
        ("Node.js", ["nodejs", "node js", "node"]),
        ("Microservices", ["microservices architecture", "microservice architecture"]),
        ("GraphQL", []),
        ("Next.js", ["nextjs"]),
        ("Angular", ["angularjs"]),
        ("Django", []),
        ("APIs", ["api design", "api development", "api integration", "api integrations"]),
        ("gRPC", []),
        ("Spring Boot", ["spring"]),
        ("Vue", ["vue.js", "vuejs"]),
        ("Ruby on Rails", ["rails"]),
        ("WebSockets", ["websocket", "websocket api"]),
        ("Streamlit", []),
        ("Pydantic", []),
        ("OAuth", ["oauth2", "oauth 2.0"]),
        ("Full-Stack Development", ["full stack development", "fullstack development"]),
        ("REST", ["restful services"]),
    ],
    "cloud": [
        ("AWS", ["amazon web services"]),
        ("Azure", ["microsoft azure"]),
        ("GCP", ["google cloud platform", "google cloud"]),
        ("AWS Bedrock", ["amazon bedrock", "bedrock"]),
        ("AWS Lambda", ["lambda"]),
        ("Vertex AI", ["gcp vertex ai", "google vertex ai"]),
        ("SageMaker", ["aws sagemaker", "amazon sagemaker"]),
        ("AWS S3", ["amazon s3", "s3"]),
        ("Azure OpenAI", ["azure openai service"]),
        ("Azure ML", ["azure machine learning"]),
        ("Azure AI Foundry", ["azure ai studio"]),
        ("Azure Functions", []),
        ("EKS", ["aws eks", "amazon eks"]),
        ("ECS", ["aws ecs"]),
        ("IAM", ["aws iam"]),
        ("API Gateway", ["aws api gateway"]),
        ("Cloud Run", ["google cloud run"]),
        ("Azure AI Search", ["azure search"]),
        ("CloudWatch", ["aws cloudwatch"]),
        ("AKS", ["azure kubernetes service"]),
        ("Vercel", []),
    ],
    "ops": [
        ("Docker", ["docker compose", "containers"]),
        ("CI/CD", ["ci cd", "cicd", "continuous integration",
                   "continuous integration/continuous deployment", "ci/cd pipelines"]),
        ("Kubernetes", ["k8s"]),
        ("MLOps", []),
        ("Terraform", ["opentofu"]),
        ("Git", []),
        ("MLflow", []),
        ("GitHub Actions", []),
        ("Jenkins", []),
        ("Grafana", []),
        ("Prometheus", []),
        ("DevOps", []),
        ("Observability", ["observability and monitoring", "monitoring and observability"]),
        ("LLMOps", []),
        ("Kubeflow", []),
        ("Datadog", []),
        ("LangSmith", []),
        ("OpenTelemetry", ["otel"]),
        ("Monitoring", []),
        ("Infrastructure as Code", ["iac"]),
        ("Helm", []),
        ("vLLM", []),
        ("Distributed Systems", []),
        ("Weights & Biases", ["w&b", "wandb"]),
        ("Langfuse", []),
        ("Ansible", []),
        ("Model Deployment", ["model serving", "llm serving", "llm inference", "inference serving"]),
        ("CloudFormation", ["aws cloudformation"]),
        ("GitLab CI", ["gitlab"]),
        ("TensorRT", []),
        ("Triton", ["triton inference server"]),
        ("ArgoCD", ["argo cd", "argo"]),
        ("Model Monitoring", []),
        ("GitOps", []),
        ("DevSecOps", []),
        ("Temporal", []),
        ("ELK Stack", ["elasticsearch logstash kibana"]),
        ("Splunk", []),
        ("OpenShift", []),
        ("Linux", []),
        ("GitHub", []),
    ],
    "languages": [
        ("Python", []),
        ("SQL", []),
        ("TypeScript", ["ts"]),
        ("Java", []),
        ("JavaScript", ["js", "javascript (es6+)"]),
        ("Go", ["golang", "go (golang)"]),
        ("C++", ["c/c++"]),
        ("C#", ["c#/.net"]),
        ("Node.js", ["nodejs", "node js"]),
        ("Scala", []),
        ("Rust", []),
        ("Bash", ["shell scripting", "shell", "unix shell scripting"]),
        ("Kotlin", []),
        ("Ruby", []),
        ("PowerShell", []),
        ("Swift", []),
        ("PHP", []),
        ("Elixir", []),
        ("Apex", []),
        ("Perl", []),
        ("Groovy", []),
        ("Clojure", []),
        ("PySpark", []),
        ("asyncio", ["async programming"]),
        ("Pydantic", []),
    ],
    "databases": [
        ("PostgreSQL", ["postgres"]),
        ("Vector Databases", ["vector database", "vectordbs", "vector dbs", "vector stores",
                              "vector store", "vector db"]),
        ("Pinecone", []),
        ("Snowflake", []),
        ("Weaviate", []),
        ("Redis", []),
        ("SQL", []),
        ("MongoDB", ["mongo"]),
        ("pgvector", []),
        ("BigQuery", []),
        ("FAISS", ["faiss"]),
        ("MySQL", []),
        ("NoSQL", ["nosql databases"]),
        ("Milvus", []),
        ("DynamoDB", []),
        ("Qdrant", []),
        ("Elasticsearch", ["elastic search"]),
        ("Neo4j", []),
        ("Chroma", ["chromadb"]),
        ("SQL Server", ["microsoft sql server"]),
        ("OpenSearch", []),
        ("ClickHouse", []),
        ("Vector Search", ["similarity search", "vector retrieval"]),
        ("Cassandra", []),
        ("Oracle", []),
        ("Redshift", ["amazon redshift"]),
        ("Supabase", []),
        ("Cosmos DB", []),
        ("Delta Lake", []),
        ("Knowledge Graphs", ["knowledge graph"]),
        ("Graph Databases", ["graph database"]),
        ("Relational Databases", ["relational database", "rdbms"]),
        ("Semantic Search", []),
    ],
    "data": [
        ("Kafka", ["apache kafka"]),
        ("Databricks", []),
        ("Airflow", ["apache airflow"]),
        ("Spark", ["apache spark"]),
        ("Data Pipelines", ["data pipeline", "etl", "etl/elt", "etl pipelines",
                            "etl/elt pipelines", "elt"]),
        ("Pandas", []),
        ("dbt", []),
        ("PySpark", []),
        ("NumPy", []),
        ("Hadoop", []),
        ("Ray", []),
        ("Prefect", []),
        ("Dagster", []),
        ("RabbitMQ", []),
        ("Data Modeling", []),
        ("Flink", ["apache flink"]),
        ("Delta Lake", []),
        ("Power BI", []),
        ("Tableau", []),
        ("Kinesis", ["aws kinesis"]),
        ("Fivetran", []),
        ("n8n", []),
        ("Azure Data Factory", []),
        ("Data Governance", []),
        ("Hive", []),
        ("Dask", []),
        ("Celery", []),
        ("Pub/Sub", ["google pub/sub"]),
        ("Looker", []),
        ("Unity Catalog", []),
        ("Segment", []),
    ],
    "domains": [
        ("NLP", ["natural language processing"]),
        ("Computer Vision", ["cv"]),
        ("Reinforcement Learning", ["rl"]),
        ("Cybersecurity", ["cyber security"]),
        ("HIPAA Compliance", ["hipaa"]),
        ("Healthcare Standards", ["fhir", "hl7", "dicom", "ccda"]),
        ("Healthcare AI", ["healthcare data", "healthcare domain knowledge"]),
        ("OCR", []),
        ("OpenCV", []),
        ("Responsible AI", ["ai ethics"]),
        ("Conversational AI", []),
        ("Diffusion Models", []),
        ("Recommender Systems", ["recommendation systems"]),
        ("Fraud Detection", []),
        ("Information Retrieval", []),
        ("Object Detection", []),
        ("Generative AI", []),
        ("Multimodal AI", []),
        ("Robotics", []),
        ("Speech Recognition", ["asr (automatic speech recognition)", "automatic speech recognition"]),
        ("NLU", []),
    ],
    "other": [
        ("Distributed Systems", ["distributed systems design"]),
        ("Salesforce", []),
        ("Cursor", []),
        ("Agile", ["agile/scrum", "agile methodologies", "agile development", "scrum"]),
        ("GitHub Copilot", ["copilot"]),
        ("Jira", []),
        ("System Design", ["solution architecture", "system architecture"]),
        ("HIPAA Compliance", ["hipaa"]),
        ("n8n", []),
        ("Zapier", []),
        ("HubSpot", []),
        ("ServiceNow", []),
        ("Power Automate", []),
        ("Power BI", []),
        ("Tableau", []),
        ("Responsible AI", ["ai governance", "ai ethics"]),
        ("GDPR", []),
        ("Claude Code", []),
        ("UiPath", []),
        ("Microservices", ["microservices architecture"]),
        ("A/B Testing", ["ab testing"]),
        ("Confluence", []),
        ("Git", []),
        ("Workato", []),
        ("RPA", ["robotic process automation"]),
        ("Event-Driven Architecture", []),
        ("SAP", []),
        ("Slack", []),
        ("Code Review", []),
        ("Figma", []),
        ("Workday", []),
        ("SOC 2", ["soc 2 compliance"]),
        ("RBAC", ["role-based access control"]),
        ("JSON", []),
        ("OAuth", []),
        ("JWT", []),
        ("Workflow Automation", []),
        ("Automation Anywhere", []),
        ("Microsoft 365", ["m365"]),
    ],
}


def _norm(s: str) -> str:
    """Lowercase, strip quotes/punctuation, collapse whitespace."""
    s = s.strip().strip('"').strip("'").rstrip(".").strip()
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s


def _strip_parens(s: str) -> str:
    return re.sub(r"\s*\(.*?\)\s*", " ", s).strip()


def _build_lookup():
    """category -> {normalized_alias: canonical_display}."""
    lookup = {}
    for cat, entries in CANON.items():
        m = {}
        for canonical, aliases in entries:
            keys = [_norm(canonical)] + [_norm(a) for a in aliases]
            for k in keys:
                if k:
                    m[k] = canonical
        lookup[cat] = m
    return lookup


LOOKUP = _build_lookup()


def canonicalize_list(category: str, skills: list[str]) -> list[str]:
    """Map + dedupe a skill list for one category. Preserves first-seen order."""
    if not isinstance(skills, list):
        return skills
    table = LOOKUP.get(category, {})
    seen = set()
    out = []
    for raw in skills:
        if not isinstance(raw, str) or not raw.strip():
            continue
        n = _norm(raw)
        canon = table.get(n)
        if canon is None:  # try without parenthetical expansions
            canon = table.get(_norm(_strip_parens(raw)))
        if canon is None:
            canon = raw.strip()
        key = _norm(canon)
        if key in seen:
            continue
        seen.add(key)
        out.append(canon)
    return out


# --------------------------------------------------------------------------- #
# YAML writer (mirrors extract_llm.write_yaml_with_wrapping exactly)
# --------------------------------------------------------------------------- #
class LiteralString(str):
    pass


class FlowList(list):
    pass


def _represent_literal(dumper, data):
    if "\n" in data or len(data) > 60:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def _represent_flow(dumper, data):
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True)


yaml.add_representer(LiteralString, _represent_literal)
yaml.add_representer(FlowList, _represent_flow)

WRAP_FIELDS = {"reasoning", "use_cases", "responsibilities", "focus"}
SKILL_CATS = {"genai", "ml", "web", "databases", "data", "cloud", "ops",
              "languages", "domains", "other"}


def _wrap(data, parent_key=""):
    wrapped = {}
    for k, v in data.items():
        if isinstance(v, str) and (k in WRAP_FIELDS or parent_key in WRAP_FIELDS):
            if len(v) > 60 or "\n" in v:
                wrapped[k] = LiteralString(textwrap.fill(v, width=60).strip())
            else:
                wrapped[k] = v
        elif isinstance(v, dict):
            wrapped[k] = _wrap(v, parent_key=k)
        elif isinstance(v, list):
            if k == "skills" or parent_key in SKILL_CATS or k in SKILL_CATS:
                wrapped[k] = FlowList(v)
            else:
                wrapped[k] = [_wrap(i, parent_key=k) if isinstance(i, dict) else i for i in v]
        else:
            wrapped[k] = v
    return wrapped


def dump_yaml(data: dict) -> str:
    return yaml.dump(_wrap(data), default_flow_style=False, allow_unicode=True, sort_keys=False)


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def load_jobs(root: Path | None = None):
    files = sorted((root or STRUCTURED_DIR).rglob("*.yaml"))
    return files


def skills_of(job: dict) -> dict:
    return job.get("position", {}).get("skills", {}) or {}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="analyze only, write nothing")
    ap.add_argument("--check", action="store_true", help="round-trip: flag files that would change")
    ap.add_argument("--dir", type=Path, default=STRUCTURED_DIR,
                    help="directory to canonicalize; point it at a staging copy "
                         "when re-extracting before the swap")
    args = ap.parse_args()

    files = load_jobs(args.dir)
    print(f"Scanning {len(files)} structured YAML files in {args.dir}\n")

    before_counts = {c: Counter() for c in CANON}
    after_counts = {c: Counter() for c in CANON}
    changed_files = 0
    total_skills_before = 0
    total_skills_after = 0
    check_mismatches = []

    for f in files:
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  SKIP (parse error) {f.name}: {e}")
            continue
        if not isinstance(data, dict):
            continue

        skills = skills_of(data)
        new_skills = {}
        changed = False
        for cat in SKILL_CATS:
            old = skills.get(cat, []) or []
            new = canonicalize_list(cat, list(old))
            for s in old:
                if isinstance(s, str):
                    before_counts[cat][_norm(s)] += 1
            for s in new:
                after_counts[cat][_norm(s)] += 1
            total_skills_before += len(old)
            total_skills_after += len(new)
            if [str(x) for x in new] != [str(x) for x in old]:
                changed = True
            new_skills[cat] = new

        if not changed:
            if args.check:
                # verify writer reproduces original bytes for an unchanged file
                original = f.read_text(encoding="utf-8")
                redumped = dump_yaml(data)
                if redumped.rstrip("\n") != original.rstrip("\n"):
                    check_mismatches.append(f.name)
            continue

        changed_files += 1
        data["position"]["skills"] = new_skills

        if args.dry_run or args.check:
            continue

        out = dump_yaml(data)
        f.write_text(out, encoding="utf-8")

    print(f"Files with skill changes: {changed_files}")
    print(f"Total skill entries: {total_skills_before} -> {total_skills_after} "
          f"(removed {total_skills_before - total_skills_after} duplicates)\n")

    print("Unique skill concepts per category (before -> after):")
    for cat in CANON:
        b, a = len(before_counts[cat]), len(after_counts[cat])
        print(f"  {cat:11s} {b:4d} -> {a:4d}  ({b - a:+d})")

    if args.check:
        print(f"\nRound-trip check: {len(check_mismatches)} unchanged files would differ on re-dump")
        if check_mismatches[:10]:
            print("  examples:", check_mismatches[:10])

    # Show the biggest merged clusters (concepts that absorbed the most aliases)
    print("\nTop merged clusters in genai (canonical absorbed these many raw forms):")
    canon_raw_forms = {c: {} for c in CANON}
    LOOKUP_INV = {}
    for cat, m in LOOKUP.items():
        inv = {}
        for alias, canon in m.items():
            inv.setdefault(canon, set()).add(alias)
        LOOKUP_INV[cat] = inv
    # recount raw forms from data for genai to show real absorption
    genai_before = Counter()
    files2 = load_jobs(args.dir)
    for f in files2:
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(data, dict):
            for s in skills_of(data).get("genai", []) or []:
                if isinstance(s, str):
                    genai_before[_norm(s)] += 1
    print("  (most frequent raw skill strings, for reference):")
    for k, v in genai_before.most_common(25):
        canon = LOOKUP["genai"].get(k) or LOOKUP["genai"].get(_norm(_strip_parens(k)))
        tag = f" -> {canon}" if canon and canon.lower() != k else ""
        print(f"    {v:5d}  {k}{tag}")


if __name__ == "__main__":
    main()
