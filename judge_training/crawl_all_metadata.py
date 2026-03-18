"""
Crawl ALL paper metadata from OpenReview for NeurIPS and ICML (all available years).
Saves CSVs in the same format as the existing ICLR files so the downstream pipeline
and review crawler pick them up automatically.

ICLR is already fully crawled (38K papers in research_data/iclr/).
This script fills in NeurIPS 2023-2025 and ICML 2023-2025.

Usage:
    python crawl_all_metadata.py                  # Crawl everything missing
    python crawl_all_metadata.py --venue neurips   # Only NeurIPS
    python crawl_all_metadata.py --venue icml       # Only ICML
    python crawl_all_metadata.py --dry-run          # Just show counts
"""

import csv
import os
import argparse
from pathlib import Path
import openreview

_RESOURCES_DIR = os.environ.get("IDEAFORGE_RESOURCES_DIR")
if _RESOURCES_DIR:
    RESEARCH_DATA = Path(_RESOURCES_DIR) / "research_data"
else:
    RESEARCH_DATA = Path(__file__).parent.parent / "research_data"

VENUES = {
    "neurips": {
        "years": [2023, 2024, 2025],
        "venue_id_fmt": "NeurIPS.cc/{year}/Conference",
        "output_dir": RESEARCH_DATA / "neurips",
        "csv_fmt": "neurips_{year}_all_submissions.csv",
    },
    "icml": {
        "years": [2023, 2024, 2025],
        "venue_id_fmt": "ICML.cc/{year}/Conference",
        "output_dir": RESEARCH_DATA / "icml",
        "csv_fmt": "icml_{year}_all_submissions.csv",
    },
}


def _get_val(content, field, default=""):
    """Extract value from OpenReview content, handling both raw and {value:...} formats."""
    v = content.get(field, default)
    if isinstance(v, dict):
        return v.get("value", default)
    return v if v is not None else default


def crawl_venue_year(client, venue_name: str, year: int, venue_id: str) -> list[dict]:
    """Fetch all submissions for a venue/year using the OpenReview SDK."""
    invitation = f"{venue_id}/-/Submission"
    print(f"  Fetching {venue_name.upper()} {year} from {invitation}...")

    all_notes = list(client.get_all_notes(invitation=invitation, details="replies"))
    print(f"    Got {len(all_notes)} submissions")

    papers = []
    for note in all_notes:
        c = note.content
        title = _get_val(c, "title", "N/A")
        abstract = _get_val(c, "abstract", "")
        venue_str = _get_val(c, "venue", "")
        keywords = _get_val(c, "keywords", [])
        if isinstance(keywords, list):
            keywords = "; ".join(str(k) for k in keywords)
        primary_area = _get_val(c, "primary_area", "")
        tldr = _get_val(c, "TLDR", "")

        # Infer decision from venue string
        venue_lower = str(venue_str).lower()
        if any(x in venue_lower for x in ["reject", "withdraw", "retract"]):
            decision = "Reject"
        elif "oral" in venue_lower:
            decision = "Accept (Oral)"
        elif "spotlight" in venue_lower:
            decision = "Accept (Spotlight)"
        elif "poster" in venue_lower:
            decision = "Accept (Poster)"
        elif venue_str:
            decision = "Accept"
        else:
            decision = ""

        forum_id = note.forum if hasattr(note, "forum") else note.id

        # Extract review scores from replies if available
        ratings = []
        confidences = []
        if hasattr(note, "details") and note.details:
            for reply in note.details.get("replies", []):
                if isinstance(reply, dict):
                    invitations = reply.get("invitations", [])
                    inv_str = " ".join(invitations) if invitations else reply.get("invitation", "")
                    content = reply.get("content", {})
                else:
                    invitations = getattr(reply, "invitations", [])
                    inv_str = " ".join(invitations) if invitations else getattr(reply, "invitation", "")
                    content = getattr(reply, "content", {})

                if "Official_Review" not in str(inv_str):
                    continue

                rating_val = _get_val(content, "rating") or _get_val(content, "recommendation")
                if rating_val:
                    try:
                        r = float(str(rating_val).split(":")[0].strip())
                        ratings.append(r)
                    except (ValueError, IndexError):
                        pass

                conf_val = _get_val(content, "confidence")
                if conf_val:
                    try:
                        c_val = float(str(conf_val).split(":")[0].strip())
                        confidences.append(c_val)
                    except (ValueError, IndexError):
                        pass

        avg_rating = round(sum(ratings) / len(ratings), 2) if ratings else None
        avg_confidence = round(sum(confidences) / len(confidences), 2) if confidences else None

        papers.append({
            "title": title,
            "decision": decision,
            "avg_rating": avg_rating,
            "min_rating": min(ratings) if ratings else None,
            "max_rating": max(ratings) if ratings else None,
            "num_reviews": len(ratings),
            "ratings": ", ".join(str(r) for r in ratings),
            "avg_confidence": avg_confidence,
            "venue": venue_str,
            "year": year,
            "authors": "; ".join(_get_val(c, "authors", [])) if isinstance(_get_val(c, "authors", []), list) else _get_val(c, "authors", ""),
            "abstract": abstract,
            "keywords": keywords,
            "primary_area": primary_area,
            "TLDR": tldr,
            "pdf_url": f"https://openreview.net/pdf?id={forum_id}",
            "forum_url": f"https://openreview.net/forum?id={forum_id}",
            "id": note.id if hasattr(note, "id") else "",
            "forum": forum_id,
        })

    return papers


def save_csv(papers: list[dict], filepath: Path):
    """Save papers to CSV in the same format as ICLR files."""
    if not papers:
        print(f"    No papers to save for {filepath.name}")
        return

    fieldnames = [
        "title", "decision", "avg_rating", "min_rating", "max_rating",
        "num_reviews", "ratings", "avg_confidence", "venue", "year",
        "authors", "abstract", "keywords", "primary_area", "TLDR",
        "pdf_url", "forum_url", "id", "forum"
    ]

    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(papers)

    with_ratings = sum(1 for p in papers if p.get("avg_rating"))
    print(f"    Saved {len(papers)} papers ({with_ratings} with ratings) to {filepath}")


def main():
    parser = argparse.ArgumentParser(description="Crawl all paper metadata from OpenReview")
    parser.add_argument("--venue", type=str, choices=["neurips", "icml"], default=None,
                        help="Only crawl a specific venue")
    parser.add_argument("--year", type=int, default=None,
                        help="Only crawl a specific year")
    parser.add_argument("--dry-run", action="store_true",
                        help="Just show what would be crawled")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing CSVs")
    args = parser.parse_args()

    print("Connecting to OpenReview API v2...")
    client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")
    print("  Connected.\n")

    venues_to_crawl = {args.venue: VENUES[args.venue]} if args.venue else VENUES

    total_new = 0
    for venue_name, config in venues_to_crawl.items():
        output_dir = config["output_dir"]
        output_dir.mkdir(parents=True, exist_ok=True)

        years = [args.year] if args.year else config["years"]

        for year in years:
            csv_name = config["csv_fmt"].format(year=year)
            csv_path = output_dir / csv_name

            if csv_path.exists() and not args.force:
                with open(csv_path, "r", encoding="utf-8") as f:
                    existing_count = sum(1 for _ in csv.reader(f)) - 1
                print(f"[SKIP] {csv_path.name} already exists ({existing_count} papers). Use --force to overwrite.")
                continue

            venue_id = config["venue_id_fmt"].format(year=year)

            if args.dry_run:
                print(f"[DRY RUN] Would crawl {venue_name.upper()} {year} ({venue_id})")
                continue

            print(f"[CRAWL] {venue_name.upper()} {year}")
            papers = crawl_venue_year(client, venue_name, year, venue_id)
            save_csv(papers, csv_path)
            total_new += len(papers)
            print()

    if not args.dry_run:
        print(f"\nDone! Crawled {total_new} new papers total.")


if __name__ == "__main__":
    main()
