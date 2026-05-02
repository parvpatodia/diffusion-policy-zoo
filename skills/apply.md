---
name: apply
description: Fill application forms via Playwright. ALWAYS stops before submission — user reviews and clicks Submit manually.
user_invocable: true
args: job_id_or_batch
---

# apply — Form Filling (NEVER Auto-Submit)

## CRITICAL RULE
**NEVER click Submit/Apply/Send.** Fill all fields. Stop. Print review checklist. User submits manually.

## Args
- `[job_id]` → fill single application
- `batch [job_ids...]` → sequential form filling, pause between each

## Pre-conditions
1. Job must have `status: Evaluated` or `Tailored` in tracker
2. PDF must exist at `output/resumes/[job_id]-[variant].pdf`
3. Score must be ≥ 50

## ATS Detection
```
URL contains "greenhouse.io" → GreenhouseHandler
URL contains "lever.co" → LeverHandler
URL contains "myworkdayjobs" → WorkdayHandler
URL contains "linkedin.com/jobs" → EasyApplyHandler
else → GenericHandler
```

## Execution
```
npm run apply -- --job [job_id]
```

Playwright opens browser (headless=false so you can watch).
Browser stays open after filling.

## Review Checklist Output
After filling, print:
```
=== READY FOR YOUR REVIEW ===
Company: [company]
Role: [role]
URL: [url]
ATS: [greenhouse/lever/linkedin/generic]

Fields filled ([N]):
  ✅ First name
  ✅ Last name
  ✅ Email
  ✅ Phone
  ✅ Resume uploaded
  ✅ LinkedIn URL
  ⚠️  Work authorization → "F-1 OPT, CPT available" [VERIFY]

Screening questions:
  Q: "Are you authorized to work in the US?"
  A: "I am on F-1 student visa and eligible for CPT/OPT" [FLAGGED — confirm phrasing]

  Q: "Expected graduation date?"
  A: "May 2027" [OK]

STOP: Open browser tab, review all fields, then click Submit.
After submitting, run: npm run track -- [job_id] Applied
```

## Flagging Rules
Flag a screening question if:
- It's about visa/authorization (phrasing matters legally)
- It asks about salary expectations (Parv has a target range to verify)
- It asks about start dates (verify against academic calendar)
- Answer might be inconsistent with resume claims

## After Each Application
Remind user to run:
```
npm run track -- [job_id] Applied
```

## LinkedIn Limit Check
Before any LinkedIn Easy Apply: verify today's count < 25.
If at limit: STOP. Say "Daily LinkedIn limit reached (25/25). Try again tomorrow."
