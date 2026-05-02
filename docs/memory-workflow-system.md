---
name: Global Workflow System
description: The 21-skill Claude Code workflow system — locations, MCP connectors, architecture decisions
type: project
originSessionId: 311796ae-39cb-4d66-8c38-58fcc55fb149
---
Built 2026-05-01. Reconstructed from deleted session `71166b16` (Apr 17-18 "Build Phase 3" session).

## Global Agent OS
`~/.claude/CLAUDE.md` — universal agent OS loaded in every project

## 21 Global Skills
Location: `~/.claude/skills/`

| # | Skill | Purpose |
|---|---|---|
| 1 | agent | Background automation, recurring tasks, multi-agent pipelines |
| 2 | apply | Form filling (NEVER auto-submit) via Playwright |
| 3 | audit | Code quality (PG/Musk lens) + product effectiveness (Naval/Hassabis lens) |
| 4 | career-ops | Job search command center router |
| 5 | debug | Systematic debugging: reproduce→isolate→hypothesize→verify→fix |
| 6 | deploy | Fly.io, Vercel, Docker, HPC deployment with pre-flight checks |
| 7 | efficiency | Caveman technique, token budgets, caching rules |
| 8 | evaluate | Job-resume fit scoring (weighted formula) |
| 9 | experiment | ML experiment tracking, checkpointing, comparison |
| 10 | learn | Learning enforcement, session summaries, Friday reconstruction |
| 11 | performance | Performance optimization, profiling, bottleneck analysis |
| 12 | refactoring | Safe refactoring protocol, named refactoring patterns |
| 13 | research | ArXiv, GitHub, SOTA lookup — structured output |
| 14 | robot | Diffusion Policy, LeRobot, ACT, SO-101 arm workflow |
| 15 | scan | Job discovery across platforms |
| 16 | security | Security audit, OWASP checklist, secrets management |
| 17 | slurm | HPC job submission, monitoring, SSH tunnels |
| 18 | spec | Spec-driven development — write spec before code |
| 19 | tailor | Resume variant selection + cover letter generation |
| 20 | testing | TDD, test pyramid, AAA pattern, anti-patterns |
| 21 | track | Application CRM, pipeline stats, conversion rates |

## MCP Connectors (active, user scope)
- `github` ✓ — GitHub API via `@modelcontextprotocol/server-github` (token from `gh auth`)
- `filesystem` ✓ — local file access via `@modelcontextprotocol/server-filesystem /Users/parvpatodia`
- `memory` ✓ — persistent KV memory via `@modelcontextprotocol/server-memory`
- `fetch` — REMOVED (package `@modelcontextprotocol/server-fetch` doesn't exist on npm; Claude Code has built-in WebFetch)

### Re-add MCP commands (if needed after reinstall)
```bash
# GitHub MCP
export GITHUB_TOKEN=$(gh auth token)
claude mcp add -s user -e "GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_TOKEN" -- github npx -y @modelcontextprotocol/server-github

# Filesystem MCP
claude mcp add -s user -- filesystem npx -y @modelcontextprotocol/server-filesystem /Users/parvpatodia

# Memory MCP
claude mcp add -s user -- memory npx -y @modelcontextprotocol/server-memory
```

## Architecture Decisions

**Why global skills (not project-local)?**
Skills like debug, research, spec, testing apply to ALL projects. Centralizing avoids duplication and ensures consistency. Project-specific skills (e.g. robot.md for summer project) live globally because they're needed across project boundaries when context-switching.

**Why user scope for MCP (not local)?**
MCP connectors should be available in any project, not just the worktree where they were registered. User scope = persistent across all Claude Code sessions.

**Why no fetch MCP?**
Package doesn't exist on npm registry. Built-in WebFetch tool in Claude Code covers web fetching needs. Filesystem + GitHub + memory covers the critical use cases.
