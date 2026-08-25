#!/usr/bin/env bash
# The cheap checks. No judge, no hand-labelling, so these run on every scrape
# and every extractor change - not just when someone suspects a problem.
#
#   ./run_checks.sh                  # current corpus, self-consistency only
#   ./run_checks.sh <git-ref>        # also diff against that ref's extraction
#
# A silent provider-side model update is the failure this is meant to catch:
# the glm-5.1 to glm-5.2 switch moved the AI-First share by up to 10 points
# before anyone noticed, and nothing in the data recorded that it happened.
set -euo pipefail
cd "$(dirname "$0")"

BASE_ARG=()
if [[ $# -ge 1 ]]; then
  REF="$1"
  BASE=$(mktemp -d)
  echo "materialising extraction at ${REF} -> ${BASE}"
  git -C ../../.. archive "${REF}" job-market/data_structured \
    | tar -x -C "${BASE}" --strip-components=2
  BASE_ARG=(--baseline "${BASE}")
  trap 'rm -rf "${BASE}"' EXIT
fi

echo
echo "### duplicate-description label consistency"
uv run python consistency.py "${BASE_ARG[@]}"

echo
echo "### named-tool recall"
uv run python recall.py "${BASE_ARG[@]}"

if [[ ${#BASE_ARG[@]} -gt 0 ]]; then
  echo
  echo "### role flags and company stage"
  uv run python fields.py "${BASE_ARG[@]}"
fi

echo
echo "Watch for: consistency below ~95%, overall recall below ~98%, or any"
echo "field share moving more than a couple of points without a prompt change."
