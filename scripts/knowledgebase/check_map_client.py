#!/usr/bin/env python3
"""Cross-check scoped map records against three local, hash-pinned client-6731 files.

Read-only and offline. This verifies source fields, not gameplay behavior or wiki
interpretation. No map source exports or full upstream datasets are published.
"""
import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "github.deadlock-data.gameplay.0d46cdecfccf"


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


def pinned_json(path, expected):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError(f"SHA-256 mismatch: {path}")
    return json.loads(raw)


def validate(npcs, misc, generic):
    errors = []

    def equal(actual, expected, label):
        if actual != expected:
            errors.append(f"{label}: {actual!r} != source {expected!r}")

    for slug, key in [("small-neutral", "neutral_trooper_weak"),
                      ("medium-neutral", "neutral_trooper_normal"),
                      ("large-neutral", "neutral_trooper_strong")]:
        record = load(f"npcs/{slug}/{slug}.yaml")
        raw = npcs[key]
        for local, source in [("base_max_health", "MaxHealth"),
                              ("damage_growth_percent_per_minute", None)]:
            expected = raw[source] if source else raw["NeutralDamageGrowth"]["DamageGrowthPctPerMin"]
            equal(record["combat"][local], expected, f"{slug}.{local}")
        modifiers = raw["IntrinsicModifiers"][0]
        for local, source in [("bullet_resistance_percent", "BULLET_DAMAGE_REDUCTION_PERCENT"),
                              ("spirit_resistance_percent", "ABILITY_DAMAGE_REDUCTION_PERCENT")]:
            equal(record["combat"][local], modifiers[source], f"{slug}.{local}")
        for local, source in [("bullet_damage", "BulletDamage"), ("rounds_per_second", "RoundsPerSecond"),
                              ("damage_per_second", "DPS"), ("range", "FalloffStartRange")]:
            equal(record["ranged_attack"][local], raw["Weapon"][source], f"{slug}.{local}")
        equal(record["camp"]["initial_spawn"], raw["InitialSpawnDelay"], f"{slug}.spawn")
        equal(record["camp"]["respawn_after_full_clear"], raw["SpawnInterval"], f"{slug}.respawn")
        equal(record["reward"]["base_unsecured_souls"], raw["GoldReward"], f"{slug}.bounty")
        equal(record["reward"]["growth_percent_of_base_per_minute"], raw["GoldRewardBonusPercentPerMinute"], f"{slug}.bounty-growth")
        for field in ("SightRangePlayers", "SightRangeNPCs"):
            equal(record["targeting_configuration"][field], raw[field], f"{slug}.{field}")

    boss = load("npcs/mid-boss/mid-boss.yaml")
    raw = npcs["npc_super_neutral"]
    for local, source in [("base_max_health", "StartingHealth"), ("health_growth_per_minute", "HealthGainPerMinute")]:
        equal(boss["combat"][local], raw[source], f"mid-boss.{local}")
    for local, source in [("health_regen_per_second", "HEALTH_REGEN_PER_SECOND"),
                          ("bullet_resistance_percent", "BULLET_ARMOR_DAMAGE_RESIST"),
                          ("spirit_resistance_percent", "ABILITY_DAMAGE_REDUCTION_PERCENT"),
                          ("status_resistance_percent", "STATUS_RESISTANCE")]:
        equal(boss["combat"][local], raw["IntrinsicModifiers"][0][source], f"mid-boss.{local}")
    for local, source in [("bullet_damage", "BulletDamage"), ("rounds_per_second", "RoundsPerSecond"),
                          ("damage_per_second", "DPS"), ("range", "FalloffStartRange")]:
        equal(boss["ranged_attack"][local], raw["Weapon"][source], f"mid-boss.{local}")
    equal(boss["spawn"]["initial"], raw["InitialSpawnDelay"], "mid-boss.initial")
    equal(boss["spawn"]["respawn_intervals_after_defeats"][0], raw["SpawnInterval"], "mid-boss.first-respawn")
    for local, source in [("base", "BaseAbsorptionPerSecond"), ("growth_per_minute", "ScalingAbsorptionPerMinute")]:
        equal(boss["combat"]["shield_absorption_per_second"][local], raw["ShieldLogic"][source], f"mid-boss.shield.{local}")

    rules = load("data/map-interactions.yaml")
    sinner = npcs["neutral_sinners_sacrifice"]
    for key, value in rules["sinners"]["configured_minigame_fields"].items():
        equal(value, sinner[key], f"sinner.{key}")
    equal(rules["sinners"]["reward_model"]["raw_gold_reward"], sinner["GoldReward"], "sinner.raw-reward")
    snacks = rules["healing_snacks"]
    equal(snacks["initial_spawn_seconds"], misc["citadel_pickup_floating_health"]["SpawnDelay"], "snack.initial")
    equal(snacks["respawn_after_pickup_seconds"], misc["citadel_pickup_floating_health"]["RespawnTime"], "snack.respawn")
    pickup = misc["citadel_pickup_health_float_in_world"]
    equal(snacks["duration_seconds"], pickup["RegenDuration"], "snack.duration")
    equal(snacks["total_heal_max_health_percent"], pickup["RegenMaxHealthPercent"]["Base"], "snack.heal")
    for kind, prop, pickup_key in [("ordinary_crates", "citadel_breakable_prop_wooden_crate", "small_gold_pickup"),
                                   ("tough_crates", "citadel_breakable_prop_tough_crate", "big_gold_pickup")]:
        local = rules["breakables"][kind]
        equal(local["configured_drop_chance_percent"], misc[prop]["PowerupDropChance"], f"{kind}.chance")
        equal(local["reward_base"], misc[pickup_key]["GoldAmount"], f"{kind}.base")
        equal(local["reward_growth_per_match_minute"], misc[pickup_key]["GoldPerMinuteAmount"], f"{kind}.growth")
    tough = misc["citadel_breakable_prop_tough_crate"]
    for local, key in [("heavy_melee_hits_to_break", "HeavyMeleeHitCount"), ("no_melee_cleave", "NoMeleeCleave"),
                       ("damaged_by_bullets", "DamagedByBullets"), ("damaged_by_abilities", "DamagedByAbilities"),
                       ("damaged_by_slide", "DamagedBySlide"), ("break_on_dodge_touch", "BreakOnDodgeTouch")]:
        equal(rules["breakables"]["tough_crates"][local], tough[key], f"tough.{local}")
    equal(rules["buff_containers"]["configured_drop_chance_percent"], misc["citadel_breakable_item_container"]["PowerupDropChance"], "buff.chance")
    for descriptor in rules["breakables"]["schedule_mapping"]["descriptors"]:
        raw = generic["BreakableSpawnTimeDesc"][descriptor["index"] - 1]
        equal(descriptor["initial_seconds"], raw["InitialSpawnTime"], f"schedule.{descriptor['index']}.initial")
        equal(descriptor["respawn_seconds"], raw["RespawnInterval"], f"schedule.{descriptor['index']}.respawn")
    weights = generic["BreakablePowerupLootParams"]["PickupsByMatchTimeMins"]["0"]
    equal(sum(weights.values()), rules["buff_containers"]["client_weight_ratios"]["total_weight"], "buff.total-weight")
    timings = load("data/map-timings.yaml")
    for tier, suffix in enumerate(("", "_lv2", "_lv3")):
        for field, prefix in [("fire_rate_percent", "firerate"), ("ammo_capacity_percent", "ammo"),
                              ("cooldown_reduction_percent", "cd"), ("weapon_damage_percent", "wp"),
                              ("health", "hp"), ("spirit_power", "spirit")]:
            values = misc[f"{prefix}_permanent_pickup{suffix}"]["Modifer"]["ScriptValues"]
            equal(timings["golden_statue_buffs"][tier][field], values[0]["value"], f"buff.{tier}.{field}")
        for field, prefix in [("bullet_resist", "bulletresist"), ("spirit_resist", "spiritresist"),
                              ("ability_range", "range"), ("move_speed", "movespeed")]:
            values = misc[f"{prefix}_permanent_pickup{suffix}"]["Modifer"]["ScriptValues"]
            entry = timings["buff_container_additional_buffs"]["buffs"][field]
            local_key = "raw_source_units_by_tier" if field == "move_speed" else "source_values_by_tier"
            equal(entry[local_key][tier], values[0]["value"], f"buff.{tier}.{field}")
            if field == "ability_range":
                equal(len(values), 2 if tier == 0 else 1, f"buff.{tier}.radius-presence")
                if tier == 0:
                    radius = entry["tier_1_additional_radius_modifier"]
                    equal(radius["modifier"], values[1]["ModifierValue"], "buff.radius-modifier")
                    equal(radius["source_value"], values[1]["value"], "buff.radius-value")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("npc", "misc", "generic"):
        parser.add_argument(f"--{name}-data", type=Path, required=True)
    args = parser.parse_args()
    source = next(s for s in load("sources/source-registry.yaml")["sources"] if s["id"] == SOURCE)
    values = [pinned_json(getattr(args, f"{name}_data"), source[f"{name}_data_sha256"])
              for name in ("npc", "misc", "generic")]
    errors = validate(*values)
    if errors:
        raise SystemExit("Map client cross-check failed:\n" + "\n".join(errors))
    print("PASS: scoped NPC/map fields match hash-pinned client 6731; wiki/runtime interpretations not tested")


if __name__ == "__main__":
    main()
