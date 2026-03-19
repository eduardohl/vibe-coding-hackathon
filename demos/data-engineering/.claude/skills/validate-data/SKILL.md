---
name: validate-data
description: Validate output data quality after a job run. Use when the user says "validate data", "check output", "verify the table", or wants to confirm job results.
---

# Validate Data Quality

Check the quality of data in the output tables after a job run.

## Steps

1. **Connect** to Databricks via MCP
   - Use the Databricks MCP to query tables

2. **Check** row counts
   - Query: `SELECT COUNT(*) FROM {catalog}.{schema}.{table}`
   - Verify row count is greater than 0

3. **Check** for nulls in key columns
   - Query null counts for critical columns
   - Flag any unexpected nulls

4. **Check** value ranges
   - Verify day_of_week is 0-6
   - Verify hour_of_day is 0-23
   - Verify numeric columns are positive

5. **Report** findings
   - Summarize data quality status
   - List any issues found
   - Suggest fixes if needed

## Usage

```
/validate-data                                        # Validate default table
/validate-data daily_order_metrics                    # Specific table
/validate-data {catalog}.{schema}.my_table            # Full path
```

## Default Table

`{catalog}.{schema}.daily_order_metrics` (uses catalog/schema from CLAUDE.md)
