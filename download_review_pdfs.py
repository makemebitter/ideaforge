"""
Download PDFs for all papers that have OpenReview review JSONs.

Scans research_data/ for review JSON files, extracts forum_id,
and downloads the PDF from OpenReview. Skips already-downloaded PDFs.

Usage:
    python download_review_pdfs.py              # Download all
    python download_review_pdfs.py --dry-run    # Preview without downloading
    python download_review_pdfs.py --limit 100  # Download at most 100
"""

import json
import os
import re
import sys
import time
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

BASE = Path(__file__).parent / "research_data"
SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (research-bot; academic use)",
})

# Rate limiting
DELAY_BETWEEN_REQUESTS = 1.5  # seconds


def sanitize_filename(title: str, max_len: int = 80) -> str:
    """Create a safe filename from a paper title."""
    name = re.sub(r'[<>:"/\\|?*]', '_', title)
    name = re.sub(r'\s+', '_', name).strip('_.')
    if len(name) > max_len:
        name = name[:max_len].rstrip('_.')
    return name


def collect_papers() -> list[dict]:
    """Scan all review JSONs and collect (forum_id, title, json_path, pdf_dir)."""
    papers = []
    seen_ids = set()

    # 1. ICLR topic subdirs
    iclr_dir = BASE / "iclr"
    if iclr_dir.exists():
        for sub in sorted(iclr_dir.iterdir()):
            if sub.is_dir():
                pdf_dir = sub / "pdfs"
                for f in sorted(sub.glob("*.json")):
                    try:
                        data = json.loads(f.read_text(encoding="utf-8"))
                        fid = data.get("forum_id") or data.get("id") or data.get("forum")
                        title = data.get("title", f.stem)
                        if fid and fid not in seen_ids:
                            seen_ids.add(fid)
                            papers.append({
                                "forum_id": fid,
                                "title": title,
                                "json_path": str(f),
                                "pdf_dir": str(pdf_dir),
                                "source": f"iclr/{sub.name}",
                            })
                    except Exception:
                        pass

    # 2. ICML subdirs
    icml_dir = BASE / "icml"
    if icml_dir.exists():
        for sub in sorted(icml_dir.iterdir()):
            if sub.is_dir():
                pdf_dir = sub / "pdfs"
                for f in sorted(sub.glob("*.json")):
                    try:
                        data = json.loads(f.read_text(encoding="utf-8"))
                        fid = data.get("forum_id") or data.get("id") or data.get("forum")
                        title = data.get("title", f.stem)
                        if fid and fid not in seen_ids:
                            seen_ids.add(fid)
                            papers.append({
                                "forum_id": fid,
                                "title": title,
                                "json_path": str(f),
                                "pdf_dir": str(pdf_dir),
                                "source": f"icml/{sub.name}",
                            })
                    except Exception:
                        pass

    # 3. NeurIPS subdirs
    neurips_dir = BASE / "neurips"
    if neurips_dir.exists():
        for sub in sorted(neurips_dir.iterdir()):
            if sub.is_dir():
                pdf_dir = sub / "pdfs"
                for f in sorted(sub.glob("*.json")):
                    try:
                        data = json.loads(f.read_text(encoding="utf-8"))
                        fid = data.get("forum_id") or data.get("id") or data.get("forum")
                        title = data.get("title", f.stem)
                        if fid and fid not in seen_ids:
                            seen_ids.add(fid)
                            papers.append({
                                "forum_id": fid,
                                "title": title,
                                "json_path": str(f),
                                "pdf_dir": str(pdf_dir),
                                "source": f"neurips/{sub.name}",
                            })
                    except Exception:
                        pass

    # 4. Author review dirs
    authors_dir = BASE / "authors"
    if authors_dir.exists():
        for author_dir in sorted(authors_dir.iterdir()):
            if author_dir.is_dir():
                reviews_dir = author_dir / "reviews"
                pdf_dir = author_dir / "pdfs"
                if reviews_dir.exists():
                    for f in sorted(reviews_dir.glob("*.json")):
                        try:
                            data = json.loads(f.read_text(encoding="utf-8"))
                            fid = data.get("forum_id") or data.get("id") or data.get("forum")
                            title = data.get("title", f.stem)
                            if fid and fid not in seen_ids:
                                seen_ids.add(fid)
                                papers.append({
                                    "forum_id": fid,
                                    "title": title,
                                    "json_path": str(f),
                                    "pdf_dir": str(pdf_dir),
                                    "source": f"authors/{author_dir.name}",
                                })
                        except Exception:
                            pass

    return papers


def find_existing_pdfs(pdf_dir: str, title: str) -> bool:
    """Check if a PDF already exists for this paper."""
    d = Path(pdf_dir)
    if not d.exists():
        return False
    safe = sanitize_filename(title)
    # Check exact match
    if (d / f"{safe}.pdf").exists():
        return True
    # Check partial match (title might have been truncated differently)
    safe_lower = safe.lower()[:40]
    for f in d.iterdir():
        if f.suffix == ".pdf" and f.stem.lower()[:40] == safe_lower:
            return True
    return False


def download_pdf(forum_id: str, pdf_dir: str, title: str) -> tuple[bool, str]:
    """Download a single PDF from OpenReview. Returns (success, message)."""
    url = f"https://openreview.net/pdf?id={forum_id}"
    safe = sanitize_filename(title)
    out_path = Path(pdf_dir) / f"{safe}.pdf"

    try:
        resp = SESSION.get(url, timeout=60)
        if resp.status_code == 200 and resp.headers.get("content-type", "").startswith("application/pdf"):
            Path(pdf_dir).mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(resp.content)
            size_kb = len(resp.content) / 1024
            return True, f"OK ({size_kb:.0f} KB)"
        elif resp.status_code == 200:
            # Might be HTML error page
            return False, f"Not a PDF (content-type: {resp.headers.get('content-type', 'unknown')})"
        else:
            return False, f"HTTP {resp.status_code}"
    except requests.exceptions.Timeout:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(description="Download PDFs for reviewed papers")
    parser.add_argument("--dry-run", action="store_true", help="Preview without downloading")
    parser.add_argument("--limit", type=int, default=0, help="Max papers to download (0=all)")
    parser.add_argument("--delay", type=float, default=DELAY_BETWEEN_REQUESTS, help="Delay between requests")
    parser.add_argument("--retry-failed", action="store_true", help="Retry previously failed downloads")
    args = parser.parse_args()

    print("[SCAN] Collecting papers from review JSONs...")
    papers = collect_papers()
    print(f"[SCAN] Found {len(papers)} unique papers with forum IDs")

    # Check which already have PDFs
    to_download = []
    already_have = 0
    for p in papers:
        if find_existing_pdfs(p["pdf_dir"], p["title"]):
            already_have += 1
        else:
            to_download.append(p)

    print(f"[SCAN] Already have: {already_have} PDFs")
    print(f"[SCAN] Need to download: {len(to_download)} PDFs")

    if args.limit > 0:
        to_download = to_download[:args.limit]
        print(f"[SCAN] Limited to: {len(to_download)} PDFs")

    # Show breakdown by source
    from collections import Counter
    source_counts = Counter(p["source"] for p in to_download)
    print("\n[BREAKDOWN]")
    for source, count in sorted(source_counts.items()):
        print(f"  {source}: {count}")

    if args.dry_run:
        print("\n[DRY RUN] Would download the above. Exiting.")
        return

    if not to_download:
        print("\n[DONE] All PDFs already downloaded!")
        return

    # Estimate time
    est_minutes = len(to_download) * args.delay / 60
    print(f"\n[DOWNLOAD] Starting... ETA: ~{est_minutes:.0f} minutes")

    success = 0
    failed = 0
    failed_list = []

    for i, p in enumerate(to_download):
        if i > 0:
            time.sleep(args.delay)

        ok, msg = download_pdf(p["forum_id"], p["pdf_dir"], p["title"])
        if ok:
            success += 1
        else:
            failed += 1
            failed_list.append((p["forum_id"], p["title"], msg))

        # Progress every 50
        if (i + 1) % 50 == 0 or (i + 1) == len(to_download):
            elapsed = (i + 1) * args.delay
            remaining = (len(to_download) - i - 1) * args.delay
            print(f"  [{i+1}/{len(to_download)}] ok={success} fail={failed} "
                  f"ETA={remaining/60:.0f}min")

        # On sustained failures (rate limit), back off
        if failed >= 3 and failed == i + 1:
            print("[WARN] First 3 downloads all failed, backing off 10s...")
            time.sleep(10)
        elif msg.startswith("HTTP 4") and "429" in msg:
            print(f"[WARN] Rate limited, backing off 30s...")
            time.sleep(30)

    print(f"\n[DONE] Downloaded: {success}, Failed: {failed}")

    if failed_list:
        fail_path = BASE / "_download_failures.txt"
        with open(fail_path, "w", encoding="utf-8") as f:
            for fid, title, msg in failed_list:
                f.write(f"{fid}\t{title}\t{msg}\n")
        print(f"[FAIL] Failure log: {fail_path}")


if __name__ == "__main__":
    main()
