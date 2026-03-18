The skill file has been written to `judge_training/skills/topics/_gen_self_supervised/skill_self_supervised.md`. Here's a summary of what it covers:

**Structure (~14,000 tokens):**

1. **Area Overview** — Taxonomy of SSL paradigms (contrastive, masked prediction, generative, self-distillation, multi-modal, graph, theory) and application domains
2. **Rating Scale Calibration** — What each score (1–8) means, anchored to the 78.7% acceptance rate and 4.92 mean rating from the 1,909-paper corpus
3. **Reviewer Priorities** — The top strength/weakness phrases analyzed from real reviews (baselines, ablations, novelty are the dominant axes of judgment)
4. **Evaluation Rubric** — 5-dimension scoring (Novelty, Soundness, Experiments, Presentation, Significance) with explicit 1–4 descriptors for each
5. **High-rated paper patterns** — What Rating-8 papers have in common (testable hypothesis, theory+empirics, broad experiments, novel problem formulation)
6. **Low-rated paper patterns** — The "glue" anti-pattern, missing baselines, scope limitations, incomplete ablations, unjustified design choices
7. **Sub-area specific expectations** — Per-domain expected baselines and benchmarks for contrastive learning, masked autoencoding, multi-modal SSL, domain-specific SSL, and theory
8. **Common reviewer questions** — By paper type (method, analysis, theory, domain-specific)
9. **Scoring guidelines** — How to map the 5-dimension assessment to a final 1–8 rating
10. **Red flags** — 7 issues requiring explicit comment (label leakage, undertuned baselines, missing key citations, etc.)
11. **SSL concepts glossary** — Collapse, alignment/uniformity, augmentation design, key losses, multi-modal phenomena
12. **Evaluation checklist** — Systematic checklist for novelty, soundness, experiments, presentation, and red flags
13. **Calibration examples** — Three real papers mapped to their ratings with reasoning (two accepted at 7.5–8.0, two rejected at 3.8)
14. **Final guidance** — Decision heuristics for borderline cases