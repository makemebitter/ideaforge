# Skill File: Evaluating Research in World Models

**For use by AI judge agents evaluating submissions in the "world_models" topic area.**

---

## 1. Topic Overview

### What This Area Covers

"World models" at ICLR/NeurIPS/ICML encompasses research on learned internal representations that simulate environment dynamics. The field spans several sub-areas:

1. **Model-Based Reinforcement Learning (MBRL) with World Models**: Using learned dynamics models for policy optimization via imagination (Dreamer/DreamerV2/DreamerV3 lineage, TD-MPC, MBPO, MuZero). The most common and competitive sub-area.
2. **Autonomous Driving World Models**: Generative video/occupancy models for predicting future states in driving scenarios (Vista, DrivingWorld, Copilot4D). Heavy focus on FID/FVD metrics and multi-camera fidelity.
3. **Causal and Structured World Models**: World models with causal structure, disentangled representations, object-centric abstractions, or factored dynamics.
4. **Long-Horizon and Hierarchical World Models**: Methods addressing the short imagination horizon limitation of standard RSSMs—temporal abstraction, hierarchical latent dynamics, jumpy state transitions.
5. **World Models with LLMs**: Using large language models as environment simulators or augmenting agents with LLM-based world model reasoning.
6. **Offline/Pre-trained World Models**: Leveraging offline or web-scale data to pre-train world models before fine-tuning on target tasks.
7. **Generative World Models for Video/3D**: Using diffusion, GPT-style, or other generative architectures as interactive world simulators.
8. **Theoretical and Conceptual World Model Analysis**: Formal definitions, stability bounds, causal relationships, identifiability guarantees.

### Key Challenges the Field Grapples With

- **Compounding errors**: Autoregressive rollouts accumulate errors, limiting imagination horizon.
- **Distribution shift**: Training on replay buffer data ≠ distribution encountered during policy optimization.
- **Scalability**: World models that work on toy environments (DMControl, Atari) often fail at complex tasks (Minecraft, real robotics).
- **Computational cost**: Training a world model + policy jointly is expensive; papers must justify the overhead.
- **Evaluation faithfulness**: Video generation metrics (FID, FVD) may not capture planning-relevant properties.
- **Memory and long-term credit assignment**: RSSM-style recurrent models struggle with long temporal dependencies.

### Score Distribution and Acceptance Bar (from 277 papers)

- **Mean rating**: 4.91 | **Median**: 5.0 | **Std**: 1.21
- **Range**: 1.5–8.0 (no paper in this dataset achieved >8.0)
- **Acceptance rate**: 70.4% (higher than average — the topic is broad and includes many solid incremental works)
- **Tier breakdown**:
  - Excellent (8–10): 19 papers — landmark contributions
  - Good (6–7): 250 papers — solid, publishable, clear contributions
  - Borderline (4–5): 536 papers — modest contribution, typical accept/reject territory
  - Low (1–3): 168 papers — insufficient novelty, weak experiments, or fundamental flaws

**Practical calibration**: A 5/10 is genuinely borderline — reviewers are split and the work solves a real problem but lacks either novelty or strong empirical support. A 6/10 is a soft accept with a meaningful contribution over Dreamer/DreamerV3 on at least one benchmark family. A 7/10 requires either a novel architectural insight with consistent SOTA improvements *or* a clean theoretical result with empirical validation. Scores of 8 are reserved for work with clear outsize impact: a new training paradigm (e.g., TD-MPC2), a fundamental theoretical insight (causal world models), or a method that dramatically improves on DreamerV3 in multiple domains.

---

## 2. What Reviewers Praise (with Real Examples)

### 2.1 Novelty of Core Idea

"Novel" is the #1 strength phrase (213 occurrences), and "novelty" appears 20 more times. Reviewers strongly reward ideas that depart meaningfully from the Dreamer lineage or offer a fresh framing.

**Real example — Mastering Memory Tasks with World Models (R2I, 8.0, Oral)**:
> "The paper addresses the problem of long-term dependencies for World Models, which is an issue for RNNs and Transformers on handling sequences in representational models. Therefore, it is very relevant to the community. Furthermore, employing SSMs to replace the aforementioned backbones for learning temporal dependencies is sound and well-motivated."

**Real example — Open-World RL over Long Short-Term Imagination (LS-Imagine, 8.0, Oral)**:
> "The jumpy prediction technique within the long-term imagination framework is innovative as it departs from the fixed interval approach prevalent in previous work, offering increased flexibility in jumpy prediction."

**Real example — Robust Agents Learn Causal World Models (8.0, Oral)**:
> "This paper makes an original and significant theoretical contribution by formally establishing a fundamental connection between causal learning and generalisation under distribution shifts... The results have important implications in safety and robustness under distribution shifts."

**What this means for evaluation**: Incremental improvements over DreamerV3 (adding one auxiliary loss, minor architecture tweak) score 4–5. True novelty means a new type of latent structure, a new connection to another field (causal inference, SSMs, LLMs), or a new problem setting with demonstrated practical value.

### 2.2 Comprehensive Baselines

"Baseline" is the most common weakness phrase (556x), but also a top strength phrase (186x). Papers praised for baselines include the relevant comparison methods from the DreamerV3/TD-MPC/MBPO family AND task-specific baselines.

**Real example — Efficient RL by Guiding World Models with Non-Curated Data (NCRL, 8.0)**:
> "The experimental methodology is thorough and high-quality: covers a wide range of environments, uses appropriate metrics (normalized scores, learning curves with confidence intervals), and includes ablations to justify the algorithm's design."

**Real example — same paper (different reviewer)**:
> "Strong empirical performance with a gain of large margins, compared with baseline methods. Comprehensive evaluations on a wide range of baseline methods and locomotion tasks."

### 2.3 Thorough Ablation Studies

"Ablation" is the #2 strength phrase (166x). Reviewers expect ablations to justify every component of the proposed method.

**Real example — Mastering Memory Tasks with World Models (R2I)**:
> "The work brings extensive and insightful ablation studies in many design decisions in the R2I architecture. These are presented as a systematic evaluation in Appendices M to P and helps understanding how the proposed method works."

A good ablation removes each component independently and shows degradation. Reviewers notice when ablations are too coarse ("with/without our method") vs. fine-grained (each design choice isolated).

### 2.4 Writing Quality and Clarity

"Well-written" (110x) and "well written" (68x) are very common praise phrases. World models papers are often complex, and reviewers reward papers that make the method understandable.

**Real example — NCRL (8.0)**:
> "The paper is written with clarity; the exposition of methods and step-by-step motivation is reasonable / comprehensive. In particular, the high-level motivation for the setting is very clear... Figure 2 provides a particularly clear and compelling motivation for the proposed approach."

**Real example — R2I (8.0)**:
> "The paper is very well presented and easy to follow. Authors do a very detailed theoretical analysis of the approach, building up intuition and making it very easy to follow. It is remarkable that they even include in-depth discussions on why they discarded alternative features when designing their algorithm."

### 2.5 Reproducibility

"Reproducib" appears 40 times in strengths. Reviewers value code release, detailed hyperparameter tables, and pseudocode.

**Real example — NCRL**:
> "Reproducibility. The paper includes extensive implementation and hyperparameter details, making the method straightforward to reproduce and encouraging further study or application."

**Real example — R2I reviewer (after rebuttal)**:
> "Appendix Q is great. I think this was one common concern from many reviewers and it was well addressed with many details."

### 2.6 Strong Empirical Results Across Diverse Benchmarks

**Real example — R2I**:
> "The proposed architecture establishes new state-of-the-art performance for several tasks in the considered environments (BSuite, POPGym, and Memory Maze), with a noticeable improvement in computational efficiency."

Note: reviewers specifically praise coverage across *multiple* benchmark families. A paper that only demonstrates improvement on DMControl easy tasks scores lower than one showing improvements across DMControl + Atari + a memory benchmark.

---

## 3. What Reviewers Criticize (with Real Examples)

### 3.1 Missing or Insufficient Baselines

"Baseline" is overwhelmingly the #1 weakness phrase (556x — 3× more than any other weakness term). Papers that compare against only older methods (Dreamer, not DreamerV3; no TD-MPC; no MBPO) are heavily penalized.

**Real example — SelfDreamer (4.0, Reject)**:
> "The paper lacks a comprehensive comparison and discussion of existing methods. There are tons of model-free efficient RL works recently (state augmentation [DrAC, DrQ-v2] and masked auxiliary losses [SPR, etc.]). I think it is worth discussing the recent progress of efficient RL in the related work session or adding baselines for comparison."

**Real example — DrivingWorld (4.5, Reject)**:
> "The method's FID and FVD scores, while reasonable, do not lead the benchmark comparisons... This becomes more apparent when considering recent SOTA works like DiVE and Vista, which are absent from the comparison."

**What to check**: Does the paper compare against the most recent strong baselines? In MBRL, that means at minimum DreamerV3, TD-MPC2, and task-relevant model-free SOTA. In driving world models: Vista, DriveWM, or UniAD depending on year.

### 3.2 Limited Novelty / Incremental Contribution

"Novelty" (159x) and "incremental" (40x) and "limited novelty" (15x) are frequent criticism phrases.

**Real example — Mastering Memory Tasks with World Models (skeptical reviewer)**:
> "Limited contribution. It is notable that there already exists a S4-based world model, namely S4WM. Despite minor design choices, the major difference of this paper is that it conducts MBRL experiments while S4WM only conducts world model learning... it is not surprising that improvements in long-term memory can lead to improved MBRL performance in memory-demanding domains."

**Real example — SelfDreamer (reject reviewer)**:
> "The key insight that improves performance in the frame-masking setting is that of using prototypes in general, already introduced with DreamerPro. SelfDreamer seems then a complex technique that delivers a small improvement over DreamerPro for all scenarios."

**What to watch for**: The reviewers specifically check whether the proposed method is differentiated from contemporaneous arXiv work. A "novel" combination of two existing ideas (DreamerV3 + SSM = R2I) can still be highly valued if it opens a new capability, but not if it merely adapts existing components with marginal gains.

### 3.3 Insufficient Ablation Studies

"Ablation" is the #2 weakness phrase (238x). Reviewers notice missing ablations immediately.

**Real example — SelfDreamer**:
> "If your method is built directly on top of the DreamerPro technique, can you conduct an ablation experiment, consisting of applying your action/transition prototyping technique on top of standard Dreamer? I imagine that such an experiment would help show whether the DreamerPro prototypes are the actual 'key' ingredient."

**Real example — LS-Imagine (good paper, but still flagged)**:
> "Some relevant citations are missing... There are no error bars for the middle and right plots in Figure 7. Are these results only based on one seed?"

### 3.4 Limited Experimental Scope

"Limited to" (42x), "unclear how" (56x), "unclear whether" (44x) — reviewers question generalizability.

**Real example — SelfDreamer**:
> "The evaluation focuses on a limited set of tasks from the DeepMind Control Suite. The paper could benefit from a broader evaluation across diverse RL benchmarks to demonstrate the method's applicability and generalizability."

**Real example — LS-Imagine (8.0 despite this weakness)**:
> "The method feels very ad-hoc to the Minecraft tasks studied in this paper. It doesn't come into my mind about any other relevant tasks other than Minecraft where the proposed method can be applied."

Even well-scored papers receive this criticism. When a paper *only* evaluates on DMControl (6–12 tasks), reviewers consistently ask for Atari, Meta-World, or another domain. Single-environment papers need to justify their scope.

### 3.5 Scalability Concerns

"Scalab" appears 85x in weaknesses.

**Real example — NCRL**:
> "The impact of showing improvements in the low-data regime with these particular simulation settings is less clear, given cheapness of simulation data and the asymptote to the same performance with more environment steps."

**Real example — LS-Imagine**:
> "The approach is limited to embodied agents navigating a 3D environment in which there are objects associated for which reward is obtained by approaching them... This approach would likely not work as well even in Crafter."

### 3.6 Unfair Comparisons

"Fair comparison" (24x) is a direct complaint about methodology.

**Real example — R2I**:
> "Has the scaling world model to 280M parameters also been applied to baseline methods for fair comparison?"

Papers that use larger model sizes, more data, or more compute than baselines without controlling for this are penalized.

### 3.7 Missing Related Work / Citations

**Real example — R2I (resolved in rebuttal)**:
> "There already exists a S4-based world model, namely S4WM... the work is almost overlooked by the proposed paper, which has a small citation in Section 5. Given the similarity, it would be crucial to provide a more detailed comparison contrasting both works."

**Real example — LS-Imagine**:
> "Some relevant citations are missing: [Director] studies the hierarchical world model which uses a similar strategy of doing the long-term imagination on the higher-level states."

Missing a directly related concurrent paper is a common reason for low initial scores that can be fixed in rebuttal — but missing major prior work is a more serious problem.

### 3.8 Clarity and Presentation Issues

Poor writing scores are terminal at top venues.

**Real example — SelfDreamer (reject reviewer)**:
> "Poor writing. There are several sentences that are hard to read for the first time... 'particularly when enforcing a single transition for various states after taking identical actions': it is hard to understand what it means."

**Real example — "What Does it Mean for a NN to Learn a World Model?" (4.75, Reject)**:
> "The paper is styled more as a blog post than a conference paper: beyond its highly informal prose and prominent citations of tweets (Lecun, 2024) and blog posts (Andreas, 2024), it also lacks the theoretical rigor that is necessary for a conceptual submission such as this one."

---

## 4. Required Baselines & Metrics

### 4.1 Core MBRL Baselines (must include for any RL-focused paper)

| Baseline | Why It's Expected |
|----------|-------------------|
| **DreamerV3** (Hafner et al., 2023) | The dominant MBRL world model; any paper claiming improvements MUST compare |
| **TD-MPC2** (Hansen et al., 2023) | Leading model-predictive-control world model for continuous control |
| **MBPO** (Janner et al., 2019) | Classic model-based RL with a Dyna-style world model |
| **SAC** / **DrQ-v2** | Strong model-free baselines for comparison (shows value of world model) |
| **DreamerV2** | Needed when comparing on Atari or partial observability settings |
| **MuZero** / **EfficientZero** | For discrete action spaces and game-playing settings |

Reviewers notice when papers skip DreamerV3 in favor of older Dreamer/DreamerV2 to make results look better.

### 4.2 Domain-Specific Baselines

**For memory / long-horizon tasks (POPGym, BSuite, Memory Maze)**:
- R2I (Samsami et al., 2024)
- S4WM (Deng et al., 2023)
- Director (Hafner et al., 2022)
- TSSM / RSSM-TBTT variants

**For autonomous driving world models**:
- Vista (2024)
- DriveWM / UniAD
- GAIA-1
- Copilot4D

**For object-centric / structured world models**:
- OCWM / SlotFormer
- C-SWM

**For LLM-based world models**:
- LLM as a zero-shot planner baselines
- Inner Monologue

### 4.3 Required Benchmarks

| Benchmark | Domain | Common in |
|-----------|--------|-----------|
| **DMControl (visual/proprio)** | Continuous control | Almost all MBRL papers |
| **Atari 100K** | Discrete, sample efficiency | Papers claiming data efficiency |
| **Meta-World** | Robotics manipulation | Multi-task world models |
| **Memory Maze / BSuite / POPGym** | Long-horizon memory | SSM/memory-focused world models |
| **Minecraft/MineDojo** | Open-world | Hierarchical world models |
| **nuScenes / nuPlan / CARLA** | Autonomous driving | Driving world model papers |
| **Crafter** | 2D open-world | General open-world benchmark |

**Red flag**: A world model paper that only evaluates on 6 DMControl tasks. Reviewers invariably ask for at least 12+ DMControl tasks or an additional benchmark.

### 4.4 Metrics

**For MBRL papers**:
- Normalized/raw episode return (mean ± std over multiple seeds, typically 5+)
- Sample efficiency curves (return vs. environment steps)
- Compute efficiency (wall-clock time if claiming efficiency gains)
- Ablation table showing contribution of each component

**For video/generative world models**:
- FID (Fréchet Inception Distance)
- FVD (Fréchet Video Distance)
- PSNR / SSIM for reconstruction quality
- Semantic consistency metrics
- Planning performance (if used as a simulator)

**Common mistake**: Reporting only final performance without sample efficiency curves, especially when claiming sample efficiency as a contribution.

---

## 5. Common Technical Pitfalls

### 5.1 Ignoring the Dreamer Ecosystem

The Dreamer lineage (DreamerV1 → V2 → V3) has introduced many improvements sequentially. Reviewers catch papers that:
- Propose a component already present in DreamerV3 without acknowledgment
- Build on DreamerV2 but call results "SOTA" without comparing to V3
- Overlook concurrent work on SSM-based world models (S4WM, when proposing SSM integration)

### 5.2 Conflating World Model Quality and Policy Performance

A world model can predict accurately without producing good policies. Reviewers often ask for:
- Visualization of imagined trajectories (do they look plausible?)
- World model prediction error metrics alongside policy performance
- Ablation that isolates world model quality contribution

### 5.3 Distribution Shift Not Addressed

The fundamental world model challenge is that the model is trained on data from the replay buffer but used to generate trajectories under the current policy. Papers that ignore this:
- Don't analyze distribution shift between training and imagination
- Don't bound or quantify model prediction error during rollouts
- Use off-policy data without justification

**Real example — NCRL reviewer catching this**:
> "Would your method prevent or slow down (in some settings) convergence of the world model to the best points in the world space? I'm just thinking that keeping around old data is fine and prevents a distribution shift but what about in the cases where the distribution shift is actually required."

### 5.4 Not Defining What Makes Something a "World Model"

Several lower-rated papers in this dataset suffer from vague claims about having a "world model" without rigorously defining it.

**Real example — DrivingWorld reviewer**:
> "The concept of the World Model may be considered controversial and could benefit from further clarification to establish its acceptance and validity within the field."

### 5.5 Over-Engineering Without Clear Motivation

Complex methods with many components that each provide marginal gain score lower than simple methods with clear contributions.

**Real example — SelfDreamer reject reviewer**:
> "The way that the technique is presented is confusing, and does not adequately convey the rationale behind the specific choice of mechanism for action/transition prototype learning."

**Real example — LS-Imagine (accepted but flagged)**:
> "Although the high-level idea is straight-forward, the implementation is overcomplicated."

### 5.6 Insufficient Seeds / Error Bars

Reviewers in this area strongly enforce statistical rigor.

**Real example — LS-Imagine**:
> "There are no error bars for the middle and right plots in Figure 7. Are these results only based on one seed?"

Standard expectation: 5 seeds for DMControl, 3 seeds for complex environments (Minecraft). Papers that report single-seed results or don't report confidence intervals are penalized.

### 5.7 Anonymity Violations

**Real example — DrivingWorld (1.0 from one reviewer)**:
> "The paper breaks the author's anonymity. I could find the full author list with their affiliations and personal web pages in two clicks, i.e., first click on the link in the abstract of the paper to go to the repo."

This is a terminal issue that overrides technical quality for blind review venues.

### 5.8 Claiming "World Model" for Pure Video Generation

Papers that generate realistic videos but cannot be used for planning or RL are questioned on their "world model" framing.

**What reviewers check**: Can you condition on actions? Can the model be queried for rewards? Is there a latent state that enables planning? Papers answering "no" to all three face pushback.

---

## 6. Scoring Rubric for This Topic

### 6.1 Score 3/10 or below — Fundamental Flaws

**What it looks like**:
- A conceptual paper with informal prose, no formalization, and cited tweets/blog posts as primary references ("What Does it Mean for a NN to Learn a World Model?")
- A method that doesn't actually outperform baselines in its claimed setting, with poor writing and unclarified design choices (SelfDreamer with frame-masking)
- An anonymity violation
- A work that proposes a "world model" that is actually just a video generation model with no action-conditioning or planning capability
- Missing the most relevant recent baselines by 2+ years

**Example**: SelfDreamer (4.0) was rejected because: (1) the method doesn't significantly outperform DreamerPro in the frame-masked setting it was designed for, (2) multiple reviewers found the method description unclear, (3) the evaluation was limited to a handful of DMControl tasks, (4) insufficient differentiation from DreamerPro.

### 6.2 Score 5/10 — Borderline (Acceptance Threshold)

**What it looks like**:
- A real problem addressed with a reasonable method, but experiments are limited to one domain
- Improvements over DreamerV3 are marginal or inconsistent across environments
- Missing 1-2 important recent baselines
- Ablation studies exist but are incomplete
- The core idea is sound but not sufficiently novel relative to concurrent/prior work
- Writing is adequate but not clear

**Example pattern**: A paper that proposes an improved latent representation for world models, evaluates on 8 DMControl tasks with solid improvements, but doesn't compare to TD-MPC2 or test on memory benchmarks, and has no theoretical justification.

**Borderline decision factors**:
- Is the setting new and valuable even if the method is not? (+0.5–1.0)
- Does the paper evaluate on diverse enough benchmarks? (missing this costs 0.5–1.0)
- Is there a compelling ablation? (missing this costs 0.5)

### 6.3 Score 7/10 — Solid Accept

**What it looks like**:
- Clear improvement over DreamerV3 on multiple benchmark families (e.g., both DMControl and Atari, or DMControl and Meta-World)
- A mechanistically justified innovation (new latent structure, new training objective, new use of offline data)
- Comprehensive ablations that validate each design choice
- Comparison against all relevant recent baselines
- 5 seeds with confidence intervals
- A memorable figure that motivates the approach

**Example**: NCRL (8.0) demonstrates the pattern: it tackles a well-motivated problem (non-curated offline data for world model RL), proposes two clearly-motivated components (experience rehearsal + execution guidance), validates on both Meta-World and DMControl, ablates each component, and compares comprehensively.

**What separates 7 from 8**: A 7-paper has strong results but limited scope (single domain, or a method that only works on the Dreamer architecture). An 8-paper generalizes, introduces a fundamentally new capability, or provides a theoretical insight.

### 6.4 Score 8–9/10 — Excellent

**What it looks like**:
- A new paradigm or formal insight that the community will build on
- Demonstrated improvements across 3+ benchmark families
- Either: (a) deep theoretical contribution (formal proofs, causal analysis) OR (b) new capability not previously demonstrated (long-horizon open-world RL, causal generalization)
- Writing that makes complex ideas accessible
- Code released, reproducible

**Real examples in dataset**:

*Robust Agents Learn Causal World Models (8.0, Oral)*: Formal proof that agents with bounded regret under distribution shifts must have learned causal structure. One reviewer wrote: "This paper is a gem. The theoretical analysis is simple and clear, the implications are broad and powerful."

*Mastering Memory Tasks with World Models / R2I (8.0, Oral)*: Demonstrated that SSMs can replace GRUs in DreamerV3, achieving SOTA on BSuite/POPGym/Memory Maze while maintaining competitive DMControl performance, with extensive ablations across design choices.

*Open-World RL over Long Short-Term Imagination / LS-Imagine (8.0, Oral)*: Novel hierarchical world model with variable-interval "jumpy" transitions for open-world Minecraft, using MineCLIP-based affordance maps for goal-directed jumpy prediction.

**Pattern**: All three oral papers opened new research directions (causal MBRL, SSM-based world models, open-world MBRL) rather than incrementally improving existing methods.

### 6.5 The "Strong Baselines" Trap

Many papers that score 4–5 have genuine technical contributions but are penalized because:
- They show improvement over DreamerV2 but not V3
- They compare against older model-free baselines instead of current MBRL SOTA
- The improvement disappears when compared to the full V3 baseline

Always verify: does the paper use the strongest available version of DreamerV3 (300M steps, full hyperparameter tuning) as the baseline?

---

## 7. Key Papers & Expected Citations

### 7.1 Foundational World Model Papers (must know for context)

| Paper | What It Introduced | Why Reviewers Cite It |
|-------|-------------------|----------------------|
| **Ha & Schmidhuber, 2018 (World Models)** | Named the concept of "world models" for RL | Foundational; not citing it in a WM paper is a red flag |
| **PlaNet (Hafner et al., 2019)** | Latent dynamics models with RSSM | First strong world model for visual RL |
| **Dreamer (Hafner et al., 2020)** | Policy optimization via imagination | Seminal; basis for all subsequent Dreamer work |
| **DreamerV2 (Hafner et al., 2021)** | Discrete latent spaces, categorical representations | Major Dreamer upgrade; Atari SOTA |
| **DreamerV3 (Hafner et al., 2023)** | General world model across domains | Current strongest baseline; must compare against |
| **TD-MPC2 (Hansen et al., 2023)** | Scalable world models with MPC | Alternative paradigm to Dreamer; must compare |
| **MuZero (Schrittwieser et al., 2020)** | Planning via learned model | Key citation for game-playing world models |

### 7.2 Sub-Area Specific Expected Citations

**For SSM/memory world models**:
- S4WM: "Facing off World Model Backbones: RNNs, Transformers, and S4" (Deng et al., NeurIPS 2023)
- STORM: "Efficient Stochastic Transformer-based World Models" (Zhang et al., NeurIPS 2024)
- RWKV and Mamba as alternative sequence models

**For hierarchical world models**:
- Director: "Deep Hierarchical Planning from Pixels" (Hafner et al., NeurIPS 2022)
- Dr. Strategy: "Model-Based Generalist Agents with Strategic Dreaming" (ICML 2024)
- Temporal abstraction literature (options framework)

**For causal world models**:
- Schölkopf et al., 2021 (causal representation learning)
- Pearl, 2009 (causality, as a foundational reference)
- C-SWM (Kipf et al., 2020) for object-centric causal dynamics

**For autonomous driving world models**:
- Vista (NeurIPS 2024)
- UniAD (CVPR 2023)
- Wayformer / NMP for comparisons

**For offline/data-efficient world models**:
- MODEM: "Accelerating visual MBRL with Demonstrations" (Hansen et al.)
- Plan2Explore (Sekar et al., 2020) for exploration
- DreamerPro (Deng et al.) for contrastive world model learning

**For LLM-augmented world models**:
- Inner Monologue (Huang et al., 2022)
- SayCan (Ahn et al., 2022)
- ReAct (Yao et al., 2023)

### 7.3 Papers Reviewers Frequently Ask Authors to Compare Against

From reviewer questions in this dataset:
1. **DreamerV3** — asked in nearly every MBRL paper review
2. **TD-MPC2** — increasingly required in continuous control papers (2024+)
3. **S4WM** — required for any SSM-based world model paper
4. **Director** — required for any hierarchical world model paper
5. **DrQ-v2** — model-free baseline required when claiming sample efficiency
6. **Vista / DiVE** — for driving world model papers

### 7.4 Red Flag: Citing Only Old Baselines

Papers that cite DreamerV1/V2 but not V3, or compare against 2021-era baselines for a 2025 submission, are almost always penalized. The reviewer will note: "comparison with DreamerV3 is missing" and this alone can drop a score by 1–2 points.

---

## 8. Calibration Notes for Borderline Cases

### 8.1 Theory-Only vs. Empirical-Only

This topic is unusual in that the dataset contains both pure theory papers (causal world models proofs) and pure empirical papers (driving video generation). These are evaluated on different axes:

- **Theory papers (rare, ~5%)**: Evaluated on rigor of proofs, significance of formal results, quality of examples. Weak theory papers often lack experiments entirely, which draws criticism but isn't always fatal if the theorem is genuinely novel.
- **Empirical papers (dominant, ~80%)**: Evaluated on benchmark coverage, baseline comprehensiveness, ablation quality, and consistency of improvement. Must show improvement on at least 2 benchmark families to score 6+.
- **Combined theory+empirical (~15%)**: Highest potential; formal insight + empirical validation. The most-praised papers in this dataset fall here.

### 8.2 Application Papers vs. Methods Papers

World models applied to a specific domain (robotics, autonomous driving, humanoid locomotion) are common in this dataset. They're evaluated somewhat differently:

- **Real-world evaluation is a major plus**: A paper with real robot experiments scores 0.5–1.0 higher than one with only simulation.
- **Domain-specific metrics matter**: For driving, FID/FVD + downstream planning performance; for robotics, task success rate.
- **Must still compare to domain-specific baselines**, not just general MBRL methods.

### 8.3 "Not a World Model" Penalty

Papers that propose a video generation model or predictive model but cannot be used for RL/planning risk a 1.0 score penalty from reviewers who argue the work doesn't belong in "world models." Watch for:
- No action-conditioning mechanism
- No reward prediction
- Evaluated only on video quality metrics, never on downstream agent performance

### 8.4 Compute and Parameter Count Disclosure

Reviewers increasingly ask for:
- Number of parameters in proposed model vs. baselines
- Training compute (GPU hours)
- Fair comparison when scaling up model size

A paper that achieves SOTA with a 3× larger model without acknowledging this will be criticized for unfair comparison.

---

## Summary: Quick Scoring Heuristics

Use these rules-of-thumb when making a fast initial judgment:

| Signal | Score Impact |
|--------|-------------|
| Compares to DreamerV3 + TD-MPC2 | +0.5 |
| Missing DreamerV3 comparison | -1.0 |
| Evaluates on 2+ benchmark families | +0.5 |
| Only evaluates on 6–8 DMControl tasks | -0.5 |
| 5+ seeds with confidence intervals | +0.5 |
| Single-seed or no error bars | -0.5 |
| Thorough component-wise ablation | +0.5 |
| No ablation or coarse ablation | -0.5 |
| Novel architecture/paradigm | +1.0–2.0 |
| Incremental improvement over DreamerV3 | +0.0 |
| Real-world (robot/car) experiments | +0.5–1.0 |
| Anonymity violation | -6.0 (effectively terminal) |
| Theory with formal proofs + experiments | +1.0–2.0 |
| Concurrent work not cited | -0.5 to -1.0 |
