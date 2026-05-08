#!/usr/bin/env python3
"""
build_kicad.py — KiCad CLI wrapper for hexa-rtsc Phase E1 verified-parse.

§A.6.1 Phase E1 deliverable per .roadmap.hexa_rtsc.

Runs `kicad-cli` to verify schematic + PCB files parse correctly without
running KiCad GUI. Generates ERC report, BOM CSV, and Gerber output if
schematic/PCB are valid.

Honesty: KiCad CLI verifies syntax + ERC. It does NOT validate against
real-board functionality. Phase E2 (procurement + first PCB fab + cold-
test) requires actual PCB and is out of code-layer scope (~$25k).

Usage:
    python3 build_kicad.py erc           # ERC report on schematic
    python3 build_kicad.py netlist       # generate netlist from schematic
    python3 build_kicad.py gerber        # PCB → Gerber files (requires .kicad_pcb)
    python3 build_kicad.py bom           # generate BOM CSV
    python3 build_kicad.py all           # all of the above

Requires:
    KiCad 7.0+ installed (kicad-cli must be in PATH).
    macOS:  brew install --cask kicad
    Linux:  apt install kicad
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent.resolve()
SCH_FILE = THIS_DIR / "quench_detect.kicad_sch"
PCB_FILE = THIS_DIR / "quench_detect.kicad_pcb"   # TBD — Phase E1 schematic-only for now
PROJ_FILE = THIS_DIR / "quench_detect.kicad_pro"
BOM_CSV = THIS_DIR / "bom_kicad.csv"
OUT_DIR = THIS_DIR / "build"


def find_kicad_cli():
    """Locate kicad-cli; return path or None."""
    cli = shutil.which("kicad-cli")
    if cli:
        return cli
    # macOS app bundle fallback
    candidates = [
        "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli",
        "/Applications/KiCad/kicad-cli",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    return None


def run_cmd(cmd, label):
    """Run shell command, print output, return returncode."""
    print(f"  → {label}")
    print(f"    cmd: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        print(f"    [TIMEOUT] command exceeded 120 s")
        return 124
    print(result.stdout.strip())
    if result.stderr.strip():
        print(f"    stderr: {result.stderr.strip()}")
    return result.returncode


def cmd_erc(cli):
    """Run ERC (electrical rules check) on schematic."""
    OUT_DIR.mkdir(exist_ok=True)
    cmd = [
        cli, "sch", "erc",
        "--output", str(OUT_DIR / "erc_report.txt"),
        "--format", "report",
        str(SCH_FILE)
    ]
    return run_cmd(cmd, "ERC report")


def cmd_netlist(cli):
    """Generate netlist from schematic."""
    OUT_DIR.mkdir(exist_ok=True)
    cmd = [
        cli, "sch", "export", "netlist",
        "--output", str(OUT_DIR / "netlist.net"),
        "--format", "kicadsexpr",
        str(SCH_FILE)
    ]
    return run_cmd(cmd, "Netlist (KiCad S-expr)")


def cmd_bom(cli):
    """Generate BOM CSV from schematic."""
    OUT_DIR.mkdir(exist_ok=True)
    cmd = [
        cli, "sch", "export", "bom",
        "--output", str(OUT_DIR / "bom_generated.csv"),
        "--fields", "Reference,Value,Footprint,Manufacturer,MPN,Datasheet",
        str(SCH_FILE)
    ]
    return run_cmd(cmd, "BOM CSV")


def cmd_gerber(cli):
    """Generate Gerber files from PCB layout (Phase E2)."""
    if not PCB_FILE.exists():
        print(f"    [SKIP] {PCB_FILE.name} not yet authored — Phase E2 deliverable.")
        print(f"           Phase E1 contract: schematic-only (this commit).")
        return 0
    OUT_DIR.mkdir(exist_ok=True)
    gerber_dir = OUT_DIR / "gerbers"
    gerber_dir.mkdir(exist_ok=True)
    cmd = [
        cli, "pcb", "export", "gerbers",
        "--output", str(gerber_dir),
        "--layers", "F.Cu,B.Cu,F.Mask,B.Mask,F.SilkS,B.SilkS,Edge.Cuts",
        str(PCB_FILE)
    ]
    return run_cmd(cmd, "Gerber files")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("step", choices=["erc", "netlist", "bom", "gerber", "all"])
    args = parser.parse_args()

    cli = find_kicad_cli()
    if not cli:
        print("=========================================================================")
        print("  [SKIP] kicad-cli not found in PATH or /Applications/KiCad/")
        print("         Install via:  brew install --cask kicad   (macOS)")
        print("                       apt install kicad           (Linux/Ubuntu)")
        print("         This script verifies schematic parse + ERC + BOM gen.")
        print("         Without KiCad, Phase E1 status: skeleton-only (verified-not-tested).")
        print("=========================================================================")
        # Phase E1 honesty: skeleton is checked into repo, parse not verified locally.
        # CI on a Linux runner with KiCad available WILL run this.
        sys.exit(0)

    print(f"=========================================================================")
    print(f"  hexa-rtsc Phase E1 — KiCad CLI build")
    print(f"  cli: {cli}")
    print(f"  sch: {SCH_FILE}")
    print(f"  pcb: {PCB_FILE} {'(present)' if PCB_FILE.exists() else '(TBD Phase E2)'}")
    print(f"=========================================================================")

    rc = 0
    if args.step in ("erc", "all"):
        rc |= cmd_erc(cli)
    if args.step in ("netlist", "all"):
        rc |= cmd_netlist(cli)
    if args.step in ("bom", "all"):
        rc |= cmd_bom(cli)
    if args.step in ("gerber", "all"):
        rc |= cmd_gerber(cli)

    print()
    if rc == 0:
        print("  __HEXA_RTSC_EDA_BUILD__ PASS")
    else:
        print(f"  __HEXA_RTSC_EDA_BUILD__ FAIL (rc={rc})")
    sys.exit(rc)


if __name__ == "__main__":
    main()
