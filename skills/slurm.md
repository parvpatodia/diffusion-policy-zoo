---
name: slurm
description: HPC SLURM job submission, monitoring, SSH tunnels for A100 training.
user_invocable: true
args: command
---

# slurm — HPC SLURM Workflow

## SSH Config (~/.ssh/config)
```
Host hpc
  HostName [cluster.university.edu]
  User ppatodia
  IdentityFile ~/.ssh/hpc_key
  ServerAliveInterval 60
```

## SLURM Script Template (A100)
```bash
#!/bin/bash
#SBATCH --job-name=[exp_name]
#SBATCH --partition=gpu
#SBATCH --gres=gpu:a100:1
#SBATCH --mem=32G
#SBATCH --cpus-per-task=8
#SBATCH --time=24:00:00
#SBATCH --output=logs/%j_%x.out
#SBATCH --error=logs/%j_%x.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=patodia.pa@northeastern.edu

module load cuda/12.1
source activate lerobot

nvidia-smi
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"

cd /scratch/$USER/[project]
uv run lerobot-train \
  --dataset.repo_id=lerobot/pusht \
  --policy.type=diffusion \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --output_dir=experiments/[exp_name] \
  --wandb.enable=true
```

## Key Commands
```bash
sbatch scripts/train.sh              # submit
squeue -u $USER                      # check status
ssh hpc "tail -f logs/[jobid].out"   # tail logs live
scancel [jobid]                      # cancel
rsync -avz hpc:/scratch/ppatodia/[project]/experiments/ ./experiments/  # sync results
```

## Interactive Session (debug before 24h submit)
```bash
ssh hpc "srun --partition=gpu --gres=gpu:a100:1 --mem=16G --time=2:00:00 --pty bash"
```

## SSH Tunnel (TensorBoard)
```bash
ssh hpc "tensorboard --logdir experiments/ --port 6006 &"
ssh -L 6006:localhost:6006 hpc -N &   # then open http://localhost:6006
```

## Anti-patterns
- Submitting 24h job without interactive test first
- Not setting `--mail-type=END,FAIL`
- Forgetting `module load cuda` before conda/uv activate
- Using `~/` for large data (use `/scratch/`)
- Not syncing results (HPC scratch is periodically purged)
