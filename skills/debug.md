---
name: debug
description: Systematic debugging. Reproduce → isolate → hypothesize → verify → fix → regression test. No guessing.
user_invocable: true
args: symptom
---

# debug — Systematic Debugging Protocol

**Rule: Never guess. Never try random fixes.**

## Steps

### 1. Reproduce
- Get exact error message + stack trace
- Create minimal reproduction case (smallest code that triggers it)
- Verify deterministic (same input → same failure)
- Regression check: `git bisect` if "it worked before"

### 2. Isolate
- Binary search callstack: which layer owns the failure?
- Is it your code or a library? Data problem or logic problem?
- Check: assumed state vs. actual state

### 3. Hypothesize (max 3)
```
H1: [specific root cause claim] — [confirming evidence]
H2: [alternative]
H3: [third alternative]
```

### 4. Verify
- Test H1 first. Write a test that fails if H1 is true.
- If denied → H2. Explicitly state: "H1 was wrong because X."

### 5. Fix
- Fix root cause, not symptom
- Minimum change. Don't refactor surrounding code.

### 6. Regression Test
- Write test that would have caught this bug
- Verify fails on broken code, passes on fix

## ML-Specific

### Training instability
1. LR too high → loss explodes. Too low → plateaus.
2. Grad norms: log them. >10 = exploding. <1e-4 = vanishing.
3. Data pipeline: batch sampled correctly? No label corruption?
4. Loss function: correct reduction? No log(0)?

### Diffusion Policy specific
1. Action normalization: min-max or z-score? Consistent train/eval?
2. Observation horizon: correct frames stacked?
3. Action horizon vs prediction horizon: slicing correctly?
4. DDPM noise schedule: alpha_bar computed correctly?

## Anti-patterns
- `try/except` to hide errors
- Commenting out code without a hypothesis
- Fixing symptom without understanding root cause
- Not writing regression test after fixing
