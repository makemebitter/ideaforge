# Skill File: Evaluating General ML/AI Research Papers

## Overview

This skill file enables an AI judge to give calibrated, expert-level evaluations of machine learning and AI research papers submitted to top venues (ICLR, NeurIPS, ICML). It is built from patterns observed across 13,469 papers with an 80.9% acceptance rate and a mean rating of 4.84 (scale 0-10).

Use this file when evaluating new research ideas across the full breadth of machine learning — computer vision, NLP, theory, generative models, reinforcement learning, optimization, benchmarks, and beyond.

---

## Part 1: Rating Calibration

### Rating Scale Reference

| Rating | Label | What it means |
|--------|-------|---------------|
| 9–10 | Excellent / Oral | Groundbreaking or paradigm-shifting. Strong novel idea, comprehensive evaluation, immediate community impact. |
| 7–8 | Good / Spotlight | Clear contribution, solid experiments, well above the bar. A strong accept. |
| 5–6 | Borderline / Poster | Interesting but incomplete. Missing baselines, limited novelty, or weak presentation. Reviewers are split. |
| 3–4 | Weak / Reject | Incremental or known results, poor experiments, insufficient novelty, missing comparisons. |
| 1–2 | Strong Reject | Poor presentation, unverified assumptions, cherry-picked examples, missing baselines, trivial contribution. |

### Score Distribution Context (from 13,469 papers)

- **80.9% acceptance rate** — this is a generous corpus, meaning many accepted papers are solid but not spectacular
- **Rating mean: 4.84, median: 4.75** — a rating of 5 is roughly "borderline acceptable"
- Tier counts: excellent (8–10): 279 papers; good (6–7): 12,398; borderline (4–5): 25,685; low (1–3): 10,214
- **A score of 6 is already a solid accept**; only ~2% of papers reach the excellent tier

---

## Part 2: Anatomy of Excellence (8–10 Papers)

Based on reading oral/spotlight papers, excellent research ideas share these properties:

### 2.1 Technical Novelty That Opens Doors

The best papers introduce a new **primitive**, **constraint**, or **framework** that changes how the community thinks about a problem. Examples:
- A new consistency loss (e.g., light transport additivity) that enables training on in-the-wild data
- A new neuron model (Kuramoto oscillatory neurons) inspired by neuroscience that enables binding across architectures
- A large-scale data engine + model pair that defines new state-of-the-art
- A benchmark that reveals previously unknown LLM weaknesses

The key is that the contribution is **non-obvious** — it isn't just applying an existing technique to a new domain; there's a novel insight driving it.

### 2.2 Comprehensive, Credible Evaluation

Top papers are characterized by:
- **Comparison to strong, recent baselines** — not cherry-picked weak competitors
- **Ablation studies** that isolate each design choice
- **Quantitative + qualitative results** — numbers alone are insufficient for methods with visual/perceptual outputs
- **Multiple datasets or benchmarks** spanning domains
- **Reproducibility signals**: code release, model release, dataset release

### 2.3 Well-Motivated Problem Framing

Excellent papers make you feel the problem is important before the solution is presented:
- Clear articulation of why existing methods fail
- The solution emerges naturally from the problem structure
- Related work is honestly situated (not dismissive of prior art)

### 2.4 Scalability and Impact

Top papers often demonstrate:
- The method works at scale (large datasets, larger models, more compute)
- Downstream applications or side benefits (e.g., normal map extraction from relighting model)
- The approach has commercial or community value (open-sourced assets)

### 2.5 Oral-Quality Checklist

A paper is likely oral/spotlight quality when ALL of these hold:
- [ ] Novel insight not previously explored (not incremental)
- [ ] Strong quantitative results (SOTA or near-SOTA on major benchmarks)
- [ ] Comprehensive ablations
- [ ] Clear exposition and intuition building
- [ ] Strong baselines, including recent methods
- [ ] Code/data released or planned for release
- [ ] At least one reviewer gives a score of 8+

---

## Part 3: Common Failure Modes (1–4 Papers)

### 3.1 Limited Novelty / Incremental Contribution

**Red flags:**
- "The findings confirm what previous works have established"
- Empirical study that produces no surprising results
- Method is a combination of existing techniques without principled motivation
- The contribution is a new dataset/benchmark but results are obvious or already known

**Reviewer language:** "incremental", "known findings", "limited novelty", "similar to [prior work]"

**Calibration:** An empirical study reporting that "more synthetic data helps when real data is scarce" is **not** novel in 2024+ — this was established by [He et al., ICLR 2023] and many others. The bar for empirical studies is: surprising findings, new theoretical understanding, or significantly broader scope than prior work.

### 3.2 Missing or Weak Baselines

The single most common weakness in rejected/borderline papers is baseline inadequacy:
- Missing recent (< 2 years) strong baselines in the comparison tables
- Only comparing against weak or outdated methods
- No ablations showing which component contributes what
- Fair comparison issues: different training data, model sizes, compute

**Reviewer language:** "baseline", "fair comparison", "ablation", "lacks a comparison to..."

**Rule:** If the paper's method is not compared against the closest recent competitor, the evaluation is incomplete, regardless of how impressive the absolute numbers are.

### 3.3 Poor Presentation / Inability to Follow

Strong papers are written for the reader. Signs of poor presentation:
- Abstract is vague and doesn't communicate the core idea
- Key variables or notation not defined before use
- Figures lack sufficient captions or are unexplained
- Methods section describes what happens but not why
- Theorems/equations are stated without interpretation

**Reviewer language:** "hard to follow", "unclear how", "unclear why", "unclear what", "dense and hard to follow in a single reading"

### 3.4 Unverified or Unjustified Assumptions

Papers that assume simplifying properties (linearity, sparsity, independence) without justification will receive poor soundness scores:
- Claim a neural network has property X, tested on 1-2 examples
- Theoretical results assume conditions (e.g., i.i.d., independence) that don't hold in practice
- Proofs skip important edge cases

### 3.5 Insufficient Experiments

A paper that only tests on 2 datasets, a handful of examples, or a single domain fails to demonstrate generality:
- Results are cherry-picked
- No statistical significance testing
- Variance/error bars missing from key tables
- Evaluation on tiny subsets of problems

### 3.6 Missing Related Work

Reviewers are expert in their domain. Missing key related work signals:
- Ignorance of the field
- Potential overlap with existing work
- Overclaiming novelty

---

## Part 4: Borderline Papers (4–6) — The Hard Cases

### 4.1 Interesting Idea, Insufficient Execution

The most common borderline case: a research idea with genuine merit but execution that leaves reviewers unconvinced:
- Interesting neuroscience-inspired architecture, but computational cost unreported and key ablations missing
- Good empirical findings, but theoretical backing absent and scope limited
- Promising approach, but only one strong baseline and dataset

**Decision heuristic:** If the idea is original but the execution gaps are fixable in a revision, this is typically a borderline accept (5–6). If the gap is fundamental (e.g., the core assumption is wrong, the contribution is not new), it's a reject.

### 4.2 Solid Engineering, Limited Science

Some papers achieve good results through careful engineering but contribute little to understanding:
- Strong benchmark numbers with no ablation showing why
- A well-crafted system with no novel components
- Lots of implementation details, but the "why" is missing

These typically score 4–6 depending on the scale of the engineering achievement.

### 4.3 Divergent Reviewer Opinions

Borderline papers often split reviewers because:
- One reviewer is an expert who knows the related work well; others are not
- The contribution is cross-disciplinary and reviewers from different fields weigh it differently
- The results are strong but the writing quality is poor

**Calibration tip:** When in doubt, weight the most expert reviewer's assessment more heavily, especially on novelty claims.

---

## Part 5: Dimension-Specific Guidance

### 5.1 Soundness (1–4 scale)

| Score | Meaning |
|-------|---------|
| 4 | No errors; all claims justified; proofs correct; assumptions stated and reasonable |
| 3 | Minor issues that don't affect main conclusions; most claims solid |
| 2 | Notable gaps; some assumptions unjustified; results may not replicate |
| 1 | Fundamental flaws; incorrect proofs; unverified assumptions; cherry-picked results |

Key questions for soundness:
- Are experimental results averaged over multiple runs with error bars?
- Are baselines fair (same model size, training data, compute)?
- Are proofs complete or are key steps "left to the reader" incorrectly?
- Are hyperparameters tuned on test sets (data leakage)?

### 5.2 Contribution (1–4 scale)

| Score | Meaning |
|-------|---------|
| 4 | Major advance; changes how the community approaches the problem; likely to be widely cited |
| 3 | Solid contribution; adds meaningfully to prior art; not transformative |
| 2 | Incremental; combines existing ideas without principled insight; limited to narrow setting |
| 1 | Negligible; known results restated; very narrow application; no new insight |

Key questions for contribution:
- Would a practitioner change their practice based on this paper?
- Does this open new research directions or close off existing questions?
- Is the dataset/benchmark sufficiently harder/broader than existing ones?
- Does the method generalize across domains, architectures, or settings?

### 5.3 Presentation (1–4 scale)

| Score | Meaning |
|-------|---------|
| 4 | Exceptionally clear; figures are informative; notation is consistent; a pleasure to read |
| 3 | Clear overall; minor issues; mostly follows the reader through the argument |
| 2 | Some confusion; key details missing; figures poorly captioned or unexplained |
| 1 | Major clarity issues; hard to understand the core method; vague or imprecise language throughout |

### 5.4 Overall Rating Composition

The overall rating is not a simple average. Use this mental model:
- **Soundness** sets the floor: a paper with fundamental flaws (soundness=1) cannot score above 5 overall
- **Contribution** drives the ceiling: a paper with only incremental contribution (contribution=1-2) rarely scores above 6
- **Presentation** is a multiplier: poor presentation (score=1) that makes the paper unreadable caps the overall at 4 regardless of idea quality

---

## Part 6: Research Idea-Specific Evaluation (vs. Finished Papers)

When evaluating a **research idea** rather than a completed paper, adjust your rubric:

### 6.1 What to Assess

For ideas at the proposal stage:
1. **Conceptual novelty**: Is the core insight new and non-obvious?
2. **Feasibility**: Is there a plausible path to implementation and empirical validation?
3. **Experimental design quality**: Are the right baselines, metrics, and datasets proposed?
4. **Potential impact**: If it works, does it matter?
5. **Risk-reward**: What's the downside if the core assumption is wrong?

### 6.2 Common Idea-Level Failures

- **Solutions looking for problems**: The method is described first, then a problem is retrofitted. Ask: what failure mode of existing methods does this address?
- **Benchmark arbitrage**: Proposing a new benchmark that's just harder, without revealing new phenomena or enabling new science
- **Overclaiming generality**: "Our method works for all X" when the evidence is from a single narrow setting
- **Circular motivation**: "We propose X because X works better" — the motivation should come from first principles

### 6.3 Idea Quality Signals

**Strong idea signals:**
- The proposal identifies a clear gap: existing methods fail in a specific, demonstrable way
- The proposed solution addresses the failure mode directly with principled reasoning
- There's a clear falsifiability criterion: "If our hypothesis is correct, we expect to see Y"
- The experimental protocol is appropriately broad (multiple datasets, ablations planned)
- The authors acknowledge limitations and potential failure modes

**Weak idea signals:**
- Vague motivation ("we want to improve X")
- No comparison planned to the closest existing methods
- The approach is purely engineering with no scientific hypothesis
- Results are only planned on easy/synthetic settings
- No discussion of when the approach would fail

---

## Part 7: Domain-Specific Calibration

The "general" topic spans many areas. Here are domain-specific calibration notes:

### 7.1 Computer Vision

- **Expected baselines**: SOTA methods from the past 12-18 months on standard benchmarks (ImageNet, COCO, etc.)
- **Must-have experiments**: Comparison on established benchmarks + ablation of key components + computational cost analysis
- **Common weak points**: Missing perceptual quality metrics for generation tasks; missing runtime/FLOPs analysis; not comparing to concurrent work
- **Novelty bar**: With large pretrained models ubiquitous, the bar for "novel" is high — fine-tuning tricks alone rarely suffice

### 7.2 Natural Language Processing

- **Expected baselines**: GPT-4, Claude, Llama, Gemini (the frontier) for LLM work; task-specific SOTA for specialized NLP
- **Must-have experiments**: Zero-shot and few-shot evaluations; multiple benchmarks; human evaluation for generation tasks
- **Common weak points**: Data contamination not addressed; benchmark saturation (near-ceiling performance means results are noise); cherry-picked qualitative examples
- **Novelty bar**: Prompt engineering alone is rarely publishable; benchmark papers need to reveal genuinely new phenomena

### 7.3 Generative Models (Diffusion, GANs, VAEs, LLMs as generators)

- **Expected baselines**: FID, IS for images (though these are known to be imperfect); CLIP scores; human preference studies
- **Must-have experiments**: Diverse samples showing consistency; failure mode analysis; comparison to diffusion/flow-based SOTA
- **Common weak points**: Using FID/IS alone without perceptual or human evaluation; overfitting to specific domains; computational cost not reported

### 7.4 Theoretical ML

- **Expected baselines**: Comparison to known bounds; tightness analysis
- **Must-have**: Clean formal statements; proofs in appendix; connecting theory to practice (even if empirical validation is simple)
- **Common weak points**: Assumptions that don't hold in practice; bounds too loose to be meaningful; no connection to empirical behavior

### 7.5 Benchmarks and Datasets

- **Expected baselines**: Comparison to existing benchmarks on difficulty, diversity, coverage
- **Must-have**: Annotation quality analysis; inter-annotator agreement; results showing SOTA models struggle; human performance baseline
- **Common weak points**: Not showing the benchmark reveals new phenomena; easy to saturate; data contamination risk not addressed; too narrow in scope

### 7.6 Reinforcement Learning

- **Expected baselines**: PPO, SAC, TD3 + recent domain-specific SOTA
- **Must-have**: Multiple seeds with confidence intervals; diverse environments; comparison on standard benchmarks (Atari, MuJoCo, etc.)
- **Common weak points**: Only tested in one environment; no error bars; comparison to weak baselines; sample efficiency not analyzed

---

## Part 8: Red Flags and Instant Signals

### 8.1 Immediate Red Flags (strongly consider reject)

- No baselines from the past 2 years in a fast-moving field
- Experiments on a single, tiny dataset with no real-world analogue
- Claims of "first to do X" without a literature review that confirms it
- Proofs with unjustified steps labeled as "straightforward"
- Results presented only qualitatively when quantitative comparison is feasible
- No ablation studies for a method with multiple novel components
- Key hyperparameters not reported (makes reproducibility impossible)
- Method description that is incomprehensible or missing crucial details

### 8.2 Green Flags (push toward higher score)

- Code/data released with the paper (reproducibility)
- Results shown on multiple independent benchmarks
- Honest discussion of limitations and failure cases
- Strong baselines that are better than naively expected
- The method is simpler than alternatives but performs better
- Multiple applications or downstream tasks demonstrate transfer
- Error bars / confidence intervals consistently reported
- Open questions and future work clearly articulated

### 8.3 Frequently Missed Issues

- **Fair comparison violations**: If Method A uses pretraining and Method B doesn't, the comparison is unfair — verify that baselines have comparable access to data and compute
- **Metric choice gaming**: FID for images, BLEU for text, and accuracy for classification can all be gamed; check if multiple metrics are reported
- **Statistical testing**: In tables with small differences, are results statistically distinguishable?
- **Cherry-picked qualitative examples**: The paper shows 5 success cases but no failure cases
- **Circular baselines**: Comparing to methods from the same group that are not competitive externally

---

## Part 9: Reviewer Language Decoder

Common phrases and what they signal:

| Phrase | Signal |
|--------|--------|
| "novel contribution" | Positive novelty signal — the idea is new |
| "incremental" | The contribution is viewed as a small step, not a new direction |
| "ablation study needed" | Key design choices are not empirically justified |
| "missing baseline" | A critical competitor is absent from the comparison |
| "limited to" | Scope is too narrow for the claims made |
| "unclear how/why/what" | Presentation is ambiguous; the reader can't follow the logic |
| "scalab..." | Scalability is either a strength (if it scales) or weakness (if it doesn't) |
| "reproducib..." | Either a strength (code available) or concern (code absent, details missing) |
| "fair comparison" | Reviewer suspects the evaluation setup favors the proposed method |
| "well-written" | Presentation is a strength |
| "lacks a theoretical..." | No formal justification for why the method works |
| "significant contribution" | High contribution score — this matters to the field |
| "strong empirical" | Quantitative results are impressive and comprehensive |

---

## Part 10: Scoring Workflow

When evaluating a research idea, follow this sequence:

### Step 1: Identify the Core Contribution

What is the single most important thing this paper proposes? It should be articulable in one sentence. If it cannot be, that's a presentation problem.

Is the contribution:
- A new method/algorithm?
- A new theoretical result?
- A new dataset/benchmark?
- A new empirical finding?
- A new application of existing methods?

Each type has a different novelty bar.

### Step 2: Situate in Related Work

- What are the 3 closest prior works?
- How does this paper differ from each?
- Is the claimed novelty accurate given related work?
- Are key related works cited?

### Step 3: Evaluate Experimental Design

- What baselines are compared?
- Are they appropriate and recent?
- What metrics are used? Are they the right ones?
- Are experiments on appropriate datasets?
- Is there a systematic ablation?

### Step 4: Assess Soundness

- Are the claims supported by the evidence?
- Are there logical gaps?
- Are assumptions stated and reasonable?
- Are statistical best practices followed?

### Step 5: Holistic Rating

Combine the above into:
- `soundness`: 1-4 (is it technically correct?)
- `contribution`: 1-4 (does it advance the field?)
- `presentation`: 1-4 (is it communicated well?)
- `overall rating`: 1-10 (calibrated against the distribution above)

### Step 6: Write Specific, Actionable Feedback

- Name the specific missing baseline (not "a baseline is missing", but "comparison to [Method X] from [Paper Y] is expected")
- Point to specific claims that are unsupported
- Give concrete suggestions for improvement

---

## Part 11: Calibration Examples

### Example 1: Excellent (9/10)

**Paper**: Introduces a physically-motivated consistency loss for diffusion-based relighting, enabling training on 10M+ in-the-wild images. Results are SOTA on multiple metrics with impressive qualitative outputs. Code will be released.

**Why excellent**: Novel physical insight (light transport additivity) applied to deep learning in a non-obvious way. Large-scale training enabled by the new loss. Multiple strong baselines. Beautiful qualitative results. Applications beyond the primary task (normal estimation).

**Expected scores**: soundness=4, contribution=4, presentation=4, overall=9-10

### Example 2: Good (7-8/10)

**Paper**: Extends an image segmentation model to video via a streaming memory-augmented transformer and builds a large-scale video segmentation dataset (SA-V).

**Why good**: Significant dataset contribution. Strong model. SOTA performance. One reviewer notes: "the technical contribution is relatively limited" but the dataset and model scale make it impactful. Well-written.

**Expected scores**: soundness=3-4, contribution=3-4, presentation=3-4, overall=7-9

### Example 3: Borderline (4-5/10)

**Paper**: Empirical study showing that synthetic data from generative models can augment image classifiers, especially when real data is limited.

**Why borderline**: The finding (synthetic data helps when real data is scarce) is known from prior work. The paper confirms but does not significantly extend. Experiments are on standard datasets. Some reviewers find it useful; others find it redundant with [He et al., ICLR 2023].

**Expected scores**: soundness=2-3, contribution=1-2, presentation=2-3, overall=3-5

### Example 4: Reject (1-2/10)

**Paper**: Proposes to explain neural network decisions in the Go game by modeling stone interactions.

**Why reject**: Poor presentation throughout. Key methods not clearly described. Experiments on 10 stones only. No baselines compared. Unverified linearity/sparsity assumptions. Cannot reproduce results. Key claims overlap with unreferenced prior work.

**Expected scores**: soundness=1, contribution=1-2, presentation=1, overall=1-2

---

## Part 12: Meta-Calibration Notes

### The Acceptance Rate Trap

This corpus has an 80.9% acceptance rate — much higher than ICLR/NeurIPS actual acceptance rates (typically 25-30%). This means **many papers in the "accepted" bin would be rejected at top venues**. Calibrate accordingly:

- A "poster accept" in this corpus might score 4-5 at a real venue
- Oral papers are genuinely excellent
- When in doubt, weight novelty and baseline quality heavily

### Year Effects

The ML landscape shifts rapidly. Novelty must be assessed relative to what was known at submission time:
- A 2020 idea that has been replicated 50 times by 2024 is no longer novel
- Concurrent work doesn't disqualify a paper, but it does lower contribution scores if the ideas are nearly identical

### Confidence Calibration

Be appropriately uncertain in unfamiliar subfields. Signal uncertainty with language like:
- "In my assessment, though I am less expert in [area]..."
- "Reviewers with expertise in [area] should verify..."

A high-confidence wrong assessment is worse than a low-confidence correct one.

---

## Summary Quick Reference

**To score 8+**: Must have a novel core insight, comprehensive experiments with strong recent baselines, systematic ablations, and clear impact on the community.

**To score 5-7**: Solid work, mostly correct, but either the novelty is limited, baselines are missing, or the scope is narrower than claimed.

**To score 1-4**: Fundamental issues with novelty, soundness, or presentation. Known results, cherry-picked examples, or incomprehensible methods.

**Always check**:
1. What are the closest 3 papers, and is this meaningfully different?
2. Are recent baselines compared? Ablated?
3. Are results averaged over seeds with error bars?
4. Is code/data released?
5. Is the core claim falsifiable and tested rigorously?
