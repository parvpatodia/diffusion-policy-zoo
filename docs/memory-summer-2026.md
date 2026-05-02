---
name: Summer 2026 Robotics Plan
description: Diffusion Policy reproduction and SO-101 arm project — 14-week plan
type: project
originSessionId: 311796ae-39cb-4d66-8c38-58fcc55fb149
---
**Why:** Pivot recommended from Laksh.ai feasibility audit (Apr 2026). Gym form-coach has a BlazePose ceiling. Diffusion Policy is frontier research with clear reproducibility path.

## Primary Target: Diffusion Policy Zoo
Reproduce Chi et al. 2023 (arXiv:2303.04137) + extend to SO-101 hardware.

## Hardware
- SO-101 robot arm kit (HuggingFace/Seeed Studio) — 6-DOF low-cost arm
- HPC A100 cluster for heavy training
- M1 for local dev, data collection, light runs

## Framework: LeRobot (HuggingFace)
- Unified DP + ACT training pipeline
- SO-101 integration built-in
- Repo: github.com/huggingface/lerobot (⭐4.2k, active)
- Installed at: ~/Desktop/lerobot (v0.5.2, uv-managed venv)

## 14-Week Plan (Summer 2026)
| Weeks | Milestone |
|---|---|
| 1-2 | LeRobot setup, Push-T 2D reproduction (>70% success) |
| 3-4 | 200 teleoperation demos for cube-pick task |
| 5-6 | Train DP on collected data, eval in MuJoCo sim |
| 7-8 | Sim-to-real transfer, document failure modes |
| 9-10 | DP vs ACT comparison on cube-pick |
| 11-12 | More complex task (pour, stack, or handover) |
| 13-14 | Write-up, HuggingFace model card, blog post |

## Key Papers
- Diffusion Policy: arXiv:2303.04137 (primary)
- ACT: arXiv:2304.13705 (comparison baseline)
- Robomimic: arXiv:2108.03298 (sim environments)

## Week 0 Math Prep (prerequisite)
- Score diffusion model math (DDPM, DDIM, score matching)
- Review: denoising score matching, Langevin dynamics, ELBO
- Resource: Deep Unsupervised Learning (Berkeley CS294-158)

**Why:** Can't implement or debug DP without understanding the forward/reverse diffusion process and why action space conditioning works.

## LeRobot Training Commands
```bash
# Activate environment
cd ~/Desktop/lerobot && source .venv/bin/activate

# Smoke test (5 steps, M1 MPS)
uv run lerobot-train \
  --policy.type=diffusion \
  --dataset.repo_id=lerobot/pusht \
  --policy.device=mps \
  --policy.push_to_hub=false \
  --training.num_workers=0 \
  --training.batch_size=4 \
  --training.num_epochs=1 \
  --training.save_checkpoint=false \
  --training.log_freq=1

# Full run (300 epochs, use HPC for this)
uv run lerobot-train \
  --policy.type=diffusion \
  --dataset.repo_id=lerobot/pusht \
  --policy.device=mps \
  --policy.push_to_hub=false
```

## Success Criteria
- Reproduce Push-T at >70% success (validates implementation)
- Real robot cube-pick at >50% success (validates sim-to-real)
- Clean ablation comparing DP vs ACT on same task
- Public model card + code on HuggingFace
