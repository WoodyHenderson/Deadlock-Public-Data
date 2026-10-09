"""Pure card/text rendering helpers for the scoped launch importer.

No network access, global source mutation, or corpus-wide writes. Callers must
supply the localization source explicitly; source fields retain their units.
"""
from html import unescape
from html.parser import HTMLParser
import json
import re

TOKEN = re.compile(r"\{g:citadel_(inline_attribute|binding):['\"]([^'\"]+)['\"]\}")


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"br", "p", "div", "li"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag.lower() in {"br", "p", "div", "li"}:
            self.parts.append("\n")


def plain_text(raw, localization):
    def replace(match):
        kind, key = match.groups()
        if kind == "inline_attribute":
            return localization[f"InlineAttribute_{key}"]
        return " [" + re.sub(r"(?<=[a-z])(?=[A-Z0-9])", " ", key) + "] "

    value = TOKEN.sub(replace, raw.replace("<{g:", "{g:"))
    parser = TextExtractor()
    parser.feed(value)
    parser.close()
    text = unescape("".join(parser.parts))
    paragraphs = [re.sub(r"[\t \r]+", " ", line).strip() for line in text.splitlines()]
    text = "\n".join(line for line in paragraphs if line)
    if not text or re.search(r"\{[^{}]*\}|<[^>]+>", text):
        raise ValueError(f"Empty or unresolved description: {text!r}")
    return text


def description_refs(value, path="card"):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "DescKey":
                yield path + "." + key, child
            else:
                yield from description_refs(child, path + "." + key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from description_refs(child, path + f"[{index}]")


def resolve(card, localization, *, source):
    entries = {}
    for path, key in description_refs(card):
        token = key.lstrip("#")
        if token not in entries:
            raw = localization[token]
            entries[token] = {
                "localization_key": token,
                "card_paths": [],
                "source": source,
                "raw_text": raw,
                "plain_text": plain_text(raw, localization),
            }
        if "IGNORED[" in entries[token]["raw_text"]:
            entries[token]["quality_note"] = (
                "Source contains an unresolved placeholder. Retained verbatim for "
                "provenance, not a usable numeric effect; consult the separate "
                "upgrade data and review before interpreting this tooltip."
            )
        entries[token]["card_paths"].append(path)
    if not entries or not any(
        any(".Upgrades[" not in p for p in entry["card_paths"])
        for entry in entries.values()
    ):
        raise ValueError("Ability lacks a base description")
    return list(entries.values())


def number(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def card_value(prop):
    value = number(prop.get("Value", "Unknown"))
    scale = prop.get("Scale")
    scales = [scale] if isinstance(scale, dict) else scale if isinstance(scale, list) else []
    terms = []
    for entry in scales:
        if not isinstance(entry, dict) or not entry.get("Type") or entry.get("Value") is None:
            continue
        amount = number(entry["Value"])
        signed = amount if amount.startswith("-") else "+" + amount
        scale_type = str(entry["Type"]).replace("_", " ")
        terms.append(f"{signed} per {scale_type}")
    if terms:
        value += " (" + ", ".join(terms) + ")"
    return value


def card_properties(card):
    out, seen = [], set()

    def add(prop):
        label = prop.get("Name") or prop.get("Key")
        if not label or prop.get("Value") is None:
            return
        rendered = (str(label), card_value(prop))
        if rendered not in seen:
            seen.add(rendered)
            out.append(rendered)

    info1 = card.get("Info1") or {}
    main = info1.get("Main") or {}
    if isinstance(main, dict):
        for prop in main.get("Props") or []:
            add(prop)
    elif isinstance(main, list):
        for prop in main:
            add(prop)
    for prop in info1.get("Alt") or []:
        add(prop)
    ignored = {"Key", "Name", "DescKey", "Info1", "Info2", "Upgrades", "Move", "Other", "AbilityCastDelay", "AbilityChannelTime"}
    for key, prop in card.items():
        if key in ignored or not isinstance(prop, dict) or "Value" not in prop:
            continue
        add(prop)
    return out


def render_card(card):
    props = card_properties(card)
    lines = ["| Card field | Base value |", "| --- | ---: |"]
    if props:
        lines.extend(f"| {label} | {value} |" for label, value in props)
    else:
        lines.append("| No card-visible fields | not supplied |")
    upgrades = []
    for index, upgrade in enumerate(card.get("Upgrades") or [], 1):
        delta = {key: value for key, value in upgrade.items() if key != "DescKey"}
        if delta:
            upgrades.append(f"- Tier {index}: `{json.dumps(delta, ensure_ascii=False, separators=(',', ':'))}`")
    if upgrades:
        lines.extend(["", "Upgrade deltas:", *upgrades])
    return "\n".join(lines)


def render_base_stats(stats):
    stamina = stats["stamina"]
    return "\n".join([
        "## Base Stats", "", "| Stat | Value |", "| --- | ---: |",
        f"| Maximum health | {number(stats['maximum_health'])} |",
        f"| Health regeneration | {number(stats['health_regeneration_per_second'])}/s |",
        f"| Move speed | {number(stats['move_speed_meters_per_second'])}m/s |",
        f"| Sprint bonus | {number(stats['sprint_speed_bonus_meters_per_second'])}m/s |",
        f"| Stamina | {number(stamina['charges'])} |",
        f"| Light / heavy melee | {number(stats['light_melee_damage'])} / {number(stats['heavy_melee_damage'])} |", "",
    ])


def render_weapon(weapon):
    lines = [
        "## Weapon", "",
        f"- Bullet damage: **{number(weapon.get('BulletDamage', 'unknown'))}**",
        f"- Rounds/s: **{number(weapon.get('RoundsPerSecond', 'unknown'))}**; magazine: **{number(weapon.get('ClipSize', 'unknown'))}**; reload: **{number(weapon.get('ReloadTime', 'unknown'))}s**",
        f"- Projectile speed: **{number(weapon.get('BulletSpeed', 'unknown'))}m/s**; falloff: **{number(weapon.get('FalloffStartRange', 'unknown'))}–{number(weapon.get('FalloffEndRange', 'unknown'))}m**",
        f"- Source DPS: **{number(weapon.get('DPS', 'unknown'))}**; sustained: **{number(weapon.get('SustainedDPS', 'unknown'))}**",
    ]
    alt = weapon.get("AltFire")
    if isinstance(alt, dict):
        lines.append(f"- Alt-fire bullet damage: **{number(alt.get('BulletDamage', 'unknown'))}**; rounds/s: **{number(alt.get('RoundsPerSecond', 'unknown'))}**; magazine: **{number(alt.get('ClipSize', 'unknown'))}**; reload: **{number(alt.get('ReloadTime', 'unknown'))}s**")
    return "\n".join(lines) + "\n"


def render_ability_stats(ability):
    bits = ability.get("data", {}).get("BehaviourBits") or []
    behavior = ", ".join(f"`{bit}`" for bit in bits) if bits else "none listed"
    lines = [f"Behavior flags: {behavior}.", "", render_card(ability.get("card") or {})]
    for note in ability.get("notes") or []:
        lines.extend(["", f"**Note:** {note['text']}"])
    for note in ability.get("patch_note_addenda") or []:
        lines.extend(["", f"**{note['evidence_status']}:** {note['text']} Source: `{note['source']}`."])
    return "\n".join(lines) + "\n"
