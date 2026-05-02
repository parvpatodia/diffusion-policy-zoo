# Research: Diffusion Policy SOTA
**Date:** 2026-05-01
**Purpose:** Pre-implementation survey before starting summer project

## 1. Diffusion Policy
**Paper:** arXiv:2303.04137 | Chi et al., RSS 2023 + IJRR 2025
**Key insight:** DDPM over robot action space conditioned on visual obs + proprio. Explicitly handles multi-modal action distributions.
**Results:** 46.9% avg improvement over prior SOTA, 12 tasks / 4 benchmarks. Push-T dataset: 205 trajectories.

| Variant | Latency | Control rate |
|---|---|---|
| DDPM (100 steps) | ~500ms | 2 Hz |
| DDIM (10 steps) | ~200ms | 5 Hz |
| Consistency Policy | ~50ms | 20 Hz |

**M1 verdict:** DDPM too slow for real robot. Use DDIM for sim. Use ACT for SO-101.

## 2. ACT — Action Chunking with Transformers
**Paper:** arXiv:2304.13705 | Zhao, Kumar, Levine, Finn, RSS 2023
**Key insight:** CVAE encodes demo into latent; transformer decodes full action chunk (20-100 steps). Fast (50ms = 20Hz).

| Condition | Prefer |
|---|---|
| <200 demos | ACT |
| Reactive/high-speed | ACT |
| Real SO-101 deployment | **ACT** |
| >500 demos, multi-modal task | DP |

| Metric | ACT | DP |
|---|---|---|
| Min demos | 50 | 200 |
| Recommended | 100–500 | 500–2000 |
| Training time (1 GPU) | 2–4h | 6–12h |

## 3. Current SOTA (2025-2026)
| Method | Type | In LeRobot? |
|---|---|---|
| π₀ (Pi Zero) | Flow VLA | Yes (Pi0Fast, Pi0.5) |
| VQ-BeT | VQ tokenization | Yes |
| GR00T N1.5 | Foundation VLA | Yes |
| SmolVLA | Compact VLA | Yes |

## 4. LeRobot v0.5.2
- Install: `uv sync --locked --extra diffusion --extra pusht --extra training`
- Apple Silicon: `--policy.device=mps` (confirmed in AGENT_GUIDE.md)
- SO-101 support: YES (`--robot.type=so101_follower`)

## 5. Real Robot Gotchas (SO-101 + ACT deployment)
- Gripper motors burn out from excessive force → stock spare servos
- 50 demos → overfitting. Need 150+ with stratified sampling (25 eps/bin × 6 bins)
- Identical webcams → USB path conflicts → write udev rules
- Calibration drift after power cycle → use persistent calibration files
- Front + top camera (not front + side — side occludes gripper)
- Lock camera exposure + white balance across sessions
- Hold out eval set (2 eps/bin) to detect overfitting

**Failure mode ladder (Try 1 → Try 3):**
1. Pecking/vibrating → overfitting (<50 demos)
2. Overreaching → insufficient position diversity
3. Grasping top-of-block → training data bias
4. No recovery → single orientation in demos
5. Jitter → synchronous inference

## 6. Recommendation
- Weeks 1-2: Push-T + DP (M1, DDIM, target >70%)
- Weeks 3-8: SO-101 cube-pick + ACT (150+ demos)
- Weeks 9-10: DP-DDIM vs ACT controlled comparison = research contribution
- Week 0: DDPM math (CS294-158, Lilian Weng DDPM blog)
