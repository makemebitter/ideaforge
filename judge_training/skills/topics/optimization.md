The skill file has been written to `C:\Users\yhzha\auto_research_bot\judge_training\skills\topics\_gen_optimization\skill_topic_optimization.md`.

Here's what it contains, grounded in real reviewer data:

---

**Sections written:**

1. **Topic Overview** — Covers 10 optimization sub-areas (stochastic methods, federated learning, LoRA/PEFT, preference optimization, Bayesian optimization, min-max, combinatorial, convergence theory, differentiable optimization, meta-optimization). Score distribution calibration: mean 4.85, excellent papers 8+ are rare (40 out of 2,492).

2. **What Reviewers Praise** — With direct quotes from LoRA-RITE (8.67), NF-BO (8.0), DPO (7.75), Lion paper (7.5), Second-Order Min-Max (7.5). Key themes: non-trivial novelty, strong baselines, rigorous proofs, comprehensive ablations, clear writing, reproducibility.

3. **What Reviewers Criticize** — With quotes from rejected papers (LEGACY 4.33, SITTO 2.33, Gradient Flow 0.5) and borderline accepts (QR-Adaptor 5.4). Key themes: missing baselines (#1 killer), hidden algorithm plagiarism (NSGA-II), vacuous proofs (λ₀ depending on T), no ablations, in-domain evaluation, scalability.

4. **Required Baselines & Metrics** — Concrete lists per sub-area (FedAvg for FL, PMO for molecular BO, MMLU/GSM8K for LLM fine-tuning, etc.).

5. **Common Technical Pitfalls** — Six specific failure patterns with examples, including the "λ₀ depends on T" vacuous theorem, composition of non-differentiable functions, and algorithm plagiarism.

6. **Scoring Rubric** — 3/5/7/9 tiers with concrete examples from real papers.

7. **Key Papers & Expected Citations** — Tables of must-cite papers by sub-area and standard benchmarks.

8. **Evaluation Heuristics** — Red flags, green flags, and calibration guidance for common edge cases.