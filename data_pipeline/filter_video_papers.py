"""
Filter ICLR papers for video generation related topics.
"""

import pandas as pd
import re

def filter_video_papers():
    df = pd.read_csv('iclr_all_titles_abstracts.csv')
    
    # Video generation related keywords (case insensitive)
    video_keywords = [
        r'video\s*generation',
        r'video\s*synthesis', 
        r'video\s*diffusion',
        r'text[\s\-]*to[\s\-]*video',
        r'video\s*prediction',
        r'video\s*model',
        r'video\s*transformer',
        r'video\s*autoencoder',
        r'video\s*vae',
        r'video\s*gan',
        r'video\s*generative',
        r'generate\s*video',
        r'generating\s*video',
        r'video\s*creation',
        r'video\s*editing',
        r'video\s*inpainting',
        r'video\s*completion',
        r'video\s*interpolation',
        r'video\s*super[\s\-]*resolution',
        r'image[\s\-]*to[\s\-]*video',
        r'motion\s*generation',
        r'motion\s*synthesis',
        r'temporal\s*generation',
        r'frame\s*generation',
        r'frame\s*prediction',
        r'frame\s*interpolation',
        r'sora',  # OpenAI's video model
        r'video\s*llm',
        r'video\s*foundation',
        r'world\s*model.*video',
        r'video.*world\s*model',
    ]
    
    pattern = '|'.join(video_keywords)
    
    def is_video_related(row):
        title = str(row['title']).lower()
        abstract = str(row['abstract']).lower()
        keywords = str(row['keywords']).lower() if pd.notna(row['keywords']) else ''
        
        combined_text = f'{title} {abstract} {keywords}'
        return bool(re.search(pattern, combined_text, re.IGNORECASE))
    
    # Filter
    video_papers = df[df.apply(is_video_related, axis=1)].copy()
    
    print(f'Found {len(video_papers)} video-related papers out of {len(df)} total')
    print(f'\nBy year:')
    print(video_papers['year'].value_counts().to_string())
    
    # Save for review
    video_papers.to_csv('iclr_video_candidates.csv', index=False)
    print(f'\nSaved to iclr_video_candidates.csv')
    
    # Print titles for quick review
    print('\n' + '='*80)
    print('VIDEO-RELATED PAPER TITLES:')
    print('='*80)
    for idx, row in video_papers.iterrows():
        year = row['year']
        title = row['title']
        print(f"[{year}] {title}")
    
    return video_papers

if __name__ == '__main__':
    filter_video_papers()
