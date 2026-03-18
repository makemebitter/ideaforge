# Skill File: Evaluating the "Novelty" Dimension of Research Papers

**For use by AI judge agents when scoring the novelty/contribution sub-dimension of any research paper.**

---

## 1. What "Novelty" Means in Peer Review

### Definition

**Novelty** (also called "originality" or "contribution") measures how much the paper advances the current state of knowledge. It is distinct from:

- **Soundness**: whether the methods and results are correct
- **Presentation**: whether the paper is well-written and clear
- **Significance**: how broadly impactful the work might be (related, but novelty is specifically about *what is new*, not *how important that new thing is*)

In most top-tier venue rubrics (NeurIPS, ICLR, ICML, AAAI), the contribution/novelty sub-score uses a 1–4 scale:

| Score | Label | Meaning |
|-------|-------|---------|
| 1 | Poor | Marginal or no advance over existing work |
| 2 | Below Average | Incremental improvement or combination of existing ideas |
| 3 | Good | Clear novel contribution, meaningfully extends prior work |
| 4 | Excellent | Significant, original contribution; new insight, method, or framework |

### What Reviewers Actually Look For

Novelty is not just "no prior paper did this exact thing." Reviewers evaluate along multiple axes:

1. **Conceptual novelty**: Does the paper introduce a new idea, perspective, or framing that the field hasn't considered?
2. **Technical novelty**: Does it introduce new algorithms, proofs, architectures, or theoretical tools?
3. **Empirical novelty**: Does it reveal unexpected findings, new benchmarks, or phenomena not documented before?
4. **Application novelty**: Does it transfer existing methods to a domain where they haven't been applied in a meaningful way?

Reviewers are experts. They will instantly recognize:
- Repackaged existing work with new notation
- Combinations of prior techniques without meaningful synthesis
- Claims of novelty that are contradicted by prior art
- Genuinely new ideas that open new research directions

### The Critical Question

When reading a paper, the novelty question is: **"If this paper didn't exist, what would the community be missing?"** A score-4 paper would leave a significant hole. A score-1 paper would leave essentially nothing missing.

---

## 2. Score 1 — Poor Novelty

### What This Looks Like

Score-1 novelty means the paper makes **no meaningful advance** over the existing literature. This can manifest as:

- **Direct replication**: The paper does something already done, possibly with minor parameter changes
- **Combination without synthesis**: Pasting two existing methods together without showing why the combination is non-trivial or what it reveals
- **Bio-inspired framing without substance**: Using biological metaphors metaphorically, without actual biological modeling or new computational insight
- **Claims contradicted by existing work**: Claiming a contribution that prior papers have already made
- **FSM/heuristic approaches to solved problems**: Proposing rule-based approaches to problems where end-to-end learned or principled methods are clearly superior

### Common Patterns from Real Reviews

**Pattern 1: "This exists already"**

From reviewer comments on BINR-MAPF (contribution=1.0):
> "It is not clear how this approach compares with many other bio-inspired algorithms (ant colony, particle swarm, etc.)..."
> "The biological idea seems novel [but] The approach itself seems rather weak compared to existing large-scale imitation learning and hybrid methods. Using an FSM alone is unlikely to achieve competitive results."
> "The ranking of agents reminds me of how PIBT works, and there could be interesting parallels..."

The reviewer's first reaction is to name the prior work that already covers the claimed contribution.

**Pattern 2: "Weak compared to baselines"**

> "Still, outperforming PRIMAL [a much older method] is not a strong baseline to compare against."

Score-1 papers either fail to compare against the strongest methods, or when they do, they underperform—which directly undermines the novelty claim.

**Pattern 3: Limited scope amplifies weak contribution**

> "It seems like a strong result considering a very niche scenario."

When the contribution is already minimal, a narrow scope makes it worse. There's little to generalize to.

**Pattern 4: The "bio-inspired" label as insufficient novelty**

> "There is some novelty in considering biological behaviors." (single hedged positive)

A score-1 novelty often earns exactly one hedged concession from reviewers before they proceed to dismantle the contribution. The phrasing "there is some novelty in..." is a hallmark signal of a score-1 review.

### Score-1 Novelty Checklist

A paper likely deserves score 1 if:
- [ ] The main claimed contribution exists in prior work, possibly with different names
- [ ] The "new" elements are purely notational or cosmetic reframings
- [ ] The paper does not outperform the strongest existing baselines it claims to surpass
- [ ] The biological/metaphorical framing doesn't translate to actual algorithmic novelty
- [ ] The contribution could be described as "X applied to Y" where X and Y are both standard

---

## 3. Score 2 — Below Average Novelty

### What This Looks Like

Score-2 novelty means the paper has **some genuine novelty**, but it is incremental, narrow, or heavily qualified. This is the most common score for borderline papers. Key characteristics:

- **Incremental improvement**: A real but small advance — e.g., adding a cluster step before an existing affine correction, or providing a theoretical analysis of an already-empirically-known phenomenon
- **Insight without scale**: The new finding is interesting but only demonstrated in limited settings (small models, one modality, restricted architectures)
- **Theory that doesn't match experiments**: The theoretical contribution is novel but can't be validated at practical scale
- **Empirical-only novelty with missing mechanistic explanation**: Interesting finding but purely descriptive, no mechanism or theory
- **Novel combination with trivial integration**: The paper combines existing components in a new way, but reviewers don't see why this combination requires a new paper rather than being an implementation detail

### Real Reviewer Examples

**Example: CAT (Post-Training Quantization) — contribution=2.0**

Reviewers acknowledged:
> "It is novel to first cluster and then use affine transformation to correct residual errors."
> "Can be used to improve PTQ methods."

But criticized:
> "The experiments are limited to relatively small vision models. Could the authors clarify why evaluations were not extended to other modalities (e.g., language or multimodal models)?"

The novelty exists — clustering before affine correction is a real insight — but the scope is so restricted that the community doesn't know if this insight is generally applicable. This caps the contribution at 2.

**Example: Linearly Decoding Refused Knowledge — contribution=2.0**

Reviewers acknowledged:
> "The paper introduces an interesting experiment transferring probes from base models to aligned models, providing direct evidence that representations of refused knowledge persist through instruction tuning."
> "This research investigates a critical question in AI alignment and interpretability."

But criticized:
> "The analysis is strictly empirical and would be strengthened by a theoretical or mechanistic explanation for the observed phenomena."
> "The research relies on manually constructed data, which limits generalizability."
> "The paper evaluates only small models (2B, 6B, 9B) from just two model families (Gemma and Yi). This is insufficient to support the broad claims about aligned language models in general."

The finding (refused knowledge is linearly decodable from representations) is genuinely interesting. But the empirical limitations — small models, two families, manual data — mean the community can't rely on this result for general conclusions.

**Example: Revisiting Prefix-tuning — contribution=2.0**

> "my main concern is about the technical contribution of the paper. Since prefix-tuning has already been proposed and used in different domains, the contribution of theoretically analyzing it seems somewhat incremental given the current state of research."
> "The lack of additional visualization results means that, despite the authors' analysis of the effectiveness of prompt techniques, there is a deficiency in more intuitive visual outcomes."
> "The beginning of Section 4 highlights the simplification of the theoretical analysis ('we focus only on the first head, namely, l = 1 in equation (6), and the first row of the attention in this head')."

The theoretical analysis is real, but prefix-tuning already existed and worked empirically. Proving it works theoretically is incremental when the community has moved on. The simplifications further limit the contribution.

### Distinguishing Score 2 from Score 1

| Aspect | Score 1 | Score 2 |
|--------|---------|---------|
| Core idea | Exists in prior work | Genuinely new, but narrow |
| Baselines | Doesn't beat them | Beats them in limited settings |
| Reviewer tone | "This already exists" | "Interesting, but limited" |
| Positive signals | Barely any | One genuine positive |

### Score-2 Novelty Checklist

- [ ] There is a real, new idea in the paper (cluster-then-transform, probe transfer, statistical reparameterization analysis)
- [ ] But it is only tested in restricted conditions (small models, one domain, single architecture)
- [ ] OR the idea is analytically novel but the method itself was already empirically used
- [ ] OR the finding is empirical with no mechanistic explanation
- [ ] OR prior work did something extremely similar with only a minor modification separating them

---

## 4. Score 3 — Good Novelty

### What This Looks Like

Score-3 novelty means the paper makes a **clear, meaningful contribution** that the field will notice and cite. It advances the state of the art in a non-trivial way, extends to a reasonable set of settings, and provides insight that wasn't previously available.

Key characteristics:
- **Real new component**: Not just combining existing ideas, but synthesizing them in a way that requires genuine insight to discover
- **Addresses a recognized problem**: The community knows this problem and will value a solution
- **Creative framing**: Even if individual components exist, the way they're assembled or motivated is genuinely original
- **Multiple positive signals**: Reviewers list multiple strengths before their weaknesses
- **Sufficient scope**: Validated on several tasks, settings, or domains (not just one)

### Real Reviewer Examples

**Example: BINR-MAPF — contribution=3.0 (the "creative framing" case)**

> "Originality is strong. The bio-inspired framing of multi-agent pathfinding through neural reflexes and FSM-based behavior modulation is creative. While reflex-based local control has precedents in robotics, integrating it into a neural MAPF framework with learned components is novel."
> "Strong motivation grounded in distributed robotics challenges (latency, bandwidth). The reflex-based local control is conceptually clean and scalable. FSM-based adaptive behavior switching and leader-follower coordination are interesting design choices."

Note the contrast with score-1 reviews of the same paper: score-3 reviewers acknowledge that the specific integration is novel even if components exist. The difference is whether the synthesis itself requires new insight.

**Example: Revisiting Prefix-tuning — contribution=3.0 (the "theory provides new perspective" case)**

> "The paper provides detailed theoretical analyses of the reparameterization strategy for prompt learning."
> "Provides a novel theoretical perspective on reparameterization, bridging prefix-tuning and mixture-of-experts frameworks."
> "Many existing studies have only applied prompt techniques in different domains without providing theoretical proof of their effectiveness. In contrast, this research explores the theoretical foundation."

When reviewers say "this is the first to provide a theoretical foundation for X," they're describing score-3 novelty. The method X existed, but understanding *why* it works is a separate contribution.

**Example: CAT — contribution=3.0 (the "well-motivated method" case)**

> "The method is well-motivated. It directly targets the failure of plain affine transformation in low-bit PTQ, a claim supported by the authors in Table 1."
> "The authors test CAT on a diverse set of models."

Score-3 novelty often comes with the phrase "well-motivated" — the paper diagnoses a real problem and proposes a targeted solution that addresses the diagnosis.

**Example: MeshMosaic — contribution=3.0 (the "important practical advance" case)**

> "The patch-based generation framework is important for complex and high-resolution mesh."
> "The experimental results are promising, with sound and detailed ablation studies."

The framework advances a practical capability (complex mesh generation) in a way the field needs. Not revolutionary, but clearly moves the frontier.

### What Score-3 Is Not

Score-3 is not guaranteed by:
- Having a working system (soundness != novelty)
- Achieving state-of-the-art numbers (empirical gains can come from implementation, not ideas)
- Applying existing methods to a new domain (application novelty is weak unless the domain adaptation itself is insightful)

Score-3 requires that the paper contains at least one idea that required non-trivial intellectual effort to discover, and that this idea is new enough that prior work did not obviously contain it.

### Score-3 Novelty Checklist

- [ ] The paper's core idea required genuine insight to discover (not just engineering effort)
- [ ] At least one reviewer says something like "the idea is novel," "creative," "interesting," or "well-motivated"
- [ ] The contribution is not fully derivable from directly combining existing papers
- [ ] Multiple settings or domains are covered
- [ ] The paper addresses a known, recognized problem in the field
- [ ] Weaknesses are about scope or depth, not about whether the contribution is real

---

## 5. Score 4 — Excellent Novelty

### What This Looks Like

Score-4 novelty means the paper makes a **significant, original contribution** that changes how the community thinks about a problem, resolves an outstanding question, introduces a new research direction, or provides a new tool that others will build on.

Key characteristics:
- **First to do something important**: Introduces the first solution, the first theoretical analysis, the first framework for a recognized problem
- **Resolves a genuine gap**: Not just "no one did this" but "this was a meaningful open question and now it's answered"
- **New proof techniques or frameworks**: Not just applying existing techniques, but developing new mathematical or algorithmic tools
- **Elegant but non-obvious**: Simple in retrospect, but required real creativity to discover
- **Community-building**: Sets up future work, defines a new problem space, or provides a canonical reference

### Real Reviewer Examples

**Example: AlgoPerf Competition Analysis — contribution=4.0**

> "The paper summarizes and analyzes the results of the AlgoPerf Training benchmark, providing a valuable focal point to the community for driving future progress in training algorithms."

This is community infrastructure novelty. A benchmark competition analysis is novel when it provides authoritative, trusted data that the community will use as a standard reference. The reviewer notes "no notable concerns" — high novelty papers at score 4 often have minimal weaknesses.

**Example: GLinSAT — contribution=4.0**

> "Enforcing constraints to the output of neural networks is an important research direction given the fact that deep neural networks are being extended from 'traditional' classification and regression..."

Score-4 novelty often involves tackling a **recognized, important research direction** with a general solution. GLinSAT provides a general linear satisfiability layer, not a special-case fix.

**Example: Barely Random Algorithms — contribution=4.0**

> "Metrical task systems are a widely acknowledged fundamental model of online computing. The question is a fundamental question in online computing. The result answers a fundamental question in online computing."

Notice the triple repetition: "fundamental question... fundamental question... fundamental question." When reviewers describe a result as answering a **fundamental question**, that is the signature language of score-4 novelty. The paper is simple ("a simple idea and a simple proof") but solves something the community has been asking for years.

**Example: Optimal Brain Apoptosis — contribution=4.0**

> "Unlike previous methods that approximate the Hessian matrix, OBA calculates the full Hessian-vector product, providing a more accurate measure of parameter importance and leading to more precise pruning."

Score-4 novelty often comes from **removing a longstanding approximation**. The community knew the exact computation was better; OBA makes it practical. This is a technical novelty that unlocks precision that was previously unavailable.

**Example: Physics-Informed Regularization — contribution=4.0**

> "The idea of imposing time-reversal symmetry via a regularization term is novel and well-motivated."
> "The implementation of the regularization term is simple yet the effect is visible."

"Simple yet effective" is a key signal for score-4. The idea is elegant — if you find a simple, principled approach to a hard problem, that's more impressive than a complicated one.

**Example: Disentangling Relational and Sensory Information — contribution=4.0**

> "The authors take a well-motivated challenge (helping transformers work with relational reasoning) and define a natural extension to the transformer architecture."

The paper creates a "natural extension" — this is the language of contribution that feels inevitable in retrospect but required real insight to discover.

**Example: Toward Understanding Transformers via Representation Theory — contribution=4.0**

> "Excellent theoretical contribution to understanding in-context-learning"
> "Using theoretical results to motivate better attention mechanisms"

Theory that is directly actionable — it motivates better attention mechanisms — earns score 4. The contribution isn't just understanding; it enables design.

**Example: Degree-aware Spiking Graph Domain Adaptation — contribution=4.0**

> "The design of effective pseudo-labels by only utilizing the degree information from the target domain is an effective approach to domain adaptation in SGNs."

Degree information is a simple, overlooked signal. Using something simple but non-obvious to solve a real adaptation problem is exactly score-4 novelty.

### The "Simple but Non-Obvious" Pattern

Many score-4 papers share a structure: the key idea is simple to state in retrospect, but it required real insight to discover:

- *GLinSAT*: Make the satisfiability layer general (not just linear equality)
- *Barely Random Algorithms*: Solve the barely-random version of MTS
- *OBA*: Actually compute the full Hessian-vector product (don't approximate)
- *Physics-Informed Reg*: Add time-reversal symmetry as a regularizer
- *Degree-aware SGDA*: Use degree information for pseudo-labels

Simplicity at score 4 is a *strength*, not a weakness. When a reviewer says "it's a simple idea," followed by high scores, that means the insight was found where others missed it.

### Score-4 Novelty Checklist

- [ ] The paper introduces something genuinely new that the community needed
- [ ] Prior work did not obviously contain the key idea (even with hindsight)
- [ ] The contribution is general enough to apply beyond one narrow setting
- [ ] Reviewers use language like: "novel," "first to," "fundamental," "natural extension," "well-motivated and effective"
- [ ] The weaknesses are about extensions and details, not about whether the core idea is new
- [ ] The paper opens new research directions or provides a tool others will use

---

## 6. Red Flags & Green Flags

### Instant Red Flags (score toward 1–2)

**Language patterns that signal low novelty:**

| Phrase | What it signals |
|--------|----------------|
| "There is *some* novelty in..." | Score 1 — minimal, hedged concession |
| "It is not clear how this compares to [long list of prior methods]" | Score 1 — contribution is indistinguishable from existing work |
| "The approach itself seems rather weak compared to..." | Score 1 — contribution is real but not competitive |
| "The limited scope/experiments prevent us from..." | Score 2 — real idea, insufficient validation |
| "The study is limited to specific configurations" | Score 2 — interesting but not generalizable |
| "The contribution is incremental given the current state" | Score 2 — the field has moved on |
| "This is the combination of [X] and [Y] without..." | Score 2 — combination without synthesis |
| "The analysis assumes simplified [architecture/setting]" | Score 2 — theoretical contribution is narrow |

**Structural red flags:**

- Paper applies existing method to a new domain without showing the adaptation required non-trivial insight
- "Novelty" section lists three prior papers and says "we combine all three"
- The claimed contribution requires checking whether prior papers already did it
- Experiments only run on one dataset or one model family
- Theoretical results require strong simplifying assumptions not satisfied in practice
- Bio-inspired framing with no actual biological modeling
- The paper's title mentions a well-known method with a new adjective ("Improved X," "Efficient X," "Better X")

### Instant Green Flags (score toward 3–4)

**Language patterns that signal high novelty:**

| Phrase | What it signals |
|--------|----------------|
| "The idea is novel and well-motivated" | Score 3+ — reviewers recognize genuine contribution |
| "First to provide theoretical foundation for..." | Score 3–4 — fills a recognized gap |
| "Answers a fundamental question in..." | Score 4 — landmark result |
| "Natural extension to the [framework/architecture]" | Score 4 — elegant, inevitable in retrospect |
| "Simple yet the effect is visible" | Score 4 — parsimonious insight |
| "The design is creative" | Score 3+ — genuine synthesis |
| "Well-motivated... directly targets the failure of..." | Score 3–4 — problem-driven novelty |
| "Opens new research directions" | Score 4 — generative contribution |

**Structural green flags:**

- Paper identifies a problem that prior work had but didn't name (a new failure mode, limitation, or phenomenon)
- Insight is stated in one sentence and is surprising but obvious in retrospect
- The paper introduces a new concept (dimension, layer, mechanism) that will appear in future work
- Theory explains an empirical observation that the community noted but didn't understand
- Paper generalizes a special-case result to a general setting without losing tractability
- Cross-domain connection: bridges two research areas that didn't talk to each other

### The Crucial Distinction: Novelty vs. Execution

Many papers with score-2 or score-3 novelty have excellent execution. This is a trap:

- A paper can be very well-written, technically sound, and empirically rigorous, but still have score-2 novelty because the idea isn't that new
- A paper can have messy presentation and incomplete experiments but still have score-4 novelty because the idea is breakthrough
- Reviewers sometimes raise novelty scores when execution is excellent, but this is a bias to watch for

Score novelty based on the **idea**, not the polish.

---

## 7. Cross-Topic Patterns

### 7.1 Theory Papers (Theoretical ML, Optimization, Learning Theory)

**Novelty expectations are high and specific:**

In theory papers, novelty is measured by:
1. **Whether the result was open**: A result that solves a known open problem scores 4. A result for a problem no one asked about scores lower.
2. **Tightness**: Results with matching upper and lower bounds are more novel than one-sided results.
3. **Technique novelty**: A new proof technique that others can use is more novel than applying an existing technique to a new setting.

**Common score-2 pattern in theory**: Analyzing an existing method (prefix-tuning, MAML) theoretically. The analysis is new, but the method is not. Score 3 if the analysis reveals something counterintuitive or enables new method design. Score 2 if it just confirms what was empirically known.

**Common score-4 pattern in theory**: Proving that something previously approximated can be done exactly (OBA, full Hessian-vector product), or resolving a question about learnability/computability that has been open.

> From Barely Random Algorithms (contribution=4): "It's a simple idea and a simple proof, though that's not necessarily a weakness."

In theory, elegance and simplicity signal deep understanding, not lack of effort.

### 7.2 Deep Learning Methods Papers (Architectures, Training, Efficiency)

**Novelty expectations center on mechanism:**

Score 3–4 requires:
- A new mechanism, not just a new configuration
- An insight about *why* the mechanism works, not just *that* it works
- Generalization across architectures or tasks

**Common score-2 pattern**: A paper adds a new component to an existing system and shows it improves performance, but doesn't explain why the improvement occurs or whether the component is general.

**Common score-4 pattern**: A paper identifies a specific failure mode of existing approaches and provides a targeted fix based on understanding the mechanism. Example: GLinSAT identifies that LinSAT is restricted to linear equalities and generalizes to all linear constraints — the failure mode is clear, the solution is principled.

> From GLinSAT (contribution=4): "Enforcing constraints to the output of neural networks is an important research direction..."

The reviewer situates the paper in a "research direction" — score-4 novelty in methods papers often advances an entire research direction, not just solves one problem.

### 7.3 Application Papers (Domain Adaptation, Medical, Robotics, Multi-Agent)

**Novelty expectations are about the application insight:**

For application papers, novelty is assessed differently:
- Applying a known method to a new domain is score 1–2 unless the domain adaptation reveals new challenges or requires genuinely new techniques
- Score 3 requires showing that the target domain has unique properties that forced new ideas
- Score 4 requires either defining a new problem space the community hadn't considered, or showing a surprising generalization across domains

**Common score-1 pattern in applications**: "We apply [MAPF method] to [new scenario]." If the scenario is new but the adaptation is straightforward, this is score 1–2.

> From BINR-MAPF (contribution=1): "The 'bio-inspired' claim is mostly metaphorical; there's no real biological modeling."

The key test: did the target application require you to *think differently*, or did you just implement an existing method in a new context?

**Common score-3/4 pattern in applications**: Discovering that a domain-specific signal (degree information in graphs, time-reversal symmetry in dynamics) provides surprisingly strong regularization for a general problem.

> From Degree-aware SGDA (contribution=4): "The design of effective pseudo-labels by only utilizing the degree information from the target domain is an effective approach to domain adaptation."

The key insight (degree information is sufficient for pseudo-labels) is application-specific but reveals a general principle.

### 7.4 Empirical/Analysis Papers (Surveys, Benchmarks, Ablations)

**Novelty expectations are about what the analysis reveals:**

- Score 1–2: Analysis that confirms expected results
- Score 3: Analysis that reveals non-obvious patterns or contradicts assumptions
- Score 4: Analysis that provides authoritative data that will shape future research

> From AlgoPerf (contribution=4): "The paper summarizes and analyzes the results of the AlgoPerf Training benchmark, providing a valuable focal point to the community."

A competition paper earns score-4 novelty when it provides data and insight that the community couldn't generate otherwise — a trusted shared reference that future papers will cite.

For analysis papers, the key novelty question is: **"What does this analysis reveal that was not known or suspected?"** Confirming suspected relationships is lower novelty. Revealing surprising, counterintuitive, or previously unmeasured phenomena is high novelty.

### 7.5 Pruning, Quantization, and Efficiency Papers

**Novelty expectations are about the efficiency-accuracy tradeoff:**

- Score 1–2: Applies existing compression technique to a new setting; accuracy numbers improve but the technique is not new
- Score 3: Diagnoses a specific failure mode of existing compression methods and addresses it
- Score 4: Removes a key approximation that prior work couldn't avoid, or enables a new class of models to be compressed

> From OBA (contribution=4): "Unlike previous methods that approximate the Hessian matrix, OBA calculates the full Hessian-vector product, providing a more accurate measure of parameter importance."

The novelty is precise: prior work approximated, OBA computes exactly. This is a principled improvement with a clear mechanism.

> From CAT (contribution=2–3): "It is novel to first cluster and then use affine transformation to correct residual errors."

The idea is novel but narrow (vision models only, no language/multimodal validation). This limits it to score 2–3 despite the genuine insight.

---

## 8. Calibration Guide: Score Boundaries in Practice

### The Score-2/3 Boundary (Most Common Judgment Call)

**Push toward score 2 when:**
- The core idea is genuinely new, but tested only in very restricted conditions (one model family, one dataset, one modality)
- The theoretical contribution analyzes an existing method without revealing anything counterintuitive
- The paper acknowledges that it makes strong simplifying assumptions and does not validate them
- Multiple reviewers say "interesting but limited"

**Push toward score 3 when:**
- At least one reviewer says "the idea is novel" without heavy qualification
- The paper covers multiple settings and the method generalizes across them
- The contribution either opens a new research direction OR validates a previously suspected but unconfirmed phenomenon
- The core idea is synthesis that required genuine insight, not just literature combination

### The Score-3/4 Boundary

**Push toward score 3 when:**
- The contribution extends existing work meaningfully but doesn't change how the field thinks about the problem
- The paper solves a specific instantiation of a general problem, not the general problem itself
- Reviewers say "good contribution" but don't use superlatives

**Push toward score 4 when:**
- Reviewers say "first to," "answers a fundamental question," "novel and well-motivated," or "natural extension"
- The paper's key insight is simple to state but wasn't obvious before the paper
- The contribution is general enough to apply to a research direction, not just one paper
- The paper introduces a concept, dimension, mechanism, or benchmark that future papers will use as a reference

### The Score-1/2 Boundary

**Push toward score 1 when:**
- The core claimed contribution is directly traceable to one or more specific prior papers
- The method doesn't outperform the baselines it claims to surpass
- Reviewers primarily list the prior methods that already covered the claim
- The only positive is "there is some novelty in..."

**Push toward score 2 when:**
- The paper identifies a real (if small) gap in prior work and fills it
- At least one genuine positive claim can be made about the contribution
- The method outperforms baselines in at least some settings
- The idea, while narrow, was not previously done in the specific way presented

---

## 9. Quick Reference Card

### Novelty Score Summary

```
Score 1 — Poor
  Signals: "There is SOME novelty in..." / Prior work already did this /
           Method doesn't beat baselines / Bio-inspired metaphor without model
  Ask: "Did any prior paper do essentially this?"

Score 2 — Below Average
  Signals: "Interesting BUT limited to..." / Analysis of existing method /
           One modality, one model family / Strong simplifying assumptions
  Ask: "Is the idea real but the scope too narrow to matter broadly?"

Score 3 — Good
  Signals: "The idea is novel" / "Well-motivated" / "Creative" /
           First theoretical foundation for X / Addresses recognized problem
  Ask: "Does this idea require genuine insight and cover enough ground?"

Score 4 — Excellent
  Signals: "Answers a fundamental question" / "First to..." /
           "Natural extension" / "Simple yet effective" / Opens research direction
  Ask: "If this paper didn't exist, what would the community be missing?"
```

### The Three Most Important Distinctions

1. **Novelty ≠ Soundness**: A well-executed incremental paper is still score 2. Don't confuse quality of execution with quality of idea.

2. **Novelty ≠ Difficulty**: An elegant simple idea can score 4. A complicated paper with lots of engineering can score 2. Reviewers reward insight, not effort.

3. **Application ≠ Contribution**: Applying method X to domain Y is only novel if the application required new insight. "We applied X to Y and it worked" is score 1–2. "We applied X to Y, but had to develop Z to make it work, and Z turns out to reveal..." is score 3–4.
