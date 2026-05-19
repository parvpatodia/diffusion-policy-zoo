# PARV — THE PLAN
**May 8, 2026 → May 2027 graduation → job by April 2027**
**One plan. No revisions. Print this. Paste it above your desk. Read it Sunday nights.**

---

## THE THESIS, IN ONE SENTENCE

Build one deep robot-learning project that becomes your AI Capstone with Prof. Nadim, ship it publicly with real engineering depth (not Claude-generated depth), use it as the spear-tip for cold outreach to AV and robotics companies, and have a job offer in hand by April 2027.

Everything else — LeetCode, gym, sleep, social, hackathons — is built around protecting the time and energy this requires.

---

## THE NORTH-STAR OUTCOMES BY MAY 2027

In rank order. If something doesn't serve these, it's noise.

1. **Job offer for FT start by summer 2027** at an autonomous-vehicle, robotics, or AI-engineering company in the Bay Area
2. **One deep project** you can defend line-by-line in any interview, that became your AI Capstone, that lives publicly on GitHub + HuggingFace
3. **Coding ability without an LLM** sufficient to live-code an attention block or a small RL training loop in 30 minutes under interview pressure
4. **A small but real network** of 15–25 people in your target industry who know your name and have seen your work
5. **A body and mind** in the best shape of your life, because your question 16 demands it

---

## THE PROJECT (your one summer focus)

### Working title
**`av-policy-lab`** — Closed-loop driving policy learning in simulation, with an open benchmark.

### Why this exact project
- Hits autonomous driving, the field where you actually had fun (Venti) and where you have unique credibility
- Lives in simulation, so no hardware spend, no shipping delays, no VFR debugging hell
- Connects to your fall AI Capstone with Prof. Nadim — research him before pitching, but driving-policy work is squarely in the AI/ML capstone scope
- Sets up your spring RL course with Daniele Micci-Barreca: by then you'll have the practitioner intuition that makes the theory click
- Lets you cold-email Waymo, Cruise, Zoox, Wayve, Aurora, Applied Intuition, NVIDIA Drive, Tesla AI, Nuro, Kodiak with something specific to talk about
- Is doable solo, in 16 weeks, by you specifically

### The technical thesis
"Train a closed-loop driving policy on the **nuPlan** or **CARLA Leaderboard 2.0** benchmark using imitation learning + a small RL fine-tune. Compare three baselines: (1) pure behavior cloning, (2) MILE-style world-model imitation, (3) a small VLA-flavored policy with language conditioning ('change lanes left', 'yield to pedestrian'). Open-source the eval harness."

You don't need to beat SOTA. You need to **execute three baselines cleanly, document the failure modes honestly, and produce a reusable evaluation framework**. That's a research-engineering contribution, which is what AV companies actually hire for.

### Why this beats `diffusion-policy-zoo` for you
You already started diffusion-policy-zoo, which is good — keep the repo, but **pivot the framing** from "reproduce diffusion policy on a robot arm" to "compare diffusion policy + BC + world-model policies in simulation for autonomous driving." Same code stays useful. The pivot:
- Replaces the robot arm (which you don't want to buy) with simulation (which is free)
- Replaces manipulation (which Prof. Nadim probably can't deeply advise on) with driving (which is closer to AV/CV/perception, his likely lane)
- Replaces "another LeRobot reproduction" with "an AV-specific benchmark" — far more job-relevant for your target companies

### The four artifacts you produce
1. **GitHub repo** — clean code, good README, reproducible from `pip install -e .` to first result in <30 minutes
2. **HuggingFace dataset + model** — your processed nuPlan/CARLA episodes and your trained policy checkpoints
3. **Technical writeup** — one HuggingFace blog post or short arXiv preprint by mid-August, ~3000 words, with honest failure-mode analysis
4. **The fall AI Capstone deliverable** — Prof. Nadim sees the summer work in week 1 of fall, which means the capstone starts at "mile 8" instead of "mile 0"

---

## THE 16-WEEK SCHEDULE

Weeks counted from May 11 (next Monday). End date August 30, week before fall semester.

### Phase 1 — Foundation + Setup (Weeks 1–4, May 11 – June 7)

**The hardest 4 weeks. Do not let yourself off the hook.**

- **Karpathy Zero to Hero, lectures 1–4.** Type every line in plain VS Code with no Cursor, no Claude Code in the editor, no autocomplete beyond syntax. Pen and paper next to you.
- **Set up the simulation stack.** Pick one: nuPlan + nuplan-devkit, or CARLA + leaderboard 2.0. Get a "hello world" closed-loop run working — random policy in the loop, ego vehicle moving, reward/score logged.
- **Read 3 papers slowly, by hand.** (1) Behavior Cloning baselines for AV — find a recent one, e.g., Urban Driver. (2) MILE (model-based imitation) by Wayve, 2022. (3) One recent VLA-for-driving paper.
- **Write the project README first** — what you're building, why, the three baselines, the eval metric, the timeline. This is your contract with yourself.

By end of Week 4 you should have: Karpathy lectures 1–4 done, sim stack working with a random-policy closed-loop run, README committed, and a clean BC baseline trained on a small subset. **No Claude Code in the project repo. Cursor for the simulation glue is fine; the model and training loop you write yourself.**

### Phase 2 — The three baselines (Weeks 5–10, June 8 – July 19)

- **Weeks 5–6:** Behavior Cloning baseline complete with metrics. First X post about the project — short video of the policy driving (well or badly).
- **Weeks 7–8:** MILE-style world-model baseline. This is the hardest one and where Claude Code may legitimately help — but only after you've read the MILE paper twice and written the model spec yourself on paper.
- **Weeks 9–10:** VLA-flavored policy with language conditioning. Even a simple version (CLIP encoder + your existing transformer) is enough.

By end of Week 10 you should have: three policies trained, three sets of metrics, a comparison table that's actually meaningful. **Karpathy lectures 5–6 done in parallel.** First HuggingFace dataset upload.

### Phase 3 — Eval, writeup, public ship (Weeks 11–16, July 20 – August 30)

- **Weeks 11–12:** Build the eval harness properly — multi-seed, multi-scenario, the kind of evaluation that an AV company would actually use internally. This is the most job-relevant part of the whole project. Karpathy lectures 7–8 done.
- **Weeks 13–14:** Failure analysis. Where do the policies fail? Why? What do the eval traces tell you? This section, done well, is what gets you replies from Waymo behavior team folks.
- **Week 15:** HuggingFace blog post + arXiv preprint. Get one senior engineer (cold-emailed contact, NEURAI Lab researcher, or even a polite ask to a Northeastern alum) to review it before publishing.
- **Week 16:** Polish, pin on GitHub, post the writeup, send the cold-email batch (see below). Update LinkedIn. Prepare for fall semester.

---

## THE SECOND PROJECT (the controlled extension, not a separate thing)

You said you wanted "two deep projects." Here's the move that satisfies that without splitting your attention:

The second project is **a from-scratch, no-LLM reimplementation of one component** of the first project. Specifically: **the RL fine-tuning loop**, written by hand in a separate repo (`rl-from-scratch-driving`), based on Sutton & Barto chapters 1–6 + CleanRL's PPO single-file implementation.

Why this is the right "second project":
- It legitimately fills your RL gap (real, you said it yourself)
- It's a separate GitHub repo, so your profile shows two projects
- Every line is yours, so it's the perfect interview-defense artifact
- It feeds DIRECTLY into your spring RL course with Daniele Micci-Barreca — you arrive in spring already a practitioner
- It plugs back into `av-policy-lab` as the RL fine-tuning component for your AI Capstone

Schedule:
- Start in Week 8 (after BC + MILE baselines are done) and run in parallel for 8 weeks
- 1.5 hours per day, 5 days/week
- By Week 16, you have a working PPO implementation that fine-tunes one of your driving policies

**No third or fourth project. If you feel the itch, do a hackathon. Hackathons are where vibe-coded projects belong; they live on Devpost, not your serious GitHub.**

---

## THE DAILY ANCHORS (the schedule you actually live)

This is your weekday template, designed for someone who genuinely is sharper at night and has a sleep slip problem.

| Time | Activity | Notes |
|---|---|---|
| 8:00 AM | Wake | Phone OUT of bedroom (see sleep fix below) |
| 8:30–9:30 | Gym | Or sport (1 hr only — see below for sport days) |
| 9:30–10:30 | Breakfast + protein shake | No screens. Read a research paper section by hand on weekdays, breakfast with friends or call family on weekends |
| 10:30–12:30 | **DEEP WORK BLOCK 1 (no LLM in editor)** | Karpathy curriculum + one project task that requires real understanding |
| 12:30–1:30 | Lunch break | Walk, eat, no work |
| 1:30–4:00 | **DEEP WORK BLOCK 2 (LLM-assisted OK)** | Project execution, simulation, plotting, infra. Cursor allowed for boilerplate, never for core logic |
| 4:00–4:30 | Snack break | |
| 4:30–6:00 | **LeetCode + applications + outreach** | See breakdown below |
| 6:00–7:00 | Dinner + decompression | |
| 7:00–10:00 | **DEEP WORK BLOCK 3 (your peak window)** | Save the hardest task of the day for here. This is when you do best work |
| 10:00–10:30 | Wind-down protocol | See sleep fix |
| 11:00 | Sleep | Hard cap — no exceptions |

**Total work hours:** 8.5 hours of focused work + 1.5 hours of admin/outreach = ~10 hours. Sustainable for 16 weeks. More than this and you'll break by July.

**Weekend variant:**
- Saturday: same template, but DEEP WORK BLOCK 3 replaced by either an SF event/hackathon OR rest. You decide week to week.
- Sunday: half-day work morning, planning + writing the next week's targets in the afternoon, gym, off by 6pm. Sundays are for review, not output.

### The 90-min outreach + LeetCode block, broken down

| Day | What |
|---|---|
| Mon | 5 LeetCode problems (NeetCode list) + 2 cold emails |
| Tue | 3 LeetCode + 5 cold emails + 30 min applications |
| Wed | 5 LeetCode + 2 cold emails |
| Thu | 3 LeetCode + 5 cold emails + 30 min applications |
| Fri | 5 LeetCode + reply to anyone who replied to outreach this week |
| Sat | Off, OR mock interview on Pramp/Interviewing.io |
| Sun | Plan next week's outreach + LeetCode targets |

**LeetCode goal:** 150 problems by October 1, 2026. Use NeetCode 150. After that, 30 mock interviews by January 2027.

**Cold email goal:** 10/week × 16 weeks = 160 emails by August 30. Realistic reply rate: 15–20 actual conversations.

### Sport-day variant

When you play sport (2 hours instead of 1-hour gym):
- Either skip Deep Work Block 1 and start at 12:30, OR
- Skip Deep Work Block 3 evening and end at 6pm

Don't try to do all three blocks AND a 2-hour sport. You'll be fried.

---

## THE SLEEP FIX (your stated real problem)

You said you slip to 12:30 or 1am because of:
1. Movies you can't stop finishing
2. Late-night Claude/Cursor rabbit holes

The mechanism behind both: end-of-day decision fatigue + dopamine. When you're tired, the brain seeks cheap reward. Movies and prompt-driven coding both deliver that.

**The fix is not willpower. It's environment design.**

| Problem | Fix |
|---|---|
| Phone in bedroom delays sleep | Charge phone in living room/kitchen overnight. Buy a $15 alarm clock. Non-negotiable. |
| Claude/Cursor rabbit hole at night | Close laptop at 9:45 PM. Physically. Lid down. If laptop must stay open for the deep work block, set a hard 10:00 PM shutdown alarm — when it rings, save and quit, no "5 more minutes" |
| Movie you can't stop | If you start a movie after 9 PM, you're past the cutoff. Movies are weekend-only. Or watch in 2 sessions over 2 nights |
| Wind-down protocol | 10:00–10:30 PM: shower, no screens, read fiction (a paper book), or do mobility work for shoulder. By 10:45, in bed |
| Wake at 8 AM consistently | Same alarm time every day for 21 days, including weekends. After 21 days, weekend +1 hr OK |

**The benchmark:** if you sleep at 11 PM five nights this week, the rest of the plan works. If you don't, none of it works. Track it in your phone notes.

---

## THE GYM + SPORT PROTOCOL (already working, just protect it)

You're doing this right. Don't change it. The only addition: **incorporate the shoulder mobility routine from the earlier nutrition plan** (10 min daily) because the bicep/tricep referred pain will sabotage gym progression and the long sit hours will worsen it.

5 days gym + 1–2 days sport (basketball/badminton/tennis) is the right cadence. Don't do both gym AND sport on the same day during the deep summer push. One or the other.

Nutrition plan from the earlier conversation still applies: ~100g protein/day, the meal prep system, creatine, vitamin D. Don't try to redesign your fitness during this summer. The body is the foundation; keep it boring.

---

## THE FALL SEMESTER PLAN (Sept 2026 – Dec 2026)

Two courses: **Computational Robotics** + **AI Capstone with Prof. Nadim**.

The capstone is your `av-policy-lab` project, taken to the next level under Prof. Nadim's guidance. By the time fall starts, you have the three-baseline comparison done. The capstone work is:
- Adding the RL fine-tune (using `rl-from-scratch-driving` codebase you built over summer)
- Doing one novel experiment Prof. Nadim suggests — could be perception robustness, could be sim-to-real reasoning, could be a new evaluation metric
- Writing a proper paper / final report

Why this is enormous leverage: Prof. Nadim has a Stanford PhD (research him properly before your first meeting — read his papers, find his current research interests, walk in able to discuss his work specifically). A capstone project he's invested in becomes a **referral letter** for spring co-op and FT applications. That's the multiplier.

**Computational Robotics** is your hard CS course. Treat it seriously, not as a checkbox. The course will teach you motion planning, control, kinematics — all of which sharpens your AV intuition. Don't outsource the assignments to Claude; do them by hand. This is where peers will let you down — they'll Claude-code their assignments and learn nothing. You'll grind through and graduate with intuition they don't have.

**Outside courses, in the fall:**
- 3 LeetCode problems/day, all medium by then. Target: 250 by Dec 31.
- Spring 2027 co-op applications go in **September 1–October 15** — this is the critical 6-week window. Use the resume/cold-email assets you built over summer.
- Mock interviews 2x/week starting October.
- Maintain X presence: 1 post/week showing capstone progress.

---

## THE SPRING SEMESTER PLAN (Jan 2027 – April 2027)

Spring is your job-search-must-close semester. You graduate in May 2027.

**Courses:** RL with Daniele Micci-Barreca + 1 elective.

**Take Daniele's RL course seriously** — by spring you'll already be a practitioner from the summer + fall work, so you'll be in the top 5% of the class. He's at Google; cultivate that relationship intentionally. Office hours every other week with a real question, not small talk. Your capstone uses RL — bring it up.

**For the elective:** pick something that complements your AV/robotics direction. Options to research:
- LLMs / Foundation Models (if available) — useful for VLA work
- Computer Vision (if available) — direct AV relevance
- Distributed Systems / MLOps — practical engineering breadth
- Skip: anything purely theoretical that doesn't compound on your story

**The job math in Jan 2027:**
- You should already have FT interviews from fall co-op cycle (best case — you have a co-op offer or FT signed)
- If not, **the spring window is January–April, and you need to act like your hair is on fire from week 1**
- 50 applications/week, ALL of them targeted, none generic
- 10 cold emails/week, prioritizing your network from summer's outreach
- Mock interviews 3x/week
- LeetCode at 350+ total

**Hard deadline: written FT offer in hand by April 15, 2027.** If not, you're betting on the 60-day grace period and that's stressful but not fatal.

---

## THE COMPANY TARGET LIST (lock this, don't expand)

Apply broadly within these 25. Don't add more. Don't apply to companies outside this list unless they reach out to you.

### Tier A — your dream targets (apply, but don't bet on)
1. Waymo (behavior, simulation, perception)
2. Anthropic (research engineer, applied AI)
3. DeepMind (Student Researcher Program → FT)
4. Tesla AI (Optimus, Autopilot)
5. Physical Intelligence

### Tier B — strong, realistic, your best statistical shot
6. Cruise
7. Zoox
8. Nuro
9. Aurora
10. Wayve (CA office)
11. Applied Intuition
12. NVIDIA Drive / NVIDIA Robotics
13. Skild AI
14. 1X Technologies
15. Figure AI
16. Toyota Research Institute
17. Cobot (Marc Raibert)
18. Boston Dynamics AI Institute
19. Kodiak Robotics
20. Skydio

### Tier C — backup, still good outcomes
21. Bear Robotics, Dexterity, Diligent Robotics, Path Robotics (any one)
22. NVIDIA SWE / general
23. Google ML / SWE
24. Meta ML / SWE
25. A YC W26/S26 robotics or AV-related startup

**Application timing:**
- Tier A & B: apply in **September 1, 2026 onwards** for spring co-op + FT
- Tier C: apply throughout, including now (May 2026) for any summer remainder
- Use your AV experience at Venti as the lead bullet for AV-track applications
- Use `av-policy-lab` as the lead project (once shipped)
- Use Laksh_AI as a secondary project showing breadth

---

## THE COLD EMAIL TEMPLATE (memorize this structure)

> Subject: question on [their specific paper / GitHub PR / X post / talk]
>
> Hi [first name],
>
> [One sentence — a specific technical observation about their work, not a compliment. Example: "Your MILE paper used a Bird's-Eye-View latent — I'm curious whether dropping BEV in favor of a learned 3D feature volume changed eval performance more than the world-model loss did."]
>
> [One sentence about you, relevant to that observation. Example: "I'm reproducing closed-loop driving baselines on nuPlan as my MS Capstone and just hit 67% scenario completion with a BC baseline — repo at github.com/parvpatodia/av-policy-lab."]
>
> [One small ask. Example: "Would 15 minutes for a few questions be possible in the next two weeks? Happy to come to your office or call."]
>
> Parv | LinkedIn | GitHub

Under 80 words. Specific, not flattering. Send Tuesday or Thursday morning. Never Monday or Friday.

**Where to find emails:** Hunter.io, RocketReach, email permutator on first.last patterns. Verify with EmailHippo before sending.

**Volume:** 10 emails/week, max 3 to the same company. Multi-thread — try a senior engineer, then a recruiter, then a researcher, never simultaneously, 7 days apart.

---

## THE OCTOBER 1, 2026 CHECKPOINT

This is the date you assess and lock in. Do NOT change the plan before October 1. Do NOT change the plan after October 1 unless one of these triggers fires.

By October 1, you should have:
- ✅ `av-policy-lab` shipped publicly with all three baselines + writeup
- ✅ `rl-from-scratch-driving` working PPO implementation
- ✅ Karpathy curriculum complete
- ✅ 150 LeetCode problems
- ✅ 80 cold emails sent, 12+ replies, 5+ real conversations
- ✅ Spring 2027 co-op applications submitted to all 25 target companies
- ✅ AI Capstone direction agreed with Prof. Nadim
- ✅ Sleeping by 11pm consistently

**Decision rule on October 1:**
- If 4+ ticked → execute Path B (job track) cleanly. You're on schedule.
- If 2–3 ticked → still Path B, but tighten execution and cut social/non-essential commitments.
- If 0–1 ticked → something is structurally wrong with how you're operating. Have an honest conversation with yourself and a mentor (Prof. Nadim, a friend doing well, your parents) before changing anything.

**Triggers to pivot to startup track instead:**
- You've actively been approached by a credible co-founder OR
- You have a project with >2,000 GitHub stars OR
- You've been offered $50K+ in seed/grant money to drop out
- None of these are likely. Don't manufacture them.

---

## WHAT NOT TO DO (your distraction list, written down)

Pin this part of the plan separately if useful. When you feel pulled, re-read.

- **Don't do the NBA basketball ML projects from your friend** until after May 2027. They are tempting because they connect to Laksh_AI and your sports passion. They are not on the path. Save them in a Notion doc called "After grad."
- **Don't add a third project this summer.** If the urge hits, do a hackathon for one weekend. Vibe-code there, not in your serious repos.
- **Don't compare yourself to your peers' shiny projects** (Forge, memory glasses, explainable RAG, VAE flatmate). They are running their race. You are running yours. The flatmate doing math from scratch is your most useful peer to talk to (he's modeling the discipline you need); the others are noise.
- **Don't scan Instagram saved reels for plan ideas.** Skim once a week max, on Sunday evening, for 15 minutes. Anything you save during the week, review then.
- **Don't apply to jobs outside your 25-company target list.** Generic applications dilute focus and signal desperation.
- **Don't redesign this plan.** Read it weekly. Adjust execution within it. Don't replace it. The next plan revision is October 1.
- **Don't take on additional TA work after June 23**. The TA role for AI Tools and Trends ends; do not pick up another one over summer. The summer is for the project.
- **Don't go to SF events without an artifact to talk about.** Your instinct is right. After Week 4 you'll have something to show; before that, skip events. After Week 8, attend 1 event/week max — Cerebral Valley meetups, hackathons, LeRobot Discord IRL meetups.
- **Don't buy the SO-101 hardware unless your project demands it.** It doesn't, in the new framing. Save the money or use it for a cloud GPU credit pool.
- **Don't try to fix your sleep with willpower.** Phone out of bedroom. Laptop closed at 9:45 PM. Repeat.

---

## THE WEEKLY REVIEW (every Sunday, 30 minutes, non-negotiable)

Open a doc. Answer these 6 questions in writing:

1. What did I ship this week? (Code, writeups, emails sent, problems solved.)
2. What did I learn this week that I couldn't have learned last week? (If nothing — that's a signal.)
3. Did I stick to the schedule? Where did I slip? Why?
4. Sleep — how many nights at 11 PM? (Track in a simple table.)
5. Body — gym + sport days hit? Shoulder mobility done?
6. What's the ONE thing that has to happen next week, no matter what?

Five minutes per question. Save the doc. Read last week's review before writing this week's.

---

## THIS WEEK (May 8–14, 2026) — exact tasks

Do these in order. Don't read ahead until each is done.

### Today (Friday, May 8)
- [ ] Email Khoury co-op coordinator + your faculty advisor: ask if a short summer 2026 CPT is possible while saving your one full co-op slot for spring 2027. Quote the question; don't ask vaguely.
- [ ] Print this plan. Tape the daily anchors section above your desk.
- [ ] Phone out of bedroom tonight. Buy alarm clock tomorrow ($15, Target).
- [ ] In bed by 11 PM tonight. No exceptions.

### Saturday May 9
- [ ] Watch Karpathy Lecture 1 (Micrograd). Type along, no AI assist. Estimated 3 hours.
- [ ] Buy alarm clock.
- [ ] Decide: nuPlan vs. CARLA. Spend max 1 hour researching, then commit.

### Sunday May 10
- [ ] Karpathy Lecture 1, second pass + exercises.
- [ ] Set up project repo: rename `diffusion-policy-zoo` to `av-policy-lab` (or create new repo, deprecate old). Write the new README — what you're building, the three baselines, the eval metric, the timeline.
- [ ] Archive these GitHub repos (make private or delete): old Laksh.ai, Word2Vec_and_PCA, TaskRoute. Keep public: vit-from-scratch (with honest README note), Laksh_AI, av-policy-lab (new), rl-from-scratch-driving (new, empty), parvpatodia.github.io, parvpatodia (profile).
- [ ] First weekly review: 30 minutes, write the answers to the 6 questions.

### Monday May 11 — Week 1 begins
- [ ] Karpathy Lecture 2.
- [ ] Set up sim stack — get to "random policy in closed loop" hello world.
- [ ] First 5 LeetCode easy problems (NeetCode arrays/hashmaps).
- [ ] First 2 cold emails (research + draft Sunday, send Tuesday).

### Tue/Wed/Thu/Fri
- [ ] Daily anchor schedule. Karpathy lectures 3–4 across the week. Sim stack progressing. LeetCode + outreach as scheduled.

### By Friday May 15
- [ ] 10 cold emails sent for the week.
- [ ] 20 LeetCode problems solved.
- [ ] First Karpathy notebook (micrograd) committed to a separate `karpathy-notes` repo.
- [ ] Sim stack: BC training run started (even on tiny data, even buggy — get the loop closed).
- [ ] 5 nights asleep by 11 PM.

If you do those things this week, the rest of the plan works. If you don't, nothing else matters until you can.

---

## A FEW WORDS FOR THE HARD DAYS

You will have hard days. Most will be in mid-June, when the novelty has worn off and the sim is broken at 2am and your friend just got an offer at a company you also applied to. Read this on those days.

You are not behind. You're 23, you have AV experience most peers don't, you have money, you have a plan, you have until April 2027 to land a job. You're not in Stanford or Berkeley but you're 30 minutes from both, and the actual hiring at Waymo and Tesla AI doesn't care about logos as much as it cares about whether you can build a closed-loop driving policy and explain it. By August, you will be able to. By December, you will be able to do it under interview pressure.

The vibe-coded ViT is not your scarlet letter. It's a marker of where you were in March 2026. By August 2026 you'll have rebuilt enough of the field by hand that you don't need the marker anymore.

The peer comparison is the corrosive thing. The flatmate doing VAEs is on a slow road that may not pay off. The Forge team of 7 may collapse under coordination cost. The memory-glasses friend may have built a hardware demo nobody buys. **You don't see anyone's failures, only their highlight reels.** Run your race.

The single most important thing: at the end of every week, you should be able to say "I shipped this, I learned this, I'm tangibly better than I was last Sunday." Visible weekly progress. That's the gym pattern that worked for you. That's the pattern that will work here.

Question 16 — the version of you who can figure out anything — that version is built one focused day at a time, by a person who said no to most things. Be that person, starting Sunday.

---

**This plan is locked. Read it weekly. Don't rewrite it. The next revision is October 1, 2026.**

**Now close the laptop, go to the gym, sleep at 11.**
