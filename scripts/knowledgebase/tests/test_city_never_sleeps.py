"""Offline retrieval and evidence-boundary checks for the pre-release refresh.

These check curated records, not runtime gameplay or patch-time placements.
"""
from pathlib import Path
import re
import unittest

KB = Path(__file__).resolve().parents[3]


class CityNeverSleepsTests(unittest.TestCase):
    def test_districts_are_retrievable_without_becoming_extra_lanes(self):
        guide = (KB / "general/map/districts-and-landmarks.md").read_text()
        index = (KB / "INDEX.md").read_text()
        for name in ("Theater", "Chinatown", "Haunted Lot", "Plaza",
                     "Bell Tower", "Sunken Plaza", "basketball court"):
            with self.subTest(name=name):
                self.assertIn(name, guide)
                self.assertTrue(any(
                    name in line and "general/map/districts-and-landmarks.md" in line
                    for line in index.splitlines()
                ))
        self.assertIn("**not additional lanes**", guide)
        self.assertIn("later interpretation", guide)
        self.assertIn("not used to claim exact September 29 placements", guide)

    def test_breakable_history_keeps_the_unmapped_group_separate(self):
        timings = (KB / "data/map-timings.yaml").read_text()
        tunnel = timings.split("  - id: breakables.underground-tunnels\n", 1)[1].split("\n  - id:", 1)[0]
        observations = re.findall(
            r"client: (\d+)\n        initial_spawn: (\d+)\n        respawn_interval: (\d+)",
            tunnel,
        )
        self.assertEqual(observations[:3], [
            ("6722", "180", "180"), ("6723", "300", "300"),
            ("6731", "300", "300"),
        ])
        self.assertIn("retain the older", tunnel)
        self.assertIn("mapping as a candidate", tunnel)
        self.assertIn("id: breakables.unmapped-group-4", timings)
        self.assertIn("source_verified_value_category_unresolved", timings)

    def test_additional_buffs_preserve_units_and_selection_uncertainty(self):
        timings = (KB / "data/map-timings.yaml").read_text()
        additional = timings.split("\nbuff_container_additional_buffs:\n", 1)[1]
        for name in ("bullet_resist", "spirit_resist", "ability_range", "move_speed"):
            self.assertIn(f"    {name}:\n", additional)
        self.assertIn("raw_source_units_by_tier: [3.937, 7.874, 11.811]", additional)
        self.assertIn("display_meters_per_second_by_tier: [0.1, 0.2, 0.3]", additional)
        self.assertIn("exact_selection_semantics: unresolved", additional)
        self.assertIn("tier_1_additional_radius_modifier:", additional)
        loot = additional.split("    loot_pool:\n", 1)[1]
        categories = re.findall(r"^          (\w+):", loot, re.MULTILINE)
        self.assertEqual(len(categories), 30)  # Ten categories at each of three tiers.

    def test_historical_review_explicitly_excludes_the_launch(self):
        review = (KB / "patches/2026-09-29-city-never-sleeps-pre-rat-king-review.md").read_text()
        self.assertIn("client 6731 (October 1) is the last included checkpoint", review)
        self.assertIn("October 2 Rat King release is not part of this review", review)
        self.assertIn("do not independently establish public match availability", review)
        self.assertIn("not** a verbatim changelog", review)
        self.assertIn("## Unresolved / excluded", review)
        self.assertIn("runtime spawn/activation remain unverified", " ".join(review.split()))


if __name__ == "__main__":
    unittest.main()
