# Skill File: Evaluating Research in Optimization

**For use by AI judge agents evaluating submissions in the "optimization" topic area.**

---

## 1. Topic Overview

### What This Area Covers

"Optimization" as a topic at ICLR/NeurIPS/ICML is broad. It spans:

1. **First/second-order methods**: SGD variants, Adam, momentum, adaptive gradient methods (AdaGrad, RMSProp, AdamW, Lion), second-order/Newton-type methods, extragradient, proximal methods.
2. **Federated and distributed optimization**: FedAvg variants, gradient compression/sparsification, communication-efficient training, heterogeneous data (non-IID), local SGD, decentralized algorithms.
3. **Fine-tuning and PEFT** (parameter-efficient fine-tuning): LoRA, QLoRA, prefix-tuning, prompt-tuning, mixed-precision quantization + fine-tuning, rank adaptation.
4. **Preference optimization**: DPO, RLHF, reward modeling, PPO for language models.
5. **Bayesian optimization (BO)**: Gaussian process surrogates, acquisition functions (EI, PI, UCB, Thompson sampling), high-dimensional BO, latent-space BO, combinatorial/molecular BO.
6. **Min-max and saddle-point optimization**: GAN training, robust optimization, distributionally robust optimization (DRO), game-theoretic equilibria, variational inequalities.
7. **Combinatorial optimization**: TSP, VRP, scheduling, integer programming, neural combinatorial solvers, learning-based heuristics.
8. **Convergence theory**: NTK analysis, gradient flow, regret bounds, oracle complexity, non-convex convergence.
9. **Differentiable/implicit optimization**: Differentiable programming, implicit differentiation, bilevel optimization, unrolled optimization.
10. **Meta-optimization / learning to optimize**: Algorithm discovery, optimizer search, hyperparameter-free methods, AutoML.

### Key Challenges

- Closing the gap between theory (e.g., convex/smooth guarantees) and practice (non-convex, noisy, large-scale).
- Reducing communication costs in distributed/federated settings while maintaining convergence.
- Efficient exploration of large discrete or continuous spaces (BO, combinatorial).
- Understanding why empirically successful optimizers (e.g., Adam, Lion) work theoretically.
- Scalability to large models/datasets while preserving theoretical soundness.

### Score Distribution and Acceptance Bar (from 2,492 papers)

- **Mean rating**: 4.85 | **Median**: 4.8 | **Std**: 1.23
- **Acceptance rate**: 82.1% (unusually high — this topic captures many accepted papers, including a long tail from workshops)
- **Tier breakdown**:
  - Excellent (8–10): 40 papers — the truly outstanding work
  - Good (6–7): 2,369 papers — solid, publishable, clear contributions
  - Borderline (4–5): 4,603 papers — modest contribution, typical accept/reject territory
  - Low (1–3): 1,864 papers — fundamental flaws, insufficient novelty, or incorrect proofs

**Practical calibration**: A 5/10 is genuinely borderline — reviewers are split. A 6/10 is a soft accept at top venues. A 7/10+ requires either a novel algorithm with strong empirical results *or* a clean theoretical result that advances understanding. Scores of 8+ are reserved for work with outsize impact: a genuinely new paradigm (like DPO for RLHF), a result that explains a widely-used algorithm, or a method that dramatically surpasses prior art.

---

## 2. What Reviewers Praise (with Real Examples)

### 2.1 Novelty of Core Idea

"Novel" appears in 1,782 reviewer strength phrases — the most common signal of a strong paper.

Reviewers value originality at multiple levels:
- **Conceptual novelty**: A new framing that changes how we think about an algorithm or problem.
- **Technical novelty**: A new proof technique, architectural insight, or algorithmic mechanism.
- **Empirical novelty**: First to demonstrate something works at scale or in a new domain.

**Real example — LoRA Done RITE (8.67, Oral)**:
> "The authors take a significant step beyond simple intuitions by delving into the core of training efficiency, proposing a novel approach to fully achieve transformation invariance in LoRA models."

**Real example — Lion Secretly Solves Constrained Optimization (7.5, Spotlight)**:
> "I believe the work is original, as it is, up to my knowledge, the first to propose such a general Lion-K algorithm along with the corresponding Lyapunov function for its dynamics. In addition the derivation of such a Lyapunov function seems non-trivial, and I believe it will be of interest to the community."

**Real example — DPO (7.75, Oral)**:
> "DPO is a significant contribution in a high impact area... DPO opens a new paradigm of learning human preferences without RL, and is a viable and performant alternative to the RLHF pipeline, reducing computational demands, and requires little tuning of hyperparameters."

### 2.2 Strong Baselines and Comprehensive Comparisons

"Baseline" is the single most common weakness phrase (2,987x) and second most common strength phrase (997x). **This is the #1 factor separating accepted from rejected papers.**

Reviewers praise papers that:
- Compare against all relevant SOTA methods (not cherry-picked older baselines)
- Include fair comparisons (same budget, same hyperparameter tuning effort)
- Report results on multiple datasets/benchmarks, not just a single favorable one

**Real example — LoRA Done RITE (8.67, Oral)**:
> "The experimental results demonstrate significant improvement with marginal computation increase, results in a better trade-off compared to all SOTA methods."

**Real example — NF-BO (Latent BayesOpt, 8.0, Oral)**:
> "The evaluation is extensive and demonstrates a strong improvement." / "In the experimental benchmarks NF-BO together with TACS sampling greatly outperforms competing methods, leading to much better solutions in a fraction of the oracle calls."

### 2.3 Rigorous Theoretical Foundations

"Solid theoretical" (82x) and "strong theoretical" (59x) are among the top strength phrases.

Reviewers in optimization especially value:
- Formal proofs with clearly stated assumptions
- Convergence rates that are tight or improve over prior work
- Proofs that are *verifiable* and not hand-wavy

**Real example — LoRA Done RITE (8.67)**:
> "They provide rigorous proofs for all mathematical statements in the paper."

**Real example — Second-Order Min-Max (7.5, Oral)**:
> "The paper is well organized, the flow is easy to follow." / "The experimental results only support this point [of better computational complexity]."

**Real example — DPO (7.75, NeurIPS Oral)**:
> "The paper is grounded theoretically, equivalent to fitting a reparameterized Bradley-Terry model. The DPO update is simple and interpretable."

### 2.4 Comprehensive Ablation Studies

"Ablation" appears in both strength (725x) and weakness (1,056x) lists — missing ablations is a major rejection reason.

Reviewers expect ablations that isolate the contribution of each proposed component. A paper that shows strong final results but cannot demonstrate *why* each component helps is systematically downgraded.

**Real example — NF-BO (8.0, Oral)**:
> "The ablation of running the method with and without TACS shows a clear improvement when including it."

### 2.5 Clarity and Presentation

"Well-written" appears 857x (+ "well written" 444x) in strengths.

Reviewers reward:
- Clear problem formulation in the introduction
- Notation that is consistently defined
- Good visual figures that explain the method intuitively
- Proofs that are easy to verify

**Real example — Lion Paper (7.5)**:
> "This paper is well written and very easy to follow. The proposed framework is very interesting, not only demystifying the Lion optimizer, but also encompassing many other algorithms. The authors have clearly explained the idea and discussed thoroughly the related background."

**Real example — DPO (7.75)**:
> "Breaking down the DPO loss into its components with clear language is an excellent addition."

### 2.6 Practical Impact and Reproducibility

"Reproducib" appears 198x in strengths.

Reviewers value:
- Code release (or anonymous links)
- Enough implementation details to reproduce results
- Compute cost analysis alongside accuracy gains

**Real example — DPO (7.75)**:
> "The authors include the minimal code for DPO in the appendix which is commendable and many GPT-4 evaluation details for excellent reproducibility."

**Real example — LoRA Done RITE (8.67)**:
> "Given that LoRA is a widely-used training method and their work is computationally inexpensive, individuals training Large Language Models can greatly benefit."

---

## 3. What Reviewers Criticize (with Real Examples)

### 3.1 Missing or Weak Baselines (Most Common Weakness)

"Baseline" is the #1 weakness phrase (2,987x) — more than twice any other weakness. This kills papers.

Papers routinely fail because:
- They omit closely related prior work as baselines
- They compare against older/weaker methods while missing the relevant recent SOTA
- They use different evaluation protocols or budgets, making comparisons unfair

**Real example — LEGACY Gradient Compression (4.33, Reject)**:
> "The paper lacks benchmarking against a closely related work, the L-GreCo method by Markov et al. (2024), which also aims to find optimal parameters per layer at each iteration."
>
> (After rebuttal) "Legacy introduces a framework that... However, two closely related works leverage similar ideas. The first is Accordion by Agarwal et al. ... The second is L-GreCo by Markov et al."

**Real example — NF-BO (8.0, Oral) — received despite missing baselines**:
> "You should also compare to the simplest possible solution to the value discrepancy problem which was employed by [1] and [3], which is simply decoding frequently and checking the actual objective value."

**Real example — SITTO (2.33, Reject)**:
> "For domain-specific single-image 3D reconstruction, there are many existing fast and robust models... No technical novelty. It is a simple combination of two off-the-shelf models."

### 3.2 Limited Novelty and Incremental Contributions

"Novelty" (1,323x) and "incremental" (372x) are the 2nd and 7th most common weakness phrases.

Reviewers flag:
- Work that applies known algorithms to a new setting without insight
- Methods that are nearly identical to prior work without proper attribution
- Theoretical results that are trivial given existing tools

**Real example — QR-Adaptor (5.4, borderline accept)**:
> "The proposed Pareto Ranking Genetic Algorithm (PRGA) bears a striking resemblance to the existing Non-dominated Sorting Genetic Algorithm II (NSGA-II), to the extent that they are virtually indistinguishable. However, the authors have failed to acknowledge or cite NSGA-II, instead claiming PRGA as a 'novel multi-objective optimization method'."

**Real example — Second-Order Min-Max (7.5, Oral)**:
> "Overall, the paper feels like a very incremental result. Authors employ a known technique to reduce number of Hessian computations to existing second-order method... it lacks any novel ideas or solution of any complex problems."

(Despite this critique, this paper was accepted because the technical execution was rigorous and the result was non-trivial even if the combination was straightforward.)

### 3.3 Insufficient or No Ablation Studies

"Ablation" is the 3rd most common weakness phrase (1,056x).

**Real example — SITTO (2.33, Reject)**:
> "No two-stage ablation studies. The paper does not ablate either stage to show the significance of design choices."

**Real example — QR-Adaptor (5.4)**:
> "The current ablation experiments are insufficient. Additional studies should be conducted to demonstrate the impact of iterations and population size on the results."

**Real example — LoRA Done RITE (8.67)** — weakness despite high score:
> "The analysis over experimental results are limited, e.g., for some datasets, the proposed method demonstrates significant performance gain compared to LoRA (Adam), what is the property of dataset such that the proposed optimization can result in such improvement?"

### 3.4 Unclear Methodology and Missing Details

"Unclear how" (364x), "unclear whether" (324x), "unclear why" (141x), "unclear what" (119x) are persistent weakness phrases.

Reviewers are frustrated when:
- The acquisition function used in BO papers is never stated
- Hyperparameter tuning procedure is opaque
- Crucial implementation details are missing (prevents reproducibility)

**Real example — NF-BO (8.0, despite acceptance)**:
> "The GP surrogate model (vanilla GP/sparse GP) and the choice of acquisition function (EI, PI, Thompson sampling) appear to be missing... I don't believe the results are reproducible from the manuscript alone."

**Real example — LEGACY (4.33, Reject)**:
> "There is limited guidance on how to select parameters for defining the 'begin' and 'end' training stages or for distinguishing between 'small' and 'large' layers."

### 3.5 Limited Scope / Scalability Concerns

"Scalab" (582x) and "limited to" (360x) appear frequently as weaknesses.

Reviewers ask: Does this work scale beyond the small models tested? Is it limited to a narrow setting that won't generalize?

**Real example — QR-Adaptor (5.4)**:
> "It would be necessary to conduct experiments for Llama-3 family (e.g., Llama 3 8B), which are known to be harder to quantize."
> "The experiments in this article are limited, conducted only on Llama2, and the datasets used are not diverse enough."

**Real example — Second-Order Min-Max (7.5, Oral) — despite acceptance**:
> "The results only cover convex-concave minimax optimization for now, and there are no clear ways suggested to extend to broader problem classes like nonconvex-nonconcave functions."

**Real example — Lion Paper (7.5)**:
> "The current analyses apply to only algorithms with full gradient. It would be interesting to see results for Lion with stochastic gradients."

### 3.6 Incorrect or Vacuous Theoretical Claims

This is a fatal flaw that produces very low scores. Reviewers with high confidence (4–5) who find proof errors will give scores of 0–2.

**Real example — Gradient Flow Convergence (0.5, Reject)**:
> "The constant λ₀ in the exponential decay in the main result depends on the time horizon T. This is a critical problem, given that any strictly decreasing function f(t) can be written e^{-λ₀(t)t} for some λ₀(t) > 0. This fundamentally undermines the argument of the authors."

> "Showing that optimization problems will not be trapped at critical points has been a longstanding difficulty, and in this particular case simply making the claim without a formal proof does not constitute a valid theoretical result."

> "Taking Corollary 3.1.1. applied to Theorem 1 means that with probability 1 training a 2 layer ReLU net, with one hidden neuron in the hidden layer with N=10, n=10, M=1 gives exponentially decaying error. This is clearly not true — all data points that are in the 'inactive region' of the initial hidden neuron will NEVER have their error reduced."

### 3.7 Fair Comparison Issues

"Fair comparison" appears 174x as a weakness.

Reviewers flag papers where the proposed method has more parameters, more compute, or domain-specific advantages that make comparisons unequal.

**Real example — SITTO (2.33, Reject)**:
> "The domain-specific model is trained on Pix3D. And the experiments are conducted on Pix3D. Such comparisons to those zero-shot single-image 3D reconstruction models are even more unfair."

---

## 4. Required Baselines & Metrics

### 4.1 By Sub-Area

#### Stochastic Optimization / Gradient Methods
- **Required baselines**: SGD, SGD+momentum, Adam/AdamW, AdaGrad, RMSProp
- For optimizer papers: AdamW is the primary baseline; for LLMs, also compare against Sophia, Adan, Muon (recent)
- **Metrics**: Training loss curves, validation accuracy, convergence rate (iterations to reach target loss), wall-clock time
- **Expected**: Compare computational complexity (FLOPs per iteration, not just oracle calls), memory overhead

#### Federated Learning
- **Required baselines**: FedAvg, FedProx, FedNova, SCAFFOLD, MOON (for heterogeneous data)
- For communication compression: Top-k sparsification, random-k, SignSGD, PowerSGD
- **Metrics**: Communication rounds to convergence, accuracy at fixed communication budget, convergence under non-IID split
- **Expected**: Different levels of data heterogeneity (IID, mild non-IID, severe non-IID)

#### Fine-tuning / PEFT / LoRA
- **Required baselines**: Full fine-tuning (FT), LoRA (base), LoRA + AdamW, QLoRA, LoftQ (for quantized)
- For preference optimization: SFT baseline, PPO baseline (critical — DPO papers that skip PPO comparison are downgraded)
- **Metrics**: Task accuracy on standard benchmarks (MMLU, GSM8K, ARC, HellaSwag), perplexity, memory footprint, training time
- **Expected**: Results on multiple model families (Llama-2, Llama-3, Mistral at minimum); ablation on rank r

#### Bayesian Optimization
- **Required baselines**: Vanilla GP + EI/UCB, TuRBO (for high-dimensional), SAAS, BOiLS (for molecular)
- For molecular/sequence BO: REINVENT, LSTM+genetic, graph-based methods
- **Standard benchmarks**: PMO (Practical Molecular Optimization benchmark), rover trajectory, MuJoCo locomotion tuning, Hartmann functions, Branin
- **Metrics**: Number of oracle calls (sample efficiency is paramount), best objective found, AUC of optimization curve
- **Expected**: Multiple random seeds (≥5), error bars, oracle budget specified clearly

#### Min-Max / Saddle-Point
- **Required baselines**: GDA (gradient descent-ascent), EG (extragradient), OGDA, AGDA
- For nonconvex settings: SGDA, Local SGDA, Stochastic AGDA
- **Metrics**: Gap function, gradient norm, distance to Nash equilibrium, iteration complexity
- **Expected**: Empirical validation on matrix games or simple GAN tasks, not just theory

#### Combinatorial Optimization
- **Required baselines**: OR-Tools/Gurobi (exact), LKH-3 (for TSP), POMO, DPDP, EAS (for neural solvers)
- **Metrics**: Optimality gap (%), inference time, generalization across instance sizes
- **Expected**: Results on standard TSP/CVRP instance sizes (TSP100, TSP500, TSP1000)

#### Convergence Theory
- **Required**: Compare your rate against prior work in a table of complexity bounds
- **Expected**: Explicit constants (not just O(·) notation), clear statement of assumptions, tightness discussion

### 4.2 What Reviewers Expect Regardless of Sub-Area

1. **Multiple datasets/benchmarks** (not one favorable dataset)
2. **Multiple random seeds** with error bars (standard deviation or standard error)
3. **Computational cost analysis** (not just accuracy; memory and time matter)
4. **Code/reproducibility** — anonymous repo links are strongly encouraged
5. **Ablation studies** that isolate each contribution
6. **Hyperparameter sensitivity** analysis

---

## 5. Common Technical Pitfalls

### 5.1 Proof Errors in Convergence Theory Papers

The most catastrophic failure mode in theory papers is a vacuous or incorrect theorem.

**Pattern 1: λ₀ dependence on T**
A convergence bound of the form `f(t) ≤ exp(-λ₀ t)` is vacuous if λ₀ is allowed to depend on the time horizon T. Any decreasing function can be upper-bounded this way. The constant λ₀ must be shown to depend only on problem parameters (initialization, data, architecture dimensions), not on T.

**Pattern 2: Assuming away the hard part**
Claims like "GF cannot reach such a critical point" in NTK analysis without proof. The hard part of convergence analysis *is* showing you don't get stuck. Making an unproven assumption about this collapses the entire proof.

**Pattern 3: Composition of non-differentiable functions**
Citing differentiability results for activation functions while relying on the chain rule for compositions that may not be differentiable (e.g., repeated ReLU composition). Lee et al. (2020, NeurIPS) showed this is a serious issue.

**Pattern 4: NTK bounded below ↔ convergence**
Knowing G(0) is positive definite does NOT immediately give G(t) > 0 during training. The standard approach requires bounding the trajectory to a ball around initialization first (requires overparameterization + lazy training regime).

### 5.2 Algorithm Plagiarism / Missing Citations

**Pattern**: Presenting a known algorithm under a new name without citing the original.

The PRGA example from QR-Adaptor is representative:
> "The proposed Pareto Ranking Genetic Algorithm (PRGA) bears a striking resemblance to NSGA-II... they are virtually indistinguishable. However, the authors have failed to acknowledge or cite NSGA-II."

Reviewers familiar with optimization algorithms will catch this. For any gradient-free or evolutionary method, check if your "novel" algorithm reduces to NSGA-II, CMA-ES, Bayesian optimization with EI/UCB, or simulated annealing.

### 5.3 In-Domain Evaluation as SOTA Claim

Papers that train on a dataset and then evaluate on the same dataset/domain, comparing against zero-shot or out-of-domain baselines, will be flagged severely.

> "The domain-specific model is trained on Pix3D. And the experiments are conducted on Pix3D. Such comparisons to those zero-shot models are even more unfair."

### 5.4 Missing the "Why" in Ablations

It's not enough to show "method A beats method B." Reviewers want causal explanation. For papers with multiple components (like QR-Adaptor with three stages, or NF-BO with normalizing flows + TACS), every component must be ablated, and the paper must explain *why* each one helps.

> "I find it to be a reasonable hypothesis, but the current comparisons to baselines do not prove the hypothesis to be correct because the experiment is confounded by all the other differing implementation choices."

### 5.5 Ignoring the Stochastic Setting

Theory papers that only prove results for full-gradient (deterministic) methods but claim applicability to practical SGD are systematically critiqued:

> "The current analyses apply to only algorithms with full gradient. It would be interesting to see results for Lion with stochastic gradients."

A theoretical paper on optimizer analysis that cannot handle stochastic gradients has limited practical relevance.

### 5.6 Hyperparameter Sensitivity Without Guidance

Papers introducing new methods with additional hyperparameters must show sensitivity analysis and provide practical tuning guidance.

> "There is limited guidance on how to select parameters for defining the 'begin' and 'end' training stages... both of these could vary for different models and training purposes."

### 5.7 Normalizing Flow / Invertibility Claims

For Bayesian optimization in latent spaces: if you use a normalizing flow claiming "no value discrepancy," reviewers will ask:
1. Is perfect reconstruction actually necessary, or would "good enough" suffice?
2. Are you trading expressivity (normalizing flows are less expressive than VAEs) for invertibility?
3. Did you ablate by reintroducing value discrepancy to confirm it's the causal factor?

### 5.8 LLM Evaluation: Single-Model, Single-Task Bias

For fine-tuning optimization papers (LoRA, quantization, PEFT), evaluating only on one model family or one task family is a major weakness:

> "It would be necessary to conduct experiments for Llama-3 family, which are known to be harder to quantize." / "The experiments are limited, conducted only on Llama2."

Models with different characteristics (attention mechanisms, vocabulary size, quantization sensitivity) may behave differently.

---

## 6. Scoring Rubric for This Topic

### 3/10 — Likely Reject: Fundamental Flaws

**What it looks like**:
- Claims a major theoretical result but the proof contains a fatal error that invalidates the main theorem (as in the Gradient Flow Convergence paper, 0.5/10)
- No meaningful ablation studies; all components are used together without justification
- Comparison only against obsolete baselines while ignoring recent SOTA
- Algorithm is nearly identical to a published method (NSGA-II, CMA-ES) without acknowledgment
- In-domain evaluation presented as generalization

**Specific signals from reviewers**:
- "The theorem is vacuous because [constant] depends on [parameter it should be independent of]"
- "No technical novelty. It is a simple combination of two off-the-shelf models."
- "The authors have failed to acknowledge [PRIOR WORK], instead claiming [THEIR METHOD] as a novel algorithm"
- Confidence 4–5 reviewers who disagree unanimously on the core claim

**Example**: A paper claiming a unified convergence guarantee for gradient flow on all neural architectures, where the bound's rate constant secretly depends on the time horizon T — making every decreasing training curve trivially satisfy the "guarantee."

---

### 5/10 — Borderline: Limited Novelty or Incomplete Execution

**What it looks like**:
- Technically sound but incremental; applies existing algorithm X to setting Y without new insight
- Experiments are on limited scope (one model family, one task) — reviewers ask "does this generalize?"
- Missing a key baseline or ablation that would clinch the argument
- Good motivation but weaker-than-claimed novelty (reviewer says "this is essentially NSGA-II + Bayesian optimization applied to LoRA quantization")
- Additional hyperparameters introduced without clear tuning guidance

**Specific signals**:
- Reviewer ratings split: some 6+, some 3–4
- "The paper is well-organized and clearly written, but the contribution is limited"
- "The comparison to [KEY BASELINE] is missing"
- "The experiments are insufficient to support the claims"
- "Incremental over prior work"

**Example (QR-Adaptor, 5.4)**: A three-stage optimizer search for mixed-precision LoRA — practical and achieves good results, but PRGA ≈ NSGA-II (uncited), experiments only on Llama-2, and the "novel" aspect is primarily engineering application of existing algorithms.

**Example (LEGACY, 4.33)**: Adaptive gradient compression using layer size and training stage. Well-written, promising direction, but misses two directly relevant baselines (Accordion, L-GreCo), adds hyperparameters without adaptive selection, and provides no large-scale evidence.

---

### 7/10 — Solid Accept: Clear Contribution, Strong Execution

**What it looks like**:
- Clear novel element, even if incremental: a new Lyapunov function, a new acquisition function, a new connection between two algorithms
- Strong empirical results on multiple benchmarks with proper baselines
- Rigorous theory with clearly stated assumptions (even if not tight)
- Good ablations that support the core claims
- Well-written and reproducible

**Specific signals**:
- Multiple reviewers at 6–8, with consensus
- "The paper is well written and very easy to follow"
- "The results seem solid and novel"
- "Strong empirical results... the authors demonstrate strong improvement"

**Example (Lion Paper, 7.5)**: Proves that Lion implicitly solves a constrained optimization problem via a novel Lyapunov function. The finding is important (Lion is widely used), the Lyapunov function is non-trivial, and the paper is clearly written. Weakness: only covers full-gradient setting, and the theory-practice connection isn't fully closed.

**Example (Second-Order Min-Max, 7.5)**: Adapts the lazy Hessian technique to minimax optimization, achieving computational cost improvement of O(d^{1/3}) over prior work. Technically sound, well-executed; weakness is that the combination of ideas is straightforward.

---

### 9/10 — Exceptional: Paradigm-Shifting or Field-Defining

**What it looks like**:
- Opens a genuinely new direction or resolves a longstanding open question
- Simultaneously strong in theory, empirics, and impact potential
- Reviewers across multiple areas recognize the significance
- Code is released; results are robust
- The paper will be cited heavily regardless of publication venue

**Specific signals**:
- Majority of reviewers at 8–10 with high confidence
- "This is timely and gives an excellent alternative to RLHF"
- "I believe DPO is highly significant for researchers in the field and will serve as a powerful tool"
- The idea is simple enough to explain in a sentence but has deep consequences

**Example (DPO, 7.75 average but Oral)**: Directly trains language models from preferences without explicit reward modeling or RL. The insight — that the optimal reward under the RLHF objective can be expressed in terms of the policy ratio — is clean, theoretically grounded, and practically transformative. Became one of the most cited NeurIPS 2023 papers.

**Example (LoRA-RITE, 8.67)**: Proves that standard LoRA violates transformation invariance (a fundamental property for optimizer efficiency), derives the correct invariant update rule, demonstrates rigorous improvement across all LoRA-based methods with minimal compute overhead. Theory + practice + impact trifecta.

**What separates 8 from 9**: An 8/10 paper makes a definitive contribution to an existing line of work. A 9/10 paper changes how the field thinks about the problem.

---

## 7. Key Papers & Expected Citations

### Widely Expected Background Citations

#### First-Order Optimization
- **Adam**: Kingma & Ba (2015) — must cite for any adaptive gradient paper
- **AdamW**: Loshchilov & Hutter (2019) — decoupled weight decay
- **SGD + Momentum**: Polyak (1964), Nesterov (1983) — for theoretical comparisons
- **Lion**: Chen et al. (2023) — for any sign-based optimizer
- **Sophia**: Liu et al. (2023) — for second-order LLM optimizers
- **Convergence of SGD in nonconvex settings**: Ghadimi & Lan (2013)

#### LoRA / PEFT
- **LoRA**: Hu et al. (2022, ICLR) — must cite for any LoRA variant
- **QLoRA**: Dettmers et al. (2023) — must cite for quantized fine-tuning
- **LoftQ**: Li et al. (2024) — for quantized LoRA initialization
- **AdaLoRA**: Zhang et al. (2023) — for adaptive rank selection
- **DPO**: Rafailov et al. (2023, NeurIPS) — for preference optimization

#### Federated Learning
- **FedAvg**: McMahan et al. (2017) — must cite
- **FedProx**: Li et al. (2020) — for heterogeneous settings
- **SCAFFOLD**: Karimireddy et al. (2020) — for variance reduction
- **Top-k sparsification**: Alistarh et al. (2018) — for communication compression
- **PowerSGD**: Vogels et al. (2019) — for low-rank gradient compression

#### Bayesian Optimization
- **Gaussian Processes for ML**: Rasmussen & Williams (2006) — background
- **EI**: Mockus (1978), Jones et al. (1998) — acquisition functions
- **TuRBO**: Eriksson et al. (2019) — must cite for high-dimensional BO
- **BOA / SMAC**: for NAS/HPO applications
- **PMO benchmark**: Gao et al. (2022, NeurIPS) — for molecular optimization
- **LaMBO-2**: Gruver et al. (2024) — for protein/sequence optimization

#### Min-Max / Saddle-Point
- **Extragradient**: Korpelevich (1976)
- **OGDA**: Popov (1980), Mokhtari et al. (2020)
- **GAN training theory**: Goodfellow et al. (2014)
- **PPO**: Schulman et al. (2017) — for RL/RLHF comparisons
- **Lazy Hessian for minimization**: Doikov et al. (2023, ICML)

#### Convergence Theory
- **NTK**: Jacot et al. (2018, NeurIPS) — must cite for any NTK analysis
- **On exact computation with infinitely wide networks**: Arora et al. (2019)
- **On correctness of automatic differentiation for non-differentiable functions**: Lee et al. (2020, NeurIPS)
- **Marion et al. (2024, ICLR)**: Implicit regularization of deep residual networks towards neural ODEs

### Benchmarks That Reviewers Expect to See

| Area | Benchmark | Why Expected |
|------|-----------|--------------|
| Molecular BO | PMO (Practical Molecular Optimization) | Standard benchmark with 23 tasks; any molecular BO paper must report here |
| LLM fine-tuning | MMLU, GSM8K, ARC-Challenge | Standard LLM evals; omitting any is suspicious |
| LLM fine-tuning | MT-Bench, AlpacaEval | For instruction-following/alignment |
| TSP/VRP | TSP100, TSP500, CVRP100 | Standard sizes for neural combinatorial solvers |
| Federated | CIFAR-10/100 (non-IID), Shakespeare | Classic FL benchmarks |
| DRO | CivilComments-WILDS, Waterbirds | Standard for subpopulation shift |
| BO (continuous) | Hartmann-6D, Branin, Ackley | Classic synthetic functions |
| Optimizer comparison | ImageNet (ResNet-50), fine-tuning benchmarks | For general optimizer claims |

---

## 8. Evaluation Heuristics for the Judge

### Red Flags (Strong Push Toward Reject)

1. **Proof errors found**: If a reviewer with confidence ≥4 identifies a flaw in the main theorem, treat this as near-fatal unless the authors can demonstrably patch it.
2. **Missing the obvious baseline**: If there's a 2023/2024 paper that directly solves the stated problem and it's not compared against, the paper should be rejected or asked for major revision.
3. **Algorithm = known algorithm**: If the "novel" algorithm is functionally equivalent to a published method, the paper must provide a clear formal distinction and justify the separate contribution.
4. **In-domain train/test**: Any paper that trains on distribution D and compares to out-of-distribution baselines on D to claim superiority.
5. **No ablation on core components**: If the paper has 3+ components and no ablation isolating each, this is a strong weakness.

### Green Flags (Push Toward Accept)

1. **Non-trivial connection revealed**: Shows that two seemingly unrelated things are deeply connected (Lion ↔ constrained optimization; DPO ↔ reward reparameterization).
2. **Tight complexity result**: Achieves the known lower bound or closes the gap to it in a meaningful way.
3. **Strong ablation + analysis**: Each design choice is justified by experiments *and* theoretical intuition.
4. **Anonymous code that runs**: Code release before review conclusion signals high confidence in reproducibility.
5. **Consistent results across model families and scales**: Not just one favorable setting.

### How to Handle the "Incremental but Well-Executed" Paper

Many optimization papers (like Second-Order Min-Max, 7.5) are "a well-known idea applied to a slightly different setting with rigorous execution." These can be solid accepts if:
- The application requires non-trivial adaptation (new proof techniques, not just plug-and-play)
- The community actively needs the result (e.g., min-max second-order methods have real applications)
- The paper is honest about the scope of contribution

These should score 6–7. They should not score 8+ unless the execution reveals something fundamentally new.

### When Theory Papers Succeed Without Experiments

Pure theory papers with no empirical results can succeed if:
1. They prove something that was *open* and non-trivial (not a corollary of known results)
2. The proof is fully verifiable and assumptions are tight
3. The result has clear practical implications even without direct empirical validation

Pure theory papers fail when:
- The result is actually known and just restated with different notation
- The theorem is vacuous (constants depend on parameters they should be independent of)
- The paper misses straightforward counterexamples that the reviewer can construct

---

## 9. Tone Calibration

The distribution of this topic shows mean rating ~4.85, which means the average submitted paper is borderline. When scoring:

- **Don't inflate scores** for ambitious papers with execution problems. A paper claiming to unify all neural network convergence theory but with vacuous proofs is a 0–2, not a 5.
- **Don't penalize incremental papers unfairly** — the field advances through solid incremental work. A paper that applies lazy Hessians to minimax optimization (7.5) deserves credit if the extension required genuine technical effort.
- **Novelty is necessary but not sufficient** — DPO and LoRA-RITE are highly novel *and* carefully executed. Novel ideas with sloppy execution (missing baselines, proof gaps) score 4–5, not 7+.
- **Soundness > Contribution for acceptance** — a paper can be modest in scope but rigorously executed (6–7). A paper with large claimed contribution but unsound execution is a reject (2–4).

The rubric in brief:
- Soundness 1 (poor) + Contribution 1 → 1–3 regardless of presentation
- Soundness 3 + Contribution 2–3 → 5–6 (borderline)
- Soundness 3–4 + Contribution 3–4 → 6–8 (accept territory)
- Soundness 4 + Contribution 4 + Novel insight → 8–10 (oral territory)
