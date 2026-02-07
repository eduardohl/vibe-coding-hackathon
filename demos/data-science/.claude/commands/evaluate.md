---
description: Evaluate model performance and generate reports
---

# Evaluate Model

Evaluate a trained model's performance with comprehensive metrics and visualizations.

## Steps

1. **Load the model**
   - Use MLflow run ID or latest run
   - Load model and test data

2. **Generate predictions**
   - Run inference on test set
   - Calculate residuals

3. **Compute metrics**
   - RMSE (Root Mean Square Error)
   - MAE (Mean Absolute Error)
   - R2 (Coefficient of Determination)
   - MAPE (Mean Absolute Percentage Error)

4. **Analyze performance**
   - Feature importance ranking
   - Error distribution analysis
   - Performance by segment (if applicable)

5. **Generate report**
   - Summary metrics table
   - Comparison with baseline/previous models
   - Recommendations for improvement

## Usage

```
/evaluate                    # Evaluate latest run
/evaluate run_id=abc123      # Evaluate specific run
/evaluate --compare baseline # Compare with baseline
```

## Output Format

```markdown
## Model Evaluation Report

### Metrics
| Metric | Value | vs Baseline |
|--------|-------|-------------|
| RMSE   | 0.85  | -15%        |
| MAE    | 0.62  | -12%        |
| R2     | 0.72  | +8%         |

### Top Features
1. feature_a (importance: 0.25)
2. feature_b (importance: 0.18)
...

### Recommendations
- Consider adding interaction features
- Try regularization to reduce overfitting
```
