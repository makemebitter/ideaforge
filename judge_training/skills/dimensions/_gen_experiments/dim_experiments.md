# Dimension Skill: Experiments

This skill file teaches an AI judge how to evaluate the **experiments** dimension of a research paper on a 1–4 scale. It is self-contained and loaded dynamically at evaluation time.

---

## 1. What "Experiments" Means in Peer Review

### Definition

The **experiments** dimension assesses the empirical evidence a paper provides to support its claims. It answers the question: *Does the paper's experimental work convincingly validate its contributions?*

This includes:

- **Scope and coverage** — Are the right benchmarks, datasets, and baselines chosen? Does evaluation cover the paper's main claims, or only cherry-picked favorable cases?
- **Rigor and reproducibility** — Are experimental setups described clearly enough to reproduce? Are hyperparameters, seeds, and evaluation protocols reported?
- **Comparison fairness** — Are baselines up-to-date, fairly tuned, and representative of the field? Are ablations provided?
- **Statistical validity** — Are results reported with uncertainty (standard deviations, confidence intervals, multiple runs)? Are differences meaningful, not just numerical?
- **Completeness relative to claims** — If the paper makes broad claims, are those claims tested broadly? If a method is claimed to be efficient, is its efficiency measured?
- **Analysis depth** — Beyond tables of numbers, do experiments illuminate *why* the method works? Are failure modes discussed?

### What Reviewers Look For

Reviewers ask themselves:
- Do the experiments actually test what the paper claims?
- Are comparisons fair and against the strongest relevant baselines?
- Could the conclusions be reversed with different experimental choices?
- Are there gaps between the claims and what is measured?
- Does the paper acknowledge limitations and negative results honestly?

### Important Context: Theory Papers

For primarily theoretical papers (complexity results, statistical learning theory, proofs of convergence), experiments are not always required. Reviewers will note their absence but may not penalize heavily if the theoretical results are self-contained. Example: in the "Barely Random Algorithms" paper (soundness=4.0), one reviewer wrote: *"There is no experimental analysis. It is understandable that the work is mainly theoretical."* The score remains high because the deficit is understood and the theoretical contribution stands alone. An AI judge must account for this — the experiments score should be interpreted relative to what is expected for the paper type.

---

## 2. Score 1 — Poor Experiments

### What This Looks Like

Score 1 experiments are fundamentally inadequate. The empirical work fails to support the paper's core claims in one or more critical ways:

- Baselines are missing, outdated, or not cited (even when state-of-the-art comparisons are standard in the subfield)
- The method is evaluated on a single toy or simulation environment with no path to real-world validity
- Key metrics are missing (e.g., a paper claiming efficiency never measures latency or FLOPs)
- Experimental setup is opaque — no detail on datasets, splits, hyperparameters, or evaluation protocols
- Scale is grossly insufficient — a tiny benchmark that cannot support the paper's broad claims
- Claims of novelty are not backed by comparisons to prior work the paper itself cites

### Common Patterns

- "Simulation-only" with highly homogeneous settings that do not stress-test the method
- Comparisons only against weak or outdated baselines, ignoring recent competitive work
- Self-reported superiority without ablations to isolate what actually drives improvement
- Missing runtime/memory analysis when the paper claims efficiency

### Real Reviewer Quotes (from LOW-scored examples)

From **BINR-MAPF** (soundness=1.0):
> *"The approach itself seems rather weak compared to existing large-scale imitation learning and hybrid methods."*
> *"Outperforming PIBT while it seems PIBT already handles much larger cases. The comparison seems limited and may be misleading."*

From **BINR-MAPF** (soundness=2.0):
> *"It is not clear how this approach compares with many other bio-inspired algorithms (ant colony, particle swarm, etc.)."*
> *"The Related Work section seems to be quite outdated and very limited. MAPPO-MAPF is mentioned but not cited."*
> *"Experiments are simulation-only with homogeneous, low-complexity scenarios."*

From **T2VTextBench** (soundness=2.0):
> *"The current benchmark includes only 73 prompts, which seems too small to be representative or authoritative. It is unclear how these 73 prompts were designed."*
> *"The evaluation is produced only by manual inspection, so inter-annotator disagreement is inevitable, and future models cannot be reproduced or compared."*

From **CAT: Post-Training Quantization** (soundness=2.0):
> *"The paper does not provide any analysis of the inference-time overhead introduced by CAT. Although PCA and cluster assignment are claimed to be lightweight, they may still incur noticeable latency."*

From **Linearly Decoding Refused Knowledge** (soundness=2.0):
> *"The analysis is strictly empirical and would be strengthened by a theoretical or mechanistic explanation."*
> *"The research relies on manually constructed data, which limits its generalizability."*

### Score 1 Threshold

Assign score 1 when:
- There are **no meaningful baselines** against relevant prior work
- The evaluation **cannot possibly support** the paper's primary claim even in principle
- The experimental setup is so narrow or flawed that conclusions are unreliable
- The paper makes efficiency or scalability claims but provides **zero quantitative evidence**

---

## 3. Score 2 — Below Average Experiments

### What This Looks Like

Score 2 experiments show effort but have **significant gaps** that undermine confidence in the results. The experiments are present and not entirely wrong, but are missing something important enough that a reviewer would require major revisions:

- Baselines exist but are incomplete or not the strongest available
- Key ablations are missing, so it is unclear what component drives the improvement
- Evaluation covers some claims but ignores others (e.g., accuracy is measured but not efficiency, or one task is tested but broad claims are made)
- The experimental scale is insufficient given the claim scope (e.g., evaluating only on small models when claiming general applicability)
- Statistical rigor is weak — single runs, no confidence intervals, or small margins that may not be significant
- Inference-time or deployment costs are unaddressed despite being central to the paper's motivation
- Manual annotation is used without inter-annotator agreement or reliability measures

### Common Patterns

- "Works in simulation, not tested on real hardware"
- "Ablation is missing" — cannot attribute performance gain to the proposed component
- "Only small models tested" when broader applicability is claimed
- Benchmark too small or narrowly designed to support conclusions
- Latency/memory overhead claimed to be negligible but not measured

### Real Reviewer Quotes (from LOW-scored examples with score 2 signals)

From **CAT: Post-Training Quantization** (soundness=2.0):
> *"The paper discusses parameter overhead but provides no analysis of the computational (latency) cost introduced by the CAT-specific steps during inference (PCA projection, cluster assignment, and affine correction). This is a notable omission given that deployment efficiency is a core motivation."*

From **T2VTextBench** (soundness=2.0):
> *"The paper's core weakness is poor verifiability and scalability: the evaluation is produced only by manual inspection... future models cannot be reproduced or compared."*
> *"The benchmark covers a comprehensive set of models" — this is a strength, but the scale and protocol undermine it.*

From **Linearly Decoding Refused Knowledge** (soundness=2.0):
> *"The paper evaluates only small models (2B, 6B, 9B) from just two model families (Gemma and Yi). This is insufficient to support the broad claims about aligned language models in general."*

From **BINR-MAPF** (soundness=2.0):
> *"No theoretical analysis of convergence, stability, or collision guarantees. Experiments are simulation-only with homogeneous, low-complexity scenarios."*

### Score 2 Threshold

Assign score 2 when:
- The experiments are real and non-trivial, but **one major gap** significantly weakens the claimed conclusions
- Baselines are present but the most important comparisons are missing
- The paper's central practical claim (efficiency, generality, robustness) is **not directly measured**
- The evaluation scope is clearly narrower than the paper's stated claims

---

## 4. Score 3 — Good Experiments

### What This Looks Like

Score 3 experiments are **solid and convincing** for the main claims, with only minor gaps or limitations. A reviewer finds the experimental section generally satisfying but can identify specific improvements:

- Baselines are up-to-date and fairly represented
- Results are reported on standard benchmarks for the subfield
- Ablations are present and informative
- The setup is reproducible with the detail provided
- Minor gaps: perhaps one additional dataset would strengthen generality, or uncertainty estimates are missing in some tables, or one efficiency metric was not reported
- The experiments clearly support the paper's main thesis, even if they do not resolve every edge case

### Common Patterns

- Strong core experiments with minor extensions missing
- Good baseline comparison, but not exhaustive
- Theory validated by experiments, though with simplifying assumptions noted
- Ablations present, but not for every component

### Real Reviewer Quotes (from MID-scored examples)

From **Revisiting Prefix-tuning** (soundness=3.0):
> *"The experiments on several tasks demonstrate the theoretical analyses."* [strength]
> *"The study is limited to specific configurations, leaving questions on broader applicability to different model types and prompt architectures."* [weakness]
> *"While theoretically sound, the real-world implications remain uncertain."*

From **Revisiting Prefix-tuning** (soundness=3.0):
> *"Demonstrates empirical improvements across multiple tasks and architectures."* [strength]
> *"The beginning of Section 4 highlights the simplification of the theoretical analysis... focusing only on the first head."* [scope limitation]

From **Linearly Decoding Refused Knowledge** (soundness=3.0):
> *"The paper introduces an interesting experiment transferring probes from base models to aligned models, providing direct evidence that representations of refused knowledge persist through instruction tuning."* [strength]
> *"The contribution and scope of experiments are very limited to the point where I think the paper likely requires additional content."* [weakness at the margin]

From **BINR-MAPF** (soundness=3.0):
> *"Strong motivation grounded in distributed robotics challenges. The reflex-based local control is conceptually clean and scalable."* [strength]
> *"No theoretical analysis of convergence, stability, or collision guarantees."* [gap that keeps it from score 4]

### Score 3 Threshold

Assign score 3 when:
- The experiments are **convincing for the main claims** but have **identifiable gaps** that a reviewer would note
- The core evaluation is complete; missing pieces are secondary or would strengthen (not rescue) the paper
- Baselines are appropriate; no egregious omissions
- Results are reproducible in principle with minor effort
- The paper does not over-claim relative to what the experiments show

---

## 5. Score 4 — Excellent Experiments

### What This Looks Like

Score 4 experiments are **exemplary**. Reviewers struggle to identify meaningful weaknesses. The experimental section:

- Covers all major claims with appropriate benchmarks and baselines
- Includes rigorous ablations isolating each component's contribution
- Reports results with statistical measures (error bars, multiple runs)
- Addresses efficiency, scalability, or robustness where relevant
- Anticipates potential objections and provides counter-evidence
- Goes beyond standard evaluation to provide novel analysis or insights
- Is reproducible in detail (code often released, hyperparameters fully specified)

For theoretical papers: either strong experiments complement the theory, or the theoretical results are so complete and rigorous that the absence of experiments is justified and noted as acceptable.

### Common Patterns

- Comprehensive benchmark suite covering in-distribution and out-of-distribution settings
- Thorough ablation table isolating every design decision
- Timing and memory benchmarks alongside accuracy
- Comparison with all major competing methods, including the strongest recent baselines
- Discussion of failure cases and limitations

### Real Reviewer Quotes (from HIGH-scored examples)

From **AlgoPerf Training Benchmark** (soundness=4.0):
> *"The paper summarizes and analyzes the results of the AlgoPerf Training benchmark, providing a valuable focal point to the community for driving future progress in training algorithms."*
> *"I have no notable concerns about the paper."*

From **SPIN: Self-Supervised Prompt Injection** (soundness=4.0):
> *"It is novel to detect jailbreakings by prompt injections. The method is well motivated to construct a task where we know the ground truth, and judge using a loss function whether the redirected input steers the model towards the injected prompt."*

From **Buckingham π-Invariant Test-Time Projection** (soundness=4.0):
> *"The method leverages Buckingham π-theorem and addresses OoD problem innovatively from a structured perspective."*
> Reviewer noted clarity concerns about figures/algorithms, but no concerns about the sufficiency or rigor of experiments.

From **GLinSAT** (soundness=4.0):
> *"It will be helpful for the readers if there is a 'discussion' section... on the trade-off."* — the only notable weakness is a suggestion for a discussion section, not a gap in experiments.

From **Fairness-Aware Estimation of Graphical Models** (soundness=4.0):
> *"The optimality analysis requires the convexity of the loss function, and it remains unclear how the performance would be affected if the loss function were non-convex."* — this is a theoretical scope question, not a missing experiment.

From **Barely Random Algorithms** (soundness=4.0, theoretical paper):
> *"All results are rigorously proven, but there is also a lot of intuition and high-level guiding of the reader."*
> *"There is no experimental analysis. It is understandable that the work is mainly theoretical, but one suggestion would be to expand on the application discussed in Remark 2.3."* — reviewer explicitly acknowledges the absence is acceptable.

### Score 4 Threshold

Assign score 4 when:
- Reviewers find **no significant experimental weaknesses**
- Any noted gaps are minor suggestions, not concerns that undermine conclusions
- For empirical papers: evaluation is broad, rigorous, and reproducible
- For theoretical papers: absence of experiments is explicitly understood as appropriate, and theoretical rigor substitutes

---

## 6. Red Flags and Green Flags

### Red Flags (push score down)

**Instant score 1–2 indicators:**
- "Simulation-only with no real-world testing" for a paper claiming practical applicability
- "Only compared to [outdated baseline from 2019]" when recent strong baselines exist
- "73 prompts" / tiny benchmark for a paper claiming to establish a new evaluation standard
- "No ablation" — cannot tell which component drives the improvement
- "No runtime or memory analysis" when the paper's motivation is efficiency
- "Manually annotated with no inter-annotator agreement reported"
- "Evaluated only on [one model family / one language / one domain]" when the claim is general
- "Related work is outdated" — often correlates with outdated baselines
- Experiments in appendix are missing entirely; main paper tables have cherry-picked results
- Error bars / standard deviations absent across all reported results

**Contextual red flags (require judgment):**
- "Simulation-only" is acceptable for some robotics/RL papers if real-world transfer is not claimed
- "Small model evaluation" is acceptable if the paper explicitly scopes to small models
- "No ablation" is less damning for benchmark/analysis papers than for method papers

### Green Flags (push score up)

**Instant score 3–4 indicators:**
- "We compare against all major baselines including [most recent competitive method]"
- "We provide ablations isolating each design choice in Table X"
- "Results averaged over [N] seeds with standard deviations"
- "We release code and data at [URL]"
- "We test on [diverse set of benchmarks/domains/model sizes]"
- "We include a failure analysis section"
- "Inference-time overhead is measured in Table Y and is negligible"
- "We test out-of-distribution performance in addition to in-distribution"
- For benchmark papers: "Inter-annotator agreement is measured at κ=0.82"
- For theory papers: Reviewer explicitly writes "the theoretical results are rigorous and self-contained"

---

## 7. Cross-Topic Patterns: How Experiment Expectations Differ by Research Area

### Machine Learning / Deep Learning (Empirical)

**Expectation level: High**

- Must compare against recent strong baselines on standard benchmarks (ImageNet, GLUE, etc.)
- Ablations are essentially required
- Multiple runs with statistical significance expected
- Efficiency (FLOPs, parameters, inference time) expected alongside accuracy
- OOD evaluation increasingly expected

**Common failure modes:**
- Evaluating only on one dataset when the method claims generality
- Missing ablations — reviewers will always ask "which part actually helps?"
- Ignoring recent strong baselines published in the last 1-2 years

Example: **CAT (PTQ)** loses credibility because it claims efficiency but provides no latency measurement. **Prefix-tuning** paper gets score 3 (not 4) because its empirical scope is limited to configurations that validate its theoretical simplifications.

### Theoretical Computer Science / Combinatorics / Online Algorithms

**Expectation level: Low to None**

- Experimental validation is *not* required if the theoretical results are complete
- Reviewers understand this and will note absence without penalizing heavily
- Simulation experiments are welcomed as supplementary but not required
- Score 4 is achievable with zero experiments if the proofs are rigorous and complete

Example: **Barely Random Algorithms** receives soundness=4.0 despite no experiments. One reviewer even says experimental validation would be "nice to have" but the absence is fully understandable.

### NLP / Language Models

**Expectation level: High, with specific concerns**

- Model diversity: evaluating on only 1-2 model families is insufficient for broad claims
- Scale diversity: evaluating only on small models (2B, 9B) does not support claims about "aligned language models in general"
- Safety/alignment papers: probing experiments need careful controls and large-scale validation
- Benchmark papers: human annotation requires inter-annotator reliability metrics

Example: **Linearly Decoding Refused Knowledge** gets score 2-3 across reviewers primarily because of narrow model evaluation (only Gemma and Yi, only small sizes). The experimental design is not wrong — it is just insufficient in scope relative to the claim.

### Multi-Agent Systems / Robotics

**Expectation level: Medium-High, with simulation vs. real-world nuance**

- Simulation-only is acceptable if the paper does not claim real-world deployment
- However, simulation must cover diverse scenarios, not just homogeneous toy settings
- Comparison to relevant baselines in the MAPF/robotics literature is required
- Scalability experiments (more agents, larger maps) expected for methods claiming scalability

Example: **BINR-MAPF** falls to score 1-2 because (a) simulation only covers low-complexity homogeneous scenarios, (b) comparisons miss recent relevant baselines, and (c) no convergence/stability analysis.

### Benchmark / Evaluation Papers

**Expectation level: Very High on methodology; lower on algorithmic experiments**

- Must justify benchmark design choices: why these prompts/tasks? How were they selected?
- Inter-annotator agreement is essentially required for human annotation
- Reproducibility is critical — automated evaluation enables future comparison; manual-only does not
- Must demonstrate the benchmark discriminates between models meaningfully

Example: **T2VTextBench** scores 2.0 because the benchmark has only 73 prompts (unjustified scale), manual-only annotation (not reproducible), and no reliability metrics. The diversity of models tested is a strength, but cannot compensate for the protocol weaknesses.

### Fairness / Responsible AI

**Expectation level: Medium-High**

- Must test across multiple demographic groups, not just binary protected attributes
- Intersectionality concerns: does the method work across intersecting groups?
- Claims about "fair estimation" require showing fairness *and* accuracy do not degrade severely
- Theoretical optimality results (e.g., "optimal under convexity") need empirical validation on non-convex settings

Example: **Fairness-Aware Estimation of Graphical Models** (soundness=4.0) is penalized mildly — a reviewer notes that performance under non-convex losses is unclear. This keeps the weakness as minor because it is a theoretical scope issue, not a missing core experiment.

---

## 8. Calibration Examples

Use these examples to calibrate your scoring:

| Paper | Score | Key Signal |
|---|---|---|
| AlgoPerf Training Benchmark | 4 | Competition analysis, no notable concerns from any reviewer |
| Barely Random Algorithms (theoretical) | 4 | No experiments, but explicitly appropriate for pure theory |
| GLinSAT | 4 | Only minor "add a discussion section" feedback |
| SPIN Jailbreak Detection | 4 | Novel experimental design, well-validated setup |
| Fairness-Aware Graphical Models | 4 | Minor scope concern (non-convex case), not a missing experiment |
| Revisiting Prefix-tuning | 3 | Experiments support claims but limited to specific configurations |
| BINR-MAPF (bio-inspired) | 3 | Present but simulation-only, no convergence analysis |
| Linearly Decoding Refused Knowledge | 3 | Good design, scope too narrow for the claim |
| CAT Post-Training Quantization | 2 | No latency analysis despite efficiency claims |
| T2VTextBench | 2 | 73-prompt benchmark, manual-only annotation, no reliability metrics |
| BINR-MAPF (weakest review) | 1 | Weak baselines, toy scenarios, no real validation of superiority |

---

## 9. Scoring Decision Tree

Use this decision tree for each paper:

```
1. Is this a pure theory paper with complete proofs?
   YES → Absence of experiments is acceptable.
         Are proofs rigorous and complete? → Score 4 possible.
         Are there notable theoretical gaps? → Score 3.
   NO → Continue.

2. Do experiments directly test the paper's primary claim?
   NO → Score 1 (if completely missing) or Score 2 (if present but wrong target).
   YES → Continue.

3. Are baselines appropriate, up-to-date, and fairly compared?
   NO (major baselines missing) → Score 1–2.
   PARTIAL (minor gaps) → Score 3.
   YES → Continue.

4. Are ablations present (for method papers)?
   NO → Push down 1 point.
   YES → Continue.

5. Is the claim scope matched by evaluation scope?
   NO (e.g., general claim, narrow evaluation) → Score 2–3.
   YES → Continue.

6. Are there statistical validity concerns (no error bars, single run)?
   YES (all results) → Push down to Score 2.
   YES (some results) → Stay at Score 3.
   NO → Continue.

7. Is the paper missing key practical metrics it claims to address (efficiency, latency, memory)?
   YES → Score 2.
   NO → Score 3–4.

8. Do reviewers find no significant weaknesses?
   YES → Score 4.
   NO → Score 3 (if weaknesses are minor).
```

---

## 10. Worked Examples with Reasoning

### Example A: AlgoPerf Benchmark → Score 4

The paper summarizes results from a competition. Every reviewer found no notable concerns. The experiments *are* the paper — the competition itself is the experimental apparatus. Score 4 because: comprehensive real-world evaluation, multiple teams/methods compared, community-validated setup, no cherry-picking possible in a competition setting.

### Example B: Barely Random Algorithms → Score 4

Pure theory paper. Three separate reviewers all agree the results are rigorously proven. One reviewer notes there is no experimental analysis but explicitly says "it is understandable that the work is mainly theoretical." Score 4 because: theory is complete, experiments are not expected for this paper type, and reviewers explicitly accept the absence.

### Example C: T2VTextBench → Score 2

A benchmark paper is judged harshly on experimental methodology. 73 prompts is insufficient for a paper claiming to establish a new benchmark standard. Manual-only annotation means the benchmark cannot be used reliably by future researchers. No inter-annotator agreement reported. Score 2 because: the paper's core contribution (the benchmark) is undermined by the experimental methodology used to build and validate it.

### Example D: Linearly Decoding Refused Knowledge → Score 2–3

Two reviewers score it soundness=2, one scores soundness=3. The experiments are present and the design is interesting (cross-model probe transfer is a genuine novel experiment). But the claim is about "aligned language models in general" while only two small model families are tested. Score 2 from stricter reviewers because narrow scope cannot support the general claim. Score 3 from the more charitable reviewer who values the experimental design despite scope limitations. **AI judge guidance**: when scope is the primary issue, lean toward 2 if the gap is large, 3 if the core experiments are solid and the scope gap is an extension rather than a rescue.

### Example E: BINR-MAPF → Score 1

The approach is evaluated only in simulation with homogeneous low-complexity scenarios. Baselines are missing (MAPPO-MAPF mentioned but not cited or compared). The bio-inspired framing is metaphorical with no biological validation. No convergence analysis. Score 1 because: the experiments cannot support the paper's claims even charitably — the scenarios do not stress-test the method and the comparison set is incomplete.

---

## Summary Reference Card

| Score | One-Line Description | Key Requirement |
|---|---|---|
| 1 | Fundamentally inadequate | Cannot support primary claims; major baselines missing or scenarios too narrow |
| 2 | Present but significantly flawed | Core claim not directly measured, or scope far too narrow for the stated generality |
| 3 | Solid with minor gaps | Main claims supported; identifiable but non-fatal improvements possible |
| 4 | Exemplary or appropriately absent | No significant weaknesses; or theoretical rigor accepted as substitute |
