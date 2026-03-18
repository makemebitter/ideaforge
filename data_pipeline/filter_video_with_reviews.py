"""
Filter video generation papers from the full dataset with reviews.
"""

import pandas as pd
import re

def is_video_generation_paper(title, abstract, keywords):
    """Check if paper is about video generation."""
    title_lower = str(title).lower()
    abstract_lower = str(abstract).lower()
    keywords_lower = str(keywords).lower() if pd.notna(keywords) else ""
    text = f"{title_lower} {abstract_lower} {keywords_lower}"
    
    # EXCLUDE patterns
    exclude_patterns = [
        r'video\s*(question|qa|understanding|comprehension|captioning|retrieval|classification)',
        r'video\s*llm.*(understanding|comprehension|question)',
        r'(understanding|comprehension|analyzing)\s*video',
        r'video\s*benchmark.*(understanding|evaluation)',
        r'brain\s*(activity|data|signal)',
        r'neural\s*(recording|activity|signal)',
        r'zebrafish',
        r'ecg\s*controlled',
        r'echocardio',
        r'gui[-\s]*(world|understanding)',
    ]
    
    for pattern in exclude_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            if not re.search(r'(generat|synthesis|creat|produc).*(video|motion|frame)', text, re.IGNORECASE):
                return False, "excluded"
    
    # INCLUDE patterns
    include_patterns = [
        (r'text[\s\-]*to[\s\-]*video', 'text-to-video'),
        (r'image[\s\-]*to[\s\-]*video', 'image-to-video'),
        (r'video\s*(generation|synthesis)', 'video-generation'),
        (r'video\s*diffusion', 'video-diffusion'),
        (r'generat\w*\s*(video|frame)', 'video-generation'),
        (r'video\s*generat', 'video-generation'),
        (r'talking\s*(head|avatar|face|body|portrait)', 'talking-head'),
        (r'audio[\s\-]*driven.*(video|avatar|portrait|animation)', 'audio-driven'),
        (r'human\s*motion\s*(generation|synthesis)', 'motion-generation'),
        (r'motion\s*(generation|synthesis)', 'motion-generation'),
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
        (r'gesture\s*(generation|synthesis)', 'gesture-generation'),
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
        (r'world\s*model.*video', 'world-model'),
        (r'video.*world\s*model', 'world-model'),
    ]
    
    for pattern, category in include_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True, category
    
    return False, "no-match"


def main():
    # Load full dataset
    df = pd.read_csv('iclr_all_with_reviews.csv')
    print(f"Total papers: {len(df)}")
    
    # Filter for video generation
    results = []
    for idx, row in df.iterrows():
        is_video, category = is_video_generation_paper(
            row['title'], row['abstract'], row.get('keywords', '')
        )
        if is_video:
            results.append({
                'title': row['title'],
                'decision': row['decision'],
                'avg_rating': row['avg_rating'],
                'min_rating': row['min_rating'],
                'max_rating': row['max_rating'],
                'num_reviews': row['num_reviews'],
                'ratings': row['ratings'],
                'venue': row['venue'],
                'year': row['year'],
                'abstract': row['abstract'],
                'keywords': row['keywords'],
                'primary_area': row.get('primary_area', ''),
                'TLDR': row.get('TLDR', ''),
                'pdf_url': row['pdf_url'],
                'forum_url': row['forum_url'],
                'category': category,
            })
    
    video_df = pd.DataFrame(results)
    
    # Save
    video_df.to_csv('iclr_video_generation_with_reviews.csv', index=False)
    
    print(f"\nFiltered to {len(video_df)} video generation papers")
    print("\nBy Year:")
    print(video_df['year'].value_counts().sort_index(ascending=False).to_string())
    
    print("\nBy Decision:")
    print(video_df['decision'].value_counts().to_string())
    
    print("\nBy Category:")
    print(video_df['category'].value_counts().to_string())
    
    # Show stats for accepted vs rejected
    print("\n" + "="*70)
    print("ACCEPTANCE STATISTICS")
    print("="*70)
    
    for year in sorted(video_df['year'].unique(), reverse=True):
        year_df = video_df[video_df['year'] == year]
        accepted = year_df[year_df['decision'].str.contains('Accept', na=False)]
        rejected = year_df[year_df['decision'] == 'Reject']
        
        print(f"\nICLR {year}:")
        print(f"  Total video papers: {len(year_df)}")
        print(f"  Accepted: {len(accepted)} ({100*len(accepted)/len(year_df):.1f}%)")
        print(f"  Rejected: {len(rejected)} ({100*len(rejected)/len(year_df):.1f}%)")
        
        if len(accepted) > 0 and accepted['avg_rating'].notna().sum() > 0:
            print(f"  Avg rating (accepted): {accepted['avg_rating'].mean():.2f}")
        if len(rejected) > 0 and rejected['avg_rating'].notna().sum() > 0:
            print(f"  Avg rating (rejected): {rejected['avg_rating'].mean():.2f}")
    
    # Also save a simplified accepted-only version
    accepted_df = video_df[video_df['decision'].str.contains('Accept', na=False)]
    accepted_df.to_csv('iclr_video_generation_accepted.csv', index=False)
    print(f"\nSaved {len(accepted_df)} accepted papers to iclr_video_generation_accepted.csv")
    
    # Print top papers by rating for each year
    print("\n" + "="*70)
    print("TOP RATED VIDEO GENERATION PAPERS (Accepted)")
    print("="*70)
    
    for year in sorted(video_df['year'].unique(), reverse=True):
        year_accepted = accepted_df[accepted_df['year'] == year].copy()
        if len(year_accepted) > 0:
            top = year_accepted.nlargest(10, 'avg_rating')[['title', 'decision', 'avg_rating', 'category']]
            print(f"\nICLR {year} - Top 10 by rating:")
            for idx, row in top.iterrows():
                print(f"  [{row['avg_rating']:.1f}] [{row['decision']}] {row['title'][:70]}...")


if __name__ == '__main__':
    main()
