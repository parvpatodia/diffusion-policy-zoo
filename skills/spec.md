---
name: spec
description: Write a machine-readable spec before writing code. No spec = no implementation.
user_invocable: true
args: type
---

# spec — Spec-Driven Development

## The Rule
**No implementation without a spec.**

## Args
- `new [project/module]` → write full architecture spec
- `update [spec_file]` → update with new decisions
- `review` → audit codebase against spec (find drift)

## Spec Template

```markdown
# [Module] Spec
**Author:** Parv Patodia | **Date:** [date] | **Status:** Draft | Approved | Implemented

## 1. Problem Statement
[1-3 sentences: problem, for whom, at what scale]

## 2. Decision Log
| Decision | Alternatives | Rationale |
|---|---|---|

## 3. Architecture
[Directory tree or module diagram]

## 4. OOP Design
- Classes and single responsibilities
- Abstract base classes and subclass contracts

## 5. Interface Contracts
[Inputs, outputs, invariants per public class/function]

## 6. TDD Plan
[Test files to write first, what each verifies]

## 7. Token/Performance Budget
[Token cost per operation, latency targets]

## 8. Non-Negotiable Constraints
[Hard rules, with reasons]

## 9. Execution Plan
[Session-sized chunks: 45-90 min each]
```

## Spec Quality Checklist
- [ ] Problem stated in terms of needs, not implementation
- [ ] Every decision has alternatives considered
- [ ] Interface contracts specific enough to write tests from
- [ ] Execution plan is session-sized
- [ ] Token budget estimated before writing code
