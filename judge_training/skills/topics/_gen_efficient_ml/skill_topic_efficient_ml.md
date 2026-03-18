# Skill File: Evaluating Research in Efficient ML

**For use by AI judge agents evaluating submissions in the "efficient_ml" topic area.**

---

## 1. Topic Overview

### What This Area Covers

"Efficient ML" at ICLR/NeurIPS/ICML encompasses any work whose primary contribution is making machine learning models faster, smaller, cheaper to train, cheaper to run, or more data-efficient. The sub-areas include:

1. **Parameter-efficient fine-tuning (PEFT)**: LoRA and variants (DoRA, QLoRA, HiRA, MoRA, ReLoRA), prefix-tuning, prompt-tuning, adapter methods, frequency-domain adaptation (FourierFT, LoCA), BitFit, (IA)³.
2. **Model compression**:
   - *Pruning*: Structured (layer/head/channel) and unstructured (weight magnitude), semi-structured (2:4), gradient-free (SparseGPT, Wanda), layer/block removal (SLEB).
   - *Quantization*: Post-training quantization (PTQ), quantization-aware training (QAT), mixed-precision, LLM quantization (GPTQ, AWQ, LLM.int8, KIVI).
   - *Knowledge distillation*: Response-based, feature-based, relation-based, self-distillation, data-free distillation.
   - *Matrix decomposition/low-rank approximation*: SVD, Nyström, CR decomposition for weight compression (SliceGPT, MoDeGPT).
3. **Efficient inference**:
   - *KV cache compression*: Token eviction (H2O, Scissorhands, SnapKV, StreamingLLM), quantized KV (KIVI, KVQuant), cross-layer sharing.
   - *Speculative decoding*: Draft models, token trees, self-speculative decoding.
   - *Attention approximation*: Linear attention, sparse attention (BigBird, Longformer), LSH-based attention (Reformer, Hyperattention).
   - *Efficient batch processing*: Continuous batching, PagedAttention, FlashAttention.
4. **Efficient architectures**:
   - *Mixture of Experts (MoE)*: Expert routing, load balancing, zero-computation experts, heterogeneous experts.
   - *Linear/subquadratic attention*: Mamba/SSMs, RWKV, RetNet, GLA.
   - *Efficient vision*: Efficient ViTs, token pruning, patch merging.
5. **Efficient training**:
   - *Data efficiency*: Active learning, curriculum learning, coreset selection, efficient pretraining data curation.
   - *Memory efficiency*: Gradient checkpointing, offloading, mixed-precision training, ZeRO.
   - *Efficient optimization*: Gradient compression, local SGD, second-order methods for large models.
6. **Neural Architecture Search (NAS)**: One-shot NAS, predictor-based NAS, hardware-aware NAS.
7. **Efficient generation**: Accelerating diffusion models (fewer NFEs, consistency models, Flow Matching, distillation), efficient autoregressive generation, efficient VAEs/autoencoders.
8. **LLM system efficiency**: Cascade inference, routing between models of different sizes, speculative RAG, efficient agent frameworks.

### Key Challenges

- Efficiency vs. quality: Most compression techniques degrade accuracy — the bar is maintaining quality at higher compression ratios than prior art.
- Generalization across scales: Methods that work on 1B models need to be validated on 7B+ to be convincing.
- Fair comparison: Different methods use different hardware, batch sizes, calibration datasets, and wall-clock measurement protocols.
- Reproducibility: Implementation details (calibration set, hyperparameters) can significantly affect results.
- Theoretical grounding: Many methods are empirically motivated but lack theoretical justification.

### Score Distribution and Acceptance Bar (from 3,854 papers)

- **Mean rating**: 4.8 | **Median**: 4.75 | **Std**: 1.24
- **Acceptance rate**: 78.3%
- **Tier breakdown**:
  - Excellent (8–10): 80 papers (~2%) — outsize impact, genuinely new paradigms
  - Good (6–7): 3,306 papers (~86%) — solid, publishable contributions
  - Borderline (4–5): 7,620 "slot-years" — split decisions, often rejected from top venues
  - Low (1–3): 2,849 papers (~74% rejected) — fundamental issues

**Practical calibration**: A 5/10 in efficient_ml means reviewers see merit but the contribution is too incremental, baselines are missing, or efficiency gains are not measured properly. A 6/10 is a poster accept at top venues — a real technical contribution with solid (but not comprehensive) experiments. A 7/10 requires a novel mechanism with strong results, comprehensive baselines, and efficiency analysis. Scores of 8+ are reserved for work that opens new directions: a new efficiency paradigm (MoE with zero-computation experts), a breakthrough compression method (MoDeGPT with theoretical guarantees), or a system that genuinely changes what's deployable.

---

## 2. What Reviewers Praise (with Real Examples)

### 2.1 Novelty of Core Idea

"Novel" is the most common strength phrase (2,569x). Reviewers distinguish between:
- **Conceptual novelty**: A new mechanism (e.g., "zero-computation experts" in MoE++ that let the router skip FFN computation entirely for simple tokens).
- **Technical novelty**: A new decomposition scheme, a new approximation, or a new theoretical insight.
- **Empirical novelty**: First to show something works at scale or in a new domain.

**Real example — MoE++ (8.0, Oral)**:
> "This work improves the existing MoE framework in terms of both efficiency (throughput) and effectiveness (performance), making it impactful for real-world applications. This paper is well-written and insightful, with clear motivation and illustrations."

**Real example — HiRA (8.0, Oral)**:
> "The paper introduces a creative way of using the Hadamard product to achieve high-rank adaptation within PEFT. This approach is an important contribution to address the common expressiveness limitation of LoRA-like PEFT methods."

**Real example — MoDeGPT (8.0, Oral)**:
> "The authors introduce Nystrom approximation, CR decomposition, and SVD to pruning row-column pairs in LLMs. To the best of my knowledge, this is the first work to use Nystrom approximation and CR decomposition to prune LLMs. The authors carefully use them to prune different types of modules."

**What earns praise**: The key novelty signal is proposing a mechanism that is *specifically motivated* by the problem structure. Reviewers are skeptical of novelty claims when the method is an obvious extension or combination of existing techniques without a new insight.

### 2.2 Strong Baselines and Comprehensive Comparisons

"Baseline" is both the most common weakness phrase (5,694x) AND a common strength phrase (1,773x). **This is the #1 factor separating accepted from rejected papers in efficient_ml.**

Reviewers praise papers that:
- Compare against all recent SOTA in the sub-area (not just 2-year-old baselines)
- Make fair comparisons (same parameter count, same FLOPs budget, same calibration data for PTQ)
- Report results on multiple architectures/sizes (not just one model)
- Include results at multiple compression ratios/budgets

**Real example — MoDeGPT (8.0, Oral)**:
> "The authors conduct exhaustive experiments to show the superiority of MoDeGPT. Their experiments not only covers accuracies, but also inference speed and pruning cost."

**Real example — HiRA (8.0, Oral)**:
> "The authors show HiRA's consistent improvements over LoRA and other baselines which demonstrate that HiRA not only theoretically sounds but also practically effective. The ablation studies, such as singular value distribution analysis, show how HiRA's parameter dynamics behaves somewhat similarly to those of full fine-tuning."

### 2.3 Comprehensive Ablation Studies

"Ablation" appears in 1,649 strength mentions. Reviewers want to understand *why* each component works.

Reviewers praise papers with:
- Component-by-component ablations showing each design choice matters
- Sensitivity analysis to hyperparameters
- Analysis of failure modes or edge cases

**Real example — SPA (8.67, Oral)**:
> "The authors show SPA extends beyond Mistral to other popular LLMs like Phi and Llama (Table 5) and is robust, in the win rate variance sense, to the seed of the initial preference data (Table 4)."

**Real example — SANA (8.5, Oral)**:
> "The ablation experiments of different design components are sufficient and convincing."

**Real example — MoE++ (8.0, Oral)**:
> "The paper is written clearly and a thorough set of ablations are performed."

### 2.4 Actual Efficiency Measurements

This is *especially critical in efficient_ml*: reviewers expect wall-clock time, throughput (tokens/sec), latency (ms/token), memory footprint, and/or FLOPs — not just compression ratio or parameter count.

**Real example — MoDeGPT (8.0, Oral)**:
> "The authors analyze the effect of MoDeGPT in a detailed way. Their experiments not only covers accuracies, but also inference speed and pruning cost... achieves a 46% increase in inference throughput."

**Real example — SANA (8.5, Oral)**:
> "Efficiency is a really big selling point... SANA can generate high-quality images even on a laptop is very impressive."

**Failure pattern**: Papers that only report parameter counts or FLOPs but not actual speedup on hardware are consistently penalized. As one reviewer noted for LSH-E (3.8, Reject): "Evaluation does not include end-to-end speedup numbers, making it more difficult to see the ultimate impact of the contribution."

### 2.5 Theoretical Grounding

"Solid theoretical" (88x) is a top strength phrase. In efficient_ml, theory serves two roles:
- *Error bounds*: Showing the approximation error introduced by compression is bounded.
- *Rank/expressivity analysis*: Showing the proposed method can represent a richer class of functions than alternatives.

**Real example — MoDeGPT (8.0, Oral)**:
> "The paper offers a comprehensive literature review and theoretical analysis, demonstrates significant performance improvements through experimental results, and provides error guarantees along with a theoretical framework."

**Real example — HiRA (8.0, Oral)**:
> "The paper offers a theoretical basis for the proposed method, and provides experimental results and ablation studies to demonstrate the effectiveness of the method."

### 2.6 Reproducibility and Practical Utility

"Reproducible" (357x) is a common strength phrase. Reviewers value:
- Code release (ideally before/at acceptance)
- Clear hyperparameter reporting
- Low implementation overhead (few lines of change to existing codebases)

**Real example — SPA (8.67, Oral)**:
> "Reproducibility: the authors provide implementation details and hyperparameters in Section 5. The authors will open-source the code and models after acceptance... because the modification to the DPO objective is minimal, the authors mention only a few lines of change to the DPO codebase, which is another advantage for practical utility of SPA."

### 2.7 Scalability

"Scalable" (373x) is a top strength phrase. In efficient_ml, this means:
- Results hold across multiple model sizes
- The efficiency gains persist at scale
- The method does not have cubic or worse hidden costs

**Real example — SANA (8.5, Oral)**:
> "Figures and tables are clear and easy to read... The model achieves competitive results compared to much larger models like Flux-12B, boasting significantly lower computational requirements."

---

## 3. What Reviewers Criticize (with Real Examples)

### 3.1 Limited Novelty / Incremental Contribution

"Novelty" is the #1 weakness phrase (2,414x) and "incremental" appears 671 times. This is the death knell for efficient_ml papers.

Common patterns:
- **"Just combining existing techniques"**: A paper that combines three existing methods (linear attention + higher compression AE + LLM text encoder) without a new insight into *why* this combination is better.
- **"Rebranding"**: Calling Chain-of-Thought a "plan" and proposing a "planning framework" for LLM efficiency.
- **"Obvious extension"**: Adding one type of expert to an existing MoE framework without showing *why* that type is better.

**Real example — COPE (2.8, Reject)**:
> "The proposed method is largely engineering-oriented, with the three-stage design appearing intuitive and lacking algorithmic or learning-based innovation."

**Real example — COPE (2.8, Reject)**:
> "Some of the papers claims are overstated and rebranding of existing well-known approaches. For example, the use of 'planning' in the paper is just as similar to the known 'CoT (chain-of-thoughts)' and cannot be considered as the contribution of the paper."

**Real example — SANA (8.5, despite being accepted)**:
> "Although the results are impressive, the contribution of this paper on the technical side is somewhat limited. Their three main components have been already explored in the literature." [Note: SANA still got 8.5 because the combination produced *dramatically* better results.]

**Lesson**: Combining existing techniques *can* be acceptable if the empirical gains are substantial and the engineering insights are non-trivial. But the bar is very high — reviewers must see that the combination produces something qualitatively new.

### 3.2 Missing Key Baselines

"Baseline" is the most common weakness phrase (5,694x). The specific pattern:
- Comparing against an L2-norm baseline but not H2O, SnapKV, StreamingLLM, or Quest (for KV cache papers).
- Comparing against LoRA but not DoRA, VeRA, FourierFT, or MoRA (for PEFT papers).
- Comparing against older pruning methods but not SparseGPT, Wanda, or SLEB (for pruning papers).

**Real example — LSH-E (3.8, Reject)**:
> "Missing baselines — only baseline used is L2 norm. Limited evaluation: can we get more results on longbenchmark at different budgets with standard baselines." [Multiple reviewers flagged this.]

**Real example — LSH-E (3.8, Reject)**:
> "The experimental setup lacks comprehensiveness; comparisons with alternative methods like H2O, SubGen, and other established baselines should be included to provide a more robust evaluation."

**Real example — MoDeGPT (8.0, despite being accepted)**:
> "There are lack of competitors. The authors should compare their results with state-of-the-art pruning algorithms, especially layer (or block) pruning algorithms, such as SLEB. Layer pruning algorithms provide significant inference speedup and should be included in Figure 3."

### 3.3 Missing Wall-Clock Time / Latency Measurements

In efficient_ml, claiming efficiency without measuring it is a near-fatal flaw.

**Real example — LSH-E (3.8, Reject)**:
> "Why is there no timing experiment, since that will be one key benefit of caching." / "Runtime metrics should be reported to assess the efficiency of token generation and to substantiate the computational benefits claimed."

**Real example — MoE++ (8.0, despite being accepted)**:
> "While Table 1 shows the 'complexity between the proposed MoE++ and MoE' and zero-computation experts enjoy a complexity of 0, they still likely lead to some extra computation overhead. Therefore, this work lacks real-world wall-clock time demonstrations of these zero-computation expert operators, especially regarding a batch of tokens."

**Real example — LoCA (5.8, Poster)**:
> "Common advantages of the PEFT method include reduced computation and memory costs. The paper's contribution would be strengthened if the authors included these aspects in their analysis."

**Pattern**: Even accepted papers are flagged for this. In efficient_ml, efficiency claims *must* be backed by wall-clock time, throughput (tokens/sec, images/sec), or latency measurements on real hardware. FLOPs alone are insufficient.

### 3.4 Insufficient Evaluation Scope

"Limited to" (587x) and "unclear whether" (557x) capture this weakness.

Common patterns:
- Evaluating only on one model size (e.g., only 7B, not 70B)
- Evaluating on only a handful of benchmarks
- Evaluating at only one compression ratio/budget
- Not testing on long-context benchmarks when claiming long-context efficiency

**Real example — LSH-E (3.8, Reject)**:
> "The datasets used in the experiments are not sufficiently large for evaluating performance in long-context scenarios. Given that these methods target long-sequence processing, experiments should ideally use token sizes over 50,000. LongBench or other large-scale datasets would be more appropriate."

**Real example — MoDeGPT (8.0, despite acceptance)**:
> "There are lack of experiments regarding large models, e.g., Llama 3 70B."

**Real example — MoE++ (8.0, accepted)**:
> "The empirical gains don't seem to be too significant and can only start to be seen at large scale ~7B parameters."

### 3.5 Overclaiming / Misleading Comparisons

"Fair comparison" (334x) and "unclear why" (205x) capture this.

Patterns:
- Claiming a method is "efficient" when its preprocessing/calibration cost is large.
- Comparing to baselines at different sparsity levels (e.g., comparing 40% compression to a baseline's 50%).
- Using efficiency metrics that ignore the actual bottleneck.

**Real example — MoDeGPT (8.0, accepted)**:
> "MoDeGPT requires expensive pruning costs more than 8 hours for pruning Llama-2 13B models. According to SELB, most of pruning algorithms requires less than 16 minutes for pruning Llama-2 13B models. Therefore, it is an overclaiming to insist that MoDeGPT is an efficient algorithm."

**Real example — MoDeGPT (8.0, accepted)**:
> "Why does Table 3 include only 50% compression results for models like SparseGPT but lack results for 40% compression? Why is a 40% compression result of MoDeGPT compared to a 50% compression result of SparseGPT?" [Comparison at different budgets is unfair.]

### 3.6 Lack of Justification for Design Choices

"Unclear why" (205x) and "unclear how" (525x).

**Real example — MoDeGPT (8.0, accepted)**:
> "The authors suggest using three different types of matrix decompositions for three different types of computations within Transformers, but they do not provide motivation for this choice. For example, why is CR decomposition more suitable for Type-2 computation?"

**Real example — MoE++ (8.0, accepted)**:
> "This work introduces three types of zero-computation experts (i.e. zero, copy, and constant) but provides minimal justification for this specific set. From Table 5, we can see they only conducted basic combinatorial ablations."

**Lesson**: Reviewers want to understand *why* a design choice is made, not just that it empirically works. Missing theoretical motivation or ablation-based justification is consistently flagged even in accepted papers.

### 3.7 Engineering Without Scientific Contribution

Papers that propose a pipeline/framework without a new algorithm or insight consistently get low scores.

**Real example — COPE (2.8, Reject)**:
> "Novelty is arguably modest. COPE looks like a heuristic cascade or router with task-specific confidence checks... Mixture-of-Experts or learned routing can address the same goal in a more principled way. The paper does not compare to MoE or to strong learned routers, so the contribution reads (arguably) incremental."

**Real example — COPE (2.8, Reject)**:
> "The proposed method is largely engineering-oriented, with the three-stage design appearing intuitive and lacking algorithmic or learning-based innovation."

### 3.8 Missing Prior Work Citations

"Lacks a" (507x) and "lack of" (1,703x) often refer to missing citations.

**Real example — LSH-E (3.8, Reject)**:
> "The term 'novel' should not be used for LSH in this context, as it is not a new approach and has appeared in prior work. Specifically, the methods used in KDEformer, Hyperattention, QJL, and SubGen demonstrate significant overlap, yet these works are not cited here."

**Pattern**: In efficient_ml specifically, the literature moves fast. A paper submitted in 2025 must cite and compare to papers from 2024. Missing KV cache papers (H2O, SnapKV, Quest), missing PEFT papers (DoRA, VeRA), or missing compression papers (SparseGPT, SLEB) is a significant red flag.

---

## 4. Required Baselines and Metrics

### 4.1 By Sub-Area

**PEFT / Fine-tuning**:
- *Must compare*: LoRA, DoRA, VeRA (vector-based random matrix adaptation), QLoRA, full fine-tuning (as upper bound)
- *Should also consider*: MoRA, ReLoRA, FourierFT (if frequency-domain), AdaLoRA (if rank-adaptive)
- *Key metrics*: Accuracy on downstream benchmarks (GLUE/SuperGLUE for NLU, MT-Bench/AlpacaEval for instruction tuning, commonsense reasoning for general LLMs), number of trainable parameters, memory footprint during training, training time

**Model Compression — Pruning**:
- *Must compare*: SparseGPT, Wanda (for unstructured/semi-structured), SliceGPT (for structured), SLEB (for layer pruning)
- *Key metrics*: Perplexity on WikiText-2/C4, zero-shot accuracy on common sense benchmarks (WinoGrande, HellaSwag, ARC, PIQA), throughput (tokens/sec), memory (GB), sparsity ratio at matched accuracy

**Model Compression — Quantization**:
- *Must compare*: GPTQ, AWQ, LLM.int8 (for PTQ); QAT methods if applicable
- *Key metrics*: Perplexity, zero-shot accuracy, bits-per-weight (BPW), throughput, latency

**Model Compression — Knowledge Distillation**:
- *Must compare*: Vanilla KD (Hinton et al.), recent task-specific and LLM-distillation methods relevant to the domain
- *Key metrics*: Accuracy on target task, training cost (GPU hours), student model size vs. teacher

**KV Cache Compression**:
- *Must compare*: H2O, Scissorhands, StreamingLLM, SnapKV (for token eviction); KIVI, KVQuant (for quantization); Quest (for query-aware methods)
- *Key metrics*: Perplexity, long-context benchmarks (LongBench, Needle-in-a-Haystack, passkey retrieval), throughput at various cache budgets, memory usage, latency (including first-token latency)
- *Critical*: Must test at meaningful cache sizes (50K+ tokens for long-context claims)

**Efficient Attention / Linear Attention**:
- *Must compare*: FlashAttention, relevant SSM/RWKV/Mamba variants
- *Key metrics*: Throughput (tokens/sec at various sequence lengths), memory consumption, quality vs. standard attention

**MoE Efficiency**:
- *Must compare*: Vanilla MoE (Switch Transformer, GLaM), recent MoE variants
- *Key metrics*: Throughput, FLOP/parameter ratio, load balance, downstream quality at matched parameter count

**Efficient Diffusion / Generative**:
- *Must compare*: State-of-the-art models (SD3, SDXL, FLUX for image; relevant video generation models)
- *Key metrics*: FID, CLIP score, ImageReward/HPS, throughput (images/sec), latency (sec/image), NFEs (number of function evaluations)

### 4.2 Universal Metrics Expected Across All Sub-Areas

1. **Wall-clock time or throughput** — not just FLOPs. Report on which GPU and what batch size.
2. **Memory footprint** — GPU memory in GB, measured empirically.
3. **Quality at multiple compression ratios** — not just one cherry-picked ratio.
4. **Multiple model sizes** — at minimum two; ideally covering a small and a large model.
5. **Multiple evaluation datasets** — at minimum two per capability being tested.

### 4.3 Benchmarks Frequently Expected

| Sub-area | Benchmarks |
|----------|------------|
| LLM general quality | WikiText-2 perplexity, MMLU, HellaSwag, WinoGrande, ARC, PIQA |
| LLM instruction following | MT-Bench, AlpacaEval 2.0 (length-controlled win rate) |
| Long-context LLM | LongBench, RULER, Needle-in-a-Haystack, passkey retrieval |
| NLU fine-tuning | GLUE/SuperGLUE (RTE, MRPC, CoLA, SST-2, MNLI, QNLI, QQP) |
| Commonsense reasoning | BoolQ, WinoGrande, HellaSwag, ARC-e, ARC-c, PIQA, SIQA, OpenbookQA |
| Code generation | HumanEval, MBPP, CodeBench |
| Math reasoning | MATH-500, GSM8K, MathInstruct |
| Image generation | FID (COCO/MS-COCO), CLIP score, DINO score, HPS, ImageReward |
| Vision + PEFT | VTAB, FGVC, Stanford Cars, ViT-B/L backbones |

---

## 5. Common Technical Pitfalls

### 5.1 Conflating Parameter Count with Efficiency

A method with fewer parameters is not necessarily more efficient at inference. Reviewers consistently flag when:
- A "parameter-efficient" method adds overhead that slows down inference (e.g., LoCA's alternating optimization).
- A method reduces parameters but requires custom CUDA kernels to see actual speedup.
- A method reduces one bottleneck (weights) without addressing the actual bottleneck (activations, memory bandwidth).

**Real example — LoCA (5.8, accepted)**:
> "LoCA introduces individual optimization of frequency component locations and coefficients for each layer. This approach appears to introduce a higher number of parameters compared to FourierFT... For example, with LLaMA-2 7B where L=32, LoCA's parameter count is approximately 2.82 times that of FourierFT."

### 5.2 Overconfident Novelty Claims for LSH/Attention Tricks

LSH, attention approximation, and locality-sensitive hashing have a long history. Papers that claim novelty for applying standard LSH to a new setting must carefully distinguish from: Reformer, Hyperattention, KDEformer, QJL, SubGen.

**Real example — LSH-E (3.8, Reject)**:
> "'novel' should not be used for LSH in this context... methods used in KDEformer, Hyperattention, QJL, and SubGen demonstrate significant overlap, yet these works are not cited."

### 5.3 Theory/Practice Gap in PEFT

For frequency-domain and other non-standard PEFT methods, reviewers watch for:
- Theoretical claims (e.g., "higher expressivity") that don't translate to consistent empirical gains.
- Assumptions (e.g., i.i.d. updates for CLT) that don't hold in practice.
- Claims that a prior method "performs worse" without empirical evidence.

**Real example — LoCA (5.8, accepted)**:
> "A central claim of the paper is that randomly selected frequencies for FourierFT yield lower expressivity than LoRA; however, this claim lacks direct experimental validation... Figure 4 in the FourierFT paper presents contrasting findings, particularly on the QQP task in GLUE. In Gao et al., FourierFT consistently outperforms LoRA."

### 5.4 Greedy Eviction Without Theoretical Justification

For KV cache and sparse attention methods, reviewers ask: why is discarding token X at step t safe for future steps? Methods that use current query to predict future relevance need to justify this assumption empirically (showing correlation across timesteps) or theoretically.

**Real example — LSH-E (3.8, Reject)**:
> "The greedy eviction algorithm assumes that the attention score between a particular key vector and the current query vector is representative of the attention score with subsequent query vectors. While there is ample empirical exploration on the correlation... I could not find provable theoretical guarantees... This is in contrast to other greedy approaches such as H2O that uses accumulated attention to be more robust."

### 5.5 MoE Load Imbalance

MoE efficiency papers must address load imbalance. Heterogeneous MoE methods in particular must show that expert utilization is balanced across the new expert types.

**Real example — MoE++ (8.0, accepted)**:
> "The dynamic routing mechanism can still result in load imbalances, especially under diverse data distributions, which may lead to underutilized or overloaded experts that affect efficiency."

### 5.6 Hyperparameter Sensitivity

Methods that introduce new hyperparameters (thresholds, ratios, temperatures) must show robustness to them.

**Real example — MoE++ (8.0, accepted)**:
> "Parameters such as τ, which regulate token allocation between zero-computation experts and original, may complicate model tuning, as the performance and burden distribution are sensitive to them."

### 5.7 Hardware-Dependent Claims

Efficiency gains measured on one GPU (e.g., A100) may not transfer to another (e.g., consumer GPUs). Reviewers increasingly expect results on relevant deployment hardware.

**Real example — LSH-E (3.8, Reject)**:
> "Given that LSH-E's efficiency largely depends on its CUDA implementation, can you elaborate on any specific optimizations made within the CUDA code?" [Reviewer implied the efficiency claim was conditional on CUDA-specific tricks not documented in the paper.]

### 5.8 Calibration Data Sensitivity

For PTQ and pruning methods, results can vary greatly depending on the calibration dataset. Papers must report calibration details and ideally ablate over calibration set size.

**Real example — MoDeGPT (8.0, accepted)**:
> "Overfitting of the model to calibration data prevents the compression method from generalizing across most tasks."

---

## 6. Scoring Rubric for This Topic

### Score 2–3/10: Fundamental Problems

**Characteristics**:
- Core contribution is not novel — it recombines or renames existing work without new insights.
- Missing standard baselines for the sub-area (e.g., no H2O/SnapKV comparison for KV cache paper).
- Efficiency claims not backed by any timing/throughput measurements.
- Writing is confusing or contradictory.
- Evaluation is shallow (1–2 benchmarks, 1 model size).

**Real example — LSH-E (rating 3.8, Reject)**:
The paper applies LSH (a decades-old technique) to KV cache eviction. Four reviewers cited: (a) missing citations to Hyperattention, KDEformer, QJL, SubGen — all using the same technique; (b) only comparison to L2-norm baseline, not H2O/SnapKV; (c) no timing experiments; (d) evaluation limited to short sequences for a long-context method.

**Real example — COPE (rating 2.8, Reject)**:
The paper proposes a "plan-then-execute" cascade between small and large LLMs. Three of five reviewers gave 2/10. Problems: (a) "planning" is essentially Chain-of-Thought rebranding; (b) engineering framework without algorithmic innovation; (c) overconfident cost-savings claims that don't account for planning token overhead; (d) inconsistent confidence measures across task types; (e) missing comparison to learned routers and MoE systems.

### Score 4–5/10: Borderline (Acceptance Threshold)

**Characteristics**:
- Real technical contribution but limited novelty or marginal improvement over strong baselines.
- Correct evaluation but missing 1–2 important baselines or efficiency metrics.
- Theory doesn't always agree with practice.
- Works on some tasks/models but unclear generalization.

**Real example — LoCA (rating 5.83, Accept Poster)**:
LoCA proposes frequency-domain PEFT using iDCT with learned frequency locations. It has a genuine theoretical contribution (expressivity analysis) and beats FourierFT on many tasks. However: (a) improvements over LoRA are marginal and inconsistent; (b) extra parameter overhead vs. FourierFT is 2.82× for LLaMA-2 7B; (c) theory assumes i.i.d. gradient updates (questionable); (d) missing VeRA comparison; (e) no memory/compute overhead analysis. Accepted as a poster because the approach is genuinely novel and theoretically motivated, even if the gains are modest.

**What would push a 5 to a 6**: Comprehensive efficiency measurements (training time, memory), broader baselines (VeRA, DoRA), more model sizes, and ablations reconciling theory-practice gaps.

### Score 6–7/10: Solid Accept

**Characteristics**:
- Clear technical novelty — a new mechanism with a principled motivation.
- Strong empirical results across multiple baselines and multiple model sizes.
- Includes efficiency measurements (wall-clock time or throughput).
- Good ablation studies justifying design choices.
- A few lingering questions (e.g., missing one baseline, no 70B experiments), but not fatal.

**Pattern**: Most accepted posters and spotlights fall here. The distinguishing factor is that the paper clearly advances the state of the art in a specific sub-area and reviewers agree the contribution is real. Scores of 6 often mean "I have a concern but I'm convinced the contribution is solid." Scores of 7 mean "this is a strong paper with minor gaps."

**Example sub-patterns**:
- A new PEFT method that consistently outperforms LoRA + DoRA + VeRA across GLUE, instruction tuning, and vision tasks.
- A new pruning method with 2× better perplexity than SparseGPT at same sparsity, with wall-clock speedup measurements.
- A new KV cache method with 50% compression at <1% accuracy drop on LongBench vs. H2O, SnapKV, with latency numbers.

### Score 8–10/10: Exceptional

**Characteristics**:
- Opens a new direction or paradigm in efficient ML.
- Results significantly outperform prior SOTA across many settings.
- Deep theoretical understanding of why the method works.
- Comprehensive evaluation leaves few open questions.
- Often includes analysis that teaches something new about the problem itself.

**Real example — SPA (rating 8.67, Accept Oral)**:
Uses DPO's implicit reward model to generate preference labels without a reward model, with a self-refinement mechanism to reduce noise. Achieves strong AlpacaEval 2.0 and MT-Bench results using only 3.3% of training data. Praised for: (a) simple yet principled idea; (b) multiple LLM backbone generalization; (c) reproducibility; (d) comprehensive baseline comparisons across iterative DPO, LLM-as-judge, and RLHF categories.

**Real example — SANA (rating 8.5, Accept Oral)**:
A complete efficient T2I framework with 4 innovations (32× compression AE, linear DiT, LLM text encoder, Flow-DPM-Solver). Generates 4K images on a laptop GPU at 100× speedup vs. FLUX-12B. While individual components existed, the *combination* produces unprecedented efficiency with competitive quality — which is why it scored 8.5 despite limited individual component novelty.

**Real example — MoDeGPT (rating 8.0, Accept Oral)**:
Modular decomposition applying Nyström, CR, and SVD to different Transformer module types, with a global sparsity allocation using entropic regularization, achieving 46% throughput improvement with error guarantees. Note: even this paper received criticism for 8-hour pruning time and missing layer-pruning baselines — but the core contribution of systematically applying different decompositions to different module types was seen as a genuine insight.

---

## 7. Key Papers and Expected Citations

When reviewing efficient_ml papers, expect the following to be cited. Missing these is a red flag.

### 7.1 PEFT / Fine-tuning

| Method | Key claim | When missing is suspicious |
|--------|-----------|---------------------------|
| LoRA (Hu et al., 2021) | Low-rank adaptation | Any PEFT paper |
| QLoRA (Dettmers et al., 2023) | 4-bit quantized LoRA | Parameter-efficient LLM fine-tuning |
| DoRA (Liu et al., 2024) | Weight decomposition for LoRA | LoRA variants |
| VeRA (Kopiczko et al., 2023) | Vector-based random matrix adaptation | Highly parameter-efficient PEFT |
| AdaLoRA (Zhang et al., 2023) | Adaptive rank allocation | Rank-adaptive PEFT |
| FourierFT (Gao et al., 2024) | Frequency-domain PEFT | Frequency/spectral PEFT methods |
| MoRA (Jiang et al., 2024) | High-rank adaptation | High-rank PEFT methods |

### 7.2 Pruning / Compression

| Method | Key claim | When missing is suspicious |
|--------|-----------|---------------------------|
| SparseGPT (Frantar & Alistarh, 2023) | Gradient-free unstructured pruning for LLMs | Any LLM pruning paper |
| Wanda (Sun et al., 2023) | Weight × activation magnitude pruning | LLM pruning |
| SliceGPT (Ashkboos et al., 2024) | Structured pruning via orthogonal transforms | Structured LLM pruning |
| SLEB (Song et al., 2024) | Layer/block removal for LLMs | Block-level pruning |
| OWL (Yin et al., 2023) | Outlier-weighted layerwise sparsity | Sparsity allocation strategies |

### 7.3 KV Cache

| Method | Key claim | When missing is suspicious |
|--------|-----------|---------------------------|
| H2O (Zhang et al., 2023) | Heavy-hitter oracle for KV eviction | KV cache eviction methods |
| Scissorhands (Liu et al., 2023) | Persistence of importance for KV | KV cache eviction |
| StreamingLLM (Xiao et al., 2023) | Attention sink + sliding window | Long-context KV compression |
| SnapKV (Li et al., 2024) | Snapshot-based KV compression | KV cache for long context |
| Quest (Tang et al., 2024) | Query-aware sparse KV cache | Query-aware KV methods |
| KIVI (Liu et al., 2024) | KV cache quantization | KV quantization |
| Hyperattention (Han et al., 2023) | LSH-based approximate attention | Attention approximation methods |

### 7.4 Efficient Architectures

| Method | Key claim | When missing is suspicious |
|--------|-----------|---------------------------|
| FlashAttention (Dao et al., 2022/2023) | IO-aware exact attention | Any attention efficiency paper |
| Mamba (Gu & Dao, 2023) | Selective SSM as attention alternative | Subquadratic sequence models |
| Mixtral (Mistral AI, 2024) | Sparse MoE for LLMs | MoE papers |
| Switch Transformer (Fedus et al., 2022) | Simplified MoE routing | MoE papers |

### 7.5 Efficient Generation / Diffusion

| Method | Key claim | When missing is suspicious |
|--------|-----------|---------------------------|
| DDIM (Song et al., 2020) | Non-Markovian diffusion sampling | Diffusion acceleration |
| DPM-Solver (Lu et al., 2022) | Fast ODE solver for diffusion | Fast diffusion sampling |
| Consistency Models (Song et al., 2023) | One-step generation | Diffusion distillation |
| PixArt-α/Σ (Chen et al., 2023/2024) | Efficient DiT for T2I | Efficient T2I |
| FLUX (Black Forest Labs, 2024) | Rectified flow transformer | SOTA T2I baseline |

### 7.6 Quantization

| Method | Key claim | When missing is suspicious |
|--------|-----------|---------------------------|
| GPTQ (Frantar et al., 2022) | Post-training quantization for LLMs | LLM quantization |
| AWQ (Lin et al., 2023) | Activation-aware weight quantization | LLM quantization |
| LLM.int8 (Dettmers et al., 2022) | 8-bit inference for LLMs | INT8 quantization |
| SmoothQuant (Xiao et al., 2023) | Quantization-friendly weight migration | Quantization |

---

## 8. Calibration Notes for the Judge

### 8.1 High Acceptance Rate Does Not Mean Low Bar

The 78.3% acceptance rate reflects that this pool includes papers from multiple venues and years, not that the acceptance threshold is low. Within any single venue (ICLR/NeurIPS), the bar for efficient_ml papers is high because:
- The field moves fast — SOTA changes every few months.
- Reviewer expectations for efficiency metrics are stringent.
- "Incremental" is the death knell; reviewers want to see meaningful empirical improvements.

### 8.2 Efficiency Metrics Are Mandatory

A paper in efficient_ml that doesn't measure actual efficiency (wall-clock time, throughput, memory) is missing its core claim. Treat missing efficiency measurements as a significant red flag equivalent to missing baselines.

### 8.3 Sub-Area Knowledge Matters

The expected baselines differ completely between sub-areas. A paper about KV cache compression is judged against H2O, SnapKV, StreamingLLM — not against LoRA. Apply sub-area-specific baseline expectations from Section 4.

### 8.4 Strong Results Can Overcome Limited Novelty

SANA (8.5) and MoDeGPT (8.0) both combined existing techniques but achieved exceptional results. If a paper's empirical results are substantially and clearly better than all baselines across many settings, this can compensate for modest individual component novelty. The key word is "substantially" — a 1–2% improvement rarely justifies a paper; a 10× speedup at matched quality does.

### 8.5 Theory Is a Bonus, Not a Requirement

Unlike theoretical_ml, most efficient_ml papers are empirical. A paper without a theoretical contribution can score 8+ if its empirical results are exceptional. However, theoretical grounding (error bounds, expressivity analysis) is highly praised when it explains *why* the method works, and it raises the paper's credibility when claims are contested.

### 8.6 Reviewer Common Questions to Emulate

The following questions appear repeatedly in high-quality reviews of efficient_ml papers. Use them as a checklist:

1. What are the wall-clock speedup numbers on real hardware?
2. How does this compare to [specific SOTA method from past 12 months]?
3. Does this work at 7B+ scale, not just 1–3B?
4. What is the calibration data size and sensitivity?
5. What happens at different compression ratios/parameter budgets?
6. Is the improvement consistent across architectures (not just LLaMA)?
7. What is the ablation showing each design choice matters?
8. Why is [specific design choice] better than the obvious alternative?
9. Does the code reproduce the results?
10. Are the efficiency metrics measured fairly (same batch size, same hardware)?
