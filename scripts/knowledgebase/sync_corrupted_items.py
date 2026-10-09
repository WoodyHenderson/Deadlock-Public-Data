#!/usr/bin/env python3
"""Extract the pinned client-6726 CorruptedUpgrades fields into a dated sidecar.

The sidecar records source-shaped variant, penalty, and mode-configuration
fields only. It does not imply that a corrupted variant was purchasable in any
mode or that its configuration values were observed in a live match.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data/corrupted-items.yaml"
EXPECTED_ITEM_DATA_SHA256 = "1aeec7caea984d22df2ae81737190008435ee9b68045fb8b14e1fdcc98d553bf"
EXPECTED_GENERIC_DATA_SHA256 = "f8c4601602ee89217ba45f7404230b2278abfa5b5f54ba30109a2cfa77805e29"
SOURCE_ID = "github.deadlock-data.gameplay.3d26c988891f"
GENERIC_SOURCE_ID = "github.deadlock-data.gameplay.3d26c988891f"
PATCH_SOURCE_ID = "wiki.update.2026-09-29.181123"
EXPECTED_ITEM_COUNT = 95


def build_document(item_data: dict, generic_data: dict) -> dict:
    items = {
        key: record["CorruptedUpgrades"]
        for key, record in sorted(item_data.items())
        if isinstance(record, dict) and "CorruptedUpgrades" in record
    }
    if len(items) != EXPECTED_ITEM_COUNT:
        raise ValueError(f"Expected {EXPECTED_ITEM_COUNT} corrupted item records, found {len(items)}")
    if any(not isinstance(upgrades, dict) or not upgrades for upgrades in items.values()):
        raise ValueError("CorruptedUpgrades values must be non-empty objects")
    return {
        "schema_version": 1,
        "id": "data.corrupted-items",
        "snapshot_id": "deadlock-data-client-6726",
        "current_as_of": "2026-09-30",
        "evidence_status": "source_verified_structured_variant_fields",
        "sources": list(dict.fromkeys([SOURCE_ID, GENERIC_SOURCE_ID, PATCH_SOURCE_ID])),
        "field_sources": {
            "item_corrupted_upgrades": SOURCE_ID,
            "penalty_definitions": GENERIC_SOURCE_ID,
            "street_brawl_configuration": GENERIC_SOURCE_ID,
            "street_brawl_patch_intent": PATCH_SOURCE_ID,
        },
        "availability": {
            "mode": "unresolved",
            "date_range": "unresolved",
            "note": (
                "A configured CorruptedUpgrades field is not evidence that the item "
                "or variant was available in a live match or purchasable in a given mode."
            ),
        },
        "scope": (
            "Source-shaped CorruptedUpgrades, penalty, and Street Brawl mode "
            "fields only; no shop pricing, variant eligibility, or runtime "
            "availability is inferred."
        ),
        "item_corrupted_upgrades": items,
        "penalty_definitions": generic_data.get("m_vecCorruptedPenaltyDefs"),
        "street_brawl_configuration": {
            "corrupt_item_round": generic_data["StreetBrawl"]["m_iCorruptItemRound"],
            "buy_time_seconds_by_round": generic_data["StreetBrawl"]["m_vecBuyTime"],
            "source": GENERIC_SOURCE_ID,
            "patch_note_intent": "one corrupted item is granted after the Round 5 item draft",
            "patch_note_source": PATCH_SOURCE_ID,
        },
    }


def serialize(document: dict) -> str:
    # JSON is valid YAML 1.2 and preserves the source's scalar types exactly.
    return json.dumps(document, indent=2, ensure_ascii=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--item-data", required=True, type=Path, help="Pinned client-6726 item-data.json")
    parser.add_argument("--generic-data", required=True, type=Path, help="Pinned client-6726 generic-data.json")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true", help="Fail if the generated sidecar differs")
    args = parser.parse_args()

    item_raw = args.item_data.read_bytes()
    item_hash = hashlib.sha256(item_raw).hexdigest()
    if item_hash != EXPECTED_ITEM_DATA_SHA256:
        raise SystemExit(f"item-data SHA-256 mismatch: expected {EXPECTED_ITEM_DATA_SHA256}, got {item_hash}")
    generic_raw = args.generic_data.read_bytes()
    generic_hash = hashlib.sha256(generic_raw).hexdigest()
    if generic_hash != EXPECTED_GENERIC_DATA_SHA256:
        raise SystemExit(f"generic-data SHA-256 mismatch: expected {EXPECTED_GENERIC_DATA_SHA256}, got {generic_hash}")
    item_data = json.loads(item_raw)
    generic_data = json.loads(generic_raw)
    penalties = generic_data.get("m_vecCorruptedPenaltyDefs")
    if not isinstance(penalties, list) or len(penalties) != 11:
        raise ValueError("Expected 11 source-defined corrupted-item penalty records")
    generated = serialize(build_document(item_data, generic_data))

    if args.check:
        if not args.output.exists() or args.output.read_text() != generated:
            raise SystemExit(f"{args.output} is not synchronized with the pinned client-6726 input")
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(generated)


if __name__ == "__main__":
    main()
