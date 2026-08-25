# AI Engineering Jobs Analysis

Generated from 6,964 job descriptions extracted from builtin.com.

I searched for jobs containing "AI Engineer" keyword from LA (Global), New York, London, Amsterdam, Berlin and India. This is the combined result of eight monthly scrapes between February 4 and August 25, 2026.

There is no overlap in job IDs between scrapes, so each month is an independent cross-section of the market rather than the same postings re-counted.

All numbers here come from quantitative analysis in the [analysis notebook](../job-market/analysis.ipynb) and the scripts in [_internal/analysis/](../job-market/_internal/analysis/). For how these numbers moved month over month, see [trends](07-trends.md).

Summary

- 70.0% of roles work directly on AI (RAG, agents)
- 86.8% need skills beyond just GenAI - it's a full-stack role
- 39.8% of roles mention RAG - the most common named pattern in all jobs
- 54.0% of AI-First roles require some ML knowledge
- AWS (2,806 jobs) > Azure (2,060 jobs) > GCP (1,908 jobs)


## A Note on Measurement

Skills are extracted by an LLM from the job description text, then normalized through [canonicalize_skills.py](../job-market/_internal/analysis/canonicalize_skills.py), which collapses case, acronym, and synonym variants (e.g. "rag", "RAG pipelines", "retrieval-augmented generation") into one canonical skill name. Extraction runs on a single model (`glm-5.2`) with one fixed prompt across all eight scrapes, so skill shares are comparable month to month.

Treat all skill percentages as a floor, not a ceiling - a skill the description doesn't spell out doesn't get counted.


## "AI Engineering" Job Types

Job positions we analyzed fall into these categories:

- AI-first
- AI-support
- ML

65 jobs (0.9%) could not be classified.

### AI-First: 4,874 jobs (70.0%)

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


### AI-Support: 1,685 jobs (24.2%)

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


### Machine Learning: 340 jobs (4.9%)

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

These "AI Engineer" roles are traditional ML roles rebranded with the AI title. They do classical ML work (PyTorch, TensorFlow, computer vision) without any GenAI components.


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

Unique companies: 2,499

Top 20 companies by job count:

- Capital One - 120 jobs
- Citi - 98 jobs
- Optum - 90 jobs
- NVIDIA - 63 jobs
- BJAK - 52 jobs
- Thomson Reuters - 49 jobs
- Hewlett Packard Enterprise - 45 jobs
- Wells Fargo - 43 jobs
- Jack & Jill AI - 39 jobs
- NextHire Consulting - 39 jobs
- Wolters Kluwer - 38 jobs
- G2i - 37 jobs
- JPMorganChase - 34 jobs
- PwC - 32 jobs
- BlackRock - 30 jobs
- OpenAI - 29 jobs
- Ecolab - 29 jobs
- EXL - 29 jobs
- NICE - 28 jobs
- Weekday, Inc. - 28 jobs

The long tail is where the jobs are: 2,499 companies for 6,964 postings, and the largest single hirer (Capital One) accounts for 1.7% of the market. The biggest identifiable names - Capital One, Citi, Optum, Wells Fargo - are large public financial and healthcare companies, not AI labs or startups.

Roles:

- Customer-facing roles: 1,158 (16.6%)
- Management roles: 164 (2.4%)

Most common job titles (exact match):

- AI Engineer - 331 jobs
- Senior AI Engineer - 221 jobs
- Applied AI Engineer - 79 jobs
- AI/ML Engineer - 73 jobs
- Lead AI Engineer - 71 jobs
- Staff AI Engineer - 54 jobs
- Senior AI/ML Engineer - 54 jobs
- Principal AI Engineer - 48 jobs
- Senior Applied AI Engineer - 30 jobs
- AI Product Engineer - 28 jobs


## Skills Analysis

Percentages are the share of all 6,964 jobs.

Top GenAI skills:

- LLMs - 4,335 jobs (62.2%)
- AI agents - 2,896 jobs (41.6%)
- RAG - 2,772 jobs (39.8%)
- prompt engineering - 2,414 jobs (34.7%)
- agentic workflows - 2,120 jobs (30.4%)
- LangChain - 1,530 jobs (22.0%)
- OpenAI API - 1,056 jobs (15.2%)
- Anthropic API - 1,001 jobs (14.4%)
- MCP - 982 jobs (14.1%)
- LangGraph - 961 jobs (13.8%)
- LlamaIndex - 576 jobs (8.3%)

Counting any agent skill (AI agents, agentic workflows, multi-agent systems) once per job: 3,859 jobs (55.4%).

MCP is the clearest steady riser in the dataset. It grew from 9.9% of jobs in the February scrape to 17.6% in August, roughly doubling over the eight months, with a temporary dip in July.

Top ML skills:

- machine learning - 2,646 jobs
- PyTorch - 1,266 jobs
- TensorFlow - 935 jobs
- model evaluation - 806 jobs
- deep learning - 631 jobs
- scikit-learn - 537 jobs
- Hugging Face - 479 jobs
- model training - 467 jobs
- transformers - 395 jobs

Fine-tuning is now tracked under GenAI rather than ML skills - see [Fine-Tuning Requirements](#fine-tuning-requirements) below.

Top web skills:

- APIs - 1,843 jobs
- REST APIs - 1,120 jobs
- React - 1,033 jobs
- microservices - 1,026 jobs
- FastAPI - 680 jobs
- full-stack development - 474 jobs
- Flask - 267 jobs

Top database skills:

- vector databases - 1,647 jobs
- PostgreSQL - 775 jobs
- Pinecone - 510 jobs
- NoSQL - 487 jobs
- vector search - 466 jobs
- Snowflake - 409 jobs
- Weaviate - 359 jobs

Top cloud skills:

- AWS - 2,806 jobs (40.3%)
- Azure - 2,060 jobs (29.6%)
- GCP - 1,908 jobs (27.4%)
- AWS Bedrock - 429 jobs (6.2%)
- Vertex AI - 380 jobs (5.5%)
- SageMaker - 367 jobs (5.3%)

Top ops skills:

- CI/CD - 2,560 jobs
- Docker - 1,700 jobs
- Kubernetes - 1,666 jobs
- observability - 1,547 jobs
- MLOps - 1,201 jobs
- model deployment - 984 jobs
- monitoring - 958 jobs

Top languages:

- Python - 4,930 jobs (70.8%)
- TypeScript - 1,345 jobs (19.3%)
- Java - 1,230 jobs (17.7%)
- SQL - 1,000 jobs (14.4%)
- JavaScript - 805 jobs (11.6%)
- Go - 801 jobs (11.5%)


## GenAI Framework Ecosystem

Framework popularity:

- LangChain - 1,530 jobs (22.0%)
- LangGraph - 961 jobs (13.8%)
- LlamaIndex - 576 jobs (8.3%)
- CrewAI - 465 jobs (6.7%)
- AutoGen - 369 jobs (5.3%)
- Semantic Kernel - 224 jobs (3.2%)
- DSPy - 56 jobs (0.8%)

Frameworks travel together rather than compete. 700 jobs ask for LangChain and LangGraph, 549 for LangChain and LlamaIndex. Companies list the ecosystem, not a single tool.


## Supporting Roles: What AI-Support Engineers Do

1,685 jobs (24.2%) classified as AI-Support

| Category | Jobs | Description |
|----------|------:|-------------|
| Platform/Infrastructure | 1,101 | Build AI platforms, GPU clusters, MLOps tooling |
| Sales/Solutions | 179 | Pre-sales, customer demos, AI solutions consulting |
| Frontend/UI | 161 | Build UIs for AI products, chatbots, AI dashboards |
| Backend/General SWE | 142 | APIs, microservices, internal tools for AI teams |
| Data/Pipelines | 58 | Data pipelines, ETL, dataset preparation for ML |
| Other / Observability / SRE | 44 | QA/test, observability tooling, SRE for AI systems |

Do AI-Support roles need AI knowledge?

- 41.8% of AI-Support roles require SOME GenAI knowledge
- 58.2% require NO GenAI skills at all

GenAI skills in AI-Support roles:

- GitHub Copilot - 9.9%
- Claude Code - 8.5%
- Cursor - 8.2%
- prompt engineering - 8.1%
- RAG - 8.1%

GitHub Copilot, Cursor and Claude Code together appear in 15.5% of AI-Support roles - higher than in AI-First roles (11.1%). For support engineers, "AI skills" increasingly means using AI coding tools, not building AI systems.


### Skill Comparison (AI-First vs AI-Support)

| Skill | AI-First | AI-Support |
|:-------|---------:|------------:|
| RAG | 54.8% | 10.5% |
| Prompt engineering | 46.5% | 8.1% |
| Agents (any) | 71.6% | 20.9% |
| LangChain | 29.7% | 4.7% |
| Fine-tuning | 24.8% | 1.7% |
| Python | 75.6% | 56.9% |
| Docker | 24.6% | 25.6% |
| Kubernetes | 22.2% | 31.0% |
| CI/CD | 35.4% | 44.2% |
| Terraform | 8.1% | 16.7% |
| AWS | 45.2% | 41.4% |
| React | 15.5% | 18.8% |

The GenAI skills separate the two groups cleanly. The infrastructure skills don't - and where they differ, AI-Support asks for more of them.


## Research vs Applied Roles

| Role Type | Jobs | Percentage |
|----------|-----:|------------:|
| Research | 203 | 2.9% |
| Applied/Production | 6,761 | 97.1% |

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
- AI Research Engineer (Kernel & Inference Optimization)
- Research Engineer, AI
- Lead AI Engineer (AI Foundations, LLM Customization and Finetuning)

Applied / Production roles work on:

- Implementing existing models in production
- Building applications with AI APIs
- Deploying and monitoring AI systems
- Customer-facing AI solutions
- Infrastructure and platforms for AI
- Fine-tuning models for specific use cases

Keywords: production, deploy, customer, enterprise, product, API integration, shipping, implementation

The market wants people who ship, not people who publish.


### Example Comparison

| Research | Applied |
|----------|---------|
| "Run pre-training and post-training of state-of-the-art models on clusters with thousands of GPUs" (Mistral AI) | "Deploy production AI solutions with measurable business impact across various industries" (Mistral FDE) |
| "Develop novel reinforcement learning algorithms" | "Implement RAG patterns with vector store integration" |
| "Publish papers at top conferences" | "Ship AI features to customers" |


## What Other Titles Do "AI Engineers" Go Under?

Titles here are grouped across seniority levels, so "AI Engineer" includes Senior, Staff, Lead and Principal variants.

Strongly AI-First titles (75%+ classified as AI-First):

- AI Engineer - 800 jobs (92% AI-First)
- AI/ML Engineer - 173 jobs (76% AI-First)
- Applied AI Engineer - 121 jobs (93% AI-First)
- AI Software Engineer - 53 jobs (81% AI-First)
- AI Developer - 49 jobs (80% AI-First)
- Software Engineer - AI - 45 jobs (82% AI-First)
- AI Product Engineer - 38 jobs (82% AI-First)
- AI Solutions Engineer - 35 jobs (91% AI-First)
- Agentic AI Engineer - 32 jobs (100% AI-First)
- Forward Deployed AI Engineer - 31 jobs (97% AI-First)
- AI Automation Engineer - 31 jobs (90% AI-First)
- AI Research Engineer - 24 jobs (79% AI-First)
- Generative AI Engineer - 21 jobs (100% AI-First)
- Full Stack AI Engineer - 14 jobs (86% AI-First)

Strongly AI-Support titles (75%+ classified as AI-Support):

- AI Infrastructure Engineer - 14 jobs (86% AI-Support)

Titles that predict nothing:

- AI Platform Engineer - 51 jobs (53% AI-First, 47% AI-Support)
- AI Data Engineer - 40 jobs (65% AI-First, 32% AI-Support)
- Software Engineer (AI) - 19 jobs (68% AI-First, 26% AI-Support)

Key insight: "AI Engineer" is still the most common title and still the most reliable one (92% AI-First). But anything with "platform" or "data" in it is a coin flip - always check the responsibilities.

Agentic AI Engineer and Generative AI Engineer are both 100% AI-First and did not exist as titles at the start of the dataset. Forward Deployed Engineer remains one of the fastest-growing titles - see [Forward Deployed Engineers](06-fde.md) for the full picture on that role.


## How Much ML Do AI Engineers Need to Know?

54.0% of AI-First roles require some ML knowledge

Most common ML skills in AI-First roles:

- fine-tuning - 1,209 jobs (24.8%)
- embeddings - 1,115 jobs (22.9%)
- PyTorch - 949 jobs (19.5%)
- model evaluation - 687 jobs (14.1%)
- TensorFlow - 676 jobs (13.9%)
- model training - 457 jobs (9.4%)
- scikit-learn - 390 jobs (8.0%)

Key findings:

1. About half of AI Engineers need some ML knowledge - 54.0% require ML skills
2. Fine-tuning and embeddings are the most common ML-adjacent tasks - more common than model training from scratch
3. PyTorch dominates - about 1.4x more common than TensorFlow in AI-First roles

Bottom Line: AI Engineers need practical ML knowledge (PyTorch basics, fine-tuning, embeddings) but don't need deep ML expertise unless specifically working on model development. See [trends](07-trends.md) for how the trainer stack is shrinking against the integrator stack.


## What Else (Besides GenAI) Do AI Engineers Need?

86.8% of AI-First roles require skills BEYOND just GenAI

Skill combinations in AI Engineer roles:

- GenAI + Ops (Docker, K8s, CI/CD) - 70.6%
- GenAI + Web skills - 58.4%
- GenAI + ML skills - 39.2%
- GenAI + ANY other tech - 86.8%
- Pure GenAI (nothing else) - 3.9%

### Non-GenAI Skills Expected

| Category | Skills | % |
|----------|--------|--:|
| Cloud | AWS (41.2%), Azure (30.1%), GCP (28.4%) | - |
| Ops | CI/CD (35.3%), Docker (24.6%), Observability (24.4%) | - |
| Web | APIs (29.7%), REST APIs (15.8%), React (14.5%) | ~58% do web work |
| Languages | Python (75.6%), TypeScript (20.5%), Java (16.2%) | Python mandatory |

Full-stack expectations (AI-First roles):

- Frontend skills - 1,496/4,874 (30.7%)
- Backend skills - 2,933/4,874 (60.2%)
- Full-stack (both) - 1,103/4,874 (22.6%)

Bottom Line: AI Engineers are full-stack engineers who specialize in AI. Only 3.9% of roles expect pure GenAI work. Most need cloud deployment (AWS/Azure/GCP), containerization (Docker, K8s), CI/CD, and often web development (React, FastAPI).


## Fine-Tuning Requirements

27.3% of AI-First roles mention fine-tuning anywhere in the posting

### Depth of Fine-Tuning Expectation

| Level | Jobs | % | Description |
|-------|------:|--:|-------------|
| Primary FT responsibility | 174 | 3.6% | FT is main focus (model architecture, LoRA, PEFT) |
| Secondary/occasional FT | 578 | 11.9% | FT mentioned but not core |
| No FT in responsibilities | 4,122 | 84.6% | No fine-tuning expected |

### Fine-Tuning Use Cases

- Instruction following - Agents that follow complex instructions, task execution
- Domain knowledge - Medical, legal, finance, industry-specific applications
- Style/Tone - Brand voice, personality, formatting requirements
- Company data - Internal documents, proprietary data
- Performance - Smaller/faster models, latency optimization
- Language - Multilingual, non-English support
- Privacy - On-prem, offline, secure environments

Key findings:

1. Most AI Engineers don't fine-tune - it's absent from the responsibilities of 84.6% of roles
2. Primary FT roles are rare - only 3.6% focus on fine-tuning as main responsibility
3. Fine-tuning is a specialization - not a core AI Engineer skill, more advanced

Bottom Line

- Fine-tuning is optional for most AI Engineers.
- Focus on RAG and agents first.
- Learn fine-tuning if targeting domain-specific roles (healthcare, finance, legal), performance optimization roles, or specialized model development.


## Evaluation Skills

59.7% of AI-First roles require evaluation-related skills (model evaluation, LLM evaluation, guardrails, monitoring, observability, model monitoring).

That share moved from 55.9% in February to 59.6% in August, peaking at 65.2% in July - not a clean climb, but consistently the majority of roles all year.

The specific skills inside that group:

- LLM evaluation - 30.9%
- Observability - 24.5%
- Guardrails - 17.9%
- Monitoring - 14.1%
- Model evaluation - 14.1%
- Model monitoring - 7.6%

"Evaluat" appears in 3,309 of 50,326 extracted responsibilities, so the real demand is broader than the skill lists suggest.

This is the differentiator. RAG and agents are now baseline expectations. The ability to measure whether an AI system actually works - LLM-as-judge, golden datasets, hallucination detection, drift monitoring - is what separates candidates.


## Key Insight: RAG + Agents = Most Use Cases

The two dominant patterns are:

- RAG - connect LLMs to your data (documents, databases). 39.8% of all jobs, 53.9% of AI-First jobs
- Agents - LLMs that use tools to accomplish tasks. 55.4% of all jobs, 71.6% of AI-First jobs

They are usually asked for together: 2,213 jobs list both. In the responsibility text, "agent" appears in 6,822 of 50,326 responsibilities and "rag" in 1,668.

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
