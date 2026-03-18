#!/usr/bin/env python3
"""
IdeaForge Setup Pipeline

One-script setup that crawls papers, builds training data, creates the FAISS
embedding index, and verifies the pre-trained judge — getting you to the point
where you can immediately run the adversarial idea refiner.

All outputs go to a `resources/` folder (configurable via --resources-dir) so
the setup does not interfere with existing local data.

Three modes:
    python setup_pipeline.py --test        # No crawl — synthetic data, tests downstream pipeline
    python setup_pipeline.py               # Normal — ~100 representative papers, safe QPS
    python setup_pipeline.py --full        # Full crawl — all papers, use at your own risk
    python setup_pipeline.py --check       # Just verify everything is ready

Prerequisites:
    - Python 3.10+
    - pip install -r requirements.txt
    - pip install sentence-transformers faiss-cpu numpy
    - Claude Code CLI installed and authenticated (for idea refinement)
"""

import argparse
import importlib
import json
import os
import random
import shutil
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent
JUDGE_DIR = BASE_DIR / "judge_training"

# Default resources directory — all pipeline outputs go here
DEFAULT_RESOURCES_DIR = BASE_DIR / "resources"

# Conservative QPS to avoid bot detection (seconds between API calls)
CRAWL_DELAY = 2.0


def get_resource_paths(resources_dir: Path) -> dict:
    """Resolve all resource paths relative to the resources directory."""
    return {
        "resources_dir": resources_dir,
        "research_data": resources_dir / "research_data",
        "data": resources_dir / "data",
        "embeddings": resources_dir / "embeddings",
        "skills": resources_dir / "skills",
        "output": resources_dir / "output",
    }


def print_header(msg: str):
    print(f"\n{'='*60}")
    print(f"  {msg}")
    print(f"{'='*60}\n")


def print_step(step: int, total: int, msg: str):
    print(f"[{step}/{total}] {msg}")


def check_dependencies() -> list[str]:
    """Check all required packages are installed."""
    missing = []
    for pkg, import_name in [
        ("openreview-py", "openreview"),
        ("pandas", "pandas"),
        ("tqdm", "tqdm"),
        ("requests", "requests"),
        ("sentence-transformers", "sentence_transformers"),
        ("faiss-cpu", "faiss"),
        ("numpy", "numpy"),
    ]:
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing.append(pkg)
    return missing


def get_openreview_credentials() -> tuple[str, str]:
    """Load OpenReview credentials from config.py or environment variables.

    Resolution order:
      1. OPENREVIEW_USERNAME / OPENREVIEW_PASSWORD env vars
      2. config.py  EMAIL / PASSWORD

    Returns (username, password) — either or both may be empty strings.
    """
    username = os.environ.get("OPENREVIEW_USERNAME", "")
    password = os.environ.get("OPENREVIEW_PASSWORD", "")
    if username and password:
        return username, password

    try:
        # config.py sits at repo root and is in .gitignore
        sys.path.insert(0, str(BASE_DIR))
        from config import EMAIL, PASSWORD
        if EMAIL and PASSWORD:
            return EMAIL, PASSWORD
    except ImportError:
        pass

    return "", ""


def check_claude_cli() -> bool:
    """Check if Claude Code CLI is available."""
    return shutil.which("claude") is not None


def run_script(script_path: str, args: list[str] = None, cwd: str = None,
               env_extra: dict = None):
    """Run a Python script as subprocess with optional extra env vars."""
    cmd = [sys.executable, script_path] + (args or [])
    env = os.environ.copy()
    if env_extra:
        env.update(env_extra)
    result = subprocess.run(
        cmd,
        cwd=cwd or str(BASE_DIR),
        capture_output=False,
        env=env,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Script failed: {script_path} (exit code {result.returncode})")


def crawl_representative_papers(paths: dict, username: str = "",
                                password: str = "", n_papers: int = 100):
    """Crawl a representative sample of ~n_papers across venues and years.

    Samples across ICLR (2024, 2025), balancing accepted/rejected and score
    ranges to get a training-useful distribution. Uses conservative QPS.
    """
    print_header("Stage 1: Crawling Representative Papers (Normal Mode)")
    print(f"  Target: ~{n_papers} papers across venues and score ranges")
    print(f"  Delay between API calls: {CRAWL_DELAY}s\n")

    import openreview.api

    _BROWSER_UA = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    )

    client = openreview.api.OpenReviewClient(
        baseurl='https://api2.openreview.net',
        username=username or None,
        password=password or None,
    )
    client.headers['User-Agent'] = _BROWSER_UA
    client.session.headers['User-Agent'] = _BROWSER_UA

    # Crawl from ICLR (has both accepted and rejected papers — best for training)
    venues = [
        ("ICLR", "ICLR.cc/2025/Conference", 2025),
        ("ICLR", "ICLR.cc/2024/Conference", 2024),
    ]

    all_papers = []
    for venue_name, venue_id, year in venues:
        print(f"  Fetching {venue_name} {year} submissions...")
        time.sleep(CRAWL_DELAY)
        try:
            submissions = list(client.get_all_notes(
                content={'venueid': venue_id},
                details='directReplies',
            ))
            print(f"    Found {len(submissions)} accepted papers")
            for s in submissions:
                all_papers.append((venue_name, year, "accepted", s))
        except Exception as e:
            print(f"    Failed to fetch accepted: {e}")

        # Also try to get rejected papers (ICLR exposes these)
        time.sleep(CRAWL_DELAY)
        try:
            rejected = list(client.get_all_notes(
                invitation=f'{venue_id}/-/Submission',
                details='directReplies',
            ))
            # Filter to only rejected (not in accepted set)
            accepted_ids = {s.id for _, _, _, s in all_papers}
            rejected_only = [s for s in rejected if s.id not in accepted_ids]
            print(f"    Found {len(rejected_only)} additional rejected/withdrawn papers")
            for s in rejected_only:
                all_papers.append((venue_name, year, "rejected", s))
        except Exception:
            pass  # Some venues don't expose rejected papers

    if not all_papers:
        print("  No papers fetched — will use synthetic data.")
        return

    # Stratified sample: balance across years and decisions
    random.seed(42)
    random.shuffle(all_papers)

    # Try to get a mix: ~60% accepted, ~40% rejected, split across years
    accepted = [p for p in all_papers if p[2] == "accepted"]
    rejected = [p for p in all_papers if p[2] == "rejected"]

    n_accepted = min(len(accepted), int(n_papers * 0.6))
    n_rejected = min(len(rejected), n_papers - n_accepted)
    n_accepted = min(len(accepted), n_papers - n_rejected)  # rebalance

    sampled = random.sample(accepted, n_accepted) + random.sample(rejected, n_rejected)
    random.shuffle(sampled)

    print(f"\n  Sampled {len(sampled)} papers ({n_accepted} accepted, {n_rejected} rejected)")

    # Now fetch reviews for each sampled paper
    import csv

    research_dir = paths["research_data"] / "iclr"
    research_dir.mkdir(parents=True, exist_ok=True)

    csv_rows = []
    review_count = 0
    for i, (venue_name, year, decision, note) in enumerate(sampled):
        content = note.content
        title_val = content.get('title', {})
        title = title_val.get('value', title_val) if isinstance(title_val, dict) else str(title_val)
        abstract_val = content.get('abstract', {})
        abstract = abstract_val.get('value', abstract_val) if isinstance(abstract_val, dict) else str(abstract_val)
        keywords_val = content.get('keywords', {})
        keywords = keywords_val.get('value', keywords_val) if isinstance(keywords_val, dict) else keywords_val

        # Extract reviews from directReplies
        reviews = []
        scores = []
        if hasattr(note, 'details') and note.details:
            for reply in note.details.get('directReplies', []):
                rc = reply.get('content', {})
                rating = rc.get('rating', rc.get('recommendation', {}))
                if isinstance(rating, dict):
                    rating = rating.get('value', '')
                rating_str = str(rating)
                # Extract numeric score
                try:
                    score = float(rating_str.split(':')[0].strip())
                    scores.append(score)
                except (ValueError, IndexError):
                    pass
                strengths = rc.get('strengths', rc.get('summary', {}))
                if isinstance(strengths, dict):
                    strengths = strengths.get('value', '')
                weaknesses = rc.get('weaknesses', {})
                if isinstance(weaknesses, dict):
                    weaknesses = weaknesses.get('value', '')
                if strengths or weaknesses:
                    reviews.append({
                        "rating": rating_str,
                        "strengths": str(strengths)[:500],
                        "weaknesses": str(weaknesses)[:500],
                    })

        avg_score = sum(scores) / len(scores) if scores else 0

        csv_rows.append({
            "forum_id": note.id,
            "title": title,
            "abstract": str(abstract)[:1000],
            "venue": f"{venue_name} {year}",
            "decision": decision,
            "avg_rating": f"{avg_score:.1f}",
            "keywords": "; ".join(keywords) if isinstance(keywords, list) else str(keywords),
        })

        # Save review JSON if we got reviews
        if reviews:
            review_dir = research_dir / str(year) / "reviews"
            review_dir.mkdir(parents=True, exist_ok=True)
            review_path = review_dir / f"{note.id}.json"
            with open(review_path, "w", encoding="utf-8") as f:
                json.dump({
                    "forum_id": note.id,
                    "title": title,
                    "venue": f"{venue_name} {year}",
                    "decision": decision,
                    "avg_score": avg_score,
                    "scores": scores,
                    "reviews": reviews,
                }, f, ensure_ascii=False, indent=2)
            review_count += 1

        if (i + 1) % 20 == 0:
            print(f"    Processed {i+1}/{len(sampled)} papers...")

    # Save CSV
    csv_path = research_dir / f"iclr_representative_sample.csv"
    if csv_rows:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_rows[0].keys())
            writer.writeheader()
            writer.writerows(csv_rows)

    print(f"  Saved {len(csv_rows)} papers to {csv_path}")
    print(f"  Saved {review_count} review JSONs to {research_dir}")


def crawl_all_papers(years: list[int], paths: dict, username: str = "",
                     password: str = ""):
    """Full crawl — all papers from all venues. Use at your own risk."""
    print_header("Stage 1: Full Paper Crawl (ALL papers — use at your own risk)")
    print("  WARNING: This crawls ~50K+ papers. May take 2-3 hours.")
    print("  Consider running during off-peak hours.\n")

    env_extra = {"IDEAFORGE_RESOURCES_DIR": str(paths["resources_dir"])}
    if username and password:
        env_extra["OPENREVIEW_USERNAME"] = username
        env_extra["OPENREVIEW_PASSWORD"] = password

    # Ensure output dirs exist
    for subdir in ["iclr", "icml", "neurips"]:
        (paths["research_data"] / subdir).mkdir(parents=True, exist_ok=True)

    for year in years:
        print(f"\n--- Crawling ICLR {year} ---")
        crawl_args = ["--year", str(year)]
        crawl_args += ["--output", str(paths["research_data"] / "iclr")]
        if username and password:
            crawl_args += ["--username", username, "--password", password]
        try:
            run_script(
                str(BASE_DIR / "data_pipeline" / "openreview_crawler.py"),
                crawl_args, env_extra=env_extra,
            )
        except RuntimeError as e:
            print(f"Warning: ICLR {year} crawl failed: {e}")

    # ICML
    print(f"\n--- Crawling ICML ---")
    try:
        icml_args = ["--output", str(paths["research_data"] / "icml")]
        run_script(str(BASE_DIR / "crawl_icml.py"), icml_args,
                   env_extra=env_extra)
    except RuntimeError as e:
        print(f"Warning: ICML crawl failed: {e}")

    # NeurIPS
    print(f"\n--- Crawling NeurIPS ---")
    try:
        neurips_args = ["--output", str(paths["research_data"] / "neurips")]
        run_script(str(BASE_DIR / "crawl_neurips.py"), neurips_args,
                   env_extra=env_extra)
    except RuntimeError as e:
        print(f"Warning: NeurIPS crawl failed: {e}")


def build_training_data(paths: dict):
    """Stage 2: Parse reviews into train/test splits."""
    print_header("Stage 2: Building Judge Training Data")

    paths["data"].mkdir(parents=True, exist_ok=True)

    env_extra = {"IDEAFORGE_RESOURCES_DIR": str(paths["resources_dir"])}

    print("Parsing crawled reviews into train/test JSONL...")
    run_script(
        str(JUDGE_DIR / "data_pipeline.py"),
        cwd=str(JUDGE_DIR),
        env_extra=env_extra,
    )

    # Verify
    train_path = paths["data"] / "train.jsonl"
    test_path = paths["data"] / "test.jsonl"
    if train_path.exists() and test_path.exists():
        train_count = sum(1 for _ in open(train_path))
        test_count = sum(1 for _ in open(test_path))
        print(f"Created train.jsonl ({train_count} reviews) and test.jsonl ({test_count} reviews)")
    else:
        print("Warning: Training data files not found after pipeline run")


def build_embeddings(paths: dict):
    """Stage 3: Build FAISS embedding index."""
    print_header("Stage 3: Building FAISS Embedding Index")

    paths["embeddings"].mkdir(parents=True, exist_ok=True)

    env_extra = {"IDEAFORGE_RESOURCES_DIR": str(paths["resources_dir"])}

    print("Building embeddings with all-MiniLM-L6-v2 (downloads ~80MB model on first run)...")
    run_script(
        str(JUDGE_DIR / "embedding_index.py"),
        cwd=str(JUDGE_DIR),
        env_extra=env_extra,
    )

    # Verify
    faiss_path = paths["embeddings"] / "paper_embeddings.faiss"
    if faiss_path.exists():
        size_mb = faiss_path.stat().st_size / (1024 * 1024)
        print(f"Created FAISS index: {size_mb:.1f} MB")
    else:
        print("Warning: FAISS index not found after build")


def generate_skills(paths: dict):
    """Stage 3b: Generate skill files if not already present."""
    index_path = paths["skills"] / "index.json"
    if index_path.exists():
        with open(index_path) as f:
            skills = json.load(f)
        print(f"Skill library already exists ({len(skills)} skills)")
        return

    # Also check the default judge_training/skills location (ships with repo)
    default_skills = JUDGE_DIR / "skills" / "index.json"
    if default_skills.exists() and not index_path.exists():
        # Copy pre-built skills to resources dir
        print("Copying pre-built skill library to resources directory...")
        skills_src = JUDGE_DIR / "skills"
        skills_dst = paths["skills"]
        if skills_src != skills_dst:
            shutil.copytree(str(skills_src), str(skills_dst), dirs_exist_ok=True)
        with open(index_path) as f:
            skills = json.load(f)
        print(f"Copied skill library ({len(skills)} skills)")
        return

    print_header("Stage 3b: Generating Skill Library")
    env_extra = {"IDEAFORGE_RESOURCES_DIR": str(paths["resources_dir"])}
    run_script(
        str(JUDGE_DIR / "generate_skills.py"),
        cwd=str(JUDGE_DIR),
        env_extra=env_extra,
    )


def create_synthetic_test_data(paths: dict):
    """Create a handful of synthetic review records for pipeline testing.

    Provides data without any network access, verifying that the data pipeline,
    embedding index, and skill/prompt copying all work.
    """
    print_header("Test Mode: Creating Synthetic Test Data")

    paths["data"].mkdir(parents=True, exist_ok=True)
    train_path = paths["data"] / "train.jsonl"
    test_path = paths["data"] / "test.jsonl"

    synthetic_papers = [
        {
            "forum_id": f"test_{i}",
            "title": title,
            "abstract": abstract,
            "venue": "ICLR 2025",
            "decision": decision,
            "avg_score": score,
            "scores": [score, score + 0.5, score - 0.5],
            "keywords": keywords,
            "reviews": [
                {
                    "rating": score,
                    "confidence": 4,
                    "strengths": "Well-written paper with clear contributions.",
                    "weaknesses": "Limited evaluation on larger benchmarks.",
                    "questions": "How does this scale?",
                }
            ],
        }
        for i, (title, abstract, decision, score, keywords) in enumerate([
            (
                "Attention Is All You Need: A Retrospective",
                "We revisit the transformer architecture five years later and analyze which design choices mattered most for downstream performance across modalities.",
                "Accept (Oral)", 8.5,
                ["transformers", "attention", "architecture"],
            ),
            (
                "Efficient KV-Cache Compression via Learned Quantization",
                "We propose a training-free method to compress key-value caches in large language models using adaptive quantization, reducing memory by 4x with minimal quality loss.",
                "Accept (Poster)", 6.5,
                ["quantization", "inference", "efficiency"],
            ),
            (
                "Physics-Aware Video Generation Through Simulation Conditioning",
                "We condition video diffusion models on physics simulation trajectories to generate physically plausible videos of rigid-body interactions.",
                "Reject", 4.0,
                ["video generation", "physics", "diffusion"],
            ),
            (
                "Scaling Laws for Sparse Mixture-of-Experts Models",
                "We derive scaling laws for MoE architectures and show that expert count scales sublinearly with compute budget for optimal performance.",
                "Accept (Spotlight)", 7.5,
                ["scaling laws", "mixture of experts", "efficiency"],
            ),
            (
                "Benchmarking ML Compiler Portability Across Hardware",
                "We present the first systematic benchmark measuring how well ML compilers generalize across GPU, TPU, and custom accelerator targets.",
                "Accept (Poster)", 7.0,
                ["compilers", "benchmarks", "hardware"],
            ),
        ])
    ]

    # Write 4 to train, 1 to test
    with open(train_path, "w", encoding="utf-8") as f:
        for paper in synthetic_papers[:4]:
            f.write(json.dumps(paper) + "\n")

    with open(test_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(synthetic_papers[4]) + "\n")

    print(f"  Created {train_path} (4 synthetic papers)")
    print(f"  Created {test_path} (1 synthetic paper)")


def copy_judge_prompt(paths: dict):
    """Copy the pre-trained judge prompt to resources if it exists."""
    src = JUDGE_DIR / "output" / "best_judge_prompt.md"
    dst_dir = paths["output"]
    dst = dst_dir / "best_judge_prompt.md"
    if src.exists() and not dst.exists():
        dst_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src), str(dst))
        print(f"Copied pre-trained judge prompt to {dst}")
    # Also copy stage1 prompt if present
    s1_src = JUDGE_DIR / "output" / "stage1_best_prompt.md"
    s1_dst = dst_dir / "stage1_best_prompt.md"
    if s1_src.exists() and not s1_dst.exists():
        shutil.copy2(str(s1_src), str(s1_dst))


def verify_setup(paths: dict) -> dict:
    """Check that everything is ready for the idea refiner."""
    print_header("Verification")

    checks = {}

    # Judge prompt (check resources dir first, then default location)
    prompt_path = paths["output"] / "best_judge_prompt.md"
    default_prompt = JUDGE_DIR / "output" / "best_judge_prompt.md"
    checks["judge_prompt"] = prompt_path.exists() or default_prompt.exists()
    found_at = prompt_path if prompt_path.exists() else default_prompt
    print(f"  Judge prompt:      {'OK' if checks['judge_prompt'] else 'MISSING'} ({found_at})")

    # Skills
    index_path = paths["skills"] / "index.json"
    default_index = JUDGE_DIR / "skills" / "index.json"
    checks["skills"] = index_path.exists() or default_index.exists()
    if checks["skills"]:
        found_at = index_path if index_path.exists() else default_index
        with open(found_at) as f:
            n_skills = len(json.load(f))
        print(f"  Skill library:     OK ({n_skills} skills)")
    else:
        print(f"  Skill library:     MISSING")

    # FAISS index
    faiss_path = paths["embeddings"] / "paper_embeddings.faiss"
    default_faiss = JUDGE_DIR / "embeddings" / "paper_embeddings.faiss"
    checks["faiss"] = faiss_path.exists() or default_faiss.exists()
    print(f"  FAISS index:       {'OK' if checks['faiss'] else 'MISSING (run setup to build)'}")

    # Training data
    train_path = paths["data"] / "train.jsonl"
    default_train = JUDGE_DIR / "data" / "train.jsonl"
    checks["training_data"] = train_path.exists() or default_train.exists()
    print(f"  Training data:     {'OK' if checks['training_data'] else 'MISSING (run setup to build)'}")

    # Claude CLI
    checks["claude_cli"] = check_claude_cli()
    print(f"  Claude Code CLI:   {'OK' if checks['claude_cli'] else 'MISSING — install from https://docs.anthropic.com/en/docs/claude-code'}")

    # Resources dir
    print(f"\n  Resources dir:     {paths['resources_dir']}")

    # Summary
    ready = checks["judge_prompt"] and checks["skills"] and checks["claude_cli"]
    full_ready = ready and checks["faiss"] and checks["training_data"]

    print()
    if full_ready:
        print("  ALL CHECKS PASSED — ready to run the adversarial idea refiner!")
        print()
        print("  Example:")
        print('    python idea_refiner/adversarial_refiner.py \\')
        print('      --from-scratch \\')
        print('      --domain "your research domain" \\')
        print('      --target-venues "ICML,NeurIPS,ICLR" \\')
        print('      --rounds 40 \\')
        print('      --use-trained-judge \\')
        print('      --min-critics 2')
    elif ready:
        print("  BASIC CHECKS PASSED — can run the refiner without FAISS retrieval.")
        print("  For full judge accuracy, build the FAISS index by running:")
        print("    python setup_pipeline.py")
    else:
        print("  SETUP INCOMPLETE — see missing items above.")

    return checks


def main():
    parser = argparse.ArgumentParser(
        description="IdeaForge: One-script setup for the full pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  --test   No crawling. Uses synthetic data to verify the downstream pipeline
           (data parsing, embeddings, skills, judge prompt) works end-to-end.

  (default) Crawls ~100 representative papers from ICLR (balanced across
           accepted/rejected, multiple years) with conservative QPS.
           Enough to build a working FAISS index and verify the full pipeline.

  --full   Crawls ALL papers from ICLR/ICML/NeurIPS (~50K+). Takes 2-3 hours.
           Use at your own risk — high API volume.
""",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Test mode: no crawling, synthetic data only — verifies downstream pipeline",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Full mode: crawl ALL papers (~50K+) — use at your own risk",
    )
    parser.add_argument(
        "--skip-crawl",
        action="store_true",
        help="Skip paper crawling; only build embeddings from existing data",
    )
    parser.add_argument(
        "--years",
        nargs="+",
        type=int,
        default=[2024, 2025],
        help="Which years to crawl (default: 2024 2025)",
    )
    parser.add_argument(
        "--resources-dir",
        type=str,
        default=str(DEFAULT_RESOURCES_DIR),
        help=f"Directory for all pipeline outputs (default: {DEFAULT_RESOURCES_DIR})",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Just verify setup status, don't build anything",
    )
    args = parser.parse_args()

    resources_dir = Path(args.resources_dir).resolve()
    paths = get_resource_paths(resources_dir)

    # Set the env var so child scripts can find resources
    os.environ["IDEAFORGE_RESOURCES_DIR"] = str(resources_dir)

    # Determine mode
    if args.test:
        mode = "test"
    elif args.full:
        mode = "full"
    else:
        mode = "normal"

    mode_labels = {
        "test": "TEST MODE — synthetic data, no crawling",
        "normal": "NORMAL MODE — ~100 representative papers",
        "full": "FULL MODE — all papers (use at your own risk)",
    }

    print_header(f"IdeaForge Setup Pipeline ({mode_labels[mode]})")
    print(f"  All outputs go to: {resources_dir}\n")

    # Check only
    if args.check:
        verify_setup(paths)
        return

    # Check dependencies
    missing = check_dependencies()
    if missing:
        print(f"Missing packages: {', '.join(missing)}")
        print(f"Install with: pip install {' '.join(missing)}")
        sys.exit(1)

    # Load OpenReview credentials (optional — public papers work without auth)
    username, password = get_openreview_credentials()

    # Create resources directory
    resources_dir.mkdir(parents=True, exist_ok=True)

    if mode == "test":
        # ---- TEST MODE: no crawling, synthetic data only ----
        total_steps = 4
        step = 0

        step += 1
        print_step(step, total_steps, "Creating synthetic test data...")
        create_synthetic_test_data(paths)

        step += 1
        print_step(step, total_steps, "Building FAISS embedding index...")
        try:
            build_embeddings(paths)
        except Exception as e:
            print(f"  Embeddings failed (expected with tiny data): {e}")

        step += 1
        print_step(step, total_steps, "Setting up skill library + judge prompt...")
        generate_skills(paths)
        copy_judge_prompt(paths)

        step += 1
        print_step(step, total_steps, "Verifying setup...")
        verify_setup(paths)

        print("\n  TEST MODE COMPLETE — downstream pipeline verified!")
        print(f"  Test outputs are in: {resources_dir}")
        print("  Run without --test for real data setup.")

    elif mode == "normal":
        # ---- NORMAL MODE: representative sample ----
        total_steps = 4 if args.skip_crawl else 5
        step = 0

        if not args.skip_crawl:
            step += 1
            print_step(step, total_steps, "Crawling representative papers...")
            try:
                crawl_representative_papers(paths, username=username,
                                            password=password)
            except Exception as e:
                print(f"  Crawl failed: {e}")
                print("  Falling back to synthetic data...")
                create_synthetic_test_data(paths)

        # Build training data from whatever we crawled
        step += 1
        print_step(step, total_steps, "Building judge training data...")
        try:
            build_training_data(paths)
        except Exception as e:
            print(f"  Data pipeline failed: {e}")

        # Check if we have data; fall back to synthetic if not
        train_path = paths["data"] / "train.jsonl"
        if not train_path.exists() or train_path.stat().st_size == 0:
            print("  No training data produced — using synthetic fallback...")
            create_synthetic_test_data(paths)

        step += 1
        print_step(step, total_steps, "Building FAISS embedding index...")
        data_path = paths["data"] / "train.jsonl"
        if data_path.exists() and data_path.stat().st_size > 0:
            try:
                build_embeddings(paths)
            except Exception as e:
                print(f"  Embeddings failed: {e}")
        else:
            print("  Skipped — no training data.")

        step += 1
        print_step(step, total_steps, "Setting up skill library + judge prompt...")
        generate_skills(paths)
        copy_judge_prompt(paths)

        step += 1
        print_step(step, total_steps, "Verifying setup...")
        verify_setup(paths)

    else:
        # ---- FULL MODE: crawl everything ----
        total_steps = 5
        step = 0

        if not args.skip_crawl:
            step += 1
            print_step(step, total_steps, "Crawling ALL papers...")
            crawl_all_papers(args.years, paths, username=username,
                             password=password)

        step += 1
        print_step(step, total_steps, "Building judge training data...")
        build_training_data(paths)

        step += 1
        print_step(step, total_steps, "Building FAISS embedding index...")
        data_path = paths["data"] / "train.jsonl"
        if data_path.exists():
            build_embeddings(paths)
        else:
            print("  Skipped — no training data. Run without --skip-crawl first.")

        step += 1
        print_step(step, total_steps, "Setting up skill library + judge prompt...")
        generate_skills(paths)
        copy_judge_prompt(paths)

        step += 1
        print_step(step, total_steps, "Verifying setup...")
        verify_setup(paths)


if __name__ == "__main__":
    main()
