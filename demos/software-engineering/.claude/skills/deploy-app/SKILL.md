---
name: deploy-app
description: Build and deploy the Databricks App. Use when the user says "deploy app", "deploy", "push to databricks apps", or wants to deploy the web application.
---

# Deploy Databricks App

Deploy the Express.js app (plain HTML frontend) to Databricks Apps using DABs.

## Pre-flight

Confirm you know these values (they should already be in CLAUDE.md or the conversation):

| Value | Example | Where to find |
|-------|---------|---------------|
| **CLI profile** | `fevm-serverless-xb4o77` | User told you at session start |
| **App name** | `supply-chain-inventory` | Ask if not set |
| **User email** | `user@databricks.com` | `databricks current-user me -p {profile} --output json` |

**CRITICAL:** Always pass `-p {profile}` on every `databricks` command. Never use the default profile.

## Steps

### 1. Run tests

```bash
cd src/generated-app && npm test
```

Stop if tests fail. No build step needed — the app uses plain HTML served by Express.

### 2. Verify `app.yaml`

The `app.yaml` supports **only two fields**: `command` and `env`. No other fields are valid.

```yaml
command:
  - node
  - server.js
env:
  - name: DATABASE_URL
    valueFrom: lakebase-db
```

**Rules:**
- **NO `resources:` block** — resources are configured in `databricks.yml`, not `app.yaml`
- **NO `npm install` in command** — the platform auto-runs `npm install` when it detects `package.json`
- **NO `bash -c` wrapper** — the platform does not run commands in a shell, so env var substitution won't work. Use `command: ["node", "server.js"]`
- The `valueFrom` key must match a resource `name` from `databricks.yml`

### 3. Verify `databricks.yml`

The `databricks.yml` must be at the **root of the app directory** (`src/generated-app/databricks.yml`).

```yaml
bundle:
  name: {app_name}

resources:
  apps:
    app:
      name: {app_name}
      description: "Supply Chain Inventory Management"
      source_code_path: .
      resources:
        - name: lakebase-db
          postgres:
            branch: projects/{app_name}/branches/production
            database: databricks_postgres
            permission: CAN_CONNECT_AND_CREATE

targets:
  dev:
    default: true
```

**Key points:**
- `source_code_path: .` means "upload the bundle root directory"
- The Lakebase resource `name: lakebase-db` must match the `valueFrom` in `app.yaml`
- `postgres.branch` is `projects/{lakebase_project_name}/branches/production`
- `postgres.database` is `databricks_postgres` (the default database Lakebase creates)
- The resource key (`app`) is what you pass to `bundle run`
- No `sync.include` for `node_modules` — the platform handles dependency installation

### 4. Verify `.gitignore`

The app directory **must** have a `.gitignore` that excludes `node_modules/`. DABs respects `.gitignore` during sync, keeping uploads fast.

```gitignore
node_modules/
.env
coverage/
__tests__/
.bundle/
```

Without this, `bundle deploy` will try to upload thousands of `node_modules` files.

### 5. Create Lakebase project (if first deploy)

Check if the Lakebase project exists. If not, create it:

```bash
# Check if project exists
databricks api get /api/2.0/postgres/projects/{app_name} -p {profile} 2>/dev/null

# Create if needed
databricks api post '/api/2.0/postgres/projects?project_id={app_name}' \
  -p {profile} --json '{"display_name": "{app_name}"}'
```

Wait ~30 seconds for the project to become active before deploying.

### 6. Deploy via DABs

Run these commands from the app directory (`src/generated-app/`):

```bash
# Validate the bundle config
databricks bundle validate -p {profile}

# Deploy: uploads source files + creates/updates the app resource
databricks bundle deploy -p {profile}

# Run: triggers actual deployment to compute (installs deps + starts the app)
databricks bundle run app -p {profile}
```

**IMPORTANT:** `bundle deploy` alone does NOT start the app — it only uploads files and creates the resource. You must also run `bundle run app` to trigger the actual deployment.

### 7. Verify deployment

```bash
# Check app status (look for compute_status: ACTIVE, deployment state: SUCCEEDED)
databricks apps get {app_name} -p {profile}
```

The app URL follows the pattern: `https://{app_name}-{workspace_id}.{region}.databricksapps.com`

Provide the URL to the user when deployment succeeds.

## Fallback: Manual deploy (if DABs has issues)

If `bundle deploy` hangs or fails, use the staging directory pattern:

```bash
# 1. Create clean staging dir with only source files (no node_modules)
STAGING_DIR="/tmp/{app_name}-deploy"
rm -rf "$STAGING_DIR" && mkdir -p "$STAGING_DIR/public"
cp server.js package.json package-lock.json app.yaml "$STAGING_DIR/" 2>/dev/null; true
cp public/* "$STAGING_DIR/public/" 2>/dev/null; true
# Copy any other source files (e.g., supplytrack-mock.js)
cp *.js "$STAGING_DIR/" 2>/dev/null; true

# 2. Upload to workspace
databricks workspace import-dir "$STAGING_DIR" \
  "/Workspace/Users/{user_email}/apps/{app_name}" \
  --overwrite -p {profile}

# 3. Create app if needed
databricks apps create {app_name} --description "Supply Chain Inventory" -p {profile} 2>/dev/null; true

# 4. Deploy
databricks apps deploy {app_name} \
  --source-code-path "/Workspace/Users/{user_email}/apps/{app_name}" \
  -p {profile}
```

After manual deploy, add the Lakebase resource via the Databricks Apps UI (Resources tab).

## Usage

```
/deploy-app                      # Deploy with default app name
/deploy-app my-inventory-app     # Deploy with custom name
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `bundle deploy` hangs | Likely uploading `node_modules/`. Check `.gitignore` excludes it |
| Deploy lock error | Add `--force-lock` to `bundle deploy` |
| `Cannot find module 'express'` | The platform should auto-install from `package.json`. Verify `package.json` is present in the deployed files |
| App crashes immediately | Check that `server.js` listens on `process.env.PORT \|\| 8000` and binds to `0.0.0.0` |
| `unknown flag: --name` | App name is positional: `databricks apps create {name}`, not `--name {name}` |
| Wrong workspace | Verify `-p {profile}` is on every command |
| 502 Bad Gateway | Server must bind to `0.0.0.0`, not `localhost`. Port must use `process.env.PORT` |
| Lakebase connection fails | Verify Lakebase project exists and resource is bound in `databricks.yml`. Check PG* env vars are set |
| 100 app limit | Delete old apps: `databricks apps delete {old-name} -p {profile}` |
| `bundle run` says "already running" | The app is already deployed. Use `databricks apps deploy` directly to redeploy |
