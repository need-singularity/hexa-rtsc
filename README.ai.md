# hexa-rtsc — AI-native handoff

> Conformance: hive raw 271 (readme-ai-native-mandate). This file is the
> canonical entry point for AI agents (Claude / Hexa / etc.) operating on
> this repository. Human entry point is [`README.md`](README.md).

## Identity

- **Name**: `hexa-rtsc` (Room-Temp Superconductor — substrate-of-substrates)
- **Axis**: `energy`
- **n=6 lattice**:
  - σ(6) ≡ 12 (BCS specific-heat molecule + 12-vertex Cooper-pair shell)
  - τ(6) ≡ 4 (4-phase ladder: normal / pseudogap / SC / strange-metal)
  - φ(6) ≡ 2 (Cooper pair = 2-electron boson)
  - Hc2 ≡ σ·τ = 48 T (critical magnetic field gate)
  - master identity: σ·φ = n·τ = 24 (J₂ Mathieu/Leech symmetry)
- **Parent (canonical SSOT)**: `n6-architecture/domains/energy/{room-temp-sc,superconductor}/`
- **Distribution**: `https://github.com/dancinlab/hexa-rtsc` (public)

## Hierarchy (canonical pattern, v1.0.0 + v1.1.0 target)

```
hexa-rtsc/                   T0 (repo root)
├── rtsc/                    T1 (single-feature core, v1.0.0 — moves to core/rtsc/ in v1.1.0)
│   ├── room-temp-sc.md      ← spec (canonical)
│   └── *-verify.hexa        ← 10 application shells (move to module/applications/ in v1.1.0)
├── sc/                      T1 (single-feature core, v1.0.0 — moves to core/sc/ in v1.1.0)
│   └── superconductor.md    ← spec (canonical)
├── module/                  T2 (per-module fan-out, RESERVED for v1.1.0+)
├── verify/                  T0 (runnable invariant audit, .hexa hexa stdlib only)
├── cli/                     T0 (single-entry router; hexa-rtsc.hexa)
├── tests/                   T0 (hexa native test runner)
├── doc/                     T0 (human-only archive + lineage)
├── .own                     T0 (project-local SSOT, mk2 own_v1 — invariants + roles + directives)
├── .roadmap.hexa_rtsc       T0 (cross-cutting state — release cadence, falsifiers)
├── hexa.toml                T0 (package manifest for `hx install`)
└── install.hexa             T0 (hx pre/post hook)
```

Imports flow **T0 → T1 → T2** only. The 10 `rtsc/*-verify.hexa` shells are
v1.0.0-grandfathered into T1 alongside the spec; v1.1.0 splits them into
`module/applications/` per the sscb pattern.

## Invariants (must not violate when editing)

1. **n=6 identity holds**: any change touching σ / τ / φ / Hc2 must restate
   the lattice equality. `verify/lattice_check.hexa` is the gate.
2. **RT-SC empirical-unproven contract**: every public artifact (CLI verb
   output, README badges, status table) MUST surface "UNPROVEN" /
   "sentinel only — does NOT validate empirical claim" alongside any
   `__HEXA_RTSC_*__ PASS` line. raw#10 honest C3 mandate.
3. **Falsifier monotone**: F-RTSC-{1,2,3} + F-SC-{1,2,3} status flips
   only `OPEN → CONFIRMED` or `OPEN → DEMOTED`. **Never** silently retract.
4. **hexa-only orchestration**: code lives in `cli/` `verify/` `tests/`
   `module/` only, .hexa primary (raw#9). No Python bridge.

## Edit policy

- **Additive-only** at the doc layer. Do not rename, move, or delete files
  in `rtsc/` / `sc/` without updating `doc/lineage/origin.md` and adding a
  redirect note.
- **English primary** in commit messages and new prose; Korean caveats
  surfaced in CLI verb output preserved as-is.
- v1.0.0 → v1.1.0 directory restructure (rtsc/ → core/rtsc/ + module/applications/)
  requires this file's hierarchy diagram **before** the implementing PR.

## Common agent tasks

| Task | Where to look first |
|---|---|
| Add a new RT-SC candidate material | `rtsc/room-temp-sc.md` (then propagate to roadmap §A.4 falsifier preregister) |
| Tighten a lattice number | `rtsc/room-temp-sc.md` + `sc/superconductor.md` (spec wins) |
| Adjust falsifier disposition | `.roadmap.hexa_rtsc` §A.4 + `.own` own 2 decl row + `cli/hexa-rtsc.hexa` falsifier table |
| Add a new verify check | `verify/<name>.hexa` (.own own 3 4-location scope) |
| Run invariant check | `hexa run cli/hexa-rtsc.hexa verify` (or directly `hexa run verify/lattice_check.hexa`) |
| Run selftest | `hexa run cli/hexa-rtsc.hexa selftest` (sentinel sweep, no empirical claim) |
| Cross-compile / native build | `hexa build cli/hexa-rtsc.hexa -o build/hexa-rtsc` (optional, not required for v1.0.0) |

## Lineage tag

This repo was extracted from `n6-architecture` on **2026-05-06**.
Source commits: see [`doc/lineage/origin.md`](doc/lineage/origin.md).
Structural pattern aligned to `hexa-sscb` mk2 own_v1 on **2026-05-07**.
