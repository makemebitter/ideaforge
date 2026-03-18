"""
Adversarial Research Idea Refiner

Three AI agents (Critic, Proposer, Judge) debate in persistent Claude sessions
to refine research ideas.
"""

from .adversarial_refiner import (
    adversarial_refinement,
    run_claude_create,
    run_claude_resume,
    run_claude_oneshot,
    extract_ideas_from_markdown,
    RefinementSession,
)

__all__ = [
    "adversarial_refinement",
    "run_claude_create",
    "run_claude_resume",
    "run_claude_oneshot",
    "extract_ideas_from_markdown",
    "RefinementSession",
]
