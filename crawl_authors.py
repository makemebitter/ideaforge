"""
Crawl all papers by specific researchers from multiple sources.

Sources (in order of priority):
  1. DBLP — complete, reliable CS bibliography (primary paper list)
  2. Google Scholar — citation counts, comprehensive coverage (via scholarly)
  3. Personal websites — scrape publication pages for additional papers
  4. Semantic Scholar — abstracts, TLDRs, external IDs (enrichment)
  5. OpenReview — full review discussions, author rebuttals, meta-reviews

Usage:
    python crawl_authors.py                                    # Crawl default authors
    python crawl_authors.py --authors "Yann LeCun"             # Custom author
    python crawl_authors.py --dry-run                          # Preview without downloading
    python crawl_authors.py --reviews-only                     # Skip PDF downloads
    python crawl_authors.py --refresh                          # Re-fetch even if cached
    python crawl_authors.py --no-pdfs                          # Skip PDF downloads

Output:
    research_data/authors/<author_name>/papers.csv             # Paper metadata
    research_data/authors/<author_name>/pdfs/<title>.pdf       # PDFs
    research_data/authors/<author_name>/reviews/<title>.json   # OpenReview discussions
"""

import csv
import re
import json
import time
import argparse
import hashlib
from pathlib import Path
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = Path(__file__).parent / "research_data" / "authors"

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
})

# ============================================================================
# Default authors to track
# ============================================================================

DEFAULT_AUTHORS = [
    {
        "name": "Hao Zhang",
        "dblp_pid": "55/2270-25",          # DBLP person ID — Hao Zhang 0025 (UCSD, vLLM)
        "scholar_id": "H1d4BS8AAAAJ",      # Google Scholar user ID
        "website": "https://haozhang.ai/",
        # S2 splits profiles for common names; list ALL known IDs to merge
        "s2_ids": ["2345362123", "2116278298"],
    },
    {
        "name": "Ion Stoica",
        "dblp_pid": "s/IonStoica",
        "scholar_id": "vN-is70AAAAJ",
        "website": "https://people.eecs.berkeley.edu/~istoica/",
        "s2_ids": ["1688378", "2344601177"],
    },
]

S2_API = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,authors,year,venue,publicationDate,externalIds,abstract,tldr,citationCount,url,openAccessPdf,publicationTypes"
S2_BATCH = 100


def _safe_filename(text: str, max_len: int = 80) -> str:
    safe = re.sub(r'[<>:"/\\|?*]', '', text)
    safe = re.sub(r'\s+', '_', safe.strip())
    return safe[:max_len]


def _dedup_key(title: str) -> str:
    """Normalized key for deduplicating papers across sources."""
    return re.sub(r'[^a-z0-9]', '', title.lower())


def safe_get(url: str, retries: int = 3, delay: float = 1.0, timeout: int = 30) -> Optional[requests.Response]:
    """GET with retries and rate-limit handling."""
    for attempt in range(retries):
        try:
            resp = SESSION.get(url, timeout=timeout)
            if resp.status_code == 429:
                wait = min(2 ** (attempt + 2), 30)
                print(f"    Rate limited on {url[:60]}..., waiting {wait}s")
                time.sleep(wait)
                continue
            if resp.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            resp.raise_for_status()
            return resp
        except requests.RequestException:
            time.sleep(2 ** attempt)
    return None


def safe_get_json(url: str, retries: int = 3, delay: float = 1.0) -> dict:
    resp = safe_get(url, retries=retries, delay=delay)
    if resp is None:
        return {}
    try:
        return resp.json()
    except Exception:
        return {}


def download_file(url: str, path: Path, retries: int = 2) -> bool:
    if path.exists() and path.stat().st_size > 1000:
        return True
    for attempt in range(retries):
        try:
            resp = SESSION.get(url, timeout=60, stream=True)
            resp.raise_for_status()
            with open(path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except Exception:
            time.sleep(2 ** attempt)
    return False


# ============================================================================
# Source 1: DBLP — complete CS bibliography
# ============================================================================

def fetch_dblp_papers(dblp_pid: str, name: str) -> list[dict]:
    """Fetch all papers from DBLP for a given person ID."""
    print(f"  [DBLP] Fetching papers for {name} (pid: {dblp_pid})...")
    url = f"https://dblp.org/pid/{dblp_pid}.xml"
    resp = safe_get(url)
    if not resp:
        print(f"    [DBLP] Failed to fetch {url}")
        return []

    soup = BeautifulSoup(resp.content, "lxml-xml")
    papers = []

    for item in soup.find_all("r"):
        # DBLP wraps each publication in <r>, with type tags inside
        pub = item.find(["article", "inproceedings", "incollection", "phdthesis", "mastersthesis", "proceedings", "book"])
        if not pub:
            continue

        title_tag = pub.find("title")
        title = title_tag.get_text(strip=True) if title_tag else ""
        if not title:
            continue

        # Extract authors
        authors = ", ".join(a.get_text(strip=True) for a in pub.find_all("author"))

        # Year
        year_tag = pub.find("year")
        year = int(year_tag.get_text(strip=True)) if year_tag else None

        # Venue
        venue_tags = pub.find_all(["journal", "booktitle"])
        venue = venue_tags[0].get_text(strip=True) if venue_tags else ""

        # URLs
        ee_tags = pub.find_all("ee")
        urls = [e.get_text(strip=True) for e in ee_tags]
        pdf_url = ""
        doi = ""
        arxiv_id = ""
        for u in urls:
            if "doi.org" in u:
                doi = u.replace("https://doi.org/", "").replace("http://doi.org/", "")
            if "arxiv.org" in u:
                m = re.search(r'(\d{4}\.\d{4,5})', u)
                if m:
                    arxiv_id = m.group(1)
                    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            if u.endswith(".pdf"):
                pdf_url = u

        # DBLP key for dedup
        dblp_key = pub.get("key", "")

        papers.append({
            "title": title,
            "authors": authors,
            "year": year,
            "venue": venue,
            "publication_date": "",
            "abstract": "",
            "tldr": "",
            "citation_count": "",
            "arxiv_id": arxiv_id,
            "doi": doi,
            "openreview_id": "",
            "pdf_url": pdf_url,
            "s2_url": "",
            "publication_types": pub.name,  # article, inproceedings, etc.
            "dblp_key": dblp_key,
            "source": "dblp",
        })

    print(f"    [DBLP] Found {len(papers)} papers")
    return papers


# ============================================================================
# Source 2: Google Scholar (via scholarly)
# ============================================================================

def fetch_scholar_papers(scholar_id: str, name: str) -> list[dict]:
    """Fetch papers from Google Scholar using the scholarly library."""
    try:
        from scholarly import scholarly
    except ImportError:
        print("    [Scholar] scholarly not installed, skipping (pip install scholarly)")
        return []

    print(f"  [Scholar] Fetching papers for {name} (ID: {scholar_id})...")
    try:
        author = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(author, sections=["publications"])
    except Exception as e:
        print(f"    [Scholar] Failed: {e}")
        return []

    papers = []
    pubs = author.get("publications", [])
    print(f"    [Scholar] Found {len(pubs)} entries, enriching...")

    for i, pub in enumerate(pubs):
        bib = pub.get("bib", {})
        title = bib.get("title", "")
        if not title:
            continue

        # Try to fill individual publication for abstract (slow, do sparingly)
        abstract = ""
        if i < 200:  # limit to avoid rate limiting
            try:
                filled = scholarly.fill(pub)
                abstract = filled.get("bib", {}).get("abstract", "")
            except Exception:
                pass

        papers.append({
            "title": title,
            "authors": bib.get("author", ""),
            "year": bib.get("pub_year", ""),
            "venue": bib.get("journal", "") or bib.get("conference", "") or bib.get("venue", ""),
            "publication_date": "",
            "abstract": abstract,
            "tldr": "",
            "citation_count": pub.get("num_citations", ""),
            "arxiv_id": "",
            "doi": "",
            "openreview_id": "",
            "pdf_url": pub.get("pub_url", ""),
            "s2_url": "",
            "publication_types": "",
            "source": "scholar",
        })

    print(f"    [Scholar] Processed {len(papers)} papers")
    return papers


# ============================================================================
# Source 3: Personal website scraping
# ============================================================================

def _resolve_arxiv_titles(arxiv_ids: list[str]) -> dict[str, dict]:
    """Batch-resolve arxiv IDs to titles/authors/abstracts via arxiv API."""
    if not arxiv_ids:
        return {}

    results = {}
    # arxiv API accepts up to ~200 IDs per request
    batch_size = 50
    for i in range(0, len(arxiv_ids), batch_size):
        batch = arxiv_ids[i:i+batch_size]
        id_list = ",".join(batch)
        url = f"http://export.arxiv.org/api/query?id_list={id_list}&max_results={len(batch)}"
        try:
            resp = SESSION.get(url, timeout=30)
            if resp.status_code != 200:
                continue
            soup = BeautifulSoup(resp.text, "lxml-xml")
            for entry in soup.find_all("entry"):
                aid_tag = entry.find("id")
                if not aid_tag:
                    continue
                aid_text = aid_tag.text.strip()
                m = re.search(r'(\d{4}\.\d{4,5})', aid_text)
                if not m:
                    continue
                aid = m.group(1)
                title = entry.find("title")
                summary = entry.find("summary")
                authors = [a.find("name").text for a in entry.find_all("author") if a.find("name")]
                published = entry.find("published")
                results[aid] = {
                    "title": re.sub(r'\s+', ' ', title.text.strip()) if title else "",
                    "abstract": summary.text.strip() if summary else "",
                    "authors": ", ".join(authors),
                    "publication_date": published.text.strip()[:10] if published else "",
                }
            time.sleep(0.5)
        except Exception:
            pass
    return results


def _extract_arxiv_ids_from_html(soup: BeautifulSoup) -> list[str]:
    """Extract all unique arxiv IDs from a page."""
    ids = []
    seen = set()
    for link in soup.find_all("a", href=True):
        href = link.get("href", "")
        if "arxiv.org" in href:
            m = re.search(r'(\d{4}\.\d{4,5})', href)
            if m and m.group(1) not in seen:
                ids.append(m.group(1))
                seen.add(m.group(1))
    return ids


def fetch_website_papers(url: str, name: str) -> list[dict]:
    """Scrape papers from an author's personal website.

    Strategy: extract all arxiv IDs from the page (and subpages like /publications),
    then batch-resolve titles via the arxiv API.
    """
    print(f"  [Website] Scraping {url}...")
    resp = safe_get(url)
    if not resp:
        print(f"    [Website] Failed to fetch {url}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    all_arxiv_ids = _extract_arxiv_ids_from_html(soup)

    # Also extract DOI/PDF links
    doi_links = []
    pdf_links = []
    for link in soup.find_all("a", href=True):
        href = link.get("href", "")
        if "doi.org" in href:
            doi = re.sub(r'https?://doi\.org/', '', href)
            doi_links.append(doi)
        elif href.endswith(".pdf") and "arxiv" not in href:
            pdf_url = href if href.startswith("http") else f"{url.rstrip('/')}/{href.lstrip('/')}"
            pdf_links.append((link.get_text(strip=True), pdf_url))

    # Check subpages for more papers
    for subpage in ["/publications", "/papers", "/research", "/pubs"]:
        sub_url = url.rstrip("/") + subpage
        try:
            sub_resp = SESSION.get(sub_url, timeout=10, allow_redirects=True)
            if sub_resp.status_code == 200 and sub_resp.url != resp.url:
                sub_soup = BeautifulSoup(sub_resp.text, "html.parser")
                all_arxiv_ids.extend(_extract_arxiv_ids_from_html(sub_soup))
        except Exception:
            pass

    # Deduplicate arxiv IDs
    seen = set()
    unique_ids = []
    for aid in all_arxiv_ids:
        if aid not in seen:
            unique_ids.append(aid)
            seen.add(aid)
    all_arxiv_ids = unique_ids

    # Resolve titles via arxiv API
    print(f"    [Website] Found {len(all_arxiv_ids)} arxiv IDs, resolving titles...")
    resolved = _resolve_arxiv_titles(all_arxiv_ids)

    papers = []
    for aid in all_arxiv_ids:
        info = resolved.get(aid, {})
        title = info.get("title", "")
        if not title:
            title = f"arXiv:{aid}"  # fallback

        papers.append({
            "title": title,
            "authors": info.get("authors", ""),
            "year": info.get("publication_date", "")[:4] or "",
            "venue": "",
            "publication_date": info.get("publication_date", ""),
            "abstract": info.get("abstract", ""),
            "tldr": "",
            "citation_count": "",
            "arxiv_id": aid,
            "doi": "",
            "openreview_id": "",
            "pdf_url": f"https://arxiv.org/pdf/{aid}.pdf",
            "s2_url": "",
            "publication_types": "",
            "source": "website",
        })

    print(f"    [Website] Resolved {len(papers)} papers")
    return papers


# ============================================================================
# Source 4: Semantic Scholar — enrichment (abstracts, citations, external IDs)
# ============================================================================

def fetch_s2_papers(s2_ids: list[str], name: str) -> list[dict]:
    """Fetch papers from all Semantic Scholar author IDs."""
    papers = []
    for s2_id in s2_ids:
        print(f"  [S2] Fetching papers for {name} (S2 ID: {s2_id})...")
        offset = 0
        fail_count = 0
        while True:
            url = (f"{S2_API}/author/{s2_id}/papers"
                   f"?fields={S2_FIELDS}&limit={S2_BATCH}&offset={offset}")
            data = safe_get_json(url)
            if not data or "data" not in data:
                fail_count += 1
                if fail_count >= 2:
                    print(f"    [S2] Rate limited, skipping remaining for ID {s2_id}")
                    break
                time.sleep(5)
                continue
            batch = data["data"]
            if not batch:
                break
            fail_count = 0

            for paper in batch:
                ext_ids = paper.get("externalIds") or {}
                arxiv_id = ext_ids.get("ArXiv", "")
                doi = ext_ids.get("DOI", "")
                openreview_id = ext_ids.get("OpenReview", "")

                tldr = paper.get("tldr")
                if isinstance(tldr, dict):
                    tldr = tldr.get("text", "")
                elif tldr is None:
                    tldr = ""

                oa_pdf = paper.get("openAccessPdf")
                pdf_url = oa_pdf.get("url", "") if isinstance(oa_pdf, dict) else ""
                if not pdf_url and arxiv_id:
                    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

                authors = ", ".join(a.get("name", "") for a in (paper.get("authors") or []))

                papers.append({
                    "title": paper.get("title", ""),
                    "authors": authors,
                    "year": paper.get("year") or "",
                    "venue": paper.get("venue", ""),
                    "publication_date": paper.get("publicationDate", ""),
                    "abstract": paper.get("abstract") or "",
                    "tldr": tldr,
                    "citation_count": paper.get("citationCount", 0),
                    "arxiv_id": arxiv_id,
                    "doi": doi,
                    "openreview_id": openreview_id,
                    "pdf_url": pdf_url,
                    "s2_url": paper.get("url", ""),
                    "publication_types": ", ".join(paper.get("publicationTypes") or []),
                    "source": "s2",
                })

            offset += S2_BATCH
            time.sleep(1.0)
            total = data.get("total", 0)
            if total and offset >= total:
                break

        print(f"    [S2] Found {len(papers)} papers from ID {s2_id}")
    return papers


def enrich_with_s2(papers: list[dict]) -> list[dict]:
    """Enrich papers that have arxiv_id or doi but missing abstract/citations via S2.

    Bails out early if rate-limited to avoid blocking for minutes.
    """
    enriched = 0
    rate_limit_count = 0
    to_enrich = [p for p in papers
                 if (not p.get("abstract") or not p.get("citation_count"))
                 and (p.get("arxiv_id") or p.get("doi"))]

    if not to_enrich:
        return papers

    print(f"    [S2] Enriching {len(to_enrich)} papers...")

    for p in to_enrich:
        lookup_id = None
        if p.get("arxiv_id"):
            lookup_id = f"ArXiv:{p['arxiv_id']}"
        elif p.get("doi"):
            lookup_id = f"DOI:{p['doi']}"
        else:
            continue

        url = f"{S2_API}/paper/{lookup_id}?fields={S2_FIELDS}"
        resp = safe_get(url, retries=1, delay=0.5)  # only 1 retry to avoid blocking

        if resp is None:
            rate_limit_count += 1
            if rate_limit_count >= 3:
                print(f"    [S2] Too many failures/rate limits, skipping remaining enrichment")
                break
            continue

        try:
            data = resp.json()
        except Exception:
            continue

        if "paperId" not in data:
            continue

        rate_limit_count = 0  # reset on success

        if not p.get("abstract"):
            p["abstract"] = data.get("abstract") or ""
        if not p.get("citation_count"):
            p["citation_count"] = data.get("citationCount", "")

        tldr = data.get("tldr")
        if not p.get("tldr") and isinstance(tldr, dict):
            p["tldr"] = tldr.get("text", "")

        ext_ids = data.get("externalIds") or {}
        if not p.get("openreview_id"):
            p["openreview_id"] = ext_ids.get("OpenReview", "")
        if not p.get("arxiv_id"):
            p["arxiv_id"] = ext_ids.get("ArXiv", "")
        if not p.get("s2_url"):
            p["s2_url"] = data.get("url", "")

        oa_pdf = data.get("openAccessPdf")
        if not p.get("pdf_url") and isinstance(oa_pdf, dict):
            p["pdf_url"] = oa_pdf.get("url", "")

        enriched += 1
        time.sleep(1.0)  # respect rate limits

    print(f"    [S2] Enriched {enriched}/{len(to_enrich)} papers")
    return papers


# ============================================================================
# Source 5: OpenReview — find forum IDs + full review discussions
# ============================================================================

OR_VENUES = {"ICLR", "NeurIPS", "ICML", "COLM", "EMNLP", "ACL", "AAAI"}

# Venue CSV files for cross-referencing forum IDs
VENUE_CSVS = [
    "research_data/iclr/iclr_2024_papers.csv",
    "research_data/iclr/iclr_2025_papers.csv",
    "research_data/iclr/iclr_2026_papers.csv",
    "research_data/neurips/neurips_2024_papers.csv",
    "research_data/neurips/neurips_2025_papers.csv",
    "research_data/icml/icml_2025_papers.csv",
]


def _build_venue_lookup() -> dict[str, str]:
    """Build title_key -> forum_id lookup from local venue CSV databases."""
    lookup: dict[str, str] = {}
    base = Path(__file__).parent
    for csv_path in VENUE_CSVS:
        full_path = base / csv_path
        if not full_path.exists():
            continue
        try:
            with open(full_path, encoding="utf-8", errors="replace") as f:
                reader = csv.DictReader(f)
                cols = reader.fieldnames or []
                fid_col = None
                for c in cols:
                    if "forum" in c.lower() or c == "id":
                        fid_col = c
                        break
                if not fid_col:
                    continue
                for row in reader:
                    title = row.get("title", "")
                    fid = row.get(fid_col, "")
                    if title and fid:
                        # Extract ID from URL if needed
                        if "forum?id=" in fid:
                            fid = fid.split("forum?id=")[-1]
                        lookup[_dedup_key(title)] = fid
        except Exception:
            pass
    return lookup


def crossref_openreview_ids(papers: list[dict]) -> int:
    """Fill in openreview_id by matching titles against local venue databases."""
    lookup = _build_venue_lookup()
    if not lookup:
        return 0
    matched = 0
    for p in papers:
        if p.get("openreview_id"):
            continue
        key = _dedup_key(p.get("title", ""))
        if key in lookup:
            p["openreview_id"] = lookup[key]
            matched += 1
    return matched


def find_openreview_ids(papers: list[dict]) -> list[dict]:
    """Search OpenReview by title to find forum IDs for papers missing them.

    Uses the /notes/search endpoint which does full-text search (no auth needed).
    Only searches papers from venues that use OpenReview.
    """
    to_search = []
    for p in papers:
        if p.get("openreview_id"):
            continue
        venue = str(p.get("venue", ""))
        # Only search venues that use OpenReview
        if any(v.lower() in venue.lower() for v in OR_VENUES) or "Conference" in venue:
            to_search.append(p)

    if not to_search:
        print(f"    [OpenReview] No papers to search (all have IDs or not from OR venues)")
        return papers

    print(f"    [OpenReview] Searching for forum IDs for {len(to_search)} papers...")
    found = 0

    for p in to_search:
        title = p.get("title", "")
        if not title or len(title) < 10:
            continue

        # Search using key words from the title (first ~6 significant words)
        words = [w for w in title.split() if len(w) > 2][:6]
        query = "+".join(words)
        url = f"https://api2.openreview.net/notes/search?query={requests.utils.quote(query)}&limit=5"

        data = safe_get_json(url, retries=2, delay=0.5)
        notes = data.get("notes", [])

        # Match by normalized title
        target_key = _dedup_key(title)
        for note in notes:
            content = note.get("content", {})
            note_title = content.get("title", {})
            if isinstance(note_title, dict):
                note_title = note_title.get("value", "")
            note_key = _dedup_key(str(note_title))

            if note_key == target_key:
                forum_id = note.get("forum", note.get("id", ""))
                # Skip DBLP imports — they don't have reviews
                invitations = note.get("invitations", [])
                if any("DBLP" in inv for inv in invitations):
                    continue
                if forum_id:
                    p["openreview_id"] = forum_id
                    found += 1
                    break

        time.sleep(1.0)  # be nice to the API

    print(f"    [OpenReview] Found forum IDs for {found}/{len(to_search)} papers")
    return papers


def fetch_openreview_discussion(forum_id: str, title: str, output_path: Path) -> dict:
    """Fetch all comments (reviews, rebuttals, meta-reviews) for a paper."""
    if output_path.exists() and output_path.stat().st_size > 100:
        return {"title": title, "status": "cached", "path": str(output_path)}

    try:
        time.sleep(1.5)  # pace requests to avoid rate limits
        data = safe_get_json(f"https://api2.openreview.net/notes?forum={forum_id}&limit=100", retries=4, delay=3.0)
        notes = data.get("notes", [])
        if not notes:
            return {"title": title, "status": "no_data", "forum_id": forum_id}

        reviews = []
        rebuttals = []
        meta_reviews = []
        other_comments = []
        paper_content = None

        for note in notes:
            invs = note.get("invitations", [])
            inv_str = invs[0] if invs else ""
            content = note.get("content", {})

            extracted = {}
            for key, val in content.items():
                extracted[key] = val.get("value", "") if isinstance(val, dict) else val

            entry = {
                "id": note.get("id", ""),
                "invitation": inv_str,
                "signatures": note.get("signatures", []),
                "created": note.get("cdate"),
                "modified": note.get("mdate"),
                "replyto": note.get("replyto", ""),
                "content": extracted,
            }

            if note.get("id") == forum_id:
                paper_content = extracted
            elif "Official_Review" in inv_str:
                reviews.append(entry)
            elif "Official_Comment" in inv_str:
                sigs = note.get("signatures", [])
                is_author = any("Authors" in s for s in sigs)
                if is_author:
                    rebuttals.append(entry)
                else:
                    other_comments.append(entry)
            elif "Meta_Review" in inv_str or "Decision" in inv_str:
                meta_reviews.append(entry)
            elif note.get("id") != forum_id:
                other_comments.append(entry)

        # Build threaded discussions
        threads = []
        for review in reviews:
            thread = {"review": review, "responses": []}
            for entry in reviews + rebuttals + meta_reviews + other_comments:
                if entry["replyto"] == review["id"]:
                    thread["responses"].append(entry)
            thread["responses"].sort(key=lambda x: x.get("created") or 0)
            threads.append(thread)

        discussion_data = {
            "title": title,
            "forum_id": forum_id,
            "forum_url": f"https://openreview.net/forum?id={forum_id}",
            "num_reviews": len(reviews),
            "num_rebuttals": len(rebuttals),
            "num_meta_reviews": len(meta_reviews),
            "num_other_comments": len(other_comments),
            "paper_content": paper_content,
            "threads": threads,
            "meta_reviews": meta_reviews,
            "unthreaded_comments": [
                c for c in other_comments
                if c["replyto"] not in {r["id"] for r in reviews}
            ],
        }

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(discussion_data, f, indent=2, ensure_ascii=False)

        time.sleep(0.5)
        return {
            "title": title, "status": "fetched", "path": str(output_path),
            "reviews": len(reviews), "rebuttals": len(rebuttals),
        }
    except Exception as e:
        return {"title": title, "status": "error", "reason": str(e)}


# ============================================================================
# Merge & deduplicate papers from all sources
# ============================================================================

def merge_papers(all_sources: list[list[dict]]) -> list[dict]:
    """Merge papers from multiple sources, preferring richer metadata."""
    by_key: dict[str, dict] = {}

    for papers in all_sources:
        for p in papers:
            key = _dedup_key(p.get("title", ""))
            if not key or len(key) < 5:
                continue

            if key in by_key:
                # Merge: fill in missing fields from this source
                existing = by_key[key]
                for field in p:
                    if field == "source":
                        # Track all sources
                        existing["source"] = existing.get("source", "") + "," + p.get("source", "")
                        continue
                    if not existing.get(field) and p.get(field):
                        existing[field] = p[field]
                # Prefer higher citation count
                try:
                    if int(p.get("citation_count") or 0) > int(existing.get("citation_count") or 0):
                        existing["citation_count"] = p["citation_count"]
                except (ValueError, TypeError):
                    pass
            else:
                by_key[key] = dict(p)

    merged = list(by_key.values())
    # Sort by year desc, then citation count desc
    def sort_key(p):
        try:
            y = int(p.get("year") or 0)
        except (ValueError, TypeError):
            y = 0
        try:
            c = int(p.get("citation_count") or 0)
        except (ValueError, TypeError):
            c = 0
        return (-y, -c)

    merged.sort(key=sort_key)
    return merged


# ============================================================================
# CSV output
# ============================================================================

CSV_FIELDS = [
    "title", "authors", "year", "venue", "publication_date",
    "citation_count", "arxiv_id", "doi", "openreview_id",
    "tldr", "abstract", "pdf_url", "s2_url", "publication_types", "source",
]


def save_csv(papers: list[dict], output_path: Path):
    if not papers:
        return
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(papers)
    print(f"  Saved {len(papers)} papers to {output_path}")


# ============================================================================
# Main crawl pipeline
# ============================================================================

def crawl_author(
    name: str,
    dblp_pid: Optional[str] = None,
    scholar_id: Optional[str] = None,
    website: Optional[str] = None,
    s2_ids: Optional[list[str]] = None,
    output_dir: Path = OUTPUT_DIR,
    download_pdfs: bool = True,
    fetch_reviews: bool = True,
    dry_run: bool = False,
    refresh: bool = False,
    workers: int = 2,
    enrich: bool = True,
):
    safe_name = _safe_filename(name)
    author_dir = output_dir / safe_name
    author_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir = author_dir / "pdfs"
    review_dir = author_dir / "reviews"

    print(f"\n{'='*60}")
    print(f"Crawling papers for: {name}")
    print(f"{'='*60}")

    csv_path = author_dir / "papers.csv"

    if csv_path.exists() and not refresh:
        with open(csv_path, "r", encoding="utf-8") as f:
            papers = list(csv.DictReader(f))
        print(f"  Loaded {len(papers)} cached papers (use --refresh to re-fetch)")
    else:
        # Collect papers from all sources
        all_sources = []

        # Source 1: DBLP (most reliable for CS papers)
        if dblp_pid:
            all_sources.append(fetch_dblp_papers(dblp_pid, name))

        # Source 2: Google Scholar (best citation data)
        if scholar_id:
            all_sources.append(fetch_scholar_papers(scholar_id, name))

        # Source 3: Personal website
        if website:
            all_sources.append(fetch_website_papers(website, name))

        # Source 4: Semantic Scholar (abstracts, external IDs)
        if s2_ids:
            all_sources.append(fetch_s2_papers(s2_ids, name))

        # Merge and deduplicate
        papers = merge_papers(all_sources)
        print(f"\n  After merging & dedup: {len(papers)} unique papers")

    # Enrich with S2 (fill in missing abstracts, citations, openreview IDs)
    # Runs on both fresh and cached data if papers still lack enrichment
    if enrich:
        needs_enrich = [p for p in papers
                        if (not p.get("abstract") or not p.get("openreview_id"))
                        and (p.get("arxiv_id") or p.get("doi"))]
        if needs_enrich:
            print(f"  Enriching {len(needs_enrich)} papers missing abstracts/OpenReview IDs via S2...")
            papers = enrich_with_s2(papers)
            save_csv(papers, csv_path)
        else:
            print(f"  All papers already enriched")
            if not (csv_path.exists() and not refresh):
                save_csv(papers, csv_path)
    else:
        if not (csv_path.exists() and not refresh):
            save_csv(papers, csv_path)

    if not papers:
        print(f"  No papers found for {name}")
        return

    # Print summary
    years: dict[str, int] = {}
    for p in papers:
        y = str(p.get("year", "") or "?")
        years[y] = years.get(y, 0) + 1
    print(f"\n  Papers by year:")
    for y in sorted(years.keys(), reverse=True)[:15]:
        print(f"    {y}: {years[y]} papers")

    venues: dict[str, int] = {}
    for p in papers:
        v = p.get("venue", "") or "Unknown"
        if v:
            venues[v] = venues.get(v, 0) + 1
    print(f"\n  Top venues:")
    for v, count in sorted(venues.items(), key=lambda x: -x[1])[:10]:
        print(f"    {count:4d} | {v[:60]}")

    if dry_run:
        or_count = sum(1 for p in papers if p.get("openreview_id"))
        pdf_count = sum(1 for p in papers if p.get("pdf_url"))
        print(f"\n  [DRY RUN] {len(papers)} papers total")
        print(f"  {or_count} with OpenReview IDs (reviews available)")
        print(f"  {pdf_count} with PDF URLs")
        print(f"\n  Most cited papers:")
        for p in sorted(papers, key=lambda x: -(int(x.get("citation_count") or 0)))[:15]:
            cite = str(p.get("citation_count", "?"))
            year = p.get("year", "?")
            title = str(p.get("title", ""))[:65]
            venue = str(p.get("venue", "") or "")[:20]
            print(f"    {cite:>6s} cites | {year} | {venue:20s} | {title}")
        return

    # Find OpenReview forum IDs: first cross-reference local venue DBs, then search API
    if fetch_reviews:
        xref = crossref_openreview_ids(papers)
        if xref:
            print(f"  Cross-referenced {xref} papers with local venue databases")
            save_csv(papers, csv_path)

        or_missing = sum(1 for p in papers if not p.get("openreview_id"))
        if or_missing:
            papers = find_openreview_ids(papers)
            save_csv(papers, csv_path)

    # Fetch OpenReview discussions
    if fetch_reviews:
        review_dir.mkdir(parents=True, exist_ok=True)
        or_papers = [p for p in papers if p.get("openreview_id")]
        if or_papers:
            print(f"\n  Fetching OpenReview discussions for {len(or_papers)} papers...")
            fetched = cached = failed = 0

            with ThreadPoolExecutor(max_workers=1) as pool:  # sequential to avoid OR rate limits
                futures = {}
                for p in or_papers:
                    safe_title = _safe_filename(p["title"])
                    review_path = review_dir / f"{safe_title}.json"
                    futures[pool.submit(
                        fetch_openreview_discussion,
                        p["openreview_id"], p["title"], review_path
                    )] = p

                for future in as_completed(futures):
                    r = future.result()
                    status = r.get("status", "error")
                    if status == "fetched":
                        fetched += 1
                        n_rev = r.get("reviews", 0)
                        n_reb = r.get("rebuttals", 0)
                        title = r["title"][:50].encode("ascii", "replace").decode("ascii")
                        print(f"    [OK] {n_rev} reviews, {n_reb} rebuttals | {title}")
                    elif status == "cached":
                        cached += 1
                    else:
                        failed += 1

            print(f"  Reviews: {fetched} fetched, {cached} cached, {failed} failed")
        else:
            print(f"\n  No papers with OpenReview IDs found")

    # Download PDFs
    if download_pdfs:
        pdf_dir.mkdir(parents=True, exist_ok=True)
        pdf_papers = [p for p in papers if p.get("pdf_url")]
        print(f"\n  Downloading PDFs for {len(pdf_papers)} papers...")
        ok = failed = 0

        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {}
            for p in pdf_papers:
                safe_title = _safe_filename(p["title"])
                pdf_path = pdf_dir / f"{safe_title}.pdf"
                futures[pool.submit(download_file, p["pdf_url"], pdf_path)] = p

            for future in as_completed(futures):
                try:
                    if future.result():
                        ok += 1
                    else:
                        failed += 1
                except Exception:
                    failed += 1

        print(f"  PDFs: {ok} ok, {failed} failed")

    print(f"\n  Done! Output in {author_dir}/")


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Crawl all papers by specific researchers from multiple sources"
    )
    parser.add_argument(
        "--authors", "-a", type=str, default=None,
        help="Comma-separated author names (default: Hao Zhang, Ion Stoica)"
    )
    parser.add_argument("--output", type=str, default=str(OUTPUT_DIR))
    parser.add_argument("--no-pdfs", action="store_true", help="Skip PDF downloads")
    parser.add_argument("--reviews-only", action="store_true", help="Only fetch reviews")
    parser.add_argument("--no-reviews", action="store_true", help="Skip review fetching")
    parser.add_argument("--dry-run", action="store_true", help="Preview without downloading")
    parser.add_argument("--refresh", action="store_true", help="Re-fetch even if cached")
    parser.add_argument("--workers", type=int, default=2, help="Parallel workers")
    parser.add_argument("--no-scholar", action="store_true", help="Skip Google Scholar (avoids CAPTCHA)")
    parser.add_argument("--no-s2", action="store_true", help="Skip Semantic Scholar entirely")
    parser.add_argument("--no-enrich", action="store_true", help="Skip S2 enrichment step")
    args = parser.parse_args()

    output_dir = Path(args.output)

    if args.authors:
        names = [n.strip() for n in args.authors.split(",")]
        authors = [{"name": n} for n in names]
    else:
        authors = DEFAULT_AUTHORS

    for author in authors:
        crawl_author(
            name=author["name"],
            dblp_pid=author.get("dblp_pid"),
            scholar_id=None if args.no_scholar else author.get("scholar_id"),
            website=author.get("website"),
            s2_ids=None if args.no_s2 else author.get("s2_ids"),
            output_dir=output_dir,
            download_pdfs=not args.no_pdfs and not args.reviews_only,
            fetch_reviews=not args.no_reviews,
            dry_run=args.dry_run,
            refresh=args.refresh,
            workers=args.workers,
            enrich=not args.no_enrich and not args.no_s2,
        )

    print(f"\n{'='*60}")
    print(f"All done! Output in {output_dir}/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
