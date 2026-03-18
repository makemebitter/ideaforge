#!/usr/bin/env python3
"""
IdeaForge Setup Pipeline

One-script setup that crawls papers, builds training data, creates the FAISS
embedding index, and verifies the pre-trained judge — getting you to the point
where you can immediately run the adversarial idea refiner.

All outputs go to a `resources/` folder (configurable via --resources-dir) so
the setup does not interfere with existing local data.

Usage:
    python setup_pipeline.py                    # Full setup (crawl + build)
    python setup_pipeline.py --skip-crawl       # Skip crawling, just build from existing data
    python setup_pipeline.py --test             # Tiny-scale test to verify pipeline works
    python setup_pipeline.py --check            # Just verify everything is ready

Prerequisites:
    - Python 3.10+
    - pip install -r requirements.txt
    - pip install sentence-transformers faiss-cpu numpy
    - OpenReview account (set in config.py or OPENREVIEW_EMAIL / OPENREVIEW_PASSWORD env vars)
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

# Default resources directory — all pipeline outputs go here
DEFAULT_RESOURCES_DIR = BASE_DIR / "resources"


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


def check_config() -> tuple[str, str]:
    """Check for OpenReview credentials in config.py or env vars."""
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


def crawl_papers(years: list[int], email: str, password: str,
                 paths: dict, test_mode: bool = False):
    """Stage 1: Crawl papers and reviews from OpenReview."""
    print_header("Stage 1: Crawling Papers + Reviews")

    env_extra = {"IDEAFORGE_RESOURCES_DIR": str(paths["resources_dir"])}

    if test_mode:
        print("  TEST MODE: crawling only ICLR for 1 year")
        years = [years[0]]

    for year in years:
        print(f"\n--- Crawling ICLR {year} ---")
        args = ["--year", str(year)]
        if email and password:
            args += ["--email", email, "--password", password]
        args += ["--output", str(paths["research_data"] / "iclr")]
        try:
            run_script(
                str(BASE_DIR / "data_pipeline" / "openreview_crawler.py"),
                args, env_extra=env_extra,
            )
        except RuntimeError as e:
            print(f"Warning: ICLR {year} crawl failed: {e}")

    if test_mode:
        print("  TEST MODE: skipping ICML/NeurIPS crawl")
        return

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
        "--test",
        action="store_true",
        help="Tiny-scale test mode: crawl ~5 papers per venue to verify pipeline works end-to-end",
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

    if args.test:
        print_header("IdeaForge Setup Pipeline (TEST MODE)")
        print("  Running tiny-scale test to verify pipeline works end-to-end.")
        print(f"  All outputs go to: {resources_dir}\n")
    else:
        print_header("IdeaForge Setup Pipeline")

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

    # Create resources directory
    resources_dir.mkdir(parents=True, exist_ok=True)

    # Get credentials from config.py or env vars
    email, password = check_config()

    total_steps = 3 if args.skip_crawl else 5
    step = 0

    if not args.skip_crawl:
        if not email and not password:
            print("Warning: No OpenReview credentials found.")
            print("Set via config.py or OPENREVIEW_EMAIL / OPENREVIEW_PASSWORD env vars")
            print("Some crawlers may still work without auth.\n")

        # Stage 1: Crawl
        step += 1
        print_step(step, total_steps, "Crawling papers and reviews...")
        crawl_papers(args.years, email, password, paths, test_mode=args.test)

        # Stage 2: Build training data
        step += 1
        print_step(step, total_steps, "Building judge training data...")
        build_training_data(paths)

    # Stage 3: Build embeddings
    step += 1
    print_step(step, total_steps, "Building FAISS embedding index...")
    data_path = paths["data"] / "train.jsonl"
    if data_path.exists():
        build_embeddings(paths)
    else:
        print("  Skipped — no training data found. Run without --skip-crawl first.")

    # Stage 4: Copy/generate skills and judge prompt
    step += 1
    print_step(step, total_steps, "Setting up skill library + judge prompt...")
    generate_skills(paths)
    copy_judge_prompt(paths)

    # Verify
    step += 1
    print_step(step, total_steps, "Verifying setup...")
    verify_setup(paths)

    if args.test:
        print("\n  TEST MODE COMPLETE — pipeline works end-to-end!")
        print(f"  Test outputs are in: {resources_dir}")
        print("  Run without --test for full setup.")


if __name__ == "__main__":
    main()
