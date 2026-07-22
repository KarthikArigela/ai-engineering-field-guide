# AI Engineering Job Market Trends - Appendix

Detailed tables, cluster signatures, methodology, and reproduction notes for [the trends summary](trends.md).

## Data and methodology

Six scrapes of builtin.com, each an independent cross-section:

- Feb 4: 895 postings
- Feb 27: 870
- Mar 27: 677
- Apr 22: 645
- May 29: 919
- Jun 25: 888

Total: 4,894 postings. Job IDs do not overlap between scrapes, so I treat each month as a fresh sample of the market. Percentages are the share of postings (within a given denominator) whose structured skill / use-case / title fields match.

Roles are tagged ai-first (the core AI engineer), ai-support (software/ML/data roles with AI scope), ml-first (traditional ML), or unknown. The headline analyses run within ai-first unless noted, since that is where the role is actually being defined.

Skills are normalized through [canonicalize_skills.py](_internal/analysis/canonicalize_skills.py), which collapses case, acronym, and synonym variants (450 duplicates removed across 4,294 files). The extraction prompt in [extract_llm.py](_internal/extract_llm.py) now enforces a canonical vocabulary scoped to skills appearing more than 30 times.

The "slope" metric in the trajectory sections is the slope of an OLS line fit to the six monthly shares, in percentage points per scrape.

## Cluster signatures

Spherical k-means (cosine distance, k-means++ init, k=6, seed=7, implemented in numpy) on a 31-skill binary signature per posting. Each cluster's top skills (share of cluster members):

- RAG app builder (1,252 postings, 25.6%). `RAG` 90%, vector databases 71%, `LangChain` 64%, `OpenAI API`/`Anthropic API` 36%, `LangGraph` 36%, AI cloud services 27%, `FastAPI`/`Flask` 25%. The dominant archetype.
- Cloud / ML platform engineer (1,041, 21.3%). `AWS` 94%, `GCP` 89%, `Azure` 87%, `Docker` 47%, `Kubernetes` 42%, `MLOps` 27%, `PyTorch`/`TensorFlow` 31%.
- Agent builder (825, 16.9%). agents 76%, `Prompt Engineering` 74%, `RAG` 46%.
- DevOps / infra engineer (723, 14.8%). `Docker` 76%, `Kubernetes` 74%, `CI/CD` 74%, `Terraform` 28%, `AWS` 40%, `SQL` 20%. Only 52% ai-first - the least AI-native cluster.
- ML trainer / researcher (406, 8.3%). `PyTorch`/`TensorFlow` 71%, `SQL` 33%, `MLOps` 21%. Small and shrinking.
- Full-stack AI engineer (358, 7.3%). `React`/frontend 89%, `Node.js` 26%, `OpenAI API`/`Anthropic API` 21%, `CI/CD` 23%, agents 20%, `Prompt Engineering` 22%.

## AI-type mix (% of all postings)

| Type | Feb 4 | Mar 27 | Jun 25 |
|---|---|---|---|
| ai-first | 69.4 | 79.0 | 75.9 |
| ai-support | 28.5 | 18.5 | 21.8 |
| ml-first | 1.8 | 2.1 | 1.2 |

ai-first rose from 69.4% to 75.9% (and 79.0% in March); the role is consolidating around the dedicated AI engineer.

## Integrator vs trainer (within ai-first)

First and last values:

- Trainer stack (`PyTorch`/`TensorFlow`/`Fine-Tune`/`CUDA`): 36.1% to 27.2%
- Integrator stack (`RAG`/agents/APIs): 73.6% to 77.9% (peak 81.6% in May)
- Pure integrator: 49.6% to 56.7% (peak 60.0%)
- Pure trainer: 12.1% to 5.9%
- Neither: 14.3% to 16.2%

## Agent-framework churn (share among jobs using any framework)

First and last values:

- `LangChain`: 88.0% to 83.8% - still dominant, but sliding
- `LangGraph`: 37.7% to 48.5% - the fast riser
- `LlamaIndex`: 27.7% to 35.3%
- `CrewAI`: 15.2% to 24.1%
- `AutoGen`: 9.9% to 19.5%
- `Semantic Kernel`: 6.3% to 11.6%
- `DSPy`: 5.2% to 3.3%

`LangChain`'s near-monopoly is fragmenting into a `LangChain`-led, multi-framework world, with `LangGraph`, `CrewAI`, and `AutoGen` all gaining share.

## ai-first sub-archetypes (within ai-first)

First and last values:

- RAG builder: 50.1% to 52.4% (peak 62.5% in May)
- Agent builder: 44.4% to 42.4% (peak 47.2%)
- Fine-tuner: 25.0% to 18.0%
- Inference / serving: 11.4% to 6.4%
- RAG and agents: 28.7% to 25.8% (peak 35.7% in May)
- Agents but not RAG: 15.8% to 16.6%

## Use-case themes (% of postings, first to last)

- Automation / workflow: 59.7% to 70.8% - dominant and rising
- Agents / autonomous: 44.7% to 52.6% (peak 53.0% in Apr)
- RAG / Q&A: 13.7% to 29.5% - more than doubled
- Search / retrieval: 23.4% to 34.1% (peak 34.1%)
- Copilot / dev tools: 28.8% to 21.2% (volatile)
- Document / extraction: 15.0% to 16.6%
- Analytics / BI: 22.6% to 20.9%
- Recommend / personalize: 16.3% to 7.7% - fading
- Chatbot / assistant: 12.7% to 11.9%
- Customer support: 5.5% to 3.8%

## Responsibility verbs (% of postings, first to last)

- build / develop: 97.1% to 98.5% - near-universal
- design / architect: 81.5% to 87.8%
- ship / deploy / integrate: 76.5% to 79.3% - rising
- collaborate / partner: 73.0% to 72.7%
- evaluate / test: 66.3% to 71.2%
- train / research / optimize: 62.3% to 51.5% - falling
- scale / performance: 58.4% to 53.0%

The verb mix is shifting from research/optimize toward ship/integrate - the same direction as the integrator-vs-trainer split.

## Eval and LLMOps maturity (% of postings, first to last)

- LLM-native eval (any of `LangSmith`, `Langfuse`, `Guardrails`, `LLM Evaluation`): 9.1% to 12.4%
- Classic MLOps (`MLflow`, `Kubeflow`): 18.5% to 16.8%
- Infrastructure monitoring (`Datadog`, `Prometheus`, `Grafana`): 6.6% to 6.9% - flat
- `Guardrails`: 4.9% to 3.9%
- `LangSmith`: 2.1% to 2.7%
- `Langfuse`: 1.8% to 2.5%
- `LLM Evaluation` (explicit): 1.5% to 4.8%
- Weights & Biases: 0.9% to 1.8%

Eval tooling is migrating from ML-style tracking to LLM-native evaluation, but absolute maturity is low - most postings name no eval tooling at all.

## GenAI skill trajectories (first to last, with slope)

Rising (slope, pp per scrape):

- `SQL`: 9.8% to 34.8%, slope +3.59
- `Prompt Engineering`: 32.7% to 47.6%, +2.90
- `CI/CD`: 29.8% to 37.7%, +1.49
- `Claude Code` (as a listed skill): 1.7% to 8.2%, +1.25
- `Docker`: 31.3% to 35.4%, +1.06
- `MCP`: 8.0% to 13.0%, +1.03
- `LangGraph`: 8.0% to 13.2%, +1.00
- `RAG`: 39.1% to 41.9%, +0.82

Declining:

- `AI Agents` (tag): 23.9% to 14.2%, slope -1.20
- `PyTorch`: 22.0% to 16.4%, -0.92
- `Fine-Tuning`: 8.2% to 5.6%, -0.63
- `TensorFlow`: 12.7% to 12.5%, -0.37
- `Function Calling`: 6.8% to 4.1%, -0.19
- `RLHF`: 1.8% to 0.9%, -0.11
- `Guardrails`: 4.9% to 3.9%, -0.06

`SQL`'s rise is the standout: the field is shifting from model work toward data-and-application work.

## AI coding tools

AI coding tools (`Claude Code`, `GitHub Copilot`, `Cursor`, `Codex`) became a listed skill: 4.2% of postings in February to 14.1% in June - roughly one in seven. The rise is fastest in ai-first roles (2.6% to 9.9%) and broadest reach in ai-support (4.1%). The trajectory and momentum charts track `Claude Code` specifically, which rose from 1.7% to 8.2%.

## AI infra emergence (within ai-first, %)

The dedicated AI-infra role did not emerge at scale:

- Any inference/serving (`vLLM`, `Triton`, `TensorRT`, `CUDA`, `Model Deployment`): 11.4% to 6.4%
- `Model Deployment`: 7.7% to 4.3%
- `CUDA`: 1.9% to 0.7%
- `vLLM`: 2.3% to 1.5%
- `Triton`: 1.0% to 0.9%
- `TensorRT`: 1.3% to 0.3%
- `Kubernetes` (general): 26.4% to 28.0% - flat, absorbed into platform work

This is a null finding: inference work is currently part of the platform/infra archetype, not a standalone mass role.

## Skill co-occurrence lift

Lift = P(B given A) / P(B) across all 4,894 postings. Lift above 1 means B is over-represented in A-jobs. Top pairs by lift:

- `LangChain` pulls `LangGraph` at 42% (lift 3.1) - the strongest pair in the dataset
- `RAG` pulls `Function Calling` (lift 2.1), `Embeddings` (2.0), vector databases (1.9), `LangGraph` (1.8)
- `PyTorch` pulls `MLOps` (2.0), `Kubernetes` (1.3), `AWS` (1.3)
- `MCP` pulls `Function Calling` (2.5), `LangGraph` (2.5)
- `Fine-Tuning` pulls `Embeddings` (1.9), `MLOps` (1.7)
- `Docker` pulls `Kubernetes` (2.5), `AWS` (1.5)

Two cleanly separated stacks: a RAG/application stack and a PyTorch/training-infra stack.

## Company stage over-index (skills)

Over/under-index versus the whole-market baseline, by funding stage. Sample sizes: early (Seed-Series A) 485, growth (Series B-F) 907, public/late 2,420.

- Early-stage (Seed-Series A): over-index on ai-first (x1.10) and agents (x1.22); under-index on `PyTorch`/`TensorFlow` (x0.55), `AWS` (x0.60), `Docker`/`Kubernetes` (x0.59)
- Growth (Series B-F): over-index on agents (x1.22); under-index on `PyTorch`/`TensorFlow` (x0.62), fine-tuning (x0.80)
- Public / late-stage: over-index on `PyTorch`/`TensorFlow` (x1.22); `AWS` (x1.09) and `Docker`/`Kubernetes` (x1.07) mildly over

Startups build with agents; large enterprises still maintain a training/platform core.

## Title predicts the stack

Title-group sizes and signatures:

| Title group | n | % ai-first | Signature |
|---|---|---|---|
| `ai engineer` | 1,472 | 92 | 61% RAG, 43% agents, 28% PyTorch/TF |
| `software` / `backend engineer` | 1,190 | 65 | 34% RAG, 34% agents, 34% Kubernetes |
| `ml engineer` / `scientist` | 409 | 87 | 52% PyTorch/TF, 44% RAG |
| `applied` / `forward deployed` | 387 | 93 | 51% customer-facing, 55% RAG, 49% agents |
| `platform` / `infra` / `devops` | 497 | 43 | 51% Kubernetes |
| `data engineer` | 136 | 34 | 38% RAG, 94% Python |

The `applied` / `forward deployed` group is the only one that is majority customer-facing.

## Forward Deployed Engineer (FDE)

I found 115 FDE postings (2.3% of the market). Monthly share: 2.0% in February, rising to 3.3% in June.

| Metric | FDE | Other ai-first |
|---|---|---|
| ai-first | 97% | 100% |
| customer-facing | 92% | 21% |
| RAG | 50% | 54% |
| agents | 50% | 42% |
| PyTorch/TF | 15% | 25% |
| fine-tuning | 7% | 10% |
| Python | 90% | 90% |
| AWS | 39% | 41% |

The FDE is a customer-facing, ship-fast generalist: RAG-and-agents fluent but light on research, heavy on delivery. Use cases cluster around enterprise automation, workflows, retrieval, and production systems.

## Skill breadth is growing

Average skills per posting:

- Total skills: 14.9 (Feb) to 19.5 (Jun)
- GenAI skills: 3.7 to 5.1

The posting is getting fatter - accumulating requirements faster than it specializes.

## Seniority (% of postings, first to last)

- Staff and above: 18.5% to 13.1%
- Senior: 30.8% to 33.9%
- Mid: 43.9% to 46.2%
- Lead: 4.6% to 4.8%
- Management / Director: 0.7% to 1.0%
- Junior / entry-level: 1.5% to 1.0% - effectively absent

The bottom rung of the posted market is essentially closed.

## Reproduction

The analysis scripts live in [job-market/_internal/analysis/](_internal/analysis/). Run them with uv from the `job-market/` directory:

- `uv run python _internal/analysis/canonicalize_skills.py --check` - verify skill normalization is byte-faithful
- `uv run python _internal/analysis/trends.py` - monthly volume, ai-type mix, seniority, and per-skill share tables
- `uv run python _internal/analysis/deep_trends.py` - integrator/trainer index, framework churn, co-occurrence lift, use-case themes
- `uv run python _internal/analysis/deep_trends2.py` - clustering, company-stage over-index, infra emergence, responsibility verbs, eval maturity, skill trajectories, title-to-stack, FDE
- `uv run python _internal/analysis/charts.py` - renders the five charts in [images/](images/)

The clustering is deterministic (seed=7) and implemented in numpy so no sklearn dependency is needed.
