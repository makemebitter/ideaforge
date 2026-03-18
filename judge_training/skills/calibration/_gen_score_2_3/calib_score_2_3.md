# Calibration Skill: Score 2–3 / 10 at Top AI Conferences (ICLR / NeurIPS)

> **Purpose:** Teach an AI judge the ABSOLUTE quality bar for papers that score in the 2–3 range. This is not a relative ranking—it is a fixed quality standard grounded in real reviewer behavior at ICLR 2024/2026 and NeurIPS 2025.

---

## 1. Score Range Profile

### What does "score 2–3 out of 10" mean?

On the OpenReview scale used by ICLR and NeurIPS, individual reviewers score papers from 1–10 (or 0–10 at ICLR 2026). A paper whose **average reviewer score is approximately 1.5–3.0** lands in this calibration bucket, corresponding roughly to individual reviewer scores of 0–3 per reviewer.

**Translation to verbal labels:**
- Score 1–2: "Strong Reject" / "Reject, not good enough"
- Score 3: "Reject" / borderline weak reject

Papers in the **2–3 range** are papers where **all or nearly all reviewers** want to reject, and at least some are emphatic about it. The paper is not simply bad in one dimension—it fails on the core criteria that ICLR/NeurIPS use for acceptance: novelty, technical rigor, and experimental evidence.

### Typical decision

**Overwhelmingly Reject.** In the 20-paper sample used for this skill file, 14/20 papers at this score level were rejected. The 6 accepted papers (e.g., "Opal," "What Is Missing," "Analysing Representations Through Layers") are exceptions that typically involve extreme reviewer disagreement (one outlier giving a 6 while three others give 0–2) or workshop-track-style contributions that happened to get through in a borderline program committee decision.

**Do not assume a 2–3 paper is a borderline paper.** Borderline papers score in the 4–5 range. A 2–3 is a clear, consistent rejection signal.

### How common?

At ICLR 2026, roughly 30–40% of all submissions receive average scores below 3. This is a large plurality of all submitted papers. The 2–3 range is the "clear reject" zone, below borderline but above the "completely unacceptable" extreme.

---

## 2. Characteristic Patterns — Real Examples

### Example 1: "Which Coauthor Should I Nominate in My 99 ICLR Submissions?"
**Rating: 1.5 | Decision: Reject | Forum: QvN5FZ3tNW**

**What it is:** A combinatorial optimization paper formalizing reviewer nomination as a risk minimization problem (greedy + min-cost flow + LP).

**Why it scored 1.5:**
- **Technical triviality.** The "basic" case is solved by a one-line greedy rule. The "hard limit" case is a textbook minimum-cost flow instance known since the 1950s. The "soft limit" case is a standard convex relaxation. One reviewer wrote: *"The connection between linear programming and minimum-cost flow is correctly stated (though trivial)."*
- **Unrealistic assumptions.** The framework assumes authors know each co-author's exact "irresponsibility probability"—a quantity that cannot be observed or estimated. Reviewers noted: *"There is no mechanism to estimate these probabilities."*
- **Wrong venue.** The paper contains no learning, no data, and no connection to neural networks. It is pure combinatorial optimization and would fit a theory-of-CS workshop, not ICLR.
- **Motivation failure.** The scenario (an author with 99 submissions optimizing reviewer nominations) is described as "implausible" by reviewers, and no empirical validation grounds the problem in real submission behavior.

**Score justification:** Every reviewer independently identified the technical contribution as trivially reducible to textbook results. Novelty score was 1/5 across all four reviews.

---

### Example 2: "Interpreting Emergent Military Tactics in a General AlphaZero Framework"
**Rating: 1.5 | Decision: Reject | Forum: Te2nrVBVo5**

**What it is:** Application of AlphaZero to a custom 7×7 battlefield gridworld environment with reward shaping experiments.

**Why it scored 1.5:**
- **Pure application paper with no algorithmic novelty.** Reviewers wrote: *"The entire methodology is a direct and unmodified (or small modified) application of AlphaZero to a small toy gridworld."* and *"The paper proposes no novelty."*
- **No baselines.** There are no comparisons to MARL baselines (SMAC, Google Research Football, MicroRTS), no comparisons to simpler algorithms like DQN, and no statistical analysis.
- **Engineering report, not research.** One reviewer explicitly characterized it: *"The paper reads more like an engineering report documenting the implementation of AlphaZero with minor adjustments, rather than a research contribution offering new understanding or advancement."*
- **Limited scope.** All experiments are on a single 7×7 gridworld, making it impossible to generalize any conclusions.

**Score justification:** Four reviewers independently rated contribution at 1–2/5. The environment is the sole potentially useful artifact, but similar environments (MicroRTS, Generals.io) already exist and were not compared against.

---

### Example 3: "SFT WITHOUT OVERFITTING: Analyzing the Training Dynamics of Supervised Fine-Tuning"
**Rating: 1.5 | Decision: Reject | Forum: C3I7nIXKHc**

**What it is:** Empirical study showing that fine-tuning only attention layers (vs. FFN layers) improves OOD generalization in LLMs.

**Why it scored 1.5:**
- **Incremental finding without theory.** The paper shows attention-only tuning helps OOD, but gives no causal explanation—no gradient flow analysis, no theoretical framework. One reviewer: *"The claim that attention-only tuning causes better OOD generalization is correlational; causal mechanisms are not deeply examined."*
- **Narrow experimental scope.** Only two tasks (GeneralPoints, V-IRL) on one model (Llama-3.2-Vision-11B). Generalization to language understanding, open-ended tasks, or other model families is unclear.
- **Insufficient literature review.** Missed directly relevant PEFT papers that showed similar phenomena. One reviewer cited: *"There have lots of PEFT works on selective FT that should be compared with."* Additionally, experimental design closely mirrors prior work ("SFT Memorizes, RL Generalizes") without clearly distinguishing the new contribution.
- **Overclaiming.** The comparison to RL alignment methods lacks sufficient baselines detail—RL algorithm type (PPO/DPO), reward function, and hyperparameters are not provided.

**Score justification:** Despite reasonably controlled experiments, reviewers consistently rated novelty as 1–2/5. The gap between what is shown (empirical correlation in two tasks) and what is claimed (general understanding of SFT dynamics) is too wide.

---

### Example 4: "Curvature Meets Bispectrum: A Correspondence Theory for Transformer Gauge Invariants"
**Rating: 1.5 | Decision: Reject | Forum: pcqyhDvG0i**

**What it is:** A highly mathematical paper connecting Fisher-Rao curvature (geometric) and bispectrum (algebraic) invariants for analyzing transformer parameter symmetries.

**Why it scored 1.5:**
- **Inaccessible to target audience.** Three of four reviewers flagged the paper as essentially unreadable for the ICLR community. Reviewer: *"The paper is written in an highly impenetrable and obscure fashion, seemingly with extensive usage of an LLM."* (Note: also flagged in the Opal paper, suggesting reviewers are developing sensitivity to LLM-generated mathematical writing.)
- **No practical relevance demonstrated.** The only hint at application (line 415) mentions *"promising targets for head merging, shared-parameter updates"* but provides no experiments. Reviewers asked repeatedly: *"Can the authors provide a concrete example where knowing these results leads to a practical improvement?"*
- **Questionable proof correctness.** One high-confidence reviewer identified specific proof gaps: *"Theorem 2.1… the proof of necessity/maximality – which is the non-trivial part – is just a few lines long, and is completely unclear to me."* This reviewer also flagged substantial overlap with another concurrent ICLR submission, raising integrity concerns.
- **Missing comparisons.** Key related work (Silva et al. ICML 2025, Ziyin ICML 2024) is not properly situated.

**Score justification:** Even the reviewer who gave it a 2/10 (vs. the others giving 0–2) noted the lack of motivation. The theoretical machinery may be correct, but it is inaccessible, unmotivated, and practically irrelevant in current form.

---

### Example 5: "Opal: An Operator-Algebra View of RLHF Objectives"
**Rating: 1.5 | Decision: Accept (!) | Forum: C3FEh03LMO**

**What it is:** A formal algebra paper showing many RLHF objectives are algebraically equivalent via rewrite theory.

**Why it scored 1.5 despite being accepted:**
- **Extreme reviewer disagreement.** One reviewer gave 6/10 (*"The theory is novel and interesting. It is also correct as far as the reviewer can tell."*). The other three gave 0/10 each—one of the clearest possible reject signals.
- **Writing catastrophe.** Three reviewers essentially said the paper is unreadable. Sample: *"The paper is written in a completely impenetrable fashion… The problem is never properly defined, motivation is barely provided, terminology is used without explanation."* Another: *"I could not understand what this paper is about."*
- **Niche but valid contribution.** The single supportive reviewer found the contribution theoretically sound and novel. This is a paper where the substance may exist but the presentation makes it inaccessible to most of the program committee.

**Lesson for judges:** A 1.5 average does not always mean "the paper is bad"—it can mean "the paper failed to communicate its contribution to the reviewers." The underlying work might be interesting but the paper-as-submitted is not publishable. **You should score the paper as presented, not the idealized version the author intended.**

---

### Example 6: "SAFE: Improving LLM Systems using Sentence-Level In-generation Attribution"
**Rating: 1.5 | Decision: Reject | Forum: wo5y09nns1**

**What it is:** A two-stage RAG attribution framework (classifier predicts citation count → attributor finds quotes) plus a cleaned dataset (HAGRID-Clean).

**Why it scored 1.5:**
- **Engineering without novelty.** Combines standard IR methods (BM25, SPLADE, embedding similarity) with a Random Forest classifier. Reviewers: *"The proposed framework lacks novelty. It mainly combines two steps… This limits the paper's contribution to an engineering solution instead of an innovation."*
- **Misleading claims.** The "in-generation" framing is misleading—the system operates post-hoc per sentence, not truly during generation. Reviewers flagged the disconnect from SOTA in-generation attribution (Gao et al. 2023, RARR).
- **Fragile design.** The best-performing classifier uses 24 hand-crafted textual features (not learned representations). Reviewers raised serious generalization concerns: *"This approach is notoriously fragile and prone to poor generalization."*
- **Low performance ceiling.** Even with a perfect pre-attribution classifier, the best attributor achieves only 78% accuracy, suggesting the core retrieval is broken.
- **Outdated baselines.** Only classical IR methods compared; no comparison to modern generative attribution or citation-generation baselines.

---

### Example 7: "Stability-Aware Post-Training Cascade of Experts for Compute-Efficient Inference"
**Rating: 1.5 | Decision: Reject | Forum: NWK6hrnZ7Z**

**What it is:** A cascade framework that post-hoc assembles heterogeneous pretrained models with learned routing thresholds.

**Why it scored 1.5:**
- **Limited novelty relative to established work.** Cascades, early-exit, Pareto optimization, and stability-based selection are well-known. Crucially, a directly comparable 2023 TMLR paper ("Efficient Inference With Model Cascades") with more thorough evaluation was not cited or compared against.
- **Distribution shift failure unaddressed.** On UrbanSound8K, the method violates its own accuracy tolerance bounds (15pp drop vs. 8pp tolerance). The paper acknowledges this failure but offers no solution or analysis.
- **No baselines.** Experiments compared only to ablations, not to competing cascade methods. Even simple baselines (set all thresholds to the median) were not included.
- **Clarity problems.** The paper "focuses on the mechanical 'how' of the algorithm and severely lacks explanation for 'what' and 'why.'" Variables are introduced without definition; motivation is absent at each algorithmic step.

---

### Example 8: "Local and Global Modeling with Large Language Models for Time Series Forecasting"
**Rating: 1.5 | Decision: Reject | Forum: b33NnpPFRA**

**What it is:** Logo-LLM, a time series forecasting model using shallow + deep GPT-2 layers with two MLP-Mixer modules.

**Why it scored 1.5:**
- **Incremental modification of existing framework.** The paper mainly adds Mixer modules to GPT4TS—all other components (patching, instance norm, frozen LLM) are inherited. Reviewers: *"Novelty is very limited. Compared to GPT4TS the main incremental change is adding the Mixer modules."*
- **Hypothesis not supported.** The claim that shallow LLM layers capture local patterns and deep layers global patterns is observational, not analytically supported. There is no theoretical justification.
- **Missing baselines.** Several 2024–2025 LLM-for-time-series papers are not compared against (TEMPO, LLM-Mixer, KAIROS). One reviewer: *"The paper fails to evaluate on benchmarks used by recent works and compare against contemporaneous multi-scale approaches."*
- **Weak experimental design.** Only GPT-2 as backbone, only 3 random seeds for few-shot, 1 seed for zero-shot. Not tested on other LLM architectures.
- **LLM motivation problem.** The method doesn't use text—it uses frozen LLM weights as feature extractors. Reviewers questioned why LLMs specifically are needed when the paper "Are Language Models Actually Useful for Time Series Forecasting?" shows that excluding LLMs can improve performance.

---

## 3. Common Traits of Score 2–3 Papers

### 3.1 The Core Problem: Contribution/Novelty Deficit

**This is the single most common failure mode.** Nearly every paper at this score level receives a contribution score of 1–2 out of 5 from most reviewers. The paper applies known techniques (min-cost flow, AlphaZero, MLP-Mixer, attention tuning) to a new setting without introducing new insight, theory, algorithm, or analysis method.

> *"The paper introduces no novel algorithmic mechanism, theoretical insight, or analytical framework."*
> *"The overall contribution remains incremental."*
> *"This limits the paper's contribution to an engineering solution instead of an innovation."*

Papers that are purely empirical ("we tried X and it worked") without theoretical grounding, surprising findings, or comprehensive evaluation fall here.

### 3.2 Missing or Outdated Baselines

Score 2–3 papers almost universally fail to compare against state-of-the-art methods. This takes several forms:
- Comparing only to methods from 2–3 years ago
- Comparing only to ablations (no external competitors)
- Using toy datasets (CIFAR-10, single 7×7 gridworld) that do not support strong conclusions
- No statistical significance testing (no error bars, single runs)

The missing baselines problem is insidious because it makes it impossible to verify that the contribution is real. If the paper doesn't beat modern baselines, there's no evidence the method works.

### 3.3 Narrow Experimental Scope

A single model, a single dataset, a single domain. Papers at this level routinely:
- Test on 1–2 benchmarks (vs. 5–10 for accepted papers)
- Use only one model size or architecture
- Restrict to one modality or task type
- Fail to conduct ablations across the key dimensions of their contribution

> *"Experiments are limited to two tasks with narrow reasoning domains; generality is unclear."*
> *"All experiments are restricted to a single 7×7 gridworld."*
> *"The entire evaluation is conducted on HAGRID and WebGLM-QA."*

### 3.4 Presentation Failures

A significant minority of score 2–3 papers (perhaps 20–30%) have severe writing problems:
- Impenetrable mathematical writing with undefined notation
- LLM-suspected text generation (dense, superficially formal, lacks intuition)
- Missing introductions, background, or motivation
- No related work contextualization
- Paper "reads like a draft" with grammar errors, citation format issues, and undefined variables

> *"The paper is written in a completely impenetrable fashion… The problem is never properly defined, motivation is barely provided."*
> *"I could not understand what this paper is about."*
> *"The main section lacks sufficient clarity to the point that it hinders proper evaluation of the paper's novelty."*

Note: Writing alone rarely kills a paper from a higher score—but at 2–3, severe writing problems often compound other issues and cause multiple reviewers to reject on presentation grounds alone.

### 3.5 Unrealistic or Unexamined Assumptions

Several papers in this range build entire frameworks on assumptions that are:
- Not estimable in practice (e.g., "irresponsibility probability" for each co-author)
- Not validated by the paper's own experiments (e.g., robustness to distribution shift)
- Inconsistent with prior work that the paper ignores (e.g., evidence that LLMs may not help time series)

> *"The entire framework hinges on a massive, unaddressed assumption."*
> *"The hypothesis… is observational, not analytical."*
> *"The reason we're unsure about the main result is that we cannot see how it can be used practically."*

### 3.6 Misalignment with Venue

A recurring (though less dominant) failure: the paper's topic or methodology is a poor fit for an ML venue. Pure combinatorics papers at ICLR, human-subjects EEG audits at ICLR main track, domain-specific engineering reports at NeurIPS—these papers may be fine work in their native fields but lack the ML contribution that justifies the venue.

---

## 4. What Distinguishes Score 2–3 from Adjacent Tiers

### vs. Score 1 (0–1.5 avg): "Complete Failure"
Score 1 papers often have:
- Fundamental logical or mathematical errors
- Results that don't support conclusions at all
- Complete lack of experimental section
- Suspected academic integrity violations (plagiarism, fabricated results)

Score 2–3 papers are at least coherent and mechanically correct. The work was done; it just doesn't rise to publication quality. Reviewers can see what the authors intended, even if they find it insufficient.

### vs. Score 4–5 (avg): "Borderline"
Score 4–5 papers have:
- One or more genuine novel contributions (algorithm, theory, dataset, insight)
- Experiments that are at least partially state-of-the-art
- Reviewers who are split—some see merit, some see gaps—rather than uniformly negative
- Usually some scores in the 4–6 range alongside the rejections

Score 2–3 papers lack the positive reviewers. The strongest advocate for a 2–3 paper typically says "interesting problem" but then adds 4–6 critical weaknesses. There is no reviewer who says "I think this should be accepted."

**The key diagnostic question:** *Do any reviewers want to accept this paper, even conditionally?* If every reviewer wants to reject, it's 2–3 or below.

---

## 5. "This Paper is a Score 2–3 Because..." Templates

Use these to justify a 2–3 score. Each template is grounded in recurring reviewer patterns from the papers above.

---

**Template A: Pure Application Without Novelty**
> "This paper applies [established method] to [new domain/environment/dataset] without introducing any novel algorithmic component, theoretical analysis, or surprising empirical finding. The authors demonstrate that the existing method works in the new setting, but this observation is neither unexpected nor sufficiently significant for a top AI conference. Contribution scores across all reviewers were 1–2/5, and the paper reads as an engineering report rather than a research contribution."

---

**Template B: Incremental Empirical Study**
> "The paper presents controlled experiments showing [finding], but the contribution is incremental—the conclusions are intuitive extensions of existing work and the experimental scope (only [N] tasks/models/datasets) is insufficient to support the general claims made. No new algorithm or theoretical framework is introduced. Reviewers noted that the core experimental design closely mirrors prior work ([cite]) without clear differentiation."

---

**Template C: Missing State-of-the-Art Baselines**
> "The paper's evaluation is disconnected from the current state of the field. Key recent baselines ([cite examples from reviews]) are absent, and the included comparisons use [classical/outdated methods] that do not represent strong modern alternatives. Without comparison to the appropriate state-of-the-art, the empirical contribution cannot be evaluated. This alone is a clear reject signal at ICLR/NeurIPS."

---

**Template D: Unrealistic Modeling Assumptions**
> "The proposed framework depends on [key assumption], which is not grounded in reality—there is no described mechanism for estimating or observing this quantity in practice, and the paper provides no empirical validation of the assumption. The entire contribution is contingent on this assumption holding, making the practical impact of the work unclear or nil. Reviewers consistently flagged this as a foundational weakness."

---

**Template E: Technical Triviality**
> "The technical contribution reduces to [standard algorithm/result], which is a well-known solution (e.g., [textbook reference / well-known prior work]). The paper presents this as novel, but reviewers with expertise in [relevant area] independently identified the reduction as immediate and non-surprising. The 'novel' algorithm is an instance of a 1950s result reframed in new notation."

---

**Template F: Impenetrable Presentation Destroying Evaluation**
> "While the paper may contain valid technical content, it fails to communicate that content to its target audience. Reviewers could not evaluate the novelty or correctness of the contribution because the writing lacks definitions, motivation, and context. Multiple reviewers noted the writing style is 'impenetrable,' with dense notation, missing intuition, and terminology used without explanation. A paper that cannot be understood by its reviewers cannot be accepted."

---

**Template G: Wrong Venue / Insufficient ML Contribution**
> "The paper's core content is [combinatorial optimization / human-subjects study / domain-specific engineering] with minimal connection to the machine learning methods, theory, or datasets expected at [ICLR/NeurIPS]. The 'ML conference' context is used as a framing device rather than an integral part of the contribution. This paper would be better suited to [a specialized workshop / a domain venue / a CS theory track]."

---

**Template H: Narrow Scope + Single Environment/Dataset**
> "The paper's empirical claims are based on experiments in a single [environment / dataset / model family], making it impossible to determine whether the observations generalize. All experiments are performed on [specific narrow scope], and no comparison to standard benchmarks from [relevant area] is provided. The lack of external validity severely limits the significance of the contribution."

---

**Template I: LLM-Suspected Writing with Proof Gaps**
> "Reviewers raised concerns about the rigor of the formal proofs. Key claims ([Theorem X, Proposition Y]) have proofs that are too brief (1–3 lines) to be convincing for the non-trivial claims being made. Additionally, the writing style is described as 'superficially formal but lacking intuition,' with dense series of technical statements without narrative motivation. This combination—brief proofs for hard claims, impenetrable writing—suggests the paper's mathematical apparatus has not been fully verified."

---

**Template J: Engineering Contribution Without Innovation**
> "The proposed system combines [existing component A] + [existing component B] in a straightforward pipeline. The contribution is a working implementation of a practical system, but the technical components (e.g., [Random Forest classifier, BM25 retrieval, standard LP relaxation]) are standard and dated. The paper demonstrates that the system functions, not that it advances the state of knowledge. At top venues, engineering contributions require either significant scale, surprising results, or a dataset/benchmark contribution to justify acceptance."

---

## 6. Score 2–3 Calibration Summary

| Dimension | Score 2–3 Papers |
|---|---|
| **Novelty** | Mostly 1–2/5; no new algorithm, theory, or insight |
| **Experimental rigor** | 1–2 datasets, no SOTA baselines, often single model |
| **Technical soundness** | Often mechanically correct but trivial or unverified |
| **Presentation** | Ranges from mediocre to completely impenetrable |
| **Reviewer consensus** | Uniform reject (all or nearly all reviewers: 0–3) |
| **Typical decision** | Reject (occasionally accept due to 1 outlier reviewer) |
| **Distinguishing from borderline** | No advocate reviewer; no conditional accept path |

**When you see these signals, assign 2–3, not 4–5:**
1. All reviewers cite "limited novelty" as a primary weakness
2. No comparison to SOTA methods from the past 1–2 years
3. Experiments on 1–2 narrow datasets/environments
4. No theoretical grounding for empirical claims
5. Core technical contribution is a standard textbook result reframed
6. Paper explicitly described as "engineering report" or "application of existing method"
7. Impenetrable writing with multiple reviewers unable to assess the contribution

**When you should NOT assign 2–3 (push toward 4–5):**
- At least one reviewer wants to accept (even conditionally)
- The method beats SOTA on at least one important benchmark
- A genuinely novel dataset, benchmark, or evaluation protocol is introduced
- The theoretical contribution is formally correct and non-trivial even if the applications are limited
- The paper has clear empirical breadth (5+ datasets, multiple baselines, statistical testing)
