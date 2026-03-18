#!/usr/bin/env python3
"""
IdeaForge Setup Pipeline

One-script setup that crawls papers, builds training data, creates the FAISS
embedding index, and verifies the pre-trained judge — getting you to the point
where you can immediately run the adversarial idea refiner.

Usage:
    python setup_pipeline.py                    # Full setup (crawl + build)
    python setup_pipeline.py --skip-crawl       # Skip crawling, just build from existing data
    python setup_pipeline.py --years 2024 2025  # Crawl specific years only
    python setup_pipeline.py --check            # Just verify everything is ready

Prerequisites:
    - Python 3.10+
    - pip install -r requirements.txt
    - pip install sentence-transformers faiss-cpu numpy
    - OpenReview account (set in config.py or pass --email / --password)
    - Claude Code CLI installed and authenticated (for idea refinement)
"""

import argparse
import importlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent
JUDGE_DIR = BASE_DIR / "judge_training"
DATA_DIR = JUDGE_DIR / "data"
EMBED_DIR = JUDGE_DIR / "embeddings"
SKILLS_DIR = JUDGE_DIR / "skills"
RESEARCH_DIR = BASE_DIR / "research_data"


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


def check_config() -> tuple[str, str]:
    """Check for OpenReview credentials."""
    # Try config.py
    config_path = BASE_DIR / "config.py"
    if config_path.exists():
        sys.path.insert(0, str(BASE_DIR))
        try:
            import config
            return getattr(config, "EMAIL", ""), getattr(config, "PASSWORD", "")
        except Exception:
            pass
    # Try environment variables
    email = os.environ.get("OPENREVIEW_EMAIL", "")
    password = os.environ.get("OPENREVIEW_PASSWORD", "")
    return email, password


def check_claude_cli() -> bool:
    """Check if Claude Code CLI is available."""
    return shutil.which("claude") is not None


def run_script(script_path: str, args: list[str] = None, cwd: str = None):
    """Run a Python script as subprocess."""
    cmd = [sys.executable, script_path] + (args or [])
    result = subprocess.run(
        cmd,
        cwd=cwd or str(BASE_DIR),
        capture_output=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Script failed: {script_path} (exit code {result.returncode})")


def crawl_papers(years: list[int], email: str, password: str):
    """Stage 1: Crawl papers and reviews from OpenReview."""
    print_header("Stage 1: Crawling Papers + Reviews")

    for year in years:
        print(f"\n--- Crawling ICLR {year} ---")
        args = ["--year", str(year)]
        if email and password:
            args += ["--email", email, "--password", password]
        try:
            run_script(
                str(BASE_DIR / "data_pipeline" / "openreview_crawler.py"),
                args,
            )
        except RuntimeError as e:
            print(f"Warning: ICLR {year} crawl failed: {e}")

    # ICML
    print(f"\n--- Crawling ICML ---")
    try:
        run_script(str(BASE_DIR / "crawl_icml.py"))
    except RuntimeError as e:
        print(f"Warning: ICML crawl failed: {e}")

    # NeurIPS
    print(f"\n--- Crawling NeurIPS ---")
    try:
        run_script(str(BASE_DIR / "crawl_neurips.py"))
    except RuntimeError as e:
        print(f"Warning: NeurIPS crawl failed: {e}")


def build_training_data():
    """Stage 2: Parse reviews into train/test splits."""
    print_header("Stage 2: Building Judge Training Data")

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Parsing crawled reviews into train/test JSONL...")
    run_script(
        str(JUDGE_DIR / "data_pipeline.py"),
        cwd=str(JUDGE_DIR),
    )

    # Verify
    train_path = DATA_DIR / "train.jsonl"
    test_path = DATA_DIR / "test.jsonl"
    if train_path.exists() and test_path.exists():
        train_count = sum(1 for _ in open(train_path))
        test_count = sum(1 for _ in open(test_path))
        print(f"Created train.jsonl ({train_count} reviews) and test.jsonl ({test_count} reviews)")
    else:
        print("Warning: Training data files not found after pipeline run")


def build_embeddings():
    """Stage 3: Build FAISS embedding index."""
    print_header("Stage 3: Building FAISS Embedding Index")

    EMBED_DIR.mkdir(parents=True, exist_ok=True)

    print("Building embeddings with all-MiniLM-L6-v2 (downloads ~80MB model on first run)...")
    run_script(
        str(JUDGE_DIR / "embedding_index.py"),
        cwd=str(JUDGE_DIR),
    )

    # Verify
    faiss_path = EMBED_DIR / "paper_embeddings.faiss"
    if faiss_path.exists():
        size_mb = faiss_path.stat().st_size / (1024 * 1024)
        print(f"Created FAISS index: {size_mb:.1f} MB")
    else:
        print("Warning: FAISS index not found after build")


def generate_skills():
    """Stage 3b: Generate skill files if not already present."""
    index_path = SKILLS_DIR / "index.json"
    if index_path.exists():
        with open(index_path) as f:
            skills = json.load(f)
        print(f"Skill library already exists ({len(skills)} skills)")
        return

    print_header("Stage 3b: Generating Skill Library")
    run_script(
        str(JUDGE_DIR / "generate_skills.py"),
        cwd=str(JUDGE_DIR),
    )


def verify_setup() -> dict:
    """Check that everything is ready for the idea refiner."""
    print_header("Verification")

    checks = {}

    # Judge prompt
    prompt_path = JUDGE_DIR / "output" / "best_judge_prompt.md"
    checks["judge_prompt"] = prompt_path.exists()
    print(f"  Judge prompt:      {'OK' if checks['judge_prompt'] else 'MISSING'} ({prompt_path})")

    # Skills
    index_path = SKILLS_DIR / "index.json"
    checks["skills"] = index_path.exists()
    if checks["skills"]:
        with open(index_path) as f:
            n_skills = len(json.load(f))
        print(f"  Skill library:     OK ({n_skills} skills)")
    else:
        print(f"  Skill library:     MISSING")

    # FAISS index
    faiss_path = EMBED_DIR / "paper_embeddings.faiss"
    checks["faiss"] = faiss_path.exists()
    print(f"  FAISS index:       {'OK' if checks['faiss'] else 'MISSING (run without --skip-crawl to build)'}")

    # Training data
    train_path = DATA_DIR / "train.jsonl"
    checks["training_data"] = train_path.exists()
    print(f"  Training data:     {'OK' if checks['training_data'] else 'MISSING (run without --skip-crawl to build)'}")

    # Claude CLI
    checks["claude_cli"] = check_claude_cli()
    print(f"  Claude Code CLI:   {'OK' if checks['claude_cli'] else 'MISSING — install from https://docs.anthropic.com/en/docs/claude-code'}")

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
        print("    python setup_pipeline.py  (without --skip-crawl)")
    else:
        print("  SETUP INCOMPLETE — see missing items above.")

    return checks


def main():
    parser = argparse.ArgumentParser(
        description="IdeaForge: One-script setup for the full pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
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
        "--email",
        help="OpenReview email (or set in config.py / OPENREVIEW_EMAIL env var)",
    )
    parser.add_argument(
        "--password",
        help="OpenReview password (or set in config.py / OPENREVIEW_PASSWORD env var)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Just verify setup status, don't build anything",
    )
    args = parser.parse_args()

    print_header("IdeaForge Setup Pipeline")

    # Check only
    if args.check:
        verify_setup()
        return

    # Check dependencies
    missing = check_dependencies()
    if missing:
        print(f"Missing packages: {', '.join(missing)}")
        print(f"Install with: pip install {' '.join(missing)}")
        sys.exit(1)

    # Get credentials
    email = args.email or ""
    password = args.password or ""
    if not email or not password:
        email, password = check_config()

    total_steps = 2 if args.skip_crawl else 4
    step = 0

    if not args.skip_crawl:
        if not email or not password:
            print("Warning: No OpenReview credentials found.")
            print("Set via: --email/--password, config.py, or OPENREVIEW_EMAIL env var")
            print("Some crawlers may still work without auth.\n")

        # Stage 1: Crawl
        step += 1
        print_step(step, total_steps, "Crawling papers and reviews...")
        crawl_papers(args.years, email, password)

        # Stage 2: Build training data
        step += 1
        print_step(step, total_steps, "Building judge training data...")
        build_training_data()

    # Stage 3: Build embeddings
    step += 1
    print_step(step, total_steps, "Building FAISS embedding index...")
    if DATA_DIR.exists() and (DATA_DIR / "train.jsonl").exists():
        build_embeddings()
    else:
        print("  Skipped — no training data found. Run without --skip-crawl first.")

    # Stage 3b: Verify skills
    step += 1
    print_step(step, total_steps, "Checking skill library...")
    generate_skills()

    # Verify
    verify_setup()


if __name__ == "__main__":
    main()
