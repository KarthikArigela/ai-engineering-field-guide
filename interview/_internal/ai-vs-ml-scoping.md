# AI Engineering vs ML Engineering Scoping

Internal reference for deciding whether a take-home assignment, interview
question, or job posting belongs in this guide (AI Engineering) or is
out of scope (traditional ML Engineering).

## The Core Distinction

**AI Engineering** (in scope) — building applications *on top of* pre-trained
models, primarily LLMs. The candidate works with models through APIs, prompt
design, orchestration, and system architecture. They are not expected to train
models from scratch or do original ML research.

**ML Engineering** (out of scope) — building and training models from scratch,
fine-tuning on custom datasets, deploying training pipelines, doing original ML
research. The candidate is expected to understand gradient descent, loss
functions, regularization, and model architecture at a mathematical level.

## What's In Scope (AI Engineering)

Assignment must involve at least one of these as the primary focus:

- **LLM integration** — calling OpenAI, Anthropic, or open-source LLM APIs
- **RAG** — retrieval-augmented generation, vector databases, document QA
- **Agents** — tool-calling, multi-step reasoning, multi-agent orchestration
- **Prompt engineering** — system prompts, structured output, chain-of-thought
- **LLM evaluation** — LLM-as-judge, evaluation harnesses, metrics
- **Conversational AI** — chatbots, voice assistants, live chat agents
- **Document processing with LLMs** — extraction, summarization, classification
  using LLMs (not traditional NLP pipelines)
- **GenAI applications** — text generation, code generation, image generation
  built on foundation models
- **LLM infrastructure** — routing, caching, observability, cost optimization
  for LLM workloads

## What's Out of Scope (ML Engineering)

Exclude if the assignment is primarily about:

- **Training models from scratch** — building neural network architectures,
  implementing backpropagation, defining loss functions
- **Traditional NLP without LLMs** — TF-IDF, word2vec, BERT fine-tuning
  as the core task (not as a comparison baseline)
- **Classical ML** — logistic regression, random forests, XGBoost, SVMs
  as the primary deliverable
- **Computer vision without LLMs** — CNN training, object detection
  (YOLO, Mask R-CNN), image classification from scratch
- **Recommender systems** — collaborative filtering, matrix factorization
  without an LLM component
- **Model training pipelines** — MLOps for training, hyperparameter tuning,
  distributed training infrastructure
- **Data science** — EDA, statistical analysis, A/B testing, dashboards
  without an AI/LLM component

## Edge Cases

These come up often and need judgment:

| Scenario | Verdict | Reasoning |
|----------|---------|-----------|
| Fine-tuning an LLM on a custom dataset | In scope | LLM is the central artifact; the assignment is about adapting a foundation model |
| Building a RAG system that compares fine-tuned vs. base model | In scope | RAG + LLM is primary; fine-tuning is secondary |
| Training a CNN for image classification from scratch | Out | No LLM, no GenAI; this is traditional CV/ML |
| Self-pruning neural network on CIFAR-10 | Out | Pure deep learning; training architecture design, no LLM/agent component |
| Anomaly detection using statistical methods | Out | Traditional ML/data science |
| Anomaly detection using LLM-based reasoning over logs | In | LLM is doing the work |
| Data pipeline with vector embeddings + semantic search | In | Core AI engineering pattern (RAG-adjacent) |
| Recommender using embeddings from a foundation model | In | Foundation model embeddings are the AI engineering component |
| SQL-to-natural-language via LLM | In | Classic LLM application |
| Credit scoring with ML ensemble + LLM explanation | In | The LLM enrichment layer makes this an AI engineering task |
| Building a chatbot UI with hardcoded rules | Out | No LLM; just a CRUD app with a chat interface |

## Decision Checklist

When evaluating a repo or assignment, ask in order:

1. Does it call an LLM or foundation model API? → Likely in scope
2. Does it use vector embeddings / semantic search / RAG? → Likely in scope
3. Does it involve agent behavior (tool use, planning, multi-step)? → Likely in scope
4. Is the primary task training a model from scratch? → Out of scope
5. Could this be done without any LLM or foundation model? → Probably out of scope
6. Is "AI Engineer" or "GenAI Engineer" in the role title? → Strong signal to include, but still verify the task is AI-engineering work

When in doubt, check whether the candidate's deliverable would exist in a world
without LLMs. If it would (e.g., a recommender, a classifier, a dashboard),
it is probably traditional ML, not AI engineering.
