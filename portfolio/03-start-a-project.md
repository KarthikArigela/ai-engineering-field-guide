# Start a Project

After you pick the project, start the repo before the idea grows.

The first step isn't coding, because you first need to turn the selection work into a visible plan.

## Create the Repo

Start with a small structure:

```text
README.md
PROJECT_PLAN.md
src/
tests/
evals/
data/
.env.example
```

Add only folders you expect to use.

Use `data/` for sample data or instructions. Don't commit private data, credentials, scraped pages with unclear terms, or interview-private material.

## Save the Evidence

Put the evidence in the repo plan.

Collect:

- target domain
- target companies
- job descriptions
- company blog posts
- product docs
- public datasets or sample documents

Use links, not vague notes.

Example:

```text
Domain: healthcare
Companies: Optum, GE HealthCare, Commure
Job descriptions:
- Optum Senior AI/ML Engineer: https://builtin.com/job/senior-ai-ml-engineer/9555837
Company sources:
- GE HealthCare research blog: https://research.gehealthcare.com/blog/
- Commure blog: https://www.commure.com/blog/
```

This makes the project defensible because you can show why it exists.

## Write the Plan

Use `PROJECT_PLAN.md`, `docs/project-plan.md`, the first section of `README.md`, or a GitHub issue.

Using AI is fine for this step. Use it to summarize notes, compare project candidates, or draft the plan. Then check the result against the job descriptions, blog posts, data, and constraints you collected.

Start with discovery:

```text
# Project Plan

## Domain

## Target Companies

## Evidence
- Job descriptions:
- Company blog posts:
- Product docs:
- Public data:

## Problem
- User:
- Input:
- Output:
- Failure modes:
- Success check:

## Project Candidates
1.
2.
3.
4.
5.

## Selected Project
```

Then add the build plan:

```text
# Build Plan

## First Version

## Technologies to Demonstrate
- LLM:
- RAG:
- Agents/tools:
- Evaluation:
- Tests:
- Monitoring/logging:
- Deployment/demo:

## Architecture

## Data

## Evaluation

## Tests

## Monitoring

## Demo

## README Notes
```

Keep each section short, with one or two paragraphs at the start.

## Define Version 1

Write what version 1 must do:

- ingest a small dataset
- run from a CLI, API, or simple UI
- produce one useful output
- handle one normal case
- handle one failure case
- run tests and evals from documented commands

Also write what it won't do.

Example:

```text
The first version will not support multi-user accounts, streaming responses, or automatic ticket updates.
It will produce a draft response that a person can review.
```

## Pick the Initial Stack

Use boring tools unless a specific tool teaches a skill you need.

A practical stack:

- Python for backend, scripts, evals, and model calls
- FastAPI, Flask, Streamlit, or CLI for the interface
- SQLite, Postgres, or files for storage
- vector database only when retrieval needs it
- pytest for deterministic tests
- small eval script for AI behavior
- logs for model calls, tool calls, cost, and latency
- README with setup, run, test, and eval commands

Add TypeScript, Docker, CI, or cloud deployment only when it helps the project or the hiring signal.

## Start Small

Build one end-to-end path first.

Example:

```text
sample input -> processing -> model call or retrieval -> validation -> output
```

Don't start with dashboards, accounts, multiple providers, or a complex agent graph.

Get one path working, then polish it.
