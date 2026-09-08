#!/usr/bin/env python3
"""Validate this standalone data snapshot offline; never fetch or modify files."""
from collections import Counter
from datetime import date
from hashlib import sha256
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
          f"{len(expected)} hash-verified changelogs; local links and source references valid.")


if __name__ == "__main__":
    main()
