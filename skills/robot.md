---
name: robot
description: Diffusion Policy, LeRobot, ACT, SO-101 workflow. From data collection to sim-to-real.
user_invocable: true
args: command
---

# robot — Robotics & Diffusion Policy

## Key Papers
| Paper | arXiv | Key insight |
|---|---|---|
| Diffusion Policy | 2303.04137 | DDPM over action space, obs+proprio conditioning |
| ACT | 2304.13705 | Action chunking with CVAE, 50ms inference |
| Robomimic | 2108.03298 | Sim benchmarks |

## LeRobot Setup (v0.5.2)
```bash
git clone --depth 1 https://github.com/huggingface/lerobot ~/Desktop/lerobot
cd ~/Desktop/lerobot
uv sync --locked --extra diffusion --extra pusht --extra training
brew install ffmpeg   # required for torchcodec
```

## Push-T Training (M1)
```bash
uv run lerobot-train \
  --dataset.repo_id=lerobot/pusht \
  --policy.type=diffusion \
  --policy.device=mps \
  --policy.push_to_hub=false \
  --output_dir=outputs/train/dp_pusht_v1 \
  --batch_size=8 \
  --wandb.enable=false
```

## SO-101 Training (ACT)
```bash
uv run lerobot-train \
  --dataset.repo_id=${HF_USER}/cube_pick \
  --policy.type=act \
  --policy.device=mps \
  --policy.push_to_hub=false \
  --output_dir=outputs/train/act_cube_pick_v1 \
  --batch_size=8
```

## Data Collection Protocol
```
1. 150+ demos minimum (50 overfits, 150 → 75% OOD)
2. 25 episodes per bin × 6 bins = 150 stratified
3. Front + top camera (NOT front + side)
4. Lock camera exposure + white balance
5. Write udev rules for USB camera assignment
6. Don't look at arm during recording
7. Hold out eval set (2 eps/bin)
```

## Sim-to-Real Checklist
```
[ ] Domain randomization during sim training
[ ] Same action frequency (Hz) in sim and real
[ ] Proprio normalization recomputed on real robot ROM
[ ] Policy runs at >10 Hz for smooth control
[ ] 5 garbage inference calls before deployment (JIT warmup)
```

## Policy Debug
If success rate <40%:
1. Erratic actions → check action normalization
2. Sluggish → increase action_horizon
3. Out-of-dist images → camera moved or lighting changed
4. Low demo count (<50) → collect more data, not tune hyperparams
5. Grad norm >10 → add gradient clipping

## 14-Week Timeline
| Weeks | Milestone |
|---|---|
| 0 | DDPM math: score matching, Langevin dynamics, DDIM |
| 1-2 | Push-T DP reproduction (>70% sim success) |
| 3-4 | SO-101 setup + 150 demos |
| 5-6 | ACT training + sim eval |
| 7-8 | Sim-to-real transfer |
| 9-10 | DP-DDIM vs ACT controlled comparison |
| 11-12 | More complex task |
| 13-14 | Write-up + HuggingFace model card |
