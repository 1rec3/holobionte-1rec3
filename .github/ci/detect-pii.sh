#!/usr/bin/env bash
# detect-pii.sh - rudimentary checks for emails, phones, long quoted blocks
# Exits 1 if finding suspicious patterns; adjust as needed.

set -eu
FILES="$@"
if [ -z "$FILES" ]; then
  FILES=$(git diff --name-only "$GITHUB_EVENT_BEFORE" "$GITHUB_SHA" | grep -E '\.md$|\.json$' || true)
fi

FOUND=0
for f in $FILES; do
  if [ ! -f "$f" ]; then continue; fi
  if grep -E -n -H -e '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f" >/dev/null 2>&1; then
    echo "PII: email found in $f"
    FOUND=1
  fi
  if grep -E -n -H -e '\b(\+?[0-9]{2,3}[ -]?)?([0-9]{2,4}[ -]?){2,4}[0-9]{2,4}\b' "$f" >/dev/null 2>&1; then
    echo "PII: phone-like string found in $f"
    FOUND=1
  fi
  if awk '/^>/{c++} !/^>/{ if (c>=5) {print "Long quote block in " FILENAME; exit 0} c=0} END{ if (c>=5) {print "Long quote block in " FILENAME; exit 0}}' "$f" >/dev/null 2>&1; then
    echo "CITA-LONG: possible long quoted block in $f"
    FOUND=1
  fi
done

if [ "$FOUND" -ne 0 ]; then
  echo "PII/CITAS detected. If this PR needs quotes or personal data to be published, open an ohm-consent issue and get explicit approvals."
  exit 1
fi
exit 0
