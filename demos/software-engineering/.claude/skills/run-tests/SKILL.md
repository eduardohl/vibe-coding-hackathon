---
name: run-tests
description: Run the test suite and report results. Use when the user says "run tests", "test", "npm test", "run the tests", "check tests", or wants to execute the test suite.
---

# Run Tests

Execute the full test suite including unit tests and API tests.

## Steps

1. **Install dependencies** if needed
   - Check if `node_modules/` exists
   - Run `npm install` if missing

2. **Run** the test suite
   - Execute: `npm test`
   - If Jest is configured: `npx jest --verbose --coverage`

3. **Analyze** results
   - Count passing/failing tests
   - Check code coverage percentage
   - Identify any failing tests

4. **Report** findings
   - Show test summary (pass/fail counts)
   - Show coverage report (statements, branches, functions, lines)
   - List any failing tests with error details
   - Suggest fixes for failing tests

## Usage

```
/run-tests                       # Run all tests
/run-tests --coverage            # Run with coverage report
/run-tests server.test.js        # Run specific test file
```

## Test Categories

- **Unit tests** - Pure function tests, utility helpers
- **API tests** - HTTP endpoint tests with mocked database
- **Component tests** - React component rendering tests

## Coverage Targets

| Category | Target |
|----------|--------|
| Statements | > 70% |
| Branches | > 60% |
| Functions | > 70% |
| Lines | > 70% |
