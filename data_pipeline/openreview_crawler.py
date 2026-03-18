"""
OpenReview ICLR Papers Crawler

This script crawls all ICLR papers from OpenReview.net for a specified year.
It uses the official OpenReview Python API to fetch paper metadata including:
- Title, authors, abstract
- Keywords, venue, decision
- PDF link, forum link
- Ratings and reviews (if available)

Usage:
    python openreview_crawler.py --year 2025 --output iclr_2025_papers.csv
    python openreview_crawler.py --year 2025 --output iclr_2025_papers.json --format json
    python openreview_crawler.py --year 2025 --submission-type all  # Get all submissions (not just accepted)
"""

import openreview
import argparse
import json
import csv
import os
from datetime import datetime
from pathlib import Path
from tqdm import tqdm
from typing import Optional, List, Dict, Any


class OpenReviewCrawler:
    """Crawler for OpenReview papers, specifically designed for ICLR."""
    
    # ICLR venue IDs by year (API v2 format for recent years)
    ICLR_VENUE_IDS = {
        '2026': 'ICLR.cc/2026/Conference',
        '2025': 'ICLR.cc/2025/Conference',
        '2024': 'ICLR.cc/2024/Conference',
        '2023': 'ICLR.cc/2023/Conference',
        '2022': 'ICLR.cc/2022/Conference',
        '2021': 'ICLR.cc/2021/Conference',
        '2020': 'ICLR.cc/2020/Conference',
        '2019': 'ICLR.cc/2019/Conference',
        '2018': 'ICLR.cc/2018/Conference',
    }
    
    # Decision categories for filtering
    ACCEPTED_DECISIONS = [
        'Accept (Oral)',
        'Accept (Spotlight)', 
        'Accept (Poster)',
        'Accept',
        'accept',
        'oral',
        'spotlight',
        'poster'
    ]

    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        """
        Initialize the crawler with OpenReview API clients.
        
        Args:
            username: OpenReview username (email). Optional for public papers.
            password: OpenReview password. Optional for public papers.
        """
        _BROWSER_UA = (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        )

        # API v2 client (for 2023+)
        self.client_v2 = openreview.api.OpenReviewClient(
            baseurl='https://api2.openreview.net',
            username=username,
            password=password
        )
        self.client_v2.headers['User-Agent'] = _BROWSER_UA
        self.client_v2.session.headers['User-Agent'] = _BROWSER_UA

        # API v1 client (for older conferences)
        self.client_v1 = openreview.Client(
            baseurl='https://api.openreview.net',
            username=username,
            password=password
        )
        if hasattr(self.client_v1, 'headers'):
            self.client_v1.headers['User-Agent'] = _BROWSER_UA
        if hasattr(self.client_v1, 'session'):
            self.client_v1.session.headers['User-Agent'] = _BROWSER_UA

        print("OpenReview API clients initialized successfully.")

    def get_venue_id(self, year: str) -> str:
        """Get the venue ID for a given year."""
        if year not in self.ICLR_VENUE_IDS:
            raise ValueError(f"Year {year} not supported. Supported years: {list(self.ICLR_VENUE_IDS.keys())}")
        return self.ICLR_VENUE_IDS[year]

    def _get_paper_content(self, note: Any, field: str, default: Any = None) -> Any:
        """
        Safely extract content from a paper note.
        Handles both API v1 and v2 formats.
        """
        if hasattr(note, 'content') and note.content:
            content = note.content
            if field in content:
                value = content[field]
                # API v2 wraps values in {'value': ...}
                if isinstance(value, dict) and 'value' in value:
                    return value['value']
                return value
        return default

    def crawl_iclr_papers(
        self,
        year: str,
        only_accepted: bool = True,
        include_reviews: bool = False,
        verbose: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Crawl all ICLR papers for a given year.
        
        Args:
            year: The year to crawl (e.g., '2025')
            only_accepted: If True, only fetch accepted papers
            include_reviews: If True, include review scores and text
            verbose: Print progress information
            
        Returns:
            List of paper dictionaries
        """
        venue_id = self.get_venue_id(year)
        papers = []
        
        if verbose:
            print(f"\nCrawling ICLR {year} papers from {venue_id}...")
        
        # Use API v2 for 2023+ conferences
        use_v2 = int(year) >= 2023
        client = self.client_v2 if use_v2 else self.client_v1
        
        try:
            if only_accepted:
                # Fetch accepted papers using venue ID
                if verbose:
                    print("Fetching accepted papers...")
                
                submissions = list(client.get_all_notes(
                    content={'venueid': venue_id},
                    details='directReplies'
                ))
            else:
                # Fetch all submissions
                if verbose:
                    print("Fetching all submissions...")
                
                # Try different invitation formats
                submissions = []
                invitation_formats = [
                    f'{venue_id}/-/Submission',
                    f'{venue_id}/-/Blind_Submission',
                ]
                
                for invitation in invitation_formats:
                    try:
                        notes = list(client.get_all_notes(
                            invitation=invitation,
                            details='directReplies'
                        ))
                        submissions.extend(notes)
                        if verbose and notes:
                            print(f"  Found {len(notes)} papers from {invitation}")
                    except Exception as e:
                        if verbose:
                            print(f"  Could not fetch from {invitation}: {e}")
            
            if verbose:
                print(f"Total submissions found: {len(submissions)}")
            
            # Process each submission
            for note in tqdm(submissions, desc="Processing papers", disable=not verbose):
                paper = self._process_paper(note, year, venue_id, include_reviews)
                
                # Filter by decision if needed
                if only_accepted:
                    decision = paper.get('decision', '')
                    if decision and not any(acc.lower() in decision.lower() for acc in self.ACCEPTED_DECISIONS):
                        continue
                
                papers.append(paper)
                
        except Exception as e:
            print(f"Error crawling papers: {e}")
            raise
        
        if verbose:
            print(f"\nSuccessfully crawled {len(papers)} papers.")
        
        return papers

    def _process_paper(
        self,
        note: Any,
        year: str,
        venue_id: str,
        include_reviews: bool = False
    ) -> Dict[str, Any]:
        """Process a single paper note and extract relevant information."""
        
        # Basic metadata
        paper = {
            'id': note.id,
            'forum': note.forum,
            'title': self._get_paper_content(note, 'title', 'N/A'),
            'authors': self._get_paper_content(note, 'authors', []),
            'authorids': self._get_paper_content(note, 'authorids', []),
            'abstract': self._get_paper_content(note, 'abstract', 'N/A'),
            'keywords': self._get_paper_content(note, 'keywords', []),
            'venue': self._get_paper_content(note, 'venue', venue_id),
            'venueid': self._get_paper_content(note, 'venueid', venue_id),
            'decision': self._get_paper_content(note, 'decision', ''),
            'year': year,
            'pdf_url': f"https://openreview.net/pdf?id={note.forum}",
            'forum_url': f"https://openreview.net/forum?id={note.forum}",
            'created_date': datetime.fromtimestamp(note.cdate / 1000).isoformat() if note.cdate else None,
            'modified_date': datetime.fromtimestamp(note.mdate / 1000).isoformat() if note.mdate else None,
        }
        
        # Additional content fields that may exist
        optional_fields = [
            'primary_area', 'TLDR', 'code', 'supplementary_material',
            'submission_track', 'presentation_type'
        ]
        for field in optional_fields:
            value = self._get_paper_content(note, field)
            if value:
                paper[field] = value
        
        # Process reviews if requested
        if include_reviews and hasattr(note, 'details') and note.details:
            replies = note.details.get('directReplies', [])
            reviews = self._extract_reviews(replies)
            paper['reviews'] = reviews
            paper['avg_rating'] = self._calculate_avg_rating(reviews)
            paper['num_reviews'] = len(reviews)
        
        return paper

    def _extract_reviews(self, replies: List[Any]) -> List[Dict[str, Any]]:
        """Extract review information from paper replies."""
        reviews = []
        for reply in replies:
            # Check if this is a review
            invitation = getattr(reply, 'invitation', '') or ''
            if 'Official_Review' in invitation or 'Review' in invitation:
                content = getattr(reply, 'content', {})
                review = {
                    'rating': self._extract_rating(content),
                    'confidence': self._extract_value(content, 'confidence'),
                    'summary': self._extract_value(content, 'summary'),
                    'strengths': self._extract_value(content, 'strengths'),
                    'weaknesses': self._extract_value(content, 'weaknesses'),
                }
                reviews.append(review)
        return reviews

    def _extract_rating(self, content: Dict) -> Optional[float]:
        """Extract numerical rating from review content."""
        for key in ['rating', 'recommendation', 'score']:
            if key in content:
                value = content[key]
                if isinstance(value, dict) and 'value' in value:
                    value = value['value']
                if isinstance(value, (int, float)):
                    return float(value)
                if isinstance(value, str):
                    # Extract number from strings like "8: Strong Accept"
                    try:
                        return float(value.split(':')[0].strip())
                    except:
                        pass
        return None

    def _extract_value(self, content: Dict, key: str) -> Optional[str]:
        """Extract a string value from content, handling API v2 format."""
        if key in content:
            value = content[key]
            if isinstance(value, dict) and 'value' in value:
                return value['value']
            return value
        return None

    def _calculate_avg_rating(self, reviews: List[Dict]) -> Optional[float]:
        """Calculate average rating from reviews."""
        ratings = [r['rating'] for r in reviews if r['rating'] is not None]
        if ratings:
            return round(sum(ratings) / len(ratings), 2)
        return None


def save_to_csv(papers: List[Dict], filepath: str):
    """Save papers to CSV file."""
    if not papers:
        print("No papers to save.")
        return
    
    # Flatten nested fields for CSV
    flat_papers = []
    for paper in papers:
        flat = paper.copy()
        # Convert lists to strings
        if 'authors' in flat and isinstance(flat['authors'], list):
            flat['authors'] = '; '.join(flat['authors'])
        if 'authorids' in flat and isinstance(flat['authorids'], list):
            flat['authorids'] = '; '.join(flat['authorids'])
        if 'keywords' in flat and isinstance(flat['keywords'], list):
            flat['keywords'] = '; '.join(flat['keywords'])
        # Remove complex nested fields
        flat.pop('reviews', None)
        flat_papers.append(flat)
    
    # Get all unique keys
    all_keys = set()
    for paper in flat_papers:
        all_keys.update(paper.keys())
    
    # Define column order
    priority_columns = [
        'title', 'authors', 'abstract', 'keywords', 'decision', 'venue', 
        'year', 'pdf_url', 'forum_url', 'avg_rating', 'num_reviews'
    ]
    columns = [c for c in priority_columns if c in all_keys]
    columns.extend(sorted(k for k in all_keys if k not in columns))
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(flat_papers)
    
    print(f"Saved {len(papers)} papers to {filepath}")


def save_to_json(papers: List[Dict], filepath: str):
    """Save papers to JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(papers)} papers to {filepath}")


def main():
    parser = argparse.ArgumentParser(
        description='Crawl ICLR papers from OpenReview.net',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Crawl all accepted ICLR 2025 papers
  python openreview_crawler.py --year 2025

  # Crawl all submissions (including rejected)
  python openreview_crawler.py --year 2025 --submission-type all

  # Save as JSON with reviews
  python openreview_crawler.py --year 2025 --format json --include-reviews

  # Use authentication for private data
  python openreview_crawler.py --year 2025 --username your@email.com --password yourpassword
        """
    )
    
    parser.add_argument(
        '--year', '-y',
        type=str,
        default='2025',
        help='ICLR year to crawl (default: 2025)'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path (default: iclr_{year}_papers.csv)'
    )
    parser.add_argument(
        '--format', '-f',
        choices=['csv', 'json'],
        default='csv',
        help='Output format (default: csv)'
    )
    parser.add_argument(
        '--submission-type', '-t',
        choices=['accepted', 'all'],
        default='accepted',
        help='Which submissions to crawl (default: accepted)'
    )
    parser.add_argument(
        '--include-reviews', '-r',
        action='store_true',
        help='Include review scores and text (slower)'
    )
    parser.add_argument(
        '--username', '-u',
        type=str,
        default=None,
        help='OpenReview username (email)'
    )
    parser.add_argument(
        '--password', '-p',
        type=str,
        default=None,
        help='OpenReview password'
    )
    
    args = parser.parse_args()
    
    # Set default output filename
    if not args.output:
        args.output = f"iclr_{args.year}_papers.{args.format}"
    else:
        # If output is a directory, append default filename inside it
        out_path = Path(args.output)
        if out_path.is_dir() or (not out_path.suffix and not out_path.exists()):
            out_path.mkdir(parents=True, exist_ok=True)
            args.output = str(out_path / f"iclr_{args.year}_papers.{args.format}")
    
    # Try to load credentials from config file if not provided
    username = args.username
    password = args.password
    
    if not username or not password:
        try:
            from config import EMAIL, PASSWORD
            if EMAIL and PASSWORD:
                username = EMAIL
                password = PASSWORD
                print("Using credentials from config.py")
        except ImportError:
            pass
    
    # Initialize crawler
    crawler = OpenReviewCrawler(username=username, password=password)
    
    # Crawl papers
    only_accepted = args.submission_type == 'accepted'
    papers = crawler.crawl_iclr_papers(
        year=args.year,
        only_accepted=only_accepted,
        include_reviews=args.include_reviews
    )
    
    # Save results
    if args.format == 'csv':
        save_to_csv(papers, args.output)
    else:
        save_to_json(papers, args.output)
    
    # Print summary
    print(f"\nSummary:")
    print(f"  Year: ICLR {args.year}")
    print(f"  Total papers: {len(papers)}")
    print(f"  Output file: {args.output}")
    
    if papers:
        # Count by decision
        decisions = {}
        for paper in papers:
            dec = paper.get('decision', 'Unknown')
            decisions[dec] = decisions.get(dec, 0) + 1
        
        print(f"\nPapers by decision:")
        for dec, count in sorted(decisions.items(), key=lambda x: -x[1]):
            print(f"  {dec}: {count}")


if __name__ == '__main__':
    main()
