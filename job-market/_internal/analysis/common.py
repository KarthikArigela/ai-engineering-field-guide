"""Shared helpers for analysis scripts."""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

import pycountry
import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
INTERNAL_ROOT = SCRIPT_DIR.parent
if str(INTERNAL_ROOT) not in sys.path:
    sys.path.insert(0, str(INTERNAL_ROOT))

from pipeline_paths import STRUCTURED_YAML_DIR, iter_files


def load_structured_jobs() -> list[dict]:
    """Load all structured jobs across dated subdirectories."""
    jobs = []
    for file in iter_files(STRUCTURED_YAML_DIR, "*.yaml"):
        try:
            with file.open("r", encoding="utf-8") as handle:
                jobs.append(yaml.safe_load(handle))
        except Exception as exc:
            print(f"Error loading {file}: {exc}")
    return jobs


# ===== SKILLS =====
#
# Umbrella terms name a whole field rather than a specific capability. The
# extractor tags them whenever the description uses the general phrase, so
# their share measures how ads are worded, not what the work involves - after
# the prompt started requiring them, "Machine Learning" went from 5.4% to
# 48.4% of jobs without any change in the underlying market. Ranked next to
# LangChain or PyTorch they crowd out the top of every table and tell a reader
# nothing, so `job_skills` drops them by default.
#
# Matching is by exact name, so this assumes canonicalize_skills.py has
# already run over the data - "large language models" only becomes "LLMs"
# there. Analysis reads post-canonicalization, so that holds in the pipeline.
#
# They are still worth counting on their own (see `umbrella_skills`), and a
# curated grouping that happens to use one - trends.py counts "Agents (any)"
# as AI Agents + Agentic Workflows + Multi-Agent Systems - is a deliberate
# choice, not an accident of ranking. Those name their members explicitly.

UMBRELLA_SKILLS = frozenset({
    "AI",
    "AI Agents",
    "Agentic Workflows",
    "Artificial Intelligence",
    "Deep Learning",
    "Generative AI",
    "LLMs",
    "Machine Learning",
    "Multi-Agent Systems",
    "Neural Networks",
})

_UMBRELLA_LOOKUP = {s.lower() for s in UMBRELLA_SKILLS}


def is_umbrella(skill: str) -> bool:
    """Whether a skill names a whole field rather than a specific capability."""
    return skill.strip().lower() in _UMBRELLA_LOOKUP


def job_skills(job: dict, *, umbrella: bool = False) -> dict[str, list[str]]:
    """A job's skills by category, umbrella terms dropped unless asked for.

    Categories left empty by the filter are omitted entirely, so callers can
    keep testing `if category in skills`.
    """
    raw = (job.get("position") or {}).get("skills") or {}
    out = {}
    for category, skills in raw.items():
        if not isinstance(skills, list):
            continue
        kept = skills if umbrella else [s for s in skills if not is_umbrella(s)]
        if kept:
            out[category] = kept
    return out


def flat_skills(job: dict, *, umbrella: bool = False) -> set[str]:
    """A job's skills lowercased and deduped across categories.

    Several skills are filed under two categories (Vector Databases under both
    `databases` and `genai`), so counting the flattened lists double-counts.
    """
    return {s.lower() for skills in job_skills(job, umbrella=umbrella).values()
            for s in skills}


def umbrella_skills(job: dict) -> set[str]:
    """Just the umbrella terms a job mentions, lowercased."""
    return flat_skills(job, umbrella=True) - flat_skills(job)


# ===== LOCATION =====
#
# Locations come from the job page's JSON-LD, not the LLM, and live under
# `meta`. `location` is the primary (first) location; `locations` is only
# present for postings listed in more than one place.

# Built In uses ISO-3166 alpha-3 codes, with a few of its own spellings.
COUNTRY_NAME_OVERRIDES = {
    "EUR": "Europe (unspecified)",
    "USA": "United States",
    "GBR": "United Kingdom",
    "KOR": "South Korea",
    "RUS": "Russia",
    "TWN": "Taiwan",
    "VNM": "Vietnam",
    "CZE": "Czechia",
    "BOL": "Bolivia",
    "VEN": "Venezuela",
    "TZA": "Tanzania",
    "IRN": "Iran",
    "MDA": "Moldova",
    "LAO": "Laos",
    "SYR": "Syria",
    "BRN": "Brunei",
}


def job_locations(job: dict) -> list[str]:
    """All locations for a job, primary first. Empty if unknown."""
    meta = job.get("meta") or {}
    if meta.get("locations"):
        return list(meta["locations"])
    return [meta["location"]] if meta.get("location") else []


def primary_location(job: dict) -> str | None:
    """The job's first listed location, or None."""
    return (job.get("meta") or {}).get("location")


def is_remote(job: dict) -> bool:
    """Whether the posting is flagged as remote (JSON-LD TELECOMMUTE)."""
    return bool((job.get("meta") or {}).get("remote"))


def split_location(location: str) -> tuple[str | None, str]:
    """Split 'Bengaluru, IND' into ('Bengaluru', 'IND').

    Country-only locations such as 'USA' return (None, 'USA').
    """
    city, _, country = location.rpartition(", ")
    return (city or None), country


def job_countries(job: dict) -> list[str]:
    """Distinct country codes for a job, primary first."""
    countries = []
    for location in job_locations(job):
        _, country = split_location(location)
        if country not in countries:
            countries.append(country)
    return countries


@lru_cache(maxsize=None)
def country_name(code: str) -> str:
    """Human-readable country name, falling back to the code itself."""
    if code in COUNTRY_NAME_OVERRIDES:
        return COUNTRY_NAME_OVERRIDES[code]
    match = pycountry.countries.get(alpha_3=code)
    return match.name if match else code
