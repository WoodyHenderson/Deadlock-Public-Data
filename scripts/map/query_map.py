"""Read a small, relevant subset of the pinned map; no pathfinding or live spawns."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

MAP = Path(__file__).resolve().parents[2] / "map"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--category", help="Coordinate file stem, e.g. tough_crates or camps")
    p.add_argument("--zone", help="Exact source zone ID, e.g. times-square-4")
    p.add_argument("--min-h", type=float, help="Minimum source-relative elevation (metres)")
    p.add_argument("--max-h", type=float, help="Maximum source-relative elevation (metres)")
    p.add_argument("--limit", type=int, default=30, help="Maximum points returned (default 30)")
    p.add_argument("--summary", action="store_true", help="Return area counts instead of points")
    args = p.parse_args()
    if args.limit < 1 or args.limit > 500:
        p.error("--limit must be 1..500")
    if args.summary:
        summary = json.loads((MAP / "breakable-zones.yaml").read_text())
        if args.zone:
            summary["zones"] = [z for z in summary["zones"] if z["zone_id"] == args.zone]
            if not summary["zones"]:
                p.error(f"Unknown zone: {args.zone}")
        print(json.dumps(summary, indent=2))
        return
    if not args.category:
        p.error("--category required unless --summary is set")
    path = MAP / "coordinates" / (args.category + ".yaml")
    if not path.is_file() or args.category != path.stem:
        p.error(f"Unknown category: {args.category}")
    data = json.loads(path.read_text())
    if args.zone:
        zones = json.loads((MAP / "zones.yaml").read_text())["zones"]
        if args.zone not in {z["id"] for z in zones}:
            p.error(f"Unknown zone: {args.zone}")
    selected = [point for point in data["points"]
                if (not args.zone or point["zone_id"] == args.zone)
                and (args.min_h is None or point["h_m"] >= args.min_h)
                and (args.max_h is None or point["h_m"] <= args.max_h)]
    print(json.dumps({
        "snapshot_id": data["snapshot_id"], "source_id": data["source_id"],
        "category": data["category"], "zone_id": args.zone,
        "matched": len(selected), "returned": min(len(selected), args.limit),
        "truncated": len(selected) > args.limit,
        "points": selected[:args.limit],
    }, indent=2))


if __name__ == "__main__":
    main()
