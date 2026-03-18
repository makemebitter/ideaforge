# AI Judge Skill File: Video Generation

## Overview

This skill file provides calibration guidance for evaluating research papers in **video generation** and closely related subfields. It synthesizes patterns from 414 papers submitted to ICLR and NeurIPS (2023–2026), with a 19.3% acceptance rate. Ratings follow a 2–8 scale (mean 4.88, median 5.0, std 1.1). The field is competitive, technically demanding, and evolving rapidly; the bar for acceptance requires genuine novelty, rigorous empirical comparison, and clear practical impact.

---

## 1. Field Overview

Video generation encompasses all methods that synthesize temporal visual sequences, either from scratch or conditioned on various inputs. It is one of the most active areas in deep learning, driven by diffusion models, autoregressive transformers, and state-space models.

### Core Subdomains

**Text-to-Video (T2V) Generation**
Synthesizing video from a natural language description. Models include cascaded pixel/latent diffusion (Make-A-Video, Imagen Video, VideoLDM, LaVie), LDM-based systems (ModelScope, VideoCrafter), DiT-based architectures, and autoregressive systems. Key challenges: temporal consistency, motion quality, text alignment, scalability to high resolution and long duration.

**Image-to-Video / Video Prediction**
Animating a single image or predicting future frames. Models: Stable Video Diffusion (SVD), SEINE, image-conditioned diffusion. Challenges: identity preservation, natural motion, multi-modal diversity, avoiding degenerate static outputs.

**Video Editing / Video-to-Video**
Modifying an existing video via text or reference instructions while preserving unedited content. Methods: TokenFlow, ControlVideo, COVE, NaRCan, FateZero, InstructPix2Pix-adapted. Challenges: temporal consistency of edits, identity preservation, structural faithfulness, avoiding flickering.

**Video Frame Interpolation (VFI)**
Synthesizing intermediate frames between two input frames. Benchmarks: Vimeo-90K, SNU-FILM, X-TEST (2K/4K). State-of-the-art: EMA-VFI, AMT, BiFormer, RIFE, VFIMamba. Challenges: large motion, velocity ambiguity, directional ambiguity, high-resolution scalability.

**Video Super-Resolution (VSR)**
Upscaling low-resolution video to high resolution while preserving temporal consistency. Benchmarks: REDS, Vid4, Vimeo-90K. Methods: sliding-window approaches, recurrent networks, diffusion-based. Challenges: temporal flickering, real-world degradations.

**Controllable Video Generation**
Camera-controlled, motion-controlled, or trajectory-guided video generation. MotionDirector, CameraCtrl, AnimateDiff+ControlNet. Challenges: precise control signal injection without degrading visual quality, disentanglement of motion and appearance.

**Long Video Generation**
Generating coherent videos beyond what a single model pass can produce. Free-Bloom, FreeNoise, FreeLong, StoryDiffusion, VideoChat-Flash. Challenges: maintaining global consistency, avoiding content drift, memory and compute efficiency.

**4D / 3D Generation from Video**
Generating or reconstructing dynamic 3D scenes from text or video. 4Real, Diffusion4D, AYG, 4Dfy, Dream-in-4D. Combines video diffusion with 3D Gaussian splatting, NeRF, or SDS optimization. Challenges: spatial-temporal consistency, view consistency, generation quality at 3D+time.

**Video Diffusion Models (Architecture and Efficiency)**
Papers targeting inference speed, memory reduction, or architectural improvements for video diffusion. StreamlinedInference, DeepCache, FlowCaching, VBench. Challenges: maintaining generation quality while reducing FLOPs/memory, generalization across model families (U-Net vs DiT).

**Video Generation for Downstream Tasks**
Using video generation models as world models, planners, or data engines. UniPi (robotics via video planning), VidMan (robot manipulation), VPR (video prediction as rewards), SafeMVDrive (autonomous driving data synthesis). Challenges: validating utility on downstream tasks, fair comparison to task-specific baselines.

**Video Understanding / Recognition via Diffusion**
Using video generation model features or joint training for recognition. GenRec (unifying generation and recognition), VideoMAE variants. Challenges: fair comparison to discriminative-only baselines, model size parity.

---

## 2. Scoring Calibration

The rating scale runs from 2 to 8. Based on the data, ratings cluster near 5 (the borderline), with only 4 papers rated 8+ ("excellent") in this corpus. The key thresholds are:

### Rating 8: Excellent — Clear Accept
A paper at this level makes a **significant, well-validated contribution** that is likely to have lasting impact. At least one reviewer must give an 8, and no major methodological flaws should exist.

Characteristics:
- Novel idea that opens a new direction or substantially advances a hard, well-defined problem
- Exhaustive ablation studies clearly attributing gains to proposed components
- Comparison against the strongest known baselines on standard benchmarks
- Strong quantitative and qualitative results, ideally including human evaluation
- Clear writing, reproducibility, released code

Examples from the corpus: VFIMamba received multiple 7s and the paper's strengths include "exhaustive ablation studies" and "state-of-the-art PSNR values especially for high-resolution frames." The reviewer who gave an 8 on the VFI distance-indexing paper cited "soundness: excellent, presentation: excellent, contribution: excellent."

### Rating 7: Good — Recommend Accept
A solid, technically sound paper with clear contributions and good evaluation. Minor weaknesses exist but are not fatal.

Characteristics:
- Clear novelty relative to prior work, even if not revolutionary
- Ablation studies present; may have minor gaps (e.g., missing one comparison)
- Results demonstrate meaningful improvement on standard benchmarks
- Well-written and reproducible
- No fundamental methodological flaws

Examples from the corpus:
- UniPi (Learning Universal Policies via Text-Guided Video Generation) received two 7s and two 6s: "well written, clear and easy to understand," "extensive experiments demonstrate effectiveness," though reviewers noted limited novelty in diffusion adaptation and missing comparisons to hierarchical RL.
- Free-Bloom received one 7: "novel and interesting, outperforms SOTA zero-shot text-video methods," well-written.
- StoryDiffusion received 7, 7, 6, 8 across reviews: praised for "simple conceptual approach that doesn't require training" and "compelling results attacking a timely problem."

### Rating 6: Borderline Accept / Weak Accept
The paper has merit and should probably be accepted, but reviewers have notable concerns that were not fully resolved.

Characteristics:
- Genuine contribution but may be incremental relative to close prior work
- Evaluation gaps: missing one or two key baselines, limited benchmarks, or weak ablations
- Results are positive but not clearly state-of-the-art
- Writing is acceptable but may have clarity issues
- Typically requires author rebuttal to tip to accept

Examples from the corpus:
- 4Real (4D scene generation via video diffusion) averaged 6.2 with one reviewer giving 8 ("very well-motivated, clear improvements") and others giving 5–6 due to limited baselines (missing AYG comparison), unclear interaction claims, and manual steps not accounted for in timings.
- VFIMamba received 6, 7, 7, 7: borderline concerns included unfair dataset comparisons (different training data across methods), missing FLOPs analysis, and discrepancies in reported numbers.
- Free-Bloom received two 5s alongside two 7s, with borderline concerns about insufficient quantitative ablations and weak coherence.

### Rating 5: Borderline Reject / Weak Reject
The paper is marginally below acceptance. Genuine contributions exist but are outweighed by execution problems.

Characteristics:
- Novelty is limited, incremental, or unclear relative to prior work
- Missing important baselines or using obsolete baselines
- Evaluation on non-standard or limited benchmarks
- Ablations insufficient to support claimed contributions
- Methodological concerns not fully addressed

Examples from the corpus:
- VideoFactory (swapped attention for T2V) averaged 5.25 and was rejected: reviewers cited "not reporting methods with better FVDs" (cherry-picked baselines), confused ablation experimental settings, and limited technical novelty relative to video classification attention work.
- Marrying Pixel and Latent Diffusion averaged 5.0 and was rejected: pipeline "not something new" (same as Make-A-Video, Imagen Video), motivation for hybrid approach unconvincing, missing time-cost comparison.
- VidMan averaged 6.4 but had one 5 and one 6 alongside a 9: key concern was using obsolete baselines (PerAct instead of RVT/Act3D/3DDA) and not comparing directly to the most similar prior work (GR-1).

### Rating 4: Reject
The paper has fundamental flaws. Contribution is marginal, evaluation is broken, or methodology contains errors.

Characteristics:
- Technical formulation is flawed (wrong at inference vs. training)
- Evaluation metrics or benchmarks mismatched to the claims
- Missing nearly all relevant prior work comparisons
- Novelty does not exceed a straightforward combination of existing ideas
- Writing quality insufficient to convey contributions clearly

Examples from the corpus:
- VideoChat-Flash received a 4 from one reviewer alongside an 8 from another: the lower rating was driven by "constituent parts are largely clever integrations of existing ideas" (novelty concern) and an ablation that seemed to contradict the "almost no performance loss" claim.
- SafeMVDrive received a 4 from one reviewer: "lacks experiments on how generated data can improve E2E AD model's performance," motivation for VLM not convincing, and key claims about VLM superiority not validated.

### Rating 2–3: Strong Reject
Reserved for papers with severe methodological errors, plagiarism concerns, or essentially no valid contribution. Rare in the corpus (232 papers in tiers 1–3, but most around 4–5 rather than 2–3).

---

## 3. What Reviewers Reward

Based on actual reviewer comments across all reviewed papers, the following consistently earn positive comments and higher ratings:

### 3.1 Genuine Novelty That Opens New Directions

Reviewers respond strongly to ideas that reframe a problem or introduce a non-obvious technical insight. Examples:
- VFIMamba: "first to adapt S6 model to VFI" — explicitly praised for bringing an emerging architecture (Mamba) into a new domain
- UniPi / VidMan: novel framing of robot manipulation as video prediction, praised for "broader impact in future applications"
- 4Real: "lifts the requirement of training a 3D generative model using limited synthetic data" — praised for identifying and solving a clear bottleneck

What is not rewarded: combinations of existing ideas without new insight, even if the system is complex. As one reviewer of VideoFactory noted, the attention mechanism "does not appear to significantly impact the task of video generation itself."

### 3.2 Exhaustive Ablation Studies

Ablations are the single most commonly praised feature in accepted papers. Reviewers expect:
- Each proposed component isolated and tested individually
- Not just qualitative ablations — quantitative comparisons on standard metrics
- Ablation on training data/curriculum if a new training scheme is proposed
- Showing where each gain comes from (not just final numbers)

Reviewer quote from VFIMamba: "Exhaustive ablation studies proving the effectiveness for each of their introduced modules."

Reviewer quote from VideoChat-Flash: "The ablation study clearly illustrates the contribution of each component."

Reviewer quote from Diffusion4D: "Ablation studies were done to justify its design choices."

### 3.3 Comparison Against Strong, Up-to-Date Baselines

Reviewers penalize papers that:
- Use only weak or outdated baselines
- Report FVD/FID only for methods with worse numbers (selectively omitting stronger methods)
- Fail to compare against the most relevant concurrent work

Reviewer quote from VidMan: "The baselines selected for the RLBench task seem somewhat arbitrary — RVT significantly improves upon PerAct, and RVTv2 improves upon that further."

Reviewer quote from GenRec: "Table 1 doesn't represent the current SOTA. E.g. InternVideo from 2022 claims 77.2% on SSv2."

Reviewer quote from VideoFactory: "When comparing FVDs on UCF-101, the paper included many previous works — but only if their FVD score is higher." (Cherry-picked table.)

### 3.4 Comprehensive Evaluation on Standard Benchmarks

Papers covering multiple standard benchmarks earn trust. Expected benchmarks vary by subfield (see Section 6), but reviewers notice when standard benchmarks are skipped without justification.

Reviewer quote from VFI distance-indexing paper: "Why did the authors only perform experimental comparisons on the Vimeo-90K dataset? There are several VFI benchmarks that are commonly used."

### 3.5 Scalability and Efficiency Analysis

For architecture papers, reviewers expect FLOPs, memory usage, inference speed, and how these scale with resolution or video length.

Reviewer quote from VFIMamba: "A plot/table showing the FLOPs compared to the input resolution would be interesting to get a better feeling for the scaling."

Reviewer quote from StreamlinedInference: "The FLOP and memory reduction is a genuine contribution, but MAC and GFlops should be included."

### 3.6 Well-Written Papers with Clear Motivation

Papers that are "easy to follow," have clear motivation, and provide strong figures earn consistent praise. Multiple reviewed papers cite "well-written" as a strength. Conversely, papers with dense unexplained notation, unclear algorithmic descriptions, or figures that don't match the text receive explicit criticism.

### 3.7 Training Details and Reproducibility

Reviewers notice when papers:
- Provide hyperparameters and training details (not just in appendix)
- Report model sizes, training compute, and inference costs
- Commit to code/model release

Reviewer quote from VideoFactory (positive): "I appreciate that training costs have been reported, and also throughput/memory requirements."

Reviewer quote from StreamlinedInference (negative): "The evaluation using FVD and CLIP score is insufficient... Include more video diffusion backbones such ModelScope and VideoCrafter to extensively verify the effectiveness."

### 3.8 Honest Failure Case Analysis

Papers that include failure cases and discuss limitations honestly are rewarded. Reviewers specifically ask for this when absent: "It would be very helpful to the community to also show failure examples so that the remaining challenges are clear" (4Real reviewer).

---

## 4. What Reviewers Penalize

### 4.1 Limited Novelty / Incremental Contributions

The most common weakness phrase across all 414 papers. Reviewers penalize:
- Papers that combine two existing systems without new insight
- Systems that follow an established pipeline with a small tweak
- Methods that are "engineering" without new algorithmic understanding

Reviewer quote from GenRec: "Considering that previous works have already demonstrated that diffusion models have the capability of extracting sufficient features for understanding tasks, the combination of generation and recognition tasks to boost both tasks is too straightforward, limiting the novelty."

Reviewer quote from Marrying Pixel and Latent: "Very similar to existing works like Make-A-Video in the algorithmic design, where the main difference lies in the choice of latent- or pixel-based diffusion models."

Reviewer quote from VidMan (low scorer): "The whole framework is very similar to small-scale diffusion planners like decision-diffuser."

### 4.2 Missing or Weak Ablations

Reviewers explicitly flag:
- Only qualitative ablations (no quantitative)
- Ablations on only 2 examples
- Ablation setup not matching main experiments (different training data, different number of steps)

Reviewer quote from Free-Bloom: "Insufficient ablation study. Only two qualitative cases, not convincing enough. More cases and quantitative results should be provided."

Reviewer quote from StoryDiffusion: "The paper repeatedly emphasizes that the proposed modules are plug-and-play. However, the main text does not provide corresponding ablation studies to offer more substantial examples."

### 4.3 Cherry-Picked or Selective Baselines

A paper that only reports baselines it beats is a red flag. Reviewers check tables against known leaderboard positions.

Reviewer quote from VideoFactory: "The paper included many previous works — but only if their FVD score is higher. It omitted Make-A-Video, VDIM, LVDM, etc."

### 4.4 Outdated Baselines (Failure to Engage with Recent Literature)

Comparing against methods from 2 years prior without justification is penalized heavily, especially in fast-moving areas like robotics + video and T2V generation.

Reviewer quote on VidMan: "The authors probably had to retrain the baselines... [PerAct] is an old baseline published two years ago. Since then, [Act3D, RVT] achieved big leaps and the current SOTA on RLBench is [3DDA]."

### 4.5 Flawed Technical Formulation

Logical errors in the method — particularly contradictions between training-time and inference-time behavior — are serious. The VFI paper (QuFHei1vuE) received a harsh initial review precisely because the reviewer found the training/inference logic contradictory: "they use the GT target frame to compute the distance map during training and use a uniform map during inference. What is the point of attempting to address speed ambiguity during training, if the authors are assuming uniform speed at inference?"

### 4.6 Unsubstantiated Claims

Claims like "our method captures object-environment interactions" or "our model is lightweight" must be supported empirically. Reviewers cite unsubstantiated claims as a clear weakness.

Reviewer quote from 4Real: "This work captures the interaction between objects and environments. From all the submitted video results, they do not seem to include any interaction between the object and the environment."

### 4.7 Insufficient Evaluation Metrics

FVD and CLIPSIM alone are often not enough. Reviewers expect:
- Multiple metrics appropriate to the subfield
- Human evaluation for perceptual quality claims
- Comprehensive benchmarks (multiple datasets, not just WebVid-10M)

Reviewer quote from StreamlinedInference: "The evaluation using FVD and CLIP score is insufficient. It would be beneficial to include more comprehensive video quality evaluation metrics, such as those proposed in VBench."

Reviewer quote from GenRec: "FVD is not a very good metric. A generative paper ought to have generative results in the main paper itself, FVD results alone are not adequate."

### 4.8 Missing Efficiency Analysis

For papers claiming computational efficiency, reviewers expect wall-clock time, not just FLOPs. For systems claiming "1/50 compression," they want to see end-to-end GPU memory and latency, not just theoretical operations.

Reviewer quote from VideoChat-Flash: "The claimed efficiency benefits (1/50 token reduction) are shown in FLOP counts but not in end-to-end wall-clock latency or GPU memory consumption."

### 4.9 Missing Direct Comparison to the Most Similar Work

Reviewers identify the closest prior work and ask for direct comparison. If not provided, this is a major issue.

Reviewer quote from VidMan: "The main competitor of this submission is [GR-1]... a fair and direct comparison against [GR-1] is required so that we know which design choices are indeed the best."

### 4.10 Reproducibility Gaps

No code release planned, missing hyperparameters, unclear dataset processing, or unreported training details undermine reproducibility and lower scores.

---

## 5. Domain-Specific Evaluation Criteria

### 5.1 Text-to-Video Generation

**Key challenges to evaluate:**
- Temporal consistency (does the subject remain the same across frames?)
- Motion quality (is motion natural, not degenerate/static?)
- Text-video alignment (does the video match the prompt?)
- Visual quality (resolution, artifacts, FVD)

**What to look for:**
- Does the paper address a genuinely harder version of T2V (e.g., longer videos, higher resolution, compositional prompts)?
- Are the baselines the most recent published T2V models?
- Is human evaluation included alongside automated metrics?
- Does the evaluation cover diverse prompt types (motion, objects, scenes)?

**Red flags specific to T2V:**
- Only evaluated on WebVid-10M subset without UCF-101 or MSR-VTT
- Using static-frame CLIP scores without temporal consistency metrics
- Dataset captions generated from a single keyframe (missing temporal information)
- Selective FVD reporting

**Example calibration:** VideoFactory (rating 5.25, Reject) was penalized for selective baseline reporting in FVD tables, while having a genuinely valuable dataset contribution. The dataset alone was not enough to overcome the methodological weaknesses.

### 5.2 Image-to-Video / Video Prediction

**Key challenges:**
- Identity and appearance preservation from the conditioning image
- Naturalness of motion and temporal coherence
- Diversity of generated motions (avoiding mode collapse)
- Handling image-conditioned diffusion without "conditional leakage" artifacts

**What to look for:**
- Comparison against SVD, SEINE, and other image-conditioned baselines
- Evaluation on multiple seed images/domains
- For video prediction specifically: FVD on standard datasets (UCF-101, Kinetics)
- For robot/manipulation settings: task success rate, not just perceptual metrics

**Paper example:** Identifying and Solving Conditional Image Leakage in I2V Diffusion (rating 6.0, Accept) — addresses a specific, well-defined failure mode of I2V models. Concrete, addressable problem with clear evaluation.

### 5.3 Video Editing / Video-to-Video

**Key challenges:**
- Edit fidelity (does the video reflect the instruction?)
- Background preservation (are unchanged regions stable?)
- Temporal consistency of edits (no flickering, no drift)
- Trade-off between edit strength and content preservation

**What to look for:**
- Comparison against DDIM-based, TokenFlow, ControlNet-based baselines
- SSIM/PSNR for background preservation alongside edit quality metrics
- Temporal consistency metrics (warping error, optical flow consistency)
- User studies or perceptual quality assessments

**Note:** Purely qualitative demonstrations are insufficient. Quantitative benchmarks on standard video editing datasets (DAVIS, TGVE) are expected.

### 5.4 Video Frame Interpolation (VFI)

**Expected benchmarks:** Vimeo-90K, SNU-FILM (multiple difficulty levels: Easy, Medium, Hard, Extreme), X-TEST (2K and 4K).

**Expected baselines:** RIFE, IFRNet, EMA-VFI, AMT, BiFormer, SGM-VFI. Papers failing to include these should be downgraded.

**Expected metrics:** PSNR (primary), SSIM, LPIPS. Higher resolution papers should report FLOPs and inference time scaling.

**Critical evaluation points:**
1. **Fair training data comparison**: Was the proposed method trained on the same data as baselines? (Vimeo-90K only vs Vimeo-90K + X-TRAIN)
2. **Multi-scale evaluation**: Does the paper evaluate at multiple difficulty levels (large motion is harder)?
3. **Plug-and-play claims**: If the method is plug-and-play, are results shown on multiple base models?

**Paper examples:**
- VFIMamba (6.75, Accept): strong because it is first SSM-based VFI, has exhaustive ablations, achieves SOTA PSNR at high resolution. Concern: some unfair training data comparisons.
- VFI distance-indexing paper (7.0, Reject due to consensus failure): technically interesting but had initial concerns about training/inference logic contradiction. Post-rebuttal, reviewers increased scores, but the paper was still rejected — showing that even well-received papers can be rejected at ICLR with mixed-reviewer panels.

### 5.5 Video Super-Resolution (VSR)

**Expected benchmarks:** REDS4, Vid4, Vimeo-90K-T, UDIS^D for stabilization tasks. Real-world degradation benchmarks (VideoLQ, RealVSR).

**Expected baselines:** BasicVSR++, RVRT, VRT (for non-real-world); RealBasicVSR (for real-world).

**Expected metrics:** PSNR/SSIM on synthetic; NIQE/BRISQUE or LPIPS for real-world. Temporal flickering metrics.

**Critical evaluation point:** Does the paper consider both synthetic (known degradations) and real-world (blind) settings? A method that only works on synthetic benchmarks has limited practical value.

### 5.6 Controllable Video Generation (Camera / Motion Control)

**Types of control:**
- Camera trajectory control (MotionDirector, CameraCtrl, CamI2V)
- Object motion trajectories (MotionBooth, DragNUWA)
- Appearance / identity control (IP-Adapter style)

**Key evaluation questions:**
- Is the control signal actually followed? (Not just visual quality)
- Is control disentangled from appearance? (Changing camera shouldn't change scene content)
- Are training-free methods compared against fine-tuned ones?

**Common weakness:** Papers that show the model generates good-looking videos without quantifying whether the control is precisely followed. Camera rotation accuracy, motion RMSE, or human evaluation on "does the camera move as specified?" are needed.

**Paper example:** MotionDirector was rejected (rating 5.5) despite interesting ideas — reviewers found the approach incremental relative to prior motion customization methods and insufficient evaluation of control precision.

### 5.7 Long Video Generation

**Core technical challenge:** A base video model generates N frames. Long video generation requires extending this to M >> N frames while maintaining temporal consistency, avoiding content drift, and managing memory.

**Approaches and what to evaluate:**
- Sliding window / noise rescheduling (FreeNoise, FreeLong): No additional training, but quality may degrade at boundaries
- Hierarchical generation (StoryDiffusion, VideoChat-Flash): Generate keyframes then fill in — evaluate consistency between keyframes
- Autoregressive extension: Must avoid error accumulation

**Expected evaluation:**
- Temporal consistency over the full sequence (not just adjacent frames)
- Comparison against base model on short segments (to show extension doesn't degrade quality)
- Human evaluation for long-range coherence
- Memory/compute profile vs. generated length

**Paper example:** StoryDiffusion (7.0, Spotlight): praised for training-free consistent self-attention and strong results on character consistency. Criticisms: limited ablation on sampling rate effect, missing story-generation-specific baselines (e.g., The Chosen One, Training-Free Consistent T2I).

**Paper example:** VideoChat-Flash (6.5, Accept): praised for multi-faceted contributions (compression, dataset, benchmark), but one reviewer noted the "almost no performance loss" claim was not fully supported by ablation Table 2, where adding HiCo alone actually drops performance before the new training data compensates.

### 5.8 4D / 3D Generation from Video

**Key distinctions:**
- **Object-centric 4D** (Diffusion4D, 4Dfy): Generate a dynamic object viewable from any angle
- **Scene-level 4D** (4Real): Generate a full scene with background and foreground dynamics
- **Static 3D from sparse views** (ReconX): Novel view synthesis

**Technical components:**
- 3D representation: NeRF vs 3D Gaussian Splatting (3DGS) vs 4DGS
- Motion representation: Deformation fields, temporal Gaussian motion
- Score Distillation Sampling (SDS) vs. direct supervision

**Expected evaluation:**
- Multi-view rendering metrics (PSNR/SSIM/LPIPS from held-out views)
- User studies comparing visual quality and naturalness
- FVD on the generated video sequence
- Speed comparison (SDS-based methods are notoriously slow; 4Real reduced from 10+ hours to 1.5 hours)

**Common weaknesses in 4D papers:**
- Generated motions are very small and simple — not actually testing the hardest cases
- Only evaluating from viewpoints used during optimization
- Comparing against weaker baselines (NeRF-based) while ignoring newer 3DGS-based methods
- "Folder called 'good results' in the supplementary" — selective example presentation

**Paper examples:**
- 4Real (6.2, Accept): praised for eliminating need for synthetic multi-view model, scene-level (not object-only) generation. Criticized for not comparing against AYG, overstating "object-environment interaction" claims, and relying on manually chosen poses.
- Diffusion4D (6.0, Accept): praised for curated Objaverse dataset, faster than SDS. Criticized for limited visual quality (low-res, blurred, obvious inconsistencies), unclear method description, small motions in qualitative examples.

### 5.9 Video Diffusion Models (Efficiency / Architecture)

For papers proposing inference acceleration or architectural improvements to video diffusion:

**Required evaluations:**
- Comparison to baseline video model (e.g., AnimateDiff, SVD, Open-Sora) on generation quality
- FVD and CLIP score (minimum) — but also VBench if claiming comprehensive quality preservation
- Memory reduction: peak GPU memory in GB
- Speed: wall-clock inference time (seconds per video), not just FLOPs
- At least two backbone architectures (to show generality beyond U-Net or DiT)

**Common weaknesses in efficiency papers:**
- Only tested on U-Net architectures (SVD/AnimateDiff) without addressing DiT-based models (Open-Sora, CogVideoX)
- FVD alone declared sufficient when quality degradation is visible in figures
- Comparing against trivial baselines (only "naive hashing" or no-caching baseline)
- Missing VBench metrics that would expose per-dimension quality differences

**Reviewer quote from StreamlinedInference:** "The evaluation relies heavily on FVD and CLIP-Scores, which may not capture all dimensions of video quality. Including additional metrics or user studies could provide a more holistic assessment."

**Reviewer quote:** "The proposed framework is only applicable to U-Net-based video diffusion models. However, recent models, such as those utilizing DiT backbones, are not addressed by this framework."

### 5.10 Video Generation for Downstream Tasks (Robotics, Planning, Autonomous Driving)

This is a particularly complex evaluation domain. Video generation is used as a **means**, not an end. The paper must justify that the generative approach is better than task-specific baselines.

**For robotics/manipulation papers:**
- Must compare against strong, current robotic baselines (not 2-year-old methods like PerAct)
- Must show task success rate, not just video quality metrics
- Should clarify if evaluation is open-loop or closed-loop (closed-loop is more credible)
- Web-scale pretraining benefits must be clearly demonstrated (not just "marginal improvement")

**For autonomous driving data synthesis:**
- Must show the generated data actually improves or challenges a planner
- Open-loop evaluation is acceptable but should acknowledge limitations vs. closed-loop
- Must compare to simulation-based alternatives where applicable

**Paper example:** VidMan (6.4, Accept Poster): the highest individual rating was 9 (for the two-stage training insight and thorough ablations), but the paper also received 5s and 6s for using obsolete baselines on RLBench (PerAct instead of RVT/3DDA) and failing to compare directly against GR-1 (the closest prior work). The paper was accepted largely because the core idea was sound and the ablations were thorough, but it illustrates the risk of outdated baselines.

**Paper example:** UniPi (6.5, Spotlight NeurIPS 2023): praised for ambitious framing (video generation as universal policy) and strong experiments across simulation and real-world. Criticized for limited technical novelty in the diffusion adaptation and overlap with Decision Diffuser.

**Paper example:** SafeMVDrive (6.0, Reject ICLR 2026): despite interesting application (safety-critical multi-view driving video generation), rejected because it lacked experiments showing the generated data improves a planner's robustness. The engineering value was acknowledged but academic contribution was unclear.

---

## 6. Expected Baselines by Subfield

### Text-to-Video Generation
- Zero-shot / training-free: Text2Video-Zero, CogVideo (smaller scale)
- Trained models: VideoLDM, ModelScope, Make-A-Video, Imagen Video, VideoCrafter, Show-1, LaVie
- Open-source recent: CogVideoX, Open-Sora, Wan
- For RLHF/reward-tuned: T2V-Turbo, InstructVideo

### Image-to-Video
- SVD (Stable Video Diffusion), SEINE, DynamiCrafter, Emu Video
- For long generation: I2VGen-XL

### Video Editing
- Prompt2Prompt, Tune-A-Video, TokenFlow, ControlVideo, FLATTEN, FateZero
- Instruction-based: InstructPix2Pix adapted, InstructVideo, RAVE

### Video Frame Interpolation
- **Must-include**: RIFE, IFRNet, EMA-VFI, AMT
- **Common**: BiFormer, SGM-VFI, FILM
- **High-resolution specific**: XVFI

### Video Super-Resolution
- BasicVSR++, RVRT, VRT
- Real-world: RealBasicVSR, BSRGAN+VSR

### Controllable Video Generation
- AnimateDiff (+ControlNet), MotionDirector (for motion), CameraCtrl (for camera), SparseCtrl

### Long Video Generation
- FreeNoise, FreeLong, NUWA-XL, Gen-L-Video

### 4D Generation
- SDS-based: DreamFusion (3D), 4Dfy, Dream-in-4D, Consistent4D
- Feed-forward: Zero123++, One-2-3-45 (for 3D prior), LGM
- 4DGS: AYG, Animate3D

### Video Diffusion Architecture/Efficiency
- Base model being accelerated: AnimateDiff, SVD, Open-Sora
- Comparable methods: DeepCache, PAB, TeaCache, AdaCache

### Robotics via Video
- **Essential**: GR-1, UniPi, SuSIE
- **Strong**: PerAct, Act3D, RVT (RLBench), 3DDA (current SOTA RLBench), Octo, OpenVLA (for general policies)

---

## 7. Expected Evaluation Metrics

### Quality Metrics
| Metric | Usage | Notes |
|--------|-------|-------|
| FVD (Frechet Video Distance) | Primary for T2V, I2V, video prediction | Lower is better; often computed on UCF-101, Kinetics-400 |
| FID (Frechet Inception Distance) | Per-frame quality | Supplementary to FVD |
| IS (Inception Score) | UCF-101 only | Historical; still reported in some papers |
| PSNR | VFI, VSR, reconstruction | Higher is better; dB scale |
| SSIM | VFI, VSR, editing preservation | 0–1, higher is better |
| LPIPS | Perceptual similarity | Lower is better |
| CLIPSIM / CLIP Score | Text-video alignment | Range ~0.2–0.35 for good models |

### Comprehensive Benchmarks
| Benchmark | Coverage |
|-----------|----------|
| VBench | 16 dimensions of T2V quality (subject consistency, motion smoothness, scene, etc.) |
| EvalCrafter | Text-video alignment, visual quality, action quality |
| MSRVTT-FVD | Standard T2V benchmark |
| UCF-101 zero-shot FVD | Historical standard |
| SNU-FILM (Easy/Medium/Hard/Extreme) | VFI large motion |
| X-TEST (2K/4K) | VFI high resolution |
| REDS4/Vid4 | VSR |
| DAVIS | Video editing preservation |

### Human Evaluation
Reviewers frequently ask for human evaluation when:
- The claim is about perceptual quality (not just FVD)
- FVD results are surprising or counter-intuitive
- The domain is hard to capture with automated metrics (4D generation, long video coherence)

Standard human evaluation for video generation compares pairs of videos on: visual quality, motion naturalness, text alignment (or other conditioning). User studies should involve at least 30–50 participants and use appropriate statistical significance tests.

### Downstream Task Metrics
- **Robotics**: Task success rate (%), inference time per step
- **Autonomous driving**: Collision Rate (CR), Near-Collision Rate (NC), Time-to-Collision (TTC), L2 displacement error
- **Video understanding**: Top-1 accuracy on K400, SSv2, EK-100

---

## 8. Red Flags That Indicate a Weak Paper

The following patterns consistently correlate with rejection or low scores:

**Technical Red Flags:**
1. **Training/inference inconsistency**: Method uses ground truth information at training time that is unavailable at inference, without justifying this gap
2. **No ablation on the most important component**: If the entire paper claims Component X is the key contribution but Component X is never ablated in isolation, the claim cannot be accepted
3. **The method is a system of existing components with no new algorithm**: Multiple reviewers used the phrase "clever integration of existing ideas" as a rejection reason
4. **Flawed baseline training setup**: Different training data, training steps, or seeds across compared methods — makes all comparisons suspect
5. **Inconsistent notation or math errors**: Multiple typos in equations undermine confidence in correctness

**Evaluation Red Flags:**
6. **Cherry-picked qualitative examples only**: Supplementary folder named "good_results" or only showing best cases
7. **Selective table population**: Comparing FVD only against methods with worse FVD; omitting methods that outperform the proposed approach
8. **Only WebVid-10M subset**: Not testing on standard benchmarks (UCF-101, MSR-VTT)
9. **Suspiciously good FVD results**: Reviewers ask for double-checking; one reviewer of GenRec explicitly asked "Is it a typo?" for an outlier FVD result
10. **User study with <20 participants or no statistical test**: Insufficient to draw conclusions

**Novelty Red Flags:**
11. **Prior work omission**: If the paper does not cite the 3 most closely related methods, reviewers will assume the authors are unaware of the field or hiding unfavorable comparisons
12. **Method described as "first to do X" without checking**: This claim will be fact-checked
13. **Contribution is just applying Architecture A to Task B**: Without new insight about why A works for B, this is typically not publishable

**Writing Red Flags:**
14. **All important implementation details in appendix with no main-paper pointers**: Reviewers cannot evaluate the method if key details are hidden
15. **Unquantified claims**: "our model is lightweight," "inference is fast," "almost no performance loss" without numbers
16. **Overclaimed scope**: Claiming scene-level generation but only showing object-level examples

---

## 9. Green Flags That Indicate a Strong Paper

**Technical Green Flags:**
1. **Clear problem statement that identifies a specific, previously unaddressed failure mode**: e.g., "velocity ambiguity in VFI," "conditional image leakage in I2V," "reliance on synthetic multi-view models in 4D generation"
2. **Principled, motivated design choices**: Each architectural decision is justified theoretically or empirically, not just empirically tuned
3. **Training-free / plug-and-play validated on multiple base models**: Demonstrates generality beyond one backbone
4. **New dataset + model + benchmark**: Multiple contributions that independently benefit the community (VideoChat-Flash: HiCo + LongVid + Multi-Hop NIAH benchmark)
5. **Interesting negative results reported honestly**: VidMan's finding that web-scale video data provides minimal benefit was praised as "good to know and it contrasts findings from recent papers"

**Evaluation Green Flags:**
6. **Comprehensive evaluation including all standard benchmarks for the subfield**: Not just the benchmarks where the paper does best
7. **Human evaluation with adequate participant count and statistical tests**
8. **Efficiency analysis (memory, latency) for systems claiming computational benefits**
9. **Real-world experiments** for robotics/manipulation (or explicit acknowledgment of the limitation)
10. **Supplementary video with genuine motion variety** — not just static scenes slightly perturbed

**Writing Green Flags:**
11. **Single clear innovation clearly articulated in one sentence in the abstract/intro**
12. **Limitations section that is honest, not defensive**: Listing genuine limitations earns reviewer trust
13. **Code/model release commitment**: Makes acceptance easier to justify
14. **Concise related work that clearly positions the paper against the 3–5 closest prior methods**

---

## 10. Border Cases: How to Handle Papers in the 5–6 Range

The 5–6 borderline is the most common and most contested range. Here is guidance for distinguishing papers that should be accepted (6) from those that should be rejected (5):

### Tip Toward Accept (6) When:
- The paper has genuine novelty in at least one component, even if the overall system is incremental
- Results are positive on multiple standard benchmarks, even if not state-of-the-art on all
- Ablations are present, even if not exhaustive
- The authors provide a rebuttal that addresses major reviewer concerns with concrete numbers
- The application area is important and the paper is one of the first to address it credibly
- Missing baselines are genuinely difficult to implement or reproduce (not just ignored)

### Tip Toward Reject (5) When:
- The technical formulation has a logical flaw that the rebuttal does not fully resolve
- Baselines are outdated and the authors argue they are sufficient without evidence
- Ablations are purely qualitative when quantitative ablations are feasible
- The paper's main claim ("we are the first to do X") is demonstrably false based on cited prior work
- Results on the most competitive benchmark are worse than or equal to a simpler baseline the paper should have cited
- Evaluation is only on a proprietary dataset with no public benchmark comparison

### The Rebuttal Factor
At ICLR and NeurIPS, strong rebuttals can swing borderline papers. The VFI distance-indexing paper (QuFHei1vuE) started at 6, 8, 6, 8 and the most critical reviewer (who gave a 6) stated post-rebuttal: "I have slightly misunderstood the main message of the work in my initial review and the authors did a great job in correcting my misunderstanding. I will happily increase my score to accept." Yet the paper was still rejected — likely due to the overall conference dynamics or area chair weighting.

### Common Borderline Pattern: The "Interesting System Paper"
A system that combines multiple existing components in a new way, with positive but not state-of-the-art results, and limited ablation distinguishing each component's contribution. These papers often receive a mix of 5s and 7s. The paper should be accepted if:
- The combination reveals new insight (not just that combining works)
- The system enables something previously impossible (e.g., real-time, or handling much longer videos)
- The paper provides the community with useful artifacts (code, data, benchmark)

---

## 11. Rating Examples: Concrete Cases from the Corpus

### Rating 8 (within a paper):
**VFIMamba, NeurIPS 2024**: Reviewer giving 8 cited: "first to adapt S6 model to VFI," "reaches new state-of-the-art performance," "exhaustive ablation studies proving the effectiveness for each introduced module," "relatively simple curriculum learning strategy with experiments confirming it is beneficial for VFI methods in general." Reviewer confidence: 5 (expert). Key: combination of genuine novelty (new architecture family for VFI), thorough ablation, and state-of-the-art results at high resolution.

**4Real, NeurIPS 2024**: Reviewer giving 8 cited: "very well-motivated and well-written," "clearly and explicitly identified" key limitation in prior work (synthetic data reliance), "evaluations demonstrate very clear improvements over the state of the art." This is a case where one strong reviewer can pull a paper up despite others giving 5–6.

### Rating 7 (accepted papers):
**StoryDiffusion, NeurIPS 2024 Spotlight**: Multiple 7s and one 8. "Strong and compelling results," "attacks a timely/important problem," "consistent self-attention solution is particularly simple conceptually and does not require any training." The spotlight designation despite mixed 6–8 scores suggests the novelty of the training-free consistency approach was highly valued.

**UniPi, NeurIPS 2023 Spotlight**: Two 7s, two 6s. "Well written, clear and easy to understand," "extensive experiments... including high-quality video generation, combinatorial generalization and multi-environment transfer." Criticized for limited novelty in diffusion adaptation and overlap with Decision Diffuser. The spotlight indicates that paper framing (universal policies via video) and breadth of experiments outweighed novelty concerns.

### Rating 6 (borderline accepted):
**VidMan, NeurIPS 2024**: Averaged 6.4 with a 9, 7, 5, 5, 6. The 9 praised the "two-stage training approach as a deep insight." The 5s criticized obsolete baselines and missing direct comparison to GR-1. The paper was accepted — the strong positive signals from the core idea and ablations outweighed the experimental shortcomings.

**Free-Bloom, NeurIPS 2023**: Averaged 6.0 with two 5s and two 7s. Borderline case: the LLM director for zero-shot T2V was novel and well-received, but insufficient ablations and weak coherence dragged it down. The two 7s were enough to carry it over.

**VideoChat-Flash, ICLR 2026**: Averaged 6.5 with a 4, 8, 6, 8. The reviewer giving 4 had legitimate concerns about novelty (clever integration), but the paper was accepted because the multi-faceted contributions (compression method + dataset + benchmark), strong overall performance, and community artifacts outweighed the novelty concerns.

### Rating 5 (borderline rejected):
**VideoFactory, ICLR 2024**: Averaged 5.25 with four 5s and one 6. The dataset contribution (HD-VG-130M) was genuinely valued, but cherry-picked evaluation tables and weak technical novelty in the attention mechanism were sufficient to reject. "The proposed 'swapped attention' mechanism does not appear to significantly impact the task of video generation itself."

**Marrying Pixel and Latent Diffusion, ICLR 2024**: All four reviewers gave 5. The paper was well-written with a clear motivation, but the pipeline was "not something new" and the motivation for the specific hybrid design was "unconvincing." No reviewer was enthused enough to push for accept.

### Rating 4 (within a paper, in accepted papers):
**VideoChat-Flash, ICLR 2026**: One reviewer gave a 4 specifically because: "novelty of the proposed method — while the system as a whole is novel and highly effective, its constituent parts are largely clever integrations of existing ideas." The reviewer also pointed to the ablation table showing performance drops when adding HiCo alone. This is instructive: even accepted papers can receive 4s when the novelty concern is legitimate, but the overall package (results, community value, artifacts) carries the paper.

---

## 12. Field-Specific Notes and Calibration Adjustments

### The Diffusion Model Era (2023–2026 Corpus)

Nearly all papers in this corpus use diffusion models. This means:
- "We propose a diffusion model for X" is no longer novel by itself — the novelty must be in the architecture, training procedure, conditioning mechanism, or application
- U-Net vs DiT is a live architectural debate: papers using only U-Net-based models (AnimateDiff, SVD) risk being dismissed as not evaluating on more modern DiT-based systems (Open-Sora, CogVideoX, Wan)
- Training-free methods (modifications to inference without fine-tuning) are valued highly for their accessibility but must still be evaluated rigorously

### The Efficiency / Compression Cluster

About 20–30 papers in this corpus propose inference acceleration or token compression. This has become crowded, and reviewers are skeptical of:
- Papers that only test on one backbone
- Papers that claim efficiency without VBench-style comprehensive quality evaluation
- Papers whose only contribution is a heuristic caching scheme without theoretical grounding

A compression paper needs either (1) theoretical understanding of why the compression works, or (2) empirical evidence it generalizes across multiple model families with negligible quality loss on comprehensive benchmarks.

### The Benchmark Saturation Problem

Multiple papers propose new benchmarks (VBench, EvalCrafter, PhyWorldBench, Multi-Hop NIAH). Benchmark papers are accepted when:
- The new benchmark captures something existing benchmarks miss (e.g., physical commonsense, multi-hop reasoning)
- The paper includes thorough analysis of how existing models fail on the new benchmark
- The benchmark is large enough and diverse enough to be reliable
- Human annotation quality is validated

Benchmark papers are rejected when the benchmark is too narrow, too easy (saturated quickly), or when no clear gap from existing benchmarks is demonstrated.

### The Robotics + Video Cluster

This is a high-value but harshly scrutinized area. Reviewers expect:
- Closed-loop evaluation or explicit acknowledgment of open-loop limitations
- State-of-the-art robotics baselines (as of submission date — this field moves fast)
- Generalization beyond the specific simulation environment
- Scalability analysis (does performance improve with more data?)

The UniPi/VidMan/GEVRM cluster of papers all show that the core idea of "video generation as world model for planning" is scientifically compelling. Papers in this space should be evaluated on whether they advance the understanding of when and why video-based planning works, not just whether they beat the previous paper in the same sub-niche.

---

## Summary: Quick Reference Card for Reviewers

| Dimension | Minimum for Accept | Sufficient for Strong Accept |
|-----------|-------------------|------------------------------|
| Novelty | One component genuinely new | Opens a new direction or reframes a problem |
| Ablations | Quantitative isolation of each claimed component | Comprehensive ablations covering architectural choices, training data, hyperparameters |
| Baselines | Current SOTA for the subfield | All methods in the subfield that are feasibly comparable |
| Benchmarks | Primary standard benchmark for subfield | Multiple standard benchmarks + human evaluation |
| Efficiency (if claimed) | Memory/latency numbers on at least 2 backbones | FLOPs, memory, latency scaling curves + VBench |
| Writing | Method clearly explained, notation consistent | Polished, figure-rich, limitations honest |
| Code | Committed to release | Already available at submission |
| Downstream value | Community can build on it | New dataset, benchmark, or model released |

**The bottom line:** In video generation, the field moves fast. A paper that was novel 18 months before submission may be incremental by submission time. The best papers clearly identify a **specific, hard, previously unaddressed problem**, provide a **principled solution with thorough ablations**, and **compare against all relevant current methods** on **standard benchmarks**. Papers that do these three things rarely fail to be accepted, regardless of whether the results are state-of-the-art on every metric.

---

## 13. Reviewer Psychology and Scoring Dynamics

Understanding how reviewers in this field reason is as important as knowing the technical standards.

### 13.1 The Novelty Anchoring Effect

In video generation, reviewers heavily anchor their initial score on perceived novelty before reading results. A paper that clearly states a novel problem in the abstract and introduction will receive the benefit of the doubt during results evaluation. A paper that reads as "we apply X to Y" will face skepticism throughout, even if results are good.

The practical implication: when judging a paper, ask yourself whether the paper's **framing** communicates a clear gap in the literature. If the introduction spends most of its space describing what they did rather than what was missing before they did it, this is usually a sign the contribution is incremental.

Specific to video generation: the field has seen so many "X meets diffusion models" papers that simply applying diffusion to a new task is no longer sufficient. The contribution must be in *how* the diffusion model is adapted, *why* naive adaptation fails, and *what specific insight* resolves this.

### 13.2 The Baseline Credibility Test

Reviewers with domain expertise immediately scan the results tables and check:
1. Is the most recent competitive method included?
2. Are the improvements large enough to be meaningful (not just noise-level improvements)?
3. Are all methods trained under the same conditions?

A paper that wins on every benchmark by a large margin is more suspicious than one that shows selective, meaningful improvements on specific dimensions. Reviewers often increase their skepticism when results appear too clean.

For video generation specifically, reviewers are aware that FVD is highly sensitive to the evaluation protocol (number of frames, reference distribution, backbone model). Papers that report novel evaluation protocols without detailed justification trigger suspicion.

### 13.3 The "I Can't Reproduce This" Concern

For papers claiming training-free methods or plug-and-play modules, reviewers evaluate whether they could independently implement and test the method. When implementation details are absent or vague, a reviewer cannot trust the results. This is why:
- Papers that share code at submission time are viewed very favorably
- Papers that describe the algorithm in an appendix without a main-paper pointer receive lower scores
- Papers with notation that changes between sections (variable T meaning both diffusion steps and frame count, as noted in the Marrying Pixel/Latent paper) signal sloppiness

### 13.4 Reviewer Score Divergence and Acceptance

In this corpus, many papers have high variance in scores — one reviewer gives 8 while another gives 4. This is especially common in:
- Robotics/video papers where some reviewers are video experts and others are robotics experts
- System papers where different reviewers weigh novelty vs. engineering contribution differently
- 4D generation papers where some reviewers value visual quality and others value methodological rigor

When you see score divergence, the decisive factor is usually whether the majority of reviewers are willing to fight for the paper. A single 8 with three 5s is typically a reject; two 7s with two 5s is more genuinely borderline. The area chair weighs reviewer confidence: a reviewer with confidence 5 (expert) who gives 5 counts more than a reviewer with confidence 2 who gives 7.

### 13.5 The Rebuttal Window

NeurIPS and ICLR include a rebuttal period. Rebuttals that change scores follow a pattern:
- The reviewer had a **specific, addressable concern** (missing ablation, missing baseline, misunderstanding of method)
- The authors provided **concrete numbers** in the rebuttal (not just promises of "we will add X in revision")
- The reviewer's fundamental position on novelty was not negative (if the reviewer says "limited novelty," no amount of new experiments will change their view)

The VFI distance-indexing paper (QuFHei1vuE) is instructive: the most critical reviewer explicitly stated they had "slightly misunderstood the main message" and increased their score after rebuttal. Yet the paper was still rejected — suggesting that paper clarity in the original submission is crucial, since reviewers who misunderstand your paper do not always correctly self-identify that misunderstanding.

---

## 14. Subfield-Specific Novelty Standards

Different subfields within video generation have different novelty bars, reflecting how saturated they are.

### 14.1 Text-to-Video: Very High Novelty Bar

By 2024–2026, the T2V space has seen dozens of papers. The community has largely converged on the following architecture: (1) a spatiotemporal UNet or DiT backbone, (2) pretrained text encoder (T5 or CLIP), (3) latent diffusion in a video VAE latent space, (4) large-scale video data training. A paper in this space needs to do one of the following to be accepted:

- **Architecture innovation**: New attention mechanism (e.g., VFIMamba's interleaved SSM tokens), new spatiotemporal representation that is demonstrably better than 3D attention
- **Training paradigm innovation**: New curriculum (VFIMamba's curriculum learning), new data strategy (high-quality curated data), new conditioning mechanism
- **Capability expansion**: Video understanding + generation jointly (GenRec), much longer videos, better controllability
- **Efficiency breakthrough**: Dramatically faster or cheaper training/inference while maintaining competitive quality (not just 20% faster with 5% FVD degradation)
- **Task formulation innovation**: Framing an entirely new problem (UniPi's "video generation as universal policy")

Papers that simply use a different backbone (e.g., "we use Mamba instead of Transformer") without showing why Mamba is specifically well-suited to the task will not pass the novelty bar.

### 14.2 Video Frame Interpolation: Moderate Novelty Bar

VFI is a more mature subfield with clear, reproducible benchmarks. The community expects:
- PSNR improvements of at least 0.1–0.2 dB on Vimeo-90K to be meaningful (not noise-level)
- New methods should be compared against all recent methods (RIFE, IFRNet, EMA-VFI, AMT, BiFormer)
- Architectural novelty should be in how the temporal modeling works, not just in applying a known architecture

The VFIMamba paper is a good example of the standard: the novelty (SSM for VFI) is clearly new and motivated (linear complexity for high-resolution inputs), the ablations are exhaustive, and the performance gains are specifically demonstrated at the task where the architecture is theoretically best suited (high-resolution frames where quadratic attention is expensive).

### 14.3 Video Editing: High Novelty Bar, Low Benchmark Saturation

Video editing has many papers but fewer agreed-upon quantitative benchmarks than T2V or VFI. This creates both an opportunity (novel benchmarks are valued) and a risk (evaluations are easier to cherry-pick). Reviewers in this space are especially skeptical of:
- Papers with only qualitative comparisons
- Papers that show edits that could have been done with simpler per-frame methods
- Papers that don't address temporal consistency explicitly

### 14.4 4D Generation: Lower Novelty Bar (Emerging Area)

4D generation (dynamic 3D from text or video) is still an emerging area with fewer methods and less consensus on evaluation. This means:
- Earlier papers in this space were accepted with relatively modest technical contributions
- By 2024–2026, the bar has risen: naive combinations of 3D + video generation are no longer sufficient
- Strong visual quality (showing diverse, large-motion 4D objects) is a prerequisite — reviewers noted that Diffusion4D's motions were "very small and easy"
- Comparison against AYG, 4Dfy, Consistent4D is expected

### 14.5 Efficiency / Compression: Rapidly Saturating

As noted earlier, efficiency papers have become very common (20–30 in this corpus). The novelty bar has risen sharply. What was novel in 2023 (training-free caching) is expected baseline behavior by 2025. Papers in this space should:
- Target a specific, hard inefficiency (not just "video diffusion is slow")
- Provide theoretical justification for why their approach works
- Show that quality is genuinely preserved across all VBench dimensions, not just FVD
- Test on both U-Net and DiT architectures

### 14.6 Robotics/Video: Moderate Novelty Bar with High Execution Standards

The robotics + video generation space is scientifically exciting but execution-heavy. A paper can have a modest technical contribution if the experimental validation is thorough. However, the standards for experiments are strict:
- CALVIN or RLBench with current SOTA baselines
- Multiple seeds for reliability
- Ablations that isolate the video pretraining benefit from other confounds (e.g., more data, larger model)

---

## 15. Common Patterns in the Accept/Reject Decision

After analyzing the full corpus, the following decision patterns emerge:

### Pattern 1: Strong Core Idea + Weak Execution = Borderline Accept
Examples: VidMan (rating 6.4), GenRec (rating 6.2). These papers have genuinely interesting scientific questions (can video pretraining help manipulation? can generation and recognition be unified?) but compromised execution (outdated baselines, missing comparisons). They are accepted because the core question is worth pursuing and the paper provides useful evidence, even if not definitive.

**Recommendation for judging**: Ask "Does this paper advance scientific understanding of an important question?" If yes, weak execution in baselines/ablations can be partially forgiven if it doesn't invalidate the core finding.

### Pattern 2: Solid Execution + Incremental Idea = Borderline Reject
Examples: VideoFactory (rating 5.25), Marrying Pixel and Latent (rating 5.0). These papers are well-executed technically and empirically, but the core idea is a variation on prior work without new insight. They are rejected because the community learns little from them that wasn't already known.

**Recommendation for judging**: Well-written, empirically sound papers that combine existing methods without insight should be rated 4–5, not 6+. The technical quality of execution does not override lack of novelty.

### Pattern 3: System Paper with Community Value = Accept Despite Modest Novelty
Examples: VideoChat-Flash (rating 6.5, with one 4 and two 8s). Papers that release new datasets, benchmarks, or large-scale models are valued as community contributions even when individual components are not novel. The Multi-Hop NIAH benchmark and the LongVid dataset in VideoChat-Flash are examples.

**Recommendation for judging**: If a paper's individual contributions seem incremental but the paper provides artifacts (code, data, benchmarks) that the community can use, add 0.5–1.0 to your rating. The community multiplier is real.

### Pattern 4: First-in-Class with Limited Comparison = Accept
Examples: VFIMamba (rating 6.75), 4Real (rating 6.2). Being first to apply a technique class to a problem (first SSM-based VFI, first photorealistic scene-level 4D) is inherently valuable even if the direct performance gains are modest. The community needs to know if the approach works.

**Recommendation for judging**: "First to do X" claims require verification (is the paper actually first?), but when verified, they lower the bar for performance gains required for acceptance.

### Pattern 5: High Reviewer Disagreement = Likely Accept
In the NeurIPS and ICLR data, papers with very high score variance (e.g., 4, 5, 8, 8) are more likely to be accepted than papers with consistent 5s, because the presence of 8s signals that at least some experts found the work compelling. Area chairs tend to break ties in favor of positive outliers for novel work.

**Recommendation for judging**: A paper that generates excited 8s alongside confused 4s is a different animal from a paper that uniformly generates 5s. The former should be treated more charitably.

---

## 16. Common Mistakes Judges Make When Evaluating Video Generation Papers

### Mistake 1: Treating Visual Quality as the Only Standard

Video generation papers often have impressive supplementary material with high-quality demos. Judges who are swayed primarily by visual quality miss:
- Whether the results are cherry-picked (look for diversity in the supplementary, not just best cases)
- Whether quantitative improvements match visual quality claims
- Whether baselines are given equal treatment (was the baseline prompt engineered as well?)

**Correction**: Always check the quantitative tables against the qualitative figures. If a paper claims "significant improvements" but the FVD gap is 3–5 points out of 100+, this is marginal.

### Mistake 2: Assuming DiT > UNet Without Checking

Recent papers often use DiT architectures (following Stable Diffusion 3, CogVideoX) and claim superiority over UNet-based methods. But this superiority often comes from scale (larger model, more data), not architecture. A judge should check:
- Are model sizes comparable?
- Is training data comparable?
- If a UNet model is trained at the same scale, does the DiT architecture still win?

### Mistake 3: Penalizing Concurrent Work Omission

Reviewers sometimes penalize a paper for not comparing against a concurrent arXiv paper submitted within weeks of the submission deadline. This is unfair. The standard is:
- Papers published in peer-reviewed venues before the submission deadline must be cited and compared
- arXiv preprints that appeared within 1–2 months of submission are optional to compare against but should at least be cited
- Papers that appeared after the submission deadline cannot be expected

### Mistake 4: Applying T2V Standards to VFI Papers

VFI papers use different benchmarks, metrics, and comparison frameworks. A judge with a T2V background might penalize a VFI paper for not reporting FVD, which is not a standard VFI metric. Similarly, a VFI expert might not recognize that FVD is the correct metric for T2V.

**Correction**: Read Section 5 of this skill file carefully and apply domain-specific standards to each subfield.

### Mistake 5: Misinterpreting "State-of-the-Art"

In video generation, "state-of-the-art" is a relative claim. A paper might be SOTA on UCF-101 at submission time and be beaten by three new methods before the camera-ready deadline. This is expected in fast-moving fields. Papers should not be penalized for not being SOTA on benchmarks where new results appeared after submission.

However, papers should be penalized for:
- Claiming SOTA while omitting the current best-known number from the table
- Achieving SOTA only by cherry-picking which benchmark to report

### Mistake 6: Confusing "Interesting" with "Publishable"

Many video generation ideas are intellectually interesting but not well enough executed to be publishable. A paper about a fascinating new framing (e.g., "video generation as physical simulation") with only qualitative results and no standard benchmark evaluation is interesting but not ready for acceptance. The judge must separate "this is a good idea worth pursuing" from "this paper provides sufficient evidence that the idea works."

---

## 17. Temporal Evolution of Standards (2023–2026)

Understanding how the standards have changed over the corpus period is important for calibrating ratings:

### NeurIPS 2023 (Earlier Papers)
- Zero-shot text-to-video methods (Free-Bloom) were novel enough to accept despite modest quality
- Planning via video generation (UniPi) was a novel framing that was spotlight-worthy
- The standard for VFI papers was: match existing SOTA on Vimeo-90K + SNU-FILM with some novelty

### NeurIPS 2024 (Middle Period)
- T2V quality has improved dramatically; zero-shot methods without any training are no longer competitive against full-training systems
- Efficiency papers for video diffusion (StreamlinedInference) are accepted but held to higher evaluation standards
- 4D generation has multiple competing methods; novelty requires scene-level (not just object-level) capabilities
- Video + robotics space is maturing; outdated baselines are harshly penalized

### ICLR 2025–2026 (Recent Papers)
- Multimodal LLMs for video understanding (VideoChat-Flash) have become a major cluster; evaluated more like LLM papers than generation papers
- Long video generation is a major focus; efficiency under long-context is now table stakes
- Camera control, motion control have become standard capabilities; papers claiming novelty here need very precise control (not just "approximate" camera following)
- DiT-based models have largely supplanted UNet in T2V; papers using only UNet backbones may be asked to add DiT experiments

The overall trajectory is: **what was exciting in 2023 is standard by 2026**. Calibrate your novelty assessment relative to the year of submission.

---

## 18. Final Calibration Exercises

Use these described papers to calibrate your rating before judging new submissions:

### Exercise 1: VFIMamba (NeurIPS 2024, avg 6.75, Accept Poster)
This paper applies Mamba (SSM) to video frame interpolation via an interleaved token rearrangement. Ablations cover each component. Results show SOTA PSNR at high resolution. Weaknesses: some unfair training data comparisons in tables, missing FLOPs scaling analysis, some discrepancies in reported numbers vs. original papers.

**Reference rating: 6.75 (Accept Poster)**. If you would rate this 8+, you are over-generous. If you would rate this 5–, you are underweighting solid execution with genuine architectural novelty.

### Exercise 2: VideoFactory (ICLR 2024, avg 5.25, Reject)
This paper proposes swapped spatiotemporal attention for T2V generation and contributes the HD-VG-130M dataset. The attention mechanism is modestly novel but not well-differentiated from prior attention work in video. The dataset is genuinely valuable. Baselines in the FVD table are selectively reported.

**Reference rating: 5.25 (Reject)**. If you would accept this paper primarily based on the dataset contribution, note that dataset papers with good technical models are typically acceptable, but this paper's technical model has weaknesses that the dataset does not compensate for.

### Exercise 3: 4Real (NeurIPS 2024, avg 6.2, Accept Poster)
This paper generates photorealistic 4D scenes via video diffusion, eliminating the need for synthetic multi-view training data. It receives an 8 from one reviewer ("very well-motivated, clear improvements") and 5–6 from others (missing AYG baseline, overstated interaction claims). Genuinely advances the field by enabling scene-level (not object-centric) 4D generation.

**Reference rating: 6.2 (Accept Poster)**. This paper illustrates that a clear, well-motivated contribution to an important problem can be accepted even with incomplete evaluation, as long as the core idea is sound and demonstrated.

### Exercise 4: Marrying Pixel and Latent Diffusion for T2V (ICLR 2024, avg 5.0, Reject)
All four reviewers give 5. Paper is well-written with clear motivation but proposes a pipeline that is fundamentally similar to Make-A-Video and Imagen Video. The incremental difference (specific placement of pixel vs. latent stages) does not provide new scientific insight.

**Reference rating: 5.0 (Reject)**. Papers at this level are technically competent but scientifically unoriginal. Even if every claimed result is true, the community learns nothing new from reading this paper.

### Exercise 5: GenRec (NeurIPS 2024, avg 6.2, Accept Poster)
This paper unifies video generation and recognition by jointly training SVD on both tasks. Receives ratings of 5, 7, 5, 9, 5 across reviewers. The extremely high 9 reflects genuine excitement about a key question (can generative models help discriminative tasks?). The multiple 5s reflect concerns about comparison fairness (missing InternVideo, missing model size parity) and limited baselines.

**Reference rating: 6.2 (Accept Poster)**. The scientific question here is important enough that even an imperfect execution is published. Note the reviewer giving 9 was an expert who found the unification scientifically compelling; this positive signal is what carried the paper.

---

These calibration exercises should give you a concrete anchor for what each rating level looks like in practice. When in doubt, ask: "What would a well-informed reviewer with no conflicts give this paper based on the standards documented in this skill file?" Apply that standard consistently.
