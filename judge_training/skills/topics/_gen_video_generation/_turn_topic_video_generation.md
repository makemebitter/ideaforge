You are an expert AI research reviewer building a **skill file** for evaluating papers in the topic area: **video_generation**.

## Your Task

Write a comprehensive skill file (Markdown, 10-20K tokens) that will be loaded by an AI judge agent when evaluating new research ideas in this area. The file should enable the judge to give calibrated, expert-level evaluations.

## Statistics from 414 papers in this area

```json
{
  "topic": "video_generation",
  "num_papers": 414,
  "num_accepted": 80,
  "acceptance_rate": 0.193,
  "rating_mean": 4.88,
  "rating_median": 5.0,
  "rating_std": 1.1,
  "rating_min": 2.0,
  "rating_max": 8.0,
  "avg_soundness": 2.67,
  "avg_contribution": 2.45,
  "avg_presentation": 2.7,
  "tier_example_count": {
    "low (1-3)": 232,
    "borderline (4-5)": 953,
    "good (6-7)": 341,
    "excellent (8-10)": 4
  }
}
```

### Most common strength phrases from reviewers:
  - novel (261x)
  - ablation (254x)
  - baseline (201x)
  - well-written (148x)
  - state-of-the-art (86x)
  - well written (58x)
  - scalab (54x)
  - novelty (42x)
  - reproducib (37x)
  - strong empirical (27x)
  - comprehensive experiments (26x)
  - comprehensive and (25x)
  - strong baselines (19x)
  - comprehensive evaluation (19x)
  - lack of (18x)
  - thorough and (17x)
  - strong performance (14x)
  - significant improvements (13x)
  - incremental (10x)
  - strong results (10x)

### Most common weakness phrases from reviewers:
  - baseline (600x)
  - ablation (392x)
  - novelty (333x)
  - lack of (252x)
  - novel (138x)
  - scalab (85x)
  - unclear how (81x)
  - state-of-the-art (79x)
  - incremental (71x)
  - unclear whether (70x)
  - limited to (67x)
  - reproducib (64x)
  - lacks a (50x)
  - fair comparison (47x)
  - limited novelty (35x)
  - unclear if (25x)
  - unclear why (24x)
  - insufficient to (17x)
  - lacks clarity (16x)
  - missing in (15x)

## Paper Manifest

Below is a manifest of all 414 papers in this topic with their scores, PDF paths, and review JSON paths.

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
# Paper Manifest for topic: video_generation
# 414 papers total

[1] rating=8.0 | decision=None | reviews=4
    title: Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator
    pdf: research_data\iclr\text-to-video\pdfs\Text-to-3D_by_Stitching_a_Multi-view_Reconstruction_Network_to_a_Video_Generator.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=kI27Niy4xY

[2] rating=7.5 | decision=None | reviews=4
    title: SlowFast-VGen: Slow-Fast Learning for Action-Driven Long Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Mixture_of_Contexts_for_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=UL8b54P96G

[3] rating=7.3 | decision=None | reviews=3
    title: InfoTok: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression
    pdf: research_data\iclr\video-tokenizer\pdfs\InfoTok__Adaptive_Discrete_Video_Tokenizer_via_Information-Theoretic_Compression.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=JEYWpFGzvn

[4] rating=7.3 | decision=None | reviews=3
    title: Self-Forcing++: Towards Minute-Scale High-Quality Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Self-Forcing++__Towards_Minute-Scale_High-Quality_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=DzvPiqh23f

[5] rating=7.3 | decision=None | reviews=3
    title: MotionAura: Generating High-Quality and Motion Consistent Videos using Discrete Diffusion
    pdf: research_data\iclr\text-to-video\pdfs\MotionAura__Generating_High-Quality_and_Motion_Consistent_Videos_using_Discrete.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=bW9fGYo44s

[6] rating=7.0 | decision=Reject | reviews=4
    title: Clearer Frames, Anytime: Resolving Velocity Ambiguity in Video Frame Interpolation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\QuFHei1vuE_reviews.json
    forum: https://openreview.net/forum?id=QuFHei1vuE

[7] rating=7.0 | decision=None | reviews=4
    title: ViBiDSampler: Enhancing Video Interpolation Using Bidirectional Diffusion Sampler
    pdf: research_data\iclr\text-to-video\pdfs\ViBiDSampler__Enhancing_Video_Interpolation_Using_Bidirectional_Diffusion_Sample.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nNYA7tcJSE

[8] rating=7.0 | decision=None | reviews=4
    title: Ctrl-Adapter: An Efficient and Versatile Framework for Adapting Diverse Controls to Any Diffusion Model
    pdf: research_data\iclr\text-to-video\pdfs\Ctrl-Adapter__An_Efficient_and_Versatile_Framework_for_Adapting_Diverse_Controls.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ny8T8OuNHe

[9] rating=7.0 | decision=None | reviews=4
    title: InternVid: A Large-scale Video-Text Dataset for Multimodal Understanding and Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=MLBdiWu4Fw

[10] rating=7.0 | decision=None | reviews=4
    title: GameGen-X: Interactive Open-world Game Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\GameGen-X__Interactive_Open-world_Game_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=8VG8tpPZhe

[11] rating=7.0 | decision=None | reviews=4
    title: Do Egocentric Video-Language Models Truly Understand Hand-Object Interactions?
    pdf: research_data\iclr\text-to-video\pdfs\Do_Egocentric_Video-Language_Models_Truly_Understand_Hand-Object_Interactions.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=M8gXSFGkn2

[12] rating=7.0 | decision=None | reviews=4
    title: OpenVid-1M: A Large-Scale High-Quality Dataset for Text-to-video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=j7kdXSrISM

[13] rating=7.0 | decision=None | reviews=4
    title: TokenFlow: Consistent Diffusion Features for Consistent Video Editing
    pdf: research_data\iclr\video-editing\pdfs\TokenFlow__Consistent_Diffusion_Features_for_Consistent_Video_Editing.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=lKK50q2MtV

[14] rating=7.0 | decision=None | reviews=4
    title: MoGA: Mixture-of-Groups Attention for End-to-End Long Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Mixture_of_Contexts_for_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=0hy9kJ1ULB

[15] rating=7.0 | decision=None | reviews=4
    title: Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation
    pdf: research_data\iclr\video-diffusion\pdfs\Lyra__Generative_3D_Scene_Reconstruction_via_Video_Diffusion_Model_Self-Distilla.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=tIVCfVnIHo

[16] rating=7.0 | decision=Accept (Spotlight) | reviews=8
    title: StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\VFqzxhINFU_reviews.json
    forum: https://openreview.net/forum?id=VFqzxhINFU

[17] rating=7.0 | decision=None | reviews=4
    title: Efficient Video Diffusion Models via Content-Frame Motion-Latent Decomposition
    pdf: research_data\iclr\video-generation\pdfs\Efficient_Video_Diffusion_Models_via_Content-Frame_Motion-Latent_Decomposition.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=dQVtTdsvZH

[18] rating=6.8 | decision=None | reviews=5
    title: ECHOPulse: ECG Controlled Echocardio-gram Video Generation
    pdf: research_data\iclr\video-generation\pdfs\ECHOPulse__ECG_Controlled_Echocardio-gram_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=i2r7LDjba3

[19] rating=6.8 | decision=None | reviews=5
    title: CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer
    pdf: research_data\iclr\text-to-video\pdfs\CogVideoX__Text-to-Video_Diffusion_Models_with_An_Expert_Transformer.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=LQzN6TRFg9

[20] rating=6.8 | decision=Accept (Poster) | reviews=8
    title: VFIMamba: Video Frame Interpolation with State Space Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\4s5UsBUsUS_reviews.json
    forum: https://openreview.net/forum?id=4s5UsBUsUS

[21] rating=6.8 | decision=None | reviews=4
    title: Compositional Video Generation as Flow Equalization
    pdf: research_data\iclr\text-to-video\pdfs\Compositional_Video_Generation_as_Flow_Equalization.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=qTWDpbF47t

[22] rating=6.8 | decision=None | reviews=4
    title: 3DTrajMaster: Mastering 3D Trajectory for Multi-Entity Motion in Video Generation
    pdf: research_data\iclr\video-generation\pdfs\3DTrajMaster__Mastering_3D_Trajectory_for_Multi-Entity_Motion_in_Video_Generatio.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Gx04TnVjee

[23] rating=6.7 | decision=None | reviews=3
    title: TweedieMix: Improving Multi-Concept Fusion for Diffusion-based Image/Video Generation
    pdf: research_data\iclr\image-to-video\pdfs\TweedieMix__Improving_Multi-Concept_Fusion_for_Diffusion-based_Image_Video_Gener.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ee2c4MEx9l

[24] rating=6.7 | decision=None | reviews=3
    title: Mixture of Contexts for Long Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Mixture_of_Contexts_for_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=y6XJZlEC2x

[25] rating=6.7 | decision=None | reviews=3
    title: SVG: 3D Stereoscopic Video Generation via Denoising Frame Matrix
    pdf: research_data\iclr\video-generation\pdfs\SVG__3D_Stereoscopic_Video_Generation_via_Denoising_Frame_Matrix.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=sx2jXZuhIx

[26] rating=6.7 | decision=None | reviews=3
    title: LongLive: Real-time Interactive Long Video Generation
    pdf: research_data\iclr\video-generation\pdfs\LongLive__Real-time_Interactive_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nCAODkpsPJ

[27] rating=6.7 | decision=None | reviews=3
    title: EgoExo-Gen: Ego-centric Video Prediction by Watching Exo-centric Videos
    pdf: research_data\iclr\video-diffusion\pdfs\EgoExo-Gen__Ego-centric_Video_Prediction_by_Watching_Exo-centric_Videos.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=8J2DrrWDKE

[28] rating=6.5 | decision=None | reviews=4
    title: Seer: Language Instructed Video Prediction with Latent Diffusion Models
    pdf: research_data\iclr\video-diffusion\pdfs\Diffusion_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=qHGgNyQk31

[29] rating=6.5 | decision=None | reviews=4
    title: CameraCtrl: Enabling Camera Control for Video Diffusion Models
    pdf: research_data\iclr\video-generation\pdfs\Boosting_Camera_Motion_Control_for_Video_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Z4evOUYrk7

[30] rating=6.5 | decision=Accept (Spotlight) | reviews=4
    title: Learning Universal Policies via Text-Guided Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\bo8q5MRcwy_reviews.json
    forum: https://openreview.net/forum?id=bo8q5MRcwy

[31] rating=6.5 | decision=None | reviews=4
    title: Stable Video Infinity: Infinite-Length Video Generation with Error Recycling
    pdf: research_data\iclr\video-generation\pdfs\Stable_Video_Infinity__Infinite-Length_Video_Generation_with_Error_Recycling.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=X96Ei9n34a

[32] rating=6.5 | decision=None | reviews=4
    title: Joint Audio-Video Diffusion Transformer with Hierarchical Spatio-Temporal Prior Synchronization
    pdf: research_data\iclr\video-generation\pdfs\Joint_Audio-Video_Diffusion_Transformer_with_Hierarchical_Spatio-Temporal_Prior.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=y7HV7KT3Bd

[33] rating=6.5 | decision=None | reviews=4
    title: Framer: Interactive Frame Interpolation
    pdf: research_data\iclr\video-generation\pdfs\Framer__Interactive_Frame_Interpolation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Lp40Z40N07

[34] rating=6.5 | decision=None | reviews=4
    title: FLATTEN: optical FLow-guided ATTENtion for consistent text-to-video editing
    pdf: research_data\iclr\text-to-video\pdfs\FLATTEN__optical_FLow-guided_ATTENtion_for_consistent_text-to-video_editing.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=JgqftqZQZ7

[35] rating=6.5 | decision=None | reviews=4
    title: Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning
    pdf: research_data\iclr\video-generation\pdfs\Cosmos_Policy__Fine-Tuning_Video_Models_for_Visuomotor_Control_and_Planning.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=wPEIStHxYH

[36] rating=6.5 | decision=Accept | reviews=4
    title: VideoChat-Flash: Hierarchical Compression for Long-Context Video Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\MUjdNcfNPv_reviews.json
    forum: https://openreview.net/forum?id=MUjdNcfNPv

[37] rating=6.5 | decision=None | reviews=4
    title: Ground-A-Video: Zero-shot Grounded Video Editing using Text-to-image Diffusion Models
    pdf: research_data\iclr\video-editing\pdfs\Ground-A-Video__Zero-shot_Grounded_Video_Editing_using_Text-to-image_Diffusion_M.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=28L2FCtMWq

[38] rating=6.5 | decision=None | reviews=4
    title: VideoGrain: Modulating Space-Time Attention for Multi-Grained Video Editing
    pdf: research_data\iclr\video-generation\pdfs\VideoGrain__Modulating_Space-Time_Attention_for_Multi-Grained_Video_Editing.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=SSslAtcPB6

[39] rating=6.5 | decision=None | reviews=4
    title: Controlling Space and Time with Diffusion Models
    pdf: research_data\iclr\image-to-video\pdfs\Controlling_Space_and_Time_with_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=d2UrCGtntF

[40] rating=6.5 | decision=None | reviews=4
    title: Autoregressive Video Generation without Vector Quantization
    pdf: research_data\iclr\text-to-video\pdfs\Autoregressive_Video_Generation_without_Vector_Quantization.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=JE9tCwe3lp

[41] rating=6.5 | decision=None | reviews=4
    title: SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer
    pdf: research_data\iclr\video-generation\pdfs\SANA-Video__Efficient_Video_Generation_with_Block_Linear_Diffusion_Transformer.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=mzAchylAtf

[42] rating=6.4 | decision=Accept (Poster) | reviews=5
    title: VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\YbhHz0X2j5_reviews.json
    forum: https://openreview.net/forum?id=YbhHz0X2j5

[43] rating=6.4 | decision=None | reviews=5
    title: Monocular Normal Estimation via Shading Sequence Estimation
    pdf: research_data\iclr\image-to-video\pdfs\Monocular_Normal_Estimation_via_Shading_Sequence_Estimation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=d7itDxMD1n

[44] rating=6.4 | decision=None | reviews=5
    title: Robust Watermarking Using Generative Priors Against Image Editing: From Benchmarking to Advances
    pdf: research_data\iclr\image-to-video\pdfs\Robust_Watermarking_Using_Generative_Priors_Against_Image_Editing__From_Benchmar.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=16O8GCm8Wn

[45] rating=6.3 | decision=None | reviews=3
    title: IV-mixed Sampler: Leveraging Image Diffusion Models for Enhanced Video Synthesis
    pdf: research_data\iclr\video-generation\pdfs\IV-mixed_Sampler__Leveraging_Image_Diffusion_Models_for_Enhanced_Video_Synthesis.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ImpeMDJfVL

[46] rating=6.2 | decision=None | reviews=4
    title: Cross-Modal Contextualized Diffusion Models for Text-Guided Visual Generation and Editing
    pdf: research_data\iclr\text-to-video\pdfs\Cross-Modal_Contextualized_Diffusion_Models_for_Text-Guided_Visual_Generation_an.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nFMS6wF2xq

[47] rating=6.2 | decision=None | reviews=4
    title: Probabilistic Adaptation of Black-Box Text-to-Video Models
    pdf: research_data\iclr\text-to-video\pdfs\Probabilistic_Adaptation_of_Black-Box_Text-to-Video_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=pjtIEgscE3

[48] rating=6.2 | decision=None | reviews=4
    title: VideoPhy: Evaluating Physical Commonsense for Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=9D2QvO1uWj

[49] rating=6.2 | decision=None | reviews=4
    title: ARLON: Boosting Diffusion Transformers with Autoregressive Models for Long Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\ARLON__Boosting_Diffusion_Transformers_with_Autoregressive_Models_for_Long_Video.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=8pusxkLEQO

[50] rating=6.2 | decision=None | reviews=5
    title: VD3D: Taming Large Video Diffusion Transformers for 3D Camera Control
    pdf: research_data\iclr\text-to-video\pdfs\VD3D__Taming_Large_Video_Diffusion_Transformers_for_3D_Camera_Control.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=0n4bS0R5MM

[51] rating=6.2 | decision=Accept (Poster) | reviews=10
    title: 4Real: Towards Photorealistic 4D Scene Generation via Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\SO1aRpwVLk_reviews.json
    forum: https://openreview.net/forum?id=SO1aRpwVLk

[52] rating=6.2 | decision=Accept (Poster) | reviews=10
    title: GenRec: Unifying Video Generation and Recognition with Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\YdfZP7qMzp_reviews.json
    forum: https://openreview.net/forum?id=YdfZP7qMzp

[53] rating=6.0 | decision=None | reviews=4
    title: Target-Aware Video Diffusion Models
    pdf: research_data\iclr\video-generation\pdfs\CameraCtrl__Enabling_Camera_Control_for_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=311AxWM8FU

[54] rating=6.0 | decision=None | reviews=4
    title: Continuous Space-Time Video Super-Resolution with 3D Fourier Fields
    pdf: research_data\iclr\video-super-resolution\pdfs\Continuous_Space-Time_Video_Super-Resolution_with_3D_Fourier_Fields.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=bLmImy7g1w

[55] rating=6.0 | decision=Reject | reviews=4
    title: SafeMVDrive: Multi-view Safety-Critical Driving Video Generation in the Real World Domain
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\tAM9SGoEmD_reviews.json
    forum: https://openreview.net/forum?id=tAM9SGoEmD

[56] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: Diffusion4D: Fast Spatial-temporal Consistent 4D generation via Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\grrefkWEES_reviews.json
    forum: https://openreview.net/forum?id=grrefkWEES

[57] rating=6.0 | decision=None | reviews=4
    title: Neodragon: Mobile Video Generation Using Diffusion Transformer
    pdf: research_data\iclr\text-to-video\pdfs\Neodragon__Mobile_Video_Generation_Using_Diffusion_Transformer.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=XBzIhhwv8d

[58] rating=6.0 | decision=None | reviews=6
    title: VideoShield: Regulating Diffusion-based Video Generation Models via Watermarking
    pdf: research_data\iclr\text-to-video\pdfs\LLM-grounded_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=uzz3qAYy0D

[59] rating=6.0 | decision=None | reviews=4
    title: LumosX: Relate Any Identities with Their Attributes for Personalized Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=r5o6PWgzav

[60] rating=6.0 | decision=None | reviews=4
    title: Animating the Uncaptured: Humanoid Mesh Animation with Video Diffusion Models
    pdf: research_data\iclr\video-diffusion\pdfs\Animating_the_Uncaptured__Humanoid_Mesh_Animation_with_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=DIPeQTxpe7

[61] rating=6.0 | decision=None | reviews=4
    title: Towards One-step Causal Video Generation via Adversarial Self-Distillation
    pdf: research_data\iclr\text-to-video\pdfs\Towards_One-step_Causal_Video_Generation_via_Adversarial_Self-Distillation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=P3O0fNmnWa

[62] rating=6.0 | decision=None | reviews=4
    title: Unified In-Context Video Editing
    pdf: research_data\iclr\text-to-video\pdfs\UniEdit__A_Unified_Tuning-Free_Framework_for_Video_Motion_and_Appearance_Editing.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Vb4nE3WWf5

[63] rating=6.0 | decision=None | reviews=3
    title: LLM-grounded Video Diffusion Models
    pdf: research_data\iclr\text-to-video\pdfs\AdaViewPlanner__Adapting_Video_Diffusion_Models_for_Viewpoint_Planning_in_4D_Sce.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=exKHibougU

[64] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: Fast and Memory-Efficient Video Diffusion Using Streamlined Inference
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\iNvXYQrkpi_reviews.json
    forum: https://openreview.net/forum?id=iNvXYQrkpi

[65] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: Free-Bloom: Zero-Shot Text-to-Video Generator with LLM Director and LDM Animator
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\paa2OU5jN8_reviews.json
    forum: https://openreview.net/forum?id=paa2OU5jN8

[66] rating=6.0 | decision=None | reviews=4
    title: VOGUE:  Unified Understanding, Generation, and Editing for Videos
    pdf: research_data\iclr\image-to-video\pdfs\VOGUE__Unified_Understanding,_Generation,_and_Editing_for_Videos.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=EDCJTaR9bk

[67] rating=6.0 | decision=None | reviews=6
    title: VADER: Video Diffusion Alignment via Reward Gradients
    pdf: research_data\iclr\text-to-video\pdfs\VADER__Video_Diffusion_Alignment_via_Reward_Gradients.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=B9dYUFfzl3

[68] rating=6.0 | decision=None | reviews=4
    title: MAGREF: Masked Guidance for Any-Reference Video Generation with Subject Disentanglement
    pdf: research_data\iclr\video-generation\pdfs\Controllable_Video_Generation_with_Provable_Disentanglement.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Nbl43eAVaE

[69] rating=6.0 | decision=None | reviews=4
    title: WorldSimBench: Towards Video Generation  Models as World Simulators
    pdf: research_data\iclr\video-generation\pdfs\OccSora__4D_Occupancy_Generation_Models_as_World_Simulators_for_Autonomous_Drivi.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ejGAytoWoe

[70] rating=6.0 | decision=None | reviews=3
    title: State & Image Guidance: Teaching Old Text-to-Video Diffusion Models New Tricks
    pdf: research_data\iclr\text-to-video\pdfs\LLM-grounded_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=zkGxROm7D3

[71] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: MotionClone: Training-Free Motion Cloning for Controllable Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\aY3L65HgHJ_reviews.json
    forum: https://openreview.net/forum?id=aY3L65HgHJ

[72] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: Vivid-ZOO: Multi-View Video Generation with Diffusion Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\bPOaHf8OcX_reviews.json
    forum: https://openreview.net/forum?id=bPOaHf8OcX

[73] rating=6.0 | decision=None | reviews=3
    title: ViDiT-Q: Efficient and Accurate Quantization of Diffusion Transformers for Image and Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Adaptive_Caching_for_Faster_Video_Generation_with_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=E1N1oxd63b

[74] rating=6.0 | decision=None | reviews=4
    title: Phantom-Data:  Towards a General Subject-Consistent Video Generation Dataset
    pdf: research_data\iclr\video-generation\pdfs\Phantom-Data__Towards_a_General_Subject-Consistent_Video_Generation_Dataset.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=IjqKXnzUXx

[75] rating=6.0 | decision=None | reviews=4
    title: DAWN: Dynamic Frame Avatar with Non-autoregressive Diffusion Framework for Talking head Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Adaptive_Caching_for_Faster_Video_Generation_with_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=vjHySpxDsv

[76] rating=6.0 | decision=None | reviews=3
    title: MoAlign: Motion-Centric Representation Alignment for Video Diffusion Models
    pdf: research_data\iclr\text-to-video\pdfs\LLM-grounded_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=OR0ySm4l9h

[77] rating=6.0 | decision=None | reviews=4
    title: MMDisCo: Multi-Modal Discriminator-Guided Cooperative Diffusion for Joint Audio and Video Generation
    pdf: research_data\iclr\video-generation\pdfs\MM-LDM__Multi-Modal_Latent_Diffusion_Model_for_Sounding_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=agbiPPuSeQ

[78] rating=6.0 | decision=None | reviews=5
    title: T2V-Turbo-v2: Enhancing Video Model Post-Training through Data, Reward, and Conditional Guidance Design
    pdf: research_data\iclr\text-to-video\pdfs\T2V-Turbo-v2__Enhancing_Video_Model_Post-Training_through_Data,_Reward,_and_Cond.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=BZwXMqu4zG

[79] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: Motion Graph Unleashed: A Novel Approach to Video Prediction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\4ztP4PujOG_reviews.json
    forum: https://openreview.net/forum?id=4ztP4PujOG

[80] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: Identifying and Solving Conditional Image Leakage in Image-to-Video Diffusion Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\o9Lkiv1qpc_reviews.json
    forum: https://openreview.net/forum?id=o9Lkiv1qpc

[81] rating=6.0 | decision=None | reviews=4
    title: VL-JEPA: Joint Embedding Predictive Architecture for Vision-language
    pdf: research_data\iclr\text-to-video\pdfs\VL-JEPA__Joint_Embedding_Predictive_Architecture_for_Vision-language.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=tjimrqc2BU

[82] rating=6.0 | decision=None | reviews=4
    title: Pusa V1.0: Unlocking Temporal Control in Pretrained Video Diffusion Models via Vectorized Timestep Adaptation
    pdf: research_data\iclr\text-to-video\pdfs\LLM-grounded_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=4adY8FepXg

[83] rating=6.0 | decision=Accept (Poster) | reviews=6
    title: Motion Consistency Model: Accelerating Video Diffusion with Disentangled Motion-Appearance Distillation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\NsqxN9iOJ7_reviews.json
    forum: https://openreview.net/forum?id=NsqxN9iOJ7

[84] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: Boosting Text-to-Video Generative Model with MLLMs Feedback
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\3ivnixHy16_reviews.json
    forum: https://openreview.net/forum?id=3ivnixHy16

[85] rating=6.0 | decision=None | reviews=3
    title: SteinsGate: Adding Causality to Diffusions for Long Video Generation via Path Integral
    pdf: research_data\iclr\video-generation\pdfs\Mixture_of_Contexts_for_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=8WS5nDWIWE

[86] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\hPWWXpCaJ7_reviews.json
    forum: https://openreview.net/forum?id=hPWWXpCaJ7

[87] rating=6.0 | decision=None | reviews=3
    title: MATRIX: Mask Track Alignment for Interaction-aware Video Generation
    pdf: research_data\iclr\video-generation\pdfs\MATRIX__Mask_Track_Alignment_for_Interaction-aware_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=lhVrFEssk5

[88] rating=5.9 | decision=None | reviews=7
    title: SynCamMaster: Synchronizing Multi-Camera Video Generation from Diverse Viewpoints
    pdf: research_data\iclr\text-to-video\pdfs\SynCamMaster__Synchronizing_Multi-Camera_Video_Generation_from_Diverse_Viewpoint.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=m8Rk3HLGFx

[89] rating=5.8 | decision=Accept (Poster) | reviews=10
    title: Collaborative Video Diffusion: Consistent Multi-video Generation with Camera Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\arHJlYiY2J_reviews.json
    forum: https://openreview.net/forum?id=arHJlYiY2J

[90] rating=5.8 | decision=None | reviews=5
    title: ReconX: Reconstruct Any Scene from Sparse Views with Video Diffusion Model
    pdf: research_data\iclr\video-diffusion\pdfs\ReconX__Reconstruct_Any_Scene_from_Sparse_Views_with_Video_Diffusion_Model.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Z30Mdbv5jO

[91] rating=5.8 | decision=None | reviews=5
    title: Training-free Camera Control for Video Generation
    pdf: research_data\iclr\video-generation\pdfs\3D_Scene_Prompting_for_Scene-Consistent_Camera-Controllable_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=KI1zldOFz9

[92] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: Enhancing Motion in Text-to-Video Generation with Decomposed Encoding and Conditioning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\nkzSE5KkCA_reviews.json
    forum: https://openreview.net/forum?id=nkzSE5KkCA

[93] rating=5.8 | decision=None | reviews=4
    title: AVID: Adapting Video Diffusion Models to World Models
    pdf: research_data\iclr\image-to-video\pdfs\AVID__Adapting_Video_Diffusion_Models_to_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=15ASUbzg0N

[94] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: FreeLong: Training-Free Long Video Generation with SpectralBlend Temporal Attention
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\X9Fga52OOv_reviews.json
    forum: https://openreview.net/forum?id=X9Fga52OOv

[95] rating=5.8 | decision=None | reviews=4
    title: MM-LDM: Multi-Modal Latent Diffusion Model for Sounding Video Generation
    pdf: research_data\iclr\video-generation\pdfs\MM-LDM__Multi-Modal_Latent_Diffusion_Model_for_Sounding_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=XqLcFMMwNb

[96] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: Evaluation of Text-to-Video Generation Models: A Dynamics Perspective
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\tmX1AUmkl6_reviews.json
    forum: https://openreview.net/forum?id=tmX1AUmkl6

[97] rating=5.8 | decision=None | reviews=4
    title: Multi-Shot Character Consistency for Text-to-Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=0zRuk3QdiH

[98] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: FreeNoise: Tuning-Free Longer Video Diffusion via Noise Rescheduling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\ijoqFqSC7p_reviews.json
    forum: https://openreview.net/forum?id=ijoqFqSC7p

[99] rating=5.7 | decision=None | reviews=3
    title: Mora: Enabling Generalist Video Generation via A Multi-Agent Framework
    pdf: research_data\iclr\text-to-video\pdfs\Mora__Enabling_Generalist_Video_Generation_via_A_Multi-Agent_Framework.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=S7F7IMGX4O

[100] rating=5.7 | decision=Accept (Poster) | reviews=6
    title: NaRCan: Natural Refined Canonical Image with Integration of Diffusion Prior for Video Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\bCR2NLm1QW_reviews.json
    forum: https://openreview.net/forum?id=bCR2NLm1QW

[101] rating=5.7 | decision=Accept (Poster) | reviews=6
    title: Precipitation Downscaling with Spatiotemporal Video Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\hhnkH8ex5d_reviews.json
    forum: https://openreview.net/forum?id=hhnkH8ex5d

[102] rating=5.6 | decision=None | reviews=5
    title: Realistic-Gesture: Co-Speech Gesture Video Generation through Semantic-aware Gesture Representation
    pdf: research_data\iclr\video-generation\pdfs\Realistic-Gesture__Co-Speech_Gesture_Video_Generation_through_Semantic-aware_Ges.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=EXsiGFkwV6

[103] rating=5.6 | decision=None | reviews=5
    title: EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning
    pdf: research_data\iclr\video-generation\pdfs\EditVerse__Unifying_Image_and_Video_Editing_and_Generation_with_In-Context_Learn.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=blJXE07r7I

[104] rating=5.5 | decision=None | reviews=4
    title: Uniform Discrete Diffusion with Metric Path for Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=GFU5yCbILk

[105] rating=5.5 | decision=None | reviews=4
    title: Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems
    pdf: research_data\iclr\sora-related\pdfs\Stop_Wasting_Your_Tokens__Towards_Efficient_Runtime_Multi-Agent_Systems.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=pzFhtpkabh

[106] rating=5.5 | decision=None | reviews=4
    title: BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching
    pdf: research_data\iclr\video-generation\pdfs\Accelerating_Diffusion_Transformers_with_Token-wise_Feature_Caching.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=5bJZtzTFYy

[107] rating=5.5 | decision=None | reviews=4
    title: MVCustom: Multi-View Customized Diffusion via Geometric Latent Rendering and Completion
    pdf: research_data\iclr\text-to-video\pdfs\MVCustom__Multi-View_Customized_Diffusion_via_Geometric_Latent_Rendering_and_Com.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=SGsxxbAjXH

[108] rating=5.5 | decision=None | reviews=4
    title: MotionStream: Real-Time Video Generation with Interactive Motion Controls
    pdf: research_data\iclr\text-to-video\pdfs\MotionStream__Real-Time_Video_Generation_with_Interactive_Motion_Controls.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=v1DKz5Vxr7

[109] rating=5.5 | decision=Accept (Poster) | reviews=8
    title: COVE: Unleashing the Diffusion Feature Correspondence for Consistent Video Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\474M9aeI4U_reviews.json
    forum: https://openreview.net/forum?id=474M9aeI4U

[110] rating=5.5 | decision=None | reviews=4
    title: AdaViewPlanner: Adapting Video Diffusion Models for Viewpoint Planning in 4D Scenes
    pdf: research_data\iclr\text-to-video\pdfs\AdaViewPlanner__Adapting_Video_Diffusion_Models_for_Viewpoint_Planning_in_4D_Sce.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=c2EfS9E5CJ

[111] rating=5.5 | decision=None | reviews=4
    title: How Confident are Video Models? Empowering Video Models to Express their Uncertainty
    pdf: research_data\iclr\text-to-video\pdfs\How_Confident_are_Video_Models__Empowering_Video_Models_to_Express_their_Uncerta.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=bRVJcc89Em

[112] rating=5.5 | decision=None | reviews=4
    title: SEINE: Short-to-Long Video Diffusion Model for Generative Transition and Prediction
    pdf: research_data\iclr\image-to-video\pdfs\SEINE__Short-to-Long_Video_Diffusion_Model_for_Generative_Transition_and_Predict.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=FNq3nIvP4F

[113] rating=5.5 | decision=None | reviews=4
    title: Improved Quality, Synchrony, and Preference Alignment for Joint Audio-Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Improved_Quality,_Synchrony,_and_Preference_Alignment_for_Joint_Audio-Video_Gene.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=hRRWfFpKRp

[114] rating=5.5 | decision=None | reviews=4
    title: TTOM: Test-Time Optimization and Memorization for Compositional Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=wqCwcTZsrv

[115] rating=5.5 | decision=None | reviews=4
    title: QuantSparse: Comprehensively Compressing Video Diffusion Transformer with Model Quantization and Attention Sparsification
    pdf: research_data\iclr\video-generation\pdfs\QuantSparse__Comprehensively_Compressing_Video_Diffusion_Transformer_with_Model.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=4TAG3aQljJ

[116] rating=5.5 | decision=None | reviews=4
    title: CameraNoise: Learning Precise Camera Control with Video Diffusion in Noise Space
    pdf: research_data\iclr\video-generation\pdfs\CameraNoise__Learning_Precise_Camera_Control_with_Video_Diffusion_in_Noise_Space.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=TT3gmYaqyc

[117] rating=5.5 | decision=None | reviews=4
    title: PreciseCache: Precise Feature Caching for Efficient and High-fidelity Video Generation
    pdf: research_data\iclr\video-generation\pdfs\PreciseCache__Precise_Feature_Caching_for_Efficient_and_High-fidelity_Video_Gene.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=DjfRkr82jn

[118] rating=5.5 | decision=None | reviews=4
    title: CamI2V: Camera-Controlled Image-to-Video Diffusion Model
    pdf: research_data\iclr\image-to-video\pdfs\CamI2V__Camera-Controlled_Image-to-Video_Diffusion_Model.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=dIZB7jeSUv

[119] rating=5.5 | decision=None | reviews=4
    title: MIMIC: Mask-Injected Manipulation Video Generation with Interaction Control
    pdf: research_data\iclr\image-to-video\pdfs\MIMIC__Mask-Injected_Manipulation_Video_Generation_with_Interaction_Control.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=COrUdVuInH

[120] rating=5.5 | decision=None | reviews=4
    title: Improving Autoregressive Video Modeling with History Understanding
    pdf: research_data\iclr\video-generation\pdfs\Improving_Autoregressive_Video_Modeling_with_History_Understanding.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=kd2V5Bkw1D

[121] rating=5.5 | decision=None | reviews=4
    title: I4VGen: Image as Free Stepping Stone for Text-to-Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=PKAZzhcIrP

[122] rating=5.5 | decision=Accept | reviews=4
    title: Time-to-Move: Training-Free Motion-Controlled Video Generation via Dual-Clock Denoising
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\OxO9OSYVw5_reviews.json
    forum: https://openreview.net/forum?id=OxO9OSYVw5

[123] rating=5.5 | decision=Accept | reviews=4
    title: Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Generation on the Edge
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\9f3Nukn6BA_reviews.json
    forum: https://openreview.net/forum?id=9f3Nukn6BA

[124] rating=5.5 | decision=None | reviews=4
    title: MarDini: Masked Autoregressive Diffusion for Video Generation at Scale
    pdf: research_data\iclr\image-to-video\pdfs\MarDini__Masked_Autoregressive_Diffusion_for_Video_Generation_at_Scale.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=YJwnlplKQ7

[125] rating=5.5 | decision=None | reviews=4
    title: DreamSwapV: Mask-guided Subject Swapping for Any Customized Video Editing
    pdf: research_data\iclr\video-generation\pdfs\DreamSwapV__Mask-guided_Subject_Swapping_for_Any_Customized_Video_Editing.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=xH0pSRWbFi

[126] rating=5.5 | decision=None | reviews=4
    title: Dual-IPO: Dual-Iterative Preference Optimization for Text-to-Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=mu8sO1Vw0C

[127] rating=5.5 | decision=None | reviews=4
    title: VMoBA: Mixture-of-Block Attention for Video Diffusion Models
    pdf: research_data\iclr\video-generation\pdfs\Mixture_of_Contexts_for_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=oQaRElUdmh

[128] rating=5.5 | decision=None | reviews=4
    title: Adaptive Caching for Faster Video Generation with Diffusion Transformers
    pdf: research_data\iclr\video-generation\pdfs\Adaptive_Caching_for_Faster_Video_Generation_with_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=DyyLUUVXJ5

[129] rating=5.5 | decision=Accept | reviews=4
    title: MoSA: Motion-Coherent Human Video Generation via Structure-Appearance Decoupling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\JKIa2rTxdB_reviews.json
    forum: https://openreview.net/forum?id=JKIa2rTxdB

[130] rating=5.5 | decision=None | reviews=4
    title: Semantically Consistent Video Inpainting with Conditional Diffusion Models
    pdf: research_data\iclr\video-diffusion\pdfs\Diffusion_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=h7fZvaU93L

[131] rating=5.5 | decision=Reject | reviews=4
    title: MotionDirector: Motion Customization of Text-to-Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\xIdIHRUn9t_reviews.json
    forum: https://openreview.net/forum?id=xIdIHRUn9t

[132] rating=5.5 | decision=None | reviews=4
    title: Trajectory-aware Shifted State Space Models for Online Video Super-Resolution
    pdf: research_data\iclr\video-super-resolution\pdfs\Trajectory-aware_Shifted_State_Space_Models_for_Online_Video_Super-Resolution.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=RygnSGcV49

[133] rating=5.5 | decision=None | reviews=4
    title: IVEBench: Modern Benchmark Suite for Instruction-Guided Video Editing Assessment
    pdf: research_data\iclr\video-editing\pdfs\IVEBench__Modern_Benchmark_Suite_for_Instruction-Guided_Video_Editing_Assessment.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=n0wVbCxcob

[134] rating=5.5 | decision=None | reviews=4
    title: $PhyWorldBench$: A Comprehensive Evaluation of Physical Realism in Text-to-Video Models
    pdf: research_data\iclr\text-to-video\pdfs\$PhyWorldBench$__A_Comprehensive_Evaluation_of_Physical_Realism_in_Text-to-Video.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rlZeILv3fm

[135] rating=5.5 | decision=None | reviews=4
    title: Streaming Autoregressive Video Generation via Diagonal Distillation
    pdf: research_data\iclr\video-generation\pdfs\Streaming_Autoregressive_Video_Generation_via_Diagonal_Distillation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=X7YW6STzeL

[136] rating=5.5 | decision=None | reviews=4
    title: Controllable First-Frame-Guided Video Editing via Mask-Aware LoRA Fine-Tuning
    pdf: research_data\iclr\image-to-video\pdfs\Controllable_First-Frame-Guided_Video_Editing_via_Mask-Aware_LoRA_Fine-Tuning.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=xkRMJ1Y7Um

[137] rating=5.5 | decision=None | reviews=4
    title: AdaFlow: Efficient Long Video Editing via Adaptive Attention Slimming And Keyframe Selection
    pdf: research_data\iclr\video-editing\pdfs\AdaFlow__Efficient_Long_Video_Editing_via_Adaptive_Attention_Slimming_And_Keyfra.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=yP0iKsinmk

[138] rating=5.5 | decision=None | reviews=4
    title: Many-for-Many: Unify the Training of Multiple Video and Image Generation and Manipulation Tasks
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=cKZw9ycVHy

[139] rating=5.5 | decision=Accept (Poster) | reviews=8
    title: OmniTokenizer: A Joint Image-Video Tokenizer for Visual Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\H6C4p8Dir7_reviews.json
    forum: https://openreview.net/forum?id=H6C4p8Dir7

[140] rating=5.5 | decision=None | reviews=4
    title: Jailbreaking on Text-to-Video Models via Scene Splitting Strategy
    pdf: research_data\iclr\text-to-video\pdfs\Jailbreaking_on_Text-to-Video_Models_via_Scene_Splitting_Strategy.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=iFGFW3sF2M

[141] rating=5.5 | decision=Accept | reviews=4
    title: Flow Caching for Autoregressive Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\vko4DuhKbh_reviews.json
    forum: https://openreview.net/forum?id=vko4DuhKbh

[142] rating=5.5 | decision=None | reviews=4
    title: Boosting Camera Motion Control for Video Diffusion Transformers
    pdf: research_data\iclr\video-generation\pdfs\Boosting_Camera_Motion_Control_for_Video_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rDRCIvTppL

[143] rating=5.5 | decision=None | reviews=4
    title: ControlVideo: Training-free Controllable Text-to-video Generation
    pdf: research_data\iclr\text-to-video\pdfs\ControlVideo__Training-free_Controllable_Text-to-video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=5a79AqFr0c

[144] rating=5.5 | decision=None | reviews=4
    title: How Far Is Video Generation from World Model: A Physical Law Perspective
    pdf: research_data\iclr\video-generation\pdfs\How_Far_Is_Video_Generation_from_World_Model__A_Physical_Law_Perspective.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ZyLkNVHBZF

[145] rating=5.5 | decision=None | reviews=4
    title: LaVie: High-Quality Video Generation with Cascaded Latent Diffusion Models
    pdf: research_data\iclr\text-to-video\pdfs\Controlling_Video_Generation_with_Vision_Language_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=p09XyFxZkc

[146] rating=5.4 | decision=Accept (Poster) | reviews=10
    title: Animate3D: Animating Any 3D Model with Multi-view Video Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\HB6KaCFiMN_reviews.json
    forum: https://openreview.net/forum?id=HB6KaCFiMN

[147] rating=5.4 | decision=None | reviews=5
    title: OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving
    pdf: research_data\iclr\video-generation\pdfs\OccSora__4D_Occupancy_Generation_Models_as_World_Simulators_for_Autonomous_Drivi.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=XIFnghzusY

[148] rating=5.4 | decision=None | reviews=5
    title: Orator: LLM-Guided Multi-Shot Speech Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Orator__LLM-Guided_Multi-Shot_Speech_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Bz6eAiOjrI

[149] rating=5.4 | decision=None | reviews=5
    title: MAVIN: Multi-Action Video Generation with Diffusion Models via Transition Video Infilling
    pdf: research_data\iclr\video-generation\pdfs\MAVIN__Multi-Action_Video_Generation_with_Diffusion_Models_via_Transition_Video.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=IIDFStLGQx

[150] rating=5.3 | decision=None | reviews=3
    title: MoCa: Modeling Object Consistency for 3D Camera Control in Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=DZcpnudp7f

[151] rating=5.3 | decision=None | reviews=3
    title: SIGMark: Scalable In-Generation Watermark with Blind Extraction for Video Diffusion
    pdf: research_data\iclr\video-generation\pdfs\Adaptive_Caching_for_Faster_Video_Generation_with_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=tKyAD2LhnI

[152] rating=5.3 | decision=Reject | reviews=3
    title: DynVideo-E: Harnessing Dynamic NeRF for Large-Scale Motion- and View-Change Human-Centric Video Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\Z73ymB1C7G_reviews.json
    forum: https://openreview.net/forum?id=Z73ymB1C7G

[153] rating=5.3 | decision=Accept (Poster) | reviews=6
    title: Video Prediction Models as Rewards for Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\HWNl9PAYIP_reviews.json
    forum: https://openreview.net/forum?id=HWNl9PAYIP

[154] rating=5.3 | decision=None | reviews=3
    title: PuppetMaster: Scaling Interactive Video Generation as a Motion Prior for Part-Level Dynamics
    pdf: research_data\iclr\video-generation\pdfs\Motion_Inversion_for_Video_Customization.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=HCUksccuFx

[155] rating=5.3 | decision=None | reviews=3
    title: Paper2Video: Automatic Video Generation from Scientific Papers
    pdf: research_data\iclr\video-generation\pdfs\Paper2Video__Automatic_Video_Generation_from_Scientific_Papers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=omEK0fdKDD

[156] rating=5.3 | decision=Reject | reviews=3
    title: Improved Video VAE for Latent Video Diffusion Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\e5288Iu4Zc_reviews.json
    forum: https://openreview.net/forum?id=e5288Iu4Zc

[157] rating=5.3 | decision=None | reviews=6
    title: TPDiff: Temporal Pyramid Video Diffusion Model
    pdf: research_data\iclr\video-generation\pdfs\TPDiff__Temporal_Pyramid_Video_Diffusion_Model.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Eg3KqoI9tS

[158] rating=5.3 | decision=None | reviews=3
    title: Model Already Knows the Best Noise: Bayesian Active Noise Selection via Attention  in Video Diffusion Model
    pdf: research_data\iclr\text-to-video\pdfs\Model_Already_Knows_the_Best_Noise__Bayesian_Active_Noise_Selection_via_Attentio.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=11dzFZ2UM1

[159] rating=5.3 | decision=None | reviews=3
    title: Consistent Noisy Latent Rewards for Trajectory Preference Optimization in Diffusion Models
    pdf: research_data\iclr\text-to-video\pdfs\Consistent_Noisy_Latent_Rewards_for_Trajectory_Preference_Optimization_in_Diffus.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=qGihS60jfT

[160] rating=5.3 | decision=None | reviews=3
    title: Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening
    pdf: research_data\iclr\image-to-video\pdfs\Motion_Prior_Distillation_in_Time_Reversal_Sampling_for_Generative_Inbetweening.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=GRElsj9W2t

[161] rating=5.2 | decision=Reject | reviews=4
    title: VideoFactory: Swap Attention in Spatiotemporal Diffusions for Text-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\dUDwK38MVC_reviews.json
    forum: https://openreview.net/forum?id=dUDwK38MVC

[162] rating=5.2 | decision=None | reviews=4
    title: VersVideo: Leveraging Enhanced Temporal Diffusion Models for Versatile Video Generation
    pdf: research_data\iclr\video-generation\pdfs\IV-mixed_Sampler__Leveraging_Image_Diffusion_Models_for_Enhanced_Video_Synthesis.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=K9sVJ17zvB

[163] rating=5.2 | decision=Accept (Poster) | reviews=8
    title: Rethinking Human Evaluation Protocol for Text-to-Video Models: Enhancing Reliability, Reproducibility, and Practicality
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\0AwMciNShl_reviews.json
    forum: https://openreview.net/forum?id=0AwMciNShl

[164] rating=5.2 | decision=Accept (Poster) | reviews=4
    title: GLOBER: Coherent Non-autoregressive Video Generation via GLOBal Guided Video DecodER
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\TRbklCR2ZW_reviews.json
    forum: https://openreview.net/forum?id=TRbklCR2ZW

[165] rating=5.2 | decision=None | reviews=5
    title: Taming Diffusion Transformer for Efficient Mobile Video Generation in Seconds
    pdf: research_data\iclr\video-generation\pdfs\SANA-Video__Efficient_Video_Generation_with_Block_Linear_Diffusion_Transformer.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=fAVvvZq6Y2

[166] rating=5.2 | decision=Accept | reviews=5
    title: ViPRA: Video Prediction for Robot Actions
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\w3Ik8HUyTT_reviews.json
    forum: https://openreview.net/forum?id=w3Ik8HUyTT

[167] rating=5.2 | decision=Accept (Spotlight) | reviews=10
    title: MotionBooth: Motion-Aware Customized Text-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\1we1V3MAHD_reviews.json
    forum: https://openreview.net/forum?id=1we1V3MAHD

[168] rating=5.2 | decision=None | reviews=5
    title: Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=6rMHcLWxl4

[169] rating=5.2 | decision=None | reviews=5
    title: VEditBench: Holistic Benchmark for Text-Guided Video Editing
    pdf: research_data\iclr\video-editing\pdfs\IVEBench__Modern_Benchmark_Suite_for_Instruction-Guided_Video_Editing_Assessment.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=6325Jzc9eR

[170] rating=5.0 | decision=None | reviews=4
    title: Taming Flow-based I2V Models for Creative Video Editing
    pdf: research_data\iclr\image-to-video\pdfs\Taming_Flow-based_I2V_Models_for_Creative_Video_Editing.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ITvVX8jaOM

[171] rating=5.0 | decision=None | reviews=4
    title: SyncFlow: Temporally Aligned Joint Audio-Video Generation from Text
    pdf: research_data\iclr\video-generation\pdfs\SyncFlow__Temporally_Aligned_Joint_Audio-Video_Generation_from_Text.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=J2EmNMLoxv

[172] rating=5.0 | decision=Accept | reviews=4
    title: ReactID: Synchronizing Realistic Actions and Identity in Personalized Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\yn0Wu7NsTa_reviews.json
    forum: https://openreview.net/forum?id=yn0Wu7NsTa

[173] rating=5.0 | decision=Accept (Poster) | reviews=8
    title: Video Diffusion Models are Training-free Motion Interpreter and Controller
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\ZvQ4Bn75kN_reviews.json
    forum: https://openreview.net/forum?id=ZvQ4Bn75kN

[174] rating=5.0 | decision=None | reviews=4
    title: PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion
    pdf: research_data\iclr\video-generation\pdfs\PanoWorld-X__Generating_Explorable_Panoramic_Worlds_via_Sphere-Aware_Video_Diffu.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=iZyBEbq6jR

[175] rating=5.0 | decision=None | reviews=4
    title: VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation
    pdf: research_data\iclr\video-generation\pdfs\VideoPhy-2__A_Challenging_Action-Centric_Physical_Commonsense_Evaluation_in_Vide.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=HA8KSQW7SO

[176] rating=5.0 | decision=Accept (Poster) | reviews=4
    title: SLA: Beyond Sparsity in Diffusion Transformers via Fine-Tunable Sparse-Linear Attention.
    pdf: research_data\authors\Ion_Stoica\pdfs\SLA__Beyond_Sparsity_in_Diffusion_Transformers_via_Fine-Tunable_Sparse-Linear_At.pdf
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\eD8IPvNoZB_reviews.json
    forum: https://openreview.net/forum?id=eD8IPvNoZB

[177] rating=5.0 | decision=None | reviews=4
    title: Rolling Forcing: Autoregressive Long Video Diffusion in Real Time
    pdf: research_data\iclr\video-generation\pdfs\LongLive__Real-time_Interactive_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=IAyzXjbfwo

[178] rating=5.0 | decision=None | reviews=4
    title: Controllable Video Generation with Provable Disentanglement
    pdf: research_data\iclr\video-generation\pdfs\Controllable_Video_Generation_with_Provable_Disentanglement.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=OcLNKpcY4J

[179] rating=5.0 | decision=None | reviews=4
    title: ASTRAEA: A Token-wise Acceleration Framework for Video Diffusion Transformers
    pdf: research_data\iclr\text-to-video\pdfs\ASTRAEA__A_Token-wise_Acceleration_Framework_for_Video_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=e8P4Oo8S6U

[180] rating=5.0 | decision=Reject | reviews=4
    title: Marrying Pixel and Latent Diffusion Models for Text-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\lSYPdXPuD9_reviews.json
    forum: https://openreview.net/forum?id=lSYPdXPuD9

[181] rating=5.0 | decision=None | reviews=4
    title: UltraViCo: Breaking Extrapolation Limits in Video Diffusion Transformers
    pdf: research_data\iclr\video-generation\pdfs\UltraViCo__Breaking_Extrapolation_Limits_in_Video_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=fLLCmC53u9

[182] rating=5.0 | decision=None | reviews=4
    title: Anchor Frame Bridging for Coherent First-Last Frame Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Anchor_Frame_Bridging_for_Coherent_First-Last_Frame_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=isNjWnVsUR

[183] rating=5.0 | decision=None | reviews=4
    title: RelightMaster: Precise Video Relighting with Multi-plane Light Images
    pdf: research_data\iclr\text-to-video\pdfs\RelightMaster__Precise_Video_Relighting_with_Multi-plane_Light_Images.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=CwVv9Yfq5e

[184] rating=5.0 | decision=None | reviews=4
    title: A Multi-In-Single-Out Network for Video Frame Interpolation without optical flow
    pdf: research_data\iclr\video-generation\pdfs\A_Multi-In-Single-Out_Network_for_Video_Frame_Interpolation_without_optical_flow.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=6HwamHLDa6

[185] rating=5.0 | decision=None | reviews=4
    title: GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video Diffusion Priors
    pdf: research_data\iclr\video-diffusion\pdfs\GSFixer__Improving_3D_Gaussian_Splatting_with_Reference-Guided_Video_Diffusion_P.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=B92Lzl1b3j

[186] rating=5.0 | decision=None | reviews=4
    title: JDM: Joint Distribution Modeling for Fine-Grained Text-to-Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Ug8NyyagOw

[187] rating=5.0 | decision=None | reviews=4
    title: We'll Fix it in Post: Improving Text-to-Video Generation with Zero Training
    pdf: research_data\iclr\text-to-video\pdfs\ControlVideo__Training-free_Controllable_Text-to-video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ifJ91JSLhq

[188] rating=5.0 | decision=Accept | reviews=4
    title: Split Happens (But Your Video Model Can Be Edited)
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\YqoFFNYKYB_reviews.json
    forum: https://openreview.net/forum?id=YqoFFNYKYB

[189] rating=5.0 | decision=None | reviews=4
    title: Weakly Supervised Motion Learning for Co-speech Gesture Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Motion_Inversion_for_Video_Customization.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=KZKQ8Iifab

[190] rating=5.0 | decision=None | reviews=3
    title: LEO: Generative Latent Image Animator for Human Video Synthesis
    pdf: research_data\iclr\video-generation\pdfs\LEO__Generative_Latent_Image_Animator_for_Human_Video_Synthesis.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=9zHxXaYEgw

[191] rating=5.0 | decision=None | reviews=4
    title: Real-Time Motion-Controllable Autoregressive Video Diffusion
    pdf: research_data\iclr\text-to-video\pdfs\MotionStream__Real-Time_Video_Generation_with_Interactive_Motion_Controls.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=4Q55RwYte9

[192] rating=5.0 | decision=Accept (Poster) | reviews=8
    title: SeeClear: Semantic Distillation Enhances Pixel Condensation for Video Super-Resolution
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\zeaBrGv7Ll_reviews.json
    forum: https://openreview.net/forum?id=zeaBrGv7Ll

[193] rating=5.0 | decision=Reject | reviews=4
    title: TGT: Text-Grounded Trajectories for Locally Controlled Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qUwOlwao20_reviews.json
    forum: https://openreview.net/forum?id=qUwOlwao20

[194] rating=5.0 | decision=None | reviews=4
    title: Generate Any Scene: Scene Graph Driven Data Synthesis for Visual Generation Training
    pdf: research_data\iclr\text-to-video\pdfs\Generate_Any_Scene__Scene_Graph_Driven_Data_Synthesis_for_Visual_Generation_Trai.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=EwdWR6lfvW

[195] rating=5.0 | decision=None | reviews=4
    title: Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective
    pdf: research_data\iclr\video-generation\pdfs\Lumos-1__On_Autoregressive_Video_Generation_with_Discrete_Diffusion_from_a_Unifi.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=wWAxwSCKR2

[196] rating=5.0 | decision=None | reviews=4
    title: InfVSR: Breaking Length Limits of Generic Video Super-Resolution
    pdf: research_data\iclr\video-diffusion\pdfs\InfVSR__Breaking_Length_Limits_of_Generic_Video_Super-Resolution.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=fZi8HxJbMO

[197] rating=5.0 | decision=None | reviews=4
    title: Macro-from-Micro Planning for High-Quality and Parallelized Autoregressive Long Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Macro-from-Micro_Planning_for_High-Quality_and_Parallelized_Autoregressive_Long.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nY8looE4lO

[198] rating=5.0 | decision=Accept | reviews=4
    title: Frame Guidance: Training-Free Guidance for Frame-Level Control in Video Diffusion Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\y39XbEp1vK_reviews.json
    forum: https://openreview.net/forum?id=y39XbEp1vK

[199] rating=5.0 | decision=None | reviews=4
    title: Kaleido: Open-Sourced Multi-Subject Reference Video Generation Model
    pdf: research_data\iclr\video-generation\pdfs\Kaleido__Open-Sourced_Multi-Subject_Reference_Video_Generation_Model.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=l8PM2RukoP

[200] rating=5.0 | decision=None | reviews=4
    title: Controllable Video Synthesis via Variational Inference
    pdf: research_data\iclr\video-generation\pdfs\Controllable_Video_Synthesis_via_Variational_Inference.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=hyJV4HYCnw

[201] rating=5.0 | decision=None | reviews=4
    title: VEnhancer: Generative Space-Time Enhancement for Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Ysdo3fyD4Q

[202] rating=5.0 | decision=Reject | reviews=4
    title: Region-wise Motion Controller for Image-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\LnN5UdhcjT_reviews.json
    forum: https://openreview.net/forum?id=LnN5UdhcjT

[203] rating=5.0 | decision=None | reviews=3
    title: LOVECon: Text-driven Training-free Long Video Editing with ControlNet
    pdf: research_data\iclr\video-editing\pdfs\LOVECon__Text-driven_Training-free_Long_Video_Editing_with_ControlNet.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=9ux2cgxw6O

[204] rating=5.0 | decision=None | reviews=4
    title: In-Context Learning with Unpaired Clips for Instruction-based Video Editing
    pdf: research_data\iclr\video-generation\pdfs\In-Context_Learning_with_Unpaired_Clips_for_Instruction-based_Video_Editing.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=5AXO7z4XLz

[205] rating=5.0 | decision=None | reviews=3
    title: Field-DiT: Diffusion Transformer on Unified Video, 3D, and Game Field Generation
    pdf: research_data\iclr\text-to-video\pdfs\Field-DiT__Diffusion_Transformer_on_Unified_Video,_3D,_and_Game_Field_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=w6YS9A78fq

[206] rating=5.0 | decision=None | reviews=5
    title: Text-Aware Diffusion Policies
    pdf: research_data\iclr\text-to-video\pdfs\Text-Aware_Diffusion_Policies.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=YhPUSofMgr

[207] rating=5.0 | decision=None | reviews=4
    title: UniVerse-1: Unified Audio-Video Generation via Stitching of Experts
    pdf: research_data\iclr\video-generation\pdfs\UniVerse-1__Unified_Audio-Video_Generation_via_Stitching_of_Experts.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=8aFYx2mDyE

[208] rating=5.0 | decision=None | reviews=4
    title: Character Mixing for Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\BachVid__Training-Free_Video_Generation_with_Consistent_Background_and_Character.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=SaBwaLcHNZ

[209] rating=5.0 | decision=Reject | reviews=3
    title: Efficient architectural aspects for text-to-video generation pipeline
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\JBLgjRRuHG_reviews.json
    forum: https://openreview.net/forum?id=JBLgjRRuHG

[210] rating=5.0 | decision=Accept | reviews=4
    title: Tex4D: Zero-shot 4D Scene Texturing with Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\0Lpz2o6NDE_reviews.json
    forum: https://openreview.net/forum?id=0Lpz2o6NDE

[211] rating=4.8 | decision=None | reviews=5
    title: Bidirectional Generative Retrieval with Multi-Modal LLMs for Text-Video Retrieval
    pdf: research_data\iclr\text-to-video\pdfs\Bidirectional_Generative_Retrieval_with_Multi-Modal_LLMs_for_Text-Video_Retrieva.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Opq0InLQn1

[212] rating=4.8 | decision=None | reviews=5
    title: CamCo: Camera-Controllable 3D-Consistent Image-to-Video Generation
    pdf: research_data\iclr\image-to-video\pdfs\CamCo__Camera-Controllable_3D-Consistent_Image-to-Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=BkJrXT3e5T

[213] rating=4.8 | decision=None | reviews=5
    title: H3AE: High Compression, High Speed, and High Quality AutoEncoder for Video Diffusion Models
    pdf: research_data\iclr\text-to-video\pdfs\H3AE__High_Compression,_High_Speed,_and_High_Quality_AutoEncoder_for_Video_Diffu.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=SRgCH8x2k2

[214] rating=4.8 | decision=Accept (Poster) | reviews=8
    title: 4Diffusion: Multi-view Video Diffusion Model for 4D Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\SFk7AMpyhx_reviews.json
    forum: https://openreview.net/forum?id=SFk7AMpyhx

[215] rating=4.8 | decision=None | reviews=4
    title: VideoAgent: Self-Improving Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Self-Forcing++__Towards_Minute-Scale_High-Quality_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=JaRihIHbZm

[216] rating=4.8 | decision=Accept (Poster) | reviews=11
    title: OmniTalker: One-shot Real-time Text-Driven Talking Audio-Video Generation With Multimodal Style Mimicking
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\eK31JidsTN_reviews.json
    forum: https://openreview.net/forum?id=eK31JidsTN

[217] rating=4.8 | decision=Reject | reviews=4
    title: VideoAlchemy: Open-set Personalization in Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\popKM1zAYa_reviews.json
    forum: https://openreview.net/forum?id=popKM1zAYa

[218] rating=4.8 | decision=Accept (Spotlight) | reviews=12
    title: Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\mSiN7i0BYH_reviews.json
    forum: https://openreview.net/forum?id=mSiN7i0BYH

[219] rating=4.8 | decision=Reject | reviews=4
    title: Video Generation Beyond a Single Clip
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\sYCrhXPVr1_reviews.json
    forum: https://openreview.net/forum?id=sYCrhXPVr1

[220] rating=4.8 | decision=None | reviews=4
    title: Continuous Space-Time Video Super-Resolution via Event Camera
    pdf: research_data\iclr\frame-interpolation\pdfs\Continuous_Space-Time_Video_Super-Resolution_via_Event_Camera.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=a8uJXdi7Df

[221] rating=4.8 | decision=Reject | reviews=4
    title: A Simple but Strong Baseline for Sounding Video Generation: Effective Adaptation of Audio and Video Diffusion Models for Joint Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\WqL4wOU3tw_reviews.json
    forum: https://openreview.net/forum?id=WqL4wOU3tw

[222] rating=4.8 | decision=Accept (Spotlight) | reviews=12
    title: Stable Part Diffusion 4D: Multi-View RGB and Kinematic Parts Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\I9F53Qlwur_reviews.json
    forum: https://openreview.net/forum?id=I9F53Qlwur

[223] rating=4.8 | decision=Accept (Poster) | reviews=12
    title: Surface-Aware Feed-Forward Quadratic Gaussian for Frame Interpolation with Large Motion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\c0c943R6ZJ_reviews.json
    forum: https://openreview.net/forum?id=c0c943R6ZJ

[224] rating=4.8 | decision=None | reviews=4
    title: LumiSculpt: A Consistency Lighting Control Network for Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=OW0uRFs51N

[225] rating=4.7 | decision=Reject | reviews=3
    title: A Reason-then-Describe Instruction Interpreter for Controllable Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ytowjGMISZ_reviews.json
    forum: https://openreview.net/forum?id=ytowjGMISZ

[226] rating=4.7 | decision=Reject | reviews=3
    title: Make it NoisEasier: Boosting Text-to-Video Generation with Direct Noise Optimization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\hSUlL8K1Ec_reviews.json
    forum: https://openreview.net/forum?id=hSUlL8K1Ec

[227] rating=4.7 | decision=Reject | reviews=3
    title: VIA: Unified Spatiotemporal Video Adaptation for Global and Local Video Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\mhFToLPjM5_reviews.json
    forum: https://openreview.net/forum?id=mhFToLPjM5

[228] rating=4.7 | decision=None | reviews=3
    title: StoryAgent: Customized Storytelling Video Generation via Multi-Agent Collaboration
    pdf: research_data\iclr\image-to-video\pdfs\StoryAgent__Customized_Storytelling_Video_Generation_via_Multi-Agent_Collaborati.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=TS4BLf951Y

[229] rating=4.7 | decision=Reject | reviews=3
    title: Live2Diff: Live Stream Translation via Uni-directional Attention in Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\YA1Ur2eGFl_reviews.json
    forum: https://openreview.net/forum?id=YA1Ur2eGFl

[230] rating=4.7 | decision=None | reviews=3
    title: Planning at Inference: MCTS Test-Time Scaling for Long Video Generation
    pdf: research_data\iclr\video-generation\pdfs\LongLive__Real-time_Interactive_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ilir6A52vh

[231] rating=4.7 | decision=Reject | reviews=3
    title: MEMO: Memory-Guided and Emotion-Aware Talking Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\CpgWRFqxhD_reviews.json
    forum: https://openreview.net/forum?id=CpgWRFqxhD

[232] rating=4.5 | decision=None | reviews=4
    title: On Equivariance and Fast Sampling in Video Diffusion Models Trained with Warped Noise
    pdf: research_data\iclr\video-generation\pdfs\Counting_Hallucinations_in_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=O5tuESInD0

[233] rating=4.5 | decision=Accept (Poster) | reviews=8
    title: Compositional 3D-aware Video Generation with LLM Director
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\oqdy2EFrja_reviews.json
    forum: https://openreview.net/forum?id=oqdy2EFrja

[234] rating=4.5 | decision=None | reviews=4
    title: OmniPainter: Global-Local Temporally Consistent Video Inpainting Diffusion Model
    pdf: research_data\iclr\video-inpainting\pdfs\OmniPainter__Global-Local_Temporally_Consistent_Video_Inpainting_Diffusion_Model.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=NMKVz3hQfz

[235] rating=4.5 | decision=Reject | reviews=4
    title: Interpreting Any Condition to Caption for Controllable Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\XoT51yzqz7_reviews.json
    forum: https://openreview.net/forum?id=XoT51yzqz7

[236] rating=4.5 | decision=None | reviews=4
    title: NeRV-Diffusion: Diffuse Implicit Neural Representation for Video Synthesis
    pdf: research_data\iclr\video-generation\pdfs\NeRV-Diffusion__Diffuse_Implicit_Neural_Representation_for_Video_Synthesis.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=tX0cSOvBnS

[237] rating=4.5 | decision=None | reviews=4
    title: SemCache:Adaptive Semantic-Aware Caching for Efficient Video Diffusion
    pdf: research_data\iclr\video-generation\pdfs\SemCache_Adaptive_Semantic-Aware_Caching_for_Efficient_Video_Diffusion.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=WyfmWX2ncn

[238] rating=4.5 | decision=None | reviews=4
    title: UniVAE: A Unified Frame-Enriched Video VAE for Latent Video Diffusion Models
    pdf: research_data\iclr\video-generation\pdfs\Target-Aware_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=hcvmYgFb2A

[239] rating=4.5 | decision=None | reviews=4
    title: DiTraj: Training-free Trajectory Control For Video Diffusion Transformer
    pdf: research_data\iclr\text-to-video\pdfs\DiTraj__Training-free_Trajectory_Control_For_Video_Diffusion_Transformer.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=zWRmev5IQ4

[240] rating=4.5 | decision=None | reviews=4
    title: CAT-VIDEO: CORRUPTION-AWARE TRAINING FOR ROBUST VIDEO DIFFUSION MODELS
    pdf: research_data\iclr\video-generation\pdfs\CAT-VIDEO__CORRUPTION-AWARE_TRAINING_FOR_ROBUST_VIDEO_DIFFUSION_MODELS.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=unZhwukf0T

[241] rating=4.5 | decision=Reject | reviews=4
    title: Fast Autoregressive Video Generation with Diagonal Decoding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\hMZbIIHMDI_reviews.json
    forum: https://openreview.net/forum?id=hMZbIIHMDI

[242] rating=4.5 | decision=None | reviews=4
    title: Compact Attention: Exploiting Structured Spatio-Temporal Sparsity for Fast Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Compact_Attention__Exploiting_Structured_Spatio-Temporal_Sparsity_for_Fast_Video.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=NLsUsrOIuh

[243] rating=4.5 | decision=Reject | reviews=4
    title: Training-free Long Video Generation with Chain of Diffusion Model Experts
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\3hc2ESNU6n_reviews.json
    forum: https://openreview.net/forum?id=3hc2ESNU6n

[244] rating=4.5 | decision=None | reviews=4
    title: Controlling Video Generation with Vision Language Models
    pdf: research_data\iclr\text-to-video\pdfs\Controlling_Video_Generation_with_Vision_Language_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=6SC61wyq8w

[245] rating=4.5 | decision=None | reviews=4
    title: Latent Reward-Guided Search for Faster Inference-Time Scaling in Video Diffusion
    pdf: research_data\iclr\video-generation\pdfs\Latent_Reward-Guided_Search_for_Faster_Inference-Time_Scaling_in_Video_Diffusion.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=i6SA9rGTAB

[246] rating=4.5 | decision=None | reviews=4
    title: Cosmos-Eval: Towards Explainable Evaluation of Physics and Semantics in Text-to-Video Models
    pdf: research_data\iclr\text-to-video\pdfs\$PhyWorldBench$__A_Comprehensive_Evaluation_of_Physical_Realism_in_Text-to-Video.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=KdYKSOY9MP

[247] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: ViDAR: Video Diffusion-Aware 4D Reconstruction From Monocular Inputs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\mLVqiNH0aA_reviews.json
    forum: https://openreview.net/forum?id=mLVqiNH0aA

[248] rating=4.5 | decision=Reject | reviews=4
    title: Camera Pose Estimation Emerging In Video Diffusion Transformer
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\lgf2LW7fOJ_reviews.json
    forum: https://openreview.net/forum?id=lgf2LW7fOJ

[249] rating=4.5 | decision=Accept (Poster) | reviews=11
    title: Force Prompting: Video Generation Models Can Learn And Generalize Physics-based Control Signals
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\eX5aXfJQZc_reviews.json
    forum: https://openreview.net/forum?id=eX5aXfJQZc

[250] rating=4.5 | decision=None | reviews=4
    title: LoCoT2V-Bench: A Benchmark for Long-Form and Complex Text-to-Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=YeWsA0VFZ5

[251] rating=4.5 | decision=Accept (Poster) | reviews=11
    title: Radial Attention: $\mathcal{O}(n\log n)$ Sparse Attention with Energy Decay for Long Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\hYovE4nHTt_reviews.json
    forum: https://openreview.net/forum?id=hYovE4nHTt

[252] rating=4.5 | decision=None | reviews=4
    title: Effortless Event-Augmented Latent Diffusion for Video Frame Interpolation
    pdf: research_data\iclr\image-to-video\pdfs\Effortless_Event-Augmented_Latent_Diffusion_for_Video_Frame_Interpolation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=DBHCRrdsfi

[253] rating=4.5 | decision=None | reviews=4
    title: VEBench: Towards Comprehensive and Automatic Evaluation for Text-guided Video Editing
    pdf: research_data\iclr\video-editing\pdfs\VEBench__Towards_Comprehensive_and_Automatic_Evaluation_for_Text-guided_Video_Ed.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nZNWrzDBHG

[254] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: VFRTok: Variable Frame Rates Video Tokenizer with Duration-Proportional Information Assumption
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\wk5B5W5OHo_reviews.json
    forum: https://openreview.net/forum?id=wk5B5W5OHo

[255] rating=4.5 | decision=None | reviews=4
    title: Video models are zero-shot learners and reasoners
    pdf: research_data\iclr\video-generation\pdfs\Video_models_are_zero-shot_learners_and_reasoners.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=MCWypEBtlF

[256] rating=4.5 | decision=None | reviews=4
    title: Enhancing Physical Plausibility in Video Generation by Reasoning the Implausibility
    pdf: research_data\iclr\video-generation\pdfs\Enhancing_Physical_Plausibility_in_Video_Generation_by_Reasoning_the_Implausibil.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=SYBfaOcbmw

[257] rating=4.5 | decision=None | reviews=4
    title: Implicit Semi-auto-regressive Image-to-Video Diffusion
    pdf: research_data\iclr\image-to-video\pdfs\Implicit_Semi-auto-regressive_Image-to-Video_Diffusion.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=BPdagk1mV7

[258] rating=4.5 | decision=Reject | reviews=4
    title: MMEval: Evaluating Video Generation Models for Motion Quality
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Vli7PVO60W_reviews.json
    forum: https://openreview.net/forum?id=Vli7PVO60W

[259] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Wan-Move: Motion-controllable Video Generation via Latent Trajectory Guidance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\lHW93LKaUk_reviews.json
    forum: https://openreview.net/forum?id=lHW93LKaUk

[260] rating=4.5 | decision=None | reviews=4
    title: Scaling Image and Video Generation via Test-Time Evolutionary Search
    pdf: research_data\iclr\video-generation\pdfs\Scaling_Image_and_Video_Generation_via_Test-Time_Evolutionary_Search.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=CFlOUNWsaP

[261] rating=4.5 | decision=Reject | reviews=4
    title: FlashVSR: Towards Real-time Diffusion-Based Streaming Video Super-Resolution
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\gzynHSyjUe_reviews.json
    forum: https://openreview.net/forum?id=gzynHSyjUe

[262] rating=4.5 | decision=None | reviews=4
    title: DVD-Quant: Data-free Video Diffusion Transformers Quantization
    pdf: research_data\iclr\video-generation\pdfs\DVD-Quant__Data-free_Video_Diffusion_Transformers_Quantization.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=3AnRMvlVDw

[263] rating=4.5 | decision=None | reviews=4
    title: Generating Human Motion Videos using a Cascaded Text-to-Video Framework
    pdf: research_data\iclr\text-to-video\pdfs\Generating_Human_Motion_Videos_using_a_Cascaded_Text-to-Video_Framework.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=XwHQMNUSZP

[264] rating=4.5 | decision=Reject | reviews=4
    title: Optimal Noise Pursuit for Augmenting Text-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\WVeUAbjx9p_reviews.json
    forum: https://openreview.net/forum?id=WVeUAbjx9p

[265] rating=4.5 | decision=Reject | reviews=4
    title: CamPilot: Improving Camera Control in Video Diffusion Model with Efficient Camera Reward Feedback
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qqij8fCGDl_reviews.json
    forum: https://openreview.net/forum?id=qqij8fCGDl

[266] rating=4.5 | decision=None | reviews=4
    title: Point Prompting: Counterfactual Tracking with Video Diffusion Models
    pdf: research_data\iclr\video-generation\pdfs\Point_Prompting__Counterfactual_Tracking_with_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=6FFQ007qLX

[267] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Controllable Human-centric Keyframe Interpolation with Generative Prior
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\OnViSNPqbT_reviews.json
    forum: https://openreview.net/forum?id=OnViSNPqbT

[268] rating=4.5 | decision=None | reviews=4
    title: Populate-A-Scene: Affordance-Aware Human Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Populate-A-Scene__Affordance-Aware_Human_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=hg0lpcHdWk

[269] rating=4.5 | decision=Accept | reviews=4
    title: Training-free Guidance in Text-to-Video Generation via Multimodal Planning and Structured Noise Initialization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1sNhPjqGub_reviews.json
    forum: https://openreview.net/forum?id=1sNhPjqGub

[270] rating=4.5 | decision=Accept | reviews=4
    title: GigaVideo-1: Advancing Video Generation via Automatic Feedback with 4 GPU-Hours Fine-Tuning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\y7wAuwErpL_reviews.json
    forum: https://openreview.net/forum?id=y7wAuwErpL

[271] rating=4.5 | decision=None | reviews=4
    title: UniMMVSR: A Unified Multi-Modal Framework for Cascaded Video Super-Resolution
    pdf: research_data\iclr\text-to-video\pdfs\UniMMVSR__A_Unified_Multi-Modal_Framework_for_Cascaded_Video_Super-Resolution.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=EbbCRpnOaC

[272] rating=4.5 | decision=None | reviews=4
    title: FaithfulFaces: Pose-Faithful Facial Identity Preservation for Text-to-Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=AnY0zJ8adz

[273] rating=4.5 | decision=None | reviews=4
    title: Syncphony: Synchronized Audio-to-Video Generation with Diffusion Transformers
    pdf: research_data\iclr\text-to-video\pdfs\Syncphony__Synchronized_Audio-to-Video_Generation_with_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=sG8dGZMaub

[274] rating=4.4 | decision=Reject | reviews=5
    title: The Devil is in the Word: Video-Conditioned Text Representation Refinement for Text-to-Video Retrieval
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\jOVJhKzc3Y_reviews.json
    forum: https://openreview.net/forum?id=jOVJhKzc3Y

[275] rating=4.4 | decision=Reject | reviews=5
    title: InnoAds: A Foundation Dataset and Benchmark for Advertising Visual Effects in Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\p6665QoG4B_reviews.json
    forum: https://openreview.net/forum?id=p6665QoG4B

[276] rating=4.4 | decision=Accept | reviews=5
    title: Spatially-Guided Temporal Attention (SGuTA) and Shifted-Cube Attention (SCubA) for Video Frame Interpolation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\LJ4CYEagg3_reviews.json
    forum: https://openreview.net/forum?id=LJ4CYEagg3

[277] rating=4.4 | decision=None | reviews=5
    title: Unveiling Temporal Telltales: Are Unconditional Video Generation Models Implicitly Encoding Temporal Information?
    pdf: research_data\iclr\video-generation\pdfs\Unveiling_Temporal_Telltales__Are_Unconditional_Video_Generation_Models_Implicit.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=p6UwN2Rxhx

[278] rating=4.3 | decision=Reject | reviews=3
    title: The Blessing of Smooth Initialization for Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\QIp1YUqgCB_reviews.json
    forum: https://openreview.net/forum?id=QIp1YUqgCB

[279] rating=4.3 | decision=Reject | reviews=3
    title: X-PlugVid: Versatile Adaptation of Image Plugins for Controllable Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\TTWxMAwS6n_reviews.json
    forum: https://openreview.net/forum?id=TTWxMAwS6n

[280] rating=4.3 | decision=Accept (Poster) | reviews=9
    title: Faster Video Diffusion with Trainable Sparse Attention
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\VrYCLQ5inI_reviews.json
    forum: https://openreview.net/forum?id=VrYCLQ5inI

[281] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: PanoWan: Lifting Diffusion Video Generation Models to 360$^\circ$ with Latitude/Longitude-aware Mechanisms
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\7VLxvVEtHh_reviews.json
    forum: https://openreview.net/forum?id=7VLxvVEtHh

[282] rating=4.2 | decision=Accept (Poster) | reviews=10
    title: Stable Cinemetrics : Structured Taxonomy and Evaluation for Professional Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\JzOZkxa8Wd_reviews.json
    forum: https://openreview.net/forum?id=JzOZkxa8Wd

[283] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: Audio-Sync Video Generation with Multi-Stream Temporal Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\12z8KLMQJD_reviews.json
    forum: https://openreview.net/forum?id=12z8KLMQJD

[284] rating=4.2 | decision=Accept (Spotlight) | reviews=12
    title: LeMiCa: Lexicographic Minimax Path Caching for Efficient Diffusion-Based Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\QIXdI207nq_reviews.json
    forum: https://openreview.net/forum?id=QIXdI207nq

[285] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: Frame In-N-Out: Unbounded Controllable Image-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\noiiyIk3hh_reviews.json
    forum: https://openreview.net/forum?id=noiiyIk3hh

[286] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: PolyVivid: Vivid Multi-Subject Video Generation with Cross-Modal Interaction and Enhancement
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\plrg87MP0F_reviews.json
    forum: https://openreview.net/forum?id=plrg87MP0F

[287] rating=4.2 | decision=Reject | reviews=4
    title: Video-Infinity: Distributed Long Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\DxT3e2f1jc_reviews.json
    forum: https://openreview.net/forum?id=DxT3e2f1jc

[288] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: VORTA: Efficient Video Diffusion via Routing Sparse Attention
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\gY9yOGYB48_reviews.json
    forum: https://openreview.net/forum?id=gY9yOGYB48

[289] rating=4.2 | decision=Reject | reviews=4
    title: Video Super-Resolution Transformer with Masked Inter&Intra-Frame Attention
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\ZGBOfAQrMl_reviews.json
    forum: https://openreview.net/forum?id=ZGBOfAQrMl

[290] rating=4.2 | decision=Accept (Poster) | reviews=10
    title: Imagine360: Immersive 360 Video Generation from Perspective Anchor
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\BcYfsMMpV1_reviews.json
    forum: https://openreview.net/forum?id=BcYfsMMpV1

[291] rating=4.2 | decision=Reject | reviews=5
    title: ETC: Towards Training-Efficient Video Synthesis with Exploiting Temporal Capabilities of Spatial Attention
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\0lVQBMhsPG_reviews.json
    forum: https://openreview.net/forum?id=0lVQBMhsPG

[292] rating=4.2 | decision=Accept (Poster) | reviews=15
    title: Let Them Talk: Audio-Driven Multi-Person Conversational Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\1aCYFQRvtz_reviews.json
    forum: https://openreview.net/forum?id=1aCYFQRvtz

[293] rating=4.2 | decision=Reject | reviews=5
    title: Self-Conditioned Diffusion Model for Consistent Human Image and Video Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\1fC4ytCAgb_reviews.json
    forum: https://openreview.net/forum?id=1fC4ytCAgb

[294] rating=4.0 | decision=Reject | reviews=4
    title: LightMotion: A Light and Tuning-free Method for Simulating Camera Motion in Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\SlqE2mfITO_reviews.json
    forum: https://openreview.net/forum?id=SlqE2mfITO

[295] rating=4.0 | decision=None | reviews=4
    title: Epipolar Geometry Improves Video Generation Models
    pdf: research_data\iclr\video-generation\pdfs\Epipolar_Geometry_Improves_Video_Generation_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=MDulpv6NRF

[296] rating=4.0 | decision=Reject | reviews=4
    title: Ditto: Scaling Instruction-Based Video Editing with a High-Quality Synthetic Dataset
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qUJZX8LwMp_reviews.json
    forum: https://openreview.net/forum?id=qUJZX8LwMp

[297] rating=4.0 | decision=Reject | reviews=4
    title: Omnicam: Unified Multimodal Video Generation via camera Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\V7dKmfdtGh_reviews.json
    forum: https://openreview.net/forum?id=V7dKmfdtGh

[298] rating=4.0 | decision=Accept (Poster) | reviews=11
    title: VideoREPA: Learning Physics for Video Generation through Relational Alignment with Foundation Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\oHjLfABsK4_reviews.json
    forum: https://openreview.net/forum?id=oHjLfABsK4

[299] rating=4.0 | decision=Accept (Poster) | reviews=12
    title: Aligning What Matters: Masked Latent Adaptation for Text-to-Audio-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\I0hRN2HMeH_reviews.json
    forum: https://openreview.net/forum?id=I0hRN2HMeH

[300] rating=4.0 | decision=Reject | reviews=4
    title: Video Diffusion Models Learn the Structure of the Dynamic World
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\SIZhZrU41O_reviews.json
    forum: https://openreview.net/forum?id=SIZhZrU41O

[301] rating=4.0 | decision=None | reviews=4
    title: Arbitrary Generative Video Interpolation
    pdf: research_data\iclr\video-generation\pdfs\Arbitrary_Generative_Video_Interpolation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=eKGkb4cFRe

[302] rating=4.0 | decision=Reject | reviews=4
    title: CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal Reconstruction Model for Autonomous Driving
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\V66pMNOVC2_reviews.json
    forum: https://openreview.net/forum?id=V66pMNOVC2

[303] rating=4.0 | decision=Reject | reviews=3
    title: ReGen4AD: Retrieval Based Online Video Generation for Reactive Autonomous Driving Simulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KRQZvECXpN_reviews.json
    forum: https://openreview.net/forum?id=KRQZvECXpN

[304] rating=4.0 | decision=None | reviews=4
    title: MoB: Mixture of Block Transformer for Accelerating Video Generation with Dynamic Routing
    pdf: research_data\iclr\video-generation\pdfs\Mixture_of_Contexts_for_Long_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=TTaAacQEdg

[305] rating=4.0 | decision=None | reviews=3
    title: Ovi: Twin Backbone Cross-Modal Fusion for Audio-Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Ovi__Twin_Backbone_Cross-Modal_Fusion_for_Audio-Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nIrF8xF0uN

[306] rating=4.0 | decision=Reject | reviews=4
    title: Zero4D: Training-Free 4D Video Generation From Single Video Using Off-the-Shelf Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\C0yjXQ1iGG_reviews.json
    forum: https://openreview.net/forum?id=C0yjXQ1iGG

[307] rating=4.0 | decision=Reject | reviews=4
    title: Autoregressive Video Generation beyond Next Frames Prediction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ao9uctmk1N_reviews.json
    forum: https://openreview.net/forum?id=ao9uctmk1N

[308] rating=4.0 | decision=Reject | reviews=4
    title: UI2V-Bench: An Understanding-based Image-to-video Generation Benchmark
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\hR39xH7rm3_reviews.json
    forum: https://openreview.net/forum?id=hR39xH7rm3

[309] rating=4.0 | decision=None | reviews=4
    title: FrameBridge: Improving Image-to-Video Generation with Bridge Models
    pdf: research_data\iclr\text-to-video\pdfs\Controlling_Video_Generation_with_Vision_Language_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=oOQavkQLQZ

[310] rating=4.0 | decision=Accept (Poster) | reviews=12
    title: VideoMAR: Autoregressive Video Generation with Continuous Tokens
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\iG4UNfUn0r_reviews.json
    forum: https://openreview.net/forum?id=iG4UNfUn0r

[311] rating=4.0 | decision=Reject | reviews=4
    title: ID-Composer: Multi-Subject Video Synthesis with Hierarchical Identity Preservation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\wLMEtQ5wBa_reviews.json
    forum: https://openreview.net/forum?id=wLMEtQ5wBa

[312] rating=4.0 | decision=Reject | reviews=4
    title: Reuse and Diffuse: Iterative Denoising for Text-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\qGZTrj48Lb_reviews.json
    forum: https://openreview.net/forum?id=qGZTrj48Lb

[313] rating=4.0 | decision=Accept | reviews=4
    title: Mitigating Surgical Data Imbalance with Dual-Prediction Video Diffusion Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\9OKxaCRPjD_reviews.json
    forum: https://openreview.net/forum?id=9OKxaCRPjD

[314] rating=4.0 | decision=None | reviews=4
    title: Vidar: Embodied Video Diffusion Model for Generalist Manipulation
    pdf: research_data\iclr\video-diffusion\pdfs\Vidar__Embodied_Video_Diffusion_Model_for_Generalist_Manipulation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=CFuNu8dK4s

[315] rating=4.0 | decision=Reject | reviews=4
    title: VideoDirectorGPT: Consistent Multi-Scene Video Generation via LLM-Guided Planning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\5PkgaUwiY0_reviews.json
    forum: https://openreview.net/forum?id=5PkgaUwiY0

[316] rating=4.0 | decision=Reject | reviews=4
    title: Progressive Autoregressive Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\WSze9IIN3d_reviews.json
    forum: https://openreview.net/forum?id=WSze9IIN3d

[317] rating=4.0 | decision=Reject | reviews=5
    title: Reasoning Diffusion for Unpaired Text-Image to Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\uqttsSVZbT_reviews.json
    forum: https://openreview.net/forum?id=uqttsSVZbT

[318] rating=4.0 | decision=None | reviews=4
    title: GenCoGS: Generative Completion-based 3D Gaussian Splatting for High-Fidelity Few-Shot Novel View Synthesis
    pdf: research_data\iclr\image-to-video\pdfs\GenCoGS__Generative_Completion-based_3D_Gaussian_Splatting_for_High-Fidelity_Few.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=piylyBPSau

[319] rating=4.0 | decision=None | reviews=4
    title: CoMo: Compositional Motion Customization  for Text-to-Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=FPpIE5lCCM

[320] rating=4.0 | decision=Reject | reviews=4
    title: MOTIONFLOW:Learning Implicit Motion Flow for Complex Camera Trajectory Control in Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\OBTmkKBmQW_reviews.json
    forum: https://openreview.net/forum?id=OBTmkKBmQW

[321] rating=4.0 | decision=Reject | reviews=4
    title: DreamActor-M2: Unleashing Pre-trained Video Models for Universal Character Image Animation via In-Context Fine-tuning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\IIBeaZNQaY_reviews.json
    forum: https://openreview.net/forum?id=IIBeaZNQaY

[322] rating=4.0 | decision=None | reviews=4
    title: SRDiffusion: Accelerate Diffusion Inference via Sketching-Rendering Cooperation
    pdf: research_data\iclr\text-to-video\pdfs\SRDiffusion__Accelerate_Diffusion_Inference_via_Sketching-Rendering_Cooperation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nRpWcxwYvC

[323] rating=4.0 | decision=None | reviews=5
    title: Shaping a Stabilized Video by Mitigating Unintended Changes for Concept-Augmented Video Editing
    pdf: research_data\iclr\video-editing\pdfs\Shaping_a_Stabilized_Video_by_Mitigating_Unintended_Changes_for_Concept-Augmente.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=CxS8mlkOH7

[324] rating=4.0 | decision=Reject | reviews=4
    title: LAVITA: Latent Video Diffusion Models with Spatio-temporal Transformers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\G2LsKEOs5k_reviews.json
    forum: https://openreview.net/forum?id=G2LsKEOs5k

[325] rating=4.0 | decision=Reject | reviews=4
    title: UniVid: The Open-Source Unified Video Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Poi2sv1K8n_reviews.json
    forum: https://openreview.net/forum?id=Poi2sv1K8n

[326] rating=4.0 | decision=Reject | reviews=4
    title: Image-driven Video Editing with Latent Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\FHhj5d2gYe_reviews.json
    forum: https://openreview.net/forum?id=FHhj5d2gYe

[327] rating=4.0 | decision=Reject | reviews=3
    title: BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ZGWwV34Vmu_reviews.json
    forum: https://openreview.net/forum?id=ZGWwV34Vmu

[328] rating=4.0 | decision=Reject | reviews=4
    title: FlashI2V: Fourier-Guided Latent Shifting Prevents Conditional Image Leakage in Image-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\9pVOX5UcBV_reviews.json
    forum: https://openreview.net/forum?id=9pVOX5UcBV

[329] rating=4.0 | decision=None | reviews=5
    title: BIGFIX: BIDIRECTIONAL IMAGE GENERATION WITH TOKEN FIXING
    pdf: research_data\iclr\image-to-video\pdfs\BIGFIX__BIDIRECTIONAL_IMAGE_GENERATION_WITH_TOKEN_FIXING.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=YCG9k9C059

[330] rating=4.0 | decision=None | reviews=4
    title: Evaluating Intuitive Physics Understanding in Video Diffusion Models via Likelihood Preference
    pdf: research_data\iclr\video-diffusion\pdfs\Diffusion_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=6UJf6B8RZ8

[331] rating=4.0 | decision=Reject | reviews=4
    title: GuideEdit: Enhancing Face Video Editing with Fine-grained Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\gWOANrFJ0t_reviews.json
    forum: https://openreview.net/forum?id=gWOANrFJ0t

[332] rating=4.0 | decision=Accept (Poster) | reviews=11
    title: GeoVideo: Introducing Geometric Regularization into Video Generation Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\be6u40gq0Y_reviews.json
    forum: https://openreview.net/forum?id=be6u40gq0Y

[333] rating=4.0 | decision=Reject | reviews=4
    title: Motion-Catcher: Upholding Motion and Content Consistency in Multi-Sequence Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\6hsnpDXgHC_reviews.json
    forum: https://openreview.net/forum?id=6hsnpDXgHC

[334] rating=4.0 | decision=Reject | reviews=4
    title: Attention Surgery: An Efficient Recipe to Linearize Your Video Diffusion Transformer
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KFXpfw5k1f_reviews.json
    forum: https://openreview.net/forum?id=KFXpfw5k1f

[335] rating=4.0 | decision=Reject | reviews=4
    title: Ctrl-V: Higher Fidelity Video Generation with Bounding-Box Controlled Object Motion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\n6To2wAOKL_reviews.json
    forum: https://openreview.net/forum?id=n6To2wAOKL

[336] rating=4.0 | decision=None | reviews=4
    title: Think Before You Diffuse: Infusing Physical Rules into Video Diffusion
    pdf: research_data\iclr\video-generation\pdfs\Think_Before_You_Diffuse__Infusing_Physical_Rules_into_Video_Diffusion.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=lPKsPBstHg

[337] rating=4.0 | decision=None | reviews=5
    title: EventSR-Zero: Training-free Event Video Super-Resolution with Diffusion Priors
    pdf: research_data\iclr\video-super-resolution\pdfs\EventSR-Zero__Training-free_Event_Video_Super-Resolution_with_Diffusion_Priors.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Kx5CcyEY39

[338] rating=4.0 | decision=None | reviews=4
    title: Realtime Video Frame Interpolation using One-Step Diffusion Sampling
    pdf: research_data\iclr\video-diffusion\pdfs\Realtime_Video_Frame_Interpolation_using_One-Step_Diffusion_Sampling.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=OiWyf1BNtC

[339] rating=4.0 | decision=Reject | reviews=4
    title: FlexTraj: Image-to-Video Generation with Flexible Point Trajectory Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\3fIBwnz4Tf_reviews.json
    forum: https://openreview.net/forum?id=3fIBwnz4Tf

[340] rating=4.0 | decision=Reject | reviews=4
    title: Investigating Memorization in Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\RFZV2tOWYN_reviews.json
    forum: https://openreview.net/forum?id=RFZV2tOWYN

[341] rating=4.0 | decision=Reject | reviews=3
    title: MoViE: Mobile Diffusion for Video Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1uZ4LpwtpN_reviews.json
    forum: https://openreview.net/forum?id=1uZ4LpwtpN

[342] rating=4.0 | decision=None | reviews=4
    title: Code2Video: A Code-centric Paradigm for Educational Video Generation
    pdf: research_data\iclr\video-generation\pdfs\Code2Video__A_Code-centric_Paradigm_for_Educational_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=nlJX6Hwyl0

[343] rating=4.0 | decision=Reject | reviews=4
    title: Mitty: Diffusion-based Human-To-Robot Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\BxeJLOrKDF_reviews.json
    forum: https://openreview.net/forum?id=BxeJLOrKDF

[344] rating=4.0 | decision=Reject | reviews=4
    title: STR-Match: Matching SpatioTemporal Relevance Score for Training-Free Video Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\XguSzViX02_reviews.json
    forum: https://openreview.net/forum?id=XguSzViX02

[345] rating=4.0 | decision=None | reviews=4
    title: U-MARVEL: Unveiling Key Factors for Universal Multimodal Retrieval via Embedding Learning with MLLMs
    pdf: research_data\iclr\text-to-video\pdfs\U-MARVEL__Unveiling_Key_Factors_for_Universal_Multimodal_Retrieval_via_Embedding.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=CUFJluq5O8

[346] rating=4.0 | decision=Reject | reviews=3
    title: Unifying Reinforcement Learning and Distillation via Distribution Matching for Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\k57oZGbdJ9_reviews.json
    forum: https://openreview.net/forum?id=k57oZGbdJ9

[347] rating=4.0 | decision=Reject | reviews=4
    title: VideoGuide: Improving Video Diffusion Models without Training Through a Teacher's Guide
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\VmR3QvfLxt_reviews.json
    forum: https://openreview.net/forum?id=VmR3QvfLxt

[348] rating=4.0 | decision=Reject | reviews=4
    title: Trash to Treasure: Paving a New Way for Improving Video Understanding via Counterfactual Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\l08OzcT7bb_reviews.json
    forum: https://openreview.net/forum?id=l08OzcT7bb

[349] rating=3.8 | decision=Reject | reviews=5
    title: CausalVE: Face Video Privacy Encryption via Causal Video Prediction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\waHmD2i1dv_reviews.json
    forum: https://openreview.net/forum?id=waHmD2i1dv

[350] rating=3.8 | decision=Accept (Poster) | reviews=12
    title: EPA: Boosting Event-based Video Frame Interpolation with Perceptually Aligned Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\zxZPpVoCNO_reviews.json
    forum: https://openreview.net/forum?id=zxZPpVoCNO

[351] rating=3.8 | decision=Accept | reviews=11
    title: DFVEdit: Conditional Delta Flow Vector for Zero-shot Video Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\uglqgGHNFb_reviews.json
    forum: https://openreview.net/forum?id=uglqgGHNFb

[352] rating=3.8 | decision=Reject | reviews=4
    title: Pre-Training and Fine-Tuning Image Super-Resolution Models for Efficient Video Super-Resolution
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\GDNo5oLpMx_reviews.json
    forum: https://openreview.net/forum?id=GDNo5oLpMx

[353] rating=3.8 | decision=Reject | reviews=4
    title: ImmersePro: End-to-End Stereo Video Synthesis Via Implicit Disparity Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\GqhvJ1o8m5_reviews.json
    forum: https://openreview.net/forum?id=GqhvJ1o8m5

[354] rating=3.8 | decision=Accept (Poster) | reviews=12
    title: Image as a World: Generating Interactive World from Single Image via Panoramic Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\PA47sKU8CU_reviews.json
    forum: https://openreview.net/forum?id=PA47sKU8CU

[355] rating=3.8 | decision=Reject | reviews=4
    title: Contextually Harmonious Local Video Editing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\GwJXJSCH1S_reviews.json
    forum: https://openreview.net/forum?id=GwJXJSCH1S

[356] rating=3.7 | decision=Reject | reviews=3
    title: Temporal-Aware Test-Time Training via Self-Distillation for One-Shot Image-to-Video Segmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\BhECSDSkAE_reviews.json
    forum: https://openreview.net/forum?id=BhECSDSkAE

[357] rating=3.5 | decision=Reject | reviews=4
    title: WorldForge: Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\5eFCw1LSIi_reviews.json
    forum: https://openreview.net/forum?id=5eFCw1LSIi

[358] rating=3.5 | decision=None | reviews=4
    title: Egocentric Cross-Embodiment Video Editing via Dual Contrastive Representation Learning
    pdf: research_data\iclr\video-generation\pdfs\Egocentric_Cross-Embodiment_Video_Editing_via_Dual_Contrastive_Representation_Le.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=hGcb46DWQD

[359] rating=3.5 | decision=None | reviews=4
    title: BachVid: Training-Free Video Generation with Consistent Background and Character
    pdf: research_data\iclr\text-to-video\pdfs\BachVid__Training-Free_Video_Generation_with_Consistent_Background_and_Character.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=BAskirM6hM

[360] rating=3.5 | decision=None | reviews=4
    title: Multi-marginal temporal Schrödinger Bridge Matching for video generation from unpaired data
    pdf: research_data\iclr\video-generation\pdfs\Multi-marginal_temporal_Schrödinger_Bridge_Matching_for_video_generation_from_un.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=9vW73ypnsU

[361] rating=3.5 | decision=Reject | reviews=4
    title: T2VUnlearning: A Concept Erasing Method for Text-to-Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\o88RP8Xqy5_reviews.json
    forum: https://openreview.net/forum?id=o88RP8Xqy5

[362] rating=3.5 | decision=None | reviews=4
    title: Next Block Prediction: Video Generation via Semi-Auto-Regressive Modeling
    pdf: research_data\iclr\video-generation\pdfs\Next_Block_Prediction__Video_Generation_via_Semi-Auto-Regressive_Modeling.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=JUYBEmwSJK

[363] rating=3.5 | decision=Reject | reviews=4
    title: Character-Driven Narrative Generation for Scene-Based Video Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bVsVbmI0qC_reviews.json
    forum: https://openreview.net/forum?id=bVsVbmI0qC

[364] rating=3.5 | decision=Reject | reviews=4
    title: Autoregressive Video Generation with Learnable Memory and Consistent Decoding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\UoRWYIGeRi_reviews.json
    forum: https://openreview.net/forum?id=UoRWYIGeRi

[365] rating=3.5 | decision=None | reviews=4
    title: NABLA: Neighborhood-Adaptive Block-Level Attention for Efficient Video Diffusion Transformers
    pdf: research_data\iclr\video-generation\pdfs\Adaptive_Caching_for_Faster_Video_Generation_with_Diffusion_Transformers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=SJ2WK6kdPJ

[366] rating=3.5 | decision=None | reviews=4
    title: TornadoAttention: Hardware-Efficient Sparse Attention via Fine-Grained Spatio-Temporal Permutation for Video Generation
    pdf: research_data\iclr\video-generation\pdfs\TornadoAttention__Hardware-Efficient_Sparse_Attention_via_Fine-Grained_Spatio-Te.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=fx3Ht2gYTR

[367] rating=3.5 | decision=Reject | reviews=4
    title: Asymmetric VAE for One-Step Video Super-Resolution Acceleration
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qccGDaGCtz_reviews.json
    forum: https://openreview.net/forum?id=qccGDaGCtz

[368] rating=3.5 | decision=Reject | reviews=4
    title: MVI2V: Human Centric Image to Video Generation with Muliview Consistent Appearance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\X1gKlHIdig_reviews.json
    forum: https://openreview.net/forum?id=X1gKlHIdig

[369] rating=3.5 | decision=None | reviews=4
    title: Moaw: Unleashing Motion Awareness for Video Diffusion Models
    pdf: research_data\iclr\image-to-video\pdfs\Moaw__Unleashing_Motion_Awareness_for_Video_Diffusion_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=E87rJRkmTk

[370] rating=3.5 | decision=Reject | reviews=4
    title: DAPE: Dual-Stage Parameter-Efficient Fine-Tuning for Consistent Video Editing with Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\SSKO69FenF_reviews.json
    forum: https://openreview.net/forum?id=SSKO69FenF

[371] rating=3.5 | decision=Reject | reviews=4
    title: OmniV2V: Versatile Video Generation and Editing via Dynamic Content Manipulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ySLgxJKvgK_reviews.json
    forum: https://openreview.net/forum?id=ySLgxJKvgK

[372] rating=3.5 | decision=Reject | reviews=4
    title: RoboTransfer: Geometry-Consistent Video Diffusion for Robotic Visual Policy Transfer
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\WCY0l6z3Rm_reviews.json
    forum: https://openreview.net/forum?id=WCY0l6z3Rm

[373] rating=3.5 | decision=Reject | reviews=4
    title: Scale-Adapter: Reversed Distillation Adapter for Efficient Training of Large Video Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\c7vpjzlDR9_reviews.json
    forum: https://openreview.net/forum?id=c7vpjzlDR9

[374] rating=3.5 | decision=Reject | reviews=4
    title: DeepVerse: 4D Autoregressive Video Generation as a World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\jdoW4zmDg3_reviews.json
    forum: https://openreview.net/forum?id=jdoW4zmDg3

[375] rating=3.5 | decision=None | reviews=4
    title: Video Generation with Learned Action Prior
    pdf: research_data\iclr\video-generation\pdfs\MAVIN__Multi-Action_Video_Generation_with_Diffusion_Models_via_Transition_Video.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=VAvZ4oinpa

[376] rating=3.5 | decision=Reject | reviews=4
    title: LightCache: Memory-Efficient, Training-Free Acceleration for Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\NomB0oiwqI_reviews.json
    forum: https://openreview.net/forum?id=NomB0oiwqI

[377] rating=3.5 | decision=Accept (poster) | reviews=4
    title: Fast Video Generation with Sliding Tile Attention.
    pdf: research_data\authors\Hao_Zhang\pdfs\Fast_Video_Generation_with_Sliding_Tile_Attention..pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=U74MOXPEJd

[378] rating=3.5 | decision=Reject | reviews=4
    title: WonderFree: Enhancing 3D World Generation via Video Diffusion Prior with Multi-view Consistency
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\IwjXdoum4W_reviews.json
    forum: https://openreview.net/forum?id=IwjXdoum4W

[379] rating=3.5 | decision=None | reviews=4
    title: Video Latent Flow Matching: Optimal Polynomial Projections for Video Interpolation and Extrapolation
    pdf: research_data\iclr\text-to-video\pdfs\Video_Latent_Flow_Matching__Optimal_Polynomial_Projections_for_Video_Interpolati.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=L0lvmP0iLp

[380] rating=3.5 | decision=None | reviews=4
    title: ExVideo: Extending Video Diffusion Models via Parameter-Efficient Post-Tuning
    pdf: research_data\iclr\video-generation\pdfs\ExVideo__Extending_Video_Diffusion_Models_via_Parameter-Efficient_Post-Tuning.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Hhx3swAQAZ

[381] rating=3.3 | decision=Reject | reviews=3
    title: Omniagent: Long-Video Generation via Cross-Modal Multi-Agent Orchestration
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Smc4U2aDzW_reviews.json
    forum: https://openreview.net/forum?id=Smc4U2aDzW

[382] rating=3.3 | decision=Reject | reviews=3
    title: OmniCustom: A Multimodal-Driven Architecture for Customized Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\nvNSyX5uV6_reviews.json
    forum: https://openreview.net/forum?id=nvNSyX5uV6

[383] rating=3.3 | decision=Reject | reviews=3
    title: Towards Redundancy Reduction in Diffusion Models for Efficient Video Super-Resolution
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\AVv0zeFlZE_reviews.json
    forum: https://openreview.net/forum?id=AVv0zeFlZE

[384] rating=3.3 | decision=Reject | reviews=3
    title: Flowing From Observed To Future Frames For Efficient Video Prediction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\p2rmqkkrOn_reviews.json
    forum: https://openreview.net/forum?id=p2rmqkkrOn

[385] rating=3.3 | decision=Reject | reviews=3
    title: Background Matters: Robust 3D Human Pose Estimation via Controllable Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Uh8NGna3VE_reviews.json
    forum: https://openreview.net/forum?id=Uh8NGna3VE

[386] rating=3.3 | decision=Reject | reviews=3
    title: Stream-DiffVSR: Low-Latency Streamable Video Super-Resolution via Auto-Regressive Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\seyWxIzcAn_reviews.json
    forum: https://openreview.net/forum?id=seyWxIzcAn

[387] rating=3.3 | decision=Accept (Poster) | reviews=8
    title: VideoTitans: Scalable Video Prediction with Integrated Short- and Long-term Memory
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\86enCXORIV_reviews.json
    forum: https://openreview.net/forum?id=86enCXORIV

[388] rating=3.3 | decision=Reject | reviews=3
    title: BlockVid: Block Diffusion for High-Fidelity and Coherent Minute-Long Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\k8KIwW4f7P_reviews.json
    forum: https://openreview.net/forum?id=k8KIwW4f7P

[389] rating=3.2 | decision=None | reviews=4
    title: Conditional density estimation for video prediction with score-based models
    pdf: research_data\iclr\video-prediction\pdfs\Conditional_density_estimation_for_video_prediction_with_score-based_models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=mHkbi3XM58

[390] rating=3.2 | decision=Accept (poster) | reviews=4
    title: Sparse Video-Gen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity.
    pdf: NO_PDF
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=u8CA3qIS0V

[391] rating=3.0 | decision=Reject | reviews=4
    title: VEFlow: Training-free Text to Video Editing via Inversion-Free Video Editing Flow
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\kMIvwXCRKt_reviews.json
    forum: https://openreview.net/forum?id=kMIvwXCRKt

[392] rating=3.0 | decision=Reject | reviews=4
    title: PAV-DiT: A Cross-modal Alignment Projected Latent Diffusion Transformer for Synchronized Audio-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\RFrc0g7pSu_reviews.json
    forum: https://openreview.net/forum?id=RFrc0g7pSu

[393] rating=3.0 | decision=Reject | reviews=4
    title: VC-VAE: Enhancing Video VAE with Video Codec Standard for Latent Video Diffusion Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\UBsmQXhXg8_reviews.json
    forum: https://openreview.net/forum?id=UBsmQXhXg8

[394] rating=3.0 | decision=Reject | reviews=4
    title: DynamicEval: Rethinking Evaluation for Dynamic Text-to-Video Synthesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0cBlhTTHfx_reviews.json
    forum: https://openreview.net/forum?id=0cBlhTTHfx

[395] rating=3.0 | decision=Reject | reviews=5
    title: TIEM: Enhancing Explanation of Video Prediction via Temporal Dynamics-Focused Dual Perturbation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\TEjXRrhqtJ_reviews.json
    forum: https://openreview.net/forum?id=TEjXRrhqtJ

[396] rating=3.0 | decision=Reject | reviews=4
    title: OmniDrive:Towards Unified Next-Gen Controllable Multi-View Driving Video Generation with LLM-Guided World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\dYW9MJyyK3_reviews.json
    forum: https://openreview.net/forum?id=dYW9MJyyK3

[397] rating=3.0 | decision=Reject | reviews=4
    title: CCM-DiT: Camera-pose Controllable Method for DiT-based Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\15lk4nBXYb_reviews.json
    forum: https://openreview.net/forum?id=15lk4nBXYb

[398] rating=3.0 | decision=Reject | reviews=4
    title: Improving Dynamic Object Interactions in Text-to-Video Generation with AI Feedback
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1FpXsGaYas_reviews.json
    forum: https://openreview.net/forum?id=1FpXsGaYas

[399] rating=3.0 | decision=Reject | reviews=4
    title: Learning to Generate Object Interactions with Physics-Guided Video Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\vrY91av397_reviews.json
    forum: https://openreview.net/forum?id=vrY91av397

[400] rating=3.0 | decision=None | reviews=4
    title: Taming Text-to-Sounding Video Generation via Advanced Modality Condition and Interaction
    pdf: research_data\iclr\video-generation\pdfs\Taming_Text-to-Sounding_Video_Generation_via_Advanced_Modality_Condition_and_Int.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=jcVOMVkljY

[401] rating=3.0 | decision=Reject | reviews=4
    title: Bowtie-flow: Efficient High-Resolution Video Generation with Prior Preservation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\BwvJx2JP11_reviews.json
    forum: https://openreview.net/forum?id=BwvJx2JP11

[402] rating=3.0 | decision=Reject | reviews=4
    title: VIDES: VIDEO EDITING IN SECONDS WITH ONE-STEP DIFFUSION MODELS
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DscflMFynS_reviews.json
    forum: https://openreview.net/forum?id=DscflMFynS

[403] rating=3.0 | decision=Reject | reviews=4
    title: Efficient Training for Human Video Generation with Entropy-Guided Prioritized Progressive Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\jBSAJyHNPa_reviews.json
    forum: https://openreview.net/forum?id=jBSAJyHNPa

[404] rating=3.0 | decision=Reject | reviews=4
    title: Mask-Guided Video Generation: Enhancing Motion Control and Quality with Limited Data
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\9GNTtaIZh6_reviews.json
    forum: https://openreview.net/forum?id=9GNTtaIZh6

[405] rating=3.0 | decision=Reject | reviews=4
    title: PROBE: Probing Residual Concept Capacity in Erased Text-to-Video Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\sncc2E4jSy_reviews.json
    forum: https://openreview.net/forum?id=sncc2E4jSy

[406] rating=2.7 | decision=Reject | reviews=3
    title: Self-Correcting Text-to-Video Generation with Misalignment Detection and Localized Refinement
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\05pfP2khzx_reviews.json
    forum: https://openreview.net/forum?id=05pfP2khzx

[407] rating=2.7 | decision=Reject | reviews=3
    title: Reward-Guided Trajectory Distillation for Accelerated Diffusion-Based Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\N5RV691l3H_reviews.json
    forum: https://openreview.net/forum?id=N5RV691l3H

[408] rating=2.5 | decision=Reject | reviews=4
    title: T2VTextBench: A Human Evaluation Benchmark for Textual Control in Video Generation Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\lAXC8rLGcM_reviews.json
    forum: https://openreview.net/forum?id=lAXC8rLGcM

[409] rating=2.5 | decision=Reject | reviews=4
    title: DiffuPhyGS: Text-to-Video Generation with 3D Gaussians and Learnable Physical Properties via Diffusion Priors
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\mq43BAAos0_reviews.json
    forum: https://openreview.net/forum?id=mq43BAAos0

[410] rating=2.5 | decision=Reject | reviews=4
    title: CSAPR: Complex-Scenario-Aware Prompt Refinement for Text-to-Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\gjhv73nXlx_reviews.json
    forum: https://openreview.net/forum?id=gjhv73nXlx

[411] rating=2.5 | decision=Reject | reviews=4
    title: DraftAttention: Fast Video Diffusion via Low-Resolution Attention Guidance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\jUNmW3s45i_reviews.json
    forum: https://openreview.net/forum?id=jUNmW3s45i

[412] rating=2.5 | decision=None | reviews=4
    title: VideoDiT: Bridging Image Diffusion Transformers for Streamlined Video Generation
    pdf: research_data\iclr\text-to-video\pdfs\Character_Mixing_for_Video_Generation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=lvgsPjRtLM

[413] rating=2.5 | decision=Accept | reviews=4
    title: Motion Score Matching in Video Generation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\dF4gObeMCu_reviews.json
    forum: https://openreview.net/forum?id=dF4gObeMCu

[414] rating=2.0 | decision=Reject | reviews=4
    title: VidSplice: Towards Coherent Video Inpainting via Explicit Spaced Frame Guidance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\pjXSfyhifn_reviews.json
    forum: https://openreview.net/forum?id=pjXSfyhifn

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
