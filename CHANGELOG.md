# Changelog

All notable changes to **hexa-rtsc** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and SemVer.

## [Unreleased]

### Added (2026-05-08 — 9th iteration · numerics_bcs_parity T2 ×2 · F-SC stack deepening)

- **`verify/numerics_bcs_parity.hexa`** (T2 numerical, slot #11, pillar `sc`,
  second-stack on F-SC-{1,2,3}) — recipe §6 hexa-rtsc 4-machine class parity:
  Nb-Ti / Nb₃Sn / MgB₂ / YBCO. 4×4 grid (4 ratios × 4 SC classes) verified:
  all 4 classes' 2Δ/kTc fits closure section [φ, σ/φ] = [2, 6]; all are
  Type-II (κ > 1/√2); Hc2(0) monotone with Tc trend (14 < 28 < 74 < 120 T);
  ΔC/γTc spans BCS canonical 1.426 (Nb-Ti 1.4, ±0.05) to d-wave (YBCO 4.5);
  4-class avg 2Δ/kTc = 4.225 ∈ [2,6] (strong-coupling pull above s-wave 3.528);
  48 T target sits between Nb₃Sn (28) and MgB₂ (74) — achievable.
  **19/19 PASS** · sentinel `__HEXA_RTSC_NUMERICS_BCS_PARITY__ PASS`.

### Changed

- F-SC-{1,2,3}: T2_SCRIPTS = ["numerics_bcs.hexa", "numerics_bcs_parity.hexa"]
  → **T2 ×2 stack** (closure stays 67% but stack-depth advances toward
  full sat-1 target T2 ≥ 3 each). Total checks 31 → 34.

### Closure progress (post iter 9 — T2 ×2 first stack)

| Falsifier | T1 | T2 | T3 | closure | T2 stack |
|-----------|----|----|----|---------|----------|
| F-RTSC-1  | ✓ | ✓ numerics_lk99 | ✗ | 67% | 1 |
| F-RTSC-2  | ✓ | ✓ numerics_mcmillan | ✗ | 67% | 1 |
| F-RTSC-3  | ✓ | ✓ numerics_hc2_48t | ✗ | 67% | 1 |
| F-SC-1    | ✓ | ✓ numerics_bcs + numerics_bcs_parity | ✗ | 67% | **2** |
| F-SC-2    | ✓ | ✓ numerics_bcs + numerics_bcs_parity | ✗ | 67% | **2** |
| F-SC-3    | ✓ | ✓ numerics_bcs + numerics_bcs_parity | ✗ | 67% | **2** |

Sat-1 progress: 3/6 falsifiers at T2 ×2 stack. Need ×3 each for full sat-1.

### Added (2026-05-07 — 8th iteration · numerics_lk99 T2 · ALL 6F AT 67% · sat-1 toehold)

- **`verify/numerics_lk99.hexa`** (T2 numerical, slot #10, pillar `rtsc`) —
  closes F-RTSC-1 via float reproduction-stat eval. τ(6)=4 floor reproduced.
  LK-99 confirmation rate p_c = 0/10 = 0.0. Binomial 95% CI upper bound
  p_max = 1 - 0.05^(1/10) ≈ 0.26 (true positive rate ≤ 26% with 95%
  confidence given 0/10 observation). σ-φ=10 false-positive multiplier
  consistency. Bayesian posterior threshold: k ≥ 4 confirmations needed
  to flip prior 0.1 → posterior > 0.5 at BF=2 (≈ τ(6) floor by independent
  derivation). σ(6)=12 substrate family partition (9 confirmed + 3
  unconfirmed). **15/15 PASS** · sentinel `__HEXA_RTSC_NUMERICS_LK99__ PASS`.
- F-RTSC-1 closure 33% → **67% PARTIAL** (T1 calc_lk99 + T2 numerics_lk99).

### 🎯 Milestone: ALL 6 FALSIFIERS AT 67% CLOSURE (sat-1 toehold)

Recipe §7.2 sat-1 first leg satisfied: `min(F1.T2, F2.T2, F3.T2, ...) ≥ 1`.
Full sat-1 requires `min ≥ 3` per recipe §7.3 — i.e., each falsifier needs
≥3 T2 stack-script. Path forward: deepen T2 stack via parity / solver
scripts (numerics_*_parity.hexa, numerics_*_solver.hexa) per recipe §7.4
priority #5-6 + §1 slot #6,7,11.

### Closure progress (post iter 8)

| Falsifier | T1 | T2 | T3 | closure |
|-----------|----|----|----|---------|
| F-RTSC-1  | ✓ calc_lk99 | ✓ numerics_lk99 | ✗ | **67% PARTIAL** |
| F-RTSC-2  | ✓ calc_mcmillan | ✓ numerics_mcmillan | ✗ | **67% PARTIAL** |
| F-RTSC-3  | ✓ calc_hc2_48t | ✓ numerics_hc2_48t | ✗ | **67% PARTIAL** |
| F-SC-1    | ✓ calc_bcs | ✓ numerics_bcs | ✗ | **67% PARTIAL** |
| F-SC-2    | ✓ calc_bcs | ✓ numerics_bcs | ✗ | **67% PARTIAL** |
| F-SC-3    | ✓ calc_bcs | ✓ numerics_bcs | ✗ | **67% PARTIAL** |

### Added (2026-05-07 — 7th iteration · numerics_hc2_48t T2 · F-RTSC-3 → 67%)

- **`verify/numerics_hc2_48t.hexa`** (T2 numerical, slot #9, pillar `rtsc`) —
  closes F-RTSC-3 via float Hc2/3-sister bridge eval. Three identity paths
  to 48 reproduce at math_pure floor (rel_err < 1e-9). WHH coefficient
  0.69 ≈ ln(2) (rel_err 0.05% via log_pure(2)=0.6931...). Pauli-Maki
  crossover Tc=48/1.84=26.087 K. RT-SC Tc=300K → Hc2_p=552T (orbital
  fully dominant, ratio 11.5×). 3-sister bridge: fusion 12T·τ=48
  (exact), cern LHC 8.3·n=49.8T (within 5%), ufo Meissner expulsion.
  Reference SC parity: Nb-Ti(14T) Nb₃Sn(28T) below 48T; MgB₂(74T)
  YBCO(120T) H₃S(70T) above. **20/20 PASS** · sentinel
  `__HEXA_RTSC_NUMERICS_HC2_48T__ PASS`.
- F-RTSC-3 closure 33% → **67% PARTIAL** (T1 calc_hc2_48t + T2 numerics_hc2_48t).

### Added (2026-05-07 — 6th iteration · numerics_mcmillan T2 · F-RTSC-2 → 67%)

- **`verify/numerics_mcmillan.hexa`** (T2 numerical, slot #8, pillar `rtsc`) —
  closes F-RTSC-2 via float McMillan/Allen-Dynes evaluation. λ ∈ [0.5, 2.0]
  sweep at Θ_D=400K, μ*=0.13: max Tc = 44 K (well below RT-SC 300 K).
  Reference SC parity via Allen-Dynes(ω_log): Pb 7.20 K (rel_err 0%),
  Nb 10.46 K (12%), Hg 3.63 K (14%). §8.1 universal Cooper at λ_eff=φ=2.
  λ→∞ phonon-free: Tc ≈ 97.5 K, requires Θ_D ≥ 1230 K for Tc=300K
  (above any known phonon spectrum → BCS framework rules out RT-SC).
  Allen-Dynes ≡ McMillan equivalence at math_pure floor. **16/16 PASS** ·
  sentinel `__HEXA_RTSC_NUMERICS_MCMILLAN__ PASS`.
- F-RTSC-2 closure 33% → **67% PARTIAL** (T1 calc_mcmillan + T2 numerics_mcmillan).

### Added (2026-05-07 — 5th iteration · numerics_bcs T2 · FIRST 67% closure)

Recipe ref: `~/core/bedrock/docs/runnable_surface_recipe.md` §1 slot #5
(numerics_<pillar1>) + §4 5-invariant lint contract. T2 numerical tier
opened — first chunk via `self/runtime/math_pure`.

- **`verify/numerics_bcs.hexa`** (T2 numerical, slot #7, pillar `sc`) —
  closes F-SC-{1,2,3} via float arithmetic re-derivation:
    §8.2  2Δ/kTc = 2π·e^(-γ_E) ≈ 3.5278 (rel_err 1.4e-4 vs 3.528 published)
    §8.4  ΔC/γTc = σ(6)/(7·ζ(3)) ≈ 1.4261 (rel_err 8.9e-5 vs 1.426 published)
    GL κ_c = 1/√2 ≈ 0.7071 (rel_err 1.6e-16 — math_pure precision floor)
    ζ(3) reproduced via 100-term series (rel_err 4e-5 vs Apéry constant)
    n=6 anchor float ↔ int round-trip (sqrt_pure(σ²)=σ, exp(log(σ))=σ)
    Type-I (Sn 0.16, Al 0.04 < 1/√2) vs Type-II (Nb 1.3, YBCO 95 > 1/√2)
    s-wave / d-wave / Allen-Dynes gap ratios all in closure [φ, σ/φ]=[2,6]
  **Recipe §4 5 invariants**: math_pure import ✓ · sentinel ✓ · FALSIFIERS ✓
  · exit(0) ✓ · RUN/FAIL counters ✓. **19/19 PASS** · sentinel
  `__HEXA_RTSC_NUMERICS_BCS__ PASS`.

### Changed

- `verify/falsifier_check.hexa`: F4_T2_SCRIPTS = F5_T2_SCRIPTS = F6_T2_SCRIPTS
  = ["numerics_bcs.hexa"] → **F-SC-{1,2,3} closure 33% → 67% PARTIAL**
  (T1+T2 locked). Total checks 25 → 28 (+3 T2-presence audits).
- `verify/run_all.hexa`: SCRIPTS list 7 → 8 (numerics_bcs added).
- `cli/hexa-rtsc.hexa`: `verify` subcommand inventory 7 → 8.
- `tests/test_calculators.hexa`: CALCULATORS row added (numerics_bcs, 5 total).
- `tests/test_falsifier.hexa`: pass criterion 25/25 → 28/28.
- `tests/test_verify.hexa`: pass criterion 7/7 → 8/8.

### Closure progress (post iter 5 — FIRST 67% milestone)

| Falsifier | T1 | T2 | T3 | closure |
|-----------|----|----|----|---------|
| F-RTSC-1  | ✓ calc_lk99 | ✗ | ✗ | 33% EARLY |
| F-RTSC-2  | ✓ calc_mcmillan | ✗ | ✗ | 33% EARLY |
| F-RTSC-3  | ✓ calc_hc2_48t | ✗ | ✗ | 33% EARLY |
| F-SC-1    | ✓ calc_bcs | ✓ numerics_bcs | ✗ | **67% PARTIAL** |
| F-SC-2    | ✓ calc_bcs | ✓ numerics_bcs | ✗ | **67% PARTIAL** |
| F-SC-3    | ✓ calc_bcs | ✓ numerics_bcs | ✗ | **67% PARTIAL** |

**Milestone:** 3/6 falsifiers at 67% closure (T1+T2 algebra+numerics). Recipe
§7.2 sat-1 progress: 50% of falsifiers at saturation target. Next chunks
land T2 for F-RTSC-{1,2,3} (numerics_mcmillan / numerics_hc2_48t / numerics_lk99
parity scripts) + numerics_bcs_parity.hexa (Nb/Sn/In/Pb/Hg s-wave gap
published comparison) for F-SC stack-of-3.

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
