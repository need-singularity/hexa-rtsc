# TAPE-AUDIT — hexa-rtsc

## A. Audit-class ledgers

- `state/markers/*.marker` — **737 markers** (`_envprobe_*`, `_orch_*`, `_test_run_all_logic_*`, `agi-architecture-verify_*`). `_FAILED.marker` grade encoding. **Class-T** fit — collapse to `state/runs.tape`.
- `state/hexa_rtsc_cli.log` — CLI log.
- `memory/` dir present (uncommon in this batch) — possible existing structured store.
- No JSONL ledger.

## B. Identity surface

`AGENTS.md` + `README.ai.md` (AI-targeted README — distinct from human README.md) + `LIMIT_BREAKTHROUGH.md` + `RELEASE_NOTES_v1.0.0.md` + `RELEASE_NOTES_v1.1.0.md`. The room-temperature-superconductor (RTSC) repo's identity is the **claimed Tc material stack**. Fit for `hexa-rtsc/identity.tape` with `@I material=hg-pb-cu-O-stack` + axis pin.

## C. Domain.md files

Only 10 root MD files — light domain coverage. Subdirs (sc/, rtsc/, firmware/, verify/) carry the structure instead. No `+`-meta-domains.

## D. Per-run/per-event history

`agi-architecture-verify_*` markers + `_orch_*` orchestration runs + `_envprobe_*` environment probes. The verification-cycle event grain is dense — `@T verify_run <- @S env=... => @R ok|err == @D Tc=...` fits naturally.

## E. Promotion candidates

- **n6 atoms** — superconductor Cooper-pair condition + critical-temperature scaling laws (`bt-1163-1168-superconductor-v5`). Lattice-closure pinned facts ready for atom-IDs.
- **hxc binaries** — resistance vs temperature curves, Meissner-effect levitation traces.
- **n12 cube cells** — material-class × Tc-tier × pressure-tier.

## Verdict

**MEDIUM** — 737 markers + dense verify-cycle event grain + 6-falsifier breakthrough series. Tape compaction is clear; atom-promotion list is focused on superconductor stack.
