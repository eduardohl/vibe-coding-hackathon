---
description: Run a DABs job and monitor its execution
---

# Run DABs Job

Execute a Databricks job defined in this bundle and monitor its progress.

## Steps

1. **Check** that the job is deployed
   - Verify the job exists in the target environment

2. **Run** the job
   - Execute: `databricks bundle run {job_name} --target {target}`
   - Default job: `daily_metrics_job`
   - Default target: `dev`

3. **Monitor** the run
   - Show the run URL in Databricks
   - Wait for completion or provide status updates

4. **Report** results
   - Show run duration
   - Show success/failure status
   - If failed, show error details

## Usage

```
/run-job                              # Run daily_metrics_job on dev
/run-job daily_metrics_job            # Explicit job name
/run-job daily_metrics_dlt            # Run the DLT pipeline
```

## Available Jobs

- `daily_metrics_job` - Standard PySpark ETL job
- `daily_metrics_dlt` - DLT pipeline job
