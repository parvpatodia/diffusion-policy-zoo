# DECISIONS.md

## Simulation environment: nuPlan (chosen over CARLA)
nuPlan uses real Motional driving data, has PDM-Score metric for
closed-loop eval, and reactive agents built-in. CARLA requires
building all evaluation infrastructure from scratch.

## Three baselines:
1. Behavior Cloning — pure imitation
2. MILE-style world model — model-based imitation
3. VLA language-conditioned policy

## Week 2 goal: nuPlan hello-world — one forward pass through the env.
