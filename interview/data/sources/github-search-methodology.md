# GitHub Search Methodology

How we find actual take-home assignments for AI/ML engineer roles on GitHub.

## Tool

Primary tool: `gh search repos` (GitHub CLI, authenticated).

The GitHub search API searches repo names, descriptions, and README content, so queries with quoted phrases match repos where those phrases appear in any of those fields.

## Step-by-Step Process

### 1. Run searches

Run multiple query patterns to maximize coverage. Each search returns up to 100 results.

```bash
mkdir -p .tmp/home-assignments-search
cd .tmp/home-assignments-search

# Core assignment keyword combinations
gh search repos "ai engineer" "take home"     --limit 100 --json fullName,updatedAt,description --jq '.[] | "\(.fullName)\t\(.updatedAt)\t\(.description // "")"' > search_takehome.txt
gh search repos "ai engineer" "assignment"    --limit 100
gh search repos "genai" "take-home"           --limit 100
gh search repos "llm" "assignment"            --limit 100

# Broader: interview/hiring signals
gh search repos "rag" "interview"             --limit 100
gh search repos "agent" "ai" "hiring"         --limit 100
gh search repos "hiring" "challenge" "ai"     --limit 100

# Additional patterns (case study, coding challenge, home assessment)
gh search repos "ai engineer" "case study"    --limit 100
gh search repos "ai engineer" "coding challenge" --limit 100
gh search repos "ai engineer" "home assessment"  --limit 50
gh search repos "llm" "task" "interview"      --limit 100
gh search repos "ml engineer" "take home"     --limit 100
```

Each query catches repos that the others miss. Overlap is expected and deduplicated later.

### 2. Combine and deduplicate

```bash
# All unique repo full names across all searches
cat search_*.txt | sed 's/\t.*//' | sort -u > all_searched_repos.txt

# Load existing repos already in the collection (from questions/06-home-assignments.md,
# data/sources/github-repos.md, data/sources/all-links.md, research-exports/home-assignments.md)
grep -ohE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' ../../interview/questions/06-home-assignments.md \
    ../../interview/data/sources/github-repos.md \
    ../../interview/data/sources/all-links.md \
    ../../interview/data/research-exports/home-assignments.md \
    | sed 's|github.com/||' | sort -u > existing_repos.txt

# New repos not yet in the collection
comm -23 all_searched_repos.txt existing_repos.txt > new_candidate_repos.txt
```

### 3. Filter for genuine assignments

Most search results are noise: course assignments, bootcamp homework, academic projects, interview prep tools, and ML research papers using the word "assignment." Filter in two passes.

**Keep** repos whose name or description contains interview-signal keywords:
- `take-home`, `take home`, `home assessment`, `home test`
- `assignment` (combined with AI/LLM/RAG/GenAI/agent keywords)
- `case study`, `coding challenge`, `hiring challenge`, `technical test`, `interview task`

**Exclude** repos matching any of:
- Course/academic: `course`, `tutorial`, `bootcamp`, `udemy`, `classroom`, `university`, `CS###`, `lab`, `assignment-N`
- Prep tools: `interview-prep`, `interview-coach`, `mock-`, `leetcode`, `practice-`
- Research papers using "assignment" in the RL sense: `credit assignment`, `assignment grader`
- Non-AI: generic web dev, fraud detection, credit scoring without AI focus

**Require** at least one AI keyword: `ai engineer`, `llm`, `rag`, `genai`, `agent`, `generative ai`, `langchain`, `chatbot`, `gpt`.

```bash
grep -iE "(take.?home|home.?assessment|case.?study|hiring.?challenge|coding.?challenge|interview.?task|technical.?assign)" all_searched_full.txt \
  | grep -ivE "(course|tutorial|bootcamp|university|CS[0-9]|lab|interview-prep|mock-|credit.assignment)" \
  | grep -iE "(ai.engineer|llm|rag|genai|agent|generative|langchain|chatbot)" \
  | sort -u > genuine_candidates.txt
```

### 4. Manual curation

The remaining candidates (typically 150-250 after filtering) need manual review:

- **Company-issued challenges**: official org repos (e.g., `AuxoAI-Hiring/`, `ml6team/`, `jaseci-labs/`). These are the highest-value finds because they contain the original problem statement.
- **Candidate submissions with named companies**: repos where the description or README names the company (e.g., "KPN AI Engineer role," "VantageScore case study"). These reveal what companies actually ask.
- **Multiple submissions for one company**: group them. A single assignment can generate 5-15+ public submissions (e.g., Tredence Analytics self-pruning neural network: 20+ repos, Bithealth RAG refactoring: 5+ repos). Count as one assignment.
- **Drop ambiguous repos**: repos with empty descriptions, no company name, and no clear README problem statement. When in doubt, skip.

### 5. Save and integrate

Save curated results in `.tmp/home-assignments-search/curated_new_assignments.md`. These are staging only — not committed. Promising finds get promoted into:
- `interview/questions/06-home-assignments.md` — as categorized assignment examples
- `interview/data/sources/github-repos.md` — in the full repo list with company attribution

## Query Patterns That Work Best

| Query | Typical yield | Notes |
|-------|--------------|-------|
| `"ai engineer" "take home"` | 90+ | Highest signal-to-noise |
| `"ai engineer" "assignment"` | 100 | Noisy, needs filtering |
| `"ai engineer" "case study"` | 80+ | Catches Tredence-style assignments |
| `"ai engineer" "coding challenge"` | 25 | Smaller, higher quality |
| `"ai engineer" "home assessment"` | 20 | Very high signal |
| `"genai" "take-home"` | 15 | Low volume, high relevance |
| `"rag" "interview"` | 100 | Noisy, many prep repos |
| `"llm" "task" "interview"` | 30 | Good for LLM-specific tasks |
| `"ml engineer" "take home"` | 20 | Catches ML-focused assignments |

## Quality Indicators

Genuine assignments tend to have:
- Repo name includes company name or role title
- Description says "take-home", "interview", "assignment", "assessment", "challenge", or "case study"
- Updated within the last 12 months (2025-2026)
- Clear problem statement or README with requirements
- Not a fork of another assignment repo

## Common False Positives

- **Course homework**: GenAI bootcamp assignments, university courses (CS###, ELL###)
- **Assignment graders**: tools that grade assignments, not assignments themselves
- **RL credit assignment**: research papers using "assignment" in the reinforcement learning sense
- **Resume screening tools**: "AI hiring" platforms, not hiring assignments
- **Hackathon entries**: competitive coding challenges, not interview assessments

## Results

As of June 2026, this methodology surfaced 200+ genuine AI Engineer interview assignments on GitHub (143 catalogued, 161 newly identified in the latest search pass). Key patterns:

- RAG systems remain the most common (40%+)
- Agentic systems growing fast (30%+), including multi-agent orchestration
- LLM-as-judge evaluation emerging as a distinct assignment type
- Legal document processing is a rising category (multiple 2026 assignments)
- Common tech stack: LangChain/LangGraph + OpenAI/Claude + FastAPI + vector DB

See [github-repos.md](github-repos.md) for the full list of catalogued repos.
