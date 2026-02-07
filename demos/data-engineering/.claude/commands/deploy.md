---
description: Deploy the DABs bundle to a target environment
---

# Deploy DABs Bundle

Deploy this Databricks Asset Bundle to the specified target.

## Steps

1. **Validate** the bundle configuration first
   - Run `databricks bundle validate`
   - If validation fails, show the errors and stop

2. **Deploy** to the target environment
   - Default target is `dev` unless specified
   - Run `databricks bundle deploy --target {target}`

3. **Verify** deployment succeeded
   - Show the deployed resources (jobs, pipelines)
   - Provide the Databricks workspace URL to view the job

## Usage

```
/deploy           # Deploy to dev (default)
/deploy staging   # Deploy to staging
/deploy prod      # Deploy to production
```

## Notes

- Always validate before deploying
- The dev target is the default and safest for testing
- Production deployments require service principal configuration
