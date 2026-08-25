# Extraction Evaluation

The job data is produced by an LLM reading job descriptions, so the numbers in
the published analysis are only as good as that extraction. In August 2026 I
re-extracted the whole corpus with a rewritten prompt, and this directory is
how I checked whether the new extraction was actually better rather than just
different.

Why it mattered: the extraction model changed from `glm-5.1` to `glm-5.2`
partway through the seven scrapes, which made a longitudinal dataset partly a
measurement of the extractor instead of the market. The AI-First share swung
between 69.1% and 79.0% across scrapes, and skills per job climbed steadily
from 15.3 to 21.3. Neither was real.


## What I measured

I sampled 50 job descriptions and put the old and new extraction of each side
by side, labelled A and B in a random per-job order. I read the description,
graded both extractions against it, and wrote every verdict to `grades.json`
before looking at which side was which.

A uniform random 50 would have spent most of its budget on jobs both
extractions get right, so the sample is stratified. Twelve jobs are a random
baseline; the other seven strata target places the two disagree or either one
is known to be shaky - classification disagreements, jobs that lost a core
skill, jobs that gained an evaluation skill, the ml-first/ai-first boundary,
the ai-support boundary, unusually sparse or dense extractions, and jobs that
were dropped or classified `unknown`. Each stratum records its share of the
corpus so `score.py` can reweight the rates back to a population estimate.

Each extraction was graded on three things:

- ai_type - correct, defensible, or wrong against the taxonomy's decision procedure
- precision - how many extracted skills the description never states
- recall - how many clearly stated skills the extraction dropped


## Results

Head to head, the new extraction was preferred on 38 of 50 jobs, the old on 2,
with 10 ties.

Classification:

- old - 39 correct, 2 defensible, 9 wrong (78.0% clean)
- new - 49 correct, 1 defensible, 0 wrong (98.0% clean)

All nine classification errors belong to the old extraction, and they cluster
where the taxonomy is hardest. Infrastructure roles read as ai-first (eBay's
inference platform), developer-tooling roles read as ai-first (Compass AI
DevEx), pure computer vision research read as ai-first (Helsing 3D vision), and
job titles overrode empty descriptions (Hexaware, whose entire posting is a
semicolon-separated keyword list, was classified ai-first from its title).

Skill precision, meaning extracted skills the description never states:

- old - 74 invented across 25 of 50 jobs
- new - 4 invented across 4 of 50 jobs

The worst single case is Protolabs `IC4 - ML Engineer AI COE`, whose "What
You'll Do" and "What It Takes" sections are both empty. The old extraction
produced 18 skills - PyTorch, TensorFlow, Docker, Kubernetes, MLflow, Python,
SQL, computer vision - none of which appear anywhere in the text. It generated
the ML-engineer archetype. The new extraction returned the two terms actually
present.

Skill recall, meaning stated skills that were dropped:

- old - 49 missed across 15 of 50 jobs
- new - 6 missed across 5 of 50 jobs

Reweighted to the corpus, the old extraction has roughly a 9.5% classification
error rate and 1.3 invented skills per job; the new one has no observed errors
and 0.1 invented skills per job.


## Two checks that need no judge

The blind eval is expensive and I am the judge, so I added two objective
probes that can run on every extraction change.

`consistency.py` finds groups of near-identical job descriptions - some
employers post the same text once per programming language - and checks whether
the group gets one label. Whatever the right answer is, it must be the same
across the group. Across 274 groups covering 620 postings, the old extraction
is 91.9% internally consistent and the new one 95.6%.

The cleanest example landed in the eval sample by chance. G2i posts the same
RLHF description once per language. The old extraction called the C version
ai-first and the Java version ai-support - same text, same day, contradictory
labels.

`recall.py` probes whether a named tool was extracted, using only tools whose
name is a distinctive string. Across 1,674 stated skills the new extraction
recalls 98.6% and the old 96.7%. MCP is the largest gap, 100.0% against 81.3%.

This probe measures recall only. Precision still needs a reader, because a
missing string is not the same as an unsupported skill - a description can
require containers without writing the word Docker.


## The fields the blind eval missed

The 50-job eval covered `ai_type` and `skills`. Afterwards I checked the fields
it did not, and two of them turned out to be the worst data in the corpus. Both
extractions are unreliable here, so this is not an old-versus-new result.

`is_management` had no definition anywhere in the prompt - it was a bare boolean
with a `False` default, and the model was left to guess. The old extraction
flags 17.2% of jobs as management and the new one 4.5%, a fourfold
disagreement. Against the text, only 3.0% of jobs have an unambiguous
management title and 1.5% describe line management in the body. Of the jobs
each extraction flags, 86.4% (old) and 71.3% (new) have neither. Recall is bad
too: on unambiguous management titles the old extraction catches 65.3% and the
new one only 37.0%. The new extraction is more conservative without being more
correct.

`company_stage` said only "extract if mentioned". Just 15.0% of descriptions
actually name a stage, but the old extraction records one for 82.1% of jobs and
the new for 49.1%. Of those, 82.6% and 76.4% respectively have no stage
anywhere in the text. The old extraction invented specific funding rounds -
Series A, Series B - which means it was recalling companies from pretraining
rather than reading the ad. The new one invents vaguer buckets like "Startup"
and "Venture-backed".

`is_customer_facing` is also undefined in the prompt. It moved from 22.4% to
16.5% with 92.8% agreement between the two. I have no objective probe for it,
so I can say it drifted but not which version is right.

Consequences for the published analysis:

- The company-stage table in `role/02-skills.md` rests on roughly 80% inferred
  data. It describes the model's memory of these companies, not the postings.
- The management share is not a usable number in either extraction.

I have since written definitions for all three into the prompt and made
`company_stage` refuse to infer. Those fields need a re-extraction before they
can be quoted again.

Caveat on the probes: "unsupported" is measured against a deliberately narrow
regex, so some genuine managers phrased unusually will be counted as
unsupported. The regex understates evidence rather than inventing it, so the
error rates are upper bounds - but the gap between 17.2% flagged and 3.0%
titled is far too wide to be probe noise.


## Limits

- I am the judge, and the correct answer is my reading of the same decision
  procedure the new prompt encodes. That biases the classification comparison
  toward the new extraction. The precision and recall findings are more
  independent, since those only ask whether the description contains the words.
- The blind leaked. The new extraction's reasoning refers to "Step 1" and to
  edge cases, so on many jobs I could tell the two apart. I graded from the
  description, but the effect is not zero.
- Zero errors in 50 is not a zero error rate. At this sample size the 95% upper
  bound is roughly 6%.
- The eval covers `ai_type` and `skills` only. Nothing here validates
  `responsibilities`, `use_cases`, `company.stage`, `is_management`, or
  `is_customer_facing`.


## Keeping the eval honest over time

Seed 2026 is burned. I have read those 50 descriptions and written verdicts on
them, so any prompt tuned against that set will start fitting my grades rather
than the job market. Treat it as a regression set: re-run it to check nothing
broke, but do not cite it as evidence that a change improved anything.

Any new claim of improvement has to be measured on a fresh seed that nobody has
looked at yet, graded once, and then retired the same way.

The two cheap probes do not have this problem. `consistency.py` and
`recall.py` derive their ground truth from the corpus itself rather than from a
grader, so they can be run continuously without being overfitted. That is why
`run_checks.sh` exists and why it runs on every scrape rather than only when
something looks wrong.


## Files

- [run_checks.sh](run_checks.sh) - the cheap checks, run these on every scrape
- [build_eval.py](build_eval.py) - samples the stratified set and writes the blind batches
- [score.py](score.py) - unblinds and scores, with population reweighting
- [consistency.py](consistency.py) - duplicate-description label agreement, no judge needed
- [recall.py](recall.py) - corpus-wide named-tool recall probe
- [fields.py](fields.py) - role flags and company stage against the job text
- [grades.json](grades.json) - my 50 verdicts, written while blind
- [manifest.json](manifest.json) - the sample, the strata, and the A/B mapping


## Reproducing

The baseline extraction is the state of `job-market/data_structured` at commit
`7e269b34`, before the re-extraction was swapped in:

```
git archive 7e269b34 job-market/data_structured | tar -x -C /tmp/base --strip-components=2
uv run python build_eval.py --baseline /tmp/base --out ./run1
uv run python score.py --dir ./run1
```

Sampling uses a fixed seed, so the same 50 jobs come back. `grades.json` is
keyed to job numbers from that seed against the current corpus.
