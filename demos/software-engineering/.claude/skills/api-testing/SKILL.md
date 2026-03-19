---
name: api-testing
description: Automatically generate and run API endpoint tests. Use when the user mentions "test api", "test endpoint", "integration test", "test route", "api test", "test the server", or "test the backend".
---

# API Testing Skill

Automatically triggered when the user mentions testing API endpoints.

## When to Activate

This skill activates when the user mentions:
- "test api", "test the API", "API tests"
- "test endpoint", "test routes"
- "integration test"
- "test the server", "test the backend"

## Actions

### 1. Identify Endpoints
- Scan the Express.js server file for `app.get()`, `app.post()`, `app.put()`, `app.delete()` routes
- Identify request parameters, body shapes, and expected responses

### 2. Generate Tests
- Create a test file using Supertest for each endpoint
- Mock the database connection with `jest.mock('pg')`
- Test both success and error paths (400, 404, 500)
- Include tests for any SupplyTrackSDK integration endpoints

### 3. Run and Report
- Execute `npm test` and present results
- Report pass/fail counts, coverage, and endpoint coverage table
