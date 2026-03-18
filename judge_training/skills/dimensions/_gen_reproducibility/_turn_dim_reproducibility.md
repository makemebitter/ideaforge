You are an expert AI research reviewer building a **dimension skill file** for the evaluation dimension: **reproducibility**.

## Your Task

Write a comprehensive skill file (Markdown, 5-15K tokens) that teaches an AI judge how to evaluate the "reproducibility" dimension of any research paper. This file is loaded dynamically — it should be self-contained.

## Real Reviewer Examples

Below are real reviewer comments grouped by their soundness sub-score (1-4 scale).

### HIGH reproducibility examples (15 papers):

**Accelerating neural network training: An analysis of the AlgoPerf competition** (rating=7.0, soundness=4.0)
  Strengths: The paper summarizes and analyzes the results of the AlgoPerf Training benchmark, providing a valuable focal point to the community for driving future progress in training algorithms and setting the a...
  Weaknesses: I have no notable concerns about the paper.

Very minor typo: L382, "framekworks" -> "frameworks"...

**SPIN: Self-Supervised Prompt INjection** (rating=5.5, soundness=4.0)
  Strengths: 1. It is novel to detect jailbreakings by prompt injections. The method is well motivated to construct a task where we know the ground truth, and judge using a loss function whether the redirected inp...
  Weaknesses: 1. The title is misleading, and it seems to be proposing a new prompt injection attack. However, the paper aims to detect jailbreakings using the idea of prompt injection. Also, I think only the inter...

**Buckingham $\pi$-Invariant Test‑Time Projection for Robust PDE Surrogate Modelin** (rating=4.5, soundness=4.0)
  Strengths: **Originality** is high. The method leverages Buckingham $\pi$-theorem and addresses OoD problem innovatively from a structured perspective, i.e., data space can be decomposed into equivalence classes...
  Weaknesses: Regarding **Clarity**:
1. An algorithm that summarizes all the procedure can be helpful to readers. Especially, corresponding to predict & inverse in Fig. 3. How to do inverse in general?
2. Above equ...

**GLinSAT: The General Linear Satisfiability Neural Network Layer By Accelerated G** (rating=6.5, soundness=4.0)
  Strengths: * Enforcing constraints to the output of neural networks is an important research direction given the fact that deep neural networks are being extended from "traditional" classification and regression...
  Weaknesses: * The major drawback of GLinSAT over LinSAT is that its inference time is longer if LinSAT is set with its default 100 iterations. It will be helpful for the readers if there is a "discussion" section...

**Fairness-Aware Estimation of Graphical Models** (rating=5.75, soundness=4.0)
  Strengths: Originality
Despite extensive research in fair machine learning, this paper tackles a relatively under-studied problem, which is to conduct fair estimation of graphical models. The authors also propos...
  Weaknesses: -	The optimality analysis requires the convexity of the loss function, and it remains unclear how the performance would be affected if the loss function were non-convex, which is common in machine lea...

**Barely Random Algorithms and Collective Metrical Task Systems** (rating=6.75, soundness=4.0)
  Strengths: Metrical task systems are a widely acknowledged fundamental model of online computing. The question is a fundamental question in online computing. The result answers a fundamental question in online c...
  Weaknesses: It's a simple idea and a simple proof, though that's not necessarily a weakness....

**Barely Random Algorithms and Collective Metrical Task Systems** (rating=6.75, soundness=4.0)
  Strengths: * The results of the paper are interesting and may inspire future work in similar directions.
* Viewing the problem as a collaborative MTS with $k$ deterministic agents provides better insights and un...
  Weaknesses: I don't see any major weaknesses in the presented results or the proofs.

However, I find that the paper is not a good fit for NeurIPS at all. A conference or journal focused on theoretical computer s...

**Barely Random Algorithms and Collective Metrical Task Systems** (rating=6.75, soundness=4.0)
  Strengths: The paper is very well written. All results are rigorously proven, but there is also a lot of intuition and high-level guiding of the reader.
The solution is non-trivial and builds on fairly complex i...
  Weaknesses: There is no experimental analysis. It is understandable that the work is mainly theoretical, but one suggestion would be to expand on the application discussed in Remark 2.3 and include an experimenta...

### MID reproducibility examples (15 papers):

**BINR-MAPF: A Bio-Inspired Neural-Reflex Architecture for Decentralized Multi-Age** (rating=3.6, soundness=3.0)
  Strengths: Originality is strong. The bio-inspired framing of multi-agent pathfinding through neural reflexes and FSM-based behavior modulation is creative. While reflex-based local control has precedents in rob...
  Weaknesses: Lack of theoretical grounding or convergence analysis

Suggestions:
1. Provide an analytical discussion (even qualitative) of conditions ensuring conflict-free convergence under the reflex vector comp...

**BINR-MAPF: A Bio-Inspired Neural-Reflex Architecture for Decentralized Multi-Age** (rating=3.6, soundness=3.0)
  Strengths: Strong motivation grounded in distributed robotics challenges (latency, bandwidth). The reflex-based local control is conceptually clean and scalable. FSM-based adaptive behavior switching and leader-...
  Weaknesses: The 'bio-inspired' claim is mostly metaphorical; there’s no real biological modeling. No theoretical analysis of convergence, stability, or collision guarantees. Experiments are simulation-only with h...

**Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Promp** (rating=6.5, soundness=3.0)
  Strengths: * The paper is clearly written and includes useful foundational knowledge to help set-up the theoretical framework.
* The work studies both the case of when prompts contain shared structures and when ...
  Weaknesses: 1. The beginning of Section 4 highlights the simplification of the theoretical analysis ("we focus only on the first head, namely, l = 1 in equation (6), and the first row of the attention in this hea...

**Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Promp** (rating=6.5, soundness=3.0)
  Strengths: 1. The paper provides detailed theoretical analyses of the reparameterization strategy for prompt learning.

2. The experiments on several tasks demonstrate the theoretical analyses....
  Weaknesses: 1. Although the paper provides detailed theoretical proof of the effectiveness of the reparameterization strategy in prefix tuning, my main concern is about the technical contribution of the paper. Si...

**Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Promp** (rating=6.5, soundness=3.0)
  Strengths: 1. Many existing studies have only applied prompt techniques in different domains without providing theoretical proof of their effectiveness. In contrast, this research explores the theoretical founda...
  Weaknesses: 1. The lack of additional visualization results means that, despite the authors' analysis of the effectiveness of prompt techniques, there is a deficiency in more intuitive visual outcomes. As a reade...

**Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Promp** (rating=6.5, soundness=3.0)
  Strengths: 1. Provides a novel theoretical perspective on reparameterization, bridging prefix-tuning and mixture-of-experts frameworks.
2. Demonstrates empirical improvements across multiple tasks and architectu...
  Weaknesses: 1. The study is limited to specific configurations, leaving questions on broader applicability to different model types and prompt architectures.
2. While theoretically sound, the real-world implicati...

**Linearly Decoding Refused Knowledge in Aligned Language Models** (rating=3.33, soundness=3.0)
  Strengths: 1. The paper introduces an interesting experiment transferring probes from base models to aligned models, providing direct evidence that representations of refused knowledge persist through instructio...
  Weaknesses: ### 1. Model
The paper evaluates only small models (2B, 6B, 9B) from just two model families (Gemma and Yi). This is insufficient to support the broad claims about aligned language models in general.
...

**Linearly Decoding Refused Knowledge in Aligned Language Models** (rating=3.33, soundness=3.0)
  Strengths: The paper is mostly easy to follow. It introduces as simple idea and performs experiments based on that. It also does a good job explaining the relation to prior work....
  Weaknesses: While I do not find anything in the paper factually wrong, the contribution and scope of experiments are very limited to the point where I think the paper likely requires additional content (experimen...

### LOW reproducibility examples (15 papers):

**BINR-MAPF: A Bio-Inspired Neural-Reflex Architecture for Decentralized Multi-Age** (rating=3.6, soundness=2.0)
  Strengths: *   Simple, interpretable swarm mechanics in use
*   Highly decentralized agent interaction with minimum communication
*   The algorithm is potentially lightweight in terms of computational resources
...
  Weaknesses: 1.  The Related Work section seems to be quite outdated and very limited. MAPPO-MAPF is mentioned but not cited. What is the connection to other swarm-based algorithms (if any), for example, to this o...

**BINR-MAPF: A Bio-Inspired Neural-Reflex Architecture for Decentralized Multi-Age** (rating=3.6, soundness=2.0)
  Strengths: - There is some novelty in considering biological behaviors....
  Weaknesses: - It is not clear how this approach compares with many other bio-inspired algorithms (ant colony, particle swarm, etc.)...

**BINR-MAPF: A Bio-Inspired Neural-Reflex Architecture for Decentralized Multi-Age** (rating=3.6, soundness=1.0)
  Strengths: - The biological idea seems novel. The ranking of agents reminds me of how PIBT works, and there could be interesting parallels or ways to improve PIBT....
  Weaknesses: W1: The approach itself seems rather weak compared to existing large-scale imitation learning and hybrid methods. Using an FSM alone is unlikely to achieve competitive results. Still, outperforming PR...

**Linearly Decoding Refused Knowledge in Aligned Language Models** (rating=3.33, soundness=2.0)
  Strengths: 1. This research investigates a critical question in AI alignment and interpretability: whether knowledge that a large language model is trained to refuse remains accessible after safety tuning.

2. T...
  Weaknesses: 1.	The analysis is strictly empirical and would be strengthened by a theoretical or mechanistic explanation for the observed phenomena.
2.	The research relies on manually constructed data, which limit...

**CAT: Post-Training Quantization Error Reduction via Cluster-based Affine Transfo** (rating=2.5, soundness=2.0)
  Strengths: 1. The method is well-motivated. It directly targets the failure of plain affine transformation in low-bit PTQ, a claim supported by the authors in Table 1.
2. The authors test CAT on a diverse set of...
  Weaknesses: 1. The paper discusses parameter overhead but provides no analysis of the computational (latency) cost introduced by the CAT-specific steps during inference (PCA projection, cluster assignment, and af...

**CAT: Post-Training Quantization Error Reduction via Cluster-based Affine Transfo** (rating=2.5, soundness=2.0)
  Strengths: 1. Using cluster-specific affine corrections to align quantized and full-precision outputs is intuitive, lightweight, and easy to implement.
2. CAT consistently improves Top-1 accuracy across multiple...
  Weaknesses: 1. The paper does not provide any analysis of the inference-time overhead introduced by CAT. Although PCA and cluster assignment are claimed to be lightweight, they may still incur noticeable latency....

**T2VTextBench: A Human Evaluation Benchmark for Textual Control in Video Generati** (rating=2.5, soundness=2.0)
  Strengths: 1.Timely and valuable problem: 
The paper addresses a highly practical and important problem that has received limited attention in the current wave of text-to-video research. Ensuring text accuracy i...
  Weaknesses: 1.Limited evaluation scale:
The current benchmark includes only 73 prompts, which seems too small to be representative or authoritative. It is unclear how these 73 prompts were designed. What dimensio...

**T2VTextBench: A Human Evaluation Benchmark for Textual Control in Video Generati** (rating=2.5, soundness=2.0)
  Strengths: 1、The paper presents a timely and focused investigation into how accurately video diffusion models can render on-screen text.

2、The benchmark covers a comprehensive set of models, spanning both open-...
  Weaknesses: 1、The paper’s core weakness is poor verifiability and scalability: the evaluation is produced only by manual inspection, so inter-annotator disagreement is inevitable, and future models cannot be repr...


## Output Format

### 1. What "reproducibility" means in peer review
- Definition, scope, what reviewers look for

### 2. Score 1 (Poor reproducibility)
- What this looks like, common patterns
- Real reviewer quotes

### 3. Score 2 (Below Average reproducibility)
- What this looks like, common patterns
- Real reviewer quotes

### 4. Score 3 (Good reproducibility)
- What this looks like
- Real reviewer quotes

### 5. Score 4 (Excellent reproducibility)
- What this looks like
- Real reviewer quotes

### 6. Red Flags & Green Flags
- Instant indicators of low vs high reproducibility

### 7. Cross-topic Patterns
- How reproducibility expectations differ by research area

Ground everything in the real reviewer examples above. Be specific and concrete.
