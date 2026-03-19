---
name: hyperparameter-tuning
description: Automatically triggered for hyperparameter optimization tasks. Use when the user mentions "hyperparameter", "optimize model", "grid search", "random search", or "bayesian optimization".
---

# Hyperparameter Tuning Skill

Automatically triggered when the user mentions hyperparameter optimization.

## When to Activate

This skill activates when the user mentions:
- "hyperparameter", "tune", "tuning"
- "optimize the model", "improve performance"
- "grid search", "random search"
- "bayesian optimization", "optuna"

## Actions

### 1. Assess Current State

- Check if a baseline model exists
- Review current hyperparameters
- Identify optimization target (RMSE, MAE, etc.)

### 2. Define Search Space

For XGBoost (default):
```python
param_space = {
    'learning_rate': [0.01, 0.05, 0.1, 0.15, 0.2],
    'max_depth': [3, 5, 7, 9, 11],
    'n_estimators': [100, 200, 300, 500],
    'min_child_weight': [1, 3, 5, 7],
    'subsample': [0.6, 0.7, 0.8, 0.9, 1.0],
    'colsample_bytree': [0.6, 0.7, 0.8, 0.9, 1.0],
    'reg_alpha': [0, 0.01, 0.1, 1],
    'reg_lambda': [0, 0.01, 0.1, 1]
}
```

### 3. Run Optimization

**Default Strategy: Random Search (10 trials)**

```python
import mlflow
from sklearn.model_selection import RandomizedSearchCV

with mlflow.start_run(run_name="hyperparameter_tuning"):
    # Log search configuration
    mlflow.log_param("search_type", "random")
    mlflow.log_param("n_trials", 10)

    for i, params in enumerate(param_samples):
        with mlflow.start_run(run_name=f"trial_{i}", nested=True):
            model = train_with_params(params)
            metrics = evaluate(model)
            mlflow.log_params(params)
            mlflow.log_metrics(metrics)
```

### 4. Report Results

```markdown
## Hyperparameter Tuning Results

### Best Configuration
| Parameter | Value |
|-----------|-------|
| learning_rate | 0.1 |
| max_depth | 6 |
| n_estimators | 300 |
| subsample | 0.8 |

### Performance Comparison
| Metric | Baseline | Tuned | Improvement |
|--------|----------|-------|-------------|
| Val RMSE | 0.95 | 0.82 | -14% |
| Test RMSE | 0.98 | 0.85 | -13% |

### Top 5 Trials
| Trial | learning_rate | max_depth | Val RMSE |
|-------|---------------|-----------|----------|
| 1 | 0.1 | 6 | 0.82 |
| 2 | 0.05 | 7 | 0.84 |
...

### MLflow Run IDs
- Parent: {parent_run_id}
- Best Trial: {best_trial_id}
```

## Example Interaction

```
User: Tune the model hyperparameters to improve RMSE

Claude: [Skill activates]
I'll run hyperparameter tuning with 10 random search trials.

Setting up search space for XGBoost:
- learning_rate: [0.01 - 0.2]
- max_depth: [3 - 11]
- n_estimators: [100 - 500]

Running trials with MLflow tracking...

Trial 1/10: learning_rate=0.15, max_depth=5 -> RMSE: 0.89
Trial 2/10: learning_rate=0.1, max_depth=6 -> RMSE: 0.82 (best so far)
...

## Results
Best configuration found:
- learning_rate: 0.1
- max_depth: 6
- Val RMSE: 0.82 (14% improvement over baseline)

Would you like me to train a final model with these parameters?
```
