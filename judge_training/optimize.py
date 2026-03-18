"""
Phase 4b: GEPA Optimization of the Judge Prompt

Uses GEPA's optimize_anything in Generalization mode to evolve the core judge
prompt. The skill files and embedding index are pre-built and fixed; GEPA
optimizes the meta-prompt that instructs the judge HOW to use them.

Usage:
    python optimize.py                            # Run with defaults
    python optimize.py --max-evals 100            # Limit evaluations
    python optimize.py --model haiku              # Use cheaper model for training
    python optimize.py --no-skills --no-retrieval  # Ablation: prompt-only
"""

import json
import random
import argparse
import functools
import time
from datetime import datetime
from pathlib import Path

import gepa
import gepa.optimize_anything as oa
from gepa.optimize_anything import (
    GEPAConfig, EngineConfig, ReflectionConfig, optimize_anything,
)

print = functools.partial(print, flush=True)  # type: ignore

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = OUTPUT_DIR / "logs"

# ---------------------------------------------------------------------------
# Seed prompt — what GEPA starts from and evolves
# ---------------------------------------------------------------------------

SEED_JUDGE_PROMPT = """You are a calibrated AI conference reviewer. Given a paper's title, abstract, and keywords, predict what score (1-10) it would receive at a top AI conference (ICLR, NeurIPS, ICML).

You have access to:
1. Skill files with domain-specific evaluation knowledge (loaded below)
2. Similar published papers with their actual review scores (retrieved below)

Use these to ground your evaluation in real conference standards.

## Evaluation Dimensions
- **Novelty** (1-4): How original is the contribution?
- **Soundness** (1-4): Are the methods technically correct?
- **Significance** (1-4): How impactful is the contribution?
- **Clarity** (1-4): How well-written and clear?

## Scoring Guidelines
- 1-3: Fundamentally flawed, trivial, or already published
- 4-5: Below average — some merit but significant weaknesses
- 6-7: Above average — solid work, acceptable for a good venue
- 8-10: Excellent — novel, well-executed, significant contribution

## Output Format (STRICTLY follow this JSON)

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


# ---------------------------------------------------------------------------
# Evaluator function for GEPA
# ---------------------------------------------------------------------------

_eval_config = {
    "use_skills": True,
    "use_retrieval": True,
    "include_reviews": True,
    "model": "opus",
}


def _make_claude_code_lm(model: str = "sonnet"):
    """Build a GEPA-compatible LLM callable that routes through Claude Code CLI."""
    from claude_utils import run_claude_oneshot

    def _lm(prompt):
        if isinstance(prompt, list):
            parts = []
            for msg in prompt:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if role == "system":
                    parts.append(f"[SYSTEM]\n{content}")
                elif role == "assistant":
                    parts.append(f"[ASSISTANT]\n{content}")
                else:
                    parts.append(content)
            prompt_text = "\n\n".join(parts)
        else:
            prompt_text = prompt

        result = run_claude_oneshot(
            prompt_text, timeout=300, model=model,
            exp_dir=OUTPUT_DIR / "_gepa_reflection",
            label="reflection",
        )
        # Sanitize: GEPA's logger uses Windows charmap encoding which chokes
        # on Unicode math/arrow symbols. Encode to ASCII with XML escapes so
        # the semantic content is preserved but no charmap errors occur.
        return result.encode("ascii", errors="xmlcharrefreplace").decode("ascii")

    return _lm

_eval_counter = 0
_eval_log_path: Path = None  # type: ignore
_candidate_log_path: Path = None  # type: ignore
_run_start_time: float = 0
_seen_candidates: set = set()


def _init_logging(stage_name: str):
    """Initialize per-stage log files."""
    global _eval_counter, _eval_log_path, _candidate_log_path, _run_start_time, _seen_candidates
    _eval_counter = 0
    _seen_candidates = set()
    _run_start_time = time.time()

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = stage_name.replace(" ", "_").replace("/", "_").replace("—", "-")
    _eval_log_path = LOG_DIR / f"{ts}_{safe_name}_evals.jsonl"
    _candidate_log_path = LOG_DIR / f"{ts}_{safe_name}_candidates.jsonl"


def _log_eval(entry: dict):
    """Append one evaluation record to the JSONL log."""
    if _eval_log_path:
        with open(_eval_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False, default=str) + "\n")


def _log_candidate(candidate: str, label: str = ""):
    """Log a candidate prompt if we haven't seen it before."""
    global _seen_candidates
    sig = hash(candidate)
    if sig in _seen_candidates:
        return
    _seen_candidates.add(sig)
    if _candidate_log_path:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "label": label,
            "candidate_len": len(candidate),
            "candidate": candidate,
        }
        with open(_candidate_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def evaluate_candidate(candidate: str, example: dict) -> tuple[float, dict]:
    """
    GEPA evaluator: score a candidate judge prompt on a single paper.

    Returns (score, side_info). Every call is logged to disk.
    """
    global _eval_counter
    _eval_counter += 1
    eval_id = _eval_counter
    t0 = time.time()

    from eval_harness import (
        load_skill_index, select_skills, load_skill_contents,
        retrieve_similar_papers, build_judge_prompt, parse_judge_output,
        score_prediction, build_diagnostic,
    )
    from claude_utils import run_claude_oneshot

    _log_candidate(candidate, label=f"eval_{eval_id}")

    paper = example
    paper_title = paper.get("title", "Unknown")[:80]

    # 1. Load skills
    skill_content = ""
    skill_files_loaded = []
    if _eval_config["use_skills"]:
        skill_index = load_skill_index()
        if skill_index:
            skill_paths = select_skills(paper, skill_index)
            skill_content = load_skill_contents(skill_paths)
            skill_files_loaded = skill_paths

    # 2. Retrieve similar papers
    retrieval_context = ""
    if _eval_config["use_retrieval"]:
        retrieval_context = retrieve_similar_papers(paper, top_k=5)

    # 3. Build and run prompt
    prompt = build_judge_prompt(paper, candidate, skill_content, retrieval_context,
                                include_reviews=_eval_config["include_reviews"])
    prompt_tokens_est = len(prompt) // 4

    output = run_claude_oneshot(
        prompt, timeout=120, model=_eval_config["model"],
        exp_dir=OUTPUT_DIR / "_gepa_runs",
        label="gepa_eval",
    )

    elapsed = time.time() - t0

    # 4. Parse and score
    predicted = parse_judge_output(output)
    if predicted is None:
        oa.log(f"PARSE FAILED for: {paper_title}")
        oa.log(f"Raw output: {output[:300]}")

        _log_eval({
            "eval_id": eval_id,
            "timestamp": datetime.now().isoformat(),
            "elapsed_s": round(elapsed, 1),
            "model": _eval_config["model"],
            "paper_id": paper.get("paper_id", ""),
            "paper_title": paper_title,
            "actual_rating": paper.get("avg_rating"),
            "status": "parse_failed",
            "raw_output_snippet": output[:500],
            "prompt_tokens_est": prompt_tokens_est,
            "skill_files": skill_files_loaded,
        })
        return 0.0, {"error": "parse_failed"}

    result = score_prediction(predicted, paper)
    diagnostic = build_diagnostic(paper, predicted, result)
    oa.log(diagnostic)

    _log_eval({
        "eval_id": eval_id,
        "timestamp": datetime.now().isoformat(),
        "elapsed_s": round(elapsed, 1),
        "model": _eval_config["model"],
        "paper_id": paper.get("paper_id", ""),
        "paper_title": paper_title,
        "actual_rating": paper.get("avg_rating"),
        "pred_rating": result["pred_rating"],
        "rating_error": result["rating_error"],
        "rating_score": result["rating_score"],
        "decision_correct": result.get("decision_correct"),
        "predicted_full": predicted,
        "status": "ok",
        "prompt_tokens_est": prompt_tokens_est,
        "skill_files": skill_files_loaded,
        "candidate_len": len(candidate),
    })

    return result["rating_score"], {
        "pred": result["pred_rating"],
        "actual": result["actual_rating"],
        "error": result["rating_error"],
        "title": paper_title,
    }


# ---------------------------------------------------------------------------
# Dataset preparation
# ---------------------------------------------------------------------------

def load_dataset(split: str, max_papers: int = None, require_reviews: bool = True,
                 seed: int = 42) -> list[dict]:
    """Load papers from a split for GEPA training."""
    path = DATA_DIR / f"{split}.jsonl"
    papers = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            p = json.loads(line)
            if not p.get("abstract") or not p.get("avg_rating"):
                continue
            if require_reviews and not p.get("review_texts"):
                continue
            papers.append(p)

    if max_papers and len(papers) > max_papers:
        rng = random.Random(seed)
        papers = rng.sample(papers, max_papers)

    return papers


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

OBJECTIVE = (
    "Predict the average reviewer rating (1-10) that a paper would receive "
    "at a top AI conference (ICLR, NeurIPS, ICML). The evaluator compares "
    "the predicted rating to the actual average reviewer rating. "
    "Higher score = smaller prediction error. "
    "The prompt should instruct the judge to use loaded skill files and "
    "retrieved similar papers to make calibrated predictions."
)


def _run_stage(stage_name: str, seed_prompt: str, train_papers: list, val_papers: list,
               model: str, max_evals: int, batch_size: int, reflection_model: str,
               use_skills: bool, use_retrieval: bool, include_reviews: bool,
               seed: int, run_dir: str) -> oa.GEPAResult:
    """Run a single GEPA optimization stage."""
    _eval_config["model"] = model
    _eval_config["use_skills"] = use_skills
    _eval_config["use_retrieval"] = use_retrieval
    _eval_config["include_reviews"] = include_reviews

    _init_logging(stage_name)
    stage_start = time.time()

    print(f"\n{'='*60}")
    print(f"STAGE: {stage_name}")
    print(f"{'='*60}")
    print(f"  Started at:       {datetime.now().isoformat()}")
    print(f"  Judge model:      {model}")
    print(f"  Max evaluations:  {max_evals}")
    print(f"  Reflection model: {reflection_model}")
    print(f"  Batch size:       {batch_size}")
    print(f"  Train:            {len(train_papers)} | Val: {len(val_papers)}")
    print(f"  Skills:           {use_skills} | Retrieval: {use_retrieval} | Reviews: {include_reviews}")
    print(f"  Seed prompt:      {len(seed_prompt)} chars")
    print(f"  Eval log:         {_eval_log_path}")
    print(f"  Candidate log:    {_candidate_log_path}")
    print()

    reflection_lm_callable = _make_claude_code_lm(model=reflection_model)
    print(f"  Reflection LM:    Claude Code CLI ({reflection_model})")

    config = GEPAConfig(
        engine=EngineConfig(
            run_dir=run_dir,
            seed=seed,
            max_metric_calls=max_evals,
            display_progress_bar=True,
            cache_evaluation=True,
        ),
        reflection=ReflectionConfig(
            reflection_lm=reflection_lm_callable,
            reflection_minibatch_size=batch_size,
        ),
    )

    result = optimize_anything(
        seed_candidate=seed_prompt,
        evaluator=evaluate_candidate,
        dataset=train_papers,
        valset=val_papers,
        objective=OBJECTIVE,
        config=config,
    )

    stage_elapsed = time.time() - stage_start
    best = result.best_candidate
    if isinstance(best, dict):
        best = best.get("prompt", str(best))

    print(f"\n[{stage_name}] Finished at:  {datetime.now().isoformat()}")
    print(f"[{stage_name}] Wall time:    {stage_elapsed/60:.1f} min")
    print(f"[{stage_name}] Evaluations:  {_eval_counter}")
    best_score = result.val_aggregate_scores[result.best_idx]
    print(f"[{stage_name}] Best score:   {best_score:.4f}")
    print(f"[{stage_name}] Best prompt:  {len(str(best))} chars")

    stage_summary = {
        "stage": stage_name,
        "started": datetime.fromtimestamp(stage_start).isoformat(),
        "finished": datetime.now().isoformat(),
        "wall_time_min": round(stage_elapsed / 60, 2),
        "evals_completed": _eval_counter,
        "best_score": best_score,
        "best_prompt_len": len(str(best)),
        "model": model,
        "reflection_model": reflection_model,
        "max_evals": max_evals,
        "batch_size": batch_size,
        "train_size": len(train_papers),
        "val_size": len(val_papers),
        "use_skills": use_skills,
        "use_retrieval": use_retrieval,
        "eval_log_file": str(_eval_log_path),
        "candidate_log_file": str(_candidate_log_path),
    }
    summary_path = LOG_DIR / f"stage_summary_{stage_name.replace(' ', '_').replace('/', '_').replace('—', '-')}.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(stage_summary, f, indent=2)
    print(f"[{stage_name}] Stage summary: {summary_path}")

    return result


def run(stage1_evals: int = 500, stage2_evals: int = 150,
        train_size: int = 100, val_size: int = 30,
        stage1_model: str = "sonnet", stage2_model: str = "opus",
        use_skills: bool = True, use_retrieval: bool = True,
        include_reviews: bool = True,
        reflection_model: str = "sonnet",
        batch_size: int = 10, seed: int = 42,
        skip_stage1: bool = False):

    run_start = time.time()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    print(f"\n{'#'*60}")
    print(f"  GEPA Judge Optimization — Full Run")
    print(f"  Started: {datetime.now().isoformat()}")
    print(f"{'#'*60}\n")

    print("Loading datasets...")
    train_papers = load_dataset("train", max_papers=train_size, seed=seed)
    val_papers = load_dataset("test", max_papers=val_size, seed=seed)
    print(f"  Train: {len(train_papers)} papers")
    print(f"  Val:   {len(val_papers)} papers")

    stage1_score = None

    # --- Stage 1: Bulk exploration with cheaper model ---
    if skip_stage1:
        stage1_prompt_path = OUTPUT_DIR / "stage1_best_prompt.md"
        if stage1_prompt_path.exists():
            stage1_best = stage1_prompt_path.read_text(encoding="utf-8")
            print(f"\n[SKIP STAGE 1] Loading from {stage1_prompt_path} ({len(stage1_best)} chars)")
        else:
            stage1_best = SEED_JUDGE_PROMPT
            print(f"\n[SKIP STAGE 1] No stage1 prompt found, using seed prompt")
    else:
        stage1_result = _run_stage(
            stage_name=f"Stage 1 — Explore ({stage1_model})",
            seed_prompt=SEED_JUDGE_PROMPT,
            train_papers=train_papers,
            val_papers=val_papers,
            model=stage1_model,
            max_evals=stage1_evals,
            batch_size=batch_size,
            reflection_model=reflection_model,
            use_skills=use_skills,
            use_retrieval=use_retrieval,
            include_reviews=include_reviews,
            seed=seed,
            run_dir=str(OUTPUT_DIR / "gepa_stage1"),
        )
        stage1_best = stage1_result.best_candidate
        if isinstance(stage1_best, dict):
            stage1_best = stage1_best.get("prompt", str(stage1_best))
        stage1_best = str(stage1_best)
        stage1_score = stage1_result.val_aggregate_scores[stage1_result.best_idx]

        stage1_path = OUTPUT_DIR / "stage1_best_prompt.md"
        stage1_path.write_text(stage1_best, encoding="utf-8")
        print(f"\nStage 1 prompt saved to: {stage1_path}")

    # --- Stage 2: Polish with production model ---
    stage2_result = _run_stage(
        stage_name=f"Stage 2 — Polish ({stage2_model})",
        seed_prompt=stage1_best,
        train_papers=train_papers,
        val_papers=val_papers,
        model=stage2_model,
        max_evals=stage2_evals,
        batch_size=batch_size,
        reflection_model=reflection_model,
        use_skills=use_skills,
        use_retrieval=use_retrieval,
        include_reviews=include_reviews,
        seed=seed + 1,
        run_dir=str(OUTPUT_DIR / "gepa_stage2"),
    )

    final_best = stage2_result.best_candidate
    if isinstance(final_best, dict):
        final_best = final_best.get("prompt", str(final_best))

    prompt_path = OUTPUT_DIR / "best_judge_prompt.md"
    Path(prompt_path).write_text(str(final_best), encoding="utf-8")

    run_elapsed = time.time() - run_start

    print(f"\n{'#'*60}")
    print(f"  OPTIMIZATION COMPLETE")
    print(f"{'#'*60}")
    print(f"  Finished:     {datetime.now().isoformat()}")
    print(f"  Total time:   {run_elapsed/60:.1f} min ({run_elapsed/3600:.2f} hr)")
    stage2_score = stage2_result.val_aggregate_scores[stage2_result.best_idx]
    if stage1_score is not None:
        print(f"  Stage 1 best: {stage1_score:.4f} ({stage1_model})")
    print(f"  Stage 2 best: {stage2_score:.4f} ({stage2_model})")
    print(f"  Final prompt: {prompt_path} ({len(str(final_best))} chars)")
    print(f"  Logs dir:     {LOG_DIR}")

    log_data = {
        "run_started": datetime.fromtimestamp(run_start).isoformat(),
        "run_finished": datetime.now().isoformat(),
        "total_wall_time_min": round(run_elapsed / 60, 2),
        "stage1_model": stage1_model,
        "stage1_evals": stage1_evals,
        "stage1_best_score": stage1_score,
        "stage1_skipped": skip_stage1,
        "stage2_model": stage2_model,
        "stage2_evals": stage2_evals,
        "stage2_best_score": stage2_score,
        "final_prompt_path": str(prompt_path),
        "final_prompt_len": len(str(final_best)),
        "train_size": len(train_papers),
        "val_size": len(val_papers),
        "use_skills": use_skills,
        "use_retrieval": use_retrieval,
        "reflection_model": reflection_model,
        "batch_size": batch_size,
        "seed": seed,
    }
    log_path = OUTPUT_DIR / "training_log.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)
    print(f"  Training log: {log_path}")

    return stage2_result


def main():
    parser = argparse.ArgumentParser(description="GEPA optimization of judge prompt")
    parser.add_argument("--stage1-evals", type=int, default=500,
                        help="Stage 1 evaluations with cheap model (default: 500)")
    parser.add_argument("--stage2-evals", type=int, default=150,
                        help="Stage 2 evaluations with production model (default: 150)")
    parser.add_argument("--train-size", type=int, default=100,
                        help="Number of training papers to use (default: 100)")
    parser.add_argument("--val-size", type=int, default=30,
                        help="Number of validation papers (default: 30)")
    parser.add_argument("--stage1-model", type=str, default="sonnet",
                        help="Cheap model for bulk exploration (default: sonnet)")
    parser.add_argument("--stage2-model", type=str, default="opus",
                        help="Production model for final polish (default: opus)")
    parser.add_argument("--reflection-model", type=str, default="sonnet",
                        help="Claude model for GEPA reflection via Claude Code CLI (default: sonnet)")
    parser.add_argument("--batch-size", type=int, default=10,
                        help="Papers per GEPA minibatch (default: 10)")
    parser.add_argument("--no-skills", action="store_true")
    parser.add_argument("--no-retrieval", action="store_true")
    parser.add_argument("--no-reviews", action="store_true",
                        help="Disable redacted review content in judge prompt")
    parser.add_argument("--skip-stage1", action="store_true",
                        help="Skip stage 1, load its output and go straight to stage 2")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    run(
        stage1_evals=args.stage1_evals,
        stage2_evals=args.stage2_evals,
        train_size=args.train_size,
        val_size=args.val_size,
        stage1_model=args.stage1_model,
        stage2_model=args.stage2_model,
        reflection_model=args.reflection_model,
        batch_size=args.batch_size,
        use_skills=not args.no_skills,
        use_retrieval=not args.no_retrieval,
        include_reviews=not args.no_reviews,
        skip_stage1=args.skip_stage1,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()
