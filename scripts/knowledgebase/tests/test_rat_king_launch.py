"""Checks for the date-pinned Rat King launch record and scoped importer."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts/knowledgebase"))
import sync_rat_king_from_launch as sync  # noqa: E402

RECORD = ROOT / "heroes/rat-king/rat-king.yaml"


class RatKingLaunchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(RECORD.read_text())

    def test_release_and_stats_use_the_launch_pin(self):
        self.assertEqual(self.data["snapshot_id"], "deadlock-data-client-6737")
        self.assertEqual(self.data["current_as_of"], "2026-10-02")
        self.assertEqual(self.data["client_version"], 6737)
        self.assertEqual(self.data["source_revision"], 11076133)
        self.assertEqual(self.data["availability"]["released_date"], "2026-10-02")
        self.assertTrue(self.data["availability"]["selectable"])
        self.assertTrue(self.data["availability"]["release_confirmed_by_official_announcement"])
        self.assertEqual(self.data["base_stats"]["maximum_health"], 800)
        self.assertEqual(self.data["base_stats"]["move_speed_meters_per_second"], 6.8)
        self.assertEqual(self.data["weapon"]["BulletsPerShot"], 2)
        self.assertEqual(self.data["weapon"]["BulletDamage"], 6.0)
        self.assertEqual([item["name"] for item in self.data["abilities"]], [
            "Scrap Grenade", "Rat Swarm", "Royal Pestments", "Rule, Ratannia!"
        ])
        self.assertEqual(
            self.data["generated_source_snapshot"]["hero_data"]["BoundAbilities"]["4"]["Name"],
            "Rule, Ratannia!",
        )

    def test_other_heroes_keep_their_earlier_pins(self):
        roster = json.loads((ROOT / "heroes/roster.yaml").read_text())
        self.assertEqual(roster["hero_count"], 39)
        others = [p for p in (ROOT / "heroes").glob("*/*.yaml") if p != RECORD]
        self.assertEqual(len(others), 38)
        for path in others:
            record = json.loads(path.read_text())
            self.assertEqual(record["client_version"], 6694, path)
            self.assertEqual(record["sources"]["ability_localization"],
                             "github.deadlock-data.english.fc4f540f12e0", path)

    def test_pre_release_data_is_explicitly_not_launch_data(self):
        previous = self.data["pre_release_comparison"]
        self.assertEqual(previous["client_version"], 6731)
        self.assertIn("never use as launch values", previous["status"])
        changed = previous["changed_hero_data_fields_before_release"]
        self.assertEqual(changed["BoundAbilities"], {})
        self.assertEqual(changed["MaxHealth"], 780.0)
        self.assertEqual(len(changed), 14)
        self.assertEqual(self.data["supporting_ability_data"]["not_numbered_in_hero_bound_abilities"], True)
        self.assertIn("npc_ratking_rat", self.data["supporting_npc_data"]["records"])

    def test_later_wiki_behavior_is_not_backdated(self):
        context = self.data["later_wiki_context"]
        self.assertEqual(context["as_of"], "2026-10-03")
        self.assertEqual(context["source"], "wiki.rat-king.180124")
        self.assertIn("not_launch_runtime_test", context["evidence_status"])
        self.assertIn("Spellbreaker", context["royal_pestments"])
        self.assertIn("Steam Vents", context["scope_note"])

    def test_description_sources_are_explicit_and_isolated(self):
        card, localization = {"DescKey": "launch_text"}, {"launch_text": "Example"}
        first = sync.descriptions.resolve(card, localization, source=sync.ENGLISH_SOURCE)
        second = sync.descriptions.resolve(card, localization, source="other-pin")
        self.assertEqual(first[0]["source"], sync.ENGLISH_SOURCE)
        self.assertEqual(second[0]["source"], "other-pin")
        with self.assertRaises(TypeError):
            sync.descriptions.resolve(card, localization)

    def test_bad_input_hash_fails_before_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "version.txt").write_text("wrong client")
            with self.assertRaisesRegex(ValueError, "version.txt SHA-256 mismatch"):
                sync.generate(directory, directory / "missing-pre-release.json")

    def test_importer_hashes_agree_with_registry(self):
        registry = yaml.safe_load((ROOT / "sources/source-registry.yaml").read_text())
        sources = {s["id"]: s for s in registry["sources"]}
        for filename, source in [("hero-data.json", sync.HERO_SOURCE),
                                 ("ability-data.json", sync.ABILITY_SOURCE),
                                 ("ability-cards.json", sync.CARD_SOURCE),
                                 ("english.json", sync.ENGLISH_SOURCE),
                                 ("npc-data.json", sync.NPC_SOURCE)]:
            self.assertEqual(sync.EXPECTED_HASHES[filename], sources[source]["sha256"])
        self.assertEqual(sync.EXPECTED_HASHES["version.txt"],
                         sources["github.deadlock-data.gameplay.dc1679b9606e"]["version_file_sha256"])
        self.assertEqual(sync.EXPECTED_PRE_RELEASE_HERO_SHA256,
                         sources[sync.PRE_RELEASE_SOURCE]["hero_data_sha256"])

    def test_ability_descriptions_and_source_ids_are_retained(self):
        for ability in self.data["abilities"]:
            self.assertTrue(ability["descriptions"])
            self.assertTrue(all(item["source"] == sync.ENGLISH_SOURCE for item in ability["descriptions"]))
            self.assertTrue(all("{" not in item["plain_text"] for item in ability["descriptions"]))
        self.assertEqual(self.data["sources"]["release_announcement"], sync.RELEASE_SOURCE)
        markdown = (ROOT / "heroes/rat-king/rat-king.md").read_text()
        self.assertNotIn("\\n", markdown)
        self.assertEqual(sync.render_markdown(self.data), markdown)
        self.assertIn("**Additional Info2 description**", markdown)
        self.assertIn("**Tier 3:**", markdown)


if __name__ == "__main__":
    unittest.main()
