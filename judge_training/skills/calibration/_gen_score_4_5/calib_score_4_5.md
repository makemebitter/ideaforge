# Calibration Skill: Score 4–5 Range (ICLR Average Rating ~3.5)

> **Purpose:** Teach an AI judge to recognize, describe, and assign scores in the 4–5 / 10 range for ML conference papers. All examples, reviewer quotes, and patterns are grounded in real ICLR 2024–2026 reviews.

---

## 1. Score Range Profile

### What "Score 4–5" Means at Top AI Conferences

On ICLR's discrete rating scale, individual reviewers use scores roughly as follows:
- **1–2**: Strong reject / reject
- **3**: Reject, not good enough
- **4**: Below acceptance threshold (sometimes described as "interesting but insufficient")
- **5**: Marginally below the acceptance threshold
- **6**: Marginally above the acceptance threshold
- **8**: Accept, good paper
- **10**: Strong accept

A **paper averaging 3.5** typically has a mix of 2s, 3s, 4s, and occasionally a 5 — all clustering **well below** the acceptance threshold of ~6. Yet at ICLR 2026, roughly half of all 3.5-average papers in this sample were **accepted** (decisions appear to be made with area-chair discretion overriding raw scores).

**In terms of a normalized 1–10 scale:**
- Score **4–5** ≈ "Borderline negative to borderline paper": there is a genuine idea, but it is undermined by one or more significant gaps — empirical, theoretical, or contextual.
- This tier is the **most common contested zone** at top venues. Papers here consume most area-chair bandwidth.

### Typical Decision Distribution at Score 4–5

Based on the 20-paper sample:
- ~50% Accept, ~50% Reject
- Accept decisions at this tier are often driven by: impact of the domain, quality of the core idea despite execution gaps, or the paper filling a genuine resource gap (dataset, benchmark)
- Reject decisions at this tier are driven by: fundamental conceptual flaw, insufficient differentiation from prior work, or results that simply don't support the claims

### How Common Is This Tier?

Very common. At large venues like ICLR, it is estimated that 25–40% of submitted papers fall into this rating band. It represents the "middle mass" — papers that are not obviously great or obviously bad.

---

## 2. Characteristic Patterns: Real Examples at This Score Level

### Example 1: *Thinking into the Future: Latent Lookahead Training for Language Models*
**Rating: 3.5 (avg) | Decision: Accept | ICLR 2026**
**Individual ratings: [4, 4, 4, 2]**

**Core idea:** A latent reasoning mechanism where hidden states are fed back into the model as "lookahead" tokens before committing to visible output. Supervised with future ground-truth tokens.

**Why reviewers liked it:**
> "Clever tool: Hidden 'think-then-speak' compute with dense j-step supervision; potentially useful for planning-style problems." (Reviewer 1)
> "Compelling Sudoku curve: Figure 4 shows performance improving as tau grows." (Reviewer 1)
> "A big limitation of Coconut from prior work was the computational slowdown of recurrence. While this is unavoidable in some sense, this work introduces a clever training procedure..." (Reviewer 3)

**Why it scored 3.5 and not higher:**
- **Task gap**: Strong results on synthetic planning tasks (Sudoku, mazes); *no* meaningful improvement on GSM8K or AQuA. One reviewer: "No setting seems to consistently outperform SFT."
- **Incremental contribution**: Reviewer 4 gave a 2, writing: "The paper proposes looping through the LLM stack to predict τ future tokens as an auxiliary objective... this is conceptually very similar to multi-token prediction (MTP)... MTP, looped transformers, and COCONUT have all been extensively evaluated in real-world, large-model scenarios — this paper's contribution remains mostly incremental."
- **Missing comparisons**: No comparison to Chain-of-Thought, Coconut, or MTP as direct baselines.
- **Presentation issues**: "Several places imply the latent lookahead is causal... an incomplete sentence 'tokens to the We perform an...'"

**Diagnostic:** Good idea building on established themes, compelling on synthetic tasks, fails to demonstrate real-world generalization. Overshadowed by recent concurrent work. Gets accepted because the direction is timely and the mechanism is genuinely novel if narrow.

---

### Example 2: *Less is Not Worse: Effective Reasoning Without Complete Reasoning Traces*
**Rating: 3.5 (avg) | Decision: Accept | ICLR 2026**
**Individual ratings: [4, 4, 4, 2]**

**Core idea:** "MidCut" — remove the redundant middle portion of LLM reasoning traces during both SFT training and inference. Motivated by attention weight analysis showing U-shaped importance.

**Why reviewers liked it:**
> "Simple and Effective Method: The work systematically reveals the existence of redundant information in reasoning trajectories... brings consistent benefits across multiple models/datasets." (Reviewer 2)
> "MidCut-SFT consistently outperforms the baseline (training with full trajectories) and other trimming strategies." (Reviewer 2)

**Why it scored 3.5 and not higher:**
- **Crowded space**: Reviewer 4 (rating=2): "There are so many papers which aim at finding the overthinking or underthinking in LRM... I believe the current paper is more like a homework assignment than a paper accepted by a conference."
- **Narrow model coverage**: All experiments on Qwen series only; "generalizability to other model families (e.g., LLaMA series) unverified."
- **Missing efficiency data**: "The paper only shows its impact on accuracy but does not provide actual efficiency improvement data (e.g., percentage reduction in generated tokens, latency reduction)."
- **Hyperparameter opacity**: Hyperparameter n=100/200 set per dataset without justification or sensitivity analysis.

**Diagnostic:** Solid empirical execution on a timely problem, but landing in a saturated subfield without adequate differentiation. Saves itself by empirical rigor even if novelty is modest.

---

### Example 3: *LLM as GNN: Graph Vocabulary Learning for Graph Foundation Model*
**Rating: 3.5 (avg) | Decision: Reject | ICLR 2025**
**Individual ratings: [5, 3, 3, 3]**

**Core idea:** Use LLMs to simulate GNN message-passing via sequential prompting; introduce "language-based IDs" to solve the OOV problem for graph nodes.

**Why reviewers liked it:**
> "The paper introduces a novel approach by employing multilayer LLMs to replicate the message-passing process of GNNs." (Reviewer 1)
> "Experimental results demonstrate the superiority of their model compared to existing LLM+GNN architectures." (Reviewer 1)

**Why it scored 3.5 and not higher:**
- **Overclaiming**: Reviewer 3 (rating=3): "The paper completely lacks theoretical and experimental support for its elaborated claims... Perhaps the biggest mistake in claiming the alignment with GNNs is the fact that GNNs are permutation-invariant models whereas all autoregressive LLMs are by default permutation-variant."
- **Scope mismatch with claim**: Billed as a "graph foundation model" but only works on text-attributed citation graphs. "The generalization... might be limited to the tasks and datasets used for fine-tuning."
- **Missing baselines**: "Table 1 didn't include those strong baseline models, such as TAPE."
- **Misleading framing**: Reviewer 3: "The paper repeatedly claims that 'existing methods treat nodes as OOV tokens' whereas the vast majority of 'LLMs for graphs' approaches do exactly the same as PromptGFM."

**Diagnostic:** Novel application idea, but the claims dramatically exceed what the experiments support. The title and abstract promise a "graph foundation model" delivering universal vocabulary; the reality is a text-graph system for citation datasets.

---

### Example 4: *QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead*
**Rating: 3.5 (avg) | Decision: Reject | ICLR 2025**
**Individual ratings: [3, 3, 5, 3]**

**Core idea:** Apply a Johnson-Lindenstrauss transform before 1-bit quantization of KV caches, preserving inner product estimates with theoretical guarantees and "zero overhead."

**Why reviewers liked it:**
> "The approach proposed in this paper is innovative, utilizing random projections and norm storage during the compression process..." (Reviewer 1)
> "The mathematical proofs are rigorous and reliable, providing a solid estimation of the error bounds." (Reviewer 1)

**Why it scored 3.5 and not higher:**
- **"Zero overhead" is incorrect**: Reviewer 2: "QJL has the non-zero overhead of 1 bit, which is the same overhead as KIVI for storing the quantization constants... QJL is performing worse (in average accuracy) in all 3 comparisons in Table 1 against existing methods."
- **Incomplete paper**: "The 'Conclusion' and 'Related Works' sections are missing from the paper. The paper ends abruptly after experiments."
- **Marginal or negative empirical results**: "The improvements over the baselines are marginal. Furthermore, on certain datasets, QJL are considerably worse than the baselines by a few points."
- **Limited experimental coverage**: Only tested at select bit-widths; no throughput evaluation; no reasoning benchmarks.

**Diagnostic:** Theoretical novelty exists (JL transform is a creative angle), but empirical results do not support the claims, a core claim ("zero overhead") is factually wrong, and the paper is submitted in an incomplete state.

---

### Example 5: *Safeguarding System Prompts for LLMs (PromptKeeper)*
**Rating: 3.5 (avg) | Decision: Reject | ICLR 2025**
**Individual ratings: [3, 3, 5, 3]**

**Core idea:** Detect system prompt leakage via a mutual information (MI) / log-likelihood ratio test; if leakage is detected, regenerate the response without the system prompt.

**Why reviewers liked it:**
> "The authors aim to derive a defense from first principles... I think that the paper follows a sensible approach." (Reviewer 2)
> "The paper is overall well-written, self-contained, and provides sensible intuition." (Reviewer 2)

**Why it scored 3.5 and not higher:**
- **Fundamental conceptual flaw**: Reviewer 4 (rating=3): "Mutual information between the LLM response and the prompt [is] zero only if they are statistically independent. A system prompt that has zero statistical influence on responses is useless. Simply throw away the system prompt, no need to worry about its confidentiality."
- **Defense defeats its own purpose**: Reviewer 1: "Practically, specialized system prompts (e.g., system prompt for an online banking chatbot) are the ones worth stealing, and having a 'no system prompt' online banking chatbot defeats its purpose."
- **Circular evaluation**: "The evaluation measures response quality and adherence to the system prompt in a combined metric, but should use two separate metrics."
- **Non-adaptive evaluation**: "The evaluation should also consider adaptive attacks... since this is a worst-case defense, it should report the maximum attack success."

**Diagnostic:** A principled security paper with elegant framing, but the security definition is self-contradictory. The fallback mechanism (drop the system prompt) trivially breaks the system's utility. This illustrates how a paper can be well-written and well-motivated yet still fundamentally broken at the concept level.

---

### Example 6: *Hijacking JARVIS: Benchmarking Mobile GUI Agents against Unprivileged Third Parties*
**Rating: 3.5 (avg) | Decision: Reject | ICLR 2026**
**Individual ratings: [4, 4, 2, 4]**

**Core idea:** Benchmark for mobile GUI agent robustness against adversarial third-party content, including an Android simulator (AgentHazard) and a 3000+ scenario static dataset.

**Why reviewers liked it:**
> "The combination of a dynamic interactive environment and a large-scale static dataset provides both high ecological validity and reproducibility." (Reviewer 1)
> "The paper reveals key trends — particularly that multimodal perception increases susceptibility to misleading content, while domain-specific GUI training enhances robustness." (Reviewer 1)

**Why it scored 3.5 and not higher:**
- **Unclear novelty over prior work**: Reviewer 1: "What is the fundamental difference between third-party attacks and traditional pop-up–based attacks? From the standpoint of agent security and defense, third-party attacks can essentially be viewed as a special case of pop-up attacks."
- **Threat model inconsistency**: Reviewer 4: "Real third parties can plausibly control in-app content regions, but they cannot modify another app's UI tree; the paper should more clearly separate realistic adversary control from tool convenience."
- **Limited model coverage**: Only one GUI-specialized model (UI-TARS-1.5) tested; Reviewer 2 notes end-to-end trained models like Mobile-Agent-v3 may differ.
- **No root-cause analysis**: Reviewer 3: "The paper shows what fails but not why. It never explores why visual models are weaker... without tools like attention maps or gradient analysis, the study stays at a surface level."

**Diagnostic:** Solid benchmark engineering, meaningful empirical findings, but the paper fails to establish clearly what it contributes beyond prior security benchmarks. The threat model has practical gaps and the analysis is more descriptive than explanatory.

---

### Example 7: *Holistic Prompting: Joint Reasoning with Reusable States and Shortcut Discovery*
**Rating: 3.5 (avg) | Decision: Reject | ICLR 2026**
**Individual ratings: [4, 2, 4, 4]**

**Core idea:** A graph-of-thoughts framework where intermediate reasoning states are shared across input instances, enabling "memoization" of subproblems. Uses exact-match state reuse.

**Why reviewers liked it:**
> "The proposed approach connects unsolved problem instances to already-explored reasoning paths from other samples, which is a good contribution. It is similar to dynamic programming." (Reviewer 2)
> "The proposed method is efficient in terms of tokens generated compared to ToT." (Reviewer 3)

**Why it scored 3.5 and not higher:**
- **Exact-match requirement kills generalization**: Reviewer 1: "Since the matched intermediate states must be very/exactly similar and are low-level states without any abstraction, it is hard to see how this method could extend beyond problems with very simple input and intermediate token sequences."
- **Narrow experimental scope**: Tested on only 2 tasks; Reviewer 3: "Game24 is a quite old synthetic dataset... the second experiment didn't use LLMs at all."
- **Unclear applicability boundary**: When reusable sub-structures are absent (most real-world NLP), the entire mechanism provides no benefit.
- **Presentation issues**: Reviewer 4: "The descriptions are filled with jargon and not simple, intuitive explanations or illustrations."

**Diagnostic:** The dynamic-programming analogy is elegant and genuinely novel; the shortcut discovery mechanism is interesting. But "exact match" as the reuse criterion is so restrictive it limits the method to structured combinatorial tasks, which is a fatal scope limitation for an ICLR paper.

---

### Example 8: *AnyCap: Omni-Modal Captioning with Instruction Alignment*
**Rating: 3.5 (avg) | Decision: Reject | ICLR 2026**
**Individual ratings: [4, 4, 4, 2]**

**Core idea:** A plug-and-play residual-correction framework for instruction-following captioning across images, video, and audio. Introduces a new dataset (AnyCapData, 300K) and benchmark (AnyCapEval).

**Why reviewers liked it:**
> "The empirical results are strong and convincing. The paper is well-written, clearly structured, and easy to follow." (Reviewer 4)
> "Plug-and-play residual editor, unified across modalities... easy to attach to existing pipelines." (Reviewer 2)

**Why it scored 3.5 and not higher:**
- **Derivative methodology**: Reviewer 4 (rating=2): "The core training paradigm of AnyCap—using a smaller model to learn a residual correction over the output of a larger, frozen model—is heavily inspired by, if not identical to, the method proposed in Aligner."
- **Data construction not novel**: "The practice of using powerful proprietary models to synthesize large-scale, instruction-rich datasets... is now a well-established paradigm."
- **Evaluation circular**: Both AnyCapEval and training data rely on GPT-4o, creating a potential feedback loop favoring GPT-4o style output.
- **Engineering vs. research**: "The paper presents a powerful and useful system, but its contributions are primarily in engineering and system-building rather than in creating new techniques for the academic community."

**Diagnostic:** Strong execution, strong empirical results, but the core technical contribution is adaptation of known technique (Aligner) to a new setting. Reviewers consistently classify this as "application paper" rather than "research paper," which places it below the ICLR bar despite clear practical value.

---

## 3. Common Traits: What Papers at Score 4–5 Almost Always Share

### Universal Trait 1: There Is a Genuine Contribution

Every paper at this level has something real. This is what distinguishes score 4–5 from score 1–3. The judge must identify what it is:
- A novel mechanism or architectural choice (latent lookahead, QJL transform, state reuse graph)
- A useful dataset or benchmark (AnyCapData, JARVIS benchmark, TRAUMA THOMPSON)
- An interesting empirical finding (MidCut's U-shaped attention, QUTCC conformal calibration)
- A reasonable application of known techniques to a new domain

**If you cannot identify a genuine contribution, score 1–3, not 4–5.**

### Universal Trait 2: A Critical Unresolved Concern

But there is always at least one fundamental problem that reviewers cannot overlook:
- **Generalization failure**: Works on synthetic tasks / specific domains, fails on real benchmarks
- **Conceptual flaw**: The core formulation is incorrect or self-defeating (PromptKeeper's MI definition, QJL's "zero overhead" claim)
- **Overclaiming**: Paper claims X but only shows Y (LLM as GNN claims "universal," only shows citation graphs)
- **Derivative methodology**: The technique is essentially a combination/application of 2+ known prior works without sufficient new insight

### Universal Trait 3: Reviewer Disagreement (The Signature of This Tier)

Score 3.5 papers almost always produce a **bimodal review distribution**:
- Typically: [4, 4, 4, 2] or [4, 4, 2, 4] or [3, 3, 5, 3] or [5, 3, 3, 3]
- There is almost always one reviewer who sees the value and one who identifies the fatal concern
- If all reviewers agree (all 4s or all 2s), the paper is probably NOT in this tier

### Universal Trait 4: Missing Ablations or Baselines

Nearly every score 3.5 paper has an obvious comparison or ablation that reviewers demand:
- "Why isn't MTP/Coconut/Chain-of-Thought a baseline?" (Latent Lookahead)
- "TAPE is missing from the baselines." (LLM as GNN)
- "No comparison with n-gram output filtering which is stronger than your cosine similarity baseline." (PromptKeeper)
- "Only 2 tasks evaluated; Game24 is old." (Holistic Prompting)
- "All experiments on Qwen; no LLaMA." (MidCut)

### Universal Trait 5: Narrow Evaluation Scope

Works well in restricted settings:
- Only one model family tested
- Only synthetic or specialized benchmarks
- Only one domain within a broader claim
- Missing efficiency/latency data when efficiency is the selling point

### Universal Trait 6: Overclaiming / Misleading Framing

The abstract and introduction promise more than the body delivers:
- "Zero overhead" → actually has the same overhead as the baseline
- "Graph foundation model" → only works on text-attributed citation graphs
- "Consistent improvements" → contradicted by the results in the paragraph above the claim
- "First systematic investigation" → prior work did essentially the same thing

### Universal Trait 7: Crowded Subfield Without Adequate Differentiation

Many score 3.5 papers are in active, saturated areas:
- LRM reasoning efficiency (MidCut): "There are far too many such papers"
- GUI agent security (JARVIS): Prior pop-up attack benchmarks exist
- KV cache compression (QJL): KIVI, KVQuant, QuaRot already cover the space
- Graph+LLM (LLM as GNN): OFA, GraphText, TAPE already close related work

The paper must clearly articulate *why* the new contribution is needed beyond incremental improvement.

### Distinguishing Score 4–5 from Adjacent Tiers

| | Score 2–3 | Score 4–5 | Score 6–7 |
|---|---|---|---|
| Genuine contribution | Unclear or absent | Present but flawed | Clear and solid |
| Empirical results | Weak or cherry-picked | Mixed or narrow | Comprehensive |
| Reviewer consensus | Mostly rejection | Split | Mostly acceptance |
| Core mechanism | Broken or trivial | Interesting but limited | Well-validated |
| Related work coverage | Missing key citations | Gaps in differentiation | Comprehensive |
| Overclaiming | Severe | Moderate | Minimal |
| Presentation | Often poor | Acceptable to good | Good to excellent |

**Key boundary at score 4–5 vs 6–7:** At score 6–7, the main experiments work on *real, diverse benchmarks* and the paper's claims are *supported by the results*. At score 4–5, there is at least one significant experiment that either fails, is missing, or contradicts the claim.

**Key boundary at score 4–5 vs 2–3:** At score 2–3, reviewers cannot identify a genuine contribution, or the fundamental approach is broken from the start. At score 4–5, *something* works — the mechanism is sound, results improve in some setting, the dataset is real and useful. The problem is the gap between what works and what is claimed.

---

## 4. "This Paper Is a Score 4–5 Because..." Templates

These templates are directly grounded in real reviewer patterns from the papers above. A judge can use them as-is or adapt them:

---

**Template 1 — Works on Synthetic, Fails on Real (generalization gap)**
> "This paper is a score 4–5 because the core mechanism shows genuine promise — [brief description of method] demonstrates strong improvements on [synthetic/specific task]. However, when evaluated on [real benchmark], the results are near-baseline or negative. The authors claim '[quote from paper]' but the results in their own tables contradict this. This gap between synthetic success and real-world failure is the defining weakness of papers at this score level."

*Grounded in: Latent Lookahead (Sudoku works, GSM8K fails), Holistic Prompting (Game24 works, no real NLP tasks), QJL (theory works, empirics don't).*

---

**Template 2 — Novel Idea, Incremental Execution**
> "This paper is a score 4–5 because the underlying idea — [brief description] — is interesting and worth pursuing, but the execution is insufficiently differentiated from prior work. Specifically, [prior work A] and [prior work B] already demonstrated [core mechanism] in comparable settings. The paper's contribution reduces to applying these existing ideas to [new domain], without providing new theoretical insight or demonstrating superiority over these baselines (which are absent from the experiments)."

*Grounded in: MidCut (LRM overthinking is saturated), AnyCap (residual correction = Aligner), Latent Lookahead (MTP + looped transformers + Coconut).*

---

**Template 3 — Fundamental Conceptual Flaw**
> "This paper is a score 4–5 because the problem is well-motivated and the execution is careful, but the core formulation contains a fundamental flaw that undermines the entire approach. Specifically, [describe flaw]. This is not a fixable weakness — it requires rethinking the approach from scratch. Despite this, the paper earns a score in this range because the presentation is competent and the motivation is real; the flaw is non-obvious and took expert reviewers to articulate clearly."

*Grounded in: PromptKeeper (zero MI = drop system prompt), QJL ("zero overhead" is wrong).*

---

**Template 4 — Overclaiming / Scope Mismatch**
> "This paper is a score 4–5 because a genuine contribution exists — [what actually works] — but the paper systematically overstates its scope. The title and abstract claim [X], but the experiments only support [Y, which is much narrower]. Reviewers consistently identify the mismatch: e.g., '[quote showing overclaiming]' versus the actual experimental setup '[what experiments show]'. The paper would be stronger if it accurately scoped its claims and evaluated within the boundaries it actually demonstrates."

*Grounded in: LLM as GNN ("universal" graph vocabulary only on text citation graphs), AnyCap ("first omni-modal" claim vs prior work), JARVIS benchmark (novelty over pop-up attacks unclear).*

---

**Template 5 — Missing Baselines / Missing Ablations**
> "This paper is a score 4–5 because the most obvious comparison is absent. [Method X] directly addresses the same problem with comparable or stronger performance, yet it does not appear in the experiments. Without this comparison, it is impossible to assess whether the proposed approach provides meaningful gains over the state of the art. Additionally, [key design choice Y] is never ablated, making it unclear whether it drives the reported improvements."

*Grounded in: Latent Lookahead (no MTP or Coconut baseline), LLM as GNN (no TAPE), PromptKeeper (no n-gram filter baseline), Holistic Prompting (no Graph of Thoughts, Buffer of Thoughts baselines).*

---

**Template 6 — Benchmark / Dataset Paper with Shallow Analysis**
> "This paper is a score 4–5 because it makes a real empirical contribution — [dataset or benchmark] fills a genuine gap — but the analysis stays at a descriptive level. The paper shows *what* happens (e.g., models are vulnerable, performance degrades) but does not explain *why*, and the set of tested models/methods is too narrow to support generalizable conclusions. Specifically, [key missing analysis or missing model type]. A score 6+ benchmark paper would include ablations, mechanistic insights, or broader coverage."

*Grounded in: JARVIS (no root-cause analysis for visual vulnerability), TRAUMA THOMPSON (dataset is small and annotation methodology is questioned), AnyCap (dataset construction methodology is standard pipeline work).*

---

**Template 7 — Narrow Evaluation Kills Generalizability**
> "This paper is a score 4–5 because the results, while positive, are confined to a narrow experimental setup that cannot support the broad claims. All experiments use [one model family / one task type / one benchmark], leaving the generalization question open. Reviewers specifically request [LLaMA series / broader datasets / more diverse tasks], and without those, the paper cannot demonstrate that its contribution is general rather than architecture- or domain-specific."

*Grounded in: MidCut (all Qwen, AIME/MATH/GPQA only), ATHENA-Serve (single GPU, single model), UES (outdated baselines, simple datasets), QUTCC (minor improvement over baseline).*

---

**Template 8 — Crowded Field, Insufficient Differentiation**
> "This paper is a score 4–5 because it operates in a saturated subfield without adequately explaining why it is needed. There are already [N] papers addressing [same problem], including [closest prior work A] and [closest prior work B]. The proposed method offers [marginal gain / comparable performance / no clear advantage] over these. The paper would need to either demonstrate a clear empirical advantage on standard benchmarks or provide a fundamentally new angle (theoretical insight, new capability, new setting) to justify publication at a top venue."

*Grounded in: MidCut (LRM efficiency papers are too many), QJL (KIVI/KVQuant already solve KV quantization), Holistic Prompting (CoT/ToT/GoT landscape is crowded).*

---

**Template 9 — Good Engineering, Weak Academic Contribution**
> "This paper is a score 4–5 because it represents solid engineering — the system works, the results are real, and the problem is important — but it lacks the academic contribution expected at a top ML venue. The methodology is a competent application of existing components ([A], [B], [C]) without new technical insight. The evaluation is comprehensive but relies on custom metrics whose validity is questionable. This is valuable industrial work, but ICLR expects either new theory, new methodology, or new fundamental understanding."

*Grounded in: AnyCap (Aligner + multi-modal = engineering application), ATHENA-Serve (scheduler is rule-based without ML contribution), DLM (data collection from near-expert MARL agent undermines the RL framing).*

---

**Template 10 — Split Reviewers Signal Borderline**
> "This paper is a score 4–5 because the reviewers are genuinely split: one or two reviewers see a meaningful contribution and give [4–5], while one reviewer identifies a fundamental concern and gives [2–3]. This bimodal distribution is itself diagnostic of this score range. The judge should read the strongest negative review carefully: if it identifies a [conceptual flaw / missing comparison / scope mismatch / generalization failure], the paper almost certainly belongs at 4–5 or below, not 6+. The presence of enthusiastic positive reviews does not override a fundamental technical concern."

*Grounded in: All 8 examples above share this bimodal distribution.*

---

## 5. The Score 4–5 Decision Rubric

When a paper has been analyzed, use this rubric to confirm the score:

**Checklist for Score 4–5 (all should be true):**
- [ ] A genuine contribution is identifiable (novel mechanism, useful resource, interesting finding)
- [ ] At least one significant unresolved concern exists (generalization failure, conceptual flaw, overclaiming, missing baselines)
- [ ] Reviewer opinions would likely be split (not unanimously positive or negative)
- [ ] The paper's claims exceed its demonstrated results in at least one material way
- [ ] At least one obvious comparison or ablation is missing

**If fewer than 3 of 5 apply → consider score 6+ (the paper may be stronger than score 4–5)**
**If all 5 apply with severe versions of each → consider score 2–3 (the paper may be weaker)**

The key calibration question: **"If the missing experiment / ablation / baseline were done and came out positive, would the paper clearly deserve acceptance?"** If yes → score 4–5 with upward potential. If no (because the fundamental concept is flawed, not just the experiments) → score 3–4.

---

## 6. Anti-Patterns: What Score 4–5 Is NOT

**Do NOT assign score 4–5 to a paper that:**
- Has a fundamental logical impossibility at its core that no experiment could fix (this is score 1–3)
- Provides no novel contribution at all — it is purely incremental work with no differentiating angle (score 2–3)
- Has comprehensive, strong results on diverse benchmarks with a clear contribution (score 7–8)
- Is a well-executed survey or position paper with limited experimental claims (these have different scales)

**Do NOT confuse "borderline" with "average":**
- Score 4–5 papers are NOT mediocre papers. They are often ambitious papers with a clear vision that fall short in execution.
- The best score 4–5 papers are intellectually stimulating and sometimes influential despite rejection (or conditional acceptance).

**Do NOT let presentation quality dominate:**
- A well-written score 4–5 paper is still score 4–5.
- A poorly-written score 6–7 paper should not be dragged into 4–5 territory.
- Writing quality adjusts the score by at most 0.5 points in this tier.

---

## 7. Calibration Summary Table

| Paper | Avg Rating | Decision | Primary Failure Mode |
|---|---|---|---|
| Latent Lookahead | 3.5 | Accept | Generalization gap (synthetic → real); incremental vs. MTP |
| MidCut (Less is Not Worse) | 3.5 | Accept | Crowded field; narrow model coverage; missing efficiency data |
| LLM as GNN | 3.5 | Reject | Overclaiming ("universal"); missing baselines; conceptual flaw in MI analogy |
| QJL | 3.5 | Reject | Core claim ("zero overhead") is factually wrong; marginal/negative empirics |
| PromptKeeper | 3.5 | Reject | Fundamental definitional flaw (zero MI = useless system prompt) |
| Hijacking JARVIS | 3.5 | Reject | Novel vs. prior work unclear; threat model inconsistency; no root cause analysis |
| Holistic Prompting | 3.5 | Reject | Exact-match reuse kills generalization; only 2 tasks; jargon-heavy presentation |
| AnyCap | 3.5 | Reject | Derivative methodology (= Aligner); engineering > research; circular evaluation |

**The pattern:** When a paper is rejected at this score, there is usually *one* clearly articulable reason that is hard to fix. When it is accepted, the contribution (however narrow or incremental) is real and the community judges that it adds *something* worth having in the proceedings.

---

*This skill file was grounded in real ICLR 2024–2026 review data. All quotes are verbatim from reviewer submissions.*
