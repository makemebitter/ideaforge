# Skill File: Evaluating Research in Reinforcement Learning

**For use by AI judge agents evaluating submissions in the "reinforcement_learning" topic area.**

---

## 1. Topic Overview

### What This Area Covers

Reinforcement learning at ICLR/NeurIPS/ICML spans a very wide range of sub-areas. A paper tagged "reinforcement_learning" may fall into one or more of:

1. **Deep RL methods (model-free)**: Policy gradient methods (PPO, A3C, REINFORCE), Q-learning variants (DQN, SAC, TD3, Rainbow), actor-critic architectures. The classic "algorithms" track.
2. **Model-based RL (MBRL)**: World models (Dreamer/DreamerV3, MBPO, PETS), Dyna-style methods, planning (MCTS, MuZero), latent imagination. Papers that learn a model and use it for planning or value estimation.
3. **Offline RL**: Learning from fixed datasets without environment interaction. Key papers: IQL, TD3+BC, CQL, Decision Transformer, MOPO, COMBO. Challenges: distribution shift, OOD action extrapolation, conservative vs. non-conservative approaches.
4. **Multi-agent RL (MARL)**: Cooperative (QMIX, MAPPO, QPLEX), competitive (OpenSpiel, matrix games), mixed settings. Centralized training + decentralized execution (CTDE) is the standard paradigm.
5. **Exploration**: Bonus-based (ICM, RND, NGU), count-based, curiosity-driven, posterior sampling, optimism-in-face-of-uncertainty. Particularly important for sparse-reward and hard-exploration tasks.
6. **RL theory**: Sample complexity bounds for tabular MDPs, average-reward MDPs, POMDPs, multi-armed bandits, regret analysis, PAC-MDP results, lower bounds.
7. **Hierarchical / goal-conditioned RL**: HRL, option frameworks, UVFA, HER, skill discovery, unsupervised RL (DIAYN, APT, APS).
8. **RL from Human Feedback (RLHF) and LLM alignment**: PPO for LLMs, DPO, GRPO, reward modeling, preference learning, safe RL/RLHF, SCoRe-style self-correction, rejection sampling.
9. **Offline-to-online RL and fine-tuning**: Methods that start from offline data and refine with online interaction.
10. **Reward learning and inverse RL (IRL)**: MaxEnt IRL, AIRL, preference-based reward learning, imitation learning (BC, GAIL, IQL-IL).
11. **Safe RL / constrained RL**: CMDPs, Lagrangian methods, safety filters, constrained policy optimization (CPO), Safe RLHF.
12. **RL + other modalities**: RL for robotics, RL for NLP/code generation, RL for scientific discovery, RL for combinatorial optimization.
13. **Representation learning for RL**: Auxiliary tasks, contrastive methods (SPR, CURL, SGI), video-based pre-training, privileged information, world model representations.
14. **Interpretability and analysis**: Probing RL agents, understanding emergent behaviors, mechanistic interpretability of trained policies.

### Key Challenges That Define the Area

- **Sample efficiency**: RL typically requires millions of environment interactions. Any paper claiming better sample efficiency must show it convincingly.
- **Stability**: RL training is notoriously unstable (deadly triad: bootstrapping + off-policy + function approximation). Papers must address or acknowledge instability.
- **Generalization**: Policies overfit to training environments. Evaluation on held-out environments is increasingly expected.
- **Credit assignment**: Long-horizon rewards make it hard to identify which actions mattered.
- **Exploration vs. exploitation**: Fundamental tension throughout RL.
- **Distribution shift (offline RL)**: Policies trained on fixed datasets face extrapolation errors.
- **Reward specification and hacking**: Reward misspecification is a recurring issue, especially in RLHF.
- **Multi-agent non-stationarity**: Each agent's environment changes as others learn.

### Score Distribution and Acceptance Bar (from 2,636 papers)

- **Mean rating**: 4.76 | **Median**: 4.75 | **Std**: 1.26
- **Acceptance rate**: 81.3% (this topic has an inflated acceptance rate because it includes many workshop papers)
- **Average soundness**: 2.56 | **Average contribution**: 2.37 | **Average presentation**: 2.62
- **Tier breakdown**:
  - Excellent (8–10): 33 papers — the truly outstanding work
  - Good (6–7): 2,227 papers — solid, publishable, clear contributions
  - Borderline (4–5): 5,092 papers — modest contribution, typical accept/reject territory
  - Low (1–3): 2,129 papers — fundamental flaws, insufficient novelty, or incorrect proofs

**Practical calibration guide**:
- **1–2**: Fatal flaws — incorrect theory, results that don't support claims, algorithm nearly identical to prior work, incomprehensible presentation, missing crucial details.
- **3**: Clearly below bar — incremental, limited experiments, significant weaknesses not addressed by rebuttal.
- **4–5**: Borderline — some novelty, some empirical support, but weaknesses in baselines, scope, or rigor. This is the hardest regime to evaluate; outcomes are often one high reviewer and two low reviewers.
- **6**: Solid accept — clear contribution, adequate baselines, well-presented. Not groundbreaking but publishable.
- **7**: Strong accept — novel, well-executed, strong empirical or theoretical results, good ablations.
- **8+**: Outstanding — paradigm-shifting (e.g., DPO, SCoRe for self-correction, DreamerV3), introduces a new benchmark the community will use, or achieves a landmark theoretical result.

---

## 2. What Reviewers Praise (with Real Examples from RL Papers)

### 2.1 Novelty and Conceptual Originality

"Novel" appears 2,034 times in reviewer strength phrases — the #1 signal of a strong paper. But novelty in RL is multi-dimensional:

- **Problem novelty**: Identifying a gap nobody has addressed (e.g., privileged sensing in MBRL, emergent planning in model-free agents).
- **Methodological novelty**: A new algorithmic mechanism with clear motivation (e.g., two-stage RL training to prevent behavior collapse in self-correction).
- **Theoretical novelty**: A new analysis (e.g., span-based complexity bounds for average-reward MDPs that are optimal).
- **Empirical novelty**: Demonstrating for the first time that something works (e.g., SCoRe being the first to achieve genuinely positive self-correction in LLMs).

**Real example — Privileged Sensing Scaffolds RL (8.5, ICLR 2024 Spotlight)**:
> "This paper adds value to the existing body of knowledge, even without introducing novel methods. The proposed method may not be groundbreaking, but it offers a comprehensive examination of this issue from four perspectives: model, value, representation, and exploration."
> "The S3 suite looks like a promising testbed for future privileged MDP work, separate from the algorithmic results of the paper."

Key insight: Even without a fundamentally new algorithm, a paper can be accepted for a comprehensive treatment and a new benchmark.

**Real example — Training LMs to Self-Correct via RL (SCoRe, 8.0, ICLR 2025 Oral)**:
> "First approach for making self-correction really work."
> "The paper's analysis of the failure modes for prior SFT-based methods is very insightful."

Key insight: Being the "first to make X work" (after prior failures) is a very strong contribution.

**Real example — Interpreting Emergent Planning in Model-Free RL (8.0, ICLR 2025 Oral)**:
> "The investigation of emergent planning using a concept-based interpretability approach is original and interesting."
> "The discovery that this is reminiscent of bi-directional search is powerful, and may have implications on the future of model-based RL."

### 2.2 Strong Empirical Results with Comprehensive Baselines

"Baseline" is the most common weakness phrase (4,429 times) and also a major strength phrase (1,613 times). **This is the single most critical experimental requirement in RL.**

Reviewers praise papers that:
- Compare against all relevant SOTA methods, not older/weaker methods
- Use fair comparison protocols (same compute budget, same hyperparameter tuning effort)
- Test on multiple benchmarks spanning diverse difficulties and environment types
- Include the key baselines specific to the RL sub-area (see Section 4)

**Real example — Privileged Sensing Scaffolds RL (8.5)**:
> "Strong empirical performance."
> "Scaffolder still outperforms these model free methods even when the model free methods are given significantly more steps."

**Real example — SCoRe (8.0)**:
> "Very solid experiments and ablation studies along with in-depth analysis providing insights for achieving inference time scaling."

**Contrasting example — CBDQ (3.0, Reject)**:
> Reviewers noted the method was only evaluated on "classic control tasks and simulated driving tasks" — far too limited for a claimed general improvement to Q-learning. Missing comparison to DQN improvements like Rainbow, DDQN, Dueling DQN.

### 2.3 Comprehensive Ablation Studies

"Ablation" appears 1,280 times in reviewer strength phrases and 1,662 times in weakness phrases. Every RL paper that proposes multiple components needs ablations.

Reviewers expect ablations that:
- Remove each proposed component one at a time
- Show that each component is independently necessary
- Test sensitivity to key hyperparameters (e.g., reward shaping coefficient, ensemble size, planning horizon)
- Include analysis of *why* components help (e.g., reducing overestimation, preventing behavior collapse)

**Real example — Privileged Sensing Scaffolds RL (8.5)**:
> "Through ablation study, this work shows different components in the system boost the performance in a different way, providing additional insight on how privileged information can be used in the future work."

**Real example — SCoRe (8.0)**:
> "Very solid experiments and ablation studies along with in-depth analysis."

**Contrasting example — CBDQ (3.0, Reject)**:
> "There is a lack of ablation studies, such as results on more environments regarding the four different smoothing strategies."

### 2.4 Solid Theoretical Foundations

"Solid theoretical" (69x) and related phrases are important in RL, especially for:
- Sample complexity guarantees (tabular RL, bandits)
- Convergence proofs for new algorithms
- Justification for algorithmic design choices (e.g., contraction properties)

Reviewers value:
- Clearly stated assumptions
- Proofs in the appendix that are verifiable (not hand-wavy)
- Matching upper and lower bounds where possible
- Connection between theory and the proposed algorithm

**Real example — Span-Based Sample Complexity (7.8, NeurIPS 2024 Oral)**:
> Oral acceptance for achieving optimal sample complexity for weakly communicating and general average-reward MDPs — a long-open theoretical problem.

**Real example — DPO (7.8, NeurIPS 2023 Oral)**:
> "The paper is grounded theoretically, equivalent to fitting a reparameterized Bradley-Terry model."

**Fatal flaw example — CBDQ (3.0, Reject)**:
> "The statement 'Since the Q is bounded and E[F_t] converges to zero with probability 1...' appears to involve circular reasoning: by using the desired conclusion as an implicit assumption."
> "If the Lemma 4.1 is based on the convex function and the Jensen's inequality? If so, how could a complex neural network be convex?"

Theoretical errors discovered by confident reviewers (confidence 4–5) typically lead to scores of 1–2 and are very hard to recover from in rebuttal.

### 2.5 Well-Written Presentation

"Well-written" appears 864 times in RL strength phrases. Reviewers reward:
- Clear problem formulation with intuitive motivation
- Consistent notation defined upon first use
- Good figures that illustrate the method and results
- Algorithm boxes that are complete and reproducible

**Real example — Privileged Sensing Scaffolds RL (8.5)**:
> "The paper is well written and motivated. The presentation is clear." (multiple reviewers)
> One reviewer gave "4: excellent" for presentation.

**Real example — Interpreting Emergent Planning (8.0)**:
> "The paper is clearly written with relevant information adequately provided."

**Contrasting example — ATD(λ) for MARL (3.0, Reject)**:
> "The paper itself does not look great: the explanations are often quite convolved and difficult to follow."
> "Figure 4 is partly covering the caption of Figure 3."
> "The text in the picture is too small; even when enlarged, it's still unreadable."

### 2.6 Reproducibility and Implementation Details

"Reproducib" appears 308 times in strength phrases for RL papers.

Reviewers strongly value:
- Code release (anonymous GitHub links are common)
- Sufficient hyperparameter details (learning rates, batch sizes, network architectures, random seeds)
- Number of seeds and statistical significance of results
- Compute/runtime comparisons
- Experiment details in appendix (environment descriptions, reward specifications)

**Real example — Privileged Sensing Scaffolds RL (8.5)**:
> "Experiment details are well presented in the Appendix, including runtime and resource comparison over different methods on different environments."

**Contrasting example — CBDQ (3.0, Reject)**:
> "The proposed method also relies on state-space clustering. Yet there are no details on how such a clustering is performed."
> "There are actually two t in the equations, one represents the horizon of the trajectories, and the other represents the updating timeline."

### 2.7 New Benchmarks and Testbeds

Creating a new benchmark is a major contribution that can elevate a paper even if the algorithmic novelty is limited.

**Real example — Privileged Sensing Scaffolds RL (8.5)**:
> The S3 benchmark of 10 diverse simulated robotic tasks was highlighted by multiple reviewers as a standalone contribution.
> "S3 suite looks like a promising testbed for future privileged MDP work, separate from the algorithmic results."

**Real example — Accelerating Goal-Conditioned RL Algorithms (7.5, Spotlight)**:
> The paper contributed benchmark infrastructure, justified even without major algorithmic novelty.

### 2.8 Scalability and Practical Impact

"Scalab" appears 307 times in strength phrases. Reviewers praise papers that demonstrate:
- Working at scale (large action spaces, many agents, large models)
- Deployment potential (robotics, real-world settings)
- Reduced computational requirements vs. prior art

**Real example — SRL: Scaling Distributed RL to Over Ten Thousand Cores (7.5)**:
> Accepted because it demonstrated RL infrastructure that scales to 10,000+ cores — practical engineering with real impact.

---

## 3. What Reviewers Criticize (with Real Examples)

### 3.1 Missing or Weak Baselines (Most Critical Weakness)

"Baseline" is the #1 weakness phrase in RL (4,429 times) — nearly twice as common as any other weakness. This is the single most common reason for rejection.

Papers fail when they:
- Omit recent SOTA methods (especially if they're from the same year or the previous year)
- Use different hyperparameter budgets for their method vs. baselines
- Test only on environments where their method is known to perform well
- Compare against older/weaker baselines while ignoring the current leader

**Real example — NEUBAY (4.67, borderline Accept)**:
> "To the best of my knowledge, there exists a method that unrestricts the planning horizon in offline model-based RL. MBOP and MOPP... share a significant conceptual overlap."
> Reviewers split 4/2/8 — the paper barely made it in, with one reviewer noting missing baselines.

**Real example — CBDQ (3.0, Reject)**:
> Missing comparisons to DQN improvements (Rainbow, DDQN, Dueling DQN) and offline RL baselines (CQL, TD3+BC).

**Real example — TreeDQN (4.7, Reject)**:
> "The experimental section primarily compares TreeDQN with basic methods and lacks extensive benchmarking against a wider range of state-of-the-art approaches."
> "Why not include the tree sizes of SCIP or CPLEX in your figure 1?"

### 3.2 Limited Novelty / Incremental Contribution

"Novelty" (1,629 times) and "incremental" (365 times) are the 2nd and 5th most common weaknesses.

Reviewers flag:
- Methods that are nearly identical to existing algorithms without proper attribution
- Applying known techniques to a new setting without revealing new insights
- "RL + X" papers where the RL component is standard and the contribution is questionable

**Real example — CBDQ (3.0, Reject)**:
> "The proposed method CBDQ, although the authors have provided extensive discussions, is almost identical to the expected Sarsa."
> "The update formula for CBDQ depends on the agent's current policy due to the existence of the belief distribution term b(a|st), which evolves over time."

**Real example — ATD(λ) for MARL (3.0, Reject)**:
> "The core mechanism... is not inherently multi-agent. It can be applied identically in single-agent RL."
> "MARL was chosen primarily because its baselines are easier to improve rather than because the problem requires a multi-agent treatment."

**Counterexample — Second-Order Min-Max (accepted despite critique)**:
> Even when reviewers called results "incremental," a paper can still be accepted if the technical execution is rigorous and the result is non-trivial. The distinction: is the combination straightforward or does it require genuine insight to make work?

### 3.3 Lack of Ablation Studies

"Ablation" is the 2nd most common weakness phrase (1,662 times). Missing ablations is a near-automatic downgrade.

**Real example — CBDQ (3.0, Reject)**:
> "There is a lack of ablation studies, such as results on more environments regarding the four different smoothing strategies. Moreover, Figure 2 does not specify the experimental environment."

**Real example — ATD(λ) for MARL (3.0, Reject)**:
> "Figure 6 shows that the ratio between on-policy and off-policy buffer sizes is a critical hyperparameter with a significant impact. The authors chose 50x as the default ratio based on empirical observation, but did not provide theoretical guidance or sensitivity analysis."

### 3.4 Unclear Methodology / Missing Implementation Details

"Unclear how" (520 times), "unclear whether" (438 times), "unclear why" (166 times), "unclear if" (168 times) are persistent weakness phrases.

Reviewers are frustrated when:
- The algorithm box is incomplete (key steps are missing or ambiguous)
- Hyperparameter choices are not justified
- Notation is used inconsistently
- The connection between theory and implementation is absent

**Real example — CBDQ (3.0, Reject)**:
> "A formally and rigorous definition of the 'subjective belief component' should be proposed."
> "There are actually two t in the equations, one represents the horizon of the trajectories, and the other represents the updating timeline."
> "The definition of letter f and b̃ introduced in Eq. 15 are never given formally."

**Real example — ATD(λ) for MARL (3.0, Reject)**:
> "Please include a clear pseudocode or algorithm box describing the full training loop."
> "I do not see any result for MAPPO in the paper... Then why do you claim you have extended ATD(λ) to this as well?"

**Real example — Interpreting Emergent Planning (8.0, accepted despite critique)**:
> "Could the authors describe in more details how the representation is computed for interventions?"
> Note: Even high-rated papers receive these critiques — the difference is the rest of the paper's quality compensates.

### 3.5 Limited Scope / Generalization Concerns

"Scalab" (684 times), "limited to" (416 times) are common criticisms.

- Papers tested on one environment are systematically downgraded
- Evaluating only on easy benchmarks when hard ones exist raises questions
- MARL papers on saturated benchmarks (old SMACv1 without SMACv2) are penalized

**Real example — Interpreting Emergent Planning (8.0)**:
> "The setting... is ultimately restricted to a single agent architecture (DRC) trained using a single type of model-free RL algorithm (IMPALA) in a single environment type (Sokoban)."
> Note: This was acknowledged but compensated by the paper's conceptual contribution.

**Real example — NEUBAY (4.7, accepted)**:
> "There is a significant disconnect between the method's justification (enabling long-horizon planning) and its empirical results. The algorithm performs poorly on tasks that genuinely require long-horizon planning (e.g., AntMaze large, 0% normalized score)."

**Real example — ATD(λ) for MARL (3.0, Reject)**:
> "The experiments are limited to saturated benchmarks such as SMAC and GRF. Although the authors acknowledge that it cannot be applied well to SMACv2, that is a significant limitation as it is recently a more standard benchmark than SMACv1."

### 3.6 Flawed or Circular Theoretical Proofs

This is a **fatal flaw** that produces very low scores (1–2). A confident reviewer who discovers a proof error will almost certainly recommend rejection.

**Real example — CBDQ (3.0, Reject)**:
> "The statement... appears to involve circular reasoning: by using the desired conclusion as an implicit assumption."
> "The proof assumes that the belief distribution places (1−δt) mass on the maximal state of Q*, yet there is no accompanying explanation or validation for this assumption."

**Real example — TreeDQN (4.7, Reject)**:
> "The definition of value function (2) is not correct. The value function (excluding optimal value function) should be policy-dependent."
> "The contraction property can be a justification for value iteration methods. However, using it as theoretical backing for Q-learning methods is fragile."

**Pattern**: Papers with theoretical proofs that have flaws discovered by confident reviewers (confidence ≥ 3) are almost always rejected regardless of their empirical results.

### 3.7 Fair Comparison / Computational Overhead Issues

"Fair comparison" appears 184 times as a weakness.

- If your method uses 2x the compute (e.g., two world models, large ensembles), show that the gains justify the overhead
- Compare at the same sample budget (transitions seen, not gradient steps)
- Report wall-clock time, not just environment steps

**Real example — Privileged Sensing Scaffolds RL (8.5)**:
> "In addition to the number of frames being the x-axis for figure 6, please also include one where x-axis is the wall-clock time."
> "It would still benefit from evaluating extra existing benchmarks, just for reference."

**Real example — NEUBAY (4.7, accepted)**:
> "NEUBAY uses a larger ensemble size (N=100) in the dynamics model compared to previous methods, which seems to introduce additional computational overhead."
> "High architectural complexity, integrating deep ensembles, LRU-based recurrent encoders, specific context-handling mechanisms."

### 3.8 Overclaiming / Insufficient Evidence for Claims

Reviewers penalize papers that make claims their experiments don't support.

**Real example — Interpreting Emergent Planning (8.0)**:
> "The paper often tends to be inclined towards a positive answer that DRC agents can plan, and omits to discuss alternative explanations for the observed behaviors."
> "The statements in lines 373-376 or 425-427 are not sharp implications as stated in the text."

**Real example — CBDQ (3.0, Reject)**:
> "The authors claim that CBDQ is off-policy while Sarsa is on-policy. However, the update formula for CBDQ depends on the agent's current policy due to the existence of the belief distribution term."

---

## 4. Required Baselines and Metrics by Sub-Area

### 4.1 Deep RL / Model-Free Methods

**Required baselines**:
- For value-based: DQN, DDQN, Dueling DQN, Rainbow, C51; for continuous control: SAC, TD3
- For policy gradient: PPO, A2C, TRPO (for on-policy methods)
- For actor-critic: SAC (continuous), PPO (discrete/continuous hybrid)
- Any other strong recent method in the same sub-area

**Standard benchmarks**:
- Atari 100k (sample efficiency) and Atari 57 (final performance) for discrete control
- MuJoCo/DMControl (HalfCheetah, Ant, Humanoid, Walker2d, Hopper) for continuous control
- Procgen for generalization
- NetHack, MiniHack, BabyAI for hard exploration / long-horizon

**Expected metrics**:
- Learning curves (performance vs. env steps, not gradient steps)
- Final performance after N steps ± std dev across 5–10 seeds
- Sample efficiency (steps to reach a target performance level)

### 4.2 Model-Based RL

**Required baselines**:
- DreamerV3 (the current MBRL flagship) — must compare if using world models
- MBPO, PETS for continuous control
- MuZero/EfficientZero for discrete domains
- TD-MPC2 for general continuous control
- The model-free SOTA (e.g., SAC) as a reference point

**Standard benchmarks**:
- DMControl 100k / 500k benchmarks for sample efficiency
- Atari 100k
- S3 or custom robotics benchmarks with privileged sensing (if applicable)
- AntMaze for long-horizon planning

**Expected metrics**:
- Performance vs. environment steps (sample efficiency is critical here)
- Wall-clock time comparison (MBRL often trains faster per step but slower per gradient update)

### 4.3 Offline RL

**Required baselines**:
- BC (behavioral cloning) — always include this floor
- TD3+BC, IQL, CQL (the three workhorses)
- MOPO, COMBO (for model-based offline RL)
- Decision Transformer (for sequence modeling approaches)
- Recent SOTA from D4RL leaderboard

**Standard benchmarks**:
- D4RL: MuJoCo (HalfCheetah, Hopper, Walker2d) with all three dataset levels (random, medium, medium-expert)
- D4RL: AntMaze (for long-horizon / sparse reward)
- NeoRL for real-world-like datasets
- ROBOMIMIC for robotics manipulation

**Expected metrics**:
- Normalized score on D4RL (normalized relative to expert policy)
- Report all dataset variants, not just the favorable ones
- Offline training time and online fine-tuning cost (if applicable)

### 4.4 Multi-Agent RL (MARL)

**Required baselines**:
- For cooperative: QMIX, MAPPO, QPLEX, FACMAC (for continuous), HAPPO
- IQL (independent Q-learning) as a decentralized baseline
- CTDE framework must be used and compared against

**Standard benchmarks**:
- SMAC (StarCraft Multi-Agent Challenge) — but SMACv2 is now preferred over the original
- Google Research Football (GRF)
- Multi-agent MuJoCo
- Hanabi (for communication)
- Avoid presenting only SMACv1 without SMACv2 (reviewers notice this)

**Expected metrics**:
- Win rate over 5+ seeds with standard error
- Convergence speed (steps to reach target win rate)
- Scalability results: does performance hold as number of agents grows?

### 4.5 RL Theory

**Required elements**:
- Clear table comparing your complexity bounds to prior work
- Explicit constants (not just O(·) notation) when relevant
- Discussion of tightness: is your upper bound matched by a lower bound?
- Statement of assumptions with discussion of whether they are standard

**Sub-area specifics**:
- Tabular RL: Compare against UCBVI, EULER, RLSVI; show regret bounds
- Average-reward MDP: Compare against span-based bounds (Fruit et al., Jia et al.)
- Offline RL theory: Sample complexity for policy evaluation and improvement
- Bandits: Compare against UCB, Thompson sampling bounds
- Q-learning convergence: Compare sample complexity against standard Q-learning bounds

**Common fatal errors**:
- Circular reasoning in convergence proofs
- Applying Jensen's inequality to non-convex functions (neural networks are not convex)
- Confusing policy-dependent and policy-independent value functions
- Ignoring the dependency on the time horizon T in bounds

### 4.6 Exploration

**Required baselines**:
- ICM (Pathak et al.), RND (Burda et al.) — the classic intrinsic motivation methods
- NGU, Agent57 for hard-exploration Atari
- Count-based methods when applicable
- GO-Explore for procedurally generated environments

**Standard benchmarks**:
- Hard-exploration Atari: Montezuma's Revenge, Pitfall, PrivateEye
- Minigrid/BabyAI for goal-conditioned sparse reward
- Procgen for generalization with exploration

### 4.7 RLHF / LLM Alignment

**Required baselines**:
- SFT (supervised fine-tuning) — always the floor
- PPO with reward model (the RLHF standard)
- DPO (if doing preference learning without explicit RL)
- GRPO, RewardedSoups (if doing reward-based optimization)
- REST-EM, self-play (if doing self-improvement)

**Standard benchmarks**:
- MATH benchmark and subsets (AIME-level problems for harder evaluation)
- HumanEval, MBPP (for code)
- MT-Bench, AlpacaEval (for general instruction following)
- Evaluations on both seen and unseen difficulty levels

**Expected for SCoRe-type papers**:
- Comparison with single-turn RL baselines
- Edit-distance-based analysis of self-correction behavior
- Analysis on held-out problems not in the training distribution

### 4.8 Safe RL

**Required baselines**:
- CPO (Constrained Policy Optimization)
- Lagrangian-augmented PPO (LA-PPO)
- PCPO, P3O
- PPO without safety constraints as a reference point

**Standard benchmarks**:
- Safety Gym (MuJoCo-based constrained control)
- CMDP benchmarks with explicit cost constraints
- Metrics: both reward performance AND constraint satisfaction rate

---

## 5. Common Failure Patterns to Watch For

### Pattern 1: The Identical-to-Prior-Work Problem
**Description**: An algorithm is presented as novel but is nearly identical to a well-known algorithm. Often the paper uses different framing or notation to obscure the similarity.

**How to detect**:
- When the algorithm "looks like" a known method (SARSA, Q-learning, PPO with modification), check whether the key equations reduce to the known method under simple assumptions.
- Check whether the claimed advantages (off-policy, convergence guarantees) are already properties of the prior method.

**Example from data**:
- CBDQ was essentially Expected SARSA with a differently-parameterized action distribution.
- ATD(λ) for MARL was essentially a single-agent density ratio technique applied to MARL critics without any MARL-specific insight.

**Score impact**: Papers with this pattern typically score 1–3.

---

### Pattern 2: The Saturated Benchmark Problem
**Description**: A paper shows strong results on benchmarks that are already well-solved or outdated, while avoiding newer, harder benchmarks where its limitations would be exposed.

**How to detect**:
- Are results only on classic control (CartPole, LunarLander, MountainCar)? This is insufficient for an RL methods paper in 2024+.
- For MARL: Only SMACv1 results without SMACv2?
- For offline RL: Only medium-quality D4RL datasets, skipping the harder random or sparse settings?
- For LLM RL: Only simple math/code benchmarks, avoiding competition-level problems?

**Example from data**:
- CBDQ tested only on classic control and simulated driving, missing MuJoCo, DMControl, and offline benchmarks.
- ATD(λ) explicitly excluded SMACv2 "because it cannot be applied well there."

**Score impact**: Papers with this pattern typically score 3–5.

---

### Pattern 3: The Missing-MARL-Insight Problem
**Description**: A MARL paper proposes a method that is entirely general to single-agent RL, then applies it to MARL without any insight about why MARL specifically benefits or requires the approach.

**How to detect**:
- Does the method use any MARL-specific structure (factorized policies, joint action spaces, communication)?
- Would the same method work identically in single-agent RL?
- Is MARL used purely because the baselines are easier to improve?

**Example from data**:
- ATD(λ): "The core mechanism is not inherently multi-agent. It can be applied identically in single-agent RL."

**Score impact**: Papers with this pattern typically score 2–4.

---

### Pattern 4: The Disconnect Between Motivation and Results
**Description**: The paper claims its method is important for reason X (e.g., long-horizon planning, rare-event robustness), but the empirical results don't validate X — they only show improvement on standard benchmarks where X doesn't matter.

**How to detect**:
- Does the evaluation specifically test the scenario that motivated the method?
- If the paper claims to enable "long-horizon planning," do results on AntMaze or sparse-reward tasks confirm this?
- If the paper claims better exploration, does it show results on hard-exploration benchmarks?

**Example from data**:
- NEUBAY: "There is a significant disconnect between the method's justification (enabling long-horizon planning) and its empirical results. The algorithm performs poorly on tasks that genuinely require long-horizon planning (AntMaze large, 0% normalized score)."

**Score impact**: This causes a split in reviewers; borderline (4–6). One reviewer may give 8 for the novelty, another gives 2 for the disconnect.

---

### Pattern 5: The Proof Error Pattern
**Description**: The paper has a convergence theorem or sample complexity bound with a subtle but fatal logical error, often discovered only by a confident (confidence 4–5) reviewer.

**Common errors**:
- Circular reasoning (using the result being proven as an assumption in the proof)
- Applying convexity tools to non-convex functions
- Conflating policy-dependent and policy-independent quantities
- Convergence proofs that work for the tabular case but don't hold with function approximation
- Bounds that depend on the time horizon T in a way that makes the bound trivially loose

**Example from data**:
- CBDQ: "Unjustified assumption of belief distribution" and "Flawed use of assumption" where the proof used its conclusion as a premise.
- TreeDQN: Value function incorrectly defined as policy-independent, undermining all downstream analysis.

**Score impact**: 1–2 from the reviewer who discovers the error; average drops to 2–4.

---

### Pattern 6: The Insufficient Reproducibility Pattern
**Description**: Missing implementation details that prevent replication — no code, ambiguous algorithm descriptions, hyperparameters not reported.

**How to detect**:
- Is the algorithm box complete? Can you implement it from the paper alone?
- Are learning rates, batch sizes, network architectures reported?
- How many seeds were used? Are error bars shown?
- Are environment details specified (observation spaces, reward scales)?

**Example from data**:
- CBDQ: Key hyperparameter N (cluster count) never analyzed; update rules inconsistent between equation and algorithm.
- ATD(λ): "I do not see any result for MAPPO in the paper... Then why do you claim you have extended your ATD(λ) to this as well?"

**Score impact**: Moderate (1–2 point deduction); rarely fatal alone, but compounds with other weaknesses.

---

### Pattern 7: The Reviewer-Split Pattern (Borderline Papers)
**Description**: One reviewer gives a high score (7–8) and others give low scores (2–4), leading to an average of 4–5. This happens when:
- The idea is genuinely novel but execution is flawed
- The paper has a niche but valid contribution
- One reviewer is an expert in the specific sub-area and sees deep value others miss

**Example from data**:
- NEUBAY: Scores 4/2/8 — one expert reviewer loved the departure from conservatism (8), one saw missing baselines (4), one saw poor AntMaze results (2). Ultimately accepted.
- TreeDQN: Scores 6/3/5 — one reviewer liked the RL-for-combinatorial-optimization framing, others doubted theoretical correctness.

**Evaluation strategy**: In these cases, focus on whether the core technical claims are sound (not just interesting), whether the empirical results are fair and sufficient, and whether the weaknesses are addressable in revision.

---

## 6. Evaluation Rubric for RL Papers

### 6.1 Dimension-by-Dimension Guidance

**Soundness** (1–4 scale):
- **4 (Excellent)**: No theoretical errors, experiments are methodologically sound, claims are fully supported by evidence.
- **3 (Good)**: Minor methodological issues (e.g., could use more seeds), but core claims are supported.
- **2 (Fair)**: Significant issues — proof gaps, unfair comparisons, missing key ablations.
- **1 (Poor)**: Fundamental errors — incorrect proofs, results that don't support claims, methodology is broken.

**Contribution** (1–4 scale):
- **4 (Excellent)**: New paradigm, new benchmark the community will use, or a result that solves a long-open problem.
- **3 (Good)**: Meaningful new algorithm or analysis with clear improvement over prior work.
- **2 (Fair)**: Incremental but genuine — combines ideas in a useful way.
- **1 (Poor)**: No genuine novelty — application of known methods without insight.

**Presentation** (1–4 scale):
- **4 (Excellent)**: Beautifully written, perfect notation, figures make the method immediately clear.
- **3 (Good)**: Clear and well-organized; minor issues with notation or figure quality.
- **2 (Fair)**: Hard to follow in places; notation is inconsistent; figures are confusing.
- **1 (Poor)**: Very difficult to understand; missing definitions; figures illegible.

### 6.2 How Sub-Area Affects Expectations

**Model-free deep RL** papers face the highest empirical bar. Reviewers will check: Is this tested on MuJoCo AND Atari (or similar dual-domain evaluation)? Does it beat SAC/PPO/TD3 consistently?

**RL theory** papers face the highest soundness bar. A clean theoretical result with limited experiments can score 7+ if the result is genuinely new and non-trivial. But any proof error found by a confident reviewer is typically fatal.

**Offline RL** papers must include D4RL benchmarks at minimum. Papers that only test on one dataset type (e.g., only medium-expert) are penalized for cherry-picking.

**MARL** papers must now use SMACv2 and/or multi-agent MuJoCo. Papers using only the old SMAC maps are considered to be on saturated benchmarks.

**RLHF / LLM alignment** papers face a rapidly moving target for baselines — a paper that omits the most recent DPO variant or GRPO-based method may be penalized even if that method was published months before submission.

**Safe RL** papers must demonstrate both reward performance AND constraint satisfaction — showing one without the other is insufficient.

### 6.3 How to Handle Competing Claims About Novelty

When a reviewer claims "this is just X from prior work," evaluate:
1. **Is the technical overlap substantive or superficial?** (Same name ≠ same algorithm)
2. **Does the paper acknowledge and differentiate from the prior work?** (Missing citation is worse than a cited distinction)
3. **Does the proposed method provide something new in theory, practice, or understanding?**
4. **Is the prior work actually in the RL literature or from a related area?** (Bringing insights from other fields can be novel)

### 6.4 Red Flags That Lower Score Regardless of Other Qualities

1. **Results are only on easy/toy benchmarks** (classic control only, 2D grid worlds only) for a 2024+ paper → deduct 1–2 points
2. **Proof errors discovered by a confident reviewer** → likely score 1–2 regardless of empirical results
3. **Missing comparison to the most closely related method** (especially if it's the natural competitor) → deduct 1–2 points
4. **Algorithm box is incomplete or inconsistent with the main text** → deduct 1 point
5. **Claims are not supported by experiments** (e.g., claims long-horizon but doesn't test on long-horizon tasks) → deduct 1–2 points
6. **No ablation studies** for a multi-component method → deduct 1 point
7. **Zero seeds or no error bars** → deduct 1 point (major concern)
8. **Method not compared to the current state-of-the-art from the last 2 years** → deduct 1–2 points

### 6.5 Green Flags That Raise Score

1. **New benchmark or testbed** that fills a gap in the community → add 1 point
2. **Open-sourced code** with reproducible experiments → add 0.5 points
3. **Failure mode analysis** (understanding *why* prior methods fail before proposing a fix) → add 0.5–1 point
4. **Theory that explains an empirical phenomenon** (or vice versa) → add 1 point
5. **Results on real-world systems** (hardware robots, production LLMs) → add 1 point
6. **Statistical rigor** (many seeds, confidence intervals, significance tests) → add 0.5 points
7. **Broad scope** (tested on many environments spanning different domains) → add 0.5–1 point

---

## 7. Topic-Specific Nuances

### 7.1 RL for LLMs: What's Expected in 2024–2026

The RLHF/LLM alignment sub-area has exploded. Key nuances:

- **Reproducibility issues**: Many papers train on closed models (e.g., Gemini, GPT-4). Reviewers consistently ask for open-source model validation (Llama, Mistral).
- **SCoRe taught us**: Identifying the failure modes of prior methods (distribution shift, behavior collapse) and showing these are real empirically is a major contribution — not just proposing a fix.
- **GRPO vs. PPO**: In 2025+, papers that use PPO for LLM RL without justifying over GRPO/RLOO may be asked about this.
- **The "positive self-correction" result**: SCoRe was groundbreaking because prior methods couldn't demonstrate genuine self-correction. Claims of LLM improvement must show the improvement is real (not just the model using a different strategy, e.g., giving a wrong first answer then correcting).

### 7.2 Reward Hacking / Reward Model Failures

As RL for LLMs matures, reviewers increasingly ask:
- Does the method address reward hacking?
- Is the reward model overfit to the training distribution?
- Does "improved performance on reward model" translate to real improvement?

### 7.3 Offline RL: The Conservatism Debate

The tension between conservative (CQL-style, pessimistic) and non-conservative approaches is an active research thread. Key points:
- Conservative methods are safer but potentially sub-optimal
- Non-conservative approaches (like NEUBAY) are more ambitious but must show they don't blow up on harder tasks
- A paper that challenges conservatism must test on the benchmarks where conservatism is most important (AntMaze, sparse-reward datasets)

### 7.4 MBRL: The Sample Efficiency Question

Model-based RL papers claim sample efficiency as a primary motivation. But:
- Wall-clock time often increases (more computation per step)
- Sample efficiency vs. compute-efficiency is a real trade-off
- Papers must report both environment steps and compute cost

### 7.5 MARL: What "CTDE" Means for Evaluation

Centralized Training, Decentralized Execution (CTDE) is the standard paradigm. Papers should:
- Clearly state whether they use centralized state during training
- Compare against methods with similar information access
- Explain whether the centralized state is available at test time

---

## 8. Distinguishing "Accept" from "Reject" at the Margin

At the borderline (4–5 range), the decision often hinges on one or two factors:

**Accept signals**:
1. The core idea is genuinely novel even if execution is imperfect
2. The experiments, while incomplete, do show a real improvement
3. The weaknesses are addressable in a revision (missing ablations can be added; missing baselines can be run)
4. The paper introduces a new benchmark or identifies a new problem formulation
5. At least one reviewer with high confidence (4–5) strongly advocates for acceptance

**Reject signals**:
1. The algorithm is demonstrably identical or nearly identical to prior work without acknowledgment
2. Theoretical proofs have fatal errors that can't be fixed without reconceiving the approach
3. The experimental results don't support the claims (not just incomplete — actively misleading)
4. The paper is missing the core comparison that would validate the method (e.g., an offline RL paper without any D4RL results)
5. The presentation is so poor that reviewers cannot evaluate the contribution

**The key question**: "If the authors ran the missing experiments and they came out positive, would the paper be clearly above the bar?" If yes, the paper likely belongs in the borderline-accept zone. If the issue is fundamental (wrong claim, proof error, no novelty), the missing experiments can't save it.

---

## 9. Scoring Quick Reference

| Rating | Meaning | Typical Profile |
|--------|---------|----------------|
| 1–2 | Strong reject | Fatal proof errors, no novelty, claims contradicted by evidence |
| 3 | Reject | Incremental, limited experiments, significant unaddressed weaknesses |
| 4 | Weak reject | Some novelty, but missing key baselines or experiments; borderline |
| 5 | Weak accept | Novel contribution, modest empirical support, some weaknesses remain |
| 6 | Accept | Clear contribution, adequate baselines, well-presented |
| 7 | Strong accept | Novel, well-executed, strong empirical or theoretical results |
| 8 | Very strong accept | Landmark contribution, new benchmark or paradigm |
| 9–10 | Outstanding | Oral-level: reshapes the field or community will immediately build on it |

**Calibration**: Given the statistics (mean=4.76, std=1.26), a 6 is meaningfully above average. A 7 places you in the top ~20%. An 8+ is in the top ~1%.

---

## 10. Example Evaluations with Reasoning

### Example 1: High-Quality Paper (Score 8)
**"Training Language Models to Self-Correct via Reinforcement Learning" (SCoRe)**

*Strengths*: First to achieve genuinely positive self-correction (novel + validated), excellent failure mode analysis (distribution shift, behavior collapse), two-stage RL training is well-motivated with ablations.

*Weaknesses*: Only evaluated on private Gemini models (reproducibility), limited to math and code, only 2 self-correction attempts.

*Reasoning*: The "first to make X work" framing is compelling and validated. The method addresses a real problem with both theoretical motivation and empirical evidence. Weaknesses are real but not fatal — the core claim holds.

**Score: 8**

---

### Example 2: Borderline Reject (Score 3–4)
**"Mimicking Human Intuition: Cognitive Belief-Driven Q-Learning" (CBDQ)**

*Strengths*: Tries to address over-estimation in Q-learning (valid goal), experiments show improvement on tested environments.

*Weaknesses*: Algorithm reduces to Expected SARSA under simple assumptions (novelty issue), theoretical proof has circular reasoning and unjustified assumptions, only tested on classic control and driving (narrow scope), no ablations for key components, inconsistent notation throughout.

*Reasoning*: The combination of (1) near-identical to prior work, (2) flawed proof, (3) narrow evaluation, and (4) missing ablations constitutes a clear rejection. No single issue is isolated — they compound.

**Score: 3**

---

### Example 3: Borderline Accept (Score 4–5)
**"Long-Horizon Model-Based Offline RL Without Conservatism" (NEUBAY)**

*Strengths*: Novel framing (neutral Bayesian vs. conservative), adaptive planning horizon is a good idea, comprehensive comparison against many baselines, strong ablation studies.

*Weaknesses*: Poor AntMaze results (0% on large) contradicts the long-horizon motivation, high architectural complexity (N=100 ensemble, LRU encoder), conceptual overlap with MBOP/MOPP.

*Reasoning*: Reviewers split 4/2/8. The paper was accepted because (a) one reviewer found the departure from conservatism genuinely valuable and (b) the experiments were comprehensive even if not perfect on all tasks. At the margin, the novel framing and broad evaluation tipped it toward acceptance.

**Score: 5** (borderline accept)

---

*End of Skill File: reinforcement_learning*
