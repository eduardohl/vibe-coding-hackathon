---
description: Train a model with MLflow logging
---

# Train Model

Train a machine learning model with proper MLflow experiment tracking.

## Steps

1. **Set up MLflow experiment**
   - Use the experiment name from CLAUDE.md or user input
   - Create experiment if it doesn't exist

2. **Prepare data**
   - Load data from specified source
   - Apply preprocessing from `src/preprocessing.py`
   - Split into train/validation/test sets

3. **Train the model**
   - Use XGBoost (or specified model type)
   - Log all hyperparameters to MLflow
   - Track training progress

4. **Log results to MLflow**
   - Log metrics: RMSE, MAE, R2
   - Log model artifact
   - Log feature importance
   - Add tags for experiment organization

5. **Report results**
   - Show training metrics
   - Provide MLflow run ID
   - Suggest next steps

## Usage

```
/train                    # Train with default settings
/train --sample 0.1       # Train on 10% sample
/train --model lightgbm   # Use LightGBM instead
```

## Notes

- Always use time-based splits for time series data
- Log-transform skewed targets for better RMSE
- Sample data for quick iterations, full data for final models
