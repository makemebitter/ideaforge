The skill file has been written to `judge_training/skills/topics/robustness_safety.md`. Here's a summary of what it covers:

**Structure (approx. 4,500 words / ~12K tokens):**

1. **Statistical context** — score distribution, acceptance rate calibration, what the 80% acceptance rate actually means for quality thresholds

2. **Subtopic landscape** — 8 distinct sub-areas (LLM safety alignment, adversarial attacks, backdoor, differential privacy, fairness, distribution shift, privacy/memorization, AI safety for generative models) with key papers cited for each

3. **What excellence looks like (8-10)** — grounded in the top-rated paper (9.5): unifying hypothesis, full empirical arc, comprehensive multi-model/multi-attack experiments, clear threat model, safety-utility trade-off

4. **Good but not excellent (6-7.5)** — three distinct profiles: incomplete baselines, negative results, theoretical methods with presentation gaps

5. **Common failure modes** — six patterns: limited novelty, unrealistic threat models, engineering without research, weak theory with overclaiming, benchmark without motivation, missing baselines

6. **Evaluation metric standards** — per-subtopic standards (GPT-4 judge vs. keyword ASR, AutoAttack vs. PGD, formal DP guarantees, fairness metrics)

7. **Novelty calibration** — what counts vs. what doesn't, borderline cases

8. **Score calibration table** — with real paper examples grounding each tier

9. **Adversarial evaluation questions** — 8 questions to stress-test any research idea in this area

10. **Known pitfalls** — per-subtopic failure modes that are hard to catch without domain knowledge