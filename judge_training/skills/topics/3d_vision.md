The skill file has been written to `judge_training/skills/topics/_gen_3d_vision/skill_3d_vision.md`. Here's a summary of what it covers, grounded in real reviewer data from 1,235 papers:

---

**What I read:**
- **High-rated (8–8.5):** LRM (first large-scale image-to-3D), Grendel/scaling 3DGS, MovingParts, No-Pose-No-Problem
- **Low-rated (2.75–4.5):** Self-Supervised Stereo Odometry (rejected for wrong template + results worse than baselines), LISA (rejected for incremental novelty + missing comparisons), Level-Set Parameters (rejected for saturated benchmarks + vague motivation)
- **Borderline (6.0):** HiSplat (accepted but criticized for missing FreeSplat/Splatt3R discussion, efficiency analysis)

**Key patterns distilled into the skill file:**

1. **#1 Weakness:** Missing baselines (1,590x in reviews). 3DGS, MVSplat, DUST3R/MAST3R are now required baselines.
2. **#2 Weakness:** Missing LPIPS for NVS papers — standard since the original NeRF paper.
3. **#3 Weakness:** Evaluation only on saturated benchmarks (ModelNet40, D-NeRF-as-monocular).
4. **Scoring rubric:** 3 = results worse than baselines + incomplete; 5 = incremental + missing work; 6 = solid but gaps; 8+ = first-of-kind + comprehensive experiments.
5. **50 key papers** reviewers expect cited — missing PF-LRM, LEAP, FreeSplat, DOGS, etc. are specific red flags.