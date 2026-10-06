"""Published map point layer and breakable-zone summary regression tests."""
import importlib.util
import json
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parent / "sync_map_coordinates.py"
spec = importlib.util.spec_from_file_location("map_coordinates", SCRIPT)
map_sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(map_sync)


class MapCoordinateTests(unittest.TestCase):
    def test_pinned_point_inventory_and_source(self):
        counts = {}
        for kind in map_sync.TYPES:
            record = json.loads((map_sync.DEST / "coordinates" / f"{kind}.yaml").read_text())
            self.assertEqual(record["source_id"], map_sync.SOURCE_ID)
            self.assertEqual(record["snapshot_id"], map_sync.SNAPSHOT)
            self.assertEqual(record["count"], len(record["points"]))
            counts[kind] = record["count"]
            self.assertEqual(len({p["id"] for p in record["points"]}), record["count"])
            for p in record["points"]:
                self.assertTrue(0 <= p["u"] <= 1 and 0 <= p["v"] <= 1)
                self.assertIn("h_m", p)
        for kind, expected in {
            "crates": 423, "tough_crates": 73, "statues": 166,
            "camps": 40, "sinners_sacrifice": 15, "snacks": 36,
            "vents": 46, "shops": 8,
        }.items():
            self.assertEqual(counts[kind], expected, kind)
        self.assertEqual(sum(counts.values()), 983)

    def test_zone_summaries_are_derived_and_recheck_offline(self):
        import subprocess
        subprocess.run(["python3", str(SCRIPT), "--check"], check=True, capture_output=True)
        summary = json.loads((map_sync.DEST / "breakable-zones.yaml").read_text())
        self.assertEqual(summary["evidence_status"], "derived")
        self.assertEqual(summary["totals"], {"crates": 423, "tough_crates": 73, "statues": 166})
        self.assertEqual(summary["unassigned"], {"crates": 4, "tough_crates": 2, "statues": 1})
        zones = {z["zone_id"]: z for z in summary["zones"]}
        self.assertEqual(zones["times-square-4"]["tough_crates"], 11)
        self.assertEqual(zones["bell-tower-20"]["tough_crates"], 4)
        self.assertEqual(zones["sunken-plaza-19"]["tough_crates"], 4)
        self.assertEqual(sum(z["tough_crates"] for z in zones.values()) + summary["unassigned"]["tough_crates"], 73)

    def test_query_returns_small_subset_without_claiming_live_availability(self):
        import subprocess
        query = Path(__file__).resolve().parent / "query_map.py"
        out = subprocess.check_output([
            "python3", str(query), "--category", "tough_crates",
            "--zone", "times-square-4", "--limit", "3",
        ], text=True)
        result = json.loads(out)
        self.assertEqual(result["matched"], 11)
        self.assertEqual(result["returned"], 3)
        self.assertTrue(result["truncated"])
        self.assertTrue(all(p["zone_id"] == "times-square-4" for p in result["points"]))

    def test_overlap_priority_and_no_unsupported_route_geometry(self):
        zones = json.loads((map_sync.DEST / "zones.yaml").read_text())["zones"]
        # A point in a nested landmark is never counted twice in the parent.
        zone, candidates = map_sync.zone_for({"u": 0.6239, "v": 0.557}, zones)
        self.assertEqual(zone, "bell-tower-20")
        self.assertIn("chinatown-7", candidates)
        self.assertEqual(map_sync.zone_for({"u": 1.0, "v": 1.0}, zones)[0], None)
        self.assertFalse((map_sync.DEST / "routes.yaml").exists())
        self.assertFalse((map_sync.DEST / "coordinates" / "ziplines.yaml").exists())


if __name__ == "__main__":
    unittest.main()
