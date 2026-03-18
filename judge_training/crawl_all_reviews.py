"""
Bulk-crawl full review text (strengths, weaknesses, questions, scores) for ALL
papers in the CSV metadata files.

Reads forum IDs from existing CSVs, skips papers that already have review JSONs,
and fetches the rest from the OpenReview API.

Usage:
    python crawl_all_reviews.py                      # Crawl everything
    python crawl_all_reviews.py --venue iclr          # Only ICLR
    python crawl_all_reviews.py --venue icml          # Only ICML
    python crawl_all_reviews.py --year 2026            # Only 2026
    python crawl_all_reviews.py --workers 4 --delay 0.2  # Faster (riskier for rate limits)
    python crawl_all_reviews.py --dry-run              # Preview counts without crawling
"""

import csv
import json
import time
import argparse
import re
import functools
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

print = functools.partial(print, flush=True)  # type: ignore

RESEARCH_DATA = Path(__file__).parent.parent / "research_data"
HEADERS = {"User-Agent": "Mozilla/5.0 (research-bot; academic use)"}


def _safe(text: str) -> str:
    return text.encode("ascii", "replace").decode("ascii")


def discover_papers() -> list[dict]:
    """Discover all papers with forum IDs from CSV files across all venues."""
    papers = []
    seen_forums = set()

    # --- ICLR ---
    iclr_dir = RESEARCH_DATA / "iclr"
    for csv_file in sorted(iclr_dir.glob("iclr_*_with_reviews.csv")):
        if "all" in csv_file.name:
            continue
        year_match = re.search(r"(\d{4})", csv_file.name)
        year = year_match.group(1) if year_match else "unknown"
        with open(csv_file, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                forum_id = row.get("forum", "").strip()
                if not forum_id or forum_id in seen_forums:
                    continue
                seen_forums.add(forum_id)
                papers.append({
                    "forum_id": forum_id,
                    "title": row.get("title", ""),
                    "venue": "iclr",
                    "year": year,
                    "avg_rating": row.get("avg_rating", ""),
                    "decision": row.get("decision", ""),
                    "forum_url": row.get("forum_url", f"https://openreview.net/forum?id={forum_id}"),
                })

    # --- NeurIPS ---
    neurips_dir = RESEARCH_DATA / "neurips"
    if neurips_dir.exists():
        for csv_file in sorted(neurips_dir.glob("neurips_*.csv")):
            year_match = re.search(r"(\d{4})", csv_file.name)
            year = year_match.group(1) if year_match else "unknown"
            with open(csv_file, "r", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    forum_id = row.get("forum_id", row.get("forum", "")).strip()
                    if not forum_id or forum_id in seen_forums:
                        continue
                    seen_forums.add(forum_id)
                    papers.append({
                        "forum_id": forum_id,
                        "title": row.get("title", ""),
                        "venue": "neurips",
                        "year": year,
                        "avg_rating": row.get("avg_rating", ""),
                        "decision": row.get("decision", ""),
                        "forum_url": f"https://openreview.net/forum?id={forum_id}",
                    })

    # --- ICML ---
    icml_dir = RESEARCH_DATA / "icml"
    if icml_dir.exists():
        for csv_file in sorted(icml_dir.glob("icml_*.csv")):
            year_match = re.search(r"(\d{4})", csv_file.name)
            year = year_match.group(1) if year_match else "unknown"
            with open(csv_file, "r", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    forum_id = row.get("forum_id", row.get("forum", "")).strip()
                    if not forum_id or forum_id in seen_forums:
                        continue
                    seen_forums.add(forum_id)
                    papers.append({
                        "forum_id": forum_id,
                        "title": row.get("title", ""),
                        "venue": "icml",
                        "year": year,
                        "avg_rating": row.get("avg_rating", ""),
                        "decision": row.get("decision", ""),
                        "forum_url": f"https://openreview.net/forum?id={forum_id}",
                    })

    return papers


def find_existing_review_forum_ids() -> set[str]:
    """Find all forum IDs that already have review JSONs."""
    existing = set()
    for jf in RESEARCH_DATA.rglob("*_reviews.json"):
        try:
            with open(jf, "r", encoding="utf-8") as f:
                data = json.load(f)
            fid = data.get("forum_id", "")
            if fid:
                existing.add(fid)
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass
    return existing


def review_output_path(venue: str, year: str, forum_id: str) -> Path:
    """Determine where to save a review JSON."""
    out_dir = RESEARCH_DATA / venue / "reviews" / year
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f"{forum_id}_reviews.json"


def fetch_reviews(paper: dict, delay: float = 0.3) -> dict:
    """Fetch full review text from OpenReview API for a single paper."""
    forum_id = paper["forum_id"]
    title = paper["title"]
    venue = paper["venue"]
    year = paper["year"]

    out_path = review_output_path(venue, year, forum_id)
    if out_path.exists() and out_path.stat().st_size > 100:
        return {"forum_id": forum_id, "status": "exists", "path": str(out_path)}

    try:
        api_url = f"https://api2.openreview.net/notes?forum={forum_id}"
        data = None
        for attempt in range(4):
            try:
                req = Request(api_url, headers=HEADERS)
                raw = urlopen(req, timeout=20).read()
                data = json.loads(raw)
                break
            except HTTPError as e:
                if e.code == 429:
                    wait = 5 * (2 ** attempt)
                    time.sleep(wait)
                    continue
                elif e.code >= 500:
                    time.sleep(2 ** attempt)
                    continue
                raise
            except (URLError, TimeoutError):
                time.sleep(2 ** attempt)
                continue

        if data is None:
            return {"forum_id": forum_id, "status": "failed_after_retries", "title": title}

        notes = data.get("notes", [])

        def extract_val(content, field):
            v = content.get(field, "")
            return v.get("value", v) if isinstance(v, dict) else v

        reviews = []
        for note in notes:
            invitations = note.get("invitations", [])
            inv_str = invitations[0] if invitations else note.get("invitation", "")
            content = note.get("content", {})

            is_review = ("Official_Review" in str(inv_str)
                         or ("rating" in content and "summary" in content))
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
            return {"forum_id": forum_id, "status": "no_reviews", "title": title,
                    "notes_count": len(notes)}

        review_data = {
            "title": title,
            "forum_id": forum_id,
            "forum_url": paper.get("forum_url", ""),
            "venue": venue,
            "year": year,
            "avg_rating": paper.get("avg_rating", ""),
            "decision": paper.get("decision", ""),
            "num_reviews": len(reviews),
            "reviews": reviews,
        }

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(review_data, f, indent=2, ensure_ascii=False)

        time.sleep(delay)
        return {
            "forum_id": forum_id,
            "status": "fetched",
            "path": str(out_path),
            "num_reviews": len(reviews),
            "title": title,
        }

    except HTTPError as e:
        return {"forum_id": forum_id, "status": "http_error", "code": e.code, "title": title}
    except Exception as e:
        return {"forum_id": forum_id, "status": "error", "reason": str(e)[:200], "title": title}


def main():
    parser = argparse.ArgumentParser(description="Bulk-crawl full review text for all papers")
    parser.add_argument("--venue", type=str, default=None, choices=["iclr", "neurips", "icml"],
                        help="Only crawl a specific venue")
    parser.add_argument("--year", type=str, default=None,
                        help="Only crawl a specific year")
    parser.add_argument("--workers", type=int, default=3,
                        help="Parallel workers (default: 3, max 5)")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between API calls per worker (seconds)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Max papers to crawl (for testing)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Just show counts, don't crawl")
    args = parser.parse_args()

    print("Discovering papers from CSV files...")
    all_papers = discover_papers()
    print(f"  Found {len(all_papers)} unique papers with forum IDs")

    print("Scanning existing review JSONs...")
    existing = find_existing_review_forum_ids()
    print(f"  Found {len(existing)} papers already crawled")

    # Filter
    to_crawl = [p for p in all_papers if p["forum_id"] not in existing]

    if args.venue:
        to_crawl = [p for p in to_crawl if p["venue"] == args.venue]
    if args.year:
        to_crawl = [p for p in to_crawl if p["year"] == args.year]
    if args.limit:
        to_crawl = to_crawl[:args.limit]

    # Stats
    by_venue_year = defaultdict(int)
    for p in to_crawl:
        by_venue_year[(p["venue"], p["year"])] += 1

    print(f"\nPapers to crawl: {len(to_crawl)}")
    for (v, y), c in sorted(by_venue_year.items()):
        print(f"  {v} {y}: {c}")

    est_hours = len(to_crawl) * args.delay / args.workers / 3600
    print(f"\nEstimated time: {est_hours:.1f} hours ({args.workers} workers, {args.delay}s delay)")

    if args.dry_run:
        print("\n[DRY RUN] No papers crawled.")
        return

    if not to_crawl:
        print("\nNothing to crawl — all reviews already fetched!")
        return

    # Crawl
    print(f"\nStarting crawl with {args.workers} workers...\n")
    workers = min(args.workers, 5)
    fetched = 0
    no_reviews = 0
    errors = 0
    skipped = 0

    progress_interval = max(1, len(to_crawl) // 100)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(fetch_reviews, p, args.delay): p
            for p in to_crawl
        }

        for i, future in enumerate(as_completed(futures), 1):
            result = future.result()
            status = result["status"]

            if status == "fetched":
                fetched += 1
            elif status == "exists":
                skipped += 1
            elif status == "no_reviews":
                no_reviews += 1
            else:
                errors += 1

            if i % progress_interval == 0 or i == len(to_crawl):
                pct = i / len(to_crawl) * 100
                title = _safe(result.get("title", "")[:50])
                print(f"  [{i:>6}/{len(to_crawl)}] {pct:5.1f}% | "
                      f"fetched={fetched} no_reviews={no_reviews} errors={errors} | "
                      f"{status:8s} | {title}")

    print(f"\n{'='*60}")
    print(f"DONE: {fetched} fetched, {skipped} already existed, "
          f"{no_reviews} had no reviews, {errors} errors")
    print(f"Total review JSONs now: {len(existing) + fetched}")


if __name__ == "__main__":
    main()
