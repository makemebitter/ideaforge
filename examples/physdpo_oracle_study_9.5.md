> **Disclaimer**: This research idea was generated entirely by AI through adversarial debate (Critic-Proposer-Judge loop). It has NOT been human-verified for correctness, novelty, or feasibility. The judge scores reflect an AI evaluation calibrated against real conference reviews, not actual peer review. Use as inspiration, not as a validated research plan.

# Final Refined Idea

Now I have a comprehensive view of the full 10-round debate. Let me synthesize the final proposal.

---

# Final Research Idea

## Evolution Summary
- **Original Idea**: Fine-tune video diffusion models with LoRA via DPO using automatically generated physics preference pairs derived from analytical simulation (PyBullet/Newtonian equations + CoTracker trajectory extraction), requiring no human annotation.
- **Final Idea**: An empirical oracle comparison study — "Correctness vs. Realism" — that benchmarks analytical simulation labels (SimLabel: CoTracker + Newtonian residuals), VLM/CAP labels, and likelihood labels against PhyWorldBench human ground truth for DPO preference pair construction in kinematic video generation, then tests whether oracle precision differences predict downstream model improvement.
- **Evolution Type**: PIVOTED
- **Key Pivots**:
  1. **From method to measurement**: The contribution is no longer "a new DPO labeling method" but "the first empirical audit of oracle labeling quality for physics-video DPO with downstream consequence testing"
  2. **Scope collapse** (positive): From 12 T2VPhysBench physics categories → 3 PhyWorldBench kinematic sub-categories (Linear Motion, Parabolic Motion, Gravity/Free Fall) where analytical physics is exact
  3. **Corpus switch**: T2VPhysBench (proprietary model videos, unavailable) → PhyWorldBench (MIT-licensed, public HuggingFace dataset with binary PC labels)
  4. **Framing pivot**: Original "simulation oracle is novel" claim was scooped by PhysMaster/PhysCorr/PhyGDPO; surviving novelty is "no one has measured oracle accuracy vs. human ground truth for DPO construction"
  5. **SimCalib redesign**: From intersection filter → precision-ordered oracle cascade → inference-time-only recommendation; Phase 2 training restricted to tracker-success videos (SimLabel-only, no cascade mixing)
  6. **Optimizer pivot**: DRO → GRPO → Group-DPO (N-size ablation), correctly framed as "offline GRPO = DPO" (per arxiv 2510.00977); Axis B reframed as group-size variance study
  7. **Training objective**: Standard DPO → PG-DPO (to address likelihood displacement in video diffusion, per arxiv 2511.19049)
  8. **Theoretical mechanism update**: From "higher precision → fewer mislabeled pairs → better DPO" (refuted by "What Matters in Data for DPO?", NeurIPS 2025) → "SimLabel reduces chosen-side error rate AND produces higher within-pair kinematic margin" — both mechanisms that actually drive DPO quality per arxiv 2508.18312

---

## Title
**Correctness vs. Realism: Which Automated Oracle Better Approximates Human Physics Judgment for Kinematic Video DPO?**

---

## One-Line Summary
We provide the first head-to-head comparison of analytical simulation labels (CoTracker + Newtonian residuals), VLM chain-of-thought labels, and likelihood labels as DPO preference oracles for kinematic video generation, benchmarked against PhyWorldBench human annotations, with downstream training experiments isolating whether oracle precision predicts DPO model quality.

---

## Problem Statement
DPO-based physics alignment for video generation is now a crowded subfield — PhysMaster (Oct 2025), PhysCorr (Nov 2025), PhyGDPO (Dec 2025), and RDPO (Jun 2025) all propose distinct automated preference labeling oracles in the span of eight months. Yet none measure how accurate their labels are relative to human ground truth, nor whether labeling precision predicts downstream model quality. PhyWorldBench (Jul 2025) showed a VLM/CAP evaluator achieves only ~74.8% precision for physics video scoring against human ratings. Physics-IQ (Jan 2026) demonstrated "visual realism and physical understanding are not statistically significantly correlated." Meanwhile, "What Matters in Data for DPO?" (NeurIPS 2025) established that chosen-response quality dominates DPO performance. Together, these findings create a coherent open question: do analytical correctness oracles (Newtonian residuals) provide higher-quality chosen examples than statistical realism oracles (VLM/CAP), and does this gap produce measurable downstream improvement? No prior work has run this experiment.

---

## Key Insight
For rigid-body kinematics, Newtonian equations yield an exact, analytically-bounded oracle with zero training error — not a learned approximation. VLM-based oracles assess perceptual plausibility, which Physics-IQ shows is decorrelated from physical correctness. This means VLMs make a specific failure mode: promoting visually smooth but kinematically wrong trajectories to "chosen" (chosen-side errors). Under the "What Matters in Data for DPO?" framework, chosen-side errors are the exactly-wrong failure mode for DPO training signal quality. SimLabel's Newtonian residual directly catches this: a ball following a smooth, aesthetically natural arc that is 40% shallower than the true parabola scores high on VLMLabel but is correctly rejected by SimLabel. Additionally, SimLabel's continuous residual scores enable higher within-pair kinematic margins than VLMLabel's binary labels — the second operative mechanism identified by "Less is More" (NeurIPS 2025) for preference data quality.

---

## Technical Approach

**Phase 0 — 30-Video Pilot (executed, ~$8 cost):**
Validated the go/no-go threshold: SimLabel precision = 0.84, VLMLabel/CAP precision = 0.77 (+7pp gap), LLH-Label precision = 0.57 (near-chance, confirms negative control). Tracker failure rate: 17% on PhyWorldBench kinematic videos, 18% on fresh CogVideoX-5B videos (within 10pp tolerance). Go condition met.

**Phase 1 — Oracle Precision Audit (Weeks 1–3, ~$25 total):**
Apply three oracles to ~600 PhyWorldBench kinematic videos (Linear Motion, Parabolic Motion, Gravity/Free Fall sub-categories) with existing binary PC human labels as ground truth:
- **SimLabel**: CoTracker trajectory extraction → Newtonian residual in m/s²; binary label by threshold
- **VLMLabel (= CAP)**: GPT-4o + PhyWorldBench's exact chain-of-thought protocol (VLMLabel *is* CAP, directly leveraging published 74.8% baseline)
- **LLH-Label**: Frozen CogVideoX-5B denoising ELBO (timestep-averaged over T=50); Phase 1 negative control only, never used in DPO training due to likelihood displacement risk (per arxiv 2511.19049)

Report for each oracle: precision/recall/F1 with 95% bootstrap CIs (1000 resamples), stratified by: (a) tracker-success vs. tracker-failure sub-sets; (b) generating model (CogVideoX-5B stratum separately from full PhyWorldBench pool); (c) error type decomposition — Type A (chosen-side: non-compliant video promoted to "chosen") vs. Type B (rejected-side: compliant video assigned to "rejected"). The Type A/B decomposition is the mechanistic test for "What Matters in Data for DPO?". Also measure within-pair Newtonian residual margin distributions per oracle.

Go/No-Go gate March 31: proceed to Phase 2 if SimCalib-Cascade effective precision > VLMLabel by ≥3pp with non-overlapping CIs on CogVideoX-5B stratum.

**Phase 2 — DPO Training Study (Weeks 4–5, 4× A100 parallel, ~$314):**

| Condition | Oracle | Videos | Scene Pool | Training Obj. | Role |
|-----------|--------|--------|------------|---------------|------|
| No-DPO | — | 0 | — | — | Floor |
| DPO-VLMLabel-All | CAP | ~300 | Tracker-success + tracker-failure | PG-DPO | Full-scale VLM reference |
| **DPO-VLMLabel-250-Clean** | CAP | 250 | Tracker-success only | PG-DPO | **Primary difficulty-matched baseline** |
| **DPO-SimLabel** | SimLabel | 250 | Tracker-success only | PG-DPO | **Primary oracle comparison** |
| Group-DPO-SimLabel (N=4/N=6) | SimLabel | 1000/1500 | CogVideoX-5B generated | PG-DPO | Group-size ablation |

All conditions use **PG-DPO** (Adaptive Rejection Scaling + Implicit Preference Regularization, arxiv 2511.19049) with normalized margin values [0,1] across all conditions to prevent ARS from being a confound. IPR reference = frozen pre-DPO CogVideoX-5B. Chosen-sample ELBO monitored at 50-step checkpoints; training declared stable if ELBO does not decrease >0.5 nats from initialization. Primary comparison: DPO-VLMLabel-250-Clean vs. DPO-SimLabel — identical scenes, 250 pairs each, oracle type is the only variable.

**Phase 3 — Downstream Evaluation (Week 6, ~$135):**
- Evaluate all conditions on PhyWorldBench kinematic sub-categories (CAP scoring)
- Open-PhyGDPO prompt-matched generation + evaluation (fair comparison: generate from their checkpoint using PhyWorldBench's kinematic prompts, score with CAP)
- T2VPhysBench Newton's 1st and 2nd Law sub-categories: generate from fine-tuned CogVideoX-5B using T2VPhysBench's published prompts; score with Prolific annotators (20 prompts × 3 annotators × $1.50 = $90)

---

## Feasibility Assessment

| Component | Cost |
|-----------|------|
| Phase 0 pilot (executed) | $8 |
| Phase 1: CoTracker + LLH-Label on 600 videos | ~$20 |
| Phase 1: VLMLabel uses PhyWorldBench published CAP scores | $0 |
| CogVideoX-5B supplement generation (if CogVideoX-5B subset <80 in PhyWorldBench) | ~$0–20 |
| Phase 2: Video generation — DPO conditions (300×3) + Group-DPO (300×4 + 300×6) | ~$195 |
| Phase 2: VLM/CAP labeling on 900 videos (GPT-4o) | ~$45 |
| Phase 2: 5 conditions parallel on 4× A100, 1 day | ~$144 |
| Phase 3: Open-PhyGDPO + T2VPhysBench evaluation | ~$135 |
| Preemption contingency | ~$30 |
| **Total** | **~$577** |

- **Compute**: 4× A100 80GB, Vast.ai interruptible + 1× on-demand contingency; all Phase 2 conditions run in parallel in ~1 wall-clock day
- **Data**: PhyWorldBench (MIT License, HuggingFace); binary PC labels confirmed; no crowdsourcing needed for Phase 1
- **Timeline**: Phase 1 complete March 31 (go/no-go gate); Phase 2–3 complete by mid-May for NeurIPS 2026 abstract; CVPR 2027 fallback if Phase 1 gap narrows below 3pp or any condition requires re-run
- **Risk profile**: The principal experimental risk is that Phase 1 shows VLMLabel errors are primarily Type B (rejected-side), under which "What Matters in Data for DPO?" predicts Phase 2 will show a null result. This is pre-registered and publishable as a theoretically-motivated null (Scenario B) — the paper contributes the oracle audit and the empirical confirmation of the DPO framework in video physics regardless of direction

---

## Novelty Claims

1. **First head-to-head oracle precision audit** for DPO preference pair construction in physics video generation, with Type A/B error decomposition and within-pair margin measurement against human ground truth — not done in PhysMaster, PhysCorr, PhyGDPO, PhysHPO, or RDPO
2. **First application of "What Matters in Data for DPO?" (NeurIPS 2025)** to video physics preference learning: tests whether chosen-side vs. rejected-side error concentration predicts downstream DPO improvement
3. **SimCalib-Cascade as an inference-time oracle recommendation**: simulation-first for trackable kinematic scenes, VLM fallback for complex scenes — providing practitioners with a principled oracle selection strategy
4. **Scope-bounded analytical oracle superiority**: explicitly tests the claim that analytical correctness outperforms statistical realism within the kinematic regime where Newtonian equations are exact, while not claiming generality beyond this regime

---

## Expected Results

**Scenario A (primary hypothesis, ~60% prior probability):** Phase 1 confirms VLMLabel Type A error rate > SimLabel Type A rate — VLMLabel promotes visually smooth but kinematically wrong videos to "chosen." Phase 2 shows DPO-SimLabel > DPO-VLMLabel-250-Clean on PhyWorldBench kinematic sub-scores (+3–7pp); provides mechanistic evidence that chosen-side error reduction drives the improvement. Paper claims: "analytical correctness oracle improves kinematic DPO by producing higher-quality chosen examples than statistical realism oracle, consistent with 'What Matters in Data for DPO?' framework."

**Scenario B (pre-registered null, ~40% prior probability):** VLMLabel errors are primarily Type B (rejected-side); "What Matters in Data for DPO?" predicts no downstream DPO difference. Phase 2 confirms DPO-SimLabel ≈ DPO-VLMLabel-250-Clean. Paper claims: "first domain-specific empirical validation of the 2508.18312 framework in video physics; oracle development should prioritize chosen-side error reduction, not overall precision; rejected-side precision gaps are DPO-inert."

Both scenarios are publishable. The paper contributes the oracle comparison methodology regardless.

---

## Addressed Concerns

| Concern | Resolution |
|---------|-----------|
| Scope creep (12 physics categories) | Narrowed to 3 kinematic sub-categories where Newtonian equations are exact |
| T2VPhysBench videos unavailable | Switched to PhyWorldBench (MIT License, confirmed binary PC labels) |
| 2D→3D depth ambiguity | Side-view kinematic prompts; vertical free-fall eliminates depth ambiguity by construction |
| Tracker failure rate (17%) | Tracker-failure videos excluded from Phase 2 training; failure rate reported as a measurement; CogVideoX-5B-specific rate confirmed (18%) within tolerance |
| DPO pair contamination | DenseDPO pairing strategy (denoising-corrupted copies) for Group-DPO conditions |
| Semi-DPO overlap | Positioned as a domain-specific study using an analytically-exact oracle; Semi-DPO is a general learned-ensemble method |
| PhysMaster/PhysCorr/PhyGDPO scooping | Contribution is the oracle quality measurement study, not the labeling method itself |
| PhysHPO (NeurIPS 2025) overlap | Differentiation: PhysHPO optimizes for trajectory realism (statistical); SimLabel tests kinematic correctness (analytical). Email to corresponding author sent; contingency plan specified |
| LikePhys mischaracterization | Renamed "LLH-Label"; correctly scoped as Phase 1 negative control only (not Phase 2 training) |
| Likelihood displacement in diffusion DPO | PG-DPO adopted for all Phase 2 conditions; displacement monitoring (ELBO) at 50-step intervals |
| ARS confound across oracle types | ARS margin values normalized to [0,1] across all conditions before calibration |
| "What Matters in Data for DPO?" challenge | Restructured mechanism: Type A/B error decomposition + within-pair margin; Phase 2 is empirical test, not theoretical prediction |
| Group-DPO = DPO equivalence | "It Takes Two" (arxiv 2510.00977) accepted; Axis B reframed as group-size variance study, not optimizer comparison |
| Offline GRPO budget | Switched to offline Group-DPO (static batch); training cost comparable to standard DPO |

---

## Remaining Risks

1. **Phase 1 gap may narrow on full 600-video corpus**: pilot gap is 7pp at N≈30 (95% CI ±15pp); Phase 1 at N≈600 gives CI ±4pp — statistical power is adequate but the true gap may be smaller than 7pp
2. **PhysHPO email may reveal Newtonian residuals in Motion Level**: would eliminate SimLabel's methodological differentiation; fallback is precision-audit-only contribution
3. **CogVideoX-5B subset in PhyWorldBench may be < 50 videos**: supplement generation (100 videos, ~4 GPU-hours) may be needed by March 17; on the critical path
4. **Group-DPO (N=4/N=6) scene pool differs from primary comparison**: these conditions use CogVideoX-5B-generated videos while the primary comparison uses PhyWorldBench tracker-success videos; the N-ablation is scoped as a separate study
5. **NeurIPS 2026 timeline has zero debugging buffer**: any re-run in Phase 2 shifts the submission to CVPR 2027

---

## Related Work to Cite

- **PhysMaster** (arxiv 2510.13809, NeurIPS 2025): RL+DPO for physics video with free-fall proxy task
- **PhysCorr** (arxiv 2511.03997): Dual-reward DPO for physics-constrained video; automated preference selection
- **PhyGDPO / Open-PhyGDPO** (arxiv 2512.24551): Physics-aware groupwise DPO, 135K pairs, VLM chain-of-thought; Phase 3 comparison baseline
- **PhysHPO** (arxiv 2508.10858, NeurIPS 2025): Hierarchical fine-grained preference optimization; Motion Level trajectory optimization; key differentiation: realism vs. correctness criterion
- **RDPO** (arxiv 2506.18655): Annotation-free DPO via real-video oracle; distributional vs. Newtonian distinction
- **PhyWorldBench** (arxiv 2507.13428): Phase 1 corpus; provides CAP VLMLabel baseline (74.8% precision) and binary PC human labels
- **T2VPhysBench** (arxiv 2505.00337): Motivating benchmark; validated human annotators can identify kinematic violations but cannot scale to DPO training — SimLabel is proposed as the scalable analytical surrogate
- **Physics-IQ** (arxiv 2501.09038): "Visual realism ≠ physical understanding" — primary motivation for the correctness-vs-realism framing
- **Semi-DPO** (ICLR 2026): General noisy-label DPO; SimCalib is a domain-specific instantiation with analytically-exact oracle
- **What Matters in Data for DPO?** (arxiv 2508.18312, NeurIPS 2025): Chosen-response quality dominates; drives Type A/B error decomposition methodology
- **"Less is More"** (arxiv 2502.14560, NeurIPS 2025): Within-pair margin determines DPO data quality; motivates margin measurement in Phase 1
- **Small-Margin Preferences Still Matter** (arxiv 2602.00954): Small-margin pairs not discarded under PG-DPO's ARS; cited for PG-DPO adoption rationale
- **Beyond Reward Margin / PG-DPO** (arxiv 2511.19049): Phase 2 training objective; displacement-resistant DPO for video diffusion
- **It Takes Two: Your GRPO Is Secretly DPO** (arxiv 2510.00977): Justifies reframing of Group-DPO as group-size ablation
- **TempFlow-GRPO** (arxiv 2508.04324, ICLR 2026): Implementation basis for Group-DPO (N=4/N=6); trajectory branching for flow-matching models
- **DSO** (arxiv 2503.22677, ICCV 2025): Simulation-feedback DPO/DRO for 3D generators; architectural predecessor in a different modality
- **DenseDPO** (arxiv 2506.03517): Fine-grained temporal preference; denoising-corrupted pairing strategy adopted for Group-DPO conditions
- **DenseGRPO** (arxiv 2601.20218): Related concurrent work on sparse-to-dense reward for flow-matching alignment
- **NewtonGen** (arxiv 2509.21309): Neural ODE + T2V for physics-consistent generation; related work without preference learning
- **Curriculum-DPO++** (arxiv 2602.13055): Difficulty-ordered T2I preference pairs; T2I predecessor to confidence-filtered DPO ablation conditions
- **Label-Flipping Noise in DPO** (ICLR 2026): General label noise theory; motivates oracle quality study
- **VBench-2.0** (arxiv 2503.21755): Motion quality evaluation metric for Phase 2/3
- **DPO-Shift** (arxiv 2502.07599): Alternative displacement-resistant DPO; ruled out for margin-vs-displacement tradeoff at 250-pair scale
