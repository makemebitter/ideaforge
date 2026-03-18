The skill file has been written to `C:\Users\yhzha\auto_research_bot\judge_training\skills\topics\_gen_motion_generation\skill_motion_generation.md`.

Here's a summary of what's covered in the ~12K token file:

**Structure:**

1. **Topic Overview** — Covers the 7 major sub-areas (text-to-motion, dance, motion prediction, multi-person, gesture, mocap, controllable), plus a score-distribution calibration table grounded in the actual 109-paper statistics (mean 4.93, 26.6% acceptance).

2. **What Reviewers Praise** — Grounded in real reviewer quotes: novel paradigms (MotionGPT's LLM approach, SEPT's SSL pretraining), strong ablations (the #1 praised element, 85x), multi-dataset evaluation, theory+empirics combination.

3. **What Reviewers Criticize** — The #1 criticism is missing baselines (142x). Includes real failure modes: unfair comparisons that change two variables simultaneously (SafeMo), outdated datasets (HumanAct12/UESTC from 2018/2020), missing video demos, no failure analysis.

4. **Required Baselines & Metrics** — Full tables for T2M (MDM, T2M-GPT, MoMask, MLD, ReMoDiffuse), dance (EDGE, Bailando), autonomous driving (QCNet, MTR, Argoverse 1&2), plus all standard metrics (FID, R-Precision, MM Dist, Diversity, MultiModality).

5. **Common Technical Pitfalls** — 8 specific pitfalls with reviewer quotes: motion representation underspecification, circular evaluation, reward hacking, VQ-VAE underspecification, etc.

6. **Scoring Rubric** — Concrete examples mapping real papers to score tiers (Humanoid-R0 = 2.0, ZNbzdBIWSd = 3.0, MotionGPT = 5.5, SEPT = 7.0).

7. **Key Papers & Expected Citations** — ~20 specific papers reviewers expect to see cited, with context for when each is required.

8. **Rapid Evaluation Checklist** — Binary yes/no questions across novelty, baselines, metrics, ablations, qualitative, reproducibility.