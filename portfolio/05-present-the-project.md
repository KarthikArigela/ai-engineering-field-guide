# Present the Project

The repo gets you the interview, and the explanation helps you use it.

Prepare two things:

- a skimmable project page
- a clear interview story

## Project Page

Use the README, a portfolio page, or a short case study as the project page.

Include:

- problem
- user
- input
- output
- demo
- architecture
- tests
- evaluation
- limitations
- links to important files

Keep it direct.

Example:

```text
This project helps support agents answer billing questions from policy documents.
It takes a support ticket and a small billing-policy knowledge base.
It returns a draft answer with citations and an escalation flag.
```

## Demo

Pick one demo format:

- live URL
- short screen recording
- screenshots
- terminal recording
- sample input and output in the README

Don't rely only on a live demo. Add screenshots or sample outputs so the project still makes sense later.

## 60-Second Pitch

Use the short pitch when someone asks, "Tell me about a project you built."

Cover:

- problem
- user
- solution
- evidence
- ownership

Example:

```text
I built a support-ticket triage assistant for small SaaS teams.
It takes a new ticket, retrieves similar past tickets and billing-policy snippets, and drafts a categorized response with citations.
I wrote the project plan first, then built the API, retrieval flow, eval set, and CI checks.
The first version beat keyword search on 34 of 50 labeled examples, but it still failed on billing edge cases.
I added refusal rules and regression tests for those cases.
```

Give the interviewer hooks instead of listing every library.

## Deep Dive

Use this order:

1. Problem and user
2. Inputs and outputs
3. First version
4. Architecture
5. Decisions
6. Evaluation
7. Tests and monitoring
8. Demo and impact
9. Next steps

This matches the [project deep dive interview](../interview/questions/03-project-deep-dive.md). Interviewers use the deep dive to test ownership, judgment, and depth.

Pause after each section and treat it as a conversation.

## Explain Decisions

Prepare the "why" behind each important choice.

Weak:

```text
I used a vector database.
```

Stronger:

```text
I started with keyword search as the baseline.
It missed paraphrased billing questions in 11 of the first 50 eval examples.
So I added vector search and kept keyword search as a fallback.
```

Use this structure:

```text
I chose X over Y because of constraint Z.
The downside was A.
I accepted it because B.
If the project grew, I would change C.
```

The decision matters more than the tool name.

## Discuss Failures

Prepare real failure stories.

Useful examples:

- the first prompt answered outside the retrieved context
- chunking broke citations
- the eval set exposed a missing refusal case
- the agent called a tool when deterministic code was enough
- the live demo was too slow or expensive
- the UI hid errors that logs made obvious

For each failure:

1. What broke?
2. How did you find it?
3. What did you change?

A clear failure story often shows more judgment than a polished feature list.

## Explain Evaluation

Be ready to explain:

- what examples are in the eval set
- how you created labels
- what baseline you used
- what metric you chose
- which cases still fail
- what changed after the eval
- what you would monitor after deployment

Impact can be modest.

Strong honest evidence:

- eval improved over baseline
- latency or cost decreased
- a user tried the demo
- the project automated part of your own work
- the project showed that the original idea should stop

"It didn't work well enough, and I can explain why" is better than pretending the demo solved everything.

## Ownership

Be precise about what you owned.

Clear ownership:

- "I wrote the project plan, picked the first version, and built the eval set."
- "The course provided the broad task, but I chose the domain, data, architecture, and tests."
- "A teammate built the UI. I built the API, retrieval code, and evaluation harness."
- "I used an AI coding assistant for boilerplate and refactoring, but I reviewed the code, wrote tests, and changed the design when evals failed."

Don't claim a tutorial or group project as solo work.

Don't undersell real decisions either.

## Follow-Up Questions

Before each interview, reread the plan and README.

Prepare short answers:

- What problem were you solving?
- Why this first version?
- What was your exact role?
- What did you design yourself?
- What alternatives did you reject?
- What trade-off are you least happy with?
- What failed first?
- How did you debug it?
- How did you evaluate AI output quality?
- What surprised you?
- What would break first if usage grew?
- What would you do differently?

After the interview, update the plan or README if an answer was weak.
