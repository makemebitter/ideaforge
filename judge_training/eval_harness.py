"""
Phase 4a: Evaluation Harness

For each paper during GEPA training:
  1. Retrieve similar papers from embedding index (top 5)
  2. Select & load relevant skill files based on topic/keywords
  3. Assemble context: core prompt + skills + retrieved papers + paper to evaluate
  4. Run judge (LLM predicts rating 1-10, soundness, contribution, accept/reject)
  5. Score: compare predictions to actual review scores

This module is called by optimize.py during GEPA training.
Can also be run standalone for testing.

Usage:
    python eval_harness.py --prompt seed_prompt.md --sample 20  # Test on 20 papers
    python eval_harness.py --prompt seed_prompt.md --full        # Full test set
"""

import json
import re
import argparse
import functools
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

print = functools.partial(print, flush=True)  # type: ignore

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
SKILLS_DIR = BASE_DIR / "skills"
LOG_DIR = BASE_DIR / "output" / "logs"

logger = logging.getLogger("eval_harness")


def _setup_file_logger(label: str = "eval") -> Path:
    """Set up a file logger for this evaluation run."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = LOG_DIR / f"{ts}_{label}.log"

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    return log_file

# Lazy imports for optional heavy deps
_embedding_module = None


def _get_embedding_module():
    global _embedding_module
    if _embedding_module is None:
        from . import embedding_index as _ei
        _embedding_module = _ei
    return _embedding_module


# ---------------------------------------------------------------------------
# Skill loading
# ---------------------------------------------------------------------------

def load_skill_index() -> dict:
    index_path = SKILLS_DIR / "index.json"
    if not index_path.exists():
        return {"topics": {}, "dimensions": {}, "calibration": {}, "keyword_to_topic": {}}
    with open(index_path, "r", encoding="utf-8") as f:
        return json.load(f)


def select_skills(paper: dict, skill_index: dict, max_skills: int = 3) -> list[str]:
    """Select the most relevant skill file paths for a paper."""
    selected = []

    # Match by primary_area and keywords
    kw_to_topic = skill_index.get("keyword_to_topic", {})
    searchable = " ".join([
        paper.get("title", ""),
        paper.get("primary_area", ""),
        " ".join(paper.get("keywords", [])),
    ]).lower()

    matched_topics = set()
    for kw, topic in kw_to_topic.items():
        if kw in searchable:
            matched_topics.add(topic)

    topic_paths = skill_index.get("topics", {})
    for topic in list(matched_topics)[:2]:
        if topic in topic_paths:
            full_path = BASE_DIR / topic_paths[topic]
            if full_path.exists():
                selected.append(str(full_path))

    # Add a calibration skill based on rating if we're looking for calibration context
    # (during eval, we don't know the true rating, but we can add general calibration)
    calib_paths = skill_index.get("calibration", {})
    for tier in ["score_4_5", "score_6_7"]:
        if tier in calib_paths and len(selected) < max_skills:
            full_path = BASE_DIR / calib_paths[tier]
            if full_path.exists():
                selected.append(str(full_path))
                break

    return selected[:max_skills]


def load_skill_contents(skill_paths: list[str]) -> str:
    """Load and concatenate skill file contents."""
    parts = []
    for path in skill_paths:
        p = Path(path)
        if p.exists():
            content = p.read_text(encoding="utf-8")
            parts.append(f"--- SKILL FILE: {p.name} ---\n{content}\n--- END SKILL ---\n")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Retrieval
# ---------------------------------------------------------------------------

def retrieve_similar_papers(paper: dict, top_k: int = 5) -> str:
    """Retrieve similar papers from the embedding index."""
    try:
        import embedding_index
        query = f"{paper.get('title', '')}. {paper.get('abstract', '')[:500]}"
        results = embedding_index.query_index(query, top_k=top_k)
        # Filter out the paper itself
        results = [r for r in results if r.get("paper_id") != paper.get("paper_id")][:top_k]
        return embedding_index.format_retrieval_context(results)
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# Judge invocation
# ---------------------------------------------------------------------------

SEED_JUDGE_PROMPT = """You are a calibrated AI conference reviewer. Given a paper's title, abstract, and keywords, predict what score (1-10) it would receive at a top AI conference (ICLR, NeurIPS, ICML).

You have access to:
1. Skill files with domain-specific evaluation knowledge (loaded below)
2. Similar published papers with their actual review scores (retrieved below)

Use these to ground your evaluation in real conference standards.

## Your Evaluation

Evaluate the paper on these dimensions:
- **Novelty** (1-4): How original is the contribution?
- **Soundness** (1-4): Are the methods technically correct?
- **Significance** (1-4): How impactful is the contribution?
- **Clarity** (1-4): How well-written and clear?

Then give an overall rating (1-10) and accept/reject recommendation.

## Output Format (STRICTLY follow this JSON format)

```json
{
    "rating": <float 1-10>,
    "soundness": <int 1-4>,
    "contribution": <int 1-4>,
    "presentation": <int 1-4>,
    "decision": "<Accept|Borderline|Reject>",
    "confidence": <int 1-5>,
    "reasoning": "<2-3 sentence justification>"
}
```
"""


def build_redacted_review_content(paper: dict, max_reviews: int = 3,
                                   max_chars_per_section: int = 800) -> str:
    """Build redacted review content — summaries + strengths + weaknesses, no scores."""
    reviews = paper.get("review_texts", [])
    if not reviews:
        return ""

    parts = ["## Expert Reviewer Assessments (scores redacted)\n"]
    for i, rev in enumerate(reviews[:max_reviews]):
        parts.append(f"### Reviewer {i + 1}")
        summary = str(rev.get("summary", "")).strip()
        if summary:
            parts.append(f"**Summary**: {summary[:max_chars_per_section]}")
        strengths = str(rev.get("strengths", "")).strip()
        if strengths:
            parts.append(f"**Strengths**: {strengths[:max_chars_per_section]}")
        weaknesses = str(rev.get("weaknesses", "")).strip()
        if weaknesses:
            parts.append(f"**Weaknesses**: {weaknesses[:max_chars_per_section]}")
        questions = str(rev.get("questions", "")).strip()
        if questions:
            parts.append(f"**Questions**: {questions[:max_chars_per_section]}")
        parts.append("")

    return "\n".join(parts)


def build_judge_prompt(paper: dict, core_prompt: str,
                       skill_content: str = "", retrieval_context: str = "",
                       include_reviews: bool = True) -> str:
    """Assemble the full judge prompt with all context layers."""
    parts = [core_prompt]

    if skill_content:
        parts.append("\n## Loaded Skill Files\n")
        parts.append(skill_content)

    if retrieval_context:
        parts.append("\n" + retrieval_context)

    parts.append("\n## Paper to Evaluate\n")
    parts.append(f"**Title**: {paper.get('title', 'Unknown')}")
    abstract = paper.get("abstract", "")
    if abstract:
        parts.append(f"**Abstract**: {abstract}")
    keywords = paper.get("keywords", [])
    if keywords:
        parts.append(f"**Keywords**: {', '.join(keywords)}")
    primary_area = paper.get("primary_area", "")
    if primary_area:
        parts.append(f"**Primary Area**: {primary_area}")

    if include_reviews:
        review_content = build_redacted_review_content(paper)
        if review_content:
            parts.append("\n" + review_content)

    parts.append("\n## Your Evaluation\n")
    parts.append("Respond with ONLY the JSON object. No other text.")

    return "\n\n".join(parts)


def parse_judge_output(output: str) -> Optional[dict]:
    """Parse the judge's JSON output."""
    json_match = re.search(r'\{[^{}]*"rating"[^{}]*\}', output, re.DOTALL)
    if not json_match:
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', output, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            return None
    else:
        json_str = json_match.group()

    try:
        parsed = json.loads(json_str)
        rating = parsed.get("rating")
        if rating is not None:
            parsed["rating"] = float(rating)
        return parsed
    except (json.JSONDecodeError, ValueError):
        return None


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_prediction(predicted: dict, actual: dict) -> dict:
    """Score a single prediction against actual review data."""
    pred_rating = predicted.get("rating", 5.0)
    actual_rating = actual.get("avg_rating", 5.0)

    rating_error = abs(pred_rating - actual_rating)
    rating_score = max(0.0, 1.0 - rating_error / 9.0)

    # Decision accuracy
    pred_decision = str(predicted.get("decision", "")).lower()
    actual_decision = str(actual.get("decision", "")).lower()
    pred_accept = "accept" in pred_decision
    actual_accept = "accept" in actual_decision

    decision_correct = pred_accept == actual_accept if actual_decision else None

    # Sub-dimension scores
    soundness_error = None
    if predicted.get("soundness") and actual.get("avg_soundness"):
        soundness_error = abs(float(predicted["soundness"]) - float(actual["avg_soundness"]))

    contribution_error = None
    if predicted.get("contribution") and actual.get("avg_contribution"):
        contribution_error = abs(float(predicted["contribution"]) - float(actual["avg_contribution"]))

    return {
        "pred_rating": pred_rating,
        "actual_rating": actual_rating,
        "rating_error": round(rating_error, 2),
        "rating_score": round(rating_score, 4),
        "decision_correct": decision_correct,
        "soundness_error": round(soundness_error, 2) if soundness_error is not None else None,
        "contribution_error": round(contribution_error, 2) if contribution_error is not None else None,
    }


def aggregate_scores(results: list[dict]) -> dict:
    """Aggregate scoring results across papers."""
    n = len(results)
    if n == 0:
        return {"n": 0, "rating_mae": 0, "rating_score": 0}

    rating_errors = [r["rating_error"] for r in results]
    rating_scores = [r["rating_score"] for r in results]
    decision_results = [r["decision_correct"] for r in results if r["decision_correct"] is not None]
    soundness_errors = [r["soundness_error"] for r in results if r["soundness_error"] is not None]

    mae = sum(rating_errors) / n
    avg_score = sum(rating_scores) / n
    decision_acc = sum(decision_results) / len(decision_results) if decision_results else None

    # Spearman rank correlation
    pred_ratings = [r["pred_rating"] for r in results]
    actual_ratings = [r["actual_rating"] for r in results]
    spearman = _spearman(pred_ratings, actual_ratings)

    return {
        "n": n,
        "rating_mae": round(mae, 3),
        "rating_score": round(avg_score, 4),
        "decision_accuracy": round(decision_acc, 3) if decision_acc is not None else None,
        "spearman_correlation": round(spearman, 3) if spearman is not None else None,
        "soundness_mae": round(sum(soundness_errors) / len(soundness_errors), 3) if soundness_errors else None,
    }


def _spearman(x: list[float], y: list[float]) -> Optional[float]:
    """Simple Spearman rank correlation."""
    n = len(x)
    if n < 3:
        return None

    def _rank(vals):
        sorted_idx = sorted(range(n), key=lambda i: vals[i])
        ranks = [0.0] * n
        for rank, idx in enumerate(sorted_idx):
            ranks[idx] = float(rank)
        return ranks

    rx = _rank(x)
    ry = _rank(y)
    d_sq = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - (6 * d_sq) / (n * (n * n - 1))


# ---------------------------------------------------------------------------
# Diagnostic ASI (per-case feedback for GEPA)
# ---------------------------------------------------------------------------

def build_diagnostic(paper: dict, predicted: dict, score_result: dict) -> str:
    """Build diagnostic string for GEPA's ASI (Adaptive Strategy Improvement)."""
    lines = [
        f"Paper: {paper.get('title', 'Unknown')[:80]}",
        f"Predicted: {score_result['pred_rating']:.1f} | Actual: {score_result['actual_rating']:.1f} | Error: {score_result['rating_error']:.1f}",
    ]

    if score_result["rating_error"] > 2:
        lines.append("** LARGE ERROR **")
        if score_result["pred_rating"] > score_result["actual_rating"]:
            lines.append("Judge was TOO GENEROUS. Real reviewers were harsher.")
        else:
            lines.append("Judge was TOO HARSH. Real reviewers were more positive.")

    # Include actual reviewer quotes for calibration
    if paper.get("review_texts"):
        rev = paper["review_texts"][0]
        if rev.get("weaknesses"):
            lines.append(f"Real reviewer weakness: {rev['weaknesses'][:200]}")
        if rev.get("strengths"):
            lines.append(f"Real reviewer strength: {rev['strengths'][:200]}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Full evaluation pipeline
# ---------------------------------------------------------------------------

def evaluate_prompt(
    core_prompt: str,
    papers: list[dict],
    use_skills: bool = True,
    use_retrieval: bool = True,
    include_reviews: bool = True,
    model: str = "haiku",
    verbose: bool = False,
    log_label: str = "eval",
) -> tuple[float, dict]:
    """
    Evaluate a judge prompt on a set of papers.

    Returns (score, details) where score is the primary metric (0-1, higher=better)
    and details contains per-paper results and aggregate metrics.
    """
    from claude_utils import run_claude_oneshot

    log_file = _setup_file_logger(log_label)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    detail_log_path = LOG_DIR / f"{ts}_{log_label}_details.jsonl"

    run_start = time.time()
    logger.info("Starting evaluation: %d papers, model=%s, skills=%s, retrieval=%s, reviews=%s",
                len(papers), model, use_skills, use_retrieval, include_reviews)
    logger.info("Core prompt length: %d chars", len(core_prompt))
    logger.info("Detail log: %s", detail_log_path)

    skill_index = load_skill_index() if use_skills else {}
    results = []
    diagnostics = []
    parse_failures = 0

    for i, paper in enumerate(papers):
        t0 = time.time()
        paper_title = paper.get("title", "Unknown")[:80]

        skill_content = ""
        skill_files_used = []
        if use_skills and skill_index:
            skill_paths = select_skills(paper, skill_index)
            skill_content = load_skill_contents(skill_paths)
            skill_files_used = skill_paths

        retrieval_context = ""
        if use_retrieval:
            retrieval_context = retrieve_similar_papers(paper, top_k=5)

        prompt = build_judge_prompt(paper, core_prompt, skill_content, retrieval_context,
                                    include_reviews=include_reviews)

        output = run_claude_oneshot(
            prompt, timeout=120, model=model,
            exp_dir=BASE_DIR / "output" / "_eval_runs",
            label=f"eval_{i}",
        )

        elapsed = time.time() - t0
        predicted = parse_judge_output(output)

        if predicted is None:
            parse_failures += 1
            logger.warning("[%d/%d] PARSE FAILED (%.1fs): %s | output: %s",
                           i + 1, len(papers), elapsed, paper_title, output[:200])
            if verbose:
                print(f"  [{i+1}/{len(papers)}] PARSE FAILED: {paper_title[:50]}")

            with open(detail_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps({
                    "idx": i, "paper_id": paper.get("paper_id", ""),
                    "paper_title": paper_title, "status": "parse_failed",
                    "elapsed_s": round(elapsed, 1),
                    "raw_output_snippet": output[:500],
                }, ensure_ascii=False, default=str) + "\n")
            continue

        result = score_prediction(predicted, paper)
        results.append(result)

        diagnostic = build_diagnostic(paper, predicted, result)
        diagnostics.append(diagnostic)

        logger.info("[%d/%d] pred=%.1f actual=%.1f err=%.1f (%.1fs) %s",
                    i + 1, len(papers), result["pred_rating"], result["actual_rating"],
                    result["rating_error"], elapsed, paper_title)

        with open(detail_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps({
                "idx": i, "paper_id": paper.get("paper_id", ""),
                "paper_title": paper_title, "status": "ok",
                "pred_rating": result["pred_rating"],
                "actual_rating": result["actual_rating"],
                "rating_error": result["rating_error"],
                "rating_score": result["rating_score"],
                "decision_correct": result.get("decision_correct"),
                "predicted_full": predicted,
                "elapsed_s": round(elapsed, 1),
                "skill_files": skill_files_used,
            }, ensure_ascii=False, default=str) + "\n")

        if verbose:
            err = result["rating_error"]
            marker = "!!" if err > 2 else "  "
            print(f"  [{i+1}/{len(papers)}] {marker} pred={result['pred_rating']:.1f} "
                  f"actual={result['actual_rating']:.1f} err={err:.1f} | "
                  f"{paper_title[:50]}")

    run_elapsed = time.time() - run_start
    agg = aggregate_scores(results)
    primary_score = agg["rating_score"]

    logger.info("Evaluation complete: %.1f min, %d scored, %d parse failures",
                run_elapsed / 60, len(results), parse_failures)
    logger.info("Aggregate: MAE=%.3f, score=%.4f, spearman=%s, decision_acc=%s",
                agg["rating_mae"], agg["rating_score"],
                agg.get("spearman_correlation", "N/A"),
                agg.get("decision_accuracy", "N/A"))

    summary = {
        "timestamp": datetime.now().isoformat(),
        "wall_time_min": round(run_elapsed / 60, 2),
        "model": model,
        "use_skills": use_skills,
        "use_retrieval": use_retrieval,
        "total_papers": len(papers),
        "scored": len(results),
        "parse_failures": parse_failures,
        "aggregate": agg,
        "prompt_len": len(core_prompt),
    }
    summary_path = LOG_DIR / f"{ts}_{log_label}_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    details = {
        "aggregate": agg,
        "per_paper": results,
        "diagnostics": "\n---\n".join(diagnostics),
        "parse_failures": parse_failures,
        "log_file": str(log_file),
        "detail_log": str(detail_log_path),
        "summary_file": str(summary_path),
    }

    return primary_score, details


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Test judge evaluation harness")
    parser.add_argument("--prompt", type=str, default=None,
                        help="Path to judge prompt file (uses seed prompt if not given)")
    parser.add_argument("--sample", type=int, default=10,
                        help="Number of papers to evaluate (default: 10)")
    parser.add_argument("--full", action="store_true",
                        help="Evaluate on full test set")
    parser.add_argument("--model", type=str, default="opus",
                        help="LLM model for judge (default: opus)")
    parser.add_argument("--no-skills", action="store_true",
                        help="Disable skill loading")
    parser.add_argument("--no-retrieval", action="store_true",
                        help="Disable retrieval")
    parser.add_argument("--no-reviews", action="store_true",
                        help="Disable redacted review content in prompt")
    parser.add_argument("--split", choices=["train", "test"], default="test",
                        help="Which split to evaluate on")
    args = parser.parse_args()

    # Load prompt
    if args.prompt:
        core_prompt = Path(args.prompt).read_text(encoding="utf-8")
    else:
        core_prompt = SEED_JUDGE_PROMPT
        print("Using seed judge prompt (no --prompt specified)\n")

    # Load papers
    split_file = DATA_DIR / f"{args.split}.jsonl"
    papers = []
    with open(split_file, "r", encoding="utf-8") as f:
        for line in f:
            p = json.loads(line)
            if p.get("abstract") and p.get("avg_rating"):
                papers.append(p)

    if not args.full:
        import random
        rng = random.Random(42)
        papers_with_reviews = [p for p in papers if p.get("review_texts")]
        papers = rng.sample(papers_with_reviews, min(args.sample, len(papers_with_reviews)))

    inc_reviews = not args.no_reviews
    print(f"Evaluating on {len(papers)} papers from {args.split} split")
    print(f"Model: {args.model} | Skills: {not args.no_skills} | Retrieval: {not args.no_retrieval} | Reviews: {inc_reviews}\n")

    score, details = evaluate_prompt(
        core_prompt, papers,
        use_skills=not args.no_skills,
        use_retrieval=not args.no_retrieval,
        include_reviews=inc_reviews,
        model=args.model,
        verbose=True,
        log_label=f"standalone_{args.split}",
    )

    agg = details["aggregate"]
    print(f"\n{'='*60}")
    print(f"RESULTS ({agg['n']} papers scored, {details['parse_failures']} parse failures)")
    print(f"{'='*60}")
    print(f"  Primary Score:       {score:.4f} (1 - MAE/9)")
    print(f"  Rating MAE:          {agg['rating_mae']:.3f}")
    print(f"  Decision Accuracy:   {agg.get('decision_accuracy', 'N/A')}")
    print(f"  Spearman Corr:       {agg.get('spearman_correlation', 'N/A')}")
    print(f"  Soundness MAE:       {agg.get('soundness_mae', 'N/A')}")
    print(f"\n  Log file:            {details.get('log_file', 'N/A')}")
    print(f"  Detail log:          {details.get('detail_log', 'N/A')}")
    print(f"  Summary:             {details.get('summary_file', 'N/A')}")


if __name__ == "__main__":
    main()
