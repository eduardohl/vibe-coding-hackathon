# Workshop Permissions Required

Databricks permissions required for workshop participants across all three demo tracks (Data Engineering, Data Science, Software Engineering).

## Compute

- Serverless compute access (or a shared cluster DBR 14.3+)

## Unity Catalog

- A catalog with write access (ideally one shared catalog for the workshop)
- Ability to create schemas, tables, and models within that catalog

## Workspace

- Upload notebooks and create files in their user folder
- Create and run Jobs (Lakeflow)
- Create MLflow experiments
- Create and deploy Databricks Apps
- Access to Lakebase (Postgres-compatible database)

## Authentication & Tooling

- Personal Access Token (PAT) or OAuth — for Databricks CLI and MCP
- Databricks CLI installed and configured
- GitHub PAT with `repo` scope — for PR workflows via MCP

## Recommended Setup

Give each participant/team a permissive role on a dedicated workshop workspace + a shared catalog where each team gets their own schema (`team_{name}`). This avoids permission debugging during the session.
