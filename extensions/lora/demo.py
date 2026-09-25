#!/usr/bin/env python3
"""Démonstration LoRa simulée par défaut ; réception série JSON en option."""
from __future__ import annotations
import argparse
from dataclasses import asdict
import json
import queue
import sys
from lora_driver import LoRaSimulationDriver, LoRaSerialJSONDriver, time_on_air_seconds

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--serial-port", help="Récepteur JSON série, par exemple /dev/ttyUSB1.")
    parser.add_argument("--baudrate", type=int, default=115200)
    parser.add_argument("--timeout", type=float, default=15.0, help="Attente maximale par paquet.")
    args = parser.parse_args()
    if args.count < 1 or args.timeout <= 0 or args.baudrate <= 0:
        parser.error("count, timeout et baudrate doivent être positifs.")
    packets = queue.Queue()
    log = lambda message: print(message, file=sys.stderr)
    driver = (LoRaSerialJSONDriver(args.serial_port, args.baudrate, packets.put, log)
              if args.serial_port else LoRaSimulationDriver(packets.put, log, interval_s=0.1))
    try:
        driver.start()
        for _ in range(args.count):
            packet = packets.get(timeout=args.timeout)
            data = asdict(packet)
            data["simulated"] = args.serial_port is None
            data["estimated_duration_s"] = time_on_air_seconds(
                packet.payload_length, packet.spreading_factor, packet.bandwidth_khz,
                int(packet.coding_rate.split("/")[-1]))
            print(json.dumps(data, ensure_ascii=False, allow_nan=False), flush=True)
    except queue.Empty:
        parser.exit(2, "Aucun paquet reçu dans le délai imparti.\n")
    except (OSError, RuntimeError, ValueError, ZeroDivisionError) as exc:
        parser.exit(2, f"Erreur LoRa : {exc}\n")
    except KeyboardInterrupt:
        return 130
    finally:
        driver.stop()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

