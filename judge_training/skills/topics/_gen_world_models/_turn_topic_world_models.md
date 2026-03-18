You are an expert AI research reviewer building a **skill file** for evaluating papers in the topic area: **world_models**.

## Your Task

Write a comprehensive skill file (Markdown, 10-20K tokens) that will be loaded by an AI judge agent when evaluating new research ideas in this area. The file should enable the judge to give calibrated, expert-level evaluations.

## Statistics from 277 papers in this area

```json
{
  "topic": "world_models",
  "num_papers": 277,
  "num_accepted": 195,
  "acceptance_rate": 0.704,
  "rating_mean": 4.91,
  "rating_median": 5.0,
  "rating_std": 1.21,
  "rating_min": 1.5,
  "rating_max": 8.0,
  "avg_soundness": 2.62,
  "avg_contribution": 2.41,
  "avg_presentation": 2.64,
  "tier_example_count": {
    "borderline (4-5)": 536,
    "low (1-3)": 168,
    "good (6-7)": 250,
    "excellent (8-10)": 19
  }
}
```

### Most common strength phrases from reviewers:
  - novel (213x)
  - baseline (186x)
  - ablation (166x)
  - well-written (110x)
  - well written (68x)
  - state-of-the-art (44x)
  - reproducib (40x)
  - scalab (27x)
  - strong empirical (20x)
  - novelty (20x)
  - comprehensive and (12x)
  - thorough and (12x)
  - strong performance (12x)
  - strong baselines (11x)
  - thorough evaluation (10x)
  - comprehensive experiments (9x)
  - significant performance (7x)
  - strong and (6x)
  - comprehensive experimental (6x)
  - significant improvement (6x)

### Most common weakness phrases from reviewers:
  - baseline (556x)
  - ablation (238x)
  - novelty (159x)
  - lack of (128x)
  - scalab (85x)
  - novel (74x)
  - unclear how (56x)
  - unclear whether (44x)
  - limited to (42x)
  - incremental (40x)
  - state-of-the-art (36x)
  - reproducib (36x)
  - lacks a (34x)
  - fair comparison (24x)
  - unclear what (19x)
  - unclear to (16x)
  - limited novelty (15x)
  - unclear if (14x)
  - unclear why (13x)
  - limited in (11x)

## Paper Manifest

Below is a manifest of all 277 papers in this topic with their scores, PDF paths, and review JSON paths.

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
# Paper Manifest for topic: world_models
# 277 papers total

[1] rating=8.0 | decision=None | reviews=4
    title: TD-MPC2: Scalable, Robust World Models for Continuous Control
    pdf: research_data\iclr\world-model\pdfs\TD-MPC2__Scalable,_Robust_World_Models_for_Continuous_Control.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Oxh5CstDJU

[2] rating=8.0 | decision=Accept (Oral) | reviews=4
    title: Robust agents learn causal world models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\pOoKI3ouv1_reviews.json
    forum: https://openreview.net/forum?id=pOoKI3ouv1

[3] rating=8.0 | decision=Accept | reviews=4
    title: Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\oBXfPyi47m_reviews.json
    forum: https://openreview.net/forum?id=oBXfPyi47m

[4] rating=8.0 | decision=Accept (Oral) | reviews=4
    title: Open-World Reinforcement Learning over Long Short-Term Imagination
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\vzItLaEoDa_reviews.json
    forum: https://openreview.net/forum?id=vzItLaEoDa

[5] rating=8.0 | decision=Accept (Oral) | reviews=3
    title: Mastering Memory Tasks with World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\1vDArHJ68h_reviews.json
    forum: https://openreview.net/forum?id=1vDArHJ68h

[6] rating=7.5 | decision=Accept (Spotlight) | reviews=4
    title: Learning Transformer-based World Models with Contrastive Predictive Coding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\YK9G4Htdew_reviews.json
    forum: https://openreview.net/forum?id=YK9G4Htdew

[7] rating=7.3 | decision=None | reviews=3
    title: Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling
    pdf: research_data\iclr\video-generation\pdfs\Generative_3D_Object_Particle_Dynamics.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=lTaPtGiUUc

[8] rating=7.2 | decision=Accept (Poster) | reviews=5
    title: Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\Psl75UCoZM_reviews.json
    forum: https://openreview.net/forum?id=Psl75UCoZM

[9] rating=7.0 | decision=Accept (Poster) | reviews=4
    title: Enhancing End-to-End Autonomous Driving with Latent World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\fd2u60ryG0_reviews.json
    forum: https://openreview.net/forum?id=fd2u60ryG0

[10] rating=7.0 | decision=Accept (Poster) | reviews=3
    title: Dream to Manipulate: Compositional World Models Empowering Robot Imitation Learning with Imagination
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\3RSLW9YSgk_reviews.json
    forum: https://openreview.net/forum?id=3RSLW9YSgk

[11] rating=7.0 | decision=None | reviews=4
    title: FOSP: Fine-tuning Offline Safe Policy through World Models
    pdf: research_data\iclr\world-model\pdfs\FOSP__Fine-tuning_Offline_Safe_Policy_through_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=dbuFJg7eaw

[12] rating=6.8 | decision=Accept (Poster) | reviews=5
    title: Efficient Exploration and Discriminative World Model Learning with an Object-Centric Abstraction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\hgwGi81ndj_reviews.json
    forum: https://openreview.net/forum?id=hgwGi81ndj

[13] rating=6.8 | decision=Accept (Poster) | reviews=4
    title: Zero-shot Model-based Reinforcement Learning using Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\uZFXpPrwSh_reviews.json
    forum: https://openreview.net/forum?id=uZFXpPrwSh

[14] rating=6.8 | decision=Accept (Poster) | reviews=8
    title: Operator World Models for Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\kbBjVMcJ7G_reviews.json
    forum: https://openreview.net/forum?id=kbBjVMcJ7G

[15] rating=6.7 | decision=Accept (Poster) | reviews=3
    title: Locality Sensitive Sparse Encoding for Learning World Models Online
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\i8PjQT3Uig_reviews.json
    forum: https://openreview.net/forum?id=i8PjQT3Uig

[16] rating=6.7 | decision=Accept (Poster) | reviews=6
    title: Discrete Codebook World Models for Continuous Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\lfRYzd8ady_reviews.json
    forum: https://openreview.net/forum?id=lfRYzd8ady

[17] rating=6.6 | decision=Accept (Spotlight) | reviews=5
    title: Adversarial Counterfactual Environment Model Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\rHAX0LRwk8_reviews.json
    forum: https://openreview.net/forum?id=rHAX0LRwk8

[18] rating=6.5 | decision=None | reviews=4
    title: FantasyWorld: Geometry-Consistent World Modeling via Unified Video and 3D Prediction
    pdf: research_data\iclr\video-generation\pdfs\FantasyWorld__Geometry-Consistent_World_Modeling_via_Unified_Video_and_3D_Predic.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=3q9vHEqsNx

[19] rating=6.5 | decision=None | reviews=4
    title: FLIP: Flow-Centric Generative Planning as General-Purpose Manipulation World Model
    pdf: research_data\iclr\video-generation\pdfs\FLIP__Flow-Centric_Generative_Planning_as_General-Purpose_Manipulation_World_Mod.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=B2N0nCVC91

[20] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: Language Agents Meet Causality -- Bridging LLMs and Causal World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\y9A2TpaGsE_reviews.json
    forum: https://openreview.net/forum?id=y9A2TpaGsE

[21] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: Enhancing Neural Training via a Correlated Dynamics Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\c9xsaASm9L_reviews.json
    forum: https://openreview.net/forum?id=c9xsaASm9L

[22] rating=6.5 | decision=Accept (Spotlight) | reviews=4
    title: Multi Time Scale World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\fY7dShbtmo_reviews.json
    forum: https://openreview.net/forum?id=fY7dShbtmo

[23] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: Drama: Mamba-Enabled Model-Based Reinforcement Learning Is Sample and Parameter Efficient
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\7XIkRgYjK3_reviews.json
    forum: https://openreview.net/forum?id=7XIkRgYjK3

[24] rating=6.5 | decision=None | reviews=4
    title: WorldGym: World Model as An Environment for Policy Evaluation
    pdf: research_data\iclr\video-generation\pdfs\WorldGym__World_Model_as_An_Environment_for_Policy_Evaluation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=hidBHy1CAw

[25] rating=6.5 | decision=Accept (Spotlight) | reviews=4
    title: Reward-Consistent Dynamics Models are Strongly Generalizable for Offline Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\GSBHKiw19c_reviews.json
    forum: https://openreview.net/forum?id=GSBHKiw19c

[26] rating=6.5 | decision=Accept | reviews=4
    title: Building spatial world models from sparse transitional episodic memories
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\w3w7WVG4ks_reviews.json
    forum: https://openreview.net/forum?id=w3w7WVG4ks

[27] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: Semi-Supervised Vision-Centric 3D Occupancy World Model for Autonomous Driving
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\rCX9l4OTCT_reviews.json
    forum: https://openreview.net/forum?id=rCX9l4OTCT

[28] rating=6.5 | decision=None | reviews=4
    title: DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving
    pdf: research_data\iclr\video-generation\pdfs\ConsisDrive__Identity-Preserving_Driving_World_Models_for_Video_Generation_by_In.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=OrgL5DsU0f

[29] rating=6.5 | decision=Accept | reviews=4
    title: Verification of the Implicit World Model in a Generative Model via Adversarial Sequences
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\BLOIB8CwBI_reviews.json
    forum: https://openreview.net/forum?id=BLOIB8CwBI

[30] rating=6.5 | decision=None | reviews=4
    title: Hierarchical World Models as Visual Whole-Body Humanoid Controllers
    pdf: research_data\iclr\world-model\pdfs\Hierarchical_World_Models_as_Visual_Whole-Body_Humanoid_Controllers.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=7wuJMvK639

[31] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: Task-aware world model learning with meta weighting via bi-level optimization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\IN3hQx1BrC_reviews.json
    forum: https://openreview.net/forum?id=IN3hQx1BrC

[32] rating=6.5 | decision=Accept (Poster) | reviews=4
    title: SafeDreamer: Safe Reinforcement Learning with World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\tsE5HLYtYg_reviews.json
    forum: https://openreview.net/forum?id=tsE5HLYtYg

[33] rating=6.3 | decision=Accept (Poster) | reviews=3
    title: Learning World Models with Identifiable Factorization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\6JJq5TW9Mc_reviews.json
    forum: https://openreview.net/forum?id=6JJq5TW9Mc

[34] rating=6.3 | decision=Accept (Poster) | reviews=6
    title: Vista: A Generalizable Driving World Model with High Fidelity and Versatile Controllability
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\Tw9nfNyOMy_reviews.json
    forum: https://openreview.net/forum?id=Tw9nfNyOMy

[35] rating=6.2 | decision=Accept (Poster) | reviews=4
    title: Reward-Free Curricula for Training Robust World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\eCGpNGDeNu_reviews.json
    forum: https://openreview.net/forum?id=eCGpNGDeNu

[36] rating=6.2 | decision=Accept (Spotlight) | reviews=8
    title: Fine Tuning Out-of-Vocabulary Item Recommendation with User Sequence Imagination
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\JyWAFGCJPl_reviews.json
    forum: https://openreview.net/forum?id=JyWAFGCJPl

[37] rating=6.2 | decision=Accept (Poster) | reviews=8
    title: Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\9SpWvX9ykp_reviews.json
    forum: https://openreview.net/forum?id=9SpWvX9ykp

[38] rating=6.2 | decision=Accept (Poster) | reviews=8
    title: Learning World Models for Unconstrained Goal Navigation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\aYqTwcDlCG_reviews.json
    forum: https://openreview.net/forum?id=aYqTwcDlCG

[39] rating=6.2 | decision=Accept (Poster) | reviews=4
    title: Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\zDbsSscmuj_reviews.json
    forum: https://openreview.net/forum?id=zDbsSscmuj

[40] rating=6.2 | decision=Accept (Spotlight) | reviews=8
    title: Diffusion for World Modeling: Visual Details Matter in Atari
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\NadTwTODgC_reviews.json
    forum: https://openreview.net/forum?id=NadTwTODgC

[41] rating=6.2 | decision=Accept | reviews=5
    title: Model-based Reinforcement Learning for Parameterized Action Spaces
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\YH9tnuUYds_reviews.json
    forum: https://openreview.net/forum?id=YH9tnuUYds

[42] rating=6.2 | decision=Accept (Poster) | reviews=5
    title: CQM: Curriculum Reinforcement Learning with a Quantized World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\tcotyjon2a_reviews.json
    forum: https://openreview.net/forum?id=tcotyjon2a

[43] rating=6.2 | decision=Accept (Poster) | reviews=10
    title: Meta-DT: Offline Meta-RL as Conditional Sequence Modeling with World Model Disentanglement
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\U9MzoDOKZu_reviews.json
    forum: https://openreview.net/forum?id=U9MzoDOKZu

[44] rating=6.0 | decision=Accept | reviews=4
    title: R2-Dreamer: Redundancy-Reduced World Models without Decoders or Augmentation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Je2QqXrcQq_reviews.json
    forum: https://openreview.net/forum?id=Je2QqXrcQq

[45] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\moWiYJuSGF_reviews.json
    forum: https://openreview.net/forum?id=moWiYJuSGF

[46] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: BLEND: Behavior-guided Neural Population Dynamics Modeling via Privileged Knowledge Distillation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\jE5ZbtMtcU_reviews.json
    forum: https://openreview.net/forum?id=jE5ZbtMtcU

[47] rating=6.0 | decision=Accept | reviews=4
    title: RIG: Synergizing Reasoning and Imagination in End-to-End Generalist Policy
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\LQv9LU2Ufg_reviews.json
    forum: https://openreview.net/forum?id=LQv9LU2Ufg

[48] rating=6.0 | decision=None | reviews=4
    title: Dreamweaver: Learning Compositional World Models from Pixels
    pdf: research_data\iclr\world-model\pdfs\Dreamweaver__Learning_Compositional_World_Models_from_Pixels.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=e5mTvjXG9u

[49] rating=6.0 | decision=Accept (Poster) | reviews=3
    title: Neurosymbolic Grounding for Compositional World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\4KZpDGD4Nh_reviews.json
    forum: https://openreview.net/forum?id=4KZpDGD4Nh

[50] rating=6.0 | decision=Accept (Poster) | reviews=6
    title: In-Context Symmetries: Self-Supervised Learning through Contextual World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\etPAH4xSUn_reviews.json
    forum: https://openreview.net/forum?id=etPAH4xSUn

[51] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\QGJSXMhVaL_reviews.json
    forum: https://openreview.net/forum?id=QGJSXMhVaL

[52] rating=6.0 | decision=Accept | reviews=3
    title: Learning Massively Multitask World Models for Continuous Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\MPabX9LEds_reviews.json
    forum: https://openreview.net/forum?id=MPabX9LEds

[53] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: PWM: Policy Learning with Multi-Task World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\hOELrZfg0J_reviews.json
    forum: https://openreview.net/forum?id=hOELrZfg0J

[54] rating=6.0 | decision=Accept (Poster) | reviews=5
    title: Pre-training Contextualized World Models with In-the-wild Videos for Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\8GuEVzAUQS_reviews.json
    forum: https://openreview.net/forum?id=8GuEVzAUQS

[55] rating=6.0 | decision=Accept (Poster) | reviews=6
    title: Seek Commonality but Preserve Differences: Dissected Dynamics Modeling for Multi-modal Visual RL
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\4php6bGL2W_reviews.json
    forum: https://openreview.net/forum?id=4php6bGL2W

[56] rating=6.0 | decision=Accept (Poster) | reviews=8
    title: iVideoGPT: Interactive VideoGPTs are Scalable World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\4TENzBftZR_reviews.json
    forum: https://openreview.net/forum?id=4TENzBftZR

[57] rating=6.0 | decision=None | reviews=5
    title: Composition of Memory Experts for Diffusion World Models
    pdf: research_data\iclr\video-generation\pdfs\Composition_of_Memory_Experts_for_Diffusion_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=sUEdpZCHdp

[58] rating=6.0 | decision=Accept | reviews=4
    title: ADM-v2: Pursuing Full-Horizon Roll-out in Dynamics Models for Offline Policy Learning and Evaluation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ICbXEwqpga_reviews.json
    forum: https://openreview.net/forum?id=ICbXEwqpga

[59] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: Any-step Dynamics Model Improves Future Predictions for Online and Offline Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\JZCxlrwjZ8_reviews.json
    forum: https://openreview.net/forum?id=JZCxlrwjZ8

[60] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: Action Inference by Maximising Evidence: Zero-Shot Imitation from Observation with World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\WjlCQxpuxU_reviews.json
    forum: https://openreview.net/forum?id=WjlCQxpuxU

[61] rating=6.0 | decision=None | reviews=4
    title: Ctrl-World: A Controllable Generative World Model for Robot Manipulation
    pdf: research_data\iclr\world-model\pdfs\4D_Latent_World_Model_for_Robot_Planning.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=748bHL2BAv

[62] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: MAMBA: an Effective World Model Approach for Meta-Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\1RE0H6mU7M_reviews.json
    forum: https://openreview.net/forum?id=1RE0H6mU7M

[63] rating=6.0 | decision=Accept | reviews=4
    title: Code World Models for General Game Playing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1UoB7IWiku_reviews.json
    forum: https://openreview.net/forum?id=1UoB7IWiku

[64] rating=6.0 | decision=Accept (Spotlight) | reviews=4
    title: RePo: Resilient Model-Based Reinforcement Learning by Regularizing Posterior Predictability
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\OIJ3VXDy6s_reviews.json
    forum: https://openreview.net/forum?id=OIJ3VXDy6s

[65] rating=6.0 | decision=Accept (Poster) | reviews=5
    title: Dream the Impossible: Outlier Imagination with Diffusion Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\tnRboxQIec_reviews.json
    forum: https://openreview.net/forum?id=tnRboxQIec

[66] rating=6.0 | decision=Accept | reviews=4
    title: Empowering Multi-Robot Cooperation via Sequential World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\IvUM6UwYCJ_reviews.json
    forum: https://openreview.net/forum?id=IvUM6UwYCJ

[67] rating=6.0 | decision=Accept (Poster) | reviews=4
    title: On Rollouts in Model-Based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Uh5GRmLlvt_reviews.json
    forum: https://openreview.net/forum?id=Uh5GRmLlvt

[68] rating=5.8 | decision=Accept (Poster) | reviews=10
    title: Simplifying Latent Dynamics with Softly State-Invariant World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\CwNevJONgq_reviews.json
    forum: https://openreview.net/forum?id=CwNevJONgq

[69] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: Simple, Good, Fast: Self-Supervised World Models Free of Baggage
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\yFGR36PLDJ_reviews.json
    forum: https://openreview.net/forum?id=yFGR36PLDJ

[70] rating=5.8 | decision=None | reviews=4
    title: AVID: Adapting Video Diffusion Models to World Models
    pdf: research_data\iclr\image-to-video\pdfs\AVID__Adapting_Video_Diffusion_Models_to_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=15ASUbzg0N

[71] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: Robust Sleep Staging over Incomplete Multimodal Physiological Signals via Contrastive Imagination
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\bc1qt1sZsW_reviews.json
    forum: https://openreview.net/forum?id=bc1qt1sZsW

[72] rating=5.8 | decision=Accept | reviews=4
    title: DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\GARbxyCV13_reviews.json
    forum: https://openreview.net/forum?id=GARbxyCV13

[73] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: PIVOT-R: Primitive-Driven Waypoint-Aware World Model for Robotic Manipulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\gnXTDQyxlU_reviews.json
    forum: https://openreview.net/forum?id=gnXTDQyxlU

[74] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: STORM: Efficient Stochastic Transformer based World Models for Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\WxnrX42rnS_reviews.json
    forum: https://openreview.net/forum?id=WxnrX42rnS

[75] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: Toward Self-Improvement of LLMs via Imagination, Searching, and Criticizing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\tPdJ2qHkOB_reviews.json
    forum: https://openreview.net/forum?id=tPdJ2qHkOB

[76] rating=5.8 | decision=Accept | reviews=4
    title: Differentially Private Deep Model-Based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\1YYp1rPRlm_reviews.json
    forum: https://openreview.net/forum?id=1YYp1rPRlm

[77] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: Efficient Exploration in Continuous-time Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\VkhvDfY2dB_reviews.json
    forum: https://openreview.net/forum?id=VkhvDfY2dB

[78] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: Parallelizing Model-based Reinforcement Learning Over the Sequence Length
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\R6N9AGyz13_reviews.json
    forum: https://openreview.net/forum?id=R6N9AGyz13

[79] rating=5.8 | decision=Accept | reviews=4
    title: DRIVE: Distributional Model-Based Reinforcement Learning via Variational Inference
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\sNZTtDRFXt_reviews.json
    forum: https://openreview.net/forum?id=sNZTtDRFXt

[80] rating=5.8 | decision=Accept | reviews=4
    title: Decentralized Transformers with Centralized Aggregation are Sample-Efficient Multi-Agent World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\4E0lCxBD0U_reviews.json
    forum: https://openreview.net/forum?id=4E0lCxBD0U

[81] rating=5.8 | decision=None | reviews=4
    title: World Model on Million-Length Video And Language With Blockwise RingAttention
    pdf: research_data\iclr\world-model\pdfs\Learning_to_Model_the_World_with_Language.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=HN8V0flwJF

[82] rating=5.8 | decision=None | reviews=4
    title: SENSEI: Semantic Exploration Guided by Foundation Models to Learn Versatile World Models
    pdf: research_data\iclr\world-model\pdfs\SENSEI__Semantic_Exploration_Guided_by_Foundation_Models_to_Learn_Versatile_Worl.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=6DkpewPCcO

[83] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\GruDNzQ4ux_reviews.json
    forum: https://openreview.net/forum?id=GruDNzQ4ux

[84] rating=5.8 | decision=Accept (Poster) | reviews=8
    title: Grounded Answers for Multi-agent Decision-making Problem through Generative World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\QWsLks8LCO_reviews.json
    forum: https://openreview.net/forum?id=QWsLks8LCO

[85] rating=5.8 | decision=Accept (Poster) | reviews=4
    title: AdaWM: Adaptive World Model based Planning for Autonomous Driving
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\NEu8wgPctU_reviews.json
    forum: https://openreview.net/forum?id=NEu8wgPctU

[86] rating=5.6 | decision=Accept | reviews=5
    title: Time-aware World Model:  Adaptive Learning of Task Dynamics
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\8lwWBSa1pJ_reviews.json
    forum: https://openreview.net/forum?id=8lwWBSa1pJ

[87] rating=5.6 | decision=Accept | reviews=5
    title: Co-Learning Empirical Games & World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\TyZhiK6fDf_reviews.json
    forum: https://openreview.net/forum?id=TyZhiK6fDf

[88] rating=5.6 | decision=Accept | reviews=5
    title: Sample Efficient Robust Offline Self-Play for Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\3lXZjsir0e_reviews.json
    forum: https://openreview.net/forum?id=3lXZjsir0e

[89] rating=5.6 | decision=Accept (Poster) | reviews=10
    title: BECAUSE: Bilinear Causal Representation for Generalizable Offline Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\4i9xuPEu9w_reviews.json
    forum: https://openreview.net/forum?id=4i9xuPEu9w

[90] rating=5.5 | decision=Accept | reviews=4
    title: Pre-Training Robo-Centric World Models For Efficient Visual Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\DJw1JBTmuk_reviews.json
    forum: https://openreview.net/forum?id=DJw1JBTmuk

[91] rating=5.5 | decision=None | reviews=4
    title: Rethinking Driving World Model as Synthetic Data Generator for Perception Tasks
    pdf: research_data\iclr\video-generation\pdfs\Rethinking_Driving_World_Model_as_Synthetic_Data_Generator_for_Perception_Tasks.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=z3cFADf6zZ

[92] rating=5.5 | decision=None | reviews=4
    title: Learning and Reusing Abstract Latent Actions in a Hippocampal-Entorhinal-Inspired World Model
    pdf: research_data\iclr\world-model\pdfs\Learning_and_Reusing_Abstract_Latent_Actions_in_a_Hippocampal-Entorhinal-Inspire.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=RSvfY6dRVN

[93] rating=5.5 | decision=None | reviews=4
    title: ChronoEdit: Towards Temporal Reasoning for In-Context Image Editing and World Simulation
    pdf: research_data\iclr\video-generation\pdfs\ChronoEdit__Towards_Temporal_Reasoning_for_In-Context_Image_Editing_and_World_Si.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=MbMzoQ91Gk

[94] rating=5.5 | decision=Accept (Poster) | reviews=8
    title: Leveraging Separated World Model for Exploration in Visually Distracted Environments
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\Osh7u2E1kC_reviews.json
    forum: https://openreview.net/forum?id=Osh7u2E1kC

[95] rating=5.5 | decision=None | reviews=4
    title: Inter-Environmental World Modeling for Continuous and Compositional Dynamics
    pdf: research_data\iclr\world-model\pdfs\Inter-Environmental_World_Modeling_for_Continuous_and_Compositional_Dynamics.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=cojJ2s1e35

[96] rating=5.5 | decision=Accept (Poster) | reviews=8
    title: The Surprising Ineffectiveness of Pre-Trained Visual Representations for Model-Based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\LvAy07mCxU_reviews.json
    forum: https://openreview.net/forum?id=LvAy07mCxU

[97] rating=5.5 | decision=Accept | reviews=4
    title: DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\plrGn3RdzN_reviews.json
    forum: https://openreview.net/forum?id=plrGn3RdzN

[98] rating=5.5 | decision=Accept | reviews=4
    title: Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\LQD1MrnbxH_reviews.json
    forum: https://openreview.net/forum?id=LQD1MrnbxH

[99] rating=5.5 | decision=Accept (Poster) | reviews=6
    title: Learning Dynamic Attribute-factored World Models for Efficient Multi-object Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\bsNslV3Ahe_reviews.json
    forum: https://openreview.net/forum?id=bsNslV3Ahe

[100] rating=5.5 | decision=Accept | reviews=4
    title: Deliberate Reasoning for LLMs as Structure-aware Planning with Accurate World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\BaMkS6E2Du_reviews.json
    forum: https://openreview.net/forum?id=BaMkS6E2Du

[101] rating=5.5 | decision=Accept | reviews=4
    title: MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ffYd6uJpJE_reviews.json
    forum: https://openreview.net/forum?id=ffYd6uJpJE

[102] rating=5.5 | decision=None | reviews=4
    title: How Far Is Video Generation from World Model: A Physical Law Perspective
    pdf: research_data\iclr\video-generation\pdfs\How_Far_Is_Video_Generation_from_World_Model__A_Physical_Law_Perspective.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ZyLkNVHBZF

[103] rating=5.4 | decision=Accept | reviews=5
    title: Decoupled Offline to Online finetuning via Dynamics Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Fxsd66d2wB_reviews.json
    forum: https://openreview.net/forum?id=Fxsd66d2wB

[104] rating=5.4 | decision=Accept (Poster) | reviews=5
    title: Expanding Small-Scale Datasets with Guided Imagination
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\82HeVCqsfh_reviews.json
    forum: https://openreview.net/forum?id=82HeVCqsfh

[105] rating=5.4 | decision=Accept (Poster) | reviews=5
    title: Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2023\VeO03T59Sh_reviews.json
    forum: https://openreview.net/forum?id=VeO03T59Sh

[106] rating=5.4 | decision=Accept (Poster) | reviews=5
    title: Learning View-invariant World Models for Visual Robotic Manipulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\vJwjWyt4Ed_reviews.json
    forum: https://openreview.net/forum?id=vJwjWyt4Ed

[107] rating=5.3 | decision=None | reviews=3
    title: Object-Centric World Models from Few-Shot Annotations for Sample-Efficient Reinforcement Learning
    pdf: research_data\iclr\world-model\pdfs\Dreamweaver__Learning_Compositional_World_Models_from_Pixels.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=qmEyJadwHA

[108] rating=5.3 | decision=None | reviews=3
    title: OmniWorld: A Multi-Domain and Multi-Modal Dataset for 4D World Modeling
    pdf: research_data\iclr\video-generation\pdfs\OmniWorld__A_Multi-Domain_and_Multi-Modal_Dataset_for_4D_World_Modeling.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=1y1YFKb9pp

[109] rating=5.3 | decision=Accept | reviews=3
    title: Horizon Imagination: Efficient On-Policy Training in Diffusion World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Obefq4k8iG_reviews.json
    forum: https://openreview.net/forum?id=Obefq4k8iG

[110] rating=5.3 | decision=Accept | reviews=3
    title: Speech World Model: Causal State–Action Planning with Explicit Reasoning for Speech
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\YGUKPGO182_reviews.json
    forum: https://openreview.net/forum?id=YGUKPGO182

[111] rating=5.2 | decision=Accept (Poster) | reviews=8
    title: PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\z86knmjoUq_reviews.json
    forum: https://openreview.net/forum?id=z86knmjoUq

[112] rating=5.2 | decision=Accept (Spotlight) | reviews=12
    title: Vector Quantization in the Brain: Grid-like Codes in World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\M44RvNMZs4_reviews.json
    forum: https://openreview.net/forum?id=M44RvNMZs4

[113] rating=5.2 | decision=Accept | reviews=4
    title: Reconstructing Training Data From Real-World Models Trained with Transfer Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\BRdYYyrAOR_reviews.json
    forum: https://openreview.net/forum?id=BRdYYyrAOR

[114] rating=5.2 | decision=Accept | reviews=4
    title: Bayes Adaptive Monte Carlo Tree Search for Offline Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\S1OAqOtN5U_reviews.json
    forum: https://openreview.net/forum?id=S1OAqOtN5U

[115] rating=5.2 | decision=Accept (Spotlight) | reviews=8
    title: Evaluating the World Model Implicit in a Generative Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\aVK4JFpegy_reviews.json
    forum: https://openreview.net/forum?id=aVK4JFpegy

[116] rating=5.0 | decision=None | reviews=4
    title: WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation
    pdf: research_data\iclr\video-generation\pdfs\WristWorld__Generating_Wrist-Views_via_4D_World_Models_for_Robotic_Manipulation.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=Ilc2ybQWwH

[117] rating=5.0 | decision=Accept | reviews=4
    title: Dream-MPC: Gradient-Based Model Predictive Control with Latent Imagination
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\uhoCh3pViS_reviews.json
    forum: https://openreview.net/forum?id=uhoCh3pViS

[118] rating=5.0 | decision=Accept | reviews=4
    title: Harmony World Models: Boosting Sample Efficiency for Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\RN7RzMxwjC_reviews.json
    forum: https://openreview.net/forum?id=RN7RzMxwjC

[119] rating=5.0 | decision=Reject | reviews=4
    title: Adapting World Models with Latent-State Dynamics Residuals
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\W5e6Kkr2WN_reviews.json
    forum: https://openreview.net/forum?id=W5e6Kkr2WN

[120] rating=5.0 | decision=Accept | reviews=4
    title: Deep SPI: Safe Policy Improvement via World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\24C3bSaH3F_reviews.json
    forum: https://openreview.net/forum?id=24C3bSaH3F

[121] rating=5.0 | decision=Accept | reviews=4
    title: Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\0z0xhXRbN3_reviews.json
    forum: https://openreview.net/forum?id=0z0xhXRbN3

[122] rating=5.0 | decision=Accept | reviews=4
    title: Overcoming Knowledge Barriers: Online Imitation Learning from Visual Observation with Pretrained World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\EbOhZyxIzQ_reviews.json
    forum: https://openreview.net/forum?id=EbOhZyxIzQ

[123] rating=5.0 | decision=None | reviews=4
    title: Delta-Triplane Transformers as Occupancy World Models
    pdf: research_data\iclr\world-model\pdfs\Delta-Triplane_Transformers_as_Occupancy_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=0klioDjSVM

[124] rating=5.0 | decision=Accept | reviews=4
    title: Unified Stability Bounds for Structured World Models: Geometry, Equivariance, and Identifiability as Sufficient Conditions
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\VoKut0M4bI_reviews.json
    forum: https://openreview.net/forum?id=VoKut0M4bI

[125] rating=5.0 | decision=Accept | reviews=4
    title: Semantic World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\KfaZaYYCvt_reviews.json
    forum: https://openreview.net/forum?id=KfaZaYYCvt

[126] rating=5.0 | decision=Accept | reviews=4
    title: Astra: General Interactive World Model with Autoregressive Denoising
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\8UZpmrxoLG_reviews.json
    forum: https://openreview.net/forum?id=8UZpmrxoLG

[127] rating=5.0 | decision=Accept | reviews=4
    title: WMPO: World Model-based Policy Optimization for Vision-Language-Action Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qE2FyvRvuF_reviews.json
    forum: https://openreview.net/forum?id=qE2FyvRvuF

[128] rating=5.0 | decision=Accept | reviews=4
    title: Ego-centric Learning of Communicative World Models for  Autonomous Driving
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\7orD38wzdi_reviews.json
    forum: https://openreview.net/forum?id=7orD38wzdi

[129] rating=5.0 | decision=Accept | reviews=4
    title: Dual-Scale World Models for LLM Agents towards Hard-Exploration Problems
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\bH5uHIVtTe_reviews.json
    forum: https://openreview.net/forum?id=bH5uHIVtTe

[130] rating=5.0 | decision=Reject | reviews=4
    title: Visual Representation Learning for World Models by Predicting Fine-Grained Motion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\8BJl6LQgW5_reviews.json
    forum: https://openreview.net/forum?id=8BJl6LQgW5

[131] rating=5.0 | decision=Accept | reviews=4
    title: Stealthy World Model Manipulation via Data Poisoning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DotYL0mTxZ_reviews.json
    forum: https://openreview.net/forum?id=DotYL0mTxZ

[132] rating=5.0 | decision=Accept (Poster) | reviews=8
    title: Policy-shaped prediction: avoiding distractions in model-based reinforcement learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\hgdh4foghu_reviews.json
    forum: https://openreview.net/forum?id=hgdh4foghu

[133] rating=5.0 | decision=Accept (Poster) | reviews=8
    title: GenRL: Multimodal-foundation world models for generalization in embodied agents
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\za9Jx8yqUA_reviews.json
    forum: https://openreview.net/forum?id=za9Jx8yqUA

[134] rating=5.0 | decision=Accept | reviews=4
    title: WIMLE: Uncertainty‑Aware World Models with IMLE for Sample‑Efficient Continuous Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\mzLOnTb3WH_reviews.json
    forum: https://openreview.net/forum?id=mzLOnTb3WH

[135] rating=5.0 | decision=Accept (Spotlight) | reviews=11
    title: DMWM: Dual-Mind World Model with Long-Term Imagination
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\Bzlt5tPFT6_reviews.json
    forum: https://openreview.net/forum?id=Bzlt5tPFT6

[136] rating=5.0 | decision=Accept | reviews=4
    title: One Model for All Tasks: Leveraging Efficient World Models in Multi-Task Planning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\iU026Hr90y_reviews.json
    forum: https://openreview.net/forum?id=iU026Hr90y

[137] rating=5.0 | decision=Accept (Poster) | reviews=12
    title: Video World Models with Long-term Spatial Memory
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\HbTxc6U1fO_reviews.json
    forum: https://openreview.net/forum?id=HbTxc6U1fO

[138] rating=5.0 | decision=Accept | reviews=4
    title: RAVL: Reach-Aware Value Learning for the Edge-of-Reach Problem in Offline Model-Based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\cMIUwcEEVw_reviews.json
    forum: https://openreview.net/forum?id=cMIUwcEEVw

[139] rating=5.0 | decision=Accept | reviews=4
    title: HuWo：Building Physical Interaction World Models for Humanoid Robot Locomotion
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\bhUIoQ61pA_reviews.json
    forum: https://openreview.net/forum?id=bhUIoQ61pA

[140] rating=5.0 | decision=Accept | reviews=4
    title: Evaluating the World Models Used by Pretrained Learners
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\QtKYYatG3Z_reviews.json
    forum: https://openreview.net/forum?id=QtKYYatG3Z

[141] rating=4.8 | decision=Accept | reviews=5
    title: ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Patx6MRipw_reviews.json
    forum: https://openreview.net/forum?id=Patx6MRipw

[142] rating=4.8 | decision=Accept | reviews=4
    title: MIND: Masked and Inverse Dynamics Modeling for Data-Efficient Deep Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\jkonJu7ScD_reviews.json
    forum: https://openreview.net/forum?id=jkonJu7ScD

[143] rating=4.8 | decision=Accept | reviews=4
    title: Conservative World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\X5qi6fnnw7_reviews.json
    forum: https://openreview.net/forum?id=X5qi6fnnw7

[144] rating=4.8 | decision=Reject | reviews=4
    title: What Does it Mean for a Neural Network  to Learn a "World Model"?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\89nUKXMt8E_reviews.json
    forum: https://openreview.net/forum?id=89nUKXMt8E

[145] rating=4.8 | decision=None | reviews=4
    title: Information-Theoretic World Model learning for Denoised Predictions
    pdf: research_data\iclr\world-model\pdfs\Information-Theoretic_World_Model_learning_for_Denoised_Predictions.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=MdHDUsP2lt

[146] rating=4.8 | decision=Accept (Poster) | reviews=11
    title: Learning and Planning Multi-Agent Tasks via an MoE-based World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\fi24ry0BX5_reviews.json
    forum: https://openreview.net/forum?id=fi24ry0BX5

[147] rating=4.8 | decision=Accept (Spotlight) | reviews=12
    title: RoboScape: Physics-informed Embodied World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\wbZCBBrq3W_reviews.json
    forum: https://openreview.net/forum?id=wbZCBBrq3W

[148] rating=4.7 | decision=Accept | reviews=3
    title: Adapting Vision-Language Models for Evaluating World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\BXKgPhaOzr_reviews.json
    forum: https://openreview.net/forum?id=BXKgPhaOzr

[149] rating=4.7 | decision=Accept | reviews=3
    title: One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\UQ36IrVCw2_reviews.json
    forum: https://openreview.net/forum?id=UQ36IrVCw2

[150] rating=4.7 | decision=Reject | reviews=3
    title: LMGenDrive: LLM Reasoning Meets World Models for End-to-End Driving
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\fSnYZZ6v49_reviews.json
    forum: https://openreview.net/forum?id=fSnYZZ6v49

[151] rating=4.7 | decision=Accept | reviews=3
    title: EvoAgent: Self-evolving Agent with Continual World Model for Long-Horizon Tasks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\WSkU78RTGC_reviews.json
    forum: https://openreview.net/forum?id=WSkU78RTGC

[152] rating=4.7 | decision=None | reviews=3
    title: X-Streamer: Unified Human World Modeling with Audiovisual Interaction
    pdf: research_data\iclr\portrait-animation\pdfs\X-Streamer__Unified_Human_World_Modeling_with_Audiovisual_Interaction.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=rCNe4N7cP4

[153] rating=4.7 | decision=Reject | reviews=3
    title: VIRTUAL CELLS AS CAUSAL WORLD MODELS: A PERSPECTIVE ON EVALUATION
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qjIq4JWFVs_reviews.json
    forum: https://openreview.net/forum?id=qjIq4JWFVs

[154] rating=4.7 | decision=Accept | reviews=3
    title: From Observations to Events: Event-Aware World Models for Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\OWkkFaq1IZ_reviews.json
    forum: https://openreview.net/forum?id=OWkkFaq1IZ

[155] rating=4.7 | decision=Accept | reviews=3
    title: Hieros: Hierarchical Imagination on Structured State Space Sequence World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\5j6wtOO6Fk_reviews.json
    forum: https://openreview.net/forum?id=5j6wtOO6Fk

[156] rating=4.7 | decision=Accept | reviews=3
    title: ResWorld: Temporal Residual World Model for End-to-End Autonomous Driving
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ptGmMFGWmk_reviews.json
    forum: https://openreview.net/forum?id=ptGmMFGWmk

[157] rating=4.7 | decision=Accept (Poster) | reviews=9
    title: Social World Model-Augmented Mechanism Design Policy Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\uFTLo48OHF_reviews.json
    forum: https://openreview.net/forum?id=uFTLo48OHF

[158] rating=4.7 | decision=Reject | reviews=3
    title: Mani-WM: An Interactive World Model for Real-Robot Manipulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\aVyJwS1fqQ_reviews.json
    forum: https://openreview.net/forum?id=aVyJwS1fqQ

[159] rating=4.5 | decision=Accept | reviews=4
    title: Policy-Driven World Model Adaptation for Robust Offline Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\30I17s8gjs_reviews.json
    forum: https://openreview.net/forum?id=30I17s8gjs

[160] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Learning Interactive World Model for Object-Centric Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\E0cjqfM55C_reviews.json
    forum: https://openreview.net/forum?id=E0cjqfM55C

[161] rating=4.5 | decision=None | reviews=4
    title: VLASim: World Modelling via VLM-Directed Abstraction and Simulation from a Single Image
    pdf: research_data\iclr\video-generation\pdfs\VLASim__World_Modelling_via_VLM-Directed_Abstraction_and_Simulation_from_a_Singl.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=GfPwZwZ9xZ

[162] rating=4.5 | decision=Reject | reviews=4
    title: TriVLA: A Triple-System-Based Unified Vision-Language-Action Model with Episodic World Modeling for General Robot Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\tmIRNo66Rg_reviews.json
    forum: https://openreview.net/forum?id=tmIRNo66Rg

[163] rating=4.5 | decision=Reject | reviews=4
    title: DrivingWorld: Constructing World Model for Autonomous Driving via Video GPT
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\xJtWqVBZya_reviews.json
    forum: https://openreview.net/forum?id=xJtWqVBZya

[164] rating=4.5 | decision=Accept | reviews=4
    title: VCWorld: A Biological World Model for Virtual Cell Simulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\hhq89Hs7T3_reviews.json
    forum: https://openreview.net/forum?id=hhq89Hs7T3

[165] rating=4.5 | decision=Reject | reviews=4
    title: AdaReP: Plug-and-Play Acceleration for World Model Predictive Control using Adaptive Re-Planning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\WbNf4npMlJ_reviews.json
    forum: https://openreview.net/forum?id=WbNf4npMlJ

[166] rating=4.5 | decision=None | reviews=4
    title: Reinforcement Learning with Inverse Rewards for World Model Post-training
    pdf: research_data\iclr\video-generation\pdfs\Reinforcement_Learning_with_Inverse_Rewards_for_World_Model_Post-training.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=n5dkjiplv4

[167] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\xpjWEgf8zi_reviews.json
    forum: https://openreview.net/forum?id=xpjWEgf8zi

[168] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Overcoming Challenges of Long-Horizon Prediction in Driving World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\OACw1Fqy6Y_reviews.json
    forum: https://openreview.net/forum?id=OACw1Fqy6Y

[169] rating=4.5 | decision=Accept | reviews=4
    title: Unified World Models: Memory-Augmented Planning and Foresight for Visual Navigation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qSJIz364pO_reviews.json
    forum: https://openreview.net/forum?id=qSJIz364pO

[170] rating=4.5 | decision=Accept | reviews=4
    title: Internalizing World Models via Self-Play Finetuning for Agentic RL
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\K8wCGMzeuY_reviews.json
    forum: https://openreview.net/forum?id=K8wCGMzeuY

[171] rating=4.5 | decision=Accept | reviews=4
    title: Envision the Future in Open-World Dynamic Tasks by a Hierarchical World Model with Residual Enhanced Foresight
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\61NVz82YHM_reviews.json
    forum: https://openreview.net/forum?id=61NVz82YHM

[172] rating=4.5 | decision=Accept | reviews=4
    title: What drives success in physical planning with Joint-Embedding Predictive World Models?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\TuYC5Fpp7M_reviews.json
    forum: https://openreview.net/forum?id=TuYC5Fpp7M

[173] rating=4.5 | decision=Reject | reviews=4
    title: Model-Based Reinforcement Learning under Random Observation Delays
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\TntCH2maP7_reviews.json
    forum: https://openreview.net/forum?id=TntCH2maP7

[174] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Improving Model-Based Reinforcement Learning by Converging to Flatter Minima
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\vcB1OwtWUZ_reviews.json
    forum: https://openreview.net/forum?id=vcB1OwtWUZ

[175] rating=4.5 | decision=Accept | reviews=4
    title: Imagine Within Practice: Conservative Rollout Length Adaptation for Model-Based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\cYksYKbf6K_reviews.json
    forum: https://openreview.net/forum?id=cYksYKbf6K

[176] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\W0sqoTL7rL_reviews.json
    forum: https://openreview.net/forum?id=W0sqoTL7rL

[177] rating=4.5 | decision=Reject | reviews=4
    title: CBP: Learning Shared Cognitive Basis Space and Connectivity Patterns for Cross-Task Brain Dynamics Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QAfvrbiq6z_reviews.json
    forum: https://openreview.net/forum?id=QAfvrbiq6z

[178] rating=4.5 | decision=Reject | reviews=4
    title: Planning with Reasoning using Vision Language World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\uvRApnkdbk_reviews.json
    forum: https://openreview.net/forum?id=uvRApnkdbk

[179] rating=4.5 | decision=None | reviews=4
    title: TOWARD MEMORY-AIDED WORLD MODELS: BENCHMARKING VIA SPATIAL CONSISTENCY
    pdf: research_data\iclr\world-model\pdfs\TOWARD_MEMORY-AIDED_WORLD_MODELS__BENCHMARKING_VIA_SPATIAL_CONSISTENCY.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=uDmxJ6133n

[180] rating=4.5 | decision=Accept (Poster) | reviews=12
    title: RLVR-World: Training World Models with Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\jpiSagi8aV_reviews.json
    forum: https://openreview.net/forum?id=jpiSagi8aV

[181] rating=4.5 | decision=None | reviews=4
    title: Scaling Laws for Pre-training Agents and World Models
    pdf: research_data\iclr\world-model\pdfs\Scaling_Laws_for_Pre-training_Agents_and_World_Models.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=D0XpSucS3l

[182] rating=4.4 | decision=Accept | reviews=5
    title: LLMPhy: Complex Physical Reasoning Using Large Language Models and World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\qGL6fE1lqd_reviews.json
    forum: https://openreview.net/forum?id=qGL6fE1lqd

[183] rating=4.4 | decision=None | reviews=5
    title: PhysWorld: From Real Videos to World Models of Deformable Objects via Physics-Aware Demonstration Synthesis
    pdf: research_data\iclr\world-model\pdfs\PhysWorld__From_Real_Videos_to_World_Models_of_Deformable_Objects_via_Physics-Aw.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=dggfgPzGFW

[184] rating=4.4 | decision=Reject | reviews=5
    title: BEVWorld: A Multimodal World Model for Autonomous Driving via Unified BEV Latent Space
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\MFrqTfubEB_reviews.json
    forum: https://openreview.net/forum?id=MFrqTfubEB

[185] rating=4.4 | decision=Accept | reviews=5
    title: Collaborative World Models: An Online-Offline Transfer RL Approach
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\AhcxMGfqQn_reviews.json
    forum: https://openreview.net/forum?id=AhcxMGfqQn

[186] rating=4.4 | decision=Accept (Spotlight) | reviews=15
    title: PoE-World: Compositional World Modeling with Products of Programmatic Experts
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\obwRcksFZw_reviews.json
    forum: https://openreview.net/forum?id=obwRcksFZw

[187] rating=4.3 | decision=Accept | reviews=3
    title: Revisiting the Othello World Model Hypothesis
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\1OkVexYLct_reviews.json
    forum: https://openreview.net/forum?id=1OkVexYLct

[188] rating=4.3 | decision=Reject | reviews=3
    title: MuDreamer: Learning Predictive World Models without Reconstruction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\9pe38WpsbX_reviews.json
    forum: https://openreview.net/forum?id=9pe38WpsbX

[189] rating=4.3 | decision=Accept | reviews=6
    title: Achieving Precise Control with Slow Hardware: Model-Based Reinforcement Learning for Action Sequence Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2024\IdEaeCbhUW_reviews.json
    forum: https://openreview.net/forum?id=IdEaeCbhUW

[190] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: SAMPO: Scale-wise Autoregression with Motion Prompt for Generative World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\PJOwQ77Mul_reviews.json
    forum: https://openreview.net/forum?id=PJOwQ77Mul

[191] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: Towards foundational LiDAR world models with efficient latent flow matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\OyX9cC9WaV_reviews.json
    forum: https://openreview.net/forum?id=OyX9cC9WaV

[192] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: Bootstrap Off-policy with World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\zNqDCSokDR_reviews.json
    forum: https://openreview.net/forum?id=zNqDCSokDR

[193] rating=4.2 | decision=Reject | reviews=4
    title: One-shot World Models Using a Transformer Trained on a Synthetic Prior
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\VjeT8VFhHo_reviews.json
    forum: https://openreview.net/forum?id=VjeT8VFhHo

[194] rating=4.2 | decision=Accept | reviews=4
    title: Learning from Demonstration with Implicit Nonlinear Dynamics Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\tpqMR73GzS_reviews.json
    forum: https://openreview.net/forum?id=tpqMR73GzS

[195] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: DyMoDreamer: World Modeling with Dynamic Modulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\SYKwGnik3w_reviews.json
    forum: https://openreview.net/forum?id=SYKwGnik3w

[196] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: SPARTAN: A Sparse Transformer World Model Attending to What Matters
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\uS5ch7GjZ4_reviews.json
    forum: https://openreview.net/forum?id=uS5ch7GjZ4

[197] rating=4.2 | decision=Accept | reviews=4
    title: Planning with an Ensemble of World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\cvGdPXaydP_reviews.json
    forum: https://openreview.net/forum?id=cvGdPXaydP

[198] rating=4.2 | decision=Reject | reviews=4
    title: Learning 4D Embodied World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\mnwlhvmKMN_reviews.json
    forum: https://openreview.net/forum?id=mnwlhvmKMN

[199] rating=4.2 | decision=Accept (Poster) | reviews=11
    title: Leveraging Conditional Dependence for Efficient World Model Denoising
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\4pe5ZNNJyG_reviews.json
    forum: https://openreview.net/forum?id=4pe5ZNNJyG

[200] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: WALL-E: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\DorAT49sxj_reviews.json
    forum: https://openreview.net/forum?id=DorAT49sxj

[201] rating=4.2 | decision=Accept | reviews=4
    title: Value-Biased Maximum Likelihood Estimation for Model-based Reinforcement Learning in Discounted Linear MDPs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\2h3m61LFWL_reviews.json
    forum: https://openreview.net/forum?id=2h3m61LFWL

[202] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: seq-JEPA: Autoregressive Predictive Learning of Invariant-Equivariant World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\GKt3VRaCU1_reviews.json
    forum: https://openreview.net/forum?id=GKt3VRaCU1

[203] rating=4.2 | decision=Accept (Poster) | reviews=12
    title: DynamicVerse: A Physically-Aware Multimodal Framework for 4D World Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\B1nCWzpnE4_reviews.json
    forum: https://openreview.net/forum?id=B1nCWzpnE4

[204] rating=4.0 | decision=Accept | reviews=4
    title: Mixture-of-World Models: Scaling Multi-Task Reinforcement Learning with Modular Latent Dynamics
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\qUQARlAx5y_reviews.json
    forum: https://openreview.net/forum?id=qUQARlAx5y

[205] rating=4.0 | decision=Accept (Poster) | reviews=12
    title: Dyn-O: Building Structured World Models with  Object-Centric Representations
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\b2u1yrTwFK_reviews.json
    forum: https://openreview.net/forum?id=b2u1yrTwFK

[206] rating=4.0 | decision=Accept (Poster) | reviews=12
    title: StateSpaceDiffuser: Bringing Long Context to Diffusion World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\g52NwTQj0Q_reviews.json
    forum: https://openreview.net/forum?id=g52NwTQj0Q

[207] rating=4.0 | decision=Reject | reviews=4
    title: SelfDreamer: Dual-Prototypical Regularization for Frame-masked Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\8Itp6Axs9Z_reviews.json
    forum: https://openreview.net/forum?id=8Itp6Axs9Z

[208] rating=4.0 | decision=Accept | reviews=4
    title: TWISTED: Enhancing Transformer World Models with Spatio-Temporal Encoding and Graph-Based Optimal Decoding
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\1O8Jye1P0k_reviews.json
    forum: https://openreview.net/forum?id=1O8Jye1P0k

[209] rating=4.0 | decision=None | reviews=4
    title: 4D Latent World Model for Robot Planning
    pdf: research_data\iclr\world-model\pdfs\4D_Latent_World_Model_for_Robot_Planning.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=iB9qx28gv4

[210] rating=4.0 | decision=Reject | reviews=4
    title: Laplacian Analysis Meets Dynamics Modelling: Gaussian Splatting for 4D Scene Reconstruction
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\CQNeFyvqn3_reviews.json
    forum: https://openreview.net/forum?id=CQNeFyvqn3

[211] rating=4.0 | decision=Reject | reviews=3
    title: Gaussian Entropy Flow World Model for Streaming 3D Occupancy Predition
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\P0xkQNyguy_reviews.json
    forum: https://openreview.net/forum?id=P0xkQNyguy

[212] rating=4.0 | decision=Reject | reviews=4
    title: Coupled Distributional Random Expert Distillation for World Model Online Imitation Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\DR9e3M9Y3y_reviews.json
    forum: https://openreview.net/forum?id=DR9e3M9Y3y

[213] rating=4.0 | decision=Accept | reviews=4
    title: Remote Sensing-Oriented World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\eEdukIJ7lQ_reviews.json
    forum: https://openreview.net/forum?id=eEdukIJ7lQ

[214] rating=4.0 | decision=None | reviews=4
    title: Language-Guided Object-Centric World Models for Predictive Control
    pdf: research_data\iclr\video-generation\pdfs\Language-Guided_Object-Centric_World_Models_for_Predictive_Control.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=29p13QihRM

[215] rating=4.0 | decision=Accept | reviews=4
    title: Latent Action Robot Foundation World Models for Cross-Embodiment Adaptation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\vEZgPr1deb_reviews.json
    forum: https://openreview.net/forum?id=vEZgPr1deb

[216] rating=4.0 | decision=Reject | reviews=3
    title: VideoVerse: How Far is Your T2V Generator from a World Model?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\yLL2oDvWSn_reviews.json
    forum: https://openreview.net/forum?id=yLL2oDvWSn

[217] rating=4.0 | decision=Accept (Poster) | reviews=11
    title: MindJourney: Test-Time Scaling with World Models for Spatial Reasoning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\L2W4wQsNkY_reviews.json
    forum: https://openreview.net/forum?id=L2W4wQsNkY

[218] rating=4.0 | decision=Accept (Poster) | reviews=11
    title: Dynamics-Aligned Latent Imagination in Contextual World Models for Zero-Shot Generalization
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\41bIzD5sit_reviews.json
    forum: https://openreview.net/forum?id=41bIzD5sit

[219] rating=4.0 | decision=Accept | reviews=3
    title: HGWM: Hierarchical Graph-guided World Model for Zero-shot Object Navigation via Scene-Goal Graph Matching
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\8UEjC5P6jx_reviews.json
    forum: https://openreview.net/forum?id=8UEjC5P6jx

[220] rating=4.0 | decision=Accept | reviews=4
    title: When do World Models Successfully Learn Dynamical Systems?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\CNiiO3BU0t_reviews.json
    forum: https://openreview.net/forum?id=CNiiO3BU0t

[221] rating=4.0 | decision=Reject | reviews=3
    title: BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ZGWwV34Vmu_reviews.json
    forum: https://openreview.net/forum?id=ZGWwV34Vmu

[222] rating=4.0 | decision=Accept | reviews=4
    title: FASTopoWM: Fast-Slow Lane Segment Topology Reasoning with Latent World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\4L6WbrohFX_reviews.json
    forum: https://openreview.net/forum?id=4L6WbrohFX

[223] rating=4.0 | decision=Reject | reviews=3
    title: PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\XZ0pRezf4O_reviews.json
    forum: https://openreview.net/forum?id=XZ0pRezf4O

[224] rating=4.0 | decision=Accept | reviews=4
    title: KeyWorld: Key Frame Reasoning Enables Effective and Efficient World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\u3I4tDGhDV_reviews.json
    forum: https://openreview.net/forum?id=u3I4tDGhDV

[225] rating=4.0 | decision=Accept (Poster) | reviews=14
    title: Learning from Reward-Free Offline Data: A Case for Planning with Latent Dynamics Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\hTZ0SJCGQX_reviews.json
    forum: https://openreview.net/forum?id=hTZ0SJCGQX

[226] rating=4.0 | decision=Reject | reviews=4
    title: Value-aligned World Model Regularization for Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ph68z0OGHX_reviews.json
    forum: https://openreview.net/forum?id=ph68z0OGHX

[227] rating=4.0 | decision=Accept | reviews=4
    title: Building Social World Model with Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\hHO7AJC5yS_reviews.json
    forum: https://openreview.net/forum?id=hHO7AJC5yS

[228] rating=4.0 | decision=Accept | reviews=3
    title: Accelerating Model-Based Reinforcement Learning Using Equivariance
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\OQRs4JYvuv_reviews.json
    forum: https://openreview.net/forum?id=OQRs4JYvuv

[229] rating=4.0 | decision=Accept | reviews=3
    title: Contextual Latent World Models for Offline Meta Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\c4D7NJGC6D_reviews.json
    forum: https://openreview.net/forum?id=c4D7NJGC6D

[230] rating=4.0 | decision=Accept | reviews=4
    title: Trust the model when it is confounded: Model-based Reinforcement learning for Confounded POMDPs
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\UNnHm7Lm4T_reviews.json
    forum: https://openreview.net/forum?id=UNnHm7Lm4T

[231] rating=4.0 | decision=Accept (Poster) | reviews=8
    title: World Models as Reference Trajectories for Rapid Motor Adaptation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\xj0DXLQZCS_reviews.json
    forum: https://openreview.net/forum?id=xj0DXLQZCS

[232] rating=3.8 | decision=Accept (Poster) | reviews=12
    title: Agents Robust to Distribution Shifts Learn Causal World Models Even Under Mediation
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\JvHif4fyeP_reviews.json
    forum: https://openreview.net/forum?id=JvHif4fyeP

[233] rating=3.7 | decision=Reject | reviews=3
    title: H2IL-MBOM: A Hierarchical World Model Integrating Intent and Latent Strategy as Opponent Modeling in Multi-UAV Game
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\9TMbdO870O_reviews.json
    forum: https://openreview.net/forum?id=9TMbdO870O

[234] rating=3.5 | decision=Reject | reviews=4
    title: Prototypical Environment-aware Proxy with Coordinated Optimization for Multi-agent Dynamics Modeling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\9wuvVpnXvC_reviews.json
    forum: https://openreview.net/forum?id=9wuvVpnXvC

[235] rating=3.5 | decision=Reject | reviews=4
    title: DiZCo: Planning Zero-Shot Coordination in World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Y47Ab11TjP_reviews.json
    forum: https://openreview.net/forum?id=Y47Ab11TjP

[236] rating=3.5 | decision=Reject | reviews=4
    title: World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\otrng1WHxG_reviews.json
    forum: https://openreview.net/forum?id=otrng1WHxG

[237] rating=3.5 | decision=Accept | reviews=4
    title: Spatiotemporal Forecasting as Planning: A Model-Based Reinforcement Learning Approach with Generative World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\ASPC2Ut0CB_reviews.json
    forum: https://openreview.net/forum?id=ASPC2Ut0CB

[238] rating=3.5 | decision=Reject | reviews=4
    title: Active Confusion Expression in Large Language Models: Leveraging World Models toward Better Social Reasoning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\vFeeVtMx0T_reviews.json
    forum: https://openreview.net/forum?id=vFeeVtMx0T

[239] rating=3.5 | decision=None | reviews=4
    title: WorldPack: Compressed Memory Improves Spatial Consistency in Video World Modeling
    pdf: research_data\iclr\video-diffusion\pdfs\WorldPack__Compressed_Memory_Improves_Spatial_Consistency_in_Video_World_Modelin.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=CuNHz3zxgm

[240] rating=3.5 | decision=Reject | reviews=4
    title: Learning Disentangled Multi-Agent World Model for Decentralized Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\2KTEaY0lLi_reviews.json
    forum: https://openreview.net/forum?id=2KTEaY0lLi

[241] rating=3.5 | decision=Accept | reviews=4
    title: PrivilegedDreamer: Explicit Imagination of Privileged Information for Adaptation in Uncertain Environments
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\Y0wAim2F8A_reviews.json
    forum: https://openreview.net/forum?id=Y0wAim2F8A

[242] rating=3.5 | decision=Reject | reviews=4
    title: Bootstrapping World Models from Dynamics Models in Multimodal Foundation Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\FsfJ3lJhMJ_reviews.json
    forum: https://openreview.net/forum?id=FsfJ3lJhMJ

[243] rating=3.5 | decision=Reject | reviews=4
    title: Induction Rather Than Imagination: Generative Zero-Shot Learning Via Inductive Variational Autoencoder
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Jy0MJYZEuN_reviews.json
    forum: https://openreview.net/forum?id=Jy0MJYZEuN

[244] rating=3.5 | decision=Accept | reviews=12
    title: Uncovering Untapped Potential in Sample-Efficient World Model Agents
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\neurips\reviews\2025\3Cr6C2zNKw_reviews.json
    forum: https://openreview.net/forum?id=3Cr6C2zNKw

[245] rating=3.5 | decision=Reject | reviews=4
    title: Terra: Explorable Native 3D World Model with Point Latents
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\GD55nbjRaD_reviews.json
    forum: https://openreview.net/forum?id=GD55nbjRaD

[246] rating=3.5 | decision=Accept | reviews=4
    title: Closing the Train-Test Gap in World Models for Gradient-Based Planning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\By4u7V6tAx_reviews.json
    forum: https://openreview.net/forum?id=By4u7V6tAx

[247] rating=3.5 | decision=Reject | reviews=4
    title: DeepVerse: 4D Autoregressive Video Generation as a World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\jdoW4zmDg3_reviews.json
    forum: https://openreview.net/forum?id=jdoW4zmDg3

[248] rating=3.5 | decision=Reject | reviews=4
    title: From Masks to Worlds: A Hitchhiker’s Guide to World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\hAHbo4EGQY_reviews.json
    forum: https://openreview.net/forum?id=hAHbo4EGQY

[249] rating=3.5 | decision=Reject | reviews=4
    title: PO-Dreamer: Memory Guided World Models for Partially Observable Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\QklhZ70C49_reviews.json
    forum: https://openreview.net/forum?id=QklhZ70C49

[250] rating=3.3 | decision=Accept | reviews=3
    title: Causal-GNN SupplyNets Enabling Resilient Semiconductor Supply Chains with Causal World Models and Lyapunov-Safe Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\c6VapnMh4Z_reviews.json
    forum: https://openreview.net/forum?id=c6VapnMh4Z

[251] rating=3.3 | decision=Accept | reviews=3
    title: Learning to Drive with Two Minds: A Competitive Dual-Policy Approach in Latent World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\9SUbx81pko_reviews.json
    forum: https://openreview.net/forum?id=9SUbx81pko

[252] rating=3.3 | decision=None | reviews=3
    title: LongScape: Advancing Long-Horizon Embodied World Models with Context-Aware MoE
    pdf: research_data\iclr\video-generation\pdfs\LongScape__Advancing_Long-Horizon_Embodied_World_Models_with_Context-Aware_MoE.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=76flfkkawe

[253] rating=3.0 | decision=Accept | reviews=4
    title: Imagination Mechanism: Mesh Information Propagation for Enhancing Data Efficiency in Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\H8RgPl5OQX_reviews.json
    forum: https://openreview.net/forum?id=H8RgPl5OQX

[254] rating=3.0 | decision=Accept | reviews=4
    title: Small features matter: Robust representation for world models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\Qr9TjKYzjl_reviews.json
    forum: https://openreview.net/forum?id=Qr9TjKYzjl

[255] rating=3.0 | decision=Reject | reviews=3
    title: Compositional World Models with Interpretable Abstractions
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\EHmjRIA4l2_reviews.json
    forum: https://openreview.net/forum?id=EHmjRIA4l2

[256] rating=3.0 | decision=Reject | reviews=4
    title: Can Weak Quantization Make World Models Physically Interpretable?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\MSL8gSuCj2_reviews.json
    forum: https://openreview.net/forum?id=MSL8gSuCj2

[257] rating=3.0 | decision=Accept | reviews=4
    title: Sparse World Models: Visual World Modeling with Sparse Representations
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\e0mUayPl40_reviews.json
    forum: https://openreview.net/forum?id=e0mUayPl40

[258] rating=3.0 | decision=Reject | reviews=4
    title: OmniDrive:Towards Unified Next-Gen Controllable Multi-View Driving Video Generation with LLM-Guided World Model
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\dYW9MJyyK3_reviews.json
    forum: https://openreview.net/forum?id=dYW9MJyyK3

[259] rating=3.0 | decision=Accept | reviews=4
    title: Transformers and slot encoding for sample efficient physical world modelling
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\2H6KhX1kJr_reviews.json
    forum: https://openreview.net/forum?id=2H6KhX1kJr

[260] rating=3.0 | decision=Reject | reviews=4
    title: GLIMO: Grounding Large Language Models With Imperfect World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\ZNsWJkFrqQ_reviews.json
    forum: https://openreview.net/forum?id=ZNsWJkFrqQ

[261] rating=3.0 | decision=Accept | reviews=4
    title: Learning Task-Sufficient World Models via Intervention-Curriculum Co-Design
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\xFmxnyNYZJ_reviews.json
    forum: https://openreview.net/forum?id=xFmxnyNYZJ

[262] rating=3.0 | decision=Accept | reviews=3
    title: Learning Generalizable Environment Models via Discovering Superposed Causal Relationships
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\7LmuXey1lH_reviews.json
    forum: https://openreview.net/forum?id=7LmuXey1lH

[263] rating=3.0 | decision=Reject | reviews=4
    title: Structured World Models From Low-Level Observations
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\B7cZvTQsUN_reviews.json
    forum: https://openreview.net/forum?id=B7cZvTQsUN

[264] rating=3.0 | decision=Reject | reviews=4
    title: Tokenized Transformer World Models for Continual Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\jus1arazi7_reviews.json
    forum: https://openreview.net/forum?id=jus1arazi7

[265] rating=3.0 | decision=Reject | reviews=4
    title: Causally Disentangled World Models: Guiding Exploration with an Agency Bonus
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\6VnyYkg37h_reviews.json
    forum: https://openreview.net/forum?id=6VnyYkg37h

[266] rating=3.0 | decision=Accept | reviews=4
    title: Tree-of-Options: Temporally Extended World Modeling, Planning, and Execution with Large Language Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\XdaX5kFXVQ_reviews.json
    forum: https://openreview.net/forum?id=XdaX5kFXVQ

[267] rating=2.7 | decision=Accept | reviews=3
    title: Learning Abstract World Models with a Group-Structured Latent Space
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\YH1gieQrxH_reviews.json
    forum: https://openreview.net/forum?id=YH1gieQrxH

[268] rating=2.5 | decision=Reject | reviews=4
    title: Clone Deterministic 3D Worlds with Geometrically Regularized World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\TLXp0scq3x_reviews.json
    forum: https://openreview.net/forum?id=TLXp0scq3x

[269] rating=2.5 | decision=Accept | reviews=4
    title: DroneDreamer: Multi-View Low-Altitude World Model with Adaptive Control
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\eDyMFksVCl_reviews.json
    forum: https://openreview.net/forum?id=eDyMFksVCl

[270] rating=2.5 | decision=Reject | reviews=4
    title: Reward-free Policy Optimization with World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\OZ3NXrF3gQ_reviews.json
    forum: https://openreview.net/forum?id=OZ3NXrF3gQ

[271] rating=2.5 | decision=Accept | reviews=4
    title: Towards Policy-Aware World Models
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\Ro2eG1RRde_reviews.json
    forum: https://openreview.net/forum?id=Ro2eG1RRde

[272] rating=2.5 | decision=Accept | reviews=4
    title: Data-Driven Creativity: Amplifying Imagination in LLM Writing
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2025\uMxiGoczX1_reviews.json
    forum: https://openreview.net/forum?id=uMxiGoczX1

[273] rating=2.5 | decision=None | reviews=4
    title: FLAM: Scaling Latent Action World Models with Factorization
    pdf: research_data\iclr\video-generation\pdfs\FLAM__Scaling_Latent_Action_World_Models_with_Factorization.pdf
    review_json: NOT_FOUND
    forum: https://openreview.net/forum?id=ovaI8QU0gS

[274] rating=2.5 | decision=Reject | reviews=4
    title: Break Stylistic Sophon: Are We Really Meant to Confine the Imagination in Style Transfer?
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\JEpWuuoqbp_reviews.json
    forum: https://openreview.net/forum?id=JEpWuuoqbp

[275] rating=2.5 | decision=Accept | reviews=4
    title: Multi-timestep models for Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2024\Rh4DmXaf8R_reviews.json
    forum: https://openreview.net/forum?id=Rh4DmXaf8R

[276] rating=2.0 | decision=Reject | reviews=3
    title: STEP-VQ: Sequence-model Agnostic Frame-level Inference with VQ-VAE for Model-based Reinforcement Learning
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\aBgX5jCTcd_reviews.json
    forum: https://openreview.net/forum?id=aBgX5jCTcd

[277] rating=1.5 | decision=Accept | reviews=4
    title: Higher Embedding Dimension Creates a Stronger World Model for a Simple Sorting Task
    pdf: NO_PDF
    review_json: C:\Users\yhzha\auto_research_bot\research_data\iclr\reviews\2026\FLArrpmsF1_reviews.json
    forum: https://openreview.net/forum?id=FLArrpmsF1

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
