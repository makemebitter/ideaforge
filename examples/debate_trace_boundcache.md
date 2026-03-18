# Example Debate Trace: BoundCache

*This is a curated excerpt from a real adversarial refinement session showing the debate dynamics. The full session ran 10 rounds over ~6 hours with score trajectory: 6 → 7 → 7.5 → 8.5 → 8 → 8.5 → 9 → 9 → 9.5. Verbose technical details are trimmed for readability.*

> **Disclaimer:** This idea is AI-generated and has not been vetted by human researchers.

---

## Original Idea

**Title:** Motion-Aware Dynamic Attention Caching for Training-Free Video Diffusion Acceleration

**One-Line Summary:** A training-free inference acceleration method for video diffusion transformers that adaptively schedules attention recomputation based on online motion complexity estimates, eliminating the static caching schedules of prior work.

**Key Insight:** Motion complexity in a generated video can be estimated online from coarse diffusion steps because temporal attention patterns at large timesteps correlate with the eventual motion structure. This early signal can dynamically allocate the attention recomputation budget — reusing cached attention aggressively on static regions and recomputing on dynamic ones.

---

## Round 1 — CRITIC

**Verdict: The core idea has been scooped.**

### FATAL FLAW: AdaCache (ICCV 2025) Already Does This

AdaCache (arXiv:2411.02397, Nov 2024, accepted ICCV 2025) implements *exactly* content-adaptive attention caching for video diffusion:

- Uses a "Motion Regularization" (MoReg) score computed from attention output differences across timesteps
- Dynamically decides per-step whether to recompute or reuse cached attention
- Evaluated on Open-Sora and CogVideoX — the same models proposed
- Reports 2× speedup with minimal quality loss on VBench

The proposal's "online motion complexity scoring from L2 distance between consecutive-frame temporal attention outputs" is functionally identical to MoReg.

**What could survive:** The proposal correctly identifies that no caching paper provides *formal quality guarantees* — AdaCache's trigger is heuristic. A paper providing provable error bounds for attention caching would occupy a genuine gap.

---

## Round 1 — PROPOSER

**DECISION: PIVOT** to BoundCache — a theoretically-grounded safety layer providing error propagation bounds for attention caching.

Instead of competing with AdaCache on the heuristic trigger, pivot to the unsolved problem: **no existing caching method can tell you how much quality it's losing.** BoundCache provides a per-step certificate: "reusing this cached attention output introduces at most ε error in the final video."

The approach uses Lipschitz continuity analysis of the denoising network to derive a computable error bound: if the attention output change between steps is below a threshold derived from the Lipschitz constant, the cache reuse is provably safe.

---

## Round 1 — JUDGE

### Score: 6/10

The pivot is correct — AdaCache fully scoops the original idea, and BoundCache occupies a genuine gap (formal quality guarantees for caching). But the theoretical claims need scrutiny.

**Guidance for next round:** Focus on the *vacuousness risk* — Lipschitz constants for 5B-parameter video DiTs are likely very large. L^(T-t) with even L=1.1 and T-t=50 gives ≈117, making the bound so tight that BoundCache recomputes almost every step, eliminating speedup entirely.

---

## Round 2 — CRITIC

The global Lipschitz bound is almost certainly vacuous. With L^50 ≈ 117, the threshold δ ≤ ε/117 forces recomputation at nearly every step. Additionally, the proposal treats each attention layer's cache decision independently, but caching layer k modifies the hidden state fed to layer k+1 — errors accumulate multiplicatively across layers.

## Round 2 — PROPOSER

**DECISION: DEFEND** — Replace global Lipschitz with *local* Lipschitz constants measured empirically. The local constant L_local ≈ 0.1–0.5 (measured via perturbation) avoids the exponential blowup. Also restrict to temporal attention only (the expensive part), keeping all other layers exact.

## Round 2 — JUDGE

### Score: 7/10

The local Lipschitz pivot is the right direction. The proxy contradiction is resolved. But the core theoretical risk is still unresolved — the proposer acknowledged the open problems but moved them to "measure empirically," which is honest but doesn't resolve the uncertainty.

---

## Round 3 — CRITIC

The local Lipschitz claim needs pressure. L_local(x_t, t) varies per timestep, per video, per layer. The proposed measurement (50 perturbation runs) measures an average — is this the right quantity, or a new heuristic dressed in theoretical clothing?

## Round 3 — PROPOSER

**DECISION: DEFEND** — Introduced end-to-end amplification factor A_e2e that directly measures how much a cache reuse error at step t amplifies in the final output. This collapses within-step and across-step error propagation into a single measurable quantity, eliminating all unmeasured Lipschitz constants.

## Round 3 — JUDGE

### Score: 7.5/10

The A_e2e measurement is the right conceptual move. The trigger formula is cleaner. But the multi-step accumulation problem remains — A_e2e bounds single-step injection, not the aggregate of all cached steps.

---

## Round 4 — CRITIC

*(Targets the multi-step error accumulation problem and the Amdahl's law ceiling for temporal-attention-only caching)*

## Round 4 — PROPOSER

Introduced adversarial conservatism factor κ validated via power iteration. Converted Amdahl ceiling from a liability into a contribution: "maximum certified speedup theorem" quantifying the theoretical ceiling for quality-certified caching.

## Round 4 — JUDGE

### Score: 8.5/10

The strongest proposal yet. The trigger formula is now clean and internally consistent. A_e2e collapses both within-step and across-step amplification into a single measurement. The adversarial direction problem is addressed. The Amdahl ceiling is converted into a framing advantage.

**Remaining issues are narrow and technical — none are structural.**

---

*[Rounds 5-6: Critic targets proxy chain gaps and failure-safety of ρ_min. Proposer resolves each. Score oscillates 8 → 8.5 as new technical issues are found and fixed.]*

---

## Round 7 — JUDGE

### Score: 9/10

Round 7 is the strongest proposal in the series. The trigger-calibration circularity is elegantly resolved by the monotonicity test. The LPIPS theoretical chain is correctly abandoned in favor of a direct empirical mapping. The sequential dependency graph with two hard stop gates is excellent risk engineering — it prevents wasting $400 on the main experiment if upstream measurements invalidate the contribution.

---

## Round 9 — JUDGE

### Score: 9.5/10

The proposal has converged to a technically sound, practically implementable research plan with clear risk management, honest scope, and a publishable contribution even in the worst-case outcome (analysis paper). The title "BoundCache: Conformal Quality Certificates for Temporal Attention Caching in Video Diffusion Transformers" is concise and correctly frames the contribution.

**ACCEPT** — the debate has achieved its purpose: a research idea that started as a scooped motion-aware caching method has been refined into the first conformal quality certificate for video DiT attention caching, with a complete experimental plan, correct statistical methodology, honest scope, and two-gate risk management before the major GPU spend.

---

## Score Trajectory

```
Round:  1    2    3    4    5    6    7    8    9
Score:  6    7   7.5  8.5   8   8.5   9    9   9.5
        ↑         ↑         ↑              ↑
     Pivot    A_e2e      ρ_min fix    Conformal framing
```

## Key Dynamics Illustrated

1. **Critic finds fatal prior art (Round 1):** AdaCache scoops the original idea → forces a complete pivot
2. **Theoretical depth through adversarial pressure:** Each round tightens the mathematical framework — global Lipschitz → local Lipschitz → end-to-end amplification → conformal certificates
3. **Score oscillation at 8+:** Fresh technical concerns (proxy chain gaps, failure-safety) temporarily drop the score before being resolved
4. **Natural evolution:** The final idea (conformal quality certificates) is fundamentally different from — and stronger than — the original idea (motion-aware caching)
5. **Judge guides both sides:** Provides specific technical guidance to both critic and proposer, steering the debate toward the most productive issues
