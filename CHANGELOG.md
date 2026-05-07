# Changelog

All notable changes to **hexa-rtsc** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and SemVer.

## [Unreleased]

### Added (2026-05-07 — 4th iteration · F-RTSC-1 T1 calc_lk99 · T1 SWEEP COMPLETE)

Recipe ref: `~/core/bedrock/docs/runnable_surface_recipe.md` §7.4 priority #3
final pass — all 6 falsifiers now have T1 algebraic anchor at 33% closure.
**Algebraic tier (T1) saturation reached.** Next iteration moves to T2
numerics tier (slot #5+ per recipe §1).

- **`verify/calc_lk99.hexa`** (T1 algebraic, slot #6, pillar `rtsc`) —
  closed-form anchor for F-RTSC-1 (LK-99 reproduction failure → next-
  candidate substrate update). Live σ(6)=12 candidate substrate family
  enumeration (cuprate / iron-pnictide / hydride / nickelate / LK-99-class
  / MgB₂-class / organic / heavy-fermion / Sr₂RuO₄ / RbCs-fulleride /
  Bi-cuprate / Lu-N-H retracted-slot). τ(6)=4 phase ladder (synth →
  measure → publish → reproduce). Reproduction floor N ≥ τ=4. LK-99
  stoichiometry (PO₄)₆ "₆" anchor + Pb count 10 = σ-φ. Timeline
  (2023-07 claim, 2023-08-12 ~10 negative reproductions, 0 confirmed).
  Historical confirmed catalog (BCS / BSCCO / YBCO / RbCs / MgB₂ /
  iron-pnictide / H₃S / LaH₁₀ — 8 entries) vs retracted catalog
  (USO / Cu-Pb-hydride / Dias 2020 / Dias 2023 / LK-99 — 5 entries).
  False-positive multiplier σ-φ = 10. **27/27 PASS** · sentinel
  `__HEXA_RTSC_CALC_LK99__ PASS`.

### Changed

- `verify/falsifier_check.hexa`: F1_T1_SCRIPTS = ["calc_lk99.hexa"] →
  F-RTSC-1 closure 0% → 33%. **All 6 falsifiers now at 33% (T1 sweep
  complete).** Total checks 24 → 25.
- `verify/run_all.hexa`: SCRIPTS list 6 → 7.
- `cli/hexa-rtsc.hexa`: `verify` subcommand inventory 6 → 7.
- `tests/test_calculators.hexa`: CALCULATORS row added (calc_lk99, 4 total).
- `tests/test_falsifier.hexa`: pass criterion 24/24 → 25/25.
- `tests/test_verify.hexa`: pass criterion 6/6 → 7/7.

### Closure progress (post iter 4 — T1 SWEEP COMPLETE)

| Falsifier | T1 | T2 | T3 | closure |
|-----------|----|----|----|---------|
| F-RTSC-1  | ✓ calc_lk99 | ✗ | ✗ | 33% EARLY (algebra only) |
| F-RTSC-2  | ✓ calc_mcmillan | ✗ | ✗ | 33% EARLY (algebra only) |
| F-RTSC-3  | ✓ calc_hc2_48t | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-1    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-2    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-3    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |

**Milestone:** algebraic tier (T1) saturation. 4 calc_*.hexa scripts
covering all 6 preregistered falsifiers — recipe §1 slot #3-4 fully
populated. Next iteration starts T2 numerics tier (numerics_*.hexa,
slot #5+) — first chunk likely numerics_bcs.hexa or numerics_lk99_parity.hexa.

### Added (2026-05-07 — 3rd iteration · F-RTSC-3 T1 calc_hc2_48t)

Recipe ref: `~/core/bedrock/docs/runnable_surface_recipe.md` §7.4 priority #3
(calc_<pillar> for next falsifier). All-T1 sweep continues — 5 of 6
falsifiers now have algebraic anchor.

- **`verify/calc_hc2_48t.hexa`** (T1 algebraic, slot #5, pillar `rtsc`) —
  closed-form derivation anchoring F-RTSC-3 (48 T SC coil substrate-of-
  substrates bridge). Three independent identity paths to 48: (a) σ·τ=12·4,
  (b) J₂²/σ=576/12, (c) (2σ)²/(2n)=576/12. n=6 uniqueness (σ(n)·τ(n)=48
  only at n=6 in [1..12]). WHH 0.69 ≈ ln(2) coefficient. GL coherence
  Hc2 ∝ 1/ξ² with Φ₀=h/(φ·e) anchor. Pauli–Maki crossover Tc=26K
  (orbital binding above). 3-sister bridge: fusion 12T·τ=48, cern LHC·n=48,
  ufo Meissner expulsion. Reference SC catalog: Nb-Ti(14T) / Nb₃Sn(28T) /
  MgB₂(74T) / YBCO(120T) / H₃S(70T) — 48 T achievable. **29/29 PASS** ·
  sentinel `__HEXA_RTSC_CALC_HC2_48T__ PASS`.

### Changed

- `verify/falsifier_check.hexa`: F3_T1_SCRIPTS = ["calc_hc2_48t.hexa"] →
  F-RTSC-3 closure 0% → 33% (EARLY, algebra only). Total checks 23 → 24.
- `verify/run_all.hexa`: SCRIPTS list 5 → 6 (calc_hc2_48t added).
- `cli/hexa-rtsc.hexa`: `verify` subcommand inventory 5 → 6.
- `tests/test_calculators.hexa`: CALCULATORS row added (calc_hc2_48t).
- `tests/test_falsifier.hexa`: pass criterion 23/23 → 24/24.
- `tests/test_verify.hexa`: pass criterion 5/5 → 6/6.

### Closure progress (post iter 3)

| Falsifier | T1 | T2 | T3 | closure |
|-----------|----|----|----|---------|
| F-RTSC-1  | ✗  | ✗  | ✗  | 0% UNVERIFIED |
| F-RTSC-2  | ✓ calc_mcmillan | ✗ | ✗ | 33% EARLY (algebra only) |
| F-RTSC-3  | ✓ calc_hc2_48t | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-1    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-2    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-3    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |

5/6 falsifiers at 33%. Last T1 chunk = `calc_lk99` for F-RTSC-1 (LK-99
negative-result anchor + σ(6)=12 candidate substrate family catalog).

### Added (2026-05-07 — 2nd iteration · F-RTSC-2 T1 calc_mcmillan)

Recipe ref: `~/core/bedrock/docs/runnable_surface_recipe.md` §7.4 priority #3
(calc_<pillar> for next falsifier).

- **`verify/calc_mcmillan.hexa`** (T1 algebraic, slot #4, pillar `rtsc`) —
  closed-form derivation anchoring F-RTSC-2 (BCS λ McMillan ceiling Tc ≤ 30 K).
  §8.1 Universal Cooper structure (exp arg = -(n/φ) = -3, cutoff 1/n = 1/6),
  §8.3 λ regime ladder (weak ≤ 1/φ=0.5, mid ≤ 1, strong ≤ φ=2 unitarity),
  Morel–Anderson μ* ≤ 1/sopfr=0.2, ceiling-ratio target/ceiling = 300/30 = 10
  = σ−φ (miniaturisation factor), above-ceiling material catalog (YBCO 92K,
  Hg-1223 138K, H₃S 203K, LaH₁₀ 250K → all > 30K, BCS-beyond active),
  McMillan/Allen–Dynes prefactors {1.20, 1.45, 1.04, 0.62} structure, §8.1
  phonon-free limit at λ_max = φ giving exp arg = -(n/φ)/φ = -3/2.
  **35/35 PASS** · sentinel `__HEXA_RTSC_CALC_MCMILLAN__ PASS`.

### Changed

- `verify/falsifier_check.hexa`: F2_T1_SCRIPTS = ["calc_mcmillan.hexa"] →
  F-RTSC-2 closure 0% → 33% (EARLY, algebra only). Total checks 22 → 23.
- `verify/run_all.hexa`: SCRIPTS list 4 → 5 (calc_mcmillan added).
- `cli/hexa-rtsc.hexa`: `verify` subcommand inventory 4 → 5.
- `tests/test_calculators.hexa`: CALCULATORS row added (calc_mcmillan).
- `tests/test_falsifier.hexa`: pass criterion 22/22 → 23/23.
- `tests/test_verify.hexa`: pass criterion 4/4 → 5/5.

### Closure progress (post iter 2)

| Falsifier | T1 | T2 | T3 | closure |
|-----------|----|----|----|---------|
| F-RTSC-1  | ✗  | ✗  | ✗  | 0% UNVERIFIED |
| F-RTSC-2  | ✓ calc_mcmillan | ✗ | ✗ | 33% EARLY (algebra only) |
| F-RTSC-3  | ✗  | ✗  | ✗  | 0% UNVERIFIED |
| F-SC-1    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-2    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |
| F-SC-3    | ✓ calc_bcs | ✗ | ✗ | 33% EARLY (algebra only) |

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
