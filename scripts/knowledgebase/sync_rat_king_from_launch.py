#!/usr/bin/env python3
"""Generate the scoped Rat King launch record from pinned client 6737 data.

This importer updates only heroes/rat-king/{rat-king.yaml,rat-king.md}. It also
retains changed pre-release hero-data fields as explicitly non-launch evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_YAML = ROOT / "heroes/rat-king/rat-king.yaml"
OUTPUT_MD = ROOT / "heroes/rat-king/rat-king.md"
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import hero_rendering as descriptions  # noqa: E402
import hero_rendering as hero_helpers  # noqa: E402

CLIENT = 6737
SOURCE_REVISION = 11076133
COMMIT = "dc1679b9606effdc9bec37842ed40d8ca927092e"
SNAPSHOT_ID = "deadlock-data-client-6737"
AS_OF = "2026-10-02"
HERO_SOURCE = "github.deadlock-data.hero-data.dc1679b9606e"
ABILITY_SOURCE = "github.deadlock-data.ability-data.dc1679b9606e"
CARD_SOURCE = "github.deadlock-data.ability-cards.dc1679b9606e"
ENGLISH_SOURCE = "github.deadlock-data.english.dc1679b9606e"
NPC_SOURCE = "github.deadlock-data.npcs.dc1679b9606e"
PRE_RELEASE_SOURCE = "github.deadlock-data.gameplay.0d46cdecfccf"
RELEASE_SOURCE = "steam.news.rat-king-release.1845383656387709"
UPDATE_SOURCE = "wiki.update.2026-10-02.181191"
WIKI_SOURCE = "wiki.rat-king.180124"
ENGLISH_URL = f"https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/{COMMIT}/data/localizations/english.json"
EXPECTED_HASHES = {
    "version.txt": "df29482596536ea557dd79c6f20eab5fa16945c68dac6193b848ea829842c5fd",
    "hero-data.json": "791c09b89b66e7a2b7bc438f86c150b80ee921f75e86bef4c7a129910efcfcdc",
    "ability-data.json": "8bdc385cc78679bd6975b79baf6a1eee1e8cab8d769cd2fb9f5f46ceed1ea0fc",
    "ability-cards.json": "24a6b1a72da896652e35aed3846357b281a4a22f6e74b96d7d53f99c6a449bb6",
    "english.json": "0b92317324ebea77c0b4770bc93c23e0da7489a8dff347582273e7041f5eb292",
    "npc-data.json": "f8ceb65ac16c4378d324ad71c89b43665cadfaaaaa82d7fc8f876bfaea6da45a",
}
EXPECTED_PRE_RELEASE_HERO_SHA256 = "5bfc1e4fe3f35dfaefd49e814f8eb410bb3e42243a2e9233f0f7434d8a5cc2df"
AUXILIARY_ABILITY_KEYS = (
    "ability_ratking_entertunnel",
    "ability_ratking_standard_bearer_trigger",
    "citadel_ability_jump_ratking",
)


def read_json(path: Path) -> tuple[bytes, dict]:
    raw = path.read_bytes()
    return raw, json.loads(raw)


def build_document(inputs: dict[str, dict], pre_release_data: dict) -> dict:
    version = inputs["version.txt"]
    if "ClientVersion=6737" not in version or "SourceRevision=11076133" not in version:
        raise ValueError("Pinned version.txt does not identify client 6737 / revision 11076133")

    hero_data = inputs["hero-data.json"]
    ability_data = inputs["ability-data.json"]
    cards_data = inputs["ability-cards.json"]
    localization = inputs["english.json"]
    npc_data = inputs["npc-data.json"]
    source = hero_data.get("hero_ratking")
    previous = pre_release_data.get("hero_ratking")
    cards = cards_data.get("hero_ratking")
    if not all(isinstance(value, dict) for value in (source, previous, cards)):
        raise ValueError("Rat King data is missing from the pinned launch or pre-release input")

    bound = source.get("BoundAbilities") or {}
    if set(bound) != {"1", "2", "3", "4"}:
        raise ValueError("Expected four numbered Rat King ability bindings")
    abilities = []
    for slot in ("1", "2", "3", "4"):
        key = bound[slot]["Key"]
        card = cards.get(slot)
        if key not in ability_data or not isinstance(card, dict) or card.get("Key") != key:
            raise ValueError(f"Missing or mismatched client-6737 card/data for slot {slot}: {key}")
        abilities.append({
            "slot": int(slot),
            "name": card.get("Name") or bound[slot].get("Name"),
            "internal_key": key,
            "data": ability_data[key],
            "card": card,
            "descriptions": descriptions.resolve(card, localization, source=ENGLISH_SOURCE),
        })

    auxiliary = {}
    for key in AUXILIARY_ABILITY_KEYS:
        if key not in ability_data:
            raise ValueError(f"Missing expected supporting client ability record: {key}")
        auxiliary[key] = ability_data[key]
    if "npc_ratking_rat" not in npc_data:
        raise ValueError("Missing Rat King helper-rat NPC record")

    previous_values = {
        key: previous.get(key)
        for key in sorted(set(previous) | set(source))
        if previous.get(key) != source.get(key)
    }
    base_stats = {
        "maximum_health": source["MaxHealth"],
        "health_regeneration_per_second": source["BaseHealthRegen"],
        "light_melee_damage": source["LightMeleeDamage"],
        "heavy_melee_damage": source["HeavyMeleeDamage"],
        "move_speed_meters_per_second": source["MaxMoveSpeed"],
        "crouch_speed_meters_per_second": source["CrouchSpeed"],
        "sprint_speed_bonus_meters_per_second": source["SprintSpeed"],
        "move_acceleration_source_units": source["MoveAcceleration"],
        "ground_dash": {
            "speed_meters_per_second": source["GroundDashSpeed"],
            "distance_meters": source["GroundDashDistanceInMeters"],
            "duration_seconds": source["GroundDashDuration"],
        },
        "air_dash": {
            "speed_meters_per_second": source["AirDashSpeed"],
            "distance_meters": source["AirDashDistanceInMeters"],
            "duration_seconds": source["AirDashDuration"],
        },
        "stamina": {
            "charges": source["Stamina"],
            "cooldown_seconds": source["StaminaCooldown"],
            "regeneration_per_second": source["StaminaRegenPerSecond"],
        },
        "ability_resource": {
            "maximum": source["AbilityResourceMax"],
            "regeneration_per_second": source["AbilityResourceRegenPerSecond"],
        },
        "spirit_duration_bonus_percent": source["TechDuration"],
        "spirit_range_bonus_percent": source["TechRange"],
        "critical_damage_bonus_percent": source["CritDamageBonusPercent"],
        "critical_damage_received_percent": source["CritDamageReceivedPercent"],
        "bullet_lifesteal_effectiveness": source["HeroBulletLifestealEffectiveness"],
        "spirit_lifesteal_effectiveness": source["HeroSpiritLifestealEffectiveness"],
    }
    weapon_key = source["Weapon"].get("NameKey")
    localized_fields = {
        key: localization[value]
        for key, value in {
            "lore": source.get("Lore"),
            "weapon_name": weapon_key,
        }.items()
        if value and value in localization
    }

    return {
        "schema_version": 2,
        "id": "hero.rat-king",
        "snapshot_id": SNAPSHOT_ID,
        "client_version": CLIENT,
        "server_version": CLIENT,
        "source_revision": SOURCE_REVISION,
        "current_as_of": AS_OF,
        "evidence_status": "source_verified_with_official_release_confirmation",
        "sources": {
            "hero_data": HERO_SOURCE,
            "ability_data": ABILITY_SOURCE,
            "ability_cards": CARD_SOURCE,
            "ability_localization": ENGLISH_SOURCE,
            "support_npc_data": NPC_SOURCE,
            "pre_release_comparison": PRE_RELEASE_SOURCE,
            "release_announcement": RELEASE_SOURCE,
            "release_update_transcription": UPDATE_SOURCE,
            "later_wiki_context": WIKI_SOURCE,
        },
        "name": source["Name"],
        "aliases": [],
        "internal_hero_key": "hero_ratking",
        "hero_type": source.get("Type"),
        "role_localization_key": source.get("Role"),
        "playstyle_localization_key": source.get("Playstyle"),
        "localized_fields": localized_fields,
        "availability": {
            "selectable": source.get("IsSelectable"),
            "recommended": source.get("IsRecommended"),
            "disabled": source.get("IsDisabled"),
            "in_development": source.get("InDevelopment"),
            "in_hero_labs": source.get("InHeroLabs"),
            "released_date": AS_OF,
            "release_confirmed_by_official_announcement": True,
            "note": (
                "IsSelectable was already true in pre-release client 6731; the official "
                "October 2 announcement, not that flag alone, establishes public release."
            ),
        },
        "base_stats": base_stats,
        "per_boon_growth": source["LevelScaling"],
        "spirit_scaling": source.get("SpiritScaling") or {},
        "weapon": source["Weapon"],
        "generated_source_snapshot": {
            "client_version": CLIENT,
            "source_revision": SOURCE_REVISION,
            "source": HERO_SOURCE,
            "hero_data": source,
        },
        "abilities": abilities,
        "supporting_ability_data": {
            "not_numbered_in_hero_bound_abilities": True,
            "note": "These records are present in client ability data but are not among the four numbered ability-card bindings; do not infer control or runtime semantics from their presence alone.",
            "records": auxiliary,
        },
        "supporting_npc_data": {
            "note": "Raw `npc_ratking_rat` configuration; not a neutral-camp or selectable-hero record, and no placement or live availability is inferred.",
            "records": {"npc_ratking_rat": npc_data["npc_ratking_rat"]},
        },
        "pre_release_comparison": {
            "client_version": 6731,
            "source_revision": 11070267,
            "source": PRE_RELEASE_SOURCE,
            "status": "incomplete pre-release data; never use as launch values",
            "comparison_scope": "all top-level hero-data fields that differ between the pinned client 6731 and client 6737 records; values below are pre-release values only",
            "changed_hero_data_fields_before_release": previous_values,
        },
        "later_wiki_context": {
            "source": WIKI_SOURCE,
            "as_of": "2026-10-03",
            "evidence_status": "later_wiki_description_not_launch_runtime_test",
            "innate": "Can enter and exit map tunnels by crouching next to a vent; cannot enter while in combat.",
            "royal_pestments": "Spellbreaker does not proc on damage dealt to the barrier.",
            "scope_note": "Article marked Construction; these statements are separately dated, not inferred from launch configuration. They do not establish that tunnel vents are Steam Vents.",
        },
        "data_boundaries": [
            "Hero stats, ability data, cards, and localized descriptions are pinned to client 6737; they are generated data, not an independent runtime test.",
            "The October 2 official announcement establishes the release date. The pre-release IsSelectable flag does not establish release availability.",
            "The October 5 Rat King balance update is later and is not applied to this launch snapshot.",
        ],
    }


def render_info2(card: dict) -> str:
    info = card.get("Info2")
    if not isinstance(info, dict):
        return ""
    proxy = {"Info1": info}
    props = hero_helpers.card_properties(proxy)
    if not props:
        return ""
    lines = ["Additional card fields (source `Info2`):", "", "| Card field | Value |", "| --- | ---: |"]
    lines.extend(f"| {label} | {value} |" for label, value in props)
    if info.get("RequiresUpgradeIndex") is not None:
        lines += ["", f"`RequiresUpgradeIndex`: {info['RequiresUpgradeIndex']}"]
    return "\n".join(lines) + "\n\n"


def render_ability_descriptions(entries: list[dict], card: dict) -> str:
    base, info2, upgrades = [], [], []
    for entry in entries:
        paths = entry["card_paths"]
        if any(path == "card.DescKey" or path.startswith("card.Info1.") for path in paths):
            base.append(entry)
        if any(path.startswith("card.Info2.") for path in paths):
            info2.append(entry)
        if any(".Upgrades[" in path for path in paths):
            upgrades.append(entry)

    lines = ["<!-- ability-descriptions:start -->", "**Description** (pinned English game text):", ""]
    for entry in dict.fromkeys(item["localization_key"] for item in base):
        value = next(item["plain_text"] for item in base if item["localization_key"] == entry)
        lines.extend("> " + paragraph for paragraph in value.splitlines())
        lines.append("")
    if info2:
        condition = card.get("Info2", {}).get("RequiresUpgradeIndex")
        heading = "**Additional Info2 description**"
        if condition is not None:
            heading += f" (`RequiresUpgradeIndex: {condition}`)"
        lines += [heading + ":", ""]
        for entry in info2:
            if any(".Upgrades[" in path for path in entry["card_paths"]):
                continue
            lines.extend("- " + paragraph for paragraph in entry["plain_text"].splitlines())
        lines.append("")
    upgrade_descriptions = []
    for entry in upgrades:
        for path in entry["card_paths"]:
            match = re.search(r"\.Upgrades\[(\d+)\]", path)
            if match:
                upgrade_descriptions.append((int(match.group(1)) + 1, entry["plain_text"]))
    if upgrade_descriptions:
        lines += ["**Upgrade descriptions** (where supplied by the source):", ""]
        for tier, text in sorted(set(upgrade_descriptions)):
            lines.append(f"- **Tier {tier}:** {text.replace(chr(10), ' ')}")
        lines.append("")
    for entry in entries:
        if entry.get("quality_note"):
            lines += [f"**Source warning** (`{entry['localization_key']}`): {entry['quality_note']}", ""]
    lines += [
        f"Description source: [`{ENGLISH_SOURCE}`]({ENGLISH_URL}). "
        "Bracketed controls denote bindable actions, not default keys. "
        "Canonical YAML retains original text and localization keys.",
        "<!-- ability-descriptions:end -->",
        "",
    ]
    return "\n".join(lines)


def render_growth(values: dict) -> str:
    if not values:
        return ""
    lines = [
        "## Per-Boon Growth",
        "",
        "Configured `LevelScaling` fields from the launch client; keys and values are preserved without deriving a live-match growth formula.",
        "",
        "| Source field | Value per boon |",
        "| --- | ---: |",
    ]
    lines.extend(f"| `{key}` | {value} |" for key, value in values.items())
    return "\n".join(lines) + "\n\n"


def render_markdown(document: dict) -> str:
    sources = list(dict.fromkeys(document["sources"].values()))
    lines = [
        "---",
        "id: hero.rat-king",
        "title: Rat King",
        "domain: heroes",
        "topics: [hero, abilities]",
        "aliases: []",
        "summary: Rat King's October 2 release snapshot, with source-shaped stats, abilities, and upgrade cards.",
        f"snapshot_id: {SNAPSHOT_ID}",
        f'current_as_of: "{AS_OF}"',
        f"evidence_status: {document['evidence_status']}",
        "sources:",
        *(f"  - {source}" for source in sources),
        "---",
        "",
        "# Rat King",
        "",
        "Valve announced Rat King as available to play on October 2, 2026. Client",
        "6737 also marks him selectable and binds four numbered abilities. The",
        "selectable flag was already true in pre-release client 6731, so the",
        "official release announcement—not that field alone—establishes the date.",
        "",
        hero_helpers.render_base_stats(document["base_stats"]),
        render_growth(document["per_boon_growth"]),
        hero_helpers.render_weapon(document["weapon"]),
        "## Abilities",
        "",
    ]
    for ability in document["abilities"]:
        lines += [
            f"### {ability['slot']}. {ability['name']}",
            "",
            f"Internal key: `{ability['internal_key']}`.",
            "",
            render_ability_descriptions(ability["descriptions"], ability["card"]),
            hero_helpers.render_ability_stats(ability),
        ]
        info2 = render_info2(ability["card"])
        if info2:
            lines.append(info2)
    lines += [
        "## Supporting Client Records",
        "",
        "The YAML preserves additional unnumbered ability records and the",
        "`npc_ratking_rat` NPC record from client 6737. They are not treated",
        "as extra numbered hero abilities or as neutral-camp placement data.",
        "",
        "## Later Wiki Context (October 3)",
        "",
        "The [early article revision](https://deadlock.wiki/Rat_King?oldid=180124),",
        "marked Construction, describes these separately dated behaviors:",
        "",
        "- " + document["later_wiki_context"]["innate"],
        "- Royal Pestments: " + document["later_wiki_context"]["royal_pestments"],
        "",
        "These are wiki descriptions, not independent launch-day runtime tests.",
        "Tunnel vents are not identified as Steam Vents by this evidence.",
        "",
        "## Data Boundaries",
        "",
        "- The launch fields and card/localization text are generated client data, not independent runtime tests.",
        "- The pre-release comparison is retained only to prevent incomplete client-6731 values from being mistaken for launch stats.",
        "- October 5 balance changes are outside this snapshot.",
        "",
        "Release evidence: [official Steam announcement](https://store.steampowered.com/news/app/1422450/view/703281025618281704?l=english).",
        "Client data: [pinned client 6737 commit](https://github.com/deadlock-wiki/deadlock-data/tree/" + COMMIT + ").",
        "",
    ]
    return "\n".join(lines)


def generate(data_dir: Path, pre_release_hero_data: Path) -> tuple[str, str]:
    raw: dict[str, bytes] = {}
    inputs: dict[str, dict] = {}
    for name, expected_hash in EXPECTED_HASHES.items():
        raw[name] = (data_dir / name).read_bytes()
        actual = hashlib.sha256(raw[name]).hexdigest()
        if actual != expected_hash:
            raise ValueError(f"{name} SHA-256 mismatch: expected {expected_hash}, got {actual}")
        inputs[name] = raw[name].decode("utf-8") if name == "version.txt" else json.loads(raw[name])
    pre_raw = pre_release_hero_data.read_bytes()
    pre_hash = hashlib.sha256(pre_raw).hexdigest()
    if pre_hash != EXPECTED_PRE_RELEASE_HERO_SHA256:
        raise ValueError(
            "pre-release hero-data SHA-256 mismatch: "
            f"expected {EXPECTED_PRE_RELEASE_HERO_SHA256}, got {pre_hash}"
        )
    pre_data = json.loads(pre_raw)
    document = build_document(inputs, pre_data)
    yaml_text = json.dumps(document, ensure_ascii=False, indent=2) + "\n"
    return yaml_text, render_markdown(document)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", required=True, type=Path, help="Pinned client-6737 JSON files")
    parser.add_argument("--pre-release-hero-data", required=True, type=Path, help="Client-6731 hero-data.json")
    parser.add_argument("--check", action="store_true", help="Fail if generated hero files differ")
    args = parser.parse_args()
    yaml_text, markdown = generate(args.data_dir, args.pre_release_hero_data)
    if args.check:
        if not OUTPUT_YAML.exists() or OUTPUT_YAML.read_text() != yaml_text:
            raise SystemExit(f"{OUTPUT_YAML} is out of sync with the pinned launch inputs")
        if not OUTPUT_MD.exists() or OUTPUT_MD.read_text() != markdown:
            raise SystemExit(f"{OUTPUT_MD} is out of sync with the pinned launch inputs")
        return
    OUTPUT_YAML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_YAML.write_text(yaml_text)
    OUTPUT_MD.write_text(markdown)


if __name__ == "__main__":
    main()
