# Skill File: Evaluating Research in Audio & Speech

**For use by AI judge agents evaluating submissions in the "audio_speech" topic area.**

---

## 1. Topic Overview

### What This Area Covers

"Audio & Speech" at ICLR/NeurIPS/ICML is a broad category encompassing any work whose primary contributions involve acoustic signals: from raw waveforms and codec representations to high-level semantic understanding. The main sub-areas are:

1. **Automatic Speech Recognition (ASR)**:
   - *Acoustic modeling*: End-to-end (CTC, RNN-T, attention-encoder-decoder), Whisper-style encoder-decoder, streaming vs. offline.
   - *Self-supervised pre-training for ASR*: HuBERT, wav2vec 2.0, WavLM, data2vec adaptation for downstream ASR.
   - *Noise-robust ASR*: Generative error correction (GER), N-best hypothesis reranking, LLM-based post-processing, denoising-before-ASR pipelines.
   - *Low-resource / multilingual ASR*: Code-switching, cross-lingual transfer, few-shot adaptation.
   - *Parameter-efficient ASR fine-tuning*: LoRA / adapter / soft-prompt tuning for foundation speech models.
   - *Pseudo-labeling and semi-supervised ASR*: CTC-guided pseudo-labeling, self-training on unlabeled audio.

2. **Text-to-Speech (TTS) and Voice Synthesis**:
   - *Neural TTS*: FastSpeech-family (non-autoregressive), VITS (VAE + flow + GAN), codec-language-model-based (VALL-E, VoiceBox, SoundStorm).
   - *Latent diffusion TTS*: NaturalSpeech 2 and successors, flow-matching TTS (P-Flow, Voicebox, E2 TTS).
   - *Zero-shot speaker adaptation*: Prompt-based TTS, speaker encoder conditioning, voice cloning.
   - *Controllable TTS*: Prosody control, style control, emotion control, text-prompt-driven voice design (PromptTTS).
   - *Neural vocoders*: HiFi-GAN, WaveGlow, Vocos, EnCodec, DAC/RVQGAN, BigVGAN.
   - *Speech synthesis evaluation*: MOS, CMOS, speaker similarity, intelligibility (WER), naturalness.

3. **Speech Enhancement, Denoising, and Separation**:
   - *Single-channel enhancement*: Mask-based (time-domain, frequency-domain), generative (diffusion, flow-matching), metric-learning approaches.
   - *Audio source separation*: Music stem separation (Demucs, MSDM), speech separation (Conv-TasNet, DPRNN, SepFormer).
   - *Audio-visual speech separation*: Lip-guided separation, bimodal SSL.
   - *Bandwidth extension / codec enhancement*: Audio super-resolution, neural audio coding.

4. **Speech and Audio Language Models (SpeechLLMs / AudioLLMs)**:
   - *Modality-alignment*: Connecting speech encoders to LLM decoders (BLSP, Qwen-Audio, Gemini-style late fusion).
   - *Speech-aware LLMs*: Models that can hear and generate speech (full-duplex, speech dialogue systems).
   - *Audio understanding LLMs*: Models evaluated on MMAU, ClothoQA, AudioCaps-QA, or similar reasoning benchmarks.
   - *Spoken QA and instruction following*: Models that perform general language tasks over spoken input.

5. **Speech Tokenization and Coding**:
   - *Semantic speech tokens*: HuBERT/CPC-based discrete units for language modeling over speech.
   - *Acoustic speech tokens*: RVQ-based codec tokens (EnCodec, DAC) for high-fidelity reconstruction.
   - *Hybrid tokenizers*: Models separating content, speaker, and prosody into different token streams.
   - *Neural audio codecs*: High-fidelity compression (RVQGAN, Lyra, Opus-ML).

6. **Music Understanding and Generation**:
   - *Symbolic music generation*: Transformer-based (Music Transformer, MuseNet), diffusion-based, hierarchical.
   - *Audio music generation*: MusicLM, MusicGen, AudioLDM, MSDM, Presto.
   - *Music source separation*: MDX, Demucs, MSDM.
   - *Music understanding*: MERT, music tagging, music captioning, genre/mood classification.
   - *Music-conditioned generation*: Dance-to-music, lyrics-to-music, accompaniment generation.

7. **General Audio Understanding and Generation**:
   - *Text-to-audio / foley synthesis*: AudioLDM, Make-An-Audio, AudioGen, Tango.
   - *Audio captioning*: WavCaps, AudioCaps, CLAP-based retrieval.
   - *Audio question answering and reasoning*: MMAU, AudioBench, GAMA.
   - *Sound event detection/classification*: AudioSet, ESC-50, FSD50K, bioacoustics (BirdSet).
   - *Spatial and binaural audio*: Ambisonics, head-related transfer function (HRTF) modeling.

8. **Audio-Visual Learning**:
   - *Audio-visual correspondence*: Sound source localization, audio-visual synchronization.
   - *Talking head / portrait generation*: Audio-driven facial animation (VASA-1, Loopy, Hallo).
   - *Co-speech gesture generation*: Audio-conditioned 3D body/hand gesture synthesis.
   - *Audio-visual speech recognition (AVSR)*: Lip-reading integration, noise-robust AVSR.
   - *Video-to-audio generation*: Foley, V2A, Frieren, AudioX.

9. **Deepfake Audio Detection and Security**:
   - *Spoofed speech detection*: ASVspoof-style countermeasures, end-to-end detection.
   - *Adversarial robustness*: Models robust to adversarial audio attacks.
   - *Voice anti-spoofing datasets*: ASVspoof 2019/2021, WaveFake, MLAAD.

10. **Datasets and Benchmarks**:
    - Papers that primarily contribute a new dataset or evaluation framework.
    - Require demonstrating scale/diversity, reproducible annotation, and baseline experiments.

### Score Distribution and Acceptance Bar (from 531 papers)

- **Mean rating**: 4.73 | **Median**: 4.67 | **Std**: 1.29
- **Min**: 0.0 | **Max**: 8.0 (no 9 or 10 scores in this sample)
- **Acceptance rate**: 67%
- **Tier breakdown** (reviewer ratings):
  - Excellent (8–10): 20 ratings (~1%) — rare, reserved for exceptional breadth + depth
  - Good (6–7): 435 ratings (~22%) — solid accepted papers
  - Borderline (4–5): 1,078 ratings (~55%) — most common region, split decisions
  - Low (1–3): 484 ratings (~25%) — rejected or fundamental issues

- **Avg soundness**: 2.59/4 | **Avg contribution**: 2.39/4 | **Avg presentation**: 2.66/4

**Practical calibration**:
- **Score 2–3**: Fundamental flaws — incremental without citation of prior art, small dataset with no novel technique, claims that contradict established results, obvious experiments missing.
- **Score 4–5**: Borderline — a real idea but insufficient baselines, weak ablations, limited evaluation scope, questionable novelty, or results that fail to significantly outperform simpler approaches.
- **Score 6–7**: Standard poster accept — a genuine technical contribution, solid (though not exhaustive) evaluation, competitive with SOTA on primary benchmarks, reasonable ablation.
- **Score 8**: Spotlight / Oral — novel unified framework, demonstrably better than SOTA on multiple benchmarks, comprehensive ablation, strong writing, reproducible. MSDM, NaturalSpeech 2, and MMAU exemplify this tier.

---

## 2. What Reviewers Praise (with Real Examples)

### 2.1 Novelty of Core Idea

"Novel" (413x) is the most common strength phrase. In audio/speech, novelty is assessed along several axes:

- **Algorithmic novelty**: A new architecture, loss function, inference procedure, or training strategy.
- **Problem framing novelty**: A new way to formulate an existing problem (e.g., music source separation as a generative task).
- **Cross-domain novelty**: Importing a technique from vision/NLP into audio in a non-trivial way.
- **Task novelty**: Introducing a new task that the community hasn't defined before.

**Real example — MSDM (8.0, Oral)**:
> "The approach the authors proposed is novel and in fact quite general. The idea of using a generative way to view music source separation is so natural and experiments show diffusion model can perform pretty well."

**Real example — LLM Noise-Robust ASR (8.0, Spotlight)**:
> "The idea of doing noise estimation from N-best transcription hypotheses is interesting... It seems that humans actually perform similar processing in noisy environments."

**Real example — NaturalSpeech 2 (8.0, Spotlight)**:
> "This work may be the first successful implementation of a latent diffusion model for speech synthesis... the overall structuring of these components is novel."

**What earns praise**: Reviewers respond strongly to a *motivated* novelty — where the proposed mechanism directly addresses a known limitation in prior work. Simply combining existing components without a compelling "why" is labeled "incremental."

### 2.2 Strong Baselines

"Baseline" is the single most common weakness phrase (883x), but also a common strength phrase (280x). This is the **#1 factor separating accepted from rejected papers in audio_speech**. Reviewers praise papers that:

- Compare against the *current* SOTA — not 2-year-old baselines
- Choose baselines that are clearly in the same setting (same language, dataset size, model capacity)
- Report results on multiple datasets, not just one proprietary or cherry-picked benchmark
- Include results from concurrent/parallel work even if disadvantageous

**Real example — NaturalSpeech 2 (8.0, Spotlight)**:
> "Although recently large-language model (LLM) -based speech synthesis models have been investigated... the authors tried to compare their model with many other works."

**Real example — MMAU (7.5, Spotlight)**:
> "Most existing LALMs are tested on MMAU in the paper... With this benchmark, we gain insights into performance comparisons among them."

**Critical failure — SONAR (4.25, Reject)**:
> "The paper does not adequately reference similar prior work in audio deepfake detection datasets. For instance, Voicewukong [1] offers a benchmark with more diverse data sourced from 34 speech synthesis platforms... it would strengthen the paper to acknowledge these datasets and clarify the specific advantages of SONAR."

### 2.3 Comprehensive Ablation Studies

"Ablation" (342x strength, 475x weakness). Ablations in audio/speech must:
- Isolate each architectural component (e.g., codec encoder vs. diffusion backbone vs. duration predictor)
- Study sensitivity to hyperparameters critical to the method (e.g., number of diffusion steps, codebook size)
- Investigate failure modes (what breaks under noise, long sequences, out-of-domain speakers)

**Real example — LLM Noise-Robust ASR (8.0, Spotlight)**:
> "Plenty of experiments and ablation studies. Insightful discussions, such as t-SNE visualization, and the relationship between noisy speech and n-best list diversity."

**Real example — NaturalSpeech 2 (8.0, Spotlight)**:
> "They also conducted an ablation study well. However, it would be better if the authors could add the results according to the dataset and model size."

### 2.4 Clear Writing and Good Presentation

"Well-written" (116x), "well written" (94x), "clearly" appears hundreds of times as a praise. Audio/speech papers often involve multiple components (encoder, decoder, codec, duration model, vocoder) and reviewers prize papers that clearly explain:
- How all components fit together (a clear architecture diagram is almost mandatory)
- What problem each component solves
- Why specific design choices were made over alternatives

**Real example — MSDM (8.0, Oral)**:
> "The manuscript is compelling to read, well organized, and very clear. The discussion of related work is quite comprehensive."

**Real example — NaturalSpeech 2 (8.0, Spotlight)**:
> "Paper is very well written and provides good intuition and justification for all model choices that the authors have made."

**Failure pattern — NaturalSpeech 2 (despite 8.0 avg rating, this was a weakness)**:
> "The paper is sometimes unclear with regards to what the model components represent and how the components fit together."

This shows that even strong papers are penalized for unclear writing; audio papers with many interacting components are especially vulnerable.

### 2.5 Reproducibility and Code Release

"Reproducible" (101x). Reviewers in audio/speech value:
- Audio demo pages (qualitative examples are essential for generative audio work)
- Code and model checkpoints promised or released
- Clear reporting of training data, preprocessing, hyperparameters
- Standardized evaluation protocols (MOS testing setup, WER measurement, SI-SDR computation)

**Real example — MSDM (8.0, Oral)**:
> "If not already planned, I would encourage the authors to release as much as they can with respect to evaluation methodology and reproducible artifacts that others can use to evaluate in a similar manner."

**Red flag**: Generative audio/speech papers without a demo page or audio samples are viewed with suspicion — reviewers cannot assess quality without listening.

### 2.6 Scalability and Generalization

"Scalable" (47x). In audio/speech, scalability and generalization mean:
- Performance across multiple test sets / datasets / languages
- Results consistent across different backbone models (not just Whisper or HuBERT)
- Zero-shot or few-shot generalization to unseen speakers, languages, or acoustic conditions

**Real example — LLM Noise-Robust ASR (8.0, Spotlight)**:
> "Tests on various LLMs show up to 53.9% improvement in word error rate with limited training data."

**Critical gap that leads to rejection**: Results only on one dataset (e.g., LibriSpeech alone) are consistently flagged, especially for work claiming general applicability.

### 2.7 Strong Empirical Results

"Strong performance" (21x), "strong results" (17x), "strong empirical" (16x). Quantitative results must:
- Beat SOTA by a meaningful margin (not just within error bars)
- Use multiple metrics (e.g., WER + speaker similarity + MOS for TTS; SDR + perceptual for separation)
- Include both objective and subjective evaluations for generative tasks

---

## 3. What Reviewers Criticize (Common Failure Modes)

### 3.1 Missing Baselines (Most Critical)

"Baseline" (883x weakness). This is the #1 reason papers in audio/speech are rejected or score poorly. Specific failure patterns:

- **Missing recent SOTA**: If your paper is about TTS, you must compare to VALL-E, NaturalSpeech series, VoiceBox, or equivalent recent work. Missing one well-known baseline is usually sufficient for rejection.
- **Unfair comparison**: Comparing models with different training data sizes, model parameters, or dataset accessibility.
- **Evaluation protocol mismatch**: Different MOS test conditions (e.g., different crowd-sourcing platforms, different reference anchors).
- **Incomplete evaluation**: Testing only on clean speech when claiming noise robustness; testing only one language.

**Real example — SONAR (4.25, Reject)**:
> "The MLAAD dataset includes 59 state-of-the-art TTS models... supplementing experiments with different models on this dataset would further enhance the credibility."

**Real example — Self-tailoring ASR (4.25, Reject)**:
> "Models fine-tuned on librispeech-100h training setting (read speech) only and performance are overall disappointing... improvements of the proposed approach over adapter fine-tuning are very tiny (<0.5%)"

### 3.2 Limited Novelty / Incremental Contribution

"Novelty" (457x weakness), "limited novelty" (47x), "incremental" (99x), "lacks novelty" (23x). This is the #2 reason for rejection. Patterns:

- **Obvious combinations**: Taking a technique from NLP/vision and applying it to speech without a novel insight about why it should work or what changes are needed.
- **Engineering paper**: Adding a new module to an existing architecture without a principled motivation.
- **Incremental improvement**: A small WER improvement over a very recent baseline, with no insight about *why* the approach works.
- **Missing connection to domain literature**: Importing NLP techniques to speech without citing the speech-specific prior work (e.g., proposing "prompt tuning for ASR" without mentioning decades of ASR adaptation literature).

**Real example — Self-tailoring ASR (4.25, Reject)**:
> "We knew from the beginning that it would work — hence a limited impact. Indeed, the depicted techniques are basically an extension of feature and model adaptation — techniques that have been investigated since 1990 in the speech domain."

**Red flag**: Any paper that proposes to apply [NLP/vision technique X] to audio/speech without explaining the non-trivial challenges introduced by the modality shift.

### 3.3 "Unclear whether" / "Unclear how"

"Unclear whether" (97x), "unclear how" (80x), "unclear why" (37x), "unclear if" (28x). Reviewers frequently flag:

- Unclear connection between motivation and method
- Unclear why a specific architectural choice was made vs. alternatives
- Unclear whether improvements come from the proposed method vs. more training data/compute
- Unclear if results are generalizable beyond the specific test conditions

**Real example — NaturalSpeech 2 (8.0 despite this weakness)**:
> "The argumentation around continuous vs discrete tokens is very hard to follow... then in Section 3.1 'However, for regularization and efficiency purposes we use residual vector quantizers'... This is a particularly surprising turn of the argument."

**Red flag for generative audio**: Claims about naturalness or quality that aren't grounded in perceptual evaluations (MOS or MUSHRA tests).

### 3.4 Reproducibility Concerns

"Reproducible" as a weakness (108x). Key issues in audio/speech:

- Training data not publicly available or not clearly specified
- Preprocessing details missing (sample rate, normalization, feature extraction)
- No demo page or audio samples for generative models
- Inconsistent evaluation protocol (e.g., using different text prompts than the baseline)
- Model checkpoints not released

### 3.5 Limited Evaluation Scope

"Limited to" (73x). Common patterns:

- English-only evaluation for work claiming multilingual capability
- Single-speaker or few-speaker evaluation for TTS work
- Only clean conditions for noise-robust models
- Single dataset or benchmark when multiple are standard in the sub-area
- Short audio clips only (e.g., 5-second clips when long-form coherence is claimed)

### 3.6 Scalability Issues

"Scalable" (61x weakness). In audio/speech:

- Methods that only work on small models (e.g., wav2vec 2.0 Base but not Large)
- Methods with high computational cost that are not measured (inference time, RTF for TTS/ASR)
- Methods that use massive proprietary data (not reproducible by others)

### 3.7 Missing Ablations

"Ablation" (475x weakness). Audio/speech papers typically need ablations on:

- Each key architectural component
- Choice of backbone (does it work with different speech encoders?)
- Effect of data quantity (data efficiency curve)
- Effect of prompt/reference audio length for TTS
- For noise-robust models: performance across different noise types and SNR levels

### 3.8 Fair Comparison Issues

"Fair comparison" (58x). Critical in audio/speech:

- TTS models should be compared on the same test speakers / same text prompts
- ASR baselines should use the same language model (or no language model)
- Different training data sizes make direct comparisons meaningless
- For diffusion models: number of sampling steps should be matched

---

## 4. Sub-Area Specific Expectations

### 4.1 ASR Papers

**Expected baselines**:
- Foundation models: Whisper (various sizes), wav2vec 2.0 / HuBERT / WavLM for SSL approaches
- SOTA for the test set (e.g., LibriSpeech 100h/960h, CHiME-4, VoiCES, CommonVoice)
- For noise-robust: AISHELL, CHiME-4/6, VoiceBank-DEMAND
- For multilingual: Common Voice, MLS, FLEURS
- For LLM-based GER: Compare against language model rescoring baselines

**Expected metrics**: WER (word error rate), CER (character error rate), RTF (real-time factor for streaming). For noise-robust: WER across multiple SNR levels.

**Critical pitfalls**:
- Claiming improvements from a new architecture when the improvement may be from more training data
- Not testing on truly noisy / out-of-domain data when claiming robustness
- Parameter-efficient fine-tuning papers should measure parameters tuned, not just model size
- Missing comparison to full fine-tuning (the gold standard baseline)

**Red flags**:
- Only testing on LibriSpeech clean; no noisy evaluation
- Not citing Whisper, wav2vec 2.0, HuBERT, WavLM in related work

### 4.2 TTS Papers

**Expected baselines** (roughly in order of recency):
- VITS/VITS2, FastSpeech 2 (older but still cited)
- VALL-E and variants for zero-shot
- NaturalSpeech 1/2/3 series
- VoiceBox, P-Flow, E2 TTS, or VoiceBox for flow-matching
- YourTTS, StyleTTS 2 for zero-shot multi-speaker
- SPEAR-TTS, SoundStorm for codec LM approaches

**Expected metrics**:
- *Naturalness*: MOS (mean opinion score) or CMOS via human evaluation
- *Speaker similarity*: Speaker encoder cosine similarity (e.g., WeSpeaker, d-vector)
- *Intelligibility*: WER on synthesized speech (ASR-based)
- *Objective*: UTMOS, NISQA, or similar for quality
- For zero-shot: speaker similarity to reference prompt

**Critical pitfalls**:
- Human MOS tests with fewer than 20 listeners or fewer than 50 utterances per condition are not reliable
- Comparing CMOS without a clear anchor condition
- Not providing a demo page with audio samples — fatal for TTS papers
- Not reporting inference speed (real-time factor) for a TTS model
- Claiming SOTA without comparing to the most recent concurrent work

**Red flags**:
- Demo page with cherry-picked samples only
- Only LJSpeech (single-speaker) evaluation when claiming zero-shot capability
- Missing comparison to VALL-E, VoiceBox, or NaturalSpeech 2

### 4.3 Music Generation and Understanding Papers

**Expected baselines**:
- For music generation: MusicGen, MusicLM, AudioLDM 2, Stable Audio
- For source separation: Demucs v4, MDX23, HTDemucs
- For music understanding: MERT, music transformer, CLAP-based models
- For accompaniment generation: SingSong, MSDM

**Expected metrics**:
- FAD (Fréchet Audio Distance) for generation quality
- SDR/SI-SDR for source separation
- KL divergence for distribution similarity
- Human evaluation (MUSHRA or MOS) for perceptual quality
- Melodic/rhythmic similarity metrics for music-specific evaluation

**Critical pitfalls**:
- FAD is sensitive to the reference model (VGGish vs. CLAP vs. PANN); must state which
- Music generation papers without perceptual evaluations are weak
- Beat/tempo tracking must be evaluated for rhythm-sensitive generation

### 4.4 Audio LLM / Speech LLM Papers

**Expected baselines**:
- SALMONN, Qwen2-Audio, Gemini-Audio, WavLLM, Pengi
- GPT-4o (audio) for capability comparison
- Whisper + LLM pipeline (as a simpler non-end-to-end baseline)

**Expected benchmarks**:
- MMAU, AudioCaps-QA, ClothoQA, AIR-Bench
- ASR: LibriSpeech, CommonVoice
- Sound event detection: AudioSet
- Music: GTZAN, MagnaTagATune

**Critical pitfalls**:
- Architecture papers that don't compare to the latest audio LLMs
- Papers that only evaluate on tasks in the training distribution
- Missing zero-shot transfer evaluation
- Not reporting performance on standard ASR/SED benchmarks alongside novel tasks

### 4.5 Speech Enhancement/Separation Papers

**Expected baselines**:
- For speech enhancement: SEGAN, Conv-TasNet, DEMUCS, BSRNN, MP-SENet, diffusion-based (SGMSE+, CDiffuSE)
- For speech separation: Conv-TasNet, DPTNet, SepFormer, TDANet
- For audio-visual separation: AV-ConvTasNet, IIANet

**Expected metrics**:
- SI-SNR (scale-invariant signal-to-noise ratio)
- SDR (signal-to-distortion ratio)
- PESQ (perceptual evaluation of speech quality)
- STOI (short-time objective intelligibility)
- For speech enhancement also: DNSMOS, NISQA, UTMOS

**Critical pitfalls**:
- Results on WSJ0-2Mix / WHAM! that don't generalize to REVERB or noisy conditions
- Not reporting PESQ and STOI alongside SI-SDR
- Causal models must be compared to other causal models (not offline models)

### 4.6 Audio/Speech Deepfake Detection Papers

**Expected baselines**:
- Traditional: LFCC-LCNN, Spec-ResNet, RawGAT-ST
- Foundation-based: wav2vec 2.0, WavLM, XLSR-based models fine-tuned for spoofing
- Recent SOTA: AASIST, RawBoost-based systems

**Expected datasets/benchmarks**:
- Training: ASVspoof 2019 LA (standard)
- Testing: ASVspoof 2021 LA, ASVspoof 5, WaveFake, In-the-wild datasets
- Cross-dataset evaluation is essential (train on one, test on another)

**Critical pitfalls**:
- Only evaluating on ASVspoof 2019 (training and test from same distribution)
- Small dataset (< 5,000 samples) without cross-dataset validation
- Not comparing to VoiceWukong/MLAAD for comprehensive coverage of recent TTS systems

### 4.7 Speech Tokenization / Codec Papers

**Expected baselines**:
- Codecs: EnCodec (Meta), DAC (Descript), SoundStream (Google)
- Semantic tokens: HuBERT, mHuBERT, dSPEECH
- Hybrid: dSPEECH, SpeechTokenizer, FACodec

**Expected metrics**:
- Reconstruction: UTMOS, STOI, PESQ, ViSQOL
- For semantic tokens: Downstream task performance (SUPERB benchmark)
- Compression rate (bits per second)
- Codebook utilization

**Critical pitfalls**:
- Not reporting downstream task performance for semantic tokenizers
- Not comparing to EnCodec/DAC at equivalent bitrates
- Missing SUPERB evaluation for speech representation claims

### 4.8 Dataset Papers

Dataset-focused papers (BirdSet, MMAU, DeepFakeVox-HQ, etc.) require:

- **Scale**: Larger and/or more diverse than existing datasets in the sub-area
- **Quality**: Clear annotation protocol, inter-annotator agreement, quality filtering
- **Baseline experiments**: Multiple baselines showing the dataset is challenging and useful
- **Accessibility**: Public release with clear license
- **Comparison to existing datasets**: Table showing what this dataset adds over DCASE, AudioSet, LibriSpeech, ASVspoof, etc.

**Critical pitfalls**:
- Small dataset (< 10K samples) for a well-studied domain
- No inter-annotator agreement reported
- No baseline experiments or only trivial baselines
- Not comparing to the most comprehensive existing datasets in the sub-area (e.g., MLAAD with 59 TTS systems for deepfake detection)

---

## 5. Technical Pitfalls Specific to Audio/Speech

### 5.1 Evaluation Methodology for Generative Models

- **MOS testing**: A proper MOS study requires ≥ 20 listeners, ≥ 50 utterances per condition, properly anchored conditions (bad anchor + reference anchor), and statistical significance testing. Single-condition MOS without CMOS is not sufficient for claiming superiority.
- **FAD sensitivity**: The Fréchet Audio Distance is sensitive to the reference model used (VGGish, PANN, CLAP). Always specify the exact reference model and embedding layer.
- **Intelligibility-quality tradeoff**: For TTS, reporting only MOS without WER (intelligibility) hides quality-intelligibility tradeoffs. Both must be reported.
- **Demo page cherry-picking**: If a paper only provides cherry-picked audio demos, reviewers will note this. The best papers include randomly selected samples or describe a systematic selection procedure.

### 5.2 ASR Evaluation

- **Data contamination**: Whisper is trained on near-unlimited internet data, including some test sets. When comparing Whisper-based methods, the evaluation set must be carefully chosen.
- **Language model integration**: WER results with and without language model rescoring must be reported separately or the experimental setup must be explicit about LM use.
- **Beam size sensitivity**: WER can vary significantly with beam size; this must be reported.

### 5.3 Codec and Tokenizer Tradeoffs

- **Rate-distortion tradeoff**: Neural codecs should be evaluated at multiple bitrates. A codec that wins at 6kbps may lose at 3kbps.
- **Codebook collapse**: VQ-based codecs can suffer from poor codebook utilization; this must be measured.
- **Downstream vs. reconstruction quality**: A tokenizer optimized for reconstruction may not produce good semantic tokens for downstream language modeling. These objectives sometimes conflict.

### 5.4 Multi-Modal Audio-Visual Models

- **Temporal alignment**: Audio-visual models must address the synchronization gap; papers that don't explicitly handle/measure A/V sync are incomplete.
- **Visual ablation**: For A/V models, an audio-only baseline is always expected. If the visual stream doesn't help much, the contribution is questionable.

### 5.5 Diffusion/Flow Models for Audio

- **Number of function evaluations (NFE)**: Diffusion models are slow; reviewers expect a table showing quality vs. NFE. Claiming SOTA quality without comparing at equivalent NFE is unfair.
- **Sampling schedule sensitivity**: Results can vary significantly across samplers (DDIM, DPM-Solver, etc.); the choice must be reported.

### 5.6 Speech LLM Integration

- **Modality gap**: Simply concatenating speech encoder outputs to LLM tokens often doesn't work well. A well-designed adapter/projector is needed, and papers must show this is better than simple baselines.
- **ASR leakage**: Speech LLMs that simply transcribe speech and answer based on text are not true audio LLMs; the architecture must demonstrate genuine audio understanding beyond ASR.
- **Instruction following calibration**: MCQ evaluation of LLMs may not reflect their true capability — a model trained on QA may underperform on a differently-prompted evaluation.

---

## 6. Expected Citations and Prior Work by Sub-Area

### 6.1 ASR
Must cite (if relevant): Whisper (Radford et al., 2022), wav2vec 2.0 (Baevski et al., 2020), HuBERT (Hsu et al., 2021), WavLM (Chen et al., 2022), conformer (Gulati et al., 2020), ESPnet/SpeechBrain toolkit.

Suspicious absence: Whisper in noise-robust ASR; HuBERT/WavLM in SSL-for-ASR papers; LoRA/adapter papers without citing PEFT literature.

### 6.2 TTS
Must cite (if relevant): VITS (Kim et al., 2021), FastSpeech 2 (Ren et al., 2020), VALL-E (Wang et al., 2023), NaturalSpeech 2 (Shen et al., 2023), VoiceBox (Le et al., 2023), Vocos (Siuzdak et al., 2023), HiFi-GAN (Kong et al., 2020).

Suspicious absence: Missing NaturalSpeech or VALL-E in a zero-shot TTS paper; missing HiFi-GAN or Vocos in a vocoder paper.

### 6.3 Music
Must cite (if relevant): MusicGen (Copet et al., 2023), AudioLDM 2 (Liu et al., 2023), MERT (Li et al., 2023), Demucs (Rouard et al., 2022), MSDM (Mariani et al., 2023), Presto (Novack et al., 2024).

### 6.4 Audio LLMs
Must cite (if relevant): CLAP (Wu et al., 2023), Pengi (Deshmukh et al., 2023), SALMONN (Tang et al., 2023), Qwen-Audio, WavLLM, AudioPaLM, Gemini-Audio.

### 6.5 Speech Tokenization
Must cite (if relevant): EnCodec (Défossez et al., 2022), DAC (Kumar et al., 2023), SoundStream (Zeghidour et al., 2022), HuBERT discrete units (Hsu et al., 2021), SpeechTokenizer (Zhang et al., 2023).

### 6.6 Enhancement/Separation
Must cite (if relevant): Conv-TasNet (Luo & Mesgarani, 2019), SepFormer (Subakan et al., 2021), BSRNN (Luo & Yu, 2023), SGMSE+ (Richter et al., 2022), Demucs (Rouard et al., 2022).

### 6.7 Deepfake Detection
Must cite (if relevant): ASVspoof series (2019, 2021), AASIST (Jung et al., 2022), WaveFake (Frank et al., 2021), RawBoost (Tak et al., 2022), VoiceWukong / MLAAD (if claiming comprehensive benchmark).

---

## 7. Scoring Rubric with Concrete Examples

### Score 2–3: Reject

**Characteristics**:
- Core claim is not supported by experiments (missing baselines, cherry-picked results)
- Incremental contribution without novel insight
- Related work is significantly incomplete (missing foundational papers)
- Dataset paper with < 2,000 samples and no comparison to existing datasets
- Method that only works in a narrow, contrived setting

**Concrete examples from this dataset**:

- **SONAR (4.25, Reject)**: Deepfake detection benchmark with 2,274 samples from 9 systems, while prior work (VoiceWukong) covers 34 systems with more samples. No new detection method. Small dataset, limited novelty.
  > "The dataset presented (2274 fake samples) is relatively small compared to existing datasets... Furthermore, the dataset is limited to 9 generation methods."

- **Self-tailoring ASR prompts (4.25, Reject)**: Proposes utterance-specific soft prompts for ASR but ignores 30+ years of speaker adaptation literature. Improvements over adapter fine-tuning are < 0.5%.
  > "Improvements of the proposed approach over adapter fine-tuning are very tiny (<0.5%) and the self-tailored prompt tuning seems to not work better than simple adapter fine-tuning."

**Key flags for 2–3**: "limited to" + one dataset, "lacks baselines", "incremental", "ignores prior work", "small dataset", "no ablation".

### Score 4–5: Borderline

**Characteristics**:
- A real idea but execution is incomplete
- One key baseline missing
- Results only on one dataset
- Ablations are partial
- Method is novel but the paper doesn't clearly explain why it works
- Dataset paper where quality/diversity is questionable

**Signs of borderline (4–5)**:
- Two out of four reviewers give 5 or 6, others give 3–4
- Strengths and weaknesses are roughly balanced
- Authors need significant revision to make their claims solid

**Reviewer quote indicating borderline territory**:
> "Unclear whether the improvements come from the proposed method vs. more training data."

> "Limited to LibriSpeech; no evaluation on truly noisy conditions."

> "The model is novel but ablation studies do not isolate the contribution of each component."

### Score 6–7: Accepted (Poster)

**Characteristics**:
- Novel core idea with a clear motivation
- Comprehensive baselines on standard benchmarks
- Solid ablation (not exhaustive but covers main design choices)
- Results beat SOTA on primary metrics
- Demo page / audio samples provided for generative work
- Clear writing and architecture diagram

**Concrete examples**:

- **I Can Hear You: Deepfake Audio Detection (7.0, Accept)**: Novel dataset (DeepFakeVox-HQ), new F-SAT method for frequency-selective adversarial training. Reviewers praised dataset scale and adversarial robustness evaluation. Weaknesses: some baselines missing, evaluation metric choice debated.

- **Scaling Transformers for Low-Bitrate High-Quality Speech Coding (7.0, Accept)**: Novel transformer-based codec at low bitrates. Strong quantitative results, clear comparison to EnCodec/Opus baselines.

- **MMAU Benchmark (7.5, Spotlight)**: Large-scale audio reasoning benchmark with 10,000 samples across 27 skills. Praised for coverage, expert annotation, and evaluation of 18 models. Weakness: only MCQ format, no long-audio evaluation.

### Score 8: Spotlight / Oral

**Characteristics**:
- Opens a new direction or establishes a new state of the art across multiple dimensions
- Addresses an important limitation in prior work with a principled solution
- Comprehensive experiments with ablations and multiple baselines
- Human evaluation + objective metrics for generative work
- Reproducible (code, demo, checkpoints)
- Writing is clear even with complex multi-component systems

**Concrete examples**:

- **Multi-Source Diffusion Models (8.0, Oral)**: First diffusion model for joint music generation and separation. Novel inference procedure, solid separation results vs. Demucs, new accompaniment generation task. All four reviewers gave 8.
  > "The approach the authors proposed is novel and in fact quite general... the overall structuring of these components is novel."

- **LLM Noise-Robust ASR (8.0, Spotlight)**: Novel language-space noise embedding from N-best hypotheses for robust ASR. Avoids cross-modal gap. 53.9% WER improvement, rich evaluation, ablation studies, t-SNE visualization.
  > "Novel idea to apply LLM for noise-robust ASR. Extract language-space noise embedding with knowledge distillation based on mutual information. Good performance improvement. Plenty of experiments and ablation studies."

- **NaturalSpeech 2 (8.0, Spotlight)**: Latent diffusion TTS with neural audio codec. Zero-shot speaker adaptation, singing synthesis, beats VALL-E and YourTTS on multiple metrics. Comprehensive evaluation table.

**Key signatures of 8+**: All or most reviewers give 8+, explicit mention of "novel" + "comprehensive" + "well-written" + specific quantitative praise, demo page, open-source artifacts.

---

## 8. Common Reviewer Patterns and Behaviors

### 8.1 What Triggers a "3" from an Expert Reviewer

Expert reviewers (confidence 4–5) give low scores when:

1. The paper misses an obvious baseline that makes the contribution trivial
2. The method is presented as novel but is actually a known technique from the speech domain under a new name
3. The experimental protocol is flawed (wrong evaluation set, data contamination, unfair comparison)
4. The claimed result cannot be reproduced with the provided details

### 8.2 What Triggers Disagreement Between Reviewers

Borderline papers (4–6) often have high variance because:

- One reviewer is an ASR expert and knows the speech-specific prior art that another reviewer missed
- One reviewer values the engineering contribution while another wants theoretical novelty
- One reviewer doesn't have a demo link and can't assess audio quality

In audio/speech, **confidence level matters a lot** for interpretation. A "5" from a reviewer with confidence 2 is less meaningful than a "5" from a reviewer with confidence 5.

### 8.3 Venue Fit

Reviewers sometimes flag that an audio/speech paper is "more suited for Interspeech or ICASSP." This happens when:

- The work is purely engineering (no learning theory, no architectural insight)
- The dataset is too domain-specific (clinical speech, single-language ASR)
- The paper lacks the broader ML contribution expected at ICLR/NeurIPS

Papers that are venue-fit for ICLR/NeurIPS typically:
- Connect audio/speech to broader ML questions (representation learning, generative modeling, foundation models)
- Introduce methods transferable to other modalities
- Propose a new learning paradigm (not just a new model)

### 8.4 On "Comprehensive Evaluation"

"Comprehensive evaluation" (35x) is a top strength. In audio/speech, this means:
- Multiple datasets (at least 2–3)
- Multiple metrics (not just WER or just MOS)
- Multiple baselines (at least 3–5 SOTA comparisons)
- Human + objective evaluation for generative work
- Ablations + sensitivity analysis

### 8.5 The Baseline-Novelty Interaction

The two most common criticisms are "missing baselines" and "limited novelty." These often co-occur: a paper that lacks a baseline is suspected of limited novelty (the results might not hold against the missing comparison). Conversely, a paper with strong novelty can survive missing one minor baseline; a paper with weak novelty cannot.

---

## 9. Evaluation Checklist for Audio/Speech Papers

When evaluating a research idea in audio/speech, systematically check:

**Novelty**
- [ ] Is the core idea genuinely new, or is it an application of a known technique from NLP/CV?
- [ ] Does the paper cite the relevant speech-specific prior work?
- [ ] Is the motivation for the design choices clear and principled?

**Baselines**
- [ ] Are the most recent SOTA models in the sub-area included?
- [ ] Are comparisons fair (same data, same model size, same evaluation protocol)?
- [ ] Is there a simple/ablated baseline to show the full model is better than its parts?
- [ ] For TTS: are VALL-E, NaturalSpeech, VoiceBox cited and compared?
- [ ] For ASR: is Whisper included as a baseline?
- [ ] For deepfake detection: are ASVspoof 2019/2021 standard protocols followed?

**Evaluation**
- [ ] Are multiple datasets used for evaluation?
- [ ] For generative work: is there a human evaluation (MOS, CMOS, MUSHRA)?
- [ ] For generative work: is there a demo page with audio samples?
- [ ] Are both objective and subjective metrics reported?
- [ ] Are intelligibility (WER) and naturalness (MOS) both reported for TTS?
- [ ] Is inference speed (RTF) reported for real-time or latency-sensitive systems?

**Ablations**
- [ ] Is each key architectural component ablated?
- [ ] Is there a sensitivity analysis to key hyperparameters?
- [ ] Is there an analysis of failure modes or limitations?

**Reproducibility**
- [ ] Are training data, preprocessing, and hyperparameters clearly specified?
- [ ] Is code / checkpoints released or promised?
- [ ] Are evaluation protocol details (number of raters, test sentences, etc.) clear for MOS studies?

**Clarity**
- [ ] Is the architecture diagram clear and complete?
- [ ] Is the connection between motivation and method clear?
- [ ] Is the contribution clearly differentiated from prior work?

---

## 10. Summary: Key Principles for Calibrated Scoring

1. **In audio/speech, missing baselines are near-fatal.** If a paper is missing the obvious SOTA comparison in its sub-area, score it as borderline (4–5) at best unless everything else is exceptional.

2. **Novelty must be motivated.** Applying NLP/vision techniques to audio without explaining the non-trivial adaptation is insufficient. The paper must show *why* the audio modality requires a new approach.

3. **Generative audio papers need demo pages.** A TTS, music generation, or audio synthesis paper without audio examples cannot be properly evaluated. Flag this explicitly.

4. **Human evaluation is expected for generative work.** Objective metrics alone (FAD, SI-SDR) are not sufficient to claim SOTA quality in TTS, music generation, or speech enhancement. MOS or MUSHRA is expected.

5. **Multi-modal audio-visual papers need visual ablations.** If adding video doesn't significantly help over audio-only, the contribution is questionable.

6. **Efficiency metrics matter.** For real-time systems (streaming ASR, TTS, live separation), RTF and latency must be reported. A diffusion model for TTS must report NFE vs. quality tradeoff.

7. **ASR papers must generalize beyond LibriSpeech.** Evaluation only on clean LibriSpeech is seen as incomplete for 2024+ papers. At minimum, a noisy or conversational test set is expected.

8. **The acceptance bar is a 6.** With a 67% acceptance rate, the bar is relatively accessible. A paper that is genuinely novel, has solid (not comprehensive) baselines, and clear writing should score 6+. Papers need to actively fail (missing baselines, limited novelty, no ablation) to score below 5.

9. **Venue fit matters at the margins.** A 5/10 paper that is purely engineering may be noted as "better fit for Interspeech/ICASSP." This can tip a borderline paper toward rejection.

10. **Dataset papers need strong baselines.** A dataset paper that only shows results with one model or trivial baselines is not sufficient. The dataset must be demonstrated to be challenging and useful across multiple approaches.
