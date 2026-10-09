"""Public source-policy and pre-release configuration regressions."""
import importlib.util
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("public_validator", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PublicScopeTests(unittest.TestCase):
    def test_official_sources_are_narrowly_allowed(self):
        registry = yaml.safe_load((ROOT / "sources/source-registry.yaml").read_text())
        official = [s for s in registry["sources"]
                    if s["id"].startswith(("valve.", "steam.news."))]
        self.assertEqual(len(official), 2)
        for source in official:
            for key, value in source.items():
                if key == "url" or key.endswith("_url"):
                    self.assertTrue(validator.allowed_source(value), value)
        for url in (
            "http://www.playdeadlock.com/cityneversleeps",
            "https://www.playdeadlock.com/unreviewed",
            "https://www.playdeadlock.com.evil.example/cityneversleeps",
            "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=999",
            "https://github.com/SteamDatabase/GameTracking-Deadlock/",
            "https://github.com/unreviewed/source/",
        ):
            self.assertFalse(validator.allowed_source(url), url)

    def test_broker_is_pre_release_configuration_not_mode_availability(self):
        timings = yaml.safe_load((ROOT / "data/map-timings.yaml").read_text())
        self.assertEqual(timings["snapshot_id"], "deadlock-data-pre-rat-king-2026-10-01")
        broker = next(e for e in timings["events"] if e["id"] == "broker.corrupted-item-shop")
        self.assertIs(broker["configured_enabled"], True)
        self.assertEqual([(h["client"], h["enabled"]) for h in broker["configuration_history"]],
                         [(6722, True), (6731, True)])
        self.assertEqual(broker["mode_availability"],
                         {"standard_ranked": "unresolved", "street_brawl": "unresolved"})
        # Preserve the pre-existing public-only timing detail during the mirror.
        regular = next(e for e in timings["events"] if e["id"] == "breakables.regular")
        self.assertEqual(regular["central_room_starts_at"], 600)

    def test_sinner_timing_is_not_a_new_reward_formula(self):
        sinner = yaml.safe_load((ROOT / "npcs/sinners-sacrifice/sinners-sacrifice.yaml").read_text())
        self.assertEqual(sinner["evidence_status"], "source_conflict")
        jackpot = sinner["jackpot"]
        self.assertEqual(jackpot["exact_timing_distribution"], "unknown")
        self.assertEqual(jackpot["configured_minigame_fast_chance"], 0.4)
        self.assertEqual(jackpot["legacy_reference"]["cycle_duration_seconds"], 3.0)
        self.assertNotIn("cycle_duration", jackpot)
        self.assertEqual(sinner["reward"]["internal_base_souls"], 310)
        reward = sinner["reward"]
        self.assertEqual(reward["raw_client_gold_reward"] * reward["wiki_conversion_multiplier"], 310)
        self.assertEqual(reward["conversion_source"], "wiki.sinners-sacrifice.177553")
        self.assertIn("not established as the success window", sinner["post_update_evidence_note"])


if __name__ == "__main__":
    unittest.main()
