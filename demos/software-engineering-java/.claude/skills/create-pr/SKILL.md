---
name: create-pr
description: Create a pull request for the current changes with quality checks. Use when the user says "create pr", "pull request", "create a PR", or wants to submit code for review.
---

# Create Pull Request

Create a pull request for the changes made in this session.

## Steps

1. **Review** changes
   - Run `git status` and `git diff` to see modifications
   - Summarize what was changed and why

2. **Run quality checks** before committing
   - Run `mvn test` to verify tests pass
   - If any check fails, fix it first

3. **Stage and commit**
   - Add relevant files: `git add <files>`
   - Do NOT add IDE files, target/, or sensitive files
   - Commit with a clear conventional commit message

4. **Push** to remote
   - Create a feature branch if not already on one
   - Push with: `git push -u origin {branch}`

5. **Create PR** via `gh` CLI
   - Clear title summarizing the change
   - Description with context and test results

## Usage

```
/create-pr                    # Create PR with auto-generated description
/create-pr "Add supply CRUD"  # Create PR with custom title
```
