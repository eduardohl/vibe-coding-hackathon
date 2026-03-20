---
name: deploy-app
description: Build and deploy the Databricks App. Use when the user says "deploy app", "deploy", "push to databricks apps", or wants to deploy the web application.
---

# Deploy Databricks App

Deploy the Express.js app (plain HTML frontend) to Databricks Apps.

## Pre-flight

Before anything, confirm you know these values (they should already be in CLAUDE.md or the conversation):

| Value | Example | Where to find |
|-------|---------|---------------|
| **CLI profile** | `fevm-serverless-xb4o77` | User told you at session start |
| **App name** | `supply-chain-inventory` | Ask if not set |
| **User email** | `user@databricks.com` | `databricks current-user me -p {profile} --output json` |

**CRITICAL:** Always pass `-p {profile}` on every `databricks` command. Never use the default profile.

## Steps

### 1. Install and test

```bash
cd src/generated-app
npm install
npm test          # Stop if failures
```

No build step needed — the app uses plain HTML served by Express.

### 2. Create `.databricksignore`

Create this file in the app root to avoid syncing unnecessary files:

```
.git/
.env
*.log
.DS_Store
__tests__/
coverage/
```

**Note:** Do NOT exclude `node_modules/` — the app needs its dependencies at runtime. With a minimal dependency set (express, pg, helmet, cors), sync is fast.

### 3. Create the app (if first deploy)

```bash
# Check if app exists
databricks apps get {app_name} -p {profile} 2>&1

# Create if needed (no --name flag — app name is positional)
databricks apps create {app_name} --description "Supply Chain Inventory" -p {profile}
```

### 4. Sync files to workspace

```bash
databricks sync . /Workspace/Users/{user_email}/{app_name} -p {profile} --watch=false
```

With minimal dependencies (no React/Vite), this should complete in under a minute.

### 5. Deploy

```bash
databricks apps deploy {app_name} \
  --source-code-path /Workspace/Users/{user_email}/{app_name} \
  -p {profile}
```

### 6. Wait and verify

```bash
# Poll status (first deploy takes 2-5 minutes)
databricks apps get {app_name} -p {profile}

# Check logs if something looks wrong
databricks apps logs {app_name} -p {profile}
```

Provide the app URL when deployment completes.

## Usage

```
/deploy-app                      # Deploy with default app name
/deploy-app my-inventory-app     # Deploy with custom name
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `unknown flag: --name` | App name is positional: `databricks apps create {name}`, not `--name {name}` |
| Sync takes forever | Check that the app has minimal deps (no React/Vite) |
| Wrong workspace | Verify `-p {profile}` is on every command |
| 300 app limit | Delete old apps: `databricks apps delete {old-name} -p {profile}` |
| App starts but DB errors | Check Lakebase resource in `app.yaml` and verify DB was created |
