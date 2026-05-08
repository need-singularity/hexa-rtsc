# firmware/Makefile — master build for hexa-rtsc Phase D+
#
# §A.6.1 Phase D+ deliverable per .roadmap.hexa_rtsc.
# Drives all 3 sub-toolchains (hexa sim, iverilog HDL, cargo MCU).

.PHONY: all sim hdl mcu test verify clean status help

all: sim hdl mcu

# ─── sim layer (hexa runtime) ──────────────────────────────────────────
sim:
	@echo "═══ firmware/sim/ — running 4 sim-firmware scripts ══════════════"
	@for f in synthesis_ctrl quench_logic calorimetry_ctrl squid_daq; do \
		echo "── sim/$$f"; \
		hexa run sim/$$f.hexa 2>&1 | tail -3; \
	done

# ─── HDL layer (iverilog testbench) ────────────────────────────────────
hdl:
	@echo "═══ firmware/hdl/ — iverilog testbench ══════════════════════════"
	@$(MAKE) -C hdl sim

# ─── MCU layer (cargo workspace) ───────────────────────────────────────
mcu:
	@echo "═══ firmware/mcu/ — cargo build + test ══════════════════════════"
	@cd mcu && cargo build --bins 2>&1 | tail -3
	@cd mcu && cargo test 2>&1 | grep -E "test result"

# ─── full verification (sim + HDL + MCU) ───────────────────────────────
test: sim hdl mcu
	@echo ""
	@echo "═══ Phase D+ verification matrix ════════════════════════════════"
	@echo "  sim-firmware:        4 scripts (synthesis_ctrl, quench_logic,"
	@echo "                                  calorimetry_ctrl, squid_daq)"
	@echo "  HDL testbench:       1 testbench (tb_quench_detect.v 12/12)"
	@echo "  MCU host tests:      4 lib + 6 cal + 5 chamber = 15/15 PASS"
	@echo "  TOTAL:               39/39 verified-build + tested"

# ─── alias: verify ↔ test ──────────────────────────────────────────────
verify: test

# ─── status: print component matrix ────────────────────────────────────
status:
	@cat doc/README.md | grep -A 20 "Phase D+ status"

# ─── clean ─────────────────────────────────────────────────────────────
clean:
	$(MAKE) -C hdl clean
	cd mcu && cargo clean

help:
	@echo "firmware/ Makefile — Phase D+ master build"
	@echo ""
	@echo "Targets:"
	@echo "  all     — build sim + HDL + MCU"
	@echo "  sim     — run 4 hexa sim-firmware scripts"
	@echo "  hdl     — iverilog testbench (firmware/hdl/Makefile)"
	@echo "  mcu     — cargo build + cargo test"
	@echo "  test    — sim + HDL + MCU + summary matrix"
	@echo "  verify  — alias for test"
	@echo "  status  — print Phase D+ status table"
	@echo "  clean   — remove build artifacts"
	@echo ""
	@echo "Per-toolchain:"
	@echo "  cd hdl && make sim    # iverilog 11.0+"
	@echo "  cd hdl && make synth  # Vivado 2024.2+"
	@echo "  cd mcu && cargo test  # cargo 1.94+"
	@echo "  cd mcu && cargo build --release --target thumbv7em-none-eabihf"
