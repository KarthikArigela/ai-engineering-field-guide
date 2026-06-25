# Job Market Data

4,894 AI Engineer job descriptions from builtin.com (January - June 2026) covering LA (Global), New York, London, Amsterdam, Berlin, and India.

For analysis and insights based on this data, see [role/](../role/).

## Contents

- [data_structured/](data_structured/) - structured YAML files grouped into `YYYY-MM-DD/` scrape-date folders
- [data_raw/](data_raw/) - raw extracted YAML files grouped into `YYYY-MM-DD/` scrape-date folders
- [analysis.ipynb](analysis.ipynb) - Jupyter notebook with data analysis
- [_internal/](_internal/) - scraping scripts, processing scripts, and `_internal/data/` for pipeline CSVs

## Highlights

- 3,567 jobs (72.9%) are AI-First (RAG, agents, LLMs)
- 1,199 jobs (24.5%) are AI-Support (platforms, infrastructure, tooling)
- 91 jobs (1.9%) are traditional ML rebranded as "AI Engineer"
- 1,954 unique companies, led by Capital One (91), Citi (74), Optum (58)

Top skills:

- Python (83.7%), TypeScript (21.3%), Java (17.6%)
- RAG (34.1%), LLMs (17.7%), prompt engineering (15.9%)
- AWS (40.0%), Docker (35.2%), Kubernetes (29.4%)
- LangChain (23.8%), PyTorch (20.9%), SQL (25.8%)

## Data Format

Each YAML file in `data_structured/YYYY-MM-DD/` contains:

```yaml
title: Senior AI/Data Engineer
company: WorkWave
location: USA
work_type: FULL_TIME
level: Expert/Leader
skills: [Python, AWS, Airflow, dbt]
company_size: 1,000 Employees
compensation: $160,000 - $180,000/year
description: |
  Full job description...
posted_date: 2026-01-18
url: https://builtin.com/job/...
source: Built In
```
