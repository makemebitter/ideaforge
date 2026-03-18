"""
Strictly filter for video GENERATION papers only.
Excludes: video understanding, video analysis, video LLM understanding, etc.
"""

import pandas as pd
import re

def is_video_generation_paper(title, abstract, keywords):
    """
    Check if paper is about video GENERATION (creating/synthesizing videos).
    Returns (is_generation, category) tuple.
    """
    title_lower = title.lower()
    abstract_lower = abstract.lower()
    keywords_lower = keywords.lower() if keywords else ""
    text = f"{title_lower} {abstract_lower} {keywords_lower}"
    
    # EXCLUDE patterns - papers about video understanding/analysis, not generation
    exclude_patterns = [
        r'video\s*(question|qa|understanding|comprehension|captioning|retrieval|classification)',
        r'video\s*llm.*(understanding|comprehension|question)',
        r'(understanding|comprehension|analyzing)\s*video',
        r'video\s*benchmark.*(understanding|evaluation)',
        r'video\s*language\s*(understanding|model)',
        r'brain\s*(activity|data|signal)',
        r'neural\s*(recording|activity|signal)',
        r'zebrafish',
        r'ecg\s*controlled',  # medical imaging
        r'echocardio',  # medical imaging
        r'gui[-\s]*(world|understanding)',  # GUI analysis
        r'visual\s*robot\s*manipulation',  # robot control using video
        r'offline\s*(model|rl|reinforcement)',  # RL papers
        r'world\s*model.*(control|rl|reinforcement|planning)',  # RL world models
        r'simulator.*(learning|training)',  # learning simulators
        r'robot.*(manipulation|control)',
        r'embodied.*(agent|ai)',
    ]
    
    for pattern in exclude_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            # But allow if it's clearly about generation
            if re.search(r'(generat|synthesis|creat|produc).*(video|motion|frame)', text, re.IGNORECASE):
                pass  # Still include
            else:
                return False, "excluded"
    
    # STRONG INCLUDE patterns - definitely video generation
    strong_include = [
        (r'text[\s\-]*to[\s\-]*video', 'text-to-video'),
        (r'image[\s\-]*to[\s\-]*video', 'image-to-video'),
        (r'video\s*(generation|synthesis)', 'video-generation'),
        (r'video\s*diffusion', 'video-diffusion'),
        (r'generat\w*\s*(video|frame)', 'video-generation'),
        (r'video\s*generat', 'video-generation'),
        (r'talking\s*(head|avatar|face|body|portrait)', 'talking-head'),
        (r'audio[\s\-]*driven.*(video|avatar|portrait|animation)', 'audio-driven'),
        (r'motion\s*(generation|synthesis)', 'motion-generation'),
        (r'human\s*motion\s*(generation|synthesis)', 'human-motion'),
        (r'video\s*editing', 'video-editing'),
        (r'video\s*interpolation', 'video-interpolation'),
        (r'frame\s*interpolation', 'frame-interpolation'),
        (r'video\s*inpainting', 'video-inpainting'),
        (r'video\s*prediction', 'video-prediction'),
        (r'video\s*super[\s\-]*resolution', 'video-super-resolution'),
        (r'video\s*(autoencoder|vae|tokeniz)', 'video-tokenizer'),
        (r'4d\s*(content|object|scene)\s*generation', '4d-generation'),
        (r'dynamic\s*3d.*generation', '4d-generation'),
        (r'character\s*(animation|image\s*animation)', 'character-animation'),
        (r'image\s*animation', 'image-animation'),
        (r'portrait\s*(animation|video)', 'portrait-animation'),
        (r'gesture\s*(generation|synthesis|video)', 'gesture-generation'),
        (r'dance\s*(generation|synthesis)', 'dance-generation'),
        (r'long[\s\-]*video\s*generation', 'long-video'),
        (r'autoregressive\s*video', 'autoregressive-video'),
        (r'video\s*transformer', 'video-model'),
        (r'diffusion.*video', 'video-diffusion'),
        (r'video.*diffusion', 'video-diffusion'),
        (r'sora', 'sora-related'),
        (r'cogvideo', 'video-model'),
        (r'animatediff', 'video-model'),
        (r'game\s*(video|engine)\s*generation', 'game-video'),
        (r'open[\s\-]*world.*video\s*generation', 'game-video'),
    ]
    
    for pattern, category in strong_include:
        if re.search(pattern, text, re.IGNORECASE):
            return True, category
    
    return False, "no-match"


def main():
    df = pd.read_csv('iclr_video_candidates.csv')
    
    results = []
    for idx, row in df.iterrows():
        title = str(row['title'])
        abstract = str(row['abstract'])
        keywords = str(row['keywords']) if pd.notna(row['keywords']) else ""
        
        is_gen, category = is_video_generation_paper(title, abstract, keywords)
        
        if is_gen:
            results.append({
                'title': row['title'],
                'abstract': row['abstract'],
                'year': row['year'],
                'venue': row['venue'],
                'forum_url': row['forum_url'],
                'keywords': row['keywords'],
                'category': category
            })
    
    # Create dataframe and save
    result_df = pd.DataFrame(results)
    result_df.to_csv('iclr_video_generation_papers.csv', index=False)
    
    print(f"Filtered to {len(result_df)} video generation papers out of {len(df)} candidates")
    print(f"\nBy year:")
    print(result_df['year'].value_counts().to_string())
    print(f"\nBy category:")
    print(result_df['category'].value_counts().to_string())
    
    print("\n" + "="*100)
    print("FINAL LIST - VIDEO GENERATION PAPERS")
    print("="*100)
    
    for year in [2025, 2024]:
        year_df = result_df[result_df['year'] == year]
        print(f"\n--- ICLR {year} ({len(year_df)} papers) ---\n")
        for idx, row in year_df.iterrows():
            print(f"[{row['category']}] {row['title']}")
            print(f"    URL: {row['forum_url']}")
            print()


if __name__ == '__main__':
    main()
