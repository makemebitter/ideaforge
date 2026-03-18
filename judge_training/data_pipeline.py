"""
Phase 1: Data Pipeline — Parse review JSONs + CSV metadata into unified train/test split.

Data sources:
  - Bulk-crawled review JSONs from research_data/{venue}/reviews/{year}/ (44K+ full reviews)
  - ICLR topic review JSONs (full reviewer text: strengths, weaknesses, questions)
  - Author review JSONs (full OpenReview threads)
  - CSV metadata: iclr_*_with_reviews.csv, neurips_*_all_submissions.csv, icml_*_all_submissions.csv

Output:
  data/train.jsonl, data/test.jsonl — unified schema, stratified split
"""

import json
import csv
import hashlib
import os
import random
from pathlib import Path
from collections import defaultdict
from typing import Optional

_RESOURCES_DIR = os.environ.get("IDEAFORGE_RESOURCES_DIR")
if _RESOURCES_DIR:
    RESEARCH_DATA = Path(_RESOURCES_DIR) / "research_data"
    OUTPUT_DIR = Path(_RESOURCES_DIR) / "data"
else:
    RESEARCH_DATA = Path(__file__).parent.parent / "research_data"
    OUTPUT_DIR = Path(__file__).parent / "data"


def parse_iclr_topic_json(filepath: Path, topic: str) -> Optional[dict]:
    """Parse an ICLR topic-level review JSON (Format 1)."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

    reviews = data.get("reviews", [])
    if not reviews:
        return None

    ratings = []
    for r in reviews:
        if "rating" in r and r["rating"] is not None:
            try:
                ratings.append(float(str(r["rating"]).split(":")[0].strip()))
            except (ValueError, IndexError):
                pass
    if not ratings:
        return None

    def _safe_float(val):
        if val is None:
            return None
        try:
            return float(str(val).split(":")[0].strip())
        except (ValueError, IndexError):
            return None

    soundness = [v for r in reviews if (v := _safe_float(r.get("soundness"))) is not None]
    contribution = [v for r in reviews if (v := _safe_float(r.get("contribution"))) is not None]
    presentation = [v for r in reviews if (v := _safe_float(r.get("presentation"))) is not None]
    confidence = [v for r in reviews if (v := _safe_float(r.get("confidence"))) is not None]

    review_texts = []
    for r in reviews:
        review_texts.append({
            "rating": r.get("rating"),
            "confidence": r.get("confidence"),
            "soundness": r.get("soundness"),
            "presentation": r.get("presentation"),
            "contribution": r.get("contribution"),
            "summary": r.get("summary", ""),
            "strengths": r.get("strengths", ""),
            "weaknesses": r.get("weaknesses", ""),
            "questions": r.get("questions", ""),
        })

    forum_id = data.get("forum_id", "")
    paper_id = f"iclr_topic_{forum_id}" if forum_id else f"iclr_topic_{hashlib.md5(data['title'].encode()).hexdigest()[:12]}"

    pdf_path = _find_pdf_for_topic(filepath.parent, data.get("title", ""))

    return {
        "paper_id": paper_id,
        "title": data.get("title", ""),
        "abstract": "",
        "keywords": [],
        "primary_area": topic,
        "venue": "iclr",
        "year": None,
        "decision": None,
        "avg_rating": round(sum(ratings) / len(ratings), 2),
        "ratings": ratings,
        "avg_soundness": round(sum(soundness) / len(soundness), 2) if soundness else None,
        "avg_contribution": round(sum(contribution) / len(contribution), 2) if contribution else None,
        "avg_presentation": round(sum(presentation) / len(presentation), 2) if presentation else None,
        "avg_confidence": round(sum(confidence) / len(confidence), 2) if confidence else None,
        "num_reviews": len(reviews),
        "review_texts": review_texts,
        "pdf_path": str(pdf_path) if pdf_path else None,
        "forum_url": data.get("forum_url", ""),
        "source": "iclr_topic_json",
    }


def _find_pdf_for_topic(topic_dir: Path, title: str) -> Optional[Path]:
    """Try to find a matching PDF in the topic directory."""
    pdfs_dir = topic_dir / "pdfs"
    if not pdfs_dir.exists():
        pdfs_dir = topic_dir
    for pdf in pdfs_dir.glob("*.pdf"):
        if _title_similarity(pdf.stem, title) > 0.5:
            return pdf.relative_to(RESEARCH_DATA.parent)
    return None


def _title_similarity(a: str, b: str) -> float:
    """Simple word-overlap similarity between two strings."""
    words_a = set(a.lower().replace("_", " ").replace("-", " ").split())
    words_b = set(b.lower().replace("_", " ").replace("-", " ").split())
    if not words_a or not words_b:
        return 0.0
    overlap = words_a & words_b
    return len(overlap) / min(len(words_a), len(words_b))


def parse_author_review_json(filepath: Path, author: str) -> Optional[dict]:
    """Parse an author-level review JSON (Format 2 — full OpenReview threads)."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

    threads = data.get("threads", [])
    if not threads:
        return None

    paper_content = data.get("paper_content", {})
    forum_id = data.get("forum_id", "")
    paper_id = f"author_{author}_{forum_id}" if forum_id else f"author_{hashlib.md5(data['title'].encode()).hexdigest()[:12]}"

    ratings = []
    review_texts = []
    soundness_vals, contribution_vals, presentation_vals, confidence_vals = [], [], [], []

    for thread in threads:
        review = thread.get("review", {})
        content = review.get("content", {})
        if not content:
            continue

        rating = content.get("rating") or content.get("overall_recommendation")
        if rating is None:
            continue

        if isinstance(rating, str):
            import re
            m = re.search(r"(\d+)", str(rating))
            rating = int(m.group(1)) if m else None
        if rating is None:
            continue

        ratings.append(float(rating))

        s = content.get("soundness")
        if isinstance(s, str):
            m = re.search(r"(\d+)", str(s))
            s = int(m.group(1)) if m else None
        if s:
            soundness_vals.append(s)

        c = content.get("contribution")
        if isinstance(c, str):
            m = re.search(r"(\d+)", str(c))
            c = int(m.group(1)) if m else None
        if c:
            contribution_vals.append(c)

        p = content.get("presentation")
        if isinstance(p, str):
            m = re.search(r"(\d+)", str(p))
            p = int(m.group(1)) if m else None
        if p:
            presentation_vals.append(p)

        conf = content.get("confidence")
        if isinstance(conf, str):
            m = re.search(r"(\d+)", str(conf))
            conf = int(m.group(1)) if m else None
        if conf:
            confidence_vals.append(conf)

        review_texts.append({
            "rating": float(rating),
            "confidence": conf,
            "soundness": s,
            "presentation": p,
            "contribution": c,
            "summary": content.get("summary", ""),
            "strengths": content.get("strengths", content.get("strengths_and_contributions", "")),
            "weaknesses": content.get("weaknesses", content.get("weaknesses_and_limitations", "")),
            "questions": content.get("questions", ""),
        })

    if not ratings:
        return None

    decision = None
    for mr in data.get("meta_reviews", []):
        d = mr.get("content", {}).get("decision", "")
        if d:
            decision = d
            break

    venue = paper_content.get("venue", "")
    year = None
    if venue:
        import re
        m = re.search(r"(20\d{2})", venue)
        if m:
            year = int(m.group(1))

    venue_short = "unknown"
    for v in ["iclr", "icml", "neurips", "nips", "emnlp", "acl", "naacl"]:
        if v in venue.lower():
            venue_short = v
            break

    pdfs_dir = filepath.parent.parent / "pdfs"
    pdf_path = None
    if pdfs_dir.exists():
        for pdf in pdfs_dir.glob("*.pdf"):
            if _title_similarity(pdf.stem, data.get("title", "")) > 0.5:
                pdf_path = str(pdf.relative_to(RESEARCH_DATA.parent))
                break

    return {
        "paper_id": paper_id,
        "title": data.get("title", ""),
        "abstract": paper_content.get("abstract", ""),
        "keywords": paper_content.get("keywords", []),
        "primary_area": paper_content.get("primary_area", ""),
        "venue": venue_short,
        "year": year,
        "decision": decision,
        "avg_rating": round(sum(ratings) / len(ratings), 2),
        "ratings": ratings,
        "avg_soundness": round(sum(soundness_vals) / len(soundness_vals), 2) if soundness_vals else None,
        "avg_contribution": round(sum(contribution_vals) / len(contribution_vals), 2) if contribution_vals else None,
        "avg_presentation": round(sum(presentation_vals) / len(presentation_vals), 2) if presentation_vals else None,
        "avg_confidence": round(sum(confidence_vals) / len(confidence_vals), 2) if confidence_vals else None,
        "num_reviews": len(review_texts),
        "review_texts": review_texts,
        "pdf_path": pdf_path,
        "forum_url": data.get("forum_url", ""),
        "source": "author_json",
    }


def parse_bulk_review_json(filepath: Path) -> Optional[dict]:
    """Parse a bulk-crawled review JSON from research_data/{venue}/reviews/{year}/."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

    reviews = data.get("reviews", [])
    if not reviews:
        return None

    def _safe_float(val):
        if val is None:
            return None
        try:
            return float(str(val).split(":")[0].strip())
        except (ValueError, IndexError):
            return None

    ratings = []
    soundness_vals, contribution_vals, presentation_vals, confidence_vals = [], [], [], []
    review_texts = []

    for r in reviews:
        rating = _safe_float(r.get("rating"))
        if rating is not None:
            ratings.append(rating)

        s = _safe_float(r.get("soundness"))
        if s is not None:
            soundness_vals.append(s)
        c = _safe_float(r.get("contribution"))
        if c is not None:
            contribution_vals.append(c)
        p = _safe_float(r.get("presentation"))
        if p is not None:
            presentation_vals.append(p)
        conf = _safe_float(r.get("confidence"))
        if conf is not None:
            confidence_vals.append(conf)

        review_texts.append({
            "rating": r.get("rating"),
            "confidence": r.get("confidence"),
            "soundness": r.get("soundness"),
            "presentation": r.get("presentation"),
            "contribution": r.get("contribution"),
            "summary": r.get("summary", ""),
            "strengths": r.get("strengths", ""),
            "weaknesses": r.get("weaknesses", ""),
            "questions": r.get("questions", ""),
        })

    if not ratings:
        return None

    forum_id = data.get("forum_id", "")
    venue = data.get("venue", "unknown")
    year = data.get("year")

    paper_id = f"bulk_{venue}_{forum_id}" if forum_id else f"bulk_{hashlib.md5(data.get('title', '').encode()).hexdigest()[:12]}"

    avg_rating_raw = data.get("avg_rating")
    if avg_rating_raw:
        try:
            avg_rating = float(str(avg_rating_raw).split(":")[0].strip())
        except (ValueError, IndexError):
            avg_rating = round(sum(ratings) / len(ratings), 2)
    else:
        avg_rating = round(sum(ratings) / len(ratings), 2)

    return {
        "paper_id": paper_id,
        "title": data.get("title", ""),
        "abstract": "",
        "keywords": [],
        "primary_area": "",
        "venue": venue,
        "year": int(year) if year else None,
        "decision": data.get("decision", ""),
        "avg_rating": avg_rating,
        "ratings": ratings,
        "avg_soundness": round(sum(soundness_vals) / len(soundness_vals), 2) if soundness_vals else None,
        "avg_contribution": round(sum(contribution_vals) / len(contribution_vals), 2) if contribution_vals else None,
        "avg_presentation": round(sum(presentation_vals) / len(presentation_vals), 2) if presentation_vals else None,
        "avg_confidence": round(sum(confidence_vals) / len(confidence_vals), 2) if confidence_vals else None,
        "num_reviews": len(reviews),
        "review_texts": review_texts,
        "pdf_path": None,
        "forum_url": data.get("forum_url", ""),
        "source": "bulk_review_json",
    }


def parse_venue_csv(filepath: Path, venue: str) -> list[dict]:
    """Parse a NeurIPS/ICML all_submissions CSV into records (metadata + scores, no review text)."""
    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                avg_rating = float(row.get("avg_rating", 0))
            except (ValueError, TypeError):
                continue
            if avg_rating <= 0:
                continue

            ratings_str = row.get("ratings", "")
            ratings = []
            if ratings_str:
                for r in ratings_str.split(","):
                    r = r.strip()
                    try:
                        ratings.append(float(r))
                    except ValueError:
                        pass

            year = None
            try:
                year = int(row.get("year", 0))
            except (ValueError, TypeError):
                pass

            forum_id = row.get("forum", row.get("id", ""))
            paper_id = f"csv_{venue}_{forum_id}" if forum_id else f"csv_{venue}_{hashlib.md5(row.get('title', '').encode()).hexdigest()[:12]}"

            kw = row.get("keywords", "")
            keywords = [k.strip() for k in kw.split(",")] if kw else []

            records.append({
                "paper_id": paper_id,
                "title": row.get("title", ""),
                "abstract": row.get("abstract", ""),
                "keywords": keywords,
                "primary_area": row.get("primary_area", ""),
                "venue": venue,
                "year": year,
                "decision": row.get("decision", ""),
                "avg_rating": avg_rating,
                "ratings": ratings,
                "avg_soundness": None,
                "avg_contribution": None,
                "avg_presentation": None,
                "avg_confidence": float(row["avg_confidence"]) if row.get("avg_confidence") else None,
                "num_reviews": int(row.get("num_reviews", 0)) if row.get("num_reviews") else len(ratings),
                "review_texts": None,
                "pdf_path": None,
                "forum_url": row.get("forum_url", ""),
                "source": f"csv_{venue}",
            })
    return records


def parse_csv_with_reviews(filepath: Path) -> list[dict]:
    """Parse a *_with_reviews.csv into records (scores + metadata, no review text)."""
    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                avg_rating = float(row.get("avg_rating", 0))
            except (ValueError, TypeError):
                continue
            if avg_rating <= 0:
                continue

            ratings_str = row.get("ratings", "")
            ratings = []
            if ratings_str:
                for r in ratings_str.split(","):
                    r = r.strip()
                    try:
                        ratings.append(float(r))
                    except ValueError:
                        pass

            year = None
            try:
                year = int(row.get("year", 0))
            except (ValueError, TypeError):
                pass

            forum_id = row.get("forum", row.get("id", ""))
            paper_id = f"csv_{forum_id}" if forum_id else f"csv_{hashlib.md5(row['title'].encode()).hexdigest()[:12]}"

            kw = row.get("keywords", "")
            keywords = [k.strip() for k in kw.split(",")] if kw else []

            records.append({
                "paper_id": paper_id,
                "title": row.get("title", ""),
                "abstract": row.get("abstract", ""),
                "keywords": keywords,
                "primary_area": row.get("primary_area", ""),
                "venue": "iclr",
                "year": year,
                "decision": row.get("decision", ""),
                "avg_rating": avg_rating,
                "ratings": ratings,
                "avg_soundness": None,
                "avg_contribution": None,
                "avg_presentation": None,
                "avg_confidence": float(row["avg_confidence"]) if row.get("avg_confidence") else None,
                "num_reviews": int(row.get("num_reviews", 0)) if row.get("num_reviews") else len(ratings),
                "review_texts": None,
                "pdf_path": None,
                "forum_url": row.get("forum_url", ""),
                "source": "csv",
            })
    return records


def score_tier(avg_rating: float) -> str:
    if avg_rating < 4:
        return "1-3"
    elif avg_rating < 6:
        return "4-5"
    elif avg_rating < 8:
        return "6-7"
    else:
        return "8-10"


def stratified_split(records: list[dict], test_ratio: float = 0.2, seed: int = 42) -> tuple[list, list]:
    """Split records into train/test, stratified by score tier and venue."""
    rng = random.Random(seed)

    buckets = defaultdict(list)
    for r in records:
        tier = score_tier(r["avg_rating"])
        venue = r.get("venue", "unknown")
        buckets[(tier, venue)].append(r)

    train, test = [], []
    for key, items in buckets.items():
        rng.shuffle(items)
        n_test = max(1, int(len(items) * test_ratio))
        test.extend(items[:n_test])
        train.extend(items[n_test:])

    rng.shuffle(train)
    rng.shuffle(test)
    return train, test


def run():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    all_records = []
    seen_titles = set()
    seen_forum_ids = set()

    # === 1. Parse bulk-crawled review JSONs (highest priority — full review text) ===
    print("[1/5] Parsing bulk-crawled review JSONs...")
    bulk_count = 0
    for venue in ["iclr", "neurips", "icml"]:
        venue_reviews_dir = RESEARCH_DATA / venue / "reviews"
        # Also check {venue}/{year}/reviews/ (setup_pipeline representative crawl)
        venue_base = RESEARCH_DATA / venue
        review_dirs = []
        if venue_reviews_dir.exists():
            review_dirs.append(venue_reviews_dir)
        if venue_base.exists():
            for year_dir in venue_base.iterdir():
                if year_dir.is_dir() and (year_dir / "reviews").exists():
                    review_dirs.append(year_dir / "reviews")
        for rdir in review_dirs:
            for jf in rdir.rglob("*.json"):
                record = parse_bulk_review_json(jf)
                if record and record["title"].lower() not in seen_titles:
                    seen_titles.add(record["title"].lower())
                    forum_url = record.get("forum_url", "")
                    if "id=" in forum_url:
                        fid = forum_url.split("id=")[-1].split("&")[0]
                        seen_forum_ids.add(fid)
                    all_records.append(record)
                    bulk_count += 1
    print(f"  Parsed {bulk_count} bulk-crawled review JSONs")

    # === 2. Parse ICLR topic review JSONs ===
    print("[2/5] Parsing ICLR topic review JSONs...")
    iclr_dir = RESEARCH_DATA / "iclr"
    topic_count = 0
    if iclr_dir.exists():
        for topic_dir in sorted(iclr_dir.iterdir()):
            if not topic_dir.is_dir() or topic_dir.name == "reviews":
                continue
            for jf in topic_dir.glob("*_reviews.json"):
                record = parse_iclr_topic_json(jf, topic_dir.name)
                if record and record["title"].lower() not in seen_titles:
                    seen_titles.add(record["title"].lower())
                    all_records.append(record)
                    topic_count += 1
    print(f"  Parsed {topic_count} ICLR topic review JSONs")

    # === 3. Parse author review JSONs ===
    print("[3/5] Parsing author review JSONs...")
    authors_dir = RESEARCH_DATA / "authors"
    author_count = 0
    if authors_dir.exists():
        for author_dir in sorted(authors_dir.iterdir()):
            if not author_dir.is_dir():
                continue
            reviews_dir = author_dir / "reviews"
            if not reviews_dir.exists():
                continue
            for jf in reviews_dir.glob("*.json"):
                record = parse_author_review_json(jf, author_dir.name)
                if record and record["title"].lower() not in seen_titles:
                    seen_titles.add(record["title"].lower())
                    all_records.append(record)
                    author_count += 1
    print(f"  Parsed {author_count} author review JSONs")

    # === 4. Parse ICLR CSVs (scores + metadata, no review text) ===
    print("[4/5] Parsing ICLR CSV review data...")
    iclr_csv_count = 0
    for csv_file in sorted(iclr_dir.glob("iclr_*_with_reviews.csv")) if iclr_dir.exists() else []:
        if "all" in csv_file.name:
            continue
        csv_records = parse_csv_with_reviews(csv_file)
        for record in csv_records:
            if record["title"].lower() not in seen_titles:
                seen_titles.add(record["title"].lower())
                all_records.append(record)
                iclr_csv_count += 1
    print(f"  Parsed {iclr_csv_count} unique ICLR CSV records")

    # === 5. Parse NeurIPS and ICML CSVs ===
    print("[5/5] Parsing NeurIPS & ICML CSV metadata...")
    venue_csv_count = 0
    for venue in ["neurips", "icml"]:
        venue_dir = RESEARCH_DATA / venue
        if not venue_dir.exists():
            continue
        for csv_file in sorted(venue_dir.glob(f"{venue}_*_all_submissions.csv")):
            csv_records = parse_venue_csv(csv_file, venue)
            for record in csv_records:
                if record["title"].lower() not in seen_titles:
                    seen_titles.add(record["title"].lower())
                    all_records.append(record)
                    venue_csv_count += 1
    print(f"  Parsed {venue_csv_count} unique NeurIPS/ICML CSV records")

    # === Enrich bulk review records with metadata from CSVs ===
    print("\n[ENRICH] Merging CSV metadata (abstracts, keywords) into bulk review records...")
    csv_by_title = {}
    for csv_file in sorted(iclr_dir.glob("iclr_*_with_reviews.csv")) if iclr_dir.exists() else []:
        if "all" in csv_file.name:
            continue
        for row in parse_csv_with_reviews(csv_file):
            csv_by_title[row["title"].lower()] = row
    for venue in ["neurips", "icml"]:
        venue_dir = RESEARCH_DATA / venue
        if not venue_dir.exists():
            continue
        for csv_file in sorted(venue_dir.glob(f"{venue}_*_all_submissions.csv")):
            for row in parse_venue_csv(csv_file, venue):
                csv_by_title[row["title"].lower()] = row

    enriched_abstract = 0
    enriched_keywords = 0
    for record in all_records:
        title_key = record["title"].lower()
        if title_key not in csv_by_title:
            continue
        csv_row = csv_by_title[title_key]
        if not record.get("abstract") and csv_row.get("abstract"):
            record["abstract"] = csv_row["abstract"]
            enriched_abstract += 1
        if not record.get("keywords") and csv_row.get("keywords"):
            record["keywords"] = csv_row["keywords"]
            enriched_keywords += 1
        if not record.get("primary_area") and csv_row.get("primary_area"):
            record["primary_area"] = csv_row["primary_area"]
        if not record.get("decision") and csv_row.get("decision"):
            record["decision"] = csv_row["decision"]
        if not record.get("venue") or record["venue"] == "unknown":
            if csv_row.get("venue"):
                record["venue"] = csv_row["venue"]
        if not record.get("year") and csv_row.get("year"):
            record["year"] = csv_row["year"]
    print(f"  Enriched {enriched_abstract} records with abstracts from CSVs")
    print(f"  Enriched {enriched_keywords} records with keywords from CSVs")

    print(f"\n[TOTAL] {len(all_records)} unique papers")

    rich = [r for r in all_records if r.get("review_texts")]
    meta_only = [r for r in all_records if not r.get("review_texts")]
    print(f"  With full review text: {len(rich)}")
    print(f"  Metadata + scores only: {len(meta_only)}")

    venue_counts = defaultdict(int)
    for r in all_records:
        venue_counts[r.get("venue", "unknown")] += 1
    print(f"\n[BY VENUE]")
    for v, c in sorted(venue_counts.items(), key=lambda x: -x[1]):
        print(f"  {v}: {c}")

    tiers = defaultdict(int)
    for r in all_records:
        tiers[score_tier(r["avg_rating"])] += 1
    print(f"\n[DISTRIBUTION]")
    for tier in ["1-3", "4-5", "6-7", "8-10"]:
        print(f"  Score {tier}: {tiers[tier]}")

    # === Split ===
    print("\n[SPLIT] Stratified 80/20 train/test...")
    train, test = stratified_split(all_records)
    print(f"  Train: {len(train)}")
    print(f"  Test:  {len(test)}")

    train_rich = sum(1 for r in train if r.get("review_texts"))
    test_rich = sum(1 for r in test if r.get("review_texts"))
    print(f"  Train with review text: {train_rich}")
    print(f"  Test with review text:  {test_rich}")

    # === Save ===
    train_path = OUTPUT_DIR / "train.jsonl"
    test_path = OUTPUT_DIR / "test.jsonl"

    for path, data in [(train_path, train), (test_path, test)]:
        with open(path, "w", encoding="utf-8") as f:
            for record in data:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"\n[SAVED] {path} ({len(data)} records)")

    summary = {
        "total_papers": len(all_records),
        "with_review_text": len(rich),
        "metadata_only": len(meta_only),
        "train_size": len(train),
        "test_size": len(test),
        "train_with_reviews": train_rich,
        "test_with_reviews": test_rich,
        "score_distribution": dict(tiers),
        "venue_distribution": dict(venue_counts),
        "sources": {
            "bulk_review_jsons": bulk_count,
            "iclr_topic_jsons": topic_count,
            "author_jsons": author_count,
            "iclr_csv_records": iclr_csv_count,
            "venue_csv_records": venue_csv_count,
        },
    }
    summary_path = OUTPUT_DIR / "summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"[SAVED] {summary_path}")


if __name__ == "__main__":
    run()
