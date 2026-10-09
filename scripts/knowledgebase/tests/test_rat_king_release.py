"""Configuration-only guards for the adjacent release review."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_rat_king_release as audit


class ReleaseTests(unittest.TestCase):
    def fixture(self):
        before = {name: {} for name in audit.EXPECTED_CHANGES}
        after = {name: dict.fromkeys(keys, 1) for name, keys in audit.EXPECTED_CHANGES.items()}
        before["convars"]["citadel_corrupted_item_shop_enabled"] = True
        after["convars"]["citadel_corrupted_item_shop_enabled"] = False
        after["convars"]["citadel_ping_can_heal_range"] = {"value": 2500}
        before["npc-data"]["npc_neutral_bug"] = {"RespawnTime": 30}
        after["npc-data"]["npc_neutral_bug"] = {"RespawnTime": 15}
        return before, after

    def test_inventory_rejects_unreviewed_changes(self):
        before, after = self.fixture()
        self.assertEqual(audit.check(before, after), [])
        changed = copy.deepcopy(after)
        changed["generic-data"]["unreviewed"] = 1
        self.assertTrue(any("generic-data" in e for e in audit.check(before, changed)))

    def test_hash_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            (path / "generic-data.json").write_text("{}")
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                audit.read_inputs(path, {"generic_data_sha256": "wrong"})

    def test_broker_history_does_not_backdate_disable_or_resolve_street_brawl(self):
        timings = yaml.safe_load((audit.KB / "data/map-timings.yaml").read_text())
        broker = next(e for e in timings["events"] if e["id"] == "broker.corrupted-item-shop")
        self.assertEqual([(h["client"], h["enabled"]) for h in broker["configuration_history"]],
                         [(6722, True), (6731, True), (6737, False)])
        self.assertIs(broker["configured_enabled"], False)
        self.assertEqual(broker["mode_availability"]["street_brawl"], "unresolved")
        self.assertEqual(broker["mode_availability_source"], "wiki.update.2026-10-02.181191")
        pre_release = yaml.safe_load((audit.KB / "data/map-interactions.yaml").read_text())
        self.assertEqual(pre_release["snapshot_id"], "pre-rat-king-map-with-dated-wiki-interpretations")
        self.assertIn("October 2 Broker disablement", pre_release["scope"])
        self.assertIn("No Rat King", pre_release["scope"])


if __name__ == "__main__":
    unittest.main()
