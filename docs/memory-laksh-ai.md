---
name: Laksh.ai Project
description: Gym form-coach app — live URLs, deploy status, known issues, architecture
type: project
originSessionId: 311796ae-39cb-4d66-8c38-58fcc55fb149
---
## Live URLs
- **Frontend (canonical):** https://laksh-ai-tawny.vercel.app (NOT laksh-ai.vercel.app — wrong account)
- **Backend API:** https://laksh-api.fly.dev
- **Health:** https://laksh-api.fly.dev/health → `{"status":"ok","chroma_ready":true,"collection_count":550}`

## Architecture
- Frontend: Next.js on Vercel (`~/Laksh_AI/web/`)
- Backend: FastAPI on Fly.io (`~/Laksh_AI/app/main.py`)
- Pose: MediaPipe BlazePose (browser) + RTMPose (server)
- Vector DB: ChromaDB (550 demos indexed)
- Video: LTX-2.3 (planned)
- Body model: SMPL/SMPL-X (planned)

## Known Issues / Constraints
- BlazePose has a ceiling — keypoint accuracy degrades at high speed
- Rep counter is realtime preview (ghost), not canonical truth
- Backend: single Fly machine in `iad`, no auto-failover
- `uncalibrated_v0` in TrustPanel = no calibration cohort yet (honest, not a bug)
- CORS regex must cover `laksh-ai-*.vercel.app` AND `*-laksh-ai.vercel.app`
- Fly machine: must have `autostop=off` for demos

## Feasibility Assessment (2026-04-19)
From `.agent-logs/feasibility-audit.md`: gym is narrow, BlazePose ceiling is real.
Recommendation: squat+deadlift only OR pivot to robotics ML (diffusion-policy-zoo).

## Active Branch
`feat/realtime-demo` — 52 commits from Apr 17-18 session. Deployed but NOT committed (per CLAUDE.md operating rules). Commit these 3 logical changes when ready:
1. `fix(api): allow Vercel preview/deploy URLs via CORS regex` — `app/main.py`
2. `fix(realtime): gap-reset and hysteresis in rep counter` — `web/lib/realtime/repCounter.ts`
3. `feat(web): trust panel and full-body camera framing` — `web/components/TrustPanel.tsx`, `web/components/PoseCamera.tsx`
