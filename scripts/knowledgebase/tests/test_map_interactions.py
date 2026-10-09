"""Regression checks for dated map behavior, conflicts, and source safety."""
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("map_client", ROOT / "scripts/knowledgebase/check_map_client.py")
client = importlib.util.module_from_spec(spec)
spec.loader.exec_module(client)


def load(name):
    return yaml.safe_load((ROOT / name).read_text())


class MapInteractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = load("data/map-interactions.yaml")

    def test_snack_pre_release_and_later_timing_stay_separate(self):
        snack = self.rules["healing_snacks"]
        self.assertEqual((snack["initial_spawn_seconds"], snack["respawn_after_pickup_seconds"]), (180, 180))
        self.assertEqual((snack["total_heal_max_health_percent"], snack["duration_seconds"]), (10, 4))
        self.assertEqual(snack["later_description"]["initial_spawn_seconds"], 150)
        self.assertEqual(snack["later_description"]["source"], "wiki.healing-snack.181344")
        event = next(e for e in load("data/map-timings.yaml")["events"] if e["id"] == "breakables.healing-snack")
        self.assertEqual(event["spawn_delay"], snack["initial_spawn_seconds"])
        self.assertEqual(event["behavior_source"], snack["source"])

    def test_vent_rules_do_not_imply_invulnerability(self):
        vent = self.rules["steam_vents"]
        self.assertEqual(vent["source"], "wiki.steam-vent.177398")
        self.assertTrue(vent["allies_can_see_occupants"])
        self.assertEqual(len(vent["reveal_triggers"]), 3)
        self.assertIn("invulnerability", vent["note"])
        self.assertIn("not independently established", vent["regeneration_display"]["interpretation"])

    def test_crate_reward_and_unmapped_descriptor_boundaries(self):
        crates = self.rules["breakables"]
        self.assertEqual([crates["tough_crates"][k] for k in ("reward_base", "reward_growth_per_match_minute", "configured_drop_chance_percent")], [46, 4, 100])
        self.assertEqual([crates["ordinary_crates"][k] for k in ("reward_base", "reward_growth_per_match_minute", "configured_drop_chance_percent")], [23, 2, 60])
        self.assertFalse(crates["reward_model"]["engine_rounding_verified"])
        mappings = crates["schedule_mapping"]["descriptors"]
        self.assertEqual(mappings[1]["wiki_category"], "tunnel_breakables")
        self.assertIsNone(mappings[3]["wiki_category"])
        self.assertEqual(mappings[3]["respawn_seconds"], 180)

    def test_permanent_buff_description_preserves_stateful_unknowns(self):
        buffs = self.rules["buff_containers"]
        self.assertEqual(buffs["configured_drop_chance_percent"], 50)
        self.assertTrue(buffs["persists_through_death"])
        self.assertEqual(buffs["tier_thresholds_match_minutes"], [0, 10, 30])
        self.assertEqual(buffs["wiki_selection_description"]["exact_algorithm_and_guarantees"], "unresolved")
        self.assertEqual(buffs["client_weight_ratios"]["total_weight"], 10)
        self.assertEqual(buffs["wiki_selection_description"]["containers_track"], "generated_buffs_even_if_not_collected")

    def test_sinner_conversion_does_not_invent_jackpot_cycle_lengths(self):
        sinner = self.rules["sinners"]
        reward = sinner["reward_model"]
        self.assertEqual(reward["raw_gold_reward"] * reward["wiki_multiplier"], reward["base_souls"])
        self.assertAlmostEqual(reward["base_souls"] * reward["growth_percent_of_base_per_minute"] / 100, reward["unrounded_growth_souls_per_minute"])
        self.assertEqual(sinner["configured_minigame_fields"]["VaultMiniGameHitWindow"], 0.5)
        self.assertEqual(sinner["configured_minigame_fields"]["VaultSuccessDestroyTime"], 1.3)
        self.assertIsNone(sinner["later_two_speed_description"]["exact_fast_slow_cycle_durations"])
        conflict = sinner["hit_count_conflict"]
        self.assertNotEqual(conflict["wiki_heavy_damage"] * conflict["wiki_heavy_hits_to_complete"], conflict["configured_health"])

    def test_npc_legacy_fields_are_not_silent_current_claims(self):
        for size in ("small", "medium", "large"):
            npc = load(f"npcs/{size}-neutral/{size}-neutral.yaml")
            self.assertEqual(npc["current_as_of"], "2026-10-01")
            self.assertIn("github.deadlock-data.gameplay.0d46cdecfccf", npc["sources"])
            self.assertIsNone(npc["weak_points"]["count"])
            self.assertGreater(npc["legacy_weak_points"]["count"], 0)
            self.assertEqual(npc["targeting_configuration"]["SightRangePlayers"], 38.1)
        large = load("npcs/large-neutral/large-neutral.yaml")
        self.assertIsNone(large["combat"]["melee_resistance_percent"])
        self.assertEqual(large["combat"]["legacy_melee_resistance"]["percent"], 20)
        boss = load("npcs/mid-boss/mid-boss.yaml")
        self.assertIn("intrinsic modifier", boss["shield_configuration"]["status"])
        self.assertEqual(boss["combat"]["shield_absorption_per_second"], {"base": 35, "growth_per_minute": 5})

    def test_behavior_catalog_covers_families_without_assigning_camps(self):
        expected = {f["id"] for f in load("data/haunt-camp-compositions.yaml")["families"]}
        self.assertEqual(set(self.rules["haunts"]["family_behaviors"]), expected)
        self.assertEqual(self.rules["haunts"]["exact_family_damage_cooldowns_and_per_camp_assignment"], "unresolved")
        self.assertEqual(self.rules["haunts"]["later_behavior_source"], "wiki.haunt.181836")

    def test_checker_rejects_unpinned_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_bytes(b'{"value": 1}')
            self.assertEqual(client.pinned_json(path, hashlib.sha256(path.read_bytes()).hexdigest()), {"value": 1})
            with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
                client.pinned_json(path, "0" * 64)

    def test_behavior_guide_is_routed_and_placement_audit_not_claimed_complete(self):
        guide = (ROOT / "general/map/map-interactions-and-open-questions.md").read_text()
        self.assertIn("No newer authorized point export", guide)
        self.assertIn("No geometry changes or camp assignments have been guessed", guide)
        self.assertIn("map-interactions-and-open-questions.md", (ROOT / "INDEX.md").read_text())


if __name__ == "__main__":
    unittest.main()
