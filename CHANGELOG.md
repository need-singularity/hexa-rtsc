# Changelog

All notable changes to **hexa-rtsc** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and SemVer.

## [Unreleased]

### Added (2026-05-07 — 1st iteration · runnable surface bootstrap)

Recipe ref: `~/core/bedrock/docs/runnable_surface_recipe.md` §1 (16-script
inventory) + §2 (7-step cycle). closure-depth accumulation begin.

- **`verify/calc_bcs.hexa`** (T1 algebraic, slot #3, pillar `sc`) — closed-form
  derivation anchoring F-SC-{1,2,3}: Cooper pair φ(6)=2, Abrikosov CN=6,
  BCS specific-heat molecule σ(6)=12. Live divisor-function lattice
  (σ/τ/φ/sopfr/J₂), master identity σ·φ = n·τ = 24, §8.1 Universal Cooper
  index n/φ=3, §8.2 closure section [φ, σ/φ]=[2,6] verified for BCS s-wave
  (3.528) / d-wave (4.3) / Allen–Dynes (5.3), §8.3 λ regime ladder + μ*
  ceiling 1/sopfr=0.2. **32/32 PASS** · sentinel `__HEXA_RTSC_CALC_BCS__ PASS`.
- **`verify/falsifier_check.hexa`** refactored from monotone-audit to combined
  closure-progress tracker (recipe §1 slot #14, §3 closure-pct ladder).
  Each falsifier (F-RTSC-{1,2,3} + F-SC-{1,2,3}) now emits T1/T2/T3 tier
  status + closure pct (0/33/67/100). F-SC-{1,2,3} at 33% (T1 = calc_bcs);
  F-RTSC-{1,2,3} at 0% (no T1 yet). Existing monotone-audit (roadmap §A.4
  row+status / .own own 2 mirror / cli surface / banned-status) retained.
  **22/22 PASS** · sentinel `__HEXA_RTSC_FALSIFIER__ PASS`.
- **`tests/test_calculators.hexa`** (recipe §1 build/tests) — registered
  (filename, sentinel) for calc_bcs.hexa; grows per future calc_/numerics_
  iteration.

### Changed

- `verify/run_all.hexa`: SCRIPTS list 3 → 4 (calc_bcs added).
- `cli/hexa-rtsc.hexa`: `verify` subcommand inventory 3 → 4 (calc_bcs added).
- `tests/test_falsifier.hexa`: pass criterion 19/19 → 22/22 + sentinel match.
- `tests/test_verify.hexa`: pass criterion 3/3 → 4/4.
- `hexa.toml` `[test].files`: `tests/test_calculators.hexa` registered.

### Closure progress (recipe §3, post-iter-1)

| Falsifier | T1 | T2 | T3 | closure |
|-----------|----|----|----|---------|
| F-RTSC-1  | ✗  | ✗  | ✗  | 0% UNVERIFIED |
| F-RTSC-2  | ✗  | ✗  | ✗  | 0% UNVERIFIED |
| F-RTSC-3  | ✗  | ✗  | ✗  | 0% UNVERIFIED |
| F-SC-1    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-2    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-3    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |

## [1.0.0] — 2026-05-06

### Added

- Initial standalone extraction from `n6-architecture/domains/energy/`
  - `rtsc/` ← `room-temp-sc/` (full directory copy, n6-arch SHA `c0f1f570`)
  - `sc/`   ← `superconductor/` (full directory copy, n6-arch SHA `c0f1f570`)
- 2-verb spec coverage: `rtsc` (Tc=300K, Hc2=σ·τ=48T, Cooper φ=2) and
  `sc` (BCS, Abrikosov CN=6, Cooper φ=2).
- n=6 invariant lattice closed-form candidate: σ(6)=12, τ(6)=4, φ(6)=2,
  J₂=24; master identity σ·φ = n·τ = 24; derived Hc2 = σ·τ = 48 T.
- Falsifier preregister tables: F-RTSC-{1,2,3} and F-SC-{1,2,3}.
- Placeholder CLI dispatcher `cli/hexa-rtsc.hexa` (5 subcommands:
  `rtsc`, `sc`, `status`, `selftest`, `help` + `--version`).
- `install.hexa` hx package-manager hook (pre/post phases, warn-only).
- `hexa.toml` package manifest with `substrate_role.role = "substrate-of-substrates"`.
- `tests/test_selftest.hexa` placeholder selftest harness.
- README with §Why (substrate-of-substrates), §Verbs, §Status (HONESTY),
  §Install, §Cross-link (3 downstream consumers), §License.
- MIT License.

### Honest scope (raw#10 C3)

- RT-SC is academically **UNPROVEN** as of 2026-05; LK-99 and subsequent
  candidates have not been independently replicated.
- v1.0.0 ships spec + falsifier preregister only — **no working empirical
  sandbox**; CLI dispatcher is **PLACEHOLDER**.
- n=6 lattice mappings are **closed-form candidates**, not empirically
  fitted constants. Synthesis-side validation is out-of-repo.

### Substrate-of-substrates downstream consumers

- `dancinlab/hexa-fusion` — 48T SC coil dependency
- `dancinlab/hexa-ufo` — Stage-1 Meissner levitation dependency
- `dancinlab/hexa-cern` — SC magnet dependency

[1.0.0]: https://github.com/dancinlab/hexa-rtsc/releases/tag/v1.0.0
