# Skill File: Evaluating 3D Vision Research Papers

**Topic:** 3d_vision
**Based on:** 1,235 papers (906 accepted, 73.4% acceptance rate), ICLR/NeurIPS 2023–2026
**Rating distribution:** mean=4.98, median=5.0, std=1.14, range=[1.33, 8.5]

---

## 1. Topic Overview

### What This Area Covers

The 3D vision area is broad and encompasses:

- **Novel view synthesis (NVS):** Generating new camera views of a scene from sparse or single inputs. Key representations: NeRF (Neural Radiance Fields), 3D Gaussian Splatting (3DGS), triplane representations.
- **3D reconstruction:** Recovering geometry and appearance from images. Includes feed-forward large reconstruction models (LRM-style), MVS, SLAM, monocular/stereo depth estimation.
- **3D generation:** Text-to-3D, image-to-3D, score distillation sampling (SDS), diffusion-based 3D generation. Representations: NeRF, 3DGS, meshes, point clouds, triplanes.
- **4D / dynamic scene understanding:** Dynamic NeRF, deformable fields, non-rigid reconstruction, part discovery, tracking.
- **3D object understanding:** Point cloud classification/segmentation, shape analysis, 3D detection, part segmentation.
- **3D scene understanding:** Indoor/outdoor 3D detection, occupancy estimation, semantic 3D reconstruction.
- **Human-centric 3D:** Body/face/hand reconstruction, pose estimation, motion capture, talking head generation.
- **Specialized 3D:** Medical imaging (CT/MRI), molecular 3D generation, LiDAR processing.

### Current State of the Art (as of 2025–2026)

The field is dominated by a few paradigm shifts:

1. **3D Gaussian Splatting (3DGS)** has become the dominant real-time representation, surpassing NeRF-based methods in speed. Papers that improve, extend, or apply 3DGS are the most common in the dataset.
2. **Feed-forward large reconstruction models (LRM, GS-LRM, GRM)** demonstrate that scaling transformers + large 3D datasets (Objaverse, MVImgNet) enables single-pass image-to-3D.
3. **Diffusion-based 3D generation** (DreamFusion/SDS, multi-view diffusion models like MVDream, Zero123, SyncDreamer) is the standard pipeline for text/image-to-3D.
4. **Pose-free reconstruction** (DUST3R, MAST3R, Splatt3R, MASt3R) has emerged as a strong direction removing dependency on camera poses.
5. **Large-scale 3D datasets** (Objaverse ~800K objects, DL3DV, ScanNet) are expected to be used for training generalizable models.

### Score Distribution and Acceptance Bar

| Score Range | Label | Count (reviews) | Interpretation |
|-------------|-------|-----------------|----------------|
| 8–10 | Excellent | 50 papers | Oral/Spotlight, clear new direction |
| 6–7 | Good | 1,096 reviews | Solid poster accept |
| 4–5 | Borderline | 2,609 reviews | Most submissions land here |
| 1–3 | Low | 686 reviews | Clear reject |

**The acceptance threshold** is approximately 5–6. A paper scoring 5 from all reviewers is borderline and will often be rejected. A paper averaging 6 from all reviewers is a likely accept (poster). Papers averaging 7+ are spotlight/oral candidates.

**Key insight from the data:** The standard deviation is 1.14, meaning reviewer disagreement is common. Many borderline papers get scores like [3, 5, 6, 6] or [5, 5, 6, 8]. The presence of a strong advocate (score ≥ 8) often tips borderline papers to acceptance.

---

## 2. What Reviewers Praise (with Real Examples)

### 2.1 Genuine Novelty and First-of-Kind Results

The single most praised quality (1,026 uses of "novel" in strengths). But reviewers distinguish **genuine novelty** from claimed novelty.

**What counts as genuinely novel:**
- Being the first to demonstrate a capability at scale (e.g., LRM being "the first *large-scale* single-view 3D reconstruction method" — Reviewer 1 on LRM)
- A conceptually new combination that enables something previously impossible
- Showing that a previously "impossible" approach actually works

**From LRM reviews (rating 8.5, Oral):**
> "To my knowledge, this paper is the first work showing the scaling ability of transformers on novel view synthesis."

> "The paper designs a 3D foundation model for reconstruction, which intrinsically establishes a 3D prior knowledge model. It fills the gap between 2D and 3D foundation generative model. This contribution makes this work not only achieve SOTA 3D generation result, but advances the 3D deep learning. It has potential to influence the 3D learning community as BERT for NLP, or DALLE2/Muse for 2D generation."

### 2.2 Comprehensive Ablation Studies

Ablations appear 745x in strengths and 1,131x in weaknesses (i.e., frequently missing). When present, they are strongly praised.

**From HiSplat (6.0, Poster):**
> "The ablative study seems complete."
> "This paper show the effective ablation study, comparing the impact of different modules on the performance."

**From MovingParts (8.0, Spotlight):**
Reviewers specifically requested ablations of cycle consistency on features vs. positions, SE(3) vs. offsets, and loss term ablations — implying these are standard expectations.

**What makes a good ablation:**
- Each major module tested independently
- Key design choices justified (why this architecture over alternatives)
- Loss terms ablated individually
- Hyperparameter sensitivity tested

### 2.3 Strong Baselines and Comparisons

Baseline coverage is mentioned 644x in strengths, 1,590x in weaknesses (the #1 weakness). Praised papers:
- Include recent SOTA methods (within 1–2 years)
- Test on the same training data as baselines for fair comparison
- Use the same evaluation splits as established benchmarks

**From Grendel/Scaling 3DGS (8.0, Oral):**
> "Sufficient experimental validation on effectiveness of the method."
> "This paper conducts extensive experiments across various scales of scenes under different experiment settings."

### 2.4 Efficiency and Practicality

Single-pass inference (no per-scene optimization) is consistently praised:

**From LRM (8.5):**
> "The method is extremely efficient during inference as it only requires a single forward pass, unlike many generative models, e.g. score-based generative models and/or optimization-based methods."

**From No Pose, No Problem (8.0, Oral):**
> "The proposed method is simple and easy to understand."
> "A simple VIT approach is competitive to pretrained ViT backbones from Dust3r, and Mast3r when overlap is minimal."

### 2.5 Well-Written, Clear Presentation

Appears as "well-written" (470x) and "well written" (215x) in strengths. Reviewers specifically value:
- Clear motivation and problem formulation
- Logical flow from problem to method to experiments
- Sufficient implementation details for reproducibility
- Good figures that illustrate key ideas

**From No Pose, No Problem (8.0):**
> "The paper is very well written and easy to follow."

**From Grendel (8.0):**
> "The paper is well-written and easy to understand."

### 2.6 Real-World Generalization

Papers that go beyond synthetic benchmarks to show real-world performance are strongly praised.

**From LRM (8.5):**
> "Qualitative results on images from different source show the superior performance of the proposed LRM."
(Objaverse synthetic + MVImgNet real-world captures + generative model outputs)

**From No Pose, No Problem (8.0):**
> "Good generalization capability on in-the-wild data."

### 2.7 Scalability

Scalability appears 114x in strengths. For reconstruction and generation models, showing behavior as data/model scale increases is valued.

**From LRM (8.5):**
> "The paper figures out a learnable positional encoding to generalize NeRF generation conditioning on 2d image features. The architecture pave the way for other 3D generative models to scale up."

---

## 3. What Reviewers Criticize (with Real Examples)

### 3.1 Missing Baselines (The #1 Criticism)

Baselines appear 1,590x in weaknesses — by far the most common criticism. This is fatal for papers.

**From Grendel (8.0, still accepted):**
> "Baselines are missing in the current version. It is a good system work to me. However, over-claiming something in the paper won't make it a better work. I would like to see a fair comparison of the method to more baselines (original 3DGS, VastGaussian, CityGaussian, DOGS, etc.) and raise my score if they do so."

**From HiSplat (6.0):**
> "Some related methods are missed in the discussion, e.g., FreeSplat and Splatt3R. Especially, FreeSplat also uses a cost-volume-based structure to estimate the depth and then Gaussians with multi-scale strategy."

**Key lesson:** Reviewers know the subfield. Missing any concurrent or closely related work is noticed and criticized harshly.

### 3.2 Overclaiming SOTA Without Proper Comparison

A common and damaging mistake — claiming state-of-the-art when the comparison is incomplete or unfair.

**From Grendel (8.0):**
> "The authors also claimed that 'None of these systems can consider a full large-scale scene directly and achieve the same quality as ours'. This is ***over-claimed and does not respect existing works since they did not compare to any of these methods*** but only tried different configurations of their Grendel methods."

**From Self-Supervised Stereo Odometry (2.75, Rejected):**
> "The authors assert that their method achieves state-of-the-art performance in visual odometry. However, a closer examination of Table 2 reveals that Yang et al. (2020) outperforms the proposed method by a significant margin, raising concerns about the veracity of this statement."

### 3.3 Limited Novelty / Incremental Contributions

"Incremental" appears 200x in weaknesses, "limited novelty" 96x.

**From LISA (4.5, Rejected):**
> "The main claim of this paper is to adapt an image diffusion model for direct 3D generation. However, this idea is not new, as [PI3D, HexaGen3D] and many other works have tried to adapt stable diffusion for direct triplane generation. There is a lack of discussion and comparisons with them."

> "The novelty is incremental given the recent surge of papers combining 2D diffusion models with 3D generation."

**From Level-Set Parameters (4.5, Rejected):**
> "I feel it is too ambitious to propose a new data modality. If the focus of the paper is on a new data modality, I would expect more versatile shape analysis beyond just classification, pose estimation, and retrieval... I would expect more groundbreaking improvements, but the enhancements in classification and retrieval are not significant."

### 3.4 Evaluation Only on Synthetic / Simple Datasets

**From MovingParts (8.0 — still accepted but heavily criticized):**
> "The experimental evaluation is provided on simple synthetic datasets where the amount of deformation is a bit limited... No full evaluation on real monocular image sequences."

> "I am concerned that video results are only shown for the synthetic D-NeRF dataset, which is effectively a multi-view dataset... I'd much prefer to see the video results of the real-world monocular scenes."

**From Level-Set Parameters (4.5, Rejected):**
> "The experimental results are presented on relatively simple datasets, such as ModelNet40 and ShapeNet. It would be valuable to evaluate the method on more complex, large-scale datasets like Objaverse."

**Key lesson:** ModelNet40, ShapeNet, D-NeRF are now considered easy/saturated benchmarks. Modern papers must evaluate on harder, real-world data.

### 3.5 Missing Ablations

Absent ablations is one of the most-cited weaknesses (1,131x). Reviewers flag:
- No comparison of proposed modules vs. simpler alternatives
- No analysis of why specific design choices were made
- Missing loss ablations
- Hyperparameters not justified

**From MovingParts (8.0) — reviewer who initially leaned reject:**
> "There appear to be no ablations. For example, applying the cycle consistency loss on features vs. positions. Or using SE(3) vs. offsets. And loss ablations, e.g.: Why is the per-point color loss useful? What happens without the total variation loss?"

### 3.6 Missing LPIPS in NVS Papers

In novel view synthesis, reporting only PSNR and SSIM without LPIPS is consistently flagged.

**From MovingParts (8.0):**
> "Please add LPIPS scores everywhere. It's standard for NeRF papers (see e.g. the original NeRF paper) and PSNR and SSIM are quite similar, while LPIPS is much more perceptual."

### 3.7 Missing Related Work / No Discussion of Prior Art

**From No Pose, No Problem (8.0 — one reviewer gave 8, another complained):**
> "Basic literatures in this field are not discussed and the claimed novelty have already been studied in prior works... PF-LRM and LEAP are the two earliest works for pose-free reconstruction, but none of them are mentioned. Almost all claimed novelty of the submission... have already been studied in these two works."

**This is a critical failure mode:** In a fast-moving field like 3D vision, a paper that omits discussion of 3–5 closely related works risks rejection or major score reduction.

### 3.8 Unfair Comparisons

**From No Pose, No Problem (8.0 — reviewer with concerns):**
> "The proposed method is trained on a joint set of RealEstate10K, DL3DV and ACID, while all the baselines are trained on a different training dataset. Moreover, the model uses the weight initialization of models trained on large dataset (MAST3R/DUST3R/Croco)."

Reviewers expect: same training data split as baselines, or explicit analysis of the advantage from extra data/initialization.

### 3.9 Computational Cost Not Reported

**From Level-Set Parameters (4.5, Rejected):**
> "The running time is not fully reported. It is only mentioned in the end of Sec. 5 that it takes 50 seconds for registration, which is clearly slow."

**From HiSplat (6.0):**
> "The hierarchical representations appear to be memory-intensive and computationally inefficient. It is recommended that the paper discusses the implications for memory, FLOPs, and inference time."

### 3.10 Poor Writing Quality

Writing is mentioned 470x in strengths (when good) and flagged heavily when poor.

**From Self-Supervised Stereo Odometry (2.75, Rejected):**
> "Use the incorrect template, should be ICLR 2024 instead of ICLR 2023."
> "An incomplete reference"
(Using the wrong year's template signals an incomplete submission — immediate red flag.)

**From LISA (4.5, Rejected):**
> "Too many typos in writing. e.g. Figure 4(b) in line 283-284. where is Fig 4b? ; line 269, Tough-> Though;..."
> "The citation formats in this paper are wrong. All citations lack '()'. It should use \\citet or \\citep instead of \\cite."

**Citation format errors** (using `\cite` instead of `\citep`) appear repeatedly across borderline and low-scored papers. This is a surprisingly common error that signals carelessness.

---

## 4. Required Baselines & Metrics

### 4.1 Novel View Synthesis (NeRF / Gaussian Splatting)

**Metrics (ALL required):**
- PSNR (higher is better)
- SSIM (higher is better)
- LPIPS (lower is better) — **missing LPIPS is a common criticism**

**Required baselines for scene-level NVS:**
- NeRF (Mildenhall et al., 2020) — original baseline
- Instant-NGP — fast NeRF
- 3DGS (Kerbl et al., 2023) — now the primary baseline for all splatting papers
- For sparse-view: MVSplat, pixelSplat, Splatt3R
- For dynamic: D-NeRF, HyperNeRF, Nerfies

**Required baselines for object-level NVS / reconstruction:**
- LRM, GS-LRM, GRM — large reconstruction models
- Zero123, Zero123++ — image-to-3D single view
- DreamGaussian — efficient 3D generation

**Standard datasets:**
- Mip-NeRF 360, Tanks-and-Temples, Deep Blending (for scene NVS)
- RealEstate10K, ACID (for generalizable indoor NVS)
- DTU (for sparse-view reconstruction generalization testing)
- ShapeNet, Objaverse (for object-level)

### 4.2 3D Reconstruction / Point Cloud

**Metrics:**
- Chamfer Distance (CD) — geometry quality
- F-score at multiple thresholds (1%, 2%)
- For depth: AbsRel, SqRel, RMSE, δ < 1.25

**Required baselines:**
- PointNet, PointNet++ — point cloud baselines (even if old, often required as lower bound)
- DGCNN, VN-DGCNN — for rotation-equivariant tasks
- DUST3R, MAST3R — for pose estimation and reconstruction
- CasMVSNet, TransMVSNet — for multi-view stereo

**Standard datasets:**
- ModelNet40 — classification (now considered easy, augment with harder data)
- ShapeNet — shape analysis
- ScanNet, NYU-Depth v2 — indoor reconstruction
- KITTI, Waymo — autonomous driving

### 4.3 3D Generation (Text/Image-to-3D)

**Metrics:**
- FID (Fréchet Inception Distance) — visual quality
- CLIP Score — text-image alignment
- PSNR/SSIM/LPIPS for comparison with GT when available
- User study (when ground truth unavailable)

**Required baselines:**
- DreamFusion / SDS-based methods
- ProlificDreamer, Magic3D — high-quality text-to-3D
- DreamGaussian — efficient object generation
- LGM, GRM — feed-forward generation
- MVDream, SyncDreamer — multi-view diffusion
- For image-to-3D: Zero123, One-2-3-45, InstantMesh

### 4.4 3D Detection / LiDAR

**Metrics:**
- mAP (mean Average Precision) at IoU thresholds (0.25, 0.5)
- For outdoor: nuScenes NDS, KITTI mAP

**Required baselines:**
- VoxelNet, PointPillars, CenterPoint — 3D detection baselines
- BEVFusion, TransFusion — multimodal fusion
- State-of-the-art on leaderboard at submission time

---

## 5. Common Technical Pitfalls

### 5.1 The "D-NeRF Problem" (Synthetic-as-Real Confusion)

D-NeRF dataset is widely cited as "monocular dynamic scenes" but is actually quasi-multi-view (from Gao et al., 2022 "Monocular Dynamic View Synthesis: A Reality Check"). Papers claiming "monocular" evaluation but only testing on D-NeRF will be called out.

**Red flag:** "We evaluate on D-NeRF dataset for monocular reconstruction."
**Correct approach:** Evaluate on HyperNeRF (truly monocular), or real-world captures, in addition to D-NeRF.

### 5.2 Stereo vs. Monocular Unfair Comparison

Comparing stereo depth estimation methods against monocular baselines and claiming SOTA is a critical error.

**From Self-Supervised Stereo Odometry (2.75, Rejected):**
> "The proposed approach (Ours) in Table 4 is the top performer, but this is expected, as it is the only work using stereo cameras. Stereo imagery considerably simplifies depth prediction in terms of accuracy, robustness and removes the ill-posed aspect of monocular approaches."

### 5.3 Training Data Advantage

Using more training data than baselines and claiming better performance. Reviewers expect:
- Same-data ablation (train proposed method on same data as baselines)
- Explicit analysis: "how much does extra data contribute?"
- Fair comparison table separating training data differences

### 5.4 Architecture Complexity Without Efficiency Analysis

Complex multi-stage models (multiple encoders, decoders, cross-attention modules) need:
- FLOPs comparison with baselines
- Memory (GPU RAM) during training and inference
- Inference time (milliseconds per frame/scene)
- Training time (GPU-hours)

### 5.5 Ignoring the Deterministic vs. Generative Trade-off in Image-to-3D

For image-to-3D tasks: deterministic (regression) vs. generative (sampling) approaches have different properties. Reviewers expect explicit discussion.

**From LRM (8.5) — even excellent papers are asked this:**
> "This LRM model actually turns the image-to-3D into a deterministic predicting task, which alleviates the ill-pose nature of the task. Does the author think the results are just 'fitting' to the training distribution rather than actually predicting / learning a 3D distribution?"

### 5.6 Uncalibrated Claims About "Non-Rigid" vs. "Piecewise Rigid"

In dynamic scene reconstruction, claiming "non-rigid" when the method only handles "piecewise rigid" (articulated) motion is called out.

**From MovingParts (8.0):**
> "The proposed method focuses on scenarios using a monocular moving camera... the type of deformation to be considered is a bit limited, as just piecewise rigid deformations are possible. In fact, this can be observed in the estimation of groups."

### 5.7 Missing Code Release / Reproducibility

Reproducibility appears 112x in strengths and 128x in weaknesses. Code release is praised; missing implementation details are consistently flagged.

**Red flags:**
- "The number of heads in multi-head attention" not specified
- Hyperparameters not reported
- Training infrastructure not described (GPU count, time)

### 5.8 Wrong Template or Incomplete Submission

Using the wrong conference year template (ICLR 2023 vs. 2024), incomplete references, or missing sections (no conclusion, no limitations) signal an incomplete submission and lead to low scores from reviewers.

**From Self-Supervised Stereo Odometry (2.75, Rejected):**
> "Use the incorrect template, should be ICLR 2024 instead of ICLR 2023." (One reviewer gave a 1/strong reject partly because of this)

### 5.9 The "Related but Missing" Problem in Fast-Moving Fields

In 3D vision, new papers appear on arXiv weekly. Reviewers expect papers to acknowledge closely related concurrent work. Missing 2–3 directly related works is a strong signal of inadequate literature review.

**Critical recent works often expected but missed:**
- DUST3R → MAST3R → Splatt3R (pose-free reconstruction progression)
- LRM → GS-LRM → GRM (large reconstruction model progression)
- 3DGS → various 3DGS extensions (VastGaussian, CityGaussian, RetinaGS, DOGS)
- Zero123 → Zero123++ → One-2-3-45 → InstantMesh (image-to-3D progression)

---

## 6. Scoring Rubric for This Topic

### Score 1–3: Strong Reject / Poor Paper

**Profile:**
- Results are worse than baselines (on the paper's own tables)
- Minimal or no genuine novelty (combination of existing components without insight)
- Incomplete submission (missing sections, wrong template, broken references)
- Claims of SOTA that are demonstrably false upon inspection
- Core technical contribution unclear or not differentiated from prior work

**Real example — Self-Supervised Stereo Odometry (rating 2.75, Rejected):**
- 3 out of 4 reviewers gave 1–3
- Results in Tables 2 and 3 are worse than prior work
- Used wrong year template (ICLR 2023 instead of 2024)
- Incomplete references
- Core contribution (3D geometric constraint) not clearly differentiated from Mahjourian et al. 2018
- Reviewer quote: "The paper looks incomplete. I hope that the authors can significantly revise the paper."

**What to look for:**
- Tables where "Ours" rows are below baselines
- Absence of ablation studies
- Vague motivation ("we propose X to improve Y" without explaining why X is the right approach)
- Related work section that doesn't acknowledge closest competitors

### Score 4–5: Borderline / Weak Paper

**Profile:**
- Some novelty but incremental or poorly differentiated from prior work
- Adequate experiments but missing 2–3 important baselines
- Missing LPIPS, or evaluation only on saturated benchmarks
- Writing issues (typos, citation format errors, unclear sections)
- Missing ablations for key design choices
- May show improvement but on simple/synthetic datasets only

**Real example — LISA: Lightweight Image Splats Adaptation (rating 4.5, Rejected):**
- Scores: [5, 5, 5, 3]
- Technically functional but crowded space (many similar works not cited)
- Reviewer: "The novelty is incremental given the recent surge of papers combining 2D diffusion models with 3D generation"
- Reviewer: "Only experiments on MVSDream is provided" — baselines insufficient
- Quality issues in generated results (albedo entangled with shadows)
- Missing FID/CLIP comparisons with LGM and other SOTA

**Real example — Level-Set Parameters (rating 4.5, Rejected):**
- Scores: [3, 5, 5, 5]
- Interesting idea (neural parameters as data representation) but poorly executed
- Evaluated only on ModelNet40/ShapeNet (saturated benchmarks)
- No evaluation on modern datasets (Objaverse)
- Running time: 50 seconds for registration — clearly slow without justification
- Reviewer: "The motivation of this submission is vague."

**What to look for:**
- Paper proposes a method that is a minor variant of existing work
- Experiments cover only easy benchmarks
- Missing discussion of 2+ clearly related concurrent works
- Citation format errors or typos throughout
- Borderline improvement (< 1dB PSNR gain)

### Score 6–7: Solid Accept / Good Paper

**Profile:**
- Clear technical contribution that is well-differentiated from prior work
- Comprehensive experiments including ablations
- Comparison to recent SOTA on standard benchmarks
- PSNR + SSIM + LPIPS all reported (for NVS papers)
- Well-written and easy to follow
- Shows some real-world generalization
- May have minor gaps (1–2 missing baselines, limited dataset variety) but these don't undermine the core claims

**Real example — HiSplat (rating 6.0, Accept Poster):**
- Scores: [6, 6, 6, 6]
- Clear motivation: hierarchical Gaussians for coarse-to-fine reconstruction
- Novel Error Aware Module and Modulating Fusion Module
- Comprehensive ablations
- Weakness: complex architecture, memory/efficiency not analyzed, limited to 2-view inputs
- Missing FreeSplat and Splatt3R discussions

**Real example — MovingParts (rating 8.0, Accept Spotlight) — note: some reviewers gave 6:**
- Weakness reviewers noted: evaluation mainly on D-NeRF synthetic, no LPIPS, limited ablations
- The 8.0 average was achieved because some reviewers focused on the novelty of the approach

**What makes a 6–7:**
- PSNR improvement > 0.5 dB over SOTA on standard benchmarks
- All ablations present
- Discussion of limitations
- Good qualitative results on diverse scenes
- Training and inference time reported

### Score 8–10: Excellent / Top-Tier Paper

**Profile:**
- Opens a genuinely new direction or demonstrates something previously thought impossible
- Comprehensive experiments at scale (large datasets, many baselines)
- Clean architecture with principled design choices
- Clear implications for the broader community
- Combination of strong quantitative and qualitative results
- Reproducibility ensured (code release planned/provided, full implementation details)

**Real example — LRM (rating 8.5, Oral):**
- "The first work showing the scaling ability of transformers on novel view synthesis"
- Trained on 1M+ objects (Objaverse + MVImgNet) using 128 A100 GPUs
- Single forward pass in 5 seconds
- Well-written, comprehensive ablations on design choices
- Even accepted despite lacking quantitative comparison (the qualitative results were so compelling)
- Reviewer: "It has potential to influence the 3D learning community as BERT for NLP"

**Real example — On Scaling Up 3DGS Training / Grendel (rating 8.0, Oral):**
- Enables distributed training of 3DGS across up to 32 GPUs
- Principled hyperparameter scaling law analysis
- Experiments on small-scale (Mip-NeRF360) AND large-scale (MatrixCity, Mega-NeRF) datasets
- Clear practical value for the community

**Key properties of a 9–10 paper:**
- Changes how the field approaches the problem
- Scales to previously intractable settings
- Every major design decision is justified and ablated
- Results are reproducible (code released or detailed implementation provided)
- Strong generalization: works on real-world data not seen during training

---

## 7. Key Papers & Expected Citations

The following papers are frequently cited by reviewers as expected baselines, comparisons, or discussion points. Missing these in related work is a red flag.

### Core 3D Representations
- **NeRF** (Mildenhall et al., 2020, ECCV) — foundational NeRF
- **3D Gaussian Splatting / 3DGS** (Kerbl et al., 2023, SIGGRAPH) — the dominant real-time representation; must be discussed and compared for any NVS paper
- **Instant-NGP** (Müller et al., 2022) — fast NeRF baseline
- **Nerfies / HyperNeRF** — for dynamic/deformable scenes
- **D-NeRF** — for dynamic scene NVS (but note its quasi-multiview limitation)

### Large Reconstruction Models
- **LRM** (Hong et al., 2023, ICLR 2024) — first transformer-based image-to-3D at scale
- **GS-LRM** (Zhang et al., 2024, ECCV) — LRM with 3DGS output
- **GRM** (Xu et al., 2024, ECCV) — another large 3DGS reconstruction model
- **PF-LRM** (Wang et al., 2024, ICLR) — pose-free large reconstruction model
- **LEAP** (Jiang et al., 2024, ICLR) — pose-free sparse-view 3D modeling

### Pose-Free / Sparse-View Reconstruction
- **DUST3R** — dense 3D reconstruction without poses
- **MAST3R** — improvement over DUST3R
- **Splatt3R** — DUST3R + 3DGS for NVS
- **MVSplat** — generalizable 3DGS from 2 views
- **pixelSplat** — another generalizable sparse-view 3DGS

### 3D Generation
- **DreamFusion** — SDS-based text-to-3D
- **ProlificDreamer** — high-quality SDS text-to-3D
- **Zero123 / Zero123++** — single image to 3D via diffusion
- **One-2-3-45** — fast image-to-3D
- **DreamGaussian** — efficient image-to-3DGS
- **MVDream / SyncDreamer** — multi-view diffusion models for 3D generation
- **InstantMesh** — feed-forward mesh generation
- **LGM** — Large multi-view Gaussian model
- **CAT3D** (Gao et al., 2024) — multi-view diffusion for 3D creation
- **Point-E / Shap-E** — text-to-3D point cloud / SDF (now considered weaker baselines)

### Dynamic 3D / 4D
- **D-NeRF** (Pumarola et al., 2021) — canonical framework for dynamic NeRF
- **Nerfies** (Park et al., 2021) — non-rigid NeRF with SE(3) deformations
- **Watch-It-Move** — for articulated object reconstruction comparison
- **DeVRF** (Liu et al., NeurIPS 2022) — cycle consistency for dynamic NeRF

### Point Cloud Analysis
- **PointNet** (Qi et al., 2017) — foundational point cloud network
- **PointNet++** (Qi et al., 2017) — hierarchical point cloud processing
- **DGCNN** (Wang et al., 2019) — graph-based point cloud
- **VN-DGCNN** (Deng et al., 2021) — rotation-equivariant DGCNN; if you report lower numbers than the original paper, reviewers will notice

### Datasets Commonly Expected
- **Objaverse** (~800K 3D objects) — standard for training generalizable models; if you train on less, justify why
- **MVImgNet** — large-scale real multi-view dataset
- **RealEstate10K / ACID** — standard for indoor scene NVS
- **DL3DV-10K** — large-scale diverse 3D scene dataset
- **ModelNet40 / ShapeNet** — point cloud benchmarks (now easy; augment with harder data)
- **ScanNet / ScanNet++** — indoor 3D understanding
- **KITTI / nuScenes / Waymo** — autonomous driving
- **Mip-NeRF 360 / Tanks-and-Temples / Deep Blending** — outdoor scene NeRF benchmarks

### Large-Scale 3DGS Systems (Often Expected as Baselines)
- **VastGaussian** — large-scale scene reconstruction with 3DGS
- **CityGaussian** — city-scale 3DGS
- **Hierarchical Gaussian / HierarchyGS** — LOD-aware 3DGS
- **DOGS** (Chen and Lee, NeurIPS 2024) — distributed 3DGS training
- **RetinaGS** — alternative distributed 3DGS approach

---

## 8. Reviewer Mental Models and Decision Patterns

### How Scores Are Assigned in Practice

Based on the review data, here is how reviewers calibrate:

**"This deserves a 3":**
- The method doesn't work better than what already exists
- The paper is clearly incomplete (missing sections, wrong template, broken refs)
- Core novelty is absent or indistinguishable from prior work

**"This deserves a 5" (borderline reject):**
- Some interesting ideas but execution is weak
- Important related works not discussed
- Main result holds but on easy/saturated benchmarks only
- Missing critical ablations

**"This deserves a 6" (borderline accept):**
- Clear technical contribution
- Experiments adequate but not comprehensive
- 1–2 missing baselines or missing LPIPS
- Writing could be better but key points are clear
- Reviewer quote: "I still have concerns and would raise my score if they are addressed"

**"This deserves an 8":**
- Novelty is clear and the paper demonstrates something new convincingly
- Strong experiments with ablations
- Well-written
- Has real-world validation
- Even if there are concerns (missing baselines), the core contribution is compelling

### The Rebuttal Pattern

Many 3D vision papers move from [5, 5, 6, 5] → acceptance after rebuttal by:
1. Adding missing baselines (even qualitative comparisons if time is limited)
2. Adding ablation tables requested by reviewers
3. Clarifying claims and related work
4. Adding LPIPS numbers to NVS tables
5. Providing efficiency analysis (FLOPs, memory, inference time)

Papers that cannot address baseline or dataset gaps in rebuttal (e.g., missing real-world evaluation) often stay rejected.

### Common Reviewer Biases to Be Aware Of

1. **Benchmark familiarity bias:** Reviewers strongly weight performance on the benchmark they know best. For 3DGS papers: Mip-NeRF 360. For sparse-view: RealEstate10K. For dynamic: HyperNeRF.
2. **Novelty-vs-thoroughness tension:** Some reviewers value "first to try X" even if experiments are incomplete. Others require comprehensive experiments first. In the dataset, LRM was accepted with weak quantitative comparison — a rare exception.
3. **Concurrent work leniency:** If a missing related work is truly concurrent (within 3 months on arXiv), reviewers are generally lenient. But for works 6+ months old, ignoring them is a red flag.
4. **System paper skepticism:** Papers that are primarily engineering contributions (e.g., distributed training) face skepticism about "algorithmic novelty" even if the practical contribution is significant. Address this head-on in the paper.

---

## 9. Sub-Topic Specific Notes

### For Gaussian Splatting Papers
- 3DGS (Kerbl et al., 2023) is the required baseline — everything is compared to vanilla 3DGS
- For sparse-view 3DGS: MVSplat and pixelSplat are required baselines
- For large-scale 3DGS: VastGaussian, CityGaussian, HierarchyGS must be discussed
- For dynamic 3DGS: 4D-GS, Deformable 3DGS must be compared
- Report: PSNR, SSIM, LPIPS on Mip-NeRF 360, Tanks-and-Temples, Deep Blending
- Report: training time, number of Gaussians, rendering FPS

### For Image-to-3D / Text-to-3D
- The field moves fast; state-of-the-art changes quarterly
- FID and CLIP Score are required quantitative metrics
- User study is expected when GT is unavailable
- Must discuss: SDS-based vs. feed-forward trade-offs, diversity vs. quality
- Report: generation time (this distinguishes methods practically)

### For Dynamic/4D Reconstruction
- D-NeRF dataset alone is insufficient — must include HyperNeRF or real captures
- Report: PSNR/SSIM/LPIPS on both synthetic and real sequences
- For part discovery/articulation: must show temporal consistency video results, not just still images
- For tracking: quantitative evaluation of correspondence quality, not just visual demos

### For Point Cloud Analysis
- ModelNet40 is saturated; must include ShapeNet-Part, ScanObjectNN, or harder benchmarks
- For rotation-equivariant methods: test under SO(3)/SO(3) and evaluate on ModelNet40-C (corrupted)
- For few-shot: N-way K-shot evaluation protocol must be specified clearly
- If comparing against VN-DGCNN, use the exact same evaluation protocol as the original paper

### For 3D Detection (LiDAR/RGB)
- Dataset: KITTI, Waymo, nuScenes are all required depending on scope
- Metric: mAP at IoU=0.5 for car detection; mAP across categories
- Latency is critical for detection papers — real-time capability (< 100ms) must be discussed

---

## 10. Quick Reference: Red Flags vs. Green Flags

### Red Flags (likely to score 3–5)
- [ ] Results in main table are worse than baselines in some metrics
- [ ] Wrong conference template year
- [ ] Missing LPIPS for NVS papers
- [ ] Evaluation only on ModelNet40 or D-NeRF without harder benchmarks
- [ ] 3+ closely related works not discussed
- [ ] Claims SOTA without comparing to recent (< 1 year) methods
- [ ] No ablation studies
- [ ] No runtime/efficiency analysis for complex methods
- [ ] Citation format errors (`\cite` without parens)
- [ ] Typos in method name, figure references broken
- [ ] Only tested on object-level synthetic data for a scene-level claim
- [ ] Training data advantage not controlled for in comparisons

### Green Flags (likely to score 6–8+)
- [ ] Demonstrates something clearly first-of-kind or at new scale
- [ ] PSNR + SSIM + LPIPS all reported for NVS
- [ ] Comprehensive ablations with a clear table
- [ ] Comparison to ≥ 5 recent SOTA methods on standard benchmarks
- [ ] Zero-shot generalization demonstrated on a held-out dataset
- [ ] Runtime and memory reported
- [ ] Code release announced or provided
- [ ] Real-world (in-the-wild) qualitative results
- [ ] Discussion of limitations is honest and specific
- [ ] Concurrent works acknowledged with discussion of differences
