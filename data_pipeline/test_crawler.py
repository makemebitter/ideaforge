"""
Quick test script for the OpenReview ICLR crawler.
This fetches a small sample of papers to verify the crawler is working.
"""

from openreview_crawler import OpenReviewCrawler, save_to_csv, save_to_json


def test_crawler():
    """Test the crawler with a quick fetch."""
    print("=" * 60)
    print("Testing OpenReview ICLR Crawler")
    print("=" * 60)
    
    # Initialize crawler (no credentials needed for public papers)
    crawler = OpenReviewCrawler()
    
    # Try crawling ICLR 2024 first (more stable data)
    print("\nTesting with ICLR 2024...")
    
    try:
        papers = crawler.crawl_iclr_papers(
            year='2024',
            only_accepted=True,
            include_reviews=False,
            verbose=True
        )
        
        if papers:
            print(f"\n[OK] Successfully fetched {len(papers)} papers")
            
            # Show sample paper
            sample = papers[0]
            print("\nSample paper:")
            print(f"  Title: {sample['title'][:80]}...")
            print(f"  Authors: {', '.join(sample['authors'][:3])}...")
            print(f"  Decision: {sample['decision']}")
            print(f"  Keywords: {', '.join(sample['keywords'][:5]) if sample['keywords'] else 'N/A'}")
            print(f"  PDF: {sample['pdf_url']}")
            
            # Save sample
            save_to_csv(papers[:10], 'test_sample.csv')
            save_to_json(papers[:10], 'test_sample.json')
            print("\n[OK] Saved sample to test_sample.csv and test_sample.json")
            
            return True
        else:
            print("\n[FAIL] No papers fetched")
            return False
            
    except Exception as e:
        print(f"\n[FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = test_crawler()
    
    if success:
        print("\n" + "=" * 60)
        print("Test passed! You can now run the full crawler:")
        print("  python openreview_crawler.py --year 2025")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("Test failed. Please check error messages above.")
        print("=" * 60)
