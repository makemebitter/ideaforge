# Dimension Skill: Reproducibility

## 1. What "Reproducibility" Means in Peer Review

**Definition:** Reproducibility, as evaluated in peer review, refers to whether the paper provides sufficient information for an independent researcher to replicate the work and verify the results. This encompasses:

- **Methodological completeness:** Are algorithms, architectures, hyperparameters, and procedures described with enough precision to reimplement from scratch?
- **Experimental transparency:** Are dataset splits, training/evaluation protocols, random seeds, hardware, and software environments reported?
- **Result verifiability:** Could an independent party run the experiments and expect to obtain approximately the same numbers?
- **Code and data availability:** Is source code, pretrained models, or datasets released (or committed to be released)?
- **Ablations and diagnostics:** Are design choices validated so the reader can understand which components drive the results?
- **Statistical rigor:** Are results reported with variance, confidence intervals, or repeated trials where appropriate?

In practice, reviewers conflate **reproducibility** tightly with **soundness**: if results cannot be reproduced in principle, their validity is uncertain. A paper that scores 4 on soundness almost always has strong reproducibility; a paper scoring 1 or 2 almost always has significant reproducibility gaps.

**Scope distinctions:**
- *Reproducibility* (same team, same code, same data) is distinct from *replicability* (different team, same method) and *generalizability* (new data/settings). Reviewers typically demand reproducibility and often expect replicability, but rarely demand generalizability as a threshold.
- For **theoretical papers**, reproducibility means proof completeness, not code. Gaps in proofs, unjustified lemmas, or hand-wavy steps are the analog of missing experimental details.
- For **benchmark/dataset papers**, reproducibility means annotation protocols, inter-annotator agreement, sampling methodology, and future model evaluation pipelines.
- For **empirical deep-learning papers**, reproducibility means hyperparameter reporting, training curves, variance estimates, and ideally code.

---

## 2. Score 1 — Poor Reproducibility

### What This Looks Like

A score-1 paper has **fundamental reproducibility failures** that make it impossible to verify any core claim. This is rare for papers that passed desk rejection, but it occurs when:

- The method description is so vague that reimplementation is impossible.
- Key experimental settings (datasets, metrics, baselines) are not defined or are inconsistently described.
- Claims are made without any supporting evidence.
- The related work is severely incomplete, making it unclear whether the method is even novel.
- The paper relies on manual inspection or subjective judgment with no inter-rater protocol described.
- Theoretical claims have no proof attempt.

Score-1 papers often have additional problems: the method is poorly motivated, the experiments do not support the claims, or the paper is so unfinished that essential sections are missing.

### Common Patterns

1. **No methodology details:** The paper says "we train a neural network" without specifying architecture, loss, optimizer, or data processing.
2. **No comparison protocol:** Baselines are mentioned without specifying how they were run (same hardware? same data split? hyperparameter-tuned?).
3. **Highly outdated or missing related work:** Reviewers cannot assess novelty, let alone reproduce.
4. **Manual evaluation without protocol:** Results depend on human judgment with no description of how raters were selected, trained, or resolved disagreements.
5. **Claimed results with no experiment section.**

### Real Reviewer Quotes (Score 1)

From **BINR-MAPF** (soundness=1.0):
> "W1: The approach itself seems rather weak compared to existing large-scale imitation learning and hybrid methods. Using an FSM alone is unlikely to achieve competitive results. Still, outperforming PRIMAL is unclear — the comparison is unfair because PRIMAL's performance degrades with more agents while the proposed approach is not evaluated at the same scales."

> "The Related Work section seems to be quite outdated and very limited. MAPPO-MAPF is mentioned but not cited."

**Key insight:** The reviewer cannot verify the comparison because the evaluation protocol is inconsistent. The absence of fair baselines means the central empirical claim cannot be reproduced or trusted.

### Scoring Guidance

Assign Score 1 when:
- You cannot determine how the main experiment was run from the paper alone.
- Core comparisons are demonstrably unfair (different data, different compute, different hyperparameter budgets).
- Essential proof steps are absent or obviously wrong.
- The paper is so incomplete that reproducibility is a secondary concern to basic completeness.

---

## 3. Score 2 — Below-Average Reproducibility

### What This Looks Like

Score-2 papers have **significant but not fatal** reproducibility gaps. The general approach is understandable, but important details are missing such that an independent researcher would need to make non-trivial assumptions or contact the authors. Results may be plausible but cannot be fully verified.

Score-2 is the most common category for papers that raise serious reviewer concerns. The method usually works to some degree, but the experimental setup has material omissions.

### Common Patterns

1. **Limited scope of evaluation hiding generalization:** Experiments cover only a narrow set of models, datasets, or conditions, but claims are stated broadly.
2. **No variance/error bars:** Single-run results reported without uncertainty estimates.
3. **Missing inference-time analysis:** For efficiency papers, runtime/latency overhead not measured.
4. **Simulation-only results with no real-world validation** for robotics or systems papers.
5. **Manual or proprietary data without release plan.**
6. **Ablations missing:** Cannot isolate which component drives performance.
7. **Hyperparameter sensitivity not reported:** The method may require careful tuning that is not disclosed.
8. **No code release and no commitment to release.**

### Real Reviewer Quotes (Score 2)

From **CAT: Post-Training Quantization** (soundness=2.0):
> "The paper does not provide any analysis of the inference-time overhead introduced by CAT. Although PCA and cluster assignment are claimed to be lightweight, they may still incur noticeable latency... Without this analysis, the practical utility of the method remains unclear."

> "The paper discusses parameter overhead but provides no analysis of the computational (latency) cost introduced by the CAT-specific steps during inference (PCA projection, cluster assignment, and affine transformation)."

From **T2VTextBench** (soundness=2.0):
> "The current benchmark includes only 73 prompts, which seems too small to be representative or authoritative. It is unclear how these 73 prompts were designed. What dimensions, attributes, or linguistic structures were considered? Without a principled construction methodology, it is hard to assess the benchmark's coverage and reliability."

> "The paper's core weakness is poor verifiability and scalability: the evaluation is produced only by manual inspection, so inter-annotator disagreement is inevitable, and future models cannot be reproduced and evaluated automatically."

From **Linearly Decoding Refused Knowledge** (soundness=2.0):
> "The paper evaluates only small models (2B, 6B, 9B) from just two model families (Gemma and Yi). This is insufficient to support the broad claims about aligned language models in general."

> "The analysis is strictly empirical and would be strengthened by a theoretical or mechanistic explanation for the observed phenomena. The research relies on manually constructed data, which limits the assessment of generalizability."

From **BINR-MAPF** (soundness=2.0):
> "It is not clear how this approach compares with many other bio-inspired algorithms (ant colony, particle swarm, etc.)."

> "Experiments are simulation-only with hardcoded maps; no real-world or large-scale tests."

### Scoring Guidance

Assign Score 2 when:
- The method is described at a level where an expert could roughly reimplement it, but key hyperparameters, dataset splits, or evaluation protocols are missing.
- Claims are broader than the experimental evidence (e.g., "our method works for LLMs" tested only on 2B models).
- The evaluation relies on human judgment without an inter-annotator agreement protocol.
- Runtime/efficiency claims lack measurements.
- Results are reported as single runs without variance.
- No code is released and no commitment is made.

---

## 4. Score 3 — Good Reproducibility

### What This Looks Like

Score-3 papers are **largely reproducible** with minor gaps. The experimental setup is described well enough that a determined researcher could reproduce results, but there are some omissions, simplifications, or assumptions that would require guesswork or additional work. Theoretical papers at this level have mostly complete proofs with some hand-wavy steps in less central parts.

Score-3 is the most common for solid, publishable work that has not gone the extra mile on reproducibility.

### Common Patterns

1. **Theoretical analysis with acknowledged simplifications:** The paper explicitly states that analysis uses simplified assumptions (e.g., focuses on one attention head, one layer) but justifies why.
2. **Experiments are sound but scope is limited:** The benchmark is reasonable but more datasets would strengthen the claims.
3. **Code not released but method is described completely enough to reimplement.**
4. **Some ablations provided but not exhaustive.**
5. **Variance reported for main results but not all supplementary experiments.**

### Real Reviewer Quotes (Score 3)

From **Revisiting Prefix-tuning** (soundness=3.0):
> "The beginning of Section 4 highlights the simplification of the theoretical analysis ('we focus only on the first head, namely, l = 1 in equation (6), and the first row of the attention in this head'). This raises the question of whether this analysis translates to more general settings. In particular, focusing on one specific head for the analysis is a substantial idealization."

> "The study is limited to specific configurations, leaving questions on broader applicability to different model types and prompt architectures."

> "While theoretically sound, the real-world implications may be limited if the configurations studied do not translate well across architectures."

From **BINR-MAPF** (soundness=3.0, MID category):
> "Lack of theoretical grounding or convergence analysis... provide an analytical discussion (even qualitative) of conditions ensuring conflict-free convergence under the reflex vector composition."

> "The 'bio-inspired' claim is mostly metaphorical; there's no real biological modeling. No theoretical analysis of convergence, stability, or collision guarantees. Experiments are simulation-only with hardcoded maps."

From **Linearly Decoding Refused Knowledge** (soundness=3.0):
> "While I do not find anything in the paper factually wrong, the contribution and scope of experiments are very limited to the point where I think the paper likely requires additional content (experiments, analysis)."

### Scoring Guidance

Assign Score 3 when:
- The methodology is described in enough detail that the work could be reproduced with some effort.
- The experimental scope is reasonable but narrower than the claims.
- Proofs are mostly complete with some acknowledged simplifications.
- Results are reported with appropriate metrics, but variance or ablations could be more thorough.
- Code may or may not be released, but the paper compensates with detailed algorithmic descriptions.

---

## 5. Score 4 — Excellent Reproducibility

### What This Looks Like

Score-4 papers are **fully reproducible**. An independent researcher could implement the method from the paper alone, run the experiments, and expect to obtain comparable results. Theoretical papers at this level have complete, rigorous proofs with clear exposition. Empirical papers provide all hyperparameters, dataset details, evaluation protocols, and ideally code.

Score-4 does **not** require perfection. A paper can score 4 on reproducibility while having minor issues like a typo or a slightly unclear ablation, as long as the core results are fully verifiable.

### Common Patterns

1. **Complete algorithmic description:** Pseudocode or formal algorithm box covers all steps.
2. **Full hyperparameter reporting:** Learning rates, batch sizes, epochs, optimizer details, regularization.
3. **Dataset details:** Source, version, preprocessing, train/val/test splits, number of samples.
4. **Baseline details:** How baselines were run (from paper, from code, re-tuned).
5. **Statistical rigor:** Multiple runs with mean ± std, or theoretical justification for why variance is irrelevant.
6. **Code release** (strongly positive signal, though not strictly required for score 4).
7. **Rigorous proofs** for theoretical claims with complete derivations, not just sketches.
8. **Runtime and resource usage** reported for efficiency claims.

### Real Reviewer Quotes (Score 4)

From **AlgoPerf** (soundness=4.0):
> "The paper summarizes and analyzes the results of the AlgoPerf Training benchmark, providing a valuable focal point to the community for driving future progress in training algorithms."

> "I have no notable concerns about the paper."

*(The near-absence of reproducibility concerns from multiple reviewers is itself a strong signal.)*

From **GLinSAT** (soundness=4.0):
> "Enforcing constraints to the output of neural networks is an important research direction... The major drawback of GLinSAT over LinSAT is that its inference time is longer if LinSAT is set with its default 100 iterations. It will be helpful for the readers if there is a 'discussion' section..."

*(The reviewer's only critique is a suggestion to add a discussion section — all experimental details are present.)*

From **Fairness-Aware Estimation of Graphical Models** (soundness=4.0):
> "The optimality analysis requires the convexity of the loss function, and it remains unclear how the performance would be affected if the loss function were non-convex, which is common in machine learning."

*(The weakness is a theoretical extension request, not a gap in what was actually done.)*

From **Barely Random Algorithms** (soundness=4.0):
> "The paper is very well written. All results are rigorously proven, but there is also a lot of intuition and high-level guiding of the reader. The solution is non-trivial and builds on fairly complex ideas."

> "I don't see any major weaknesses in the presented results or the proofs."

From **SPIN: Self-Supervised Prompt INjection** (soundness=4.0):
> "It is novel to detect jailbreakings by prompt injections. The method is well motivated to construct a task where we know the ground truth, and judge using a loss function whether the redirected input aligns with the injected instruction."

*(No concerns about verification — the method is described precisely enough for the reviewer to follow and validate.)*

### Scoring Guidance

Assign Score 4 when:
- Reviewers raise **no** concerns about missing details or inability to verify results.
- Weaknesses cited are about **extensions or future work**, not about gaps in current claims.
- Theoretical proofs are described as rigorous and complete.
- The experimental setup is described in sufficient detail that reproduction is straightforward.
- Any remaining critiques are about presentation or scope, not verifiability.

---

## 6. Red Flags and Green Flags

### Red Flags (Instant Indicators of Low Reproducibility)

**Methodology red flags:**
- "We train a model on X" with no architecture, hyperparameter, or optimization details.
- Algorithm description is prose-only with no pseudocode or formal notation for a complex method.
- Loss function or objective not stated mathematically.
- Key design choices (e.g., number of clusters, projection dimensions) not reported.

**Experimental red flags:**
- Results from a single run with no variance.
- Baselines compared without specifying whether they were re-run, taken from paper, or re-tuned.
- Dataset not identified by version, split, or preprocessing.
- "Our method is efficient" with no runtime numbers.
- Evaluation metric defined ambiguously or inconsistently.
- Human evaluation without inter-annotator agreement (Cohen's kappa, Fleiss's kappa, or equivalent).
- Small benchmark (e.g., 73 prompts) with no justification of representativeness.
- Claims about "LLMs" or "neural networks" in general tested on 1-2 small models.

**Theoretical red flags:**
- "It can be shown that..." without proof or citation.
- Proof sketch that skips the hard steps.
- Theorem stated with conditions that don't hold in practice, without acknowledgment.
- Analysis restricted to a single attention head/layer justified by "for simplicity" without verification that the result generalizes.

**Code/data red flags:**
- No code released and no commitment to release for an empirical paper.
- Proprietary or unavailable dataset with no plan to release a reproducible version.
- Manual annotation data not released.

### Green Flags (Instant Indicators of High Reproducibility)

**Methodology green flags:**
- Algorithm box with pseudocode covering all steps.
- Hyperparameter table in the appendix.
- Ablation study isolating each component.
- Architecture diagrams with exact dimensions.

**Experimental green flags:**
- Results reported as mean ± std over multiple seeds.
- Baselines run from official code with hyperparameters from original papers.
- Train/val/test split sizes reported.
- Hardware (GPU type, count) and wall-clock time reported.
- Hyperparameter sensitivity analysis included.

**Theoretical green flags:**
- Complete proofs in the appendix with every step justified.
- Explicit statement of all assumptions with discussion of when they hold.
- Proof cross-checked by illustrative examples or simulations.

**Code/data green flags:**
- Code released on GitHub or as supplementary.
- Pretrained model checkpoints available.
- Dataset released under a clear license.
- README with exact commands to reproduce all reported numbers.

---

## 7. Cross-Topic Patterns

### Empirical Deep Learning (CV, NLP, RL)

Reproducibility expectations are **highest** in this area because results are sensitive to hyperparameters, random seeds, hardware, and data ordering. Reviewers specifically look for:
- Multiple seeds (at least 3-5) for variance.
- Compute budget parity across baselines.
- Code release (now standard at top venues).
- Exact model sizes, training steps, and data quantities.

A common failure mode is comparing against baselines taken from prior papers without re-running in the same environment, which can introduce systematic biases from hardware, library versions, or data preprocessing differences.

### Theoretical Computer Science / Algorithms

Reproducibility means **proof completeness**. Code is often irrelevant. Reviewers focus on:
- Are all lemmas proven (or cited if known)?
- Are the assumptions stated and justified?
- Is the problem formulation standard enough to be unambiguous?

The **Barely Random Algorithms** paper is exemplary: multiple reviewers note "all results are rigorously proven" and "I don't see any major weaknesses in the presented results or the proofs." The paper scores soundness=4 despite having no experiments, because for this type of work, proof completeness is the only reproducibility criterion.

Theoretical simplifications (e.g., "we analyze the first attention head only") are acceptable if:
1. The simplification is explicitly acknowledged.
2. There is empirical or theoretical reason to believe the simplified analysis extends.
3. The main claims are qualified accordingly.

They are **not** acceptable if the paper makes general claims that the simplified analysis cannot support.

### Benchmark and Dataset Papers

Reproducibility criteria are **specialized**:
- How were prompts/instances constructed? (Coverage, diversity, difficulty calibration)
- How were annotations collected? (Worker selection, training, quality control)
- Inter-annotator agreement reported?
- Can future work evaluate on this benchmark automatically, or does it require manual inspection?
- Is the benchmark released?

The **T2VTextBench** paper fails on most of these. With 73 prompts and purely manual evaluation, "future models cannot be reproduced and evaluated automatically." This is a fundamental reproducibility failure for a benchmark paper.

A benchmark paper that does not release the benchmark, does not report inter-annotator agreement, and does not provide an automatic evaluation pipeline should score 1-2 on reproducibility regardless of the novelty of the benchmark design.

### Systems and Robotics

Key considerations:
- Simulation vs. real-world: simulation-only results are less reproducible in practice because simulation environments may differ.
- Hardware specs: results on a specific robot platform may not transfer.
- Convergence guarantees: for learning-based systems, does the training reliably converge, or are results cherry-picked runs?

**BINR-MAPF** is a clear example of reproducibility failures for a systems paper: "Experiments are simulation-only with hardcoded maps; no real-world or large-scale tests" and "No theoretical analysis of convergence, stability, or collision guarantees."

### Security / Interpretability Empirical Papers

These papers often work with restricted or sensitive data (e.g., jailbreak prompts, proprietary models). Reviewers recognize this constraint but still expect:
- Clearly described methodology for constructing test cases.
- Protocol for how alignment/refusal was measured.
- Multiple model families tested to assess generality.
- Transfer experiments run with defined protocols.

**Linearly Decoding Refused Knowledge** fails because it tests only 2B-9B models from 2 families, uses manually constructed data without a systematic protocol, and makes broad claims about "aligned language models in general."

---

## 8. Calibration Summary

| Score | Characterization | Key Signals |
|-------|-----------------|-------------|
| 1 | Fatal reproducibility gap | Cannot determine how main experiment was run; unfair comparisons; missing proof attempts; purely subjective evaluation with no protocol |
| 2 | Significant gap | Narrow evaluation scope with broad claims; no variance; missing runtime analysis; manual evaluation without IAA; no code and no commitment |
| 3 | Good, minor gaps | Method reproducible with effort; some simplifications acknowledged; scope somewhat narrow; code not released but details sufficient |
| 4 | Excellent | Reviewers raise no missing-detail concerns; rigorous proofs or complete experimental specs; critiques are about extensions, not verifiability |

**Decision rule:** When a reviewer's weakness section focuses on *what the paper doesn't claim* (extensions, future work, additional experiments that would be nice) rather than *gaps in what it does claim*, that is strong evidence for Score 4. When weaknesses focus on *missing details needed to understand or reproduce the existing claims*, that is evidence for Score 2 or below.

**Theoretical vs. empirical papers:** Do not penalize theoretical papers for lacking experiments unless the paper itself makes empirical claims. Do not give empirical papers a pass for lacking statistical rigor just because the method is novel. The relevant reproducibility standard is determined by the claims the paper makes, not the area it is in.
