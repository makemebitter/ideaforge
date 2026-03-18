"""Shared Claude Code CLI helpers for judge_training modules."""

import os
import subprocess
import shutil
import tempfile
import time
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger("claude_utils")

_CLAUDE_EXE: Optional[str] = None


def get_claude_exe() -> str:
    global _CLAUDE_EXE
    if _CLAUDE_EXE is None:
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


def write_turn_file(exp_dir: Optional[Path], label: str, content: str) -> Path:
    if exp_dir:
        exp_dir.mkdir(parents=True, exist_ok=True)
        path = exp_dir / f"_turn_{label}.md"
    else:
        fd, tmp = tempfile.mkstemp(suffix=".md", prefix=f"turn_{label}_")
        os.close(fd)
        path = Path(tmp)
    path.write_text(content, encoding="utf-8")
    return path


def file_ref(path: Path) -> str:
    return f'Read your full task and context from the file at "{path.resolve()}". Respond based on it.'


def run_claude_oneshot(
    prompt: str,
    timeout: int = 1800,
    model: str = "sonnet",
    exp_dir: Optional[Path] = None,
    label: str = "oneshot",
    cwd: Optional[str] = None,
) -> str:
    t0 = time.time()
    turn_file = write_turn_file(exp_dir, label, prompt)
    exe = get_claude_exe()
    cmd = [
        exe, "-p",
        "--dangerously-skip-permissions",
        "--model", model,
        file_ref(turn_file),
    ]
    logger.debug("claude_oneshot: model=%s label=%s prompt=%d chars turn_file=%s",
                 model, label, len(prompt), turn_file)
    result = _run_subprocess(cmd, timeout, cwd=cwd)
    elapsed = time.time() - t0
    is_error = result.startswith("Agent") or result.startswith("Error")
    logger.debug("claude_oneshot: label=%s elapsed=%.1fs output=%d chars error=%s",
                 label, elapsed, len(result), is_error)
    if is_error:
        logger.warning("claude_oneshot: label=%s FAILED: %s", label, result[:300])
    return result


def _run_subprocess(cmd: list[str], timeout: int, cwd: Optional[str] = None) -> str:
    try:
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
        )
        output = result.stdout.strip()

        if not output and result.stderr:
            stderr = result.stderr.strip()
            if "usage limit" in stderr.lower():
                return f"Agent hit usage limit: {stderr[:300]}"
            return f"Agent error (stderr): {stderr[:500]}"

        if not output:
            if result.returncode in (137, 143):
                return "Agent timed out"
            return f"Agent returned empty output (exit code: {result.returncode})"

        return output

    except subprocess.TimeoutExpired:
        return "Agent timed out"
    except FileNotFoundError as e:
        return f"Error: claude executable not found - {e}"
    except Exception as e:
        return f"Agent error: {str(e)}"
