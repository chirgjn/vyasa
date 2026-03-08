#!/usr/bin/env bash
set -euo pipefail
# Lint shell scripts with shellcheck.
# Usage: shellcheck-lint.sh [file ...]  (defaults to scripts/ if no args)
if [ $# -eq 0 ]; then
    # shellcheck disable=SC2046
    set -- $(find scripts/ framework/tools/ -name '*.sh' -type f)
fi
uv run shellcheck -x --source-path=scripts/setup "$@"
