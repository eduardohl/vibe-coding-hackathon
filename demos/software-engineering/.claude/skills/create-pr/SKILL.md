---
name: create-pr
description: Create a pull request for the current changes with quality checks. Use when the user says "create pr", "pull request", "create a PR", "push and create PR", or wants to submit code for review.
---

# Create Pull Request

Create a pull request for the changes made in this session.

## Steps

1. **Review** changes
   - Run `git status` to see modified files
   - Run `git diff` to see the actual changes
   - Summarize what was changed and why

2. **Run quality checks** before committing
   - Run `npm test` to verify tests pass
   - Run `npx prettier --check .` to verify formatting
   - Run `npx eslint .` to verify no lint errors
   - If any check fails, fix it first

3. **Stage** changes
   - Add relevant files: `git add <files>`
   - Do NOT add sensitive files (.env, credentials, node_modules, etc.)

4. **Commit** with a clear message
   - Follow conventional commit format
   - Include what changed and why

5. **Push** to remote
   - Create a feature branch if not already on one
   - Push with: `git push -u origin {branch}`

6. **Create PR** via GitHub MCP
   - Use the GitHub MCP to create the PR
   - Include:
     - Clear title summarizing the change
     - Description with context
     - Test results summary
     - Link to any relevant work items

## PR Template

```markdown
## Summary
Brief description of what this PR does.

## Changes
- List of specific changes made

## Testing
- Test results (pass/fail counts)
- Coverage percentage
- Manual testing performed

## Quality Checks
- [ ] Tests passing
- [ ] Linting clean
- [ ] No security issues
- [ ] Code reviewed by agent
```

## Usage

```
/create-pr                    # Create PR with auto-generated description
/create-pr "Add product CRUD" # Create PR with custom title
```
