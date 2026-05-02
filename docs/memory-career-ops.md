---
name: Career Ops Project
description: AI job search automation — architecture, constraints, current state
type: project
originSessionId: 311796ae-39cb-4d66-8c38-58fcc55fb149
---
**Repo:** ~/career-ops (forked from santifer/career-ops)
**Purpose:** Automate job discovery, evaluation, resume tailoring, form filling, tracking

## Architecture (from SPEC.md)
- OOP: Scanner → Evaluator → Tailor → Applier → Tracker pipeline
- Abstract base classes with platform-specific subclasses
- TypeScript + Playwright + Apify MCP
- TDD with Vitest

## Key Files
- `CLAUDE.md` — agent OS with all commands
- `files_extracted/SPEC.md` — full architecture spec
- `files_extracted/efficiency.md` — caveman technique reference
- `.claude/skills/` — 9 skills (all copied to global `~/.claude/skills/`)

## Hard Constraints
1. NEVER auto-submit applications
2. NEVER fabricate resume content
3. NEVER exceed 25 LinkedIn applications/day
4. NEVER apply to jobs scoring <50/100
5. ALWAYS log every application to `data/applications.json`

## Resume Variants (cv/)
master.md | ai.md | ml.md | robotics.md | ta.md

## Scoring Weights
skill_match 30% + experience 20% + location 15% + visa 15% + company 10% + timing 10%

## Current State (as of 2026-05-01)
- Repo exists locally at ~/career-ops
- Spec written, CLAUDE.md complete
- Source code (src/) NOT yet implemented (pending Session 2+)
- cv/ directory needs to be populated with actual resume content
