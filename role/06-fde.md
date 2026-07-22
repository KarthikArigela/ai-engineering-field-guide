# Forward Deployed Engineers: What Our Job Data Shows

Forward Deployed Engineer (FDE) is one of the fastest-growing titles in our AI engineering job data. We found 28 live FDE listings in February 2026 and 118 in July, a 4.2x increase in less than six months.

We're writing a longer article about this FDE trend for Substack. [Subscribe on Substack](https://alexeyondata.substack.com/) if you want to read it when it comes out.

The rest of the AI engineering market grew too, but much more slowly. Our full scrape grew 2.3x over the same period. FDE roles also increased from 2.0% to 3.6% of all listings.

We use only data collected by the [AI Engineering Field Guide](../job-market/README.md).

We analyze the job titles and structured descriptions from our scrapes to answer three questions:

- How quickly is the role growing?
- What do FDEs do?
- Which skills do employers want?

## FDE listings grew 4.2x

We count a listing as an FDE role when its title contains `FDE` or `forward deploy`.

Across our seven scrapes, we found:

| Scrape date | All AI engineering listings | FDE listings | FDE share |
|---|---:|---:|---:|
| 2026-02-04 | 1,416 | 28 | 2.0% |
| 2026-02-27 | 2,057 | 41 | 2.0% |
| 2026-03-27 | 2,341 | 58 | 2.5% |
| 2026-04-22 | 2,473 | 65 | 2.6% |
| 2026-05-29 | 2,751 | 80 | 2.9% |
| 2026-06-25 | 3,024 | 108 | 3.6% |
| 2026-07-22 | 3,320 | 118 | 3.6% |

The headline count grew by 321%, from 28 to 118. The full market grew by 134%, from 1,416 to 3,320.

FDE hiring grew about 1.8 times faster than the market in our dataset. The title is still a small part of the market, but it's no longer a rounding error.

These counts measure live listings in each scrape, and the same vacancy can appear on more than one date. We use the per-scrape figures for the trend and a separate deduplicated dataset to study the jobs.

## We found 146 unique FDE roles

After deduplicating by job ID, we found 146 FDE positions from 94 companies.

No single company dominates the sample:

- Databricks has five unique listings
- Mistral AI, Stord, Thomson Reuters, and Truelogic Software have four each
- Anthropic, Invisible Technologies, NewRocket, OneStream Software, and Turing have three each

The other employers cover many sectors. We found the title at model companies and data platforms. We also found it at enterprise software vendors, consulting firms, logistics companies, and healthcare businesses. FDE isn't limited to frontier AI labs.

## Customer work plus production ownership

We extracted and classified the responsibilities in every matched posting:

- 132 postings, or 90%, mention building or deploying production systems
- 129, or 88%, mention working directly with customers or clients
- 94, or 64%, mention integrating systems, APIs, or data
- 76, or 52%, mention scoping requirements or running discovery
- 71, or 49%, mention evaluation, testing, or monitoring
- 45, or 31%, mention feeding field lessons into the product
- 42, or 29%, mention prototypes, proofs of concept, or demos
- 13, or 9%, mention travel or onsite work

The combination is more revealing than any individual number. An FDE doesn't just demo a product or advise a customer. Employers expect the engineer to discover the problem, integrate the customer's systems, write production code, and stay responsible for whether the result works.

Our structured classifier marks 133 of the 146 roles, or 91%, as customer-facing. Only 16 roles, or 11%, are management positions. FDE is primarily an individual-contributor engineering role with unusually high customer exposure.

## The skill profile is applied, not research-heavy

Python appears in 91% of the postings.

Prompt engineering and RAG come next, followed by cloud and delivery skills:

- Python: 133 postings, or 91%
- Prompt engineering: 80, or 55%
- RAG: 76, or 52%
- AWS: 68, or 47%
- LLMs: 63, or 43%
- AI agents: 62, or 42%
- Docker: 59, or 40%
- GCP: 55, or 38%
- Kubernetes: 51, or 35%
- Azure: 50, or 34%
- CI/CD: 49, or 34%
- LangChain: 48, or 33%

Employers want LLM application skills, but they also expect engineers to work with APIs and customer data. Containers, cloud platforms, and deployment pipelines appear throughout the postings.

AWS appears in 47% of the sample, GCP in 38%, and Azure in 34%. FDEs can't assume that every customer uses the same stack. They need to deploy into the environment already in place.

## This is not an entry-level title

Most titles don't state a level, but the titles that do skew senior:

- 107 titles have no seniority marker
- 19 say Senior
- 8 say Principal
- 6 say Staff
- 5 say Lead
- 1 says Founding
- 0 say Junior or entry-level

The lack of a marker doesn't mean that 107 roles are junior. Their descriptions still ask for production ownership, customer communication, and broad technical judgment. None of the 146 titles explicitly targets junior or entry-level candidates.

That makes sense given the work. An FDE has to make technical decisions in an unfamiliar customer environment, often before the requirements are clear. Companies are looking for engineers who can handle both the code and the conversation.

## FDE hiring is outgrowing the market

We draw three conclusions from our dataset:

1. FDE hiring is outgrowing the AI engineering market. Live listings grew 4.2x while the full crawl grew 2.3x.
2. Employers define the role through production delivery. Around nine in ten postings mention production work and direct customer interaction.
3. Employers ask for broad technical skills. Python, RAG, agents, cloud platforms, containers, and CI/CD all appear frequently.

Job postings describe employer demand, not the exact day-to-day experience of every FDE. Our title match can miss similar jobs advertised under other names. For example, we also see Applied AI Engineer, Solutions Engineer, and Deployment Engineer. Read our numbers as a lower bound for this style of work, not a complete count.

AI companies need engineers who can bridge the gap between a working demo and a system inside a customer's business. More employers are calling that engineer an FDE.

## Methodology

We analyzed the seven scrape snapshots in [`job-market/_internal/data/scrapes`](../job-market/_internal/data/scrapes/) from February 4 through July 22, 2026.

For the trend, we matched titles containing `FDE` or `forward deploy`, without case sensitivity. We calculated the role profile from the 146 matching job IDs in the [deduplicated dataset](../job-market/_internal/data/all_jobs_dedup.csv) and their latest available records in [`job-market/data_structured`](../job-market/data_structured/).

The responsibility figures use keyword groups across the structured responsibility bullets. The customer-facing and management figures come from the structured classifications produced by the Field Guide pipeline.
