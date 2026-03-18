"""
Enhanced crawler that fetches papers with reviews and decisions.
"""

import openreview
import pandas as pd
from tqdm import tqdm
from typing import Optional, List, Dict, Any
import time


class EnhancedCrawler:
    """Enhanced crawler that properly fetches reviews and decisions."""
    
    VENUE_IDS = {
        '2026': 'ICLR.cc/2026/Conference',
        '2025': 'ICLR.cc/2025/Conference',
        '2024': 'ICLR.cc/2024/Conference',
    }
    
    def __init__(self):
        self.client = openreview.api.OpenReviewClient(
            baseurl='https://api2.openreview.net'
        )
        print("OpenReview client initialized.")
    
    def get_decision_from_venue(self, venue: str) -> str:
        """Extract decision from venue string."""
        venue_lower = venue.lower() if venue else ''
        if 'oral' in venue_lower:
            return 'Accept (Oral)'
        elif 'spotlight' in venue_lower:
            return 'Accept (Spotlight)'
        elif 'poster' in venue_lower:
            return 'Accept (Poster)'
        elif 'reject' in venue_lower or 'withdrawn' in venue_lower:
            return 'Reject'
        elif 'conditional' in venue_lower:
            return 'Conditional Accept'
        elif venue and ('ICLR' in venue or 'iclr' in venue_lower):
            return 'Accept'  # Generic accept if venue mentions ICLR
        return ''
    
    def crawl_year(self, year: str, fetch_all: bool = True) -> List[Dict]:
        """
        Crawl papers for a given year with reviews.
        
        Args:
            year: Year to crawl
            fetch_all: If True, fetch all submissions. If False, only accepted.
        """
        venue_id = self.VENUE_IDS.get(year)
        if not venue_id:
            raise ValueError(f"Year {year} not supported")
        
        print(f"\nCrawling ICLR {year}...")
        
        papers = []
        
        if fetch_all:
            # Fetch all submissions
            print("Fetching all submissions...")
            submissions = list(self.client.get_all_notes(
                invitation=f'{venue_id}/-/Submission',
                details='replies'
            ))
        else:
            # Fetch only accepted
            print("Fetching accepted papers...")
            submissions = list(self.client.get_all_notes(
                content={'venueid': venue_id},
                details='replies'
            ))
        
        print(f"Found {len(submissions)} submissions")
        
        for note in tqdm(submissions, desc="Processing"):
            paper = self._process_paper(note, year, venue_id)
            papers.append(paper)
        
        return papers
    
    def _get_content(self, note, field: str, default=None):
        """Extract content from note."""
        if hasattr(note, 'content') and note.content:
            value = note.content.get(field)
            if value is None:
                return default
            if isinstance(value, dict) and 'value' in value:
                return value['value']
            return value
        return default
    
    def _process_paper(self, note, year: str, venue_id: str) -> Dict:
        """Process a paper and extract all info including reviews."""
        
        # Basic info
        venue = self._get_content(note, 'venue', '')
        decision = self._get_content(note, 'decision', '')
        
        # Infer decision from venue if not explicit
        if not decision:
            decision = self.get_decision_from_venue(venue)
        
        paper = {
            'id': note.id,
            'forum': note.forum,
            'title': self._get_content(note, 'title', 'N/A'),
            'authors': self._get_content(note, 'authors', []),
            'abstract': self._get_content(note, 'abstract', 'N/A'),
            'keywords': self._get_content(note, 'keywords', []),
            'venue': venue,
            'decision': decision,
            'year': int(year),
            'pdf_url': f"https://openreview.net/pdf?id={note.forum}",
            'forum_url': f"https://openreview.net/forum?id={note.forum}",
            'primary_area': self._get_content(note, 'primary_area', ''),
            'TLDR': self._get_content(note, 'TLDR', ''),
        }
        
        # Extract reviews
        reviews = self._extract_reviews(note)
        paper['num_reviews'] = len(reviews)
        
        if reviews:
            ratings = [r['rating'] for r in reviews if r['rating'] is not None]
            confidences = [r['confidence'] for r in reviews if r['confidence'] is not None]
            
            paper['avg_rating'] = round(sum(ratings) / len(ratings), 2) if ratings else None
            paper['min_rating'] = min(ratings) if ratings else None
            paper['max_rating'] = max(ratings) if ratings else None
            paper['ratings'] = ratings
            paper['avg_confidence'] = round(sum(confidences) / len(confidences), 2) if confidences else None
        else:
            paper['avg_rating'] = None
            paper['min_rating'] = None
            paper['max_rating'] = None
            paper['ratings'] = []
            paper['avg_confidence'] = None
        
        return paper
    
    def _extract_reviews(self, note) -> List[Dict]:
        """Extract reviews from note details."""
        reviews = []
        
        # Check if we have replies in details
        if hasattr(note, 'details') and note.details:
            replies = note.details.get('replies', [])
            
            for reply in replies:
                # Handle both dict and object formats
                if isinstance(reply, dict):
                    # Check invitations list (API v2 format)
                    invitations = reply.get('invitations', [])
                    invitation_str = ' '.join(invitations) if invitations else reply.get('invitation', '')
                    content = reply.get('content', {})
                else:
                    invitations = getattr(reply, 'invitations', [])
                    invitation_str = ' '.join(invitations) if invitations else getattr(reply, 'invitation', '')
                    content = getattr(reply, 'content', {})
                
                # Check if this is a review
                if 'Official_Review' in str(invitation_str):
                    review = {
                        'rating': self._extract_rating(content),
                        'confidence': self._extract_confidence(content),
                    }
                    reviews.append(review)
        
        return reviews
    
    def _extract_rating(self, content: Dict) -> Optional[float]:
        """Extract rating from review content."""
        for key in ['rating', 'recommendation', 'score', 'soundness']:
            if key in content:
                value = content[key]
                if isinstance(value, dict) and 'value' in value:
                    value = value['value']
                if isinstance(value, (int, float)):
                    return float(value)
                if isinstance(value, str):
                    try:
                        # Extract number from "8: Strong Accept" format
                        return float(value.split(':')[0].strip())
                    except:
                        pass
        return None
    
    def _extract_confidence(self, content: Dict) -> Optional[float]:
        """Extract confidence from review content."""
        if 'confidence' in content:
            value = content['confidence']
            if isinstance(value, dict) and 'value' in value:
                value = value['value']
            if isinstance(value, (int, float)):
                return float(value)
            if isinstance(value, str):
                try:
                    return float(value.split(':')[0].strip())
                except:
                    pass
        return None


def save_papers(papers: List[Dict], filepath: str):
    """Save papers to CSV."""
    flat_papers = []
    for p in papers:
        flat = p.copy()
        # Convert lists to strings
        if isinstance(flat.get('authors'), list):
            flat['authors'] = '; '.join(flat['authors'])
        if isinstance(flat.get('keywords'), list):
            flat['keywords'] = '; '.join(str(k) for k in flat['keywords'])
        if isinstance(flat.get('ratings'), list):
            flat['ratings'] = ', '.join(str(r) for r in flat['ratings'])
        flat_papers.append(flat)
    
    df = pd.DataFrame(flat_papers)
    
    # Reorder columns
    priority_cols = [
        'title', 'decision', 'avg_rating', 'min_rating', 'max_rating', 
        'num_reviews', 'ratings', 'avg_confidence', 'venue', 'year',
        'authors', 'abstract', 'keywords', 'primary_area', 'TLDR',
        'pdf_url', 'forum_url', 'id', 'forum'
    ]
    
    cols = [c for c in priority_cols if c in df.columns]
    cols.extend([c for c in df.columns if c not in cols])
    df = df[cols]
    
    df.to_csv(filepath, index=False)
    print(f"Saved {len(df)} papers to {filepath}")
    
    return df


def main():
    crawler = EnhancedCrawler()
    
    all_papers = []
    
    for year in ['2026', '2025', '2024']:
        papers = crawler.crawl_year(year, fetch_all=True)
        all_papers.extend(papers)
        
        # Save individual year
        df = save_papers(papers, f'iclr_{year}_with_reviews.csv')
        
        # Show stats
        print(f"\nICLR {year} Statistics:")
        print(f"  Total submissions: {len(papers)}")
        
        decisions = {}
        for p in papers:
            dec = p.get('decision') or 'Unknown/Pending'
            decisions[dec] = decisions.get(dec, 0) + 1
        
        print("  By decision:")
        for dec, count in sorted(decisions.items(), key=lambda x: -x[1]):
            print(f"    {dec}: {count}")
        
        ratings = [p['avg_rating'] for p in papers if p.get('avg_rating')]
        if ratings:
            print(f"  Papers with ratings: {len(ratings)}")
            print(f"  Avg rating: {sum(ratings)/len(ratings):.2f}")
        
        print()
    
    # Save combined
    save_papers(all_papers, 'iclr_all_with_reviews.csv')
    print(f"\nTotal: {len(all_papers)} papers across all years")


if __name__ == '__main__':
    main()
