"""
Crawl ICML papers and reviews from OpenReview API.

Fetches all accepted papers for a given year, filters by keywords,
and downloads reviews + optionally PDFs.

Usage:
    python crawl_icml.py --year 2024                           # All accepted ICML 2024
    python crawl_icml.py --year 2025 --keywords "video,diffusion"  # Filter by keywords
    python crawl_icml.py --year 2024 --reviews-only            # Just reviews, no PDFs
    python crawl_icml.py --year 2024 --dry-run                 # Preview what would be fetched

Output:
    icml_papers/icml_<year>_papers.csv       # Paper metadata
    icml_papers/<year>/<title>_reviews.json   # Reviews per paper
    icml_papers/<year>/<title>.pdf            # PDFs (if not --reviews-only)
"""

import csv
import re
import json
import time
import argparse
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from concurrent.futures import ThreadPoolExecutor, as_completed


HEADERS = {"User-Agent": "Mozilla/5.0 (research-bot; academic use)"}
OUTPUT_DIR = Path(__file__).parent / "research_data" / "icml"

BATCH_SIZE = 200  # OpenReview API max per request


def _safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def _val(content: dict, field: str):
    """Extract value from OpenReview API v2 content field."""
    v = content.get(field, "")
    return v.get("value", v) if isinstance(v, dict) else v


def api_get(url: str, retries: int = 3) -> dict:
    for attempt in range(retries):
        try:
            req = Request(url, headers=HEADERS)
            return json.loads(urlopen(req, timeout=20).read())
        except HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(2 ** attempt)
                continue
            raise
    return {"notes": []}


def _is_accepted(venue_str: str, venueid_str: str, year: int) -> bool:
    """Determine if a paper is accepted based on venue/venueid fields.

    Accepted papers have venue like "ICML 2025 poster", "ICML 2025 oral", etc.
    Excluded: "Submitted to ICML 2025" (pending/rejected), "Retracted", "Withdrawn",
    or papers explicitly marked as rejected.
    """
    venue_lower = str(venue_str).lower()
    # Explicit rejection/withdrawal/retraction
    for reject_term in ("reject", "withdraw", "retract", "submitted to"):
        if reject_term in venue_lower:
            return False
    # Must have a non-empty venue mentioning the conference
    if venue_str and f"icml" in venue_lower:
        return True
    # Fallback: check venueid (e.g. "ICML.cc/2025/Conference")
    if venueid_str and f"ICML.cc/{year}/Conference" in str(venueid_str):
        return True
    return False


def fetch_all_papers(year: int) -> list[dict]:
    """Fetch all submissions for ICML <year> from OpenReview."""
    venue = f"ICML.cc/{year}/Conference"
    papers = []
    offset = 0
    total_submissions = 0
    skipped = 0

    print(f"Fetching ICML {year} papers from OpenReview...")

    while True:
        url = (f"https://api2.openreview.net/notes?"
               f"invitation={venue}/-/Submission&limit={BATCH_SIZE}&offset={offset}")
        data = api_get(url)
        notes = data.get("notes", [])

        # On first batch, report total count from API
        if offset == 0 and "count" in data:
            total_submissions = data["count"]
            print(f"  Total submissions in OpenReview: {total_submissions}")

        if not notes:
            break

        for note in notes:
            content = note.get("content", {})
            venue_str = _val(content, "venue")
            venueid_str = _val(content, "venueid")

            if not _is_accepted(venue_str, venueid_str, year):
                skipped += 1
                continue

            title = _val(content, "title")
            abstract = _val(content, "abstract")
            keywords = _val(content, "keywords")
            if isinstance(keywords, list):
                keywords = ", ".join(keywords)
            tldr = _val(content, "TLDR")
            forum_id = note.get("forum", note.get("id", ""))

            papers.append({
                "title": title,
                "abstract": abstract,
                "keywords": keywords,
                "tldr": tldr,
                "venue": venue_str,
                "year": year,
                "forum_id": forum_id,
                "forum_url": f"https://openreview.net/forum?id={forum_id}",
                "pdf_url": f"https://openreview.net/pdf?id={forum_id}",
            })

        offset += BATCH_SIZE
        print(f"  Fetched {offset} submissions so far ({len(papers)} accepted, {skipped} skipped)...")

    print(f"  Total accepted: {len(papers)} / {total_submissions} submissions ({skipped} skipped)")
    return papers


def filter_by_keywords(papers: list[dict], keywords: list[str]) -> list[dict]:
    """Filter papers whose title/abstract/keywords contain any of the given terms."""
    if not keywords:
        return papers

    filtered = []
    kw_lower = [k.lower().strip() for k in keywords]
    for p in papers:
        searchable = (p["title"] + " " + p["abstract"] + " " + p["keywords"]).lower()
        if any(k in searchable for k in kw_lower):
            filtered.append(p)
    return filtered


def fetch_reviews_for_paper(paper: dict, output_dir: Path, delay: float = 0.3) -> dict:
    """Fetch reviews for a single paper from OpenReview."""
    title = paper["title"]
    forum_id = paper["forum_id"]

    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
    safe_title = re.sub(r'\s+', '_', safe_title.strip())[:80]
    reviews_path = output_dir / f"{safe_title}_reviews.json"

    if reviews_path.exists() and reviews_path.stat().st_size > 100:
        return {"title": title, "status": "exists", "path": str(reviews_path)}

    try:
        data = api_get(f"https://api2.openreview.net/notes?forum={forum_id}")
        notes = data.get("notes", [])

        reviews = []
        for note in notes:
            invs = note.get("invitations", [])
            inv_str = invs[0] if invs else ""
            if "Official_Review" not in inv_str:
                continue

            c = note.get("content", {})
            reviews.append({
                "rating": _val(c, "rating"),
                "confidence": _val(c, "confidence"),
                "soundness": _val(c, "soundness"),
                "presentation": _val(c, "presentation"),
                "contribution": _val(c, "contribution"),
                "summary": _val(c, "summary"),
                "strengths": _val(c, "strengths"),
                "weaknesses": _val(c, "weaknesses"),
                "questions": _val(c, "questions"),
                "limitations": _val(c, "limitations"),
            })

        if not reviews:
            return {"title": title, "status": "no_reviews", "notes": len(notes)}

        review_data = {
            "title": title,
            "forum_id": forum_id,
            "forum_url": paper["forum_url"],
            "venue": paper["venue"],
            "num_reviews": len(reviews),
            "reviews": reviews,
        }

        with open(reviews_path, "w", encoding="utf-8") as f:
            json.dump(review_data, f, indent=2, ensure_ascii=False)

        time.sleep(delay)
        return {"title": title, "status": "fetched", "path": str(reviews_path), "num_reviews": len(reviews)}

    except Exception as e:
        return {"title": title, "status": "error", "reason": str(e)}


def save_csv(papers: list[dict], output_path: Path):
    """Save paper metadata as CSV."""
    if not papers:
        return
    fieldnames = ["title", "venue", "year", "keywords", "tldr", "abstract", "forum_url", "pdf_url", "forum_id"]
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(papers)
    print(f"Saved {len(papers)} papers to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Crawl ICML papers and reviews from OpenReview")
    parser.add_argument("--year", "-y", type=int, required=True, help="ICML year (e.g. 2024, 2025)")
    parser.add_argument("--keywords", "-k", type=str, default=None,
                        help="Comma-separated keywords to filter papers (e.g. 'video,diffusion,generation')")
    parser.add_argument("--output", type=str, default=str(OUTPUT_DIR), help="Output directory")
    parser.add_argument("--reviews-only", action="store_true", help="Skip PDF downloads")
    parser.add_argument("--no-reviews", action="store_true", help="Skip review fetching")
    parser.add_argument("--workers", type=int, default=2, help="Parallel workers (default: 2)")
    parser.add_argument("--dry-run", action="store_true", help="Just list papers without downloading")
    args = parser.parse_args()

    output_dir = Path(args.output)
    year_dir = output_dir / str(args.year)
    year_dir.mkdir(parents=True, exist_ok=True)

    # Fetch papers
    papers = fetch_all_papers(args.year)

    if args.keywords:
        kw_list = [k.strip() for k in args.keywords.split(",")]
        papers = filter_by_keywords(papers, kw_list)
        print(f"After keyword filter ({args.keywords}): {len(papers)} papers")

    if not papers:
        print("No papers found.")
        return

    # Save CSV
    csv_path = output_dir / f"icml_{args.year}_papers.csv"
    save_csv(papers, csv_path)

    if args.dry_run:
        for p in papers[:20]:
            print(f"  {_safe(p['venue'][:25]):25s} | {_safe(p['title'][:65])}")
        if len(papers) > 20:
            print(f"  ... and {len(papers) - 20} more")
        return

    # Fetch reviews
    if not args.no_reviews:
        print(f"\nFetching reviews for {len(papers)} papers...\n")
        fetched = skipped = failed = 0

        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {
                pool.submit(fetch_reviews_for_paper, p, year_dir, 0.3): p
                for p in papers
            }
            for future in as_completed(futures):
                r = future.result()
                status = r["status"]
                title = _safe(r["title"][:55])
                if status == "fetched":
                    fetched += 1
                    n = r.get("num_reviews", 0)
                    print(f"  [OK]   {n} reviews | {title}")
                elif status == "exists":
                    skipped += 1
                else:
                    failed += 1
                    if status != "no_reviews":
                        print(f"  [FAIL] {status:12s} | {title}")

        print(f"\nReviews: {fetched} fetched, {skipped} cached, {failed} failed")

    # Download PDFs
    if not args.reviews_only and not args.no_reviews:
        print(f"\nPDF download not implemented yet - use --reviews-only for now")
        print(f"PDFs can be downloaded from: https://openreview.net/pdf?id=<forum_id>")

    print(f"\nDone! Output in {output_dir}/")


if __name__ == "__main__":
    main()
