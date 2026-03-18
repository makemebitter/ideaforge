"""
Download PDFs and reviewer reviews of high-scoring ICLR papers.

Usage:
    python crawl_papers.py                          # Download PDFs + reviews, rating >= 7.0
    python crawl_papers.py --min-rating 6.5         # Custom threshold
    python crawl_papers.py --min-rating 6.0 --limit 50  # Top 50 papers rated 6.0+
    python crawl_papers.py --category video-diffusion    # Filter by category
    python crawl_papers.py --no-reviews             # Skip review fetching
    python crawl_papers.py --reviews-only           # Only fetch reviews (skip PDFs)
    python crawl_papers.py --dry-run                # Just list what would be downloaded

Papers saved to: papers/<category>/<rating>_<title>.pdf
Reviews saved to: papers/<category>/<rating>_<title>_reviews.json
"""

import csv
import re
import time
import argparse
import json
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed


CSV_PATH = Path(__file__).parent / "iclr_video_generation_accepted.csv"
OUTPUT_DIR = Path(__file__).parent / "papers"
INDEX_PATH = OUTPUT_DIR / "index.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
}


def _safe(text: str) -> str:
    """Make text safe for Windows console output."""
    return text.encode("ascii", "replace").decode("ascii")


def load_papers(csv_path: Path = CSV_PATH) -> list[dict]:
    with open(csv_path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def filter_papers(
    papers: list[dict],
    min_rating: float = 7.0,
    category: str = None,
    limit: int = None,
) -> list[dict]:
    filtered = []
    for p in papers:
        try:
            rating = float(p["avg_rating"])
        except (ValueError, KeyError):
            continue
        if rating < min_rating:
            continue
        if category and p.get("category", "") != category:
            continue
        if not p.get("pdf_url", "").startswith("http"):
            continue
        filtered.append(p)

    filtered.sort(key=lambda x: float(x["avg_rating"]), reverse=True)
    if limit:
        filtered = filtered[:limit]
    return filtered


def sanitize_filename(title: str, max_len: int = 80) -> str:
    safe = re.sub(r'[<>:"/\\|?*]', '', title)
    safe = re.sub(r'\s+', '_', safe.strip())
    return safe[:max_len]


def download_pdf(paper: dict, output_dir: Path, delay: float = 0.5) -> dict:
    """Download a single PDF. Returns status dict."""
    rating = float(paper["avg_rating"])
    title = paper["title"]
    category = paper.get("category", "uncategorized")
    pdf_url = paper["pdf_url"]

    safe_title = sanitize_filename(title)
    filename = f"{rating:.1f}_{safe_title}.pdf"
    cat_dir = output_dir / category
    cat_dir.mkdir(parents=True, exist_ok=True)
    filepath = cat_dir / filename

    if filepath.exists() and filepath.stat().st_size > 10_000:
        return {"title": title, "status": "exists", "path": str(filepath)}

    try:
        req = Request(pdf_url, headers=HEADERS)
        with urlopen(req, timeout=30) as resp:
            data = resp.read()

        if len(data) < 5_000:
            return {"title": title, "status": "too_small", "size": len(data)}

        filepath.write_bytes(data)
        time.sleep(delay)
        return {
            "title": title,
            "status": "downloaded",
            "path": str(filepath),
            "size": len(data),
        }

    except HTTPError as e:
        return {"title": title, "status": "http_error", "code": e.code}
    except URLError as e:
        return {"title": title, "status": "url_error", "reason": str(e.reason)}
    except Exception as e:
        return {"title": title, "status": "error", "reason": str(e)}


def fetch_reviews(paper: dict, output_dir: Path, delay: float = 0.3) -> dict:
    """Fetch reviewer reviews from OpenReview API. Returns status dict."""
    title = paper["title"]
    category = paper.get("category", "uncategorized")
    rating = float(paper["avg_rating"])
    forum_url = paper.get("forum_url", "")

    if not forum_url or "openreview.net" not in forum_url:
        return {"title": title, "status": "no_forum_url"}

    # Extract forum ID from URL
    forum_id = forum_url.split("id=")[-1].split("&")[0] if "id=" in forum_url else ""
    if not forum_id:
        return {"title": title, "status": "bad_forum_url"}

    safe_title = sanitize_filename(title)
    cat_dir = output_dir / category
    cat_dir.mkdir(parents=True, exist_ok=True)
    reviews_path = cat_dir / f"{rating:.1f}_{safe_title}_reviews.json"

    if reviews_path.exists() and reviews_path.stat().st_size > 100:
        return {"title": title, "status": "exists", "path": str(reviews_path)}

    try:
        api_url = f"https://api2.openreview.net/notes?forum={forum_id}"
        # Retry up to 3 times on transient failures
        data = None
        for attempt in range(3):
            try:
                req = Request(api_url, headers=HEADERS)
                data = json.loads(urlopen(req, timeout=15).read())
                break
            except HTTPError as e:
                if e.code == 429 or e.code >= 500:
                    time.sleep(2 ** attempt)
                    continue
                raise
        if data is None:
            return {"title": title, "status": "http_error_after_retries"}
        notes = data.get("notes", [])

        def extract_val(content, field):
            v = content.get(field, "")
            return v.get("value", v) if isinstance(v, dict) else v

        reviews = []
        for note in notes:
            invitations = note.get("invitations", [])
            inv_str = invitations[0] if invitations else note.get("invitation", "")
            content = note.get("content", {})

            is_review = ("Official_Review" in inv_str or
                         "rating" in content or
                         "soundness" in content)
            if not is_review:
                continue

            reviews.append({
                "rating": extract_val(content, "rating"),
                "confidence": extract_val(content, "confidence"),
                "soundness": extract_val(content, "soundness"),
                "presentation": extract_val(content, "presentation"),
                "contribution": extract_val(content, "contribution"),
                "summary": extract_val(content, "summary"),
                "strengths": extract_val(content, "strengths"),
                "weaknesses": extract_val(content, "weaknesses"),
                "questions": extract_val(content, "questions"),
                "limitations": extract_val(content, "limitations"),
                "recommendation": extract_val(content, "recommendation"),
            })

        if not reviews:
            return {"title": title, "status": "no_reviews_found", "notes_count": len(notes)}

        review_data = {
            "title": title,
            "forum_id": forum_id,
            "forum_url": forum_url,
            "avg_rating": rating,
            "num_reviews": len(reviews),
            "reviews": reviews,
        }

        with open(reviews_path, "w", encoding="utf-8") as f:
            json.dump(review_data, f, indent=2, ensure_ascii=False)

        time.sleep(delay)
        return {
            "title": title,
            "status": "fetched",
            "path": str(reviews_path),
            "num_reviews": len(reviews),
        }

    except HTTPError as e:
        return {"title": title, "status": "http_error", "code": e.code}
    except URLError as e:
        return {"title": title, "status": "url_error", "reason": str(e.reason)}
    except Exception as e:
        return {"title": title, "status": "error", "reason": str(e)}


def save_index(papers: list[dict], results: list[dict], output_dir: Path):
    """Save an index.json mapping titles to files and metadata."""
    index = []
    result_map = {r["title"]: r for r in results}
    for p in papers:
        r = result_map.get(p["title"], {})
        index.append({
            "title": p["title"],
            "avg_rating": float(p["avg_rating"]),
            "category": p.get("category", ""),
            "year": p.get("year", ""),
            "pdf_url": p.get("pdf_url", ""),
            "forum_url": p.get("forum_url", ""),
            "local_path": r.get("path", ""),
            "download_status": r.get("status", "pending"),
        })

    index_path = output_dir / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump({"papers": index, "total": len(index)}, f, indent=2)
    return index_path


def main():
    parser = argparse.ArgumentParser(description="Download high-scoring ICLR paper PDFs")
    parser.add_argument("--min-rating", type=float, default=7.0,
                        help="Minimum avg_rating threshold (default: 7.0)")
    parser.add_argument("--category", type=str, default=None,
                        help="Filter by category (e.g. 'video-diffusion')")
    parser.add_argument("--limit", type=int, default=None,
                        help="Max number of papers to download")
    parser.add_argument("--output", type=str, default=str(OUTPUT_DIR),
                        help="Output directory for PDFs")
    parser.add_argument("--delay", type=float, default=0.5,
                        help="Delay between downloads in seconds (default: 0.5)")
    parser.add_argument("--workers", type=int, default=4,
                        help="Number of parallel download threads (default: 4)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Just list papers without downloading")
    parser.add_argument("--no-reviews", action="store_true",
                        help="Skip fetching reviewer reviews")
    parser.add_argument("--reviews-only", action="store_true",
                        help="Only fetch reviews (skip PDF downloads)")
    parser.add_argument("--csv", type=str, default=str(CSV_PATH),
                        help="Path to the ICLR CSV file")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    papers = load_papers(Path(args.csv))
    filtered = filter_papers(papers, min_rating=args.min_rating,
                             category=args.category, limit=args.limit)

    print(f"Found {len(filtered)} papers with avg_rating >= {args.min_rating}"
          + (f" in category '{args.category}'" if args.category else ""))

    if not filtered:
        print("No papers match the criteria.")
        return

    if args.dry_run:
        for p in filtered:
            r = float(p["avg_rating"])
            cat = p.get("category", "?")
            title = p['title'][:70].encode('ascii', 'replace').decode('ascii')
            print(f"  {r:.1f} | {cat:20s} | {title}")
        print(f"\nWould process {len(filtered)} papers to {output_dir}/")
        return

    # --- PDF Downloads ---
    results = []
    downloaded = 0
    skipped = 0
    failed = 0

    if not args.reviews_only:
        print(f"Downloading PDFs to {output_dir}/ with {args.workers} workers...\n")
        if args.workers > 1:
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                futures = {
                    pool.submit(download_pdf, p, output_dir, args.delay): p
                    for p in filtered
                }
                for future in as_completed(futures):
                    r = future.result()
                    results.append(r)
                status = r["status"]
                title = _safe(r["title"][:60])
                if status == "downloaded":
                    downloaded += 1
                    size_mb = r.get("size", 0) / 1_000_000
                    print(f"  [OK]   {size_mb:.1f}MB | {title}")
                elif status == "exists":
                    skipped += 1
                    print(f"  [SKIP] exists  | {title}")
                else:
                    failed += 1
                    print(f"  [FAIL] {status} | {title}")
        else:
            for p in filtered:
                r = download_pdf(p, output_dir, args.delay)
                results.append(r)
                status = r["status"]
                title = _safe(r["title"][:60])
                if status == "downloaded":
                    downloaded += 1
                    size_mb = r.get("size", 0) / 1_000_000
                    print(f"  [OK]   {size_mb:.1f}MB | {title}")
                elif status == "exists":
                    skipped += 1
                    print(f"  [SKIP] exists  | {title}")
                else:
                    failed += 1
                    print(f"  [FAIL] {status} | {title}")

        print(f"\nPDFs: {downloaded} downloaded, {skipped} skipped, {failed} failed")

    # --- Reviews ---
    if not args.no_reviews:
        print(f"\nFetching reviews from OpenReview API...\n")
        rev_fetched = 0
        rev_skipped = 0
        rev_failed = 0

        with ThreadPoolExecutor(max_workers=min(args.workers, 2)) as pool:
            futures = {
                pool.submit(fetch_reviews, p, output_dir, 0.3): p
                for p in filtered
            }
            for future in as_completed(futures):
                r = future.result()
                status = r["status"]
                title = _safe(r["title"][:55])
                if status == "fetched":
                    rev_fetched += 1
                    n = r.get("num_reviews", 0)
                    print(f"  [OK]   {n} reviews | {title}")
                elif status == "exists":
                    rev_skipped += 1
                elif status == "no_reviews_found":
                    rev_failed += 1
                    print(f"  [NONE] 0 reviews | {title}")
                else:
                    rev_failed += 1
                    print(f"  [FAIL] {status:12s} | {title}")

        print(f"\nReviews: {rev_fetched} fetched, {rev_skipped} cached, {rev_failed} failed")

    idx = save_index(filtered, results, output_dir)
    print(f"\nIndex saved to {idx}")


if __name__ == "__main__":
    main()
