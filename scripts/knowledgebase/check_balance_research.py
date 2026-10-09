#!/usr/bin/env python3
"""Verify downloaded October 4/5 research inputs and reproduce the delta ledger.

Read-only and offline. Input filenames are CLIENT/PATH with slashes in PATH
replaced by double underscores. No canonical record is generated or changed.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "patches/research/2026-10-05"
DATASETS = ("hero-data", "ability-data", "ability-cards", "npc-data",
            "street-brawl-data", "convars", "item-data", "generic-data", "misc-data")


def differences(before, after, path=""):
    if type(before) == type(after) and isinstance(before, dict):
        for key in sorted(before.keys() | after.keys()):
            child = path + "." + key
            if key not in before:
                yield child, "<absent>", after[key]
            elif key not in after:
                yield child, before[key], "<absent>"
            else:
                yield from differences(before[key], after[key], child)
    elif type(before) == type(after) and isinstance(before, list) and len(before) == len(after):
        for index, (old, new) in enumerate(zip(before, after)):
            yield from differences(old, new, f"{path}[{index}]")
    elif before != after:
        yield path, before, after


def verify(directory):
    manifest = json.loads((RESEARCH / "input-manifest.json").read_text())
    inputs = {}
    for entry in manifest:
        path = directory / str(entry["client"]) / entry["path"].replace("/", "__")
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != entry["sha256"]:
            raise ValueError(f"Hash mismatch: {path}")
        if entry["path"].endswith(".json"):
            inputs[entry["client"], entry["path"]] = json.loads(raw)
    lines = []
    for name in DATASETS:
        for old, new in ((6737, 6746), (6746, 6753)):
            key = f"data/json/{name}.json"
            for path, before, after in differences(inputs[old, key], inputs[new, key]):
                lines.append(f"{old}→{new} {name}{path}: "
                             f"{json.dumps(before, ensure_ascii=False)} → {json.dumps(after, ensure_ascii=False)}")
    if "\n".join(lines) + "\n" != (RESEARCH / "field-deltas.txt").read_text():
        raise ValueError("Recorded delta ledger differs from pinned inputs")
    # These extra datasets were explicitly reported unchanged in the review.
    for name in ("item-cards", "hero-meaningful-stats"):
        key = f"data/json/{name}.json"
        if not inputs[6737, key] == inputs[6746, key] == inputs[6753, key]:
            raise ValueError(f"Unexpected {name} change")
    return len(manifest), len(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs-dir", type=Path, required=True)
    args = parser.parse_args()
    count, deltas = verify(args.inputs_dir)
    print(f"PASS: {count} hash-pinned inputs; {deltas} ledger deltas reproduced; no canonical writes")


if __name__ == "__main__":
    main()
