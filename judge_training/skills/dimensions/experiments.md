Written to `judge_training/skills/dimensions/_gen_experiments/dim_experiments.md`. The skill file covers:

1. **Definition & scope** — what "experiments" means in peer review, what reviewers look for, and the theory-paper exception
2. **Score 1 (Poor)** — missing/outdated baselines, toy-only evaluation, unmeasured efficiency claims; grounded in BINR-MAPF and T2VTextBench quotes
3. **Score 2 (Below Average)** — present but incomplete experiments; key metrics absent despite being central to claims; grounded in CAT, T2VTextBench, Linearly Decoding Refused Knowledge
4. **Score 3 (Good)** — solid core experiments with identifiable but minor gaps; grounded in Prefix-tuning and BINR-MAPF mid-tier reviews
5. **Score 4 (Excellent)** — exemplary or theory-justified absence; grounded in AlgoPerf, Barely Random Algorithms, GLinSAT
6. **Red & Green Flags** — instant pattern-matching signals for quick calibration
7. **Cross-topic patterns** — different expectations for empirical ML, theory CS, NLP, robotics, benchmark, and fairness papers
8. **Calibration table**, **decision tree**, and **worked examples** for reliable scoring