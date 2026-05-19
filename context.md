# Project Context: diffusion-policy-zoo
> Persistent memory. Claude Code reads this at session start.

## 1. Vision
Reproduce Diffusion Policy (arXiv:2303.04137), benchmark vs ACT, deploy to SO-101 robot arm via LeRobot.

## 2. Problem Statement
Learn robot manipulation policies via imitation learning. Primary task: Push-T (sim) → cube-pick (SO-101). Research contribution: controlled DP-DDIM vs ACT comparison on real hardware.

## 3. Tech Stack
- Python 3.12 | PyTorch 2.10.0 (MPS on M1, CUDA on A100)
- LeRobot 0.5.2 | diffusers 0.35.2 | gym-pusht | uv (package manager)
- SLURM (HPC A100 training) | wandb (experiment tracking)
- FFmpeg 8.1 (required for torchcodec video decoding)

## 4. Hardware
- M1 MacBook Pro: local dev, data collection, Push-T runs (`--policy.device=mps`)
- HPC A100: heavy training (`--policy.device=cuda`)
- SO-101 arm: real robot eval (weeks 7+)

## 5. Current Status
- [x] LeRobot 0.5.2 installed at ~/Desktop/lerobot
- [x] Push-T training pipeline verified on M1 (smoke test: training ran at 100s)
- [x] FFmpeg 8.1 installed (fixes torchcodec `libavutil.60.dylib` error)
- [ ] Push-T full training run (300 epochs, target >70% success)
- [ ] SO-101 hardware setup + udev rules
- [ ] Data collection (150+ demos, stratified sampling)

## 6. LeRobot Commands
```bash
# Train Diffusion Policy on Push-T
cd ~/Desktop/lerobot
uv run lerobot-train \
  --dataset.repo_id=lerobot/pusht \
  --policy.type=diffusion \
  --policy.device=mps \
  --policy.push_to_hub=false \
  --output_dir=outputs/train/dp_pusht_v1 \
  --job_name=dp_pusht_v1 \
  --batch_size=8 \
  --wandb.enable=false

# Train ACT on SO-101 dataset
uv run lerobot-train \
  --dataset.repo_id=${HF_USER}/my_task \
  --policy.type=act \
  --policy.device=mps \
  --policy.push_to_hub=false \
  --output_dir=outputs/train/act_cube_pick_v1 \
  --job_name=act_cube_pick_v1
```

## 7. Known Issues / Gotchas
- `lerobot/diffusion_pusht` HuggingFace pretrained model is pre-v0.5 format — missing `policy_preprocessor.json`. Train from scratch.
- torchcodec needs FFmpeg at `/opt/homebrew/opt/ffmpeg/lib/` — fix: `brew install ffmpeg`
- Training command needs `--policy.push_to_hub=false` to skip hub auth requirement
- Real SO-101: USB conflicts with identical webcams → write udev rules before data collection
- 50 demos → overfitting. Need 150+ with stratified sampling for >75% OOD success.

## 8. Key Decisions
| Decision | Alternative | Rationale |
|---|---|---|
| LeRobot over raw DP impl | real-stanford/diffusion_policy | SO-101 support, unified DP+ACT, active maintenance |
| ACT for SO-101 real robot | DP-DDIM | 50ms inference (20Hz) vs 200ms (5Hz). Arm control needs ≥10Hz |
| DP for Push-T sim | ACT | Educational: understand DDPM action space conditioning |
| uv over conda | conda env | LeRobot's official package manager, locked deps, faster |

## 9. 14-Week Timeline
| Weeks | Milestone |
|---|---|
| 0 | Math: DDPM forward/reverse, score matching, DDIM |
| 1-2 | Push-T DP reproduction (>70% success in sim) |
| 3-4 | SO-101 setup + 150 teleoperation demos |
| 5-6 | Train ACT on collected data, sim eval |
| 7-8 | Sim-to-real transfer, document failures |
| 9-10 | DP-DDIM vs ACT controlled comparison |
| 11-12 | More complex task (pour / stack) |
| 13-14 | Write-up, HuggingFace model card, blog post |

## 10. Session Log
| Date | What was done | Key decisions |
|------|---------------|---------------|
| 2026-05-01 | Project setup, LeRobot install, training pipeline verified | uv + FFmpeg fix, ACT for real robot |
