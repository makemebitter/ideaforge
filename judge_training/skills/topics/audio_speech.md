The skill file has been written to `judge_training/skills/topics/_gen_audio_speech/skill_topic_audio_speech.md`.

Here's a summary of what was produced:

**Skill file: `audio_speech` (~10 sections, ~12K tokens)**

Based on reading 7 actual paper reviews spanning all tiers:
- **High (8.0)**: MSDM (Oral), LLM Noise-Robust ASR (Spotlight), NaturalSpeech 2 (Spotlight)
- **Mid-high (7.0–7.5)**: MMAU benchmark (Spotlight), I Can Hear You deepfake detection
- **Low (4.25, Reject)**: SONAR deepfake benchmark, Self-tailoring ASR prompts

**Key findings grounded in real reviewer quotes**:

1. **Topic overview**: 10 sub-areas (ASR, TTS, enhancement/separation, speech LLMs, speech tokenization, music, general audio, audio-visual, deepfake detection, datasets) with score calibration for 531 papers.

2. **What reviewers praise**: Novelty of core mechanism, strong baselines, comprehensive ablation, clear writing, reproducibility + demo pages, scalability/generalization.

3. **What reviewers criticize**: Missing baselines (#1 killer), limited novelty/incremental (#2), unclear claims (97x "unclear whether"), limited evaluation scope (single dataset/language), no human evaluation for generative work.

4. **Sub-area specific expectations** — concrete baselines, metrics, and pitfalls for ASR, TTS, music, audio LLMs, speech tokenization, enhancement/separation, deepfake detection, and dataset papers.

5. **Technical pitfalls**: MOS evaluation rigor, FAD sensitivity, ASR evaluation (data contamination, LM integration), codec rate-distortion tradeoffs, diffusion NFE comparisons, speech LLM modality gap.

6. **Expected citations** by sub-area with conditions for suspicious absence.

7. **Scoring rubric** with concrete examples (SONAR/self-tailoring ASR for 2–4, deepfake detection for 6–7, MSDM/NaturalSpeech 2 for 8).

8. **10-point checklist** covering novelty, baselines, evaluation, ablations, reproducibility, and clarity.