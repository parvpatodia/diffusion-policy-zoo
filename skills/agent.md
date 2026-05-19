---
name: agent
description: Meta-agent for background automation — schedule recurring tasks, monitor long-running jobs, trigger multi-step pipelines.
user_invocable: true
args: command
---

# agent — Background Automation Hub

## Args
- `list` → show all active background automations and their status
- `monitor-slurm [job_id] [exp_name]` → watch HPC training job, alert on complete/fail
- `monitor-deploy [url]` → watch a deployment endpoint for health
- `schedule [task] [cron]` → set up a recurring task
- `run [task]` → execute a one-off background pipeline
- `stop [task_id]` → cancel a running background agent

## Active Automations Registry

| ID | Task | Schedule | Last Run | Status |
|---|---|---|---|---|
| kb-daily | knowledge-base daily update | daily 06:00 | — | — |
| career-weekly | career-ops weekly scan | sun 09:00 | — | — |

## Monitor SLURM Job

Checks HPC job every 30 minutes:
```
1. ssh hpc "squeue -j [job_id] --format='%T'"
   - RUNNING → tail last 20 lines of log, check for loss divergence
   - COMPLETED → sync results, send notification, update experiment registry
   - FAILED → tail error log, extract failure reason, send alert
2. Divergence check: if loss > 10x initial loss after epoch 10 → alert
3. On completion: rsync experiments/[exp_name] from HPC to local
```

## Monitor Deploy Health

Polls an endpoint every 5 minutes:
```
1. curl -s -o /dev/null -w "%{http_code}" [url]/health
2. If not 200 for 3 consecutive checks → alert
3. Recovery: fly machine start [machine_id]
```

## Multi-agent Delegation Pattern

```python
Agent(
  subagent_type="general-purpose",
  prompt="[task brief with full context — no memory of current session]",
  description="[3-5 word description]",
  run_in_background=True
)
```

Rules:
- Background agents need fully self-contained prompts
- Foreground agents: use when you need their output before proceeding
- Never duplicate work between main agent and subagent

## Token Budget
| Task | Target | Hard Limit |
|---|---|---|
| SLURM monitor check | 0.5K | 2K |
| Deploy health check | 0.2K | 1K |
| Daily job scan | 5K/platform | 25K total |
| Session: full pipeline | 30K | 50K |
