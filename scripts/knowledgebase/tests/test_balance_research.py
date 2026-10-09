"""Offline publication and chronology checks for research, not applied balance."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts/knowledgebase"))
import check_balance_research as audit


class BalanceResearchTests(unittest.TestCase):
    def test_manifest_is_complete_and_immutable(self):
        manifest = json.loads((audit.RESEARCH / "input-manifest.json").read_text())
        self.assertEqual(len(manifest), 40)
        self.assertEqual(len({(e["client"], e["path"]) for e in manifest}), 40)
        pins = {6737: "dc1679b9606effdc9bec37842ed40d8ca927092e",
                6746: "46c3fd0cfbf2108f48123e1dddd59e416db1b7ee",
                6753: "edb16660368ef3b693a4ac6d525697f5570a4dce"}
        for entry in manifest:
            self.assertEqual(entry["commit"], pins[entry["client"]])
            self.assertEqual(entry["url"],
                             f"https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/{entry['commit']}/{entry['path']}")
            self.assertRegex(entry["sha256"], r"^[a-f0-9]{64}$")

    def test_published_artifact_hashes_and_chronology(self):
        registry = yaml.safe_load((ROOT / "sources/source-registry.yaml").read_text())
        sources = {s["id"]: s for s in registry["sources"]}
        for suffix in ("46c3fd0cfbf2", "edb16660368e"):
            source = sources[f"github.deadlock-data.gameplay.{suffix}"]
            self.assertEqual(hashlib.sha256((ROOT / source["input_manifest"]).read_bytes()).hexdigest(),
                             source["input_manifest_sha256"])
        source = sources["github.deadlock-data.gameplay.edb16660368e"]
        ledger = ROOT / source["field_delta_ledger"]
        self.assertEqual(hashlib.sha256(ledger.read_bytes()).hexdigest(), source["field_delta_sha256"])
        lines = ledger.read_text().splitlines()
        self.assertEqual(len(lines), 85)
        self.assertTrue(all(line.startswith(("6737→6746 ", "6746→6753 ")) for line in lines))
        self.assertIn('6737→6746 generic-data.StreetBrawl.m_iCorruptItemRound: 5 → 0', lines)

    def test_source_shape_changes_are_not_flattened(self):
        self.assertEqual(list(audit.differences({"duration": {"Value": 1.7}}, {"duration": 1.7})),
                         [(".duration", {"Value": 1.7}, 1.7)])
        self.assertEqual(list(audit.differences({"tier": {"cooldown": -20}}, {"tier": {}})),
                         [(".tier.cooldown", -20, "<absent>")])

    def test_review_does_not_claim_canonical_import(self):
        text = (ROOT / "patches/2026-10-05-sinclair-rat-king-research.md").read_text()
        self.assertIn("Research only", text)
        self.assertIn("Patch-note-only for the assistant", text)
        self.assertIn("25.4 / 60.96m", text)
        self.assertNotIn("Planning/", text)
        self.assertNotIn(".git/research", text)


if __name__ == "__main__":
    unittest.main()
