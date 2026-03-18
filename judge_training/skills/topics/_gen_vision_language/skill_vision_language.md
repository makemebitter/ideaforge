# Skill File: Evaluating Vision-Language (VL) Papers

> **Purpose**: This file provides an AI judge with the knowledge, criteria, and heuristics needed to give calibrated, expert-level evaluations of research ideas and papers in the **vision-language** topic area. It is grounded in analysis of 1,945 VL papers submitted to ICLR and NeurIPS, with an acceptance rate of ~74% and mean reviewer rating of 4.72 (median 4.67, std 1.13).

---

## 1. Area Overview and Scope

Vision-language (VL) research studies the intersection of visual perception and natural language understanding. At top venues (ICLR, NeurIPS, ICML), this umbrella covers a broad set of subfields unified by the theme of grounding visual information in language and vice versa.

### 1.1 Core Subfields

| Subfield | Representative Methods | Key Goal |
|---|---|---|
| **CLIP / Contrastive VLMs** | CLIP, SigLIP, ALIGN, Florence, EVA-CLIP | Pre-train joint vision-language embedding spaces via contrastive objectives on image-text pairs |
| **Large Multimodal Models (LMMs/MLLMs)** | LLaVA, InstructBLIP, mPLUG-Owl, CogVLM, GPT-4V, Gemini | Extend LLMs with visual input for instruction-following, VQA, captioning |
| **Prompt Tuning / PEFT for VLMs** | CoOp, CoCoOp, MaPLe, PromptSRC, CLIP-Adapter, Tip-Adapter, APE | Efficient adaptation of pretrained VLMs to downstream tasks with few examples |
| **Benchmarking and Evaluation** | MMBench, SEED-Bench, MMMU, MMStar, PhysBench, LOKI | Systematic evaluation of VLM capabilities across diverse tasks and domains |
| **Visual Grounding and Referring** | GLIP, Grounding DINO, UNINEXT, Ferret | Localizing visual regions from text expressions |
| **VQA and Image Captioning** | BLIP, BLIP-2, OFA | Answering questions about images; generating descriptions |
| **Hyperbolic / Hierarchical VLMs** | MERU, HyCoCLIP | Embedding visual-linguistic hierarchies in non-Euclidean spaces |
| **Vision-Language-Action (VLA)** | RT-2, OpenVLA, Octo | VLMs applied to robotic control and embodied AI |
| **Medical / Scientific VLMs** | BioViL, LLaVA-Med, MedFlamingo | Domain-specific VLMs for clinical or scientific data |
| **Multimodal RAG and Agents** | MM-ReAct, Visual-ChatGPT | VLMs combined with tool use, retrieval, or agent frameworks |
| **Safety and Trustworthiness** | Hallucination analysis, adversarial robustness, bias detection | Understanding and mitigating failure modes of VLMs |
| **Efficient VLMs** | LLaVA-1.5, MobileVLM, token compression, quantization | Reducing compute requirements while retaining capability |
| **Analysis / Interpretability** | DAAM, attention analysis, text-based decomposition | Understanding internal representations of VLMs |
| **Synthetic Data Detection** | LOKI, fake image/video detection benchmarks | Using VLMs to detect AI-generated content |
| **Continual Learning for VLMs** | LVLM-CL, CLIP-based CIL | Incremental adaptation of VLMs without catastrophic forgetting |

### 1.2 Structural Characteristics of the VL Research Space

VL research is unusually broad. A paper might propose a new training objective for CLIP, build a benchmark of 100K questions, introduce a prompt tuning method for domain generalization, or analyze why VLMs fail at physical reasoning. These are evaluated by different standards. The judge must first identify *which subfield* a paper belongs to before applying specific criteria.

Key structural observations:
- **Benchmarking papers** form a significant fraction of accepted VL work. A well-constructed benchmark with broad coverage, strong data quality controls, and surprising findings can be accepted even without a new model.
- **Prompt tuning papers** (CoOp variants) have become a crowded subfield. The bar for novelty has risen substantially since 2022, and reviewers now expect comparisons against MaPLe, PromptSRC, and APE at minimum.
- **MLLM papers** (LLaVA-style) are now highly competitive. Architecture-only contributions are insufficient; the contribution must be a new capability, a new evaluation finding, or a new training methodology with broad applicability.
- **Analysis papers** (e.g., studying modality gap, attention heads, alignment) can reach high ratings if they combine controlled experiments, novel metrics, and actionable insights.

---

## 2. Rating Scale Calibration

Based on 1,945 papers; ratings on the 0–8 scale used at ICLR/NeurIPS:

| Rating | Label | What It Means in VL Context |
|---|---|---|
| **8** | Top-tier (Oral/Spotlight) | Exceptional: new fundamental insight, or a benchmark that reshapes evaluation, or a method that achieves dramatically better results with a principled explanation. ~30 papers (~1.5%) reach this. |
| **6–7** | Good (Spotlight/Accept) | Clear, solid contribution. Advances the field in a specific subfield with well-executed experiments, sound methodology, and good baselines. ~1,294 papers in this tier. |
| **5** | Borderline Accept | One or two notable weaknesses (missing a baseline, limited novelty, narrow evaluation) but the core idea is sound and the execution is reasonable. High variance among reviewers. |
| **4** | Borderline Reject | The idea is not wrong but reviewers are unconvinced. Typically: incremental over prior work, missing key comparisons, or evaluation too narrow. Issues not fixable in rebuttal. |
| **3** | Weak Reject | Multiple significant weaknesses. Limited novelty over cited work, missing obvious baselines, experimental setup has confounds. |
| **1–2** | Strong Reject | Fundamental problems: wrong claims, missing the most basic related work, unsubstantiated results, or not relevant to venue. |

**Calibration notes specific to VL:**
- The mean rating is 4.72, slightly below 5, meaning the "average" VL paper falls just below borderline accept. Papers must actively do something right to be accepted.
- The acceptance rate is 74%, but this is skewed by the breadth of the area and the volume of benchmark/dataset papers, which tend to be accepted at lower average ratings when the dataset is genuinely useful and well-validated.
- Oral papers in VL typically have a clear "aha" finding that changes how practitioners or researchers think—not just better numbers.
- avg_soundness (2.6), avg_contribution (2.4), avg_presentation (2.68) all sit just above the midpoint of the 1–4 scale, confirming that reviewers in VL are not lenient—typical papers receive "good but not excellent" marks across all dimensions.

---

## 3. What Reviewers Care About

### 3.1 Strength Phrases (Grounded in Frequency Data)

The following are positive signals reviewers use, with the frequency and what they mean concretely:

1. **Novel / novelty** (1,224 + 113 mentions as strength): Reviewers look for genuinely new ideas. In VL, this means: a new training signal, a new benchmark filling an identified gap, a new theoretical insight into VLM behavior, or a new method for a known problem that is principled rather than heuristic.

   *Example (ICLR 2025 Oral, HyCoCLIP)*: "The central idea is clever and novel – utilizing the hierarchical nature of nouns mentioned in image captions as supervision for a hyperbolic model." The novelty was specifically the combination of hyperbolic space + compositional hierarchy from grounded noun phrases.

2. **Ablation** (1,100 mentions as strength): Reviewers praise papers that systematically ablate each component. In VL, expected ablations include: removing each loss term, testing different prompt lengths, comparing different backbone sizes, testing different dataset sizes.

   *What good ablation looks like*: Table 1 in HyCoCLIP directly compared CLIP trained on additional image-text boxes (no improvement) vs. HyCoCLIP on the same data (significant improvement), demonstrating that the hierarchical loss itself drives gains, not just extra data.

3. **Baseline** (835 mentions as strength): Having the right baselines is a signal that authors understand the field. Reviewers note when a paper includes hard-to-beat comparisons and still prevails.

4. **Well-written** (600 mentions): VL papers span multiple communities (CV, NLP, ML). Clear exposition, consistent notation, and well-motivated problem statements are rewarded because the audience is diverse.

5. **State-of-the-art** (278 mentions): Quantitative improvements matter, but reviewers care about margin. A 0.5% improvement on ImageNet is not compelling; a 5% improvement on a task where progress had stalled is.

6. **Reproducible** (247 mentions): Releasing code, providing hyperparameters, and making datasets available. Particularly important for benchmarks (otherwise they cannot be used by the community).

7. **Scalable** (201 mentions): Does the method work with larger models? Does it transfer to ViT-L as well as ViT-B? Does the benchmark cover multiple scales?

8. **Comprehensive evaluation / strong empirical** (130 + 122 mentions): Testing on many benchmarks, many models, many settings. The LOKI benchmark paper (ICLR 2025 Spotlight, 8.0) was praised for evaluating 22 open-source and 6 closed-source LMMs across 5 modalities, 26 categories, and 18K+ questions.

9. **Strong performance / comprehensive experiments** (111 + 110 mentions): Multiple tasks + multiple baselines + multiple metrics.

### 3.2 Weakness Phrases (Grounded in Frequency Data)

1. **Baseline** (2,765 mentions as weakness): Missing baselines is the #1 complaint in VL, just as in other ML areas. In VL, this is especially acute because:
   - The field moves extremely fast; a paper from 6 months ago may be the relevant baseline.
   - Many prompt tuning methods have comparable performance; omitting any one of them raises suspicion.
   - LMM papers must compare against LLaVA-1.5, InstructBLIP, MiniGPT-4, and ideally GPT-4V.

   *Example (MMDocBench, ICLR 2025 Reject)*: "The selected proprietary models such as GPT-4o and GPT-4v are homogeneous, and the authors may consider other proprietary models such as Gemini-1.5 and Claude-3.5." Missing baselines in a benchmark paper invalidates comparisons.

2. **Ablation** (1,527 mentions as weakness): Missing ablations prevent understanding of which component drives results. This is particularly damaging for method papers that combine prompt learning + adapters (e.g., PAT, ICLR 2026 Reject, rating 2.0): reviewers could not determine if gains came from prompt tuning, adapter tuning, or the alignment loss.

3. **Novelty / limited novelty / incremental** (1,366 + 373 + 134 mentions): The most common rejection reason in VL. Reviewers recognize when a method is "CoOp + adapter + regularization" without principled motivation.

   *Example (PAT, ICLR 2026, rating 2.0)*: "The core techniques—prompt learning, adapter tuning, and contrastive regularization—are all based on existing methods. The paper primarily repurposes these techniques for VLM adaptation without introducing fundamentally novel algorithms or theoretical insights."

   *Example (DOR for prompt miscalibration, ICLR 2025, accepted at 5.25)*: Accepted despite novelty concerns because it identified a real problem (calibration trade-off in prompt tuning) and provided empirical evidence across multiple datasets, even if the solution was not groundbreaking.

4. **Lack of** (953 mentions): Generic complaint covering missing experiments, missing analysis, missing motivation, missing discussion of related work.

5. **Unclear whether / unclear how / unclear why / unclear if** (335 + 332 + 117 + 101 mentions): Design choices not motivated, generalization claims not justified, claims about model behavior that are assertions rather than evidence.

   *Example (PhysBench, ICLR 2025 Oral)*: Despite being accepted, reviewers asked detailed questions: "Does that mean PhysAgent is dataset dependent?" and "How does it support the claim that PhysAgent retains generalization abilities?" The authors addressed these in rebuttal.

6. **Reproducible** (325 mentions): Missing code, missing hyperparameters, unclear experimental details. For benchmarks, this means: are annotation guidelines available? Is the leaderboard maintained?

7. **Limited to** (295 mentions): Method only works for specific settings—e.g., only CLIP ViT-B/16, only zero-shot anomaly detection, only industrial datasets.

8. **Fair comparison** (195 mentions): Different model sizes, different pretraining data, different numbers of training shots used for baselines vs. the proposed method.

9. **State-of-the-art** (292 mentions as weakness): Method does not reach or surpass relevant SOTA. In VL, this is especially damaging when the paper claims improvement but the improvement is below noise level.

---

## 4. Evaluation Criteria and Rubric

Evaluate every VL paper on five dimensions, each 1–4:

### 4.1 Novelty / Originality (1–4)

**4 (Excellent)**: The paper introduces a fundamentally new insight, objective, benchmark design, or problem formulation.
- New theoretical explanation for a known empirical phenomenon (e.g., modality gap caused by information imbalance, not cone effects or object bias alone)
- New benchmark that reveals capabilities VLMs were assumed to have but demonstrably lack (e.g., PhysBench revealing that ALL 39 tested VLMs fail on physical reasoning tasks; LOKI revealing that LMMs cannot reliably detect synthetic data across modalities)
- New pre-training objective that changes how we think about VLM training (e.g., compositional entailment learning using hyperbolic space + grounded noun phrases)
- New interpretability framework that enables new downstream applications (e.g., text-based decomposition of CLIP attention heads enabling spurious-correlation removal)

**3 (Good)**: Clear incremental advance with insight. A new loss function or training procedure that solves a known problem in a principled way; a new benchmark that covers an underexplored capability with non-trivial data collection; empirically discovering a new phenomenon in MLLM behavior with controlled experiments; a new adaptation method that outperforms the prompt tuning SOTA with a clear explanation.

**2 (Fair)**: Mostly combining existing methods. Applying CoOp + adapter tuning + contrastive regularization; a new VQA benchmark that is similar to existing ones with slightly different topic coverage; a method that extends PromptSRC with an additional regularization term without understanding why it helps.

**1 (Poor)**: Direct replication, trivial extension, or combination of existing methods without justification. A benchmark that simply reuses existing datasets with new prompts. A prompt tuning method that adds a hyperparameter without explaining its role.

**Key questions for novelty assessment in VL:**
- Can the core contribution be stated in one sentence that would surprise an expert in this subfield?
- For method papers: what specifically is new—is it the loss, the architecture, the training procedure, or the problem framing?
- For benchmark papers: what capability gap does this benchmark expose, and why couldn't existing benchmarks expose it?
- For analysis papers: does this paper change how practitioners should think about or use VLMs?
- Is the contribution subfield-generic (applicable to all VLMs) or highly specialized?

### 4.2 Technical Soundness (1–4)

**4 (Excellent)**: Claims are rigorously justified. Experimental claims have appropriate controls, fair comparisons, and are replicated across architectures. Theory (if present) is correct and complete. No obvious gaps between motivation and execution.

**3 (Good)**: Mostly sound. Minor gaps (missing hyperparameter sensitivity, one baseline not included, or one claim not fully supported). The main result is solid and trustworthy.

**2 (Fair)**: Notable soundness issues. The experimental setup has confounds (e.g., different backbone sizes between proposed method and baselines; base model fine-tuned differently; IoU metric measured inconsistently across models). Key claims rest on weak evidence or are asserted without ablation.

   *Example (MMDocBench, rating 4.25)*: IoU scores were notably low for all models (GPT-4 achieves only 2.44%) despite those same models scoring well on other metrics, suggesting either a measurement error or an invalid metric—but this was not investigated or explained.

**1 (Poor)**: Fundamental soundness issues. Unfair comparisons that benefit the proposed method. Claims contradicted by results. Assumptions in theoretical sections are unrealistic (e.g., assuming Gaussian-distributed VLM features without validation). The loss is non-differentiable but the paper claims to optimize via gradient descent.

   *Example (PAT, rating 2.0)*: "The proposed technique claims probability distributions but assumes a Gaussian distribution—which is unrealistic, since a proper probabilistic model should satisfy the simplex constraint. Additionally, the paper mentions the proposed loss is non-differentiable, but does not explain how it is optimized."

**Key questions for soundness:**
- Are baselines fairly tuned? Do they use the same CLIP backbone, same training shots, same evaluation protocol?
- For benchmark papers: are annotations verified? Is inter-annotator agreement reported? Is data contamination with pretraining data addressed?
- For MLLM papers: is the comparison at the same model size and training data?
- Are ablations complete, or are components added in bundles without individual isolation?
- For prompt tuning: are results reported on both base and novel classes? Only reporting one is misleading.

### 4.3 Empirical Contribution / Experiments (1–4)

**4 (Excellent)**: Comprehensive. Multiple benchmarks tested. Multiple model sizes and architectures. All relevant baselines included. Analysis experiments (not just numbers) that build understanding. Results clearly outperform on standard benchmarks while being tested on harder benchmarks too.

   *Example*: PhysBench (ICLR 2025 Oral) tested 39 VLMs, covered 4 major physical understanding dimensions and 19 sub-tasks, provided error analysis, showed transfer to embodied AI tasks, and analyzed the correlation between physical understanding benchmarks and general VLM benchmarks.

**3 (Good)**: Solid evaluation on standard benchmarks. The main baselines are present. Core claim is demonstrated with multiple experiments. Some analysis beyond just numbers.

**2 (Fair)**: Limited scope. Only tested on 2–3 datasets. Key baselines are missing. Evaluation is primarily on tasks where the method is favorable. Marginal improvements that could be within noise.

**1 (Poor)**: Experiments do not support the claims. No ablation. Only toy datasets. Comparisons are against undertuned or old baselines only.

**Domain-specific benchmark expectations (by subfield — see Section 5 for detail):**
- **CLIP-style methods**: ImageNet zero-shot, VTAB, COCO retrieval, Winoground/ARO
- **Prompt tuning**: Base-to-novel generalization, cross-dataset generalization (from ImageNet to OOD datasets like EuroSAT, DTD, Caltech101), domain generalization
- **MLLMs**: MMBench, SEED-Bench, MMMU, LLaVA-Bench; optionally MMStar, MME, HallusionBench
- **Benchmarks**: Human performance baselines, comparison with 10+ existing models, inter-annotator agreement, contamination analysis
- **Efficient VLMs**: Compute-accuracy tradeoff curves, comparison at matched parameters and FLOPs
- **Analysis papers**: Multiple model families, both controlled (synthetic) and naturalistic (real model) experiments

### 4.4 Presentation / Clarity (1–4)

**4 (Excellent)**: Beautifully written. Problem precisely motivated. Related work comprehensive. Method section self-contained. Figures explain the method at a glance. Notation consistent and defined.

**3 (Good)**: Clear and readable with modest effort. Minor issues (undefined symbol, a figure that doesn't add information, related work missing one citation).

**2 (Fair)**: Hard to follow. Key definitions missing. Method described in text does not match the figure. Notation inconsistent (e.g., using `Clsa...Clsn` in one equation and `clsA...clsB` in a figure without reconciliation). Referencing errors (table numbers wrong).

   *Example (LVLM-CL, rating 2.5)*: "Paper suffers from frequent grammatical errors, awkward phrasing and inconsistent terminology. Most of the in-text citations are incorrectly formatted. References to images and tables within text are often incorrect."

   *Example (LOKI, rating 8.0)*: "The paper is easy to read and well-organised. Extensive examples and case studies provided in appendices."

**1 (Poor)**: Significant writing problems. Key related work missing. Claims not substantiated in text. Logical inconsistencies. Table captions like "Results." are not acceptable.

### 4.5 Broader Impact / Significance (1–4)

**4 (Excellent)**: Opens a new research direction, reveals a fundamental limitation of VLMs that motivates new research, or enables new applications. Likely to generate substantial follow-on work.

   *Example*: Interpreting CLIP's image representation via text-based decomposition (ICLR 2024 Oral, 8.0) demonstrated that CLIP attention heads have interpretable, specialized roles—this opened new directions for model editing, spurious correlation removal, and zero-shot segmentation.

**3 (Good)**: Solid contribution to a clearly active research area. Will be cited by practitioners in this subfield. A new benchmark with >10K questions covering a real capability gap is a 3 on impact even if the findings are not groundbreaking.

**2 (Fair)**: Incremental advance. Useful but narrow. A new prompt tuning variant that improves average base+novel accuracy by 0.5% will be cited but not widely adopted.

**1 (Poor)**: Marginal or unclear contribution. Contribution is too specialized to matter beyond a narrow application (e.g., a benchmark with 3 datasets and 2 models evaluated, only on image classification).

---

## 5. Subfield-Specific Standards

### 5.1 CLIP / Contrastive VLMs

**What this includes**: New pretraining objectives, new data curation methods, analysis of CLIP behavior, new variants that improve zero-shot transfer.

**Expected baselines**:
- CLIP (ViT-B/16, ViT-L/14) — always required
- SigLIP — required for recent papers (2024+)
- ALIGN, Florence, EVA-CLIP — include if the comparison is about pretraining scale
- MERU — required if hyperbolic space is involved
- SLIP, DeCLIP, PyramidCLIP — for contrastive training variants

**Expected benchmarks**:
- Zero-shot ImageNet (top-1 accuracy) — always required
- COCO and Flickr30K image-text retrieval (R@1, R@5, R@10) — for retrieval-focused work
- VTAB (Visual Task Adaptation Benchmark) — for transfer learning claims
- Winoground, ARO (Attribution, Relation, Order) — for compositional understanding claims
- ObjectNet, ImageNet-V2, ImageNet-R, ImageNet-Sketch — for robustness claims
- Linear probe on ImageNet and VTAB-Full — for representation quality claims
- Attribute/relation benchmarks (SugarCrepe, CREPE) — for claims about compositionality

**What makes a contribution strong**:
- New understanding of *why* CLIP works or fails (empirically or theoretically)—e.g., modality gap analysis, information imbalance
- New metrics that characterize CLIP behavior better than existing ones (e.g., RMG, MOAD)
- A new training signal that improves *both* zero-shot classification and compositional benchmarks (it's easy to improve one at the cost of the other)
- Analysis that covers many model variants (98 VLMs is impressive; 2–3 is insufficient for making general claims)
- Post-hoc correction methods that are training-free and verifiably effective

**Common weaknesses flagged**:
- Claims about "CLIP in general" supported only by ViT-B/16 experiments
- Analysis on synthetic/controlled datasets that doesn't extend to real pretrained models
- Missing the most directly competing analysis paper (e.g., not citing Liang et al. on modality gap if studying modality gap)
- Zero-shot improvement on ImageNet that comes at the cost of compositional benchmarks (not disclosed)

### 5.2 Large Multimodal Models (MLLMs / LMMs)

**What this includes**: New architectures, new training procedures, new instruction tuning datasets, new evaluation findings about MLLMs.

**Expected baselines** (cite appropriately by year):
- LLaVA-1.5 (2023) — the reference open-source MLLM
- InstructBLIP — early instruction-tuned VLM
- MiniGPT-4, mPLUG-Owl2 — other open-source comparisons
- BLIP-2 — for architecture comparisons
- GPT-4V / GPT-4o — for closed-source upper bound
- Gemini-1.5, Claude-3.5 — for closed-source comparison if GPT-4V is included
- LLaVA-NeXT, LLaVA-OneVision — for papers after 2024

**Expected benchmarks**:
- MMBench (Chinese and English) — standard classification benchmark
- SEED-Bench — comprehensive seed evaluation
- MMMU — university-level multi-discipline QA
- MMStar — harder, reduced data contamination risk
- LLaVA-Bench (in-the-wild) — open-ended evaluation
- MME — comprehensive capability evaluation
- HallusionBench or POPE — hallucination evaluation
- ScienceQA — science reasoning
- For specific capabilities: TextVQA (OCR), ChartQA (chart understanding), DocVQA (document understanding), VQAv2 (general VQA)

**What makes a contribution strong**:
- A new finding about MLLM behavior that is counterintuitive and well-supported (e.g., PhysBench: all frontier MLLMs fail on physical reasoning, and fine-tuning on physical understanding data transfers to robot manipulation)
- A new training methodology that improves performance across multiple benchmarks simultaneously, not just one
- A new modality integration strategy with clear ablation showing why the design works
- Cross-dataset transfer: if fine-tuning on task X improves task Y, that's a compelling scientific finding

**Common weaknesses flagged**:
- Comparisons to LLaVA-1.5 only, ignoring LLaVA-NeXT and stronger 2024 baselines
- Improvements only on MMBench while degrading on other benchmarks (not disclosed)
- Method described at high level without sufficient implementation detail (what is the base LLM? How are visual tokens processed? What dataset is used for fine-tuning?)
- "Multimodal" paper that only tests vision + language, not other modalities despite claiming generality

### 5.3 Benchmarking and Evaluation Papers

**What makes a benchmark paper publishable at top venues**:
- Exposing a *specific, measurable capability gap* that existing benchmarks cannot measure
- Data quality validation: inter-annotator agreement (IAA), contamination check, difficulty analysis, human performance baseline
- Broad model coverage: evaluate 10+ models (mix of open-source and closed-source)
- Non-trivial findings: the benchmark should reveal surprising things about model capabilities
- Sustained release: leaderboard, maintainable data format

**What reviewers demand for benchmark papers**:
- Comparison with existing benchmarks in a table (what tasks? how many samples? what modalities? what ground truth type?)
- Human performance as an upper bound
- Detailed annotation guidelines and validation procedures
- Error analysis and failure mode analysis
- Contamination concern addressed (if test data could overlap with model training data)

**Examples from reviewed papers**:
- *LOKI (ICLR 2025 Spotlight, 8.0)*: Accepted because it covered 5 modalities, 26 subcategories, 18K+ questions, evaluated 28 models, introduced Normalized Bias Index (NBI) as a new metric, and revealed that LMMs perform poorly even on basic authenticity detection.
- *PhysBench (ICLR 2025 Oral, 8.0)*: Accepted because it covered 4 major dimensions, 19 tasks, 100K entries, tested 39 VLMs, provided human performance, error type analysis, and demonstrated embodied AI transfer.
- *MMDocBench (ICLR 2025 Reject, 4.25)*: Rejected because the "fine-grained" framing was not sufficiently differentiated from DocVQA / ChartQA / MMLongBench-Doc, the IoU metric had suspicious results that were not explained, and missing baselines like Gemini-1.5, UReader, and LLVAR.

**Red flags for benchmark papers**:
- "We propose a benchmark" without showing what existing benchmarks cannot measure
- No human performance baseline
- Small-scale (< 2K test instances) without strong justification
- Only evaluating 2–5 models (insufficient to draw conclusions)
- Primary contribution is combining existing datasets with new prompts

### 5.4 Prompt Tuning / Parameter-Efficient VLM Adaptation

**What this includes**: CoOp variants, adapter-based methods, test-time adaptation, lightweight fine-tuning.

**Expected baselines** (as of 2025):
- CoOp (minimal baseline)
- CoCoOp (context optimization + conditional)
- MaPLe (multi-modal prompt learning)
- PromptSRC (self-regulating context optimization)
- CLIP-Adapter
- Tip-Adapter (training-free adapter)
- APE (adaptive prior refinement)
- KgCoOp (knowledge-guided context optimization)
- DePT, ProDA — for distribution-level prompt tuning
- TCP, ProGrad — for calibration-aware methods

**Expected evaluation protocol** (must include all):
1. **Base-to-novel generalization**: Train on base classes, test on novel classes. Report base accuracy, novel accuracy, and harmonic mean (HM). This is the standard evaluation introduced by CoCoOp.
2. **Cross-dataset generalization**: Train on ImageNet, test on 10 other datasets (EuroSAT, DTD, FGVCAircraft, Food101, UCF101, Caltech101, OxfordPets, Flowers102, SUN397, StanfordCars).
3. **Domain generalization**: Train on ImageNet, test on ImageNet-V2, ImageNet-Sketch, ImageNet-A, ImageNet-R.
4. **Few-shot accuracy**: 1, 2, 4, 8, 16 shots on main datasets.

**What makes a prompt tuning contribution strong**:
- Identifying a new failure mode (e.g., calibration trade-off, overfitting to visual distribution) and fixing it with principled insight
- Improving novel class accuracy without sacrificing base class accuracy (the key tension in this subfield)
- Method that is architecture-agnostic (works for ViT-B/16 and ViT-L/14)
- Theoretical motivation for why the proposed method avoids the observed failure mode

**Example (DOR for calibration, ICLR 2025, 5.25 accept)**:
Accepted because it identified a calibration trade-off (CoOp overconfident on novel classes; KgCoOp underconfident on base classes) with empirical evidence, and proposed Dynamic Outlier Regularization with ablations on multiple datasets. Borderline because reviewers noted it didn't compare against CoPrompt and PromptSRC, both of which address the same calibration issue.

**Common weaknesses**:
- Only comparing against CoOp and CoCoOp, ignoring MaPLe, PromptSRC
- Missing the harmonic mean of base+novel (reporting only one is misleading)
- Method improves on 16-shot but doesn't improve on 1-shot (no acknowledgment)
- Ablation does not isolate prompt component from adapter component
- Not comparing against the best existing adapter (CLIP-Adapter, Tip-Adapter)

### 5.5 Analysis / Understanding Papers

**What this includes**: Mechanistic analysis of VLM internals (attention heads, layers, embeddings), empirical studies of VLM failure modes, theoretical analyses of training dynamics.

**Expected standards**:
- Multiple model architectures (at least two different scales or families)
- Controlled synthetic experiments AND validation on real pretrained models
- New metrics or evaluation tools that others can use to study these phenomena
- Actionable insights: the analysis should suggest a method or design choice

**What makes analysis papers strong**:
- *New theoretical framework* that unifies previously separate observations (e.g., modality gap + object bias → information imbalance as unified cause)
- *Precise, falsifiable claims* with controlled experiments that rule out confounders
- *Transferable tools*: new metrics (RMG, MOAD), decomposition algorithms (TextBase), or visualizations that others can use

**Example (Interpreting CLIP via text-based decomposition, ICLR 2024 Oral, 8.0)**:
Scored highly because it provided a reusable algorithm (TextBase) that decomposes CLIP image representations into text-aligned components, validated on multiple architectures, revealed interpretable head roles (location, shape, color), and enabled practical applications (zero-shot segmentation, spurious correlation removal). All reviewers gave 8.

**Common weaknesses**:
- Findings only validated on CLIP ViT-B/16, not generalized to ViT-L or SigLIP
- Controlled experiments on synthetic data with weak evidence on real models
- "Interesting finding" without actionable implication
- Alternative explanations not ruled out

### 5.6 Efficient VLMs

**What this includes**: Token compression, quantization, pruning, knowledge distillation for VLMs, mobile-friendly VLMs.

**Required for acceptance**:
- Compute-accuracy tradeoff curves (not just a single operating point)
- Comparison at matched parameter counts or FLOPs
- Evaluation across multiple benchmarks (not just ImageNet)
- Validation that efficiency gains don't come from reduced input resolution (unless that's explicit)

**What reviewers expect**:
- Latency / throughput measurements on real hardware (not just theoretical FLOPs)
- Comparison against MobileVLM, MobileNetV3-based approaches, or other mobile-oriented baselines
- Quantization: compare against GPTQ, AWQ, SmoothQuant at matched bit-widths
- Token compression: compare against FastViT, ToMe (Token Merging), EViT

**Common weaknesses**:
- Only reporting accuracy without compute cost
- Efficiency gain measured on non-standard hardware without reproducibility
- Missing the primary PEFT comparison at matched parameter count

### 5.7 Continual Learning for VLMs

**What this includes**: Class-incremental learning with VLMs, sequential instruction tuning, catastrophic forgetting in VLMs.

**Expected baselines** (as of 2025):
- LwF (Learning without Forgetting)
- EWC (Elastic Weight Consolidation)
- DualPrompt, L2P (prompt-based continual learning)
- iCaRL (for class-incremental)
- CoIN (Continual Instruction Tuning benchmark)
- CLIP-based CIL methods (AttriCLIP, Class-Incremental Learning with CLIP)

**What makes a contribution strong**:
- New setting that is genuinely different from existing continual learning (not just applying DualPrompt to a VLM without modification)
- Large-scale evaluation with 10+ tasks and multiple model families
- Addressing catastrophic forgetting with a principled method (not just a memory buffer)

**Common rejection patterns** (from LVLM-CL and MCIL benchmark):
- CoIN benchmark already exists and covers the same setting; must differentiate clearly
- Only evaluating one VLM architecture (e.g., only LLaVA)
- Comparing only against zero-shot (not against existing CIL methods applied to the same VLM)
- Dataset is only 3 small-scale classification datasets (Oxford Flowers, CUB, DVM-CAR)
- Presentation quality issues (missing citations, wrong table references, grammatical errors)

---

## 6. Common Failure Modes

### 6.1 The "Module Soup" Anti-Pattern

The most common rejection pattern in VL method papers: combining existing components (prompt learning + adapter tuning + contrastive regularization + alignment loss) without principled motivation. The method section simply adds several loss terms with weights (λ₁ · L₁ + λ₂ · L₂ + λ₃ · L₃) without explaining why each component is necessary, what problem each addresses, and how they interact.

Reviewers immediately ask: "What would happen if you removed component X?" If the ablation is missing, or if the ablation shows one component dominates, the paper's claimed novelty evaporates.

*From PAT (ICLR 2026, rating 2.0)*: "The work seems to be a direct combination of prompt tuning and adapter tuning. Even when combined, the model complexity and training cost are higher than using either alone. What's the additional benefits beyond performance gains?"

**Warning sign**: The method section says "we combine A and B" and the ablation shows A+B > A and A+B > B, but doesn't explain *why* the combination helps.

### 6.2 Missing the Field-Defining Baseline

Different from "missing a baseline" generally — this is missing the single most important comparison. In VL:
- Prompt tuning paper without PromptSRC or MaPLe
- MLLM paper without LLaVA-1.5
- CLIP analysis paper without citing Liang et al. (2022) on modality gap
- Benchmark paper without comparison to MMMU, MMBench, or SEED-Bench in a comparison table
- Continual learning paper without CoIN or DualPrompt

Reviewers know the field. Missing the most critical baseline is a signal that the authors are not fully aware of the state-of-the-art, which undermines confidence in all other claims.

### 6.3 Narrow Evaluation Masking Poor Generalization

Papers that evaluate only on tasks or settings where the proposed method was designed to work, without testing on broader or harder tasks. This is common in:
- Prompt tuning: reporting only 16-shot accuracy on ImageNet, not cross-dataset or base-to-novel
- Anomaly detection: testing on industrial datasets (MVTec, VisA) but not generalizing conclusions
- Benchmark papers: only evaluating models that were known to struggle with the proposed task

*From FuzzyCLIP (ICLR 2025, borderline 5.25)*: "In two out of five datasets, their method does not outperform AnomalyCLIP, which raises questions about the general applicability of their approach."

### 6.4 Benchmark Papers with Weak Differentiation

A benchmark paper fails when reviewers cannot identify what it measures that existing benchmarks do not. MMDocBench was rejected (4.25) in part because reviewers noted DocVQA, ChartQA, TextVQA, and MMLongBench-Doc already required fine-grained visual understanding of documents — the authors did not provide a comparative analysis table showing what MMDocBench uniquely exposes.

**Pattern**: Paper says "existing benchmarks focus on global understanding; we focus on fine-grained understanding" but doesn't demonstrate this distinction quantitatively (e.g., no experiment showing that models with high scores on DocVQA can still fail on MMDocBench).

### 6.5 Benchmark Papers with Data Quality Issues

Reviewers scrutinize data collection methodology:
- How were annotations collected? (crowdsourced vs. expert? IAA threshold?)
- How was contamination with model pretraining data checked?
- Is the evaluation metric appropriate? (Exact Match may not work for generative VLMs; F1 is better for open-ended answers)
- Are the questions free of answer leakage? (e.g., class name appears in the text question)

*From MMDocBench (ICLR 2025, 4.25)*: Reviewers found that IoU scores for all models were suspiciously low (GPT-4 achieves 2.44% despite high EM scores), suggesting the evaluation metric was incorrectly applied to different VLMs that use different coordinate normalization conventions. The authors were not forthcoming about this discrepancy.

### 6.6 Analysis Papers that Don't Rule Out Alternatives

Analysis papers must actively disprove alternative explanations. For example, a paper claiming "information imbalance causes modality gap" must also show that other proposed causes (cone effect at initialization, object bias alone) do not account for the observed modality gap. Papers that only present positive evidence for their hypothesis while ignoring competing explanations are incomplete.

*From "Two Effects, One Trigger" (ICLR 2025 Oral, 8.0)*: Reviewers appreciated that the paper explicitly addressed confounders: "The section effectively demonstrates how common confounding factors affect results, and shows that when they control for these factors, a smaller modality gap indeed leads to better performance."

### 6.7 Continual Learning Papers with Trivial Baselines

CL papers in VL fail when baselines are zero-shot VLMs (without any continual learning method) or when the proposed method is compared only against non-VLM CL methods. The relevant comparison is: existing CL methods *applied to the same VLM*. Papers that show "our VLM-specific method > non-VLM CL methods" may be showing an architecture advantage, not a CL method advantage.

### 6.8 Poor Writing in a Multi-Community Field

VL papers are reviewed by NLP, CV, and ML researchers. Writing quality that is passable within one community can be opaque to another. Specific problems:
- Undefined acronyms (MCIL, ZSAD, EFA introduced without expansion)
- Inconsistent notation (same variable named differently in equations vs. figures)
- Missing figure captions that are self-contained (caption says "Results." — not acceptable)
- Citation formatting errors (bibliography breaks, wrong cross-references)

These are weighed more heavily in VL than in narrower ML subfields because the reviewer pool is diverse.

---

## 7. What Excellence Looks Like

### 7.1 Characteristics of High-Rated VL Papers (Rating 8)

All five ICLR 2025 oral/spotlight papers at rating 8.0 in this sample share these properties:

**1. A clear, testable central claim that is surprising**
- "Two Effects, One Trigger" (8.0 Oral): *Information imbalance (not cone effects, not object bias directly) is the root cause of both the modality gap and object bias in CLIP.* This was counterintuitive because prior work attributed these phenomena to separate causes.
- "PhysBench" (8.0 Oral): *All 39 tested VLMs—including GPT-4V and Gemini—have a significant gap from human performance on physical reasoning, and this gap transfers predictively to embodied AI performance.* Surprising because these models were assumed to have strong physical reasoning.
- "HyCoCLIP" (8.0 Oral): *Training CLIP with compositional entailment losses in hyperbolic space using automatically extracted noun-phrase grounding improves both standard benchmarks and hierarchical understanding.* Principled and elegant.
- "Interpreting CLIP" (2024 Oral): *Specific attention heads in CLIP are interpretable via text—they specialize in location, shape, color, etc.—and removing heads associated with spurious features improves downstream accuracy.* Immediately actionable.
- "LOKI" (8.0 Spotlight): *A comprehensive benchmark revealing that state-of-the-art LMMs cannot reliably detect synthetic data across modalities, with systematic bias toward treating synthetic data as real.*

**2. Comprehensive, well-controlled experiments**
- Coverage across multiple model families (not just one backbone)
- Ablations that isolate the key contribution
- Analysis experiments that build understanding, not just numeric comparisons
- Human performance or theoretical upper bound provided

**3. New tools or metrics that others can use**
- MOAD (measures object/attribute bias in VLMs)
- RMG (Relative Modality Gap, a better metric than L2M)
- NBI (Normalized Bias Index for synthetic detection benchmarks)
- TextBase decomposition algorithm
- PhysBench benchmark + PhysAgent framework

**4. Clear, actionable takeaways**
- High-rated papers don't just describe what they found; they explain what it means for the field. "Caption enrichment and trainable temperature can reduce information imbalance and improve attribute recognition" is more useful than "we observe that information imbalance exists."

**5. The paper was revised in response to reviewer feedback**
- Several oral papers in this sample explicitly addressed reviewer concerns during the rebuttal phase. Papers that engage substantively with reviewer concerns and update accordingly (e.g., adding new experiments, clarifying claims) tend to have their scores raised.

### 7.2 The Difference Between Rating 6 and Rating 8

- Rating 6: The paper makes a valid contribution that advances the field. The experiments are solid, the baselines are present, the writing is clear. But there is no "aha" insight—it is well-executed incremental work.
- Rating 8: There is a specific finding or method that experts would say "this changed how I think about VLMs." The experiments are designed to *prove a point*, not just to *demonstrate performance*.

---

## 8. Red Flags and Instant Rejection Criteria

Always flag these issues explicitly in your evaluation:

### 8.1 Missing the Primary Baseline for the Subfield
If a prompt tuning paper doesn't compare against MaPLe/PromptSRC, or a MLLM paper doesn't compare against LLaVA-1.5, or a benchmark paper doesn't discuss MMBench/SEED-Bench — this is a fundamental issue, not a minor weakness. It suggests the authors are not current with the literature.

### 8.2 Evaluation Protocol Violations
- Reporting base-class accuracy only in a base-to-novel paper (the real metric is harmonic mean)
- Testing on different numbers of shots for different methods
- Evaluating the same test set used for method development (data leakage)
- Using CLIP as an out-of-the-box baseline at suboptimal configuration

### 8.3 Benchmark Data Quality Issues
- No IAA (inter-annotator agreement) for subjective annotations
- No contamination analysis (especially for benchmarks that could overlap with training data of tested LMMs)
- Test set too small to draw conclusions (< 500 questions per task)
- Metric obviously unsuitable for the task (exact match for free-form VLM output)

### 8.4 Fabricated or Misreported Baselines
If a baseline from a prior paper is reported significantly lower than in its original publication (>2% difference), the comparison is suspect. The proposed method's gains may not be real.

### 8.5 Incremental Benchmark with No Differentiation
A benchmark that is "like DocVQA but with more tasks" — without any experiment showing that models which score well on DocVQA fail on the new benchmark — provides no evidence that the new benchmark is necessary.

### 8.6 Method Only Applicable to a Specific Setting
A prompt tuning method that works only for anomaly detection (FuzzyCLIP) but claims general applicability to VLMs. Or a CLIP analysis that only holds for ViT-B/16 but claims to characterize "contrastive VLMs" generally.

### 8.7 Impossible or Unjustified Claims
- "We are the first to study X" without acknowledging clearly related prior work (X exists in the literature)
- "Our method generalizes to all VLMs" without testing beyond CLIP
- "We improve calibration" without defining the calibration metric or its statistical validity

### 8.8 Critical Writing Failures
- Non-differentiable loss claimed to be trained by gradient descent
- Symbol defined differently in equation vs. figure
- Results table that is a duplicate of another table (reviewers catch this)
- Missing introduction section header (yes, this appears in rejected papers)

---

## 9. Accept / Reject Decision Heuristics for Borderline Papers

### 9.1 The Fundamental Question
Does this paper leave the field better off? Specifically:
- Does it provide a new benchmark that practitioners can use to identify VLM weaknesses?
- Does it provide a new insight that changes how researchers think about VLMs?
- Does it provide a new method that practitioners can deploy?
- Does it identify a new failure mode that motivates future work?

If the answer to at least one of these is yes AND the execution is sound → accept (5–6).

### 9.2 Borderline Accept Heuristics (Score ~5)

Accept if ALL of the following hold:
- The core problem being addressed is real and acknowledged by reviewers as important
- The proposed method or benchmark is not identical to prior work (even if similar)
- The experimental results are positive on most evaluated benchmarks
- The paper demonstrates awareness of the most important related work
- Weaknesses are addressable in a revised version (not fundamental)

*Example (DOR for prompt miscalibration, ICLR 2025, 5.25)*: Accepted despite not comparing against CoPrompt and PromptSRC, because the identified problem (calibration trade-off) was acknowledged as real, the proposed fix (outlier regularization) was empirically demonstrated on multiple datasets, and the issue of missing comparisons was addressable. Average reviewer rating split: two gave 6, one gave 3, one gave 6.

### 9.3 Borderline Reject Heuristics (Score ~4)

Reject if ANY of the following hold:
- The primary baseline is missing AND the gains would likely disappear with the right baseline
- The benchmark paper doesn't show what existing benchmarks cannot capture
- The method is a direct combination of prior work without clear insight into the combination
- The evaluation protocol is flawed in a way that invalidates the main result
- The claims about generalization are not supported by the experiments

*Example (MMDocBench, ICLR 2025, 4.25)*: Two reviewers gave 3; core issue was insufficient differentiation from existing benchmarks (DocVQA, MMLongBench-Doc) and an IoU metric with suspicious results that weren't explained.

*Example (FuzzyCLIP, ICLR 2025, 5.25 — note the reject despite the score)*: Mixed scores (8, 5, 3, 5). One reviewer gave 8 but majority found: (1) limited innovation over AnomalyCLIP; (2) method fails on 2/5 datasets compared against the primary baseline; (3) notation inconsistencies suggesting rushed paper preparation.

### 9.4 For Method Papers: The "Why Does It Work?" Test
A paper that achieves good numbers but cannot explain *why* its method works is a borderline reject. The question "why does combining X and Y improve over X or Y alone?" must be answered empirically (with ablation showing the interaction effect) or theoretically. Papers that answer this clearly jump from 4 to 6.

### 9.5 For Benchmark Papers: The "Surprising Finding" Test
A benchmark paper is more likely to be accepted if its evaluation reveals at least one surprising finding:
- "GPT-4V achieves only 38% on PhysBench, close to random chance on Dynamics tasks" — surprising
- "All LMMs show systematic bias toward classifying synthetic audio as real in LOKI" — surprising
- "Models that score well on general VLM benchmarks (MMBench, SEED) do not necessarily score well on physical reasoning (PhysBench)" — surprising and useful

Without at least one surprising finding, a benchmark paper is documentation, not research.

### 9.6 For Analysis Papers: The "Alternative Explanation" Test
Analysis papers that don't rule out the most obvious alternative explanation for their finding should be pushed toward borderline reject. The burden of proof for mechanistic claims is high: correlation data is necessary but not sufficient; controlled experiments that remove confounders are required.

---

## 10. Example Calibration Cases

### 10.1 Rating 8.0 Oral: "Two Effects, One Trigger" (ICLR 2025)
**Paper**: Analyzed modality gap and object bias in CLIP, found information imbalance (image contains more information than text) as the unified root cause.
**Why it scored 8.0**:
- Controlled experiments with 98 VLMs (comprehensive scale)
- New metrics (RMG for modality gap, MOAD for object bias) that are better than existing ones
- New finding that confounders (model size, training data) explain the false positive correlation between modality gap and performance
- Actionable remedy (caption enrichment, trainable temperature)
- Well-written with 7 clear takeaways
**What reviewers flagged (but accepted anyway)**: Evidence on real pretrained models (vs. synthetic data) was weaker; presentation quality was "fair" not "excellent" for one reviewer.
**Lesson**: Novel insight + 98-model evidence + new metrics + actionable remedy = Oral even with minor presentation weaknesses.

### 10.2 Rating 8.0 Oral: "PhysBench" (ICLR 2025)
**Paper**: 100K-question benchmark for physical world understanding; tested 39 VLMs; proposed PhysAgent framework.
**Why it scored 8.0**:
- Coverage of 19 tasks across 4 dimensions
- Human performance baseline showing large gap to VLMs
- Error type analysis identifying perceptual errors vs. knowledge deficits
- Transfer to embodied AI (fine-tuning on PhysBench improves robot manipulation)
- Comprehensive comparison revealing all frontier models fail at physics
**What reviewers flagged**: Some PhysAgent details were unclear; embodied AI experiments could be fairer. But the benchmark itself was strong enough to carry the paper.

### 10.3 Rating 8.0 Oral: "HyCoCLIP" (ICLR 2025)
**Paper**: Pre-trains VLMs with hierarchical compositional contrastive + entailment losses in hyperbolic space using GRIT (20.5M image-text pairs with grounded noun phrases).
**Why it scored 8.0**:
- Elegant and simple idea (hierarchical nouns → hyperbolic training signal)
- Table 1 ablation showing that CLIP + extra data ≠ HyCoCLIP (the loss matters, not just data)
- Strong performance on classification, retrieval, detection, scene understanding
- Automatic procedure to extract noun-phrase bounding boxes is reproducible
**What reviewers flagged**: Should compare against newer VLMs; batch size limited by memory. Minor concerns.

### 10.4 Rating 8.0 Spotlight: "LOKI Benchmark" (ICLR 2025)
**Paper**: Comprehensive benchmark for LMM-based synthetic data detection across 5 modalities, 26 categories, 18K+ questions.
**Why it scored 8.0**:
- Addresses a timely and underserved problem (deepfake/synthetic content detection)
- Introduced NBI metric for measuring model bias
- Evaluated 28 models with revealing findings (Claude-3.5 misclassifies synthetic images as real)
- Multi-level task design (binary judgment + MCQ + anomaly selection + explanation)
**What reviewers flagged**: Dataset size relatively small; deepfake detection category absent; limited analysis of why CoT doesn't help.

### 10.5 Rating 8.0 Oral: "Interpreting CLIP via Text-Based Decomposition" (ICLR 2024)
**Paper**: Decomposes CLIP image representations by layers, heads, and tokens using text embeddings; finds interpretable head roles; demonstrates spurious correlation removal and zero-shot segmentation.
**Why it scored 8.0**:
- TextBase algorithm is novel and reusable by others
- Multiple downstream applications enabled by the analysis
- Tested on multiple CLIP architectures and scales
- All four reviewers gave exactly 8
**Lesson**: Analysis papers can score 8 if the insight is fundamental, the method is reusable, and there are multiple compelling applications.

### 10.6 Rating 5.25 Accept: "DOR for Prompt Miscalibration" (ICLR 2025)
**Paper**: Dynamic Outlier Regularization to address calibration trade-off between base/novel classes in prompt tuning.
**Why it was borderline accepted**:
- Real problem identified (CoOp overconfident on novel; KgCoOp underconfident on base)
- Multiple datasets tested with consistent improvement
- DOR is lightweight and pluggable
**Why it almost wasn't accepted**:
- Missing comparison against CoPrompt and PromptSRC (methods that already address calibration)
- Improvement over vanilla TCP was inconsistent
- Limited analysis of *why* outlier regularization fixes calibration
**Lesson**: Identifying a real problem and providing empirical evidence can carry a paper to borderline accept, even with gaps.

### 10.7 Rating 5.25 Reject: "FuzzyCLIP" (ICLR 2025)
**Paper**: Clustering-driven stacked prompts for zero-shot anomaly detection.
**Why it was rejected despite 5.25 average**:
- High variance (8, 5, 3, 5) with majority finding limited novelty
- Method fails to outperform AnomalyCLIP on 2 of 5 datasets
- Notation inconsistencies (CSP vs. CFP; different equation variable names)
- One reviewer who gave 8 acknowledged "one major concern is the incremental nature of this work"
**Lesson**: High variance with novelty concerns + inconsistent results + notation issues = reject even at 5.25 average.

### 10.8 Rating 4.25 Reject: "MMDocBench" (ICLR 2025)
**Paper**: Benchmark for fine-grained visual document understanding.
**Why it was rejected**:
- Insufficient differentiation from DocVQA, ChartQA, MMLongBench-Doc
- IoU metric results inconsistent (high EM/F1 but near-zero IoU for same models)
- Missing Gemini-1.5, Claude-3.5 in closed-source evaluations
- No experiment showing gap between existing benchmarks and MMDocBench
**Lesson**: Benchmark papers need to prove they measure something existing benchmarks don't, and metric design must be consistent with model evaluation protocols.

### 10.9 Rating 2.5 Reject: "LVLM-CL" (ICLR 2025)
**Paper**: Continual learning for LVLMs with task-specific prompts and memory bank.
**Why it was rejected**:
- CoIN benchmark already exists for LVLM continual instruction tuning (not differentiated from)
- Only evaluated on LLaVA-1.5 with no other VLM
- Compared against zero-shot models, not existing CL methods
- Writing: grammatical errors, citation formatting errors, wrong table references, missing symbols
**Lesson**: Insufficient differentiation from existing work + only one architecture + poor writing quality = strong reject.

### 10.10 Rating 2.0 Reject: "PAT - Bootstrap Prompt Learning" (ICLR 2026)
**Paper**: Combined prompt learning + adapter tuning with tolerance regularization for CLIP adaptation.
**Why it was rejected**:
- All three reviewers gave 2: unanimously poor
- "Tolerance loss overlaps SigLIP" — similar to an established, well-cited method
- "Claims to be the first successful attempt to simultaneously combine prompt and adapter tuning" — false; APoLLo (EMNLP 2023) and CLIP-Adapter precede this
- Non-differentiable loss optimized via gradient descent (mathematical error)
- Gaussian distribution assumption for VLM features (invalid)
- Gains are within 1% of SOTA on 11 datasets, not enough to justify the added complexity
**Lesson**: False novelty claims + mathematical errors + overlooked prior work = 2.0 even if the application domain is reasonable.

### 10.11 Rating 2.3 Reject: "Multimodal Class-Incremental Learning Benchmark" (ICLR 2025)
**Paper**: Proposed MCIL benchmark using Oxford Flowers, CUB, DVM-CAR with Flava model.
**Why it was rejected**:
- Three existing VLM continual learning benchmarks already cover this setting
- Only three small-scale, narrow-domain datasets
- Only one VLM (Flava) evaluated — CLIP experiments missing
- No new CL method; only existing methods applied
- Paper is 7 pages of main content ("semi-finished product")
**Lesson**: Benchmark papers with only 3 datasets, 1 model, and no differentiation from prior benchmarks are strong rejects.

---

## 11. Evaluation Checklist

When evaluating a VL research idea or paper, work through:

**Subfield Identification:**
- [ ] Which VL subfield does this paper belong to? (CLIP, MLLM, benchmark, prompt tuning, etc.)
- [ ] Are subfield-specific standards being applied?

**Novelty Check:**
- [ ] What is the core new contribution in one sentence?
- [ ] What is the closest prior work, and how does this differ substantively?
- [ ] Would an expert in this subfield say "I didn't know this before reading the paper"?
- [ ] Is this combination of existing methods, or genuinely new framing?

**Baseline Check:**
- [ ] What are the field-defining baselines for this subfield? Are they all included?
- [ ] For CLIP methods: CLIP (ViT-B/16 + ViT-L/14), SigLIP?
- [ ] For prompt tuning: CoOp, CoCoOp, MaPLe, PromptSRC, KgCoOp at minimum?
- [ ] For MLLMs: LLaVA-1.5, InstructBLIP, GPT-4V?
- [ ] For benchmarks: comparison table with existing benchmarks?
- [ ] Are the baselines from the same model size and training budget?

**Evaluation Protocol Check:**
- [ ] For prompt tuning: base-to-novel, cross-dataset, domain generalization all reported?
- [ ] For MLLMs: multiple benchmarks (not just MMBench)?
- [ ] For benchmarks: human performance, IAA, contamination analysis?
- [ ] Are evaluation metrics appropriate for the task?
- [ ] Error bars / multiple seeds / statistical significance?

**Soundness Check:**
- [ ] Are ablations present and isolating individual contributions?
- [ ] Are there confounds in the comparison (different backbone, different training data)?
- [ ] For analysis papers: are alternative explanations addressed?
- [ ] Any mathematical errors or unjustified assumptions?

**Impact Check:**
- [ ] Does the paper have at least one surprising finding or actionable insight?
- [ ] For benchmarks: what do we now know about VLMs that we didn't know before?
- [ ] For methods: does it enable a practically useful application?

**Red Flag Check:**
- [ ] Missing the primary related work for this subfield?
- [ ] Baseline reported lower than in original paper?
- [ ] Only half of the standard evaluation protocol reported?
- [ ] Claims of novelty that are contradicted by cited prior work?
- [ ] Notation inconsistencies suggesting rushed preparation?
- [ ] Non-differentiable or mathematically invalid loss claimed to be optimized by gradient descent?

---

## 12. Key Technical Concepts for Evaluating VL Papers

### 12.1 VLM Representation Space Concepts
- **Modality gap**: Image and text embeddings occupy separate regions of the embedding sphere. Causes: information imbalance (image has more information than its caption), cone effect at initialization, training dynamics.
- **Object bias**: CLIP-like models assign high similarity to images based on object category rather than attributes (color, texture, relations). Connected to information imbalance: captions rarely describe attributes as richly as images depict them.
- **Temperature scaling (τ)**: Controls sharpness of contrastive distribution in training. Lower τ = harder negatives, stronger gradient from near-positives. Critical hyperparameter; sensitivity analysis required.
- **Information imbalance**: The gap between information present in the image and information present in the paired text. Root cause of modality gap and object bias in contrastive VLMs.

### 12.2 Base-to-Novel Generalization in Prompt Tuning
The standard evaluation protocol for VLM adaptation:
- Train with prompts on *base classes* (e.g., 500 ImageNet classes)
- Evaluate on *base classes* and *novel classes* (e.g., 500 unseen ImageNet classes)
- Report: Base accuracy, Novel accuracy, Harmonic Mean (HM = 2·Base·Novel/(Base+Novel))
- The tension: CoOp improves base but hurts novel; CoCoOp and PromptSRC maintain both. A new method that improves HM without hurting base is the goal.

### 12.3 Hyperbolic Space for VLMs
- Hyperbolic space is negatively curved; it naturally represents hierarchies (trees can be embedded with low distortion).
- In hyperbolic VLMs (MERU, HyCoCLIP): visual concepts at different levels of abstraction are embedded at different depths in the Poincaré ball.
- Entailment cone: a region of hyperbolic space that contains all concepts "more specific than" a given concept. Image regions should be entailed by their corresponding text phrases.
- Key parameter: curvature c. Must be ablated.

### 12.4 MLLM Architecture
Modern MLLMs consist of:
1. **Visual encoder**: Usually a CLIP ViT (image → visual tokens)
2. **Vision-language connector**: Linear projection (LLaVA), Q-Former (BLIP-2), or resampler (Flamingo)
3. **LLM backbone**: LLaMA, Vicuna, Mistral, or proprietary
4. **Training stages**: (1) connector pretraining on image-caption data; (2) visual instruction tuning on VQA/conversation data
The quality of each stage and the data used matter enormously; reviewers ask about training data when MLLM results seem inconsistent.

### 12.5 Common VLM Evaluation Benchmarks Explained
- **MMBench**: Multiple-choice questions across 20 dimensions; diverse topics; Chinese and English versions.
- **SEED-Bench**: 12 evaluation dimensions including spatial relationships, action recognition, image captioning.
- **MMMU**: University-level questions requiring college-level domain knowledge; 30 disciplines.
- **MMStar**: Filtered benchmark designed to minimize data contamination; "stars" are questions models cannot answer without visual understanding.
- **HallusionBench**: Tests hallucination (does the model say things that aren't in the image?).
- **POPE**: Object existence hallucination benchmark (does the model hallucinate objects?).
- **LLaVA-Bench (In-the-Wild)**: Open-ended conversation and QA; GPT-4 as judge.
- **PhysBench**: Physical world understanding (object properties, spatial relations, scene, dynamics).
- **LOKI**: Synthetic data detection across 5 modalities.

---

## 13. Final Guidance for the Judge

**The fundamental question for VL papers**: Does this paper help us understand, evaluate, or improve vision-language models in a way that advances the field?

- **If yes, with strong evidence and clear exposition** → 6–7
- **If yes, with genuinely new insight that surprises experts** → 8
- **If yes, but evidence is incomplete or presentation is confusing** → 5
- **If the answer is unclear or "not really"** → 3–4
- **If the paper has fundamental flaws** → 1–2

**When in doubt about novelty in a crowded subfield (e.g., prompt tuning)**:
Ask whether the authors have identified a new *problem* (not just a new solution to an already-solved problem). "CoOp causes miscalibration between base and novel classes" is a new problem. "Our new regularization term improves CoOp by 0.7%" is not.

**When in doubt about benchmark papers**:
Ask for the "surprising finding test." Does the benchmark reveal something about VLMs that we couldn't have known before? If the finding is "GPT-4V is better than open-source models" — that's not surprising and doesn't justify a new benchmark.

**The borderline (4–5) judgment in VL**:
The key question is: *if this paper didn't exist, would the field miss something important?* For methods: would practitioners be missing a useful tool? For benchmarks: would researchers be missing an important evaluation? For analysis: would there be a gap in our understanding? Papers where the answer is "no" should be rejected at 4; papers where the answer is "probably yes, though the execution could be stronger" should be borderline-accepted at 5.

**Be especially suspicious of**:
- Benchmark papers that don't provide a table comparing with existing benchmarks
- Method papers that claim improvements on all tasks but show them on only 3–4 datasets
- Analysis papers that explain one phenomenon but attribute it to a new cause without ruling out existing explanations
- Continual learning papers that don't compare against CoIN or existing CL methods applied to VLMs
- Prompt tuning papers that don't report harmonic mean of base+novel accuracy
- "First work to apply X to VLMs" without explaining why X wasn't applied before and what the non-trivial challenges were
