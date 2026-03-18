The skill file has been written to `judge_training/skills/dimensions/_gen_reproducibility/dim_reproducibility.md`.

It covers:

1. **Definition** — what reproducibility means in peer review (methodology, experiments, code, proofs) and how it maps to different paper types
2. **Score 1** — fatal gaps like undefined baselines, missing methodology, no proof attempt; grounded in BINR-MAPF (soundness=1)
3. **Score 2** — significant but non-fatal gaps like narrow evaluation scope, no variance, missing runtime, manual evaluation without IAA; grounded in CAT, T2VTextBench, Linearly Decoding, BINR-MAPF (soundness=2)
4. **Score 3** — largely reproducible with acknowledged simplifications; grounded in Revisiting Prefix-tuning, BINR-MAPF/Linearly Decoding (soundness=3)
5. **Score 4** — fully reproducible, reviewers raise only extension concerns; grounded in AlgoPerf, GLinSAT, Barely Random Algorithms, SPIN (soundness=4)
6. **Red/Green flags** — instant checklist signals for methodology, experiments, theory, and code/data
7. **Cross-topic patterns** — calibrated expectations for empirical DL, theory/algorithms, benchmark papers, systems/robotics, and security/interpretability
8. **Calibration summary table** — quick decision rule anchored on whether reviewer weaknesses target *gaps in existing claims* vs. *desired extensions*