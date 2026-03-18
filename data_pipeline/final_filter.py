"""
Final manual review and filter for video generation papers.
Remove false positives that are not actually about video generation.
"""

import pandas as pd

# Load the filtered candidates
df = pd.read_csv('iclr_video_generation_papers.csv')

# Papers to EXCLUDE (not actually about video generation)
exclude_titles = [
    # Not video generation - these are about other topics
    "Accelerating Diffusion Transformers with Token-wise Feature Caching",  # Generic diffusion acceleration, not video-specific
    "SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model",  # Video guardrail/safety, not generation
    "SaRA: High-Efficient Diffusion Model Fine-tuning",  # Generic diffusion fine-tuning
    "Semantix: An Energy-guided Sampler for Semantic Style Transfer",  # Style transfer, not video generation
    "Faster Inference of Flow-Based Generative Models",  # Generic flow matching
    "A Large-scale Training Paradigm for Graph Generative Models",  # Graph generation, not video
    "Diffusion Transformers for Tabular Data Time Series Generation",  # Tabular data, not video
    "ClassDiffusion: More Aligned Personalization Tuning",  # Image personalization, video is just mentioned
    "Diffusion-NPO: Negative Preference Optimization",  # Generic diffusion training
    "Disentangling 3D Animal Pose Dynamics",  # Pose analysis, not generation
    "ECHOPulse: ECG Controlled Echocardio-gram Video Generation",  # Medical imaging, not general video
    "Fantastic Copyrighted Beasts and How (Not) to Generate Them",  # Copyright analysis
    "Needle In A Video Haystack",  # Video understanding benchmark
    "GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation",  # Robot manipulation
    "FlashAttention-2: Faster Attention",  # Attention mechanism, not video generation
    "MogaNet: Multi-order Gated Aggregation Network",  # Network architecture
    "DiffusionSat: A Generative Foundation Model for Satellite Imagery",  # Satellite imagery
    "Variational Inference for SDEs Driven by Fractional Noise",  # Math/theory paper
    "SPDER: Semiperiodic Damping-Enabled Object Representation",  # Object representation
    "Robust Watermarking Using Generative Priors",  # Watermarking
]

# Filter out excluded papers
mask = ~df['title'].isin(exclude_titles)
filtered_df = df[mask].copy()

# Categorize more precisely
def get_category(row):
    title = str(row['title']).lower()
    abstract = str(row['abstract']).lower()
    keywords = str(row.get('keywords', '')).lower() if pd.notna(row.get('keywords', '')) else ''
    text = f"{title} {abstract} {keywords}"
    
    # Check categories in order of specificity
    if any(x in text for x in ['text-to-video', 'text to video', 't2v']):
        return 'text-to-video'
    elif any(x in text for x in ['image-to-video', 'image to video', 'i2v', 'image animation']):
        return 'image-to-video'
    elif any(x in text for x in ['talking head', 'talking avatar', 'talking body', 'portrait animation', 'audio-driven']):
        return 'talking-head/avatar'
    elif any(x in text for x in ['human motion', 'motion generation', 'motion synthesis', 'dance', 'gesture']):
        return 'motion-generation'
    elif any(x in text for x in ['video editing', 'video-to-video']):
        return 'video-editing'
    elif any(x in text for x in ['4d generation', '4d content', 'dynamic 3d']):
        return '4d-generation'
    elif any(x in text for x in ['frame interpolation', 'video interpolation', 'inbetweening']):
        return 'video-interpolation'
    elif any(x in text for x in ['video diffusion', 'video generation model', 'video generative']):
        return 'video-diffusion-model'
    elif any(x in text for x in ['video tokeniz', 'video vae', 'video autoencoder']):
        return 'video-tokenizer'
    elif any(x in text for x in ['world model', 'game video', 'game engine']):
        return 'world-model/game'
    elif any(x in text for x in ['video generat', 'generat video']):
        return 'video-generation'
    else:
        return 'other'

filtered_df['category'] = filtered_df.apply(get_category, axis=1)

# Save final filtered list
filtered_df.to_csv('iclr_video_generation_final.csv', index=False)

print(f"Final filtered list: {len(filtered_df)} papers")
print(f"\nBy year:")
print(filtered_df['year'].value_counts().to_string())
print(f"\nBy category:")
print(filtered_df['category'].value_counts().to_string())

print("\n" + "="*100)
print("FINAL VIDEO GENERATION PAPERS - ICLR 2024, 2025 & 2026")
print("="*100)

for year in [2026, 2025, 2024]:
    year_df = filtered_df[filtered_df['year'] == year].sort_values('category')
    print(f"\n{'='*50}")
    print(f"ICLR {year} ({len(year_df)} papers)")
    print(f"{'='*50}")
    
    current_cat = None
    for idx, row in year_df.iterrows():
        if row['category'] != current_cat:
            current_cat = row['category']
            print(f"\n### {current_cat.upper()} ###\n")
        print(f"- {row['title']}")
        print(f"  {row['forum_url']}")

# Also save a simplified version with just title, URL, year, category
simple_df = filtered_df[['title', 'year', 'venue', 'forum_url', 'category']].copy()
simple_df.to_csv('iclr_video_generation_simple.csv', index=False)
print(f"\n\nSimplified list saved to: iclr_video_generation_simple.csv")
