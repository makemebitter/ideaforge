The skill file has been written to `judge_training/skills/dimensions/_gen_clarity/dim_clarity.md`. Here's what it covers:

1. **What clarity means** — a precise definition scoped to communication quality (not correctness or originality), with a breakdown of the layers reviewers assess (structure, motivation, technical precision, figures, language, reproducibility).

2. **Score 1 (Poor)** — systemic failures: incomprehensible method sections, missing related work citations, undefined notation. Grounded in the BINR-MAPF score-1 examples where related work named but didn't cite methods.

3. **Score 2 (Below average)** — localized but notable gaps: missing inference cost analysis (CAT, 3 reviewers converging), unspecified benchmark construction (T2VTextBench), theory simplifications not flagged (Prefix-tuning). The pattern of *multiple reviewers independently citing the same gap* is highlighted as a strong score-2 signal.

4. **Score 3 (Good)** — fully followable, reviewer concerns shift to content not comprehension. Grounded in the Prefix-tuning ("clearly written") and Linearly Decoding ("mostly easy to follow") examples.

5. **Score 4 (Excellent)** — rigorous + intuitive + actively guiding. Grounded in Barely Random Algorithms ("a lot of intuition and high-level guiding") and AlgoPerf (sole weakness: one typo).

6. **Red/Green flags** — concrete signal table for rapid scoring decisions, including ambiguous signals and how to interpret hedged reviewer language.

7. **Cross-topic patterns** — calibrated expectations for theory, empirical ML, benchmark, safety/alignment, and systems papers.

8. **Scoring procedure** — a 5-step process the judge can apply mechanically.

9. **Quick reference card** — a compact cheat sheet with score summaries and anchoring examples.