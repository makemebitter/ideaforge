# GNN Judge Skill File: Graph Neural Networks

**Topic:** graph_neural_networks
**Based on:** 858 papers, 709 accepted (82.6% acceptance rate)
**Rating distribution:** mean=4.79, median=4.75, std=1.24, range=[1.33, 8.0]
**Skill file compiled:** 2026-03-14

---

## 1. Overview of GNN Research Landscape

Graph Neural Networks (GNNs) constitute one of the most active and theoretically rich areas of deep learning. The field spans an enormous range from foundational theory to domain-specific applications. A judge evaluating GNN papers must be fluent across many subfields, since papers frequently combine theory with application or import ideas from adjacent areas like spectral graph theory, combinatorics, and chemistry.

### Major Subfields

**GNN Expressiveness and Theory**
The canonical question is whether a GNN can distinguish non-isomorphic graphs. This line is anchored to the Weisfeiler-Lehman (WL) hierarchy and its higher-order variants (k-WL). Key directions include: logical characterizations of expressiveness (connecting GNNs to fragments of first-order or counting logic), homomorphism expressivity, subgraph GNNs that enumerate neighborhoods beyond 1-hop, and quantitative frameworks for expressiveness (beyond binary WL-equivalent vs. not). This is a mature subfield where novelty requires pushing beyond well-known results.

**Message Passing Neural Networks (MPNNs)**
The core architectural framework. Research here concerns aggregation functions (sum vs. mean vs. max vs. learnable), depth and oversmoothing, oversquashing (information bottlenecks through narrow graph cuts), normalization, and skip connections. Work in this area is often incremental and must be carefully distinguished from a long list of prior methods.

**Scalable GNNs**
Applying GNNs to graphs with millions or billions of nodes/edges. Approaches include neighborhood sampling (GraphSAGE-style), layer-wise sampling, mini-batch training, graph distillation (GNN-to-MLP), precomputed propagation (SGC-style), and scalable transformers. Scalability claims require empirical validation on genuinely large graphs (OGB-products, OGB-papers, MAG240M-scale), not just medium-sized datasets.

**Graph Transformers**
Transformers applied to graphs, using attention as a global (or sparse) aggregation mechanism. Key design choices: positional encodings (Laplacian eigenvectors, random walk encodings, structural encodings), sparse attention patterns, how to handle graph structure in the attention bias, and computational complexity. This is now a crowded area; new graph transformers must show genuine architectural innovation or strong empirical gains.

**GNNs for Molecules and Chemistry**
Perhaps the largest application domain. Includes molecular property prediction (QM9, MoleculeNet benchmarks), 3D molecular geometry (force fields, conformation generation), protein structure, drug-target interaction, and retrosynthesis. Equivariant GNNs (E(n)-equivariant, SE(3)/SO(3)-equivariant) are central here. This subfield has its own benchmark conventions and strong baselines (SchNet, DimeNet, SphereNet, Equiformer, NequIP, MACE, etc.).

**Graph Learning for PDEs and Physics**
Using GNNs on irregular meshes to solve partial differential equations. Pioneered by MeshGraphNets (DeepMind). Physics-encoding (conservation laws, symmetries, Laplace-Beltrami operators) is highly valued. Key benchmark: outperforming MeshGraphNets is a meaningful signal.

**Temporal/Dynamic Graphs**
Graphs that evolve over time. Two paradigms: discrete-time (snapshots) and continuous-time (event streams, TGN-style). Applications include traffic forecasting, social network evolution, financial fraud. Key challenge: modeling both temporal and structural dependencies without computational explosion.

**Knowledge Graphs**
Relational learning over (entity, relation, entity) triples. Covers link prediction, rule learning, embedding methods (TransE, RotatE, etc.) adapted with GNN-style propagation. Applications in question answering, recommendation, and biomedical knowledge bases.

**GNN Robustness and Adversarial**
Attacks on GNNs (node injection, edge perturbation, feature poisoning) and defenses. Certifiable robustness is valued; empirical robustness claims must survive adaptive attacks. Related area: out-of-distribution generalization on graphs.

**Heterogeneous and Hypergraph Learning**
Graphs with multiple node or edge types (heterogeneous graphs), or higher-order relations (hypergraphs). Applications in recommendation systems, citation networks, biomedical networks.

**GNN Interpretability and Explainability**
Methods for explaining GNN predictions (GNNExplainer, PGExplainer, etc.), counterfactual explanations, self-interpretable GNNs. A growing area with its own benchmark challenges.

**GNN Applications: Beyond Molecules**
Traffic, weather forecasting, brain networks, combinatorial optimization, program analysis, hardware design, recommendation systems. These application papers are judged on both the GNN contribution and domain relevance.

---

## 2. Calibration Guide

### Understanding the Rating Scale

The GNN area shows a right-skewed acceptance distribution. The mean accepted paper scores approximately 4.79 with median 4.75. The calibration table below maps abstract ratings to concrete quality levels:

| Rating | Label | What it means in practice |
|--------|-------|---------------------------|
| 8-10 | Excellent | Oral/Spotlight candidate; fundamental contribution; will be widely cited; clear correctness; strong theory or overwhelming empirical evidence |
| 6-7 | Good | Solid accepted paper; novel contribution; adequate baselines; some limitations but not fatal |
| 4-5 | Borderline | Mixed reviews; partial novelty; experimental gaps; incremental over prior work; often splits reviewers |
| 1-3 | Low/Reject | Fatal flaws: missing baselines, incorrect claims, negligible novelty, reproducibility failures |

**Important calibration facts from this dataset:**
- 82.6% acceptance rate is high because this is a curated dataset of GNN papers from top venues (ICLR, NeurIPS); this does NOT mean 82.6% of GNN submissions get accepted. The actual venue acceptance rate is ~25-35%.
- An average rating of 5 is borderline and could go either way.
- An average rating of 6 is solidly above threshold.
- Ratings of 8 are rare (16 papers in the "excellent" tier in this dataset out of 858) and require genuine significance.
- Most accepted papers cluster between 5-7 (the "borderline" and "good" tiers together).

### Reviewer Dynamics

GNN reviewers are particularly attentive to:
1. **Baselines** (appears 1,399 times in weaknesses vs. 392 in strengths) — the single most common failure mode
2. **Novelty** (562 times in weaknesses) — incremental work is frequently penalized
3. **Ablations** (468 in weaknesses) — design choices must be validated
4. **Scalability** (338 in weaknesses) — claims about scalability require appropriate experiments
5. **Reproducibility** (135 in weaknesses) — missing code, hyperparameters, or computational details

When these appear as strengths, the paper is doing well. When they appear as weaknesses (and they do far more often), the paper is in trouble.

---

## 3. What Excellent GNN Papers Look Like

Based on the 8.0-rated papers reviewed (all oral/spotlight decisions), here is a synthesis of what separates truly excellent GNN work:

### Case Study 1: "Towards a Complete Logical Framework for GNN Expressiveness" (rating=8.0, ICLR 2025 Oral)

This paper achieved the highest tier by:
- **Unifying multiple prior frameworks** into a single theoretical lens (first-order logic characterization of GNN expressiveness)
- **Classifying existing models systematically** using the proposed framework (applied to 8 GNN variants)
- **Connecting to multiple existing expressivity measures** (WL hierarchy, homomorphism expressivity) — cross-linking different research threads
- **Subsumes prior work** rather than merely adding to it

Key reviewer quotes: "The contribution is significant and will be of interest to the ICLR community. It unifies existing work on logical expressivity of GNNs." The paper earned high contribution scores (3-4) despite some presentation concerns.

**The lesson:** Unifying, systematic theoretical work that connects previously disparate results is rated at the top. The bar for the theory being correct and general is extremely high.

### Case Study 2: "On the Holder Stability of Multiset and Graph Neural Networks" (rating=8.0, ICLR 2025 Oral)

This paper achieved top scores by:
- **Identifying a novel gap**: that WL-expressive MPNNs can still "squash" embeddings of distinguishable graphs
- **Proposing a new concept** (lower-Holder in expectation) that is precisely defined, measurable, and connected to practical performance
- **Deriving concrete results** for a table of common architectures — actionable theory
- **Proposing new architectures** (AdaptMPNN, SortMPNN) that provably fix the identified problem
- **Empirical validation** that adversarial graph pairs (epsilon-trees) that break standard MPNNs are handled by the new architectures
- **First claim of its kind**: "SortMPNN is the first MPNN with both upper and lower Lipschitz guarantees"

The paper was accepted despite:
- Some marginal experimental benefits
- Typos and rushed presentation
- Incomplete theoretical analysis of AdaptMPNN

**The lesson:** A novel concept that is theoretically grounded, connects to practical separability, AND motivates concrete architectural improvements can achieve top scores even with presentation imperfections.

### Case Study 3: "PhyMPGN: Physics-encoded Message Passing Graph Network" (rating=8.0, ICLR 2025 Spotlight)

This paper achieved top scores by:
- **Beating a strong industry baseline** (MeshGraphNets by DeepMind) by over 50%
- **Physics integration is principled**: learnable Laplace-Beltrami operator, not ad-hoc
- **Generalization beyond training**: to different Reynolds numbers, initial conditions, boundary conditions
- **Simple and compatible**: designed to integrate with other GNN-based methods
- **Thorough ablation studies** validating the Laplace block and boundary condition padding separately

Note: one reviewer gave a 6, citing novelty concerns about the Laplace-GNN connection and boundary condition handling; two others gave 8 and 10. The average was 8.0. Strong empirical results can outweigh moderate novelty when baselines are genuinely strong.

**The lesson:** Domain application papers need to (a) beat meaningful baselines by a large margin, (b) have principled (not ad-hoc) technical contributions, and (c) demonstrate robustness and generalization.

### Case Study 4: "Online GNN Evaluation Under Test-time Graph Distribution Shifts" (rating=8.0, ICLR 2024 Spotlight)

This paper achieved top scores by:
- **Identifying a new problem**: online GNN evaluation without ground-truth labels under distribution shift
- **Novel metric (LEBED)** grounded in learning theory: measures parameter-space discrepancy, not just output discrepancy
- **Diverse experimental validation**: node feature shifts, domain shifts, temporal shifts — not just one type of distribution shift
- **Well-structured and easy to understand** — presentation quality contributed to high ratings
- **Correlation with ground-truth error** is the right evaluation criterion for the metric

**The lesson:** A clearly new problem framing, with a clean metric that has theoretical motivation and diverse empirical validation, is a recipe for top papers even in niche areas.

### Shared Characteristics of 8.0 Papers

1. **Novel framing or concept** that reshapes how the community thinks about something
2. **Connections to prior work** that are explicit — these papers do not ignore related work, they engage with it and show where they go beyond
3. **Either theoretical completeness OR overwhelming empirical results** — rarely both, but one is essential
4. **At least one "first" or "only" claim** that is defensible: first framework to do X, first architecture with property Y
5. **Diversity in validation** — multiple datasets, multiple shifts, multiple architectures
6. **Principled design** — why each component exists, with ablation confirming it

---

## 4. Common Failure Modes

Based on low-rated papers (ratings 3-5), rejected papers, and the weakness phrase analysis, the following failure modes are pervasive in the GNN literature:

### Failure Mode 1: Missing or Weak Baselines (by far the most common)

"The experiments seem weak, the experimental results are not competitive, and the selected baselines are not state-of-the-art." (j56A1HUTQS, rating=4.67, rejected)

Specific manifestations:
- Comparing against methods from 2019-2021 when 2022-2024 methods exist on the same benchmark
- Not comparing against the directly competing method that addresses the same problem (e.g., a paper on scalable GNNs that misses GraphSAINT, SIGN, or GAMLP)
- Using OOM failures of baselines as a substitute for fair comparison (valid, but must still compare on smaller graphs where both methods fit)
- Inconsistent train/val/test splits across baselines (a cardinal sin in molecular property prediction)
- Not including ablation variants as baselines

**What good baseline selection looks like:**
- Every competing method from the past 2 years that addresses the same problem
- Proper hyperparameter tuning of baselines (not just default settings)
- Fair evaluation protocol: same splits, same featurization pipeline, same evaluation metric
- For molecular property prediction: using the exact same scaffold/random split and specifying which one

### Failure Mode 2: Incremental/Limited Novelty

"This paper essentially takes the Graph U-Net approach of pooling and unpooling node embeddings from a core subset of node embeddings, yet the authors do not mention this work." (j56A1HUTQS)

"The two encoders for different modalities in the proposed approach employ different models that have been introduced in prior research." (sOXKeeVxqW)

Reviewers characterize incremental work as:
- Combining two existing methods without a principled reason
- "Engineering" improvements: adding more blocks, attention heads, or dimensions without new insight
- Reproducing a known result in a slightly different setting
- Minor variations on existing architectures (adding one new type of aggregation to an existing framework)
- Applying an existing architecture to a new domain without adapting it or understanding domain requirements

The threshold for "novel" in GNNs is high because the field moves fast. A design decision that was novel in 2022 may be a baseline by 2024.

### Failure Mode 3: Missing Ablation Studies

Without ablations, reviewers cannot determine which component is responsible for reported improvements. Common ablation failures:
- Not ablating the key proposed component (e.g., proposing a new boundary condition padding strategy but not testing without it)
- Not testing alternative design choices (e.g., different choices of core-node selection in a hierarchical GNN)
- Ablations only in the appendix, not discussed in main paper
- Ablation only on one dataset, which may not generalize

### Failure Mode 4: Scalability Claims Without Large-Scale Experiments

"Motivated by the scalability, but the selected datasets are not large-scale, and the time complexity analysis is not formal." (j56A1HUTQS)

If a paper claims scalability as a contribution, reviewers expect:
- Experiments on genuinely large graphs (at minimum: ogbn-products with ~2M edges; ideally ogbn-papers100M or larger)
- Time/memory benchmarks compared to alternatives, not just accuracy benchmarks
- Formal or empirical analysis of time complexity

### Failure Mode 5: Theoretical Claims Without Proper Validation

"The statement on gradient oversmoothing in the asymptotic case is likely to be equivalent to gradient vanishing... This has to be addressed, otherwise this paper cannot be published." (EFhzmn3RJG, rating=4.0, rejected)

"Many claims of invariance or equivariance to permutation symmetries, without any proofs." (oO6FsMyDBt)

Theory papers must:
- State what is new in the theorem, not just present the theorem
- Validate theory matches empirical behavior (plot the quantity the theorem bounds)
- Distinguish their result from closely related prior results
- Not rely on assumptions that render the theorem trivially true or practically inapplicable

### Failure Mode 6: Unfair Comparisons in Molecular Benchmarks

"UniMol's performance exhibits a significant disparity when compared to kANO and MoleSG. This difference can be attributed to the unconventional split method." (sOXKeeVxqW)

In molecular property prediction (MoleculeNet, QM9, etc.):
- Scaffold splits are more stringent than random splits; comparing methods across different split types is invalid
- Different featurization (2D vs. 3D, atom features, etc.) must be controlled for or explicitly discussed
- Pre-training corpus differences must be disclosed

### Failure Mode 7: Domain Motivation Not Justified

"The ultimate goal of the manuscript is to learn the nonlinear operator F. However, it is not explained why it is needed while F is known and given." (fU8H4lzkIm, from a 6-rated reviewer)

"While equivariant neural networks exhibit appropriate inductive biases... leading to inefficient learning of interactions between atoms. I do not agree with (or understand) this claim at all." (BBD6KXIGJL)

Application papers must clearly explain: why is the learned model needed when domain knowledge or classical methods exist? What is the principled tradeoff?

### Failure Mode 8: Writing and Reproducibility

The frequency of "well-written" (293x) as a strength and writing problems as a weakness indicates presentation matters significantly. Common presentation failures:
- Typos that undermine mathematical rigor (especially in a math-heavy paper)
- Undefined notation, symbols used before definition
- Missing implementation details (learning rate, number of layers, dataset splits)
- Claiming code availability but not providing it

---

## 5. Evaluation Criteria Deep Dive

### 5.1 Novelty Assessment

**Framework for novelty evaluation:**

First, identify the claimed novelty. GNN papers typically claim novelty along one or more axes:
1. A new theoretical result (expressiveness, stability, generalization)
2. A new architecture or architectural component
3. A new problem formulation or task
4. A new training procedure or objective
5. A new application domain or state-of-the-art on a benchmark
6. A new dataset or evaluation protocol

For each claimed contribution, ask:
- Is there a direct prior work that does essentially the same thing? (Even if unacknowledged)
- Is the contribution a straightforward combination of existing ideas?
- Does the contribution require new technical insight to derive or implement?
- Is the claimed novelty actually novel relative to concurrent work?

**High-novelty signals in GNNs:**
- Identifying a counterintuitive phenomenon (e.g., GNNs can be WL-expressive but fail to separate in practice — the Holder stability paper)
- Unifying multiple prior frameworks
- Proving something thought to be hard is actually achievable
- Demonstrating that a widespread assumption is incorrect (e.g., showing certain GNN benchmarks cannot distinguish GNN advances from simple baselines)
- First method to achieve a certain property (bi-Lipschitz GNN, provably converging scalable GNN, etc.)

**Low-novelty signals:**
- "We add X to the existing Y framework" without a principled reason why X belongs
- Combination of two methods that have been combined before under a different name
- Applying a known architecture to a new dataset without architectural changes
- Replacing one component of an existing system with a marginally better one

### 5.2 Baseline Requirements

Baselines are the single most common weakness in GNN papers. The following is a detailed guide:

**For node classification papers:**
Must include at minimum: GCN, GAT, GraphSAGE (the classical trio), plus the most recent SOTA on each specific benchmark being used. For heterophilic graphs: H2GCN, GPRGNN, ACM-GCN or equivalent. For scalable settings: GraphSAINT, SIGN, or equivalent.

**For graph classification papers:**
GIN (the expressiveness standard), MPNN, DiffPool, or appropriate hierarchical methods. Must include graph-level pooling baselines if the task is graph-level. For molecular graphs: specific molecular GNN baselines (MPNN, D-MPNN/Chemprop, AttFP, etc.).

**For link prediction papers:**
SEAL, BUDDY, Neo-GNN, NeoGNN+, NCN/NCNC are current strong baselines. Heuristic baselines (common neighbors, Adamic-Adar, resource allocation) remain important.

**For molecular property prediction:**
Must use the most recent competitive methods on the exact same benchmark with the same split. SchNet, DimeNet++, SphereNet, NequIP, MACE, Equiformer are relevant baselines depending on whether 3D information is used.

**For temporal graph learning:**
TGN, TGAT, GraphMixer, DyGFormer are current strong baselines.

**For scalable GNNs:**
GraphSAGE, GraphSAINT, SIGN, GAS, GAMLP are standard. For billion-scale: specific cluster-GCN, graph distillation methods.

**For knowledge graphs:**
TransE, RotatE, ComplEx as embedding baselines; NBFNet, RED-GNN, NodePiece for GNN-based methods.

**What counts as an unfair baseline:**
- A reimplementation that performs worse than reported in the original paper
- A method run without hyperparameter search when the proposed method is tuned
- An older version of a method when a newer, stronger version is available
- Missing the specific method that is most directly comparable

### 5.3 Ablation Study Requirements

Ablations are the second most common weakness. An adequate ablation study:

**Must validate each major proposed component separately:**
If a paper proposes three new elements (A, B, C), the ablation should include: full model (A+B+C), minus A, minus B, minus C, and ideally minus A+B, minus A+C, minus B+C.

**Must be run on multiple datasets:**
Single-dataset ablations are not convincing, especially if the full model's improvements over baselines vary across datasets.

**Must compare against meaningful alternatives:**
Not just "with/without our component" but also "with the simplest alternative to our component." For example, if proposing a learned aggregation, compare against sum/mean/max aggregations.

**Must be included in the main paper:**
Ablations in appendix only are suspicious and reviewers will flag them.

**Ablation depth scales with model complexity:**
Simple architectures need fewer ablations; papers with 4+ novel components need thorough ablations.

### 5.4 Scalability Considerations

Scalability is contested terrain in GNN research. The following distinctions matter:

**Linear vs. sublinear complexity:** Most GNNs with neighborhood sampling are linear in the number of edges. True sublinear algorithms exist but are rare. Claims of "scalability" that are merely linear should be stated accurately.

**Memory vs. time:** Scalability must address both. A method that reduces training time but requires loading the full graph into memory is not truly scalable for billion-scale graphs.

**Mini-batch training is not sufficient for "scalable":** Mini-batch training of GNNs is standard. "Scalable GNN" implies something beyond this: handling graphs too large for standard mini-batch methods.

**The OGB datasets are the reference standard:**
- ogbn-products (2.5M nodes, 61M edges): minimum for scalable node classification
- ogbn-papers100M (111M nodes, 1.6B edges): large-scale
- ogbn-mag240M: heterogeneous large-scale

Papers claiming scalability that only report results on Cora, Citeseer, and Ogbn-arxiv (169K nodes) will be penalized by reviewers.

### 5.5 Theoretical vs. Empirical Contributions

**Theory-first papers** (expressiveness, stability, generalization bounds):
- Reviewers expect proofs to be correct and checked
- The theorem must say something that was not already known
- The theorem must be tight or the gap must be explained
- Empirical validation that the theoretical phenomena manifest in practice is expected even if not required
- The utility of the theoretical result must be clear (does it help design better models? predict which models will work well?)

**Empirically-driven papers** (new architecture, new application):
- Theory is not required but appreciated
- Strong baselines are non-negotiable
- Ablation must be comprehensive
- Statistical significance: error bars, multiple seeds, proper significance tests
- Hyperparameter sensitivity should be studied

**Papers claiming both theory and empirical contributions:**
Must deliver on both. A paper with a weak theorem and weak experiments will receive lower scores than a paper that clearly belongs to one camp and does it well.

---

## 6. Subfield-Specific Criteria

### 6.1 GNN Expressiveness / Theory

**Key works every paper in this area must know:**
- WL test (Weisfeiler & Lehman, 1968)
- Xu et al. 2019 (GIN, "How Powerful are Graph Neural Networks?")
- Maron et al. 2019 (k-GNN, invariant graph networks)
- Murphy et al. 2019 (relational pooling)
- Bodnar et al. 2021 (cellular message passing)
- Bevilacqua et al. 2022 (equivariant subgraph aggregation)
- Zheng et al. 2023 (Beyond Weisfeiler-Lehman: Quantitative Framework)
- Logical characterizations: Barcelo et al. 2020, Grohe 2021

**What reviewers look for:**
1. Clear placement in the WL hierarchy (at what level does this method sit?)
2. Are the distinguishability claims for specific graph pairs (not just asymptotic)?
3. Does the theoretical gain come at polynomial or exponential cost?
4. Experimental verification on graph isomorphism tests (EXP, CSL, CEXP datasets are standard)
5. Can the framework be used to derive positive results for existing architectures, not just negative?

**Common mistakes:**
- Claiming strict WL improvement without a distinguishing graph pair example
- Ignoring the complexity cost of higher expressiveness
- Not comparing to the quantitative framework papers (Zheng et al.)
- Theory only for node-level tasks, ignoring graph-level implications

### 6.2 Graph Learning for Molecules/Chemistry

**Benchmark conventions (very strict in this area):**

For 2D molecular GNNs (MoleculeNet):
- Use scaffold splits (not random splits) unless specifically studying random split performance
- Report standard deviations over multiple runs (typically 3 seeds minimum)
- Must include DeeperGCN, AttentiveFP, Chemprop/D-MPNN, and recent pre-training methods as baselines
- GROVER, GraphMVP, MolCLR, GraphMAE are relevant pre-training baselines

For 3D molecular GNNs (QM9, MD17, OC20, ANI-1ccx):
- Must include the current SOTA in the equivariant/invariant GNN space
- SchNet (baseline), DimeNet++ (competitive), SphereNet, NequIP, MACE, Equiformer (current strong baselines)
- SE(3)/E(3) equivariance must be explicit: which symmetry group is respected?
- Must specify whether rotations/reflections are both handled (vs. just rotations)

**What separates good molecular GNN papers:**
- Clear understanding of which molecular properties require 3D information and which do not
- Principled integration of physical symmetries (not heuristic)
- Validation on multiple property types (energy, forces, HOMO/LUMO gap, etc.)
- Understanding of equivariance vs. invariance for scalar vs. vector vs. tensor properties
- Attention to data leakage across scaffold splits

**Red flags in molecular GNNs:**
- Comparing 3D methods to 2D baselines to claim unfair advantages
- Not specifying whether 3D coordinates are used at inference time
- Claiming "equivariant" without proving it or providing group-theoretic justification
- Using inconsistent evaluation metrics across compared methods

### 6.3 Scalable GNNs

**The scalability evidence ladder (from weakest to strongest):**
1. Time complexity analysis alone (not sufficient)
2. Memory profiling on medium-scale graphs (not sufficient for "scalable" claim)
3. OGB-products results with training time comparison
4. OGB-papers100M or billion-scale with wall-clock training time
5. Billion-scale + distributed training + convergence guarantees

**Benchmark expectations:**
- ogbn-products: ~87% accuracy is competitive for 2023+, ~88%+ is excellent
- ogbn-arxiv: ~73%+ is competitive
- ogbn-papers100M: any completion is notable; >66% is excellent

**Key considerations unique to scalable GNNs:**
- Neighborhood explosion: how is the exponential explosion of neighborhoods handled?
- Feature aggregation: are features pre-computed or computed on the fly?
- Communication overhead in distributed settings
- Convergence: does the scalable approximation converge to the full-graph solution?

### 6.4 Graph Transformers

**Architectural requirements for credibility:**
- Must handle varying graph sizes (not fixed-size adjacency matrices)
- Positional encoding (PE) strategy must be justified: random walk PE, Laplacian eigenvector PE, or structural PE
- For large graphs: must address quadratic attention complexity (sparse attention, virtual nodes, etc.)
- Ablation of PE choices is expected

**Key baselines that must be compared:**
- GPS (General, Powerful, Scalable): a versatile graph transformer baseline
- Exphormer: sparse graph transformer with strong results
- NodeFormer: linear-complexity graph transformer
- Graphormer: the benchmark-setting transformer for molecular graphs
- GRPE, GraphGPS, Graphformer, etc. depending on the task

**The PE crowded space:**
Dozens of positional encoding strategies have been proposed. New PE methods must compare against RWSE, LapPE, SignNet (for sign-invariant Laplacian eigenvector PE), and BasisNet. Simply proposing a new PE without these comparisons will be penalized.

**Common failure modes for graph transformers:**
- Claiming global receptive field as a contribution (it is now expected of any graph transformer)
- O(n^2) complexity on graphs with thousands of nodes (must be addressed)
- Not addressing the sign ambiguity of Laplacian eigenvectors
- Not testing on both node classification and graph classification tasks

### 6.5 Heterogeneous Graphs

**Key models that serve as baselines:**
- HAN (Heterogeneous Attention Network)
- HGT (Heterogeneous Graph Transformer)
- RGCN (Relational GCN, very common baseline for knowledge graphs)
- HeCo, SHGP (for unsupervised heterogeneous learning)
- Simple-HGN

**Dataset conventions:**
- DBLP, ACM, IMDB are the standard academic benchmarks
- OGB-MAG for large-scale heterogeneous
- Proper handling of meta-path definitions (and sensitivity to meta-path choices must be studied)

**What distinguishes good heterogeneous GNN papers:**
- Clear formulation of what the heterogeneity enables vs. a homogeneous model on the same data
- Fair comparison: homogeneous GNN on the same graph is always a baseline
- Ablation of how different relation types contribute

### 6.6 GNN Robustness/Adversarial

**Standard attack benchmarks:**
- Cora, Citeseer, Polblogs for node classification under perturbation
- Mettack, PGD, DICE, Nettack as attack methods
- For certifiable robustness: randomized smoothing adapted to graphs (Bojchevski et al.)

**What good robustness papers do:**
- Adaptive attacks: the defense must be tested against an attacker who knows the defense
- Fair comparison: same budget perturbation for all methods
- Evaluation on both clean and perturbed performance
- Explanation of WHY the defense works (graph-theoretic or statistical justification)

**Red flags:**
- Claiming robustness without adaptive attack evaluation
- Robustness only against non-adaptive or weak attacks
- Not specifying perturbation budget in comparison tables
- Conflating adversarial robustness with OOD robustness

### 6.7 Temporal/Dynamic Graphs

**The continuous-time vs. discrete-time divide:**
- Continuous-time models (TGN, JODIE) process events as they arrive with a memory state
- Discrete-time models (EvolveGCN, DySAT) process graph snapshots
- These are not directly comparable; papers should position clearly in one framework

**Key baselines:**
Continuous-time: TGN, TGAT, GraphMixer, DyGFormer, TCL
Discrete-time: EvolveGCN, STGCN, DCRNN (for spatial-temporal)
For traffic: STGCN, DCRNN, ASTGCN, GWN (WaveNet on graphs)
For weather: GraphCast, Pangu-Weather (industry models)

**Unique challenges:**
- Temporal leakage: using future information in historical encoding
- Memory efficiency for long time horizons
- Handling irregular time stamps
- Inductive generalization to new nodes

### 6.8 Knowledge Graphs

**The table-stakes baselines:**
TransE, RotatE, ComplEx, DistMult for embedding methods.
CompGCN, KGNN, R-GCN for message passing approaches.
NBFNet (Neural Bellman-Ford Networks) for path-based GNN on KG link prediction — this is currently among the strongest methods and must be compared.

**Evaluation conventions:**
- Mean Reciprocal Rank (MRR) and Hits@1/3/10 are standard
- Filtered MRR (removing true positives from candidates) is required
- FB15K-237 and WN18RR are the standard benchmarks (not the original FB15K/WN18 which have test leakage)

---

## 7. Red Flags and Green Flags

### Red Flags (likely problems)

**Experimental red flags:**
- "We outperform all baselines" with baselines not matching the current SOTA year
- Results on only Cora and Citeseer (too small, too well-studied to be meaningful)
- Performance improvements less than 0.5% on standard benchmarks without statistical testing
- No error bars / single-seed results
- Improvement only on one of many benchmarks, cherry-picked reporting
- Baselines not tuned or run with suboptimal hyperparameters
- Table footnotes like "N/A" or "OOM" that are not independently verified
- No comparison against the one method this paper is most similar to

**Theory red flags:**
- "Straightforward extension of [prior work X]" by the reviewers' assessment
- Theorem proving O(n^3) achieves what O(n^2) already achieves
- The main theorem relies on assumptions that are never empirically verified
- Mathematical errors in submitted proofs (even typos in formal statements are penalized heavily in theory-only papers)
- Claiming WL-incomparability without exhibiting a specific distinguishing graph pair

**Motivation red flags:**
- The stated problem is solved sufficiently well by a simple baseline (e.g., an MLP)
- The application domain motivation does not match the proposed technical solution
- Physical symmetry claims that are incorrect (an incorrect equivariance claim in a molecular paper)
- The proposed method requires information unavailable at test time

**Writing red flags:**
- "State-of-the-art" in the title or abstract without strong quantitative support
- Vague claims: "our method is more expressive" without a formal definition of expressiveness used
- Not discussing limitations (reviewers will add it as a weakness if absent)
- Related work omitting 2-3 directly relevant papers from the past 2 years

### Green Flags (strong positive signals)

**Experimental green flags:**
- Clear, comprehensive baseline table with proper citations and hyperparameter details
- Results across multiple datasets spanning different graph types and sizes
- Statistical significance demonstrated (p-values or confidence intervals)
- Ablation study with multiple ablation conditions in the main paper
- Code released with paper submission
- Computational cost reported (training time, inference time, memory)

**Theory green flags:**
- Theorem comes with a matching lower bound
- The result is tight or the gap is characterized
- Empirical experiments verify the theoretical predictions
- Clear statement of what is new relative to prior work, with formal comparison
- Proof sketch in main text, full proof in appendix

**Presentation green flags:**
- Well-motivated problem statement with clear gap analysis
- Intuitive examples or visualizations that build reader understanding before formal definitions
- Explicit discussion of limitations and failure cases
- Connections to related work that are specific (not just a citation dump)
- Reproducibility appendix with full hyperparameter settings

**Contribution green flags:**
- Identifies a phenomenon that exists in practice but lacks theoretical explanation
- Proposes a method that simultaneously improves on multiple related metrics
- Demonstrates that existing approaches fail on a new evaluation dimension (not just accuracy)
- Provides negative results with scientific value (e.g., showing a widely used benchmark is insufficient)

---

## 8. Benchmark and Dataset Standards

### Standard Benchmarks by Task

**Node Classification (transductive):**
- Planetoid (Cora, Citeseer, Pubmed): very commonly used but considered "too easy" by 2024 standards; results here are necessary but not sufficient
- ogbn-arxiv: 169K nodes, 2022-era competitive; ~72% for simple methods, ~74%+ for strong methods
- ogbn-products: 2.5M nodes, scalability test; ~87%+ competitive
- ogbn-papers100M: very large scale; used for scalability claims

**Node Classification (inductive):**
- PPI (protein-protein interaction): standard inductive benchmark
- ogbn-mag: heterogeneous graph inductive benchmark

**Graph Classification:**
- TUDatasets (MUTAG, PROTEINS, RDT-B, IMDB-B, IMDB-M): these benchmarks are now known to be problematic (the paper "Rethinking Effectiveness of Graph Classification Datasets" was rejected but raised legitimate concerns that the community accepts). Results here should be presented with caution.
- ZINC (molecular): more reliable; 12K training graphs; MAE below 0.10 is competitive for full dataset
- ogbg-molhiv (41K graphs, ROC-AUC): ~79%+ is competitive
- ogbg-molpcba (437K graphs, AP): harder and more reliable benchmark
- LRGB (Long Range Graph Benchmark): recent, designed to test long-range dependency methods

**Link Prediction:**
- ogbl-collab, ogbl-ddi, ogbl-ppa, ogbl-citation2: OGB link prediction
- Cora/Citeseer transductive link prediction: dated, do not use alone
- FB15K-237, WN18RR: knowledge graph link prediction

**Molecular Property Prediction:**
- QM9: 12 quantum chemical targets; MAE in eV units; this benchmark is saturated for 3D methods
- MD17/rMD17: molecular dynamics energy/force prediction; rMD17 is the revised version with better splits
- OC20 (Open Catalyst 2020): large-scale catalyst energy prediction; very strong baselines (GemNet, PaiNN, Equiformer)
- MoleculeNet (scaffold split): 8 binary classification tasks; AUROC on each; use scaffold split

### Known Benchmark Issues

The GNN community is increasingly aware of benchmark reliability issues:
1. **TUDatasets**: many splits are random, leading to high variance; kernel methods can match GNNs on some tasks, calling into question whether graph structure is being tested
2. **Cora/Citeseer**: very small graphs; results depend heavily on train/val/test split; homophily makes even simple baselines strong
3. **QM9**: approaching human-level precision for most targets with E(n)-equivariant GNNs; marginal improvements require extraordinary evidence
4. **MoleculeNet inconsistency**: different scaffold split implementations exist; must specify which one

A paper that only reports results on problematic benchmarks (TUDatasets, Cora/Citeseer) without acknowledging their limitations will receive skepticism. Papers that propose new, more reliable benchmarks are valued.

---

## 9. Example Evaluations

### Example A: High-Quality Theory Paper (expected rating: 7-8)

**Hypothetical submission:** "Equivariant Message Passing with First-Order Logic: A Complete Characterization"

**What makes this high quality:**
- Proves that any GNN architecture expressible in first-order logic with counting can be represented in the proposed framework
- Applies the framework to classify 10+ existing architectures
- Identifies gaps: shows two widely-used architectures believed to be incomparable are actually WL-equivalent under this framework
- Includes empirical validation on synthetic graph isomorphism tasks

**Expected reviewer response:**
- Soundness: 3-4 (proofs appear correct, framework is general)
- Contribution: 3-4 (unifies existing work, identifies new facts)
- Presentation: 2-3 (theory papers are often dense)
- Rating: 7-8

**What could lower the rating:**
- If the classification of existing architectures just reproduces known results
- If the "completeness" claim has a significant loophole
- If no intuition is given for why the framework is correct

### Example B: Borderline Architecture Paper (expected rating: 4-5)

**Hypothetical submission:** "Hierarchical Graph Transformer with Multi-Scale Positional Encoding"

**What makes this borderline:**
- Proposes combining graph transformers with hierarchical pooling and a new multi-scale PE
- Gets strong results on ZINC and ogbg-molhiv
- Compares against Graphormer and GPS but misses Exphormer
- Ablation studies show each component helps but the paper doesn't explain why they work together
- No scalability analysis despite claiming efficiency improvements

**Expected reviewer response:**
- Soundness: 2-3 (method is sound but lacks justification)
- Contribution: 2 (engineering combination of existing ideas)
- Presentation: 3 (reasonably well-written)
- Rating: 4-5 (borderline: some reviewers accept for empirical contribution, others reject for missing Exphormer comparison and limited novelty)

### Example C: Weak Application Paper (expected rating: 2-4)

**Hypothetical submission:** "Graph Neural Networks for Brain Disease Prediction"

**What makes this weak:**
- Uses GCN/GAT on fMRI connectivity graphs for disease classification
- Baselines are non-GNN methods (SVM, MLP) without GNN baselines
- Datasets are private or very small (N < 200)
- No comparison to existing brain GNN methods (BrainNetCNN, BrainGB)
- Claims "state-of-the-art" but only compared to baselines from 2017

**Expected reviewer response:**
- Soundness: 2 (methodology is not wrong but evaluation is inadequate)
- Contribution: 1 (no GNN contribution; only application of existing GNN to a domain)
- Presentation: 2 (application paper with insufficient motivation for why GNNs are needed)
- Rating: 2-4

### Example D: Strong Empirical Paper (expected rating: 6-7)

**Hypothetical submission:** "Scalable Physics-Informed GNN for Weather Forecasting on Irregular Grids"

**What makes this strong:**
- Outperforms GraphCast on medium-resolution forecasting with 5x fewer parameters
- Demonstrates generalization to different resolutions and geographic regions
- Principled integration of atmospheric physics constraints (conservation of mass/energy)
- Ablation of physics constraints vs. pure data-driven
- Memory efficiency benchmarks on GPU cluster
- Comparison to both ML methods (FourCastNet, GraphCast) and numerical weather prediction

**Expected reviewer response:**
- Soundness: 3 (physics integration is principled; some aspects of generalization analysis could be deeper)
- Contribution: 3 (significant application contribution; moderate technical novelty)
- Presentation: 3 (clearly written with good figures)
- Rating: 6-7

---

## 10. Scoring Rubric

Use this rubric to assign final scores. The rubric maps individual dimension assessments to an overall score, calibrated to the GNN field specifically.

### Dimension 1: Novelty (N)

| Score | Description |
|-------|-------------|
| 4 | Fundamental new concept, unifying framework, or first proof of a long-conjectured result |
| 3 | Clearly new method or problem formulation with principled motivation |
| 2 | Incremental improvement over prior work with a clear but limited new contribution |
| 1 | Engineering combination of existing methods; the same or essentially the same paper has been published before |

### Dimension 2: Technical Soundness (S)

| Score | Description |
|-------|-------------|
| 4 | Proofs are correct (or reproducible experiments are compelling); no identified errors; full rigor |
| 3 | Mostly sound with minor issues; identified errors are correctable; empirical results are reproducible |
| 2 | Some soundness concerns: unproven claims, questionable assumptions, experimental protocol issues |
| 1 | Significant errors that undermine the main claims |

### Dimension 3: Experimental Quality (E)

| Score | Description |
|-------|-------------|
| 4 | Comprehensive baselines (current SOTA), multiple datasets, strong ablation, statistical rigor |
| 3 | Good baselines, adequate datasets, ablation present |
| 2 | Missing key baselines or datasets; weak ablation; limited dataset diversity |
| 1 | Missing critical baselines; evaluation protocol is unfair; insufficient experiments |

### Dimension 4: Significance (SIG)

| Score | Description |
|-------|-------------|
| 4 | Will substantially change how the community thinks about or approaches this problem; likely to be widely cited |
| 3 | Useful contribution that advances the field; moderate impact |
| 2 | Narrow contribution with limited impact; interesting but niche |
| 1 | Low impact; does not advance the field beyond incremental benchmarks |

### Overall Score Mapping

The following formula is approximate and should be tempered by holistic judgment:

**Overall = 2 + (N + S + E + SIG) × (6/16)**

In practice:
- **8-10 (Excellent/Oral):** All four dimensions at 3-4; at least two at 4; paper reframes or unifies the field
- **6-7 (Good/Spotlight-Poster):** Most dimensions at 3; perhaps one at 2 but compensated elsewhere; solid contribution
- **4-5 (Borderline):** Mix of 2s and 3s; real contribution but with gaps; reviewers will disagree
- **2-3 (Weak/Reject):** Multiple dimensions at 1-2; fundamental problems with baselines, novelty, or soundness
- **1 (Strong Reject):** Pervasive errors or misrepresentation

### Mandatory Reject Conditions

Regardless of other dimensions, the following are grounds for rejection:

1. **Mathematically incorrect central theorem** (not just a typo, but a substantive error that is not correctable)
2. **Missing the most directly competitive baseline** and the paper's claims depend on that comparison
3. **Experimental protocol that makes results impossible to reproduce** (no hyperparameters, no code, no dataset details)
4. **Data leakage in evaluation** (test set used in any training stage, including hyperparameter selection)
5. **Incorrect equivariance/invariance claims** that are central to the contribution
6. **Plagarism or substantial overlap** with prior unpublished work by other authors

### Adjustments for Subfield

**Theory papers:** Weight S (soundness) more heavily; excellent theory can compensate for weak empirics
**Application papers:** Weight E (experimental quality) and SIG (significance to the domain); weak novelty is acceptable if empirical contribution is strong
**Benchmark papers:** Weight E heavily; must demonstrate the benchmark reveals something existing benchmarks do not

### How to Handle Split Reviews

When reviewers disagree significantly (e.g., one reviewer gives 8 and another gives 3):
- Look for whether one reviewer identified a fatal flaw the others missed
- Check if the disagreeing reviewer has much higher confidence
- Look for whether the author rebuttal addressed the concerns
- When in doubt, give more weight to the specific technical objections over general praise

---

## Appendix: Quick Reference — GNN-Specific Reviewer Vocabulary

**Oversmoothing:** Node representations become indistinguishable as GNN depth increases; related to mixing of neighborhoods
**Oversquashing:** Information bottleneck at narrow graph cuts; exponentially many neighbors' information gets compressed
**WL-equivalence:** A GNN is bounded by the 1-WL test in discriminative power (most MPNNs)
**k-WL:** Higher-order WL hierarchy; k-GNNs can distinguish graphs k-WL cannot
**Equivariance:** f(Rg(x)) = Rg(f(x)); output transforms predictably with input transformation
**Invariance:** f(Rg(x)) = f(x); output is unchanged by group transformations
**Scaffold split:** Drug discovery split based on molecular scaffold (core structure); more realistic than random
**TUD benchmark:** TUDatasets; community aware of their limitations (high variance, some tasks solvable by simple baselines)
**LRGB:** Long Range Graph Benchmark; tests ability to propagate information across long graph distances
**Message passing:** Iterative local aggregation from neighbors; the dominant GNN paradigm
**Graph-level readout:** Aggregation from all node representations to a single graph-level representation
**Subgraph GNN:** GNN that computes representations over subgraphs centered at each node; more expressive than 1-WL
**Positional encoding:** Encoding of a node's position or structural role in the graph, added to node features
**Virtual node:** A global node connected to all nodes; commonly improves molecular GNN performance
**Neighborhood sampling:** Stochastic selection of neighbors for mini-batch training (e.g., GraphSAGE, FastGCN)
**Spectral GNN:** GNN defined in the spectral domain (eigendecomposition of Laplacian); often contrasted with spatial/message-passing GNNs
