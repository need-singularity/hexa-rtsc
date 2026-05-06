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

Verdict: **SPEC_ONLY** (0/2 verbs wired; 2/2 spec + falsifier preregister).

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

### Via `hx` (recommended, when registered)

```bash
hx install hexa-rtsc          # global, pulls latest from registry
hx install hexa-rtsc@1.0.0    # pin specific version
hexa-rtsc --version           # → 1.0.0
```

### Via git clone (works today)

```bash
git clone https://github.com/need-singularity/hexa-rtsc.git ~/.hexa-rtsc
export HEXA_RTSC_ROOT=~/.hexa-rtsc
export PATH="$HEXA_RTSC_ROOT/cli:$PATH"

# Run any subcommand:
hexa run $HEXA_RTSC_ROOT/cli/hexa-rtsc.hexa selftest
```

### Quick Start

```bash
hexa-rtsc selftest      # 2-spec sentinel sweep
hexa-rtsc status        # verb table + verdict + caveats
hexa-rtsc rtsc          # RTSC spec excerpt + falsifier preregister
hexa-rtsc sc            # SC   spec excerpt + falsifier preregister
```

---

## Verb status table

| Verb   | Status        | n=6 lattice candidate          | Empirical sandbox     |
|--------|---------------|--------------------------------|-----------------------|
| `rtsc` | SPEC v1.0.0   | Tc=300K, σ·τ=48T, φ=2          | UNPROVEN (TBD)        |
| `sc`   | SPEC v1.0.0   | Cooper φ=2, Abrikosov CN=6     | UNPROVEN (TBD)        |

Verdict: **SPEC_ONLY** (0/2 verbs wired; 2/2 spec + falsifier preregister).

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
/Users/ghost/core/hexa-rtsc/
├── cli/
│   └── hexa-rtsc.hexa            # 2-verb router + status + selftest (PLACEHOLDER)
├── rtsc/                         # SPEC — extracted from n6-arch room-temp-sc/
│   ├── room-temp-sc.md
│   ├── *-verify.hexa             # 10 verify shells (downstream applications)
│   ├── arxiv-metadata.json
│   └── osf-metadata.json
├── sc/                           # SPEC — extracted from n6-arch superconductor/
│   └── superconductor.md
├── tests/
│   └── test_selftest.hexa
├── install.hexa                  # hx hook (pre/post)
├── hexa.toml                     # package manifest
├── LICENSE                       # MIT
├── CHANGELOG.md
├── RELEASE_NOTES_v1.0.0.md
└── README.md                     # (this file)
```

---

## Provenance

- RTSC spec **imported** from `n6-architecture/domains/energy/room-temp-sc/`
  (SHA `c0f1f570`, 2026-05-06).
- SC spec **imported** from `n6-architecture/domains/energy/superconductor/`
  (SHA `c0f1f570`, 2026-05-06).
- CLI dispatcher created **fresh** as placeholder during this extraction.
- Sister-of-substrates extraction template: `hexa-bio` v1.0.0
  (need-singularity/hexa-bio, 2026-05-04).

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
