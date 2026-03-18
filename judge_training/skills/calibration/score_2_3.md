The calibration skill file has been written to `judge_training/skills/calibration/_gen_score_2_3/calib_score_2_3.md`.

Here's what it covers, all grounded in real papers and reviewer quotes:

**Structure:**
1. **Score Range Profile** — What avg 1.5–3.0 means at ICLR/NeurIPS, typical decision (overwhelmingly Reject), and prevalence (~30–40% of submissions)

2. **8 Real Paper Examples** with detailed analysis of *why* each landed at this score:
   - *Coauthor Nomination* — technical triviality (LP→flow is textbook)
   - *AlphaZero Battlefield* — pure application with no novelty
   - *SFT Without Overfitting* — incremental empirical, missing theory
   - *Curvature Meets Bispectrum* — impenetrable math, suspected LLM-written proofs
   - *Opal (RLHF)* — extreme reviewer split (3×0 + 1×6), accepted despite avg 1.5
   - *SAFE RAG Framework* — engineering without novelty, outdated baselines
   - *Cascade of Experts* — limited novelty, no baselines, distribution shift failure
   - *Logo-LLM Time Series* — incremental modification of GPT4TS

3. **Common Traits** — The 6 recurring failure modes: novelty deficit, missing baselines, narrow experimental scope, presentation failure, unrealistic assumptions, venue mismatch

4. **Tier Differentiation** — How to distinguish 2–3 from score 1 ("complete failure") and score 4–5 ("borderline")

5. **10 Justification Templates** (A–J) grounded in real reviewer patterns, ready to use when scoring