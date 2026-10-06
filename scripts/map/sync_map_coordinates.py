"""Import an authorized private map export; validate derived summaries.

Inputs are owner-authorized JSON exports of point and district data. Do not
fetch any website here. Private source provenance stays outside the repository;
images, site code and route geometry are excluded.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

DEST = Path(__file__).resolve().parents[2] / "map"
SOURCE_ID = "private.map-coordinates.2026-10-06"
SNAPSHOT = "private-map-2026-10-06"
# Exclude polygons/paths that are not points of interest: lanes, ziplines,
# tunnel links. Keep veil centres, NOT their proprietary polygon meshes.
TYPES = (
    "guardians", "walkers", "base_guardians", "shrines", "patrons",
    "mid_boss", "shops", "camps", "sinners_sacrifice", "bridge_buffs",
    "urn_pads", "rift", "item_crates", "crates", "tough_crates",
    "statues", "teleporters", "veils", "jump_pads", "snacks", "vents",
    "small_tunnels",
)
BREAKABLES = ("crates", "tough_crates", "statues")
NESTED_ZONES = ("sunken-plaza-19", "bell-tower-20")


def slug(text: str) -> str:
    import re
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def dump(path: Path, obj: dict, check: bool) -> None:
    # JSON is valid YAML; preserve consistent, parseable and diffable records.
    text = json.dumps(obj, indent=2, ensure_ascii=False) + "\n"
    if check:
        if not path.exists() or path.read_text() != text:
            raise ValueError(f"Out of date: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)


def inside(u: float, v: float, polygon: list) -> bool:
    result = False
    prev_u, prev_v = polygon[-1]
    for current_u, current_v in polygon:
        if (current_v > v) != (prev_v > v):
            crossing = (prev_u - current_u) * (v - current_v) / (prev_v - current_v) + current_u
            if u < crossing:
                result = not result
        prev_u, prev_v = current_u, current_v
    return result


def zone_for(point: dict, zones: list) -> tuple[str | None, list[str]]:
    hits = [z["id"] for z in zones if any(
        inside(point["u"], point["v"], poly) for poly in z["polygons"]
    )]
    if len(hits) == 1:
        return hits[0], hits
    # Small named landmarks overlap their parent districts. Choose the most
    # specific ONLY for the known nested areas, never arbitrarily pick a parent.
    nested = [name for name in hits if name in NESTED_ZONES]
    if len(nested) == 1:
        return nested[0], hits
    return None, hits  # outside, on a boundary or otherwise ambiguous


def zones_from_source(source: list) -> list:
    zones = []
    for z in source:
        zones.append({
            "id": f"{slug(z['name'])}-{z['n']}" + (
                "a" if z["name"] == "Docks" and z["label"][1] < .3 else
                "b" if z["name"] == "Docks" else ""
            ),
            "name": z["name"],
            "parent": z.get("sub"),
            "lane": z.get("lane"),
            "label_uv": z["label"],
            "polygons": z["area"],
        })
    if len({z["id"] for z in zones}) != len(zones):
        raise ValueError("Zone IDs are not unique")
    return zones


def marker(kind: str, index: int, raw: dict, zones: list) -> dict:
    u, v, h = (raw[key] for key in ("u", "v", "h"))
    if not (0 <= u <= 1 and 0 <= v <= 1 and isinstance(h, (int, float))):
        raise ValueError(f"Invalid point {kind}[{index}]")
    zone_id, hits = zone_for(raw, zones)
    result = {
        "id": f"map.{kind}.{index + 1:04}",
        "u": u,
        "v": v,
        "h_m": h,
        "zone_id": zone_id,
    }
    if len(hits) > 1 and zone_id is None:
        result["candidate_zone_ids"] = hits
    for key in ("name", "tier", "kind", "team", "lane", "group", "tether", "first_spawn_s", "respawn_s", "net"):
        if key in raw:
            result[key] = raw[key]
    if "to" in raw:
        result["destination_uvh_m"] = [raw["to"][key] for key in ("u", "v", "h")]
    return result


def build(map_source: dict, districts_source: list) -> tuple[dict, dict, dict]:
    if set(TYPES) - set(map_source):
        raise ValueError(f"Missing categories: {set(TYPES) - set(map_source)}")
    zones = zones_from_source(districts_source)
    files = {}
    for kind in TYPES:
        if not isinstance(map_source[kind], list):
            raise ValueError(f"Not a marker list: {kind}")
        points = [marker(kind, i, raw, zones) for i, raw in enumerate(map_source[kind])]
        files[kind] = {
            "schema_version": 1, "snapshot_id": SNAPSHOT, "current_as_of": "2026-10-06",
            "evidence_status": "source_verified", "source_id": SOURCE_ID,
            "category": kind, "count": len(points), "points": points,
        }
    totals = {kind: len(files[kind]["points"]) for kind in TYPES}
    zone_counts = {z["id"]: Counter() for z in zones}
    unassigned = Counter()
    for kind in BREAKABLES:
        for point in files[kind]["points"]:
            target = zone_counts[point["zone_id"]] if point["zone_id"] else unassigned
            target[kind] += 1
    summaries = []
    for z in zones:
        c = zone_counts[z["id"]]
        summaries.append({
            "zone_id": z["id"], "name": z["name"], "parent": z["parent"],
            "crates": c["crates"], "tough_crates": c["tough_crates"],
            "statues": c["statues"],
        })
    summary = {
        "schema_version": 1, "snapshot_id": SNAPSHOT, "current_as_of": "2026-10-06",
        "evidence_status": "derived", "source_id": SOURCE_ID,
        "method": "point_in_source_subarea_polygon; known nested zones take precedence; unassigned never guessed",
        "totals": {k: totals[k] for k in BREAKABLES},
        "unassigned": {k: unassigned[k] for k in BREAKABLES},
        "zones": summaries,
    }
    zones_record = {
        "schema_version": 1, "snapshot_id": SNAPSHOT, "current_as_of": "2026-10-06",
        "evidence_status": "source_verified", "source_id": SOURCE_ID,
        "coordinate_system": "Normalized unflipped minimap (u right, v down), not game-world coordinates",
        "zones": zones,
    }
    for kind in BREAKABLES:
        assert sum(z[kind] for z in summaries) + unassigned[kind] == totals[kind]
    return files, zones_record, summary


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--map-input", type=Path, help="Authorized JSON export of public map point data")
    p.add_argument("--zones-input", type=Path, help="Authorized JSON export of district overlays")
    p.add_argument("--check", action="store_true", help="Check existing records; do not write")
    args = p.parse_args()
    if bool(args.map_input) != bool(args.zones_input):
        p.error("Specify both --map-input and --zones-input")
    if args.map_input:
        files, zones, summary = build(json.loads(args.map_input.read_text()),
                                      json.loads(args.zones_input.read_text()))
        for kind, record in files.items():
            dump(DEST / "coordinates" / f"{kind}.yaml", record, args.check)
        dump(DEST / "zones.yaml", zones, args.check)
        dump(DEST / "breakable-zones.yaml", summary, args.check)
    elif args.check:
        # Check published material without requiring the source's site bundle.
        zones = json.loads((DEST / "zones.yaml").read_text())
        files = {k: json.loads((DEST / "coordinates" / f"{k}.yaml").read_text()) for k in TYPES}
        data = {k: record["points"] for k, record in files.items()}
        for kind, record in files.items():
            if record["count"] != len(record["points"]):
                raise ValueError(f"Count mismatch: {kind}")
        for kind in TYPES:
            for i, point in enumerate(data[kind]):
                if point["id"] != f"map.{kind}.{i + 1:04}":
                    raise ValueError(f"Unstable marker ID: {kind}[{i}]")
                zone, _ = zone_for(point, zones["zones"])
                if point["zone_id"] != zone:
                    raise ValueError(f"Zone mismatch: {point['id']}")
        counts = {z["id"]: Counter() for z in zones["zones"]}
        unassigned = Counter()
        for kind in BREAKABLES:
            for point in data[kind]:
                (counts[point["zone_id"]] if point["zone_id"] else unassigned)[kind] += 1
        summary = json.loads((DEST / "breakable-zones.yaml").read_text())
        for kind in BREAKABLES:
            if summary["totals"][kind] != len(data[kind]) or summary["unassigned"][kind] != unassigned[kind]:
                raise ValueError(f"Summary mismatch: {kind}")
        for z in summary["zones"]:
            if any(z[k] != counts[z["zone_id"]][k] for k in BREAKABLES):
                raise ValueError(f"Summary zone mismatch: {z['zone_id']}")
        if {z["zone_id"] for z in summary["zones"]} != set(counts):
            raise ValueError("Summary zone coverage mismatch")
    else:
        p.error("Provide --map-input and --zones-input, or --check")
    print("Map coordinates and zone summaries verified" if args.check else "Map coordinates and zone summaries written")


if __name__ == "__main__":
    main()
