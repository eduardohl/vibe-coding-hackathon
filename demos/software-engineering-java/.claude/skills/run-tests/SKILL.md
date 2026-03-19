---
name: run-tests
description: Run the Maven test suite and report results. Use when the user says "run tests", "test", "mvn test", "run the tests", or wants to execute the test suite.
---

# Run Tests

Execute the full test suite with Maven.

## Steps

1. **Find** the project directory
   - Look for `pom.xml` in the generated app directory

2. **Run** the test suite
   - Execute: `mvn test` in the project directory
   - For verbose output: `mvn test -Dsurefire.useFile=false`

3. **Analyze** results
   - Count passing/failing tests
   - Identify any failing tests with stack traces
   - Check for compilation errors

4. **Report** findings
   - Show test summary (pass/fail counts)
   - List any failing tests with error details
   - Suggest fixes for failures

## Usage

```
/run-tests                       # Run all tests
/run-tests -Dtest=SupplyControllerTest  # Run specific test class
```
