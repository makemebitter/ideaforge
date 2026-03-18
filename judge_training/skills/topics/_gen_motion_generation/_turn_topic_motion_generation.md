You are an expert AI research reviewer building a **skill file** for evaluating papers in the topic area: **motion_generation**.

## Your Task

Write a comprehensive skill file (Markdown, 10-20K tokens) that will be loaded by an AI judge agent when evaluating new research ideas in this area. The file should enable the judge to give calibrated, expert-level evaluations.

## Statistics from 109 papers in this area

```json
{
  "topic": "motion_generation",
  "num_papers": 109,
  "num_accepted": 29,
  "acceptance_rate": 0.266,
  "rating_mean": 4.93,
  "rating_median": 4.67,
  "rating_std": 1.09,
  "rating_min": 2.0,
  "rating_max": 7.5,
  "avg_soundness": 2.69,
  "avg_contribution": 2.41,
  "avg_presentation": 2.69,
  "tier_example_count": {
    "borderline (4-5)": 258,
    "good (6-7)": 92,
    "low (1-3)": 52
  }
}
```

### Most common strength phrases from reviewers:
  - ablation (85x)
  - novel (83x)
  - baseline (57x)
  - state-of-the-art (34x)
  - well-written (30x)
  - reproducib (14x)
  - well written (13x)
  - comprehensive and (9x)
  - novelty (9x)
  - scalab (8x)
  - strong empirical (6x)
  - strong results (6x)
  - lack of (6x)
  - comprehensive experiments (5x)
  - solid and (4x)
  - thorough and (4x)
  - strong generalization (4x)
  - significant improvements (4x)
  - significant gap (4x)
  - significant contributions (3x)

### Most common weakness phrases from reviewers:
  - baseline (142x)
  - ablation (114x)
  - novelty (79x)
  - lack of (60x)
  - novel (30x)
  - state-of-the-art (23x)
  - unclear how (21x)
  - lacks a (19x)
  - scalab (19x)
  - incremental (17x)
  - reproducib (17x)
  - fair comparison (14x)
  - unclear whether (11x)
  - limited to (8x)
  - limited in (8x)
  - limited novelty (6x)
  - missing in (5x)
  - lacks sufficient (5x)
  - unclear what (5x)
  - limited performance (4x)

## Paper Manifest

Below is a manifest of all 109 papers in this topic with their scores, PDF paths, and review JSON paths.

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
# Paper Manifest for topic: motion_generation
# 109 papers total

[1] rating=7.5 | decision=None | reviews=4
    title: Co$^{\mathbf{3}}$Gesture: Towards Coherent Concurrent Co-speech 3D Gesture Generation with Interactive Diffusion
    pdf: research_data\iclr\gesture-generation\pdfs\Co$^{_mathbf{3}}$Gesture__Towards_Coherent_Concurrent_Co-speech_3D_Gesture_Gener.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=VaowElpVzd

[2] rating=7.3 | decision=None | reviews=3
    title: MTVCraft: Tokenizing 4D Motion for Arbitrary Character Animation
    pdf: research_data\iclr\video-generation\pdfs\MTVCraft__Tokenizing_4D_Motion_for_Arbitrary_Character_Animation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=m7AQM9H6wa

[3] rating=7.3 | decision=None | reviews=3
    title: Direct Post-Training Preference Alignment for Multi-Agent Motion Generation Model Using Implicit Feedback from Pre-training Demonstrations
    pdf: research_data\iclr\motion-generation\pdfs\Direct_Post-Training_Preference_Alignment_for_Multi-Agent_Motion_Generation_Mode.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=8UFG9D8xeU

[4] rating=7.2 | decision=None | reviews=4
    title: NeRM: Learning Neural Representations for High-Framerate Human Motion Synthesis
    pdf: research_data\iclr\motion-generation\pdfs\NeRM__Learning_Neural_Representations_for_High-Framerate_Human_Motion_Synthesis.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=sOJriBlOFd

[5] rating=7.0 | decision=Accept | reviews=4
    title: Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\mIeKe74W43_reviews.json
    forum: https://openreview.net/forum?id=mIeKe74W43

[6] rating=7.0 | decision=Accept (Poster) | reviews=4
    title: Towards Unified Human Motion-Language Understanding via Sparse Interpretable Characterization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Oh8MuCacJW_reviews.json
    forum: https://openreview.net/forum?id=Oh8MuCacJW

[7] rating=7.0 | decision=Accept (Poster) | reviews=4
    title: SEPT: Towards Efficient Scene Representation Learning for Motion Prediction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\efeBC1sQj9_reviews.json
    forum: https://openreview.net/forum?id=efeBC1sQj9

[8] rating=7.0 | decision=None | reviews=4
    title: Aligning Human Motion Generation with Human Perceptions
    pdf: research_data\iclr\motion-generation\pdfs\Aligning_Human_Motion_Generation_with_Human_Perceptions.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=QOHgjY5KDp

[9] rating=6.5 | decision=None | reviews=4
    title: PianoMotion10M: Dataset and Benchmark for Hand Motion Generation in Piano Performance
    pdf: research_data\iclr\motion-generation\pdfs\PianoMotion10M__Dataset_and_Benchmark_for_Hand_Motion_Generation_in_Piano_Perfor.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rxVvRBgqmS

[10] rating=6.5 | decision=None | reviews=4
    title: Think Then React: Towards Unconstrained Action-to-Reaction Motion Generation
    pdf: research_data\iclr\motion-generation\pdfs\Think_Then_React__Towards_Unconstrained_Action-to-Reaction_Motion_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=UxzKcIZedp

[11] rating=6.5 | decision=None | reviews=4
    title: TapMo: Shape-aware Motion Generation of Skeleton-free Characters
    pdf: research_data\iclr\motion-generation\pdfs\TapMo__Shape-aware_Motion_Generation_of_Skeleton-free_Characters.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=OeH6Fdhv7q

[12] rating=6.5 | decision=None | reviews=4
    title: OmniControl: Control Any Joint at Any Time for Human Motion Generation
    pdf: research_data\iclr\motion-generation\pdfs\OmniControl__Control_Any_Joint_at_Any_Time_for_Human_Motion_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=gd0lAEtWso

[13] rating=6.2 | decision=None | reviews=5
    title: Motion-Agent: A Conversational Framework for Human Motion Generation with LLMs
    pdf: research_data\iclr\motion-generation\pdfs\Aligning_Human_Motion_Generation_with_Human_Perceptions.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=AvOhBgsE5R

[14] rating=6.0 | decision=Accept | reviews=4
    title: Sparkle: A Robust and Versatile Representation for Point Cloud-based Human Motion Capture
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0blfYtdJES_reviews.json
    forum: https://openreview.net/forum?id=0blfYtdJES

[15] rating=6.0 | decision=Accept (Poster) | reviews=10
    title: Optimal-state Dynamics Estimation for Physics-based Human Motion Capture from Videos
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\RkOT8rAmRR_reviews.json
    forum: https://openreview.net/forum?id=RkOT8rAmRR

[16] rating=6.0 | decision=None | reviews=4
    title: BRIDGING THE GAP BETWEEN HUMAN MOTION AND ACTION SEMANTICS VIA KINEMATIC PHRASES
    pdf: research_data\iclr\motion-generation\pdfs\BRIDGING_THE_GAP_BETWEEN_HUMAN_MOTION_AND_ACTION_SEMANTICS_VIA_KINEMATIC_PHRASES.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=80faVLl6ji

[17] rating=6.0 | decision=Accept (Poster) | reviews=3
    title: InterMask: 3D Human Interaction Generation via Collaborative Masked Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\ZAyuwJYN8N_reviews.json
    forum: https://openreview.net/forum?id=ZAyuwJYN8N

[18] rating=6.0 | decision=None | reviews=4
    title: InfBaGel: Human-Object-Scene Interaction Generation with Dynamic Perception and Iterative Refinement
    pdf: research_data\iclr\video-generation\pdfs\InfBaGel__Human-Object-Scene_Interaction_Generation_with_Dynamic_Perception_and.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=TeyHNq4WlI

[19] rating=6.0 | decision=None | reviews=4
    title: HumanTOMATO: Text-aligned Whole-body Motion Generation
    pdf: research_data\iclr\video-generation\pdfs\HumanTOMATO__Text-aligned_Whole-body_Motion_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rxD2ZCExRG

[20] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: Human Motion Diffusion as a Generative Prior
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\dTpbEdN9kr_reviews.json
    forum: https://openreview.net/forum?id=dTpbEdN9kr

[21] rating=6.0 | decision=None | reviews=5
    title: Quo Vadis, Motion Generation? From Large Language Models to Large Motion Models
    pdf: research_data\iclr\motion-generation\pdfs\Quo_Vadis,_Motion_Generation__From_Large_Language_Models_to_Large_Motion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=9QYJu1cGfE

[22] rating=6.0 | decision=None | reviews=4
    title: LaMP: Language-Motion Pretraining for Motion Generation, Retrieval, and Captioning
    pdf: research_data\iclr\motion-generation\pdfs\LaMP__Language-Motion_Pretraining_for_Motion_Generation,_Retrieval,_and_Captioni.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=LYawG8YkPa

[23] rating=6.0 | decision=None | reviews=4
    title: MotionDreamer: One-to-Many Motion Synthesis with Localized Generative Masked Transformer
    pdf: research_data\iclr\motion-generation\pdfs\MotionDreamer__One-to-Many_Motion_Synthesis_with_Localized_Generative_Masked_Tra.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=d23EVDRJ6g

[24] rating=5.8 | decision=None | reviews=5
    title: Multi-modal Controlled Coherent Motion Synthesis
    pdf: research_data\iclr\motion-generation\pdfs\Multi-modal_Controlled_Coherent_Motion_Synthesis.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=i5Gxilzk0u

[25] rating=5.7 | decision=None | reviews=3
    title: Sitcom-Crafter: A Plot-Driven Human Motion Generation System in 3D Scenes
    pdf: research_data\iclr\motion-generation\pdfs\Fixation-Driven_Time-Aware_3D_Human_Motion_Forecasting_in_Indoor_Scenes.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=FvIASa0tau

[26] rating=5.7 | decision=Accept (Poster) | reviews=6
    title: MoGenTS: Motion Generation based on Spatial-Temporal Joint Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\FisyQfoJCm_reviews.json
    forum: https://openreview.net/forum?id=FisyQfoJCm

[27] rating=5.6 | decision=None | reviews=5
    title: InterDance: Reactive 3D Dance Generation with Realistic Duet Interactions
    pdf: research_data\iclr\motion-generation\pdfs\InterDance__Reactive_3D_Dance_Generation_with_Realistic_Duet_Interactions.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=KfkmwYQXWh

[28] rating=5.5 | decision=Accept | reviews=4
    title: MotionCLR: Motion Generation and Training-free Editing via Understanding Attention Mechanisms
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\ijQp6HA4rK_reviews.json
    forum: https://openreview.net/forum?id=ijQp6HA4rK

[29] rating=5.5 | decision=Accept (Poster) | reviews=4
    title: MotionGPT: Human Motion as a Foreign Language
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\WqiZJGNkjn_reviews.json
    forum: https://openreview.net/forum?id=WqiZJGNkjn

[30] rating=5.5 | decision=None | reviews=4
    title: AvatarGO: Zero-shot 4D Human-Object Interaction Generation and Animation
    pdf: research_data\iclr\motion-generation\pdfs\AvatarGO__Zero-shot_4D_Human-Object_Interaction_Generation_and_Animation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Trf0R8eoGF

[31] rating=5.5 | decision=None | reviews=4
    title: Text2Interact: High-Fidelity and Diverse Text-to-Two-Person Interaction Generation
    pdf: research_data\iclr\motion-generation\pdfs\Text2Interact__High-Fidelity_and_Diverse_Text-to-Two-Person_Interaction_Generati.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=cthzUgBUn7

[32] rating=5.5 | decision=None | reviews=4
    title: Motion-R1: Enhancing Motion Generation with Decomposed Chain-of-Thought and RL Binding
    pdf: research_data\iclr\motion-generation\pdfs\Motion-R1__Enhancing_Motion_Generation_with_Decomposed_Chain-of-Thought_and_RL_B.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=eXXsUer975

[33] rating=5.5 | decision=None | reviews=4
    title: ReactDance: Hierarchical Representation for High-Fidelity and Coherent Long-Form Reactive Dance Generation
    pdf: research_data\iclr\motion-generation\pdfs\ReactDance__Hierarchical_Representation_for_High-Fidelity_and_Coherent_Long-Form.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=FvMyAMbbX0

[34] rating=5.5 | decision=Accept | reviews=4
    title: Primary-Fine Decoupling for Action Generation in Robotic Imitation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\wySMuWHmt4_reviews.json
    forum: https://openreview.net/forum?id=wySMuWHmt4

[35] rating=5.5 | decision=None | reviews=4
    title: Disentangled Hierarchical VAE for 3D Human-Human Interaction Generation
    pdf: research_data\iclr\motion-generation\pdfs\Disentangled_Hierarchical_VAE_for_3D_Human-Human_Interaction_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=53eIDko6N5

[36] rating=5.5 | decision=Accept | reviews=4
    title: The Quest for Generalizable Motion Generation: Data, Model, and Evaluation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KNke6Pkq4o_reviews.json
    forum: https://openreview.net/forum?id=KNke6Pkq4o

[37] rating=5.5 | decision=Accept (Poster) | reviews=4
    title: FineMoGen: Fine-Grained Spatio-Temporal Motion Generation and Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\GYjV1M5s0D_reviews.json
    forum: https://openreview.net/forum?id=GYjV1M5s0D

[38] rating=5.3 | decision=Accept | reviews=3
    title: RedMotion: Motion Prediction via Redundancy Reduction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\72MSbSZtHv_reviews.json
    forum: https://openreview.net/forum?id=72MSbSZtHv

[39] rating=5.3 | decision=None | reviews=3
    title: Novelty Unlocking with Multiobjective Generative Models: Batch Diversity of Human Motions
    pdf: research_data\iclr\video-generation\pdfs\Novelty_Unlocking_with_Multiobjective_Generative_Models__Batch_Diversity_of_Huma.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=xNwmWaq2KN

[40] rating=5.2 | decision=Accept | reviews=4
    title: ESDMotion: End-to-end Motion Prediction Only with SD Maps
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\sEJYPiVEt4_reviews.json
    forum: https://openreview.net/forum?id=sEJYPiVEt4

[41] rating=5.2 | decision=Accept (Poster) | reviews=8
    title: Harmonizing Stochasticity and Determinism: Scene-responsive Diverse Human Motion Prediction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\NQCkNM6TES_reviews.json
    forum: https://openreview.net/forum?id=NQCkNM6TES

[42] rating=5.2 | decision=None | reviews=5
    title: FlexMotion: Lightweight, Physics-Aware, and Controllable Human Motion Generation
    pdf: research_data\iclr\motion-generation\pdfs\ControlMM__Controllable_Masked_Motion_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=7652tHbbVE

[43] rating=5.0 | decision=Accept | reviews=4
    title: Can-Cap: Calibration-Free and Noise-Resilient Human Motion Capture via LiDAR-Camera Integration
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\FkdxBEF9gf_reviews.json
    forum: https://openreview.net/forum?id=FkdxBEF9gf

[44] rating=5.0 | decision=None | reviews=4
    title: Unconditional Human Motion and Shape Generation via Balanced Score-Based Diffusion
    pdf: research_data\iclr\motion-generation\pdfs\MotionDDM__Motion_Generation_and_Understanding_via_Discrete_Diffusion_Model.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=OHZRUCa1HW

[45] rating=5.0 | decision=Accept | reviews=4
    title: CharacterShot: Controllable and Consistent 4D Character Animation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\zvUiJqGRZx_reviews.json
    forum: https://openreview.net/forum?id=zvUiJqGRZx

[46] rating=5.0 | decision=None | reviews=4
    title: MoGIC: Boosting Motion Generation via Intention Understanding and Visual Context
    pdf: research_data\iclr\motion-generation\pdfs\MoGIC__Boosting_Motion_Generation_via_Intention_Understanding_and_Visual_Context.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=dCEBpoWVQw

[47] rating=5.0 | decision=None | reviews=4
    title: EchoMotion: Unified Human Video and Motion Generation via Dual-Modality Diffusion Transformer
    pdf: research_data\iclr\video-generation\pdfs\EchoMotion__Unified_Human_Video_and_Motion_Generation_via_Dual-Modality_Diffusio.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=eflUxFmIhZ

[48] rating=5.0 | decision=Accept | reviews=4
    title: DIVA: Discrete Diffusion Vision-Language-Action Models for Parallelized Action Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\mNya9d1DA2_reviews.json
    forum: https://openreview.net/forum?id=mNya9d1DA2

[49] rating=5.0 | decision=None | reviews=4
    title: Unified Multi-Modal Interactive and Reactive 3D Motion Generation via Rectified Flow
    pdf: research_data\iclr\motion-generation\pdfs\Unified_Multi-Modal_Interactive_and_Reactive_3D_Motion_Generation_via_Rectified.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=QaAgHKbJop

[50] rating=5.0 | decision=Reject | reviews=3
    title: Efficient Text-driven Human Motion Generation via Latent Consistency Training
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\SNsdlEp3Ne_reviews.json
    forum: https://openreview.net/forum?id=SNsdlEp3Ne

[51] rating=5.0 | decision=None | reviews=4
    title: MotionGPT3: Human Motion as a Second Modality
    pdf: research_data\iclr\motion-generation\pdfs\MotionGPT3__Human_Motion_as_a_Second_Modality.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Ha075JDMZR

[52] rating=4.8 | decision=Reject | reviews=4
    title: Physics-based Skinned Dance Generation with RL Fine-tuning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\8Rad5LwSv2_reviews.json
    forum: https://openreview.net/forum?id=8Rad5LwSv2

[53] rating=4.7 | decision=Reject | reviews=3
    title: LaMoGen: Language to Motion Generation Through LLM-Guided Symbolic Inference
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\SeVHd0s3T4_reviews.json
    forum: https://openreview.net/forum?id=SeVHd0s3T4

[54] rating=4.7 | decision=Reject | reviews=3
    title: Never Forget the Basics: In-distribution Knowledge Retention for Continual Test-time Adaptation in Human Motion Prediction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\nc0XGK40dn_reviews.json
    forum: https://openreview.net/forum?id=nc0XGK40dn

[55] rating=4.7 | decision=Accept | reviews=3
    title: KinemaDiff: Towards Diffusion for Coherent and Physically Plausible Human Motion Prediction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\uxTQeKAUh5_reviews.json
    forum: https://openreview.net/forum?id=uxTQeKAUh5

[56] rating=4.7 | decision=None | reviews=3
    title: SyMoFlow: Interaction-Aware Motion Synthesis from Text via Symmetric Flows
    pdf: research_data\iclr\motion-generation\pdfs\SyMoFlow__Interaction-Aware_Motion_Synthesis_from_Text_via_Symmetric_Flows.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rArZ9eXuA7

[57] rating=4.6 | decision=Reject | reviews=5
    title: Causal Motion Tokenizer for Streaming Motion Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\WavXPunwzM_reviews.json
    forum: https://openreview.net/forum?id=WavXPunwzM

[58] rating=4.6 | decision=Accept (Poster) | reviews=5
    title: Social Motion Prediction with Cognitive Hierarchies
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\lRu0dN7BY6_reviews.json
    forum: https://openreview.net/forum?id=lRu0dN7BY6

[59] rating=4.5 | decision=None | reviews=4
    title: TriC-Motion: Tri-Domain Causal Modeling Grounded Text-to-Motion Generation
    pdf: research_data\iclr\video-generation\pdfs\TriC-Motion__Tri-Domain_Causal_Modeling_Grounded_Text-to-Motion_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ROh4oDPVpD

[60] rating=4.5 | decision=None | reviews=4
    title: PlanMoGPT: Flow-Enhanced Progressive Planning for Text to Motion Synthesis
    pdf: research_data\iclr\motion-generation\pdfs\PlanMoGPT__Flow-Enhanced_Progressive_Planning_for_Text_to_Motion_Synthesis.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=SjHaqpXDVW

[61] rating=4.5 | decision=None | reviews=4
    title: Fixation-Driven Time-Aware 3D Human Motion Forecasting in Indoor Scenes
    pdf: research_data\iclr\motion-generation\pdfs\Fixation-Driven_Time-Aware_3D_Human_Motion_Forecasting_in_Indoor_Scenes.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=uj90Ef5zxo

[62] rating=4.5 | decision=None | reviews=4
    title: Multi-Modal Action Recognizer Bridges Human Motion Generation and Understanding
    pdf: research_data\iclr\motion-generation\pdfs\Multi-Modal_Action_Recognizer_Bridges_Human_Motion_Generation_and_Understanding.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ZL1QqLkfLD

[63] rating=4.5 | decision=Reject | reviews=4
    title: OpenT2M: No-frill Motion Generation with Open-source, Large-scale, High-quality Data
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\YcJnHKVB9v_reviews.json
    forum: https://openreview.net/forum?id=YcJnHKVB9v

[64] rating=4.5 | decision=Reject | reviews=4
    title: Revisiting Standard-Definition Map Based Motion Prediction in the Era of End-to-End Autonomous Driving
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\aqwtK0OIGs_reviews.json
    forum: https://openreview.net/forum?id=aqwtK0OIGs

[65] rating=4.5 | decision=None | reviews=4
    title: Event-T2M: Event-level Conditioning for Complex Text-to-Motion Synthesis
    pdf: research_data\iclr\motion-generation\pdfs\Event-T2M__Event-level_Conditioning_for_Complex_Text-to-Motion_Synthesis.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=mXPeXZ1KWT

[66] rating=4.5 | decision=Reject | reviews=4
    title: UniMo: Unifying 2D Video and 3D Human Motion with an Autoregressive Framework
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\n8s5RILeBs_reviews.json
    forum: https://openreview.net/forum?id=n8s5RILeBs

[67] rating=4.5 | decision=Reject | reviews=4
    title: Diffusion Implicit Policy for Unpaired Scene-aware Motion Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\rvOpON15JJ_reviews.json
    forum: https://openreview.net/forum?id=rvOpON15JJ

[68] rating=4.5 | decision=None | reviews=4
    title: Pulp Motion: Framing-aware multimodal camera and human motion generation
    pdf: research_data\iclr\motion-generation\pdfs\Pulp_Motion__Framing-aware_multimodal_camera_and_human_motion_generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=RRbnVt9c8t

[69] rating=4.5 | decision=None | reviews=4
    title: HINT: Hierarchical Interaction Modeling for Autoregressive Multi-Human Motion Generation
    pdf: research_data\iclr\motion-generation\pdfs\Disentangled_Hierarchical_VAE_for_3D_Human-Human_Interaction_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=CGALrQfkYi

[70] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Autoregressive Motion Generation with Gaussian Mixture-Guided Latent Sampling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\3oh7lBEF7X_reviews.json
    forum: https://openreview.net/forum?id=3oh7lBEF7X

[71] rating=4.5 | decision=None | reviews=4
    title: Generating Human Motion Videos using a Cascaded Text-to-Video Framework
    pdf: research_data\iclr\text-to-video\pdfs\Generating_Human_Motion_Videos_using_a_Cascaded_Text-to-Video_Framework.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=XwHQMNUSZP

[72] rating=4.5 | decision=Reject | reviews=4
    title: Video Language Models are Human-Aligned Evaluators for Text to Motion Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\nHEMumYcwt_reviews.json
    forum: https://openreview.net/forum?id=nHEMumYcwt

[73] rating=4.5 | decision=None | reviews=4
    title: COME: Advancing Representation Learning and Generative Modeling for High-Quality Text-to-Motion Generation
    pdf: research_data\iclr\motion-generation\pdfs\COME__Advancing_Representation_Learning_and_Generative_Modeling_for_High-Quality.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=D8fW5tAHq8

[74] rating=4.5 | decision=None | reviews=4
    title: FreeMo: Motion Generation with Structured Joint-Collision Energy
    pdf: research_data\iclr\video-generation\pdfs\FreeMo__Motion_Generation_with_Structured_Joint-Collision_Energy.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=QJJMUErY1k

[75] rating=4.5 | decision=Reject | reviews=4
    title: MoRe4D: Joint 3D Motion Generation and Geometry Reconstruction for 4D Synthesis from a Single Image
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0unRcs07Bb_reviews.json
    forum: https://openreview.net/forum?id=0unRcs07Bb

[76] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: MEGADance: Mixture-of-Experts Architecture for Genre-Aware 3D Dance Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\oIBwHvF930_reviews.json
    forum: https://openreview.net/forum?id=oIBwHvF930

[77] rating=4.5 | decision=Accept | reviews=4
    title: HOI-PAGE: Zero-Shot Human-Object Interaction Generation with Part Affordance Guidance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qZhk7prB7v_reviews.json
    forum: https://openreview.net/forum?id=qZhk7prB7v

[78] rating=4.5 | decision=None | reviews=4
    title: SceneAdapt: Scene-aware Adaptation of Human Motion Diffusion
    pdf: research_data\iclr\motion-generation\pdfs\SceneAdapt__Scene-aware_Adaptation_of_Human_Motion_Diffusion.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=n2RM4uVFSM

[79] rating=4.3 | decision=Reject | reviews=3
    title: Textual $\textbf{D}$ecomposition then Sub-motion-space $\textbf{S}$cattering for $\textbf{O}$pen-Vocabulary Motion Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\ja2gQFYA9R_reviews.json
    forum: https://openreview.net/forum?id=ja2gQFYA9R

[80] rating=4.3 | decision=Reject | reviews=3
    title: Pose-guided Motion Diffusion Model for Text-to-motion Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\if8iIYcmVC_reviews.json
    forum: https://openreview.net/forum?id=if8iIYcmVC

[81] rating=4.3 | decision=Reject | reviews=3
    title: Motion Flow Matching for Efficient Human Motion Synthesis and Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\ikdB0VXPlw_reviews.json
    forum: https://openreview.net/forum?id=ikdB0VXPlw

[82] rating=4.3 | decision=Reject | reviews=3
    title: MAS: Multi-view Ancestral Sampling for 3D motion generation using 2D diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\dBO8ZPQMVF_reviews.json
    forum: https://openreview.net/forum?id=dBO8ZPQMVF

[83] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: EverybodyDance: Bipartite Graph–Based Identity Correspondence for Multi-Character Animation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\vqXWCC0aUG_reviews.json
    forum: https://openreview.net/forum?id=vqXWCC0aUG

[84] rating=4.2 | decision=Reject | reviews=4
    title: PhaseFusion: A Diffusion-based Periodic Parameterized Motion Generation Framework
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\iHSp6wvQmV_reviews.json
    forum: https://openreview.net/forum?id=iHSp6wvQmV

[85] rating=4.0 | decision=None | reviews=3
    title: SimDiff: Simulator-constrained Diffusion Model for Physically Plausible Motion Generation
    pdf: research_data\iclr\motion-generation\pdfs\SimDiff__Simulator-constrained_Diffusion_Model_for_Physically_Plausible_Motion_G.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=jFHaK889Jv

[86] rating=4.0 | decision=Reject | reviews=4
    title: Motion Generalist: Multimodal Motion Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\mx9jLnzQGr_reviews.json
    forum: https://openreview.net/forum?id=mx9jLnzQGr

[87] rating=4.0 | decision=Reject | reviews=4
    title: TopoFormer: Topology-aware Transformer for Reactive Motion Prediction in Close Interactions
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\PBEQIxXDDD_reviews.json
    forum: https://openreview.net/forum?id=PBEQIxXDDD

[88] rating=4.0 | decision=Reject | reviews=4
    title: SemanticBoost: Elevating Motion Generation with Augmented Textual Cues
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\sVlvuV70Yn_reviews.json
    forum: https://openreview.net/forum?id=sVlvuV70Yn

[89] rating=4.0 | decision=Accept (Poster) | reviews=11
    title: ToF-IP: Time-of-Flight Enhanced Sparse Inertial Poser for Real-time Human Motion Capture
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\fLKrX29Zy6_reviews.json
    forum: https://openreview.net/forum?id=fLKrX29Zy6

[90] rating=4.0 | decision=None | reviews=3
    title: High-Fidelity Human Motion Generation with Motion Quality Feedbacks
    pdf: research_data\iclr\motion-generation\pdfs\Aligning_Human_Motion_Generation_with_Human_Perceptions.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=FAgro0MDDp

[91] rating=4.0 | decision=Reject | reviews=4
    title: DisCo: Disentangled Control for Realistic Human Dance Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\sk7RRHFk7M_reviews.json
    forum: https://openreview.net/forum?id=sk7RRHFk7M

[92] rating=4.0 | decision=None | reviews=4
    title: Learning Text-driven 3D Human Motion Generation from 3D-free Web Videos
    pdf: research_data\iclr\motion-generation\pdfs\Learning_Text-driven_3D_Human_Motion_Generation_from_3D-free_Web_Videos.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nvu9jVEqoo

[93] rating=4.0 | decision=Accept | reviews=12
    title: Absolute Coordinates Make Motion Generation Easy
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\TaURJrZcjJ_reviews.json
    forum: https://openreview.net/forum?id=TaURJrZcjJ

[94] rating=4.0 | decision=Reject | reviews=3
    title: Understanding the Task and Data Misconceptions in Online Map Based Motion Prediction for Autonomous Driving and a Boundary-Free Baseline
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\M14YpuTejd_reviews.json
    forum: https://openreview.net/forum?id=M14YpuTejd

[95] rating=4.0 | decision=Reject | reviews=5
    title: MMG-VL: A Vision-Language Driven Approach for Multi-Person Motion Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\B5AN6IRyXc_reviews.json
    forum: https://openreview.net/forum?id=B5AN6IRyXc

[96] rating=3.8 | decision=Accept (Poster) | reviews=12
    title: HMVLM:Human Motion-Vision-Language Model via MoE LoRA
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\Gvq2AfuVEA_reviews.json
    forum: https://openreview.net/forum?id=Gvq2AfuVEA

[97] rating=3.8 | decision=Accept | reviews=12
    title: CacheFlow: Fast Human Motion Prediction by Cached Normalizing Flow
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\y8dGdBJkWa_reviews.json
    forum: https://openreview.net/forum?id=y8dGdBJkWa

[98] rating=3.7 | decision=Reject | reviews=6
    title: Web Agents Are Still Greedy: Progress-Aware Action Generation and Selection via Meta-Plan
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\6PT63brh4E_reviews.json
    forum: https://openreview.net/forum?id=6PT63brh4E

[99] rating=3.5 | decision=Reject | reviews=4
    title: SIG-Chat: Spatial Intent-Guided Conversational Gesture Generation Involving How, When and Where
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1XYG3pVCWf_reviews.json
    forum: https://openreview.net/forum?id=1XYG3pVCWf

[100] rating=3.5 | decision=None | reviews=4
    title: Back to Basics: Motion Representation Matters for Human Motion Generation Using Diffusion Model
    pdf: research_data\iclr\motion-generation\pdfs\Back_to_Basics__Motion_Representation_Matters_for_Human_Motion_Generation_Using.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Ly6NP07Rw5

[101] rating=3.5 | decision=Reject | reviews=4
    title: OmniMotion: Multimodal Motion Generation with Continuous Masked Autoregression
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qKaMU1l7Lc_reviews.json
    forum: https://openreview.net/forum?id=qKaMU1l7Lc

[102] rating=3.5 | decision=Reject | reviews=4
    title: SHAPING LATENT DIFFUSION FOR EFFICIENT TEXT-CONDITIONED INTERACTION GENERATION
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\BUd2FPvJb2_reviews.json
    forum: https://openreview.net/forum?id=BUd2FPvJb2

[103] rating=3.5 | decision=Reject | reviews=4
    title: SafeMo: Trustworthy Motion Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\SKTxKHumh3_reviews.json
    forum: https://openreview.net/forum?id=SKTxKHumh3

[104] rating=3.5 | decision=Reject | reviews=4
    title: CODA: Commonsense-Driven Autoregressive Human Interaction Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KH32pA5Mr5_reviews.json
    forum: https://openreview.net/forum?id=KH32pA5Mr5

[105] rating=3.5 | decision=Reject | reviews=6
    title: iMotion-LLM: Motion Prediction Instruction Tuning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\VlWWzN7RtJ_reviews.json
    forum: https://openreview.net/forum?id=VlWWzN7RtJ

[106] rating=3.0 | decision=None | reviews=4
    title: MotionDDM: Motion Generation and Understanding via Discrete Diffusion Model
    pdf: research_data\iclr\motion-generation\pdfs\MoGIC__Boosting_Motion_Generation_via_Intention_Understanding_and_Visual_Context.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=oZ9f1pwXEM

[107] rating=3.0 | decision=Reject | reviews=4
    title: Refine Synthesized Action-Conditioned 3D Human Motion with Unsupervised Learned Motion Concepts
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ZNbzdBIWSd_reviews.json
    forum: https://openreview.net/forum?id=ZNbzdBIWSd

[108] rating=2.0 | decision=Reject | reviews=4
    title: Humanoid-R0: Bridging Text-to-Motion Generation and Physical Deployment via RL
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\agohD5ewsR_reviews.json
    forum: https://openreview.net/forum?id=agohD5ewsR

[109] rating=2.0 | decision=None | reviews=4
    title: Motion-R1: Latent-Intent Motion Generation with Physical Consistency
    pdf: research_data\iclr\motion-generation\pdfs\Motion-R1__Latent-Intent_Motion_Generation_with_Physical_Consistency.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=r5Ii1GTEWj

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
