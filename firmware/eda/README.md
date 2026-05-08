# firmware/eda/ — Phase E1 KiCad schematic skeleton + EDA BOM

> **Status (2026-05-08)**: Phase E1 paper-design + KiCad-CLI verified-parse
> path. Phase E2 (PCB layout fab, $25k procurement) deferred per
> `.roadmap §A.6 Step 2`.

Per `.roadmap.hexa_rtsc §A.6.1` extension beyond Phase D+, this directory
adds the **schematic + EDA BOM + Gerber-build script** layer: the natural
bridge from `firmware/hdl/constraints.xdc` (FPGA pin assignments) to
actual PCB fabrication.

## Files

| File | Type | Purpose |
|:----|:----|:--------|
| `quench_detect.kicad_sch` | KiCad 7+ schematic (S-expr text format) | Top-level schematic skeleton: 8 ICs (FPGA + 2 ADC + 2 diff-amp + 2 isolator + opto), net labels per `firmware/hdl/constraints.xdc`, signal-path topology |
| `quench_detect.kicad_pro` | KiCad project file | Net classes (Default / POWER / DIFF_LVDS), ERC severity rules, PCB design defaults |
| `quench_detect.kicad_pcb` | TBD | Phase E2 deliverable (PCB layout, $25k procurement) |
| `bom_kicad.csv` | EDA-format BOM | 18 part rows + PCB/PCBA targets, Manufacturer + MPN + Vendor + Cost columns |
| `build_kicad.py` | Python 3.10+ | Wrapper around `kicad-cli` (ERC, netlist, BOM, Gerber). Skip gracefully when KiCad not installed. |

## Phase E sub-stages

```
Phase E1 (this commit)          : KiCad schematic skeleton + EDA BOM + build script
                                  — verified-parse (when kicad-cli installed)
                                  — open-source-EDA, no commercial license
                                  — $0 cost, runs today via brew install
Phase E2 (~2026-Q4)             : PCB layout (kicad_pcb) + Gerber + DRC
                                  — requires schematic finalization
                                  — verified-fab via PCBWay quote
                                  — $200 PCB pilot, $400 PCBA per board
Phase E3 (Stage 4 = §A.6 Step 4): Bring-up + cold-test on Cernox + REBCO
                                  — Step 4 hardware procurement complete
                                  — physical board flashed + first quench-test
                                  — out of code-layer scope, $25k+
```

## Build (when KiCad installed)

```bash
brew install --cask kicad           # macOS
# OR: apt install kicad             # Linux

cd firmware/eda
python3 build_kicad.py erc          # ERC report on schematic
python3 build_kicad.py netlist      # generate kicadsexpr netlist
python3 build_kicad.py bom          # auto-generate BOM CSV
python3 build_kicad.py gerber       # → Gerber files (Phase E2 only)
python3 build_kicad.py all          # all of the above
```

When KiCad is **not** installed, `build_kicad.py` exits cleanly with a
SKIP message — Phase E1 contract is "skeleton-checked-into-repo,
verified-parse-when-toolchain-available". This matches the Phase D
honesty model (HDL/MCU compile via toolchain but no flash).

## Spec traceability

Every component in `bom_kicad.csv` traces to:

1. `firmware/doc/chip_design.md` §1 silicon inventory
2. `firmware/doc/pinout_summary.md` datasheet-link table
3. `firmware/hdl/constraints.xdc` pin assignments (FPGA side)
4. `doc/48t_rebco_coil_v0.md` §3 BOM (board-level cross-reference)

| `bom_kicad.csv` ref | Justification | Verified by |
|:-------------------:|:--------------|:-----------:|
| U1 XC7A35T          | doc §1 silicon row 2; constraints.xdc clk_100mhz_i E3 | tb_quench_detect 12/12 |
| U2/U3 LTC2378-20    | doc §1 row 7 (REBCO ADC); constraints.xdc v_rebco_i[15:0] | sim quench_logic 15/15 |
| U4/U5 AD8429        | doc §3 power budget (4×80mA = 0.32W); chip_design.md ASCII schematic | (matches doc §4) |
| U6/U7 ISO224        | doc §3 power budget; chip_design.md cryogen boundary | (matches doc §4) |
| U8 TLP358           | doc §1 silicon row 9 (gate driver opto, 250 ns) | constraints.xdc igbt_gate_o D4 |
| Y1 100 MHz osc      | constraints.xdc create_clock period 10 ns | (Vivado timing) |
| TOTAL board cost    | bom_kicad.csv subtotal $3,242.10 / 5 boards = $648/board | matches firmware/build/bom.csv "PCB + PCBA pilot" row |

## Honesty contract

Phase E1 ships:

- **Schematic skeleton** in KiCad 7+ S-expression format (`.kicad_sch`).
  This is text-format and can be inspected via any text editor; KiCad
  required for graphical view + DRC.
- **EDA-format BOM** with full Manufacturer + MPN + Vendor + Datasheet
  columns suitable for direct paste into PCBWay / JLCPCB quote.
- **Python wrapper** (`build_kicad.py`) that calls `kicad-cli` for
  verified-parse + ERC + netlist + BOM auto-generation.

Phase E1 does **NOT** ship:

- PCB layout (`.kicad_pcb`) — Phase E2 deliverable.
- Gerber / drill files — Phase E2 deliverable.
- Physical board — Phase E3 (= `.roadmap §A.6` Step 4).
- Functional verification — Phase E3 (cold-test on real REBCO + Cernox).

## Reproducibility

```bash
git clone https://github.com/dancinlab/hexa-rtsc
cd hexa-rtsc/firmware/eda

# Optional toolchain install:
brew install --cask kicad      # macOS
# OR: apt install kicad        # Linux

python3 build_kicad.py all      # → ERC + netlist + BOM (when kicad-cli present)
                                # OR clean SKIP (when not present)

# Manual inspection:
cat quench_detect.kicad_sch     # text-format S-expression
cat bom_kicad.csv               # EDA-format BOM
```

## Cross-references

- `firmware/doc/chip_design.md` — silicon inventory + pin assignments + ASCII schematic
- `firmware/hdl/constraints.xdc` — FPGA-side pin map (Vivado XDC)
- `firmware/build/bom.csv` — master master BOM (system-level, includes
  cryostat / NHMFL Bitter / SQUID)
- `doc/48t_rebco_coil_v0.md` — Stage A bench spec ($3.3M / 31 mo)
- `.roadmap.hexa_rtsc §A.6 Step 2` — funding round ($25k PCB pilot tier)
- `.roadmap.hexa_rtsc §A.6 Step 4` — Stage 2/3 actual board cold-test
