---
name: experiment
description: ML experiment tracking — setup, run, log, compare, checkpoint. PyTorch/JAX on M1 or HPC A100.
user_invocable: true
args: command
---

# experiment — ML Experiment Tracking

## Directory Structure
```
experiments/[exp_name]/
├── config.yaml       # frozen at run start
├── train.log
├── metrics.jsonl     # one line per step: {epoch, step, loss, val_loss, lr, grad_norm}
├── checkpoints/
│   ├── best.pt
│   ├── latest.pt
│   └── epoch_050.pt  # every 50 epochs
└── summary.md        # human-readable result + decision
```

## Logging Standard
```json
{"epoch": 1, "step": 100, "loss": 0.421, "val_loss": 0.389, "lr": 3e-4, "grad_norm": 2.1}
```

## Checkpoint Protocol
```python
# Save best
if val_loss < best_val_loss:
    torch.save({"epoch": epoch, "model_state": ..., "optimizer_state": ..., "config": config},
               exp_dir / "checkpoints/best.pt")
# Always save latest (for resume)
torch.save(checkpoint, exp_dir / "checkpoints/latest.pt")
```

## Diffusion Policy Pre-run Checks
```
[ ] Actions min-max scaled to [-1, 1]
[ ] Images in [0,1], proprio z-scored
[ ] Cosine noise schedule (better than linear for manipulation)
[ ] EMA enabled (ema_decay=0.9999)
[ ] pred_horizon > action_horizon (usually 2x)
[ ] Dataset size: <200 demos on Push-T is normal
```

## Anti-patterns
- No frozen config (unreproduce-able)
- Not logging grad_norm (can't diagnose instability)
- Saving only model weights (need optimizer state to resume)
- No summary.md (can't compare 3 weeks later)
- Changing hyperparams mid-run (split into two experiments)
