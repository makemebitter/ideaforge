"""
Phase 2: Skill Library Generation

Generates a library of skill files from the review corpus, organized into:
  A. Topic skills   — one per research area (video_generation, diffusion, etc.)
  B. Dimension skills — one per evaluation axis (novelty, soundness, etc.)
  C. Calibration skills — one per score tier (2-3, 4-5, 6-7, 8-10)
  D. Skill index    — maps keywords to skill file paths for dynamic loading

Two-step generation per skill file:
  Step 1: Statistical extraction (Python, no LLM)
  Step 2: Agentic synthesis (Claude Code session that reads PDFs on demand)

Usage:
    python generate_skills.py                       # Generate all skills
    python generate_skills.py --type topics          # Only topic skills
    python generate_skills.py --type dimensions      # Only dimension skills
    python generate_skills.py --type calibration     # Only calibration skills
    python generate_skills.py --stats-only           # Only compute stats, skip LLM
    python generate_skills.py --parallel 4           # Run 4 Claude sessions in parallel
"""

import json
import re
import argparse
import functools
import time
import logging
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

import os

from claude_utils import run_claude_oneshot

print = functools.partial(print, flush=True)  # type: ignore

BASE_DIR = Path(__file__).parent
_RESOURCES_DIR = os.environ.get("IDEAFORGE_RESOURCES_DIR")
if _RESOURCES_DIR:
    DATA_DIR = Path(_RESOURCES_DIR) / "data"
    SKILLS_DIR = Path(_RESOURCES_DIR) / "skills"
    RESEARCH_DATA = Path(_RESOURCES_DIR) / "research_data"
    LOG_DIR = Path(_RESOURCES_DIR) / "output" / "logs"
else:
    DATA_DIR = BASE_DIR / "data"
    SKILLS_DIR = BASE_DIR / "skills"
    RESEARCH_DATA = BASE_DIR.parent / "research_data"
    LOG_DIR = BASE_DIR / "output" / "logs"

logger = logging.getLogger("generate_skills")


def _setup_skill_logger() -> Path:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = LOG_DIR / f"{ts}_skill_generation.log"
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    return log_file


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_train_data() -> list[dict]:
    """Load training split (only papers with full review text)."""
    train_path = DATA_DIR / "train.jsonl"
    if not train_path.exists():
        raise FileNotFoundError(f"Run data_pipeline.py first: {train_path}")
    records = []
    with open(train_path, "r", encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if r.get("review_texts"):
                records.append(r)
    return records


# ---------------------------------------------------------------------------
# Topic detection — group papers into topics from primary_area + keywords
# ---------------------------------------------------------------------------

TOPIC_MAP = {
    "video_generation": [
        "video generation", "video synthesis", "text-to-video", "image-to-video",
        "video diffusion", "video editing", "video inpainting", "video prediction",
        "video super-resolution", "video interpolation", "frame interpolation",
        "video tokenizer", "video model", "sora",
    ],
    "motion_generation": [
        "motion generation", "motion synthesis", "human motion", "dance generation",
        "gesture generation", "character animation", "motion prediction",
        "motion capture", "action generation",
    ],
    "diffusion_models": [
        "diffusion model", "denoising diffusion", "score-based", "flow matching",
        "ddpm", "ddim", "stable diffusion", "latent diffusion", "consistency model",
        "rectified flow",
    ],
    "world_models": [
        "world model", "world simulation", "environment model", "dynamics model",
        "model-based reinforcement", "imagination",
    ],
    "language_models": [
        "language model", "llm", "large language", "transformer", "gpt",
        "instruction tuning", "rlhf", "alignment", "chain-of-thought",
        "in-context learning", "prompting",
    ],
    "vision_language": [
        "vision-language", "multimodal", "visual question answering", "vqa",
        "image captioning", "clip", "contrastive learning", "visual grounding",
    ],
    "image_generation": [
        "image generation", "image synthesis", "text-to-image", "image editing",
        "inpainting", "super-resolution", "style transfer", "image-to-image",
        "gan", "generative adversarial",
    ],
    "3d_vision": [
        "3d", "nerf", "gaussian splatting", "point cloud", "mesh", "3d reconstruction",
        "novel view", "3d generation", "depth estimation", "3d object",
    ],
    "reinforcement_learning": [
        "reinforcement learning", "policy gradient", "q-learning", "reward",
        "multi-agent", "offline rl", "safe rl", "exploration",
    ],
    "optimization": [
        "optimization", "gradient descent", "adam", "learning rate", "convergence",
        "federated learning", "distributed", "communication efficiency",
    ],
    "graph_neural_networks": [
        "graph neural", "gnn", "graph learning", "message passing",
        "graph transformer", "molecular", "drug discovery",
    ],
    "robustness_safety": [
        "adversarial", "robustness", "safety", "fairness", "bias", "privacy",
        "differential privacy", "backdoor", "certification",
    ],
    "efficient_ml": [
        "efficient", "pruning", "quantization", "distillation", "compression",
        "neural architecture search", "nas", "mixture of experts", "moe",
        "sparse", "attention mechanism",
    ],
    "self_supervised": [
        "self-supervised", "contrastive", "masked", "pretraining", "representation learning",
        "foundation model", "pre-training",
    ],
    "audio_speech": [
        "audio", "speech", "text-to-speech", "tts", "voice", "music",
        "sound", "talking head", "portrait animation",
    ],
    "theoretical_ml": [
        "theory", "generalization", "pac", "sample complexity", "statistical learning",
        "information theory", "kernel", "approximation",
    ],
}


def classify_topic(paper: dict) -> list[str]:
    """Return list of topics this paper belongs to (can be multiple)."""
    searchable = " ".join([
        paper.get("title", ""),
        paper.get("primary_area", ""),
        " ".join(paper.get("keywords", [])),
        paper.get("abstract", "")[:500],
    ]).lower()

    topics = []
    for topic, keywords in TOPIC_MAP.items():
        if any(kw in searchable for kw in keywords):
            topics.append(topic)
    return topics if topics else ["general"]


# ---------------------------------------------------------------------------
# Step 1: Statistical extraction (Python, no LLM)
# ---------------------------------------------------------------------------

def extract_topic_stats(papers: list[dict], topic: str) -> dict:
    """Compute statistics for a topic from its papers."""
    ratings = [p["avg_rating"] for p in papers]
    accepted = sum(1 for p in papers if p.get("decision") and "accept" in str(p["decision"]).lower())

    tier_strengths = defaultdict(list)
    tier_weaknesses = defaultdict(list)
    all_strengths_phrases = Counter()
    all_weaknesses_phrases = Counter()

    for p in papers:
        tier = _score_tier_label(p["avg_rating"])
        for rev in (p.get("review_texts") or []):
            s = rev.get("strengths", "")
            w = rev.get("weaknesses", "")
            if s:
                tier_strengths[tier].append(s[:500])
                for phrase in _extract_phrases(s):
                    all_strengths_phrases[phrase] += 1
            if w:
                tier_weaknesses[tier].append(w[:500])
                for phrase in _extract_phrases(w):
                    all_weaknesses_phrases[phrase] += 1

    soundness = [p["avg_soundness"] for p in papers if p.get("avg_soundness")]
    contribution = [p["avg_contribution"] for p in papers if p.get("avg_contribution")]
    presentation = [p["avg_presentation"] for p in papers if p.get("avg_presentation")]

    return {
        "topic": topic,
        "num_papers": len(papers),
        "num_accepted": accepted,
        "acceptance_rate": round(accepted / len(papers), 3) if papers else 0,
        "rating_mean": round(sum(ratings) / len(ratings), 2) if ratings else 0,
        "rating_median": round(sorted(ratings)[len(ratings) // 2], 2) if ratings else 0,
        "rating_std": round(_std(ratings), 2),
        "rating_min": min(ratings) if ratings else 0,
        "rating_max": max(ratings) if ratings else 0,
        "avg_soundness": round(sum(soundness) / len(soundness), 2) if soundness else None,
        "avg_contribution": round(sum(contribution) / len(contribution), 2) if contribution else None,
        "avg_presentation": round(sum(presentation) / len(presentation), 2) if presentation else None,
        "top_strength_phrases": all_strengths_phrases.most_common(30),
        "top_weakness_phrases": all_weaknesses_phrases.most_common(30),
        "tier_example_count": {t: len(v) for t, v in tier_strengths.items()},
    }


def _score_tier_label(avg_rating: float) -> str:
    if avg_rating < 4:
        return "low (1-3)"
    elif avg_rating < 6:
        return "borderline (4-5)"
    elif avg_rating < 8:
        return "good (6-7)"
    else:
        return "excellent (8-10)"


def _std(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return (sum((v - mean) ** 2 for v in values) / (len(values) - 1)) ** 0.5


def _extract_phrases(text: str) -> list[str]:
    """Extract commonly occurring evaluative phrases from reviewer text."""
    patterns = [
        r"lack(?:s|ing)?\s+\w+",
        r"insufficient\s+\w+",
        r"strong\s+\w+",
        r"weak\s+\w+",
        r"novel(?:ty)?",
        r"incremental",
        r"significant\s+\w+",
        r"missing\s+\w+",
        r"unclear\s+\w+",
        r"well[\s-]written",
        r"poorly[\s-]written",
        r"comprehensive\s+\w+",
        r"limited\s+\w+",
        r"solid\s+\w+",
        r"thorough\s+\w+",
        r"ablation",
        r"baseline",
        r"state[\s-]of[\s-]the[\s-]art",
        r"reproducib",
        r"scalab",
        r"fair comparison",
    ]
    found = []
    text_lower = text.lower()
    for pat in patterns:
        for m in re.finditer(pat, text_lower):
            found.append(m.group().strip())
    return found


def build_paper_manifest(papers: list[dict], topic: str) -> str:
    """Build a manifest of papers for the Claude agent to choose from."""
    sorted_papers = sorted(papers, key=lambda p: p["avg_rating"], reverse=True)
    lines = [f"# Paper Manifest for topic: {topic}", f"# {len(papers)} papers total\n"]

    for i, p in enumerate(sorted_papers):
        title = p.get("title", "Unknown")
        rating = p["avg_rating"]
        decision = p.get("decision", "?")
        pdf = p.get("pdf_path") or "NO_PDF"
        forum_url = p.get("forum_url", "")
        n_reviews = len(p.get("review_texts") or [])

        # Find review JSON path if available
        review_json = _find_review_json(p)

        lines.append(f"[{i+1}] rating={rating:.1f} | decision={decision} | reviews={n_reviews}")
        lines.append(f"    title: {title}")
        lines.append(f"    pdf: {pdf}")
        lines.append(f"    review_json: {review_json}")
        lines.append(f"    forum: {forum_url}")
        lines.append("")

    return "\n".join(lines)


def _find_review_json(paper: dict) -> str:
    """Try to locate the review JSON file for a paper."""
    forum_url = paper.get("forum_url", "")
    if "id=" in forum_url:
        forum_id = forum_url.split("id=")[-1].split("&")[0]
        venue = paper.get("venue", "iclr")
        year = paper.get("year")
        if year:
            candidate = RESEARCH_DATA / venue / "reviews" / str(year) / f"{forum_id}_reviews.json"
            if candidate.exists():
                return str(candidate)
    return "NOT_FOUND"


# ---------------------------------------------------------------------------
# Step 2: Agentic skill synthesis via Claude Code
# ---------------------------------------------------------------------------

def generate_topic_skill(topic: str, papers: list[dict], stats: dict,
                         model: str = "sonnet", timeout: int = 1800) -> str:
    """Generate a single topic skill file using Claude Code."""
    manifest = build_paper_manifest(papers, topic)
    stats_text = json.dumps({k: v for k, v in stats.items()
                             if k not in ("top_strength_phrases", "top_weakness_phrases")},
                            indent=2)
    top_strengths = "\n".join(f"  - {phrase} ({count}x)" for phrase, count in stats["top_strength_phrases"][:20])
    top_weaknesses = "\n".join(f"  - {phrase} ({count}x)" for phrase, count in stats["top_weakness_phrases"][:20])

    prompt = f"""You are an expert AI research reviewer building a **skill file** for evaluating papers in the topic area: **{topic}**.

## Your Task

Write a comprehensive skill file (Markdown, 10-20K tokens) that will be loaded by an AI judge agent when evaluating new research ideas in this area. The file should enable the judge to give calibrated, expert-level evaluations.

## Statistics from {stats['num_papers']} papers in this area

```json
{stats_text}
```

### Most common strength phrases from reviewers:
{top_strengths}

### Most common weakness phrases from reviewers:
{top_weaknesses}

## Paper Manifest

Below is a manifest of all {len(papers)} papers in this topic with their scores, PDF paths, and review JSON paths.

**YOUR READING STRATEGY:**
1. Start by reading 3-4 of the HIGHEST rated papers (8+) to understand what excellence looks like
2. Read 3-4 of the LOWEST rated papers (1-4) to understand common failures
3. Read 3-4 BORDERLINE papers (5-6) to understand the acceptance threshold
4. Read 2-3 more papers that seem interesting or unusual based on what you've learned

For each paper you read:
- Read the review JSON first (it has reviewer strengths/weaknesses/questions)
- If the paper has a PDF, skim the methods and experiments sections
- Note specific patterns: what methods do reviewers praise? what baselines are expected?

```
{manifest}
```

## Output Format

Write the skill file with these sections:

### 1. Topic Overview
- What this research area is about, key challenges, state of the art
- Score distribution: what scores are typical, what's the acceptance bar

### 2. What Reviewers Praise (with real examples)
- Specific technical contributions that earn high scores
- Quote actual reviewer language where possible

### 3. What Reviewers Criticize (with real examples)
- Common failure modes, missing comparisons, weak experiments
- Quote actual reviewer language where possible

### 4. Required Baselines & Metrics
- What baselines and metrics are EXPECTED in this area
- Papers that miss these consistently score lower

### 5. Common Technical Pitfalls
- Specific technical mistakes reviewers flag in this area

### 6. Scoring Rubric for This Topic
- What a 3/10 paper in this area looks like (with example)
- What a 5/10 paper looks like (borderline)
- What a 7/10 paper looks like (solid accept)
- What a 9/10 paper looks like (exceptional)

### 7. Key Papers & Expected Citations
- Papers that reviewers frequently cite as expected baselines or comparisons

IMPORTANT: Ground everything in REAL reviewer quotes and paper examples. Do NOT make up generic advice.
Read the actual papers and reviews to produce technically specific, calibrated content.
"""

    exp_dir = SKILLS_DIR / "topics" / f"_gen_{topic}"
    output = run_claude_oneshot(
        prompt, timeout=timeout, model=model,
        exp_dir=exp_dir, label=f"topic_{topic}",
        cwd=str(BASE_DIR.parent),
    )
    return output


def generate_dimension_skill(dimension: str, papers: list[dict],
                             model: str = "sonnet", timeout: int = 1800) -> str:
    """Generate a dimension skill file (novelty, soundness, etc.)."""
    dim_lower = dimension.lower()

    review_field_map = {
        "novelty": "contribution",
        "soundness": "soundness",
        "experiments": "soundness",
        "clarity": "presentation",
        "significance": "contribution",
        "reproducibility": "soundness",
    }
    score_field = review_field_map.get(dim_lower, "soundness")

    examples_by_tier = defaultdict(list)
    for p in papers:
        for rev in (p.get("review_texts") or []):
            sub_score = rev.get(score_field)
            if sub_score is None:
                continue
            try:
                sub_score = float(str(sub_score).split(":")[0].strip())
            except (ValueError, IndexError):
                continue
            tier = "high" if sub_score >= 3.5 else ("mid" if sub_score >= 2.5 else "low")
            examples_by_tier[tier].append({
                "title": p.get("title", ""),
                "rating": p.get("avg_rating", 0),
                "sub_score": sub_score,
                "strengths": rev.get("strengths", "")[:400],
                "weaknesses": rev.get("weaknesses", "")[:400],
            })

    for tier in examples_by_tier:
        examples_by_tier[tier] = examples_by_tier[tier][:15]

    examples_text = ""
    for tier in ["high", "mid", "low"]:
        exs = examples_by_tier.get(tier, [])
        if exs:
            examples_text += f"\n### {tier.upper()} {dimension} examples ({len(exs)} papers):\n"
            for e in exs[:8]:
                examples_text += f"\n**{e['title'][:80]}** (rating={e['rating']}, {score_field}={e['sub_score']})\n"
                examples_text += f"  Strengths: {e['strengths'][:200]}...\n"
                examples_text += f"  Weaknesses: {e['weaknesses'][:200]}...\n"

    prompt = f"""You are an expert AI research reviewer building a **dimension skill file** for the evaluation dimension: **{dimension}**.

## Your Task

Write a comprehensive skill file (Markdown, 5-15K tokens) that teaches an AI judge how to evaluate the "{dimension}" dimension of any research paper. This file is loaded dynamically — it should be self-contained.

## Real Reviewer Examples

Below are real reviewer comments grouped by their {score_field} sub-score (1-4 scale).
{examples_text}

## Output Format

### 1. What "{dimension}" means in peer review
- Definition, scope, what reviewers look for

### 2. Score 1 (Poor {dimension})
- What this looks like, common patterns
- Real reviewer quotes

### 3. Score 2 (Below Average {dimension})
- What this looks like, common patterns
- Real reviewer quotes

### 4. Score 3 (Good {dimension})
- What this looks like
- Real reviewer quotes

### 5. Score 4 (Excellent {dimension})
- What this looks like
- Real reviewer quotes

### 6. Red Flags & Green Flags
- Instant indicators of low vs high {dimension}

### 7. Cross-topic Patterns
- How {dimension} expectations differ by research area

Ground everything in the real reviewer examples above. Be specific and concrete.
"""

    exp_dir = SKILLS_DIR / "dimensions" / f"_gen_{dimension}"
    output = run_claude_oneshot(
        prompt, timeout=timeout, model=model,
        exp_dir=exp_dir, label=f"dim_{dimension}",
        cwd=str(BASE_DIR.parent),
    )
    return output


def generate_calibration_skill(tier: str, papers: list[dict],
                               model: str = "sonnet", timeout: int = 1800) -> str:
    """Generate a calibration skill file for a score tier."""
    tier_ranges = {
        "score_2_3": (1.5, 3.5),
        "score_4_5": (3.5, 5.5),
        "score_6_7": (5.5, 7.5),
        "score_8_10": (7.5, 10.5),
    }
    lo, hi = tier_ranges[tier]
    tier_papers = [p for p in papers if lo <= p["avg_rating"] < hi]
    tier_papers.sort(key=lambda p: p["avg_rating"])

    sample = tier_papers[:20]
    manifest = build_paper_manifest(sample, f"calibration_{tier}")

    examples_text = ""
    for p in sample[:12]:
        examples_text += f"\n### {p.get('title', 'Unknown')[:80]}\n"
        examples_text += f"**Rating: {p['avg_rating']:.1f}** | Decision: {p.get('decision', '?')}\n"
        for i, rev in enumerate((p.get("review_texts") or [])[:2]):
            examples_text += f"\nReviewer {i+1} (rating={rev.get('rating', '?')}):\n"
            examples_text += f"  Strengths: {rev.get('strengths', '')[:300]}\n"
            examples_text += f"  Weaknesses: {rev.get('weaknesses', '')[:300]}\n"

    prompt = f"""You are an expert AI research reviewer building a **calibration skill file** for papers scoring in the **{tier.replace('_', ' ')}** range.

## Your Task

Write a comprehensive skill file (Markdown, 5-15K tokens) that teaches an AI judge what papers in this score range look like. This is critical for calibration — the judge must learn the ABSOLUTE quality bar, not just relative ranking.

## Paper Manifest (for reading PDFs on demand)

```
{manifest}
```

## Real Examples at This Score Level
{examples_text}

## Reading Strategy

Read 5-8 papers from the manifest above:
- Read their review JSONs for detailed reviewer feedback
- Skim PDFs if available to see the actual paper quality
- Focus on understanding WHY these papers got this score

## Output Format

### 1. Score Range Profile
- What {tier.replace('_', ' ')}/10 means at top AI conferences
- Typical decision: accept, borderline, or reject?
- How common are papers at this level?

### 2. Characteristic Patterns (5-8 real examples)
For each example paper:
- Title, score, decision
- Key strengths/weaknesses from reviewers
- Why it landed at this score specifically

### 3. Common Traits
- What almost ALL papers at this level share
- What distinguishes this tier from adjacent tiers

### 4. "This paper is a {tier.replace('_', ' ')} because..." Templates
- 5-10 sentence templates a judge could use to justify this score
- Each grounded in real reviewer patterns

Ground everything in REAL papers and reviewer quotes. Read the papers!
"""

    exp_dir = SKILLS_DIR / "calibration" / f"_gen_{tier}"
    output = run_claude_oneshot(
        prompt, timeout=timeout, model=model,
        exp_dir=exp_dir, label=f"calib_{tier}",
        cwd=str(BASE_DIR.parent),
    )
    return output


# ---------------------------------------------------------------------------
# Skill index generation
# ---------------------------------------------------------------------------

def build_skill_index(topics_generated: list[str], dimensions: list[str],
                      calibration_tiers: list[str]) -> dict:
    """Build the skill index mapping keywords to file paths."""
    index = {"topics": {}, "dimensions": {}, "calibration": {}, "keyword_to_topic": {}}

    for topic in topics_generated:
        path = f"skills/topics/{topic}.md"
        index["topics"][topic] = path
        for kw in TOPIC_MAP.get(topic, []):
            index["keyword_to_topic"][kw] = topic

    for dim in dimensions:
        index["dimensions"][dim] = f"skills/dimensions/{dim}.md"

    for tier in calibration_tiers:
        index["calibration"][tier] = f"skills/calibration/{tier}.md"

    return index


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def run(skill_type: str = "all", stats_only: bool = False,
        parallel: int = 2, model: str = "sonnet", timeout: int = 1800):

    log_file = _setup_skill_logger()
    run_start = time.time()

    print("Loading training data (papers with full review text)...")
    papers = load_train_data()
    print(f"  Loaded {len(papers)} papers with review text")
    print(f"  Log file: {log_file}\n")
    logger.info("Skill generation started: type=%s, model=%s, parallel=%d, papers=%d",
                skill_type, model, parallel, len(papers))

    # Group papers by topic
    topic_papers = defaultdict(list)
    for p in papers:
        for topic in classify_topic(p):
            topic_papers[topic].append(p)

    print(f"Topics detected: {len(topic_papers)}")
    for topic, plist in sorted(topic_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {topic}: {len(plist)} papers")
    print()

    # --- Topic Skills ---
    if skill_type in ("all", "topics"):
        print("=" * 60)
        print("GENERATING TOPIC SKILLS")
        print("=" * 60)

        # Skip topics with too few papers
        viable_topics = {t: ps for t, ps in topic_papers.items() if len(ps) >= 5}
        print(f"Viable topics (>=5 papers): {len(viable_topics)}\n")

        topic_stats = {}
        for topic, plist in viable_topics.items():
            stats = extract_topic_stats(plist, topic)
            topic_stats[topic] = stats
            stats_path = SKILLS_DIR / "topics" / f"{topic}_stats.json"
            stats_path.parent.mkdir(parents=True, exist_ok=True)
            with open(stats_path, "w", encoding="utf-8") as f:
                json.dump(stats, f, indent=2, default=str)
            print(f"  [{topic}] {stats['num_papers']} papers, "
                  f"mean={stats['rating_mean']}, accept={stats['acceptance_rate']:.0%}")

        if stats_only:
            print("\n[STATS ONLY] Skipping LLM synthesis.")
            return

        print(f"\nLaunching Claude agents for {len(viable_topics)} topics "
              f"(parallel={parallel}, model={model})...\n")

        def _gen_topic(topic):
            plist = viable_topics[topic]
            stats = topic_stats[topic]
            t0 = time.time()
            logger.info("[TOPIC START] %s (%d papers)", topic, len(plist))
            print(f"  [START] {topic} ({len(plist)} papers)")
            result = generate_topic_skill(topic, plist, stats, model=model, timeout=timeout)
            elapsed = time.time() - t0
            out_path = SKILLS_DIR / "topics" / f"{topic}.md"
            out_path.write_text(result, encoding="utf-8")
            logger.info("[TOPIC DONE] %s -> %s (%d chars, %.1fs)",
                        topic, out_path.name, len(result), elapsed)
            print(f"  [DONE]  {topic} -> {out_path.name} ({len(result)} chars, {elapsed:.0f}s)")
            return topic

        completed_topics = []
        with ThreadPoolExecutor(max_workers=parallel) as pool:
            futures = {pool.submit(_gen_topic, t): t for t in viable_topics}
            for future in as_completed(futures):
                try:
                    completed_topics.append(future.result())
                except Exception as e:
                    logger.error("[TOPIC ERROR] %s: %s", futures[future], e)
                    print(f"  [ERROR] {futures[future]}: {e}")

    # --- Dimension Skills ---
    dimensions = ["novelty", "soundness", "experiments", "clarity", "significance", "reproducibility"]

    if skill_type in ("all", "dimensions"):
        print("\n" + "=" * 60)
        print("GENERATING DIMENSION SKILLS")
        print("=" * 60)

        if stats_only:
            print("[STATS ONLY] Skipping.\n")
        else:
            for dim in dimensions:
                t0 = time.time()
                logger.info("[DIM START] %s", dim)
                print(f"  [START] {dim}")
                result = generate_dimension_skill(dim, papers, model=model, timeout=timeout)
                elapsed = time.time() - t0
                out_path = SKILLS_DIR / "dimensions" / f"{dim}.md"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(result, encoding="utf-8")
                logger.info("[DIM DONE] %s -> %s (%d chars, %.1fs)",
                            dim, out_path.name, len(result), elapsed)
                print(f"  [DONE]  {dim} -> {out_path.name} ({len(result)} chars, {elapsed:.0f}s)")

    # --- Calibration Skills ---
    calibration_tiers = ["score_2_3", "score_4_5", "score_6_7", "score_8_10"]

    if skill_type in ("all", "calibration"):
        print("\n" + "=" * 60)
        print("GENERATING CALIBRATION SKILLS")
        print("=" * 60)

        if stats_only:
            print("[STATS ONLY] Skipping.\n")
        else:
            for tier in calibration_tiers:
                t0 = time.time()
                logger.info("[CALIB START] %s", tier)
                print(f"  [START] {tier}")
                result = generate_calibration_skill(tier, papers, model=model, timeout=timeout)
                elapsed = time.time() - t0
                out_path = SKILLS_DIR / "calibration" / f"{tier}.md"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(result, encoding="utf-8")
                logger.info("[CALIB DONE] %s -> %s (%d chars, %.1fs)",
                            tier, out_path.name, len(result), elapsed)
                print(f"  [DONE]  {tier} -> {out_path.name} ({len(result)} chars, {elapsed:.0f}s)")

    # --- Build Index ---
    print("\n" + "=" * 60)
    print("BUILDING SKILL INDEX")
    print("=" * 60)

    existing_topics = [p.stem for p in (SKILLS_DIR / "topics").glob("*.md")]
    existing_dims = [p.stem for p in (SKILLS_DIR / "dimensions").glob("*.md")]
    existing_calibs = [p.stem for p in (SKILLS_DIR / "calibration").glob("*.md")]

    index = build_skill_index(existing_topics, existing_dims, existing_calibs)
    index_path = SKILLS_DIR / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    print(f"  Saved to {index_path}")
    print(f"  Topics: {len(index['topics'])}, Dimensions: {len(index['dimensions'])}, "
          f"Calibration: {len(index['calibration'])}, Keywords: {len(index['keyword_to_topic'])}")

    run_elapsed = time.time() - run_start
    logger.info("Skill generation complete: %.1f min, %d topics, %d dimensions, %d calibration tiers",
                run_elapsed / 60, len(index["topics"]), len(index["dimensions"]),
                len(index["calibration"]))

    summary = {
        "timestamp": datetime.now().isoformat(),
        "wall_time_min": round(run_elapsed / 60, 2),
        "skill_type": skill_type,
        "model": model,
        "parallel": parallel,
        "total_papers": len(papers),
        "topics_generated": len(index["topics"]),
        "dimensions_generated": len(index["dimensions"]),
        "calibration_generated": len(index["calibration"]),
        "keywords_mapped": len(index["keyword_to_topic"]),
    }
    summary_path = LOG_DIR / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_skill_gen_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"\nDone! Total time: {run_elapsed/60:.1f} min")
    print(f"  Summary: {summary_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate skill library from review corpus")
    parser.add_argument("--type", choices=["all", "topics", "dimensions", "calibration"],
                        default="all", help="Which skill type to generate")
    parser.add_argument("--stats-only", action="store_true",
                        help="Only compute statistics, skip LLM synthesis")
    parser.add_argument("--parallel", type=int, default=2,
                        help="Number of parallel Claude sessions for topic skills")
    parser.add_argument("--model", type=str, default="sonnet",
                        help="Claude model to use (default: sonnet)")
    parser.add_argument("--timeout", type=int, default=1800,
                        help="Timeout per Claude session in seconds (default: 1800)")
    args = parser.parse_args()

    run(skill_type=args.type, stats_only=args.stats_only,
        parallel=args.parallel, model=args.model, timeout=args.timeout)


if __name__ == "__main__":
    main()
