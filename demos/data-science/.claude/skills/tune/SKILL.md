---
name: tune
description: Run hyperparameter tuning with MLflow tracking. Use when the user says "tune", "tune hyperparameters", "run tuning trials", "optimize hyperparameters", or wants to search for better model parameters.
---

# Hyperparameter Tuning

Run automated hyperparameter search with MLflow experiment tracking.

## Steps

1. **Define search space**
   - learning_rate: [0.01, 0.05, 0.1, 0.2]
   - max_depth: [3, 5, 7, 9]
   - n_estimators: [100, 200, 500]
   - subsample: [0.7, 0.8, 0.9, 1.0]

2. **Set up MLflow tracking**
   - Create parent run for tuning session
   - Each trial is a nested run

3. **Run trials**
   - Default: 10 trials (configurable)
   - Log all hyperparameters and metrics
   - Track best result so far

4. **Report results**
   - Best hyperparameters found
   - Performance improvement over default
   - MLflow comparison link

## Usage

```
/tune                     # Run 10 trials with defaults
/tune --trials 20         # Run 20 trials
/tune --target rmse       # Optimize for RMSE (default)
/tune --target mae        # Optimize for MAE
```

## Search Strategies

**Grid Search (default for small spaces):**
- Exhaustive search over parameter grid
- Guaranteed to find best in grid

**Random Search (for larger spaces):**
- Sample randomly from distributions
- Often finds good solutions faster

**Bayesian Optimization (for expensive evaluations):**
- Uses past results to guide search
- Most efficient for limited budgets

## Notes

- Use small sample for tuning, full data for final training
- Log all trials for reproducibility
- Consider early stopping to save time
