# Defining the AI Engineer Role

Analysis of what AI engineers actually do, based on 5,740 job descriptions from builtin.com, collected in seven monthly scrapes between February and July 2026.

## Contents

1. [My vision of the role](01-my-vision.md) - how I see AI engineering, comparison with DS/ML/DE roles, CRISP-DM for AI
2. [Skills analysis](02-skills.md) - top skills, job types, cloud platforms, frameworks
3. [Responsibilities](03-responsibilities.md) - 33,957 extracted responsibilities across 4,894 jobs
4. [Use cases](04-use-cases.md) - 24,502 real use cases showing what companies build with AI
5. [Reality vs. job postings](05-reality-vs-postings.md) - what candidates experience vs. what's advertised
6. [Forward Deployed Engineers](06-fde.md) - growth, responsibilities, and skills from 146 FDE job postings

## Key Takeaways

### What is an "AI Engineer" in 2026?

- It's a new role, distinct from ML Engineer. AI engineers integrate pre-trained models into applications (RAG, agents, orchestration). ML engineers train models. But titles are broken - "AI Engineer" means different things at different companies.
- Three types of roles hide under the same title:
  - AI-First (72.9%) - builds RAG systems, agents, LLM-powered features
  - AI-Support (24.1%) - builds platforms, infrastructure, tooling for AI teams
  - ML (2.0%) - traditional ML rebranded
- It's fundamentally a full-stack role. 93.7% of roles need skills beyond GenAI. Only 1.5% expect pure GenAI work. You need cloud, Docker, CI/CD, often web development too.

### What they actually build

- RAG + Agents dominate. RAG appears in 42.9% of all jobs, agents in 35.5%. Together they cover 70%+ of use cases. If you learn these two patterns deeply, you cover most of the work.
- The #1 problem AI solves is automating manual workflows (15.4% of use cases). Not glamorous - it's reducing repetitive work at scale.
- Knowledge access is universal. Every domain (healthcare, legal, finance, enterprise) has the same problem: too much information, can't find what's needed. RAG solves this everywhere.

### Skills that matter

- Python is mandatory (84.6%). After that: RAG (42.9%), AWS (41.8%), prompt engineering (41.0%), CI/CD (38.0%), Docker (37.5%), Kubernetes (30.3%).
- Fine-tuning is overhyped. Only 3.1% of roles focus on it as a primary responsibility. 85.4% don't mention it at all. Focus on RAG and agents first.
- 57.8% still require some ML knowledge - but it's practical ML (PyTorch basics, fine-tuning, embeddings), not deep research expertise.

### What actually gets you hired

- Evaluation is the differentiator. 46.0% of AI-First roles explicitly require evaluation skills, and that share is rising. Anyone can build a chatbot - companies hire people who can measure if it works (LLM-as-judge, golden datasets, hallucination detection).
- Production thinking wins over accuracy obsession. 77.0% of AI-First roles combine GenAI with production/ops skills (Docker, Kubernetes, CI/CD, MLOps, Terraform).
- 97.2% of roles are applied/production, not research. Only 2.8% are research roles. The market wants people who ship, not people who publish.

