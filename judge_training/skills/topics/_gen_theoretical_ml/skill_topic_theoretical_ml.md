# Skill File: Evaluating Research in Theoretical Machine Learning

**For use by AI judge agents evaluating submissions in the "theoretical_ml" topic area.**

---

## 1. Topic Overview

### What This Area Covers

"Theoretical ML" at ICLR/NeurIPS/ICML spans a wide range of mathematically rigorous work:

1. **PAC learning and statistical learning theory**: VC dimension, fat-shattering, Rademacher complexity, generalization bounds, sample complexity, agnostic vs. realizable learning, online learning, regret bounds, learnability characterizations (OIG dimension, Littlestone dimension, DS dimension).
2. **Kernel methods and spectral algorithms**: Kernel ridge regression (KRR), spectral profiles, reproducing kernel Hilbert spaces (RKHS), generalization error for kernel methods, Gaussian processes.
3. **Neural network theory**: NTK (neural tangent kernel) analysis, gradient flow, mean-field theory, feature learning, two-layer network theory, expressivity, depth-width trade-offs.
4. **High-dimensional statistics**: Random matrix theory, high-dimensional asymptotics, Wishart model, Gaussian models, spiked covariance, SGD in high dimensions.
5. **Optimization theory** (with theoretical focus): Convergence analysis of gradient methods, second-order methods, regret bounds for online optimization, variance reduction, meta-learning theory.
6. **Reinforcement learning theory**: MDP sample complexity, PAC-MDP, average reward MDPs, span-based complexity, model-based RL bounds, weakly communicating/ergodic/multichain MDPs.
7. **Information-theoretic approaches**: Mutual information bounds, channel capacity, compression schemes, minimax lower bounds via Fano's inequality.
8. **Operator learning theory**: Approximation theory for operators between function spaces, holomorphic operators, Banach/Hilbert space learning.
9. **Domain generalization and distribution shift theory**: Invariant risk minimization, causal inference theory, posterior generalization, Bayesian treatment of domain shift.
10. **Combinatorial/approximation algorithms with ML**: Learning-augmented algorithms, algorithms with predictions, online algorithms, competitive analysis.
11. **Graph neural networks theory**: Graphon approximation, expressivity, separation power, Weisfeiler-Leman hierarchy.
12. **Continual learning theory**: Online/meta-continual learning, Hessian-based regularization, regret in sequential settings.

### Key Challenges

- Closing the gap between theoretical assumptions (realizability, convexity, Gaussianity) and practical non-convex, overparameterized settings.
- Proving tight matching upper and lower bounds for fundamental quantities (sample complexity, regret, approximation error).
- Characterizing learnability with novel combinatorial dimensions that are both necessary and sufficient.
- Understanding why empirically successful methods work (e.g., why SGD generalizes, why transformers learn features).
- Extending results from toy/Gaussian models to realistic architectures and data distributions.
- Making theoretical results self-contained and accessible to the broader ML community.

### Score Distribution and Acceptance Bar (from 2,238 papers)

- **Mean rating**: 4.97 | **Median**: 5.0 | **Std**: 1.25
- **Acceptance rate**: 83.2%
- **Rating range**: 0.0 to 8.67
- **Tier breakdown**:
  - Excellent (8–10): 38 papers — landmark results, open problem resolutions, paradigm shifts
  - Good (6–7): 2,382 papers — solid publishable theory with clear contributions
  - Borderline (4–5): 4,199 papers — partial contributions, unclear assumptions, limited scope
  - Low (1–3): 1,407 papers — incorrect proofs, no ML relevance, trivial results, insufficient novelty

**Practical calibration**: A 5/10 is genuinely borderline — reviewers often split 3/6/6/5. A 6/10 means solid theoretical contribution with correct proofs and reasonable scope. A 7/10+ requires either (a) a new proof technique that resolves a known open problem, (b) tight matching bounds, or (c) a unifying framework that explains multiple existing results. Scores of 8+ are reserved for resolving long-standing open problems or providing foundational insights that will reshape how the community thinks about a problem.

---

## 2. What Reviewers Praise (with Real Examples)

### 2.1 Resolving Open Problems and Fundamental Characterizations

The highest-rated papers resolve open problems or provide fundamental characterizations that were previously unknown. Reviewers respond extremely positively to work that answers questions the field has been asking for years.

**Real example — "Optimal Learners for Realizable Regression" (7.6, NeurIPS 2023 Oral)**:
> "This paper studies a fundamental problem in learning theory, which has, surprisingly, been left open for several decades. The results are strong and comprehensive." (Rating: 8)

> "Significant results that complete the landscape of learnability of PAC/online learning in realizability regression." (Rating: 9)

> "The paper provides combinatorial dimensions that characterize realizable regression in both batch as well as online settings... technically sound and is definitely an important technical contribution to the field." (Rating: 8)

This paper introduced new dimensions (γ-OIG, γ-graph, online dimension) that both characterize and construct optimal learners for regression — solving problems in PAC and online learning simultaneously.

**Real example — "Span-Based Optimal Sample Complexity for Weakly Communicating and General Average Reward MDPs" (7.75, NeurIPS 2024 Oral)**:
> "Solving a major open problem based on an interesting insight: This is a breakthrough paper." (Rating: 10)

> "The algorithmic novelty of the paper seems limited. Only the analysis seems new." (Rating: 7) — even critical reviewers accepted it because the result was important enough.

### 2.2 Tight Matching Upper and Lower Bounds

Theoretical papers that provide both upper and lower bounds that match (up to log factors) are consistently praised. This demonstrates the result is optimal and not improvable.

**Real example — "Optimal deep learning of holomorphic operators between Banach spaces" (7.67, NeurIPS 2024 Spotlight)**:
> "They identify a family of DNNs that achieve optimal generalization bounds for such operators... The results demonstrate that deep learning achieves the best possible generalization bounds, and no method can surpass these bounds, up to logarithmic terms."

> "Authors managed to significantly improve previously known bounds and show that DNN can obtain near-optimal performance (in terms of the number of samples needed) in non-adaptive iid settings."

> "The results are new and interesting, expanding on previous work by addressing holomorphic mappings between arbitrary Banach spaces and allowing standard training methods for the DNNs utilized." (Rating: 8)

### 2.3 Novel Connections Between Previously Separate Areas

Papers that formally bridge two distinct research streams are highly valued. This demonstrates that the author has a deep understanding of both areas and has uncovered a non-trivial relationship.

**Real example — "Meta Continual Learning Revisited" (8.67, ICLR 2024 Oral)**:
> "The reviewer really enjoys reading this paper. This should be the first paper that formally and clearly dissects the relationship between seminal regularization-based methods and the methodology of meta-continual learning." (Rating: 10)

> "It is interesting to see that an inherent connection can be built between the regularization-based methods and Meta-CL methods via the roles of the Hessian information in these two methodological streams." (Rating: 8)

> "Although there exist papers that try to unify different regularization-based CL methods in a unified framework, to the best of my knowledge, this paper should be the first one to connect the regularization-based CL methods with the methodology of Meta-CL, which may stand as a new research direction in the future." (Rating: 10)

### 2.4 Non-Obvious, Counterintuitive Results

Results that challenge intuitions are especially valued. Reviewers look for papers that reveal surprising phenomena with rigorous proof.

**Real example — "Towards a statistical theory of data selection under weak supervision" (7.75, ICLR 2024 Oral)**:
> "Biased to unbiased sampling comparison was very insightful, as there are many works where only unbiased sampling is considered, which appeared to be suboptimal under the presented setting." (Rating: 10)

> "data selection can beat training on the full sample in some cases and unbiased data selection can be highly sub-optimal compared to biased mechanisms." (Rating: 8)

> "The paper reveals properties of data selection schemes, unusual in the well-established fields of data selection, such as the field of coresets." (Rating: 10, after discussion)

### 2.5 Unifying Frameworks with Broad Scope

Papers that introduce a general framework applicable to many existing methods, rather than solving one specific problem, receive strong praise.

**Real example — "Generalization error of spectral algorithms" (8.0, ICLR 2024 Spotlight)**:
> "The idea of spectral algorithm is novel and can be seen as unifying different common machine learning methods like KRR and GD." (Rating: 8)

> "Equation (7) in introducing the profile h(λ) seems new and interesting. The theory appears to be rich, reasonable and self-contained." (Rating: 8)

> "The paper takes a generic point of view. It seems that the result can be applied to many different situations, which improves the power of the result. The theory is nicely applied to provide a new perspective to already observed phenomena." (Rating: 8)

### 2.6 Accessible Writing Despite Technical Depth

Even for highly technical papers, reviewers praise clear writing that guides the reader through complex material with appropriate intuition.

**Real example — "Optimal Learners for Realizable Regression"**:
> "The paper is well-written, easy to follow... The authors did a great job in introducing the prior results and presenting the high-level roadmaps behind the technical proofs." (Rating: 8)

**Real example — "Meta Continual Learning Revisited"**:
> "The key message and insights are conveyed smoothly in the whole paper, and the author does a really good job of presenting them in a decent way. Table 1 provides a very precise and clear summary and comparison of the seminar and the state-of-the-art regularization-based method." (Rating: 10)

**Real example — "Optimal deep learning of holomorphic operators"**:
> "The paper is well-written and includes a thorough review of current research on learning holomorphic operators... formal statements are well explained, supplemented with discussions and examples which significantly simplifies understanding of the results." (Rating: 8)

### 2.7 Theory Validated by Experiments

For papers that are primarily theoretical, even simple experiments on synthetic datasets significantly strengthen acceptance. Reviewers want to see the theory "come to life" with numerical validation.

**Real example — "Optimal deep learning of holomorphic operators"**:
> "The theoretical findings are also backed up by practical experiments." (Rating: 8)

> "The contribution is primarily theoretical, but formal statements are well explained, supplemented with discussions and examples... Authors illustrate their theoretical results... with several numerical experiments, including diffusion equation in D=2, Navier-Stokes-Brinkman equation in D=2 and Boussinesq equation in D=3." (Rating: 8)

**Real example — "Generalization error of spectral algorithms"**:
> "The paper contains both theoretical deductions and experimental validations." (Rating: 8)

One reviewer flagged: "Although this is a theoretical paper, it would be helpful to include some experiments, even if they are on synthetic datasets. This helps explain (and justify) the theory." — illustrating that for purely theoretical papers, even simple numerical validation is expected.

---

## 3. What Reviewers Criticize (with Real Examples)

### 3.1 Incorrect or Hand-Wavy Proofs

This is the most fatal flaw in theoretical ML papers. Even one unverifiable proof collapses an entire submission.

**Real example — "Curvature Meets Bispectrum: A Correspondence Theory for Transformer Gauge Invariants" (1.5, ICLR 2026 Rejected)**:
> "Theorem 2.1 claims to describe the full gauge group of a single layer of multi-head attention. This is a notoriously-challenging problem. The proof of this theorem is mis-referenced... Crucially, the proof of necessity/maximality – which is the non-trivial part of the claim – is just a few lines long, and is completely unclear to me." (Rating: 0)

> "Even further, Proposition 2.2 claims that the gauge group of a deep network factorizes as a product of layer-wise gauge groups. This is an even more challenging problem which, in my view, would probably require a highly-elaborate proof. Again, the provided proof is a few lines long, and is completely vague, informal, and unclear." (Rating: 0)

> "The combination of mis-references, overall structure, and unsupported claims, raises the suspicion of heavy LLM involvement in the writing of the paper." (Rating: 0)

### 3.2 Unclear Motivation and Lack of Practical Relevance

Even mathematically correct theoretical results can be rejected if reviewers cannot see why the ML community should care. The onus is on the authors to motivate why their theoretical contribution matters.

**Real example — "Curvature Meets Bispectrum"**:
> "The paper lacks clear motivation and practical relevance. While the authors establish a mathematical connection, they fail to articulate why this matters for the broader machine learning community or what concrete problems this solves. The only hint at application mentions 'promising targets for head merging, shared-parameter updates, or careful learning-rate scheduling,' but provides no elaboration." (Rating: 2)

> "I am unsure how the main result in Theorem 5.1 is practically relevant, that is, how specifically it can be used to understand or analyze transformers in practice." (Rating: 2)

### 3.3 Non-Novel or Trivially Known Results

Claiming as main contributions results that are already well-established in the literature leads to rejection.

**Real example — "Approximation of the Gompertz trend with a multilogistic function" (1.33, ICLR 2026 Rejected)**:
> "it has been long known that a Gompertz function is itself a logistic function, so estimating it with a sum of other logistic functions is already well known, routine and doesn't tell us anything new." (Rating: 0)

**Real example — "Bayesian Domain Invariant Learning" (5.0, ICLR 2024 Accept)**:
> "There is no need to present p(w|D^{c}) = E_{p(D^{v})}(p(w|D^{c}, D^{v})) as a theorem; it is a standard statistical technique known as marginalization. Routine operations in statistics, like this, do not necessitate proof." (Rating: 6, margin above threshold)

> "the assumption of full independence between the domain invariant and domain-specific information is quite strong." (Rating: 3)

### 3.4 Insufficient Scope / Too Narrow

Papers that only validate on one synthetic example, one specific data model, or one particular architecture are criticized for limited generality.

**Real example — "Generalization error of spectral algorithms" (8.0, despite this weakness)**:
> "due to the complex form of the generalisation error, only two simple data models are considered." (Rating: 8)

> "The analysis in the paper does not account for the errors induced by discretization... Although it is claimed at the beginning of the paper that the theory covers gradient descent, what is really done is for gradient flow." (Rating: 8)

**Real example — "Approximation of the Gompertz trend"**:
> "The scope is limited. Only one specific Gompertz function is tested. The method's behavior for general parameters or noisy data is not explored." (Rating: 2)

> "No mathematical guarantees are given, e.g., no proof that three logistic terms are needed for such an error, or, more interestingly, how the approximation error behaves as more terms are added." (Rating: 2)

> "The work seems too narrow and descriptive for a top-tier conference like ICLR." (Rating: 2)

### 3.5 Missing ML Relevance

Papers with purely mathematical content that do not connect to machine learning problems are summarily rejected.

**Real example — "Approximation of the Gompertz trend"**:
> "The main weakness of the paper is its possible lack of relevance to the ICLR community. Although there are uses of Gompertz curves in machine learning the authors make no effort to draw out these connections or illustrate the relevance of their work to a machine learning community." (Rating: 2)

> "What is the relevance of this work to the machine learning community?" (Rating: 2)

### 3.6 Not Self-Contained / Relies on Concurrent Submissions

Papers that require the reader to consult simultaneously submitted companion papers are viewed very negatively.

**Real example — "Sequential Indeterminate Probability Theory" (1.5, ICLR 2024 Rejected)**:
> "The paper builds upon another work submitted at the same conference. The core ideas of indeterminate probability theory have not been presented in the paper, making this paper hard to read." (Rating: 3)

> "Indeterminate Probability Theory is inadequately explained in this submission, forcing the reader to the supplementary material for the concurrent submission." (Rating: 1)

> "the theoretical contribution is highly dependent on [concurrent submission], but I failed to figure out the key contribution of the manuscript upon [it]." (Rating: 1)

### 3.7 Over-Mathematicized Without Justification

Dense streams of technical statements without intuition or narrative are a common failure mode in rejected theoretical papers.

**Real example — "Curvature Meets Bispectrum"**:
> "The paper is inaccessible and poorly organized. The paper jumps between topics, primarily highly technical, without providing intuitive explanations or clear narrative flow. Even the introduction does not establish a clear high-level insight about the problem." (Rating: 2)

> "Dense (and rather discrete) series of technical statements and theoretical machinery follow one after another, without first establishing why they are introduced and what they imply." (Rating: 2)

### 3.8 Assumptions Too Strong, Unsatisfied in Practice

Reviewers frequently challenge assumptions. If the core results require unrealistic conditions (e.g., perfect surrogate models, infinite batch sizes, locations near optima), the practical significance is undermined.

**Real example — "Towards a statistical theory of data selection"**:
> "My main concern is the applicability in general setting and the assumptions in the paper: There is a concern in that (to my understanding) only the behavior exactly at the optimum was considered... In most non-trivial non-linear models an iterative optimization procedure must be considered, which results in parameters passing through a range of values." (Rating: 5, borderline)

> "all mathematical analyses beyond Section 4 assume that the surrogate model is equivalent to the optimal Bayes conditional distribution... the authors have not been able to provide a sound theoretical justification for the 'magic' effects claimed in Figure 1." (Rating: 8, despite this criticism)

**Real example — "Meta Continual Learning Revisited"**:
> "In Proposition 3, the authors assumed that the batch size of the inner step adaptation is sufficiently large. I wonder how large is enough to make the following analyses hold." (Rating: 8)

> "In Proposition 2, the authors assumed that θ is located in the ε-neighbourhood of the optimal model parameter. Is it too strong?" (Rating: 8)

### 3.9 Disconnect Between Theory and Experiments

A common complaint is when experiments do not validate the key theoretical claims, or when the theory and experiments are set up in different ways.

**Real example — "Optimal deep learning of holomorphic operators"**:
> "one can clearly see the signs of saturation for larger m. This is also clear from operator learning literature that relative error rarely fell below 10^{-3}. Can the authors please comment on that? Is it because optimization error prevails for large m?" (Rating: 8)

> "All results are given for perfect encoder and decoder. Can the authors share some thoughts on whether it is possible to test their upper bound with an imperfect decoder and encoder?" (Rating: 8)

### 3.10 Missing Recent State-of-the-Art Baselines

Even in theoretical papers, reviewers expect comparisons to recent work. Citing only old baselines while ignoring recent improvements is penalized.

**Real example — "Bayesian Domain Invariant Learning"**:
> "The literature compared in this study appears to be somewhat outdated, with the highlighted method, SOTA CORAL, dating back to 2017. Given that the proposed method relies on an existing domain generalization (DG) method for initialization, it becomes crucial to benchmark against more recent approaches." (Rating: 6)

**Real example — "Meta Continual Learning Revisited"**:
> "the paper could benefit from a more extensive comparison by including well-established methods such as FTML and LFW." (Rating: 8)

---

## 4. Required Baselines & Metrics

### 4.1 For Learning Theory Papers (PAC, Online, Statistical)

**Expected theoretical comparisons**:
- VC dimension and fat-shattering dimension (for regression/classification complexity)
- Rademacher complexity bounds
- Prior learnability characterizations (e.g., Littlestone dimension for online learning)
- Minimax lower bounds (via Fano's inequality or Le Cam's method)
- Prior state-of-the-art sample complexity bounds (must cite and surpass)

**Expected empirical validation** (even if secondary):
- Synthetic datasets demonstrating the theoretical scaling (e.g., error vs. sample size plots)
- Comparison showing theory matches empirical behavior
- Computation of the proposed dimension/quantity for natural function classes

### 4.2 For Kernel Methods / Spectral Algorithms

**Expected baselines**:
- Kernel Ridge Regression (KRR) — the canonical baseline
- Gradient Descent / Gradient Flow
- Nyström approximation methods
- Random features (for scalability comparisons)
- Prior generalization bounds for KRR (e.g., Caponnetto & De Vito 2007, Steinwart & Christmann)

**Expected metrics**:
- Generalization error (excess risk)
- Sample complexity
- Comparison of saturation effects

### 4.3 For Neural Network Theory

**Expected baselines**:
- NTK (neural tangent kernel) bounds
- Mean-field theory results
- Prior bounds for specific architectures (two-layer networks, transformer theory)
- Feature learning vs. lazy training regime comparisons

**Key references expected to appear**:
- Jacot et al. (2018) for NTK
- Du et al. (2019) for gradient descent convergence
- Arora et al. (2019) for fine-grained optimization analysis

### 4.4 For MDP / RL Theory

**Expected baselines**:
- Model-based vs. model-free sample complexity comparison
- Prior span-based / diameter-based complexity bounds
- Comparison against navigating model results (generative model is stronger assumption)
- Regret vs. PAC-sample-complexity framing

**Expected metrics**:
- ε-optimal policy sample complexity
- Minimax lower bounds
- State-action space size and span/diameter dependence

### 4.5 For Continual / Meta-Learning Theory

**Expected baselines**:
- EWC (Elastic Weight Consolidation) and its variants
- MAML / Meta-learning baselines (FTML, LA-MAML)
- Replay-based methods (ER, GEM)
- Online gradient descent (OGD)

**Datasets expected** (for empirical validation):
- CIFAR-10, CIFAR-100, TinyImageNet
- Split versions (Split-CIFAR, Permuted MNIST)

### 4.6 For Domain Generalization Theory

**Expected baselines**:
- ERM (Empirical Risk Minimization)
- IRM (Invariant Risk Minimization, Arjovsky et al. 2019)
- DomainBed benchmark results
- Recent DG methods (post-2020)

**Common failure**: Comparing only against CORAL (2017) while ignoring 2020–2024 advances.

### 4.7 For Operator Learning Theory

**Expected baselines**:
- FNO (Fourier Neural Operator) — DeepMind/MIT standard
- DeepONet
- Classical approximation theory bounds (sparse polynomial / Chebyshev approximation)
- Encoder-decoder neural operators with prior bounds

---

## 5. Common Technical Pitfalls

### 5.1 Proof at Optimal Only, Not Along Optimization Path

Many theoretical papers prove results only at the global optimum of a non-convex loss, but SGD does not necessarily reach the global optimum. Reviewers consistently flag this.

> "There is a concern in that only the behavior exactly at the optimum was considered... In most non-trivial non-linear models an iterative optimization procedure must be considered, which results in parameters passing through a range of values in addition to the final minima." (from data selection paper review)

### 5.2 Gradient Flow vs. Gradient Descent Conflation

Many theoretical papers analyze gradient flow (continuous time) but claim results for gradient descent (discrete). Reviewers catch this.

> "Although it is claimed at the beginning of the paper that the theory covers gradient descent, what is really done is for gradient flow." (from spectral algorithms paper review)

### 5.3 Trivial Theorems Presented as Main Contributions

Basic results from probability theory (marginalization, Bayes rule) or well-known results presented as novel theorems without proper attribution damage credibility severely.

> "There is no need to present p(w|D^{c}) = E_{p(D^{v})}(p(w|D^{c}, D^{v})) as a theorem; it is a standard statistical technique known as marginalization." (from Bayesian DG paper)

### 5.4 Undefined or Inconsistent Notation

Technical papers with undefined symbols or inconsistent notation lose reviewer confidence quickly, even if the underlying ideas are sound.

> "some detailed notations are not clear in the context, which reduces the readability." (from Meta-CL paper)

> "In Section 3.1, the paper claims that 'we do not need to specify how D^{c} and D^{v} are extracted from D'. Is this useful?" (from Bayesian DG paper)

> "The terminologies used in the paper are confusing. In the introduction, the authors equate domain-invariant features to domain-invariant parameters... parameters refer to learnable model weights and biases, while features denote the encoder's output." (from Bayesian DG paper)

### 5.5 Assumptions Not Quantified or Verified

Vague qualitative assumptions ("sufficiently large batch size", "ε-neighbourhood of optimum") without characterization of when they hold in practice are a red flag.

> "In Proposition 3, the author assumes that the batch size for inner step adaptation is sufficiently large. How do we quantify the term 'sufficiently large' in reality? Is there any principle we can obtain from the proposed theorem to guide us in choosing the batch size?" (from Meta-CL paper)

### 5.6 Circular or Incomplete Lower Bound Arguments

For papers claiming minimax optimality, reviewers carefully check that lower bounds are genuine and the argument is complete.

> "To me, the discussion on the lower bound is not complete." (from RL sample complexity paper)

### 5.7 Parameter Dependence on Unknown Quantities

Algorithms or results that depend on parameters that cannot be estimated in practice (e.g., horizon H, span, Bayes-optimal distribution) require careful discussion.

> "The authors discuss the fact that H cannot be estimated while D can be. However they do not mention anything about B?" (from RL sample complexity paper)

### 5.8 Mixing Asymptotic and Non-Asymptotic Claims

Papers that mix asymptotic analysis (n→∞) with claims about finite-sample behavior without clear delineation confuse reviewers.

> "all the mathematical analyses in this work are based on asymptotic conditions (n,N→∞ with n/N→γ), which remain intriguing but could be expanded to encompass a broader scope. For instance, non-asymptotic guarantees and cases where n/N→0 could be explored." (from data selection paper)

### 5.9 Experimental Setup Not Aligned with Theory

When the experiments use perfect encoders/decoders while the theory's significance comes from handling imperfect ones, or when approximation factors in theory don't appear in experiments, reviewers notice.

> "All results are given for perfect encoder and decoder. Can the authors share some thoughts on whether it is possible to test their upper bound with an imperfect decoder and encoder?" (from holomorphic operators paper)

### 5.10 No Comparison Against Adjacent Work

Concurrent or very recent work that addresses similar problems must be cited and discussed, even if it appeared while the paper was in review.

> "I think they should be mentioned because they answer some questions raised in the paper. First XXBoone shows that regret bounds using H are possible without prior knowledge of H, disproving the supposed conjecture in papers [5,4,25] cited in this submission." (from RL sample complexity paper)

---

## 6. Scoring Rubric for This Topic

### 3/10 — Clearly Below Bar (Example: Approximation of Gompertz trend, rating=1.33)

**Characteristics**:
- No connection to machine learning problems, or ML connection is superficial
- Results are either incorrect, trivially known, or demonstrate no advance over prior work
- Paper is not self-contained (relies on concurrent submissions for core theory)
- Writing is poor (grammatical errors, undefined notation throughout)
- Only one synthetic example, no generality
- No mathematical guarantees (only empirical demonstration on one case)
- Missing any comparison to relevant prior work

**Reviewer language at this tier**:
- "it has been long known that..."
- "the work seems too narrow and descriptive for a top-tier conference"
- "the manuscript is not well self-contained"
- "technically not sound"
- "results worse than baselines"

**Score 1–3 when**: The paper fundamentally fails on correctness, novelty, or ML relevance. Any single fatal flaw (incorrect proofs, trivial results, no ML connection) can put a paper here.

### 5/10 — Borderline (Example: Bayesian Domain Invariant Learning, rating=5.0 Accept; EDM, rating=5.0 Reject)

**Characteristics**:
- Interesting idea or direction, but execution has significant gaps
- Core theorem is either trivial or has strong/unverifiable assumptions
- Reasonable experiments but missing important baselines or ablations
- Writing is imprecise: notation issues, concepts not clearly defined
- Contribution is real but incremental or narrow
- Mixed reviewer verdicts (some positive, some negative)

**What separates accepted from rejected at this tier**:
- At 5/10, decisions often come down to reviewer discussion and AC judgment
- Accepted papers at 5/10 typically have at least one strong reviewer who champions the direction
- Rejected papers have multiple reviewers finding fundamental conceptual issues

**Reviewer language at this tier**:
- "The idea is interesting, but..."
- "the assumption of full independence is quite strong"
- "There is no need to present this as a theorem"
- "borderline below the acceptance threshold"
- "limited novelty" (combined with some positive remarks)

**Score 4–5 when**: The paper has a genuine contribution but significant presentation, scope, or correctness issues that prevent confident acceptance. The work is in the right area but execution is incomplete.

### 7/10 — Solid Accept (Example: Towards statistical theory of data selection, 7.75 Oral; Span-based optimal sample complexity, 7.75 Oral)

**Characteristics**:
- Clear, important contribution that the field will cite
- Correct proofs with well-stated assumptions
- Non-obvious results (challenges existing intuitions OR resolves natural questions)
- Good scope: applies to a range of settings, not just one toy example
- Experiments validate theory (even if simple/synthetic)
- Well-written: clear narrative, proper notation, accessible to non-specialists in the subarea
- Baselines are appropriate and fair

**What distinguishes 7 from 6**:
- At 6: the contribution is correct and published, but could be somewhat incremental or the paper covers known terrain with modest improvement
- At 7: the contribution either resolves a natural open question, introduces a genuinely new technique/dimension, or produces non-obvious results

**Reviewer language at this tier**:
- "solid theoretical work with robust mathematical underpinnings"
- "The paper is well written and explains the previous work well"
- "results paint an interesting picture for data selection and open nice research directions"
- "The paper improves on related work and obtains an algorithm that matches the lower bound"

**Score 6–7 when**: Paper is technically sound, novel in a meaningful sense, well-presented, and advances the field. Minor issues (restricted to special cases, one missing baseline, slightly strong assumptions) don't prevent acceptance.

### 9/10 — Exceptional (Example: Optimal Learners for Realizable Regression, 7.6 Oral; Meta-CL Revisited, 8.67 Oral)

**Characteristics**:
- Resolves a fundamental open problem, or
- Provides a new paradigm/framework that unifies multiple existing approaches, or
- Delivers tight matching bounds for a major problem in ML theory
- Multiple reviewers independently describe it as important or landmark
- Self-contained with complete proofs
- Results are fully general (not restricted to Gaussian/linear models or single architectures)
- Writing is exemplary: clear, well-motivated, beautifully presented
- Impact clearly extends beyond the specific paper

**Reviewer language at this tier**:
- "This is a breakthrough paper."
- "should be the first paper that formally and clearly dissects the relationship..."
- "This paper studies a fundamental problem in learning theory, which has, surprisingly, been left open for several decades."
- "The reviewer really enjoys reading this paper."
- "groundbreaking impact on at least one area of AI/ML"
- "Significant results that complete the landscape of learnability"

**Score 8–10 when**: The paper settles a field-defining question, introduces a new theoretical lens, or provides results that the community will use as a gold standard. These papers often appear as orals at NeurIPS/ICLR.

---

## 7. Key Papers & Expected Citations

### 7.1 PAC Learning Theory Foundations

Papers in learnability theory are expected to cite and situate themselves with respect to:
- Blumer et al. (1989) — VC dimension and PAC learning foundations
- Littlestone (1988) — Online learning, Mistake bound model
- Bartlett & Mendelson (2002) — Rademacher complexity
- Shalev-Shwartz & Ben-David (2014) — "Understanding Machine Learning" textbook
- Hanneke (2016) — Optimal sample complexity of PAC learning
- Bousquet, Hanneke, Moran, van Handel, Yehudayoff (2021) — Proper learning, realizable setting

### 7.2 Kernel Methods

- Scholkopf & Smola (2002) — "Learning with Kernels"
- Caponnetto & De Vito (2007) — Optimal rates for KRR
- Steinwart & Christmann (2008) — "Support Vector Machines"
- Bach (2017) — Breaking the curse of dimensionality with kernel methods

### 7.3 Neural Network Theory

- Jacot, Gabriel, Hongler (2018) — Neural Tangent Kernel
- Du, Zhai, Poczos, Singh (2019) — Gradient descent provably optimizes overparameterized neural networks
- Li, Liang (2018) — On the convergence of gradient descent for DNN
- Allen-Zhu, Li, Song (2019) — A convergence theory for deep learning
- Arora, Du, Hu, Li, Wang (2019) — Fine-grained analysis of overparameterized networks

### 7.4 Average Reward / RL Theory

- Puterman (1994) — "Markov Decision Processes" (foundational)
- Bartlett & Tewari (2009) — REGAL algorithm
- Jin, Shen, Yang, Wang (2021) — Towards tight bounds on sample complexity
- Kearns & Singh (2002) — Near-optimal reinforcement learning

### 7.5 Continual Learning Theory

- Kirkpatrick et al. (2017) — EWC: Elastic Weight Consolidation
- Lopez-Paz & Ranzato (2017) — GEM: Gradient Episodic Memory
- Finn, Abbeel, Levine (2017) — MAML: Model-Agnostic Meta-Learning
- Finn, Rajeswaran, Kakade, Levine (2019) — Online Meta-Learning (FTML)

### 7.6 Domain Generalization Theory

- Arjovsky, Bottou, Gulrajani, Lopez-Paz (2020) — IRM: Invariant Risk Minimization
- Gulrajani & Lopez-Paz (2021) — DomainBed benchmark
- Sun & Saenko (2016) — CORAL: Deep CORAL
- Peters, Janzing, Schölkopf (2017) — Elements of Causal Inference

### 7.7 Operator Learning

- Kovachki et al. (2023) — FNO: Fourier Neural Operator
- Lu et al. (2021) — DeepONet: Deep Operator Networks
- Adcock, Cardenas (2020, 2022) — Holomorphic operator approximation theory

### 7.8 Frequently Cited as Missing Comparisons

Based on reviewer weakness patterns, reviewers frequently call out these missing citations/comparisons:
- Linear models (too often absent as simple baselines in empirical validation)
- "Are Transformers Effective for Time Series Forecasting?" (DLinear/NLinear methods)
- Recent concurrent work on arXiv (reviewers track new preprints)
- SOTA in DomainBed that post-date 2020

---

## 8. Evaluator Quick-Reference Checklist

Use this when scoring a theoretical ML paper:

**Correctness (Must-Pass)**
- [ ] Are the main proofs verifiable and free from logical gaps?
- [ ] Are all assumptions explicitly stated and discussed for plausibility?
- [ ] Do experiments actually validate what the theory claims?

**Novelty**
- [ ] Is the main result non-trivial (not reducible to marginalization/standard results)?
- [ ] Does the paper introduce new techniques, dimensions, or frameworks?
- [ ] Are results non-obvious (e.g., counterintuitive phenomena, tight bounds)?

**Scope and Generality**
- [ ] Does the theory cover a range of settings beyond one toy example?
- [ ] Are there matching lower bounds (for any claims of optimality)?
- [ ] Do the results apply to standard settings (Gaussian may be too restrictive)?

**Relevance**
- [ ] Is there a clear ML problem being solved?
- [ ] Would practitioners or applied ML researchers care about the result?
- [ ] Is the paper connected to contemporary open problems?

**Presentation**
- [ ] Is the paper self-contained (no reliance on concurrent submissions)?
- [ ] Is notation consistently defined and used?
- [ ] Is there a clear narrative guiding the reader through technical material?

**Baselines and Comparison**
- [ ] Are recent (post-2022) baselines included where applicable?
- [ ] Is there a fair comparison to prior bounds or methods?
- [ ] Are missing baselines obvious gaps that reviewers would flag?

**Red Flags (any one of these significantly lowers the score)**
- Paper relies on a concurrent submission for core theory
- Main theorem is equivalent to a known result (marginalization, chain rule)
- Proofs are missing, mis-referenced, or trivially short for hard claims
- No ML connection demonstrated
- Only one synthetic example, no theoretical guarantees
- Paper is not self-contained in notation/background
