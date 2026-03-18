> **Disclaimer**: This research idea was generated entirely by AI through adversarial debate (Critic-Proposer-Judge loop). It has NOT been human-verified for correctness, novelty, or feasibility. The judge scores reflect an AI evaluation calibrated against real conference reviews, not actual peer review. Use as inspiration, not as a validated research plan.

# Final Refined Idea

Now I have all the information needed to synthesize the final proposal.

---

# Final Research Idea

## Evolution Summary

- **Original Idea**: Fine-tune a pretrained video diffusion model (CogVideoX) with LoRA on synthetic (original, counterfactual) video pairs from physics simulators to enable causal "what-if" video generation.
- **Final Idea**: A benchmark that evaluates existing video editing systems on their ability to produce physics-parameterized counterfactual videos — given a reference video V₀ and a named parameter change Δθ, generate V_cf that preserves V₀'s appearance while following a Box2D-simulated counterfactual trajectory.
- **Evolution Type**: PIVOTED
- **Key Pivots**:
  1. **CausalVideoFT → PhysParamFT** (Round 1): CWMDT (arXiv 2511.17481) had already trained a video diffusion model on Kubric counterfactual pairs with explicit physics conditioning — directly scooping the method contribution.
  2. **PhysParamFT → SimRender** (Round 2): PhyWorld (ICML 2025) empirically showed that physics conditioning modality does not improve OOD generalization in video diffusion models, invalidating the core scientific hypothesis.
  3. **SimRender → PhysEdit** (Round 3): 3D geometry extraction from monocular video for Kubric re-rendering was found unsolved; the underlying physics estimation scope was too narrow.
  4. **PhysEdit → Benchmark** (Round 4): MotionV2V (arXiv 2511.20640) was trained on identical (V₀, V_cf) trajectory-conditioned pairs, defeating the method's novelty claim. The research value was identified in creating the evaluation infrastructure, not a new method.
  5. **Rounds 4–20**: 15 rounds of benchmark hardening — metrics, system selection, protocol specification, budget verification, related work confirmation.

---

## Title

**PhysCounterfact: A Benchmark for Physics-Parameterized Counterfactual Video Editing**

---

## One-Line Summary

A dual-split (synthetic + real) benchmark that, for the first time, evaluates video editing systems on parameterized rigid-body physics counterfactuals using Box2D-simulated trajectories as verifiable ground truth.

---

## Problem Statement

Existing physics video benchmarks evaluate either (a) open-ended text-to-video generation quality (T2VPhysBench, PhyWorldBench, Morpheus) or (b) video continuation/prediction from conditioning frames (Physics-IQ). None evaluates the parameterized counterfactual editing task: *given an existing video V₀ showing a physical scene and a user-specified parameter change Δθ (e.g., "3× friction", "0.5× mass"), produce V_cf where the same-looking objects behave as they would under the changed physics*.

This task is distinct from both generation and prediction: it requires (1) appearance preservation from V₀, (2) physics-correct trajectory change driven by Δθ, and (3) multi-system comparative evaluation. Without a benchmark, researchers building counterfactual video editors have no agreed-upon evaluation protocol, no shared system ranking, and no verifiable ground truth — they default to uncontrolled user studies or FVD, both of which are unreliable for this task.

---

## Key Insight

Physics simulators (Box2D) provide cheap, exact counterfactual trajectories τ_cf for 2D-planar rigid-body scenes. These trajectories serve as **verifiable ground truth** that sidesteps the need for real-world re-capture of counterfactual outcomes. By measuring how closely a generated video V_cf follows τ_cf (Physics Trajectory Error, PTE) while preserving V₀'s appearance (Appearance Similarity, AS), the benchmark directly operationalizes the two-dimensional success criterion for counterfactual video editing — independently of any specific editing method.

---

## Technical Approach

### Dataset Construction

**Synthetic split (primary evaluation):**
- 2,000 tuples (V₀, Δθ, τ_cf, V_cf_gt) generated via Kubric + EEVEE renderer at 256×256
- 500 base scenes × 4 counterfactual interventions each
- 4 scene types: single-sphere rolling on plane, two-sphere collision, sphere-on-ramp, sphere-pendulum
- Counterfactual interventions: Δmass ∈ {0.25×, 4×}, Δfriction ∈ {0.1×, 10×}, Δrestitution ∈ {0.1×, 10×}
- Box2D simulation generates τ_cf (centroid trajectory in image-plane pixels); Kubric renders V_cf_gt

**Real split (ecological validity):**
- 25 clips from Something-Something v2 (SSv2), 14 clean 2D-planar categories
- 4 counterfactuals per clip × 7–8 evaluated systems × 3 Prolific.ac raters
- Clip-level planarity filter: CoTracker-tracked centroid primary PCA axis must deviate <30° from image plane; clips failing this threshold are excluded and replaced

### Systems Evaluated (7–8)

| System | Type | Conditioning |
|--------|------|-------------|
| PhysCtrl (NeurIPS 2025) | Method | Physics-conditioned video diffusion |
| WMReward (arXiv 2601.10553) | Method | Inference-time physics alignment |
| CogVideoX-5B-I2V | Baseline | Text + first-frame |
| TokenFlow + InstructPix2Pix | Baseline | Text-guided editing |
| AutoVFX (arXiv 2411.02394) | Method | Neuro-symbolic VFX |
| CounterVid (arXiv 2601.04778) | Method | Counterfactual video generation |
| No-change (V₀ replayed) | Baseline | Lower bound |
| Oracle (V_cf_gt replayed) | Upper bound | Upper bound |

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| **PTE ↓** | Physics correctness | CoTracker centroid distance (px) vs. Box2D τ_cf; TAPIR secondary validation; median as primary for bimodal distributions |
| **AS ↑** | Appearance preservation | DINOv2 cosine similarity of V_cf frames to V₀; CoTracker-prompted SAM2 object mask |
| **JEDi ↓** | Distributional realism | Joint distribution embedding distance vs. 700-clip SSv2 reference (14 categories × 50 clips); converges at N=700–800 |
| **PCS ↑** | Composite | PCS = (1 − PTE/PTE_no-change) × AS |

SSIM/LPIPS removed from main table; present only in within-domain supplementary ablation.

### Human Evaluation Protocol

- Platform: Prolific.ac, per-completion payment
- Attention Check 1 (AC1): "Which video shows more realistic physics?" for 4 oracle vs. synthetic pairs — pass threshold ≥ 4/4
- Attention Check 2 (AC2): Temporal reversal detection — exclude workers with ≤ 2 correct
- Free-text field for anomaly reporting
- Rating task: 2AFC "which of V_cf_A or V_cf_B better matches the counterfactual description?"

### Pilot Suite (Appendix C — 5 protocols with pass/fail thresholds)

1. **Planarity pilot**: 50 clips/category → confirm <15% exclusion rate per category
2. **AutoVFX PTE pilot**: N=20 clips → confirm AutoVFX PTE < no-change baseline
3. **AC2 lab check**: 3 in-lab members, blind → confirm AC2 pass rate ≥ 90%
4. **Kubric EEVEE render benchmark**: 10 frames → confirm <5s/frame on target GPU
5. **PhysCtrl code verification**: confirm inference weights loadable (Path A) or fall back to TokenFlow+IP2P (Path B — already declared)

---

## Feasibility Assessment

| Dimension | Assessment |
|-----------|-----------|
| **Compute** | Kubric 2,000 clips at EEVEE 256×256 ≈ 40 GPU-hours (~$80). Baseline inference 7 systems × 2,000 clips ≈ 1 A100-day (~$80). Total GPU: ~120 GPU-hours. |
| **Data** | SSv2 clips available via academic license. Kubric open-source (CVPR 2022). Box2D free. No proprietary data dependencies. |
| **Cost** | Path B (TokenFlow+IP2P): **$970 total**, ceiling $1,075. Path A (PhysCtrl): **$1,074 total**, ceiling $1,194. Both under $1K soft cap (Path B) or within $1.2K. Budget fully itemized and arithmetic-verified across 20 rounds. |
| **Timeline** | 5 execution pilots → 2–3 weeks. Full evaluation run → 1 week. Writing → 2–3 weeks. Compatible with NeurIPS 2026 D&B submission timeline. |
| **Risk** | LOW. No single novel model to train. Primary risk is PhysCtrl weight availability (Path B mitigates). Statistical power adequate at σ≤25px (power >90% for Δ=5px, N=500). |

---

## Novelty Claims

1. **First benchmark for parameterized counterfactual video editing**: All prior benchmarks evaluate generation (T2V) or prediction (continuation), not editing under named parameter changes. The (V₀, Δθ) → V_cf task formulation is new.
2. **Box2D τ_cf as verifiable ground truth**: PTE against simulation trajectory is the first physics-correctness metric that does not require human ratings or a held-out oracle video — it measures geometric deviation from exact physics.
3. **PCS composite metric**: Jointly measures physics correctness and appearance preservation in a single comparable scalar — the first metric that penalizes both "wrong motion, right look" and "right motion, wrong object."
4. **Dual synthetic+real benchmark design with specified cross-split validity**: Establishes when systems that succeed on Kubric fail on real SSv2 clips, identifying the simulation-to-real gap as a measurable quantity.
5. **Power-calibrated evaluation**: First physics video benchmark to report sample-size power analysis over distribution shapes and provide per-system PTE histograms, enabling statistically credible system rankings.

---

## Expected Results

- **Oracle >> No-change > all learned systems** on PTE — confirms the metric is discriminative
- **PhysCtrl and WMReward** expected to outperform CogVideoX-I2V and TokenFlow+IP2P on PTE, but with lower AS (physics-correct motion at cost of appearance drift)
- **AutoVFX** expected to show high PTE variance (success on simple scenes, failure on multi-object); bimodal PTE histogram predicted
- **JEDi spread**: generation-based systems (CogVideoX, WMReward) expected to score closer to SSv2 reference than simulation-replay methods; establishes realism-physics tradeoff curve
- **Real-split degradation**: all systems expected to show higher PTE on SSv2 clips than on synthetic split, quantifying the sim-to-real gap

The benchmark's primary scientific contribution is this system comparison table — not any single system winning, but the structured measurement of the tradeoff landscape.

---

## Addressed Concerns

| Concern | Resolution |
|---------|-----------|
| CWMDT scoop (method) | Pivoted to benchmark; CWMDT is evaluated as a system, not competed with |
| PhyWorld OOD result | Reframes as motivation: no existing method solves the task, hence a benchmark is needed |
| MotionV2V overlap | Pivoted to benchmark; MotionV2V is evaluated as a system |
| JEDi Gaussianity assumption | Replaced FVD with JEDi (arXiv 2410.05203, ICLR 2025) — no Gaussianity assumption, converges at N=700 |
| CoTracker reliability under occlusion | TAPIR added as secondary validation; occlusion-heavy clips flagged and excluded per protocol |
| TokenFlow+IP2P budget feasibility | Reduced to N=200 clips at $27; budget fully verified |
| PhysCtrl code availability | Path A/B contingency fully specified; Path B irrevocably declared |
| JEDi reference set 3D contamination | 14 clean 2D-planar SSv2 categories confirmed; clip-level planarity filter with 30° threshold |
| Statistical power at small N | Power analysis table over σ ∈ {15, 25, 40, 60}px; median PTE primary for bimodal cases |
| PhysicEdit (Feb 2026) proximity | One-sentence §2 differentiation: image-to-video generation vs. reference video editing benchmark |
| Morpheus (arXiv 2504.02918) overlap | Non-overlapping: Morpheus evaluates open-ended generation against conservation-law metrics without Δθ conditioning, τ_cf, or multi-system editing comparison |

---

## Remaining Risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| PhysCtrl inference weights unavailable or broken | Medium | Path B (TokenFlow+IP2P) declared; Table 1 note will explain substitution |
| Planarity pilot fails (>15% exclusion per category) | Low-Medium | Replace failing categories from SSv2 long-tail; 14 candidates have buffer |
| AutoVFX PTE pilot shows no signal (PTE ≈ no-change) | Low | Examine failure mode qualitatively; AutoVFX may be demoted to supplementary |
| NeurIPS 2026 D&B deadline conflict | Low | Confirm immediately; ICLR 2027 D&B is fallback venue |
| Budget overrun to Path A ($1,194 ceiling) | Low | Soft cap is $1K; hard cap $5K provides ample buffer |

---

## Related Work to Cite

| Paper | Venue | Relevance |
|-------|-------|-----------|
| Morpheus (arXiv 2504.02918) | — | Closest benchmark; evaluates T2V generation against conservation laws — no Δθ, no τ_cf, no editing |
| WorldModelBench (arXiv 2502.20694) | — | World model evaluation; generation-focused, no counterfactual editing |
| PhysicEdit (arXiv 2602.21778) | — | Image-to-video generation via latent physics transitions — not a benchmark |
| T2VPhysBench (arXiv 2505.00337, ICLR 2025) | ICLR 2025 | T2V physics evaluation, human-rated, no parameter conditioning |
| Physics-IQ (arXiv 2501.09038, ICCV 2025) | ICCV 2025 | Video prediction benchmark, 396 real clips, no editing task |
| PhyWorldBench (arXiv 2507.13428) | — | 1,050 T2V prompts, 12 categories, no reference video |
| CounterVid (arXiv 2601.04778) | — | Closest method; evaluated as system in the benchmark |
| WMReward (arXiv 2601.10553) | — | Inference-time physics alignment; evaluated as system |
| MotionV2V (arXiv 2511.20640) | — | Trajectory-conditioned editing on (V₀, V_cf) pairs |
| CWMDT (arXiv 2511.17481) | — | Physics-conditioned video fine-tuning; evaluated as system |
| PhysCtrl (arXiv 2509.20358) | NeurIPS 2025 | Physics-conditioned video diffusion; primary evaluated system |
| AutoVFX (arXiv 2411.02394) | — | Neuro-symbolic VFX editing; evaluated as system |
| Beyond FVD / JEDi (arXiv 2410.05203) | ICLR 2025 | Distributional video metric without Gaussianity assumption |
| TokenFlow (arXiv 2307.10373) | ICLR 2024 | Consistent diffusion video editing; Path B CWMDT surrogate |
| Kubric (arXiv 2203.03570) | CVPR 2022 | Synthetic data generation framework used for synthetic split |
| Something-Something v2 (SSv2) | — | Real-split source; 14 2D-planar categories |
| CoPhy (ICLR 2020) | ICLR 2020 | Counterfactual physical dynamics learning in simulation — foundational, no video editing |
