# Demo: Software Engineering (Java) with Claude Code

> **40 min** | Spring Boot + JUnit 5 + H2 | No cloud required | [Full Claude Code Docs](https://code.claude.com/docs/en/overview)
>
> **Focus:** Automated testing, code quality tooling, and teaching Claude proprietary libraries

---

## Quick Reference — Prompts to Type

| Step | Prompt | Feature Shown |
|------|--------|---------------|
| 0 | *Start Claude Code in `demos/software-engineering-java/`* | [CLAUDE.md](https://code.claude.com/docs/en/memory) |
| 1 | `Create a Spring Boot REST API for medical supply inventory...` *(see below)* | Code gen + [Hooks](https://code.claude.com/docs/en/hooks) |
| 2 | `What do you know about SupplyTrackSDK?` | [Skills](https://code.claude.com/docs/en/skills) (bundled docs) |
| 3 | `Add a POST /api/supplies/{sku}/reserve endpoint using SupplyTrackSDK...` *(see below)* | Code gen with proprietary library |
| 4 | `Write JUnit 5 tests for the controller and the SupplyTrackSDK integration` | Testing + [Hooks](https://code.claude.com/docs/en/hooks) |
| 5 | `/run-tests` | [Skills](https://code.claude.com/docs/en/skills) |
| 6 | `Delegate to the code-reviewer agent to review my code` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 7 | `Delegate to the security-auditor agent to check for vulnerabilities` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 8 | `Commit these changes` / *Press `Esc` twice* | Git + [Checkpoints](https://code.claude.com/docs/en/overview) |

---

## Prerequisites

> **First time?** Follow the [Setup Guide](../../SETUP.md) to install Claude Code (Java and Maven are the only other requirements).

1. Terminal open in `demos/software-engineering-java/`
2. Java 17+ installed (`java --version`)
3. Maven 3.8+ installed (`mvn --version`)
4. Fresh session: start `claude`, then type `/clear`

---

## Walkthrough

### Step 0: Start Claude Code

```bash
cd demos/software-engineering-java
claude .
```

> **Observe:** Claude reads the `CLAUDE.md` and knows the domain (medical supply inventory), the tech stack (Spring Boot + H2), and the available skills/agents. That's [CLAUDE.md](https://code.claude.com/docs/en/memory).

---

### Step 1: Scaffold the Spring Boot API

```
Create a Spring Boot REST API for medical supply inventory management:
- Entity: MedicalSupply with fields: sku, name, category, stockLevel, reorderPoint, expirationDate, lotNumber
- Full CRUD endpoints under /api/supplies
- H2 in-memory database with sample data (PPE, surgical instruments, pharmaceuticals)
- Global error handling with @ControllerAdvice
- Input validation on create/update

Structure as generated-inventory-api/ with standard Maven layout.
Don't write tests yet.
```

> **Observe:** (1) Claude generates a complete Spring Boot app — entity, repository, service, controller, config, and sample data. (2) Each `.java` file gets auto-formatted by the [PostToolUse hook](https://code.claude.com/docs/en/hooks). How many files did Claude create?

---

### Step 2: Teach Claude a Proprietary Library

```
What do you know about SupplyTrackSDK?
```

> **Observe:** Claude reads the bundled docs from `.claude/skills/supply-track-sdk/` — a library it was **never trained on**. It can now describe the API, the builder pattern, the methods, and the error handling. This is how you teach Claude your internal libraries using [Skills with bundled documentation](https://code.claude.com/docs/en/skills).

**Discuss:** This is the key insight for proprietary codebases. Bundle your internal library docs as skills and Claude can use them correctly.

---

### Step 3: Integrate the Proprietary SDK

```
Add a POST /api/supplies/{sku}/reserve endpoint that uses SupplyTrackSDK to:
1. Check real-time stock via getStockLevel()
2. Reserve items via reserveItems()
3. Return the reservation ID

Also add a GET /api/warehouses/capacity endpoint using getWarehouseCapacity().
Mock the SupplyTrackClient as a Spring bean since we don't have a real server.
```

> **Observe:** Claude writes code using the SDK's builder pattern, method signatures, and error types — all learned from the bundled docs. The code should match the API reference exactly.

---

### Step 4: Write Tests

```
Write JUnit 5 tests:
1. MockMvc tests for all controller endpoints (CRUD + reserve + capacity)
2. Mock the SupplyTrackClient with @MockitoBean
3. Test both success and error paths (404, 400, SDK failures)
```

> **Observe:** Claude generates tests using MockMvc, mocks the SDK correctly (matching the API from the docs), and covers edge cases. The hooks auto-format each test file. Notice the test names follow the convention from CLAUDE.md.

---

### Step 5: Run the Tests

```
/run-tests
```

> **Observe:** The [Skill](https://code.claude.com/docs/en/skills) runs `mvn test`, parses results, and reports pass/fail counts. You typed `/run-tests` instead of explaining what to do.

**Discuss:** What's the test coverage? What edge cases are missing?

---

### Step 6: Code Review with a Subagent

```
Delegate to the code-reviewer agent to review my code for quality, test coverage, and Spring Boot best practices
```

> **Observe:** The [subagent](https://code.claude.com/docs/en/sub-agents) reviews with its own checklist — Spring conventions, input validation, error handling, test quality. It runs in an isolated context. Do you agree with the findings?

---

### Step 7: Security Audit with a Subagent

```
Delegate to the security-auditor agent to check my API for vulnerabilities
```

> **Observe:** Another [subagent](https://code.claude.com/docs/en/sub-agents) checks for injection, missing validation, error leakage, and other OWASP issues. Each agent is a `.md` file with specialized instructions. What would you add?

---

### Step 8: Commit & Checkpoints

```
Commit these changes with a meaningful message
```

After the commit, try something experimental:

```
Add WebSocket support for real-time stock updates
```

Then press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot before every edit. Roll back the WebSocket experiment instantly without touching git.

**Bonus — compact a long conversation:**

```
/compact
```

---

> **Reflect with the group:** How does teaching Claude a proprietary library change what's possible? What internal tools or SDKs would you bundle as skills? How do subagents compare to your current code review process?

---

## Features Cheat Sheet

| Feature | What It Does | Where It Lives | Docs |
|---------|--------------|----------------|------|
| [CLAUDE.md](https://code.claude.com/docs/en/memory) | Project context, auto-loaded | `CLAUDE.md` | [Memory](https://code.claude.com/docs/en/memory) |
| [Skills](https://code.claude.com/docs/en/skills) | `/run-tests`, `/create-pr`, SupplyTrackSDK docs | `.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | Code reviewer, security auditor | `.claude/agents/` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| [Hooks](https://code.claude.com/docs/en/hooks) | Auto-format Java with google-java-format | `.claude/settings.json` | [Hooks](https://code.claude.com/docs/en/hooks) |
| [Checkpoints](https://code.claude.com/docs/en/overview) | `Esc+Esc` to rewind changes | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
