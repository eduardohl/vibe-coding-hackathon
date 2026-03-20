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

### 1. Verify tests pass

```bash
cd src/generated-app
npm install
npm test          # Stop if failures
```

No build step needed — the app uses plain HTML served by Express.

### 2. Ensure `app.yaml` is correct

The app.yaml **must** have these properties:

```yaml
command:
  - "bash"
  - "-c"
  - "npm install --production && node server.js"
resources:
  - name: lakebase-db
    type: lakebase
    config:
      database: {db_name}
env:
  - name: DATABASE_URL
    valueFrom: lakebase-db
```

**Why `npm install` in command:** We do NOT upload `node_modules/` — deps are installed at deploy time by the platform. Without this, the app crashes with "Cannot find module 'express'".

Also verify `server.js` listens on `process.env.PORT || 8080` — Databricks Apps injects the `PORT` env var.

### 3. Create the app (if first deploy)

```bash
# Check if app exists
databricks apps get {app_name} -p {profile} 2>&1

# Create if needed (app name is positional, not a flag)
databricks apps create {app_name} --description "Supply Chain Inventory" -p {profile}
```

### 4. Upload source files via staging directory

**Do NOT use `databricks sync` or `databricks workspace import-dir` directly on the app folder** — both will try to upload `node_modules/` (thousands of files, extremely slow). Instead, use a staging directory with only the files the app needs:

```bash
# Create clean staging dir
STAGING_DIR="/tmp/{app_name}-deploy"
rm -rf "$STAGING_DIR" && mkdir -p "$STAGING_DIR" "$STAGING_DIR/public"

# Copy only what the app needs at runtime
cp src/generated-app/server.js "$STAGING_DIR/"
cp src/generated-app/package.json "$STAGING_DIR/"
cp src/generated-app/package-lock.json "$STAGING_DIR/" 2>/dev/null || true
cp src/generated-app/app.yaml "$STAGING_DIR/"
cp src/generated-app/public/* "$STAGING_DIR/public/"

# Upload to workspace (~5-10 files, takes seconds)
databricks workspace import-dir "$STAGING_DIR" \
  "/Workspace/Users/{user_email}/{app_name}" \
  --overwrite -p {profile}
```

**Why staging?** This pattern (from Databricks' own ai-dev-kit) guarantees only source files are uploaded — no `node_modules/`, no `__tests__/`, no `.git/`. Upload takes seconds, not minutes.

### 5. Deploy

```bash
databricks apps deploy {app_name} \
  --source-code-path "/Workspace/Users/{user_email}/{app_name}" \
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
| `Cannot find module 'express'` | app.yaml command must include `npm install --production &&` before `node server.js` |
| Upload takes forever | You're uploading `node_modules/`. Use the staging directory pattern in Step 4 |
| `unknown flag: --name` | App name is positional: `databricks apps create {name}`, not `--name {name}` |
| Wrong workspace | Verify `-p {profile}` is on every command |
| 300 app limit | Delete old apps: `databricks apps delete {old-name} -p {profile}` |
| App starts but DB errors | Check Lakebase resource in `app.yaml` and verify DB was created |
| Port mismatch | `server.js` must use `process.env.PORT \|\| 8080` — Databricks injects PORT |
