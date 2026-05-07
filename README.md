# 🧲 hexa-rtsc — Room-Temp Superconductor (substrate-of-substrates)

> **Room-Temp Superconductor — Meissner + 48T SC coil. Substrate-of-substrates for fusion · UFO · accelerator.**
>
> 2-verb energy substrate organized around the **n=6 invariant lattice**:
> RTSC (Tc=300K, Hc2=σ·τ=48T, Cooper φ=2) / SC (BCS, Abrikosov CN=6).
> v1.0.0 ships **spec + falsifier preregister** only — no working empirical
> sandbox. RT-SC is **academically unproven** (LK-99 et al. unsettled).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-informational.svg)](CHANGELOG.md)
[![Verbs: 0/2 wired](https://img.shields.io/badge/verbs-0%2F2_wired_(spec_only)-orange.svg)](#verb-status-table)
[![n=6 lattice](https://img.shields.io/badge/n%3D6-σ·τ%3D48T_φ%3D2_Tc%3D300K-purple.svg)](#n6-invariant-lattice)
[![Status: SPEC_ONLY](https://img.shields.io/badge/status-SPEC__ONLY-orange.svg)](#status)
[![Verify: 10/10](https://img.shields.io/badge/verify-10%2F10-brightgreen.svg)](verify/lattice_check.hexa)
[![Audit: 8/8](https://img.shields.io/badge/audit-8%2F8-brightgreen.svg)](verify/cross_doc_audit.hexa)
[![Falsifier: 19/19](https://img.shields.io/badge/falsifier-19%2F19-brightgreen.svg)](verify/falsifier_check.hexa)
[![Substrate-of-substrates](https://img.shields.io/badge/role-substrate--of--substrates-blueviolet.svg)](#why)

---

## Why

`hexa-rtsc` is the **substrate-of-substrates**: the n=6 base substrate that
three sister substrates depend on:

- **need-singularity/hexa-fusion** — needs **48T SC coil** (σ·τ=48 satisfies confinement gate)
- **need-singularity/hexa-ufo** — needs **Stage-1 Meissner levitation** (B-field expulsion)
- **need-singularity/hexa-cern** — needs **SC magnet** (accelerator beamline bending)

If RT-SC is empirically realised, all three downstream substrates unlock at
once: tabletop fusion, room-temp magnetic levitation, and benchtop accelerator
beamlines. If it is not, all three remain upper-bounded by current
liquid-helium-cooled cuprate / Nb-Ti / Nb₃Sn limits.

This repo extracts the n=6 closed-form candidate spec + falsifier preregister
from `n6-architecture/domains/energy/{room-temp-sc,superconductor}/` (SHA
`c0f1f570`, 2026-05-06).

---

## Status

> **RT-SC is academically UNPROVEN.** LK-99 (2023) and subsequent room-temp
> candidates have **not been independently replicated**. This v1.0.0 release
> ships:
>
> - n=6 **closed-form candidate** spec (Tc=300K, Hc2=σ·τ=48T, Cooper φ=2 boson, Abrikosov CN=6)
> - **falsifier preregister** tables per verb (F-RTSC-{1,2,3} + F-SC-{1,2,3})
> - **PLACEHOLDER** CLI dispatcher (working `.hexa` empirical sandbox is **TBD**)
>
> No empirical claim of working RT-SC is made or implied. Synthesis-side
> validation is out-of-repo (would require a materials lab).

Verdict: **SPEC_ONLY** for the empirical RT-SC claim (0/2 RT-SC/SC verbs
deliver bench evidence). The lattice machinery itself — closed-form
arithmetic, cross-document audits, falsifier preregister — is **WIRED**:
3 verify/*.hexa scripts (10/10 + 8/8 + 19/19) + 4 tests/*.hexa pass
end-to-end. Per `.own` own 2: a `__HEXA_RTSC_*__ PASS` sentinel **never**
validates the empirical RT-SC claim.

---

## Verbs

### `rtsc` — Room-Temp Superconductor (SPEC)

n=6 closed-form candidate:

| symbol      | value                       | role                              |
|-------------|-----------------------------|-----------------------------------|
| Tc          | 300 K                       | room-temperature target           |
| Hc2         | σ(6)·τ(6) = 12·4 = 48 T     | critical magnetic field           |
| cooper pair | φ(6) = 2                    | electron boson pair → R=0         |
| meissner    | full B-expulsion            | substrate of UFO levitation       |
| miniaturise | 1/(σ-φ) = 1/10              | SC magnet shrink ratio            |

Falsifier preregister:

- **F-RTSC-1**: Tc(measured) < 250 K → DEMOTE n=6 Tc claim
- **F-RTSC-2**: Hc2 < 30 T at 4.2 K → DEMOTE σ·τ=48 closed-form
- **F-RTSC-3**: no Meissner expulsion → DEMOTE φ=2 boson claim

### `sc` — Superconductor (BCS / Abrikosov) (SPEC)

n=6 closed-form candidate:

| symbol       | value                  | role                                    |
|--------------|------------------------|-----------------------------------------|
| cooper       | φ(6) = 2               | electron boson pair                     |
| abrikosov    | CN = 6                 | hexagonal vortex lattice coordination   |
| bcs_ratio    | σ(6) = 12              | specific-heat jump molecule             |
| flux_quantum | Φ₀ = h/(2e)            | φ=2 denominator                         |
| Tc_high      | 150 K → RT-SC 300 K    | rtsc verb upgrade target                |

Falsifier preregister:

- **F-SC-1**: Cooper pair size ≠ φ=2 → DEMOTE φ=2 pair claim
- **F-SC-2**: vortex lattice not CN=6 → DEMOTE Abrikosov CN=6 claim
- **F-SC-3**: BCS ratio ΔC/γTc ≠ ~1.43 → DEMOTE σ=12 molecule claim

---

## Install

### Via `hx` (recommended)

```bash
hx install hexa-rtsc          # bare-name → resolves need-singularity/hexa-rtsc
hx install /path/to/hexa-rtsc # local path — entry auto-detected from hexa.toml
hexa-rtsc --version           # → 1.0.0
```

> Entry auto-detection requires hx with the 2026-05-07 `detect_entry()` patch
> (parses `[package].entry` / `[[bin]].path` from `hexa.toml`, plus
> `cli/<name>.hexa` candidate). Older hx needs `--entry cli/hexa-rtsc.hexa`.

### Via git clone

```bash
git clone https://github.com/need-singularity/hexa-rtsc.git ~/.hexa-rtsc
export HEXA_RTSC_ROOT=~/.hexa-rtsc
export PATH="$HEXA_RTSC_ROOT/cli:$PATH"

# Run any subcommand:
hexa run $HEXA_RTSC_ROOT/cli/hexa-rtsc.hexa selftest
```

### Quick Start

```bash
hexa-rtsc selftest      # sentinel sweep — specs + own_v1 + verify/ landing
hexa-rtsc status        # verb table + verdict + caveats
hexa-rtsc lattice       # live-compute n=6 closed-form (σ τ φ Hc2 master)
hexa-rtsc verify        # run all verify/*.hexa invariant audits (3 scripts)
hexa-rtsc rtsc          # RTSC spec excerpt + falsifier preregister
hexa-rtsc sc            # SC   spec excerpt + falsifier preregister
```

---

## Verb status table

| Verb       | Status        | n=6 lattice candidate          | Empirical sandbox     |
|------------|---------------|--------------------------------|-----------------------|
| `rtsc`     | SPEC v1.0.0   | Tc=300K, σ·τ=48T, φ=2          | UNPROVEN (TBD)        |
| `sc`       | SPEC v1.0.0   | Cooper φ=2, Abrikosov CN=6     | UNPROVEN (TBD)        |
| `lattice`  | WIRED v1.0.x  | live divisor-fn computation    | n/a (math only)       |
| `verify`   | WIRED v1.0.x  | runs 3 verify/*.hexa scripts   | n/a (sentinel)        |
| `selftest` | WIRED v1.0.x  | sentinel sweep (8 files)       | n/a (sentinel)        |

Verdict: **SPEC_ONLY for the empirical claim** (0/2 RT-SC/SC verbs deliver
empirical evidence) **+ WIRED for the lattice machinery** (3/3 invariant
audits + 4/4 .hexa tests pass; closed-form arithmetic verifiable live).

---

## n=6 invariant lattice

The lattice anchors the substrate to a single algebraic identity:

```
σ(6) = 12        BCS specific-heat molecule + 12-vertex Cooper-pair shell
τ(6) = 4         4-state ladder (normal / fluctuation / pair / condensate)
φ(6) = 2         binary dichotomy (Cooper pair: 2-electron boson)
J₂   = 24        octahedral O ⊂ icosahedral I subgroup (vortex grouping)

master identity:   σ · φ = n · τ = 12 · 2 = 6 · 4 = 24
derived:           Hc2  = σ · τ  = 12 · 4 = 48 T   (critical field gate)
```

These are **closed-form candidates**, not empirically fitted constants.
Synthesis-side validation is out-of-repo.

---

## Build & verify

```bash
hexa-rtsc selftest                 # sentinel sweep — 8 files (specs + own + verify/ + lineage)
hexa-rtsc verify                   # 3 invariant audits, exit 0 = all PASS
hexa-rtsc lattice                  # live n=6 closed-form computation
hexa run verify/lattice_check.hexa # 10/10 PASS expected (direct invocation)
hexa run verify/run_all.hexa       # 3/3 verify scripts (orchestrator)
hexa test tests/test_lattice.hexa  # native hexa test runner
```

### Last validation sweep — 2026-05-07

| Check                              | Result        | Notes                                                  |
|------------------------------------|---------------|--------------------------------------------------------|
| `verify/lattice_check.hexa`        | ✅ 10/10 PASS | σ=12, τ=4, φ=2, Hc2=σ·τ=48 T, master σ·φ=n·τ=24       |
| `verify/cross_doc_audit.hexa`      | ✅ 8/8 PASS   | lattice tokens + 6 falsifiers across spec/cli/roadmap |
| `verify/falsifier_check.hexa`      | ✅ 19/19 PASS | F-RTSC-{1,2,3} + F-SC-{1,2,3} monotone (no banned tokens) |
| `verify/run_all.hexa`              | ✅ 3/3 PASS   | aggregator                                             |
| `tests/test_*.hexa`                | ✅ 4/4 PASS   | selftest / lattice / verify / falsifier                |
| `hx install /path/to/hexa-rtsc`    | ✅ shim OK    | entry auto-detected (hexa.toml `[package].entry`)      |
| `hexa-rtsc {selftest,lattice,verify,status,rtsc,sc}` | ✅ all OK | sentinel-only — does NOT validate empirical RT-SC      |

`verify/` exits non-zero on lattice / cross-doc / falsifier drift; the
falsifier audit caught a real `.roadmap §A.4` gap on first run (F-SC-{1,2,3}
table rows missing) which was corrected in the same cycle.

---

## Cross-link — substrate-of-substrates downstream consumers

`hexa-rtsc` is the n=6 base substrate; the following sister substrates
depend on it:

- [need-singularity/hexa-fusion](https://github.com/need-singularity/hexa-fusion) — 48T SC coil dependency (σ·τ=48 confinement gate)
- [need-singularity/hexa-ufo](https://github.com/need-singularity/hexa-ufo) — Stage-1 Meissner levitation dependency (B-field expulsion)
- [need-singularity/hexa-cern](https://github.com/need-singularity/hexa-cern) — SC magnet dependency (accelerator beamline bending)

Their working status is upper-bounded by RT-SC empirical realisation. If
this substrate stays in SPEC_ONLY status, all three downstream substrates
also stay upper-bounded by current cryogenic SC technology.

---

## Architecture

```
hexa-rtsc/
├── README.md                     ← this file (public landing)
├── README.ai.md                  ← AI-native handoff (raw 271)
├── LICENSE                       ← MIT
├── CHANGELOG.md
├── RELEASE_NOTES_v1.0.0.md
├── .own                          ← project-local SSOT (mk2 own_v1) — n=6 lattice + falsifier + code-scope
├── .roadmap.hexa_rtsc            ← cross-cutting tracker — release cadence + falsifier preregister
├── hexa.toml                     ← package manifest (entry/[[bin]] auto-detected by hx)
├── install.hexa                  ← hx pre/post hook
├── cli/
│   └── hexa-rtsc.hexa            ← single-entry router (status / lattice / verify / selftest / rtsc / sc)
├── rtsc/                         ← T1 SPEC — extracted from n6-arch domains/energy/room-temp-sc/
│   ├── room-temp-sc.md
│   ├── *-verify.hexa             ← 10 application shells (move to module/applications/ in v1.1.0)
│   ├── arxiv-metadata.json
│   └── osf-metadata.json
├── sc/                           ← T1 SPEC — extracted from n6-arch domains/energy/superconductor/
│   └── superconductor.md
├── verify/                       ← runnable invariant audit (.hexa, hexa stdlib only)
│   ├── lattice_check.hexa        ← n=6 master identity (10/10 PASS expected)
│   ├── cross_doc_audit.hexa      ← cross-document lattice + falsifier presence (8/8)
│   ├── falsifier_check.hexa      ← F-RTSC/F-SC monotonicity (19/19)
│   └── run_all.hexa              ← orchestrator
├── tests/                        ← hexa native test runner
│   ├── test_selftest.hexa        ← sentinel sweep
│   ├── test_lattice.hexa         ← exercises verify/lattice_check
│   ├── test_verify.hexa          ← exercises verify/run_all
│   └── test_falsifier.hexa       ← exercises verify/falsifier_check
└── doc/
    └── lineage/
        └── origin.md             ← provenance manifest (n6-arch SHA, file-by-file)
```

The `core/<feature>/` + `module/<feature>/` + `README.ai.md` triplet
follows **hive raw.mk2 arch.001** — the canonical core-hierarchy pattern
shared with sister substrates `hexa-sscb` (compute axis, doc-first) and
`hexa-bio` (molecular toolkit). v1.0.0 keeps `rtsc/` + `sc/` flat; v1.1.0
will split them into `core/rtsc/` + `core/sc/` + `module/applications/`
per `.own` own 3 + `doc/lineage/origin.md` migration plan.

---

## Provenance

- RTSC spec **imported** from `n6-architecture/domains/energy/room-temp-sc/`
  (SHA `c0f1f570`, 2026-05-06).
- SC spec **imported** from `n6-architecture/domains/energy/superconductor/`
  (SHA `c0f1f570`, 2026-05-06).
- CLI dispatcher created **fresh** at extraction; `lattice` + `verify`
  subcommands wired 2026-05-07.
- Structural pattern (.own + README.ai.md + verify/ + doc/lineage/)
  aligned to `hexa-sscb` mk2 own_v1 on 2026-05-07.
- Sister-of-substrates extraction template: `hexa-bio` v1.0.0
  (need-singularity/hexa-bio, 2026-05-04).
- Full file-by-file provenance: [`doc/lineage/origin.md`](doc/lineage/origin.md).

---

## License

MIT. See [LICENSE](LICENSE).

---

## Cross-links

- Sister standalone: [`hexa-bio v1.0.0`](https://github.com/need-singularity/hexa-bio) (Molecular Toolkit substrate)
- Downstream consumer: [`hexa-fusion`](https://github.com/need-singularity/hexa-fusion) (48T SC coil dep)
- Downstream consumer: [`hexa-ufo`](https://github.com/need-singularity/hexa-ufo) (Meissner levitation dep)
- Downstream consumer: [`hexa-cern`](https://github.com/need-singularity/hexa-cern) (SC magnet dep)
- Upstream concept SSOT: `n6-architecture/domains/energy/room-temp-sc/room-temp-sc.md`
- Upstream concept SSOT: `n6-architecture/domains/energy/superconductor/superconductor.md`
