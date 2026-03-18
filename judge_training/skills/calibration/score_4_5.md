The calibration skill file has been written to `judge_training/skills/calibration/_gen_score_4_5/calib_score_4_5.md`.

Here's what it covers:

## File Summary

**~5,200 words / ~8,000 tokens** — within the 5–15K target.

### Structure:

1. **Score Range Profile** — Explains that score 4–5 maps to ICLR's ~3.5 average rating (mix of 2s, 3s, 4s), the borderline accept/reject zone (~50/50 in this dataset).

2. **8 Real Paper Examples** with full reviewer quote analysis:
   - *Latent Lookahead* (Accept) — generalization gap: Sudoku works, GSM8K fails
   - *MidCut* (Accept) — crowded field, narrow model coverage
   - *LLM as GNN* (Reject) — overclaiming "universal" graph model
   - *QJL* (Reject) — "zero overhead" claim is factually wrong
   - *PromptKeeper* (Reject) — definitional flaw: zero MI = useless system prompt
   - *Hijacking JARVIS* (Reject) — unclear novelty over pop-up attacks
   - *Holistic Prompting* (Reject) — exact-match reuse kills generalization
   - *AnyCap* (Reject) — derivative of Aligner, engineering not research

3. **7 Universal Traits** with tier comparison table (score 2–3 vs 4–5 vs 6–7)

4. **10 Justification Templates** each grounded in specific reviewer quotes

5. **Decision Rubric** — 5-item checklist

6. **Anti-Patterns** — what to avoid conflating with score 4–5

7. **Calibration Summary Table** — one-line failure mode per paper