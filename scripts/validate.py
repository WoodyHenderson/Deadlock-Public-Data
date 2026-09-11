#!/usr/bin/env python3
"""Validate this standalone data snapshot offline; never fetch or modify files."""
from collections import Counter
from datetime import date
from hashlib import sha256
from math import isclose
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


def walk(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)
    elif isinstance(value, str):
        yield value


def allowed_source(url):
    parsed = urlsplit(url)
    if parsed.scheme != "https":
        return False
    if parsed.netloc in {"deadlock.wiki", "deadlock-api.com", "api.deadlock-api.com"}:
        return True
    return (parsed.netloc in {"github.com", "raw.githubusercontent.com"}
            and parsed.path.startswith("/deadlock-wiki/deadlock-data/"))


def card_refs(value, prefix="card"):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "DescKey":
                yield prefix + "." + key, child.lstrip("#")
            else:
                yield from card_refs(child, prefix + "." + key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from card_refs(child, prefix + f"[{i}]")


def validate_lifesteal(records, source_ids):
    """Check curation consistency, not whether the rules match runtime behavior."""
    rules = records["data/universal-rules.yaml"]["healing"]["lifesteal"]
    entries = rules["target_specific_effects"]
    effects = {e["id"]: e for e in entries}
    check(len(effects) == len(entries), "Duplicate lifesteal effect IDs")
    for effect in entries:
        check(effect.get("source") in source_ids, f"Lifesteal source: {effect['id']}")
        check(effect.get("record") in records, f"Lifesteal record: {effect['id']}")

    # Compare curated fractions to their pinned ability fields, including upgrades.
    # Scorn's source values are already ratios; the other fields are percentages.
    for name, divisor, tier in [
        ("abrams.siphon-life", 100, None),
        ("warden.last-stand", 100, None),
        ("lash.flog", 100, None),
        ("mo-and-krill.scorn", 1, None),
        ("bebop.hyper-beam.tier-3", 100, 3),
    ]:
        effect = effects.get(name)
        check(effect is not None, f"Missing lifesteal effect: {name}")
        if effect is None or effect.get("record") not in records:
            continue
        fields = effect.get("source_fields", [])
        check(len(fields) == 2, f"Lifesteal source fields: {name}")
        if len(fields) != 2:
            continue
        candidates = []
        for ability in records[effect["record"]].get("abilities", []):
            data = ability["data"]
            if tier is not None:
                upgrades = data.get("Upgrades", [])
                data = upgrades[tier - 1] if len(upgrades) >= tier else {}
            if all(field in data for field in fields):
                candidates.append(data)
        check(len(candidates) == 1, f"Ambiguous or missing lifesteal source fields: {name}")
        if len(candidates) != 1:
            continue
        check(effect.get("value_kind") == "absolute_damage_to_heal_fraction",
              f"Lifesteal value kind: {name}")
        if tier is not None:
            check(effect.get("required_upgrade_tier") == tier, f"Lifesteal upgrade gate: {name}")
        for target, field in zip(("hero", "non_hero"), fields):
            raw = candidates[0][field]
            raw = raw["Value"] if isinstance(raw, dict) else raw
            value = effect.get(target)
            check(isinstance(value, (int, float)) and isclose(value, raw / divisor),
                  f"Lifesteal value differs from canonical field: {name}.{target}")

    check(rules["target_resolution"].get("apply_generic_npc_reduction_to_explicit_npc_value") is False,
          "Explicit NPC lifesteal values must not receive a second generic reduction")
    for name in ("item.melee-lifesteal", "item.lifestrike"):
        check(effects.get(name, {}).get("value_kind") == "multiplier_on_proc_heal",
              f"Item proc must remain separate from damage-to-healing fractions: {name}")
    for name, mode in [("warden.last-stand", "standard"),
                       ("warden.last-stand.street-brawl", "street_brawl")]:
        check(effects.get(name, {}).get("game_mode") == mode, f"Lifesteal mode isolation: {name}")


def validate_burst_profiles(records):
    """Cross-check baseline curation; do not validate hypothetical runtime models."""
    profiles = records["data/burst-weapons.yaml"]["weapons"]
    expected = {p for p, r in records.items() if p.startswith("heroes/")
                and r.get("weapon", {}).get("BulletsPerBurst", 1) > 1}
    actual = {p["record"] for p in profiles}
    check(actual == expected, "Burst profile coverage differs from canonical weapons")
    check(len(actual) == len(profiles), "Duplicate burst profiles")
    estimates = records["data/burst-weapons.yaml"]["estimated_between_burst_gaps"]
    estimate_values = estimates["values_seconds"]
    for profile in profiles:
        path = profile["record"]
        check(path in records, f"Missing burst weapon record: {path}")
        if path not in records:
            continue
        weapon = records[path]["weapon"]
        n, intra, cycle = (profile[k] for k in
                           ("burst_shot_count", "intra_burst_cycle_time", "cycle_time"))
        check(n == weapon["BulletsPerBurst"], f"Burst shot count: {path}")
        check(isclose(intra, weapon["BurstInterShotInterval"]), f"Burst interval: {path}")
        period = n * intra + cycle
        check(period > 0, f"Nonpositive API burst period: {path}")
        if period > 0:
            check(isclose(n / period, profile["shots_per_second"]), f"API burst average: {path}")
            check(abs(n / period - weapon["RoundsPerSecond"]) <= 0.00005,
                  f"Burst rate differs from rounded canonical rate: {path}")
        expected_gap = intra + cycle
        check(profile["hero"] in estimate_values, f"Missing burst gap estimate: {path}")
        if profile["hero"] in estimate_values:
            check(isclose(estimate_values[profile["hero"]], expected_gap),
                  f"Burst gap estimate differs from documented derivation: {path}")


def main():
    registry = load("sources/source-registry.yaml")
    sources = registry["sources"]
    ids = {s["id"] for s in sources}
    check(len(ids) == len(sources), "Duplicate source IDs")
    for source in sources:
        check(allowed_source(source["url"]), f"Unapproved source: {source['id']}")
        for key, value in source.items():
            if isinstance(value, str) and (key == "url" or key.endswith("_url")):
                check(allowed_source(value), f"Unapproved URL: {source['id']}.{key}")
    records = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part.startswith(".") or part == "__pycache__"
                                     for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix not in {".md", ".yaml", ".txt"}:
            continue
        text = path.read_text()
        relative = path.relative_to(ROOT)
        # Raw historical text retains upstream outbound links; it is not a source registry.
        check(not re.search(r"(?i)owner[._-]confirmed|Planning/", text),
              f"Private or excluded reference: {relative}")
        record = None
        if path.suffix == ".yaml":
            record = yaml.safe_load(text)
            records[str(relative)] = record
        elif path.suffix == ".md":
            if text.startswith("---\n"):
                record = yaml.safe_load(text.split("---", 2)[1])
            for target in re.findall(r"\]\(([^)]+)\)", text):
                parsed = urlsplit(target)
                if parsed.scheme or not parsed.path:
                    continue
                dest = (path.parent / unquote(parsed.path)).resolve()
                check(ROOT == dest or ROOT in dest.parents, f"Link escapes repository: {relative}: {target}")
                check(dest.exists(), f"Broken link: {relative}: {target}")
        if record is not None and str(relative) != "sources/source-registry.yaml":
            for value in walk(record):
                if re.fullmatch(r"(?:wiki\.|deadlock-api\.|github\.deadlock-data\.)[\w.-]+", value):
                    check(value in ids, f"Missing source ID: {relative}: {value}")
    validate_lifesteal(records, ids)
    validate_burst_profiles(records)
    index = (ROOT / "INDEX.md").read_text()
    for domain, collection, count_key in [
        ("heroes", "heroes", "hero_count"), ("items", "items", "item_count"),
        ("npcs", "included", "included_count"), ("objectives", "included", "included_count"),
    ]:
        roster = records[f"{domain}/roster.yaml"]
        entries = roster[collection]
        check(len(entries) == roster[count_key], f"Roster count: {domain}")
        expected = set()
        for entry in entries:
            slug = entry["id"].split(".", 1)[1]
            path = f"{domain}/{entry.get('path', f'{slug}/{slug}.yaml')}"
            check(path in records, f"Missing record: {path}")
            expected.add(path)
            route = path.replace(".yaml", ".md") if domain in {"heroes", "items"} else path
            check(f"]({route})" in index, f"Missing index route: {route}")
        actual = {str(p.relative_to(ROOT)) for p in (ROOT / domain).glob("*/*.yaml")}
        check(expected == actual, f"Extra or missing {domain} records")
    counts = Counter()
    for path in (ROOT / "heroes").glob("*/*.yaml"):
        hero = records[str(path.relative_to(ROOT))]
        md = path.with_suffix(".md").read_text()
        for ability in hero["abilities"]:
            counts["abilities"] += 1
            expected = set(card_refs(ability["card"]))
            actual = {(p, d["localization_key"]) for d in ability["descriptions"] for p in d["card_paths"]}
            check(expected == actual, f"Description references: {hero['name']} / {ability['name']}")
            check(any(".Upgrades[" not in p for p, _ in actual), f"Missing base description: {ability['name']}")
            counts["card_references"] += len(actual)
            counts["descriptions"] += len(ability["descriptions"])
            for desc in ability["descriptions"]:
                check(bool(desc["raw_text"] and desc["plain_text"]), f"Empty description: {ability['name']}")
                check(desc["source"] in ids, f"Description source: {ability['name']}")
                check(all(line in md for line in desc["plain_text"].splitlines()), f"Unrendered description: {ability['name']}")
            check(ability["name"] in index, f"Unindexed ability: {ability['name']}")
    check(dict(counts) == {"abilities": 152, "card_references": 630, "descriptions": 481}, "Description coverage totals")
    manifest = records["patches/manifest.yaml"]
    expected = set()
    for entry in manifest["files"]:
        path = ROOT / "patches" / entry["path"]
        expected.add(path)
        check(path.is_file(), f"Missing patch: {entry['path']}")
        if path.is_file():
            data = path.read_bytes()
            check(sha256(data).hexdigest() == entry["sha256"], f"Patch hash: {entry['path']}")
            check(len(data) == entry["bytes"], f"Patch size: {entry['path']}")
        date.fromisoformat(str(entry["date"]))
        check(allowed_source(entry["source_url"]), f"Patch origin: {entry['path']}")
    check(expected == set((ROOT / "patches/raw").glob("*.txt")), "Patch inventory mismatch")
    check(len(expected) == 135, "Patch count")
    if errors:
        raise SystemExit("Validation failed:\n" + "\n".join(errors))
    print(f"PASS: {len(records)} YAML files; 38 heroes, 173 items, 14 NPCs, 2 objectives; "
          f"{counts['abilities']} abilities, {counts['descriptions']} descriptions; "
          f"{len(expected)} hash-verified changelogs; local links, source references, lifesteal consistency, and burst profiles valid.")


if __name__ == "__main__":
    main()
