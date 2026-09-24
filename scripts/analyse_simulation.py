#!/usr/bin/env python3
"""Résumé reproductible d'un CSV exclusivement simulé ; bibliothèque standard."""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path
from statistics import mean

DEFAULT_CSV = Path(__file__).resolve().parents[1] / "examples/simulation/mesures.csv"
REQUIRED = {"source", "device", "band", "simulated", "elapsed_s",
            "power_antenna_dbm", "power_w", "duration_s", "energy_j"}

def summarize(path: Path) -> dict:
    groups = {}
    count = 0
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, delimiter=";")
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError("Colonnes manquantes : " + ", ".join(sorted(missing)))
        for number, row in enumerate(reader, 2):
            if row["simulated"].strip().lower() != "true":
                raise ValueError(f"Ligne {number} : données non simulées ; analyse refusée.")
            values = {}
            for field in ("elapsed_s", "power_antenna_dbm", "power_w", "duration_s", "energy_j"):
                try:
                    value = float(row[field])
                except (ValueError, TypeError) as exc:
                    raise ValueError(f"Ligne {number} : {field} doit être numérique.") from exc
                if not math.isfinite(value):
                    raise ValueError(f"Ligne {number} : {field} doit être fini.")
                values[field] = value
            if any(values[f] < 0 for f in ("elapsed_s", "power_w", "duration_s", "energy_j")):
                raise ValueError(f"Ligne {number} : temps, puissance W ou énergie négatifs.")
            key = (row["source"], row["device"], row["band"])
            group = groups.setdefault(key, [])
            if group and values["elapsed_s"] < group[-1]["elapsed_s"]:
                raise ValueError(f"Ligne {number} : temps décroissant dans une même voie.")
            if not math.isclose(values["energy_j"], values["power_w"] * values["duration_s"],
                                rel_tol=1e-6, abs_tol=1e-18):
                raise ValueError(f"Ligne {number} : énergie incompatible avec puissance × durée.")
            group.append(values)
            count += 1
    if not count:
        raise ValueError("Le CSV ne contient aucun enregistrement.")
    result = {"simulation_only": True, "record_count": count, "channels": []}
    for (source, device, band), rows in sorted(groups.items()):
        dbm = [r["power_antenna_dbm"] for r in rows]
        watts = [r["power_w"] for r in rows]
        average_w = mean(watts)
        result["channels"].append({
            "source": source, "device": device, "band": band, "record_count": len(rows),
            "observed_span_s": rows[-1]["elapsed_s"] - rows[0]["elapsed_s"],
            "sum_configured_durations_s": math.fsum(r["duration_s"] for r in rows),
            "power_min_dbm": min(dbm), "power_max_dbm": max(dbm),
            "power_mean_w": average_w,
            "power_mean_dbm_from_w": 10 * math.log10(average_w) + 30 if average_w > 0 else None,
            "estimated_energy_j": math.fsum(r["energy_j"] for r in rows),
        })
    return result

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--output", type=Path, help="Enregistrer aussi le résumé JSON.")
    args = parser.parse_args()
    try:
        result = summarize(args.csv)
        text = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        if args.output:
            if args.output.resolve() == args.csv.resolve():
                raise ValueError("Le résumé ne doit pas remplacer le CSV source.")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
    except (OSError, ValueError, csv.Error) as exc:
        parser.exit(2, f"Erreur : {exc}\n")
    print(text, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
