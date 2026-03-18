The skill file has been written to `judge_training/skills/topics/_gen_world_models/skill_world_models.md`.

Here's a summary of what I produced based on reading 10+ review JSONs across the rating spectrum:

**Structure (following the required output format):**

1. **Topic Overview** — 8 sub-areas (MBRL, autonomous driving, causal/structured, long-horizon, LLM-based, offline/pretrained, generative, theoretical), key challenges, calibrated score distribution (mean 4.91, 70.4% acceptance)

2. **What Reviewers Praise** — Grounded in real quotes from R2I (8.0 Oral), LS-Imagine (8.0 Oral), NCRL (8.0), and causal world models paper (8.0 Oral). Key themes: novelty, comprehensive baselines, thorough ablations, clarity, reproducibility

3. **What Reviewers Criticize** — Real quotes from SelfDreamer (4.0 Reject), DrivingWorld (4.5 Reject), and the conceptual "What is a World Model?" paper (4.75 Reject). Key failure modes: missing baselines, incremental novelty, limited scope, unfair comparisons

4. **Required Baselines & Metrics** — Explicit table of must-compare baselines (DreamerV3, TD-MPC2, MBPO, etc.), domain-specific benchmarks (DMControl, Atari 100K, Memory Maze, nuScenes), and metric expectations

5. **Common Technical Pitfalls** — 8 specific pitfalls with real reviewer quotes: ignoring the Dreamer ecosystem, conflating world model quality with policy performance, distribution shift, over-engineering, insufficient seeds

6. **Scoring Rubric** — Concrete descriptions of 3/5/7/9-tier papers with real examples from the dataset

7. **Key Papers & Expected Citations** — Foundational papers table, sub-area specific citations, and a "red flag: citing only old baselines" warning

8. **Quick Scoring Heuristics** — A summary table with +/- score impacts for common signals