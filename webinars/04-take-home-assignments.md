# Webinar 4: AI Engineering - Take-Home Assignments

- Date: March 9, 2026
- Host: [Alexey Grigorev](https://www.linkedin.com/in/agrigorev/)
- [Recording on YouTube](https://www.youtube.com/watch?v=NItSoNCj7bg)

## Description

Take-home assignments are where your ability to build production-ready systems is truly measured. This session focuses on moving beyond understanding requirements to mastering execution in take-home assignments used by top-tier companies.

## Topics Covered

1. Home assignments analysis - examining recent Q4 2025 and Q1 2026 submissions to understand current AI hiring standards
2. Implementation discussion - deconstructing real-world assignment prompts and analyzing effective architectural approaches with trade-offs
3. End-to-end document implementation - building a complete solution for document-instruction tasks, emphasizing high-accuracy PDF parsing and data extraction

## Key Findings

### How common are take-home assignments?

Of the 51 companies with disclosed interview processes, 17 (33%) include a take-home or asynchronous assignment, and an additional 5 use paid work trials. Analysis of 100+ GitHub repos of real candidate submissions (Q4 2025 / Q1 2026) shows what companies actually ask for.

Full data and assignment examples are in [Home Assignments](../interview/questions/06-home-assignments.md).

### What companies ask for

- RAG systems (40%+) - document upload, vector databases, citation support
- Agentic systems (30%+) - tool-calling, multi-step reasoning, multi-agent orchestration
- Conversational AI (20%+) - chatbots, live chat agents, voice assistants
- Document processing (15%) - PDF parsing, data extraction, marksheet extraction
- LLM-as-judge evaluation (10%+) - build a system then evaluate it with another LLM

### Format

Asynchronous assignments completed on your own time, typically with a 2-7 day deadline. You submit code, a writeup, or a working prototype, then defend your solution in a 45-90 minute follow-up interview. The most common format is a take-home coding project (2-4 hours of actual work) where companies emphasize decision-making and clarity over cleverness.

AI tool policy for take-homes: only 1 company explicitly allows AI tools, none explicitly ban them (bans apply to live interviews only), and most don't mention it at all.

### Evaluation criteria

Many assignments include explicit scoring rubrics. Patterns across repos:

- Functional correctness - does the system work end-to-end and handle edge cases
- Code quality and architecture - modular design, extensibility, error handling
- Evaluation methodology - whether you build an eval harness and measure quality systematically
- Production readiness - caching, monitoring, cost optimization, security (PII handling, rate limiting)
- Performance targets - response time (<2s p95), throughput (100+ req/s), cache hit rates (>40%)
- Testing - unit tests are sometimes mandatory, with coverage targets around 80%
- Weighted rubrics - e.g., 30% functionality, 30% challenge completion, 25% context engineering, 15% code quality

### What makes a submission stand out

- Start with evaluation - build an eval harness before writing the main logic. YC startups report this as the top signal: "Red flag if candidate doesn't start with evals"
- Document design decisions and trade-offs, not just the final code
- Include a video walkthrough of your submission
- Make it configurable - one engineer built a PDF summarizer CLI with configurable models and chunking strategies, got two competing offers within 72 hours
- Show production awareness - error handling, monitoring hooks, cost estimates, even when not explicitly required
- The single biggest differentiator: candidates who skip evaluation and testing of AI outputs are the ones who don't get offers
