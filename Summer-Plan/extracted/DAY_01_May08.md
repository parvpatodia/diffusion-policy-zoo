# DAY 1 — Friday, May 8, 2026

**Theme:** Setup day. No deep work yet — you set up the environment so Day 2 onwards just runs.
**Promise to yourself:** Phone in kitchen tonight. Sleep at 11.

---

## TODAY'S NUMBERS

- 🎯 LeetCode: **0 problems** (setup day — start tomorrow)
- 💼 Applications: **0 submitted** (start Monday)
- 📧 Outreach: **0 sent** (start Tuesday)
- 📚 Karpathy: **Watch first 30 min of Lecture 1** (orientation only, type-along starts tomorrow)
- 🛠️ Setup tasks: **9 specific items below**

This is the lightest day of the week. The point is to clear all logistics so the rest of Week 1 just executes.

---

## THE SCHEDULE

| Time | Block | Tasks |
|---|---|---|
| Now → 6 PM | Setup tasks #1–6 | The infrastructure |
| 6 PM | Dinner break (8–9 PM your normal) | |
| 8–9 PM | Dinner | |
| 9–10:30 PM | Setup tasks #7–9 + Karpathy preview | |
| 10:30 PM | Laptop closed | Lid down |
| 10:30–11 PM | Wind-down | Shower, paper book |
| 11 PM | SLEEP | Hard cap |

---

## SETUP TASKS (do in this order)

### 🛠️ Task 1 — Email Khoury co-op coordinator (15 min)
- [ ] Open email, send to `coopcoordinator@khoury.northeastern.edu`, cc your faculty advisor
- [ ] Subject: "CPT eligibility question — Summer 2026 short internship vs Spring 2027 co-op"
- [ ] Body (use this verbatim, edit names):

> Hi [coordinator name],
>
> I'm an MS AI student at the SV campus, finished my second semester this week. I'm exploring a short summer 2026 internship via CPT and want to make sure I'm not jeopardizing my one full Khoury co-op slot, which I'd like to use Spring 2027 (Jan–April 2027) for the strongest FT conversion path before my May 2027 graduation.
>
> Can you confirm:
> 1. Is a short summer 2026 CPT internship (e.g., 8–12 weeks) compatible with also doing a full Spring 2027 co-op?
> 2. What's the typical timeline from offer letter → CPT authorization?
> 3. Are there any prerequisites I should complete now (Canvas course, advisor signoff, etc.)?
>
> Thanks for the guidance.
>
> Parv Patodia
> NUID: [yours]

### 🛠️ Task 2 — Build outreach target list (45 min)
- [ ] Open Notion or Google Sheet, name it "Outreach Targets"
- [ ] Columns: Name | Company | Role | Why interesting | Email | Status
- [ ] Find **12 candidates** for Tuesday/Thursday outreach this week:
  - 4 from Tier-B robotics startups (Bear Robotics, Dexterity, Diligent Robotics, Pickle Robot, Path Robotics — pick founders or engineers)
  - 4 Northeastern alumni at AV companies (LinkedIn → Northeastern alumni filter → Waymo/Cruise/Aurora/Wayve, MS or recent PhD grads)
  - 2 HuggingFace LeRobot team members (Remi Cadene + 1 other)
  - 2 YC startup founders/hiring managers (Work at a Startup → ML roles)
- [ ] For each, paste their LinkedIn URL. Don't find emails yet — that's Tuesday's task.

### 🛠️ Task 3 — Build job application target list (30 min)
- [ ] Same doc, new sheet called "Applications"
- [ ] Columns: Date | Company | Role | JD link | Why I fit | Submitted? | Reply?
- [ ] Pre-fill Monday–Thursday's 8 targets with actual JD links found NOW:
  - Mon: Tesla AI / Optimus or AI Inference (find specific posting on tesla.com/careers)
  - Mon: Kodiak Robotics (kodiak.ai/careers)
  - Tue: Applied Intuition (appliedintuition.com/careers)
  - Tue: Skydio (skydio.com/careers)
  - Wed: Bear Robotics (bearrobotics.ai/careers)
  - Wed: Dexterity (dexterity.ai/careers)
  - Thu: YC startup (workatastartup.com → filter ML)
  - Thu: NVIDIA Robotics (nvidia.com/careers, search "Isaac" or "robotics intern")
- [ ] If a specific role isn't open at one of these, swap it for the next-best at that company. Don't leave blanks.

### 🛠️ Task 4 — Sign up for LeetCode + NeetCode (15 min)
- [ ] Make sure you have a LeetCode account
- [ ] Open neetcode.io, bookmark the "NeetCode 150" list
- [ ] Bookmark NeetCode YouTube channel — you'll watch his explanations this week
- [ ] Create a tracker doc/sheet: "LeetCode Log" with columns: # | Date | Problem | Difficulty | Time | Help needed?

### 🛠️ Task 5 — Buy alarm clock + decide phone protocol (15 min)
- [ ] Order $15 alarm clock on Amazon (search "basic digital alarm clock") — arrives Saturday
- [ ] OR if you need it tonight, walk to Target/Walmart now
- [ ] Tonight: phone goes in kitchen, charges there. No exceptions ever.

### 🛠️ Task 6 — Clean up GitHub profile (30 min)
- [ ] Archive these repos (Settings → Archive): old `Laksh.ai` (the duplicate), `Word2Vec_and_PCA`
- [ ] Decide on `vit-from-scratch` README — add this honest note at the top:

> **Status note (May 2026):** This was an early exploration written in collaboration with Claude Code. I am revisiting the architecture from scratch as part of my Karpathy Zero-to-Hero curriculum and will update this README when components have been independently rebuilt.

- [ ] Pin these on your profile (Profile → "Customize your pins"):
  1. Laksh_AI
  2. av-policy-lab (next task)
  3. CRPO-Cross-Domain-Optimization
  4. Federated-Learning-Client-Selection
- [ ] Update profile README to mention current focus: "Building closed-loop driving policies in simulation. MS AI @ Northeastern SV."

### ⏸️ DINNER BREAK (8–9 PM)

### 🛠️ Task 7 — Rename / set up av-policy-lab repo (45 min)
- [ ] Either rename `diffusion-policy-zoo` → `av-policy-lab` in GitHub Settings, OR create new repo and migrate context.md
- [ ] Update README with this skeleton (~600 words, write it yourself, not Claude):

```
# av-policy-lab

Closed-loop autonomous driving policy learning in simulation.

## Project goal
Train and compare three policy learning approaches on [nuPlan / CARLA Leaderboard 2.0]
for closed-loop urban driving:

1. **Behavior Cloning** — pure imitation baseline
2. **MILE-style world-model imitation** — model-based imitation (Wayve 2022)
3. **VLA-flavored language-conditioned policy** — policy that takes natural-language directives

## Why
Closed-loop policy learning is the central problem in autonomous driving and embodied AI.
Most public reproductions stop at open-loop imitation; this project closes the loop with
honest scenario-based evaluation.

## Status
Week 1 of 16 — setting up simulation environment.

## Roadmap
- [ ] Week 1–4: simulation hello-world + first BC training run
- [ ] Week 5–6: complete BC baseline with metrics
- [ ] Week 7–8: MILE-style world-model baseline
- [ ] Week 9–10: VLA-conditioned policy
- [ ] Week 11–12: eval harness + multi-seed evaluation
- [ ] Week 13–14: failure analysis + writeup
- [ ] Week 15–16: HuggingFace blog post + arXiv preprint

## References
[Add: MILE paper, Urban Driver, Diffusion Policy, OpenVLA — fill in as you read]
```

- [ ] Commit + push: "Initial scoping for av-policy-lab"
- [ ] Create empty folders: `av_policy_lab/`, `data/`, `notebooks/`, `experiments/`

### 🛠️ Task 8 — Decide nuPlan vs CARLA (30 min)
- [ ] Read nuPlan docs landing page (nuplan-devkit on GitHub)
- [ ] Read CARLA Leaderboard 2.0 landing page
- [ ] Make decision based on:
  - Which has clearer setup docs?
  - Which has more recent papers / community activity?
  - Which is easier to get a "hello world" running on your hardware?
- [ ] Write decision in `DECISIONS.md` in the repo, with 2-sentence rationale
- [ ] Commit it

### 🛠️ Task 9 — Karpathy Lecture 1 preview (30 min)
- [ ] Open Karpathy's "Neural Networks: Zero to Hero" on YouTube
- [ ] Watch the FIRST 30 MINUTES of Lecture 1 (Micrograd) — orientation only, NO TYPING tonight
- [ ] Goal: understand what you're committing to. The actual type-along starts tomorrow morning.
- [ ] Create folder `karpathy-notes/lecture-1-micrograd/` in a separate repo (`karpathy-notes`) — empty for now

---

## END-OF-DAY REPORT FORMAT

**Tonight before bed (or tomorrow morning before gym), message me with this exact format:**

```
DAY 1 REPORT — May 8

Setup tasks completed: __ / 9
- Task 1 (Khoury email): ✅ / ❌
- Task 2 (outreach list, 12 targets): ✅ / ❌ (got __ targets)
- Task 3 (apps list, 8 JDs): ✅ / ❌ (got __ JDs)
- Task 4 (LeetCode setup): ✅ / ❌
- Task 5 (alarm clock + phone protocol): ✅ / ❌
- Task 6 (GitHub cleanup): ✅ / ❌
- Task 7 (av-policy-lab repo): ✅ / ❌
- Task 8 (nuPlan vs CARLA decision): ___ (which one)
- Task 9 (Karpathy Lecture 1 preview): ✅ / ❌

Sleep: in bed by __:__ PM
Phone in kitchen: ✅ / ❌

What blocked me: [1–2 sentences]
What surprised me: [1 sentence]
Energy level (1-10): __
What I want different tomorrow: [1 sentence]
```

That's it. I'll calibrate Day 2 based on this.

---

## WHY DAY 1 IS THIS LIGHT

You might feel like "I should be doing more on Day 1." Resist this.

Day 1 is environment setup. If you do this right, Days 2–7 just *execute* — no friction, no decisions, no "wait, I need to find that JD link first." Most people fail their plans not because the plan is wrong, but because every day they have to re-decide what to do. **You're eliminating that decision cost tonight.**

Tomorrow morning at 8:30 AM you wake up, gym, breakfast, then sit down and just start Karpathy Lecture 1 type-along. No deciding. No setup. Just work.

---

## TONIGHT'S ONE BEHAVIORAL ANCHOR

**Phone in kitchen at 10:30 PM. Laptop closed at 10:30 PM. In bed by 11 PM.**

If you only do this and skip half the setup tasks, the week still works. If you do all 9 setup tasks but stay up till 1 AM, the week breaks.

**Sleep > tasks. Always.**

---

**Print this. Cross items off as you go. Report tonight or tomorrow morning.**

**Day 2 plan comes after I see your report.**
