> **Disclaimer**: This research idea was generated entirely by AI through adversarial debate (Critic-Proposer-Judge loop). It has NOT been human-verified for correctness, novelty, or feasibility. The judge scores reflect an AI evaluation calibrated against real conference reviews, not actual peer review. Use as inspiration, not as a validated research plan.

# Final Refined Idea

Now I have a complete picture of the 12-round debate. Let me synthesize the final research proposal.

---

# Final Research Idea

## Evolution Summary

- **Original Idea**: A training-free, denoising stage-adaptive sparse tile attention schedule for video DiTs that varies window sizes by timestep.
- **Final Idea**: A theoretically grounded, SNR-derived closed-form formula W*(t, h, l) = Ξ^(h,l)·[ln(SNR(t)/ε_per)]³ that analytically predicts the quality-preserving optimal attention window at each denoising timestep, head, and layer for video DiTs — requiring only 1 VBench quality pass and 5 attention-capture passes to calibrate vs. 100–1600+ passes for prior empirical methods.
- **Evolution Type**: REFINED
- **Key Pivots**:
  1. *1D → 3D formula*: W*(t) = ξ·log(SNR) replaced by W*(t) = Ξ·[ln(SNR/ε_per)]³ (product of per-dimension spatial-temporal correlation volumes; cubic log because volume = length³)
  2. *Assumption A4 → Approximation 1*: The mixture-attention structure was derived from A1–A3 via mean-field perturbation theory, achieving O(1/L²) error bound (~10⁻⁹ for HunyuanVideo); downgraded from "Lemma" to "Approximation" for honesty
  3. *T₀ fix*: Regime boundary correctly derived as T₀ = 1/(1+√ε_per) = 0.76 for ε_per = 0.10 (earlier claimed T₀ = 0.50, off by a factor of 5)
  4. *L correction*: HunyuanVideo has L = 115,200 tokens (not 30,000); formula now quantitatively consistent with STA's empirical 9% window
  5. *Quality-correctness framing*: W*(t) > STA at near-clean steps (steps 46–49) is not an efficiency cost but a prediction that STA under-attends there; reframes the method as a Pareto improvement over STA
  6. *Calibration de-circularity*: ε_per calibrated via VBench quality threshold at a fixed interior timestep t_mid = 0.40; Ξ estimated from recall measurement at t_high = 0.10; sequential 2-step, no division-by-zero
  7. *AdaSpa reconciliation*: Pattern identity (which tokens) is step-invariant; window count (how many tokens) varies with SNR(t). These are orthogonal dimensions; the formula addresses the latter.
  8. *SALAD acknowledged as prior art* for quality-threshold per-head calibration; differentiation is analytic extrapolation from O(1) quality passes vs. SALAD's O(H×L) quality passes

---

## Title

**SNR-Theoretic Sparse Attention for Video Diffusion Transformers (DAS-3D)**

---

## One-Line Summary

We derive the first closed-form analytic formula predicting optimal attention window size as a function of the diffusion noise schedule — W*(t, h, l) = Ξ^(h,l)·[ln(SNR(t)/ε_per)]³ — requiring only 1 VBench quality pass and 5 forward passes to calibrate, and achieving 2.33× attention speedup on the sparse denoising steps and ~1.14× overall speedup vs. Sliding Tile Attention on HunyuanVideo.

---

## Problem Statement

Sparse attention for video DiTs (e.g., STA, Sparse-vDiT, CalibAtt, SALAD) assigns either a static window per (head, layer) for all timesteps, or calibrates empirically via 100–1,600+ profiling passes. The former ignores that the signal-to-noise ratio changes across the 50-step denoising trajectory — leading to over-sparse mid-noise steps (quality risk) and under-sparse near-clean steps (compute waste). The latter is accurate but requires expensive per-model re-calibration. No prior work provides a closed-form analytic formula relating the optimal attention window to the diffusion noise schedule SNR(t), despite this connection being theoretically grounded in the diffusion forward process.

---

## Key Insight

Under a mean-field approximation of the diffusion forward process (Approximation 1, error O(1/L²) ≈ 10⁻⁹ for L = 115K), expected attention weights decompose as: E[w_ij(x_t)] ≈ SNR(t)·w_signal(i,j) + (1−SNR(t))·(1/L). The signal term decays exponentially in spatiotemporal distance under natural-image-statistics assumptions (Assumption A2). The minimum window capturing all tokens with above-threshold signal contribution is therefore W*(t) ∝ [ln(SNR(t)/ε_per)]³ in 3D (the cube of the per-dimension log-SNR radius). This yields two regimes: full attention when SNR < ε_per (high noise, no exploitable structure), and sparse W*(t) otherwise.

A critical distinction from four convergent prior papers (SpargeAttn, AdaSpa, Sparse-vDiT, LiteAttention) that find "step-invariant" sparsity patterns: those papers measure **recall** at fixed-K, which is indeed step-invariant because the identity of the top-K tokens is architecturally fixed. The **quality loss** from excluding tokens outside a fixed window scales with SNR(t) under Approximation 1, which means the quality-preserving minimum window grows substantially at near-clean steps. This is the theory's central falsifiable prediction (Experiment C).

---

## Technical Approach

**Theoretical chain:**
- A1 (linear projections) + A2 (separable exponential spatial-temporal correlation, A2 = approximation) + A3 (i.i.d. Gaussian noise tokens) → **Approximation 1** (mean-field; O(1/L²) error; proof sketch in Appendix A via perturbation expansion of softmax ratio)
- Approximation 1 → **Proposition 1**: For sparsifiable layer l, head h at timestep t: W*(t,h,l) = { L if SNR(t) < ε_per [Regime I]; max(W_min, Ξ^(h,l)·[ln(SNR(t)/ε_per)]³) otherwise [Regime II] }
- Proposition 1 → **Corollary 1**: T₀ = 1/(1+√ε_per); analytically computable from the noise schedule

**Calibration (sequential 2-step, non-circular):**
1. VBench quality sweep (K ∈ {1%,2%,5%,10%,20%} of L) at step 30 only (full attention elsewhere) → K_quality(t_mid) → ε_per = SNR(t_mid)·exp(−(K_quality/Ξ₀)^{1/3})
2. 20 forward passes with attention capture at step 45 (SNR ≈ 77.4) → W_recall^(h,l) per head → Ξ^(h,l)_model = W_recall / [ln(77.4/ε_per)]³

**Critical pre-step**: One forward pass identifies non-sparsifiable "critical layers" (Δvar > 3σ under 50% random block masking); these always use full attention.

**Implementation**: FlexAttention BlockMask, pre-computed offline for all 49 timesteps; 50 distinct BlockMask objects ≈ 2.8 MB GPU memory; O(1) per-step dispatch.

**Key experimental schedule:**
- **Experiment C (pass/fail gate)**: At steps {15, 20, 30, 45}, test K ∈ {0.5%, 1%, 5%, 10%, 15%, 20%} of L (full attention elsewhere). Measures whether quality-preserving minimum K varies with timestep for HunyuanVideo. Prediction B (step-variant quality) must hold for the paper to be viable.
- **Ablation E1 (4×3 grid)**: 1D-log vs. 3D-cubic formula × {no warmup, theory T₀, aggressive warmup} — directly tests whether cubic-log outperforms linear-log and whether T₀ derivation adds value
- **Cross-model validation**: Scale Ξ_model from HunyuanVideo to Wan2.1 via tokenizer geometry ratio; predict W*(t=0.30, 0.50) without re-calibrating
- **SALAD accuracy comparison**: Compare formula predictions vs. SALAD's per-head empirical calibration at t = 0.40; report distribution of relative errors
- **Position B experiment**: Matched-FLOPs comparison of DAS-3D vs. STA at steps 46–49 only, measuring VBench temporal consistency

---

## Feasibility Assessment

**Compute**: ~170 GPU-hours on H100 (HunyuanVideo 5s/720p, L=115,200 tokens; ~4 min/video)
**Cost**: ~$510 at $3/hr — well within $1,000 soft cap
**Data**: VBench-mini 50 prompts; public HunyuanVideo, CogVideoX, Wan2.1 checkpoints
**Timeline**: ~4–6 weeks of focused implementation + experiments
**Implementation risk**: FlexAttention BlockMask available in PyTorch 2.5+; 3D windowed masks are standard; W_min = 576 ≈ one STA tile (3×12×16 tokens) maps to existing kernel primitives

**Primary risk (40% probability)**: Experiment C shows quality at fixed K is step-invariant for HunyuanVideo, invalidating the paper's core premise. Pre-committed fallback: reframe as "analytic SNR-derivation of why prior fixed-window methods are theoretically justified; provides the first formula for the quality-equivalent constant window as a function of noise schedule."

**Secondary risk (30%)**: Cross-model prediction error > 30%, limiting generalizability claim to within-model characterization.

---

## Novelty Claims

1. **First closed-form analytic formula** W*(t) = Ξ·[ln(SNR(t)/ε_per)]³ predicting quality-preserving attention window from diffusion physics (confirmed absent in comprehensive literature search through March 2026)
2. **First derivation of T₀** (the warmup / full-attention boundary) analytically from ε_per without fitting to warmup step counts
3. **Recall ≠ quality distinction**: Mathematical proof (under Approximation 1) that step-invariant recall at fixed-K is compatible with step-varying quality-preserving minimum K, resolving the apparent contradiction with four prior papers
4. **First CalibAtt baseline on HunyuanVideo** (CalibAtt arXiv:2603.05503 does not test HunyuanVideo)
5. **O(1) quality calibration**: 1 VBench pass + 5 recall passes vs. 100+ (CalibAtt) or 1600+ (SALAD) quality evaluations for equivalent per-head window prediction

---

## Expected Results

| Metric | Prediction |
|---|---|
| W*(step 45, t=0.10) | ~10,588 tokens ≈ STA's 9% window (9.4% of L=115K) — non-circular consistency check |
| T₀ prediction (ε_per=0.10) | T₀ = 0.76 ≈ STA's 12/50 empirical warmup |
| Speedup on sparse steps 13–49 vs. STA | 2.33× |
| Overall speedup vs. STA | ~1.14× |
| W* at near-clean step 49 | ~31.7% of L (vs. STA's 9%) — Position B prediction |
| Experiment C outcome (Prediction B) | Quality at fixed K = 10% degrades at step 45 vs. step 15 on HunyuanVideo |
| Cross-model error (HunyuanVideo Ξ → Wan2.1) | < 30% relative error at held-out t values |
| Formula vs. SALAD per-head accuracy | Median relative error < 20% at t = 0.40 |

---

## Addressed Concerns

- **MOD-DiT overlap (Round 4)**: MOD-DiT uses empirical PCA → 3 components; this paper derives 2 components (signal + noise) from diffusion physics → produces analytic formula. MOD-DiT has no closed-form W(t), no T₀ derivation, requires early-step attention observation.
- **A4 → Approximation 1 (Round 5)**: Downgraded from "Lemma" (proved theorem) to "Approximation" with a proof sketch (O(1/L²)) and empirical validation (Step 3a). Mean-field approximation with rigorous perturbation bound.
- **O(1/L) vs. O(1/L²) typo (Round 6–7)**: Corrected; numerator O(C²_exp) constant / denominator O(L²) = O(1/L²); ~10⁻⁹ at L=115K.
- **L=30,000 wrong (Round 8)**: Corrected to L=115,200 (30×48×80 for HunyuanVideo 5s/720p); all numerics recomputed.
- **T₀ arithmetic error (Round 7–8)**: Corrected; T₀ = 1/(1+√ε_per), not 0.50.
- **1D formula → 3D formula (Round 8)**: Cubic-log extension derived from separability of A2 in temporal and spatial dimensions; W*(t) ≈ 10,836 tokens at step 45 matches STA's 10,368 (5% agreement) as an independent non-circular check.
- **ε_per circularity (Round 9–12)**: Resolved via sequential calibration: ε_per from quality sweep at interior t_mid = 0.40 (not at T₀); Ξ from recall measurement at t_high = 0.10; no algebraic circularity.
- **Step-invariant recall (Rounds 9–11)**: Mechanistic proof that recall invariance (pattern identity fixed by architecture) is compatible with quality-varying minimum K (absolute magnitude of excluded tokens scales with SNR). Experiment C tests this distinction.
- **Ruderman & Bialek misattribution (Round 7)**: Replaced with Field (1987, JOSA A) and Simoncelli & Olshausen (2001, Annual Review of Neuroscience) as the correct citations for natural image spatial correlation lengths.
- **W_min = 576 theoretical justification (Round 12)**: At steps 13–26 (SNR < ε_per), the 3D signal contribution outside W_min is bounded by SNR·exp(−4)³ ≈ 10⁻⁶ per token — 4 orders below ε_per. W_min is the natural discretization of Proposition 1, not an arbitrary floor.
- **Calibration division-by-zero (Round 12)**: Fixed by measuring ε_per at t_mid = 0.40 (not at T₀ where ln = 0), and Ξ at t_high = 0.10.

---

## Remaining Risks

1. **Experiment C failure (40%)**: If quality at fixed K is step-invariant for HunyuanVideo, the formula's main utility evaporates. Fallback proposal ready but substantially weaker.
2. **W_min validation (unrun)**: W = 576 (0.5% of L) at steps 13–26 is extremely aggressive relative to prior art (minimum in ecosystem is ~5%). A single data point at K=0.5% at step 20 would validate or collapse this regime.
3. **Cross-model generalization (30%)**: Ξ_model scaling by tokenizer geometry ratio is theoretically motivated but untested. If it fails, the formula is HunyuanVideo-specific.
4. **A2 separability failure**: Video motion creates non-separable spatiotemporal correlations. Step 3a (measuring empirical W*(t) at 5 timesteps) tests whether the cubic-log functional form holds; if CV of Ξ_model across timesteps > 50%, A2 is badly violated.
5. **Ξ_model >> Ξ₀ (60%)**: Natural image prior Ξ₀ = 36 may differ substantially from the model-calibrated Ξ_model. Theoretically expected (model learns beyond raw pixel statistics), already acknowledged. The formula's functional form (cubic-log in SNR) is the contribution; Ξ is empirically estimated.

---

## Related Work to Cite

**Core sparse attention for video DiTs:**
- STA: Sliding Tile Attention (arXiv:2502.04507) — static window, 9% of L on HunyuanVideo; primary comparison target
- Sparse-vDiT (arXiv:2506.03065) — three static patterns per head; content-independent (supports Approx. 1); 1.85× speedup
- CalibAtt (arXiv:2603.05503) — per-(timestep,head,layer) calibration, Wan2.1/Mochi/LightX2V; NOT HunyuanVideo; 100+ passes
- SALAD (arXiv:2601.16515) — per-head quality-threshold window calibration, 1600+ passes; prior art for quality-threshold calibration procedure
- AdaSpa (arXiv:2502.21079) — step-invariant pattern identity (supportive of the recall-vs-quality distinction)
- SpargeAttn (arXiv:2502.18137, ICML 2025) — step-invariant recall for HunyuanVideo specifically; Experiment C directly responds to this
- LiteAttention (arXiv:2511.11062) — 3-stage empirical discrete schedule; Ablation E1 baseline
- MOD-DiT (arXiv:2601.11641) — empirical mixture-of-distributions schedule; no closed-form formula
- PISA (arXiv:2602.01077) — piecewise step-varying sparsity improves over fixed; empirical support for the paper's premise
- SVG-EAR (arXiv:2603.08982) — error-aware routing complementary to window scheduling
- Radial Attention (arXiv:2506.19852) — static energy-decay mask; no timestep adaptation
- Analysis of Attention in Video DiTs (arXiv:2504.10317) — critical layers; attention structure characterization

**Theory foundations:**
- Field (1987, JOSA A 4:2379) — natural image spatial correlation lengths (basis for ξ₀ prior)
- Simoncelli & Olshausen (2001, Annual Review of Neuroscience) — natural image statistics survey
- Bounds on the Jensen Gap (arXiv:1712.05267) — general framework for Approximation 1 proof sketch
- Tight Bounds for Jensen's Gap (arXiv:2502.03988) — tighter bounds framework

**Model/infrastructure:**
- HunyuanVideo (arXiv:2412.03603) — L=115,200 for 5s/720p, tokenizer geometry
- FlexAttention (PyTorch 2.5+) — BlockMask implementation
- FlashInfer (MLSys 2025) — kernel backend option
