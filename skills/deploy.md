---
name: deploy
description: Deployment workflow for Fly.io, Vercel, Docker, HPC. Pre-flight checks, rollback, post-deploy verification.
user_invocable: true
args: target
---

# deploy — Deployment Workflow

## Pre-flight Checklist (ALWAYS run first)
```
[ ] Tests passing
[ ] No secrets in code: grep -r "sk-\|api_key" --include="*.py"
[ ] .env not committed
[ ] Build succeeds locally
[ ] CORS config correct for target environment
[ ] Env vars set in target platform
```

## Fly.io
```bash
fly status && fly machine list
fly deploy --remote-only
curl -I https://[app].fly.dev/health          # verify HTTP 200
fly machine update [id] --autostop=off --autostart
```

**Laksh.ai:** `laksh-api.fly.dev` | health `{"status":"ok","chroma_ready":true}`
CORS regex must cover `laksh-ai-*.vercel.app` AND `*-laksh-ai.vercel.app`

## Vercel
```bash
vercel env add NEXT_PUBLIC_API_BASE production
vercel --prod --yes
curl -I https://laksh-ai-tawny.vercel.app     # NOT laksh-ai.vercel.app (wrong account)
```

## Post-deploy Verification
```
1. Health endpoint: HTTP 200 + expected JSON
2. CORS preflight from frontend: HTTP 200, allow-origin header present
3. CORS preflight from random URL: HTTP 400 (security check)
4. One real API call end-to-end
5. Document deploy in SESSION_LOG or HANDOFF.md
```

## Anti-patterns
- Deploying without tests
- Env vars in code instead of platform secrets
- Skipping CORS verification after backend deploy
- Fly machine with autostop=on during demos
