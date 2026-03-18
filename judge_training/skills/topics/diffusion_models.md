I've written the comprehensive skill file at `judge_training\skills\topics\_gen_diffusion_models\skill_diffusion_models.md`. Here's a summary of what it covers:

---

**Skill File: Evaluating Diffusion Model Papers** (~13K tokens)

Based on deep reading of reviews from 1293 papers (acceptance rate 72%, mean rating 4.98), the file provides:

1. **Rating Scale Calibration** — Concrete score anchors (1-10) with real examples from the corpus:
   - 9-10: Provably correct algorithms or fundamental theoretical insights (e.g., MCGDiff, 8.5)
   - 7-8: Novel insight + comprehensive ablations (e.g., Memorization detection, SDXL)
   - 5-6: Borderline — technically sound but incomplete experiments or incremental novelty
   - 3-4: False novelty claims, wrong baselines, insufficient experiments (e.g., LAVITA reject)

2. **Sub-Area Technical Knowledge** across 8 domains: generative synthesis, inverse problems, theory, efficient training, guided generation, scientific applications, privacy/safety, flow matching

3. **Expected Baselines Table** — Precisely which methods reviewers expect to see compared against in each sub-area

4. **Standard Metrics** — FID, FVD, AUC, TPR@FPR=1%, PSNR/SSIM/LPIPS, designability scores, etc.

5. **Common Failure Patterns** — The 8 most frequent rejection causes with real examples:
   - False novelty claims (LAVITA missed VDT)
   - Wrong baseline numbers (PVDM at 2000 FVD vs. actual <400)
   - Missing ablations, limited experimental scope, incremental combination

6. **Practical Evaluation Checklist** — Binary questions covering novelty, soundness, experiments, presentation

7. **Key Foundational Papers** — The canonical references reviewers expect cited (DDPM, Score-SDE, EDM, DiT, DPS, etc.)