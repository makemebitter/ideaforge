You are an expert AI research reviewer building a **skill file** for evaluating papers in the topic area: **audio_speech**.

## Your Task

Write a comprehensive skill file (Markdown, 10-20K tokens) that will be loaded by an AI judge agent when evaluating new research ideas in this area. The file should enable the judge to give calibrated, expert-level evaluations.

## Statistics from 531 papers in this area

```json
{
  "topic": "audio_speech",
  "num_papers": 531,
  "num_accepted": 356,
  "acceptance_rate": 0.67,
  "rating_mean": 4.73,
  "rating_median": 4.67,
  "rating_std": 1.29,
  "rating_min": 0.0,
  "rating_max": 8.0,
  "avg_soundness": 2.59,
  "avg_contribution": 2.39,
  "avg_presentation": 2.66,
  "tier_example_count": {
    "good (6-7)": 435,
    "borderline (4-5)": 1078,
    "low (1-3)": 484,
    "excellent (8-10)": 20
  }
}
```

### Most common strength phrases from reviewers:
  - novel (413x)
  - ablation (342x)
  - baseline (280x)
  - state-of-the-art (130x)
  - well-written (116x)
  - reproducib (101x)
  - well written (94x)
  - novelty (63x)
  - scalab (47x)
  - comprehensive evaluation (35x)
  - strong baselines (28x)
  - comprehensive and (25x)
  - strong performance (21x)
  - incremental (21x)
  - significant contribution (20x)
  - lack of (19x)
  - strong results (17x)
  - comprehensive experiments (16x)
  - strong empirical (16x)
  - thorough and (14x)

### Most common weakness phrases from reviewers:
  - baseline (883x)
  - ablation (475x)
  - novelty (457x)
  - lack of (339x)
  - novel (197x)
  - state-of-the-art (115x)
  - reproducib (108x)
  - incremental (99x)
  - unclear whether (97x)
  - unclear how (80x)
  - limited to (73x)
  - scalab (61x)
  - fair comparison (58x)
  - lacks a (48x)
  - limited novelty (47x)
  - unclear why (37x)
  - unclear if (28x)
  - unclear to (26x)
  - unclear what (26x)
  - lacks novelty (23x)

## Paper Manifest

Below is a manifest of all 531 papers in this topic with their scores, PDF paths, and review JSON paths.

**YOUR READING STRATEGY:**
1. Start by reading 3-4 of the HIGHEST rated papers (8+) to understand what excellence looks like
2. Read 3-4 of the LOWEST rated papers (1-4) to understand common failures
3. Read 3-4 BORDERLINE papers (5-6) to understand the acceptance threshold
4. Read 2-3 more papers that seem interesting or unusual based on what you've learned

For each paper you read:
- Read the review JSON first (it has reviewer strengths/weaknesses/questions)
- If the paper has a PDF, skim the methods and experiments sections
- Note specific patterns: what methods do reviewers praise? what baselines are expected?

```
# Paper Manifest for topic: audio_speech
# 531 papers total

[1] rating=8.0 | decision=Accept (Spotlight) | reviews=4
    title: Large Language Models are Efficient Learners of Noise-Robust Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\ceATjGPTUD_reviews.json
    forum: https://openreview.net/forum?id=ceATjGPTUD

[2] rating=8.0 | decision=Accept | reviews=4
    title: Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\sSbEEHNEsL_reviews.json
    forum: https://openreview.net/forum?id=sSbEEHNEsL

[3] rating=8.0 | decision=None | reviews=4
    title: Loopy: Taming Audio-Driven Portrait Avatar with Long-Term Motion Dependency
    pdf: research_data\iclr\video-generation\pdfs\Loopy__Taming_Audio-Driven_Portrait_Avatar_with_Long-Term_Motion_Dependency.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=weM4YBicIP

[4] rating=8.0 | decision=Accept (Oral) | reviews=4
    title: Multi-Source Diffusion Models for Simultaneous Music Generation and Separation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\h922Qhkmx1_reviews.json
    forum: https://openreview.net/forum?id=h922Qhkmx1

[5] rating=8.0 | decision=Accept (Spotlight) | reviews=4
    title: NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\Rc7dAwVL3v_reviews.json
    forum: https://openreview.net/forum?id=Rc7dAwVL3v

[6] rating=7.5 | decision=Accept (Spotlight) | reviews=4
    title: MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\TeVAZXr3yv_reviews.json
    forum: https://openreview.net/forum?id=TeVAZXr3yv

[7] rating=7.5 | decision=Accept | reviews=4
    title: StableToken: A Noise-Robust Semantic Speech Tokenizer for Resilient SpeechLLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\17DNmdQ9aU_reviews.json
    forum: https://openreview.net/forum?id=17DNmdQ9aU

[8] rating=7.5 | decision=Accept (Spotlight) | reviews=4
    title: ADIFF: Explaining audio difference using natural language
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\l4fMj4Vnly_reviews.json
    forum: https://openreview.net/forum?id=l4fMj4Vnly

[9] rating=7.5 | decision=None | reviews=4
    title: Co$^{\mathbf{3}}$Gesture: Towards Coherent Concurrent Co-speech 3D Gesture Generation with Interactive Diffusion
    pdf: research_data\iclr\gesture-generation\pdfs\Co$^{_mathbf{3}}$Gesture__Towards_Coherent_Concurrent_Co-speech_3D_Gesture_Gener.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=VaowElpVzd

[10] rating=7.5 | decision=Accept (Spotlight) | reviews=4
    title: BirdSet: A Large-Scale Dataset for Audio Classification in Avian Bioacoustics
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\dRXxFEY8ZE_reviews.json
    forum: https://openreview.net/forum?id=dRXxFEY8ZE

[11] rating=7.5 | decision=Accept (Poster) | reviews=4
    title: MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\w3YZ9MSlBu_reviews.json
    forum: https://openreview.net/forum?id=w3YZ9MSlBu

[12] rating=7.3 | decision=Accept (Poster) | reviews=6
    title: A Full-duplex Speech Dialogue Scheme Based On Large Language Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\YawXY6mWiK_reviews.json
    forum: https://openreview.net/forum?id=YawXY6mWiK

[13] rating=7.2 | decision=Accept (Spotlight) | reviews=4
    title: Presto! Distilling Steps and Layers for Accelerating Music Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Gj5JTAwdoy_reviews.json
    forum: https://openreview.net/forum?id=Gj5JTAwdoy

[14] rating=7.2 | decision=Accept (Oral) | reviews=8
    title: VASA-1: Lifelike Audio-Driven Talking Faces Generated in Real Time
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\5zSCSE0k41_reviews.json
    forum: https://openreview.net/forum?id=5zSCSE0k41

[15] rating=7.2 | decision=Accept (Spotlight) | reviews=4
    title: Whole-Song Hierarchical Generation of Symbolic Music Using Cascaded Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\sn7CYWyavh_reviews.json
    forum: https://openreview.net/forum?id=sn7CYWyavh

[16] rating=7.0 | decision=Accept (Poster) | reviews=4
    title: SSLAM: Enhancing Self-Supervised Models with Audio Mixtures for Polyphonic Soundscapes
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\odU59TxdiB_reviews.json
    forum: https://openreview.net/forum?id=odU59TxdiB

[17] rating=7.0 | decision=Accept | reviews=4
    title: AVoCaDO: An Audiovisual Video Captioner Driven by Temporal Orchestration
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\vjEl1PuIDE_reviews.json
    forum: https://openreview.net/forum?id=vjEl1PuIDE

[18] rating=7.0 | decision=Accept (Poster) | reviews=8
    title: MoMu-Diffusion: On Learning Long-Term Motion-Music Synchronization and Correspondence
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\YscR3LBIi7_reviews.json
    forum: https://openreview.net/forum?id=YscR3LBIi7

[19] rating=7.0 | decision=Accept (Spotlight) | reviews=4
    title: Kiki or Bouba? Sound Symbolism in Vision-and-Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\bfmSc1ETT9_reviews.json
    forum: https://openreview.net/forum?id=bfmSc1ETT9

[20] rating=7.0 | decision=Accept (Spotlight) | reviews=4
    title: High-Fidelity Audio Compression with Improved RVQGAN
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\qjnl1QUnFA_reviews.json
    forum: https://openreview.net/forum?id=qjnl1QUnFA

[21] rating=7.0 | decision=Accept (Poster) | reviews=4
    title: I Can Hear You: Selective Robust Training for Deepfake Audio Detection
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\2GcR9bO620_reviews.json
    forum: https://openreview.net/forum?id=2GcR9bO620

[22] rating=7.0 | decision=Accept (Poster) | reviews=4
    title: Scaling Transformers for Low-Bitrate High-Quality Speech Coding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\4YpMrGfldX_reviews.json
    forum: https://openreview.net/forum?id=4YpMrGfldX

[23] rating=7.0 | decision=Accept | reviews=4
    title: AudioX: A Unified Framework for Anything-to-Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qjJWxK3yWo_reviews.json
    forum: https://openreview.net/forum?id=qjJWxK3yWo

[24] rating=6.9 | decision=Accept (Poster) | reviews=7
    title: How to Verify Any (Reasonable) Distribution Property: Computationally Sound Argument Systems for Distributions
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\GfXMTAJaxZ_reviews.json
    forum: https://openreview.net/forum?id=GfXMTAJaxZ

[25] rating=6.8 | decision=Accept (Poster) | reviews=5
    title: RFWave: Multi-band Rectified Flow for Audio Waveform Reconstruction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\gRmWtOnTLK_reviews.json
    forum: https://openreview.net/forum?id=gRmWtOnTLK

[26] rating=6.8 | decision=Accept (Poster) | reviews=4
    title: Multi-Task Corrupted Prediction for Learning Robust Audio-Visual Speech Representation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\WEQL5ksDnB_reviews.json
    forum: https://openreview.net/forum?id=WEQL5ksDnB

[27] rating=6.8 | decision=Accept (Poster) | reviews=4
    title: Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\izrOLJov5y_reviews.json
    forum: https://openreview.net/forum?id=izrOLJov5y

[28] rating=6.8 | decision=Reject | reviews=4
    title: Enhancing Deception Detection with Cognitive Load Features: An Audio-Visual Approach
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\WNZNsyzcaB_reviews.json
    forum: https://openreview.net/forum?id=WNZNsyzcaB

[29] rating=6.8 | decision=Accept (Poster) | reviews=4
    title: Synthio: Augmenting Small-Scale Audio Classification Datasets with Synthetic Data
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\bR1J7SpzrD_reviews.json
    forum: https://openreview.net/forum?id=bR1J7SpzrD

[30] rating=6.8 | decision=Accept (Poster) | reviews=4
    title: Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\90Db4RUBc7_reviews.json
    forum: https://openreview.net/forum?id=90Db4RUBc7

[31] rating=6.8 | decision=Accept (Poster) | reviews=4
    title: CR-CTC: Consistency regularization on CTC for improved speech recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\CIs9x2ZRgh_reviews.json
    forum: https://openreview.net/forum?id=CIs9x2ZRgh

[32] rating=6.8 | decision=Accept (Poster) | reviews=4
    title: Sylber: Syllabic Embedding Representation of Speech from Raw Audio
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\FyMjfDQ9RO_reviews.json
    forum: https://openreview.net/forum?id=FyMjfDQ9RO

[33] rating=6.8 | decision=Accept (Poster) | reviews=4
    title: Audio Large Language Models Can Be Descriptive Speech Quality Evaluators
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\U42TkrEDzb_reviews.json
    forum: https://openreview.net/forum?id=U42TkrEDzb

[34] rating=6.7 | decision=Accept (Poster) | reviews=3
    title: Weakly-supervised Audio Separation via Bi-modal Semantic Similarity
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\4N97bz1sP6_reviews.json
    forum: https://openreview.net/forum?id=4N97bz1sP6

[35] rating=6.7 | decision=Accept | reviews=6
    title: VibeVoice: Expressive Podcast Generation with Next-Token Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\FihSkzyxdv_reviews.json
    forum: https://openreview.net/forum?id=FihSkzyxdv

[36] rating=6.7 | decision=None | reviews=3
    title: SpeakerVid-5M: A Large-Scale High-Quality Dataset for Audio-Visual Dyadic Interactive Human Generation
    pdf: research_data\iclr\video-generation\pdfs\SpeakerVid-5M__A_Large-Scale_High-Quality_Dataset_for_Audio-Visual_Dyadic_Intera.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=U004uqALWl

[37] rating=6.7 | decision=Accept (Poster) | reviews=3
    title: Continuous Autoregressive Modeling with Stochastic Monotonic Alignment for Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\cuFzE8Jlvb_reviews.json
    forum: https://openreview.net/forum?id=cuFzE8Jlvb

[38] rating=6.6 | decision=Accept (Poster) | reviews=5
    title: UNSSOR: Unsupervised Neural Speech Separation by Leveraging Over-determined Training Mixtures
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\T5h69frFF7_reviews.json
    forum: https://openreview.net/forum?id=T5h69frFF7

[39] rating=6.5 | decision=Accept | reviews=4
    title: Music Flamingo: Scaling Music Understanding in Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\RS7T9S16Bl_reviews.json
    forum: https://openreview.net/forum?id=RS7T9S16Bl

[40] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: MuPT: A Generative Symbolic Music Pretrained Transformer
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\iAK9oHp4Zz_reviews.json
    forum: https://openreview.net/forum?id=iAK9oHp4Zz

[41] rating=6.5 | decision=None | reviews=4
    title: Joint Audio-Video Diffusion Transformer with Hierarchical Spatio-Temporal Prior Synchronization
    pdf: research_data\iclr\video-generation\pdfs\Joint_Audio-Video_Diffusion_Transformer_with_Hierarchical_Spatio-Temporal_Prior.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=y7HV7KT3Bd

[42] rating=6.5 | decision=Accept | reviews=4
    title: Objective Soups: Multilingual Multi-Task Acoustic Modeling for Automatic Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\gW4bdLwypB_reviews.json
    forum: https://openreview.net/forum?id=gW4bdLwypB

[43] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: SonicSim: A customizable simulation platform for speech processing in moving sound source scenarios
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Hx2ADQLi8M_reviews.json
    forum: https://openreview.net/forum?id=Hx2ADQLi8M

[44] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: Mega-TTS 2: Boosting Prompting Mechanisms for Zero-Shot Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\mvMI3N4AvD_reviews.json
    forum: https://openreview.net/forum?id=mvMI3N4AvD

[45] rating=6.5 | decision=Accept (Poster) | reviews=8
    title: SSDM: Scalable Speech Dysfluency Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\IxEhb4NCvy_reviews.json
    forum: https://openreview.net/forum?id=IxEhb4NCvy

[46] rating=6.5 | decision=Accept | reviews=4
    title: PACE: Pretrained Audio Continual Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\k5PgSlNc4E_reviews.json
    forum: https://openreview.net/forum?id=k5PgSlNc4E

[47] rating=6.5 | decision=Accept (Poster) | reviews=8
    title: FINALLY: fast and universal speech enhancement with studio-like quality
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\18RdkSv9h9_reviews.json
    forum: https://openreview.net/forum?id=18RdkSv9h9

[48] rating=6.5 | decision=Accept (Poster) | reviews=6
    title: DinoSR: Self-Distillation and Online Clustering for Self-supervised Speech Representation Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\twmHKU3Ds4_reviews.json
    forum: https://openreview.net/forum?id=twmHKU3Ds4

[49] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: Bridging the Data Provenance Gap Across Text, Speech, and Video
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\G5DziesYxL_reviews.json
    forum: https://openreview.net/forum?id=G5DziesYxL

[50] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: WavTokenizer: an Efficient Acoustic Discrete Codec Tokenizer for Audio Language Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\yBlVlS2Fd9_reviews.json
    forum: https://openreview.net/forum?id=yBlVlS2Fd9

[51] rating=6.5 | decision=Accept | reviews=4
    title: Incentivizing Consistent, Effective and Scalable Reasoning Capability in Audio LLMs via Reasoning Process Rewards
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DUr48hxO2h_reviews.json
    forum: https://openreview.net/forum?id=DUr48hxO2h

[52] rating=6.5 | decision=Accept (Poster) | reviews=8
    title: SLIM: Style-Linguistics Mismatch Model for Generalized Audio Deepfake Detection
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\fymr0CBDHZ_reviews.json
    forum: https://openreview.net/forum?id=fymr0CBDHZ

[53] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: LLaMA-Omni: Seamless Speech Interaction with Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\PYmrUQmMEw_reviews.json
    forum: https://openreview.net/forum?id=PYmrUQmMEw

[54] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: Improving Semantic Understanding in Speech Language Models via Brain-tuning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\KL8Sm4xRn7_reviews.json
    forum: https://openreview.net/forum?id=KL8Sm4xRn7

[55] rating=6.5 | decision=Accept (Poster) | reviews=6
    title: Modality-Independent Teachers Meet Weakly-Supervised Audio-Visual Event Parser
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\p8gTWkFIvx_reviews.json
    forum: https://openreview.net/forum?id=p8gTWkFIvx

[56] rating=6.5 | decision=None | reviews=4
    title: EcoFace: Audio-Visual Emotional Co-Disentanglement Speech-Driven 3D Talking Face Generation
    pdf: research_data\iclr\talking-head\pdfs\EcoFace__Audio-Visual_Emotional_Co-Disentanglement_Speech-Driven_3D_Talking_Face.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=iDcWYtYUwX

[57] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: SyllableLM: Learning Coarse Semantic Units for Speech Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\dGSOn7sdWg_reviews.json
    forum: https://openreview.net/forum?id=dGSOn7sdWg

[58] rating=6.4 | decision=Accept (Poster) | reviews=5
    title: CLaM-TTS: Improving Neural Codec Language Model for Zero-Shot Text-to-Speech
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\ofzeypWosV_reviews.json
    forum: https://openreview.net/forum?id=ofzeypWosV

[59] rating=6.4 | decision=Accept (Poster) | reviews=5
    title: HALL-E: Hierarchical Neural Codec Language Model for Minute-Long Zero-Shot Text-to-Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\868masI331_reviews.json
    forum: https://openreview.net/forum?id=868masI331

[60] rating=6.4 | decision=Accept (Poster) | reviews=5
    title: Disentangling Voice and Content with Self-Supervision for Speaker Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\KoFYzuwjCA_reviews.json
    forum: https://openreview.net/forum?id=KoFYzuwjCA

[61] rating=6.4 | decision=Accept (Poster) | reviews=5
    title: ViSAGe: Video-to-Spatial Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\8bF1Vaj9tm_reviews.json
    forum: https://openreview.net/forum?id=8bF1Vaj9tm

[62] rating=6.4 | decision=Accept (Poster) | reviews=10
    title: SCOREQ: Speech Quality Assessment with Contrastive Regression
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\HDVsiUHQ1w_reviews.json
    forum: https://openreview.net/forum?id=HDVsiUHQ1w

[63] rating=6.4 | decision=Accept (Poster) | reviews=10
    title: Mixtures of Experts for Audio-Visual Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\SNmuKbU0am_reviews.json
    forum: https://openreview.net/forum?id=SNmuKbU0am

[64] rating=6.3 | decision=Accept (Poster) | reviews=6
    title: Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\NjewXJUDYq_reviews.json
    forum: https://openreview.net/forum?id=NjewXJUDYq

[65] rating=6.2 | decision=Accept (Poster) | reviews=4
    title: Simple and Controllable Music Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\jtiQ26sCJi_reviews.json
    forum: https://openreview.net/forum?id=jtiQ26sCJi

[66] rating=6.2 | decision=Accept (Poster) | reviews=4
    title: Aligned Better, Listen Better for Audio-Visual Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\1SYUKPeM12_reviews.json
    forum: https://openreview.net/forum?id=1SYUKPeM12

[67] rating=6.2 | decision=Accept (Poster) | reviews=4
    title: DiTTo-TTS: Diffusion Transformers for Scalable Text-to-Speech without Domain-Specific Factors
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\hQvX9MBowC_reviews.json
    forum: https://openreview.net/forum?id=hQvX9MBowC

[68] rating=6.2 | decision=Reject | reviews=4
    title: TransFace: Unit-Based Audio-Visual Speech Synthesizer for Talking Head Translation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\71oyMJiUm2_reviews.json
    forum: https://openreview.net/forum?id=71oyMJiUm2

[69] rating=6.2 | decision=Accept (Poster) | reviews=4
    title: VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\K4FAFNRpko_reviews.json
    forum: https://openreview.net/forum?id=K4FAFNRpko

[70] rating=6.2 | decision=Accept (Poster) | reviews=4
    title: CoLLAT: On Adding Fine-grained Audio Understanding to Language Models using Token-Level Locked-Language Tuning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\2NncD8AaFK_reviews.json
    forum: https://openreview.net/forum?id=2NncD8AaFK

[71] rating=6.2 | decision=Accept (Poster) | reviews=4
    title: Contrastive Learning from Synthetic Audio Doppelgängers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\XRtyVELwr6_reviews.json
    forum: https://openreview.net/forum?id=XRtyVELwr6

[72] rating=6.2 | decision=Accept | reviews=4
    title: BLSP: Bootstrapping Language-Speech Pre-training via Behavior Alignment of Continuation Writing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\H4zAFFyoXK_reviews.json
    forum: https://openreview.net/forum?id=H4zAFFyoXK

[73] rating=6.2 | decision=Accept (Poster) | reviews=8
    title: Self-Taught Recognizer: Toward Unsupervised Adaptation for Speech Foundation Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\oLoqHRbXYE_reviews.json
    forum: https://openreview.net/forum?id=oLoqHRbXYE

[74] rating=6.2 | decision=Accept (Poster) | reviews=5
    title: Dual Mean-Teacher: An Unbiased Semi-Supervised Framework for Audio-Visual Source Localization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\CFhpBJ8eZ5_reviews.json
    forum: https://openreview.net/forum?id=CFhpBJ8eZ5

[75] rating=6.0 | decision=Accept (Poster) | reviews=3
    title: Resilient Multiple Choice Learning: A learned scoring scheme with application to audio scene analysis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\eibTaY6qGI_reviews.json
    forum: https://openreview.net/forum?id=eibTaY6qGI

[76] rating=6.0 | decision=Accept | reviews=4
    title: Gogo: Group-wise granularity-ordered codec for stable and efficient speech generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\JbLmIoWwDC_reviews.json
    forum: https://openreview.net/forum?id=JbLmIoWwDC

[77] rating=6.0 | decision=None | reviews=4
    title: LipVoicer: Generating Speech from Silent Videos Guided by Lip Reading
    pdf: research_data\iclr\video-diffusion\pdfs\LipVoicer__Generating_Speech_from_Silent_Videos_Guided_by_Lip_Reading.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ZZCPSC5OgD

[78] rating=6.0 | decision=Accept | reviews=4
    title: YuE: Scaling Open Foundation Models for Long-Form Music Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\hZy6YG2Ij8_reviews.json
    forum: https://openreview.net/forum?id=hZy6YG2Ij8

[79] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: OmniSep: Unified Omni-Modality Sound Separation with Query-Mixup
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\DkzZ1ooc7q_reviews.json
    forum: https://openreview.net/forum?id=DkzZ1ooc7q

[80] rating=6.0 | decision=Accept (Poster) | reviews=5
    title: UniWav: Towards Unified Pre-training for Speech Representation Learning and Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\yj9lLwMjnE_reviews.json
    forum: https://openreview.net/forum?id=yj9lLwMjnE

[81] rating=6.0 | decision=None | reviews=4
    title: Hallo2: Long-Duration and High-Resolution Audio-Driven Portrait Image Animation
    pdf: research_data\iclr\video-generation\pdfs\Hallo2__Long-Duration_and_High-Resolution_Audio-Driven_Portrait_Image_Animation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rkzabmWl5k

[82] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: ComSL: A Composite Speech-Language Model for End-to-End Speech-to-Text Translation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\6Qx7G1xrAk_reviews.json
    forum: https://openreview.net/forum?id=6Qx7G1xrAk

[83] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: GenSE: Generative Speech Enhancement via Language Models using Hierarchical Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\1p6xFLBU4J_reviews.json
    forum: https://openreview.net/forum?id=1p6xFLBU4J

[84] rating=6.0 | decision=Accept | reviews=3
    title: SiNGER: A Clearer Voice Distills Vision Transformers Further
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\exjrxVc2yT_reviews.json
    forum: https://openreview.net/forum?id=exjrxVc2yT

[85] rating=6.0 | decision=None | reviews=4
    title: DiffPoseTalk: Speech-Driven Stylistic 3D Facial Animation and Head Pose Generation via Diffusion Models
    pdf: research_data\iclr\video-generation\pdfs\DiffPoseTalk__Speech-Driven_Stylistic_3D_Facial_Animation_and_Head_Pose_Generati.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=PORUmWsgBN

[86] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: Vocos: Closing the gap between time-domain and Fourier-based neural vocoders for high-quality audio synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\vY9nzQmQBw_reviews.json
    forum: https://openreview.net/forum?id=vY9nzQmQBw

[87] rating=6.0 | decision=Accept | reviews=4
    title: AC-Foley: Reference-Audio-Guided Video-to-Audio Synthesis with Acoustic Transfer
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\URPXhnWdBF_reviews.json
    forum: https://openreview.net/forum?id=URPXhnWdBF

[88] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: Rethinking Audio-Visual Adversarial Vulnerability from Temporal and Modality Perspectives
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\ePJrZLIqpV_reviews.json
    forum: https://openreview.net/forum?id=ePJrZLIqpV

[89] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: PromptTTS 2: Describing and Generating Voices with Text Prompt
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\NsCXDyv2Bn_reviews.json
    forum: https://openreview.net/forum?id=NsCXDyv2Bn

[90] rating=6.0 | decision=Accept | reviews=4
    title: SpeechOp: Inference-Time Task Composition for Generative Speech Processing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\eLsEjjFODE_reviews.json
    forum: https://openreview.net/forum?id=eLsEjjFODE

[91] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: Frieren: Efficient Video-to-Audio Generation Network with Rectified Flow Matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\prXfM5X2Db_reviews.json
    forum: https://openreview.net/forum?id=prXfM5X2Db

[92] rating=6.0 | decision=Accept | reviews=4
    title: Declarative Audio Editing with Audio Language Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\eNmANCkefl_reviews.json
    forum: https://openreview.net/forum?id=eNmANCkefl

[93] rating=6.0 | decision=Accept | reviews=4
    title: Elucidating the Design Space of Text-to-Audio Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\xmgvF0sLIn_reviews.json
    forum: https://openreview.net/forum?id=xmgvF0sLIn

[94] rating=6.0 | decision=Accept (Poster) | reviews=5
    title: DASpeech: Directed Acyclic Transformer for Fast and High-quality Speech-to-Speech Translation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\JvYSSPtQyk_reviews.json
    forum: https://openreview.net/forum?id=JvYSSPtQyk

[95] rating=6.0 | decision=Accept | reviews=4
    title: Generative Adversarial Post-Training Mitigates Reward Hacking in Live Human-AI Music Interaction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\FXm5U16vxD_reviews.json
    forum: https://openreview.net/forum?id=FXm5U16vxD

[96] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\NGrINZyZKk_reviews.json
    forum: https://openreview.net/forum?id=NGrINZyZKk

[97] rating=6.0 | decision=Accept | reviews=4
    title: Bridging Fairness and Explainability: Can Input-Based Explanations Promote Fairness in Hate Speech Detection?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\fPMu3Afv3s_reviews.json
    forum: https://openreview.net/forum?id=fPMu3Afv3s

[98] rating=6.0 | decision=Accept | reviews=3
    title: Closing the Gap Between Text and Speech Understanding in LLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\dDHnO3Vhyj_reviews.json
    forum: https://openreview.net/forum?id=dDHnO3Vhyj

[99] rating=6.0 | decision=Accept | reviews=4
    title: MuseCoco: Generating Symbolic Music from Text
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\yvxDJ8eyBu_reviews.json
    forum: https://openreview.net/forum?id=yvxDJ8eyBu

[100] rating=6.0 | decision=Accept | reviews=4
    title: Discovering and Steering Interpretable Concepts in Large Generative Music Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\mGtEoLYr9j_reviews.json
    forum: https://openreview.net/forum?id=mGtEoLYr9j

[101] rating=6.0 | decision=None | reviews=3
    title: PrismAudio: Decomposed Chain-of-Thought and Multi-dimensional Rewards for Video-to-Audio Generation
    pdf: research_data\iclr\video-generation\pdfs\Mixture_of_Contexts_for_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=cIfDKEbAky

[102] rating=6.0 | decision=None | reviews=4
    title: DAWN: Dynamic Frame Avatar with Non-autoregressive Diffusion Framework for Talking head Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Adaptive_Caching_for_Faster_Video_Generation_with_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=vjHySpxDsv

[103] rating=6.0 | decision=Accept (Poster) | reviews=5
    title: AV-NeRF: Learning Neural Fields for Real-World Audio-Visual Scene Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\snY3FOnlQi_reviews.json
    forum: https://openreview.net/forum?id=snY3FOnlQi

[104] rating=6.0 | decision=None | reviews=4
    title: MMDisCo: Multi-Modal Discriminator-Guided Cooperative Diffusion for Joint Audio and Video Generation
    pdf: research_data\iclr\video-generation\pdfs\MM-LDM__Multi-Modal_Latent_Diffusion_Model_for_Sounding_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=agbiPPuSeQ

[105] rating=6.0 | decision=Accept | reviews=4
    title: AVERE: Improving Audiovisual Emotion Reasoning with Preference Optimization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\td682AAuPr_reviews.json
    forum: https://openreview.net/forum?id=td682AAuPr

[106] rating=6.0 | decision=Accept (Poster) | reviews=6
    title: Differentiable Modal Synthesis for Physical Modeling of Planar String Sound and Motion Simulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\fpxRpPbF1t_reviews.json
    forum: https://openreview.net/forum?id=fpxRpPbF1t

[107] rating=6.0 | decision=Accept | reviews=4
    title: Sound Verification of Deployed Neural Networks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\5IHuwRwMHK_reviews.json
    forum: https://openreview.net/forum?id=5IHuwRwMHK

[108] rating=6.0 | decision=Accept | reviews=4
    title: WearVox: An Egocentric Multichannel Voice Assistant Benchmark for Wearables
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QpaNErg7ug_reviews.json
    forum: https://openreview.net/forum?id=QpaNErg7ug

[109] rating=6.0 | decision=Accept | reviews=4
    title: Latent Speech-Text Transformer
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\krGpQzo8Mz_reviews.json
    forum: https://openreview.net/forum?id=krGpQzo8Mz

[110] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: MDSGen: Fast and Efficient Masked Diffusion Temporal-Aware Transformers for Open-Domain Sound Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\yFEqYwgttJ_reviews.json
    forum: https://openreview.net/forum?id=yFEqYwgttJ

[111] rating=6.0 | decision=Accept | reviews=4
    title: Entropy-Monitored Kernelized Token Distillation for Audio-Visual Compression
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\nspzrcvzcB_reviews.json
    forum: https://openreview.net/forum?id=nspzrcvzcB

[112] rating=5.8 | decision=Accept | reviews=5
    title: NIRANTAR: Continual Learning with New Languages and Domains on Real-world Speech Data
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Exnt2DcdKD_reviews.json
    forum: https://openreview.net/forum?id=Exnt2DcdKD

[113] rating=5.8 | decision=Accept (Poster) | reviews=10
    title: Talking Heads: Understanding Inter-Layer Communication in Transformer Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\LUsx0chTsL_reviews.json
    forum: https://openreview.net/forum?id=LUsx0chTsL

[114] rating=5.8 | decision=Accept (Poster) | reviews=5
    title: From Discrete Tokens to High-Fidelity Audio Using Multi-Band Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\dOanKg3jKS_reviews.json
    forum: https://openreview.net/forum?id=dOanKg3jKS

[115] rating=5.8 | decision=Accept (Poster) | reviews=5
    title: Talking Turns: Benchmarking Audio Foundation Models on Turn-Taking Dynamics
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\2e4ECh0ikn_reviews.json
    forum: https://openreview.net/forum?id=2e4ECh0ikn

[116] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: DiffAR: Denoising Diffusion Autoregressive Model for Raw Speech Waveform Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\GTk0AdOYLq_reviews.json
    forum: https://openreview.net/forum?id=GTk0AdOYLq

[117] rating=5.8 | decision=Accept | reviews=4
    title: The Curse of Multi-Modalities: Evaluating Hallucinations of Large Multimodal Models across Language, Visual, and Audio
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\VeSsiD0DP9_reviews.json
    forum: https://openreview.net/forum?id=VeSsiD0DP9

[118] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: Speech Robust Bench: A Robustness Benchmark For Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\D0LuQNZfEl_reviews.json
    forum: https://openreview.net/forum?id=D0LuQNZfEl

[119] rating=5.8 | decision=None | reviews=4
    title: MM-LDM: Multi-Modal Latent Diffusion Model for Sounding Video Generation
    pdf: research_data\iclr\video-generation\pdfs\MM-LDM__Multi-Modal_Latent_Diffusion_Model_for_Sounding_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=XqLcFMMwNb

[120] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: Generative Pre-training for Speech with Flow Matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\KpoQSgxbKH_reviews.json
    forum: https://openreview.net/forum?id=KpoQSgxbKH

[121] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: Images that Sound: Composing Images and Sounds on a Single Canvas
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\aAR0ejrYw1_reviews.json
    forum: https://openreview.net/forum?id=aAR0ejrYw1

[122] rating=5.8 | decision=Reject | reviews=4
    title: Sparse Alignment Enhanced Latent Diffusion Transformer for Zero-Shot Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\o362EkNU2z_reviews.json
    forum: https://openreview.net/forum?id=o362EkNU2z

[123] rating=5.8 | decision=Accept | reviews=4
    title: VChangeCodec: A High-efficiency Neural Speech Codec with Built-in Voice Changer for Real-time Communication
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\qDSfOQBrOD_reviews.json
    forum: https://openreview.net/forum?id=qDSfOQBrOD

[124] rating=5.8 | decision=Accept | reviews=4
    title: LLark: A Multimodal Foundation Model for Music
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\7fwzPsn1lJ_reviews.json
    forum: https://openreview.net/forum?id=7fwzPsn1lJ

[125] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\AF9Q8Vip84_reviews.json
    forum: https://openreview.net/forum?id=AF9Q8Vip84

[126] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: MAViL: Masked Audio-Video Learners
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\OmTMaTbjac_reviews.json
    forum: https://openreview.net/forum?id=OmTMaTbjac

[127] rating=5.7 | decision=Accept | reviews=3
    title: OTTC: A differentiable alignment approach to automatic speech recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\EMpvfnzQqD_reviews.json
    forum: https://openreview.net/forum?id=EMpvfnzQqD

[128] rating=5.7 | decision=None | reviews=3
    title: FOLEYCRAFTER: BRING SILENT VIDEOS TO LIFE WITH LIFELIKE AND SYNCHRONIZED SOUNDS
    pdf: research_data\iclr\video-diffusion\pdfs\FOLEYCRAFTER__BRING_SILENT_VIDEOS_TO_LIFE_WITH_LIFELIKE_AND_SYNCHRONIZED_SOUNDS.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=4cQVUNpPkt

[129] rating=5.7 | decision=Accept | reviews=6
    title: FlexiCodec: A Dynamic Neural Audio Codec for Low Frame Rates
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\kYkfCs4ZAH_reviews.json
    forum: https://openreview.net/forum?id=kYkfCs4ZAH

[130] rating=5.7 | decision=Accept | reviews=3
    title: MuVi: Video-to-Music Generation with Semantic Alignment and Rhythmic Synchronization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\E040QmNETN_reviews.json
    forum: https://openreview.net/forum?id=E040QmNETN

[131] rating=5.7 | decision=Accept (Poster) | reviews=6
    title: Listenable Maps for Zero-Shot Audio Classifiers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\lV1wGHKd5x_reviews.json
    forum: https://openreview.net/forum?id=lV1wGHKd5x

[132] rating=5.7 | decision=Accept | reviews=3
    title: SpeechFake: A Large-Scale Multilingual Speech Deepfake Dataset Toward Cutting-Edge Speech Generation Methods
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\GpUO6qYNQG_reviews.json
    forum: https://openreview.net/forum?id=GpUO6qYNQG

[133] rating=5.7 | decision=Reject | reviews=3
    title: The Brain's Bitter Lesson: Scaling Speech Decoding With Self-Supervised Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\IAFStwZPNu_reviews.json
    forum: https://openreview.net/forum?id=IAFStwZPNu

[134] rating=5.6 | decision=Accept | reviews=5
    title: Echo: Towards Advanced Audio Comprehension via Audio-Interleaved Reasoning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\xI6yOdOtga_reviews.json
    forum: https://openreview.net/forum?id=xI6yOdOtga

[135] rating=5.6 | decision=None | reviews=5
    title: Realistic-Gesture: Co-Speech Gesture Video Generation through Semantic-aware Gesture Representation
    pdf: research_data\iclr\video-generation\pdfs\Realistic-Gesture__Co-Speech_Gesture_Video_Generation_through_Semantic-aware_Ges.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=EXsiGFkwV6

[136] rating=5.6 | decision=Accept | reviews=5
    title: Lifelong Audio-video Masked Autoencoder with Forget-robust Localized Alignments
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\GGPyzKsHZ1_reviews.json
    forum: https://openreview.net/forum?id=GGPyzKsHZ1

[137] rating=5.6 | decision=Accept | reviews=5
    title: STAR-Bench: Probing Deep Spatio-Temporal Reasoning as Audio 4D Intelligence
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Ts6j3GoZDE_reviews.json
    forum: https://openreview.net/forum?id=Ts6j3GoZDE

[138] rating=5.6 | decision=Accept | reviews=5
    title: Knowing When to Quit: Probabilistic Early Exits for Speech Separation Networks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\RKzBRfV6J8_reviews.json
    forum: https://openreview.net/forum?id=RKzBRfV6J8

[139] rating=5.6 | decision=Accept (Poster) | reviews=10
    title: Du-IN: Discrete units-guided mask modeling for decoding speech from Intracranial Neural signals
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\uyLtEFnpQP_reviews.json
    forum: https://openreview.net/forum?id=uyLtEFnpQP

[140] rating=5.5 | decision=Accept | reviews=4
    title: Measuring Audio's Impact on Correctness: Audio-Contribution-Aware Post-Training of Large Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\sJ0jUO9Mxr_reviews.json
    forum: https://openreview.net/forum?id=sJ0jUO9Mxr

[141] rating=5.5 | decision=Accept | reviews=4
    title: Structured-Noise Masked Modeling for Video, Audio and Beyond
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ksEMDtSj53_reviews.json
    forum: https://openreview.net/forum?id=ksEMDtSj53

[142] rating=5.5 | decision=Accept | reviews=4
    title: Beyond Instance-Level Alignment: Dual-Level Optimal Transport for Audio-Text Retrieval
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\cFhcd4WGjO_reviews.json
    forum: https://openreview.net/forum?id=cFhcd4WGjO

[143] rating=5.5 | decision=None | reviews=4
    title: Improved Quality, Synchrony, and Preference Alignment for Joint Audio-Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Improved_Quality,_Synchrony,_and_Preference_Alignment_for_Joint_Audio-Video_Gene.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=hRRWfFpKRp

[144] rating=5.5 | decision=Accept (Poster) | reviews=4
    title: RobustTSF: Towards Theory and Design of Robust Time Series Forecasting with Anomalies
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\ltZ9ianMth_reviews.json
    forum: https://openreview.net/forum?id=ltZ9ianMth

[145] rating=5.5 | decision=Accept | reviews=4
    title: Towards True Speech-to-Speech Models Without Text Guidance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\zjaV5zmlkl_reviews.json
    forum: https://openreview.net/forum?id=zjaV5zmlkl

[146] rating=5.5 | decision=Accept (Poster) | reviews=4
    title: Revisit Weakly-Supervised Audio-Visual Video Parsing from the Language Perspective
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\doWqIXcRlq_reviews.json
    forum: https://openreview.net/forum?id=doWqIXcRlq

[147] rating=5.5 | decision=Accept | reviews=4
    title: Enhancing Zero-shot Text-to-Speech Synthesis with Human Feedback
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\bAdSmSR10C_reviews.json
    forum: https://openreview.net/forum?id=bAdSmSR10C

[148] rating=5.5 | decision=Reject | reviews=4
    title: Time-Accurate Speech Rich Transcription with Non-Fluencies
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\gHPUXP51L0_reviews.json
    forum: https://openreview.net/forum?id=gHPUXP51L0

[149] rating=5.5 | decision=Accept (Poster) | reviews=4
    title: AUDIT: Audio Editing by Following Instructions with Latent Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\EO1KuHoR0V_reviews.json
    forum: https://openreview.net/forum?id=EO1KuHoR0V

[150] rating=5.5 | decision=Accept | reviews=4
    title: ASROB: Measuring Automatic Speech Recognition from One Book
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\sjvz40tazX_reviews.json
    forum: https://openreview.net/forum?id=sjvz40tazX

[151] rating=5.5 | decision=Accept | reviews=4
    title: Continuous Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\MFrJ3NzA5H_reviews.json
    forum: https://openreview.net/forum?id=MFrJ3NzA5H

[152] rating=5.5 | decision=Accept (Poster) | reviews=4
    title: AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\0BujOfTqab_reviews.json
    forum: https://openreview.net/forum?id=0BujOfTqab

[153] rating=5.5 | decision=Accept | reviews=4
    title: SPARQ: Outlier-free SpeechLM with Fast Adaptation and Robust Quantization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Z2uhdwOrn0_reviews.json
    forum: https://openreview.net/forum?id=Z2uhdwOrn0

[154] rating=5.5 | decision=Accept | reviews=4
    title: SummaryMixing: A Linear-Complexity Alternative to Self-Attention for Speech Recognition and Understanding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\PoBB8n52oi_reviews.json
    forum: https://openreview.net/forum?id=PoBB8n52oi

[155] rating=5.5 | decision=Accept | reviews=4
    title: A$^2$-Flow: Alignment-Aware Pre-training for Speech Synthesis with Flow Matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\e2p1BWR3vq_reviews.json
    forum: https://openreview.net/forum?id=e2p1BWR3vq

[156] rating=5.5 | decision=Accept | reviews=4
    title: OpenPros: A Large-Scale Dataset for Limited View Prostate Ultrasound Computed Tomography
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\kcFEpBagea_reviews.json
    forum: https://openreview.net/forum?id=kcFEpBagea

[157] rating=5.5 | decision=Accept (Poster) | reviews=4
    title: P-Flow: A Fast and Data-Efficient Zero-Shot TTS through Speech Prompting
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\zNA7u7wtIN_reviews.json
    forum: https://openreview.net/forum?id=zNA7u7wtIN

[158] rating=5.5 | decision=Accept | reviews=4
    title: LLM2Fx-Tools: Tool Calling for Music Post-Production
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\OyIJvyyB3R_reviews.json
    forum: https://openreview.net/forum?id=OyIJvyyB3R

[159] rating=5.5 | decision=Accept | reviews=4
    title: Efficient Audio-Visual Speech Separation with Discrete Lip Semantics and Multi-Scale Global-Local Attention
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\LaIkPfPu9K_reviews.json
    forum: https://openreview.net/forum?id=LaIkPfPu9K

[160] rating=5.5 | decision=Accept | reviews=4
    title: CS-Dialogue: A 104-Hour Dataset of Spontaneous Mandarin-English Code-Switching Dialogues for Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Y3auRTgDEX_reviews.json
    forum: https://openreview.net/forum?id=Y3auRTgDEX

[161] rating=5.5 | decision=Accept | reviews=4
    title: Flow2GAN: Hybrid Flow Matching and GAN with Multi-Resolution Network for One-/Two-step High-Fidelity Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\5eTpRIULtb_reviews.json
    forum: https://openreview.net/forum?id=5eTpRIULtb

[162] rating=5.5 | decision=Accept | reviews=4
    title: RepCodec: A Speech Representation Codec for Speech Tokenization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\LfDUzzQa3g_reviews.json
    forum: https://openreview.net/forum?id=LfDUzzQa3g

[163] rating=5.5 | decision=Accept | reviews=4
    title: Human or Machine? A Preliminary Turing Test for Speech-to-Speech Interaction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Pv5l6cvfno_reviews.json
    forum: https://openreview.net/forum?id=Pv5l6cvfno

[164] rating=5.5 | decision=Accept | reviews=4
    title: Representing speech through autoregressive prediction of cochlear tokens
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\TQdg1X6eqm_reviews.json
    forum: https://openreview.net/forum?id=TQdg1X6eqm

[165] rating=5.5 | decision=None | reviews=4
    title: SyncLipMAE: Contrastive Masked Pretraining for Audio–Visual Talking-Face Representations
    pdf: research_data\iclr\talking-head\pdfs\SyncLipMAE__Contrastive_Masked_Pretraining_for_Audio–Visual_Talking-Face_Represe.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=HgdXXylDjs

[166] rating=5.5 | decision=Accept | reviews=4
    title: Epistemic-Aware Vision–Language Foundation Model for Fetal Ultrasound Interpretation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Z8GPdfPLFa_reviews.json
    forum: https://openreview.net/forum?id=Z8GPdfPLFa

[167] rating=5.5 | decision=Accept | reviews=4
    title: SSR: Alignment-Aware Modality Connector for Speech Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\tZDhrhUOcs_reviews.json
    forum: https://openreview.net/forum?id=tZDhrhUOcs

[168] rating=5.4 | decision=Accept (Poster) | reviews=5
    title: Pengi: An Audio Language Model for Audio Tasks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\gJLAfO4KUq_reviews.json
    forum: https://openreview.net/forum?id=gJLAfO4KUq

[169] rating=5.4 | decision=Accept (Poster) | reviews=10
    title: Continual Audio-Visual Sound Separation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\PZCiWtQjAw_reviews.json
    forum: https://openreview.net/forum?id=PZCiWtQjAw

[170] rating=5.4 | decision=None | reviews=5
    title: Orator: LLM-Guided Multi-Shot Speech Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Orator__LLM-Guided_Multi-Shot_Speech_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Bz6eAiOjrI

[171] rating=5.4 | decision=Accept | reviews=5
    title: SoundStorm: Efficient Parallel Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\KknWbD5j95_reviews.json
    forum: https://openreview.net/forum?id=KknWbD5j95

[172] rating=5.4 | decision=Reject | reviews=5
    title: A Discrete and Variational Approach to Speech Representation Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\rQRDt8F2Yh_reviews.json
    forum: https://openreview.net/forum?id=rQRDt8F2Yh

[173] rating=5.4 | decision=Accept (Poster) | reviews=5
    title: Efficient Neural Music Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\cxazQGSsQa_reviews.json
    forum: https://openreview.net/forum?id=cxazQGSsQa

[174] rating=5.4 | decision=Accept | reviews=5
    title: dMel: Speech Tokenization Made Simple
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\BomQa84efw_reviews.json
    forum: https://openreview.net/forum?id=BomQa84efw

[175] rating=5.4 | decision=Accept (Poster) | reviews=5
    title: Disentangled Counterfactual Learning for Physical Audiovisual Commonsense Reasoning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\trHfuGQyyr_reviews.json
    forum: https://openreview.net/forum?id=trHfuGQyyr

[176] rating=5.3 | decision=Accept | reviews=3
    title: TTSDS2: Resources and Benchmark for Evaluating Human-Quality Text to Speech Systems
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\uGai5lYHlV_reviews.json
    forum: https://openreview.net/forum?id=uGai5lYHlV

[177] rating=5.3 | decision=Accept | reviews=3
    title: Instruction-Tuned Video-Audio Models Elucidate Functional Specialization in Brain
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\EUJ33R3LwL_reviews.json
    forum: https://openreview.net/forum?id=EUJ33R3LwL

[178] rating=5.3 | decision=Accept | reviews=3
    title: Myna: Masking-Based Contrastive Learning of Musical Representations
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\gF60Ou6flQ_reviews.json
    forum: https://openreview.net/forum?id=gF60Ou6flQ

[179] rating=5.3 | decision=Accept | reviews=3
    title: Drax: Speech Recognition with Discrete Flow Matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\E9hSdtsAG0_reviews.json
    forum: https://openreview.net/forum?id=E9hSdtsAG0

[180] rating=5.3 | decision=Accept | reviews=3
    title: TVTSyn: Content-Synchronous Time-Varying Timbre for Streaming Voice Conversion and Anonymization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Tf4Lfw85lS_reviews.json
    forum: https://openreview.net/forum?id=Tf4Lfw85lS

[181] rating=5.3 | decision=Accept | reviews=3
    title: Scalable Multilingual Multimodal Machine Translation with Speech-Text Fusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\HQMVRQUEaM_reviews.json
    forum: https://openreview.net/forum?id=HQMVRQUEaM

[182] rating=5.3 | decision=Accept (Poster) | reviews=3
    title: NatureLM-audio: an Audio-Language Foundation Model for Bioacoustics
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\hJVdwBpWjt_reviews.json
    forum: https://openreview.net/forum?id=hJVdwBpWjt

[183] rating=5.3 | decision=Accept | reviews=3
    title: Speech World Model: Causal State–Action Planning with Explicit Reasoning for Speech
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\YGUKPGO182_reviews.json
    forum: https://openreview.net/forum?id=YGUKPGO182

[184] rating=5.3 | decision=Accept | reviews=3
    title: Steering Autoregressive Music Generation with Recursive Feature Machines
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\NaHzPMaCY9_reviews.json
    forum: https://openreview.net/forum?id=NaHzPMaCY9

[185] rating=5.3 | decision=Accept | reviews=3
    title: Physics-Informed Audio-Geometry-Grid Representation Learning for Universal Sound Source Localization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bWXpJFesLS_reviews.json
    forum: https://openreview.net/forum?id=bWXpJFesLS

[186] rating=5.3 | decision=Accept | reviews=3
    title: OWL : Geometry-Aware Spatial Reasoning for Audio Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\zPv46YKv3w_reviews.json
    forum: https://openreview.net/forum?id=zPv46YKv3w

[187] rating=5.2 | decision=Accept | reviews=4
    title: Generative Pre-Trained Speech Language Model with Efficient Hierarchical Transformer
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\TJNCnkDRkY_reviews.json
    forum: https://openreview.net/forum?id=TJNCnkDRkY

[188] rating=5.2 | decision=Accept | reviews=4
    title: AVESFormer: Efficient Transformer Design for Real-Time Audio-Visual Segmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\u8SYRtXDsZ_reviews.json
    forum: https://openreview.net/forum?id=u8SYRtXDsZ

[189] rating=5.2 | decision=Reject | reviews=4
    title: Personalized Facial Expressions and Head Poses for Speech-Driven 3D Facial Animation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\HJVe0NH4qq_reviews.json
    forum: https://openreview.net/forum?id=HJVe0NH4qq

[190] rating=5.2 | decision=Reject | reviews=4
    title: Segment, Associate, and Classify: Decoupled Audio-Visual Segmentation Framework
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\8VnS320esG_reviews.json
    forum: https://openreview.net/forum?id=8VnS320esG

[191] rating=5.2 | decision=Accept | reviews=4
    title: Reverse the auditory processing pathway: Coarse-to-fine audio reconstruction from fMRI
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\3JoLo0mmHH_reviews.json
    forum: https://openreview.net/forum?id=3JoLo0mmHH

[192] rating=5.2 | decision=Accept | reviews=4
    title: FINE-GRAINED AUDIO-VISUAL JOINT REPRESENTATIONS FOR MULTIMODAL LARGE LANGUAGE MODELS
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\wD8L86iCvD_reviews.json
    forum: https://openreview.net/forum?id=wD8L86iCvD

[193] rating=5.2 | decision=Accept (Poster) | reviews=8
    title: SILENCE: Protecting privacy in offloaded speech understanding on resource-constrained devices
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\tKuLgnDWWN_reviews.json
    forum: https://openreview.net/forum?id=tKuLgnDWWN

[194] rating=5.2 | decision=Accept (Poster) | reviews=4
    title: Weakly-Supervised Audio-Visual Segmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\sUqG96QqZM_reviews.json
    forum: https://openreview.net/forum?id=sUqG96QqZM

[195] rating=5.2 | decision=Accept (Poster) | reviews=4
    title: MaskGCT: Zero-Shot Text-to-Speech with Masked Generative Codec Transformer
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\ExuBFYtCQU_reviews.json
    forum: https://openreview.net/forum?id=ExuBFYtCQU

[196] rating=5.2 | decision=Accept (Spotlight) | reviews=12
    title: Audio Flamingo 3: Advancing Audio Intelligence with Fully Open Large Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\FjByDpDVIO_reviews.json
    forum: https://openreview.net/forum?id=FjByDpDVIO

[197] rating=5.2 | decision=Accept (Poster) | reviews=4
    title: Masked Autoencoders with Multi-Window Local-Global Attention Are Better Audio Learners
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\Q53QLftNkA_reviews.json
    forum: https://openreview.net/forum?id=Q53QLftNkA

[198] rating=5.2 | decision=Accept | reviews=4
    title: Taming Data and Transformers for Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\lidVssyB7G_reviews.json
    forum: https://openreview.net/forum?id=lidVssyB7G

[199] rating=5.2 | decision=Reject | reviews=5
    title: Collaborative Hybrid Propagator for Temporal Misalignment in Audio-Visual Segmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\yqJoqtUwSI_reviews.json
    forum: https://openreview.net/forum?id=yqJoqtUwSI

[200] rating=5.2 | decision=Accept | reviews=5
    title: Hierarchical Semantic-Acoustic Modeling via Semi-Discrete Residual Representations for Expressive End-to-End Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\h5KLpGoqzC_reviews.json
    forum: https://openreview.net/forum?id=h5KLpGoqzC

[201] rating=5.2 | decision=Accept | reviews=5
    title: TASTE: Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\6STb8DauN1_reviews.json
    forum: https://openreview.net/forum?id=6STb8DauN1

[202] rating=5.2 | decision=Reject | reviews=5
    title: ControlSpeech: Towards Simultaneous Zero-shot Speaker Cloning and Zero-shot Language Style Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\zAogQOIphH_reviews.json
    forum: https://openreview.net/forum?id=zAogQOIphH

[203] rating=5.2 | decision=Accept | reviews=5
    title: Vec-Tok Speech: Speech Vectorization and Tokenization for Neural Speech Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\C53xlgEqVh_reviews.json
    forum: https://openreview.net/forum?id=C53xlgEqVh

[204] rating=5.0 | decision=Accept | reviews=5
    title: Symbolic Music Generation with Fine-grained Interactive Textural Guidance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Qt5sBi0u7I_reviews.json
    forum: https://openreview.net/forum?id=Qt5sBi0u7I

[205] rating=5.0 | decision=None | reviews=4
    title: SyncFlow: Temporally Aligned Joint Audio-Video Generation from Text
    pdf: research_data\iclr\video-generation\pdfs\SyncFlow__Temporally_Aligned_Joint_Audio-Video_Generation_from_Text.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=J2EmNMLoxv

[206] rating=5.0 | decision=Accept | reviews=4
    title: Query-Guided Spatial–Temporal–Frequency Interaction for Music Audio–Visual Question Answering
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\8CnU2kchiw_reviews.json
    forum: https://openreview.net/forum?id=8CnU2kchiw

[207] rating=5.0 | decision=Accept | reviews=4
    title: Self-Guidance: Training VQ-VAE Decoders to be Robust to Quantization Artifacts for High-Fidelity Neural Speech Codec
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\lCaU7NlZ1I_reviews.json
    forum: https://openreview.net/forum?id=lCaU7NlZ1I

[208] rating=5.0 | decision=Accept | reviews=4
    title: EchoMind: An Interrelated Multi-level Benchmark for Evaluating Empathetic Speech Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\l5re5ppqrX_reviews.json
    forum: https://openreview.net/forum?id=l5re5ppqrX

[209] rating=5.0 | decision=Reject | reviews=4
    title: Bridge-TTS: Text-to-Speech Synthesis with Schrodinger Bridge
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\F9ApWtHVac_reviews.json
    forum: https://openreview.net/forum?id=F9ApWtHVac

[210] rating=5.0 | decision=Accept | reviews=4
    title: TangoFlux: Text to Audio Generation with CLAP-Ranked Preference Optimization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qgNs5NmQB7_reviews.json
    forum: https://openreview.net/forum?id=qgNs5NmQB7

[211] rating=5.0 | decision=Accept | reviews=4
    title: VALL-E 2: Neural Codec Language Models are Human Parity Zero-Shot Text to Speech Synthesizers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\0bcRCD7YUx_reviews.json
    forum: https://openreview.net/forum?id=0bcRCD7YUx

[212] rating=5.0 | decision=Accept | reviews=4
    title: VowelPrompt: Hearing Speech Emotions from Text via Vowel-level Prosodic Augmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\PMbionN5cC_reviews.json
    forum: https://openreview.net/forum?id=PMbionN5cC

[213] rating=5.0 | decision=Accept | reviews=4
    title: Leveraging characteristics of the output distribution for identifying adversarial audio examples
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\R1crLHQ4kf_reviews.json
    forum: https://openreview.net/forum?id=R1crLHQ4kf

[214] rating=5.0 | decision=Accept | reviews=4
    title: SupCLAP: Controlling Optimization Trajectory Drift in Audio-Text Contrastive Learning with Support Vector Regularization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\S1CW6PLsqS_reviews.json
    forum: https://openreview.net/forum?id=S1CW6PLsqS

[215] rating=5.0 | decision=Accept | reviews=8
    title: Potts Relaxations and Soft Self-labeling for Weakly-Supervised Segmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\V5Sbh42uDe_reviews.json
    forum: https://openreview.net/forum?id=V5Sbh42uDe

[216] rating=5.0 | decision=Conditional Accept | reviews=4
    title: Data-Centric Lessons To Improve Speech-Language Pretraining
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\4amNkYCDqX_reviews.json
    forum: https://openreview.net/forum?id=4amNkYCDqX

[217] rating=5.0 | decision=Accept | reviews=5
    title: WavJourney: Compositional Audio Creation with Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\8JCn0kmS8W_reviews.json
    forum: https://openreview.net/forum?id=8JCn0kmS8W

[218] rating=5.0 | decision=Accept | reviews=4
    title: SonicMaster: Towards Controllable All-in-One Music Restoration and Mastering
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\k7ifkwmsXn_reviews.json
    forum: https://openreview.net/forum?id=k7ifkwmsXn

[219] rating=5.0 | decision=Accept | reviews=4
    title: Resource Efficient Self-Supervised Learning for Speech Embeddings
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\Wsab3NhIwC_reviews.json
    forum: https://openreview.net/forum?id=Wsab3NhIwC

[220] rating=5.0 | decision=Accept | reviews=4
    title: OpenWaves: A Large-Scale Anatomically Realistic Ultrasound-CT Dataset for Benchmarking Neural Wave Equation Solvers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\u14Y236LwX_reviews.json
    forum: https://openreview.net/forum?id=u14Y236LwX

[221] rating=5.0 | decision=Accept | reviews=4
    title: Which pre-trained model is effective for speech separation ?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\qqExiDNsa7_reviews.json
    forum: https://openreview.net/forum?id=qqExiDNsa7

[222] rating=5.0 | decision=None | reviews=4
    title: Weakly Supervised Motion Learning for Co-speech Gesture Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Motion_Inversion_for_Video_Customization.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=KZKQ8Iifab

[223] rating=5.0 | decision=Reject | reviews=4
    title: Can AI Truly Represent Your Voice in Deliberations? A Comprehensive Study of Large-Scale Opinion Aggregation with LLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bl9hFm04Lc_reviews.json
    forum: https://openreview.net/forum?id=bl9hFm04Lc

[224] rating=5.0 | decision=None | reviews=5
    title: Playing For You: Text Prompt-guided Joint Audio-visual Generation for Narrating Faces using Multi-entangled Latent Space
    pdf: research_data\iclr\video-generation\pdfs\Playing_For_You__Text_Prompt-guided_Joint_Audio-visual_Generation_for_Narrating.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=kMz43DyCKA

[225] rating=5.0 | decision=Accept | reviews=4
    title: LATTS: LAtent space Test Time Scaling for diffusion language models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Q524K1mgCc_reviews.json
    forum: https://openreview.net/forum?id=Q524K1mgCc

[226] rating=5.0 | decision=Accept | reviews=4
    title: SMILE: Audio-Visual Speech Recognition with Siamese Masked Interaction Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\74IIsh2kM6_reviews.json
    forum: https://openreview.net/forum?id=74IIsh2kM6

[227] rating=5.0 | decision=Accept | reviews=4
    title: MambaVoiceCloning: Efficient and Expressive Text-to-Speech via State-Space Modeling and Diffusion Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0oXyMbPMtP_reviews.json
    forum: https://openreview.net/forum?id=0oXyMbPMtP

[228] rating=5.0 | decision=None | reviews=4
    title: InterActHuman: Multi-Concept Human Animation with Layout-Aligned Audio Conditions
    pdf: research_data\iclr\video-generation\pdfs\InterActHuman__Multi-Concept_Human_Animation_with_Layout-Aligned_Audio_Condition.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rJilRU8D3c

[229] rating=5.0 | decision=Accept | reviews=4
    title: Voice Evaluation of Reasoning Ability: Diagnosing the Modality-Induced Performance Gap
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bA51NZVNFT_reviews.json
    forum: https://openreview.net/forum?id=bA51NZVNFT

[230] rating=5.0 | decision=None | reviews=4
    title: Intentional-Gesture: Deliever your Thoughts by Gestures for Speech
    pdf: research_data\iclr\motion-generation\pdfs\Intentional-Gesture__Deliever_your_Thoughts_by_Gestures_for_Speech.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=3tGybflFMm

[231] rating=5.0 | decision=Reject | reviews=3
    title: Rethinking Audiovisual Segmentation with Semantic Quantization and Decomposition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\nuWVS4SBUu_reviews.json
    forum: https://openreview.net/forum?id=nuWVS4SBUu

[232] rating=5.0 | decision=Accept | reviews=5
    title: ACUS: Audio Captioning with Unbiased Sliced Wasserstein Kernel
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\3sf7SpOYIe_reviews.json
    forum: https://openreview.net/forum?id=3sf7SpOYIe

[233] rating=5.0 | decision=None | reviews=4
    title: UniVerse-1: Unified Audio-Video Generation via Stitching of Experts
    pdf: research_data\iclr\video-generation\pdfs\UniVerse-1__Unified_Audio-Video_Generation_via_Stitching_of_Experts.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=8aFYx2mDyE

[234] rating=5.0 | decision=Accept | reviews=4
    title: OmniCVR: A Benchmark for Omni-Composed Video Retrieval with Vision, Audio, and Text
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KxxR7emO5K_reviews.json
    forum: https://openreview.net/forum?id=KxxR7emO5K

[235] rating=5.0 | decision=Accept (Poster) | reviews=4
    title: Aria-MIDI: A Dataset of Piano MIDI Files for Symbolic Music Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\X5hrhgndxW_reviews.json
    forum: https://openreview.net/forum?id=X5hrhgndxW

[236] rating=5.0 | decision=Accept | reviews=4
    title: Speech-to-LaTeX: New Models and Datasets for Converting Spoken Equations and Sentences
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\gk8WMxzIQP_reviews.json
    forum: https://openreview.net/forum?id=gk8WMxzIQP

[237] rating=4.8 | decision=Accept | reviews=5
    title: Universal Semantic Disentangled Privacy-preserving Speech Representation Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Id2JMVSQHZ_reviews.json
    forum: https://openreview.net/forum?id=Id2JMVSQHZ

[238] rating=4.8 | decision=Accept | reviews=5
    title: HiViBiX: Hierarchical Visually-informed Binaural Audio Generation using Ambisonics
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\pzXAS6Tf2r_reviews.json
    forum: https://openreview.net/forum?id=pzXAS6Tf2r

[239] rating=4.8 | decision=Accept | reviews=5
    title: PAL: Probing Audio Encoders via LLMs - Audio Information Transfer into LLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ZUIgJSAex6_reviews.json
    forum: https://openreview.net/forum?id=ZUIgJSAex6

[240] rating=4.8 | decision=Accept | reviews=5
    title: Scaling Speech Tokenizers with Diffusion Autoencoders
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\llMfmDtWka_reviews.json
    forum: https://openreview.net/forum?id=llMfmDtWka

[241] rating=4.8 | decision=Accept | reviews=5
    title: AlignSep: Temporally-Aligned Video-Queried Sound Separation with Flow Matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DVDkFcxU1D_reviews.json
    forum: https://openreview.net/forum?id=DVDkFcxU1D

[242] rating=4.8 | decision=Accept | reviews=5
    title: Reproducing and Dissecting Denoising Language Models for Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\dS9nGa5Mun_reviews.json
    forum: https://openreview.net/forum?id=dS9nGa5Mun

[243] rating=4.8 | decision=Accept | reviews=5
    title: EvA: An Evidence-First Audio Understanding Paradigm for LALMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\PNRGSW9jPz_reviews.json
    forum: https://openreview.net/forum?id=PNRGSW9jPz

[244] rating=4.8 | decision=Accept | reviews=5
    title: Acoustic-based Gender Differentiation in Speech-aware Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\SIaH5RWfzm_reviews.json
    forum: https://openreview.net/forum?id=SIaH5RWfzm

[245] rating=4.8 | decision=Accept (Poster) | reviews=4
    title: VAST: A Vision-Audio-Subtitle-Text Omni-Modality Foundation Model and Dataset
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\scYa9DYUAy_reviews.json
    forum: https://openreview.net/forum?id=scYa9DYUAy

[246] rating=4.8 | decision=Accept | reviews=4
    title: DC-Spin: A Speaker-invariant Speech Tokenizer For Spoken Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\OW332Wh9S5_reviews.json
    forum: https://openreview.net/forum?id=OW332Wh9S5

[247] rating=4.8 | decision=Accept (Poster) | reviews=11
    title: OmniTalker: One-shot Real-time Text-Driven Talking Audio-Video Generation With Multimodal Style Mimicking
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\eK31JidsTN_reviews.json
    forum: https://openreview.net/forum?id=eK31JidsTN

[248] rating=4.8 | decision=Accept | reviews=4
    title: CerebroVoice: A Stereotactic EEG Dataset and Benchmark for Bilingual Brain-to-Speech Synthesis and Activity Detection
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\3sfOGsBh85_reviews.json
    forum: https://openreview.net/forum?id=3sfOGsBh85

[249] rating=4.8 | decision=Reject | reviews=4
    title: AVSET-10M: An Open Large-Scale Audio-Visual Dataset with High Correspondence
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\PdDm14eXO4_reviews.json
    forum: https://openreview.net/forum?id=PdDm14eXO4

[250] rating=4.8 | decision=Accept | reviews=4
    title: Enhancing Audio--Language Models through Self--Supervised Post--Training with Text--Audio Pairs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\nplYdpc1Pm_reviews.json
    forum: https://openreview.net/forum?id=nplYdpc1Pm

[251] rating=4.8 | decision=Accept (Spotlight) | reviews=12
    title: Word-Level Emotional Expression Control in Zero-Shot Text-to-Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\SYcggdxX6W_reviews.json
    forum: https://openreview.net/forum?id=SYcggdxX6W

[252] rating=4.8 | decision=Accept | reviews=4
    title: Unlocking Speech Instruction Data Potential with Query Rewriting
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\QQoWeCscSH_reviews.json
    forum: https://openreview.net/forum?id=QQoWeCscSH

[253] rating=4.8 | decision=Accept | reviews=4
    title: MapLearn: Indoor Mapping using Audio
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\PdwrCm5Msr_reviews.json
    forum: https://openreview.net/forum?id=PdwrCm5Msr

[254] rating=4.8 | decision=Reject | reviews=4
    title: Modeling Abstract Style Prompts for Text-to-Speech Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\E1DGY1FXef_reviews.json
    forum: https://openreview.net/forum?id=E1DGY1FXef

[255] rating=4.8 | decision=Accept (Poster) | reviews=11
    title: Brain-tuning Improves Generalizability and Efficiency of Brain Alignment in Speech Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\4jgsUhWWaF_reviews.json
    forum: https://openreview.net/forum?id=4jgsUhWWaF

[256] rating=4.8 | decision=Reject | reviews=4
    title: DMDSpeech: Distilled Diffusion Model Surpassing The Teacher in Zero-shot Speech Synthesis via Direct Metric Optimization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\LhuDdMEIGS_reviews.json
    forum: https://openreview.net/forum?id=LhuDdMEIGS

[257] rating=4.8 | decision=Accept | reviews=4
    title: Distilling an End-to-End Voice Assistant Without Instruction Training Data
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\yuuyPlywuO_reviews.json
    forum: https://openreview.net/forum?id=yuuyPlywuO

[258] rating=4.8 | decision=Reject | reviews=4
    title: A Simple but Strong Baseline for Sounding Video Generation: Effective Adaptation of Audio and Video Diffusion Models for Joint Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\WqL4wOU3tw_reviews.json
    forum: https://openreview.net/forum?id=WqL4wOU3tw

[259] rating=4.8 | decision=Accept | reviews=4
    title: Variational Inference for Self-Supervised Speech Models Fine-tuning on Downstream Tasks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\UT5B7fktaw_reviews.json
    forum: https://openreview.net/forum?id=UT5B7fktaw

[260] rating=4.8 | decision=Reject | reviews=4
    title: Unispeaker: A unified speech generation model for multimodality-driven voice control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\NVASzf27bL_reviews.json
    forum: https://openreview.net/forum?id=NVASzf27bL

[261] rating=4.7 | decision=Accept | reviews=3
    title: JALMBench: Benchmarking Jailbreak Vulnerabilities in Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DJkQ236C8B_reviews.json
    forum: https://openreview.net/forum?id=DJkQ236C8B

[262] rating=4.7 | decision=Accept | reviews=3
    title: Can Speech LLMs Think while Listening?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\dFVenZdVbX_reviews.json
    forum: https://openreview.net/forum?id=dFVenZdVbX

[263] rating=4.7 | decision=Accept (Spotlight) | reviews=9
    title: ARECHO: Autoregressive Evaluation via Chain-Based Hypothesis Optimization for Speech Multi-Metric Estimation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\P2yIMJP5b1_reviews.json
    forum: https://openreview.net/forum?id=P2yIMJP5b1

[264] rating=4.7 | decision=None | reviews=3
    title: X-Streamer: Unified Human World Modeling with Audiovisual Interaction
    pdf: research_data\iclr\portrait-animation\pdfs\X-Streamer__Unified_Human_World_Modeling_with_Audiovisual_Interaction.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rCNe4N7cP4

[265] rating=4.7 | decision=Accept | reviews=3
    title: SwiftTS: A Swift Selection Framework for Time Series Pre-trained Models via Multi-task Meta-Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\XrmXvv75KP_reviews.json
    forum: https://openreview.net/forum?id=XrmXvv75KP

[266] rating=4.7 | decision=Accept | reviews=3
    title: UniSS: Unified Expressive Speech-to-Speech Translation with Your Voice
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\5o0ZvYzh6B_reviews.json
    forum: https://openreview.net/forum?id=5o0ZvYzh6B

[267] rating=4.7 | decision=Accept | reviews=3
    title: Confident and Adaptive Generative Speech Recognition via Conformal Risk Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ck5T7QeiDh_reviews.json
    forum: https://openreview.net/forum?id=ck5T7QeiDh

[268] rating=4.7 | decision=Accept | reviews=3
    title: FUAS-Agents: Autonomous Multi-Modal LLM Agents for Treatment Planning in Focused Ultrasound Ablation Surgery
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\xRy3olU4GT_reviews.json
    forum: https://openreview.net/forum?id=xRy3olU4GT

[269] rating=4.7 | decision=Accept | reviews=3
    title: MoST: Mixing Speech and Text with Modality-Aware Mixture of Experts
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\BlbLPArfCD_reviews.json
    forum: https://openreview.net/forum?id=BlbLPArfCD

[270] rating=4.7 | decision=Accept | reviews=3
    title: Brain2Music: Reconstructing Music from Human Brain Activity
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\SJPUmX4LXD_reviews.json
    forum: https://openreview.net/forum?id=SJPUmX4LXD

[271] rating=4.6 | decision=Accept | reviews=5
    title: Zero-Shot Text-to-Speech from Continuous Text Streams
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\RK3Gj9J5my_reviews.json
    forum: https://openreview.net/forum?id=RK3Gj9J5my

[272] rating=4.6 | decision=Accept | reviews=5
    title: Analyzing and Mitigating Inconsistency in Discrete Audio Tokens for Neural Codec Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\KFLtFSOtdj_reviews.json
    forum: https://openreview.net/forum?id=KFLtFSOtdj

[273] rating=4.6 | decision=Reject | reviews=5
    title: DNASpeech: A Contextualized and Situated Text-to-Speech Dataset with Dialogues, Narratives and Actions
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\ZGRZ5GPKWX_reviews.json
    forum: https://openreview.net/forum?id=ZGRZ5GPKWX

[274] rating=4.6 | decision=Accept | reviews=5
    title: Machine Unlearning in Audio: Bridging The Modality Gap Via the Prune and Regrow Paradigm
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\i3tBySZWrR_reviews.json
    forum: https://openreview.net/forum?id=i3tBySZWrR

[275] rating=4.5 | decision=Reject | reviews=4
    title: On more accurate alignment modeling methods for automatic speech recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\7NlGsjrEd8_reviews.json
    forum: https://openreview.net/forum?id=7NlGsjrEd8

[276] rating=4.5 | decision=Accept | reviews=4
    title: DeepOmni: Towards Seamless and Smart Speech Interaction with Adaptive Modality-Specific MoE
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\RQhHdNJQlE_reviews.json
    forum: https://openreview.net/forum?id=RQhHdNJQlE

[277] rating=4.5 | decision=Reject | reviews=4
    title: ViML: A Video, Music, Language Unified Dataset for Understanding and Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Tgsc0KEkN6_reviews.json
    forum: https://openreview.net/forum?id=Tgsc0KEkN6

[278] rating=4.5 | decision=Accept | reviews=4
    title: Towards an AI Musician: Synthesizing Sheet Music Problems for Musical Reasoning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\6EO8JzLyBS_reviews.json
    forum: https://openreview.net/forum?id=6EO8JzLyBS

[279] rating=4.5 | decision=Accept | reviews=4
    title: EQUALS: An Audio-Visual LLM with One-Stage Question-Guided Alignment and Flexible Fusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\D5sN85PDx7_reviews.json
    forum: https://openreview.net/forum?id=D5sN85PDx7

[280] rating=4.5 | decision=Accept | reviews=4
    title: Hallucination Benchmark for Speech Foundation Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\YkfhTzq3hL_reviews.json
    forum: https://openreview.net/forum?id=YkfhTzq3hL

[281] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: PreFM: Online Audio-Visual Event Parsing via Predictive Future Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\kWZRLR7w52_reviews.json
    forum: https://openreview.net/forum?id=kWZRLR7w52

[282] rating=4.5 | decision=Accept | reviews=4
    title: TTS Can Speak in Any Style with Any Voice
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\F7GmbfyVg9_reviews.json
    forum: https://openreview.net/forum?id=F7GmbfyVg9

[283] rating=4.5 | decision=Reject | reviews=4
    title: Audio-driven 3D Conversational Full-body Human Avatar Generation from a Single Image
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\oATS6CUmC7_reviews.json
    forum: https://openreview.net/forum?id=oATS6CUmC7

[284] rating=4.5 | decision=Accept (Spotlight) | reviews=11
    title: JavisGPT: A Unified Multi-modal LLM for Sounding-Video Comprehension and Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\MZoOpD9NHV_reviews.json
    forum: https://openreview.net/forum?id=MZoOpD9NHV

[285] rating=4.5 | decision=Accept | reviews=4
    title: TFMAudio: High-Fidelity Long-Form Text-to-Audio via Mamba-based Flow Matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\WFgtMF6vk6_reviews.json
    forum: https://openreview.net/forum?id=WFgtMF6vk6

[286] rating=4.5 | decision=Reject | reviews=4
    title: EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\6p9n68cxGM_reviews.json
    forum: https://openreview.net/forum?id=6p9n68cxGM

[287] rating=4.5 | decision=Reject | reviews=4
    title: AnyAvatar: Dynamic and Consistent Audio-Driven Human Animation for Multiple Characters
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\tRLShDqhmi_reviews.json
    forum: https://openreview.net/forum?id=tRLShDqhmi

[288] rating=4.5 | decision=Accept | reviews=4
    title: Can LLMs Reason Soundly in Law? Auditing Inference Patterns for Legal Judgment
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\5T0BXtJxzN_reviews.json
    forum: https://openreview.net/forum?id=5T0BXtJxzN

[289] rating=4.5 | decision=Accept | reviews=4
    title: From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ZBXc88hTd9_reviews.json
    forum: https://openreview.net/forum?id=ZBXc88hTd9

[290] rating=4.5 | decision=Accept | reviews=4
    title: Towards Unsupervised Speech Recognition at the Syllable-Level
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0fk3GVbJPm_reviews.json
    forum: https://openreview.net/forum?id=0fk3GVbJPm

[291] rating=4.5 | decision=Accept | reviews=4
    title: FoleyGenEx: Unified Video-to-Audio Generation with Multi-Modal Control, Temporal Alignment, and Semantic Precision
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\99CJ4Slq0i_reviews.json
    forum: https://openreview.net/forum?id=99CJ4Slq0i

[292] rating=4.5 | decision=Accept | reviews=4
    title: DurMI: Duration Loss as a Membership Signal in TTS Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\NvHFk2D2g3_reviews.json
    forum: https://openreview.net/forum?id=NvHFk2D2g3

[293] rating=4.5 | decision=Accept | reviews=4
    title: DASB-Discrete Audio and Speech Benchmark
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\nsFucJqKmR_reviews.json
    forum: https://openreview.net/forum?id=nsFucJqKmR

[294] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: SALMONN-omni: A Standalone Speech LLM without Codec Injection for Full-duplex Conversation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\AsRB5nmlOD_reviews.json
    forum: https://openreview.net/forum?id=AsRB5nmlOD

[295] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Objective Soups: Multilingual Multi-Task Modeling for Speech Processing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\u0YyIHljXO_reviews.json
    forum: https://openreview.net/forum?id=u0YyIHljXO

[296] rating=4.5 | decision=Accept | reviews=4
    title: AVI-Bench: Toward Human-like Audio-Visual Intelligence of Omni-MLLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\SJQj5INbyl_reviews.json
    forum: https://openreview.net/forum?id=SJQj5INbyl

[297] rating=4.5 | decision=Accept | reviews=4
    title: UDDETTS: Unifying Discrete and Dimensional Emotions for Controllable Emotional Text-to-Speech
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DuPYSaCiep_reviews.json
    forum: https://openreview.net/forum?id=DuPYSaCiep

[298] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Audio Super-Resolution with Latent Bridge Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\LkA1yLshF8_reviews.json
    forum: https://openreview.net/forum?id=LkA1yLshF8

[299] rating=4.5 | decision=Reject | reviews=4
    title: Towards Fine-grained Audio Captioning with Multimodal Contextual Fusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\3q3LnQ63Az_reviews.json
    forum: https://openreview.net/forum?id=3q3LnQ63Az

[300] rating=4.5 | decision=Accept | reviews=4
    title: Fast Text-to-Audio Generation with One-Step Sampling via Energy-Scoring and Auxiliary Contextual Representation Distillation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QU8raq5UhG_reviews.json
    forum: https://openreview.net/forum?id=QU8raq5UhG

[301] rating=4.5 | decision=Accept (Poster) | reviews=8
    title: Aligning Audio-Visual Joint Representations with an Agentic Workflow
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\QMaLS4VeY3_reviews.json
    forum: https://openreview.net/forum?id=QMaLS4VeY3

[302] rating=4.5 | decision=Accept | reviews=4
    title: OmniVideoBench: Towards Audio-Visual Understanding Evaluation for Omni MLLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ItRYEe8E61_reviews.json
    forum: https://openreview.net/forum?id=ItRYEe8E61

[303] rating=4.5 | decision=Accept (Poster) | reviews=11
    title: Improving Target Sound Extraction via Disentangled Codec Representations with Privileged Knowledge Distillation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\rew03VaNUJ_reviews.json
    forum: https://openreview.net/forum?id=rew03VaNUJ

[304] rating=4.5 | decision=Accept | reviews=4
    title: Low-Rank Tensor Encoding Models Decompose Natural Speech Comprehension Processes
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\lTr1dv6A26_reviews.json
    forum: https://openreview.net/forum?id=lTr1dv6A26

[305] rating=4.5 | decision=Accept | reviews=4
    title: Resp-Agent: An Agent-Based System for Multimodal Respiratory Sound Generation and Disease Diagnosis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ZkoojtEm3W_reviews.json
    forum: https://openreview.net/forum?id=ZkoojtEm3W

[306] rating=4.5 | decision=None | reviews=4
    title: RETA: Real-Time and Expressive Talking Head Animation without Emotion Label
    pdf: research_data\iclr\talking-head\pdfs\RETA__Real-Time_and_Expressive_Talking_Head_Animation_without_Emotion_Label.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=NsEH4UpalD

[307] rating=4.5 | decision=None | reviews=4
    title: Step-by-Step Video-to-Audio Synthesis via Negative Audio Guidance
    pdf: research_data\iclr\video-diffusion\pdfs\Step-by-Step_Video-to-Audio_Synthesis_via_Negative_Audio_Guidance.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=lvLnFzRyLx

[308] rating=4.5 | decision=Accept | reviews=4
    title: BLAB: Brutally Long Audio Bench
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\By0sbtFROd_reviews.json
    forum: https://openreview.net/forum?id=By0sbtFROd

[309] rating=4.5 | decision=Reject | reviews=4
    title: SARSteer: Safeguarding Large Audio Language Models via Safe-Ablated Refusal Steering
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\pz3WCd3HtG_reviews.json
    forum: https://openreview.net/forum?id=pz3WCd3HtG

[310] rating=4.5 | decision=Reject | reviews=4
    title: SONAR: Spectral‑Contrastive Audio Residuals for Robust Deepfake Detection
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\EzHQZ991im_reviews.json
    forum: https://openreview.net/forum?id=EzHQZ991im

[311] rating=4.5 | decision=None | reviews=4
    title: HiFi-Foley: Multimodal Diffusion with Representation Alignment for High-Fidelity Foley Audio Generation
    pdf: research_data\iclr\video-generation\pdfs\HiFi-Foley__Multimodal_Diffusion_with_Representation_Alignment_for_High-Fidelity.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=72xWFIzG15

[312] rating=4.5 | decision=Accept | reviews=4
    title: XGC-AVis: Towards Audio-Visual Content Understanding with a Multi-Agent Collaborative System
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\jjWPr6maKd_reviews.json
    forum: https://openreview.net/forum?id=jjWPr6maKd

[313] rating=4.5 | decision=None | reviews=4
    title: Syncphony: Synchronized Audio-to-Video Generation with Diffusion Transformers
    pdf: research_data\iclr\text-to-video\pdfs\Syncphony__Synchronized_Audio-to-Video_Generation_with_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=sG8dGZMaub

[314] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Failure by Interference: Language Models Make Balanced Parentheses Errors  When Faulty Mechanisms Overshadow Sound Ones
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\1t4hR9JCcS_reviews.json
    forum: https://openreview.net/forum?id=1t4hR9JCcS

[315] rating=4.4 | decision=Reject | reviews=5
    title: FLEXOUNDIT: VARIABLE-LENGTH DIFFUSION TRANSFORMER FOR TEXT-TO-AUDIO GENERATION
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\6Tyo0yCCez_reviews.json
    forum: https://openreview.net/forum?id=6Tyo0yCCez

[316] rating=4.4 | decision=Accept | reviews=5
    title: Are Deep Speech Denoising Models Robust to Adversarial Noise?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\WtH2JxKJKf_reviews.json
    forum: https://openreview.net/forum?id=WtH2JxKJKf

[317] rating=4.4 | decision=Reject | reviews=5
    title: MoDA: Multi-modal Diffusion Architecture for Talking Head Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bQyPTtOBoM_reviews.json
    forum: https://openreview.net/forum?id=bQyPTtOBoM

[318] rating=4.4 | decision=Reject | reviews=5
    title: MuSiCNet: A Gradual Coarse-to-Fine Framework for Irregularly Sampled Multivariate Time Series Analysis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\BHgMPObtE0_reviews.json
    forum: https://openreview.net/forum?id=BHgMPObtE0

[319] rating=4.4 | decision=Accept | reviews=5
    title: SQuBa: Speech Mamba Language Model with Querying-Attention for Efficient Summarization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\zOMa82W1HV_reviews.json
    forum: https://openreview.net/forum?id=zOMa82W1HV

[320] rating=4.4 | decision=Accept | reviews=5
    title: PACE: Part-Wise Slow-Fast Conditioning for Dance-to-Music Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1Ip4pZoHTH_reviews.json
    forum: https://openreview.net/forum?id=1Ip4pZoHTH

[321] rating=4.4 | decision=Accept | reviews=5
    title: Diffusion-based dynamics as a cognitive model of human speech production
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\u8lN11Gqbx_reviews.json
    forum: https://openreview.net/forum?id=u8lN11Gqbx

[322] rating=4.4 | decision=Accept | reviews=5
    title: TTS-Hub: Leveraging Modular LoRAs and  Arithmetic Composition for Controllable Text-to-Speech
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\43LvSiz6af_reviews.json
    forum: https://openreview.net/forum?id=43LvSiz6af

[323] rating=4.3 | decision=Reject | reviews=3
    title: SoundMorpher: Perceptually-Uniform Sound Morphing with Diffusion Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\h3n7al4mhk_reviews.json
    forum: https://openreview.net/forum?id=h3n7al4mhk

[324] rating=4.3 | decision=Accept | reviews=3
    title: Encoding Speaker-Specific Latent Speech Feature for Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\ngp5jzx5oK_reviews.json
    forum: https://openreview.net/forum?id=ngp5jzx5oK

[325] rating=4.3 | decision=Reject | reviews=6
    title: VoiceAssistant-Eval: Benchmarking AI Assistants across Listening, Speaking, and Viewing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KmMijz0wRa_reviews.json
    forum: https://openreview.net/forum?id=KmMijz0wRa

[326] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: E2E-VGuard: Adversarial Prevention for Production LLM-based End-To-End Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\CHN4HG9R5e_reviews.json
    forum: https://openreview.net/forum?id=CHN4HG9R5e

[327] rating=4.2 | decision=Reject | reviews=4
    title: SELF-TAILORING PROMPTS FOR PARAMETER EFFICIENT TUNING SPEECH RECOGNITION
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\rgjmqqP923_reviews.json
    forum: https://openreview.net/forum?id=rgjmqqP923

[328] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: Resounding Acoustic Fields with Reciprocity
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\37b23mxKH8_reviews.json
    forum: https://openreview.net/forum?id=37b23mxKH8

[329] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: Efficient Speech Language Modeling via Energy Distance in Continuous Latent Space
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\pDWwz9F7Zh_reviews.json
    forum: https://openreview.net/forum?id=pDWwz9F7Zh

[330] rating=4.2 | decision=Reject | reviews=4
    title: SONAR: A Synthetic AI-Audio Detection Framework and Benchmark
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\rGGwXo0Fo0_reviews.json
    forum: https://openreview.net/forum?id=rGGwXo0Fo0

[331] rating=4.2 | decision=Reject | reviews=4
    title: SQS: Speech Quality Assessment in the Data Annotation Context
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\FbRWdSxTPY_reviews.json
    forum: https://openreview.net/forum?id=FbRWdSxTPY

[332] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: Audio-Sync Video Generation with Multi-Stream Temporal Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\12z8KLMQJD_reviews.json
    forum: https://openreview.net/forum?id=12z8KLMQJD

[333] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: TTS-VAR: A Test-Time Scaling Framework for Visual Auto-Regressive Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\qGW1GulvFH_reviews.json
    forum: https://openreview.net/forum?id=qGW1GulvFH

[334] rating=4.2 | decision=Accept | reviews=4
    title: Boosting Fast and High-Quality Speech Synthesis with Linear Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\41CYtxM2jQ_reviews.json
    forum: https://openreview.net/forum?id=41CYtxM2jQ

[335] rating=4.2 | decision=Reject | reviews=4
    title: Not Only Vision: Evolve Visual Speech Recognition via Peripheral Information
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\TykT5YB89r_reviews.json
    forum: https://openreview.net/forum?id=TykT5YB89r

[336] rating=4.2 | decision=Reject | reviews=4
    title: Head Information Bottleneck: An Evaluation Method for Transformer Head Contributions in Speech Task
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\WjYNFZEjc7_reviews.json
    forum: https://openreview.net/forum?id=WjYNFZEjc7

[337] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: Watch and Listen: Understanding Audio-Visual-Speech Moments with Multimodal LLM
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\kWGJa9ZO3M_reviews.json
    forum: https://openreview.net/forum?id=kWGJa9ZO3M

[338] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: OpenOmni: Advancing Open-Source Omnimodal Large Language Models with Progressive Multimodal Alignment and Real-time Emotional Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\4iehXI36QG_reviews.json
    forum: https://openreview.net/forum?id=4iehXI36QG

[339] rating=4.2 | decision=Accept | reviews=4
    title: GETMusic: Generating Music Tracks with a Unified Representation and Diffusion Framework
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\z80CwkWXmq_reviews.json
    forum: https://openreview.net/forum?id=z80CwkWXmq

[340] rating=4.2 | decision=Reject | reviews=4
    title: DLPO: Diffusion Model Loss-Guided Reinforcement Learning for Fine-Tuning Text-to-Speech Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\WzrkZeDxrM_reviews.json
    forum: https://openreview.net/forum?id=WzrkZeDxrM

[341] rating=4.2 | decision=Reject | reviews=4
    title: AV-PEA: PARAMETER-EFFICIENT ADAPTER FOR AUDIO-VISUAL MULTIMODAL LEARNING
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\gWw0NjTQRg_reviews.json
    forum: https://openreview.net/forum?id=gWw0NjTQRg

[342] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: Model-Guided Dual-Role Alignment for High-Fidelity Open-Domain Video-to-Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\02qdHz1LU0_reviews.json
    forum: https://openreview.net/forum?id=02qdHz1LU0

[343] rating=4.2 | decision=Reject | reviews=4
    title: Rethinking MUSHRA: Addressing Modern Challenges in Text-to-Speech Evaluation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\n6YVISFrcN_reviews.json
    forum: https://openreview.net/forum?id=n6YVISFrcN

[344] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: MoME: Mixture of Matryoshka Experts for Audio-Visual Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\n6SrVj7I0g_reviews.json
    forum: https://openreview.net/forum?id=n6SrVj7I0g

[345] rating=4.2 | decision=Reject | reviews=4
    title: AnyExpress: One Adapter Enabling Highly Flexible Audio-Driven Portrait Animation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\sOmojPmnlL_reviews.json
    forum: https://openreview.net/forum?id=sOmojPmnlL

[346] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: ThinkSound: Chain-of-Thought Reasoning in Multimodal LLMs for Audio Generation and Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\mj8VN4MyrO_reviews.json
    forum: https://openreview.net/forum?id=mj8VN4MyrO

[347] rating=4.2 | decision=Accept | reviews=4
    title: Two Halves Make a Whole: How to Reconcile Soundness and Robustness in Watermarking for Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\hULJCP47PU_reviews.json
    forum: https://openreview.net/forum?id=hULJCP47PU

[348] rating=4.2 | decision=Reject | reviews=4
    title: Audio-Agent: Leveraging LLMs For Audio Generation, Editing and Composition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\J8yH8ontdq_reviews.json
    forum: https://openreview.net/forum?id=J8yH8ontdq

[349] rating=4.2 | decision=Accept (Poster) | reviews=15
    title: E-BATS: Efficient Backpropagation-Free Test-Time Adaptation for Speech Foundation Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\WwzurufeFN_reviews.json
    forum: https://openreview.net/forum?id=WwzurufeFN

[350] rating=4.2 | decision=Reject | reviews=5
    title: Controllable Text-to-Speech Synthesis with Masked-Autoencoded Style Representation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\qH5uyYCG2j_reviews.json
    forum: https://openreview.net/forum?id=qH5uyYCG2j

[351] rating=4.2 | decision=Accept (Poster) | reviews=15
    title: Let Them Talk: Audio-Driven Multi-Person Conversational Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\1aCYFQRvtz_reviews.json
    forum: https://openreview.net/forum?id=1aCYFQRvtz

[352] rating=4.2 | decision=Reject | reviews=6
    title: WaveFluid: A New Adversarial Approach for Efficient High-Fidelity Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\ttRSBZiCiu_reviews.json
    forum: https://openreview.net/forum?id=ttRSBZiCiu

[353] rating=4.0 | decision=Reject | reviews=4
    title: AudioStory: Generating Long-Form Narrative Audio with Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\JKoytS8x0O_reviews.json
    forum: https://openreview.net/forum?id=JKoytS8x0O

[354] rating=4.0 | decision=Accept | reviews=4
    title: Audio Prototypical Network for Controllable Music Recommendation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\pKDmt7pc6h_reviews.json
    forum: https://openreview.net/forum?id=pKDmt7pc6h

[355] rating=4.0 | decision=Accept (Poster) | reviews=12
    title: Aligning What Matters: Masked Latent Adaptation for Text-to-Audio-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\I0hRN2HMeH_reviews.json
    forum: https://openreview.net/forum?id=I0hRN2HMeH

[356] rating=4.0 | decision=Reject | reviews=4
    title: AV-Odyssey Bench: From Fundamental Audio Perception to Audio-Visual Understanding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\xx3DCKbt1T_reviews.json
    forum: https://openreview.net/forum?id=xx3DCKbt1T

[357] rating=4.0 | decision=Accept | reviews=4
    title: Efficient Audiovisual Speech Processing via MUTUD: Multimodal Training and Unimodal Deployment
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\TCFtGBTxkq_reviews.json
    forum: https://openreview.net/forum?id=TCFtGBTxkq

[358] rating=4.0 | decision=Reject | reviews=3
    title: From Silence to Sound: Towards Audio-Visual Subject Customization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\WjqO2pNfh2_reviews.json
    forum: https://openreview.net/forum?id=WjqO2pNfh2

[359] rating=4.0 | decision=None | reviews=4
    title: Beyond Audio-Visual Alignment: Unmasking Talking Head Deepfakes via Red Hue Discrepancies in HSV Color Space
    pdf: research_data\iclr\talking-head\pdfs\Beyond_Audio-Visual_Alignment__Unmasking_Talking_Head_Deepfakes_via_Red_Hue_Disc.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=8qQrEcsdls

[360] rating=4.0 | decision=Reject | reviews=4
    title: Towards Multimodal Understanding, Reasoning, and Tool Usage across Vision, Speech, and Audio in Long Videos
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\4w9HzBBLRk_reviews.json
    forum: https://openreview.net/forum?id=4w9HzBBLRk

[361] rating=4.0 | decision=Accept | reviews=4
    title: SupertonicTTS: Towards Highly Efficient and Streamlined Text-to-Speech System
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\urGk2mIJc3_reviews.json
    forum: https://openreview.net/forum?id=urGk2mIJc3

[362] rating=4.0 | decision=Reject | reviews=4
    title: Mini-Omni-Reasoner: Token-Level Thinking-in-Speaking in Large Speech Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ZRokRhD72w_reviews.json
    forum: https://openreview.net/forum?id=ZRokRhD72w

[363] rating=4.0 | decision=None | reviews=3
    title: Ovi: Twin Backbone Cross-Modal Fusion for Audio-Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Ovi__Twin_Backbone_Cross-Modal_Fusion_for_Audio-Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nIrF8xF0uN

[364] rating=4.0 | decision=Accept | reviews=4
    title: PI-Controlled Uncertainty for Steady-State Error Elimination in  Ultrasound Image Segmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\EyUa0s2RWg_reviews.json
    forum: https://openreview.net/forum?id=EyUa0s2RWg

[365] rating=4.0 | decision=Accept | reviews=3
    title: Cocktail-Party at the MUSEUM: Referring Audio-Visual Segmentation requires Augmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\LQSlLfKAoZ_reviews.json
    forum: https://openreview.net/forum?id=LQSlLfKAoZ

[366] rating=4.0 | decision=Accept | reviews=4
    title: Resolving Domain Shift For Representations Of Speech In Non-Invasive Brain Recordings
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\HJp1g4w1Or_reviews.json
    forum: https://openreview.net/forum?id=HJp1g4w1Or

[367] rating=4.0 | decision=Accept | reviews=4
    title: DiceFormer: Spiking Audio Transformer with Density-Aware Dice Attention
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\GSLcetBFva_reviews.json
    forum: https://openreview.net/forum?id=GSLcetBFva

[368] rating=4.0 | decision=Accept | reviews=4
    title: CRAFT: Cross-Representation modeling on Audio waveForms and specTrograms
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\Mzb7XD0O1Q_reviews.json
    forum: https://openreview.net/forum?id=Mzb7XD0O1Q

[369] rating=4.0 | decision=Reject | reviews=4
    title: Towards Universal Mono-to-Binaural Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\S8VFVe6MWL_reviews.json
    forum: https://openreview.net/forum?id=S8VFVe6MWL

[370] rating=4.0 | decision=None | reviews=4
    title: A Bridge from Audio to Video: Phoneme-Viseme Alignment Allows Every Face to Speak Multiple Languages
    pdf: research_data\iclr\talking-head\pdfs\A_Bridge_from_Audio_to_Video__Phoneme-Viseme_Alignment_Allows_Every_Face_to_Spea.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=yZaTmUOW1o

[371] rating=4.0 | decision=Accept | reviews=4
    title: video-SALMONN S: Streaming Audio-Visual LLMs Beyond Length Limits via Memory
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\cO1PLFtIxe_reviews.json
    forum: https://openreview.net/forum?id=cO1PLFtIxe

[372] rating=4.0 | decision=Accept | reviews=3
    title: Learnable Fractional Superlets with a Spectro-Temporal Emotion Encoder for Speech Emotion Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\uZGEEL20mU_reviews.json
    forum: https://openreview.net/forum?id=uZGEEL20mU

[373] rating=4.0 | decision=Accept (Poster) | reviews=15
    title: Time-Masked Transformers with Lightweight Test-Time Adaptation for Neural Speech Decoding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\0U7D9AFiZ0_reviews.json
    forum: https://openreview.net/forum?id=0U7D9AFiZ0

[374] rating=4.0 | decision=Accept | reviews=4
    title: Sound Probabilistic Safety Bounds for Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\papImkPLf5_reviews.json
    forum: https://openreview.net/forum?id=papImkPLf5

[375] rating=4.0 | decision=Reject | reviews=4
    title: VoxGenesis: Unsupervised Discovery of Latent Speaker Manifold for Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\gSB6IfUEGz_reviews.json
    forum: https://openreview.net/forum?id=gSB6IfUEGz

[376] rating=4.0 | decision=Accept | reviews=11
    title: Hear you are: Teaching LLMs Spatial Reasoning with Vision and Spatial Sound
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\b6s1jIHj6o_reviews.json
    forum: https://openreview.net/forum?id=b6s1jIHj6o

[377] rating=4.0 | decision=Accept (Poster) | reviews=12
    title: AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\BuYtcTUMyA_reviews.json
    forum: https://openreview.net/forum?id=BuYtcTUMyA

[378] rating=4.0 | decision=Accept | reviews=3
    title: Heeding the Inner Voice: Aligning ControlNet Training via Intermediate Features Feedback
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\e0x4huHvTe_reviews.json
    forum: https://openreview.net/forum?id=e0x4huHvTe

[379] rating=4.0 | decision=Accept | reviews=3
    title: Turning Speech Language Models into Multilingual Listeners
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\cL3M1VwZyn_reviews.json
    forum: https://openreview.net/forum?id=cL3M1VwZyn

[380] rating=4.0 | decision=Accept | reviews=4
    title: DiffSound: Differentiable Modal Sound Simulation for Inverse Reasoning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\6jFjYmahxu_reviews.json
    forum: https://openreview.net/forum?id=6jFjYmahxu

[381] rating=4.0 | decision=Accept | reviews=4
    title: VoiceBridge: Designing Latent Bridge Models for General Speech Restoration at Scale
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\XudGcVeUKO_reviews.json
    forum: https://openreview.net/forum?id=XudGcVeUKO

[382] rating=4.0 | decision=Reject | reviews=4
    title: SAFE: Spiking Neural Network-based Audio Fidelity Evaluation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\QWDZE2mYIe_reviews.json
    forum: https://openreview.net/forum?id=QWDZE2mYIe

[383] rating=4.0 | decision=Reject | reviews=4
    title: S$^6$-DAMON: Unlocking Structured Sparsity in Self-Supervised Speech Models via Data-Model Co-Compression
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\5qxdlSyyB3_reviews.json
    forum: https://openreview.net/forum?id=5qxdlSyyB3

[384] rating=4.0 | decision=Accept | reviews=4
    title: Aurelius: Relation Aware Text-to-Audio Generation At Scale
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\LAYCYiIgZ1_reviews.json
    forum: https://openreview.net/forum?id=LAYCYiIgZ1

[385] rating=4.0 | decision=Reject | reviews=4
    title: AVCAPS: AN AUDIO-VISUAL DATASET WITH MODALITY-SPECIFIC CAPTIONS
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\FFUmPQM8c5_reviews.json
    forum: https://openreview.net/forum?id=FFUmPQM8c5

[386] rating=4.0 | decision=Reject | reviews=3
    title: StreamUni: Achieving Streaming Speech Translation with a Unified Large Speech-Language Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\7t0vUDDDI6_reviews.json
    forum: https://openreview.net/forum?id=7t0vUDDDI6

[387] rating=4.0 | decision=Accept (Poster) | reviews=9
    title: Enabling Differentially Private Federated Learning for Speech Recognition: Benchmarks, Adaptive Optimizers, and Gradient Clipping
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\4HZaFk9O4r_reviews.json
    forum: https://openreview.net/forum?id=4HZaFk9O4r

[388] rating=4.0 | decision=Accept | reviews=3
    title: GRAM: Spatial general-purpose audio representations for real-world applications
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QIgRLpdneh_reviews.json
    forum: https://openreview.net/forum?id=QIgRLpdneh

[389] rating=4.0 | decision=Accept | reviews=5
    title: ACAV-1M: Data Curation and Benchmarking for Audio-Visual Representation Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\HUjFpOgVCK_reviews.json
    forum: https://openreview.net/forum?id=HUjFpOgVCK

[390] rating=4.0 | decision=Accept | reviews=4
    title: Don’t Forget the Context: A Multitask Transformer for Intracortical Speech Decoding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bn1uLCkXOu_reviews.json
    forum: https://openreview.net/forum?id=bn1uLCkXOu

[391] rating=4.0 | decision=Accept | reviews=4
    title: Integrating Distributed Acoustic Sensing and PINN Frameworks for Enhanced Indoor Sound Source Localization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\S2WUJUETyc_reviews.json
    forum: https://openreview.net/forum?id=S2WUJUETyc

[392] rating=4.0 | decision=Reject | reviews=4
    title: MEDIC: Zero-shot Music Editing with Disentangled Inversion Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\3f8556SIEn_reviews.json
    forum: https://openreview.net/forum?id=3f8556SIEn

[393] rating=4.0 | decision=Accept | reviews=3
    title: Brain encoding models based on binding multiple modalities across audio, language, and vision
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\3NMYMLL92j_reviews.json
    forum: https://openreview.net/forum?id=3NMYMLL92j

[394] rating=4.0 | decision=Accept | reviews=4
    title: Variable-Length Audio Fingerprinting
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0wwcANeTjd_reviews.json
    forum: https://openreview.net/forum?id=0wwcANeTjd

[395] rating=4.0 | decision=Reject | reviews=4
    title: AudioMarathon: A Comprehensive Benchmark for Long-Context Audio Understanding and Efficiency in Audio LLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\i55jA7FSvZ_reviews.json
    forum: https://openreview.net/forum?id=i55jA7FSvZ

[396] rating=4.0 | decision=Accept | reviews=4
    title: SAKE: Towards Editing Auditory Attribute Knowledge of Large Audio-Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\pmqI5sV5PX_reviews.json
    forum: https://openreview.net/forum?id=pmqI5sV5PX

[397] rating=4.0 | decision=Accept | reviews=5
    title: Fork-Merge Decoding: Enhancing Multimodal Understanding in Audio-Visual Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\jXgDfBpwHH_reviews.json
    forum: https://openreview.net/forum?id=jXgDfBpwHH

[398] rating=4.0 | decision=None | reviews=4
    title: SALSA-V: Shortcut-Augmented Long-form Synchronized Audio from Videos
    pdf: research_data\iclr\video-diffusion\pdfs\SALSA-V__Shortcut-Augmented_Long-form_Synchronized_Audio_from_Videos.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=3FcjKYmNY5

[399] rating=4.0 | decision=Accept | reviews=4
    title: CM^2: Cross-Modal Contextual Modeling for Audio-Visual Speech Enhancement
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\EO2hZTtK3M_reviews.json
    forum: https://openreview.net/forum?id=EO2hZTtK3M

[400] rating=4.0 | decision=Reject | reviews=5
    title: Think Smart, Not Hard: Difficulty Adaptive Reasoning for Large Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\aFZ0zQHfyO_reviews.json
    forum: https://openreview.net/forum?id=aFZ0zQHfyO

[401] rating=4.0 | decision=Accept | reviews=4
    title: video-SALMONN 2: Caption-Enhanced Audio-Visual Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\O2tca5tExP_reviews.json
    forum: https://openreview.net/forum?id=O2tca5tExP

[402] rating=4.0 | decision=Accept (Poster) | reviews=12
    title: Mellow: a small audio language model for reasoning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\um4aiicz3L_reviews.json
    forum: https://openreview.net/forum?id=um4aiicz3L

[403] rating=4.0 | decision=Reject | reviews=4
    title: ReasonAudio: Semantic Reasoning and Temporal Synchrony in Video–Text-to-Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\7QlJcWwd14_reviews.json
    forum: https://openreview.net/forum?id=7QlJcWwd14

[404] rating=4.0 | decision=Reject | reviews=4
    title: Investigating Self-Supervised Representations for Audio-Visual Deepfake Detection
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\IKihT0qTdt_reviews.json
    forum: https://openreview.net/forum?id=IKihT0qTdt

[405] rating=4.0 | decision=Accept | reviews=4
    title: VGPO: Fine-Tuning Speech Autoregressive Diffusion Models with Value Guided Policy Optimization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\LLWIaUZvEu_reviews.json
    forum: https://openreview.net/forum?id=LLWIaUZvEu

[406] rating=4.0 | decision=Reject | reviews=3
    title: Advancing Energy Efficiency in On-Device Streaming Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\A6QotWIQim_reviews.json
    forum: https://openreview.net/forum?id=A6QotWIQim

[407] rating=3.8 | decision=Reject | reviews=5
    title: GigaSpeech 2: An Evolving, Large-Scale and Multi-domain ASR Corpus for Low-Resource Languages with Automated Crawling, Transcription and Refinement
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\SbK9GtQlVg_reviews.json
    forum: https://openreview.net/forum?id=SbK9GtQlVg

[408] rating=3.8 | decision=Reject | reviews=4
    title: InfiniteAudio: Infinite-Length Audio Generation with Consistent Acoustic Attributes
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Hp6f6VKAeP_reviews.json
    forum: https://openreview.net/forum?id=Hp6f6VKAeP

[409] rating=3.8 | decision=Accept (Poster) | reviews=12
    title: AudSemThinker: Enhancing Audio-Language Models Through Reasoning over Semantics of Sound
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\pozsP0ZcZN_reviews.json
    forum: https://openreview.net/forum?id=pozsP0ZcZN

[410] rating=3.8 | decision=Accept | reviews=4
    title: Highly efficient Speech Separation using relative Context
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\UPOUVsEafz_reviews.json
    forum: https://openreview.net/forum?id=UPOUVsEafz

[411] rating=3.8 | decision=Accept | reviews=4
    title: Disentangling Textual and Acoustic Features of Neural Speech Representations
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\xJc3PazBwS_reviews.json
    forum: https://openreview.net/forum?id=xJc3PazBwS

[412] rating=3.8 | decision=Accept | reviews=4
    title: EquiAV: Single-modal Equivariance Promotes Audio-Visual Contrastive Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\9k4Yvb75ED_reviews.json
    forum: https://openreview.net/forum?id=9k4Yvb75ED

[413] rating=3.7 | decision=Reject | reviews=3
    title: Advancing African-Accented English Speech Recognition: Epistemic Uncertainty-Driven Data Selection for Generalizable ASR Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\MazxSMs6Hs_reviews.json
    forum: https://openreview.net/forum?id=MazxSMs6Hs

[414] rating=3.7 | decision=Accept | reviews=3
    title: FlowHash: Accelerating Audio Search with Balanced Hashing via Normalizing Flow
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\3wGi5m2YHY_reviews.json
    forum: https://openreview.net/forum?id=3wGi5m2YHY

[415] rating=3.7 | decision=Accept | reviews=6
    title: Kanade: Compact Linguistically Rich Speech Tokens for Spoken Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\dNUcKJEPTh_reviews.json
    forum: https://openreview.net/forum?id=dNUcKJEPTh

[416] rating=3.7 | decision=Reject | reviews=3
    title: Video-to-Audio generation with Hidden Alignment
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\YQjdNC0NkW_reviews.json
    forum: https://openreview.net/forum?id=YQjdNC0NkW

[417] rating=3.7 | decision=Accept | reviews=3
    title: Attacking Audio Language Models with Best-of-N Jailbreaking
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\yougZBoUY3_reviews.json
    forum: https://openreview.net/forum?id=yougZBoUY3

[418] rating=3.6 | decision=Reject | reviews=5
    title: Automating Thought of Search: A Journey Towards Soundness and Completeness
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DE9Vapk5DW_reviews.json
    forum: https://openreview.net/forum?id=DE9Vapk5DW

[419] rating=3.6 | decision=Accept | reviews=5
    title: Audio-FLAN: An Instruction-Following Dataset for Unified Understanding and Generation of Speech, Music, and Sound
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\43YIq34nYw_reviews.json
    forum: https://openreview.net/forum?id=43YIq34nYw

[420] rating=3.5 | decision=Accept | reviews=4
    title: T-VecTTS: Adding time-varying-emotion control to flow-matching-based TTS
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\x77sW1KUNE_reviews.json
    forum: https://openreview.net/forum?id=x77sW1KUNE

[421] rating=3.5 | decision=Reject | reviews=4
    title: Towards Multimodal Understanding of Music Scores and Performance Audio
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\kDqH5KmRWR_reviews.json
    forum: https://openreview.net/forum?id=kDqH5KmRWR

[422] rating=3.5 | decision=Reject | reviews=4
    title: FARV: Leveraging Facial and Acoustic Representation in Vocoder For Video-to-Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\5fRlsiNDZR_reviews.json
    forum: https://openreview.net/forum?id=5fRlsiNDZR

[423] rating=3.5 | decision=Reject | reviews=4
    title: SpeechMedAssist: Efficiently and Effectively Adapting Speech Language Model for Medical Consultation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\d4zZEeUC1J_reviews.json
    forum: https://openreview.net/forum?id=d4zZEeUC1J

[424] rating=3.5 | decision=Accept | reviews=4
    title: Bioacoustic Geolocation: Species Sounds as Geographic Signals
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\7CyXgo9tys_reviews.json
    forum: https://openreview.net/forum?id=7CyXgo9tys

[425] rating=3.5 | decision=Reject | reviews=4
    title: Audio Image Generation for Denoising
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\PuTJF5Tzfa_reviews.json
    forum: https://openreview.net/forum?id=PuTJF5Tzfa

[426] rating=3.5 | decision=Reject | reviews=4
    title: BrainStratify: Coarse-to-Fine Disentanglement of Intracranial Recordings for Speech Decoding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\SG5ivsCB76_reviews.json
    forum: https://openreview.net/forum?id=SG5ivsCB76

[427] rating=3.5 | decision=Accept | reviews=4
    title: HybridSB-MoE: Dual-Domain Schrödinger Bridges with Scene-Adaptive Expert Routing for Speech Enhancement
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\SbahKA6FTf_reviews.json
    forum: https://openreview.net/forum?id=SbahKA6FTf

[428] rating=3.5 | decision=Accept | reviews=4
    title: TalkPlayData 2: An Agentic Synthetic Data Pipeline for Multimodal  Conversational Music Recommendation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Phv5G3rxOx_reviews.json
    forum: https://openreview.net/forum?id=Phv5G3rxOx

[429] rating=3.5 | decision=Reject | reviews=4
    title: It Hears, It Sees too: Multi-Modal LLM for Depression Detection By Integrating Visual Understanding into Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KA9StC9l3T_reviews.json
    forum: https://openreview.net/forum?id=KA9StC9l3T

[430] rating=3.5 | decision=Reject | reviews=4
    title: TETA: Temporal-Enhanced Text-to-Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\t7izmSufIi_reviews.json
    forum: https://openreview.net/forum?id=t7izmSufIi

[431] rating=3.5 | decision=Accept | reviews=4
    title: Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ISSxXXiu3w_reviews.json
    forum: https://openreview.net/forum?id=ISSxXXiu3w

[432] rating=3.5 | decision=Reject | reviews=4
    title: Thinking with Sound: Audio Chain-of-Thought Enables Multimodal Reasoning for Large Audio-Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\nn1CV8VXcI_reviews.json
    forum: https://openreview.net/forum?id=nn1CV8VXcI

[433] rating=3.5 | decision=Reject | reviews=4
    title: CAN DEEPFAKE SPEECH BE RELIABLY DETECTED?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\St7k6NJKn1_reviews.json
    forum: https://openreview.net/forum?id=St7k6NJKn1

[434] rating=3.5 | decision=Reject | reviews=4
    title: InterAvatar: Real-time Interactive Portrait Animation via Behavioral Interaction Prompts
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\9p2l8ue94K_reviews.json
    forum: https://openreview.net/forum?id=9p2l8ue94K

[435] rating=3.5 | decision=Accept | reviews=4
    title: UNISE: Unified Noise-Invariant Learning for Speech Enhancement toward Improved Content Preservation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qyd974TxRh_reviews.json
    forum: https://openreview.net/forum?id=qyd974TxRh

[436] rating=3.5 | decision=Accept | reviews=4
    title: Soundness-Aware Level: A Microscopic Signature that Predicts LLM Reasoning Potential
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\8NdXdmWqgD_reviews.json
    forum: https://openreview.net/forum?id=8NdXdmWqgD

[437] rating=3.5 | decision=Reject | reviews=4
    title: FAVEN: Fast Audio-Visual Embodied Navigation in 3D Environments
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\48nAxwEyQ0_reviews.json
    forum: https://openreview.net/forum?id=48nAxwEyQ0

[438] rating=3.5 | decision=Reject | reviews=4
    title: OpenMU: Your Swiss Army Knife for Music Understanding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\burz7mU0YD_reviews.json
    forum: https://openreview.net/forum?id=burz7mU0YD

[439] rating=3.5 | decision=Reject | reviews=4
    title: Semi-Supervised Speech Enhancement with Gradient-Guided Channel Attenuation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\xGmWHCpVoM_reviews.json
    forum: https://openreview.net/forum?id=xGmWHCpVoM

[440] rating=3.5 | decision=Accept | reviews=4
    title: TF-Restormer: Complex Spectral Prediction for Speech Restoration
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bPM2KgvK53_reviews.json
    forum: https://openreview.net/forum?id=bPM2KgvK53

[441] rating=3.5 | decision=Reject | reviews=4
    title: A Dual-branch Multi-Band Neural Vocoder with Harmonic Discriminator for High-Fidelity Speech Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\YTxx02MnTS_reviews.json
    forum: https://openreview.net/forum?id=YTxx02MnTS

[442] rating=3.5 | decision=Accept | reviews=4
    title: Decoding Inner Speech with an End-to-End Brain-to-Text Neural Interface
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Lp1noMpMUG_reviews.json
    forum: https://openreview.net/forum?id=Lp1noMpMUG

[443] rating=3.5 | decision=Reject | reviews=4
    title: Speaking Guided by Listening: Unsupervised Text-to-Speech Generative Model Guided by End-to-End Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Hd4jB1ErMk_reviews.json
    forum: https://openreview.net/forum?id=Hd4jB1ErMk

[444] rating=3.5 | decision=Reject | reviews=4
    title: Roadmap towards Superhuman Speech Understanding using Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Pnr8XNWcY0_reviews.json
    forum: https://openreview.net/forum?id=Pnr8XNWcY0

[445] rating=3.5 | decision=Reject | reviews=4
    title: SALMONN-omni: A Speech Understanding and Generation LLM in a Codec-free Full-duplex Framework
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\eJpI20hzWf_reviews.json
    forum: https://openreview.net/forum?id=eJpI20hzWf

[446] rating=3.5 | decision=Accept | reviews=4
    title: VoiceNoNG: High-Quality Speech Editing Model without Hallucinations
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\BVsFp5rQxd_reviews.json
    forum: https://openreview.net/forum?id=BVsFp5rQxd

[447] rating=3.5 | decision=Reject | reviews=4
    title: UltraVoice: Scaling Fine-Grained Style-Controlled Speech Conversations for Spoken Dialogue Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\UrWdRcLINM_reviews.json
    forum: https://openreview.net/forum?id=UrWdRcLINM

[448] rating=3.5 | decision=Reject | reviews=4
    title: Takin-VC: Zero-shot Voice Conversion via Jointly Hybrid Content and Memory-Augmented Context-Aware Timbre Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\F0TrRRKkQT_reviews.json
    forum: https://openreview.net/forum?id=F0TrRRKkQT

[449] rating=3.5 | decision=Reject | reviews=4
    title: MVoice: Multilingual Unified Voice Generation With Discrete Representation at Scale
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\eGdhD93hZr_reviews.json
    forum: https://openreview.net/forum?id=eGdhD93hZr

[450] rating=3.5 | decision=Reject | reviews=4
    title: TwinVoice: A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona Simulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\f4o9OdqAfy_reviews.json
    forum: https://openreview.net/forum?id=f4o9OdqAfy

[451] rating=3.5 | decision=Reject | reviews=4
    title: SpeechWakBench: How Well do Large Language Models Speak with Watermarks?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\nK5UCo43d1_reviews.json
    forum: https://openreview.net/forum?id=nK5UCo43d1

[452] rating=3.5 | decision=Accept | reviews=4
    title: MORE: Multi-Objective Adversarial Attacks on Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QGuGHSHh9W_reviews.json
    forum: https://openreview.net/forum?id=QGuGHSHh9W

[453] rating=3.5 | decision=Accept | reviews=4
    title: A Bio-Inspired Sound Localization Spiking Neural Network with Unsupervised Local Plasticity and Proximity Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\sJHf6crz89_reviews.json
    forum: https://openreview.net/forum?id=sJHf6crz89

[454] rating=3.5 | decision=Reject | reviews=4
    title: Chord-Transformer:Chord-Progression Guided Transformer for Long-Sequence Symbolic Music Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\A7jXhEXORd_reviews.json
    forum: https://openreview.net/forum?id=A7jXhEXORd

[455] rating=3.5 | decision=Reject | reviews=4
    title: Sound in Sights: Deriving Visual Insights from Audio for Comprehensive Video Understanding with Large Multimodal Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\35cHQuDeo4_reviews.json
    forum: https://openreview.net/forum?id=35cHQuDeo4

[456] rating=3.5 | decision=Reject | reviews=4
    title: Backdoor Attacks Against Speech Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\HcytH0HSaG_reviews.json
    forum: https://openreview.net/forum?id=HcytH0HSaG

[457] rating=3.5 | decision=Reject | reviews=4
    title: Cross-Attention is Half Explanation in Speech-to-Text Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\EsltWxcYlN_reviews.json
    forum: https://openreview.net/forum?id=EsltWxcYlN

[458] rating=3.5 | decision=Reject | reviews=4
    title: MDAR: A Multi-scene Dynamic Audio Reasoning Benchmark
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\meRHki4HwQ_reviews.json
    forum: https://openreview.net/forum?id=meRHki4HwQ

[459] rating=3.5 | decision=Reject | reviews=4
    title: MGM-Omni: Scaling Omni LLMs to Personalized Long-Horizon Speech
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Cry2mpEocV_reviews.json
    forum: https://openreview.net/forum?id=Cry2mpEocV

[460] rating=3.3 | decision=Reject | reviews=3
    title: FastALM: Hierarchical Frame Q-Former for Effective Audio Modality Adaptation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1Hxtv5kT5Y_reviews.json
    forum: https://openreview.net/forum?id=1Hxtv5kT5Y

[461] rating=3.3 | decision=Reject | reviews=3
    title: From Scores to Preferences: Redefining MOS Benchmarking for Speech Quality Reward Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\pz1tpHPiM3_reviews.json
    forum: https://openreview.net/forum?id=pz1tpHPiM3

[462] rating=3.3 | decision=Reject | reviews=3
    title: BatonVoice: An Operationalist Framework for Enhancing Controllable Speech Synthesis with Linguistic Intelligence from LLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\YsVQBe0HNA_reviews.json
    forum: https://openreview.net/forum?id=YsVQBe0HNA

[463] rating=3.3 | decision=Accept | reviews=3
    title: Harmonic-Percussive Disentangled Neural Audio Codec for Bandwidth Extension
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\TgRMixfAPK_reviews.json
    forum: https://openreview.net/forum?id=TgRMixfAPK

[464] rating=3.3 | decision=Accept | reviews=3
    title: DiSTAR: Diffusion over a Scalable Token Autoregressive Representation for Speech Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\2EQPpEZtEK_reviews.json
    forum: https://openreview.net/forum?id=2EQPpEZtEK

[465] rating=3.3 | decision=Reject | reviews=3
    title: Training-Free Spectral Fingerprints of Voice Processing in Transformers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\9f1MuExEbF_reviews.json
    forum: https://openreview.net/forum?id=9f1MuExEbF

[466] rating=3.3 | decision=Accept | reviews=3
    title: FoeGlass: When Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\gwi2T2CsfK_reviews.json
    forum: https://openreview.net/forum?id=gwi2T2CsfK

[467] rating=3.3 | decision=Reject | reviews=3
    title: AlignMark: Content-Aligned Audio Watermarking for Robustness Against Neural Transformations
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1pN7mqygAr_reviews.json
    forum: https://openreview.net/forum?id=1pN7mqygAr

[468] rating=3.3 | decision=Reject | reviews=3
    title: AHELM: A Holistic Evaluation of Audio-Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DwerBtrre2_reviews.json
    forum: https://openreview.net/forum?id=DwerBtrre2

[469] rating=3.2 | decision=Reject | reviews=5
    title: PolyAudio: Advancing Multi-Audio Analysis & Reasoning in Large Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Tq0oPUyVTz_reviews.json
    forum: https://openreview.net/forum?id=Tq0oPUyVTz

[470] rating=3.2 | decision=Accept | reviews=5
    title: Alignment Does Matter: Enables Pure-Speech-Token Dialogue with Frozen Text LLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\PUZCbh6IfK_reviews.json
    forum: https://openreview.net/forum?id=PUZCbh6IfK

[471] rating=3.2 | decision=Reject | reviews=5
    title: UniTTS: Towards End-to-End Speech Synthesis with Joint Acoustic-Semantic Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\YsrswIqSZ9_reviews.json
    forum: https://openreview.net/forum?id=YsrswIqSZ9

[472] rating=3.0 | decision=Accept | reviews=4
    title: FRELA: Frequency-Layered Audio Watermarking for Robust Content Authentication
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\6zYv52WeQD_reviews.json
    forum: https://openreview.net/forum?id=6zYv52WeQD

[473] rating=3.0 | decision=Reject | reviews=4
    title: VocSim: A Training-free Benchmark for Zero-shot Content Identity in Single-source Audio
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\74jqVzrUQ5_reviews.json
    forum: https://openreview.net/forum?id=74jqVzrUQ5

[474] rating=3.0 | decision=Reject | reviews=4
    title: Balanced Multimodal Learning: An Integrated Framework for Multi-Task Learning in Audio-Visual Fusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\V7WjTjX7AY_reviews.json
    forum: https://openreview.net/forum?id=V7WjTjX7AY

[475] rating=3.0 | decision=Reject | reviews=4
    title: PAV-DiT: A Cross-modal Alignment Projected Latent Diffusion Transformer for Synchronized Audio-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\RFrc0g7pSu_reviews.json
    forum: https://openreview.net/forum?id=RFrc0g7pSu

[476] rating=3.0 | decision=Reject | reviews=3
    title: Turn-by-Turn Driving Navigation: Leveraging Sequence Model for Real-time Audio Instructions
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\2JXe3RprGS_reviews.json
    forum: https://openreview.net/forum?id=2JXe3RprGS

[477] rating=3.0 | decision=Reject | reviews=4
    title: THEval. Evaluation Framework for Talking Head Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\G1147yjk9T_reviews.json
    forum: https://openreview.net/forum?id=G1147yjk9T

[478] rating=3.0 | decision=Accept | reviews=6
    title: AlignChat: Endowing LLMs with End-to-End Speech-to-Text Chat Capability through Token-Level Representation Alignment
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\VgYweldMYb_reviews.json
    forum: https://openreview.net/forum?id=VgYweldMYb

[479] rating=3.0 | decision=Accept | reviews=4
    title: Perceived speech decoding and neurophysiological knowledge mining with explainable AI and non-invasive  brain activity recordings
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\hfRb6yC0W0_reviews.json
    forum: https://openreview.net/forum?id=hfRb6yC0W0

[480] rating=3.0 | decision=Reject | reviews=4
    title: Fox-TTS: Scalable Flow Transformers for Expressive Zero-Shot Text to Speech
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\pWdkM9NNCA_reviews.json
    forum: https://openreview.net/forum?id=pWdkM9NNCA

[481] rating=3.0 | decision=Reject | reviews=4
    title: Representational Alignment between Deep Neural Networks and Human Brain in Speech Processing under Audiovisual Noise
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DJ6AR99XFA_reviews.json
    forum: https://openreview.net/forum?id=DJ6AR99XFA

[482] rating=3.0 | decision=Accept | reviews=4
    title: Adaptable Symbolic Music Infilling with MIDI-RWKV
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\lFn1Bb1ZMD_reviews.json
    forum: https://openreview.net/forum?id=lFn1Bb1ZMD

[483] rating=3.0 | decision=Reject | reviews=4
    title: Detecting and Mitigating Insertion Hallucination in Video-to-Audio Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\BLaJXoEAEW_reviews.json
    forum: https://openreview.net/forum?id=BLaJXoEAEW

[484] rating=3.0 | decision=Reject | reviews=3
    title: Federated Learning with Differential Privacy for End-to-End Speech Recognition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\zI6fKENVL8_reviews.json
    forum: https://openreview.net/forum?id=zI6fKENVL8

[485] rating=3.0 | decision=Reject | reviews=4
    title: CapTalk: Text-Guided Stylization and Speech-Driven 3D Head Animation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\MBt9cEAdLb_reviews.json
    forum: https://openreview.net/forum?id=MBt9cEAdLb

[486] rating=3.0 | decision=Reject | reviews=4
    title: Partner-Bench: Evaluating Visually-Grounded IQ and Interactive EQ in Audio-Visual Dialogue
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DEA4s0Bokq_reviews.json
    forum: https://openreview.net/forum?id=DEA4s0Bokq

[487] rating=3.0 | decision=Reject | reviews=4
    title: Hyperbolic Music Representations
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\rIyS3dYAiH_reviews.json
    forum: https://openreview.net/forum?id=rIyS3dYAiH

[488] rating=3.0 | decision=Reject | reviews=4
    title: MoMamba: A Lightweight Music Oriented Mamba-Based Model for Music Information Retrieval Tasks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\TUbfsCpciR_reviews.json
    forum: https://openreview.net/forum?id=TUbfsCpciR

[489] rating=3.0 | decision=Reject | reviews=4
    title: AudioMoG: Guiding Audio Generation with Mixture-of-Guidance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\LElJH6EYBq_reviews.json
    forum: https://openreview.net/forum?id=LElJH6EYBq

[490] rating=3.0 | decision=Reject | reviews=4
    title: Talk2Me: High-Fidelity and Controllable Audio-Driven Avatars with Gaussian Splatting
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\rDWvX5dxGC_reviews.json
    forum: https://openreview.net/forum?id=rDWvX5dxGC

[491] rating=3.0 | decision=Accept | reviews=3
    title: Simple-TTS: End-to-End Text-to-Speech Synthesis with Latent Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\m4mwbPjOwb_reviews.json
    forum: https://openreview.net/forum?id=m4mwbPjOwb

[492] rating=3.0 | decision=Reject | reviews=4
    title: Speech Codecs Beyond Compression: Towards Autoregressive Generative Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\FA2R2KwyTH_reviews.json
    forum: https://openreview.net/forum?id=FA2R2KwyTH

[493] rating=3.0 | decision=Reject | reviews=4
    title: AVSU-Bench and VSpeech-R1: A Dataset and MLLM for Audio-Visual Speech Understanding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\M9jciGcJpC_reviews.json
    forum: https://openreview.net/forum?id=M9jciGcJpC

[494] rating=3.0 | decision=None | reviews=4
    title: Taming Text-to-Sounding Video Generation via Advanced Modality Condition and Interaction
    pdf: research_data\iclr\video-generation\pdfs\Taming_Text-to-Sounding_Video_Generation_via_Advanced_Modality_Condition_and_Int.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=jcVOMVkljY

[495] rating=3.0 | decision=Accept | reviews=4
    title: Lost in Time: Systematic Temporal Bias in Large Audio Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0Fc9yLlIYX_reviews.json
    forum: https://openreview.net/forum?id=0Fc9yLlIYX

[496] rating=3.0 | decision=Reject | reviews=4
    title: See both ways: A bidirectional evaluation of Multimodal Language Models and Human Spontaneous Speech for Image Captioning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\mWJ0EBxCqc_reviews.json
    forum: https://openreview.net/forum?id=mWJ0EBxCqc

[497] rating=3.0 | decision=Accept | reviews=3
    title: UniComposer: Band-Level Music Composition with Symbolic and Audio Unification
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\FOcleL0ltt_reviews.json
    forum: https://openreview.net/forum?id=FOcleL0ltt

[498] rating=3.0 | decision=Reject | reviews=4
    title: DM-Codec: Distilling Multimodal Representations for Speech Tokenization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\UFwefiypla_reviews.json
    forum: https://openreview.net/forum?id=UFwefiypla

[499] rating=3.0 | decision=Reject | reviews=4
    title: Character Beyond Speech: Leveraging Role-Playing Evaluation in Large Audio Language Models via Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QQp11zpm8M_reviews.json
    forum: https://openreview.net/forum?id=QQp11zpm8M

[500] rating=3.0 | decision=Reject | reviews=4
    title: CTTS: Collective Test-Time Scaling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\yBSoEHMN6p_reviews.json
    forum: https://openreview.net/forum?id=yBSoEHMN6p

[501] rating=3.0 | decision=Accept | reviews=4
    title: Bayesian Speech Synthesisers Can Learn from Multiple Teachers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ADRwyhQWzY_reviews.json
    forum: https://openreview.net/forum?id=ADRwyhQWzY

[502] rating=2.8 | decision=Accept | reviews=5
    title: DeCodec: Rethinking Audio Codecs as Universal Disentangled Representation Learners
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\4hkMvkzai5_reviews.json
    forum: https://openreview.net/forum?id=4hkMvkzai5

[503] rating=2.7 | decision=Reject | reviews=3
    title: AVRT: Audio-Visual Reasoning Transfer through Single-Modality Teachers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\57bSlUHBfV_reviews.json
    forum: https://openreview.net/forum?id=57bSlUHBfV

[504] rating=2.7 | decision=Accept | reviews=3
    title: Towards real-time BCI for speech with Whisper-based decoding of neural activity
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\gcwzqA8iWa_reviews.json
    forum: https://openreview.net/forum?id=gcwzqA8iWa

[505] rating=2.7 | decision=Reject | reviews=3
    title: SRAMA: LEARNING SYLLABLE REPRESENTATIONS WITH ADAPTIVE LOCAL MONOTONIC ATTENTION FOR SYLLABLE STRESS DETECTION IN L2 SPEECH
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\81BKrrISll_reviews.json
    forum: https://openreview.net/forum?id=81BKrrISll

[506] rating=2.7 | decision=Reject | reviews=3
    title: LLaSO: A Reproducible Foundation for Large Speech-Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\6GWYvfsfgg_reviews.json
    forum: https://openreview.net/forum?id=6GWYvfsfgg

[507] rating=2.5 | decision=Accept | reviews=4
    title: Toward Robust Real-World Audio Deepfake Detection: Closing the Explainability Gap
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\uy9oR0nYCW_reviews.json
    forum: https://openreview.net/forum?id=uy9oR0nYCW

[508] rating=2.5 | decision=Reject | reviews=4
    title: Enabling Conversational Behavior Reasoning Capabilities in Full-Duplex Speech
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\XIuhMkAbUz_reviews.json
    forum: https://openreview.net/forum?id=XIuhMkAbUz

[509] rating=2.5 | decision=Reject | reviews=4
    title: SpeechQC-Agent: A Natural Language Driven Multi-Agent System for Speech Dataset Quality
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\AJMgU3Rspx_reviews.json
    forum: https://openreview.net/forum?id=AJMgU3Rspx

[510] rating=2.5 | decision=Accept | reviews=4
    title: Zero-Shot Non-Autoregressive TTS Beyond Autoregressive Models Using Soft Alignment Generation and Residual Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\im2a2MHoke_reviews.json
    forum: https://openreview.net/forum?id=im2a2MHoke

[511] rating=2.5 | decision=Reject | reviews=4
    title: The Sword of DamocleSpeech: Demystifying Jailbreaking Attack in Discrete Token-based Speech Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\q1Zt6mK0Kg_reviews.json
    forum: https://openreview.net/forum?id=q1Zt6mK0Kg

[512] rating=2.5 | decision=Accept | reviews=4
    title: EchoX: Towards Mitigating Acoustic-Semantic Gap via Echo Training for Speech-to-Speech LLMs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\iYjUG2LcnE_reviews.json
    forum: https://openreview.net/forum?id=iYjUG2LcnE

[513] rating=2.5 | decision=Reject | reviews=4
    title: Calibrating the Voice of Doubt: How LLMs Diverge from Humans in Verbal Uncertainty
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\uZ2A0k5liR_reviews.json
    forum: https://openreview.net/forum?id=uZ2A0k5liR

[514] rating=2.5 | decision=Reject | reviews=4
    title: DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Factorized Discrete Flow Matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\FaGDopTTTC_reviews.json
    forum: https://openreview.net/forum?id=FaGDopTTTC

[515] rating=2.5 | decision=Accept | reviews=4
    title: ivrit.ai: A Comprehensive Dataset of Hebrew Speech for AI Research and Development
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\aOPTDchLBz_reviews.json
    forum: https://openreview.net/forum?id=aOPTDchLBz

[516] rating=2.5 | decision=Accept | reviews=4
    title: OmniVIVO: Towards Unified Multimodal Generative Modeling for Simultaneous Language-Guided Speech and Image Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QHNu3atxMb_reviews.json
    forum: https://openreview.net/forum?id=QHNu3atxMb

[517] rating=2.5 | decision=Accept | reviews=4
    title: Speech-CLAP: Towards Style-Aware Speech Representation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\kylhUNRXyt_reviews.json
    forum: https://openreview.net/forum?id=kylhUNRXyt

[518] rating=2.4 | decision=Reject | reviews=5
    title: AudioCodecBench: A Comprehensive Benchmark for Audio Codecs as Tokenizer and Detokenizer for Multimodal Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\JeIDPXc9XG_reviews.json
    forum: https://openreview.net/forum?id=JeIDPXc9XG

[519] rating=2.0 | decision=Accept | reviews=3
    title: Temporal Aware Iterative Speech Model for Dementia Detection
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\A3xbZR0nUD_reviews.json
    forum: https://openreview.net/forum?id=A3xbZR0nUD

[520] rating=2.0 | decision=Reject | reviews=4
    title: WavJEPA: Semantic learning unlocks robust audio foundation models for raw waveforms
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KHcSu8HSh9_reviews.json
    forum: https://openreview.net/forum?id=KHcSu8HSh9

[521] rating=2.0 | decision=Reject | reviews=4
    title: StrucBooth: Structural Gradient Supervised Tuning for Enhanced Portrait Animation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\p75bqs6dzY_reviews.json
    forum: https://openreview.net/forum?id=p75bqs6dzY

[522] rating=2.0 | decision=Reject | reviews=4
    title: Think Out Loud, Pause in Silence: Confidence-Guided Reflect–Pause–Abort for Robust  Audio Perceptual Understanding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0zJ9aU7Tds_reviews.json
    forum: https://openreview.net/forum?id=0zJ9aU7Tds

[523] rating=2.0 | decision=Reject | reviews=4
    title: Speech-DRAME: A Framework for Human-Aligned Benchmarks in Speech Role-Play
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\FOZ4FwC7YX_reviews.json
    forum: https://openreview.net/forum?id=FOZ4FwC7YX

[524] rating=2.0 | decision=Accept | reviews=4
    title: Hierarchical Graph-coding Diffusion Model with Adaptive Information Bottleneck for Multichannel Speech Enhancement
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\WkGnZsnCDR_reviews.json
    forum: https://openreview.net/forum?id=WkGnZsnCDR

[525] rating=2.0 | decision=Reject | reviews=4
    title: Comprehend and Talk: Text to Speech Synthesis  via Dual Language Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\VPju7xAxb1_reviews.json
    forum: https://openreview.net/forum?id=VPju7xAxb1

[526] rating=2.0 | decision=Accept | reviews=4
    title: Optimizing Large Language Models with Automatic Speech Recognition for Medication Corpus in Low-Resource Healthcare Settings.
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\gpKEDj9Dgg_reviews.json
    forum: https://openreview.net/forum?id=gpKEDj9Dgg

[527] rating=1.7 | decision=Reject | reviews=3
    title: HarmonyLM: Advancing Unified Large-Scale Language Modeling for Sound and Music Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\mp8ZgMZ1RG_reviews.json
    forum: https://openreview.net/forum?id=mp8ZgMZ1RG

[528] rating=1.5 | decision=Reject | reviews=4
    title: MelCap: A Unified Single-Codebook Neural Codec for High-Fidelity Audio Compression
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\2nr6FVNOtu_reviews.json
    forum: https://openreview.net/forum?id=2nr6FVNOtu

[529] rating=1.3 | decision=Reject | reviews=3
    title: Active speech enhancement: beyond passive denoising declipping and dereverberation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QN4WZ5QoqC_reviews.json
    forum: https://openreview.net/forum?id=QN4WZ5QoqC

[530] rating=0.5 | decision=Reject | reviews=4
    title: Riemannian Geometry: Speech Detection from MEG Brain Signals Towards Non-Invasive BCI
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bkhsrCOZTu_reviews.json
    forum: https://openreview.net/forum?id=bkhsrCOZTu

[531] rating=0.0 | decision=Reject | reviews=4
    title: LLM-Augmented Soft-Label Distillation and Cluster-Guided Alignment for Language-Based Audio Retrieval
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\m7gNW26Zih_reviews.json
    forum: https://openreview.net/forum?id=m7gNW26Zih

```

## Output Format

Write the skill file with these sections:

### 1. Topic Overview
- What this research area is about, key challenges, state of the art
- Score distribution: what scores are typical, what's the acceptance bar

### 2. What Reviewers Praise (with real examples)
- Specific technical contributions that earn high scores
- Quote actual reviewer language where possible

### 3. What Reviewers Criticize (with real examples)
- Common failure modes, missing comparisons, weak experiments
- Quote actual reviewer language where possible

### 4. Required Baselines & Metrics
- What baselines and metrics are EXPECTED in this area
- Papers that miss these consistently score lower

### 5. Common Technical Pitfalls
- Specific technical mistakes reviewers flag in this area

### 6. Scoring Rubric for This Topic
- What a 3/10 paper in this area looks like (with example)
- What a 5/10 paper looks like (borderline)
- What a 7/10 paper looks like (solid accept)
- What a 9/10 paper looks like (exceptional)

### 7. Key Papers & Expected Citations
- Papers that reviewers frequently cite as expected baselines or comparisons

IMPORTANT: Ground everything in REAL reviewer quotes and paper examples. Do NOT make up generic advice.
Read the actual papers and reviews to produce technically specific, calibrated content.
