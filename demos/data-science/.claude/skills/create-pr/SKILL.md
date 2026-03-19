---
name: create-pr
description: Create a GitHub PR with experiment results. Use when the user says "create pr", "pull request", "create a PR", "push and create PR", or wants to submit ML code for review.
---

# Create Pull Request

Create a GitHub pull request with ML experiment changes and results.

## Steps

1. **Check for changes**
   - Run `git status` to see modified files
   - Ensure training code changes are staged

2. **Gather experiment context**
   - Get latest MLflow run metrics
   - Summarize model improvements

3. **Create commit**
   - Stage all relevant changes
   - Write descriptive commit message with metrics

4. **Push and create PR**
   - Push to feature branch
   - Create PR with experiment summary

## PR Description Format

```markdown
## Summary
Brief description of the model changes.

## Experiment Results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| RMSE   | 0.95   | 0.82  | -14%   |
| MAE    | 0.71   | 0.61  | -14%   |
| R2     | 0.65   | 0.74  | +14%   |

## Changes Made
- Added feature engineering for cyclical time features
- Implemented log transform for target variable
- Tuned hyperparameters (learning_rate=0.1, max_depth=6)

## MLflow Run
- Run ID: `{run_id}`
- Experiment: `/Users/{user}/hackathon-demand`

## Test Plan
- [ ] Validated on holdout test set
- [ ] Checked for data leakage
- [ ] Reviewed feature importance
```

## Usage

```
/create-pr                    # Create PR with auto-generated description
/create-pr --draft            # Create as draft PR
/create-pr --title "Add XGBoost model"  # Custom title
```

## Notes

- Always include experiment metrics in PR description
- Link to MLflow run for full details
- Request review from ML team members
