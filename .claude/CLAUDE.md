# IdeaForge

AI-powered research idea generation through adversarial multi-agent debate.

## Quick Reference

```bash
python ideaforge.py --check                           # verify setup
python ideaforge.py --run --domain "your area"        # generate ideas
python ideaforge.py                                   # crawl ~1K papers
python ideaforge.py --full                             # crawl all ~50K papers
```

## Architecture

- **ideaforge.py** — single entry point for setup, verification, and running the refiner
- **idea_refiner/adversarial_refiner.py** — 3-agent debate system (Critic, Proposer, Judge)
  - Spawns Claude Code sessions via `claude -p --dangerously-skip-permissions`
  - Each agent is a stateful session resumed with `claude -r <session-id>`
- **judge_training/** — GEPA judge training pipeline
  - `optimize.py` — prompt evolution (Stage 1: Sonnet, Stage 2: Opus)
  - `embedding_index.py` — FAISS index builder + query interface
  - `eval_harness.py` — evaluation against real reviewer scores
  - `skills/` — 26 skill files loaded dynamically by the judge
  - `embeddings/` — pre-built 50K-paper FAISS index (Git LFS)
  - `output/best_judge_prompt.md` — GEPA-optimized judge prompt
- **data_pipeline/** — OpenReview crawlers for ICLR
- **crawl_neurips.py**, **crawl_icml.py** — venue-specific crawlers

## Key Patterns

- All generated data goes to `resources/` (configurable via `IDEAFORGE_RESOURCES_DIR` env var or `--resources-dir`)
- The FAISS index and judge prompt ship with the repo — no setup needed to generate ideas
- `embedding_index.py` auto-resolves: user-built index in `resources/` > shipped index in `judge_training/embeddings/`
- Encoding: always use `encoding="utf-8"` with `open()` (Windows defaults to cp1252)

## Testing

```bash
python ideaforge.py --test    # synthetic data, verifies downstream pipeline
python ideaforge.py --check   # verify all components are present
```
