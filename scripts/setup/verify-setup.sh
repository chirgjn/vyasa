#!/usr/bin/env bash
# Verify the project setup is working correctly
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/helpers.sh"

echo "Verification"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export PATH="${REPO_ROOT}/.local/bin:${PATH}"

if [[ ! -f pyproject.toml ]]; then
    fail "pyproject.toml not found.
       Run this script from the project root directory.
       Current directory: $(pwd)"
fi

if ! command -v uv &>/dev/null; then
    fail "uv not found — run scripts/setup/install-uv.sh first"
fi

if ! command -v jq &>/dev/null; then
    fail "jq not found — run scripts/setup/install-jq.sh first"
fi

if ! command -v gh &>/dev/null; then
    fail "gh not found — run scripts/setup/install-gh.sh first"
fi

if ! gh auth status &>/dev/null; then
    fail "gh is not authenticated — run: gh auth login"
fi

if ! command -v taplo &>/dev/null; then
    fail "taplo not found — run scripts/setup/install-taplo.sh first"
fi

if ! command -v pnpm &>/dev/null; then
    fail "pnpm not found — run scripts/setup/install-pnpm.sh first"
fi

info "running taplo lint..."
if ! taplo lint pyproject.toml; then
    fail "taplo found issues in pyproject.toml.
       Fix the issues listed above, then re-run verification."
fi
ok "pyproject.toml valid"

info "running prettier..."
if ! framework/tools/prettier-fix.sh --check; then
    fail "prettier found formatting issues.
       Auto-fix with: framework/tools/prettier-fix.sh
       Then re-run verification: scripts/setup/verify.sh"
fi
ok "markdown formatted"

info "running shellcheck..."
if ! scripts/tools/shellcheck-lint.sh; then
    fail "shellcheck found shell script issues.
       Fix the violations listed above, then re-run verification."
fi
ok "no shell lint errors"

info "running yamllint..."
if ! scripts/tools/yamllint-fmt.sh --check; then
    fail "yamllint found issues in YAML files.
       Auto-fix with: scripts/tools/yamllint-fmt.sh
       Then re-run verification: scripts/setup/verify.sh"
fi
ok "YAML files valid"

info "running actionlint..."
if ! uv run actionlint; then
    fail "actionlint found issues in .github/workflows/.
       Fix the issues listed above, then re-run verification."
fi
ok "GitHub Actions workflows valid"

info "running tests..."
if ! scripts/tools/pytest-run.sh; then
    fail "Tests failed.
       Check the output above for details.
       Run tests manually for more verbose output: uv run pytest tests/ -v"
fi
ok "tests pass"
