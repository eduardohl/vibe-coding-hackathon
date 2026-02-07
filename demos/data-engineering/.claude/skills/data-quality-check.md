---
name: data-quality-check
description: Automatically check data quality when writing to Delta tables
triggers:
  - data quality
  - check table
  - validate output
  - null check
  - schema validation
---

# Data Quality Check Skill

Automatically triggered when the user mentions data quality concerns.

## When to Activate

This skill activates when the user mentions:
- "data quality", "DQ", "quality check"
- "null check", "missing values"
- "schema validation", "schema drift"
- "validate the table", "check the output"

## Actions

### 1. Identify Target Table
- Determine which table needs checking
- Use context from conversation or ask if unclear
- Default: most recently written table

### 2. Run Quality Checks

Use Databricks MCP to execute these checks:

```sql
-- Row count check
SELECT COUNT(*) as row_count FROM {table};

-- Null check for key columns
SELECT
  SUM(CASE WHEN {column} IS NULL THEN 1 ELSE 0 END) as null_count,
  COUNT(*) as total_count,
  ROUND(SUM(CASE WHEN {column} IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as null_pct
FROM {table};

-- Value range check
SELECT
  MIN({numeric_column}) as min_val,
  MAX({numeric_column}) as max_val,
  AVG({numeric_column}) as avg_val
FROM {table};

-- Distinct value check
SELECT COUNT(DISTINCT {column}) as distinct_count
FROM {table};
```

### 3. Generate Report

Present findings in a clear format:

```
## Data Quality Report: {table}

### Summary
- Total Rows: X
- Quality Score: X/100

### Column Analysis
| Column | Nulls | Null % | Distinct | Min | Max |
|--------|-------|--------|----------|-----|-----|
| col1   | 0     | 0%     | 100      | 1   | 10  |

### Issues Found
- ⚠️ Warning: Column X has 5% null values
- ❌ Error: Column Y has values outside expected range

### Recommendations
- Consider adding data quality expectations in DLT
- Add null handling in transformation logic
```

## Example Interaction

```
User: Check the data quality of my output table

Claude: [Skill activates]
I'll run a comprehensive data quality check on your output table.

[Queries via MCP]

## Data Quality Report: hackathon_catalog.demo.daily_order_metrics

✅ All checks passed!

- Total Rows: 168
- No null values in key columns
- All values within expected ranges
...
```
