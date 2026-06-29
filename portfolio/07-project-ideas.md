# Project Ideas

Use this page to see how the selection exercise works in different domains.

Don't copy these projects.

Use each example to study:

- domain
- companies
- job descriptions
- blogs or docs
- problems
- real repos with similar ideas
- technology choices

## Exercise

For each domain:

1. Read the job descriptions
2. Read the company blogs or docs
3. List problems the companies solve
4. Pick one problem
5. Find public or synthetic data
6. Build a small version
7. Add tests, evals, logs, and a clear README

## Finance

Companies and sources:

- Capital One: [Senior Lead AI Engineer, GenAI Platform Services](https://builtin.com/job/senior-lead-ai-engineer-gen-ai-platform-services/9420327), [tech blog](https://www.capitalone.com/tech/blog/)
- Wells Fargo: [Lead Specialty AI Java Software Engineer](https://builtin.com/job/lead-specialty-ai-java-software-engineer-electronic-trading/9879596), [developer portal](https://developer.wellsfargo.com/)
- BlackRock: [Rust AI Engineer](https://builtin.com/job/rust-ai-engineer-director/9629914), [engineering blog](https://engineering.blackrock.com/)

Problems to look for:

- compare long financial documents
- extract risks from filings or earnings calls
- summarize research with citations
- monitor policy or compliance changes
- route analyst questions to the right data source

Repos to study:

- [SEC Insights](https://github.com/run-llama/sec-insights)
  - domain: finance
  - problem: analysts need to explore SEC filings without manually reading every filing
  - approach: RAG over SEC documents with a finance-specific UI
- [Invoice Extract and Reconcile](https://github.com/run-llama/template-workflow-extract-reconcile-invoice)
  - domain: finance operations
  - problem: teams need to extract invoice fields and reconcile them against agreements
  - approach: structured extraction, typed schema, confidence, rationale, and review UI

Possible candidates:

- earnings-call risk extractor
- SEC filing comparison assistant
- invoice extraction and reconciliation tool
- compliance-change monitor
- analyst research assistant with citations

Likely technology:

- RAG for filings and policies
- structured output for extracted fields
- eval set for citation correctness and field accuracy
- logs for latency, cost, and retrieval failures

## Healthcare

Companies and sources:

- Optum: [Senior AI/ML Engineer](https://builtin.com/job/senior-ai-ml-engineer/9555837), [technology and automation insights](https://business.optum.com/en/insights/technology-automation.html)
- GE HealthCare: [Senior AI Engineer, Intelligent Automation](https://builtin.com/job/senior-ai-engineer-intelligent-automation/9641768), [research blog](https://research.gehealthcare.com/blog/)
- Commure: [Senior Software Engineer, AI Integrations](https://www.builtinla.com/job/senior-software-engineer-ai-integrations/9835679), [blog](https://www.commure.com/blog/)

Problems to look for:

- search medical content safely
- summarize clinical or administrative notes
- classify patient messages
- route requests to the right workflow
- extract structured fields from forms

Repos to study:

- [Claims RAG Assistant](https://github.com/ayusyagol11/claims-rag-assistant)
  - domain: healthcare and insurance
  - problem: workers-comp users need answers grounded in claim documents
  - approach: document ingestion, RAG, citations, Streamlit UI, and a 20-question eval
- [HR Policy LLM RAG Assistant](https://github.com/galafis/hr-policy-llm-rag-assistant)
  - domain: policy Q&A
  - problem: users need grounded policy answers with fallback behavior
  - approach: RAG, guardrails, FastAPI, Streamlit, Docker, tests, and evals

Possible candidates:

- patient-message triage assistant
- medical policy search assistant
- insurance claim Q&A tool
- appointment-note follow-up generator
- intake-form extractor

Likely technology:

- RAG for policy and medical content
- refusal behavior for unsafe advice
- structured output for forms and routing
- evals for groundedness and refusal correctness

## Legal and Regulatory

Companies and sources:

- Thomson Reuters: [Senior Software Engineer, AI Legal CoCounsel FDE](https://builtin.com/job/senior-software-engineer-ai-legal-cocounsel-fde/9090355), [TR Labs](https://www.thomsonreuters.com/en/about-us/labs)
- Wolters Kluwer: [Enterprise Software Engineer, GenAI](https://builtin.com/job/enterprise-software-engineer-python-azure-aws-gen-ai/9827155), [AI page](https://www.wolterskluwer.com/en/about-us/artificial-intelligence)
- Diligent: [Forward Deployment Engineer](https://builtin.com/job/technical-pre-sales-prototyper-forward-deployment-engineer/8775074), [AI governance blog](https://www.diligent.com/resources/blog/ai-governance)

Problems to look for:

- review contracts
- extract risky clauses
- search regulations
- summarize legal documents
- produce auditable answers with source text

Repos to study:

- [ExtractThinker](https://github.com/enoch3712/ExtractThinker)
  - domain: document intelligence
  - problem: teams need typed extraction from PDFs and document images
  - approach: OCR, LLM extraction, typed schemas, and batch processing
- [Invoice Extract and Reconcile](https://github.com/run-llama/template-workflow-extract-reconcile-invoice)
  - domain: document review
  - problem: reviewers need extracted fields, discrepancies, confidence, and rationale
  - approach: extraction plus reconciliation and human review UI

Possible candidates:

- risky-clause reviewer
- policy compliance checker
- legal document summarizer with citations
- regulation change monitor
- document extraction review queue

Likely technology:

- structured output for clauses and fields
- RAG for legal sources
- human review for high-risk outputs
- evals for extraction accuracy and citation correctness

## Cybersecurity

Companies and sources:

- CrowdStrike: [Senior AI Engineer](https://builtin.com/job/sr-ai-engineer-remote-ind/9716390), [engineering blog](https://www.crowdstrike.com/en-us/blog/author.crowdstrike-engineering/)
- Arctic Wolf: [Senior Staff Developer, AI SOC Automation](https://builtin.com/job/senior-staff-developer-ai-soc-automation/9592723), [blog](https://arcticwolf.com/resources/blog/)
- Cisco: [Gen AI Software Engineer](https://builtin.com/job/gen-ai-software-engineer-python-devops-frontend/9882427), [developer docs](https://developer.cisco.com/)

Problems to look for:

- summarize alerts
- explain suspicious activity
- classify incidents
- route alerts to response playbooks
- reduce analyst overload

Repos to study:

- [Vercel Express Issue Triage Agent](https://github.com/vercel-labs/express-issue-triage-agent-template)
  - domain: triage workflow
  - problem: maintainers need to classify issues and draft replies
  - approach: webhook, classifier, labels, and generated responses
- [Agentic RAG](https://github.com/tohio/agentic-rag)
  - domain: operational RAG
  - problem: users need answers that may require routing and tool use
  - approach: RAG, routing, date lookup, traces, evals, Docker, tests, and Streamlit

Possible candidates:

- security alert summarizer
- incident triage assistant
- suspicious-login explanation tool
- playbook retrieval assistant
- vulnerability report classifier

Likely technology:

- classification for severity and routing
- RAG for playbooks
- tool use for enrichment lookups
- logs and traces for every decision

## Developer Tools

Companies and sources:

- JetBrains: [Senior Software Developer, IntelliJ AI](https://builtin.com/job/senior-software-developer-intellij-ai/9646277), [AI blog](https://blog.jetbrains.com/ai/)
- Grafana Labs: [Staff AI Engineer](https://builtin.com/job/staff-ai-engineer-grafana-ai-ml-usa-remote/9886859), [engineering blog](https://grafana.com/blog/engineering/)
- Coinbase: [Staff Software Engineer, AI Platform](https://www.builtinla.com/job/staff-software-engineer-ai-platform-team/9889856), [engineering blog](https://www.coinbase.com/blog/landing/engineering)

Problems to look for:

- triage issues
- review pull requests
- explain code changes
- generate release notes
- search internal engineering docs

Repos to study:

- [Repo Assistant](https://github.com/guillermoscript/repo-assistant)
  - domain: developer tools
  - problem: maintainers need to detect duplicate GitHub issues
  - approach: GitHub app, embeddings, Supabase, and `pgvector`
- [Qodo PR Agent](https://github.com/qodo-ai/pr-agent)
  - domain: developer tools
  - problem: teams need automated pull-request review support
  - approach: PR analysis, comments, summaries, and review automation
- [Open Code Review](https://github.com/spencermarx/open-code-review)
  - domain: developer tools
  - problem: reviewers need help finding issues in code changes
  - approach: multi-agent review workflow

Possible candidates:

- duplicate issue detector
- PR review assistant
- release-note generator
- voice-to-GitHub-issue bot
- engineering-doc search assistant

Likely technology:

- embeddings for duplicate detection
- tool use for GitHub APIs
- structured output for labels and comments
- tests around routing, parsing, and permissions

## Marketplace and E-Commerce

Companies and sources:

- Airbnb: [Staff Software Engineer, Marketplaces Intelligence](https://www.builtinla.com/job/staff-software-engineer-marketplaces-intelligence-data-and-ai/9609308), [tech blog](https://airbnb.tech/blog/)
- eBay: [AI Platform Engineer](https://builtin.com/job/ai-platform-engineer/9345591), [tech stories](https://innovation.ebayinc.com/stories/)
- Toast: [Principal Software Engineer, AI Pod](https://builtin.com/job/principal-software-engineer-ai-pod-dublin-ireland/9611924), [technology blog](https://technology.toasttab.com/)

Problems to look for:

- create product listings
- enrich catalogs
- classify listings
- detect duplicates
- improve search and recommendations

Repos to study:

- [LISTING-INTELLIGENCE](https://github.com/KazKozDev/LISTING-INTELLIGENCE)
  - domain: marketplace listings
  - problem: sellers need better listing quality, SEO, and compliance checks
  - approach: vision, OCR, multimodal LLMs, FastAPI, React, and compliance checks
- [eBay Listing Automation](https://github.com/jjshay/ebay-listing-automation)
  - domain: e-commerce
  - problem: sellers need to turn inventory and images into listings
  - approach: vision, structured listing fields, tests, Docker, and eBay API integration
- [AWS AI-Powered Product Catalog](https://github.com/aws-samples/sample-ai-powered-product-catalog)
  - domain: product catalog
  - problem: teams need to create product catalog entries from photos
  - approach: Bedrock, Streamlit, S3, Lambda, Step Functions, and DynamoDB

Possible candidates:

- listing generator with quality checks
- product categorization and deduplication
- policy-compliant listing review
- catalog enrichment from images and vendor data
- marketplace search evaluator

Likely technology:

- vision model for images
- structured output for listing fields
- deterministic validation for policy checks
- evals for field accuracy and compliance

## Study Checklist

For each repo, ask:

- What domain is it in?
- What problem does it solve?
- Who's the user?
- What input does it take?
- What output does it produce?
- How does it prove the output works?
- Which parts are deterministic code?
- Which parts need an LLM?
- What tests or evals are included?
- What would make the repo stronger?

Use those answers to write your own repo plan.
