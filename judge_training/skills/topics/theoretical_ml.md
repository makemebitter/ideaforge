The skill file has been written to `judge_training/skills/topics/_gen_theoretical_ml/skill_topic_theoretical_ml.md`.

Here's what it covers, grounded in real reviewer data from 2,238 papers across ICLR 2024–2026 and NeurIPS 2023–2024:

**8 sections with real reviewer quotes:**

1. **Topic Overview** — 12 subtopics (PAC learning, kernel methods, NN theory, high-dimensional stats, RL theory, operator learning, etc.); score distribution (mean 4.97, 83.2% acceptance, only 38 "excellent" papers)

2. **What Reviewers Praise** — 7 categories with real quotes:
   - Resolving open problems (e.g., "This is a breakthrough paper" for the span-based MDP complexity paper)
   - Tight matching upper/lower bounds (holomorphic operators paper)
   - Novel connections between areas (Meta-CL ↔ regularization-based CL via Hessian)
   - Counterintuitive results (biased > unbiased subsampling)
   - Unifying frameworks (spectral profile for KRR + GD)
   - Accessible writing despite technical depth
   - Theory validated by experiments

3. **What Reviewers Criticize** — 10 failure modes with real quotes:
   - Incorrect/hand-wavy proofs (including LLM-generated math concerns)
   - No ML relevance (Gompertz curve paper)
   - Trivial theorems (marginalization presented as main result)
   - Not self-contained (relying on concurrent submissions)

4. **Required Baselines & Metrics** — by subarea (PAC, kernel, NN theory, RL, continual learning, domain generalization, operator learning)

5. **10 Technical Pitfalls** — proof-at-optimum-only, gradient flow vs. discrete, undefined notation, etc.

6. **Scoring Rubric** — anchored to real papers at each tier (1.33, 5.0, 7.75, 8.67 rated papers)

7. **Key Papers & Expected Citations** — ~30 foundational works reviewers expect

8. **Quick-Reference Checklist** — correctness, novelty, scope, relevance, presentation, red flags