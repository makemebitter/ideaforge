# Skill File: Evaluating Image Generation Research (ICLR 2024–2026)

## Overview

This skill file equips an AI judge agent to evaluate research papers in **image generation** — a high-volume, fast-moving subfield covering text-to-image synthesis, personalization, editing, and foundational model architectures. With 829 papers analyzed (70.2% acceptance rate, mean rating 4.81), the field is competitive but not uniformly selective. Calibrated scoring requires recognizing what separates strong engineering papers from genuinely novel contributions, and what distinguishes borderline incremental work from clear rejections.

---

## 1. Topic Overview: What Image Generation Research Covers

Image generation at ICLR encompasses the following major subfields:

### 1.1 Foundational Model Architectures
- **Latent Diffusion Models (LDMs)**: Models that denoise in a compressed latent space (e.g., VAE-encoded), enabling high-resolution generation at reduced compute. SDXL and Würstchen are canonical examples.
- **Diffusion Transformers (DiT)**: Transformer-based denoising backbones replacing U-Nets. Linear attention variants (e.g., SANA) aim to reduce quadratic complexity at high resolution.
- **Flow Matching / Rectified Flows**: Continuous normalizing flows trained with straight-path ODEs; increasingly preferred over DDPM for faster sampling.
- **Autoregressive Models**: Treating image generation as next-token prediction over discrete visual tokens (VQVAE codebooks or continuous tokens).
- **GANs**: Still present but increasingly rare as main subject; more often appear as baselines.
- **VAEs**: Foundational role in latent compression; deep compression autoencoders (e.g., 32× compression vs. standard 8×) are active research.

### 1.2 Training and Fine-tuning Techniques
- **Knowledge Distillation**: Distilling large diffusion models into fewer-step generators (consistency models, progressive distillation).
- **LoRA / Low-rank Adaptation**: Parameter-efficient fine-tuning using rank-decomposed updates; nearly universal in personalization research.
- **Parameter Rank Reduction (PaRa)**: Reducing rank of model parameters during fine-tuning to constrain generation space for personalization.
- **DreamBooth / Textual Inversion**: Canonical subject-driven fine-tuning baselines; any personalization paper must outperform these.
- **Multi-aspect / Multi-resolution Training**: Training on varied aspect ratios and resolutions to improve real-world utility.
- **Classifier-Free Guidance (CFG)**: The dominant conditioning mechanism; papers proposing CFG alternatives or improvements must demonstrate meaningful gains.

### 1.3 Text-to-Image Controllability
- **Text Encoders**: Moving from CLIP (T5-XXL) to decoder-only LLMs (Gemma, LLaMA) for richer semantic alignment.
- **Complex Human Instruction (CHI)**: Using in-context prompting pipelines to improve prompt following.
- **ControlNet-style conditioning**: Spatial control via edges, depth, pose, segmentation maps.
- **IP-Adapter / Image Prompting**: Image-conditioned generation.

### 1.4 Personalization and Subject-Driven Generation
- **Single-subject fine-tuning**: DreamBooth-style, few-shot adaptation to novel concepts.
- **Multi-concept composition**: Combining multiple personalized subjects in one image.
- **Identity-preserving generation**: Maintaining identity features while enabling text-driven edits.
- **Disentanglement**: Separating identity-relevant from identity-irrelevant features (DisenBooth model).

### 1.5 Image Editing
- **Text-guided editing**: Modifying an existing image based on a text instruction.
- **Inpainting / Outpainting**: Filling masked regions consistent with the image context.
- **SDEdit / DDIM Inversion**: Noise-injection-and-denoise paradigms for editing.
- **Evaluation Metrics for Editing**: The field has ongoing challenges with evaluation — CLIPScore alone is insufficient; AugCLIP and directional CLIP similarity are emerging alternatives.

### 1.6 Efficiency and Scalability
- **High-compression autoencoders**: 32× spatial compression enabling faster DiT operation.
- **Linear attention mechanisms**: Replacing O(n²) quadratic attention with O(n) variants.
- **Inference speed**: Steps-per-image, NFEs (Number of Function Evaluations), latency benchmarks.
- **Deployment efficiency**: Running on consumer hardware (laptop GPUs) is a notable achievement.
- **Training efficiency**: GPU-hours required; Würstchen's ~9× reduction in training cost is a benchmark.

---

## 2. Evaluation Framework: Rating Scale (1–10)

Calibrated to the ICLR distribution (mean 4.81, median 4.75, std 1.15):

| Score | Band | What It Means |
|-------|------|---------------|
| 9–10 | Exceptional | Foundational work that redefines the field or sets a new SOTA that will be widely cited. Rarely awarded. |
| 8 | Strong Accept | Clear Oral/Spotlight candidate. Novel system with multiple innovations, strong empirical validation, comprehensive ablations. |
| 7 | Accept | Solid Poster. Meaningful contribution with adequate experiments. One or two minor gaps. |
| 6 | Marginal Accept | "Borderline above threshold." Interesting idea, but experiments incomplete, comparison unfair, or limited novelty. |
| 5 | Borderline | Could be either way. Usually reflects divided reviewers. Weak novel contribution or solid contribution with major missing baselines. |
| 4 | Marginal Reject | Incremental work, poor evaluation design, or claims not supported by experiments. |
| 3 | Reject | Clear deficiencies: overclaiming, missing baselines, trivial technical contribution, or theoretical errors. |
| 1–2 | Strong Reject | Fundamental technical flaws, misrepresentation, or work that is not competitive with baselines. |

**Key insight from review data**: Most accepted papers cluster around 6–8. A paper with all reviewers giving 8 is rare — that typically requires an SDXL-tier or SANA-tier system. A single 3 from a reviewer among otherwise 6s often keeps a paper borderline. The acceptance rate of 70.2% is high, meaning the bar is not extremely selective — but reviewers consistently reward novelty, ablations, and fair baselines.

---

## 3. Key Technical Dimensions and How to Evaluate Them

### 3.1 Architecture Novelty

**What to look for:**
- Is the architecture modification genuinely new, or is it a combination of existing techniques?
- Does the paper provide a principled motivation (theoretical or empirical) for the architectural choice?
- Are ablations provided for each proposed component?

**Common patterns:**
- **Strong**: Introducing linear attention into DiT (SANA), three-stage latent hierarchy (Würstchen), or a novel autoencoder compression scheme.
- **Weak**: Combining LoRA + existing architecture with no explanation of why the combination is non-trivial.
- **Flag**: "We combine A, B, and C" papers where each component already exists in published work and the ablations don't demonstrate synergistic effects.

**Questions to ask:**
- Could the same result be achieved by simply using a larger existing model?
- Is the proposed architecture significantly different from VP-SDE / standard DDPM / LDM variants, or just a different noise schedule?

### 3.2 Training Techniques

**What to look for:**
- Parameter count comparisons (total vs. diffusion model only — reviewers penalize inconsistency)
- Training data disclosure (LAION vs. proprietary data — any undisclosed data advantage must be acknowledged)
- Training efficiency claims must be supported with actual GPU-hour comparisons

**Red flags:**
- Comparing to baselines with less training data
- LoRA rank not matched between baselines and proposed method
- Claiming efficiency gains without measuring wall-clock time

### 3.3 Evaluation Metrics and Benchmarks

**Standard benchmarks (2024–2026):**
- **FID** (Fréchet Inception Distance): Lower is better; must be computed at standard resolution (256×256 or 1024×1024)
- **IS** (Inception Score): Less reliable than FID; must note resolution
- **CLIP Score / CLIP-T**: Text-image alignment; often insufficient alone
- **HPSv2** (Human Preference Score v2): Increasingly expected for T2I
- **ImageReward**: Human preference for T2I
- **DINO Score**: For personalization fidelity
- **MS-COCO**: Standard benchmark for T2I; 30K sample subset expected
- **DrawBench / PartiPrompts**: Compositional generation evaluation
- **TIFA**: Text-image faithfulness
- **Human evaluation / User studies**: Expected for high-resolution generation claims

**For personalization papers:**
- DINO similarity (subject fidelity)
- CLIP-T (text alignment)
- Human preference studies
- DreamBench (subject-driven generation benchmark)

**Common metric mistakes:**
- Using CLIP similarity as the only metric for editing (AugCLIP or directional CLIP similarity expected)
- Reporting FID at non-standard resolutions without explanation
- Not reporting confidence intervals for human studies (small N is a red flag)
- Using IS without noting resolution (CIFAR-10 and MS-COCO FID/IS numbers are resolution-dependent)

### 3.4 Efficiency Claims

**What is expected:**
- Wall-clock inference time comparisons (not just FLOPs)
- NFE (number of function evaluations) comparisons
- GPU memory requirements at inference
- Training cost comparisons (GPU-hours)

**Strong efficiency claims (calibration):**
- SANA: 100× speedup over comparable quality models, laptop-deployable → Oral
- Würstchen: ~9× GPU training hour reduction → Oral
- Merely "faster than DDPM" without comparison to modern ODE samplers is insufficient

**Red flag:** Papers claiming efficiency gains without comparing to DDIM, DPM-Solver, or flow-matching baselines (which already offer significant speedups).

### 3.5 Controllability and Text Alignment

**What to look for:**
- Does the paper quantify text-image alignment (CLIP-T, TIFA, or human evaluation)?
- Are there failure cases or qualitative comparisons on challenging prompts?
- Does the paper address multi-object composition, counting, color binding?

**Typical weaknesses in this area:**
- Text-image alignment evaluated only on FID (FID can be high-quality but semantically misaligned)
- No comparison on compositional prompts (multiple objects, spatial relationships)
- Claims about "better alignment" supported only by cherry-picked qualitative examples

### 3.6 Personalization-Specific Dimensions

**What is expected:**
- Comparison against DreamBooth, Textual Inversion, and ideally Custom Diffusion and SVDiff
- LoRA fine-tuning is a strong baseline that must be included
- Multi-subject composition results (if claimed)
- Single-image editing consistency
- Identity preservation under text variation (different contexts, poses, etc.)

**Common weaknesses:**
- Not comparing to encoder-based personalization methods (ELITE, E4T)
- Only testing on objects, not human faces/identities
- Insufficient number of test subjects for quantitative claims

---

## 4. Common Strengths to Recognize

Based on frequency in accepted paper reviews:

### 4.1 Novelty (cited 598× in strengths)
- Genuinely new architectural component (not just a combination of known techniques)
- New problem formulation with clear motivation
- Creative application of existing tools to a genuinely new problem

### 4.2 Ablation Studies (cited 399× in strengths)
- Component-by-component ablations (each proposed innovation tested independently)
- Hyperparameter sensitivity analysis
- Ablations on multiple datasets
- "Comprehensive ablation" is explicitly praised; absent ablations are the #1 cited weakness

### 4.3 Strong Baselines (cited 341× in strengths)
- Contemporary baselines (within 12 months of submission)
- Comparable compute and data budgets
- Open-sourced baselines using their best settings (not cherry-picked)

### 4.4 Well-Written (cited 283× in strengths)
- Clear organization with explicit problem statement, method overview figure, and results table
- Consistent notation
- Self-contained explanations without excessive undefined acronyms

### 4.5 State-of-the-Art Results (cited 141× in strengths)
- Results that clearly exceed existing published methods
- Results on multiple benchmarks (not just one dataset)
- Human evaluation supporting quantitative metrics

### 4.6 Scalability (cited 81× in strengths)
- Demonstrated results at multiple resolutions (512, 1024, 4096)
- Results with different model sizes (small, medium, large)
- Efficiency claims that hold at scale

### 4.7 Reproducibility (cited 63× in strengths)
- Code release
- Detailed implementation details (learning rates, batch sizes, training duration)
- Public checkpoints
- Pseudo-code or algorithm boxes

---

## 5. Common Weaknesses to Flag

Based on frequency in weakness phrases (calibrated to the review data):

### 5.1 Missing Baselines (cited 1038× in weaknesses — the #1 concern)
**Always ask:**
- Are the most recent methods (within 12 months) included?
- Are baselines using their best hyperparameters?
- Are unfair advantages acknowledged (more data, larger model, more training time)?

**Specific baselines almost always expected:**
- For T2I: Stable Diffusion 1.x, SDXL, PixArt-α/Σ, FLUX, Playground v3
- For personalization: DreamBooth, LoRA, Textual Inversion, Custom Diffusion, SVDiff
- For efficiency: DPM-Solver, DDIM, Flow Matching
- For editing: SDEdit, Prompt-to-Prompt, InstructPix2Pix, DDIM Inversion

### 5.2 Missing Ablation Studies (cited 662× in weaknesses)
Papers that propose 3 components but only ablate 1 are consistently penalized. Every proposed component should be ablated.

### 5.3 Limited Novelty (cited 639× in weaknesses)
**"Incremental" is cited 131×.** Reviewers distinguish between:
- Engineering contributions (valid but should be framed as such)
- Conceptual contributions (new insight about how the problem should be solved)
- System contributions (combine known techniques into a more capable/efficient system)

A paper combining existing techniques (A + B + C) must demonstrate that the combination is non-trivial and provide ablations showing each component's individual contribution.

### 5.4 Lack of Evidence (cited 382× as "lack of")
- "Lack of comparison with recent methods"
- "Lack of ablation study"
- "Lack of theoretical justification"
- "Lacks human evaluation"
- "Lacks failure case analysis"

### 5.5 Scalability Concerns (cited 161× in weaknesses)
- Does the method work only on small datasets / small resolutions?
- Are results only at 512×512 when the method claims high-resolution capability?
- Does the approach require per-sample fine-tuning that doesn't scale?

### 5.6 Reproducibility Concerns (cited 130× in weaknesses)
- Training details missing (dataset size, learning rate schedule)
- No code or checkpoints
- Inference time not reported
- Evaluation protocol unclear

### 5.7 Unfair Comparisons (cited 76× as "fair comparison")
- Paper's model uses larger backbone but comparison is presented as equivalent
- Baselines not using their optimal settings
- Using ViT-L vs. ResNet50 backbone without acknowledging the capacity difference
- Training data advantage not disclosed

---

## 6. Baseline Expectations by Subfield (2024–2026)

### 6.1 Text-to-Image Generation (General)
**Minimum expected baselines:**
- Stable Diffusion v1.5, v2.1, SDXL
- PixArt-α and/or PixArt-Σ (if efficiency-focused)
- DALL-E 3 or Midjourney v5+ as upper-bound reference
- FLUX.1 (2024) as a strong open-source baseline for recent work

**Expected benchmarks:**
- MS-COCO FID and CLIP-T
- HPSv2 or ImageReward for preference
- GenEval or TIFA for compositional accuracy
- Human evaluation with statistical significance

### 6.2 Efficient Generation
**Minimum expected baselines:**
- DDIM (baseline ODE sampler)
- DPM-Solver++
- Consistency Models (if distillation-focused)
- Latent Consistency Models (LCM)
- Würstchen (if training efficiency is the claim)

**Expected metrics:**
- NFEs at equivalent quality (FID-NFE tradeoff curve)
- Wall-clock time (not just FLOPs)
- GPU memory at inference
- Training GPU-hours

### 6.3 Personalization
**Minimum expected baselines:**
- DreamBooth (fine-tuning-based)
- Textual Inversion
- LoRA (must use same or comparable rank to proposed method)
- Custom Diffusion (multi-concept)
- SVDiff

**Strongly recommended (2024–2026):**
- LyCoris, DiffuseKronA (if comparing against rank-reduction methods)
- ELITE, E4T (encoder-based — must include if claiming zero-shot or few-shot advantages)
- InstantID, IP-Adapter (if identity-preserving claim)

**Expected metrics:**
- DINO cosine similarity (subject fidelity)
- CLIP-T (text alignment)
- Human evaluation (DreamBench protocol)
- Number of fine-tuning steps/images (efficiency claim support)

### 6.4 Image Editing
**Minimum expected baselines:**
- Prompt-to-Prompt (P2P)
- InstructPix2Pix
- SDEdit
- DDIM Inversion + text guidance
- Null-text Inversion

**Expected metrics:**
- CLIP directional similarity (modification)
- LPIPS or SSIM (preservation)
- Human evaluation (two-alternative forced choice)
- Note: CLIPScore alone is insufficient for editing (multiple reviewers flag this)

---

## 7. Tiered Rubric with Calibration Examples

### 7.1 Excellent (8–10): Oral/Spotlight Quality

**Characteristics:**
- Multiple genuine innovations that work synergistically
- State-of-the-art results on established benchmarks by clear margin
- Comprehensive ablations for each component
- Strong efficiency or scalability results
- Well-written, reproducible, code released or promised
- Addresses a real limitation of prior work convincingly

**Real examples:**

**SANA (rating=8.5, Oral):**
- Four distinct innovations: 32× deep compression autoencoder, linear DiT replacing quadratic attention, decoder-only LLM text encoder, Flow-DPM-Solver
- 100× faster than comparable quality models; laptop-deployable
- Comprehensive ablations for each component
- FID and speed benchmarks at multiple resolutions
- Reviewers noted slight concern about individual components being published separately elsewhere, but the *system* integration and empirical results justified Oral status
- Lesson: Even when components individually exist, a well-validated system paper with strong empirical results can earn Oral. The key was comprehensive ablations and the magnitude of efficiency gain.

**SDXL (rating=8.0, Spotlight):**
- Larger U-Net (3× parameter increase), dual text encoders (CLIP ViT-L + OpenCLIP ViT-bigG)
- Novel conditioning schemes: image size conditioning, crop conditioning, multi-aspect training
- New VAE with EMA + large batch training
- Refinement model stage
- Open-sourced (major community impact)
- Lesson: Systems-paper-style contributions can score very high if the engineering choices are well-ablated and the results are competitive with closed models.

**Würstchen (rating=8.0, Oral):**
- Three-stage architecture where Stage C operates on 24×24 latent (vs. 64×64+ for most LDMs)
- 9× GPU training hour reduction
- Competitive FID/IS despite much smaller training budget
- Well-motivated semantic compressor design
- Weakness acknowledged: ablation study requested by reviewers (added in rebuttal)
- Lesson: Training efficiency with maintained quality at scale is highly valued. Papers should explicitly quantify training cost savings.

**PaRa (rating=7.5, Spotlight):**
- Novel idea: rank reduction of model parameters to constrain generation space
- 2× parameter efficiency vs. LoRA
- Extensive experiments on single/multi-subject generation and editing
- Conceptually clean motivation (small concept = small rank space)
- Lesson: Clean conceptual contribution + parameter efficiency + comprehensive experiments = Spotlight without being a full system paper.

**DisenBooth (rating=7.5, Poster):**
- Identity-preserving disentangled tuning
- Novel dual embedding objective (identity-relevant + identity-irrelevant)
- Weak denoising and contrastive embedding losses
- Strong ablation studies
- Lesson: Personalization papers succeed when they have a clear disentanglement motivation, thorough ablations, and good qualitative results.

### 7.2 Good (6–7): Strong Poster Quality

**Characteristics:**
- One clear novel contribution
- Reasonable baselines (may be missing 1–2 recent methods)
- Adequate ablations (may miss some component ablations)
- Results competitive or slightly above SOTA
- Minor presentation or evaluation gaps

**Patterns from borderline-accepted papers:**
- SEED Tokenizer (6.33): Interesting T2I unification via discrete tokens, but limited FID evaluation, FID was not reported (only CLIP similarity), reviewers noted fairness issues with backbone comparisons
- Inner CFG / ICFG (6.0): Theoretically interesting but marginal empirical improvement (FID 15.42 → 15.22); additional compute cost (3 forward passes) not fully resolved
- CompoDiff (5.25): Novel CIR approach with large-scale dataset, but dataset fairness comparison issues and small improvements over baselines with same architecture

### 7.3 Borderline (4–5): Could Go Either Way

**Characteristics:**
- Idea has merit but execution is weak
- Missing key baselines (especially recent ones)
- Ablations insufficient or missing
- Results do not clearly outperform simpler baselines
- Evaluation design flawed (wrong metrics, unfair conditions)

**Pattern signals:**
- "The idea is interesting but...": Usually means the reviewer sees potential but experiments don't support claims
- "Marginal improvement over X": FID or CLIP score improvement of <0.5 points
- "Limited novelty" combined with incomplete experiments
- Evaluation metrics that don't capture the claimed advantage

**AugCLIP (4.25, Rejected):**
- Proposed a new evaluation metric for text-guided image editing
- Interesting observation about CLIPScore limitations
- Overclaimed contributions ("first to point out...")
- Wrong definition of CLIPScore used (vs. standard definition)
- Only evaluated on one editing method per benchmark
- Did not compare with methods from same year
- Lesson: Metric papers must be evaluated on diverse methods; overclaiming kills credibility

### 7.4 Weak (1–3): Clear Rejection

**Characteristics:**
- No genuine novelty beyond combining existing techniques trivially
- Missing major relevant baselines (e.g., no comparison to EDM when claiming efficiency)
- Theoretical flaws (e.g., strong duality claimed for non-convex problems)
- Overclaiming (e.g., "decoupled" diffusion that is mathematically equivalent to VP-SDE with different noise schedule)
- Generated images visually worse than baselines

**Decoupled Diffusion Models (3.5, Rejected):**
- Claimed novel "image-to-zero + zero-to-noise" decoupling
- Reviewer demonstrated mathematically that the proposed forward process reduces to VP-SDE with different noise scheduling
- Missing key baselines: no EDM, no DPM-Solver comparison
- Images described as "too smooth and hence not realistic"
- Poor theoretical justification for why decoupling improves sampling
- Lesson: The most penalized pattern in this domain is claiming conceptual novelty when the method is mathematically equivalent to or a strict subset of prior work.

---

## 8. Specific Red Flags That Lower a Score

### 8.1 Mathematical/Theoretical Red Flags
- **Claiming a known technique is novel**: Check if the proposed forward process, loss function, or architectural component reduces to a published method under substitution. This is the most damaging criticism in diffusion model papers.
- **Unjustified strong duality**: Non-convex optimization problems do not admit strong duality without convexification.
- **Incorrect metric definitions**: Using a non-standard definition of CLIPScore, FID, or CLIP similarity without acknowledgment destroys credibility with knowledgeable reviewers.
- **Missing derivation steps**: Particularly in continuous-time diffusion models, hand-wavy derivations will be caught by expert reviewers.

### 8.2 Evaluation Red Flags
- **FID without resolution specification**: FID is resolution-dependent; 256×256 and 1024×1024 numbers are not comparable.
- **User study with N < 30 per comparison**: Statistical significance is not achievable.
- **Only qualitative comparisons**: Any claim of "better quality" needs quantitative support.
- **Cherry-picked examples only**: No failure case analysis is an explicit weakness.
- **CLIPScore-only for editing**: Reviewers consistently flag this as insufficient; directional CLIP similarity and preservation metrics are required.
- **FID at non-standard sampling steps**: Must specify NFE when reporting FID.
- **Reporting Inception Score without FID**: IS is less reliable; FID is the primary metric.

### 8.3 Baseline Red Flags
- **Comparing to methods more than 2 years old**: If work was submitted in 2025 but only compares to 2021–2022 baselines, this will be penalized.
- **Missing LoRA comparison for personalization**: LoRA is a strong, fast baseline that must be included.
- **Not matching backbone capacity**: Comparing ViT-L backbone to ResNet-50 without acknowledging the gap.
- **Using original published numbers from different training data**: If baselines were not retrained on the same data, differences may be due to data, not method.
- **No encoder-based personalization comparison**: ELITE, IP-Adapter are must-include for personalization claims.

### 8.4 Scalability Red Flags
- **Only demonstrated at 512×512 resolution**: High-resolution claims require high-resolution evaluation.
- **Only on CIFAR-10 or LSUN**: These datasets are too simple for 2024–2026 standards.
- **Per-subject fine-tuning with no inference time analysis**: If the method requires fine-tuning per concept, this must be quantified.
- **No real-world or out-of-distribution testing**: Methods that only work on clean, centered, high-quality training images.

### 8.5 Presentation Red Flags
- **Undefined acronyms throughout**: Overuse of acronyms degrades readability significantly.
- **Missing algorithm pseudocode for complex methods**: For multi-stage pipelines, explicit algorithms are expected.
- **Figure captions that don't stand alone**: Reviewers should not need to read the full text to understand a figure.
- **No limitation section**: Papers must acknowledge failure cases and scope limitations.

---

## 9. Domain-Specific Nuances

### 9.1 Personalization vs. General T2I

These are evaluated differently. A personalization paper (DreamBooth-style) is expected to:
1. Demonstrate per-concept fine-tuning efficiency (fewer images, fewer steps)
2. Maintain generative diversity (not overfit to training images)
3. Achieve text editability (the concept in different contexts)
4. Separate identity from background/style

Metrics for personalization are fundamentally different from general T2I:
- FID is inappropriate (fine-tuned model generates a specific concept, not the distribution)
- DINO similarity + CLIP-T + human evaluation is the standard

A paper that applies general T2I metrics (FID on MS-COCO) to a personalization method shows a methodological misunderstanding.

### 9.2 Efficiency vs. Quality Tradeoff

Papers claiming efficiency gains must explicitly address the efficiency-quality tradeoff:
- Present the FID-NFE Pareto curve (not just a single operating point)
- Compare against dedicated fast samplers (DPM-Solver, Consistency Models, LCM) not just DDPM
- Acknowledge whether quality is maintained or degraded at the operating point

A paper that is faster but has worse FID without acknowledging this tradeoff will be penalized.

### 9.3 System Papers vs. Algorithmic Papers

**System papers** (SDXL, SANA, Würstchen) are evaluated primarily on:
- Scale of the system and practical utility
- Quality and breadth of ablations
- Open-source contribution
- Community impact potential
- Empirical results on standard benchmarks

**Algorithmic papers** (PaRa, DisenBooth, ICFG) are evaluated primarily on:
- Conceptual novelty of the algorithm
- Theoretical motivation (if applicable)
- Ablations demonstrating each component's contribution
- Comparison to nearest algorithmic prior work

Mixing these standards is a common error. A system paper should not be penalized for not having a mathematical proof, and an algorithmic paper should not be praised only for system-level results.

### 9.4 Architecture Novelty in a Saturated Space

By 2024–2026, the diffusion model architecture space is crowded. The key questions:
- Is the proposed change well-motivated (not just "we replaced X with Y")?
- Does the change lead to measurably better tradeoffs (quality/speed/memory)?
- Are there ablations showing the specific contribution of the architectural change?

Simply "replacing quadratic attention with linear attention" is not novel by itself — many papers have done this. What earns novelty credit is showing that the combination (e.g., linear attention + 32× compression + LLM text encoder) creates emergent benefits beyond what each component achieves independently.

### 9.5 Evaluation Metric Validity

The image generation field has ongoing debate about metrics:
- **FID** measures distribution similarity, not perceptual quality
- **CLIP Score** measures text-image alignment but not generation fidelity
- **HPSv2/ImageReward** measure human preference but are training-data-dependent
- **Human evaluation** is the ground truth but expensive and slow

A paper that exclusively uses FID will be questioned on text-image alignment. A paper that exclusively uses CLIP score will be questioned on image quality. The strongest papers use multiple metrics covering multiple dimensions (quality, alignment, diversity, preference).

### 9.6 Decoder-Only LLM as Text Encoder

A trend from 2024–2025: replacing T5-XXL with decoder-only LLMs (Gemma, LLaMA) as text encoders. Reviewers will ask:
- Why this LLM specifically? (Comparison to T5 and other LLMs expected)
- Does the benefit come from the LLM architecture or from better instruction following via CHI?
- Can larger LLMs further improve performance?
- Does the text encoder choice interact with the image decoder architecture?

### 9.7 High-Resolution Generation Claims

Any paper claiming high-resolution generation (2K, 4K) must:
- Show quality comparisons at that resolution (not just speed comparisons)
- Provide FID or human evaluation at high resolution
- Acknowledge that FID-based metrics have limitations at very high resolution
- Compare against methods specifically designed for high resolution (UltraPixel, etc.)

The gap between "can generate 4096×4096" and "generates good 4096×4096 images" must be closed with evidence.

---

## 10. Calibration Reference Table

| Paper | Rating | Decision | Key Distinguishing Features |
|-------|--------|----------|----------------------------|
| SANA | 8.5 | Oral | 4 integrated innovations; 100× speed; 4K generation; comprehensive ablations; laptop deployable |
| SDXL | 8.0 | Spotlight | 3× larger U-Net; novel conditioning; multi-aspect training; open-source; community impact |
| Würstchen | 8.0 | Oral | 9× training efficiency; 3-stage semantic hierarchy; competitive FID; code released |
| PaRa | 7.5 | Spotlight | Novel rank reduction for personalization; 2× parameter efficiency; comprehensive experiments |
| DisenBooth | 7.5 | Poster | Identity disentanglement with weak denoising + contrastive losses; strong ablations |
| SEED Tokenizer | 6.33 | Poster | Interesting T2I unification; limited FID evaluation; backbone fairness issues |
| Inner CFG | 6.0 | Poster | Theoretically novel but marginal empirical gain (FID 15.42→15.22); 3 forward passes cost |
| Decoupled Diffusion | 3.5 | Reject | Mathematically equivalent to VP-SDE; missing EDM baseline; smooth/unrealistic outputs |
| AugCLIP metric | 4.25 | Reject | Overclaims; wrong CLIPScore definition; evaluated on only one method per benchmark |

---

## 11. Judging Heuristics and Practical Advice

### 11.1 The "Should Have Compared" Test
When reading a paper, ask: "What is the most obvious recent method they should have compared against?" If that method is missing from baselines and it is within 12 months of the venue deadline, this is a significant weakness.

### 11.2 The "Why Not Just..." Test
For architectural papers: "Why not just use standard X with Y configuration?" If the paper doesn't answer this clearly, the contribution is weakly motivated.

### 11.3 The Ablation Count Heuristic
Count the number of proposed innovations. Count the number of ablation experiments. If the ratio is < 0.7 (fewer ablations than innovations), the experimental section is incomplete.

### 11.4 The "Biggest Table" Pattern
Many image generation papers have a large comparison table as their main result. Evaluate whether:
- All entries in the table use consistent settings (same resolution, same NFEs)
- Model parameter counts are comparable across methods
- Training data is comparable
- The comparison is truly fair

### 11.5 The "Claimed vs. Demonstrated" Gap
Flag any paper where the abstract/intro claims X but the experiments demonstrate X-epsilon or only demonstrate X on toy settings. Common examples:
- Claims 4K generation → only qualitative 4K samples, no 4K FID
- Claims better text alignment → only FID reported, no CLIP-T
- Claims efficient training → only inference efficiency measured

### 11.6 Distinguishing Incremental from Genuinely Novel

**Incremental (lower score):**
- Applies existing technique from domain A to domain B without theoretical justification
- Combines two existing methods with no synergistic benefit
- Modifies a hyperparameter or loss weight and claims novelty

**Novel (higher score):**
- Identifies a genuine limitation of prior work and proposes a principled solution
- Provides theoretical grounding or empirical insight into *why* the approach works
- Enables qualitatively new capabilities (e.g., 4K generation, laptop deployment)
- Achieves a new efficiency frontier (e.g., 9× training reduction with maintained quality)

### 11.7 The Reviewer Confidence Calibration
When a reviewer gives a low score with confidence 2–3, weight it less heavily than a reviewer with confidence 4–5. A confident 3 is more damaging than an uncertain 3. Similarly, a confident 8 carries more weight than a hedged 8.

---

## 12. Summary: Quick-Reference Checklist for Evaluation

Before scoring a paper, verify:

**Technical Correctness**
- [ ] No mathematical errors (e.g., non-convex duality claimed, incorrect metric definitions)
- [ ] Proposed method is not mathematically equivalent to a published baseline
- [ ] Theoretical claims supported by proofs or rigorous empirical justification

**Novelty**
- [ ] At least one genuinely new technical contribution
- [ ] Contribution is non-trivial (not just combining A+B without justification)
- [ ] Related work section addresses the most relevant prior art within 12 months

**Experiments**
- [ ] Ablation for each proposed component
- [ ] State-of-the-art baselines (within 12 months of submission)
- [ ] Multiple metrics covering quality, alignment, and diversity
- [ ] Fair comparison (same compute, data, and resolution)
- [ ] Quantitative results (not just qualitative)

**Efficiency Claims (if applicable)**
- [ ] FID-NFE Pareto curve (not just one operating point)
- [ ] Wall-clock time, not just FLOPs
- [ ] Comparison to dedicated fast samplers

**Personalization Claims (if applicable)**
- [ ] DreamBooth + LoRA + Textual Inversion baselines present
- [ ] DINO similarity + CLIP-T + human evaluation reported
- [ ] Multi-concept tested (if claimed)

**Reproducibility**
- [ ] Training details sufficient to reproduce
- [ ] Code or checkpoint released/promised
- [ ] Evaluation protocol specified (N samples, resolution, seeds)

**Presentation**
- [ ] Clear method overview figure
- [ ] Failure cases acknowledged
- [ ] No overclaiming in abstract/intro
- [ ] Consistent notation throughout

---

## Appendix A: Key Terminology Quick Reference

| Term | Definition |
|------|-----------|
| FID | Fréchet Inception Distance; distribution similarity metric; lower is better |
| IS | Inception Score; quality and diversity metric; higher is better |
| NFE | Number of Function Evaluations; proxy for inference cost |
| CFG | Classifier-Free Guidance; guidance scale controls quality-diversity tradeoff |
| DDPM | Denoising Diffusion Probabilistic Models; standard stochastic sampler |
| DDIM | Denoising Diffusion Implicit Models; deterministic ODE sampler |
| DPM-Solver | Fast ODE solver for diffusion; typically 20 NFEs for competitive FID |
| DiT | Diffusion Transformer; transformer-based backbone replacing U-Net |
| LDM | Latent Diffusion Model; diffusion in VAE latent space |
| LoRA | Low-rank Adaptation; parameter-efficient fine-tuning method |
| T2I | Text-to-Image generation |
| CLIP-T | CLIP text-image alignment score |
| DINO | Self-supervised ViT features; used for subject fidelity in personalization |
| HPSv2 | Human Preference Score v2; trained on human preference data |
| Flow Matching | Continuous normalizing flow with straight-path training objective |
| CHI | Complex Human Instruction; in-context learning for text encoder improvement |

---

## Appendix B: Deep Dive — How High-Rated Papers Were Defended Against Reviewer Concerns

Understanding the rebuttal dynamics of highly rated papers reveals what the community considers truly important vs. what can be addressed post-hoc.

### B.1 SANA (8.5 Oral) — How Novelty Concerns Were Navigated

SANA's reviewers raised an important concern that appears frequently in high-rated systems papers: "All three main components have been already explored in the literature, deep autoencoder in [1], linear DiT in [2] and using LLM as text encoder in [3, 4]. So combining them is not really a significant novel idea."

The paper was still awarded Oral status because:
1. **System-level novelty**: Despite individual components existing in isolation, the *combination* and the resulting empirical performance (100× speedup, laptop deployment) was demonstrably novel at the system level.
2. **Scale of contribution**: 4K resolution generation on a laptop was qualitatively beyond what any single prior component enabled.
3. **Practical significance**: The efficiency claims had verifiable real-world impact that the community valued.
4. **Comprehensive ablations**: Every component was individually ablated, satisfying the reviewers who questioned novelty.

**Lesson for the judge**: When evaluating "combination papers," the key question is not whether each component individually exists, but whether:
(a) The combination enables qualitatively new capabilities
(b) Each component is validated independently through ablations
(c) The system-level results are substantially beyond prior work

A combination paper that merely matches prior SOTA with less compute is borderline. A combination paper that opens entirely new operating regimes (4K on laptop) merits higher scores.

### B.2 Würstchen (8.0 Oral) — Ablation Added in Rebuttal

The initial Würstchen submission received a review asking for ablation studies and additional evaluation metrics (CLIPScore was missing from the original submission). The reviewer raised the score to Accept after the authors added these in the rebuttal.

This illustrates an important pattern: **papers that are conceptually strong but have evaluation gaps can often recover score during rebuttal** — but only if the core idea is sound and the missing experiments are achievable.

**Lesson for the judge**: When flagging missing ablations or metrics, differentiate between:
- "Missing ablations that would likely confirm the story" (borderline, can be fixed in rebuttal)
- "Missing ablations that would likely undermine the story" (stronger rejection signal)

For Würstchen, reviewers were confident the architecture was genuinely efficient, so the missing CLIPScore was a presentation gap, not a fundamental validity concern.

### B.3 DisenBooth (7.5 Poster) — Missing Baselines Tolerated at Poster Level

DisenBooth received criticism for not comparing against Break-a-scene, Custom Diffusion, and SVDiff (all published that year). Yet it was accepted as a Poster.

Why was this tolerable?
1. The core disentanglement mechanism was novel regardless of the missing comparisons.
2. The ablations were comprehensive for the proposed components.
3. The qualitative results were strong.
4. The missing baselines were published concurrent with or after DisenBooth's submission, making the comparison impractical.

**Lesson for the judge**: Missing baselines published concurrently (within 1–2 months of submission deadline) are less penalized than missing baselines that were clearly available before the deadline. For ICLR, the submission deadline context matters.

---

## Appendix C: Scoring Difficult Cases — Common Judgment Scenarios

### C.1 "Interesting idea, marginal results"

A paper proposes a theoretically interesting extension of CFG (Inner CFG). The math is novel, but the empirical gain is FID 15.42 → 15.22 on MS-COCO. Additional compute cost: 3 forward passes instead of 2.

**How to score:**
- If the theoretical insight is genuinely novel and well-proven: 5–6
- If the theoretical insight is interesting but the compute overhead exceeds the gain: 4–5
- If the method requires additional hyperparameter tuning to achieve those marginal gains: 4

The key question: "Would a practitioner use this?" If the answer is no due to cost/gain tradeoff, the score should reflect limited practical contribution.

### C.2 "Large dataset + fine-tuned model = good results"

A paper introduces a large synthetic dataset (e.g., 18M triplets) for image retrieval and trains a model on it. Results on benchmarks are better, but reviewers note:
1. Backbone capacity differs (ViT-L vs. RN50)
2. The improvement plateaus after a certain dataset size
3. The diffusion model used is essentially a minor modification of Stable Diffusion

**How to score:**
- Dataset contribution alone: 5–6 (if large, novel, publicly released)
- Dataset + significantly modified model: 6–7
- Dataset + essentially the same model: 4–5 (the dataset is the contribution, not the method)

For pure dataset papers in image generation, the key questions are:
- Is the dataset significantly larger or more diverse than existing options?
- Does the paper demonstrate that the dataset specifically enables capabilities not achievable with existing data?
- Is the dataset publicly released?

### C.3 "New metric paper"

A paper proposes a new evaluation metric (e.g., AugCLIP) for text-guided image editing. The metric correlates better with human judgments than CLIPScore.

**How to score:**
- If evaluated on diverse methods (5+) across multiple benchmarks: 6–7
- If only evaluated on 1 method per benchmark: 4–5 (insufficient validation)
- If the definition of the baseline metric is incorrect: automatic score reduction to 3–4

Metric papers are particularly sensitive to:
1. **Validation breadth**: Must test on many methods, not just 1–2
2. **Human study design**: Must have meaningful N and be statistically significant
3. **Correctness**: Any mischaracterization of existing metrics is a hard disqualifier
4. **Overclaiming**: "First to point out X" when prior work has extensively documented X is a credibility destroyer

### C.4 "Strong results, incremental idea"

A paper fine-tunes SDXL with a novel multi-stage training procedure and achieves the best HPSv2 score on DrawBench. The method is a series of engineering choices (learning rate schedule, data filtering, aspect ratio training, refiner training) without a unifying theoretical insight.

**How to score:**
- If all engineering choices are ablated and the result is SOTA: 6–7
- If SOTA by a clear margin and code/model released: 7–8
- If SOTA by marginal margin (within noise): 5–6

Engineering papers can score highly if they are well-documented (enabling the community to replicate), but the absence of a conceptual contribution limits them to the 6–7 range unless the results are truly exceptional.

### C.5 "Novel architecture, no fair comparison"

A paper proposes a new transformer-based architecture for image generation that achieves FID 3.2 on ImageNet 256×256. However, the model has 2× the parameters of the baseline and was trained for 3× longer.

**How to score:**
- Without matching parameter count and compute: 4–5 (results uninterpretable)
- With explicit acknowledgment of the imbalance: 5–6
- With results at matched compute (iso-FLOPs analysis): 6–7

Parameter/compute-matched comparisons are non-negotiable for architecture papers in 2024–2026. Any paper that avoids this is suspect.

---

## Appendix D: Understanding the 70.2% Acceptance Rate

With an acceptance rate of 70.2%, ICLR's image generation track is accepting a substantial fraction of submissions. This means:

1. **The bar is not extremely high**: Papers can be accepted with meaningful limitations — missing 1–2 baselines, minor ablation gaps, or marginal empirical improvements over SOTA.

2. **Rejection signals are clear**: Rejected papers typically have multiple fundamental issues, not just one small gap. A paper rejected with average rating 3.5 (Decoupled Diffusion) had: (a) mathematically equivalent method to prior work, (b) missing major baselines, (c) weak qualitative results.

3. **The rating distribution matters**: A paper with reviews [8, 8, 8, 6] (SDXL-tier) looks very different from [6, 5, 5, 5] (CompoDiff-tier) even if both are above threshold.

4. **Oral/Spotlight papers need consensus**: SANA had [10, 8, 8, 8] — all reviewers agreed it was good, with the highest reviewer giving 10. Getting an Oral/Spotlight requires that no reviewer gives a low score (3–4) and at least one gives a very high score.

**Calibration for the judge**: Given the 70.2% acceptance rate and mean rating 4.81, a score of:
- 6+ should typically be "likely accept" territory
- 4.5–5.5 is genuinely borderline
- <4.0 should represent papers with clear, multiple problems
- 7+ should represent work that contributes meaningfully to the field beyond threshold

---

## Appendix E: Evolution of the Field (2024–2026 Context)

Understanding the trajectory of the field helps contextualize whether a paper is genuinely novel or just catching up.

### E.1 Architecture Trajectory
- **2021–2022**: U-Net LDMs dominate (Stable Diffusion, DALL-E 2)
- **2022–2023**: DiT architectures introduced; ControlNet for spatial conditioning
- **2023–2024**: SDXL scales U-Net; PixArt uses DiT; rectified flows gain popularity
- **2024–2025**: SANA linearizes DiT; FLUX replaces U-Net with transformer; decoder-only LLMs as text encoders
- **2025–2026**: High-compression latent spaces; multi-billion parameter DiTs; diffusion-language model unification

**Implication**: By 2025–2026, "we use a DiT instead of U-Net" is not a novel contribution. "We use a linear DiT with 32× compression autoencoder and LLM text encoder" is a novel *system* contribution.

### E.2 Personalization Trajectory
- **2022**: DreamBooth and Textual Inversion establish the field
- **2023**: LoRA becomes the dominant fine-tuning method; Custom Diffusion enables multi-concept
- **2023–2024**: Encoder-based methods (ELITE, IP-Adapter) enable faster adaptation
- **2024–2025**: Rank-reduction methods (PaRa, SVDiff variants); identity-preserving methods (InstantID)
- **2025–2026**: Few-shot and zero-shot personalization; privacy-preserving personalization

**Implication**: By 2025, a personalization paper that only compares to DreamBooth and LoRA without including encoder-based methods is missing 2 years of progress.

### E.3 Efficiency Trajectory
- **2020–2022**: DDPM baselines (1000 steps); DDIM brings this to 50
- **2023**: Consistency Models (1–4 steps); DPM-Solver++ (10–20 steps)
- **2024**: LCM (4 steps, distilled from LDM); SDXL Turbo (1–4 step adversarial distillation)
- **2025**: Flow matching at <10 NFEs as standard; sub-1-second generation on consumer GPU

**Implication**: By 2025, "we reduce sampling from 50 steps to 20 steps" is not novel — DPM-Solver already achieves this. Papers must compare against these fast samplers.

### E.4 Evaluation Metric Trajectory
- **2020–2022**: FID + IS as primary metrics
- **2022–2023**: CLIP-T added for text alignment; human evaluation for preference
- **2023–2024**: HPSv2, ImageReward trained on human preference data
- **2024–2025**: GenEval, TIFA, DrawBench for compositional evaluation; AugCLIP for editing
- **2025–2026**: Multimodal LLM-as-judge evaluation emerging

**Implication**: A 2025 paper using only FID + IS looks outdated. At minimum, CLIP-T or HPSv2 is expected for T2I papers.

---

## Appendix F: Subfield-Specific Scoring Adjustments

### F.1 Adjustments for Unconditional Image Generation Papers
These papers (generating images without text conditioning) are increasingly rare at ICLR because the community has moved to conditional generation. For such papers:
- Apply a -0.5 to -1.0 adjustment to the score since the problem is considered more solved
- Demand stronger novelty on the architectural or theoretical side to compensate
- Standard benchmarks: CelebA-HQ, FFHQ, LSUN, ImageNet 256×256 / 512×512

### F.2 Adjustments for Super-Resolution and Inpainting Papers
These conditional generation tasks have a different baseline landscape:
- **Super-resolution**: Compare against Real-ESRGAN, StableSR, ResShift, DiffBIR
- **Inpainting**: Compare against LaMa, Stable Diffusion inpainting, PowerPaint, BrushNet
- Evaluation uses PSNR, SSIM, LPIPS in addition to FID
- Papers claiming "diffusion-based super-resolution" must compare to all dedicated SR diffusion models, not just general T2I models applied to SR

### F.3 Adjustments for Compositional Generation Papers
Papers specifically targeting multi-object, multi-attribute compositional generation:
- Standard benchmarks: DrawBench, PartiPrompts, T2I-CompBench, GenEval
- Key capability claims: counting, spatial relationships, attribute binding, negation
- Must compare against SDXL, DALL-E 3, PixArt-Σ as strong baselines
- Common weakness: evaluating on toy compositional tasks while claiming general improvement

### F.4 Adjustments for Theoretical/Analysis Papers
Papers analyzing diffusion model properties (score function analysis, convergence bounds, optimal transport):
- Theoretical papers can score highly (7–8) with weak empirical results if the theory is strong
- The theory must be non-trivial and provide actionable insights or explain existing phenomena
- Common weakness: proving properties that are already known empirically without providing new insight
- Demand that claimed "theoretical insights" translate to concrete empirical recommendations

---

## Appendix G: Interview Checklist for Complex Papers

When a paper is technically dense, use this structured set of questions to extract the key information needed for scoring.

### G.1 Core Contribution Questions
1. What is the single most important technical innovation in this paper?
2. Does this innovation exist in any published or contemporaneous work?
3. What is the motivation for this innovation — does it address a real limitation?
4. What would happen if this component were removed (ablation)?

### G.2 Experimental Design Questions
5. What benchmarks are used? Are they standard for this task?
6. What baselines are compared against? What is the most recent baseline?
7. Are baselines run at matched capacity (parameters, compute, data)?
8. Is there a human evaluation? How many raters, how was it designed?
9. Are there failure cases or known limitations documented?

### G.3 Claims Verification Questions
10. The abstract claims X — is X directly demonstrated in the experiments?
11. Are the efficiency claims (speed, memory) measured fairly (wall-clock vs. FLOPs)?
12. Are resolution claims supported at that resolution (not just at 512×512)?
13. Are the numbers in the comparison table drawn from the same evaluation setting?

### G.4 Significance Questions
14. Is this the first paper to address this specific problem?
15. If not, how does it differ from the most recent prior work?
16. Would a practitioner use this method? At what cost?
17. Does the method generalize beyond the tested scenarios?

### G.5 Reproducibility Questions
18. Is code/checkpoints released or promised?
19. Are training details sufficient to reproduce?
20. Are evaluation protocols (sample counts, seeds, resolution) specified?

---

## Appendix H: Rating Anchors with Full Justification

The following rating anchors are calibrated specifically to the image generation domain based on the review data analyzed.

### Score: 10 — Transformative Contribution
Reserved for papers that fundamentally change what is possible. In image generation, this means:
- Opening a completely new problem domain (e.g., first text-to-image model)
- Achieving an order-of-magnitude improvement in quality AND efficiency simultaneously
- Providing a unifying theoretical framework that explains and predicts existing results
- Essentially no prior work addresses the same problem

*Practical note: Score 10 is awarded rarely. SANA's highest reviewer gave 10 but the average was 8.5. Do not give 10 to papers that are merely excellent; reserve it for paradigm shifts.*

### Score: 9 — Exceptional, Clear Oral
- Strong multiple novel contributions
- Best FID/human preference on multiple benchmarks by clear margin
- Comprehensive ablations
- Open-source with community impact
- No fundamental weaknesses
- Reviewers would all agree this is a strong accept

### Score: 8 — Strong Accept (Oral/Spotlight Candidate)
- One to three genuine innovations with synergistic effects
- State-of-the-art results validated across multiple benchmarks
- Comprehensive ablations for each component
- Well-written, reproducible
- Minor gaps: may be missing one recent baseline or one ablation experiment
- This is the SDXL / Würstchen tier

### Score: 7 — Clear Accept (Poster)
- One clear novel contribution
- Results competitive with or better than SOTA on 2+ benchmarks
- Ablations for main components
- Adequate baselines (may miss 1–2 very recent methods)
- May have minor presentation issues
- This is the DisenBooth / PaRa tier

### Score: 6 — Weak Accept (Marginal Poster)
- Interesting idea with meaningful experiments
- Results are mixed (better on some metrics, worse on others)
- Key baselines present but may miss some recent work
- Some ablations but not comprehensive
- Minor theoretical or empirical concerns
- Reviewers disagree: some find it acceptable, others find it borderline
- This is the SEED Tokenizer / Inner CFG tier

### Score: 5 — Borderline (Lean Reject)
- Idea has merit but execution is clearly incomplete
- Missing one or more important baselines or ablations
- Claims partially supported but central contribution unclear
- Would benefit significantly from additional experiments
- Rebuttal might change the outcome
- This is the CompoDiff (5.25) tier

### Score: 4 — Marginal Reject
- Idea is incremental or poorly motivated
- Multiple missing comparisons
- Results do not clearly support the claimed advantages
- Evaluation design has flaws (wrong metrics, unfair conditions)
- This is the DOG paper (4.25) tier

### Score: 3 — Clear Reject
- Missing major, obviously relevant baselines
- Claims partially contradicted by reviewer analysis
- Significant theoretical or methodological flaws
- Overclaiming that damages credibility
- Images/results visually inferior to baselines
- This is the Decoupled Diffusion (3.5) / AugCLIP (4.25) territory

### Score: 1–2 — Strong Reject
- Fundamental misunderstanding of prior work
- Mathematical errors that invalidate the theoretical contribution
- Results fabricated or non-reproducible
- Work that is a minor variation of a single published paper without acknowledgment
- Complete failure to meet baseline performance

---

## Appendix I: The Soundness-Contribution-Presentation Triangle

ICLR reviewers score three dimensions explicitly (besides the overall rating):
- **Soundness** (avg 2.6 for this topic): Technical correctness and experimental rigor
- **Contribution** (avg 2.37): Novelty and significance
- **Presentation** (avg 2.65): Clarity, organization, writing quality

These averages (on a 1–4 scale) suggest that in image generation:
- **Contribution is the hardest dimension to satisfy** (lowest average of 2.37 out of 4)
- **Soundness and Presentation are more achievable** (2.6 and 2.65)

**What this means for evaluation:**

A paper with high Soundness but low Contribution (correct results, incremental idea) will score around 5–6 and may still be accepted at the 70% acceptance rate. This is the most common pattern in the review data.

A paper with low Soundness (theoretical errors) will be rejected regardless of Contribution, because fundamental correctness is non-negotiable.

A paper with low Presentation but high Soundness and Contribution (poorly written but genuinely novel with strong results) can still be accepted, as presentation issues can often be fixed.

**Implication for scoring**: Weight Contribution most heavily when determining the final score. A paper with Soundness 4, Contribution 2, Presentation 4 should score around 5–6 (technically solid, well-written, but incremental). A paper with Soundness 3, Contribution 4, Presentation 3 should score around 7–8 (genuinely novel, adequate execution).

---

## Appendix J: Frequently Misunderstood Aspects of Image Generation Evaluation

### J.1 "FID is all you need" — False

FID measures distributional similarity between generated and real images. It can be high (good) for images that:
- Are visually realistic but unrelated to the text prompt
- Show the most common objects in the training set
- Are high-quality but lack diversity

A model that always generates a golden retriever on grass would have excellent FID on a dataset dominated by dogs but terrible text-image alignment. Papers claiming improvements based solely on FID must be questioned.

### J.2 "CLIP Score reflects generation quality" — False

CLIP Score measures how well a generated image matches its corresponding text prompt. It does not measure:
- Whether the image is aesthetically pleasing
- Whether the image is photorealistic
- Whether the image is diverse (mode collapse not penalized)
- Whether the image has realistic physics/geometry

### J.3 "More parameters = better model" — False in 2024–2026

SANA demonstrates that a 1.6B parameter model with efficient architecture can outperform a 12B model in quality-per-FLOP. The field has moved beyond simple parameter scaling. Papers claiming "we use a larger model" without architectural innovations are not contributing meaningfully.

### J.4 "Our method is faster" — Requires context

"Faster" can mean:
- Fewer inference steps (NFEs) at matched quality
- Lower wall-clock time per image at matched quality
- Lower GPU memory per image at matched quality
- Lower training cost at matched final performance

A paper claiming speedup must specify *which* of these it achieves and compare against the strongest fast sampler baselines, not DDPM.

### J.5 "Human evaluation validates quality" — Only if done correctly

Human evaluation is the most trusted metric but is frequently poorly designed:
- Sample size must be sufficient (N >= 100 per comparison for 95% confidence)
- Raters must be blind to which method produced each image
- Task must be well-defined (preference vs. quality vs. alignment are different)
- Platform and rater demographics must be specified
- Inter-rater agreement must be reported

A user study with N=20 comparisons per method is not statistically meaningful and should be treated as qualitative evidence only.

### J.6 "We outperform SDXL" — Depends on model size and data

SDXL is a strong baseline but it was trained on a specific dataset at a specific scale. Outperforming SDXL with:
- 5× more training data → not clearly a methodological advance
- Same data + different architecture → genuine contribution
- Significantly larger model → not clearly a methodological advance
- Same model size, same data, better training recipe → genuine contribution

Always ask: "What advantage does the proposed method have, and is this advantage due to the method or due to the resources?"

---

## Appendix K: Worked Example — How to Score a Hypothetical Paper

**Paper**: "FlowDiT: Rectified Flow with Diffusion Transformer for Efficient High-Resolution Text-to-Image Generation"

**Abstract claims**: Combines rectified flow training with a transformer backbone and sparse attention pattern to achieve 50× faster inference than SDXL at equivalent quality. Demonstrates generation at 2048×2048 resolution with state-of-the-art FID on MS-COCO and DrawBench.

**Reading the paper:**
- Architecture: DiT with sparse attention (using fixed windowed attention pattern, not learned sparsity)
- Training: Rectified flow objective (FM framework), standard linear noise schedule
- Autoencoder: Uses existing SD 1.5 VAE (8× compression, not modified)
- Text encoder: T5-XXL (not modified)
- Main results table: FID 7.2 on MS-COCO 30K vs. SDXL FID 9.1
- Baselines: DDPM, DDIM, SD v1.5, SD v2.1, SDXL (missing: PixArt-Σ, FLUX, Würstchen, Consistency Models)
- Speed: 50× faster than SDXL at 20 NFEs, but SDXL was measured at 50 NFEs (unfair comparison)
- Ablations: Ablates sparse attention vs. full attention, but not rectified flow vs. DDPM
- Human evaluation: 3AFC with 30 raters, N=50 image pairs per comparison
- Code: "Will be released upon acceptance"

**Analysis:**

Novelty: Combining rectified flow with DiT is incremental — both are well-established. Sparse windowed attention is borrowed from BERT/ViT literature without significant modification for diffusion. However, no single paper has combined these specific components at this scale.

Soundness: Experimental comparison with SDXL at different NFEs is unfair. Should compare at 20 NFEs for both. FID improvement may be partially due to this unfair comparison.

Missing critical baselines: PixArt-Σ (also uses DiT + T5 for T2I), FLUX.1 (uses transformer + flow matching), Würstchen (efficiency-focused LDM), LCM (consistency distillation for speed). These are all directly comparable methods published within the previous 12 months.

Ablation gap: Rectified flow is a key innovation claimed but not ablated (no comparison to DDPM training with same architecture).

Human evaluation issues: N=50 image pairs with 30 raters is marginal; no inter-rater agreement reported.

Efficiency claim issue: The 50× speedup claim uses unfair NFE comparison. Properly normalized, the speedup may be much smaller.

**Suggested Score: 5**
- Novel enough to not be rejected outright (interesting combination)
- Several missing baselines reduce confidence in the results
- Key ablation (rectified flow contribution) missing
- Unfair speed comparison
- Marginal human evaluation
- With proper baselines and ablations, could potentially score 6–7

**What would move this to 6–7:**
- Add PixArt-Σ, FLUX, and LCM to the baseline table
- Fix the speed comparison to use equal NFEs for SDXL
- Ablate rectified flow vs. DDPM training
- Increase human study to N=100+ per comparison
- Report CLIP-T and HPSv2 in addition to FID

**What would move this to 3–4:**
- If the FID improvement disappears after fair NFE comparison
- If PixArt-Σ already achieves similar FID at similar speed
- If the sparse attention pattern degrades quality at 2K resolution

