# Motion Generation: Expert Judge Skill File

*Grounded in 109 papers from ICLR 2024–2026 and NeurIPS 2023–2025. Acceptance rate: 26.6%. Mean reviewer rating: 4.93.*

---

## 1. Topic Overview

### What This Area Covers

Motion generation is a broad field spanning:

1. **Text-to-Motion (T2M)**: Generating 3D human motion sequences from natural language descriptions. The core benchmark is HumanML3D (14,616 motions) and KIT-ML. Dominant approaches: diffusion models (MDM, MLD, MotionDiffuse), masked autoregressive models (T2M-GPT, MoMask), and LLM-based tokenization (MotionGPT).

2. **Music-to-Dance**: Generating choreography synchronized with music. Benchmark: AIST++. Dominant approaches: diffusion (EDGE), GAN-based (Bailando), autoregressive.

3. **Motion Prediction for Autonomous Driving**: Forecasting agent trajectories in traffic scenes. Benchmarks: Argoverse 1 and 2. Metrics: minADE, minFDE, Miss Rate.

4. **Multi-person / Interaction Generation**: Two-person or multi-agent motion, HOI (human-object interaction), human-scene interaction. Emerging benchmarks: InterHuman, CHAIRS, CORE4D.

5. **Speech/Gesture Generation**: Co-speech 3D gesture generation. Benchmark: BEAT2, Trinity.

6. **Motion Capture / Physics**: Pose estimation, physics-based generation, sim-to-real transfer.

7. **Conditional/Controllable Generation**: Joint-level control, trajectory guidance, style transfer, zero-shot editing.

### The Acceptance Landscape

| Score Range | Label | What It Means |
|---|---|---|
| 7.0+ | Strong Accept | Clear novelty, solid theory OR very strong empirics, comprehensive ablations |
| 6.0–6.9 | Accept (borderline) | Novel contributions with minor gaps, competitive results |
| 5.0–5.9 | Borderline | Interesting idea but lacks comparisons, novelty concerns, or evaluation gaps |
| 4.0–4.9 | Borderline Reject | Limited novelty OR poor evaluation OR missing key baselines |
| ≤3.9 | Reject | Severe deficiencies: unfair comparisons, no video demos, trivial contributions |

**Key calibration**: A 5.5 paper (like MotionGPT, NeurIPS 2023) can be accepted if the novelty angle is compelling even with some performance gaps. A 4.0 paper (like Motion Generalist) gets rejected when it's "technically combining text and music modalities, which has been explored a lot" and evaluation relies solely on self-proposed benchmarks.

The acceptance threshold in this domain is genuinely competitive. Papers must both introduce real novelty AND demonstrate it with fair, thorough experiments.

---

## 2. What Reviewers Praise

### 2.1 Novelty That Lands Well

**Novel representation or paradigm shifts:**
- MotionGPT (NeurIPS 2023, rating 5.5, accepted): "This is the first work that explores the application of Large Language Models (LLMs) in the field of text-driven motion generation. The proposed prompt finetuning method further extends the scope of applications by including 10 different tasks."
- Lexical Motion-Language Understanding (ICLR 2025, rating 7.0): "Introducing the lexical representation paradigm to the text-motion domain is novel... Experimental results show remarkable improvements over baseline methods."
- SEPT (ICLR 2024, rating 7.0): "Pre-training and self-supervised learning for the motion prediction task are under-explored areas, and this paper sets a strong benchmark."

**Novel technical mechanisms:**
- Mean Flow Policy (ICLR 2026, rating 7.0): "This is a strong paper that introduces a new formulation for flow matching... Unlike 'hacks', this paper presents a clean reformulation using the ideas of mean-flow to reduce inference time."
- MotionCLR (ICLR 2025, rating 5.5/accepted): "Novel technical contribution in disentangling text-motion correspondence and motion-motion interactions through separate attention mechanisms. Impressive range of editing capabilities achieved without paired editing data."

### 2.2 Evaluation Quality

Reviewers consistently praise:
- **Ablation studies** (the single most praised element—85x in strengths): "Extensive ablation study shows that the three tasks collaborate and yield positive effects." (SEPT)
- **Novel benchmarks with human validation**: "MBench metrics are corroborated by a large-scale human preference study, ensuring their alignment with human judgment." (ViMoGen)
- **Multi-dataset evaluation**: Papers evaluated on both HumanML3D AND KIT-ML get stronger reviews than single-dataset papers.
- **Comprehensive baselines**: "The proposed method ranks top on two widely used leaderboards." (SEPT)

### 2.3 Theory + Empirics Combination

Reviewers explicitly reward papers that have both:
- Mean Flow Policy: "The theoretical analysis is strong... IVC ablation confirms its stabilizing effect."
- "The authors provide rigorous mathematical proofs to justify their framework."

### 2.4 Reproducibility Signals

- Well-written, easy to follow
- Open-source code release or clear intent to release
- Clear implementation details (motion representation, hyperparameters)
- Dataset release alongside paper

### 2.5 Real-World Validation

For physics/robotics papers specifically: "The work directly addresses the pressing challenge of deploying text-based motion generation models on physical humanoid robots." Real-robot experiments are praised but must be quantitative, not just qualitative images.

---

## 3. What Reviewers Criticize

### 3.1 The Baseline Problem (142x cited as weakness)

This is the **#1 criticism** in the dataset. Reviewers expect all directly relevant published methods to be compared:

**Text-to-motion**: Every paper must compare against the current SOTA. As of 2024–2026, expected baselines include MDM, T2M-GPT, MLD, MotionDiffuse, MoMask, ReMoDiffuse. Missing any will be flagged:
- ViMoGen: "This paper lacks key comparison with methods: MotionCraft... FineMoGen... MotionDiffuse both of which are also representative recent approaches."
- Motion Generalist (ICLR 2026, rating 4.0): "Currently, the generated dances show artifacts... there are very limited comparisons and visualizations."

**Specific comparison traps:**
- Comparing your method to 2–3 year old baselines while ignoring newer work: "Three baselines (MDM, T2M-GPT, MotionGPT) are pure motion generators; moreover, they are all relatively **dated baselines**." (Humanoid-R0 reviewer)
- Changing multiple variables simultaneously: "This changes two variables at once: the unlearning algorithm AND the model architecture. Therefore, it is impossible to know how much of the performance gain is due to the algorithm versus the more advanced model." (SafeMo review—a critical structural flaw)

### 3.2 Novelty Concerns (79x cited)

Reviewers sharply distinguish between:
- **Novel mechanisms** vs. **direct application of prior work**
- **Incremental extension** vs. **new paradigm**

Real examples of novelty rejection language:
- SEPT: "The framework presented lacks novelty. Compared to [Traj-MAE, Forecast-MAE], they achieve better performance, but the paper does not give a thorough analysis regarding the difference."
- Motion Generalist: "The main novelty is technically combining text and music modalities, which has been explored a lot. Therefore, the broader impact on the community is unclear."
- Mean Flow Policy (lower-scoring reviewer): "The mean-flow formulation itself is taken directly from prior generative modeling work; this paper mainly applies it to RL. The proposed IVC is conceptually implied by the mean-flow definition."

**How to survive novelty scrutiny**: Clearly articulate what was NOT possible before, provide a detailed comparison table with prior art, and analyze *why* your approach works differently, not just that it does.

### 3.3 Missing Ablations (114x cited as weakness)

Specific patterns that cause reviewer frustration:
- "There are still several aspects of the design choice untouched in the ablation studies. For example, can the masking ratio be scheduled?" (Motion Generalist)
- "The cross-task ablations are missing. Train on text only → test on text; train on music only → test on music." (Motion Generalist)
- No ablation for the core claimed contribution: "It remains unclear how much improvement comes from this representation alone versus the unsupervised 'motion concepts'." (ZNbzdBIWSd review)

### 3.4 Limited Scope / Outdated Datasets

- "Experiments are restricted to small-scale, relatively clean datasets (HumanAct12, UESTC). Using only UESTC (2018) and HumanAct12 (2020) makes the evidence dated." (Multiple reviews for rating=3.0 paper)
- Expected modern datasets for text-to-motion: HumanML3D (minimum), Motion-X (ideal)
- Expected modern datasets for motion prediction: Argoverse 2 (minimum), Waymo or nuScenes ideal

### 3.5 Visualization / Video Demo Failures

This is a domain where qualitative results matter enormously. Reviewers notice:
- No video demos: "For a paper focused on motion quality and deployability, higher-quality motion visualization is essential." (Humanoid-R0, rating 2.0)
- Poor visualization: "The qualitative figures stack too many overlapping SMPL frames, which makes it hard for the readers to evaluate the generated motion details." (Motion Generalist)
- Static images insufficient: "Real-world results lack quantitative numbers... static snapshots do not convey motion smoothness, stability, or transition quality." (Humanoid-R0)
- "No demo videos are provided. Given the limitations of static frame shot figures, it's crucial to provide convincing video demos." (ViMoGen review)

### 3.6 Scalability Concerns (19x cited)

- "The proposed ComMDM is constrained to two persons only. It is hard to scale to multiple persons." (Human Motion Diffusion as Prior)
- "The scope is too narrow. The focus on action-to-motion is inherently limited; demonstrating extension or zero-shot transfer to text-to-motion would make the paper more applicable." (ZNbzdBIWSd review)

### 3.7 Physical Plausibility Gaps

For any method claiming physical realism or sim-to-real transfer:
- Expected: foot contact consistency, penetration rates, bone length stability, velocity/acceleration/jerk smoothness
- "Foot-sliding/skating and low-amplitude/stationary behaviors are acknowledged, but quantitative physics proxies are absent." (SafeMo review)
- "Video demo exhibits extensive artifacts, mostly just being frozen all the way, over smooth, or jittery transitions." (SafeMo review—video quality contradicting claimed improvements)

---

## 4. Required Baselines & Metrics

### 4.1 Text-to-Motion (Core Task)

**Standard datasets:**
- HumanML3D: 14,616 motion-text pairs (22 joints, 20 fps). The minimum required dataset.
- KIT-ML: 3,911 motions. Papers should include both for credibility.
- Motion-X: Larger, more diverse. Increasingly expected in 2025–2026.

**Standard metrics (FrechetMoDiff evaluation):**
| Metric | What It Measures | Direction |
|---|---|---|
| FID (Frechet Inception Distance) | Distribution match quality | Lower is better |
| R-Precision (Top-1/2/3) | Text-motion alignment | Higher is better |
| MM Dist (MultiModal Distance) | Text-motion semantic distance | Lower is better |
| Diversity | Variety of generated motions | Match GT |
| MultiModality | Diversity given same text | Higher is better |

**Required baselines for T2M papers:**
- **Diffusion-based**: MDM (Tevet et al., 2022), MLD (Chen et al., 2023), MotionDiffuse (Zhang et al., 2022)
- **Autoregressive/masked**: T2M-GPT (Zhang et al., 2023), MoMask (Guo et al., 2024)
- **Retrieval-augmented**: ReMoDiffuse (Zhang et al., 2023)
- **LLM-based**: MotionGPT (Jiang et al., 2023) if doing multi-task

### 4.2 Motion Prediction (Autonomous Driving)

**Datasets**: Argoverse 1, Argoverse 2. Waymo Open Dataset, nuScenes increasingly expected.

**Metrics**: minADE@K, minFDE@K, Miss Rate (MR), brier-minFDE. Both validation and test leaderboard submissions valued.

**Required baselines**: MTR (Shi et al., 2022), QCNet (Zhou et al., 2023), Scene Transformer (Ngiam et al., 2022), Wayformer (Nayakanti et al., 2023).

### 4.3 Music-to-Dance

**Datasets**: AIST++ (primary), FINEDANCE (for fine-grained), LODGE.

**Metrics**:
- FID on generated dance (kinematic features)
- Beat Alignment Score (BAS): synchronization with music beats
- Physical Quality: foot skating ratio, penetration rate
- User study: naturalness, music-dance synchronization

**Required baselines**: EDGE (Tseng et al., 2023), Bailando (Siyao et al., 2022), GDANCE, Bailando++ (Siyao et al., 2023).

### 4.4 Multi-Person Interaction

**Datasets**: InterHuman (Liang et al., 2023/InterGen), CHAIRS (Shan et al., 2023), NTU-RGB+D (for action recognition).

**Required baselines**: InterGen (Liang et al., 2023), MDM-based extension, ComMDM (Shafir et al., 2024), RIG.

### 4.5 Speech/Gesture Generation

**Datasets**: BEAT2 (Liu et al., 2023), Trinity, ZEGGS, SHOW.

**Metrics**: FID, BeatAlign, MPJPE, human study naturalness scores.

---

## 5. Common Technical Pitfalls

### 5.1 Motion Representation Underspecification

A surprisingly common and costly error: not specifying the motion representation used.

Reviewer quote: "The paper does not provide details on the underlying motion representation. Is it 3D positions or rotations? If the latter, which representation? What do the 'raw motion vectors' look like?" (FineMoGen review)

Expected: Clear statement of whether using: (a) 3D joint positions, (b) local rotation matrices, (c) 6D rotation representation, (d) SMPL parameters, or (e) VQ-VAE latent tokens. Resolution (FPS), number of joints, body model (SMPL, SMPL-X, skeleton).

### 5.2 VQ-VAE / Tokenization Details Missing

For any autoregressive or masked modeling approach:
- Codebook size, commitment loss weighting
- Whether codebooks are shared per joint/frame or global
- Tokenization stride and reconstruction quality
- "The VQ-VAE component is not described in sufficient detail. Please provide architecture specifics." (Motion Generalist review)

### 5.3 Circular Evaluation

Creating a dataset and then evaluating primarily or exclusively on that dataset:
- "The primary quantitative results are reported on MBench, a benchmark concurrently introduced by the authors. This presents a potential risk that the new data and model may have 'overfit' to the specific evaluation criteria of this new benchmark." (ViMoGen review)
- "Optical MoCap subset selection is optimized using MBench, risking overfitting the training data to the proposed evaluation." (ViMoGen review)

**Fix**: Always compare on established benchmarks first (HumanML3D, KIT-ML), then introduce new benchmark as supplementary.

### 5.4 Physics/RL Reward Hacking

For papers using RL or physical rewards:
- "Training diverges; they manually pick an early checkpoint instead of addressing the root cause, indicating instability." (Humanoid-R0 review)
- Reward signs inconsistency: "The consistency reward is a distance penalty but appears to be added positively in the total reward; the signs seem inconsistent." (Humanoid-R0 review)
- "Ad-hoc reward design: the specific rewards are overly ad-hoc and unlikely to cover all necessary physical scenarios." (Humanoid-R0 review)

### 5.5 Claiming SOTA Without Fair Setting

The Robomimic/OGBench saturation issue: if baselines already perform well, claiming improvements is weak unless you address a specific known limitation.

"The reported environments seem 'saturated' in that the baselines already perform pretty well. It would have been nice to look at more complex benchmarks." (Mean Flow Policy reviewer)

### 5.6 Self-Supervised Pretraining Pitfalls

For SSL pretraining papers:
- Must show ablation of each pretraining task independently
- Must clarify if test set is used for pretraining (can be an unfair advantage)
- Must compare carefully against prior SSL methods, not just supervised baselines
- "The paper mentions using the test set (unlabeled wrt the actual task) for self-supervised learning... Using the unlabelled part of this dataset for pre-training could be giving the model an unfair advantage." (SEPT review)

### 5.7 Missing Failure Analysis

Reviewers repeatedly note the absence of failure cases:
- "The lack of failure analysis is a bit concerning. It is difficult to gauge how well the model learns the relationship between motion and language." (MotionGPT review)
- "Failure cases or limitations are not discussed." (Motion Generalist review)
- Including failure cases actually increases credibility and reviewer confidence.

### 5.8 Dataset Quality for New Contributions

When contributing a new dataset:
- Must provide quality statistics and filtering pipeline details
- Must show examples in paper or supplementary
- Must address inter-annotator agreement or automated quality checks
- Must detail licensing and provenance
- "The SafeMoEngine both labels and rewrites prompts... Without human QC, leakage and confirmation bias are likely." (SafeMo review)
- "Key aspects such as music clip length, diversity, coverage... are not thoroughly detailed." (Motion Generalist review)

---

## 6. Scoring Rubric for Motion Generation

### 3/10 Paper (Certain Reject)

**Characteristics:**
- Addresses a problem with no clear motivation beyond "existing methods are imperfect"
- Comparisons are unfair: different backbones, outdated baselines only, or evaluation only on self-proposed metrics
- No video demos or qualitative results are weak/misleading
- Reward hacking or training instability not addressed
- Claims SOTA but R-Precision is ~0.1 when published methods achieve ~0.5–0.7

**Real Example**: Humanoid-R0 (rating 2.0): Proposes RL fine-tuning of text-to-motion model for physical deployment. Despite addressing a real problem, it: (1) compares only to dated baselines (MDM, T2M-GPT, MotionGPT) while missing RobotMDM, ReinDiffuse, RLPF; (2) missing comparisons to "recent RL-augmented text-to-motion methods"; (3) "supplementary material is not uploaded" so no videos; (4) "training diverges; they manually pick an early checkpoint instead of addressing the root cause"; (5) "R-Precision (Top 1) of ~0.1 seems unusually low."

**Another Real Example**: ZNbzdBIWSd (rating 3.0): Motion refinement on HumanAct12 and UESTC only—"UESTC (2018) and HumanAct12 (2020) makes the evidence dated"—no generalization to text-to-motion, "scope is too narrow."

### 5/10 Paper (Borderline)

**Characteristics:**
- Clear problem motivation and reasonable approach
- Results on standard benchmarks but lags behind SoTA on some key metrics
- Missing 1–2 key baselines (flagged but not fatal)
- Solid ablation but limited to one dataset
- Novel formulation but builds heavily on concurrent/prior work without clearly articulating the gap

**Real Example**: MotionGPT (NeurIPS 2023, rating 5.5, accepted): "MotionGPT exhibits poorer performance in the crucial text-to-motion task, with a significant gap in FID metrics compared to T2M-GPT." Despite this, accepted because: novel paradigm (LLM for motion), 10 supported tasks, well-written, and "the first work that explores the application of LLMs in the field."

**Real Example**: Human Motion Diffusion as Generative Prior (ICLR 2024, rating 6.0, accepted): Three composition techniques (DoubleTake, ComMDM, DiffusionBlending). Accepted borderline because methods work well without extra data, but reviewers note: "technically, there are not much contributions," "constrained to two persons only," "lacks comparative experiments with InterGen."

**Real Example**: MotionCLR (ICLR 2025, rating 5.5, accepted): Novel training-free editing via attention. Accepted despite "the cross-attention control method comes from an existing text-to-image editing paper, Prompt-to-Prompt" and "evaluation relies too heavily on qualitative results"—the broad capabilities enabled without paired data was the saving grace.

### 7/10 Paper (Solid Accept)

**Characteristics:**
- Clearly novel contribution not achievable by prior methods
- Evaluated on both HumanML3D and KIT-ML (or domain-equivalent multi-benchmark)
- Beats SoTA on at least 2–3 key metrics
- Ablation validates each proposed component
- Well-written with clear figures and video demos
- May have minor gaps (limited environments, some missing baselines) but these are minor

**Real Example**: SEPT (ICLR 2024, rating 7.0, accepted): "Pre-training and self-supervised learning for the motion prediction task are under-explored areas. Achieves state-of-the-art on two of the largest datasets. Extensive ablation shows each task contributes." Weaknesses noted (limited novelty vs. Traj-MAE) but the SoTA results and clean architecture carried it.

**Real Example**: Lexical Motion-Language (ICLR 2025, rating 7.0, accepted): Novel lexical representation paradigm with multi-phase training. "Experimental results show remarkable improvements... comprehensive experiments across multiple public datasets." Well-written, novel representation approach.

**Real Example**: FineMoGen (NeurIPS 2023, rating 5.5, accepted but lower tier): This shows that 7/10 quality requires MORE than FineMoGen's level—FineMoGen has motion artifacts, limited presentation, and only 5.5. A genuine 7/10 would not have artifacts in the demo video.

### 9/10 Paper (Exceptional)

**Characteristics:**
- Paradigm-shifting: enables capabilities that were fundamentally not possible before
- Strong theory with proofs OR very large-scale empirical validation
- Multi-task evaluation across diverse benchmarks
- Clean, reproducible, with code release
- Human perceptual study with adequate sample sizes (50+ participants)
- Video demos showing diverse and complex motions
- Ablation covers every design choice

**What would earn this in motion generation:**
- A method that genuinely unifies multiple conditioning modalities (text, music, speech, video) with SoTA on all, plus a new high-quality dataset
- A physically-based approach with real-robot deployment AND quantitative metrics across many trials
- A foundational model that achieves SoTA across 5+ benchmarks simultaneously and releases a large-scale pre-trained model
- Novel theoretical framing (like mean flows) with clear proofs AND strong empirical results on complex benchmarks

Note: No paper in this 109-paper corpus achieved a rating of 8+ average. The highest was 7.5 (Co3Gesture, no reviews available). Papers reaching 7.0+ are the top ~8% of submissions.

---

## 7. Key Papers & Expected Citations

### 7.1 Foundational Text-to-Motion Papers (Expected Knowledge)

Papers that reviewers implicitly or explicitly expect to know:

**MDM / Motion Diffusion Model** (Tevet et al., 2022)
- The baseline diffusion approach. Any diffusion-based T2M paper must compare.
- Sets the standard for diversity, FID evaluation on HumanML3D.

**T2M-GPT** (Zhang et al., 2023)
- Strong autoregressive baseline. Often beats diffusion approaches on FID.
- "MotionGPT exhibits poorer performance in the crucial text-to-motion task, with a significant gap in FID metrics compared to T2M-GPT." (NeurIPS 2023 reviewer)

**MLD (Motion Latent Diffusion)** (Chen et al., 2023)
- Latent diffusion for motion. Expected comparison in all T2M papers.

**MoMask** (Guo et al., 2024)
- Masked motion generation. Strong baseline expected for masked approaches.

**ReMoDiffuse** (Zhang et al., 2023)
- Retrieval-augmented diffusion. Expected when claiming SoTA.

**MotionDiffuse** (Zhang et al., 2022)
- Early diffusion for T2M with fine-grained control. Expected baseline.

**InterGen** (Liang et al., 2023)
- Two-person interaction generation. Expected for any multi-person paper.
- "Dual-person motion generation lacks comparative experiments, for example, with InterGen." (MDM as Prior reviewer)

### 7.2 Key Dataset Papers

**HumanML3D** (Guo et al., 2022)
- The HumanML3D dataset paper. Defines the standard evaluation protocol.
- "The evaluation pipeline is based on the MotionDiffuse evaluation." Must use their feature extractor.

**KIT-ML** (Plappert et al., 2016)
- Older but still expected. Papers on single dataset get penalized.

**Motion-X** (Lin et al., 2023)
- Large-scale expressive whole-body dataset. Increasingly expected as of 2024–2025.
- "Could test more zero-shot examples to validate... taking a sample from Motion-X." (reviewer suggestion)

**AMASS** (Mahmood et al., 2019)
- Large-scale motion capture. Expected for physics-based papers and generalization.

**AIST++** (Li et al., 2021)
- Standard music-to-dance benchmark. Required for dance papers.

### 7.3 Motion Prediction (Autonomous Driving) Expected Citations

**Scene Transformer** (Ngiam et al., 2022 ICLR)
- Foundational architecture. Expected baseline.

**QCNet** (Zhou et al., 2023)
- Strong baseline. Often cited for comparison.

**Traj-MAE, Forecast-MAE** (ICCV 2023)
- SSL pretraining baselines. Required for SSL motion prediction papers.
- "The three self-supervised tasks presented appear to be inspired or derived from these preceding studies." (SEPT reviewer)

**MTR (Motion Transformer)** (Shi et al., NeurIPS 2022)
- Standard baseline for Waymo. Expected citation.

### 7.4 Physics and Controllable Generation

**PhysDiff** (Yuan et al., 2023)
- Physics-based motion generation. Required comparison for any physically-aware approach.
- "What is the difference between the proposed RL fine-tuning and existing methods like PhysDiff?" (dance RL reviewer)
- "I also think it would be beneficial to include a comparison with PhysDiff." (Physics dance reviewer)

**EDGE** (Tseng et al., CVPR 2023)
- Editable dance generation from music. Required baseline for dance.

**OmniControl** (from manifest, ICLR)
- Joint-level controllable generation. Expected for fine-grained control papers.

**FineMoGen** (Zhang et al., NeurIPS 2023)
- Fine-grained spatio-temporal control. Expected baseline for controllable generation.

**TEACH** (Athanasiou et al., 2022)
- Long sequence generation baseline.
- "Comparing with TEACH is not very fair... Is it possible to have the same setting?" (MDM as Prior reviewer)

### 7.5 LLM-Based Motion Papers

**MotionGPT** (Jiang et al., NeurIPS 2023)
- First LLM-based T2M. Expected when claiming LLM integration.

**TMR** (Petrovich et al., 2023)
- Text-motion retrieval. TMR similarity (TMR-sim) used as an evaluation metric.
- "The TMR metric somewhat makes sense for evaluating motion emphasizing/erasing." (MotionCLR reviewer)

### 7.6 What Metric Benchmarks Reviewers Cite

**"What is the Best Automated Metric for Text-to-Motion Generation?"** (SIGGRAPH 2023)
- Reviewers cite this when standard metrics seem insufficient.
- "Evaluate perceptual and physical plausibility... Relevant references: What is the Best Automated Metric for Text-to-Motion Generation?" (ZNbzdBIWSd review)

**Pose-NDF** (Tiwari et al., ECCV 2022)
- For evaluating physical plausibility via human pose manifolds.

---

## 8. Rapid Evaluation Checklist

Use this when evaluating a motion generation paper:

### Novelty Check
- [ ] Is the core contribution clearly different from MDM, T2M-GPT, MoMask, and other established methods?
- [ ] Does the paper clearly state what was NOT possible before?
- [ ] Is the novelty a new mechanism (strong) or just applying existing techniques to a new domain (weak)?
- [ ] If using flow matching / diffusion, is there a clear reason not to use existing methods?

### Baseline Check
- [ ] Does the paper compare against at least 4–5 current SOTA methods?
- [ ] Are the baselines contemporary (within 1–2 years)?
- [ ] Is the evaluation on HumanML3D? On KIT-ML too?
- [ ] If multi-person: does it compare against InterGen?
- [ ] If physics-based: does it compare against PhysDiff?
- [ ] If dance: does it compare against EDGE, Bailando?

### Metric Check
- [ ] FID reported on HumanML3D? (required)
- [ ] R-Precision (Top-1, Top-2, Top-3)?
- [ ] MM Dist and Diversity?
- [ ] MultiModality?
- [ ] Physical metrics if claiming physics (foot contact, penetration)?

### Ablation Check
- [ ] Is each proposed component validated by ablation?
- [ ] Are ablations on the same dataset as main results?
- [ ] Are the ablations meaningful (not just removing everything at once)?

### Qualitative Check
- [ ] Is there a video demo (project page or supplementary)?
- [ ] Are qualitative comparisons provided (not just solo results)?
- [ ] Do the qualitative results NOT contradict the quantitative claims?
- [ ] Are failure cases discussed?

### Reproducibility Check
- [ ] Is the motion representation clearly specified (joints, FPS, body model)?
- [ ] Are implementation details sufficient to reproduce?
- [ ] Is code release planned?

---

## 9. Calibration Notes for Edge Cases

### When Limited Baselines Are Acceptable
- If the method is genuinely the first in a niche subarea (e.g., first safe T2M, first specific interaction type)
- If code/models for relevant baselines are unavailable and authors clearly state this
- If the paper's contribution is a new dataset or benchmark (evaluation focus shifts)

### When Incremental is OK
- If the improvement enables a qualitatively new capability (e.g., training-free editing)
- If the method significantly simplifies the pipeline while matching SoTA
- If the work opens a new research direction with clear future impact

### The Single-Dataset Trap
Papers evaluated on only HumanML3D without KIT-ML consistently receive criticism. KIT-ML is smaller but results must be consistent across both. This is a near-universal expectation by ICLR 2025–2026 reviewers.

### The Video Demo Expectation
Unlike image generation, motion papers MUST provide video demonstrations. A paper without a project page or supplementary video in 2024+ will almost always get a "missing video demo" criticism, regardless of quantitative strength. This has moved from being "nice to have" to being an expected deliverable.

### User Study Requirements
Human studies are praised but must meet basic standards:
- Minimum 15–20 participants (but 50+ is preferred per reviewer: "15 users may be considered an insufficient sample size for a reliable evaluation")
- Double-blind evaluation when possible
- Enough trials per participant to be statistically meaningful
- Should not replace quantitative metrics—serve as supplement

### The "Saturated Benchmark" Problem
When baselines already score 90%+ on a benchmark, even SoTA improvements become minor:
- "The reported environments seem 'saturated' in that the baselines already perform pretty well." (Mean Flow Policy reviewer)
- Solution: Use more challenging benchmarks, or reframe the contribution around speed/efficiency rather than accuracy

### Physics-Based Papers: Extra Scrutiny
Physics-based motion papers face unique challenges:
1. Must compare against physics-based baselines (PhysDiff, SimPoE, etc.), not just kinematic methods
2. Must report both motion quality AND physical plausibility metrics
3. Sim-to-real gap must be addressed quantitatively if deployment is claimed
4. Reward hacking is a known failure mode that must be discussed and mitigated

---

## 10. Summary: The Three Questions That Decide Accept/Reject

Based on analysis of all 109 papers, virtually every accept/reject decision hinges on:

1. **Is the novelty real?** Not "is it new?" but "does it enable something genuinely not possible before, with non-trivial technical contribution?"

2. **Is the evaluation fair and comprehensive?** All relevant baselines, standard datasets (both HumanML3D AND KIT-ML for T2M), standard metrics, video demos.

3. **Do the ablations validate every claimed contribution?** Each proposed component must be ablated independently, on the same dataset, with clear gain attribution.

A paper that answers YES to all three is a solid accept (6.0+). A paper answering NO to any one faces serious rejection risk unless the other two dimensions are exceptional.
