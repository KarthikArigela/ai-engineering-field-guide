# Polishing

A portfolio project becomes useful when someone can understand it, run it, and discuss it with you.

Polish isn't decoration because it shows evidence.

## README

Most people read the README first.

Make it answer:

- What problem does this solve?
- Who's it for?
- What input does it take?
- What output does it produce?
- How do I run it?
- How do I run tests and evals?
- What did the eval show?
- What failed or changed?
- Where are the important files?

Keep the first screen useful:

- one-paragraph summary
- demo screenshot, GIF, video, or sample output
- setup commands
- run command
- test command
- eval command

Don't write marketing copy because the work is the signal.

## Code Structure

Make the repo easy to scan.

Example:

```text
src/
  app.py
  retrieval.py
  prompts.py
  schemas.py
tests/
evals/
data/
README.md
PROJECT_PLAN.md
.env.example
```

Names should explain the project, so avoid one giant notebook or one giant script.

## Tests

Tests check deterministic behavior.

Good test targets:

- parsers
- chunking
- routing
- schema validation
- API responses
- refusal rules
- formatting

Run tests with one command.

Example:

```bash
pytest
```

Add CI if it's simple. A small GitHub Actions workflow that runs tests is enough.

## Evaluation

Evaluation checks AI behavior.

Start with 20-50 examples.

Include:

- easy cases
- messy cases
- out-of-scope requests
- refusal cases
- citation cases when sources matter

Pick metrics that match the project:

- answer relevance and citation correctness for RAG
- field accuracy and schema validity for extraction
- tool choice accuracy and task success for agents
- latency, token use, and cost for multi-step systems
- refusal correctness for safety-sensitive tasks

Save eval results in the repo.

Example:

```text
evals/results/2026-06-29.json
```

## Logs

Monitoring can start as a local log.

Log enough to debug:

- request ID
- model name
- prompt version
- retrieved sources
- tool calls
- validation errors
- latency
- token use
- cost
- feedback

A local JSONL file is enough if you can open it and explain what you learned.

## Demo

Pick one demo format:

- live URL
- short screen recording
- screenshots
- terminal recording
- sample input and output in the README

Don't depend on a fragile live demo only. Add screenshots or sample outputs so the repo still makes sense later.

## Final Pass

Before sharing the repo, check:

- README explains the problem and user
- setup works from a clean clone
- `.env.example` exists
- tests pass
- eval command runs
- sample data is legal to share
- no credentials are committed
- important files are linked from the README
- limitations are honest

Polishing makes the project easier to review, easier to remember, and easier to discuss.
