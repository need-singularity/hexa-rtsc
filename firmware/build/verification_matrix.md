# Phase D+ verification matrix — hexa-rtsc firmware/

> §A.6.1 Phase D+ deliverable per `.roadmap.hexa_rtsc`. This is the
> single-page status board for the entire hardware-prototype layer.

## Matrix view

| Bench / subsystem | Stage A spec | Sim ([.hexa](../sim/)) | HDL ([.v](../hdl/)) | MCU ([.rs](../mcu/)) | Chip design ([doc/](../doc/)) | EDA schematic ([eda/](../eda/)) | Status |
|:----|:----|:--:|:--:|:--:|:--:|:--:|:------:|
| Synthesis chamber | [synthesis_bench_v0.md](../../doc/synthesis_bench_v0.md) | synthesis_ctrl ✓ 7/7 | — | chamber_drv ✓ 5/5 | ✓ | synthesis_chamber.kicad_sch ✓ | **5/6** |
| 48 T REBCO coil   | [48t_rebco_coil_v0.md](../../doc/48t_rebco_coil_v0.md)     | quench_logic ✓ 15/15 | quench_detect + tb ✓ 12/12 | — | ✓ | quench_detect.kicad_sch + .kicad_pcb skel ✓ | **6/6** |
| Calorimetry rig   | [calorimetry_rig_v0.md](../../doc/calorimetry_rig_v0.md)   | calorimetry_ctrl ✓ 12/12 | calorimetry_daq ✓ compile | calorimetry_drv ✓ 6/6 | ✓ | calorimetry_rig.kicad_sch ✓ | **6/6** |
| SQUID DAQ pipeline| synthesis_bench_v0.md §6  | squid_daq ✓ 9/9 | — | — (host-side via PyVISA TBD) | ✓ | squid_host_adapter.kicad_sch ✓ | **4/6** |
| Power tree (shared) | firmware/doc/chip_design.md §6 | — | — | — | ✓ | power_tree.kicad_sch ✓ | **2/6** |

## Test count per layer

| Layer | Component | Tests | Status |
|:------|:----------|:----:|:------:|
| sim   | synthesis_ctrl.hexa     | 7  | ✓ |
| sim   | quench_logic.hexa       | 15 | ✓ |
| sim   | calorimetry_ctrl.hexa   | 12 | ✓ |
| sim   | squid_daq.hexa          | 9  | ✓ |
| hdl   | tb_quench_detect.v      | 12 | ✓ |
| mcu   | lib.rs (anchors+pid+telemetry) | 4 | ✓ |
| mcu   | chamber_drv.rs          | 5  | ✓ |
| mcu   | calorimetry_drv.rs      | 6  | ✓ |
| **TOTAL** | **8 components** | **70** | **70/70 PASS** |

Plus verify/ runtime tier (separate from firmware/):

| Tier | Scripts | Tests |
|:----|:-------|:------|
| T1 algebraic | 6  | (calc_*.hexa pass count varies) |
| T2 numerical | 17 | 113+ lint checks (cross_pillar adds 12 inter-pillar invariants) |
| T3 archival  | 6  | per-empirical 3/3 |
| meta         | 3  | falsifier 43/43 + lint 119/119 + saturation 9/9 (recipe §7.3) |

## Toolchain status

| Tool | Version | Status | Used for |
|:----|:--------|:-------|:--------|
| hexa runtime | 0.x (homebrew) | ✓ today | sim-firmware + verify/ |
| iverilog | 11.0 | ✓ today (homebrew) | HDL testbench |
| cargo + rustc | 1.94+ | ✓ today (rustup) | MCU host build + tests |
| thumbv7em-none-eabihf | rust target | ✓ available (rustup target add) | MCU embedded cross-compile |
| Vivado | 2024.2 | ✗ not installed | HDL synth + impl + bitstream |
| OpenOCD / probe-rs | latest | ✗ not installed | flash (no board) |

## Bridge to physical hardware

| Phase | Deliverable | Cost (cum.) | Time | Status |
|:-----:|:-----------|:-----------:|:----:|:------:|
| **A** | 3 hardware design docs | $0 | 1 d | ✓ pushed 702ad75 |
| **B** | 3 sim-parity scripts (DFT/TDGL/WHH) | $0 | 1 d | ✓ pushed e983f10 |
| **C** | 2 sim-firmware (synthesis + quench) | $0 | 1 d | ✓ pushed 89c031f |
| **D** | HDL + MCU skeletons | $0 | 1 d | ✓ pushed 71c3202 |
| **D+ HDL** | testbench + 2 modules + Vivado tcl | $0 | 1 d | ✓ pushed 35f0ebb |
| **D+ MCU** | workspace + lib + 2nd binary + 15 tests | $0 | 1 d | ✓ pushed bbb00b0 |
| **D+ doc** | chip design + schematics + pinout | $0 | 1 d | ✓ pushed 2e53cdd |
| **D+ sim** | calorimetry_ctrl + squid_daq | $0 | 1 d | ✓ pushed c39a8e2 |
| **D+ build** | this Makefile + bom.csv + matrix | $0 | 1 d | ✓ pushed b2584e9 |
| **D+ md**    | comprehensive .md doc refresh    | $0 | 1 d | ✓ pushed fe7e021 |
| **E1**       | KiCad schematic (1 board) + EDA BOM + build script | $0 | 1 d | ✓ pushed 8f74f28 |
| **E1+**      | 4 schematics + power-tree subsheet + PCB skeleton + multi-target build | $0 | 1 d | ← this commit |
| **E2**       | PCB layout placement + routing + Gerber + DRC | $1k | 2 mo | ✗ funding-gated |
| **E3**       | Cold-test on real REBCO + Cernox         | $25k | 4 mo | ✗ §A.6 Step 4 |
| **Step 1** | external collab decision (NIMS / NHMFL / Lake Shore) | $20k pre-dev | 2–4 mo | ✗ |
| **Step 2** | Funding round + PCB pilot (5 boards × 3 designs) | +$15k | 2 mo | ✗ |
| **Step 2.5** | Procurement (silicon + Cs + AMI 4Q) | +$140k | 6 mo | ✗ |
| **Step 4** | PCBA + bring-up + cold test | +$50k | 4 mo | ✗ |
| **Total to first flashed firmware** | | **~$225k** | **14–20 mo** | |

## Reproducibility

```bash
git clone https://github.com/dancinlab/hexa-rtsc
cd hexa-rtsc/firmware
brew install icarus-verilog            # iverilog dependency
make test                               # → 70/70 PASS

# Per-layer:
make sim                                # 4 sim-firmware scripts
make hdl                                # iverilog testbench (12/12)
make mcu                                # cargo build + cargo test (15/15)
```

## Honesty contract

This matrix represents **paper design + verified-compile + sim-PASS**.
No PCB exists. No silicon procured. No board flashed. No cold-test
performed. All claims are spec-traceable to either:

1. Stage A bench specs (`doc/*_v0.md`)
2. Phase B sim-parity scripts (`verify/numerics_*.hexa`)
3. Phase C/D code (`firmware/sim/, hdl/, mcu/`)
4. Vendor datasheets (referenced in `firmware/doc/pinout_summary.md`)

Real-hardware closure is **out of code-layer scope** per `.roadmap §A.6`
(estimated $225k + 14-20 mo from funding round).
