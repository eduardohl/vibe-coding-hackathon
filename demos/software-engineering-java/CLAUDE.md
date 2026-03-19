# Software Engineering Demo — Java

## Overview

Build a **Supply Chain Inventory** REST API using Spring Boot and H2, then teach Claude a proprietary SDK it was never trained on.

**Problem:** Build a Medical Supply Inventory Service
**Stack:** Spring Boot + JUnit 5 + H2 (in-memory)
**Deployment:** Local only — no cloud, no tokens

**This demo showcases Claude Code features including:**
- Custom skills (`/run-tests`, `/create-pr`)
- Skills with bundled documentation (SupplyTrackSDK)
- Specialized subagents (code reviewer, security auditor)
- Hooks for automatic Java formatting (google-java-format)
- Zero external dependencies beyond Java + Maven

## Rules

- **ONLY use local skills** from this project's `.claude/skills/` directory — do NOT use `fe-databricks-tools`, `fe-workflows`, or any other external plugin skills. This demo must be self-contained.
- ALWAYS check `.claude/skills/` directory before implementing any task manually
- Read the skill file and follow its instructions exactly before writing any code
- **IMPORTANT:** When creating new files, use the `generated-` prefix for top-level directories (e.g., `generated-inventory-api/`)

## Environment

- Java 17+
- Maven 3.8+
- No cloud services, no MCP servers, no tokens
- All code runs locally with H2 in-memory database

## Domain: Medical Supply Chain

This app manages medical supply inventory for hospital distribution centers:

| Entity | Description | Key Fields |
|--------|-------------|------------|
| `MedicalSupply` | Inventory item | sku, name, category, stockLevel, reorderPoint, expirationDate, lotNumber |
| `Warehouse` | Distribution center | warehouseId, name, region, capacity, utilization |

**Categories:** PPE, Surgical Instruments, Pharmaceuticals, Lab Supplies, Diagnostic Equipment

## Claude Code Features

### Custom Skills

| Skill | Triggers On |
|-------|-------------|
| `/run-tests` | User invokes `/run-tests` |
| `/create-pr` | User invokes `/create-pr` |
| `supply-track-sdk` | "SupplyTrackSDK", "supply track", "warehouse SDK", "inventory SDK" |

### Subagents (Specialists)

| Agent | Purpose |
|-------|---------|
| `code-reviewer` | Review code for quality, test coverage, and Spring Boot best practices |
| `security-auditor` | Audit code for OWASP vulnerabilities (injection, input validation, error handling) |

### Hooks (Automation)

| Hook | Trigger | Action |
|------|---------|--------|
| PostToolUse:Write/Edit | After writing or editing .java files | Auto-format with google-java-format |

## SupplyTrackSDK

A fictional proprietary SDK for real-time warehouse inventory operations. Claude has **never seen this library** — it learns it from the bundled docs in `.claude/skills/supply-track-sdk/`.

**Demo flow:**
1. Ask: "What do you know about SupplyTrackSDK?" — Claude reads the bundled docs
2. Ask Claude to add an inventory endpoint using the SDK — it writes correct code

See `.claude/skills/supply-track-sdk/api-reference.md` for the full API.

## Coding Standards

### Java
- Use records for DTOs, classes for entities
- Constructor injection (no field injection)
- `Optional` for nullable returns — never return null
- Meaningful names, no abbreviations

### Spring Boot
- `@RestController` with `@RequestMapping` prefix
- `@Valid` on request bodies, `@PathVariable` / `@RequestParam` with validation
- `ResponseEntity<>` for all controller returns
- `@ControllerAdvice` for global error handling

### Testing
- JUnit 5 + MockMvc for controller tests
- `@MockitoBean` for service dependencies
- Test both happy path and error cases
- Descriptive test names (`shouldReturn404WhenSupplyNotFound`)

## File Structure

```
├── CLAUDE.md                    # This file
├── README.md                    # Demo script
├── .gitignore                   # Ignores generated files
├── .claude/
│   ├── settings.json            # Hooks and permissions
│   ├── agents/                  # Specialized subagents
│   │   ├── code-reviewer.md
│   │   └── security-auditor.md
│   └── skills/
│       ├── run-tests/SKILL.md
│       ├── create-pr/SKILL.md
│       └── supply-track-sdk/    # Proprietary SDK docs
│           ├── SKILL.md
│           ├── api-reference.md
│           └── examples.md
└── src/
    └── generated-*/             # Created during demo by Claude
```

> **Note:** Files with `generated-` prefix are created live during the demo and are gitignored.
