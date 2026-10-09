#!/usr/bin/env python3
"""Read-only adjacent-client audit for the October 2 release review.

Accepts ordinary filenames or the cached data__json__ filenames. Every input is
hash-checked against the source registry before any field comparisons.
This verifies configuration differences, not runtime or wiki behavior.
"""
import argparse
import hashlib
import json
from pathlib import Path

import yaml

KB = Path(__file__).resolve().parents[2]
EXPECTED_CHANGES = {
    "generic-data": set(),
    "item-data": set(),
    "item-cards": set(),
    "ability-data": {
        "ability_ratking_entertunnel", "ability_ratking_ratarmor",
        "ability_ratking_ratnibble", "ability_ratking_scrap_grenade",
        "ability_ratking_standard_bearer", "ability_ratking_standard_bearer_trigger",
        "citadel_ability_jump_ratking",
    },
    "ability-cards": {"hero_ratking"},
    "hero-data": {"hero_ratking", "hero_baba", "hero_familiar", "hero_necro",
                  "hero_unicorn", "hero_werewolf", "hero_werewolf_transformed"},
    "hero-meaningful-stats": {"HeroBulletLifestealEffectiveness", "HeroSpiritLifestealEffectiveness"},
    "misc-data": {"citadel_pickup_health_float_in_world", "medic_trooper_aoe_health_pickup_amber",
                  "medic_trooper_aoe_health_pickup_sapphire"},
    "npc-data": {"npc_neutral_bug", "npc_neutral_bug_rat", "npc_neutral_bug_rat_swarm", "npc_ratking_rat"},
    "street-brawl-data": {"item-buckets"},
    "convars": {"citadel_corrupted_item_shop_enabled", "citadel_ping_can_heal_range",
                "citadel_settings_default_view", "citadel_settings_remember_selected_hero",
                "r_particle_explicit_fetch"},
}


def read_inputs(directory, source):
    result = {}
    for name in EXPECTED_CHANGES:
        candidates = (directory / f"{name}.json", directory / f"data__json__{name}.json")
        path = next((p for p in candidates if p.exists()), candidates[0])
        raw = path.read_bytes()
        key = name.replace("-", "_") + "_sha256"
        if hashlib.sha256(raw).hexdigest() != source[key]:
            raise ValueError(f"{path}: SHA-256 differs from registry")
        result[name] = json.loads(raw)
    return result


def check(before, after):
    errors = []
    for name, expected in EXPECTED_CHANGES.items():
        old, new = before[name], after[name]
        changed = {key for key in old.keys() | new.keys() if old.get(key) != new.get(key)}
        if changed != expected:
            errors.append(f"{name}: changed keys {sorted(changed)} != {sorted(expected)}")
    old, new = before["convars"], after["convars"]
    if old["citadel_corrupted_item_shop_enabled"] is not True or new["citadel_corrupted_item_shop_enabled"] is not False:
        errors.append("Broker enabled-state transition differs")
    if new["citadel_ping_can_heal_range"]["value"] != 2500:
        errors.append("Healing-ping source-unit range differs")
    timings = yaml.safe_load((KB / "data/map-timings.yaml").read_text())
    broker = next(e for e in timings["events"] if e["id"] == "broker.corrupted-item-shop")
    if broker["configured_enabled"] != new["citadel_corrupted_item_shop_enabled"]:
        errors.append("Canonical Broker state differs from launch input")
    if before["npc-data"]["npc_neutral_bug"]["RespawnTime"] != 30 or after["npc-data"]["npc_neutral_bug"]["RespawnTime"] != 15:
        errors.append("Neutral-bug respawn transition differs")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pre-release-dir", type=Path, required=True)
    parser.add_argument("--launch-dir", type=Path, required=True)
    args = parser.parse_args()
    registry = yaml.safe_load((KB / "sources/source-registry.yaml").read_text())
    sources = {s["id"]: s for s in registry["sources"]}
    before = read_inputs(args.pre_release_dir, sources["github.deadlock-data.gameplay.0d46cdecfccf"])
    after = read_inputs(args.launch_dir, sources["github.deadlock-data.gameplay.dc1679b9606e"])
    errors = check(before, after)
    if errors:
        raise SystemExit("\n".join(errors))
    print("PASS: 22 hash-pinned inputs; client 6731→6737 changed-key inventory and scoped launch fields agree")


if __name__ == "__main__":
    main()
