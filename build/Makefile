# hexa-rtsc/build/Makefile — pandoc + xelatex PDF rebuild
#
# Recipe §1 slot #12. Builds three corpora:
#   1. pillar specs    (rtsc/room-temp-sc.md, sc/superconductor.md)
#   2. roadmap         (.roadmap.hexa_rtsc)
#   3. hardware specs  (doc/{synthesis_bench, 48t_rebco_coil,
#                            calorimetry_rig}_v0.md, firmware/doc/*.md)
#
# Sister of hexa-cern's build/Makefile (same xelatex+header.tex pattern,
# different doc set). Independent of firmware/build/Makefile (which
# orchestrates HDL + MCU + iverilog testbenches — no doc overlap).
#
# Toolchain:
#   - pandoc          ≥ 2.19 (Markdown reader + LaTeX writer)
#   - xelatex         (TeX Live ≥ 2022 recommended)
#   - tlmgr packages  fontspec, xeCJK, unicode-math, hyperref, geometry,
#                     amsmath, amssymb, longtable, booktabs, microtype,
#                     fvextra, xcolor
#   - fonts           TeX Gyre Termes/Heros/Cursor + Noto Sans CJK KR
#                     (latter required for Korean prose in pillar specs)
#
# Targets:
#   make pillars      → rtsc.pdf + sc.pdf
#   make roadmap      → roadmap.pdf
#   make hardware     → 5 hw_*.pdf (3 doc/ + 2 firmware/doc/)
#   make all          → pillars + roadmap + hardware
#   make clean        → rm -rf out/
#
# Outputs land in build/out/ (gitignored — ephemeral artefacts).
#
# Honesty contract reminder (closure-honesty memory): rebuilding a PDF
# from a pillar spec does NOT advance T1/T2/T3 closure — the math
# already lives in calc_*.hexa + numerics_*.hexa. PDFs are reader-
# facing distribution artifacts, not predicate-bearing surfaces.

ROOT     := $(shell git rev-parse --show-toplevel 2>/dev/null || pwd)
HEADER   := $(ROOT)/build/header.tex
OUT      := $(ROOT)/build/out

PANDOC   := pandoc
PFLAGS   := --pdf-engine=xelatex \
            --include-in-header=$(HEADER) \
            --variable=geometry:a4paper,margin=2.5cm \
            --variable=fontsize:11pt \
            --variable=lang:ko \
            --highlight-style=tango \
            --table-of-contents \
            --toc-depth=3 \
            --number-sections

# ─── corpora ───────────────────────────────────────────────────────────

PILLAR_SRC := $(ROOT)/rtsc/room-temp-sc.md \
              $(ROOT)/sc/superconductor.md
PILLAR_PDF := $(OUT)/rtsc.pdf $(OUT)/sc.pdf

ROADMAP_SRC := $(ROOT)/.roadmap.hexa_rtsc
ROADMAP_PDF := $(OUT)/roadmap.pdf

HW_SRC := $(ROOT)/doc/synthesis_bench_v0.md \
          $(ROOT)/doc/48t_rebco_coil_v0.md \
          $(ROOT)/doc/calorimetry_rig_v0.md \
          $(ROOT)/firmware/doc/chip_design.md \
          $(ROOT)/firmware/doc/pinout_summary.md
HW_PDF := $(OUT)/hw_synthesis_bench.pdf \
          $(OUT)/hw_48t_rebco_coil.pdf \
          $(OUT)/hw_calorimetry_rig.pdf \
          $(OUT)/hw_chip_design.pdf \
          $(OUT)/hw_pinout_summary.pdf

ALL_PDF := $(PILLAR_PDF) $(ROADMAP_PDF) $(HW_PDF)

# ─── default + meta targets ───────────────────────────────────────────

.PHONY: all pillars roadmap hardware clean help check-tools

all: pillars roadmap hardware

pillars: $(PILLAR_PDF)

roadmap: $(ROADMAP_PDF)

hardware: $(HW_PDF)

help:
	@echo "hexa-rtsc/build — pandoc + xelatex PDF rebuild"
	@echo ""
	@echo "Targets:"
	@echo "  make pillars      → out/rtsc.pdf + out/sc.pdf"
	@echo "  make roadmap      → out/roadmap.pdf"
	@echo "  make hardware     → out/hw_*.pdf (5 docs)"
	@echo "  make all          → all of the above"
	@echo "  make clean        → rm -rf out/"
	@echo "  make check-tools  → verify pandoc + xelatex + fonts present"
	@echo ""
	@echo "Outputs land in $(OUT) (gitignored)."

check-tools:
	@command -v $(PANDOC) >/dev/null 2>&1 || \
		{ echo "ERROR: pandoc not found. install: brew install pandoc"; exit 1; }
	@command -v xelatex   >/dev/null 2>&1 || \
		{ echo "ERROR: xelatex not found. install MacTeX/TeX Live."; exit 1; }
	@$(PANDOC) --version | head -1
	@xelatex --version | head -1
	@echo "build toolchain present."

clean:
	rm -rf $(OUT)

# ─── per-target rules ─────────────────────────────────────────────────

$(OUT):
	@mkdir -p $(OUT)

$(OUT)/rtsc.pdf: $(ROOT)/rtsc/room-temp-sc.md $(HEADER) | $(OUT)
	$(PANDOC) $(PFLAGS) \
		--metadata=title:"hexa-rtsc — Room-Temp Superconductor pillar" \
		--metadata=subtitle:"n=6 closed-form spec (RT-SC)" \
		-o $@ $<

$(OUT)/sc.pdf: $(ROOT)/sc/superconductor.md $(HEADER) | $(OUT)
	$(PANDOC) $(PFLAGS) \
		--metadata=title:"hexa-rtsc — Superconductor pillar" \
		--metadata=subtitle:"BCS / Cooper / Abrikosov n=6 closed-form" \
		-o $@ $<

$(OUT)/roadmap.pdf: $(ROOT)/.roadmap.hexa_rtsc $(HEADER) | $(OUT)
	$(PANDOC) $(PFLAGS) \
		--metadata=title:"hexa-rtsc — Roadmap (§A invariant lattice + falsifier)" \
		-o $@ $<

$(OUT)/hw_synthesis_bench.pdf: $(ROOT)/doc/synthesis_bench_v0.md $(HEADER) | $(OUT)
	$(PANDOC) $(PFLAGS) \
		--metadata=title:"Synthesis bench v0 — RT-SC candidate growth" \
		-o $@ $<

$(OUT)/hw_48t_rebco_coil.pdf: $(ROOT)/doc/48t_rebco_coil_v0.md $(HEADER) | $(OUT)
	$(PANDOC) $(PFLAGS) \
		--metadata=title:"48 T REBCO coil v0 — F-RTSC-3 hardware" \
		-o $@ $<

$(OUT)/hw_calorimetry_rig.pdf: $(ROOT)/doc/calorimetry_rig_v0.md $(HEADER) | $(OUT)
	$(PANDOC) $(PFLAGS) \
		--metadata=title:"Calorimetry rig v0 — F-SC-3 ΔC/γTc bench" \
		-o $@ $<

$(OUT)/hw_chip_design.pdf: $(ROOT)/firmware/doc/chip_design.md $(HEADER) | $(OUT)
	$(PANDOC) $(PFLAGS) \
		--metadata=title:"Chip design — STM32F407 + Artix-7 11-IC inventory" \
		-o $@ $<

$(OUT)/hw_pinout_summary.pdf: $(ROOT)/firmware/doc/pinout_summary.md $(HEADER) | $(OUT)
	$(PANDOC) $(PFLAGS) \
		--metadata=title:"Pinout summary — chamber + calorimetry + DAQ" \
		-o $@ $<
