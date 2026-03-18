# Clarity Dimension Skill File

> **Purpose:** This file teaches an AI judge how to evaluate the **clarity** dimension of a research paper on a 1–4 integer scale, mirroring the presentation sub-score used by top ML venues (ICLR, NeurIPS, ICML, etc.).
>
> Load this file whenever the evaluation task requires scoring or reasoning about clarity/presentation quality.

---

## 1. What "Clarity" Means in Peer Review

### Definition

**Clarity** (also called *presentation quality*) measures how well a paper communicates its contributions to its intended audience. A clarity score is not a measure of the paper's *importance* or *correctness* — it is purely about how effectively the authors convey what they did, why they did it, and what it means.

Reviewers assess clarity holistically across:

| Layer | Questions reviewers ask |
|---|---|
| **Macro-structure** | Is the paper logically organized? Does the narrative flow from problem → method → experiments → conclusions? |
| **Motivation & framing** | Is the problem clearly stated? Do readers quickly understand *why this matters*? |
| **Technical precision** | Are definitions, notation, and algorithms stated unambiguously? |
| **Figures & tables** | Do visuals reinforce the text rather than confuse it? Are axes, legends, and captions self-contained? |
| **Related work** | Is prior work cited accurately and positioned clearly relative to the new contribution? |
| **Language** | Is the prose grammatically correct, free of jargon overload, and readable by the target audience? |
| **Reproducibility scaffolding** | Are enough implementation details provided for the reader to follow the approach? |

### What clarity is NOT

- **Not originality.** A perfectly clear paper can still have incremental contributions.
- **Not correctness.** A technically wrong paper can be written with crystalline clarity.
- **Not length.** Clarity is not rewarded by length; a concise, dense paper can score 4; a bloated one can score 1.
- **Not polish alone.** A paper with near-zero typos but poor logical organization still has low clarity.

### The 1–4 scale at a glance

| Score | Label | One-line summary |
|---|---|---|
| 1 | Poor | The paper is difficult to follow; major organizational or expository failures |
| 2 | Below average | Intelligible in parts but has notable gaps, inconsistencies, or confusing sections |
| 3 | Good | Clear and well-organized; minor issues do not impede comprehension |
| 4 | Excellent | Exceptionally well-written; sets a standard for the community |

---

## 2. Score 1 — Poor Clarity

### What this looks like

A score-1 paper leaves the reviewer unable to reliably understand the core contribution without significant effort. Common failure modes:

- **Disorganized structure:** Sections do not build on each other; the reader cannot construct a coherent mental model of the method.
- **Missing or outdated related work:** Key baselines are unnamed, uncited, or mischaracterized, making it impossible to calibrate novelty.
- **Undefined concepts or notation:** Variables, acronyms, or model components are used before being introduced or are never formally defined.
- **Figures/tables that obscure rather than reveal:** Axes unlabeled, figures unexplained in the caption, or visuals that contradict the text.
- **Method description that cannot be replicated:** The algorithm is described at such a high level, or with so many implicit assumptions, that even an expert cannot reconstruct it.
- **Language barriers:** Grammar errors pervasive enough to cause ambiguity about technical claims.

### Common reviewer patterns at score 1

Reviewers citing score-1 clarity will often:
- Report they "cannot understand" the method from the paper alone.
- Flag specific sections as incomprehensible.
- Note that related work is missing or that key comparisons are absent.
- Use phrases like *"it is not clear how..."*, *"the paper does not explain..."*, *"no formal definition of..."*.

### Grounded examples from the real reviewer data

From the **BINR-MAPF** paper (presentation=1.0):

> *"The Related Work section seems to be quite outdated and very limited. MAPPO-MAPF is mentioned but not cited. What is the connection to other swarm-based algorithms (if any), for example, to this other swarm algorithm...?"*

This illustrates score-1 behavior: related work is incomplete to the point of factual omission (citing a method without a reference), and the positioning relative to the field is absent.

> *"It is not clear how this approach compares with many other bio-inspired algorithms (ant colony, particle swarm, etc.)..."*

A second reviewer on the same paper identifies the same structural gap: the method exists in a vacuum because the surrounding literature is not properly engaged.

### Scoring heuristics for score 1

Apply score 1 when **any two or more** of the following are true:
1. The method section cannot be understood without external resources.
2. Related work is missing, severely outdated, or misattributes prior work.
3. Key terms are undefined and used inconsistently.
4. Multiple figures or tables are uninterpretable from context alone.
5. Language errors cause genuine ambiguity in technical claims.

---

## 3. Score 2 — Below Average Clarity

### What this looks like

A score-2 paper is intelligible — an expert reader can eventually extract the main contribution — but requires substantial effort. The paper has real organizational or expository weaknesses that impede comprehension. Common patterns:

- **Excessive simplification in presented proofs or algorithms:** The authors oversimplify to the point where the theoretical analysis is no longer rigorous or general, and this is not clearly flagged.
- **Missing visualizations that would make abstract ideas concrete:** The text describes phenomena but does not show them; reviewers find themselves re-reading sections to build an intuition that a single figure would provide immediately.
- **Incomplete experimental descriptions:** Hyperparameters, dataset splits, or evaluation protocols are missing or buried in appendices without clear pointers.
- **Disconnected sections:** The introduction promises contributions that the experiments do not directly test, or the related work does not set up the method section.
- **Narrow or cherry-picked framing:** The paper presents results in a way that requires the reader to actively reconstruct the full picture.

### Common reviewer patterns at score 2

- Reviewers note the paper is "understandable in principle" but flag specific gaps.
- Complaints focus on *what is missing* rather than on confusion about what is present.
- Reviewers suggest specific additions: "a figure showing X would help", "the authors should clarify the setup of Y".

### Grounded examples from the real reviewer data

From **Revisiting Prefix-tuning** (presentation=2.0):

> *"Although the paper provides detailed theoretical proof of the effectiveness of the reparameterization strategy in prefix tuning, my main concern is about the technical contribution of the paper. Since the problem formulation simplifies the original framework significantly..."*

The reviewer can follow the proof but recognizes that the simplifications are not adequately flagged — the gap between what is proven and what is claimed is a clarity problem as much as a technical one.

> *"The lack of additional visualization results means that, despite the authors' analysis of the effectiveness of prompt techniques, there is a deficiency in more intuitive visual outcomes. As a reader, I find it difficult to intuitively understand the effectiveness of these techniques without visual representations."*

This is a canonical score-2 weakness: the text is comprehensible but relies entirely on abstract description where a figure would communicate far more efficiently.

From **CAT: Post-Training Quantization** (presentation=2.0):

> *"The paper does not provide any analysis of the inference-time overhead introduced by CAT. Although PCA and cluster assignment are claimed to be lightweight, they may still incur noticeable latency..."*

Three independent reviewers flagged the same missing analysis. When multiple reviewers independently identify the same gap, it is strong evidence of a clarity failure: the paper does not make its scope of claims transparent enough for readers to evaluate them.

From **T2VTextBench** (presentation=2.0):

> *"It is unclear how these 73 prompts were designed. What dimensions were considered? How were they selected?..."*

A methodology whose selection criteria are not explained is a classic score-2 clarity failure: the reader understands *what* was done but not *why* or *how*, which undermines the validity of the results.

### Scoring heuristics for score 2

Apply score 2 when:
- The paper is followable but requires significant inference by the reader.
- One or two key sections have notable gaps (missing ablations, missing visualizations, missing protocol details).
- The simplifications to theory or methodology are not made explicit.
- Multiple reviewers converge on the same specific missing element.
- No single failure is catastrophic, but the combined effect meaningfully impedes comprehension.

---

## 4. Score 3 — Good Clarity

### What this looks like

A score-3 paper is well-written, clearly organized, and communicates its contribution effectively. A careful reader can follow the paper without undue effort. Weaknesses at this level are minor — they may slow reading slightly or leave an isolated detail unclear, but they do not disrupt comprehension of the main contribution.

Common characteristics:

- **Coherent narrative arc:** Introduction → motivation → method → experiments → conclusions flow naturally.
- **Adequate but not exceptional figures:** Visualizations support the text; captions are sufficient but occasionally could be more self-contained.
- **Well-positioned related work:** Prior work is cited and contextualized, though perhaps not exhaustively.
- **Clear method description:** The approach can be understood and reproduced with reasonable effort.
- **Minor surface issues:** Occasional typos, mildly awkward phrasing, or one section that could be reorganized — but nothing that impedes understanding.

### Common reviewer patterns at score 3

- Reviewers describe the paper as "clearly written" or "easy to follow" in strengths, then note specific but minor improvements in weaknesses.
- Concerns are about scope, depth, or additional experiments — not about basic comprehension.
- Reviewers may note that a particular section is confusing without characterizing the whole paper as opaque.

### Grounded examples from the real reviewer data

From **Revisiting Prefix-tuning** (presentation=3.0, multiple reviewers):

> *"The paper is clearly written and includes useful foundational knowledge to help set-up the theoretical framework."*

This is the archetypal score-3 strength statement: clarity is affirmed, and a specific mechanism (foundational framing) is credited.

The weakness from the same reviewer:

> *"The beginning of Section 4 highlights the simplification of the theoretical analysis ('we focus only on the first head...'). This simplification could limit the generalizability of the results..."*

This is a score-3 weakness: one section is explicitly flagged as simplified, but the rest of the paper is comprehensible. The issue is localized, not pervasive.

From **BINR-MAPF** (presentation=3.0):

> *"Strong motivation grounded in distributed robotics challenges (latency, bandwidth). The reflex-based local control is conceptually clean and scalable."*

"Conceptually clean" is a direct clarity signal. The reviewer can follow the core idea.

Weakness on the same paper:

> *"The 'bio-inspired' claim is mostly metaphorical; there's no real biological modeling."*

This is a scope/framing weakness, not a comprehension failure — the paper is clear about what it does, but the framing overstates the connection to biology. This is a borderline clarity issue (misleading framing can impede accurate comprehension) but does not prevent understanding the technical content.

From **Linearly Decoding Refused Knowledge** (presentation=3.0):

> *"The paper is mostly easy to follow. It introduces a simple idea and performs experiments based on that. It also does a good job explaining the relation to prior work."*

This is a textbook score-3 summary: easy to follow, simple idea well-explained, prior work handled. The caveat ("mostly") and subsequent weaknesses about scope and contribution depth are why this is 3 and not 4.

### Scoring heuristics for score 3

Apply score 3 when:
- The paper can be understood by its target audience without requiring external references.
- Any flaws in clarity are localized (one section, one figure, one undefined term) rather than pervasive.
- Reviewer concerns are primarily about *content* (contributions, experiments, scope) rather than *communication*.
- At least one reviewer explicitly affirms that the paper is "clear", "well-written", or "easy to follow".
- Minor surface errors (typos, awkward sentences) exist but are rare.

---

## 5. Score 4 — Excellent Clarity

### What this looks like

A score-4 paper is a model of scientific communication. Reading it is effortless; even readers at the edges of the target subdomain can follow the main ideas. The presentation actively enhances the contribution's impact.

Hallmarks of score-4 clarity:

- **Exemplary narrative construction:** The paper tells a coherent story from first principles to final insight. Each section sets up the next.
- **Rigorous yet intuitive exposition:** Technical depth is matched by high-level intuition. Formal definitions coexist with plain-language explanations and examples.
- **Figures that stand alone:** Captions are complete; figures are interpretable without reading the body text. Visualizations make non-obvious phenomena obvious.
- **Generous reader guidance:** The paper anticipates reader confusion and addresses it proactively — through remarks, examples, running commentary, and pointers.
- **Immaculate language:** Prose is fluent, precise, and grammatically correct throughout. Rare typos do not affect comprehension.
- **Scoped claims:** Limitations and scope boundaries are stated explicitly, preventing misinterpretation.

### Common reviewer patterns at score 4

- Strengths sections are long and specific; weaknesses are either absent or contain only minor suggestions.
- Reviewers note that the paper will serve as a reference or benchmark for the community.
- Praise specifically mentions intuition, high-level guidance, or proactive reader support — not just "it is clear".

### Grounded examples from the real reviewer data

From **Barely Random Algorithms and Collective Metrical Task Systems** (presentation=4.0):

> *"The paper is very well written. All results are rigorously proven, but there is also a lot of intuition and high-level guiding of the reader. The solution is non-trivial and builds on fairly complex ideas..."*

This captures the score-4 ideal: rigorous AND intuitive, with the authors actively guiding the reader through complexity. The reviewer explicitly credits "high-level guiding" — a hallmark of proactive exposition.

From **Physics-Informed Regularization for Domain-Agnostic Dynamical System Modeling** (presentation=4.0):

> *"The idea of imposing time-reversal symmetry via a regularization term is novel and well-motivated. The implementation of the regularization term is simple yet the effect is visible. Overall the paper is well written."*

"Simple yet the effect is visible" reflects a clarity achievement: the authors made a potentially complex idea look easy without sacrificing rigor.

From **AlgoPerf** (presentation=4.0):

> *"Very minor typo: L382, 'framekworks' -> 'frameworks'..."*

When a reviewer's only criticism is a single typo, the paper has cleared the clarity bar entirely. The weakness section is effectively empty of substantive concerns.

The same paper's strength:

> *"The paper summarizes and analyzes the results of the AlgoPerf Training benchmark, providing a valuable focal point to the community for driving future progress..."*

Score-4 papers are not just clear — they are clear in a way that amplifies their impact. The presentation makes the contribution feel more significant than it would with weaker exposition.

From **Optimal Brain Apoptosis** (presentation=4.0):

> *"Unlike previous methods that approximate the Hessian matrix, OBA calculates the full Hessian-vector product, providing a more accurate measure of parameter importance and leading to more precise pruning."*

The reviewer can articulate the technical distinction precisely because the paper made it precise. When reviewers can reproduce technical distinctions in their own words, that is strong evidence of clarity success.

### Scoring heuristics for score 4

Apply score 4 when:
- No reviewer raises a clarity concern in their weaknesses (substantive or surface-level).
- Reviewers explicitly credit the *quality* of exposition, not just its adequacy.
- The paper provides both formal rigor and high-level intuition for non-trivial contributions.
- Figures are praised or treated as self-evident.
- Any mentioned flaws are cosmetic (single typos, minor formatting).
- The paper would serve as a writing model for PhD students in the area.

---

## 6. Red Flags & Green Flags

### Red flags — signals of low clarity (scores 1–2)

| Signal | Likely score impact |
|---|---|
| Related work section lacks citations for named methods | Score 1 |
| Key algorithm contains undefined variables or symbols | Score 1–2 |
| No figure or diagram for a complex multi-stage method | Score 1–2 |
| Multiple reviewers independently identify the *same* missing element | Score 2 |
| Theoretical analysis explicitly simplifies away the general case without acknowledgment | Score 2 |
| Experimental protocol (datasets, splits, metrics) underspecified | Score 2 |
| Paper claims broad applicability but evaluates only a narrow slice without flagging the gap | Score 2 |
| Captions that say "results are shown" without describing what to observe | Score 2 |
| Framing language (e.g., "bio-inspired") not matched by technical content | Score 2–3 |
| Conclusions are weak or generic ("future work may explore...") | Score 2–3 |

### Green flags — signals of high clarity (scores 3–4)

| Signal | Likely score impact |
|---|---|
| Reviewer's weakness section is entirely about *content* (scope, experiments) not *presentation* | Score 3–4 |
| Reviewer can articulate the core technical distinction in their own words | Score 3–4 |
| Explicit high-level guidance language: "the authors explain...", "the paper walks the reader through..." | Score 4 |
| Reviewer uses "well-written", "easy to follow", "conceptually clean" | Score 3 |
| Reviewer uses "very well written", "exceptional", "sets a standard", "will serve as a reference" | Score 4 |
| Only weakness is a single typo or minor formatting issue | Score 4 |
| Reviewers across different subdomain backgrounds all understand the contribution | Score 4 |
| Paper explicitly scopes limitations and discusses where results may not generalize | Score 3–4 |
| Figures described as "clear", "informative", or praised for standalone readability | Score 3–4 |
| Foundational concepts introduced before they are needed | Score 3–4 |

### Ambiguous signals (require context)

| Signal | Interpretation |
|---|---|
| "The paper is mostly easy to follow" | Score 3 (the hedge matters) |
| "The paper introduces a simple idea" | Neutral; may reflect genuine simplicity or underselling |
| Reviewer raises both clarity praise and content concerns | Clarity is likely 3; content is a separate dimension |
| No explicit comment on presentation | Default to 3; absence of complaint is not the same as excellence |
| One reviewer praises clarity; another cites a specific gap | Score 2–3; weight the specific concern |

---

## 7. Cross-Topic Patterns: How Clarity Expectations Differ by Research Area

Clarity is universal, but what it *looks like* varies by subdomain. An AI judge must calibrate expectations accordingly.

### Theory papers (e.g., online algorithms, statistical learning theory)

**Higher bar for formal rigor; lower bar for figures.**

Theory papers are expected to state theorems precisely, define all objects before use, and provide proof sketches in the body alongside complete proofs in appendices. Intuition is especially valued in theory papers because the formalism can be opaque. Reviewers explicitly credit "high-level guiding of the reader" (as seen in the Barely Random Algorithms paper).

*What constitutes clarity at score 4:* Rigorous definitions + readable proof strategy + clear delineation of where each assumption is used + at least one worked example or diagram illustrating the abstract result.

*Common failure mode:* Theorem statements that are technically correct but whose hypotheses are so complex that no reader can quickly understand when the result applies.

### Empirical ML papers (e.g., new architectures, training algorithms, benchmarks)

**Higher bar for experimental transparency; moderate bar for formalism.**

Reviewers expect complete experimental protocols: datasets, splits, hyperparameters, compute resources, and random seeds (or at minimum, aggregate statistics across runs). Clarity failures in empirical papers almost always manifest as missing experimental detail or figures that do not communicate what a fair comparison looks like.

*What constitutes clarity at score 4:* Method diagram + clear ablation design + tables with all relevant baselines + captions that explain what each result shows + discussion of where the method fails.

*Common failure mode (score 2):* Results reported on narrow benchmarks with no discussion of why those benchmarks were chosen; readers cannot evaluate generalizability claims.

### Benchmark/evaluation papers (e.g., T2VTextBench)

**Highest bar for methodology transparency; evaluators must be able to reproduce the benchmark.**

Benchmark papers are judged on whether the evaluation protocol is reproducible and whether the benchmark design choices are justified. Clarity failures include: unexplained prompt or data selection, unspecified annotation guidelines, no inter-annotator agreement, and unclear metrics.

*What constitutes clarity at score 4:* Complete description of data collection, annotation, and validation pipelines; justification of design choices; example instances showing what good/bad outputs look like; discussion of benchmark limitations.

*Common failure mode (score 2):* The benchmark exists but the reader cannot determine if it measures what it claims to measure, because the construction process is opaque.

### Safety/alignment papers (e.g., Linearly Decoding Refused Knowledge)

**Higher bar for framing precision; claims must match experimental scope.**

Safety papers often make claims with broad societal implications. Clarity requires that the scope of claims exactly matches the scope of experiments. Overstating generalizability (e.g., "aligned language models" when only models under 10B parameters were tested) is a clarity failure as much as a validity failure, because readers cannot accurately assess applicability.

*Common failure mode (score 2–3):* Paper headline claims ("knowledge that models refuse is linearly decodable") are not hedged to match the actual experimental coverage (two model families, small scale), leaving readers to infer scope.

### Systems/engineering papers (e.g., AlgoPerf benchmark analysis)

**Higher bar for engineering detail; reader must understand what the system actually does.**

Systems papers require precise description of the system's components, their interactions, and the measurement methodology. Clarity at score 4 means a practitioner reading the paper could implement the system or reproduce the evaluation without contacting the authors.

*Common failure mode (score 2):* "Our system achieves X" without explaining which component of the system is responsible for the gain, making it impossible to adopt the contribution.

---

## 8. Scoring Procedure for the AI Judge

When assigned a clarity score task, follow this procedure:

### Step 1: Read for comprehension failure

Ask: *Can I follow this paper as a knowledgeable reader in the field?*

- If substantial sections are incomprehensible or undefined: **lean toward 1–2.**
- If comprehensible throughout with isolated gaps: **lean toward 2–3.**
- If fully comprehensible: **proceed to Step 2.**

### Step 2: Audit key clarity elements

Check the following and note failures:

| Element | Check |
|---|---|
| Abstract | Does it clearly state problem, approach, and contribution? |
| Introduction | Does it motivate the problem and preview the solution? |
| Related work | Are key baselines cited and positioned relative to the new work? |
| Method | Can the approach be understood and (in principle) reproduced? |
| Figures/tables | Are visuals interpretable from caption + context alone? |
| Experiments | Is the evaluation protocol fully specified? |
| Conclusions | Do they accurately reflect what was demonstrated? |

Count the failures. Zero or one minor failure → **3–4**. Two or more notable failures → **2–3**. Systemic failures → **1–2**.

### Step 3: Apply the reviewer language heuristic

Scan reviewer comments for the language patterns in Section 6 (Red/Green flags). Anchor your score to the pattern that best matches.

### Step 4: Resolve ambiguity with subdomain calibration

Apply the calibrations from Section 7 to adjust expectations for the paper type.

### Step 5: Assign and justify

Assign an integer 1–4. Write one sentence grounding the score in a specific aspect of the paper (e.g., "Score 2: the method section omits the clustering criterion, and three reviewers independently flagged this gap.").

---

## 9. Quick Reference Card

```
SCORE 1 — POOR
  • Cannot follow the method without external help
  • Related work missing or badly incomplete
  • Undefined variables/notation used throughout
  • Figures uninterpretable
  • Example: BINR-MAPF (presentation=1.0): related work missing citations, comparisons absent

SCORE 2 — BELOW AVERAGE
  • Intelligible but requires effort
  • Specific section(s) have notable gaps
  • Theory/methodology simplifications not flagged
  • Multiple reviewers cite the same missing element
  • Example: CAT quantization (presentation=2.0): inference cost missing across 3 reviewers
  • Example: T2VTextBench (presentation=2.0): prompt selection criteria unspecified

SCORE 3 — GOOD
  • Fully followable by target audience
  • Minor, localized issues only
  • Reviewer concerns are about content, not comprehension
  • At least one reviewer affirms clarity
  • Example: Prefix-tuning paper (presentation=3.0): "clearly written" + one localized theory simplification
  • Example: Linearly Decoding (presentation=3.0): "mostly easy to follow"

SCORE 4 — EXCELLENT
  • Effortless to read; rigorous and intuitive
  • High-level guidance explicitly credited by reviewers
  • No substantive clarity weaknesses
  • Only typos/cosmetic issues flagged
  • Example: Barely Random Algorithms (presentation=4.0): "rigorous + lot of intuition + high-level guiding"
  • Example: AlgoPerf (presentation=4.0): only weakness is a single typo
```

---

*End of Clarity Dimension Skill File*
