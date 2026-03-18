# Skill File: Evaluating Research in Diffusion Models

**Topic:** `diffusion_models`
**Dataset:** 1293 papers | Acceptance rate: 72% | Mean rating: 4.98 (σ=1.24)
**Tier distribution:** Excellent (8-10): 57 reviews | Good (6-7): 1314 | Borderline (4-5): 2664 | Low (1-3): 888

---

## 1. Field Overview

Diffusion models (and the closely related flow matching models) define a family of generative methods based on iteratively denoising data sampled from a noise distribution. The field encompasses:

- **Score-based generative models (SGMs):** Learn the score function ∇_x log p(x) and sample via Langevin dynamics or SDEs.
- **DDPM / DDIM:** Denoising Diffusion Probabilistic Models and their deterministic variant.
- **Latent diffusion models (LDMs):** Operate in compressed latent spaces (e.g., Stable Diffusion).
- **Flow matching / Rectified flows:** Straight-line transport between noise and data distributions; closely related but distinct from diffusion.
- **Consistency models:** Single-step or few-step distillation of diffusion ODE trajectories.

**Core sub-areas in the 1293-paper corpus:**
1. Generative image, video, and audio synthesis
2. Bayesian inverse problems (super-resolution, inpainting, deblurring, colorization)
3. Theoretical understanding (convergence, generalization, memorization, inductive bias)
4. Efficient training and inference (distillation, acceleration, sampling schedules)
5. Guided/conditional generation (text, class, image, ControlNet-style)
6. Scientific applications (protein design, molecule generation, crystal structure)
7. Privacy, safety, and copyright (memorization detection, watermarking, unlearning)
8. 3D generation (NeRF, point clouds, mesh generation)
9. Discrete diffusion models (for text, graphs, sequences)

---

## 2. Rating Scale Calibration

Use the following calibrated scale. **Note:** The dataset has a high baseline acceptance rate (72%), so your ratings should cluster around 4-6 for typical work, with strong work at 7-8 and exceptional work at 8.5+.

### Score 9-10: Exceptional / Oral-worthy
Rare (top ~1.4% of reviews). Papers that redefine how we think about a problem, prove previously unknown theoretical guarantees, or achieve breakthroughs with clear empirical backing.

**Hallmarks:**
- Solves a long-standing open problem or provides the first provably correct algorithm for a significant task
- Theory and experiments are tightly coupled and mutually reinforcing
- All reviewers enthusiastic (avg confidence ≥ 4), typically no major weaknesses
- Opens new research directions the community will follow

**Example:** "Monte Carlo guided Denoising Diffusion models for Bayesian linear inverse problems" (8.5, Oral) — first provably consistent algorithm for conditional sampling from diffusion posteriors, complete mathematical proofs, strong empirical results on multiple imaging tasks, code released.

### Score 7-8: Clear Accept / Good Paper
Top ~32% of reviews. Solid, significant contributions that advance the field clearly. One or two weaknesses, but nothing that undermines the core contribution.

**Hallmarks:**
- Novel insight, method, or analysis that the community hasn't seen before
- Comprehensive experiments with appropriate baselines
- Clear ablation studies isolating each component
- Well-written paper easy to follow
- May have minor gaps (e.g., missing one baseline, limited to one dataset) but core is solid

**Examples:**
- "Generalization in diffusion models arises from geometry-adaptive harmonic representations" (8.5, Oral) — compelling theory of inductive bias (GAHBs), clean empirical study with two datasets, plausible hypothesis well-tested
- "Detecting, Explaining, and Mitigating Memorization in Diffusion Models" (8.0, Oral) — clever insight (text-conditional noise magnitude as memorization signal), fast detection without training data, multiple mitigation strategies shown effective
- "SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis" (8.0, Spotlight) — large practical impact, open-sourced model, multiple novel conditioning techniques with ablations, real community impact
- "Improved Techniques for Training Consistency Models" (7.0, Oral) — thorough ablations of each improvement, competitive SOTA results, well-written, even though mainly empirical engineering

### Score 5-6: Borderline (Marginally Above/Below Threshold)
Largest cluster (~65% of all reviews). Competent work with real limitations. Scores of 5 often get rejected despite being technically sound.

**5 (Marginally below):** Correct methods but limited novelty, missing key baselines, insufficient experiments, or incremental contribution to an existing work.

**6 (Marginally above):** Mostly solid, addresses important problem, may have one notable weakness but the contribution is clear.

**What pushes a paper from 5 to 6:**
- Adding that missing ablation study
- Fixing baseline numbers (very common failure mode)
- Broadening evaluation to a second dataset
- Providing theoretical justification for empirical findings

### Score 3-4: Reject / Weak Work
Fundamental issues that cannot be fixed with minor revisions.

**Hallmarks:**
- Overclaimed novelty with directly overlapping prior work
- Wrong or cherry-picked baseline comparisons
- Contribution is literally just combining A+B without insight
- Very limited experimental scope (single dataset, single model)
- Missing entire class of relevant baselines

**Examples:**
- "LAVITA: Latent Video Diffusion Models with Spatio-temporal Transformers" (4.0, Reject) — missed related work VDT that directly overlaps; baseline numbers were wrong (PVDM reported at 2000 FVD instead of <400); performance not actually SOTA
- "Image-driven Video Editing with Latent Diffusion Models" (4.0, Reject) — poor writing, limited qualitative results, 25-minute processing time for 8 frames, no ablations, task definition unclear
- "Mitigating Generative Privacy Risks of Diffusion Models" (4.0, Reject) — perturbation method directly borrowed from Anti-DreamBooth without improvement, tested only on SD v1.4, limited novelty, missing theoretical justification

### Score 1-2: Strong Reject
Fundamentally flawed science, reproducibility crises, or clearly wrong claims. Rare (<2% of papers) but real.

---

## 3. Sub-Area Technical Knowledge

### 3.1 Generative Image/Video/Audio Synthesis

**Core technical concepts:**
- U-Net vs. Transformer (DiT) backbone tradeoffs: DiT scales better, U-Net has spatial inductive biases
- Latent space vs. pixel space: LDMs trade reconstruction quality for computational efficiency
- Text conditioning: CLIP (global) vs. T5 (fine-grained) vs. combined (SDXL uses CLIP ViT-L + OpenCLIP ViT-bigG)
- Classifier-free guidance (CFG): `ε_guided = ε_uncond + w(ε_cond - ε_uncond)` — higher w = stronger conditioning, worse diversity
- Noise schedules: linear, cosine, log-SNR, EDM-style (Karras et al. 2022)
- Multi-aspect-ratio training (bucketing) and resolution conditioning

**Video-specific concerns:**
- Spatio-temporal attention: spatial (within-frame) vs. temporal (across-frame) factorization
- Motion coherence: FlowScore, FVD (Fréchet Video Distance), CLIP-SIM
- Frame patch embedding: uniform vs. compressed, impact on quality
- Temporal consistency vs. single-frame quality tradeoff

**Expected baselines (image generation):**
- Stable Diffusion v1.x / v2.x / XL (must compare against whichever is closest in scale)
- DALL-E 2/3 (for text-to-image)
- DiT (Peebles & Xie 2023) for transformer-based architectures
- For distillation: LCM, ADD, SDXL-Turbo
- For conditioning: ControlNet, IP-Adapter, T2I-Adapter

**Expected baselines (video generation):**
- SVD (Stable Video Diffusion), AnimateDiff, ModelScope
- For pixel-space: MCVD, PVDM (if comparing older models, numbers must match original paper)
- For video editing: Tune-A-Video (TAV), Video-P2P

**Standard metrics:**
- **FID** (Fréchet Inception Distance): lower is better; standard on COCO, ImageNet, CIFAR-10
- **CLIP score**: text-image alignment; typically reported as cosine similarity
- **IS** (Inception Score): less reliable than FID; still used for CIFAR-10
- **FVD** (Fréchet Video Distance): video equivalent of FID; lower is better
- **Human preference studies**: A/B preference rates; must specify sample sizes and methodology
- **DINO similarity**, **SSCD similarity**: for memorization/copyright detection

**Red flags specific to generative models:**
- Comparing FID evaluated at different number of samples (standard is 50K)
- Reporting IS for video generation instead of FVD
- Missing the most competitive recent baseline (e.g., evaluating T2I without comparing SD-XL in 2024+)
- Reporting PVDM numbers that don't match their official paper (specific known issue from LAVITA)
- User studies with <50 participants or unclear methodology

### 3.2 Inverse Problems with Diffusion Models

**Core technical concepts:**
- Goal: sample from p(x|y) where y = Ax + n (A = degradation operator, n = noise)
- The challenge: likelihood p(y|x_t) at intermediate diffusion step t is intractable
- Key approximations: replacing x_t with denoised estimate x̂_0(x_t), Gaussian approximation of likelihood

**Method families:**
- **Projection-based:** DPS (Chung et al. 2022), DDRM, DDNM — project to constraint manifold during reverse diffusion
- **Sequential Monte Carlo (SMC):** MCGDiff — particle filtering over diffusion trajectories; first provably consistent
- **Variational approaches:** optimize over latent trajectories
- **Plug-and-play (PnP):** use diffusion model as learned prior, iterate with data fidelity

**Expected baselines:**
- DPS (Diffusion Posterior Sampling, Chung et al. 2022) — mandatory
- DDRM (Denoising Diffusion Restoration Models) for linear operators
- Score-SDE based methods (Song et al. 2021)
- DDNM (Wang et al. 2022)
- For latent diffusion: PSLD, STSL, ReSample

**Standard tasks and metrics:**
- Super-resolution (×4, ×8): PSNR, SSIM, LPIPS
- Inpainting (random mask, box mask, outpainting): PSNR, SSIM, FID on reconstructions
- Deblurring (motion/Gaussian): PSNR, SSIM
- Colorization: FID, LPIPS
- For Bayesian methods: sliced Wasserstein distance to ground truth posterior (when analytically tractable)

**Common reviewer concerns:**
- Does the method actually sample from the true posterior, or is it an approximation? What are the approximation errors?
- Is the method limited to linear inverse problems (lower bar) or does it handle non-linear?
- How does computational cost (number of NFE/function evaluations) compare?
- Can the method handle noisy measurements (not just noiseless y = Ax)?
- For latent diffusion: inconsistency between latent-space likelihood and pixel-space likelihood

**Red flags:**
- Reporting PSNR/SSIM on a very small test set (<100 images)
- Missing DPS as a baseline after it became standard in 2022
- Not reporting runtime/NFE alongside quality metrics

### 3.3 Theoretical Understanding

**Core topics:**
- **Convergence guarantees:** polynomial sample complexity, TV distance or KL divergence to target; depends on score estimation error
- **Memorization vs. generalization:** phase transition with training set size; trigger tokens, SSCD similarity
- **Inductive bias:** geometry-adaptive harmonic bases (GAHBs), spectral analysis of Jacobians
- **Training dynamics:** exposure bias in diffusion (train on clean x̂_0, test on noisy x_t approximations)
- **Discrete diffusion convergence:** masked diffusion, absorbing state diffusion

**Excellence markers in theory papers:**
- Clear mathematical setup with minimal assumptions
- Tight bounds (matching upper and lower bounds if possible)
- Connecting theoretical predictions to empirical observations
- Addressing the gap between toy models and practical architectures

**Common reviewer concerns for theory papers:**
- Does the theory apply to practical architectures (U-Net with attention, positional embeddings), or only to simplified settings (bias-free CNNs)?
- Are the assumptions realistic (e.g., assuming perfect score estimation)?
- Is there a phase transition or sharp threshold, or just a smooth dependency?
- Gap between theoretical results and observed behavior in practice

### 3.4 Efficient Training and Inference

**Core concepts:**
- **Consistency models (CM/iCT):** one- or two-step generation via self-consistency training; key innovations: pseudo-Huber loss, removing EMA from teacher, improved noise schedule
- **Distillation:** teacher diffusion model → student few-step model; includes progressive distillation, ADD, LCD
- **Deterministic samplers:** DDIM, DPM-Solver, DPM-Solver++; trade NFE vs. quality
- **Parallel sampling:** Picard iterations, ParaDiGMS; reduces wall-clock time
- **Rectified flow / Flow matching:** straighter trajectories require fewer steps; one-/multi-step possible

**Expected baselines:**
- Consistency Distillation (CD) vs. Consistency Training (CT)
- DPM-Solver++ (popular ODE solver baseline)
- For text-to-image: LCM, ADD, Hyper-SD, SDXL-Turbo
- For flow matching: RF-Solver

**Standard metrics:**
- **NFE (Number of Function Evaluations):** must report alongside FID
- FID at NFE=1, NFE=2, NFE=4, NFE=8 — show the Pareto frontier
- For flow matching: OT cost, straightness of paths

**Red flags:**
- Comparing own 2-step method against baselines run at 50+ steps without also showing the NFE-matched comparison
- Not ablating the discretization schedule
- Claiming SOTA without including recent fast samplers (if post-2023, must include LCM-family)

### 3.5 Guided and Conditional Generation

**Core concepts:**
- **Classifier guidance:** use external classifier to tilt generation toward a class; requires differentiable classifier on noisy images
- **Classifier-free guidance (CFG):** joint training of conditional and unconditional models; linear interpolation at inference
- **ControlNet-style conditioning:** adapter modules controlling spatial structure (depth, edges, pose)
- **IP-Adapter, T2I-Adapter:** lightweight adapters for image-conditioned generation
- **RLHF for diffusion:** reward alignment via DPO, PPO, or gradient-based reward optimization

**Expected baselines:**
- CFG baseline (always) — what's the benefit over just tuning the guidance scale?
- ControlNet (if proposing structural conditioning)
- UniCon, T2I-Adapter for lightweight adapter comparisons
- For RLHF/alignment: DPOK, DDPO, AlignProp, DRaFT

**Reviewer concerns:**
- Does the method generalize across different backbone diffusion models, or is it tied to one specific model?
- Does conditioning degrade diversity? (Standard critique of high-guidance methods)
- For adapter methods: compute overhead (add-on FLOPs, inference latency)

### 3.6 Scientific Applications (Protein, Molecule, Crystal)

**Core concepts:**
- Proteins: SE(3)-equivariant diffusion/flow matching over backbone coordinates; key models: FrameDiff, FoldFlow, Chroma
- Flow matching on manifolds (Riemannian manifolds, SO(3), torus)
- Molecules: SMILES string diffusion (discrete) vs. 3D coordinate diffusion (continuous); evaluation by chemical validity, drug-likeness (SA score, QED)
- Crystals: periodic structure generation; lattice + atom type + position

**Expected baselines:**
- For protein backbone generation: FrameDiff, RFdiffusion, Chroma (must compare to most recent)
- For molecular generation: GEOM, GDSS, EDM
- For protein-ligand docking: DiffDock
- For crystals: DiffCSP, CDVAE

**Standard metrics:**
- Protein: designability (scTM score, novelty vs. training set), structural diversity, secondary structure content
- Molecule: validity, uniqueness, novelty, drug-likeness (QED, SA score), property optimization
- Crystal: match rate vs. known structures, energy above hull

**Key reviewer concern:** Are experimental comparisons to physical baselines (docking scores, MD simulation) included, not just generative metrics?

### 3.7 Privacy, Safety, and Copyright

**Core concepts:**
- **Memorization types:** verbatim (exact copy), approximate (near-identical), template (semantic copying)
- **Membership inference attacks (MIA):** determine whether a sample was in the training set; SecMI, PIA, loss-based
- **Detection methods:** SSCD similarity, text-conditional noise magnitude (Wen et al. 2023)
- **Mitigation:** training-time (remove memorized samples), inference-time (perturb prompt embeddings), machine unlearning
- **Watermarking:** invisible signals embedded in generated images or in model weights; Tree-Ring, Stable Signature
- **Copyright:** fair use, style copying (not covered by copyright), exact reproduction (copyright violation)

**Expected baselines:**
- For memorization detection: SSCD-based detection (Carlini 2023), l2 distance baseline
- For watermarking: Tree-Ring, Hidden Signatures
- For MIA: SecMI (Zhu 2023), PIA, training loss threshold

**Standard metrics:**
- **AUC** (Area Under ROC Curve): for detection tasks; AUC=0.5 is random, AUC=0.999 is near-perfect
- **TPR@FPR=1%**: True Positive Rate at 1% False Positive Rate — key metric for practical detection
- **CLIP score** (to measure generation quality preservation after mitigation)
- **Bit accuracy** (for watermarking): percentage of watermark bits correctly extracted

**Red flags:**
- Evaluating only one MIA method; reviewers expect ≥2 different attack types
- Not reporting both AUC and TPR@low-FPR
- Limited to one model (e.g., only SD v1.4); multiple model versions expected
- Claiming "complete" unlearning without testing adaptive attacks

### 3.8 Flow Matching and Continuous Normalizing Flows

**Core concepts:**
- Flow matching: learns a vector field v(x, t) such that integrating ODE dx/dt = v(x,t) pushes noise to data
- Optimal transport (OT) conditional flow matching: minimize path length → straighter trajectories
- Riemannian flow matching: extends to non-Euclidean manifolds (SE(3), hypersphere, torus)
- Discrete flow matching: analogous for discrete data (tokens, graphs)

**Expected baselines:**
- Continuous normalizing flows (CNF) trained via simulation
- DDPM / consistency models for generative quality comparison
- For manifold flow: DiffSBDD, FrameFlow for proteins

---

## 4. What Excellence Looks Like

Based on analysis of oral/spotlight papers (rating ≥ 7.5):

### 4.1 Theory + Empirics Interplay
The best theory papers don't just prove theorems — they connect predictions to observed phenomena. The paper "Generalization in diffusion models arises from geometry-adaptive harmonic representations" (8.5) earned high scores by:
1. Forming a concrete hypothesis (GAHBs as inductive bias)
2. Testing it on synthetic cases where the optimal basis is known analytically
3. Testing it on cases where it's *suboptimal* (to demonstrate it persists even there)
4. Leaving clear open questions for future work

**Template for excellent theory:** hypothesis → synthetic validation → naturalistic validation → failure analysis → open questions.

### 4.2 Problem Formulation Novelty
"Detecting, Explaining, and Mitigating Memorization" (8.0) scored highly because it:
- Reframed memorization detection as a signal-processing problem (magnitude of text-conditional noise)
- Made detection dramatically faster (single step vs. multiple full generations)
- Didn't require access to training data (privacy-preserving)
- Unified detection + explanation + mitigation under one framework

**Template for excellent applications:** new formulation → insight about why existing methods fail → elegant solution → fast + no-training-data-access advantage.

### 4.3 Engineering Excellence
"SDXL" (8.0) succeeded as an engineering paper because:
- Each design choice was ablated (Table 2 was cited by multiple reviewers)
- Open-sourced the model → immediate community impact
- Novel training techniques (size conditioning, crop conditioning, multi-aspect-ratio) are generalizable insights
- Honest about what didn't help (transformer backbones showed "no immediate benefit")

**Template for excellent engineering:** ablation → ablation → ablation → open-source → honest negative results.

### 4.4 Algorithmic Completeness
"Monte Carlo guided Diffusion" (8.5) succeeded because:
- It was the *first provably consistent* algorithm (a well-defined theoretical gap filled)
- Proofs covered both noiseless and noisy observation cases
- Validated against analytically tractable posterior distributions (GMM, funnel)
- Code released
- Clear extension to non-image data discussed

**Template for excellent algorithms:** fill a known gap → prove it correctly → validate on tractable cases where ground truth is known → then apply to harder cases.

---

## 5. Common Failure Patterns

### 5.1 Missing Related Work / False Novelty Claims
**Pattern:** Paper claims to be "the first" to do X, but a directly overlapping paper exists that reviewers know.

**Example:** LAVITA (4.0, reject) claimed to be first to use transformers for video diffusion, but VDT already existed. Rating was severely penalized.

**How to catch it:**
- Search for "first to" claims and verify them
- Check if the proposed architecture (spatial-temporal decomposition, factored attention) has been done in concurrent work
- Relevant overlapping work: VDT, DiT, ViViT, CogVideo, Imagen Video, Make-A-Video

**Penalty:** A false "first" claim, when discovered, typically causes a 2-3 point rating drop even if the method works.

### 5.2 Wrong or Cherry-Picked Baseline Numbers
**Pattern:** Reproducing a baseline method and reporting significantly worse numbers than the original paper.

**Example:** LAVITA reported PVDM at FVD >2000 on UCF-101, but the original PVDM paper shows <400. This is a critical failure — it suggests the authors didn't faithfully reproduce baselines.

**How to detect:** When a very strong method (like PVDM, which is a CVPR paper) suddenly appears to perform terribly, check if the numbers match the original paper.

**How to flag it:** "The authors report [method] at [number], however the original paper reports [better number]. If the correct value is used, the proposed method does not appear to achieve SOTA."

### 5.3 Incremental Combination Without Insight
**Pattern:** Method = A + B (where A and B are known), with no explanation of why combining them works or what new phenomenon is revealed.

**Example:** The privacy mitigation paper (MixSyn, 4.0) was essentially Anti-DreamBooth perturbations + Mixup, borrowed from two existing papers. No new insight about why the combination works.

**Acceptable vs. not acceptable:**
- Acceptable: A + B combination + novel insight about interaction between components + ablation showing the combination is necessary
- Not acceptable: A + B combination with "we combine A and B" as the only justification

### 5.4 Limited Experimental Scope
**Pattern:** Method only tested on one model, one dataset, or one domain.

**Threshold for image generation:**
- Minimum: two datasets (e.g., CelebA + LSUN, or CIFAR-10 + ImageNet-64)
- Expected for SOTA claims: COCO validation set + PickScore or HPSv2 human preference

**Threshold for video generation:**
- Minimum: one dataset (UCF-101 or MSR-VTT), but two is expected
- For text-to-video: WebVid is standard

**Threshold for inverse problems:**
- Minimum: super-resolution + inpainting + deblurring (three tasks)
- Single-task papers are possible but must be much more thorough

### 5.5 Missing Ablations
**Pattern:** Multiple design choices are made, but none are ablated.

**Minimum expected ablations:**
- Loss function variants (if a new loss is proposed)
- Architecture variants (if a new module is proposed)
- Hyperparameter sensitivity (if new hyperparameters are introduced)
- Per-component contribution (if 3+ components are proposed)

**Borderline → Accept conversion:** Adding ablation studies is the most common way to convert a borderline submission into an accept.

### 5.6 Poor Scalability Justification
**Pattern:** Method is only demonstrated at small scale (CIFAR-10, ImageNet-32) when reviewers expect evidence it scales to high resolution or larger models.

**Specific concern for consistency models:** Reviewers specifically asked whether the improvements from "Improved Techniques for Training Consistency Models" (7.0) scale to text-to-image settings (256×256 → 1024×1024). This was flagged as a weakness even in an accepted paper.

### 5.7 Computational Cost Not Reported
**Pattern:** A new method is proposed without reporting inference time, training time, GPU requirements, or number of function evaluations.

**What reviewers expect:**
- NFE (number of function evaluations) for sampler papers
- GPU hours for training
- Inference latency per image/video
- Comparison of computational cost against baselines

### 5.8 Theory-Experiment Mismatch
**Pattern:** Theory makes claims about a simplified model that don't clearly apply to the experimental setup.

**Example from LAVITA:** Theory-free paper proposing architectural variants without principled justification.

**Example from iCT:** The theoretical analysis for removing EMA was considered questionable by one reviewer, but the paper was accepted because the empirical contribution was strong.

**Rule:** Theory should illuminate experiments. If theory and experiments are disconnected (one validates something the other doesn't study), this is a red flag.

---

## 6. Expected Baselines by Sub-Area

### 6.1 Text-to-Image Generation
| Baseline | When Required |
|----------|--------------|
| Stable Diffusion v1.5 | Always (pre-2024) |
| Stable Diffusion v2.1 | Always |
| SDXL | Required for post-2024 T2I papers |
| Midjourney v6 | For user study comparisons |
| DALL-E 3 | For commercial comparisons |
| DiT-XL/2 | When using transformer backbone |
| PixArt-α/Σ | When proposing transformer-based T2I |

### 6.2 Video Generation
| Baseline | When Required |
|----------|--------------|
| SVD (Stable Video Diffusion) | Always for image-to-video |
| AnimateDiff | Always for text-to-video with motion modules |
| CogVideo | For long video / text-to-video |
| Sora / VDT | When claiming SOTA |
| VDT | Required when using transformer architecture for video |

### 6.3 Inverse Problems
| Baseline | When Required |
|----------|--------------|
| DPS (Chung et al. 2022) | Always |
| DDRM | For linear problems with known operators |
| DDNM | For noiseless linear problems |
| Score-SDE (Song et al. 2021) | Always |
| MCGDiff | If solving general Bayesian inverse problems |
| PSLD / STSL | For latent diffusion inverse problems |
| PnP-ADMM | For plug-and-play comparison |

### 6.4 Efficient Sampling
| Baseline | When Required |
|----------|--------------|
| DDIM (50 steps) | Always as upper bound |
| DPM-Solver++ | Always |
| LCM | Required for 2024+ distillation papers |
| ADD / Consistency Distillation | For 2-4 step methods |
| Progressive Distillation | For distillation comparisons |

### 6.5 Protein/Molecule Generation
| Baseline | When Required |
|----------|--------------|
| RFdiffusion | Required for protein backbone design (2023+) |
| Chroma / FrameDiff | Required alternatives |
| GEOM-DRUGS / GDiff | For molecule generation |
| EDM (Hoogeboom 2022) | For 3D molecule generation |
| DiffDock | For protein-ligand docking |

### 6.6 Memorization/Privacy
| Baseline | When Required |
|----------|--------------|
| Carlini 2023 (l2-distance detection) | Always for memorization detection |
| SSCD similarity baseline | Always |
| SecMI | Always for MIA |
| PIA | For personalized model MIA |
| Anti-DreamBooth | For training-time mitigation |

---

## 7. Standard Evaluation Metrics

### Generation Quality
- **FID** (Fréchet Inception Distance): lower is better; use 50K samples unless specified
- **FID-30K**: some papers use 30K, must be consistent with compared baselines
- **Precision/Recall**: complementary to FID; precision = quality, recall = diversity
- **CLIP-Score** (ViT-L/14): for text alignment; typical range 25-35 for good models
- **PickScore / HPS v2**: learned human preference metrics; better than CLIP for T2I
- **IS** (Inception Score): used for CIFAR-10; typical range 8-12 for good models
- **FVD** (Fréchet Video Distance): for video; lower is better; typical range 50-500

### Inverse Problem Quality
- **PSNR**: peak signal-to-noise ratio; higher is better (dB)
- **SSIM**: structural similarity; higher is better (range 0-1)
- **LPIPS**: learned perceptual metric; lower is better (correlates with human judgment)
- **Posterior coverage**: sliced Wasserstein distance for Bayesian methods

### Scientific Applications
- **Designability (scTM ≥ 0.5)**: fraction of generated proteins that can be redesigned to fold to target structure
- **Diversity**: pairwise TM-score; lower = more diverse
- **Novelty**: TM-score to nearest training set structure; should be <0.7 for novel proteins
- **Validity / Uniqueness / Novelty** (VUN): for molecules; validity is chemical rules
- **QED / SA Score**: drug-likeness and synthetic accessibility; for drug design

### Classification / Detection
- **AUC**: area under ROC; for binary classification problems
- **TPR@FPR=1%**: operational metric; what fraction of true positives caught at 1% false alarm rate
- **Accuracy** (Top-1): for classification tasks

---

## 8. Common Reviewer Questions and Red Flags

### 8.1 Novelty-Related Questions
- "How does this differ from [specific prior work]?" — requires a clear novelty statement
- "Is this the first to [claim]?" — verify before assigning credit
- "What is the core insight/contribution beyond combining [A] and [B]?"
- "Does the method apply to a different class of problems than [prior work], or is it the same setting?"

### 8.2 Experimental Rigor
- "Why is [baseline X] not included?" — check if it's the standard in the sub-area
- "The reported number for [baseline] differs from their original paper — can you explain the discrepancy?"
- "How does performance change with [hyperparameter]?" — sensitivity analysis
- "Is there ablation on [component X]?" — if new components are proposed without ablation
- "What is the computational cost compared to baselines?"

### 8.3 Scalability and Generalization
- "Does this scale to larger models / higher resolutions?"
- "Is this limited to [specific architecture]?"
- "Does this apply to video / audio / 3D, not just images?"
- "How does this perform on out-of-distribution data?"

### 8.4 Theoretical Soundness
- "What assumptions does the theory require? Are they realistic?"
- "Does the theory apply to modern architectures (with attention and positional embeddings), or only simplified ones?"
- "Is there a gap between the theoretical analysis and the experimental setup?"
- "Are the proofs correct? [For math-heavy papers, reviewers with confidence ≥ 4 often check]"

### 8.5 Reproducibility
- "Is code released?" — significant positive signal; its absence is a mild negative
- "Are hyperparameters fully specified?"
- "Is the training dataset described?"
- "What GPU / compute resources are required?"

---

## 9. The Acceptance Threshold: Borderline Analysis

The acceptance threshold in this corpus is approximately **5.0** (mean 4.98). Papers at 5.0 are nearly equally likely to be accepted or rejected.

**What separates a 5.0 (borderline) from a 6.0 (clear accept):**

1. **Comprehensiveness of experiments:** A borderline paper has 1-2 tasks; a clear accept has 3+.
2. **Ablation completeness:** A borderline paper ablates 1 component; a clear accept ablates all components.
3. **Baseline correctness:** A borderline paper has one questionable baseline; a clear accept has all correct numbers.
4. **Theoretical justification:** A borderline paper has purely empirical findings; a clear accept provides some theoretical insight.
5. **Writing quality:** Both may be technically sound, but a clear accept is easier to follow.

**What separates a 5.0 (borderline) from a 4.0 (weak reject):**

1. **Core insight:** Borderline has a real insight but insufficient support; weak reject has no real insight.
2. **Missing related work:** Borderline paper acknowledges related work; weak reject misses or dismisses key papers.
3. **Baseline quality:** Borderline has incomplete baselines; weak reject has wrong/cherry-picked baselines.
4. **Experimental validity:** Borderline has sound experiments (just limited); weak reject has questionable experimental setup.

---

## 10. Domain-Specific Red Flags

### 10.1 For Generative Models
- Claiming SOTA without including models released in the last 6 months (the field moves very fast)
- Evaluating FID on different datasets than baselines
- No human preference study for text-to-image papers (2024+: PickScore is standard)
- Video generation with only single-frame quality metrics (must show temporal metrics)
- Missing FVD for video generation

### 10.2 For Inverse Problems
- Method assumes noiseless measurements (y = Ax) but real applications have noise — should at least test noisy case
- Missing DPS (Chung et al. 2022, ICLR 2023) as a baseline — this is now mandatory
- Not reporting NFE alongside quality metrics
- Testing only on "easy" degradations (low noise, mild blur)

### 10.3 For Theory Papers
- Theorem applies only to linear score functions or Gaussian distributions — not realistic
- Rate is slower than O(d/T) where d=dimension, T=steps — should match or improve known bounds
- Score estimation error is assumed zero — discuss what happens when it's not
- Missing comparison to Chen et al. 2022 or Lee et al. 2022 for convergence papers

### 10.4 For Efficient Sampling
- Claiming few-step generation without showing Pareto frontier (quality vs. NFE curve)
- Not showing failure cases at NFE=1 (nearly all methods fail at 1 step; being honest about this is expected)
- Missing text-to-image evaluation for general-purpose samplers

### 10.5 For Scientific Applications
- No structural validation beyond generative metrics (need docking scores, MD stability, or expert assessment)
- Ignoring equivariance: protein/molecule methods must be SE(3)-equivariant or justify why not
- Missing RFdiffusion (2023) as baseline for protein design papers post-2023
- No unconditional generation capability check (can the model explore the space freely?)

### 10.6 For Privacy/Safety Papers
- Evaluating only one attack type (need at least 2 MIA variants)
- Not testing adaptive attacks (adversary who knows the defense strategy)
- Using AUC alone without TPR@low-FPR
- Privacy-utility tradeoff not shown — what is the quality cost of mitigation?

---

## 11. Calibration Examples with Scores and Justifications

### Example A: Score 8.5 — "Generalization in Diffusion Models from Geometry-Adaptive Harmonic Representations"
**What reviewers praised:**
- Important open question addressed (why do diffusion models generalize from few samples?)
- Non-trivial theory connecting denoising to classical harmonic analysis (bandlets/wedgelets)
- Multiple complementary experiments: CelebA + LSUN bedrooms, optimal (Cα) and suboptimal (shuffled) image classes
- Clean, accessible writing for a broad audience

**Minor concerns (didn't lower score significantly):**
- Theory specific to bias-free CNNs; doesn't directly extend to modern U-Net with attention layers
- Limited to controlled experimental settings, not large-scale modern diffusion models

**Lesson:** A strong hypothesis, tested rigorously at controlled scale, with careful acknowledgment of limitations, can score 8.5 even if it doesn't study the largest modern models.

---

### Example B: Score 8.0 — "Detecting, Explaining, and Mitigating Memorization"
**What reviewers praised:**
- Insight that text-conditional noise magnitude correlates with memorization (simple + effective)
- No training data access needed (key practical advantage)
- Works from first diffusion step (orders of magnitude faster than previous methods)
- Three contributions: detection, trigger-token explanation, mitigation (unified framework)
- AUC = 0.999 on known memorized set

**Minor concerns:**
- CLIP score drops significantly under inference-time mitigation
- Threshold selection requires tuning

**Lesson:** A well-specified problem + elegant insight + practical advantages (speed, no data access) + quantitative evidence of improvement = 8.0 regardless of whether every conceivable experiment is run.

---

### Example C: Score 4.0 (Reject) — "LAVITA: Latent Video Diffusion Models with Spatio-temporal Transformers"
**Why it failed:**
1. **False novelty claim:** VDT already explored spatial-temporal transformers for video diffusion — not mentioned or compared
2. **Wrong baseline numbers:** PVDM reported at FVD >2000 instead of <400 — reviewers found this immediately
3. **Architectural contribution unclear:** Four variants proposed but no clear winner or principled selection
4. **Performance not actually SOTA:** Given corrected baselines, LAVITA does not improve over them

**Lesson:** A single false claim (wrong PVDM numbers) combined with a missed related work is enough to push an otherwise technically sound paper to rejection.

---

### Example D: Score 7.0 (Oral!) — "Improved Techniques for Training Consistency Models"
**What reviewers praised:**
- Thorough ablations of each technique (weighting, EMA removal, pseudo-Huber loss, discretization)
- Makes consistency training (without distillation) competitive for the first time
- Well-written, easy to follow
- SOTA on CIFAR-10 and ImageNet-64

**Minor concerns that didn't lower score enough:**
- Primarily empirical engineering without deep theoretical justification
- Limited to small datasets; question about scaling to text-to-image
- Some theoretical analysis (EMA removal) questioned by one reviewer

**Lesson:** Thorough ablations + SOTA results + well-written paper can score 7.0 (Oral) even when the contribution is "improved training techniques" rather than fundamentally new methods. Completeness and rigor compensate for limited novelty.

---

### Example E: Score 5.5 — Borderline Paper Characteristics
**Typical borderline profile:**
- Technically correct method with real, measurable improvements
- Missing 1-2 expected baselines
- Tested on single dataset
- Ablation study covers most but not all components
- Contribution is incremental: "we add [new module] to [existing framework]"
- Writing is adequate but not exemplary

**Decision factor:** Whether a borderline paper gets 5 or 6 usually comes down to whether the core insight is genuinely novel. If the insight is new but execution is incomplete → 6. If the insight is a combination of prior insights with solid execution → 5.

---

## 12. Practical Evaluation Checklist

When evaluating a new diffusion model paper, work through this checklist:

**Novelty:**
- [ ] Is the core technical contribution identified and genuinely new?
- [ ] Is there prior work that overlaps significantly? (VDT, ControlNet, DPS, RFdiffusion, etc.)
- [ ] Is the problem formulation novel, or is it the standard setting with minor modifications?

**Technical soundness:**
- [ ] Are the methods described clearly enough to reproduce?
- [ ] If theoretical, are assumptions stated and realistic?
- [ ] If empirical, are all design choices ablated?

**Experiments:**
- [ ] Are all standard baselines for this sub-area included? (Check Section 6)
- [ ] Do the reported baseline numbers match the original papers?
- [ ] Is evaluation on ≥2 datasets or ≥3 tasks?
- [ ] Are standard metrics for this sub-area used? (Check Section 7)
- [ ] Is computational cost (NFE, GPU hours, latency) reported?

**Presentation:**
- [ ] Is the paper well-written and easy to follow?
- [ ] Are figures informative and clearly captioned?
- [ ] Is code released or will it be released upon acceptance?

**Limitations:**
- [ ] Does the paper acknowledge and discuss its own limitations?
- [ ] Are failure cases shown?

**Score calibration:**
- 8+: Yes to all above, plus novel insight + provable/theoretical backing
- 6-7: Yes to most, with 1-2 gaps; core contribution is clear
- 5: Some gaps, incremental contribution, but technically sound
- 3-4: Multiple major issues (wrong baselines, false novelty claims, insufficient experiments)

---

## 13. Key Papers and Concepts to Know

### Foundational Diffusion Model Papers
- Ho et al. 2020, "DDPM" — original denoising diffusion model
- Song & Ermon 2020, "Score-based generative models" — score matching with Langevin dynamics
- Song et al. 2021, "Score-based models through SDEs" — unified SDE framework
- Dhariwal & Nichol 2021, "Diffusion models beat GANs" — classifier guidance; ADM model
- Nichol & Dhariwal 2021, "Improved DDPM" — cosine schedule, learned variance
- Song et al. 2022, "DDIM" — deterministic sampling via non-Markovian process
- Rombach et al. 2022, "LDM / Stable Diffusion" — latent diffusion; foundational for practical T2I
- Karras et al. 2022, "EDM" — unified noise schedule; Karras et al. is the standard training reference

### Key Architectural References
- Peebles & Xie 2023, "DiT" — scalable diffusion with transformers; replace U-Net
- Zhang & Agrawala 2023, "ControlNet" — spatially-conditioned generation
- Podell et al. 2024, "SDXL" — high-resolution latent diffusion with dual text encoders

### Inverse Problems
- Chung et al. 2023, "DPS" — diffusion posterior sampling; mandatory baseline
- Song et al. 2023, "MCGDiff" — provably consistent posterior sampling

### Efficient Sampling
- Song et al. 2023, "Consistency Models" — one-step distillation
- Lu et al. 2023, "DPM-Solver++" — fast ODE solver; 10-25 steps typically
- Luo et al. 2023, "LCM" — latent consistency models; text-to-image in 4 steps

### Flow Matching
- Lipman et al. 2022, "Flow Matching" — optimal transport paths
- Albergo & Vanden-Eijnden 2023, "Stochastic Interpolants"
- Chen et al. 2023, "Flow Matching on General Geometries" — Riemannian manifolds

### Theory
- Chen et al. 2022, "Sampling via score-based diffusion" — polynomial convergence
- Lee et al. 2022, "Convergence of score-based generative modeling" — near-optimal rates

---

*This skill file was generated from systematic analysis of 1293 ICLR/NeurIPS diffusion model papers (2023-2026), including deep reading of high-rated (8.5), mid-rated (7.0), and rejected (4.0) papers across multiple sub-areas. It should enable calibrated, expert-level evaluation of new research ideas in the diffusion models domain.*
