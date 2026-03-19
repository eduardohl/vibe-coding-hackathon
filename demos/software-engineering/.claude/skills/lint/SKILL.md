---
name: lint
description: Lint and format all code in the project. Use when the user says "lint", "format code", "run eslint", "run prettier", "fix formatting", or wants to clean up code style.
---

# Lint and Format Code

Run code quality tools to check and fix formatting and lint issues.

## Steps

1. **Format** with Prettier
   - Run: `npx prettier --write "src/**/*.{js,jsx,ts,tsx,json,css}"`
   - Run: `npx prettier --write "*.{js,json,yaml,yml}"`
   - Report files changed

2. **Lint** with ESLint
   - Run: `npx eslint --fix "src/**/*.{js,jsx,ts,tsx}"`
   - Run: `npx eslint --fix "*.js"`
   - Report issues found and auto-fixed

3. **Format Python** files (if any)
   - Run: `ruff format src/**/*.py` (for setup scripts)
   - Run: `ruff check --fix src/**/*.py`

4. **Report** results
   - Files formatted by Prettier
   - ESLint issues found vs auto-fixed
   - Any remaining issues that need manual attention

## Usage

```
/lint                            # Fix all formatting and lint issues
/lint --check                    # Check only, don't fix
```

## Tools Used

| Tool | Purpose | Config |
|------|---------|--------|
| Prettier | Code formatting (JS/TS/JSON/CSS) | `.prettierrc` |
| ESLint | Code quality and patterns | `.eslintrc` |
| Ruff | Python formatting and linting | `ruff.toml` |

## Notes

- Prettier runs first (formatting), then ESLint (logic/patterns)
- Auto-fix resolves most issues automatically
- Remaining issues require manual attention
