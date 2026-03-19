---
name: deploy-app
description: Build and deploy the Databricks App. Use when the user says "deploy app", "deploy", "push to databricks apps", or wants to deploy the web application.
---

# Deploy Databricks App

Build the React frontend and deploy the full-stack app to Databricks Apps.

## Steps

1. **Install dependencies**
   - Run `npm install` in the app directory
   - Verify all dependencies resolve

2. **Run tests** before deploying
   - Execute `npm test` to verify nothing is broken
   - If tests fail, stop and report the failures

3. **Build** the frontend
   - Run `npm run build` to create the production bundle
   - Verify the `dist/` directory is created

4. **Lint** the code
   - Run `npx prettier --check .` and `npx eslint .`
   - Fix any issues before deploying

5. **Deploy** to Databricks Apps
   - Check if the app already exists: `databricks apps get {app_name}`
   - If it doesn't exist, create it: `databricks apps create --name {app_name}`
   - Sync local files to workspace: `databricks sync . /Workspace/Users/{user_email}/{app_name}`
   - Deploy: `databricks apps deploy {app_name} --source-code-path /Workspace/Users/{user_email}/{app_name}`

6. **Verify** deployment
   - Check app status: `databricks apps get {app_name}`
   - Provide the app URL for browser testing

## Usage

```
/deploy-app                      # Deploy with default app name
/deploy-app my-inventory-app     # Deploy with custom name
```

## Notes

- Always run tests before deploying
- The app.yaml file must be in the root of the app directory
- Lakebase resources are configured in app.yaml
- First deployment may take a few minutes to provision resources
