# AI Engineering Job Market Trends - Appendix

Detailed tables, cluster signatures, methodology, and reproduction notes for [the trends summary](trends.md).

## Data and methodology

Eight scrapes of builtin.com, each an independent cross-section:

- Feb 4: 895 postings
- Feb 27: 869
- Mar 27: 680
- Apr 22: 645
- May 29: 919
- Jun 25: 888
- Jul 22: 846
- Aug 25: 1,222

Total: 6,964 postings. Job IDs do not overlap between scrapes, so I treat each month as a fresh sample of the market. Percentages are the share of postings (within a given denominator) whose structured skill / use-case / title fields match.

Roles are tagged ai-first (the core AI engineer), ai-support (software/ML/data roles with AI scope), ml-first (traditional ML), or unknown. The headline analyses run within ai-first unless noted, since that is where the role is actually being defined.

A note on extraction quality: the Feb-Jul scrapes were originally extracted with a prompt that silently changed model (`glm-5.1` to `glm-5.2`) partway through, which meant month-over-month swings were partly measuring the extractor, not the market. In August I rewrote the prompt and re-extracted the entire Feb-Jul corpus, then validated the new extraction against the old on a 50-job blind eval: preferred 38/50 (2 old, 10 tie), 98.0% classification-clean versus 78.0%, far fewer invented or missed skills - see [_internal/eval/](_internal/eval/) for the full writeup. This appendix and the August scrape both use that validated extraction (`model: glm-5.2`, `prompt_sha: ef6fdeb19af2` in every file's `meta`), so all eight months are now on one consistent measurement, which is why some numbers here read differently - and more stable - than earlier versions of this analysis.

Skills are normalized through [canonicalize_skills.py](_internal/analysis/canonicalize_skills.py), which collapses case, acronym, and synonym variants into one canonical form per concept and round-trips byte-stable across all 6,964 files (146,638 total skill entries). The extraction prompt in [extract_llm.py](_internal/extract_llm.py) enforces a canonical vocabulary scoped to skills appearing more than 30 times.

The "slope" metric in the trajectory sections is the slope of an OLS line fit to the eight monthly shares, in percentage points per scrape.

## Cluster signatures

Spherical k-means (cosine distance, k-means++ init, k=6, seed=7, implemented in numpy) on a 31-skill binary signature per posting. Each cluster's top skills (share of cluster members, with lift over baseline):

- RAG app builder (1,763 postings, 25.3%, 96% ai-first). `LangChain` 65% (x2.8), `LangGraph` 41% (x2.8), vector databases 71% (x2.6), `Fine-Tuning` 36% (x2.1), `RAG` 90% (x2.1), AI cloud services 29% (x2.1), `FastAPI`/`Flask` 22% (x2.1). The dominant archetype.
- Cloud / ML platform engineer (1,257, 18.0%, 58% ai-first). `GCP` 88% (x3.0), `Azure` 88% (x2.8), `AWS` 94% (x2.2), `PyTorch`/`TensorFlow` 33% (x1.7), inference/serving 26% (x1.5), `Kubernetes` 36% (x1.4), `Docker` 35% (x1.3).
- Prompt-driven agent builder (1,040, 14.9%, 92% ai-first). `Prompt Engineering` 97% (x2.6), `Function Calling` 30% (x2.0), `OpenAI`/`Anthropic API` 30% (x1.5), `MCP` 21% (x1.4), agents 77% (x1.3), `RAG` 46% (x1.1).
- Pure agent builder (950, 13.6%, 84% ai-first). Agents 100% (x1.7), `RAG` 31% (x0.7, under-index). Agent frameworks without a retrieval layer - a distinct cluster from the RAG-and-agents builders above.
- DevOps / full-stack engineer (923, 13.3%, only 33% ai-first). `Terraform` 26% (x2.4), `React`/frontend 41% (x2.4), coding tools 23% (x1.9), `Kubernetes` 47% (x1.8), `CI/CD` 72% (x1.8), `Docker` 44% (x1.7). The infra and full-stack archetypes that were separate six months ago now cluster together - the least AI-native group.
- ML trainer / researcher (571, 8.2%, 46% ai-first). `PyTorch`/`TensorFlow` 62% (x3.1), inference/serving 52% (x3.0), `MLOps` 31% (x1.5), `SQL` 22% (x1.4). Still the smallest archetype.

The agent-builder archetype has split into two distinct clusters since the six-scrape version of this analysis: one built around prompt engineering and provider APIs, one built around agent frameworks with little to no retrieval. Meanwhile the old DevOps/infra and full-stack clusters merged into one.

## AI-type mix (% of all postings)

| Type | Feb 4 | Mar 27 | May 29 | Aug 25 |
|---|---|---|---|---|
| ai-first | 71.5 | 71.3 | 69.2 | 70.2 |
| ai-support | 22.2 | 24.0 | 24.5 | 23.2 |
| ml-first | 5.9 | 4.4 | 4.5 | 5.0 |

On the corrected extraction, ai-first has held in a tight 68-71% band the whole eight months - no consolidation trend either direction. That range itself is informative: roughly 7 in 10 "AI Engineer" postings are the dedicated GenAI-integration role, and that ratio has been stable since February.

## Integrator vs trainer (within ai-first)

First and last values:

- Trainer stack (`PyTorch`/`TensorFlow`/`Fine-Tune`/`CUDA`): 37.5% to 30.4%
- Integrator stack (`RAG`/agents/APIs): 80.0% to 88.0% (peak 89.4% in Jul)
- Pure integrator: 50.9% to 62.8%
- Pure trainer: 8.4% to 5.2%
- Neither: 11.6% to 6.8%

## Agent-framework churn (share among jobs using any framework)

First and last values:

- `LangChain`: 86.3% to 84.5% - still dominant, roughly flat
- `LangGraph`: 37.7% to 61.4% - the fast riser, now used by a majority of framework adopters
- `LlamaIndex`: 28.6% to 31.3%
- `CrewAI`: 16.6% to 28.4%
- `AutoGen`: 10.9% to 27.2%
- `Semantic Kernel`: 6.9% to 16.7%
- `DSPy`: 5.7% to 0.9% - the one framework losing share outright

`LangChain`'s dominance isn't eroding so much as everyone is adding a second framework on top - `LangGraph` most often, but `CrewAI` and `AutoGen` both roughly doubled their share of framework-using jobs.

## ai-first sub-archetypes (within ai-first)

First and last values:

- RAG builder: 43.4% to 58.4%
- Agent builder: 63.8% to 77.2%
- Fine-tuner: 24.2% to 24.9% - flat, not declining
- Inference / serving: 19.8% to 9.9% - roughly halved
- RAG and agents (both): 33.1% to 50.5% - now a majority of ai-first jobs
- Agents but not RAG: 30.6% to 26.7%

## Use-case themes (% of postings, first to last)

- Automation / workflow: 52.2% to 59.6% - dominant and rising
- Agents / autonomous: 43.0% to 48.9%
- Search / retrieval: 19.8% to 24.6%
- RAG / Q&A: 13.6% to 20.6% - up more than half
- Copilot / dev tools: 23.0% to 20.0%
- Document / extraction: 12.3% to 12.8%
- Analytics / BI: 18.5% to 16.4%
- Recommend / personalize: 12.8% to 7.0% - fading
- Chatbot / assistant: 12.6% to 11.2%
- Customer support: 4.4% to 1.9%

## Responsibility verbs (% of postings, first to last)

- build / develop: 97.3% to 98.0% - near-universal
- design / architect: 84.9% to 84.8% - flat
- ship / deploy / integrate: 78.2% to 75.3%
- collaborate / partner: 77.9% to 58.1% - the sharpest mover
- evaluate / test: 68.9% to 67.2%
- train / research / optimize: 64.5% to 45.9% - falling steadily
- scale / performance: 62.9% to 44.9%

Train/research/optimize is the clearest directional mover - it fell in six of the last seven scrapes. The drop in "collaborate/partner" language is worth reading cautiously; it may reflect wording drift in how postings are written as much as a change in the work itself.

## Eval and LLMOps maturity (% of postings, first to last)

- LLM-native eval (any of `LangSmith`, `Langfuse`, `Guardrails`, `LLM Evaluation`): 26.7% to 30.1%
- Classic MLOps (`MLflow`, `Kubeflow`): 19.9% to 16.9%
- `Guardrails`: 10.2% to 15.2%
- `LangSmith`: 1.9% to 2.5%
- `Langfuse`: 1.9% to 2.1%
- `LLM Evaluation` (explicit): 20.3% to 21.4%
- Weights & Biases: 0.9% to 1.1%
- Infrastructure monitoring (general): 6.4% to 6.8% - flat

Eval tooling is migrating from ML-style tracking toward LLM-native evaluation and guardrails, but most postings still name no dedicated eval tool at all - "LLM Evaluation" as a bare requirement is far more common than any named product.

## GenAI skill trajectories (first to last, with slope)

Rising (slope, pp per scrape):

- `Prompt Engineering`: 26.1% to 39.0%, +1.46
- Coding tools (`Claude Code`/`Copilot`/`Cursor`): 3.5% to 8.9%, +1.06
- `RAG`: 32.8% to 43.2%, +1.02
- `LangGraph`: 7.4% to 17.2%, +0.90
- `Function Calling`: 9.6% to 14.3%, +0.87
- `MCP`: 9.9% to 17.6%, +0.86
- `Guardrails`: 10.2% to 15.2%, +0.76
- `CI/CD`: 27.9% to 39.4%, +0.73

Declining:

- `PyTorch`: 20.8% to 15.3%, -0.95
- `Fine-Tuning`: 17.1% to 12.7%, -0.76
- `TensorFlow`: 12.2% to 11.5%, -0.50
- `RLHF`: 0.3% to 0.1%, -0.03

Roughly flat:

- `Kubernetes`: 22.5% to 25.3%, +0.03
- `Docker`: 20.9% to 26.9%, +0.06
- `AWS Bedrock`: 3.4% to 7.0%, +0.12
- `Embeddings`: 14.2% to 18.2%, +0.17

`Prompt Engineering` is now the fastest-rising named skill on the corrected data, with `RAG` and the agent-framework cluster (`LangGraph`, `MCP`, `Function Calling`) close behind. Unlike the earlier version of this analysis, `SQL` is no longer a standout riser once the extraction is consistent across months (11.1% to 15.8%, a modest gain) - its earlier "fastest-rising skill" reading was partly a prompt-change artifact.

## AI coding tools

AI coding tools (`Claude Code`, `GitHub Copilot`, `Cursor`, `Codex`) as a listed skill: 7.6% of postings in February to 12.8% in August - about one in eight. The rise is present in both segments: ai-first roles went from 5.5% to 8.2%, ai-support from 2.1% to 4.3%. The trajectory isn't monotonic - it peaked at 16.2% in June before easing back - so treat the August reading as noisy rather than a reversal.

## AI infra emergence (within ai-first, %)

The dedicated AI-infra role still hasn't emerged at scale, and on the corrected data the inference/serving footprint looks smaller than before:

- Any inference/serving (`vLLM`, `Triton`, `TensorRT`, `CUDA`, `Model Deployment`): 19.8% to 9.9% - roughly halved
- `Model Deployment`: 18.3% to 6.9%
- `CUDA`: 0.3% to 1.5%
- `vLLM`: 1.1% to 2.6%
- `Triton`: 0.5% to 1.3%
- `TensorRT`: 0.5% to 1.0%
- `Kubernetes` (general, infra proxy): 18.6% to 24.0% - rising, absorbed into platform work

This remains a null finding on the AI-infra-as-a-standalone-role question, and more strongly than before: inference/serving work is concentrating into the platform/infra archetype rather than growing its own dedicated posting category.

## Skill co-occurrence lift

Lift = P(B given A) / P(B) across all 6,964 postings. Lift above 1 means B is over-represented in A-jobs. Top pairs by lift:

- `LangChain` pulls `LangGraph` at 46% (lift 3.3) - still the strongest pair in the dataset
- `Docker` pulls `Kubernetes` at 72% (lift 3.0)
- `RAG` pulls `Embeddings` (lift 2.2), vector databases (2.0), `Function Calling` (1.9), `LangGraph` (1.8)
- `MCP` pulls `Function Calling` (2.5), `LangGraph` (2.3)
- `OpenAI API` pulls `Embeddings` (2.2), `FastAPI` (2.1), `LangGraph` (2.1)
- `Fine-Tuning` pulls `Embeddings` (2.1), `MLOps` (2.0), `LangGraph` (2.0)
- `PyTorch` pulls `MLOps` (2.2), vector databases (1.4), `Kubernetes` (1.4)

Two cleanly separated stacks persist: a RAG/application stack (RAG, embeddings, vector databases, LangGraph, function calling) and a PyTorch/training-infra stack (PyTorch, MLOps, Kubernetes, AWS) - `MCP` and `Fine-Tuning` both sit closer to the application stack than the training one, which is a shift from six months ago.

## Company stage over-index (skills)

Over/under-index versus the whole-market baseline, by funding stage. Sample sizes: early (Seed-Series A) 335, growth (Series B-F) 202, public/late 291. Baseline: ai-first 70.0%, `RAG` 39.8%, agents 55.4%, `Fine-Tuning` 15.7%, coding tools 11.6%, `PyTorch`/`TensorFlow` 18.6%, `AWS` 40.3%, `Docker`/`Kubernetes` 30.8%.

- Early-stage (Seed-Series A): over-index on ai-first (x1.16) and `Fine-Tuning` (x1.23); sharply under-index on `PyTorch`/`TensorFlow` (x0.56), `AWS` (x0.59), `Docker`/`Kubernetes` (x0.54)
- Growth (Series B-F): over-index on coding tools (x1.36) and `AWS` (x1.15); under-index on `RAG` (x0.66), `Fine-Tuning` (x0.44), `PyTorch`/`TensorFlow` (x0.48)
- Public / late-stage: over-index on `RAG` (x1.22) and `Fine-Tuning` (x1.18); roughly at baseline everywhere else

The pattern shifted since the six-scrape version: early-stage companies now lead on `Fine-Tuning` rather than avoiding it, and it's growth-stage companies (not early-stage) that lean hardest into agents and coding tools while avoiding the training stack. Public/late-stage companies are the only group over-indexing on RAG.

## Title predicts the stack

Title-group sizes and signatures:

| Title group | n | % ai-first | % customer-facing | Signature |
|---|---|---|---|---|
| `ai engineer` | 2,131 | 88 | 16 | 56% RAG, 68% agents, 25% PyTorch/TF |
| `software` / `backend engineer` | 1,637 | 62 | 11 | 32% RAG, 55% agents, 28% Kubernetes |
| `ml engineer` / `scientist` | 578 | 74 | 10 | 45% RAG, 46% agents, 49% PyTorch/TF |
| `applied` / `forward deployed` | 587 | 91 | 47 | 50% RAG, 74% agents, 13% PyTorch/TF |
| `platform` / `infra` / `devops` | 711 | 47 | 11 | 27% RAG, 46% agents, 42% Kubernetes |
| `data engineer` | 189 | 44 | 8 | 41% RAG, 39% agents, 88% Python |

The `applied` / `forward deployed` group is still the only one that is majority customer-facing, and by a wide margin - 47% versus 8-16% everywhere else.

## Forward Deployed Engineer (FDE)

I found 187 FDE postings (2.7% of the market). Monthly share: 2.0% in February, peaking at 4.4% in July before easing to 2.9% in August.

| Metric | FDE | Other ai-first |
|---|---|---|
| ai-first | 94% | 100% |
| ai-support | 5% | 0% |
| customer-facing | 89% | 14% |
| RAG | 47% | 54% |
| agents | 72% | 72% |
| PyTorch/TF | 10% | 20% |
| fine-tuning | 18% | 22% |
| Python | 68% | 76% |
| AWS | 36% | 41% |

The FDE remains a customer-facing, ship-fast generalist: RAG-and-agents fluent but lighter on research than other ai-first roles. Use cases cluster around enterprise automation, workflows, and production agent systems.

## Skill breadth is roughly flat

Average skills per posting (including umbrella terms like "LLMs" and "Machine Learning"):

- Total skills: 18.4 (Feb) to 19.7 (Aug), peaking at 22.8 in Feb 27
- GenAI skills: 4.6 to 5.5

On the corrected extraction, postings aren't accumulating requirements the way the six-scrape version suggested - breadth has bounced in a 18-23 skill range all year rather than trending up.

## Seniority (% of postings, first to last)

- Staff and above: 18.5% to 11.0% - the clearest decline
- Senior: 30.8% to 30.3% - flat
- Mid: 43.9% to 48.4%
- Lead: 4.6% to 8.1%
- Management / Director: 0.7% to 1.0%
- Junior / entry-level: 1.5% to 1.2% - effectively absent throughout

The bottom rung of the posted market has been essentially closed since February. The one clear move is at the top: Staff+ postings have nearly halved as a share of the market, while Lead roles picked up some of that share.

## Reproduction

The analysis scripts live in [job-market/_internal/analysis/](_internal/analysis/). Run them with uv from the `job-market/` directory:

- `uv run python _internal/analysis/canonicalize_skills.py --check` - verify skill normalization is byte-faithful
- `uv run python _internal/analysis/trends.py` - monthly volume, ai-type mix, seniority, and per-skill share tables
- `uv run python _internal/analysis/deep_trends.py` - integrator/trainer index, framework churn, co-occurrence lift, use-case themes
- `uv run python _internal/analysis/deep_trends2.py` - clustering, company-stage over-index, infra emergence, responsibility verbs, eval maturity, skill trajectories, title-to-stack, FDE
- `uv run python _internal/analysis/charts.py` - renders the five charts in [images/](images/)

The clustering is deterministic (seed=7) and implemented in numpy so no sklearn dependency is needed.
