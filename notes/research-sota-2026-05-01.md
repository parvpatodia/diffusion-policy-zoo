# Research: Diffusion Policy SOTA
**Date:** 2026-05-01
**Purpose:** Pre-implementation survey before starting summer project

---

## 1. Primary Method: Diffusion Policy

**Paper:** arXiv:2303.04137 — "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
**Authors:** Chi, Xu, Feng, Cousineau, Du, Burchfiel, Tedrake, Song (RSS 2023 + IJRR 2025)
**Key insight:** Apply DDPM denoising diffusion to the *action space* conditioned on visual observations + proprioception. Explicitly models multi-modal action distributions — can output two valid solutions to the same task.

**Benchmark summary:**
- 46.9% average improvement over prior SOTA across 12 tasks / 4 benchmarks
- Push-T dataset: 205 trajectories (small, good for prototyping)
- Backbone choice matters: CNN (UNet) vs. Transformer — transformer wins on longer-horizon tasks

**Inference latency (critical for real robot):**
| Variant | Latency | Control rate |
|---|---|---|
| DDPM (100 steps) | ~500ms | 2 Hz |
| DDIM (10 steps) | ~200ms | 5 Hz |
| Consistency Policy | ~50ms | 20 Hz |

**Verdict on M1:** DDPM is too slow for real robot (2 Hz). Use DDIM for sim eval. Use Consistency Policy or ACT for SO-101.

---

## 2. Comparison: ACT (Action Chunking with Transformers)

**Paper:** arXiv:2304.13705 — "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware"
**Authors:** Zhao, Kumar, Levine, Finn (RSS 2023)
**Key insight:** CVAE encodes demonstration into latent; transformer decodes full action *chunk* (20-100 steps at once). Temporal consistency built-in, fast inference.

**ACT vs. DP decision table:**

| Condition | Use |
|---|---|
| <200 demos available | ACT |
| Reactive / high-speed task | ACT |
| Low-compute deployment (Jetson) | ACT |
| Multiple valid action solutions | DP |
| >500 demos, slow precision task | DP |
| Real SO-101 deployment | **ACT** (50ms = 20Hz) |

**Data requirements:**
| Metric | ACT | DP |
|---|---|---|
| Minimum demos | 50 | 200 |
| Recommended | 100–500 | 500–2000 |
| Training time (single GPU) | 2–4h | 6–12h |

---

## 3. Current SOTA Beyond DP (2025-2026)

| Method | Type | Key contribution | Available in LeRobot? |
|---|---|---|---|
| π₀ (Pi Zero) | Flow VLA | Flow matching + pretrained VLM, multi-platform | Yes (Pi0Fast, Pi0.5) |
| VQ-BeT | VQ tokenization | SOTA on unconditional behavior generation, 5/7 envs | Yes |
| Consistency Policy | Distilled DP | ACT-speed with DP multi-modal properties | Needs check |
| GR00T N1.5 | Foundation VLA | NVIDIA, general manipulation | Yes |
| SmolVLA | Compact VLA | HuggingFace, small model | Yes |

**What this means for the project:**
- Push-T reproduction: use standard DP (educational, validate implementation)
- SO-101 real robot: use ACT (inference speed wins)
- If time permits: compare DP-DDIM vs ACT on same real task (the actual research contribution)

---

## 4. LeRobot Framework

**Repo:** github.com/huggingface/lerobot
**Install:** `pip install lerobot`
**Policies available:** ACT, Diffusion, VQ-BeT, Multitask DiT, Pi0Fast, Pi0.5, GR00T N1.5, SmolVLA
**SO-101 support:** YES (confirmed via blog posts + issue tracker, has requirements-macos.txt)
**Push-T dataset:** Hosted on HuggingFace Hub, 205 trajectories, auto-downloads

---

## 5. Real Robot Gotchas (SO-101 + ACT — sourced from actual deployment blog)

These are hard-won lessons from real deployment, not theory:

### Hardware
- **Gripper motors burn out** from excessive force during teleop. Stock spare motors.
- **50 demos → pecking/overfitting**. Need 150+ for >75% OOD success.
- **USB conflicts**: identical webcams get random path assignments → write udev rules.
- **Calibration drift after power cycle**: use persistent calibration files, never temp dirs.

### Data Collection
- Camera must stay physically fixed (tape + markers) between collection and eval — even small changes cause failures.
- Lock camera exposure + white balance across sessions.
- Use front + top camera (not front + side — side occludes gripper during grasps).
- Stratified sampling: define clear bins for object start positions, 25 eps/bin min.
- **Don't look at the arm during recording** — your body provides implicit info the camera can't see.

### Training
- No eval set = can't detect overfitting. Always hold out 2 eps/bin.
- 90% in-distribution / 75% OOD success requires ~150 demos with good coverage.

### Failure mode ladder (from Try 1 → Try 3 experience):
1. Pecking/vibrating: overfitting to <50 demos
2. Overreaching: insufficient position diversity
3. Grasping top-of-block: training data bias
4. No recovery: single orientation in demos
5. Jitter: synchronous inference (use async / action chunking properly)

---

## 6. Recommendation for This Project

**Weeks 1-2:** Push-T with DP on M1 (validates understanding, small dataset, runs locally)
- Use DDIM (10 steps) not DDPM — 5 Hz acceptable for sim
- Target: >70% success before touching real robot

**Weeks 3-8:** SO-101 cube-pick with ACT
- Start with 50 demos to confirm pipeline, then scale to 150+
- Use front + top camera from day 1 (not front + side)
- Write udev rules before collecting data
- Use stratified bin sampling (25 eps/bin × 6 bins = 150)

**Weeks 9-10:** DP-DDIM vs ACT comparison on same cube-pick task
- This is the research contribution: controlled comparison on real hardware
- Hypothesis: ACT wins on speed/data-efficiency, DP wins on multi-modal tasks

**Week 0 (math prep, before code):**
- Understand DDPM forward/reverse process (score matching, Langevin dynamics)
- Resource: Deep Unsupervised Learning Berkeley CS294-158, Lilian Weng's DDPM blog
- Without this, can't debug training instability or understand why DDIM works
