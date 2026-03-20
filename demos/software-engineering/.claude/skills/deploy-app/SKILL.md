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

### 2. Ensure `app.yaml` has the right command

The app.yaml `command` MUST run `npm install` before starting the server. This is how dependencies get installed at deploy time — we do NOT sync `node_modules/`.

```yaml
command:
  - "bash"
  - "-c"
  - "npm install --production && node server.js"
```

If the command is just `["node", "server.js"]`, update it to the above. Without this, the app will crash with "Cannot find module 'express'" at runtime.

### 3. Create `.databricksignore`

Create this file in the app root. It controls what `databricks sync` uploads:

```
.git/
.env
*.log
.DS_Store
__tests__/
coverage/
node_modules/
```

**Why exclude `node_modules/`:** The app installs its own deps via the `npm install` command above. Syncing `node_modules/` would be slow (thousands of files) and fails anyway because `databricks sync` also honors `.gitignore`.

### 4. Create the app (if first deploy)

```bash
# Check if app exists
databricks apps get {app_name} -p {profile} 2>&1

# Create if needed (app name is positional, not a flag)
databricks apps create {app_name} --description "Supply Chain Inventory" -p {profile}
```

### 5. Sync source files to workspace

```bash
databricks sync . "/Workspace/Users/{user_email}/{app_name}" -p {profile} --watch=false
```

This syncs only source files (server.js, public/, package.json, app.yaml) — fast because no `node_modules/`.

### 6. Deploy

```bash
databricks apps deploy {app_name} \
  --source-code-path "/Workspace/Users/{user_email}/{app_name}" \
  -p {profile}
```

### 7. Wait and verify

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
| `unknown flag: --name` | App name is positional: `databricks apps create {name}`, not `--name {name}` |
| Wrong workspace | Verify `-p {profile}` is on every command |
| 300 app limit | Delete old apps: `databricks apps delete {old-name} -p {profile}` |
| App starts but DB errors | Check Lakebase resource in `app.yaml` and verify DB was created |
| Sync warning about .git | Harmless — `databricks sync` just can't find a `.git` dir in the app folder |
