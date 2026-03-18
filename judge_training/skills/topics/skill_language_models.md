# Skill File: Evaluating Language Model Research Papers

**Topic Area:** Language Models (LLMs, NLP, language generation, alignment, efficiency, safety)
**Data Source:** 8,419 papers across ICLR/NeurIPS/ICML; 78.1% historical acceptance rate
**Rating Statistics:** Mean 4.73, Std 1.26, Range 0–9.5
**Tier Distribution:** Low (1–3): 7,072 papers | Borderline (4–5): 16,435 | Good (6–7): 6,712 | Excellent (8–10): 193

---

## 1. Overview of the Language Models Research Area

### Scope

The language models topic covers all research that centers on training, adapting, deploying, understanding, or evaluating neural language models — with a strong emphasis in the current era on large language models (LLMs) built on the Transformer architecture. This is the single largest topic area in modern NLP/ML venues, encompassing everything from fundamental architectural innovations to safety and deployment concerns.

Papers in this area come from multiple communities: machine learning, natural language processing, AI safety, cognitive science, and increasingly systems/hardware. The reviewer pool is likewise diverse, which creates variance in scoring — especially for cross-disciplinary work.

### Key Sub-Areas

1. **LLM Pretraining and Architecture** — Novel architectures, attention mechanisms, positional encodings, scaling laws, data curation, tokenization, MoE variants.
2. **Instruction Tuning and RLHF/Alignment** — Supervised fine-tuning, PPO/REINFORCE-based RL, DPO and offline preference optimization, reward modeling, constitutional AI, preference data.
3. **Reasoning and Chain-of-Thought** — Step-by-step prompting, self-consistency, tree/graph of thought, process reward models, math and code reasoning, planning.
4. **Efficiency** — PEFT methods (LoRA, prefix tuning, adapters), quantization, pruning, speculative decoding, knowledge distillation, caching, inference-time compute tradeoffs.
5. **Safety and Robustness** — Jailbreaks, adversarial attacks, harmful fine-tuning, red-teaming, mechanistic alignment, interpretability of safety-relevant features.
6. **Evaluation Benchmarks and Datasets** — New benchmarks, contamination analysis, meta-evaluation of LLM judges, capability elicitation.
7. **Agents and Tool Use** — Agentic LLM frameworks, function calling, code execution, multi-agent systems, planning with LLMs.
8. **Retrieval-Augmented Generation (RAG)** — Dense retrieval, re-ranking, knowledge grounding, open-domain QA.
9. **Multimodal LLMs** — Vision-language models, audio-language, video, cross-modal alignment, multimodal instruction following.
10. **Interpretability and Mechanistic Analysis** — Probing, sparse autoencoders (SAEs), circuit discovery, knowledge representations, hallucination mechanisms.

### Typical Paper Types

- **Architecture papers:** Propose a new model component or variant; require large-scale training experiments and comparison to standard Transformer.
- **Method papers (alignment/efficiency/reasoning):** Propose a new training or inference procedure; require controlled comparisons, ablations, and multiple models.
- **Benchmark/dataset papers:** Introduce new evaluation data; require analysis of existing models, inter-annotator agreement, and leakage analysis.
- **Analysis/understanding papers:** Study why models behave as they do; require mechanistic or statistical evidence across multiple models and settings.
- **Application papers:** Apply LLMs to a specific domain or task; require comparison to domain-specific baselines and strong motivation for why LLMs are the right tool.

---

## 2. Rating Calibration Guide

The ICLR/NeurIPS rating scale typically runs 1–10, with the acceptance threshold near 5–6 depending on the venue and year. The distribution observed in this dataset is highly left-skewed: most papers cluster in the 4–5 borderline range, and scores above 7 are rare (fewer than 2.3% of papers in this corpus reach 8+).

### Excellent Papers (8–10): What Makes a Paper Exceptional

Excellent papers (193 of 8,419 = 2.3%) share several defining characteristics:

**1. Novel conceptual contribution that reshapes how the community thinks about a problem.**
The best papers are not just incrementally better — they introduce a new way of framing the problem. "Safety Alignment Should be Made More Than Just a Few Tokens Deep" (rating 9.5) reframed the entire literature on jailbreak attacks by identifying a single unifying explanation (shallow alignment) and providing both empirical evidence and defenses. The community can build on this framing.

**2. Comprehensive, multi-faceted empirical validation.**
Excellence requires experiments that anticipate skeptical reviewers' questions. The safety alignment paper covered four attack types (adversarial/GCG, prefilling, sampling, fine-tuning) in a unified framework, included multiple models, and measured diverse metrics. Reviewers explicitly praised that "many questions that I had while reading were sooner or later answered/investigated within the paper."

**3. Clean, elegant theory or mechanism paired with clear practical payoff.**
"Self-Improvement in Language Models: The Sharpening Mechanism" (rating 8.0) provided sample complexity bounds for SFT-Sharpening and RLHF-Sharpening. This is theoretically novel and practically motivating even if some reviewers wished for more empirical validation of the training-time sharpening algorithms themselves.

**4. Technical soundness across the board (soundness=3–4).**
All four reviewed excellent papers had soundness ratings of 3–4. This does not mean perfect — reviewers still listed weaknesses — but the core claims are solid, reproducible, and not undermined by the weaknesses.

**5. Strong presentation (clear writing, well-organized).**
"The paper is well written and easy to follow" or "writing is excellent" appear in reviews of every excellent paper reviewed here. The Differential Transformer paper was praised for being "well-written, easy to follow" with "clear illustrations and analogies." This is not a sufficient condition but appears to be necessary.

**6. First-mover or breakthrough in a contested area.**
"Differential Transformer" (rating 8.0) was described as "the first work to propose a new architecture using differential attention." In architecture papers, being first to a clean, general-purpose mechanism matters enormously. Scale of experiments (3B parameters, 350B tokens) further validated the claim.

**What separates 8 from 10:**
- Ratings of 10 typically come from reviewers who find the paper "important to the community" beyond just technically strong. "Do I Know This Entity?" (avg 9.0) received two 10s and two 8s. The 10-raters emphasized causal analysis and multi-layer evidence. The 8-raters noted limited model diversity (Gemma only) as a genuine constraint.
- Weaknesses that remain in excellent papers are typically: limited model diversity, missing one or two baselines, minor presentation issues, or theoretical analysis that could be tighter. These do not undermine the core contribution.

### Good Papers (6–7): What Makes a Solid Paper

Good papers (6,712 of 8,419 = 7.97% of labeled papers, but a large fraction of accepted papers) represent solid, publishable contributions that do not fundamentally reshape the field but make a clear, well-validated incremental advance.

**Characteristics of good papers:**
- A clear, well-motivated contribution with appropriate scope. Not overclaiming.
- At least 2–3 strong baselines on standard benchmarks.
- Ablation studies that validate the key design choices.
- Results that hold across at least 2 model sizes or model families.
- Readable presentation with a well-structured experiments section.
- Related work that is comprehensive enough to situate the contribution.

**What keeps a paper below 8:**
- Missing a key baseline that reviewers consider obvious.
- Claims that slightly overshoot what experiments support.
- One sub-area of experiments is weak or missing (e.g., no efficiency comparison for an efficiency paper).
- Limited model diversity (e.g., only one architecture or only proprietary models).
- Theoretical analysis that is more motivational than rigorous.

**Example signal for 6:** "The experiment is well done... The idea is clear and straightforward... The authors didn't provide sufficient explanations about the occurred phenomenon... it would be great if the authors can provide some theoretical analysis." (SALSA reviewer, rating=5–6)

### Borderline Papers (4–5): The Acceptance Threshold

Borderline papers (16,435 = the largest tier) are where the most difficult decisions live. These papers have a genuine contribution but suffer from one or more significant gaps. At venues with 78% acceptance rate (as in this dataset), most borderline papers are accepted; at more selective venues (ICLR main track ~31-33% acceptance), borderline papers are often rejected.

**The acceptance question for borderline papers:** Does the paper make a contribution that is worth the community's attention, even if the execution is imperfect?

**Characteristics of borderline papers:**
- The core idea is interesting and novel, but the empirical evidence is incomplete.
- Missing ablations on key design choices.
- Baselines are insufficient — either outdated, weak, or missing important recent work.
- Evaluation is limited to a narrow set of tasks or models.
- Some overclaiming in the abstract/introduction relative to what experiments show.
- Technical soundness is adequate (soundness=2–3) but not excellent.

**What tips a 4–5 paper toward accept:**
- The idea is sufficiently novel that even imperfect experiments are informative.
- The paper opens a new research direction.
- The authors address reviewer concerns in rebuttal.

**What tips a 4–5 paper toward reject:**
- Missing a critical baseline that would likely eliminate the advantage.
- The contribution is largely incremental over an unacknowledged prior work.
- Claims in the abstract are not supported by experiments.

**Key insight about borderline papers:** Reviewers in this regime almost always mention "baseline" and "ablation" as weaknesses. The SALSA paper (avg 4.83, accepted) received repeated criticism: "does not compare SALSA method with other existing alignment or optimization methods," "reward-free methods such as DPO are not discussed," "missing WARP, WARM" related works. It was still accepted because the core idea (model soup for RLHF reference) was genuinely novel and experiments showed improvement.

### Low Papers (1–3): Common Fatal Flaws

Low-rated papers (7,072 samples in this corpus; rated 1–3) are rejected because of fundamental problems that cannot be fixed with a rebuttal.

**Fatal flaw categories:**

**Category 1: Mathematically unsound foundation.**
The Memorisable Prompting paper (avg 1.67, rejected) received ratings of 1/1/3 because reviewers found "fundamental flaws in the probabilistic framework and problem formulation." Specifically, the core equation marginalized over ground truth labels as if they were random variables — a conceptual error that the entire method rested on. No amount of experiments can fix a methodologically broken formulation.

**Category 2: Contribution is not research — it is engineering or application.**
"Unleashing the Potential of LLMs for Quantum Computing" (avg 1.67, rejected) was criticized for "blindly using these models without attempting to understand the basis of the problem." Reviewers asked "What is the real contribution?" Simple application of an existing API to a new domain, without scientific insight, is not a publishable contribution at top venues.

**Category 3: Writing and presentation so poor as to be uninterpretable.**
The Memorisable Prompting paper was criticized by two reviewers for having "multiple formatting errors," "basic grammar errors," undefined symbols, figures not referenced in the text, and sections that "are not clearly or rigorously written." Papers that reviewers cannot understand cannot be evaluated charitably.

**Category 4: No comparison to meaningful baselines.**
Papers that compare only to trivial baselines (e.g., zero-shot CoT) without acknowledging state-of-the-art methods signal that the authors do not know the field well enough to know what they need to beat.

**Category 5: Scope mismatch with venue.**
QAS/quantum computing paper was explicitly criticized: "QAS is not a problem of great interest to the ICLR community." Papers in highly specialized domains need to demonstrate why their contribution matters to the broad ML/NLP community.

**Common 1-3 review language:**
- "The contribution is not clear."
- "Fundamental errors in both model construction and experimental setups."
- "This is more of a technical report."
- "I don't even know what kind of prompt form the authors employ."
- "The paper does not fully investigate the related work."
- "Multiple errors in the paper... the readability of the paper is poor."

---

## 3. Key Evaluation Dimensions

### 3.1 Novelty and Originality

**How to assess novelty:**

Novelty is the single most contested dimension in LM papers and the most frequently cited in both strengths (5,571 occurrences) and weaknesses (5,086 occurrences) in this dataset. The same word appears in both columns because "novel" in strengths means genuine novelty, while "novelty" in weaknesses usually signals its absence.

**High novelty signals:**
- Introduces a new problem formulation that the community has not considered.
- Identifies a single unifying explanation for previously disparate phenomena.
- The first work to achieve a specific capability at scale.
- Proposes a mechanism that is both simple and previously overlooked.

**Low novelty signals:**
- The paper combines two existing methods (A + B) without explaining why A+B is fundamentally different from A or B alone.
- "Limited novelty" — the paper improves a known method by a marginal amount with no new insight.
- The contribution was already made in a published workshop paper or preprint that is not acknowledged.
- The idea has been independently proposed in concurrent work that the authors do not cite.

**Borderline novelty cases:**
- Using an existing mechanism in a new application domain: acceptable if the application is high-impact and the adaptation is non-trivial.
- Providing theoretical analysis of an existing method: acceptable if the analysis is tight and the implications are non-trivial.
- Empirical studies of known phenomena: acceptable if the study is comprehensive and yields non-obvious insights.

**Key nuance:** In the LM field, "incremental" is used pejoratively but not always correctly. The Differential Transformer (rating 8.0) is technically incremental — it is a modification to the standard attention mechanism — but reviewers rated it highly because it is well-motivated, generalizes across scales, and introduces a new design paradigm. The difference between "incremental" (good) and "incremental" (bad) is whether the paper teaches you something new vs. merely demonstrates that a small twist on existing methods gets 1–2 points on a benchmark.

### 3.2 Technical Soundness

**What soundness means in LM papers:**

The average soundness score in this dataset is 2.58 (on a scale of 1–4), indicating that even accepted papers typically have soundness issues. Reviewers distinguish between:

- **Soundness 1 (poor):** Core claims are wrong, math is incorrect, key experiments are missing.
- **Soundness 2 (fair):** Claims are plausible but insufficiently supported; missing ablations or baselines.
- **Soundness 3 (good):** Main claims are well-supported with minor gaps.
- **Soundness 4 (excellent):** Claims are rigorously supported; all major alternative explanations are ruled out.

**Common soundness issues in LM papers:**
1. **Confounding variables in training comparisons.** If Paper A uses more compute, more data, or a stronger base model than Paper B, claiming superiority is unsound without controlling for these.
2. **LLM-as-judge evaluation without calibration.** Using GPT-4 to evaluate outputs is now standard but flagged as a weakness unless the paper also reports human evaluation or shows the judge is calibrated. The safety alignment paper (rating 9.5) was criticized for this but accepted anyway because the overall evidence was overwhelming.
3. **Stochastic results without variance reporting.** Generation with non-greedy decoding requires multiple runs and variance reporting. "The outputs are sampled using non-greedy decoding. Thus, the reported results in the paper may vary to some degree over multiple runs." (Safety alignment reviewer, rating=10)
4. **Missing ablations on critical design choices.** In architectures: why is this specific parameterization needed? In prompting methods: which component contributes how much? Ablations are cited as strengths in 3,531 reviews but as weaknesses in 5,079 reviews — the single most asymmetric signal in the dataset.
5. **Insufficient scale of experiments for architecture papers.** Architecture papers that only validate at small scale (e.g., 125M parameters, 1B tokens) are systematically weaker. The Differential Transformer was trained at up to 3B parameters and 350B tokens, which makes its claims convincing.

### 3.3 Empirical Evaluation Quality

**What baselines are expected (general):**

The word "baseline" appears 11,973 times in weakness sections vs. 3,517 in strength sections — the most asymmetric word in the entire dataset. Inadequate baselines are the single most common reason for reviewer criticism.

**Minimum baseline requirements by paper type:**
- **Architecture papers:** Must compare to the standard Transformer baseline at matched parameter counts. Additional comparisons to other Transformer variants (e.g., RetNet, Mamba, sparse attention) strengthen the paper. The Differential Transformer was criticized for not comparing to sparse attention methods despite claiming attention sparsity benefits.
- **Alignment/RLHF papers:** Must compare to DPO, PPO, and SFT baselines. The SALSA paper (avg 4.83) was criticized for not comparing to DPO or reward-free methods, which are now standard.
- **Reasoning papers:** Must compare to standard CoT, zero-shot CoT, self-consistency, and recent SOTA methods on the evaluated benchmarks (e.g., HotpotQA, FEVER, GSM8K, MATH, MMLU).
- **Safety papers:** Must compare to existing defenses. The safety alignment paper (rating 9.5) was still criticized for not comparing to Circuit Breaking / Short Circuiting despite being rated 8–10. This shows that even excellent papers face baseline criticism.
- **RAG papers:** Must compare to RAG-Fusion, standard dense retrieval + reader, and strong prompting-only baselines.

**What ablations are expected:**
- Every key design choice that differs from prior work should have an ablation.
- For architecture papers: ablations on each novel component.
- For prompting/agent papers: ablations on each agent component, without each module.
- For training method papers: ablations on hyperparameter choices and training dataset composition.
- Token/compute budget comparisons when the proposed method adds overhead.

**Benchmark selection:**
- Claiming improvement on narrow or easy benchmarks (where ceiling effects exist) is a weakness. Reviewers expect evaluation on challenging, widely-used benchmarks.
- For NLU: MMLU, BIG-Bench, HellaSWAG, ARC, TruthfulQA.
- For reasoning: GSM8K, MATH, HotpotQA, StrategyQA.
- For generation/instruction following: MT-Bench, Arena-Hard, AlpacaEval.
- For safety: AdvBench, HarmBench, JailbreakBench.
- For long context: SCROLLS, RULER, NeedleInHaystack.

### 3.4 Clarity and Reproducibility

Reproducibility ("reproducib") appears as a strength word 1,046 times and as a weakness word 1,235 times. The gap is relatively small compared to "baseline" or "novelty," suggesting that reproducibility is now a table-stakes expectation rather than a differentiator.

**What reviewers expect for reproducibility:**
- Full hyperparameter details (learning rates, batch sizes, warmup schedules, model sizes).
- Training data specifics and any preprocessing steps.
- Inference configuration (temperature, top-p, sampling strategy).
- Evaluation metrics explained with formulas or citations.
- Code released or promised.
- Prompts reproduced in full (especially for prompting/agent papers).

**Clarity expectations:**
- All variables defined before use.
- Figures and tables referenced in the main text.
- Algorithm pseudocode for non-standard training procedures.
- Related work section that is specific (not just a list of citations but with comparisons).

---

## 4. Sub-Area Specific Criteria

### 4.1 LLM Pretraining and Architecture

**Core question:** Is this architecture change meaningfully better than the Transformer, at scale, in a fair comparison?

**Minimum experimental bar:**
- Pre-train to convergence at multiple model sizes (at minimum 2 sizes, ideally following scaling laws).
- Compare against standard Transformer at matched parameter count AND matched compute (FLOPs).
- Report perplexity on validation data AND downstream task performance.
- Report throughput/efficiency (FLOPs/token, training time per token, inference latency).

**Common weaknesses:**
- Only validated at small scale (< 1B parameters) — insufficient to claim general superiority.
- No discussion of whether the change is compatible with existing optimizations (FlashAttention, tensor parallelism).
- No related work section comparing to other Transformer variants (RetNet, Mamba, GLA, RWKV, etc.).
- Not trained on sufficiently large data (claim: "we train on X tokens" where X is less than what would show meaningful scaling).

**Green flags:**
- Training experiments at 3B+ parameters and 100B+ tokens.
- Ablation on each novel component.
- Code released with training config.
- Compatibility with standard infrastructure demonstrated.
- Analysis of why the architecture works (attention patterns, activation statistics, etc.).

**The Differential Transformer example:** Architecture paper rated 8.0. Key strengths: large-scale validation (3B, 350B tokens), multi-benchmark evaluation, attention pattern analysis. Key weakness: no comparison to sparse attention methods despite claiming sparsity benefits; no instruction tuning experiments; missing related work section. Rating was still 8 because the core mechanism was novel and validated at scale.

### 4.2 Instruction Tuning, RLHF, and Alignment

**Core question:** Does this training method produce models that are more aligned, more helpful, or more safe, in a way that is fair and reproducible?

**Minimum experimental bar:**
- Compare to SFT baseline, DPO baseline, and at least one PPO-based baseline.
- Evaluate on MT-Bench, Arena-Hard, or AlpacaEval (standard instruction following).
- Report both reward (if RL-based) and win-rate against a reference model.
- Evaluate safety/harmlessness trade-off if claiming improvements on helpfulness.
- Report compute cost relative to baselines.

**Common weaknesses:**
- Comparing only to PPO without comparing to DPO (now considered standard). SALSA (avg 4.83) was heavily criticized for this.
- Using LLM-as-judge without human calibration.
- Not reporting KL divergence from reference policy (which can "hide" reward hacking).
- Missing comparison to important related methods (WARP, WARM, BOND for model merging approaches).
- Testing only on one model family.

**Green flags:**
- Comparison across 3+ model families (Llama, Mistral, Gemma etc.).
- Reward-efficiency Pareto frontier (reward vs. KL).
- Human evaluation on a sample.
- Ablation on data quality and mixing ratios.
- Discussion of reward hacking and mitigation.

**Key calibration point:** The RLHF/alignment area has become crowded, making novelty harder. Reviewers now expect more than "we changed X and the win-rate improved" — they want to understand *why* the change works and have evidence that the improvement is not just gaming evaluation.

### 4.3 Reasoning and Chain-of-Thought

**Core question:** Does this method improve reasoning on genuinely hard tasks, and is the improvement due to the proposed mechanism?

**Minimum experimental bar:**
- Evaluate on at least 3 of: GSM8K, MATH, ARC-C, HotpotQA, FEVER, MMLU, StrategyQA, CommonsenseQA.
- Compare to: zero-shot CoT, standard few-shot CoT, self-consistency, and at least one recent strong baseline (Tree of Thought, Self-Discover, Program-Aided Language Models, etc.).
- Report both zero-shot and few-shot comparisons if the method uses examples.
- Cost analysis: tokens used, number of LLM calls.

**Common weaknesses:**
- Evaluating only on knowledge-intensive QA (HotpotQA, FEVER) and claiming general reasoning improvements. Reviewers will point out that math and commonsense reasoning require fundamentally different approaches.
- Not comparing to self-consistency (sampling K completions and taking the majority vote) — a very strong, cheap baseline.
- "Structure-oriented reasoning" or similar approaches may improve performance but via extra LLM calls, which is unfair without compute-matched comparison.
- SARA (avg 4.83, accepted) was criticized for exactly this: "SARA generates far more tokens than any of the baselines; comparison with just a few-shot CoT/ReAct may not suffice since additional tokens are on the input side."

**Green flags:**
- Cost-normalized performance comparison.
- Testing on models from multiple families (GPT-4, Claude, Llama, etc.).
- Analysis of failure modes — when does the method fail?
- Evidence that the specific proposed mechanism is what drives improvement (ablation removing the key component).

### 4.4 Efficiency: PEFT, Quantization, Speculative Decoding

**Core question:** Does this method achieve the same or better performance with significantly less compute, memory, or time, in a fair comparison?

**Minimum experimental bar:**
- Compare full fine-tuning, standard LoRA, and the proposed method at matched parameter counts.
- Report both training speed/memory AND evaluation accuracy.
- Evaluate across multiple tasks to ensure the efficiency gain is not task-specific.
- For quantization: report accuracy degradation at each bit-width.
- For speculative decoding: report actual speedup (not theoretical), wall-clock time.

**Common weaknesses:**
- Only reporting accuracy gains without reporting compute cost.
- Not comparing to the most recent PEFT baselines (LoRA-FA, DoRA, AdaLoRA, etc.).
- Claims of efficiency that are only valid for specific hardware or batch sizes.
- Missing analysis of the efficiency-accuracy trade-off curve.

**Green flags:**
- Pareto curves (accuracy vs. compute/memory/latency).
- Experiments on multiple hardware configurations.
- Theoretical analysis of why the efficiency gain works.
- Scaling analysis (does the efficiency advantage hold at larger scales?).

### 4.5 Safety and Robustness

**Core question:** Is the proposed attack/defense meaningful in a realistic threat model, and does it generalize beyond the specific test cases shown?

**Minimum experimental bar:**
- For attack papers: test against multiple defense methods on multiple models; report attack success rate (ASR) with confidence intervals.
- For defense papers: test against multiple attack types; compare to existing defenses; measure safety-helpfulness tradeoff.
- Define the threat model clearly (white-box vs. black-box, open-weight vs. API access).
- Report false positive rate for defenses (how often are benign inputs incorrectly blocked).

**Common weaknesses:**
- Unclear threat model — who is the attacker, what access do they have?
- Defense does not compare to existing state-of-the-art defenses (Circuit Breaking, Vaccine, Representation Noising, etc.).
- Attack success not tested with adaptive attackers who know the defense.
- Only tested on open-weight models when the threat is most relevant to API-based deployments.
- Missing analysis of why the defense works mechanistically.

**Green flags (from the safety alignment paper, rating 9.5):**
- "The paper is addressing an important problem... that can be very useful to real world problems."
- "The paper ties together prior works in a way that makes it easier to learn from them."
- "The paper includes a good variety of experiments (models, datasets, attacks types) and includes both empirical and theoretical support for their claims."
- Connecting seemingly disparate attack types through a single unified explanation.
- Constrained optimization objective that has theoretical motivation.

**Notable calibration:** The safety alignment paper (9.5) was criticized for: no comparison to circuit breaking, ASR not reaching zero after defense, LLM-as-judge evaluation. These weaknesses did not prevent a near-perfect rating because the conceptual contribution was so strong. In safety papers, identifying a new problem class can be more valuable than a perfect defense.

### 4.6 Evaluation Benchmarks and Datasets

**Core question:** Does this benchmark measure something important that existing benchmarks do not, and is it carefully designed to avoid contamination and confounds?

**Minimum experimental bar:**
- Demonstrate that existing benchmarks are insufficient for the target capability.
- Provide inter-annotator agreement or validation of annotation quality.
- Analysis of data contamination risk (when model training data is known).
- Baseline results across multiple models to establish the benchmark is non-trivial but solvable.
- Meta-evaluation: does performance on the benchmark predict performance on downstream tasks of interest?

**Common weaknesses:**
- New benchmark that largely overlaps with existing ones (redundancy).
- No contamination analysis — especially concerning given that models are trained on large web crawls.
- Poorly defined evaluation criteria or LLM-as-judge without calibration.
- "We find that current models score X on our benchmark" — without demonstrating that X is a meaningful number.

**Green flags:**
- Carefully designed to avoid contamination (e.g., using post-training-cutoff data, or synthetic generation with verified ground truth).
- Multi-dimensional evaluation (scores on multiple sub-capabilities, not just one aggregate number).
- Analysis of what specific failure modes the benchmark reveals.
- Released with evaluation infrastructure.

### 4.7 Agents and Tool Use

**Core question:** Does the proposed agent framework enable LLMs to perform tasks that they cannot perform without the proposed architecture, and is the improvement not simply due to more compute?

**Minimum experimental bar:**
- Compare to: ReAct, Plan-and-Execute, standard CoT, and task-specific state-of-the-art.
- Report success rate on multi-step tasks, not just single-turn accuracy.
- Include failure analysis — what kinds of tasks does the agent fail on?
- Report cost (number of LLM calls, tokens, time per task).
- Test on at least 2–3 different task domains.

**Common weaknesses:**
- Agent performance is due to more LLM calls, not the proposed architecture.
- Only tested on 1 LLM (usually GPT-4) without testing on open-source alternatives.
- Missing ablation on agent components (removing retrieval, removing memory, etc.).
- Evaluation on toy tasks that are too easy for the claimed contribution to be meaningful.

**Green flags:**
- Systematic analysis of when agents fail and why.
- Cost-performance Pareto comparisons.
- Works with multiple LLM backends.
- Task success defined rigorously (not just "response quality").

### 4.8 Retrieval-Augmented Generation (RAG)

**Core question:** Does the proposed retrieval or integration mechanism improve factual accuracy in a way that is robust to retrieval errors and generalizes across domains?

**Minimum experimental bar:**
- Compare to: BM25 + reader, DPR + reader, and standard prompting without retrieval.
- Evaluate on: Natural Questions, TriviaQA, HotpotQA, FEVER, and/or domain-specific QA.
- Test with imperfect retrieval (what happens when retrieved documents are noisy or irrelevant).
- Analyze the contribution of retrieval quality vs. reader quality.

**Common weaknesses:**
- RAG compared to closed-book baselines only (too easy to beat).
- No analysis of retrieval quality (how often does the retrieved document contain the answer?).
- Does not test with adversarial or irrelevant documents.
- Improvements may be due to using a stronger base LLM, not the RAG method.

### 4.9 Multimodal LLMs

**Core question:** Does the proposed method improve cross-modal understanding or generation in a way that cannot be achieved by unimodal models?

**Minimum experimental bar:**
- Compare to strong vision-language baselines (LLaVA, InstructBLIP, GPT-4V where applicable).
- Evaluate on standard benchmarks (VQAv2, MME, MMMU, GQA, NoCaps).
- Include both standard VQA and more complex tasks (visual reasoning, document understanding).
- Ablation on the cross-modal alignment component.

**Common weaknesses:**
- Only compared to much weaker baselines.
- Only tested on one modality type (e.g., only images, not video or audio).
- Architecture change is not motivated — why is this specific cross-modal design better?
- Improvements are not consistent across all benchmarks.

---

## 5. Common Reviewer Phrases and What They Signal

### Strength Phrase Analysis

| Phrase | Count in Strengths | What it Signals |
|---|---|---|
| "novel" | 5,571 | Genuine novelty — reviewer recognizes the contribution as new |
| "ablation" | 3,531 | Ablation studies present and informative |
| "baseline" | 3,517 | Strong baselines included; fair comparison |
| "well-written" / "well written" | 3,905 combined | Paper is clear, easy to follow |
| "reproducib" | 1,046 | Code/details provided; can be reproduced |
| "state-of-the-art" | 858 | Outperforms current SOTA |
| "scalab" | 802 | Method scales with model size or data |
| "strong empirical" | 492 | Empirical evidence is convincing |
| "comprehensive experiments" | 424 | Broad evaluation across tasks/models |
| "significant contribution" | 163 | Reviewer sees this as impactful |

**Key interpretation:** When reviewers cite "ablation" and "baseline" as strengths, the paper has done the minimum required work. When they cite "novel" plus "comprehensive experiments," you are looking at a strong accept.

### Weakness Phrase Analysis

| Phrase | Count in Weaknesses | What it Signals |
|---|---|---|
| "baseline" | 11,973 | Missing baselines — the #1 rejection trigger |
| "novelty" / "limited novelty" | 6,267 combined | Insufficient originality |
| "ablation" | 5,079 | Missing ablation studies |
| "lack of" | 4,233 | Generic weakness flag — usually "lack of ablation/baselines/analysis" |
| "scalab" | 1,679 | Results don't scale or scalability not tested |
| "unclear whether/how/if/why/what/to" | ~4,800 combined | Clarity problems — key aspects not explained |
| "limited to" | 1,381 | Scope is too narrow |
| "reproducib" | 1,235 | Cannot reproduce due to missing details |
| "incremental" | 1,181 | Paper viewed as insufficient advance |
| "fair comparison" | 706 | Baselines are weaker than proposed method for unfair reasons |
| "state-of-the-art" | 999 | Missing comparison to SOTA |

**Critical asymmetry:** "Baseline" appears 11,973 times in weaknesses but only 3,517 in strengths — a 3.4x ratio. This is the single largest asymmetry in the dataset. Missing baselines doom papers; having baselines is table stakes.

**"Unclear" phrases (combined ~4,800 in weaknesses):** This cluster signals that the paper's claims or methods are not clearly articulated. "Unclear whether X implies Y," "unclear how the method handles Z," "unclear what the contribution is beyond A." A paper with many "unclear" phrases in reviews is poorly written or overclaiming.

**Interpreting "incremental":** This word is a soft rejection signal but not automatic. Reviewers use it when the contribution is a combination of existing ideas without new insight. The counter-argument (used by the authors of borderline papers) is to clearly articulate what is novel about the combination. If reviewers see "incremental" in multiple reviews, the paper is unlikely to reach 6+.

---

## 6. Red Flags — Patterns That Reliably Indicate Rejection

These patterns, when present, reliably push ratings into the 1–4 range:

**RF-1: Core mathematical or logical error in the method.**
When reviewers identify a fundamental error in the theoretical foundation (wrong equation, incorrect Bayesian derivation, invalid independence assumption), rejection is near-certain. This is the highest-severity issue because it cannot be fixed in a rebuttal.
- Example: "The core mathematical error lies in the proposed marginalization over Y: P(Y'|X,Y-vec) = sum_Y P(Y'|Y,X,Y-vec)P(Y|X,Y-vec). This equation is fundamentally incorrect as Y represents a ground truth label, not a random variable." (Memorisable Prompting, rating=1)

**RF-2: The "what is the contribution?" problem.**
When all reviewers ask this question, the paper has failed to communicate its novelty. Often the paper reports results of using an existing tool/API on a new dataset without novel insight.
- Example: "What is the real contribution?" (Quantum LLM paper, rating=1)

**RF-3: Missing the obvious baseline that would eliminate the advantage.**
If a reviewer can name a specific existing method that likely achieves the same results, and the paper has not compared to it, this is a critical weakness. The safety alignment paper (9.5) was criticized for not comparing to Circuit Breaking — but survived because the conceptual contribution was larger than the missing comparison. For borderline papers, a single missing critical baseline can tip the vote to reject.

**RF-4: Evaluation is incompatible with the claim.**
If a paper claims "general reasoning improvement" but only evaluates on 2 datasets, or claims "real-world safety improvement" but only tests in a lab setting with perfect threat model knowledge, reviewers will be skeptical. The SARA paper (avg 4.83) was criticized: "Since the authors did not claim the scope of the reasoning problems they are about to address in the introduction, we... should assume this is a solution towards general reasoning. And the general reasoning should evaluate a wide range of domains."

**RF-5: Poor writing that prevents understanding the contribution.**
When reviewers say "even after reading the whole paper, I don't even know what kind of prompt form the authors employ," the paper cannot be evaluated. Poor writing is both a red flag for quality and independently makes it hard to review charitably.

**RF-6: Scope too narrow for the venue audience.**
Papers that apply LLMs to a specialized domain (quantum computing, niche biology applications, specific enterprise software) need to make a compelling case for why the general ML community cares. Without this case, even technically correct papers are viewed as out of scope.

**RF-7: No acknowledgment of important concurrent or prior work.**
Reviewers who are experts in the area know the recent arxiv literature. Papers that fail to cite directly related work (especially work that reduces the novelty claim) are viewed as either careless or dishonest. The safety alignment paper was criticized for a large list of missing citations despite being rated 9.5 — for papers near the borderline, missing citations can be fatal.

**RF-8: Token/compute budget confound in multi-agent or prompting papers.**
When a paper's "improvement" comes from using many more LLM calls than the baseline, and no compute-normalized comparison is provided, reviewers correctly flag this as unfair. "SARA generates far more tokens than any of the baselines" — this undermines the comparison.

---

## 7. Green Flags — Patterns That Reliably Indicate Acceptance

**GF-1: Unifying explanation for previously fragmented phenomena.**
Papers that introduce a single concept that explains multiple existing observations are highly valued. The safety alignment paper connected prefilling attacks, GCG attacks, sampling attacks, and fine-tuning attacks under "shallow alignment." This single conceptual move justified an oral acceptance despite technical weaknesses.

**GF-2: Multi-level evidence (correlational + causal + interventional).**
The best interpretability/mechanistic papers provide evidence at multiple levels. "Do I Know This Entity?" identified features (correlational), showed they affect model outputs (causal via activation steering), and demonstrated transfer from base to chat model (unexpected generalization). Reviewers noted: "fruitfully pursues multiple lines of evidence for its core claims."

**GF-3: Experiments at scale with consistent results across model sizes.**
Architecture and pretraining papers that demonstrate consistent improvements across model sizes (e.g., 300M, 1B, 3B parameters) are much more convincing than single-size comparisons. The Differential Transformer followed scaling laws and showed consistent improvement, which is a strong signal the finding is real and not a hyperparameter artifact.

**GF-4: Simple mechanism that works surprisingly well.**
Papers where the core idea can be explained in two sentences and still produces strong results tend to be rated highly. "The proposed modification of attention in Diff Transformer is well-motivated" and "while the technique itself is not complex, this is the first work to propose a new architecture using differential attention." Simplicity is a feature.

**GF-5: Identifies a previously unknown or underappreciated phenomenon.**
"The paper revealed that the knowledge of a large language model can be detected from a sparse latent space." Finding that entity recognition directions generalize across entity types and transfer from base to instruction-tuned models was a genuine discovery.

**GF-6: Connects insights across sub-areas.**
Papers that bridge, say, mechanistic interpretability and alignment, or pretraining dynamics and in-context learning, attract broad reviewer interest. The safety alignment paper explicitly bridged the alignment literature (RLHF/DPO) with the jailbreak attack literature.

**GF-7: Rigorous experiment design with appropriate statistical reporting.**
Error bars, multiple seeds, held-out test sets, calibrated metrics, statistical significance tests. These signal methodological maturity and distinguish genuinely strong results from noise.

**GF-8: Practical, deployable solution with a clear threat model.**
In safety, efficiency, and alignment papers, having a clearly defined practical setting (who uses this, in what deployment context, against what threat) makes the contribution concrete and actionable.

---

## 8. Typical Baselines Expected by Sub-Area

### Pretraining/Architecture
- Standard Transformer (Vaswani et al., 2017) at matched compute
- GPT-2/3/LLaMA at matched scale
- RetNet, Mamba, GLA (for papers claiming efficiency advantages over attention)
- FlashAttention-based Transformer for efficiency comparisons

### Instruction Tuning / RLHF
- Supervised fine-tuning (SFT) baseline
- DPO (Direct Preference Optimization, Rafailov et al., 2023) — now mandatory
- PPO-based RLHF (Ouyang et al., 2022)
- Best-of-N sampling
- WARP, WARM (for model merging/soup approaches)
- BOND, REBEL, XPO (for newer RL-based methods)

### Reasoning / Chain-of-Thought
- Zero-shot CoT ("Let's think step by step")
- Few-shot CoT (standard prompting with examples)
- Self-Consistency (majority vote over N samples)
- Tree of Thought, Graph of Thought
- Least-to-Most Prompting, Decomposed Prompting
- Program-Aided Language Models (PAL)
- For agent papers: ReAct, Plan-and-Execute, LATM

### Safety / Alignment Robustness
- Standard RLHF/DPO alignment (no defense)
- Circuit Breakers / Short Circuiting (Zou et al., 2024)
- Vaccine (Huang et al., 2024)
- Representation Noising
- GCG attack (for adversarial robustness)
- Harmless refusal rate / ASR on AdvBench/HarmBench

### Efficiency (PEFT)
- Full fine-tuning
- Standard LoRA (Hu et al., 2022)
- Prefix Tuning
- Prompt Tuning
- DoRA, AdaLoRA, LoRA+ (for papers claiming improvements over LoRA)
- QLoRA (for quantization + fine-tuning)

### RAG
- Closed-book GPT baseline (no retrieval)
- BM25 + reader
- DPR + reader
- Standard RAG (Lewis et al., 2020)
- RAG-Fusion, HyDE

### Evaluation / Benchmarking
- Current SOTA models (GPT-4, Claude, Gemini, open-source SOTA)
- Simple heuristic baselines (to show the task is non-trivial)
- Human performance (for tasks where meaningful)

---

## 9. Calibration Examples — Worked Examples from Actual Papers

### Example 1: Excellent Paper (Rating 9.5)
**Title:** "Safety Alignment Should be Made More Than Just a Few Tokens Deep"
**Forum ID:** 6Mxhg9PtDE
**Avg Rating:** 9.5 | Decision: Accept (Oral)

**Why it scored 9.5:**
- Identified a single unifying explanation (shallow alignment) for four distinct attack types that had previously been studied in isolation. This is the hallmark of an excellent paper: one idea that illuminates many things.
- Provided both an empirical diagnosis (KL divergence is concentrated in first few tokens of aligned model vs. base model) and practical solutions (data augmentation for input-space attacks, constrained SFT for fine-tuning attacks).
- Experiments were comprehensive: multiple models, multiple attack types, with evidence that the proposed defenses work.
- Writing quality was "excellent" per one reviewer.
- "The paper flows nicely. It is nicely organized."

**Weaknesses that did not prevent high rating:**
- No comparison to circuit breaking (missing baseline).
- ASR not reduced to zero by the proposed defenses.
- Uses LLM-as-judge without human calibration.
- Non-greedy decoding without variance reporting.

**Lesson for AI judge:** A conceptually transformative paper can overcome missing baselines if the core contribution is strong enough. When multiple weaknesses are present but the paper clearly identifies a new problem class and opens research directions, rate it highly. The test: can a reasonable researcher point to this paper as the source of a new research agenda? If yes, rate 8+.

---

### Example 2: Excellent Paper (Rating 9.0)
**Title:** "Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models"
**Forum ID:** WCRQFlji2q
**Avg Rating:** 9.0 | Decision: Accept (Oral)

**Why it scored 9.0:**
- Discovered that sparse autoencoders (SAEs) can extract entity recognition directions that predict whether a model will hallucinate about a given entity.
- Multi-level evidence: correlational (the features fire differently for known vs. unknown entities), causal (steering activations changes model behavior), and transfer (base model features transfer to chat model).
- Well-written, with "the prose is very clear and arguments are well structured."
- The finding that base model mechanisms are repurposed during RLHF chat-tuning is a non-obvious and impactful discovery.

**Weaknesses that were present:**
- Only tested on Gemma 2B and 9B (limited model diversity).
- Some claims not rigorously quantified (e.g., degree of generalization across entity types).
- Mechanistic analysis could use more statistical rigor.

**Lesson for AI judge:** Discovery papers that reveal how models work internally — especially with multi-level causal evidence — deserve high ratings even if model diversity is limited. The counterfactual is: do we learn something fundamentally new about how LLMs represent and use knowledge? If yes, and the evidence is credible, rate 8+.

---

### Example 3: Good Paper (Rating 8.0)
**Title:** "Differential Transformer"
**Forum ID:** OvoCm1gGhN
**Avg Rating:** 8.0 | Decision: Accept (Oral)

**Why it scored 8.0 and not higher:**
- All four reviewers gave 8, indicating consensus on a strong but not exceptional paper.
- Novel architecture (differential attention) validated at scale — this is the key.
- All reviewers noted strengths: "solid and well-written paper," "first work to propose a new architecture using differential attention," "extensive experimental validation."
- Missing: no comparison to sparse attention methods despite claiming sparsity benefits; no instruction tuning experiments; missing related work section; no analysis of why RMSNorm is critical.

**What would have pushed this to 9–10:**
- Comparison to other attention variants (sparse attention, linear attention).
- Analysis of attention sparsity (claimed but not quantified).
- Instruction-tuning experiments on the architecture.
- Missing related work section is unusual and reduces confidence in the contribution's novelty.

**Lesson for AI judge:** Architecture papers that are well-validated at scale, with consistent improvements across benchmarks, deserve 7–8 even if some analyses are missing. What separates 8 from higher: the paper claims mechanisms (sparsity) without fully quantifying them. "The authors mention promoting the emergence of sparse attention patterns multiple times... but do not provide statistics and quantification of the sparsity."

---

### Example 4: Borderline Paper (Rating 4.83, Accepted)
**Title:** "SALSA: Soup-based Alignment Learning for Stronger Adaptation in RLHF"
**Forum ID:** AN6PIiObp0
**Avg Rating:** 4.83 | Decision: Accept

**Why it was borderline:**
- Interesting and novel core idea (model soup as RLHF reference model) but:
  - Insufficiently justified mechanism (why does the midpoint work best?).
  - Missing DPO comparison (critical for RLHF papers).
  - Missing WARP, WARM (closely related prior work not acknowledged).
  - No theoretical analysis.
  - Experiments show higher win-rate but KL not controlled, so reward hacking possible.
- Reviewer ratings were 5/5/5/6/3/5 — moderate disagreement, all near borderline.

**Why it was still accepted:**
- The core idea is genuinely novel and the empirical results do show improvements.
- The paper is well-structured and the idea is clearly communicated.
- No fatal flaws — weaknesses are gaps in evidence, not errors.

**Lesson for AI judge:** A borderline RLHF/alignment paper will be accepted if the idea is novel and the experiments are positive, even if critical baselines (DPO, reward-free methods) are missing. The question is whether the missing evidence would likely overturn the conclusion. If probably not, lean toward accept. At ~78% acceptance rate, borderline papers are usually accepted.

---

### Example 5: Borderline Paper (Rating 4.83, Accepted)
**Title:** "Make LLMs Better Zero-Shot Reasoners: Structure-oriented Autonomous Reasoning"
**Forum ID:** rLaMcF516k
**Avg Rating:** 4.83 | Decision: Accept

**Why it was borderline:**
- Multi-agent reasoning system (SARA) with ablations, but:
  - Evaluated on limited datasets (HotpotQA, FEVER, MMLU subsets) — no GSM8K, MATH, StrategyQA.
  - No compute-normalized comparison (SARA uses far more tokens than baselines).
  - Comparison to retrieval-augmented baselines without retrieval-free ablation for SARA.
  - Limited model diversity.
  - PGM-based theoretical section takes 3 pages but does not yield practical insight.
- Reviewer ratings were 6/3/3/8/6/3 — high disagreement.

**Key tension:** One reviewer (rating=8) found the experimental protocol "really good" with "complete ablations and versatility to multiple base models." Other reviewers (rating=3) found the evaluation insufficient and the novelty limited.

**Lesson for AI judge:** High reviewer disagreement on a borderline paper often reflects genuine ambiguity. When one reviewer gives 8 and others give 3, look carefully at whether the 8-rater has specific insight the others lack, or whether they evaluated differently. If the 8-rater's points are well-grounded, the paper may deserve closer to a 5–6. If the 3-raters identify systematic weaknesses, lean toward reject.

---

### Example 6: Low Paper (Rating 1.67, Rejected)
**Title:** "Memorisable Prompting: Preventing LLMs Forgetting False Positive Alarm"
**Forum ID:** 3viQDuclu0
**Avg Rating:** 1.67 | Decision: Reject

**Why it failed:**
- Core mathematical error: marginalization over ground truth labels as random variables is conceptually wrong.
- Writing was poor: "multiple formatting errors," undefined symbols, figures not referenced.
- The method was not clearly described — reviewers couldn't reproduce it.
- Comparison baseline was not meaningful.
- "Even after reading the whole paper, I don't even know what kind of prompt form the authors employ."

**Lesson for AI judge:** Mathematical errors in the core method, combined with poor writing, guarantee rejection. Rate 1–2.

---

## 10. Decision Rubric — Structured Scoring Guide

Use the following rubric to arrive at a calibrated rating. Work through each dimension and combine according to the weights below.

### Step 1: Identify the paper type

- Architecture/pretraining
- Method (alignment/RLHF/efficiency/safety/reasoning)
- Analysis/interpretability
- Benchmark/dataset
- Application

This determines which baselines are expected and which standards apply.

### Step 2: Score Each Dimension

#### Novelty (0–3 points)
- 0: No novel contribution; application of existing tool to new task without insight.
- 1: Incremental improvement to known method; contribution could have been predicted.
- 2: Clear novel contribution; extends prior work in non-obvious way.
- 3: Genuinely new framing, mechanism, or finding; opens research directions.

#### Technical Soundness (0–3 points)
- 0: Core mathematical error or invalid experimental design.
- 1: Main claims plausible but inadequately supported.
- 2: Main claims well-supported with minor gaps.
- 3: Rigorous; alternative explanations ruled out; uncertainty quantified.

#### Baselines and Empirical Evaluation (0–3 points)
- 0: Missing the most critical baseline(s) entirely.
- 1: Baselines present but missing 1–2 important comparisons.
- 2: All standard baselines included; fair comparison.
- 3: Comprehensive baselines + compute-normalized + ablations + human eval.

#### Ablations (0–2 points)
- 0: No ablations of key design choices.
- 1: Partial ablations present.
- 2: All key components ablated; contribution of each understood.

#### Clarity and Reproducibility (0–2 points)
- 0: Cannot understand the method from the paper; would not be reproducible.
- 1: Understandable with effort; partially reproducible.
- 2: Clear writing; full hyperparameters; code released or equivalent.

#### Scale and Generalization (0–2 points)
- 0: Only tested at tiny scale or on 1 model/dataset.
- 1: Moderate scale; tested on 2–3 models or datasets.
- 2: Large-scale validation; generalizes across model families and benchmarks.

### Step 3: Convert to Rating

| Total Points | Rating Range | Typical Decision |
|---|---|---|
| 14–15 | 9–10 | Accept (Oral) |
| 11–13 | 7–8 | Accept (Oral/Spotlight) |
| 8–10 | 5–6 | Accept (Poster) |
| 5–7 | 4–5 | Borderline; context-dependent |
| 2–4 | 2–3 | Reject |
| 0–1 | 1 | Strong Reject |

### Step 4: Apply Modifiers

**Upward modifiers (+0.5 to +1.0 on final rating):**
- Paper opens a new, high-impact research direction even if execution is imperfect.
- Unifying explanation for multiple previously disparate phenomena.
- Multi-level evidence (correlational + causal + interventional).
- First paper to do X at scale (where X is valuable and not trivial).

**Downward modifiers (-0.5 to -1.5 on final rating):**
- Core mathematical or logical error (severe: -1.5).
- Missing the single most important baseline for the sub-area (-0.5 to -1.0).
- Evaluation is unfair (compute budget, weaker models as comparison) (-0.5 to -1.0).
- Writing so poor that the contribution cannot be assessed (-1.0).
- Scope clearly outside the venue's interests (-0.5).

### Step 5: Calibrate Against Population Statistics

Given that the mean rating is 4.73 and std is 1.26:
- A rating of 6 means "top third of accepted papers."
- A rating of 8 means "top 2.3% of all papers."
- A rating of 4–5 means "typical accepted paper" at venues with 78% acceptance.
- A rating of 3 means "should be rejected."

**Final calibration check:**
Ask yourself: if this paper were accepted, would researchers building on it in 2 years have a solid foundation? Would it be cited in related work sections? Would it be on a recommended reading list for PhD students entering this sub-area? If the answer is clearly yes: rate 6+. If yes but with significant caveats: rate 5. If the answer is no or uncertain: rate 4 or below.

---

## Appendix: Quick Reference — Sub-Area Checklists

### Architecture Paper Checklist
- [ ] Large-scale training (1B+ parameters, 10B+ tokens)
- [ ] Comparison to Transformer at matched compute
- [ ] Multiple downstream benchmarks
- [ ] Ablation of each novel component
- [ ] Efficiency analysis (FLOPs, throughput)
- [ ] Scaling law analysis
- [ ] Related work covering Transformer variants

### Alignment/RLHF Paper Checklist
- [ ] Comparison to SFT, DPO, PPO
- [ ] Win-rate on MT-Bench or Arena-Hard
- [ ] KL divergence analysis
- [ ] Multiple model families
- [ ] Safety-helpfulness tradeoff
- [ ] Reward hacking analysis

### Reasoning Paper Checklist
- [ ] GSM8K/MATH for math; HotpotQA/FEVER for QA; MMLU for knowledge
- [ ] Comparison to CoT, self-consistency, recent SOTA
- [ ] Compute-normalized comparison
- [ ] Ablation of each reasoning component
- [ ] Failure mode analysis

### Safety Paper Checklist
- [ ] Clear threat model (white/black box, open/closed weight)
- [ ] Multiple attack types
- [ ] Comparison to existing defenses (Circuit Breaking, Vaccine, etc.)
- [ ] False positive analysis
- [ ] Mechanistic explanation of why the defense works

### Interpretability Paper Checklist
- [ ] Correlational evidence
- [ ] Causal evidence (activation patching, steering)
- [ ] Multiple entity types / conditions
- [ ] Generalization to held-out cases
- [ ] Statistical significance for all claims
- [ ] Analysis on multiple models

### Efficiency/PEFT Paper Checklist
- [ ] Comparison to full fine-tuning and standard LoRA
- [ ] Accuracy vs. compute Pareto curve
- [ ] Multiple task types
- [ ] Hardware-specific implementation details
- [ ] Scaling analysis

---

*This skill file is based on analysis of 8,419 language model papers from ICLR 2024–2025 and NeurIPS 2023–2024, with detailed calibration examples drawn from reviewed papers. Ratings and reviewer comments reflect the actual reviewing community standards at these venues.*
