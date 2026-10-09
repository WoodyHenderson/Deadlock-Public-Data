"""Regression checks for the dated corrupted-item configuration sidecar."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
RECORD = ROOT / "data/corrupted-items.yaml"


class CorruptedItemTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(RECORD.read_text())

    def test_sidecar_is_scoped_and_source_pinned(self):
        self.assertEqual(self.data["snapshot_id"], "deadlock-data-client-6726")
        self.assertEqual(self.data["current_as_of"], "2026-09-30")
        self.assertIn("github.deadlock-data.gameplay.3d26c988891f", self.data["sources"])
        self.assertEqual(self.data["availability"]["mode"], "unresolved")
        self.assertEqual(self.data["availability"]["date_range"], "unresolved")
        self.assertEqual(
            self.data["field_sources"]["penalty_definitions"],
            "github.deadlock-data.gameplay.3d26c988891f",
        )
        self.assertEqual(
            self.data["street_brawl_configuration"]["corrupt_item_round"], 5
        )
        self.assertEqual(
            self.data["street_brawl_configuration"]["buy_time_seconds_by_round"],
            [50, 50, 50, 50, 65],
        )

    def test_all_source_corrupted_upgrade_blocks_are_retained(self):
        items = self.data["item_corrupted_upgrades"]
        self.assertEqual(len(items), 95)
        self.assertEqual(len(self.data["penalty_definitions"]), 11)
        self.assertEqual(
            self.data["penalty_definitions"][4]["m_vecEffects"][0]["BonusPerTier"],
            ["0", "0", "0", "-25", "-30", "0"],
        )
        self.assertEqual(
            items["upgrade_ability_power_shard"],
            {
                "BulletResist": 15,
                "TechResist": 15,
                "AbilityCooldown": -15,
                "ImbuedCooldownMultiplier": -50,
            },
        )
        self.assertTrue(all(key.startswith("upgrade_") for key in items))
        self.assertTrue(all(isinstance(value, dict) and value for value in items.values()))


if __name__ == "__main__":
    unittest.main()
