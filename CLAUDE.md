# CLAUDE.md — Global Agent OS
> Loaded in every Claude Code session. Last updated: 2026-05-01.

## Identity

Operator: **Parv Patodia** — MS AI @ Northeastern Silicon Valley (GPA 3.85, grad May 2027)
Domain focus: ML/robotics research (Diffusion Policy, pose estimation), AI product engineering, job search automation
Hardware: M1 MacBook Pro (dev) + HPC A100 cluster (training, SLURM)
GitHub: parvpatodia | Visa: F-1 (CPT/OPT available)

---

## Operating Protocol

**Before every response:**
1. Load project context: read `CLAUDE.md` and `context.md` in the working directory if they exist
2. Identify which skill applies to the task — route to it
3. Check `GOALS.md` or `TODO.md` if touching feature work
4. Use caveman technique for all internal operations (see `/efficiency`)
5. End every session with `learn summary`

**Decision hierarchy:**
1. Is there a failing test? Fix it first. Nothing else.
2. Is there a spec? Follow it. Don't improvise architecture.
3. Is this a bug fix? Fix only the bug. Refactor separately.
4. Is this a new feature? Write spec → test → implement.

---

## Hard Rules (non-negotiable)

- **NEVER auto-submit** applications or forms. Fill + stop. User clicks submit.
- **NEVER fabricate** resume content. Tailor = select + reframe real experience.
- **NEVER commit** without running tests. `npm test` / `pytest` / `cargo test` first.
- **NEVER add** features, abstractions, or error handling beyond what's asked.
- **NEVER use** em dashes, "passionate about", "excited to", or AI filler phrases in cover letters.
- **ALWAYS explain** design decisions with `// WHY:` comments in non-obvious code.
- **ALWAYS log** every application to `data/applications.json`.
- **ALWAYS use** structured data (JSON/YAML), not prose, for internal operations.
- **ALWAYS run** `learn summary` at session end.

---

## Skill Routing

| User says... | Skill |
|---|---|
| scan / find jobs | `/scan` |
| evaluate / score job | `/evaluate` |
| tailor resume / cover letter | `/tailor` |
| apply / fill form | `/apply` |
| track / stats | `/track` |
| audit code / product | `/audit` |
| research efficiency / caveman | `/efficiency` |
| write tests / TDD | `/testing` |
| optimize performance | `/performance` |
| refactor | `/refactoring` |
| security review | `/security` |
| learn / explain / reconstruct | `/learn` |
| research papers / arXiv / GitHub | `/research` |
| write spec / design document | `/spec` |
| debug / diagnose / reproduce | `/debug` |
| deploy / ship / push | `/deploy` |
| run experiment / train model | `/experiment` |
| SLURM / HPC / cluster | `/slurm` |
| diffusion policy / robot / SO-101 | `/robot` |
| background job / automate | `/agent` |
| job search command center | `/career-ops` |

---

## OOP Principles (enforced in all code)

- **S**: One class, one responsibility. Scanner discovers. Evaluator scores.
- **O**: Abstract base classes open for extension, closed for modification.
- **L**: Subclasses substitutable for base without breaking pipeline.
- **I**: Scanner doesn't import PDF generation. Tailor doesn't import form filling.
- **D**: Pipeline orchestration depends on abstractions (interfaces), not concrete classes.

---

## TDD Workflow

```
1. Write failing test (describes expected behavior)
2. Run test → confirm it fails for the RIGHT reason
3. Implement minimum code to pass
4. Refactor with tests green
5. Commit only when all tests pass
```

Never write code before the test. Never commit failing tests. Never skip step 2.

---

## Caveman Technique (token minimization)

```
BAD:  "Could you please search for machine learning intern positions..."
GOOD: "scan linkedin ml intern bayarea 48h"

BAD:  "Please evaluate this JD against my resume..."
GOOD: "eval jd#42"
```

Rules: no pleasantries, return JSON not prose, use IDs not full titles, batch operations.
See `/efficiency` for full reference.

---

## Git Workflow

```
main        ← stable, tests always pass
feat/*      ← feature branches (one concern per branch)
fix/*       ← bug fixes
exp/*       ← experiments (ML runs, prototypes — not merged to main)
```

Commit message format: `type(scope): description`
Types: feat | fix | refactor | test | docs | chore | exp

---

## MCP Connectors (user-scope, re-add after fresh install)

```bash
GITHUB_TOKEN=$(gh auth token)
claude mcp add -s user -e "GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_TOKEN" -- github npx -y @modelcontextprotocol/server-github
claude mcp add -s user filesystem -- npx -y @modelcontextprotocol/server-filesystem /Users/parvpatodia
claude mcp add -s user memory -- npx -y @modelcontextprotocol/server-memory
```

---

## Session End Checklist

Before closing any session:
- [ ] All tests passing
- [ ] All new code has `// WHY:` comments on non-obvious decisions
- [ ] `data/applications.json` updated if any applications were processed
- [ ] Git status clean (or staged with clear commit message ready)
- [ ] Run `learn summary` → 3 sentences: BUILT / UNDERSTAND / STUDY
