# Common Mistakes

Weak portfolio projects usually break before coding starts.

Most weak projects skip problem discovery, evaluation, and a runnable repo plan.

## Picking Technology First

"I want to build a RAG app" isn't a project idea.

Start with the work someone needs to do.

Then choose the tool:

- retrieval
- tool use
- structured output
- vision
- classifier
- deterministic code

RAG fits when answers must be grounded in documents.

Agents fit when the system must use tools, look at intermediate results, or take multiple steps.

Use structured output when the user needs fields, labels, summaries, or actions.

Reddit and X discussions around AI engineer portfolios repeat the same warning. Generic chatbots and RAG demos are weak without evals, logs, baselines, and a clear user problem. Source: [discussion notes](_internal/discussion-threads.md).

## Picking Random Companies

Don't choose companies by brand name alone.

Pick target jobs, then group them into domains:

- support
- e-commerce
- legal
- healthcare
- finance
- developer tools
- education
- logistics

A project aimed at OpenAI plus Stripe plus a hospital is too scattered.

A project aimed at "B2B support teams that answer policy questions from long docs" has clearer users, inputs, outputs, and eval cases.

## Reading Blogs Passively

Engineering blogs are useful only if you extract problems.

Ask:

- What work was the team improving?
- What did a person have to read, decide, route, summarize, or check?
- What data was involved?
- What made the old process slow, expensive, risky, or inconsistent?
- What would a small useful version do?
- How would someone know whether it worked?

Passive research gives you buzzwords, while active research gives you specs.

## Not Extracting Problems

A domain isn't a problem.

Too broad:

```text
Healthcare AI
```

Concrete:

```text
Summarize appointment notes into a structured follow-up message, with a refusal path for medical advice.
```

Before building, write:

- who uses it
- what input they provide
- what output they need
- what version 1 will do
- how you'll check it

If you can't answer those, go back to discovery.

## Building a Generic Chatbot

"Chat with your documents" is usually too generic.

Stronger versions name the user and task:

- support lead reviews refund requests against company policy
- legal ops analyst extracts risky clauses from vendor contracts
- developer relations team turns GitHub issues into triaged tickets
- marketplace seller drafts product listings from photos and rough notes

Chat can be the interface, but it shouldn't be the whole idea.

## Choosing Tools That Do Not Fit

RAG, agents, and multi-agent systems add work.

They require:

- data ingestion
- tool schemas
- error handling
- traces
- evaluation
- failure cases

Use the advanced part only when the problem needs it.

Examples:

- Use structured output for field extraction.
- Use RAG when the system must cite changing documents.
- Use tool calling when the system must query APIs or update state.
- Use multiple agents only when separate roles make evaluation easier.

If one model call and deterministic code solve version 1, start there.

## No Evaluation Plan

An AI portfolio project needs a way to tell whether it improved.

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

Take-home reviewers check the same thing in [Home Assignments](../interview/questions/06-home-assignments.md).

## No Monitoring Plan

Monitoring can start as a local log.

Log:

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

These logs help you debug and show that you treat AI systems as software systems.

## No Repo Plan

A good project can still look weak if the repo is hard to understand.

Plan the repo:

- `README.md` explains problem, user, first version, demo, and trade-offs
- `src/` or app folders contain product code
- `tests/` covers deterministic code
- `evals/` contains eval data, runner, and results
- `data/` contains sample data or instructions
- `.env.example` lists configuration
- CI runs tests and a small eval when practical

Public project and take-home sources keep repeating the same basics:

- readable README
- run instructions
- tests
- evaluation
- clear explanation of decisions

See the [local corpus](_internal/local-corpus.md) and [discussion notes](_internal/discussion-threads.md).

## Quick Check

Before committing to an idea, ask:

- Can I name the target domain and user?
- Did I look at real companies or workflows?
- Did I extract a concrete problem?
- Do I have realistic inputs?
- Does the technology fit the task?
- Can I define version 1?
- Can I evaluate it?
- Can I log failures, cost, or latency?
- Can I make the repo easy to run and discuss?

If the answer is no, the project isn't ready to build.
