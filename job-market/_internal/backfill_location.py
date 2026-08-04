#!/usr/bin/env python3
"""Backfill location fields in data_raw and data_structured YAML.

Early runs of the pipeline dropped `jobLocation` whenever Built In emitted it as
a list (multi-location postings), so those jobs ended up with an empty
`location`. This re-reads the stored HTML and patches the location lines only,
leaving descriptions and every other field byte-identical.

Usage:
    python backfill_location.py --dry-run
    python backfill_location.py
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
if str(SCRIPT_DIR / "scrapers") not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR / "scrapers"))

from pipeline_paths import (
    RAW_HTML_DIR,
    RAW_YAML_DIR,
    STRUCTURED_YAML_DIR,
    infer_job_id_from_filename,
    iter_files,
)
from extract_from_html import extract_from_json_ld, parse_job_locations, yaml_quote

LOCATION_BLOCK_RE = re.compile(
    r"^location:.*\n(?:locations:\n(?:  - .*\n)*)?(?:remote: true\n)?",
    re.MULTILINE,
)
META_BLOCK_RE = re.compile(r"^meta:\n((?:  .*\n|  - .*\n|\n)*)", re.MULTILINE)
META_LOCATION_LINE_RE = re.compile(
    r"^  location:.*\n(?:  locations:\n(?:  - .*\n)*)?|^  remote: true\n",
    re.MULTILINE,
)
META_JOB_ID_LINE_RE = re.compile(r"^  job_id: .*\n", re.MULTILINE)


def index_html_files():
    """Map job_id -> HTML path for every downloaded job page."""
    return {
        infer_job_id_from_filename(path): path
        for path in iter_files(RAW_HTML_DIR, "*.html")
    }


def read_locations(html_path):
    """Return (locations, remote) parsed from a stored job page."""
    json_ld = extract_from_json_ld(html_path.read_text(encoding="utf-8"))
    if not json_ld:
        return [], False
    return parse_job_locations(json_ld), json_ld.get("jobLocationType") == "TELECOMMUTE"


def read_locations_from_raw(raw_path):
    """Fall back to whatever the data_raw YAML already holds.

    The 2026-02-04 batch was extracted before the HTML was pruned, so its pages
    are gone but the single-location jobs still carry a usable `location`.
    """
    data = yaml.safe_load(raw_path.read_text(encoding="utf-8")) or {}
    locations = data.get("locations") or ([data["location"]] if data.get("location") else [])
    return locations, bool(data.get("remote"))


def render_raw_block(locations, remote):
    """Render the data_raw location lines."""
    primary = yaml_quote(locations[0]) if locations else ""
    lines = [f"location: {primary}\n" if primary else "location:\n"]
    if len(locations) > 1:
        lines.append("locations:\n")
        lines.extend(f"  - {yaml_quote(loc)}\n" for loc in locations)
    if remote:
        lines.append("remote: true\n")
    return "".join(lines)


def render_meta_block(locations, remote):
    """Render the data_structured meta location lines (two-space indented)."""
    if not locations and not remote:
        return ""
    lines = []
    if locations:
        lines.append(f"  location: {yaml_quote(locations[0])}\n")
        if len(locations) > 1:
            lines.append("  locations:\n")
            lines.extend(f"  - {yaml_quote(loc)}\n" for loc in locations)
    if remote:
        lines.append("  remote: true\n")
    return "".join(lines)


def patch_raw(path, locations, remote, dry_run):
    """Replace the location block in a data_raw YAML file."""
    text = path.read_text(encoding="utf-8")
    new_block = render_raw_block(locations, remote)
    if not LOCATION_BLOCK_RE.search(text):
        return "no-location-field"
    new_text = LOCATION_BLOCK_RE.sub(lambda _: new_block, text, count=1)
    if new_text == text:
        return "unchanged"
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return "patched"


def patch_structured(path, locations, remote, dry_run):
    """Insert location fields into the meta block of a data_structured YAML file."""
    text = path.read_text(encoding="utf-8")
    meta_match = META_BLOCK_RE.search(text)
    if not meta_match:
        return "no-meta-block"

    body = META_LOCATION_LINE_RE.sub("", meta_match.group(1))
    job_id_match = META_JOB_ID_LINE_RE.search(body)
    if not job_id_match:
        return "no-meta-job-id"

    new_body = (
        body[: job_id_match.end()]
        + render_meta_block(locations, remote)
        + body[job_id_match.end():]
    )
    new_text = text[: meta_match.start(1)] + new_body + text[meta_match.end(1):]
    if new_text == text:
        return "unchanged"
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return "patched"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Report counts without writing")
    args = parser.parse_args()

    html_by_id = index_html_files()
    print(f"Indexed {len(html_by_id)} HTML files")

    structured_by_id = {
        infer_job_id_from_filename(path): path
        for path in iter_files(STRUCTURED_YAML_DIR, "*.yaml")
    }

    counts = {"raw": {}, "structured": {}}
    no_html = 0

    for raw_path in iter_files(RAW_YAML_DIR, "*.yaml"):
        job_id = infer_job_id_from_filename(raw_path)
        html_path = html_by_id.get(job_id)

        if html_path is not None:
            locations, remote = read_locations(html_path)
            result = patch_raw(raw_path, locations, remote, args.dry_run)
            counts["raw"][result] = counts["raw"].get(result, 0) + 1
        else:
            # No page to re-parse - propagate what data_raw already has.
            no_html += 1
            locations, remote = read_locations_from_raw(raw_path)

        structured_path = structured_by_id.get(job_id)
        if structured_path is not None:
            result = patch_structured(structured_path, locations, remote, args.dry_run)
            counts["structured"][result] = counts["structured"].get(result, 0) + 1

    print(f"data_raw:        {counts['raw']}")
    print(f"data_structured: {counts['structured']}")
    print(f"No stored HTML (data_raw left as-is): {no_html}")
    if args.dry_run:
        print("Dry run - nothing written")


if __name__ == "__main__":
    main()
