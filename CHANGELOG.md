# Changelog

All notable changes to **hexa-rtsc** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and SemVer.

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

- `need-singularity/hexa-fusion` — 48T SC coil dependency
- `need-singularity/hexa-ufo` — Stage-1 Meissner levitation dependency
- `need-singularity/hexa-cern` — SC magnet dependency

[1.0.0]: https://github.com/need-singularity/hexa-rtsc/releases/tag/v1.0.0
