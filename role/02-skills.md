# AI Engineering Jobs Analysis

Generated from 5,740 job descriptions extracted from builtin.com.

I searched for jobs containing "AI Engineer" keyword from LA (Global), New York, London, Amsterdam, Berlin and India. This is the combined result of seven monthly scrapes between February 4 and July 22, 2026, so it covers jobs published from January through July 2026.

There is no overlap in job IDs between scrapes, so each month is an independent cross-section of the market rather than the same postings re-counted.

All numbers here come from quantitative analysis in the [analysis notebook](../job-market/analysis.ipynb) and the scripts in [_internal/analysis/](../job-market/_internal/analysis/). For how these numbers moved month over month, see [trends](../job-market/trends.md).

Summary

- 72.9% of roles work directly on AI (RAG, agents)
- 93.7% need skills beyond just GenAI - it's a full-stack role
- 42.9% of roles mention RAG - the most common pattern in all jobs
- 57.8% of AI-First roles require some ML knowledge
- AWS (2,399 jobs) > Azure (1,646 jobs) > GCP (1,596 jobs)


## A Note on Measurement

Skills are extracted by an LLM from the job description text. Two things changed over the seven scrapes:

- Skill names were canonicalized after the fact, so variants like "rag", "RAG pipelines" and "retrieval-augmented generation" now collapse into one skill. This raises the counts for common skills compared to the February version of this analysis.
- The extraction model changed from `glm-5.1` to `glm-5.2` before the July scrape. The newer model extracts more skills per job (23.9 vs 16-21), and it is much more aggressive about tagging agent skills specifically.

Most skill shares are stable from scrape to scrape. Agent skills are the exception and the one place to be careful: excluding the July scrape, agents appear in 30.8% of all jobs instead of 35.5%. Treat all skill percentages as a floor, not a ceiling - a skill the description doesn't spell out doesn't get counted.


## "AI Engineering" Job Types

Job positions we analyzed fall into these categories:

- AI-first
- AI-support
- ML

54 jobs (0.9%) could not be classified.

### AI-First: 4,186 jobs (72.9%)

Working ON AI/ML systems directly.

What they build:

- RAG (Retrieval-Augmented Generation) systems
- AI agents and agentic workflows
- Fine-tuned LLMs for specific domains
- Model serving and inference pipelines
- Prompt engineering and optimization

Example responsibilities:

- "Build RAG system for knowledge retrieval"
- "Implement agent workflows for automation"
- "Fine-tune Llama 3 for domain-specific tasks"
- "Deploy AI models to production"
- "Optimize prompts and model performance"

Position title examples

- AI Engineer
- Senior AI Engineer
- Applied AI Engineer
- Lead AI Engineer
- Staff AI Engineer
- Principal AI Engineer
- AI/ML Engineer


### AI-Support: 1,384 jobs (24.1%)

Working NEAR AI but NOT ON AI itself.

These roles enable AI work by building the platforms, infrastructure, and tools that AI-First engineers use.

What they build:

- AI platforms and internal tooling
- GPU clusters and inference infrastructure
- Data pipelines for training/fine-tuning
- Frontend for AI products
- Deployment and monitoring systems

Example responsibilities:

- "Build platform for RAG systems"
- "Pipeline data for fine-tuning"
- "Build deployment infrastructure"
- "Build prompt management UI"
- "Create internal tooling for AI experimentation"

Position title examples

- AI Sales Engineer
- AI Data Engineer
- AI Infrastructure Engineer
- AI Platform Engineer
- Backend Engineer - AI Systems
- Full-Stack Engineer (AI/LLM Platform)


### Machine Learning: 116 jobs (2.0%)

Traditional ML/DL work without LLMs/agents.

What they build:

- Classical ML models (scikit-learn, XGBoost)
- Deep learning models (PyTorch, TensorFlow)
- Computer vision systems
- Recommendation systems
- Model training pipelines

Position title examples

- Computer Vision AI Engineer
- AI Research Engineer - AI Safety
- AI Research Engineer - Reinforcement Learning
- AI Research Engineer - Robotics, Control, RL
- Sr. AI/Machine Learning Engineer - Supply Chain

These "AI Engineer" roles are traditional ML roles rebranded with the AI title. They do classical ML work (PyTorch, TensorFlow, computer vision) without any GenAI components. The share stayed small in every scrape, between 1.2% and 3.0%.


### How to Tell the Difference

The key question is: Does this role work ON AI systems, or NEAR them?

AI-First:

- Builds RAG systems
- Fine-tunes models
- Implements agent workflows
- Optimizes prompts
- Deploys AI features

AI-Support:

- Builds platforms for others
- Manages GPU infrastructure
- Builds data pipelines
- Creates deployment tooling
- Builds UIs for AI products

ML:

- Trains traditional ML models
- Works with structured data
- Builds computer vision systems
- Does NOT work with LLMs/agents


## Dataset Statistics

Unique companies: 2,172

Top 20 companies by job count:

- Capital One - 102 jobs
- Citi - 84 jobs
- Optum - 72 jobs
- NVIDIA - 53 jobs
- Thomson Reuters - 46 jobs
- BJAK - 44 jobs
- Hewlett Packard Enterprise - 41 jobs
- Jack & Jill AI - 39 jobs
- Wells Fargo - 37 jobs
- NextHire Consulting - 37 jobs
- G2i - 34 jobs
- BlackRock - 28 jobs
- Wolters Kluwer - 28 jobs
- OpenAI - 27 jobs
- Ecolab - 26 jobs
- NICE - 25 jobs
- PwC - 21 jobs
- Celonis - 21 jobs
- Databricks - 21 jobs
- Autodesk - 21 jobs

The long tail is where the jobs are: 2,172 companies for 5,740 postings, and the largest single hirer accounts for 1.8% of the market.

Company stage distribution. The stage field is free text written by the extractor, so I grouped it into buckets. 4,589 jobs (79.9%) state a stage at all, and percentages below are shares of those:

| Stage | Jobs | % |
|-------|-----:|--:|
| Public | 2,649 | 57.7% |
| Growth / Series B-C | 824 | 18.0% |
| Early stage / Seed-Series A | 519 | 11.3% |
| Late stage / pre-IPO | 324 | 7.1% |
| Private / established | 172 | 3.7% |

AI engineering hiring is dominated by large public companies, not startups. Capital One, Citi, Optum and Wells Fargo hire more AI engineers than any AI lab in this dataset.

Roles:

- Customer-facing roles: 1,283 (22.4%)
- Management roles: 990 (17.2%)

Most common job titles (exact match):

- AI Engineer - 270 jobs
- Senior AI Engineer - 187 jobs
- Applied AI Engineer - 67 jobs
- AI/ML Engineer - 62 jobs
- Lead AI Engineer - 52 jobs
- Staff AI Engineer - 49 jobs
- Senior AI/ML Engineer - 46 jobs
- Principal AI Engineer - 45 jobs
- Senior Applied AI Engineer - 24 jobs
- Forward Deployed AI Engineer - 24 jobs


## Skills Analysis

Percentages are the share of all 5,740 jobs.

Top GenAI skills:

- RAG - 2,463 jobs (42.9%)
- prompt engineering - 2,353 jobs (41.0%)
- LLMs - 2,088 jobs (36.4%)
- LangChain - 1,363 jobs (23.7%)
- AI agents - 1,347 jobs (23.5%)
- agentic workflows - 1,111 jobs (19.4%)
- OpenAI API - 886 jobs (15.4%)
- LangGraph - 796 jobs (13.9%)
- Anthropic API - 732 jobs (12.8%)
- MCP - 628 jobs (10.9%)
- LlamaIndex - 489 jobs (8.5%)

Counting any agent skill (AI agents, agentic workflows, agentic AI) once per job: 2,036 jobs (35.5%).

MCP is the clearest genuine riser in the dataset. It grew from 8.0% of jobs in the February scrape to 13.2% in July, and unlike agent skills it grew steadily every month rather than jumping when the extraction model changed.

Top ML skills:

- PyTorch - 1,196 jobs
- TensorFlow - 843 jobs
- scikit-learn - 490 jobs
- machine learning - 478 jobs
- fine-tuning - 451 jobs
- Hugging Face - 437 jobs
- deep learning - 347 jobs
- model evaluation - 273 jobs
- model training - 238 jobs

Top web skills:

- REST APIs - 1,511 jobs
- React - 874 jobs
- APIs - 742 jobs
- FastAPI - 706 jobs
- microservices - 684 jobs
- Node.js - 227 jobs
- Flask - 227 jobs

Top database skills:

- vector databases - 1,311 jobs
- PostgreSQL - 850 jobs
- Pinecone - 432 jobs
- Snowflake - 341 jobs
- Weaviate - 310 jobs
- Redis - 299 jobs
- pgvector - 207 jobs

Top cloud skills:

- AWS - 2,399 jobs (41.8%)
- Azure - 1,646 jobs (28.7%)
- GCP - 1,596 jobs (27.8%)
- AWS Bedrock - 358 jobs (6.2%)
- SageMaker - 315 jobs (5.5%)
- Vertex AI - 285 jobs (5.0%)

Top ops skills:

- CI/CD - 2,181 jobs
- Docker - 2,150 jobs
- Kubernetes - 1,741 jobs
- MLOps - 777 jobs
- Terraform - 612 jobs
- observability - 541 jobs
- MLflow - 439 jobs

Top languages:

- Python - 4,856 jobs (84.6%)
- SQL - 1,315 jobs (22.9%)
- TypeScript - 1,226 jobs (21.4%)
- Java - 1,017 jobs (17.7%)
- Go - 679 jobs (11.8%)
- JavaScript - 650 jobs (11.3%)


## GenAI Framework Ecosystem

Framework popularity:

- LangChain - 1,363 jobs (23.7%)
- LangGraph - 796 jobs (13.9%)
- LlamaIndex - 489 jobs (8.5%)
- CrewAI - 369 jobs (6.4%)
- AutoGen - 277 jobs (4.8%)
- Semantic Kernel - 166 jobs (2.9%)
- DSPy - 53 jobs (0.9%)

Frameworks travel together rather than compete. 587 jobs ask for LangChain and LangGraph, 468 for LangChain and LlamaIndex. Companies list the ecosystem, not a single tool.


## Supporting Roles: What AI-Support Engineers Do

1,384 jobs (24.1%) classified as AI-Support

| Category | Jobs | Description |
|----------|------:|-------------|
| Platform/Infrastructure | 904 | Build AI platforms, GPU clusters, MLOps tooling |
| Sales/Solutions | 134 | Pre-sales, customer demos, AI solutions consulting |
| Frontend/UI | 130 | Build UIs for AI products, chatbots, AI dashboards |
| Backend/General SWE | 102 | APIs, microservices, internal tools for AI teams |
| Data/Pipelines | 65 | Data pipelines, ETL, dataset preparation for ML |

Do AI-Support roles need AI knowledge?

- 60.8% of AI-Support roles require SOME GenAI knowledge
- 39.2% require NO GenAI skills at all

GenAI skills in AI-Support roles:

- LLMs (general) - 14.8%
- prompt engineering - 12.4%
- RAG - 11.4%
- GitHub Copilot - 9.2%
- AI agents - 7.7%
- Anthropic API - 7.4%

GitHub Copilot, Cursor and Claude Code together appear in 14.2% of AI-Support roles - higher than in AI-First roles (8.6%). For support engineers, "AI skills" increasingly means using AI coding tools, not building AI systems.


### Skill Comparison (AI-First vs AI-Support)

| Skill | AI-First | AI-Support |
|:-------|---------:|------------:|
| RAG | 55.0% | 11.4% |
| Prompt engineering | 52.1% | 12.4% |
| Agents | 44.5% | 12.4% |
| LangChain | 30.5% | 6.1% |
| Fine-tuning | 20.0% | 1.7% |
| Python | 90.7% | 67.7% |
| Docker | 38.2% | 37.7% |
| Kubernetes | 29.6% | 36.0% |
| CI/CD | 36.7% | 44.3% |
| Terraform | 9.0% | 17.5% |
| AWS | 42.9% | 41.1% |
| React | 15.2% | 18.5% |

The GenAI skills separate the two groups cleanly. The infrastructure skills don't - and where they differ, AI-Support asks for more of them.


## Research vs Applied Roles

| Role Type | Jobs | Percentage |
|----------|-----:|------------:|
| Research | 161 | 2.8% |
| Applied/Production | 5,579 | 97.2% |

Research roles work on:

- Novel algorithms and techniques
- Model architecture design
- Training methods and optimization
- Safety and alignment research
- Publishing papers, pushing SOTA
- Experimental work with uncertain outcomes

Keywords: research, scientist, publication, novel, algorithm, architecture, state of the art, experimental

Sample research titles:

- AI Research Engineer
- Applied Scientist / Research Engineer
- AI Research Engineer - Reinforcement Learning
- AI Research Engineer (Model Compression & Quantization)
- Principal AI Research Engineer - World Models
- Principal AI/ML Scientist & Engineer

Applied / Production roles work on:

- Implementing existing models in production
- Building applications with AI APIs
- Deploying and monitoring AI systems
- Customer-facing AI solutions
- Infrastructure and platforms for AI
- Fine-tuning models for specific use cases

Keywords: production, deploy, customer, enterprise, product, API integration, shipping, implementation

The February scrape had the highest research share at 4.4%. Every scrape since has been between 1.6% and 3.3%. The market wants people who ship, not people who publish.


### Example Comparison

| Research | Applied |
|----------|---------|
| "Run pre-training, post-training and deploy state of the art models on clusters with thousands of GPU" (Mistral Research) | "Deploy production AI solutions with measurable business impact across various industries" (Mistral FDE) |
| "Develop novel reinforcement learning algorithms" | "Implement RAG patterns with vector store integration" |
| "Publish papers at top conferences" | "Ship AI features to customers" |


## What Other Titles Do "AI Engineers" Go Under?

Titles here are grouped across seniority levels, so "AI Engineer" includes Senior, Staff, Lead and Principal variants.

Strongly AI-First titles (75%+ classified as AI-First):

- AI Engineer - 1,081 jobs (94% AI-First)
- AI/ML Engineer - 203 jobs (88% AI-First)
- Applied AI Engineer - 170 jobs (92% AI-First)
- AI Software Engineer - 81 jobs (78% AI-First)
- Machine Learning Engineer - 73 jobs (79% AI-First)
- AI Research Engineer - 55 jobs (85% AI-First)
- AI Developer - 55 jobs (89% AI-First)
- Forward Deployed Engineer - 49 jobs (94% AI-First)
- AI Automation Engineer - 48 jobs (92% AI-First)
- AI Solutions Engineer - 47 jobs (83% AI-First)
- AI Product Engineer - 47 jobs (85% AI-First)
- Agentic AI Engineer - 28 jobs (100% AI-First)
- Generative AI Engineer - 24 jobs (100% AI-First)
- Full Stack AI Engineer - 24 jobs (96% AI-First)

Strongly AI-Support titles (75%+ classified as AI-Support):

- Data Engineer - 53 jobs (75% AI-Support)
- AI Infrastructure Engineer - 21 jobs (76% AI-Support)

Titles that predict nothing:

- AI Platform Engineer - 60 jobs (43% AI-First, 57% AI-Support)
- AI Data Engineer - 41 jobs (44% AI-First, 56% AI-Support)
- Software Engineer - 778 jobs (69% AI-First, 30% AI-Support)
- Full Stack Engineer - 59 jobs (56% AI-First, 42% AI-Support)
- Product Engineer - 22 jobs (45% AI-First, 55% AI-Support)

Key insight: "AI Engineer" is still the most common title and still the most reliable one (94% AI-First). But anything with "platform" or "data" in it is a coin flip - always check the responsibilities.

Two title families are worth watching. Agentic AI Engineer did not appear at all in the February scrape and has shown up in every scrape since (28 jobs, 100% AI-First). Forward Deployed Engineer is the fastest-growing title in the dataset - 86 postings here across both spellings, and growing faster than the market. See [Forward Deployed Engineers](06-fde.md) for the full picture on that role.


## How Much ML Do AI Engineers Need to Know?

57.8% of AI-First roles require some ML knowledge

Most common ML skills in AI Engineer roles:

- PyTorch - 1,022 jobs (24.4%)
- Fine-tuning - 963 jobs (23.0%)
- TensorFlow - 711 jobs (17.0%)
- Embeddings - 702 jobs (16.8%)
- Machine learning (general) - 502 jobs (12.0%)
- scikit-learn - 409 jobs (9.8%)
- Model evaluation - 357 jobs (8.5%)

Key findings:

1. Most AI Engineers need some ML knowledge - 57.8% require ML skills, ranging from 51.3% to 64.4% across individual scrapes
2. Fine-tuning is the most common ML task - more common than model training from scratch
3. PyTorch dominates - 1.5x more common than TensorFlow in AI-First roles

Bottom Line: AI Engineers need practical ML knowledge (PyTorch basics, fine-tuning, embeddings) but don't need deep ML expertise unless specifically working on model development. This requirement is slowly weakening - see [trends](../job-market/trends.md) for how the trainer stack is shrinking against the integrator stack.


## What Else (Besides GenAI) Do AI Engineers Need?

93.7% of AI-First roles require skills BEYOND just GenAI

Skill combinations in AI Engineer roles:

- GenAI + Ops (Docker, K8s, CI/CD) - 77.0%
- GenAI + Web skills - 60.4%
- GenAI + ML skills - 51.5%
- GenAI + ANY other tech - 93.7%
- Pure GenAI (nothing else) - 1.5%

### Non-GenAI Skills Expected

| Category | Skills | % |
|----------|--------|--:|
| Cloud | AWS (42.9%), Azure (29.2%), GCP (28.6%) | - |
| Ops | Docker (38.2%), CI/CD (36.7%), Kubernetes (29.6%) | - |
| Web | REST APIs (27.7%), FastAPI (14.8%), React (15.2%) | ~60% do web work |
| Languages | Python (90.7%), TypeScript (22.0%), Java (16.8%) | Python mandatory |

Full-stack expectations:

- Frontend skills - 1,352/4,186 (32.3%)
- Backend skills - 2,551/4,186 (60.9%)
- Full-stack (both) - 1,012/4,186 (24.2%)

Across 40,074 extracted responsibilities, "deploy" appears in 3,716 and "monitor" in 1,885.

Bottom Line: AI Engineers are full-stack engineers who specialize in AI. Only 1.5% of roles expect pure GenAI work. Most need cloud deployment (AWS/Azure/GCP), containerization (Docker, K8s), CI/CD, and often web development (React, FastAPI).


## Fine-Tuning Requirements

27.4% of AI-First roles mention fine-tuning anywhere in the posting

### Depth of Fine-Tuning Expectation

| Level | Jobs | % | Description |
|-------|------:|--:|-------------|
| Primary FT responsibility | 130 | 3.1% | FT is main focus (model architecture, LoRA, PEFT) |
| Secondary/occasional FT | 480 | 11.5% | FT mentioned but not core |
| No FT in responsibilities | 3,576 | 85.4% | No fine-tuning expected |

### Fine-Tuning Use Cases

- Instruction following - Agents that follow complex instructions, task execution
- Domain knowledge - Medical, legal, finance, industry-specific applications
- Style/Tone - Brand voice, personality, formatting requirements
- Company data - Internal documents, proprietary data
- Performance - Smaller/faster models, latency optimization
- Language - Multilingual, non-English support
- Privacy - On-prem, offline, secure environments

Key findings:

1. Most AI Engineers don't fine-tune - it's absent from the responsibilities of 85.4% of roles
2. Primary FT roles are rare - only 3.1% focus on fine-tuning as main responsibility, down from 4.0%
3. Most common FT use case - domain knowledge (medical, legal, finance) and instruction following for agents
4. FT is a specialization - not a core AI Engineer skill, more advanced

Bottom Line

- Fine-tuning is optional for most AI Engineers.
- Focus on RAG and agents first.
- Learn fine-tuning if targeting domain-specific roles (healthcare, finance, legal), performance optimization roles, or specialized model development.


## Evaluation Skills

46.0% of AI-First roles explicitly require evaluation-related skills (model evaluation, LLM evaluation, guardrails, monitoring, observability, testing).

That number rose across the scrapes, from 41.2% in February to 71.1% in July. I would not read the full size of that jump as real - evaluation skills are exactly the kind of thing a more thorough extractor picks up more of, and the July extraction is the most thorough one. The scrape-by-scrape series is 41.2, 32.5, 34.2, 43.5, 39.8, 56.5, 71.1 - flat for four months, then a step up in the last two. Some of that step is the new extractor.

The specific skills inside that group:

- Observability - 9.7%
- Monitoring - 8.8%
- LLM evaluation - 7.7%
- Guardrails - 7.1%
- Model evaluation - 6.9%
- Model monitoring - 3.6%

"Evaluat" appears in 2,523 of 40,074 responsibilities, so the real demand is broader than the skill lists suggest.

This is the differentiator. RAG and agents are now baseline expectations. The ability to measure whether an AI system actually works - LLM-as-judge, golden datasets, hallucination detection, drift monitoring - is what separates candidates.


## Key Insight: RAG + Agents = 70%+ of Use Cases

The two dominant patterns are:

- RAG - connect LLMs to your data (documents, databases). 42.9% of all jobs, 55.0% of AI-First jobs
- Agents - LLMs that use tools to accomplish tasks. 35.5% of all jobs, 44.5% of AI-First jobs

They are usually asked for together: 835 jobs list both AI agents and RAG. In the responsibility text, "agent" appears in 5,187 of 40,074 responsibilities and "RAG" in 2,309.

If you learn these two patterns deeply, you can handle most AI Engineering use cases. See [use cases](04-use-cases.md) for what companies actually build with them.


## Learning Path for AI Engineers

- Foundation - Python, APIs, basic web development (FastAPI/React)
- LLM Basics - Prompt engineering, OpenAI/Anthropic APIs
- RAG - Vector databases, embeddings, retrieval patterns
- Frameworks - LangChain or LlamaIndex
- Agents - LangGraph, agent orchestration, MCP
- Evaluation - LLM-as-judge, golden datasets, guardrails, monitoring
- Production - Docker, Kubernetes, CI/CD, observability

The typical AI engineering stack:

- APPLICATION layer - React, Next.js, FastAPI
- AI ORCHESTRATION layer - LangChain, LangGraph, LlamaIndex
- LLM APIS layer - OpenAI, Anthropic, local models
- VECTOR DATABASES layer - Pinecone, Weaviate, pgvector
- INFRASTRUCTURE layer - Docker, K8s, AWS/GCP/Azure
