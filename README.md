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

The Rat King has a separate, date-scoped launch record pinned to client 6737 and
Valve's October 2, 2026 availability announcement. This addition does not advance
the September 3 baseline or incorporate later balance changes.

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
changelogs come from pinned wiki-data commits. The Rat King release date is also
supported by Valve's official Steam announcement; it does not establish numeric
mechanics. Existing material source disagreements stay visible rather than being
silently merged.

Gameplay rules that relied on private confirmations or internal documents were excluded
from the September 3 baseline. They have not been relabelled as wiki/API-verified. See
[limitations](LIMITATIONS.md) for the resulting coverage boundary.

### Historical archive boundary

The changelogs are useful for explicit historical or patch-note questions only.
They do **not** update, override, or supply missing facts in current records. If
you are implementing search I suggest you exclude `patches/` by default. Use it
for more simple questions regarding older values such as "What was the highest 
max weapon damage intensifying mag ever provided" or something along those lines.

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
behavior. Validation runs without network access and makes no changes. This export does not include an
automated data updater. Future updates should pin sources, retain prior evidence,
review changes, and regenerate the affected records and index together.

Again, this is just a sister project for something personal, it is not affiliated 
with Valve and is not used for any form of commercial or monetary gain.
