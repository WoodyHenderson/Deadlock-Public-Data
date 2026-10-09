# Deadlock Data Reference

A maybe-maintained Deadlock data snapshot used for training data as a fun side project. 
It includes all the data I could get my hands on from a variety of sources including
far too much manual interaction testing and information gathering.

Start with the [keyword index](INDEX.md) to find a hero, ability, item, or mechanic.
Use Markdown for readable explanations and adjacent YAML for structured fields.
This is a standalone data repository: it contains no application, model, planning
documents, evaluation answers, or private source notes.

## Snapshot, not a live feed

This does not update live, if it is staying updated it's me manually maintaining it,
Deadlock patch notes are nowhere near all-encompassing, they leave significant amounts
of information out of the patch notes intentional or not so I will try my best to
use my own knowledge of the game, community available information and Valve published
information to keep as accurate a snapshot as I can. 

Base snapshot was created from the Sep 3rd patch and then expanded upon from there
(right before the first major patch in 9 months thanks Yoshi)

The September 3 root baseline remains in place. The original 38 hero and 173 item records,
plus selected economy and mechanics records, have a separately dated refresh from
client 6694 (September 16, source revision 11005995). See the [client-6694 review](patches/2026-09-16-client-6694-review.md) for its scope and limits.

A scoped **September 29–October 1 City Never Sleeps refresh** now covers map and
breakable configuration, Sinner timing caveats, four-district prose, and a dated
sidecar of 95 corrupted-item variants and 11 penalty definitions. It stops at
**client 6731, before Rat King's October 2 release**. Later wiki geography is
labeled interpretation, not a launch-day placement snapshot. Hero/item rosters,
map coordinates, and the root baseline are unchanged by this refresh. See the
[pre-Rat King review](patches/2026-09-29-city-never-sleeps-pre-rat-king-review.md)
and [limitations](LIMITATIONS.md#city-never-sleeps-boundary).
The [camp-composition guide](general/map/haunt-camps-and-sinner-sites.md) adds
pinned pre-release wiki family tiers, camp patterns, and Sinner configurations
(15 machines/11 sites), tied to the existing map-marker inventory. Later wiki
differences are explicit; exact family/unit assignments at every named camp
remain incomplete rather than being inferred.
The [map-interaction pass](general/map/map-interactions-and-open-questions.md)
adds source-dated family attacks, vent rules, snack healing, breakable rewards,
buff selection and Sinner reward/jackpot interpretations. Three neutral tier
baselines and Mid-Boss combat fields are cross-checked to client 6731 without
advancing unrelated NPCs or the root baseline. Remaining conflicts and the
uncompleted placement re-audit are listed in that guide.

A separate **October 2/client-6737 Rat King launch import** adds the 39th hero,
including weapon/stats, four abilities, cards/upgrades and pinned English text.
The other 38 heroes keep their previous pins. It also records the Broker toggle
and healing-ping configuration; October 3 wiki tunnel/barrier behavior is
explicitly later evidence. See the [launch record](heroes/rat-king/rat-king.md),
[release review](patches/2026-10-02-rat-king-release-review.md) and
[release boundaries](LIMITATIONS.md#rat-king-release-boundary). October 4/5
mode/balance changes are not applied.

## Contents

| Path | Contents |
| --- | --- |
| [heroes/roster.yaml](heroes/roster.yaml) | Selectable heroes, stats, weapons, abilities, descriptions, and upgrades |
| [items/roster.yaml](items/roster.yaml) | Purchasable items, descriptions, displayed effects, conditions, and components |
| [npcs/roster.yaml](npcs/roster.yaml) | Troopers, neutrals, structures, Mid-Boss, and Sinner's Sacrifice |
| [objectives/roster.yaml](objectives/roster.yaml) | Rejuvenator and Soul Urn |
| [general/](general/) | Wiki-sourced gameplay and mechanics explanations |
| [data/](data/) | Structured economy, progression, timing, and general rules |
| [patches/](patches/) | Historical changelogs, isolated from the current snapshot |
| [map/README.md](map/README.md) | Separately pinned map coordinates and breakable counts by named area; potential locations, not live availability |
| [sources/source-registry.yaml](sources/source-registry.yaml) | Source attribution, revisions, and provenance |
| [LIMITATIONS.md](LIMITATIONS.md) | Source conflicts and intentionally omitted unsupported rules |
| [ATTRIBUTION.md](ATTRIBUTION.md) | Upstream credits and licensing boundaries |

### Source policy

The September 3 gameplay baseline uses only **Deadlock Wiki**, **Deadlock API**,
and the **Deadlock Wiki's `deadlock-wiki/deadlock-data` repository** as published
data sources. The versioned API is the structured authority for item records; 
wiki-generated data provides the secondary representation. Hero descriptions and
changelogs come from pinned wiki-data commits. Structured client snapshots can
advance specific records without advancing the root baseline. Existing material
source disagreements stay visible rather than being silently merged.
The City Never Sleeps refresh additionally cites Valve's official announcement
and its Steam news entry for dated feature intent, not runtime verification;
the exact official URLs and source pins are recorded in the registry.
Rat King's availability is separately confirmed by the pinned October 2 Valve
Steam announcement, not by the pre-release selectable flag alone.

Gameplay rules that relied on private confirmations or internal documents were excluded
from the September 3 baseline. They have not been relabelled as wiki/API-verified. See
[limitations](LIMITATIONS.md) for the resulting coverage boundary.

### Historical archive boundary

The raw changelog archive is useful for explicit historical or patch-note
questions. It does not by itself update or override current records; curated
dated reviews keep patch-note intent separate from pinned structured data. If
you are implementing search I suggest you exclude `patches/` by default. Use it
for more simple questions regarding older values such as "What was the highest 
max weapon damage intensifying mag ever provided" or something along those lines.

### Reproduce the Rat King launch import

Provide the pinned client-6737 `version.txt`, `hero-data.json`, `ability-data.json`,
`ability-cards.json`, `english.json` and `npc-data.json`, plus the client-6731
hero file. The importer verifies hashes and only targets Rat King's two files:

```sh
python scripts/knowledgebase/sync_rat_king_from_launch.py \
  --data-dir /path/to/client-6737 \
  --pre-release-hero-data /path/to/client-6731/hero-data.json --check
```

The adjacent release checker takes the eleven JSON datasets named in its
`EXPECTED_CHANGES` inventory from each client and checks all 22 hashes:

```sh
python scripts/knowledgebase/check_rat_king_release.py \
  --pre-release-dir /path/to/client-6731 --launch-dir /path/to/client-6737
```

These are offline source/configuration checks, not runtime tests. Rendering
helpers have no network access or corpus-wide write operation.

### Record format

Most generated `.yaml` records use JSON syntax, which is valid YAML 1.2. General
rules and some objective records use native YAML; use a YAML parser for the full
corpus. Preserve raw precision, scaling types, field provenance, and exceptions.
Raw flags and numeric deltas are not automatically complete runtime formulas.

`abilities[].descriptions` retains localization keys, card paths, original text,
normalized plain text, and source IDs. Bracketed controls such as `[Attack]`
represent bindable actions, not fixed keyboard defaults. Numeric-only upgrades
remain in the numeric fields; tooltip text never silently replaces those fields.

Evidence labels describe source support, not independent in-game validation:

- `source_verified`: supported by the cited source artifact.
- `source_conflict`: sources disagree; do not assume a disputed value is settled.
- `needs_primary_verification`: incomplete or uncertain source evidence.
- `derived`: calculated or organized from other records, including the index.

## Validation

Python 3.9+ is sufficient; validation requires PyYAML:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
python scripts/validate.py
```

Validation checks local links, YAML parsing, roster counts, description coverage,
source references, allowed source origins, historical file hashes, and lifesteal
rule consistency with canonical records (including upgrade gates and mode
isolation), and baseline burst profiles against canonical weapon fields and
API-derived averages. These checks validate local data consistency, not in-game
behavior. Validation runs without network access and makes no changes.

Additional offline regression checks:

```sh
python -m unittest discover -s scripts/knowledgebase/tests
python -m unittest discover -s scripts/map -p 'test_*.py'
```

There is no general upstream auto-updater. The map importer normalizes authorized
local inputs; the corrupted-item generator extracts only two hash-pinned
client-6726 local files and does not fetch data:

```sh
python scripts/knowledgebase/sync_corrupted_items.py \
  --item-data /path/to/client-6726/item-data.json \
  --generic-data /path/to/client-6726/generic-data.json --check
```

Remove `--check` only to regenerate that sidecar from the same pinned inputs.
To reproduce the read-only NPC, breakable, snack and ten-category buff cross-check,
provide the three client-6731 files (hashes are verified against the registry):

```sh
python scripts/knowledgebase/check_map_client.py \
  --npc-data /path/to/client-6731/npc-data.json \
  --misc-data /path/to/client-6731/misc-data.json \
  --generic-data /path/to/client-6731/generic-data.json
```

This checks configured values, not independent runtime behavior or wiki claims.
Future updates should pin sources, retain prior evidence, review changes, and
regenerate the affected records and index together.

Again, this is just a sister project for something personal, it is not affiliated 
with Valve and is not used for any form of commercial or monetary gain.
