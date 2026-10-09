"""Check sourced camp patterns and joins without inventing per-marker rosters."""
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[3]


def load(path):
    return yaml.safe_load((ROOT / path).read_text())


class HauntCompositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load("data/haunt-camp-compositions.yaml")

    def test_pre_release_sources_and_later_comparison_are_separate(self):
        sources = {s["id"]: s for s in load("sources/source-registry.yaml")["sources"]}
        cutoff = datetime.fromisoformat("2026-10-02T00:00:00+00:00")
        for source_id in self.data["scope"]["pre_release_sources"]:
            source = sources[source_id]
            self.assertLess(datetime.fromisoformat(source["last_modified"].replace("Z", "+00:00")), cutoff)
            self.assertRegex(source["wikitext_sha256"], r"^[a-f0-9]{64}$")
        self.assertEqual(self.data["scope"]["placement_snapshot"], "private-map-2026-10-06")
        self.assertGreater(datetime.fromisoformat(sources["wiki.haunt.181836"]["last_modified"].replace("Z", "+00:00")), cutoff)

    def test_sinner_patterns_reconcile_sites_machines_and_units(self):
        sinner = self.data["sinner_site_patterns"]
        patterns = sinner["configurations"]
        self.assertEqual(len(patterns), 4)
        self.assertEqual(sum(p["site_count"] for p in patterns), sinner["site_count"])
        self.assertEqual(sum(p["site_count"] * p["machines_per_site"] for p in patterns), sinner["machine_count"])
        self.assertEqual((sinner["site_count"], sinner["machine_count"]), (11, 15))
        self.assertEqual(sum(p["site_count"] for p in patterns if p["medium_haunts_per_site"]), 4)
        self.assertEqual(sum(p["site_count"] * p["medium_haunts_per_site"] for p in patterns), 6)
        rule = sinner["clear_rule"]
        self.assertIs(rule["requires_all_machines_destroyed"], True)
        self.assertIs(rule["requires_all_member_haunts_killed"], True)
        self.assertIs(rule["requires_nearby_crates_or_buff_containers_destroyed"], False)

    def test_marker_grouping_preserves_every_machine_without_inferred_haunts(self):
        inventory = self.data["placement_inventory"]
        actual = defaultdict(list)
        for point in load(inventory["machine_record"])["points"]:
            actual[(point["name"], point["zone_id"])].append(point["id"])
        groups = inventory["sinner_marker_groups"]
        recorded = {(g["name"], g["zone_id"]): g["marker_ids"] for g in groups}
        self.assertEqual(recorded, dict(actual))
        self.assertEqual(len(groups), 11)
        self.assertEqual(sum(len(g["marker_ids"]) for g in groups), 15)
        self.assertEqual(Counter(len(g["marker_ids"]) for g in groups), {1: 8, 2: 2, 3: 1})
        self.assertIsNone(inventory["per_marker_haunt_family"])
        self.assertIsNone(inventory["per_marker_haunt_unit_counts"])
        self.assertTrue(all(set(g) == {"name", "zone_id", "marker_ids"} for g in groups))

    def test_ordinary_markers_and_incomplete_composition_patterns(self):
        inventory = self.data["placement_inventory"]
        camps = load(inventory["ordinary_camp_record"])["points"]
        self.assertEqual(len(camps), inventory["ordinary_camp_count"])
        self.assertEqual(Counter(p["tier"] for p in camps), inventory["camp_tiers"])
        patterns = self.data["ordinary_camp_patterns"]
        self.assertEqual(patterns["small"]["members"], [{"tier": "small", "count": 3}])
        self.assertEqual(patterns["medium"]["reported_combination_count"], 6)
        self.assertIsNone(patterns["medium"]["exact_combinations"])
        self.assertIsNone(patterns["large"]["exact_per_location_compositions"])
        self.assertTrue(all(p["family"] is None for p in patterns.values()))

    def test_family_tier_revision_differences_are_not_silently_overwritten(self):
        families = {f["id"]: f for f in self.data["families"]}
        self.assertEqual(len(families), 9)
        self.assertEqual(families["crabbage-pot"]["reported_tiers"], ["small", "medium"])
        self.assertEqual(families["crabbage-pot"]["later_reported_tiers"], ["small", "medium", "large"])
        self.assertEqual(families["stage-hand"]["reported_tiers"], ["small", "medium", "large"])
        self.assertEqual(families["stage-hand"]["later_reported_tiers"], ["medium", "large"])

    def test_canonical_counts_clear_rule_and_navigation_agree(self):
        timing = next(e for e in load("data/map-timings.yaml")["events"] if e["id"] == "sinners-sacrifice")
        npc = load("npcs/sinners-sacrifice/sinners-sacrifice.yaml")["site_composition"]
        self.assertEqual((timing["map_locations"], timing["total_machines"]), (11, 15))
        self.assertEqual((npc["site_count"], npc["machine_count"]), (11, 15))
        self.assertTrue(timing["clear_requires_all_machines_and_member_haunts"])
        self.assertFalse(npc["requires_nearby_breakables_cleared"])
        for filename in ("INDEX.md", "map/README.md", "general/map/timed-events-and-neutral-objectives.md"):
            self.assertIn("haunt-camps-and-sinner-sites.md", (ROOT / filename).read_text())


if __name__ == "__main__":
    unittest.main()
