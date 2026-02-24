---
description: Create a pull request for the current changes
---

# Create Pull Request

Create a pull request for the changes made in this session.

## Steps

1. **Review** changes
   - Run `git status` to see modified files
   - Run `git diff` to see the actual changes
   - Summarize what was changed and why

2. **Stage** changes
   - Add relevant files: `git add <files>`
   - Do NOT add sensitive files (.env, credentials, etc.)

3. **Commit** with a clear message
   - Follow conventional commit format
   - Include what changed and why

4. **Push** to remote
   - Create a feature branch if not already on one
   - Push with: `git push -u origin {branch}`

5. **Create PR** via GitHub MCP
   - Use the GitHub MCP to create the PR
   - Include:
     - Clear title summarizing the change
     - Description with context
     - Link to any relevant work items

## PR Template

```markdown
## Summary
Brief description of what this PR does.

## Changes
- List of specific changes made

## Testing
- How this was tested
- Job run URL (if applicable)

## Checklist
- [ ] Code follows project standards
- [ ] Job runs successfully
- [ ] Data quality validated
```

## Usage

```
/create-pr                    # Create PR with auto-generated description
/create-pr "Add new metrics"  # Create PR with custom title
```
