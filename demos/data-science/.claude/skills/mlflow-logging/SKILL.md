---
name: mlflow-logging
description: Ensures proper MLflow logging for all ML experiments. Use when the user mentions "mlflow", "log experiment", "track experiment", "experiment tracking", "log metrics", or "log model".
---

# MLflow Logging Skill

Ensures all ML experiments are properly tracked in MLflow.

## When to Activate

This skill activates when:
- User trains a model
- User mentions "mlflow", "log", "track"
- User runs experiments without explicit logging

## Standard Logging Requirements

### Every Run Must Log:

**1. Parameters (log_params)**
```python
mlflow.log_params({
    # Model hyperparameters
    'learning_rate': 0.1,
    'max_depth': 6,
    'n_estimators': 200,

    # Data parameters
    'train_size': len(train_df),
    'feature_count': len(features),
    'target_transform': 'log1p',

    # Preprocessing
    'scaler': 'StandardScaler',
    'encoding': 'target_encoding'
})
```

**2. Metrics (log_metrics)**
```python
mlflow.log_metrics({
    # Training metrics
    'train_rmse': train_rmse,
    'train_mae': train_mae,
    'train_r2': train_r2,

    # Validation metrics
    'val_rmse': val_rmse,
    'val_mae': val_mae,
    'val_r2': val_r2,

    # Test metrics
    'test_rmse': test_rmse,
    'test_mae': test_mae,
    'test_r2': test_r2
})
```

**3. Tags (set_tags)**
```python
mlflow.set_tags({
    'model_type': 'xgboost',
    'problem_type': 'regression',
    'data_version': 'v1.0',
    'owner': username,
    'env': 'dev'
})
```

**4. Artifacts (log_artifact)**
```python
# Feature importance
mlflow.log_artifact('feature_importance.csv')

# Model
mlflow.xgboost.log_model(model, 'model')

# Plots (optional)
mlflow.log_artifact('residual_plot.png')
```

## Experiment Setup Template

```python
import mlflow

# Get username for experiment path
username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()

# Set experiment
experiment_name = f"/Users/{username}/hackathon-demand"
mlflow.set_experiment(experiment_name)

# Start run with descriptive name
with mlflow.start_run(run_name="xgboost_v1_log_target"):
    # Log everything
    mlflow.log_params(params)

    # Train model
    model = train_model(params)

    # Log metrics
    metrics = evaluate_model(model)
    mlflow.log_metrics(metrics)

    # Log model
    mlflow.xgboost.log_model(model, "model")

    # Log tags
    mlflow.set_tags({
        'model_type': 'xgboost',
        'feature_version': 'v2'
    })

    print(f"Run ID: {mlflow.active_run().info.run_id}")
```

## Validation Checks

Before completing a training run, verify:

- [ ] Experiment name follows convention
- [ ] All hyperparameters logged
- [ ] Train/val/test metrics logged
- [ ] Model artifact saved
- [ ] Tags include model_type and owner
- [ ] Run name is descriptive

## Example Interaction

```
User: Train an XGBoost model on the demand data

Claude: [Skill activates]
I'll train the model with proper MLflow tracking.

Setting up MLflow experiment: /Users/{user}/hackathon-demand

Starting run: xgboost_baseline_v1
- Logging parameters: learning_rate=0.1, max_depth=6, n_estimators=200
- Training model...
- Logging metrics: train_rmse=0.65, val_rmse=0.82, test_rmse=0.85
- Logging model artifact
- Adding tags: model_type=xgboost, problem_type=regression

Run completed! Run ID: abc123xyz

View in MLflow UI: [link to experiment]
```
