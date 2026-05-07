# firmware/ — hexa-rtsc Stage C/D HW prototype layer

> **Status (2026-05-08)**: pre-procurement skeleton. No board, no flash,
> no cold-test. Files compile via toolchain but cannot be verified
> without physical hardware.

Per `.roadmap.hexa_rtsc §A.6.1` recommended Stage C/D ordering:

| Subdir | Stage | Language | Toolchain | Purpose |
|:------|:------|:--------|:--------|:-------|
| `sim/` | C | hexa | hexa runtime | sim-only control logic, runs in CI |
| `hdl/` | D | Verilog 2001 | Vivado 2024.2 | FPGA quench-protection skeleton |
| `mcu/` | D | Rust no_std | cargo + thumbv7em-none-eabihf | STM32F4 chamber driver skeleton |

## sim/  (Stage C — sim-only, runs in CI)

| File | Purpose | Sentinel | Result |
|:-----|:--------|:--------|:------|
| `synthesis_ctrl.hexa` | Synthesis-chamber PID + interlock sim | `__HEXA_RTSC_FW_SIM_SYNTHESIS_CTRL__` | 7/7 PASS |
| `quench_logic.hexa`   | 48 T magnet quench-detection sim     | `__HEXA_RTSC_FW_SIM_QUENCH_LOGIC__`   | 15/15 PASS |

Run:
```
hexa run firmware/sim/synthesis_ctrl.hexa
hexa run firmware/sim/quench_logic.hexa
```

## hdl/  (Stage D — verified-compile only)

| File | Purpose | Toolchain | Status |
|:-----|:--------|:--------|:-------|
| `quench_detect.v` | Quench-detect FPGA Verilog skeleton | Vivado 2024.2 | not built |

Build (when Vivado available):
```
cd firmware/hdl
vivado -mode batch -source build.tcl    # TBD
```

## mcu/  (Stage D — verified-compile only)

| File | Purpose | Toolchain | Status |
|:-----|:--------|:--------|:-------|
| `chamber_drv.rs` | Synthesis chamber STM32F4 driver skeleton | `cargo build --target thumbv7em-none-eabihf` | not built |

Build (when target installed):
```
cd firmware/mcu
cargo build --release --target thumbv7em-none-eabihf
cargo test    # host-side unit tests work today
```

## Honesty contract

Per `.roadmap §A.6` and recipe `~/core/bedrock/docs/runnable_surface_recipe.md §9`:

- **Stage C** (`sim/`) closes today and runs in CI alongside `verify/*.hexa`.
- **Stage D** (`hdl/` + `mcu/`) compiles via toolchain but cannot
  validate functional correctness without physical board. Skeletons
  are spec-traceable to Stage A docs (`doc/{synthesis_bench_v0,
  48t_rebco_coil_v0}.md`) and Stage C sim test cases.

Real-hardware flash + cold-test → `.roadmap §A.6 Step 4` (Stage-2/3,
~2027-Q1+ ASPIRATIONAL).
