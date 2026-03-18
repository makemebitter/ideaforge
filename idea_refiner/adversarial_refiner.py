"""
Adversarial Research Idea Refiner — Three-Agent Stateful Architecture

Three AI agents debate in persistent Claude Code sessions:
- CRITIC: Finds flaws, searches for prior work, challenges assumptions
- PROPOSER: Can DEFEND, PIVOT, or REPROPOSE entirely based on criticisms
- JUDGE: Evaluates each round, scores the idea, guides the next round

Each agent runs as a separate stateful Claude session with a fixed system prompt
set once.  Subsequent rounds send only short turn messages via `claude -r`.

RESUMABILITY: State is checkpointed after every phase. If the process crashes,
resume from the last checkpoint with --resume.

Usage:
    python adversarial_refiner.py --idea 1 --rounds 10
    python adversarial_refiner.py --idea 1 --rounds 10 --domain "video generation"
    python adversarial_refiner.py --idea 1 --rounds 10 --phase refine

Two-phase workflow:
    # Phase 1: Explore broadly (allows REPROPOSE)
    python adversarial_refiner.py --idea 1 --rounds 10 --domain "video generation"
    # Phase 2: Deep refine (DEFEND/PIVOT only)
    python adversarial_refiner.py --resume refinements/exp_xxx/session.pkl --rounds 20 --phase refine

Resume from crash:
    python adversarial_refiner.py --resume refinements/exp_xxx/session.pkl

Start from scratch (agent proposes initial idea, then debate):
    python adversarial_refiner.py --from-scratch --domain "video generation" --rounds 5
"""

import subprocess
import json
import argparse
import re
import os
import sys
import pickle
import functools
import uuid
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field, asdict

# Force unbuffered stdout so output appears immediately in Cursor terminal
print = functools.partial(print, flush=True)  # type: ignore


@dataclass
class RefinementSession:
    """
    Checkpointable session for adversarial idea refinement.
    
    All state is stored in this object and can be saved/loaded for resumability.
    """
    # Configuration
    original_idea: str = ""
    idea_num: Optional[int] = None
    idea_title: Optional[str] = None
    total_rounds: int = 2
    domain: str = ""  # e.g. "video generation" - constrains proposals to this domain
    refinement_phase: str = "explore"  # "explore" (allow REPROPOSE) or "refine" (DEFEND/PIVOT only)
    seed_paper: str = ""  # arxiv ID or title of seed paper to ground idea generation
    seed_paper_content: str = ""  # fetched abstract/content of seed paper
    target_venues: str = ""  # comma-separated venue names, e.g. "ICML,NeurIPS,ICLR"
    
    # State
    current_idea: str = ""
    current_round: int = 0
    current_phase: str = "init"  # init, critic, proposer, synthesis, complete
    history: List[str] = field(default_factory=list)
    
    # Results per round
    round_results: Dict[int, Dict[str, str]] = field(default_factory=dict)
    
    # Evolution tracking: list of {round, action, title, summary}
    evolution_path: List[Dict[str, str]] = field(default_factory=list)
    
    # Final output
    final_idea: Optional[str] = None
    evolution_type: Optional[str] = None  # REFINED, PIVOTED, REPROPOSED
    
    # Metadata
    experiment_id: str = ""
    experiment_dir: str = ""
    started_at: str = ""
    completed_at: Optional[str] = None
    status: str = "initialized"  # initialized, in_progress, complete, failed

    # Claude Code stateful sessions (separate per role) - used with -r to resume
    critic_session_id: Optional[str] = None
    proposer_session_id: Optional[str] = None
    judge_session_id: Optional[str] = None

    # Critic rotation: replace the critic with a fresh independent one when the
    # judge's score crosses a threshold, ensuring the idea survives scrutiny from
    # multiple independent reviewers rather than one that gets gradually convinced.
    critic_replace_threshold: float = 8.0
    min_independent_critics: int = 3
    critic_rotation_count: int = 0  # how many independent critics have been used
    critic_rotation_rounds: List[int] = field(default_factory=list)  # rounds where rotation happened
    critic_is_fresh: bool = True  # whether the current critic needs create (True) vs resume (False)
    judge_is_fresh: bool = False  # whether the judge needs create (True) vs resume (False); starts False because round 0 creates it

    # Tournament mode: generate N candidate ideas, quick-score them, debate the best
    tournament_size: int = 1  # number of candidate ideas to generate (1 = no tournament)
    tournament_scores: Dict[int, float] = field(default_factory=dict)  # {candidate_idx: score}
    tournament_ideas: List[str] = field(default_factory=list)  # all candidate ideas
    tournament_titles: List[str] = field(default_factory=list)  # titles for each candidate

    # Early kill: force repropose if score < threshold after N rounds
    early_kill_threshold: float = 7.0  # minimum score after early_kill_rounds
    early_kill_rounds: int = 3  # check score after this many rounds

    # Score plateau detection: force repropose if no improvement for N consecutive rounds
    plateau_patience: int = 2  # number of rounds without improvement before forcing repropose

    # Repropose budget: maximum number of full reproposals allowed
    max_reproposals: int = 3  # allow up to N full reproposals before settling
    reproposal_count: int = 0  # how many reproposals have been used so far
    last_repropose_round: int = 0  # round number of last reproposal (for resetting early kill)

    # Internal: pending force-repropose message for next proposer turn
    _pending_force_repropose: str = ""

    def __post_init__(self):
        """Initialize timestamps if not set."""
        if not self.started_at:
            self.started_at = datetime.now().isoformat()
        if not self.current_idea:
            self.current_idea = self.original_idea
    
    def save(self, filepath: Optional[str] = None) -> str:
        """Save session to checkpoint file."""
        if filepath is None:
            if self.experiment_dir:
                filepath = str(Path(self.experiment_dir) / "session.pkl")
            else:
                filepath = f"session_{self.experiment_id}.pkl"
        
        with open(filepath, 'wb') as f:
            pickle.dump(self, f)
        
        # Also save as JSON for human readability
        json_path = filepath.replace('.pkl', '.json')
        self._save_json(json_path)
        
        # Save evolution path
        self.save_evolution()
        
        return filepath
    
    def _save_json(self, filepath: str) -> None:
        """Save human-readable JSON version (for inspection)."""
        data = {
            "experiment_id": self.experiment_id,
            "idea_num": self.idea_num,
            "idea_title": self.idea_title,
            "total_rounds": self.total_rounds,
            "current_round": self.current_round,
            "current_phase": self.current_phase,
            "status": self.status,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "evolution_type": self.evolution_type,
            "history_length": len(self.history),
            "rounds_completed": list(self.round_results.keys()),
            "evolution_path": self.evolution_path,
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load(cls, filepath: str) -> 'RefinementSession':
        """Load session from checkpoint file."""
        session = None
        with open(filepath, 'rb') as f:
            session = pickle.load(f)
        # Backward compatibility with old checkpoints
        if not hasattr(session, 'evolution_path'):
            session.evolution_path = []
        if not hasattr(session, 'domain'):
            session.domain = ""
        if not hasattr(session, 'refinement_phase'):
            session.refinement_phase = "explore"
        if not hasattr(session, 'critic_session_id'):
            session.critic_session_id = None
        if not hasattr(session, 'proposer_session_id'):
            session.proposer_session_id = None
        if not hasattr(session, 'judge_session_id'):
            session.judge_session_id = None
        if not hasattr(session, 'critic_replace_threshold'):
            session.critic_replace_threshold = 8.0
        if not hasattr(session, 'min_independent_critics'):
            session.min_independent_critics = 3
        if not hasattr(session, 'critic_rotation_count'):
            session.critic_rotation_count = 0
        if not hasattr(session, 'critic_rotation_rounds'):
            session.critic_rotation_rounds = []
        if not hasattr(session, 'critic_is_fresh'):
            session.critic_is_fresh = True
        if not hasattr(session, 'judge_is_fresh'):
            session.judge_is_fresh = False
        return session
    
    def record_proposer(self, round_num: int, response: str) -> None:
        """Record proposer output for a round."""
        if round_num not in self.round_results:
            self.round_results[round_num] = {}
        self.round_results[round_num]['proposer'] = response
        self.history.append(f"## Round {round_num} - PROPOSER\n\n{response}")
        self.current_phase = "proposer"
        
        # Extract the new idea for next round - try multiple header patterns
        self.current_idea = self._extract_current_idea(response)
        
        # Detect evolution type
        if "REPROPOSE" in response.upper():
            self.evolution_type = "REPROPOSED"
        elif "PIVOT" in response.upper():
            self.evolution_type = "PIVOTED"
        else:
            self.evolution_type = "REFINED"
        
        # Track evolution: extract title and build summary
        title = self._extract_title(response)
        summary = self._extract_summary(response)
        action = self.evolution_type or "REFINED"
        self.evolution_path.append({
            "round": round_num,
            "action": action,
            "title": title,
            "summary": summary,
        })
    
    def record_critic(self, round_num: int, critique: str) -> None:
        """Record critic output for a round."""
        if round_num not in self.round_results:
            self.round_results[round_num] = {}
        self.round_results[round_num]['critic'] = critique
        self.history.append(f"## Round {round_num} - CRITIC\n\n{critique}")
        self.current_round = round_num
        self.current_phase = "critic"
        self.status = "in_progress"
        
        # Track critic verdict in evolution
        verdict = self._extract_critic_verdict(critique)
        self.evolution_path.append({
            "round": round_num,
            "action": "CRITIC",
            "title": f"Round {round_num} Critique",
            "summary": verdict,
        })
    
    def _extract_current_idea(self, response: str) -> str:
        """Extract the current idea from a proposer response for next round's critic.
        
        Tries multiple header patterns since agents use inconsistent formatting.
        Falls back to using the full response if no structured section is found.
        """
        # Skip error/timeout responses
        if len(response) < 200 or _is_agent_error(response):
            return self.current_idea
        
        # Try structured section headers (most specific first)
        section_markers = [
            "## Proposed Idea",
            "## Refined Idea",
            "## NEW IDEA:",
            "## NEW IDEA",
            "## REPROPOSED IDEA",
            "## Final Proposal",
            "## Proposed Research",
            "## Updated Idea",
        ]
        
        for marker in section_markers:
            if marker in response:
                extracted = response.split(marker, 1)[-1].strip()
                if len(extracted) > 100:
                    return f"{marker}\n{extracted}"
        
        # Try to extract from "### Title" onward (common in well-formatted responses)
        title_match = re.search(r'(###\s*Title\s*\n.+)', response, re.DOTALL)
        if title_match and len(title_match.group(1)) > 100:
            return title_match.group(1).strip()
        
        # If it's a REPROPOSE/PIVOT, use everything after the decision line
        for decision_marker in ["Decision: REPROPOSE", "Decision: PIVOT", "DECISION: REPROPOSE", "DECISION: PIVOT"]:
            if decision_marker in response:
                after_decision = response.split(decision_marker, 1)[-1].strip()
                if len(after_decision) > 200:
                    return after_decision[:5000]
        
        # Last resort: if response is substantive, use the whole thing
        # but strip agent meta-commentary (lines like "I've created..." or "Perfect!")
        if len(response) > 500:
            lines = response.split('\n')
            # Skip leading meta-commentary lines
            start = 0
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith('#') or stripped.startswith('**') or stripped.startswith('- ') or stripped.startswith('|'):
                    start = i
                    break
                if len(stripped) > 0 and not any(stripped.startswith(p) for p in [
                    "I've ", "Perfect", "Excellent", "Now ", "Let me", "Based on",
                    "The response", "Here's", "Agent ", "---", "node.exe"
                ]):
                    start = i
                    break
            cleaned = '\n'.join(lines[start:])
            if len(cleaned) > 200:
                return cleaned[:5000]
            return response[:5000]
        
        return self.current_idea
    
    def _extract_title(self, response: str) -> str:
        """Extract the idea title from a proposer response."""
        # Look for common title patterns in proposer output
        for pattern in [
            # "## NEW IDEA: **Title**" or "## Proposed Idea: **Title**"
            r'##\s*(?:NEW IDEA|Proposed Idea|REPROPOSED IDEA)[:\s]*\*\*(.+?)\*\*',
            # "### Title\n**Title Text**" or "### Title\nTitle Text"
            r'###\s*Title\s*\n+\*?\*?(.+?)(?:\*?\*?)?\s*$',
            # "**Title:** Something" or "**Title**: Something"  
            r'\*\*Title\*?\*?[:\s]+(.+?)(?:\*?\*?)?\s*$',
            # "**AdapTok: Full Title Here**" after Proposed Idea section
            r'(?:Proposed Idea|NEW IDEA)[\s\S]{0,200}\*\*([A-Z][^*]{10,100})\*\*',
        ]:
            match = re.search(pattern, response, re.MULTILINE)
            if match:
                title = match.group(1).strip().strip('*').strip()
                if 10 < len(title) < 200:
                    return title
        
        # Fallback: look for first bold text after "NEW IDEA" or "Proposed Idea"
        for section in ["NEW IDEA", "Proposed Idea", "REPROPOSED IDEA"]:
            if section in response:
                after = response.split(section, 1)[-1][:800]
                bold_match = re.search(r'\*\*([A-Z][^*]{10,120}?)\*\*', after)
                if bold_match:
                    return bold_match.group(1).strip()
        
        # Last resort: look for any bold text that looks like a title (starts with capital, 10+ chars)
        bold_matches = re.findall(r'\*\*([A-Z][^*]{10,120}?)\*\*', response[:2000])
        for candidate in bold_matches:
            candidate = candidate.strip()
            # Skip common non-title patterns
            skip_words = ["DEFEND", "PIVOT", "REPROPOSE", "FATAL", "CRITICAL", "Problem", "Why", "How"]
            if not any(candidate.startswith(w) for w in skip_words):
                return candidate
        
        return f"Round {self.current_round} proposal"
    
    def _extract_summary(self, response: str) -> str:
        """Extract a short summary from a proposer response."""
        # Look for key insight or problem statement
        for pattern in [
            r'###?\s*Key Insight\s*\n+(.+?)(?:\n\n|\n###)',
            r'###?\s*Problem\s*\n+(.+?)(?:\n\n|\n###)',
            r'###?\s*Core Idea\s*\n+(.+?)(?:\n\n|\n###)',
        ]:
            match = re.search(pattern, response, re.DOTALL)
            if match:
                text = match.group(1).strip()
                # Take first sentence or first 200 chars
                first_sentence = re.split(r'(?<=[.!?])\s', text)[0]
                if len(first_sentence) > 200:
                    first_sentence = first_sentence[:200] + "..."
                return first_sentence
        
        # Fallback: first meaningful paragraph after decision
        for marker in ["## Proposed Idea", "## Decision", "REPROPOSE", "DEFEND"]:
            if marker in response:
                after = response.split(marker, 1)[-1].strip()
                paragraphs = [p.strip() for p in after.split('\n\n') if p.strip() and len(p.strip()) > 30]
                if paragraphs:
                    text = paragraphs[0][:200]
                    if len(paragraphs[0]) > 200:
                        text += "..."
                    return text
        
        return "See full proposer response for details."
    
    def _extract_critic_verdict(self, critique: str) -> str:
        """Extract the critic's bottom-line verdict."""
        # Look for Summary Verdict, Bottom Line, or Recommendation sections
        for pattern in [
            r'##\s*(?:Summary\s*)?Verdict\s*\n+([\s\S]+?)(?:\n##|\Z)',
            r'##\s*Bottom Line\s*\n+([\s\S]+?)(?:\n##|\Z)',
            r'\*\*Recommendation\*?\*?:\s*(.+?)(?:\n\n|\Z)',
        ]:
            match = re.search(pattern, critique, re.MULTILINE)
            if match:
                text = match.group(1).strip()
                # Take first 2 lines or 200 chars
                lines = [l.strip() for l in text.split('\n') if l.strip()][:2]
                result = ' '.join(lines)
                if len(result) > 250:
                    result = result[:250] + "..."
                return result
        
        # Fallback: look for rating prediction
        rating_match = re.search(r'(?:Rating|Expected).*?(\d+\.?\d*\s*[-/]\s*\d+\.?\d*)', critique)
        if rating_match:
            return f"Predicted rating: {rating_match.group(1)}"
        
        return "See full critique for details."
    
    def save_evolution(self, exp_dir: Optional[str] = None) -> None:
        """Save evolution.md showing the idea's journey."""
        if exp_dir is None:
            exp_dir = self.experiment_dir
        if not exp_dir:
            return
        
        lines = [
            "# Idea Evolution Path\n",
            f"**Experiment:** {self.experiment_id}",
            f"**Started:** {self.started_at}",
            f"**Status:** {self.status}",
            f"**Original Idea:** {self.idea_title or '(untitled)'}",
            "",
            "---\n",
        ]
        
        # Add original idea entry
        lines.append(f"## Starting Point")
        lines.append(f"**Title:** {self.idea_title or '(untitled)'}")
        orig_preview = self.original_idea[:300].replace('\n', ' ')
        if len(self.original_idea) > 300:
            orig_preview += "..."
        lines.append(f"**Summary:** {orig_preview}")
        lines.append("")
        lines.append("---\n")
        
        # Add each evolution step
        for entry in self.evolution_path:
            round_num = entry.get("round", "?")
            action = entry.get("action", "UNKNOWN")
            title = entry.get("title", "Untitled")
            summary = entry.get("summary", "No summary")
            
            if action == "CRITIC":
                lines.append(f"## Round {round_num} - CRITIC")
                lines.append(f"**Verdict:** {summary}")
            elif action == "JUDGE":
                lines.append(f"## Round {round_num} - JUDGE")
                lines.append(f"**Assessment:** {summary}")
            else:
                emoji_map = {"REPROPOSED": "[REPROPOSE]", "PIVOTED": "[PIVOT]", "REFINED": "[DEFEND]"}
                tag = emoji_map.get(action, f"[{action}]")
                lines.append(f"## Round {round_num} - PROPOSER {tag}")
                lines.append(f"**Title:** {title}")
                lines.append(f"**Summary:** {summary}")
            
            lines.append("")
            lines.append("---\n")
        
        # Add final idea if available
        if self.final_idea:
            lines.append("## FINAL IDEA")
            lines.append(f"**Evolution type:** {self.evolution_type or 'REFINED'}")
            final_preview = self.final_idea[:500].replace('\n', ' ')
            if len(self.final_idea) > 500:
                final_preview += "..."
            lines.append(f"**Summary:** {final_preview}")
            lines.append("")
        
        content = '\n'.join(lines)
        Path(exp_dir, "evolution.md").write_text(content, encoding="utf-8")
    
    def record_synthesis(self, synthesis: str) -> None:
        """Record final synthesis."""
        self.final_idea = synthesis
        self.current_phase = "synthesis"
        self.status = "complete"
        self.completed_at = datetime.now().isoformat()
    
    def get_resume_point(self) -> tuple:
        """Get the point to resume from: (round_num, phase)."""
        if self.status == "complete":
            return (self.total_rounds + 1, "complete")
        return (self.current_round, self.current_phase)
    
    def needs_critic(self, round_num: int) -> bool:
        """Check if this round needs critic phase."""
        return round_num not in self.round_results or 'critic' not in self.round_results.get(round_num, {})
    
    def needs_proposer(self, round_num: int) -> bool:
        """Check if this round needs proposer phase."""
        return round_num not in self.round_results or 'proposer' not in self.round_results.get(round_num, {})
    
    def needs_judge(self, round_num: int) -> bool:
        """Check if this round needs judge phase."""
        return round_num not in self.round_results or 'judge' not in self.round_results.get(round_num, {})

    def record_judge(self, round_num: int, judgement: str) -> None:
        """Record judge output for a round."""
        if round_num not in self.round_results:
            self.round_results[round_num] = {}
        self.round_results[round_num]['judge'] = judgement
        self.history.append(f"## Round {round_num} - JUDGE\n\n{judgement}")
        self.current_phase = "judge"

        score = self._extract_judge_score(judgement)
        direction = self._extract_judge_direction(judgement)
        self.evolution_path.append({
            "round": round_num,
            "action": "JUDGE",
            "title": f"Round {round_num} Judgement",
            "summary": f"Score: {score}/10 | Direction: {direction}",
        })

    def _extract_judge_score(self, judgement: str) -> str:
        """Extract numeric score from judge output.

        Tries multiple patterns, returning the earliest match to avoid
        picking up historical score references (e.g. "R0 score 5/10")
        that appear later in the text.
        """
        candidates = []
        # Pattern 1: "### Score" section header followed by X/10
        m = re.search(r'###\s*Score.*?(\d+(?:\.\d+)?)\s*/\s*10', judgement, re.IGNORECASE | re.DOTALL)
        if m:
            candidates.append((m.start(), m.group(1)))
        # Pattern 2: "Score:" or "Rating:" at start of line
        m = re.search(r'^(?:Score|Rating)[:\s]*\**(\d+(?:\.\d+)?)\s*/\s*10', judgement, re.IGNORECASE | re.MULTILINE)
        if m:
            candidates.append((m.start(), m.group(1)))
        # Pattern 3: bold or plain X/10 (first occurrence)
        m = re.search(r'\**(\d+(?:\.\d+)?)\s*/\s*10\**', judgement)
        if m:
            candidates.append((m.start(), m.group(1)))
        if candidates:
            # Return the earliest match in the text
            candidates.sort(key=lambda x: x[0])
            return candidates[0][1]
        return "?"

    def _extract_judge_direction(self, judgement: str) -> str:
        """Extract direction signal from judge output."""
        for keyword in ["KEEP REFINING", "PIVOT", "EXPLORE NEW", "CONVERGING", "READY"]:
            if keyword in judgement.upper():
                return keyword.title()
        match = re.search(r'##\s*Direction\s*\n+(.+?)(?:\n##|\n\n|\Z)', judgement, re.MULTILINE)
        if match:
            text = match.group(1).strip()
            return text[:80] if len(text) > 80 else text
        return "See judgement"

    def get_judge_score_numeric(self, round_num: int) -> Optional[float]:
        """Get the judge's numeric score for a given round, or None if unavailable."""
        if round_num not in self.round_results:
            return None
        judgement = self.round_results[round_num].get('judge', '')
        if not judgement:
            return None
        score_str = self._extract_judge_score(judgement)
        if score_str == "?":
            return None
        try:
            return float(score_str)
        except ValueError:
            return None

    def rotate_critic(self) -> str:
        """Replace the current critic AND judge with fresh independent ones.

        The judge is also replaced to prevent score anchoring — a judge that
        has watched the idea evolve over many rounds will be biased toward
        the score trajectory it established. A fresh judge evaluates the
        idea on its own merits.

        Returns the new critic session ID.
        """
        self.critic_session_id = str(uuid.uuid4())
        self.judge_session_id = str(uuid.uuid4())
        self.judge_is_fresh = True
        self.critic_rotation_count += 1
        return self.critic_session_id

    def needs_initial_judge(self) -> bool:
        """Check if the Round 0 (initial baseline) judge assessment is needed."""
        return 0 not in self.round_results or 'judge' not in self.round_results.get(0, {})

    def needs_synthesis(self) -> bool:
        """Check if synthesis is needed."""
        return self.final_idea is None and self.current_round >= self.total_rounds


def safe_print(text: str) -> None:
    """Print text safely, handling Unicode characters on Windows."""
    try:
        print(text, flush=True)
    except UnicodeEncodeError:
        # Replace non-ASCII characters with ? for Windows terminals
        safe_text = text.encode('ascii', 'replace').decode('ascii')
        print(safe_text, flush=True)


# ---------------------------------------------------------------------------
# Claude Code CLI backend
# ---------------------------------------------------------------------------

_CLAUDE_EXE: Optional[str] = None


def _get_claude_exe() -> str:
    """Locate the claude executable (cached)."""
    global _CLAUDE_EXE
    if _CLAUDE_EXE is None:
        import shutil
        found = shutil.which("claude")
        if found:
            _CLAUDE_EXE = found
        else:
            for p in [
                Path.home() / ".local" / "bin" / "claude.exe",
                Path.home() / ".local" / "bin" / "claude",
            ]:
                if p.exists():
                    _CLAUDE_EXE = str(p)
                    break
            else:
                _CLAUDE_EXE = "claude"
    return _CLAUDE_EXE


def _run_subprocess(cmd: list[str], timeout: int, cwd: Optional[str] = None) -> str:
    """Run a command, capture stdout, return it.

    *cwd* pins the working directory so that Claude CLI resolves session
    files from a consistent project path regardless of where the script
    was launched from.
    """
    try:
        # Strip env vars that trigger Claude Code's nested-session check
        child_env = {k: v for k, v in os.environ.items()
                     if k not in ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT", "CLAUDE_AGENT_SDK_VERSION")}
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.DEVNULL,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
            cwd=cwd,
            env=child_env,
        )
        output = result.stdout.strip()

        if not output and result.stderr:
            stderr = result.stderr.strip()
            if "usage limit" in stderr.lower():
                return f"Agent hit usage limit: {stderr[:300]}"
            return f"Agent error (stderr): {stderr[:500]}"

        if not output:
            if result.returncode in (137, 143):  # SIGKILL (128+9), SIGTERM (128+15)
                return "Agent timed out - the query may be too complex. Try increasing timeout or simplifying the prompt."
            return f"Agent returned empty output (exit code: {result.returncode})"

        return output

    except subprocess.TimeoutExpired:
        return "Agent timed out - the query may be too complex. Try increasing timeout or simplifying the prompt."
    except FileNotFoundError as e:
        return f"Error: claude executable not found - {e}"
    except Exception as e:
        return f"Agent error: {str(e)}"


def _write_turn_file(exp_dir: Optional[Path], label: str, content: str) -> Path:
    """Write turn content to a file in exp_dir and return the path.

    Falls back to a temp file if no exp_dir is available.
    """
    if exp_dir:
        path = exp_dir / f"_turn_{label}.md"
    else:
        import tempfile as _tf
        fd, tmp = _tf.mkstemp(suffix=".md", prefix=f"turn_{label}_")
        os.close(fd)
        path = Path(tmp)
    path.write_text(content, encoding="utf-8")
    return path


def _file_ref(path: Path) -> str:
    """Short CLI message telling Claude to read a file."""
    return f'Read your full task and context from the file at "{path.resolve()}". Respond based on it.'


def run_claude_create(
    session_id: str,
    system_prompt: str,
    turn_message: str,
    timeout: int = 1800,
    model: str = "sonnet",
    exp_dir: Optional[Path] = None,
    label: str = "create",
    cwd: Optional[str] = None,
) -> str:
    """Start a new Claude session.

    The turn message is always written to a file to avoid CLI length limits.
    System prompt is passed via --append-system-prompt (keeps default tools).
    """
    turn_file = _write_turn_file(exp_dir, label, turn_message)
    exe = _get_claude_exe()
    cmd = [
        exe, "-p",
        "--dangerously-skip-permissions",
        "--model", model,
        "--session-id", session_id,
        "--append-system-prompt", system_prompt,
        _file_ref(turn_file),
    ]
    return _run_subprocess(cmd, timeout, cwd=cwd)


def run_claude_resume(
    session_id: str,
    turn_message: str,
    timeout: int = 1800,
    model: str = "sonnet",
    exp_dir: Optional[Path] = None,
    label: str = "resume",
    cwd: Optional[str] = None,
) -> str:
    """Resume an existing Claude session.

    The turn message is always written to a file to avoid CLI length limits.
    """
    turn_file = _write_turn_file(exp_dir, label, turn_message)
    exe = _get_claude_exe()
    cmd = [
        exe, "-p",
        "--dangerously-skip-permissions",
        "--model", model,
        "-r", session_id,
        _file_ref(turn_file),
    ]
    return _run_subprocess(cmd, timeout, cwd=cwd)


def run_claude_oneshot(
    prompt: str,
    timeout: int = 1800,
    model: str = "sonnet",
    exp_dir: Optional[Path] = None,
    label: str = "oneshot",
    cwd: Optional[str] = None,
) -> str:
    """Run a single non-session Claude call (scratch idea gen, etc.).

    The prompt is always written to a file to avoid CLI length limits.
    """
    turn_file = _write_turn_file(exp_dir, label, prompt)
    exe = _get_claude_exe()
    cmd = [
        exe, "-p",
        "--dangerously-skip-permissions",
        "--model", model,
        _file_ref(turn_file),
    ]
    return _run_subprocess(cmd, timeout, cwd=cwd)


# ---------------------------------------------------------------------------
# Tournament mode: generate N ideas, quick-score, debate the best
# ---------------------------------------------------------------------------

_QUICK_SCORE_PROMPT = """You are a research idea QUICK SCORER.

Score this research idea from 1-10 on its potential to become a top-venue (ICML/NeurIPS/ICLR) paper.

Consider:
- Novelty: Is this genuinely new or incremental/crowded?
- Feasibility: Can a solo researcher do this for < $5K?
- Impact: Would this change how people think or work?
- Clarity: Is the core insight crisp?

Be HARSH. Most ideas are 4-6. Only truly exceptional ideas get 8+.
A 7 means "solid but incremental." An 8 means "this could be a spotlight paper."

Output ONLY a JSON object:
{"score": <float>, "reasoning": "<2-3 sentences>", "main_risk": "<biggest weakness>"}
"""


def quick_score_idea(idea_text: str, exp_dir: Optional[Path] = None,
                     label: str = "quick_score") -> tuple:
    """Quick-score a single idea. Returns (score, reasoning, raw_response)."""
    prompt = f"{_QUICK_SCORE_PROMPT}\n\n=== IDEA ===\n{idea_text}"
    raw = run_claude_oneshot(prompt, timeout=300, model="sonnet",
                            exp_dir=exp_dir, label=label)
    # Extract JSON from response
    score = 5.0
    reasoning = ""
    try:
        import json as _json
        # Find JSON in response
        match = re.search(r'\{[^}]+\}', raw, re.DOTALL)
        if match:
            data = _json.loads(match.group())
            score = float(data.get("score", 5.0))
            reasoning = data.get("reasoning", "")
    except Exception:
        # Try to extract score from text
        m = re.search(r'(\d+(?:\.\d+)?)\s*/\s*10', raw)
        if m:
            score = float(m.group(1))
    return score, reasoning, raw


def run_tournament(
    domain: str,
    n_candidates: int,
    target_venues: str = "",
    seed_paper: str = "",
    seed_paper_content: str = "",
    frontier_context: str = "",
    exp_dir: Optional[Path] = None,
    verbose: bool = True,
) -> tuple:
    """Generate N candidate ideas, quick-score all, return the best.

    Returns (best_idea_text, best_title, all_ideas, all_scores).
    """
    if verbose:
        print(f"\n{'='*70}")
        print(f"[TOURNAMENT] Generating {n_candidates} candidate ideas")
        print(f"{'='*70}")

    ideas = []
    titles = []
    scores = []

    for i in range(n_candidates):
        if verbose:
            print(f"\n[CANDIDATE {i+1}/{n_candidates}] Generating idea...")

        # Vary the prompt slightly for diversity
        diversity_hint = ""
        if i > 0 and ideas:
            prev_titles = ", ".join(f'"{t}"' for t in titles)
            diversity_hint = f"""
=== DIVERSITY CONSTRAINT ===
The following ideas have ALREADY been proposed. You MUST propose something DIFFERENT:
{prev_titles}

Do NOT propose variations of the above. Find a genuinely different angle, problem, or method.
"""

        prompt = get_scratch_idea_prompt(
            domain,
            target_venues=target_venues,
            seed_paper=seed_paper,
            seed_paper_content=seed_paper_content,
        )
        if diversity_hint:
            prompt = prompt + diversity_hint
        if frontier_context:
            prompt = prompt + f"\n\n=== FRONTIER CONTEXT (underexplored areas) ===\n{frontier_context}"

        raw_idea = run_claude_oneshot(prompt, timeout=1800,
                                     exp_dir=exp_dir, label=f"tournament_idea_{i}")
        # Extract structured idea
        if "## Title" in raw_idea and len(raw_idea) > 200:
            idea_text = raw_idea.split("## Title", 1)[-1].strip()
            if not idea_text.startswith("##"):
                idea_text = "## Title\n" + idea_text
        elif len(raw_idea) > 300 and not _is_agent_error(raw_idea):
            idea_text = raw_idea
        else:
            if verbose:
                print(f"  [SKIP] Candidate {i+1} failed to generate valid idea")
            continue

        # Extract title
        title_match = re.search(r"##\s*Title\s*\n+(.+?)(?:\n##|\n\n|\Z)",
                                idea_text, re.MULTILINE | re.DOTALL)
        title = title_match.group(1).strip()[:80] if title_match else f"Candidate {i+1}"

        ideas.append(idea_text)
        titles.append(title)

        if verbose:
            print(f"  [IDEA] {title}")

    if not ideas:
        raise RuntimeError("Tournament failed: no valid ideas generated")

    # Quick-score all candidates
    if verbose:
        print(f"\n[TOURNAMENT] Quick-scoring {len(ideas)} candidates...")

    for i, (idea, title) in enumerate(zip(ideas, titles)):
        score, reasoning, _ = quick_score_idea(
            idea, exp_dir=exp_dir, label=f"tournament_score_{i}")
        scores.append(score)
        if verbose:
            print(f"  [{i+1}] {score:.1f}/10 — {title}")
            if reasoning:
                print(f"      {reasoning[:120]}")

    # Select the best
    best_idx = max(range(len(scores)), key=lambda i: scores[i])
    if verbose:
        print(f"\n[TOURNAMENT WINNER] #{best_idx+1}: {titles[best_idx]} "
              f"(score: {scores[best_idx]:.1f}/10)")

    return ideas[best_idx], titles[best_idx], ideas, scores


# ---------------------------------------------------------------------------
# Frontier seeding: find underexplored gaps from downloaded papers
# ---------------------------------------------------------------------------

def get_frontier_context(domain: str, exp_dir: Optional[Path] = None,
                         verbose: bool = True) -> str:
    """Analyze recent papers to find underexplored gaps for idea generation.

    Uses the downloaded paper corpus to identify areas with few papers
    but high potential, giving the idea generator better starting points.
    """
    base = Path(__file__).parent.parent / "research_data"

    # Gather paper titles and topics from the corpus for the prompt
    paper_samples = []
    for venue_dir in ["iclr", "icml", "neurips"]:
        venue_path = base / venue_dir
        if not venue_path.exists():
            continue
        for sub in sorted(venue_path.iterdir()):
            if sub.is_dir():
                jsons = list(sub.glob("*.json"))[:3]  # sample 3 per topic
                for f in jsons:
                    try:
                        data = json.loads(f.read_text(encoding="utf-8"))
                        title = data.get("title", "")
                        score = data.get("average_rating", data.get("score", ""))
                        if title:
                            paper_samples.append(f"- [{sub.name}] {title} (score: {score})")
                    except Exception:
                        pass
        if len(paper_samples) > 80:
            break

    if not paper_samples:
        return ""

    sample_text = "\n".join(paper_samples[:80])

    prompt = f"""Analyze these recent ML conference papers and identify UNDEREXPLORED gaps
in the domain of "{domain}" that would make strong research directions.

=== SAMPLE OF RECENT PAPERS ===
{sample_text}

=== YOUR TASK ===
Identify 3-5 specific underexplored research directions that:
1. Are NOT already crowded (few existing papers)
2. Have clear practical impact
3. Are feasible for a solo researcher with < $5K budget
4. Would be novel at ICML/NeurIPS/ICLR

For each direction, explain:
- What gap exists
- Why it's underexplored
- What a paper in this direction might look like

Be specific — not "improve efficiency" but "X specific technique applied to Y specific problem."
Output plain text, no JSON.
"""
    if verbose:
        print(f"[FRONTIER] Analyzing {len(paper_samples)} papers for underexplored gaps...")

    result = run_claude_oneshot(prompt, timeout=600, model="sonnet",
                               exp_dir=exp_dir, label="frontier_analysis")
    if verbose:
        print(f"[FRONTIER] Found underexplored directions ({len(result)} chars)")
    return result


# ---------------------------------------------------------------------------
# System prompts (set once per session) and turn messages (per round)
# ---------------------------------------------------------------------------

_RESOURCES_BLOCK = """=== YOUR RESOURCES ===
**PRIMARY — Use these EXTENSIVELY every round:**
1. **Web search (MANDATORY)**: Search arxiv, Google Scholar, Semantic Scholar, OpenReview
   for EVERY prior work claim. Use multiple search queries with different phrasings.
   Do NOT rely only on local files. The internet has the most up-to-date papers.
2. **Read paper PDFs and abstracts** from URLs you find via web search.

**SUPPLEMENTARY — Local paper databases (may be incomplete/outdated):**
3. **ICLR papers**: `research_data/iclr/iclr_*_with_reviews.csv` — papers with reviews
   - Category PDFs + reviews: `research_data/iclr/<category>/*.pdf` and `*_reviews.json`
4. **NeurIPS papers**: `research_data/neurips/neurips_*_papers.csv` + `<year>/*_reviews.json`
5. **ICML papers**: `research_data/icml/icml_*_papers.csv` + `<year>/*_reviews.json`

IMPORTANT: Local databases may NOT contain the latest papers. Always cross-check
with web search. If an idea pivots or changes direction, you MUST search the web
for prior work on the NEW direction — do not assume prior searches still apply.
"""

_BUDGET_BLOCK = """=== BUDGET CONSTRAINT ===
Solo researcher. Soft cap $1,000, hard cap $5,000.
Prefer: fine-tuning, inference tricks, efficient architectures, pretrained models.
Avoid: training large models from scratch, hundreds of GPUs, massive datasets.
"""


def _domain_block(domain: str) -> str:
    if not domain:
        return ""
    return f"""=== DOMAIN CONSTRAINT ===
All work MUST stay within: **{domain}**. Do NOT drift to unrelated domains.
"""


def _venue_block(target_venues: str) -> str:
    if not target_venues:
        return ""
    venues = [v.strip() for v in target_venues.split(",")]
    venue_str = ", ".join(venues)
    return f"""=== TARGET VENUE CONSTRAINT ===
This paper MUST be publishable at: **{venue_str}**
The idea must be a good fit for the ML/AI research community at these venues.
DO NOT propose ideas that belong in systems venues (OSDI, SOSP, EuroSys, NSDI, ATC, etc.).
The contribution must be primarily about **algorithms, methods, theory, or empirical ML insights** —
not about building/optimizing software systems. Systems-flavored work is fine ONLY if the core
contribution is a new ML method, training/inference algorithm, or scientific finding.
Reviewers at {venue_str} care about: novelty of the method, rigorous experiments with baselines,
ablations, theoretical grounding, and reproducibility. Frame everything accordingly.
"""


def _phase_block(phase: str) -> str:
    if phase != "refine":
        return ""
    return """=== REFINEMENT PHASE ===
DEEP REFINEMENT mode — the idea is already promising.
Focus on making it STRONGER, not killing it. Do NOT recommend abandoning it.
"""


def get_critic_system_prompt(domain: str = "", phase: str = "explore", target_venues: str = "") -> str:
    """Static system prompt for the Critic role — set once at session creation."""
    return f"""You are a HARSH but constructive research critic.

YOUR MISSION: Find flaws, gaps, and weaknesses in research ideas. Be ruthless but fair.
{_domain_block(domain)}{_venue_block(target_venues)}{_phase_block(phase)}{_BUDGET_BLOCK}
{_RESOURCES_BLOCK}
YOUR TASK EACH ROUND:
1. **WEB SEARCH (MANDATORY — do this EVERY round)**:
   - Run at least 3-5 different web searches per round targeting the idea's core claims.
   - Search for: the idea's title keywords, the specific technique, the claimed novelty,
     the domain + "error bounds"/"guarantees"/"certificates" or whatever the approach claims.
   - Check arxiv, OpenReview, Google Scholar, Semantic Scholar.
   - If the idea PIVOTED or REPROPOSED since last round, search for prior work on the
     NEW direction — your previous searches are STALE and may miss critical papers.
2. Read reviewer reviews (*_reviews.json) for similar papers if available locally
3. Identify technical flaws
4. Challenge novelty — cite SPECIFIC papers with URLs
5. Question feasibility for a solo researcher (<$5k)
6. Find missing baselines
7. **NOVELTY AUDIT (MANDATORY — do this EVERY round)**:
   For EACH claimed contribution, apply this test:
   "Could this result be stated using only prior work's numbers/techniques, without
   any new technical content from this paper?"
   If YES → it is NOT a novel contribution. Flag it as **DERIVATIVE** and demand removal.
   Examples of derivative claims: repackaging a baseline's empirical number into a new
   formula, restating a known result with different notation, proving something trivially
   implied by existing work. A paper that merely reframes existing results is unpublishable.
   Be especially suspicious of "guaranteed bounds" or "certified floors" that just plug
   prior work's measurements into a simple formula.

CRITICAL: The #1 failure mode of this debate is missing a published paper that scoops
the idea. The #2 failure mode is letting DERIVATIVE contributions survive because they
are dressed in mathematical notation. Both are fatal. You MUST search the web thoroughly
every round AND audit every contribution for genuine novelty. If you cannot find scooping
work, say so explicitly — don't just skip the search.

OUTPUT FORMAT:
## Prior Work Found (MANDATORY — list what you searched for and found)
[Search queries used. Specific papers with URLs and how they relate.]

## Novelty Audit (MANDATORY)
For EACH claimed contribution, verdict: **NOVEL** or **DERIVATIVE**.
A contribution is DERIVATIVE if it could be stated using only prior work's
numbers, techniques, or trivial reformulations. DERIVATIVE contributions
must be removed — they waste space and invite reviewer rejection.

## Technical Concerns
[Numbered list]

## Novelty Concerns
[What's been done before? Cite specific papers with links.]

## Feasibility Issues (CRITICAL)
[Compute requirements, budget estimate, solo researcher viability]

## Key Questions the Authors Must Answer
[Make-or-break questions]
"""


def get_proposer_system_prompt(domain: str = "", phase: str = "explore", target_venues: str = "") -> str:
    """Static system prompt for the Proposer role — set once at session creation."""
    if phase == "refine":
        options = """You have TWO options each round:
- **DEFEND**: Criticisms are addressable. Fix issues and strengthen.
- **PIVOT**: Core insight is valuable but approach is flawed. Change the method.
Do NOT repropose entirely new ideas in refine mode."""
    else:
        options = """You have THREE options each round:
- **DEFEND**: Criticisms are addressable. Fix issues and strengthen.
- **PIVOT**: Core insight is valuable but approach is flawed. Change the method.
- **REPROPOSE**: Idea is fundamentally broken OR better opportunity exists. Propose NEW idea.
Choose what leads to the BEST publishable research."""

    return f"""You are a research idea PROPOSER responding to a critic's review.

YOUR MISSION: Respond to criticisms and produce the strongest possible idea.

{options}
{_domain_block(domain)}{_venue_block(target_venues)}{_BUDGET_BLOCK}
{_RESOURCES_BLOCK}
IMPORTANT: When you PIVOT or REPROPOSE, you MUST web-search for prior work on your
new direction BEFORE proposing it. Do not propose an idea without first checking if
it already exists. Verify your novelty claims with actual searches.

NOVELTY STANDARD (CRITICAL):
Every claimed contribution MUST pass this test: "Could this result be stated without
any new technical content from this paper?" If yes, DROP IT — it is derivative, not
a contribution. Do NOT defend derivative contributions when the critic flags them.
Instead, either find a genuinely novel angle or remove the claim. Dressing up a prior
work's number in new notation does not make it novel. A paper that follows others'
work without adding substantial new insight is UNPUBLISHABLE at top venues.
If the critic marks a contribution as DERIVATIVE, you must either:
(a) provide a concrete argument for why it requires this paper's new content, OR
(b) drop it from the contributions list.
Never defend a weak contribution just because it is mathematically valid.

OUTPUT FORMAT:
## Assessment of Critiques
[Which are valid? Fatal vs fixable?]

## Decision: [DEFEND / PIVOT / REPROPOSE]
[Why you chose this]

## Supporting Evidence Found
[Papers searched for and found — with URLs. What did you search for?]

## Proposed Idea

### Title
[Paper title]

### Problem
[Problem statement]

### Key Insight
[Core insight]

### Technical Approach
[Concrete method — feasible for solo researcher]

### Compute Budget Estimate
[GPU hours, cost estimate, feasibility]

### Novelty Claim
[What's new — cite the closest related work and explain the gap]

### Why This Will Work
[Evidence-based argument]
"""


def _enrich_with_retrieval(turn_msg: str, idea_text: str) -> str:
    """Add embedding-based retrieval context to a judge turn message."""
    try:
        import sys
        judge_training_dir = str(Path(__file__).parent.parent / "judge_training")
        if judge_training_dir not in sys.path:
            sys.path.insert(0, judge_training_dir)
        import embedding_index
        results = embedding_index.query_index(idea_text[:1000], top_k=7)
        if results:
            context = embedding_index.format_retrieval_context(results)
            print(f"[RETRIEVAL] Injected {len(results)} similar papers into judge context")
            turn_msg = context + "\n\n" + turn_msg
        else:
            print("[RETRIEVAL] No similar papers found")
    except Exception as e:
        print(f"[RETRIEVAL] Failed to enrich with retrieval: {e}")
    return turn_msg


def _build_trained_judge_system_prompt(domain: str = "", phase: str = "explore", target_venues: str = "") -> str:
    """Build judge system prompt using the GEPA-optimized prompt + skill library + retrieval."""
    judge_training_dir = Path(__file__).parent.parent / "judge_training"

    # Load GEPA-optimized prompt if available, else use a calibration-aware default
    optimized_path = judge_training_dir / "output" / "best_judge_prompt.md"
    if optimized_path.exists():
        core_prompt = optimized_path.read_text(encoding="utf-8")
        print(f"[TRAINED JUDGE] Loaded GEPA-optimized prompt ({len(core_prompt)} chars) from {optimized_path}")
    else:
        core_prompt = (
            "You are a calibrated AI conference reviewer trained on thousands of real "
            "peer reviews from ICLR, NeurIPS, and ICML. Evaluate ideas against real "
            "conference standards. Use the skill files and retrieved papers below to "
            "ground your assessment."
        )
        print(f"[TRAINED JUDGE] WARNING: No optimized prompt found at {optimized_path}, using default")

    skills_dir = judge_training_dir / "skills"
    resources = _RESOURCES_BLOCK + f"""

**TRAINED JUDGE RESOURCES (use these for calibrated evaluation):**
5. **Skill library**: Read `{skills_dir / 'index.json'}` to find skill files
   relevant to this paper's topic. Load 1-2 topic skills for domain-specific
   evaluation criteria. These contain real reviewer patterns and scoring rubrics.
6. **Skill files directory**: `{skills_dir}/` — topics/, dimensions/, calibration/
7. **Embedding index for retrieval**: Similar papers have been pre-retrieved and
   injected into your context (see "Similar Published Papers" section below).
"""

    return f"""{core_prompt}

You are judging an adversarial research debate between a Critic and Proposer.
{_domain_block(domain)}{_venue_block(target_venues)}{_phase_block(phase)}{_BUDGET_BLOCK}
{resources}

CRITICAL: You have access to a skill library with real reviewer patterns from
thousands of papers. BEFORE scoring, read the relevant skill file for this
paper's topic area. The skill files contain:
- What reviewers actually praise/criticize in this area
- Required baselines and metrics
- Score distribution and acceptance bar
- Real reviewer quotes at each score level

Your scoring must be CALIBRATED against real conference standards:
- 1-3: Fundamentally flawed or already published
- 4-5: Below average, significant weaknesses
- 6-7: Solid work, above acceptance threshold
- 8-10: Excellent, would be spotlight/oral at top venue

OUTPUT FORMAT:
## Score: [X/10]
## Assessment
[2-3 sentences on debate convergence and idea quality]
## Independent Literature Check
[Your own web searches for prior art]
## Contribution Novelty Gate (MANDATORY)
For EACH contribution: **NOVEL** or **DERIVATIVE** (drop derivatives)
## What the Critic Got Right / Missed
## Guidance for Critic / Proposer (Next Round)
## Direction
[KEEP REFINING | PIVOT SUGGESTED | EXPLORE NEW TERRITORY | CONVERGING]
"""


def get_judge_system_prompt(domain: str = "", phase: str = "explore", target_venues: str = "") -> str:
    """Static system prompt for the Judge role — set once at session creation."""
    return f"""You are a meta-reviewer JUDGE overseeing an adversarial research debate.

Two agents debate: a Critic finds flaws, a Proposer defends/pivots/reproposes.
Your job is to evaluate each round, INDEPENDENTLY verify novelty, and steer the next one.
{_domain_block(domain)}{_venue_block(target_venues)}{_phase_block(phase)}{_BUDGET_BLOCK}
{_RESOURCES_BLOCK}
CRITICAL DUTY 1 — INDEPENDENT LITERATURE VERIFICATION:
You MUST NOT trust the Critic's or Proposer's prior art claims at face value.
Each round, run your OWN web searches to verify:
- Are there papers the Critic missed that scoop the idea?
- Are the Proposer's novelty claims actually true?
- Has anything been published since the debate started that changes the landscape?
Search arxiv, OpenReview, Google Scholar with queries related to the current idea's
core technique and claimed contribution.

CRITICAL DUTY 2 — CONTRIBUTION NOVELTY GATE (EQUALLY IMPORTANT):
For EACH claimed contribution in the current proposal, apply this kill test:
"Could this result be stated using only prior work's numbers, techniques, or
trivial reformulations — WITHOUT any genuinely new technical content from this paper?"
If YES → the contribution is DERIVATIVE. You MUST instruct the proposer to DROP IT.
Do NOT suggest "elevating" or "promoting" derivative results. Do NOT let mathematically
valid but non-novel claims persist as contributions just because they have a formula.
A paper's contributions list must contain ONLY results that REQUIRE this paper's new
ideas to exist. Everything else is background, not contribution.
Examples of derivative claims to REJECT:
- Plugging a baseline's empirical measurement into a new formula
- Restating a known result with different notation
- "Certified bounds" that trivially follow from prior work's numbers
- Speedup floors derived entirely from another paper's head-type statistics
The bar is: would a knowledgeable reviewer say "I could have computed this myself
from [prior work] without reading your paper"? If yes, KILL IT.

OUTPUT FORMAT:
## Score: [X/10]
Rate the current idea's publishability (10 = ready to submit, 1 = fundamentally broken).

## Assessment
[2-3 sentences: Is the debate converging? Is the idea improving?]

## Independent Literature Check
[What did YOU search for? What did you find that neither agent mentioned?
If you found nothing new, say so explicitly with the queries you tried.]

## Contribution Novelty Gate (MANDATORY)
For EACH claimed contribution, verdict: **NOVEL** (requires this paper's ideas) or
**DERIVATIVE** (could be stated from prior work alone). Any DERIVATIVE contribution
must be dropped — instruct the proposer to remove it. Do NOT suggest promoting
derivative results.

## What the Critic Got Right
[Which criticisms were valid and important]

## What the Critic Missed
[Blind spots, unfair criticisms, overlooked strengths, OR papers the critic should have found]

## Guidance for Critic (Next Round)
[What should the critic focus on next? What's the weakest remaining point?
If the idea pivoted, EXPLICITLY tell the critic to re-search for the new direction.]

## Guidance for Proposer (Next Round)
[What should the proposer prioritize? What's the biggest gap to address?]

## Direction
[One of: KEEP REFINING | PIVOT SUGGESTED | EXPLORE NEW TERRITORY | CONVERGING — ALMOST READY]
"""


def get_critic_turn_message(
    current_idea: str,
    round_num: int,
    judge_assessment: str = "",
    last_proposer_action: str = "",
) -> str:
    """Per-round message sent to the Critic session."""
    parts = [f"=== ROUND {round_num} ==="]
    if last_proposer_action and last_proposer_action in ("REPROPOSED", "PIVOTED"):
        parts.append(
            f"\n** ALERT: The Proposer {last_proposer_action} last round -- the idea has "
            f"CHANGED DIRECTION. Your previous prior art searches may be STALE. "
            f"You MUST run NEW web searches targeting the current idea's specific "
            f"technique, claimed novelty, and core keywords. Do NOT rely on prior searches."
        )
    if judge_assessment:
        parts.append(f"\n--- JUDGE'S GUIDANCE FOR YOU (from previous round) ---\n{judge_assessment}")
    parts.append(f"\n--- CURRENT IDEA TO CRITIQUE ---\n{current_idea}")
    parts.append("\nProvide your critique following your output format. Remember: web search is MANDATORY.")
    return "\n".join(parts)


def get_proposer_turn_message(
    original_idea: str,
    current_idea: str,
    critique: str,
    round_num: int,
    judge_assessment: str = "",
) -> str:
    """Per-round message sent to the Proposer session."""
    parts = [f"=== ROUND {round_num} ==="]
    if judge_assessment:
        parts.append(f"\n--- JUDGE'S GUIDANCE FOR YOU (from previous round) ---\n{judge_assessment}")
    parts.append(f"\n--- ORIGINAL IDEA (for reference) ---\n{original_idea}")
    parts.append(f"\n--- CURRENT VERSION ---\n{current_idea}")
    parts.append(f"\n--- LATEST CRITIQUE ---\n{critique}")
    parts.append("\nRespond to the critique following your output format.")
    return "\n".join(parts)


def get_judge_turn_message(
    current_idea: str,
    critique: str,
    proposer_response: str,
    round_num: int,
    total_rounds: int,
) -> str:
    """Per-round message sent to the Judge session."""
    parts = [
        f"=== ROUND {round_num}/{total_rounds} ===",
        f"\n--- CURRENT IDEA ---\n{current_idea}",
        f"\n--- CRITIC'S REVIEW ---\n{critique}",
        f"\n--- PROPOSER'S RESPONSE ---\n{proposer_response}",
        "\nEvaluate this round following your output format.",
    ]
    return "\n".join(parts)


def get_judge_initial_turn_message(idea: str, total_rounds: int) -> str:
    """Round 0 message: Judge scores the raw initial idea before debate begins."""
    return f"""=== ROUND 0/{total_rounds} — INITIAL ASSESSMENT ===

This is the raw initial idea BEFORE any adversarial debate. No critic has reviewed
it yet. Your job is to provide a baseline score so we can measure how much the
debate improves (or changes) the idea.

Use your tools (web search, paper databases) to check novelty and feasibility,
just as the critic will. Score honestly — this baseline anchors the entire debate.

--- INITIAL IDEA ---
{idea}

Evaluate this idea following your output format. For the "What the Critic Got Right"
and "What the Critic Missed" sections, instead provide "Initial Strengths" and
"Initial Weaknesses" since no critique has happened yet. For guidance sections,
describe what the Critic should look for first and what the Proposer should
be prepared to defend.
"""


def _fetch_seed_paper(seed: str) -> str:
    """Fetch seed paper abstract from arxiv. Accepts arxiv ID or title."""
    import urllib.request
    import xml.etree.ElementTree as ET

    # Normalize arxiv ID (strip URL prefix if given)
    arxiv_id = seed.strip()
    for prefix in ["https://arxiv.org/abs/", "http://arxiv.org/abs/",
                    "https://arxiv.org/pdf/", "arxiv:"]:
        if arxiv_id.lower().startswith(prefix):
            arxiv_id = arxiv_id[len(prefix):]
            break

    # If it looks like an arxiv ID, fetch directly
    if re.match(r"^\d{4}\.\d{4,5}(v\d+)?$", arxiv_id):
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    else:
        # Treat as title search
        from urllib.parse import quote
        url = f"http://export.arxiv.org/api/query?search_query=ti:{quote(arxiv_id)}&max_results=1"

    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            xml_data = resp.read().decode("utf-8")
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            return f"[Could not fetch paper: {seed}]"

        title = (entry.findtext("atom:title", "", ns) or "").strip().replace("\n", " ")
        abstract = (entry.findtext("atom:summary", "", ns) or "").strip().replace("\n", " ")
        authors = [a.findtext("atom:name", "", ns) for a in entry.findall("atom:author", ns)]
        author_str = ", ".join(authors[:10])
        if len(authors) > 10:
            author_str += f" et al. ({len(authors)} authors)"

        return f"**Title:** {title}\n**Authors:** {author_str}\n**Abstract:** {abstract}"
    except Exception as e:
        return f"[Could not fetch paper: {seed} — {e}]"


def get_scratch_idea_prompt(domain: str, target_venues: str = "", seed_paper: str = "", seed_paper_content: str = "") -> str:
    """Prompt for generating an initial research idea from scratch or from a seed paper."""
    domain_desc = domain if domain else "machine learning / AI"
    venue_constraint = ""
    if target_venues:
        venues = [v.strip() for v in target_venues.split(",")]
        venue_str = ", ".join(venues)
        venue_constraint = f"""
=== TARGET VENUE ===
This paper MUST be publishable at: **{venue_str}**
The contribution must be primarily about **algorithms, methods, theory, or empirical ML insights**.
DO NOT propose ideas that belong in systems venues (OSDI, SOSP, EuroSys, NSDI, ATC, etc.).
Systems-flavored work is fine ONLY if the core novelty is a new ML method or scientific finding.
"""

    seed_block = ""
    if seed_paper or seed_paper_content:
        seed_block = f"""
=== SEED PAPER ===
Your idea MUST be directly inspired by and build upon this seed paper:
**{seed_paper}**

{seed_paper_content}

Your task: Read this paper carefully (search for the full paper on arxiv if needed),
understand its contributions and limitations, then propose a NOVEL follow-up idea that:
1. Extends, improves, or addresses a limitation of this paper
2. Is clearly differentiated from the seed paper (not just incremental tweaking)
3. Cites and positions itself relative to this paper
4. Searches for OTHER follow-up work on this paper to avoid duplicating existing extensions

Do NOT just re-propose what the seed paper already does. Find a genuine gap or opportunity.
"""

    return f"""You are proposing a NEW research idea{' grounded in a seed paper' if seed_block else ' from scratch'}.

=== YOUR TASK ===
Propose a novel, publishable research idea in the domain of: **{domain_desc}**
{seed_block}{venue_constraint}
Find gaps and opportunities using web search:
1. Do thorough web searches on arxiv/Google Scholar to find recent trends and unsolved problems
2. {'Read the seed paper and its citations/follow-ups thoroughly' if seed_block else 'Once you have a candidate idea, do more searches to check it has not been published'}
3. Search as much as you need — thoroughness is more important than speed

=== CRITICAL CONSTRAINT ===
This is for a SOLO RESEARCHER with LIMITED BUDGET:
- Soft cap: $1,000 | Hard cap: $5,000
- Must be feasible: fine-tuning, inference, efficient methods
- Avoid: training large models from scratch, hundreds of GPUs

=== OUTPUT FORMAT ===
## Title
[Clear, descriptive paper title]

## One-Line Summary
[Single sentence - the key contribution]

## Problem Statement
[What gap or problem does this address? Reference the seed paper if applicable.]

## Key Insight
[The core idea that makes this novel]

## Technical Approach
[Concrete method - must be feasible for solo researcher]

## Feasibility
- Compute: [GPU requirements]
- Data: [What's needed, is it public?]
- Estimated cost: [Under $5k]
"""


_SYNTHESIS_SYSTEM_PROMPT = """You are synthesizing an adversarial debate into a FINAL polished research proposal.

The debate may have resulted in a refined idea, a PIVOT, or a completely NEW idea.
Extract the BEST final idea regardless of how different it is from the original.

Solo researcher constraint: $1K soft cap, $5K hard cap.

OUTPUT FORMAT:
# Final Research Idea

## Evolution Summary
- **Original Idea**: [1 sentence]
- **Final Idea**: [1 sentence]
- **Evolution Type**: [REFINED / PIVOTED / REPROPOSED]
- **Key Pivots**: [list]

## Title
## One-Line Summary
## Problem Statement
## Key Insight
## Technical Approach
## Feasibility Assessment (Compute, Data, Cost, Timeline, Risk)
## Novelty Claims
## Expected Results
## Addressed Concerns
## Remaining Risks
## Related Work to Cite
"""


def write_synthesis_context(exp_dir: Path, original_idea: str, history: list[str]) -> Path:
    """Write the full debate history to a file for the synthesis agent to read."""
    ctx_path = exp_dir / "_synthesis_context.md"
    content = f"""# Synthesis Context

## Original Idea
{original_idea}

## Complete Debate History
{chr(10).join(history)}
"""
    ctx_path.write_text(content, encoding="utf-8")
    return ctx_path


def get_synthesis_turn_message(context_file: Path) -> str:
    """Short turn message pointing the synthesis agent to the context file."""
    return f'Read the complete debate history from "{context_file.resolve()}" and synthesize the FINAL research idea following your output format.'


def _is_agent_error(response: str) -> bool:
    """Check if a response indicates an agent-level failure rather than real output."""
    error_prefixes = ("Agent error", "Agent hit usage limit", "Agent timed out", "Agent returned empty output", "Error:")
    return response.startswith(error_prefixes)


def _call_agent(
    session_id: str,
    system_prompt: str,
    turn_message: str,
    is_first_call: bool,
    timeout: int = 1800,
    model: str = "sonnet",
    exp_dir: Optional[Path] = None,
    label: str = "agent",
    session: Optional['RefinementSession'] = None,
    role: Optional[str] = None,
    cwd: Optional[str] = None,
) -> str:
    """Route to create or resume depending on whether this is the first call.

    If a resume fails because the session was lost (e.g. "No conversation found"),
    automatically fall back to creating a fresh session so the run can continue.
    When *session* and *role* are provided, the new session ID is persisted on
    the session object (role should be "critic", "proposer", or "judge").

    *cwd* is forwarded to the subprocess so that Claude CLI always resolves
    session files from the same project directory.
    """
    if is_first_call:
        response = run_claude_create(session_id, system_prompt, turn_message, timeout, model, exp_dir, label, cwd=cwd)
        # If the session already exists (e.g. crash-resume), fall back to resume
        if _is_agent_error(response) and "already in use" in response.lower():
            safe_print(f"  [RECOVER] Session {session_id[:8]}... already exists, resuming instead")
            response = run_claude_resume(session_id, turn_message, timeout, model, exp_dir, label, cwd=cwd)
        return response

    response = run_claude_resume(session_id, turn_message, timeout, model, exp_dir, label, cwd=cwd)

    # If the session was lost, recover by creating a fresh one with a new ID
    if _is_agent_error(response) and "no conversation found" in response.lower():
        new_id = str(uuid.uuid4())
        safe_print(f"  [RECOVER] Session {session_id[:8]}... lost, creating fresh session {new_id[:8]}...")
        response = run_claude_create(new_id, system_prompt, turn_message, timeout, model, exp_dir, label, cwd=cwd)
        # Persist the new session ID so future rounds resume correctly
        if session is not None and role:
            attr = f"{role}_session_id"
            if hasattr(session, attr):
                setattr(session, attr, new_id)

    return response


def run_refinement_session(
    session: RefinementSession,
    verbose: bool = True,
    use_trained_judge: bool = False,
) -> RefinementSession:
    """
    Run or resume a refinement session with checkpointing.

    Three-agent loop per round: Critic -> Proposer -> Judge.
    Each agent runs as a persistent Claude session.
    """
    exp_dir = Path(session.experiment_dir)

    if verbose:
        resume_point = session.get_resume_point()
        if resume_point[1] != "init" and resume_point[0] > 0:
            print(f"\n{'='*70}")
            print(f"[RESUMING] From round {resume_point[0]}, phase: {resume_point[1]}")
            print(f"{'='*70}")
        else:
            print(f"\n{'='*70}")
            print("[TARGET] ADVERSARIAL RESEARCH IDEA REFINEMENT (3-Agent)")
            print(f"{'='*70}")
        print(f"[EXPERIMENT] {exp_dir.name}")
        if session.domain:
            print(f"[DOMAIN] {session.domain}")
        print(f"[PHASE] {session.refinement_phase.upper()}")
        print(f"\n[IDEA] Original Idea:\n{session.original_idea[:500]}{'...' if len(session.original_idea) > 500 else ''}\n")
        print(f"[BATTLE] Running {session.total_rounds} base rounds (Critic -> Proposer -> Judge)")
        print(f"[CRITICS] Rotating at judge score >= {session.critic_replace_threshold}/10, "
              f"minimum {session.min_independent_critics} independent critics required\n")

    # Build system prompts (only actually sent on session creation)
    critic_sys = get_critic_system_prompt(session.domain, session.refinement_phase, session.target_venues)
    proposer_sys = get_proposer_system_prompt(session.domain, session.refinement_phase, session.target_venues)

    if use_trained_judge:
        judge_sys = _build_trained_judge_system_prompt(
            session.domain, session.refinement_phase, session.target_venues)
        if verbose:
            print("[JUDGE] Using GEPA-trained judge with skill library + retrieval")
    else:
        judge_sys = get_judge_system_prompt(session.domain, session.refinement_phase, session.target_venues)

    # Ensure session IDs exist
    if session.critic_session_id is None:
        session.critic_session_id = str(uuid.uuid4())
    if session.proposer_session_id is None:
        session.proposer_session_id = str(uuid.uuid4())
    if session.judge_session_id is None:
        session.judge_session_id = str(uuid.uuid4())

    # The first critic counts as independent critic #1
    if session.critic_rotation_count == 0:
        session.critic_rotation_count = 1

    # critic_is_fresh is now persisted on the session for correct resume behavior

    # === ROUND 0: BASELINE JUDGE ASSESSMENT ===
    if session.needs_initial_judge():
        if verbose:
            print(f"\n{'='*70}")
            print("[ROUND 0] BASELINE JUDGE ASSESSMENT")
            print(f"{'='*70}")
            print("\n[JUDGE] Scoring raw initial idea before debate begins...")
        turn_msg = get_judge_initial_turn_message(
            session.original_idea, session.total_rounds
        )
        if use_trained_judge:
            turn_msg = _enrich_with_retrieval(turn_msg, session.original_idea)
        baseline = run_claude_create(
            session.judge_session_id, judge_sys, turn_msg, timeout=1800,
            exp_dir=exp_dir, label="r0_judge", cwd=str(exp_dir),
        )
        if _is_agent_error(baseline):
            raise RuntimeError(f"Initial judge failed: {baseline[:200]}")
        session.record_judge(0, baseline)
        save_round_output(exp_dir, 0, "JUDGE_BASELINE", baseline)
        session.save()
        if verbose:
            safe_print(f"\n{baseline}")
    else:
        if verbose:
            print("\n[ROUND 0] Baseline judge already completed (loaded from checkpoint)")

    round_num = 0
    while True:
        round_num += 1

        # Determine if we've passed the base round limit
        past_base_rounds = round_num > session.total_rounds
        enough_critics = session.critic_rotation_count >= session.min_independent_critics

        # Stop condition: past base rounds AND enough independent critics have weighed in
        if past_base_rounds and enough_critics:
            break

        # Hard cap: don't run forever (3x base rounds as absolute maximum)
        if round_num > session.total_rounds * 3:
            if verbose:
                print(f"\n[STOP] Hard cap reached ({session.total_rounds * 3} rounds). "
                      f"Critics used: {session.critic_rotation_count}/{session.min_independent_critics}")
            break

        if verbose:
            critic_tag = f" [Critic #{session.critic_rotation_count}]"
            if past_base_rounds:
                print(f"\n{'='*70}")
                print(f"[ROUND] {round_num} (EXTENDED — need {session.min_independent_critics - session.critic_rotation_count} more independent critic(s)){critic_tag}")
                print(f"{'='*70}")
            else:
                print(f"\n{'='*70}")
                print(f"[ROUND] {round_num}/{session.total_rounds}{critic_tag}")
                print(f"{'='*70}")

        proposer_is_first = (round_num == 1)

        # Previous round's judge assessment (Round 0 baseline for round 1)
        prev_round = round_num - 1
        prev_judge = ""
        if prev_round in session.round_results:
            prev_judge = session.round_results[prev_round].get('judge', '')

        # Detect if the proposer pivoted/reproposed last round
        last_action = ""
        if prev_round > 0 and prev_round in session.round_results:
            prev_proposer = session.round_results[prev_round].get('proposer', '')
            if "REPROPOSE" in prev_proposer.upper():
                last_action = "REPROPOSED"
            elif "PIVOT" in prev_proposer.upper():
                last_action = "PIVOTED"

        # === CRITIC PHASE ===
        if session.needs_critic(round_num):
            if verbose:
                print(f"\n[CRITIC #{session.critic_rotation_count}] Analyzing...")
                if last_action:
                    print(f"  (Proposer {last_action} last round — fresh search triggered)")
                if session.critic_is_fresh and round_num > 1:
                    print(f"  (NEW INDEPENDENT CRITIC — fresh perspective, no prior debate context)")
            # Fresh (rotated) critics get NO judge guidance — they must form
            # their own independent assessment from the idea alone.
            critic_judge_guidance = "" if session.critic_is_fresh else prev_judge
            turn_msg = get_critic_turn_message(
                session.current_idea, round_num, judge_assessment=critic_judge_guidance,
                last_proposer_action=last_action,
            )
            critique = _call_agent(
                session.critic_session_id, critic_sys, turn_msg,
                is_first_call=session.critic_is_fresh,
                exp_dir=exp_dir, label=f"r{round_num}_critic",
                session=session, role="critic", cwd=str(exp_dir),
            )
            if _is_agent_error(critique):
                safe_print(f"  [ERROR] Critic agent failed: {critique[:200]}")
                raise RuntimeError(f"Critic agent failed on round {round_num}: {critique[:200]}")
            session.critic_is_fresh = False  # subsequent calls to this critic use resume
            session.record_critic(round_num, critique)
            save_round_output(exp_dir, round_num, "CRITIC", critique)
            session.save()
            if verbose:
                safe_print(f"\n{critique}")
        else:
            if verbose:
                print("\n[CRITIC] Already completed (loaded from checkpoint)")
            critique = session.round_results[round_num]['critic']

        # === PROPOSER PHASE ===
        if session.needs_proposer(round_num):
            # Check if a forced repropose is pending (from early kill / plateau)
            force_repropose_prefix = ""
            if session._pending_force_repropose:
                force_repropose_prefix = session._pending_force_repropose
                session._pending_force_repropose = ""
                proposer_is_first = True  # fresh proposer session after force repropose
                if verbose:
                    print(f"\n{'-'*50}")
                    print(f"\n[PROPOSER] FORCED REPROPOSE — must propose entirely new idea...")
            else:
                if verbose:
                    options = "DEFEND or PIVOT" if session.refinement_phase == "refine" else "DEFEND, PIVOT, or REPROPOSE"
                    print(f"\n{'-'*50}")
                    print(f"\n[PROPOSER] Responding (can {options})...")
            turn_msg = get_proposer_turn_message(
                session.original_idea, session.current_idea, critique,
                round_num, judge_assessment=prev_judge,
            )
            if force_repropose_prefix:
                turn_msg = force_repropose_prefix + "\n\n" + turn_msg
            response = _call_agent(
                session.proposer_session_id, proposer_sys, turn_msg,
                is_first_call=proposer_is_first,
                exp_dir=exp_dir, label=f"r{round_num}_proposer",
                session=session, role="proposer", cwd=str(exp_dir),
            )
            if _is_agent_error(response):
                safe_print(f"  [ERROR] Proposer agent failed: {response[:200]}")
                raise RuntimeError(f"Proposer agent failed on round {round_num}: {response[:200]}")
            session.record_proposer(round_num, response)
            save_round_output(exp_dir, round_num, "PROPOSER", response)
            session.save()
            if verbose:
                safe_print(f"\n{response}")
        else:
            if verbose:
                print("\n[PROPOSER] Already completed (loaded from checkpoint)")
            response = session.round_results[round_num].get('proposer', '')

        # === JUDGE PHASE ===
        if session.needs_judge(round_num):
            if verbose:
                print(f"\n{'-'*50}")
                if session.judge_is_fresh:
                    print("\n[JUDGE] NEW INDEPENDENT JUDGE — fresh evaluation, no prior score history")
                else:
                    print("\n[JUDGE] Evaluating round...")
            turn_msg = get_judge_turn_message(
                session.current_idea, critique, response,
                round_num, session.total_rounds,
            )
            if use_trained_judge:
                turn_msg = _enrich_with_retrieval(turn_msg, session.current_idea)
            judge_first = session.judge_is_fresh
            judgement = _call_agent(
                session.judge_session_id, judge_sys, turn_msg,
                is_first_call=judge_first,
                exp_dir=exp_dir, label=f"r{round_num}_judge",
                session=session, role="judge", cwd=str(exp_dir),
            )
            if judge_first:
                session.judge_is_fresh = False
            if _is_agent_error(judgement):
                safe_print(f"  [ERROR] Judge agent failed: {judgement[:200]}")
                raise RuntimeError(f"Judge agent failed on round {round_num}: {judgement[:200]}")
            session.record_judge(round_num, judgement)
            save_round_output(exp_dir, round_num, "JUDGE", judgement)
            session.save()
            if verbose:
                safe_print(f"\n{judgement}")
        else:
            if verbose:
                print("\n[JUDGE] Already completed (loaded from checkpoint)")

        # === CRITIC ROTATION CHECK ===
        judge_score = session.get_judge_score_numeric(round_num)
        if (judge_score is not None
                and judge_score >= session.critic_replace_threshold):
            old_count = session.critic_rotation_count
            session.rotate_critic()
            session.critic_rotation_rounds.append(round_num)
            session.critic_is_fresh = True
            session.save()
            if verbose:
                print(f"\n{'*'*70}")
                print(f"[ROTATION] Judge score {judge_score}/10 >= {session.critic_replace_threshold} threshold")
                print(f"[ROTATION] Replacing critic AND judge with INDEPENDENT REVIEWER #{session.critic_rotation_count}")
                print(f"  Critics so far: {old_count} -> {session.critic_rotation_count} "
                      f"(need {session.min_independent_critics})")
                print(f"{'*'*70}")

        # === EARLY KILL + PLATEAU DETECTION + REPROPOSE FORCING ===
        # Only applies in explore phase (where REPROPOSE is allowed)
        if session.refinement_phase == "explore" and judge_score is not None:
            should_force_repropose = False
            repropose_reason = ""

            # Early kill: score too low after N rounds since last reproposal
            rounds_since_repropose = round_num - session.last_repropose_round
            if (rounds_since_repropose >= session.early_kill_rounds
                    and judge_score < session.early_kill_threshold):
                should_force_repropose = True
                repropose_reason = (
                    f"score {judge_score:.1f} < {session.early_kill_threshold} "
                    f"after {rounds_since_repropose} rounds since last reproposal (early kill)")

            # Plateau detection: no improvement for N consecutive rounds (since last reproposal)
            if not should_force_repropose and rounds_since_repropose >= session.plateau_patience + 1:
                recent_scores = []
                start_r = max(round_num - session.plateau_patience, session.last_repropose_round + 1)
                for r in range(start_r, round_num + 1):
                    s = session.get_judge_score_numeric(r)
                    if s is not None:
                        recent_scores.append(s)
                if (len(recent_scores) >= session.plateau_patience + 1
                        and max(recent_scores) - min(recent_scores) <= 0.5
                        and judge_score < 8.0):
                    should_force_repropose = True
                    scores_str = ", ".join(f"{s:.1f}" for s in recent_scores)
                    repropose_reason = (
                        f"score plateaued at [{scores_str}] for "
                        f"{session.plateau_patience} rounds (no improvement)")

            # Check repropose budget before forcing
            if should_force_repropose:
                if session.reproposal_count < session.max_reproposals:
                    session.reproposal_count += 1
                    if verbose:
                        print(f"\n{'!'*70}")
                        print(f"[FORCE REPROPOSE] {repropose_reason}")
                        print(f"[FORCE REPROPOSE] Reproposal {session.reproposal_count}"
                              f"/{session.max_reproposals} — resetting debate")
                        print(f"{'!'*70}")

                    # Reset: new proposer, critic, and judge sessions
                    session.proposer_session_id = str(uuid.uuid4())
                    session.rotate_critic()
                    session.critic_is_fresh = True

                    # Inject a forced repropose message into the proposer's
                    # next round by recording a synthetic "FORCE REPROPOSE"
                    # critic output that tells the proposer to start over.
                    force_msg = (
                        f"## SYSTEM: FORCED REPROPOSE\n\n"
                        f"The judge has determined this idea is not strong enough: "
                        f"{repropose_reason}.\n\n"
                        f"You MUST **REPROPOSE** a completely new idea. Do NOT defend "
                        f"or pivot the current idea. Start fresh with a new direction.\n\n"
                        f"Previous ideas that did not work (DO NOT reuse):\n"
                    )
                    # Collect titles of all previous ideas to avoid
                    for ep in session.evolution_path:
                        if ep.get("action") in ("REFINED", "PIVOTED", "REPROPOSED"):
                            force_msg += f"- {ep.get('title', 'Unknown')}\n"

                    session._pending_force_repropose = force_msg
                    session.last_repropose_round = round_num
                    session.save()
                else:
                    if verbose:
                        print(f"\n[REPROPOSE BUDGET EXHAUSTED] {session.reproposal_count}"
                              f"/{session.max_reproposals} reproposals used. "
                              f"Continuing with current idea.")

    # === FINAL SYNTHESIS ===
    if session.needs_synthesis():
        if verbose:
            print(f"\n{'='*70}")
            print("[SYNTHESIS] FINAL SYNTHESIS")
            print(f"{'='*70}")
            print("\n[WORKING] Synthesizing debate into final refined idea...")

        ctx_file = write_synthesis_context(exp_dir, session.original_idea, session.history)
        turn_msg = get_synthesis_turn_message(ctx_file)
        synthesis_sid = str(uuid.uuid4())
        final_idea = run_claude_create(
            synthesis_sid, _SYNTHESIS_SYSTEM_PROMPT, turn_msg, timeout=1800,
            exp_dir=exp_dir, label="synthesis", cwd=str(exp_dir),
        )
        if _is_agent_error(final_idea):
            raise RuntimeError(f"Synthesis agent failed: {final_idea[:200]}")

        session.record_synthesis(final_idea)
        save_round_output(exp_dir, 0, "SYNTHESIS", final_idea)
        session.save()

        if verbose:
            safe_print(f"\n{final_idea}")
    else:
        if verbose:
            print("\n[SYNTHESIS] Already completed (loaded from checkpoint)")

    # Save final history
    save_debate_history(
        session.original_idea,
        session.history,
        session.final_idea,
        str(exp_dir / "full_history.md"),
        exp_dir
    )

    # Update metadata with final status
    save_experiment_metadata(exp_dir, {
        "experiment_id": session.experiment_id,
        "idea_num": session.idea_num,
        "idea_title": session.idea_title,
        "total_rounds": session.total_rounds,
        "status": session.status,
        "started_at": session.started_at,
        "completed_at": session.completed_at,
        "evolution_type": session.evolution_type,
        "rounds_completed": list(session.round_results.keys()),
        "evolution_steps": len(session.evolution_path),
    })

    update_experiment_index(exp_dir.parent, session)

    if verbose:
        print(f"\n[COMPLETE] Experiment saved to: {exp_dir}")
        print(f"[EVOLUTION] Type: {session.evolution_type or 'REFINED'}")
        print(f"[CRITICS] {session.critic_rotation_count} independent critic(s) used")
        if session.critic_rotation_rounds:
            print(f"[ROTATIONS] Rotated after rounds: {session.critic_rotation_rounds}")

    return session


def adversarial_refinement(
    idea: str,
    rounds: int = 2,
    output_file: Optional[str] = None,
    verbose: bool = True,
    idea_num: Optional[int] = None,
    idea_title: Optional[str] = None,
    resume_from: Optional[str] = None,
    domain: str = "",
    phase: str = "explore",
    seed_paper: str = "",
    seed_paper_content: str = "",
    target_venues: str = "",
    critic_threshold: float = 8.0,
    min_critics: int = 3,
    use_trained_judge: bool = False,
    early_kill_threshold: float = 7.0,
    early_kill_rounds: int = 3,
    plateau_patience: int = 2,
    max_reproposals: int = 3,
) -> str:
    """
    Refine a research idea through adversarial debate.

    Three agents (Critic, Proposer, Judge) debate in persistent Claude sessions.
    """
    # Resume from checkpoint if provided
    if resume_from:
        if verbose:
            print(f"[LOADING] Resuming from checkpoint: {resume_from}")
        session = RefinementSession.load(resume_from)
        exp_dir = Path(session.experiment_dir)
        if phase and phase != session.refinement_phase:
            if verbose:
                print(f"[PHASE] Switching from {session.refinement_phase} -> {phase}")
            session.refinement_phase = phase
        session.critic_replace_threshold = critic_threshold
        session.min_independent_critics = min_critics
    else:
        exp_dir = create_experiment_dir(idea_title=idea_title, idea_num=idea_num)

        session = RefinementSession(
            original_idea=idea,
            idea_num=idea_num,
            idea_title=idea_title,
            total_rounds=rounds,
            current_idea=idea,
            experiment_id=exp_dir.name,
            experiment_dir=str(exp_dir),
            domain=domain,
            refinement_phase=phase,
            seed_paper=seed_paper,
            seed_paper_content=seed_paper_content,
            target_venues=target_venues,
            critic_replace_threshold=critic_threshold,
            min_independent_critics=min_critics,
            early_kill_threshold=early_kill_threshold,
            early_kill_rounds=early_kill_rounds,
            plateau_patience=plateau_patience,
            max_reproposals=max_reproposals,
        )

        (exp_dir / "original_idea.md").write_text(idea, encoding="utf-8")

        save_experiment_metadata(exp_dir, {
            "experiment_id": session.experiment_id,
            "idea_num": idea_num,
            "idea_title": idea_title,
            "total_rounds": rounds,
            "domain": domain,
            "phase": phase,
            "status": "initialized",
            "started_at": session.started_at,
            "original_idea_preview": idea[:300],
        })

        session.save()

    session = run_refinement_session(session, verbose=verbose,
                                     use_trained_judge=use_trained_judge)

    if output_file:
        save_debate_history(
            session.original_idea,
            session.history,
            session.final_idea,
            output_file,
            exp_dir
        )
        if verbose:
            print(f"\n[SAVED] Full debate saved to: {output_file}")

    return session.final_idea


def resume_refinement(checkpoint_path: str, verbose: bool = True) -> str:
    """
    Resume a refinement from a checkpoint file.
    
    Args:
        checkpoint_path: Path to session.pkl checkpoint file
        verbose: If True, print progress
    
    Returns:
        The final refined idea
    """
    session = RefinementSession.load(checkpoint_path)
    session = run_refinement_session(session, verbose=verbose)
    return session.final_idea


def create_experiment_dir(idea_title: str = None, idea_num: int = None) -> Path:
    """Create a new experiment directory with unique ID."""
    # Base directory for all refinements
    base_dir = Path(__file__).parent / "refinements"
    base_dir.mkdir(exist_ok=True)
    
    # Generate experiment ID: timestamp + optional idea info
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if idea_num:
        exp_id = f"exp_{timestamp}_idea{idea_num}"
    elif idea_title:
        # Sanitize title for folder name
        safe_title = re.sub(r'[^\w\s-]', '', idea_title)[:30].strip().replace(' ', '_')
        exp_id = f"exp_{timestamp}_{safe_title}"
    else:
        exp_id = f"exp_{timestamp}"
    
    exp_dir = base_dir / exp_id
    exp_dir.mkdir(exist_ok=True)
    
    return exp_dir


def save_experiment_metadata(exp_dir: Path, metadata: dict) -> None:
    """Save experiment metadata to JSON file."""
    metadata_file = exp_dir / "metadata.json"
    
    # Update with current timestamp
    metadata["last_updated"] = datetime.now().isoformat()
    
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)


def update_experiment_index(refinements_dir: Path, session: 'RefinementSession') -> None:
    """Update the top-level index.json with a summary of all experiments."""
    index_file = refinements_dir / "index.json"
    
    # Load existing index
    if index_file.exists():
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                index = json.load(f)
        except (json.JSONDecodeError, IOError):
            index = {"experiments": []}
    else:
        index = {"experiments": []}
    
    # Build summary for this experiment
    # Extract final idea title from evolution path
    final_title = session.idea_title or "(untitled)"
    if session.evolution_path:
        # Find the last proposer entry
        proposer_entries = [e for e in session.evolution_path if e.get("action") != "CRITIC"]
        if proposer_entries:
            final_title = proposer_entries[-1].get("title", final_title)
    
    entry = {
        "experiment_id": session.experiment_id,
        "idea_num": session.idea_num,
        "original_title": session.idea_title,
        "final_title": final_title,
        "total_rounds": session.total_rounds,
        "status": session.status,
        "evolution_type": session.evolution_type,
        "started_at": session.started_at,
        "completed_at": session.completed_at,
        "num_reproposals": sum(1 for e in session.evolution_path if e.get("action") == "REPROPOSED"),
        "num_pivots": sum(1 for e in session.evolution_path if e.get("action") == "PIVOTED"),
        "dir": str(Path(session.experiment_dir).name),
    }
    
    # Update or insert
    existing_ids = {e["experiment_id"] for e in index["experiments"]}
    if session.experiment_id in existing_ids:
        index["experiments"] = [
            entry if e["experiment_id"] == session.experiment_id else e
            for e in index["experiments"]
        ]
    else:
        index["experiments"].append(entry)
    
    index["last_updated"] = datetime.now().isoformat()
    index["total_experiments"] = len(index["experiments"])
    
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)


def save_round_output(exp_dir: Path, round_num: int, phase: str, content: str) -> None:
    """Save individual round output to its own file."""
    filename = f"round{round_num}_{phase.lower()}.md"
    filepath = exp_dir / filename
    filepath.write_text(content, encoding="utf-8")


def save_intermediate_history(
    original: str,
    history: list[str],
    filename: str,
    round_num: int,
    phase: str,
    exp_dir: Path = None
) -> None:
    """Save intermediate debate history after each phase (crash recovery)."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    content = f"""# Adversarial Idea Refinement (IN PROGRESS)
*Generated: {timestamp}*
*Status: Round {round_num} - {phase} complete*

---

## Original Idea

{original}

---

## Debate History

{chr(10) + "---" + chr(10).join(history)}

---

## Final Refined Idea

*(Synthesis not yet complete - debate in progress)*
"""
    
    Path(filename).write_text(content, encoding="utf-8")
    
    # Also save to experiment directory if provided
    if exp_dir:
        (exp_dir / "full_history.md").write_text(content, encoding="utf-8")


def save_debate_history(
    original: str,
    history: list[str],
    final: str,
    filename: str,
    exp_dir: Path = None
) -> None:
    """Save the final debate history to a markdown file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    content = f"""# Adversarial Idea Refinement
*Generated: {timestamp}*
*Status: COMPLETE*

---

## Original Idea

{original}

---

## Debate History

{chr(10) + "---" + chr(10).join(history)}

---

## Final Refined Idea

{final}
"""
    
    Path(filename).write_text(content, encoding="utf-8")
    
    # Also save to experiment directory if provided
    if exp_dir:
        (exp_dir / "full_history.md").write_text(content, encoding="utf-8")
        (exp_dir / "final_idea.md").write_text(f"# Final Refined Idea\n\n{final}", encoding="utf-8")


def extract_ideas_from_markdown(filepath: str) -> list[dict]:
    """Extract individual ideas from a markdown file like research_ideas.md."""
    content = Path(filepath).read_text(encoding="utf-8")
    
    # Split by "## Idea" headers
    idea_pattern = r'## Idea (\d+): (.+?)(?=\n## Idea \d+:|## Summary|---\s*$|\Z)'
    matches = re.findall(idea_pattern, content, re.DOTALL)
    
    ideas = []
    for num, text in matches:
        # Extract just the idea content (title + everything until next section)
        title_match = re.search(r'^(.+?)$', text.strip(), re.MULTILINE)
        title = title_match.group(1).strip() if title_match else f"Idea {num}"
        
        ideas.append({
            "number": int(num),
            "title": title,
            "content": f"## Idea {num}: {text.strip()}"
        })
    
    return ideas


def menu_mode():
    """Run in menu mode - prompts user to select ideas (not for automated pipelines)."""
    print("\n" + "="*70)
    print("[REFINER] ADVERSARIAL RESEARCH IDEA REFINER")
    print("="*70)
    
    # Check for research_ideas.md
    ideas_file = Path("../research_ideas.md")
    if ideas_file.exists():
        ideas = extract_ideas_from_markdown(str(ideas_file))
        
        if ideas:
            print(f"\n[LIST] Found {len(ideas)} ideas in research_ideas.md:\n")
            for idea in ideas:
                print(f"  [{idea['number']}] {idea['title']}")
            
            print("\n  [0] Enter a custom idea")
            print("  [q] Quit\n")
            
            choice = input("Select idea number to refine: ").strip().lower()
            
            if choice == 'q':
                return
            
            try:
                choice_num = int(choice)
                if choice_num == 0:
                    idea_text = input("\nEnter your research idea:\n> ").strip()
                else:
                    matching = [i for i in ideas if i['number'] == choice_num]
                    if matching:
                        idea_text = matching[0]['content']
                    else:
                        print(f"[ERROR] No idea #{choice_num} found")
                        return
            except ValueError:
                print("[ERROR] Invalid input")
                return
    else:
        idea_text = input("\nEnter your research idea:\n> ").strip()
    
    if not idea_text:
        print("[ERROR] No idea provided")
        return
    
    # Ask for rounds
    rounds_input = input("\nNumber of debate rounds [2]: ").strip()
    rounds = int(rounds_input) if rounds_input.isdigit() else 2
    
    # Generate output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"refinement_{timestamp}.md"
    
    # Run refinement
    result = adversarial_refinement(
        idea_text,
        rounds=rounds,
        output_file=output_file,
        verbose=True
    )
    
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Refine research ideas through adversarial AI debate"
    )
    parser.add_argument(
        "--idea", "-i",
        type=str,
        help="The research idea to refine"
    )
    parser.add_argument(
        "--idea-num", "-n",
        type=int,
        help="Idea number from research_ideas.md to refine"
    )
    parser.add_argument(
        "--file", "-f",
        type=str,
        help="File containing ideas (extracts all and lets you choose)"
    )
    parser.add_argument(
        "--resume",
        type=str,
        help="Resume from checkpoint file (session.pkl)"
    )
    parser.add_argument(
        "--rounds", "-r",
        type=int,
        default=2,
        help="Number of adversarial rounds (default: 2)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file for debate history"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress verbose output"
    )
    parser.add_argument(
        "--domain", "-d",
        type=str,
        default="",
        help="Domain constraint - proposals must stay in this domain (e.g. 'video generation')"
    )
    parser.add_argument(
        "--phase",
        type=str,
        choices=["explore", "refine"],
        default="explore",
        help="Phase: 'explore' allows REPROPOSE, 'refine' restricts to DEFEND/PIVOT only (default: explore)"
    )
    parser.add_argument(
        "--from-scratch",
        action="store_true",
        help="Start from scratch: agent proposes initial idea in domain, then critic/proposer debate. Requires --domain."
    )
    parser.add_argument(
        "--seed-paper",
        type=str,
        default="",
        help="Seed paper to ground idea generation (arxiv ID like '2401.12345' or full title)"
    )
    parser.add_argument(
        "--target-venues",
        type=str,
        default="",
        help="Target venues, comma-separated (e.g. 'ICML,NeurIPS,ICLR'). Constrains ideas to ML venues."
    )
    parser.add_argument(
        "--critic-threshold",
        type=float,
        default=8.0,
        help="Judge score threshold to trigger critic rotation (default: 8.0)"
    )
    parser.add_argument(
        "--min-critics",
        type=int,
        default=3,
        help="Minimum independent critics required before the session can end (default: 3)"
    )
    parser.add_argument(
        "--use-trained-judge",
        action="store_true",
        help="Use GEPA-trained judge prompt with skill library and paper retrieval"
    )
    parser.add_argument(
        "--tournament",
        type=int,
        default=1,
        help="Tournament mode: generate N candidate ideas, quick-score, debate the best (default: 1 = no tournament)"
    )
    parser.add_argument(
        "--early-kill-threshold",
        type=float,
        default=7.0,
        help="Force repropose if score below this after --early-kill-rounds (default: 7.0)"
    )
    parser.add_argument(
        "--early-kill-rounds",
        type=int,
        default=3,
        help="Number of rounds before early kill check kicks in (default: 3)"
    )
    parser.add_argument(
        "--plateau-patience",
        type=int,
        default=2,
        help="Force repropose if score doesn't improve for this many consecutive rounds (default: 2)"
    )
    parser.add_argument(
        "--max-reproposals",
        type=int,
        default=3,
        help="Maximum number of full reproposals allowed (default: 3)"
    )
    parser.add_argument(
        "--use-frontier",
        action="store_true",
        help="Analyze paper corpus to find underexplored gaps before generating ideas"
    )

    args = parser.parse_args()
    
    # Handle resume mode
    if args.resume:
        if not Path(args.resume).exists():
            print(f"[ERROR] Checkpoint file not found: {args.resume}")
            return

        print(f"[RESUMING] Loading checkpoint: {args.resume}")
        session = RefinementSession.load(args.resume)
        if args.phase and args.phase != session.refinement_phase:
            print(f"[PHASE] Switching: {session.refinement_phase} -> {args.phase}")
            session.refinement_phase = args.phase
        # Allow extending rounds on a completed session
        if args.rounds and args.rounds > session.total_rounds:
            print(f"[ROUNDS] Extending: {session.total_rounds} -> {args.rounds}")
            session.total_rounds = args.rounds
            if session.status == "complete":
                session.status = "in_progress"
                session.current_phase = "critic"
                session.completed_at = None
                session.final_idea = None  # re-synthesize at new end
        session.save()
        result = resume_refinement(args.resume, verbose=not args.quiet)

        if args.quiet:
            safe_print(result)
        return
    
    # Determine the idea to refine
    idea_text = None
    idea_num = None
    idea_title = None

    if args.from_scratch or args.seed_paper:
        args.domain = args.domain or "machine learning"
        seed_content = ""
        if args.seed_paper:
            if not args.quiet:
                print(f"[SEED PAPER] Fetching: {args.seed_paper}")
            seed_content = _fetch_seed_paper(args.seed_paper)
            args._seed_content = seed_content
            if not args.quiet:
                print(f"[SEED PAPER] {len(seed_content)} chars fetched")

        # Frontier seeding: analyze paper corpus for underexplored gaps
        frontier_context = ""
        if args.use_frontier:
            frontier_context = get_frontier_context(
                args.domain, verbose=not args.quiet)

        # Tournament mode: generate N candidates, quick-score, pick the best
        if args.tournament > 1:
            idea_text, idea_title, all_ideas, all_scores = run_tournament(
                domain=args.domain,
                n_candidates=args.tournament,
                target_venues=args.target_venues,
                seed_paper=args.seed_paper,
                seed_paper_content=seed_content,
                frontier_context=frontier_context,
                verbose=not args.quiet,
            )
        else:
            # Single idea generation (original path)
            if not args.quiet:
                label = f"[FROM SEED: {args.seed_paper}]" if args.seed_paper else "[FROM SCRATCH]"
                venues_info = f" -> target: {args.target_venues}" if args.target_venues else ""
                print(f"{label} Generating initial idea in domain: {args.domain}{venues_info}")
            scratch_prompt = get_scratch_idea_prompt(
                args.domain,
                target_venues=args.target_venues,
                seed_paper=args.seed_paper,
                seed_paper_content=seed_content,
            )
            if frontier_context:
                scratch_prompt += f"\n\n=== FRONTIER CONTEXT (underexplored areas) ===\n{frontier_context}"
            raw_idea = run_claude_oneshot(scratch_prompt, timeout=1800, label="scratch_idea")
            # Extract structured idea
            if "## Title" in raw_idea and len(raw_idea) > 200:
                idea_text = raw_idea.split("## Title", 1)[-1].strip()
                if not idea_text.startswith("##"):
                    idea_text = "## Title\n" + idea_text
            elif len(raw_idea) > 300 and not _is_agent_error(raw_idea):
                idea_text = raw_idea
            else:
                print(f"[ERROR] Agent failed to produce a valid initial idea: {raw_idea[:200]}")
                return
            # Extract title for experiment tracking
            title_match = re.search(r"##\s*Title\s*\n+(.+?)(?:\n##|\n\n|\Z)", idea_text, re.MULTILINE | re.DOTALL)
            idea_title = title_match.group(1).strip()[:80] if title_match else "From Scratch"
            if not args.quiet:
                print(f"[GENERATED] {idea_title}\n")
    
    if idea_text is None and args.idea:
        # If the user passed a number, treat it as idea_num lookup
        if args.idea.strip().isdigit():
            args.idea_num = int(args.idea.strip())
            # Fall through to idea_num handling below
        else:
            idea_text = args.idea
            idea_title = args.idea[:50]  # Use first 50 chars as title
    
    if idea_text is None and args.idea_num:
        ideas_file = Path("../research_ideas.md")
        if not ideas_file.exists():
            print("[ERROR] research_ideas.md not found")
            return
        
        ideas = extract_ideas_from_markdown(str(ideas_file))
        matching = [i for i in ideas if i['number'] == args.idea_num]
        
        if matching:
            idea_text = matching[0]['content']
            idea_num = args.idea_num
            idea_title = matching[0]['title']
            print(f"[REFINING] {idea_title}")
        else:
            print(f"[ERROR] No idea #{args.idea_num} found")
            return
    
    if idea_text is None and args.file:
        if not Path(args.file).exists():
            print(f"[ERROR] File not found: {args.file}")
            return
        idea_text = Path(args.file).read_text(encoding="utf-8")
        idea_title = Path(args.file).stem  # Use filename as title
    
    if idea_text is None:
        # Menu mode (manual selection - not for automated pipelines)
        menu_mode()
        return
    
    # Generate output filename if not provided
    output_file = args.output
    if not output_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"refinement_{timestamp}.md"
    
    # Run refinement
    result = adversarial_refinement(
        idea_text,
        rounds=args.rounds,
        output_file=output_file,
        verbose=not args.quiet,
        idea_num=idea_num,
        idea_title=idea_title,
        domain=args.domain,
        phase=args.phase,
        seed_paper=getattr(args, "seed_paper", ""),
        seed_paper_content=getattr(args, "_seed_content", ""),
        target_venues=getattr(args, "target_venues", ""),
        critic_threshold=args.critic_threshold,
        min_critics=args.min_critics,
        use_trained_judge=args.use_trained_judge,
        early_kill_threshold=args.early_kill_threshold,
        early_kill_rounds=args.early_kill_rounds,
        plateau_patience=args.plateau_patience,
        max_reproposals=args.max_reproposals,
    )
    
    if args.quiet:
        safe_print(result)


if __name__ == "__main__":
    main()
