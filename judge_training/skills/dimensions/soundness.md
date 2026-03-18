# Dimension Skill File: **Soundness**

*Self-contained reference for AI judges evaluating the soundness dimension of research papers.*

---

## 1. What "Soundness" Means in Peer Review

**Soundness** measures whether the paper's claims are justified by the evidence, methods, and reasoning presented. It is distinct from novelty or impact — a paper can be highly original yet unsound, or moderately novel yet perfectly sound. Soundness asks:

> *Can we trust that the conclusions follow from the work?*

### Core Components of Soundness

**A. Technical/Methodological Correctness**
- Are the methods properly defined and applied?
- Are theoretical proofs correct, complete, and without hidden gaps?
- Are experimental protocols appropriate for the claims being made?
- Are assumptions stated and justified?

**B. Empirical Validity**
- Do experiments actually test what the paper claims to test?
- Are baselines appropriate, fairly implemented, and competitive?
- Is the evaluation setup free from data leakage, cherry-picking, or other confounds?
- Is statistical significance reported where relevant?

**C. Scope Alignment**
- Are the conclusions scoped appropriately to the actual evidence?
- Does the paper avoid overgeneralizing from limited settings?
- Are limitations acknowledged honestly?

**D. Consistency and Internal Coherence**
- Are claims in the introduction consistent with what is demonstrated?
- Do the results actually support the abstract/conclusion?
- Are there unexplained contradictions or anomalies?

**E. Experimental Completeness**
- Are ablations sufficient to isolate the contribution?
- Are failure modes analyzed or at least acknowledged?
- Is the computational/inference cost analyzed when relevant?

### What Soundness Is NOT

- Soundness is **not** novelty — a well-known technique applied correctly is sound.
- Soundness is **not** impact — a niche result can be perfectly sound.
- Soundness is **not** clarity — a paper can be poorly written but technically correct.
- Soundness is **not** significance — a minor result soundly proven is sound.

### The 1–4 Scale in Practice

| Score | Label | Core Meaning |
|-------|-------|--------------|
| 4 | Excellent | Claims fully justified; methodology rigorous; no notable gaps |
| 3 | Good | Mostly sound with minor gaps or limitations; core claims hold |
| 2 | Below Average | Notable technical gaps, limited scope, or unsupported claims |
| 1 | Poor | Fundamental methodological flaws; claims unsupported or incorrect |

---

## 2. Score 1 — Poor Soundness

### What This Looks Like

Score-1 papers have **fundamental flaws** that undermine the core claims. These are not minor gaps — they are problems that make the central contribution questionable or incorrect.

**Characteristic patterns:**
- The proposed method is empirically weaker than existing baselines but claims superiority
- Experimental comparisons are not apples-to-apples (different settings, missing baselines)
- Theoretical claims are made without any proof or formal justification
- The approach is described at such a high level that reproducibility is impossible
- Core experiments contradict the paper's central claim

### Real Reviewer Evidence (Score 1)

From the **BINR-MAPF** paper (rating=3.6, soundness=1.0):

> *"W1: The approach itself seems rather weak compared to existing large-scale imitation learning and hybrid methods. Using an FSM alone is unlikely to achieve competitive results."*

> *"The Related Work section seems to be quite outdated and very limited. MAPPO-MAPF is mentioned but not cited. What is the connection to other swarm-based algorithms (if any), for example, to this one...?"*

**Key signals in score-1 reviews:**
- Direct statement that the method underperforms prior work
- Missing or outdated related work that would reveal prior art that invalidates claims
- No theoretical grounding for safety/convergence claims
- Experimental evaluation described as too weak to support claims

### How to Identify Score 1

Ask yourself:
1. If the main baseline outperforms the proposed method, is there a satisfying explanation? If not → score 1 candidate.
2. Are the experiments so limited (toy settings, no ablations, no comparisons) that nothing is actually demonstrated? → score 1 candidate.
3. Does the paper make strong claims (e.g., "provably safe," "theoretically optimal") with no formal support? → score 1 candidate.
4. Would a practitioner find the paper unreproducible due to missing details? → score 1 candidate.

---

## 3. Score 2 — Below Average Soundness

### What This Looks Like

Score-2 papers have **notable but not fatal** methodological gaps. The core idea may be valid, but the evidence presented is insufficient to support the strength of the claims. Reviewers at this level often say the paper is interesting but under-developed.

**Characteristic patterns:**
- Experiments are too narrow (few models, few datasets, small scale) to support general claims
- Key costs (inference time, parameter overhead) analyzed partially or not at all
- Empirical results with no theoretical motivation or vice versa
- Manual/human evaluation without inter-annotator agreement or reproducibility protocol
- Claims about "aligned language models in general" based on 2-3 small models
- Bio-inspired or biological claims that are purely metaphorical with no actual modeling

### Real Reviewer Evidence (Score 2)

From **BINR-MAPF** (soundness=2.0):

> *"It is not clear how this approach compares with many other bio-inspired algorithms (ant colony, particle swarm, etc.)..."*

> *"There is some novelty in considering biological behaviors."* [strengths — but this alone isn't enough]

From **Linearly Decoding Refused Knowledge** (soundness=2.0):

> *"The analysis is strictly empirical and would be strengthened by a theoretical or mechanistic explanation for the observed phenomena."*
> *"The research relies on manually constructed data, which limits generalizability."*
> *"The paper evaluates only small models (2B, 6B, 9B) from just two model families (Gemma and Yi). This is insufficient to support the broad claims about aligned language models in general."*

From **CAT: Post-Training Quantization** (soundness=2.0):

> *"The paper does not provide any analysis of the inference-time overhead introduced by CAT. Although PCA and cluster assignment are claimed to be lightweight, they may still incur noticeable latency..."*
> *"The paper discusses parameter overhead but provides no analysis of the computational (latency) cost introduced by the CAT-specific steps during inference (PCA projection, cluster assignment, and affine transform)."*

From **T2VTextBench** (soundness=2.0):

> *"The current benchmark includes only 73 prompts, which seems too small to be representative or authoritative. It is unclear how these 73 prompts were designed."*
> *"The evaluation is produced only by manual inspection, so inter-annotator disagreement is inevitable, and future models cannot be reproduced on the benchmark."*

### How to Identify Score 2

Ask yourself:
1. Is the evaluation so narrow (small models, one dataset, simulation-only) that the claims are overstated? → score 2 candidate.
2. Does the paper ignore a relevant cost or metric that would be expected (inference latency, memory, inter-annotator agreement)? → score 2 candidate.
3. Are important comparisons missing that would be necessary to interpret the results? → score 2 candidate.
4. Is the theoretical/empirical support one-sided (all theory, no experiments, or all experiments, no theory) in a field where both are expected? → score 2 candidate.

### Score 2 vs Score 1

The critical distinction: in score-2 papers, the core idea and some evidence are there — reviewers say "interesting but incomplete." In score-1 papers, reviewers say "the core claim itself is not supported or is wrong." If the paper's central contribution is questionable, lean toward 1; if the contribution plausible but under-evidenced, lean toward 2.

---

## 4. Score 3 — Good Soundness

### What This Looks Like

Score-3 papers are **mostly sound** — the core claims are supported by the evidence, but there are meaningful limitations, simplifications, or gaps that prevent full confidence. Reviewers at this level acknowledge solid work while pointing to specific concerns that would need to be addressed for full endorsement.

**Characteristic patterns:**
- Theoretical analysis relies on simplifying assumptions that may not hold in practice
- Experiments are comprehensive but miss one or two important ablations or baselines
- The work is empirically demonstrated but lacks theoretical grounding
- Scope is narrower than the claims suggest (e.g., attention to "first head only")
- Results need more visual/qualitative evidence to be fully convincing
- Claims hold within tested settings but generalizability is uncertain

### Real Reviewer Evidence (Score 3)

From **Revisiting Prefix-tuning** (soundness=3.0):

> *"The beginning of Section 4 highlights the simplification of the theoretical analysis ('we focus only on the first head, namely, l = 1 in equation (6), and the first row of the attention in this head')."*

> *"My main concern is about the technical contribution of the paper. Since [technique X] is well known, the theoretical contribution seems incremental."*

> *"The study is limited to specific configurations, leaving questions on broader applicability to different model types and prompt architectures."*

From **BINR-MAPF** (soundness=3.0):

> *"Lack of theoretical grounding or convergence analysis. Provide an analytical discussion (even qualitative) of conditions ensuring conflict-free convergence under the reflex vector comp..."*

> *"The 'bio-inspired' claim is mostly metaphorical; there's no real biological modeling. No theoretical analysis of convergence, stability, or collision guarantees. Experiments are simulation-only with highly variable outcomes."*

> *"Strong motivation grounded in distributed robotics challenges (latency, bandwidth). The reflex-based local control is conceptually clean and scalable."* [positive signal — core is credible]

From **Linearly Decoding Refused Knowledge** (soundness=3.0):

> *"The paper introduces an interesting experiment transferring probes from base models to aligned models, providing direct evidence that representations of refused knowledge persist through instruction tuning."*

> *"While I do not find anything in the paper factually wrong, the contribution and scope of experiments are very limited to the point where I think the paper likely requires additional content."*

### How to Identify Score 3

Ask yourself:
1. Are the core claims justified within a narrower scope than the paper suggests? → score 3.
2. Is there one important gap (missing baseline, missing ablation, simplified assumption) but everything else checks out? → score 3.
3. Does the theoretical analysis make simplifying assumptions that are stated but significant? → score 3.
4. Is the empirical evidence solid but the theoretical justification thin (or vice versa)? → score 3.

### Score 3 vs Score 2

The key difference is whether the core claims hold. In score-3 papers, reviewers say "the main contribution is valid, but here's what's missing." In score-2 papers, reviewers say "the main contribution may be valid, but the evidence is too limited to tell." If reviewers find nothing factually wrong but note limited scope → score 3. If reviewers find the scope so limited that the conclusion is unjustified → score 2.

---

## 5. Score 4 — Excellent Soundness

### What This Looks Like

Score-4 papers have **no notable soundness concerns**. The claims are fully justified by the methods and evidence. Proofs (if present) are correct. Experiments are comprehensive. Assumptions are stated and reasonable. Reviewers may still have criticisms (novelty, significance, fit for venue) but raise no methodological objections.

**Characteristic patterns:**
- All claims are rigorously supported; theoretical results are proven or empirically validated
- Experiments cover appropriate baselines, ablations, and scales
- Costs and limitations are transparently reported
- The paper's conclusions are precisely scoped to what was shown
- Even minor concerns are stylistic or presentational, not methodological

### Real Reviewer Evidence (Score 4)

From **AlgoPerf** (soundness=4.0):

> *"I have no notable concerns about the paper."*

> *"Very minor typo: L382, 'framekworks' -> 'frameworks'..."* [the only criticism is a typo]

From **SPIN: Self-Supervised Prompt Injection** (soundness=4.0):

> *"It is novel to detect jailbreakings by prompt injections. The method is well motivated to construct a task where we know the ground truth, and judge using a loss function whether the redirected input..."*

From **Buckingham π-Invariant** (soundness=4.0):

> *"Originality is high. The method leverages Buckingham π-theorem and addresses OoD problem innovatively from a structured perspective."* [weaknesses are about clarity, not soundness]

From **GLinSAT** (soundness=4.0):

> *"The major drawback of GLinSAT over LinSAT is that its inference time is longer if LinSAT is set with its default 100 iterations. It will be helpful for the readers if there is a 'discussion' section..."* [acknowledged limitation, reported honestly — still sound]

From **Barely Random Algorithms** (soundness=4.0):

> *"The paper is very well written. All results are rigorously proven, but there is also a lot of intuition and high-level guiding of the reader."*

> *"I don't see any major weaknesses in the presented results or the proofs."*

> *"The results of the paper are interesting and may inspire future work in similar directions."*

> *"It's a simple idea and a simple proof, though that's not necessarily a weakness."* — Note: simplicity does not reduce soundness.

### How to Identify Score 4

Ask yourself:
1. Do reviewers raise any methodological concern at all? If the only concerns are about clarity, novelty, or venue fit — not methodology — → score 4.
2. Are the proofs/experiments described as rigorous and complete? → score 4.
3. Are limitations acknowledged and honestly scoped? → score 4.
4. Is the paper's scope tightly aligned with its evidence? → score 4.

**Important:** A theoretically-focused paper with no experiments can still be score 4 if its proofs are correct and complete. The **Barely Random Algorithms** paper received score 4 even though one reviewer noted "there is no experimental analysis" — because the theoretical results were rigorous and the claims were scoped appropriately.

---

## 6. Red Flags & Green Flags

### Red Flags (Indicators of Low Soundness)

**Instant score-1 red flags:**
- Method empirically underperforms baselines with no explanation
- Core claim made without any supporting evidence (theoretical or empirical)
- Fundamental comparison missing that would likely reverse the conclusion
- Related work so outdated it misses work that invalidates the contribution

**Score 1–2 red flags:**
- "Bio-inspired" or similar framing that is purely metaphorical with no actual modeling
- No convergence/stability analysis for optimization or RL methods
- Simulation-only experiments for a method claimed to work in real settings
- Manual evaluation with no inter-annotator agreement reported
- Benchmark with very small scale (e.g., 73 prompts) claiming to be representative

**Score 2–3 red flags:**
- "We evaluate only on [narrow subset]" without acknowledging this limits generalizability
- Important cost (latency, memory, parameter count) claimed lightweight but not measured
- Theoretical proof limited to simplified setting without noting how this limits applicability
- Claims about "in general" based on 2–3 small models or one architecture family
- Missing ablations that would distinguish the proposed method from simpler alternatives

**General warning patterns:**
- The word "straightforward" used to skip steps in proofs
- Appendix contains all crucial experiments or ablations (possible but suspicious)
- Assumptions stated in a footnote that are actually load-bearing for the main result
- Conclusion claims broader impact than what the experiments show

### Green Flags (Indicators of High Soundness)

**Instant score-4 green flags:**
- Reviewer's only criticism is a typo or a suggestion to add a discussion section
- "All results are rigorously proven" — reviewer explicitly endorses proof correctness
- "I don't see any major weaknesses in the presented results or the proofs"
- Limitations are proactively disclosed in the paper (not extracted by reviewers)

**Score 3–4 green flags:**
- Ablation study systematically isolates each component's contribution
- Computational costs are explicitly measured and reported
- Claims are carefully scoped: "we show X holds under condition Y" rather than "X always holds"
- Multiple baselines including the strongest available comparisons
- Diverse evaluation settings (multiple datasets, scales, architectures)

**Strong theoretical soundness signals:**
- Proofs provided for all main theorems, not just sketches
- Assumptions are listed explicitly at the start of theorems
- Proof techniques are standard and well-established in the field
- Remark/discussion sections explain why the assumptions are reasonable

**Strong empirical soundness signals:**
- Results are reproducible (code released, hyperparameters reported)
- Statistical significance tested where appropriate
- Negative results or failure cases reported honestly
- Baselines run by the authors under the same conditions (not copied from prior papers without verification)

---

## 7. Cross-Topic Patterns: How Soundness Expectations Differ by Research Area

### Theory Papers (Algorithms, Optimization, Learning Theory)

**What "sound" means:** Proofs are complete, correct, and assumptions are stated explicitly. Theorems are scoped precisely.

**Common soundness failures:**
- Simplified proofs that don't cover the general case
- Assumptions that are too strong to be realistic (e.g., convexity of loss in deep learning)
- Analysis of one component of a multi-component system without establishing the rest

**Reference from examples:** The **Barely Random Algorithms** paper received score 4 because reviewers found all results rigorously proven. The **Revisiting Prefix-tuning** paper received score 3 because the theoretical analysis focused only on "the first head" — a significant simplification left insufficiently justified.

**Key question for theory papers:** *Are the assumptions stated, and are the conclusions scoped to match those assumptions?*

---

### Empirical ML Papers (NLP, CV, Robotics)

**What "sound" means:** Experiments are comprehensive, baselines are fair, results generalize beyond the specific setup shown.

**Common soundness failures:**
- Too few models/datasets to support general claims
- Inference time / memory cost not analyzed for efficiency-claiming methods
- Baselines not tuned fairly (comparison favors proposed method by default)
- Human evaluation without reproducibility protocol

**Reference from examples:**
- **CAT** (score 2): Claimed a lightweight method but never measured inference latency. The claim "lightweight" cannot be accepted without measurement.
- **T2VTextBench** (score 2): Only 73 prompts; evaluation by manual inspection only; no inter-annotator agreement. A benchmark paper needs scale and reproducibility.
- **Linearly Decoding Refused Knowledge** (score 2–3): Only small models (2B, 6B, 9B) from two families; broad claims about "aligned LMs in general" are not supportable.

**Key question for empirical papers:** *Are the experiments comprehensive enough that a practitioner could trust the results and know when they'd break?*

---

### AI Safety / Alignment Papers

**What "sound" means:** Experiments cover realistic attack/defense conditions; probes/measurements are interpretable; claims about model internals are supported by mechanistic evidence.

**Common soundness failures:**
- Empirical findings with no mechanistic explanation
- Claims about model families based on a few small models
- Manually constructed datasets that may not reflect real-world distributions

**Reference from examples:**
- **SPIN** (score 4): Method is well-motivated, detection mechanism is clearly specified with loss function grounding.
- **Linearly Decoding Refused Knowledge** (score 2): "The analysis is strictly empirical and would be strengthened by a theoretical or mechanistic explanation." The claim that refused knowledge "persists" is empirically shown but not explained.

**Key question for alignment/safety papers:** *Is the threat model or intervention clearly defined, and are the experiments realistic enough to trust?*

---

### Benchmark Papers

**What "sound" means:** The benchmark is large enough, diverse enough, reproducible, and measures what it claims to measure. Annotation quality is verified.

**Common soundness failures:**
- Too small to be representative
- No inter-annotator agreement or quality control
- Prompts/items designed in an ad hoc way with no described methodology
- No automated evaluation protocol — manual only

**Reference from examples:**
- **T2VTextBench** (score 2): 73 prompts, manual-only evaluation, no inter-annotator agreement, no described prompt design methodology. Multiple reviewers flagged this.

**Key question for benchmark papers:** *Can someone else use this benchmark to evaluate a new model, and will the result be trustworthy?*

---

### Hybrid Theory+Empirical Papers

**What "sound" means:** The theoretical and empirical components are consistent with each other. Theory makes predictions that experiments verify.

**Common soundness failures:**
- Theory proves X, experiments measure Y, no connection established
- Theoretical assumptions don't hold for the empirical setting used
- Theoretical results are for a simplified model, but experiments use the full model without bridge

**Reference from examples:**
- **Revisiting Prefix-tuning** (score 3): Theoretical analysis focused on first attention head only; experiments tested full models; the gap between theory and experiments was not bridged.
- **Fairness-Aware Estimation of Graphical Models** (score 4): "The optimality analysis requires the convexity of the loss function" — this was noted as a weakness, but the paper still scored 4, suggesting the theoretical contribution was sound within its stated scope.

---

## 8. Calibration Guide: Putting It All Together

### Step-by-Step Scoring Protocol

**Step 1: Read the methodology section carefully.**
- Are the methods clearly defined?
- Are assumptions stated?
- Are proofs present and complete (for theory papers)?

**Step 2: Read the experiments section.**
- Are the baselines appropriate and competitive?
- Is the evaluation metric well-chosen?
- Are important costs (latency, memory, annotation effort) measured?

**Step 3: Check scope alignment.**
- Does the abstract/intro claim something broader than what's shown?
- Are limitations acknowledged?

**Step 4: Read reviewer comments (if available) looking for:**
- Direct statements about proof correctness
- Missing baselines or ablations
- Overly narrow evaluation
- Missing cost analysis

**Step 5: Apply the scale:**
- If no methodological concerns raised → 4
- If minor gaps noted but core claims hold → 3
- If notable gaps that limit confidence in the core claims → 2
- If fundamental flaw that undermines the core contribution → 1

### Anchor Phrases That Indicate Each Score

| Score | Anchor Phrases |
|-------|---------------|
| 4 | "I have no notable concerns," "All results are rigorously proven," "Only minor typo" |
| 3 | "Core claims are valid but," "Limited to specific configurations," "Lacks theoretical grounding," "Simplification may not hold" |
| 2 | "Too limited to support broad claims," "No analysis of [critical cost]," "Insufficient to support claims about X in general," "Manual evaluation only" |
| 1 | "Weaker than existing methods," "No comparison to," "Fundamental weakness," "Does not justify the claim" |

### Common Mistakes When Scoring Soundness

1. **Conflating novelty with soundness.** A paper reproducing known results rigorously is sound. A highly novel paper with loose experiments is not. Separate these.

2. **Penalizing acknowledged limitations.** If the paper honestly says "we only test on two model families," that's actually a sign of good scientific practice — don't penalize it the same as a paper that makes broad claims based on two model families.

3. **Ignoring missing costs.** For efficiency/compression methods, not reporting inference latency is a soundness issue, not just a presentation issue. The claim "method X is efficient" requires measurement.

4. **Over-crediting theoretical sections.** A long theoretical section with simplified assumptions that don't apply to the actual experiments does not raise soundness; it may even lower it by overpromising.

5. **Ignoring evaluation reproducibility for benchmarks.** A benchmark paper without a reproducible evaluation protocol is fundamentally unsound — future work cannot be compared on it.

---

*This skill file is grounded in real NeurIPS/ICML reviewer feedback. All quoted examples are from actual peer reviews across papers spanning ML theory, NLP, robotics, alignment, and benchmarking.*