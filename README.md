# Deadlock Data Reference

A community-maintained, source-attributed Deadlock data snapshot in Markdown and
YAML. It includes **38 heroes, 152 abilities, 173 items, 14 NPC records, two
claimable objectives, and 135 historical changelogs**.

Start with the [keyword index](INDEX.md) to find a hero, ability, item, or mechanic.
Use Markdown for readable explanations and adjacent YAML for structured fields.
This is a standalone data repository: it contains no application, model, planning
documents, evaluation answers, or private source notes.

## Snapshot, not a live feed

- Base snapshot: `deadlock-wiki-2026-09-03`
- Game-data client: `6684`; source revision: `10933105`
- Source access dates, wiki revisions, commits, and hashes are recorded separately.
- Ability descriptions resolve all 630 card references into 481 distinct entries:
  170 base/secondary descriptions and 311 upgrade descriptions.
- Historical changelogs cover **2024-05-03 through 2026-08-22**, including separate
  same-date and Hero Lab files.

A curation/access date is not a claim that the data matches today's game. An old
article revision does not itself pin separately transcluded data; generated
source records have their own references.

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
| [sources/source-registry.yaml](sources/source-registry.yaml) | Source attribution, revisions, and provenance |
| [LIMITATIONS.md](LIMITATIONS.md) | Source conflicts and intentionally omitted unsupported rules |
| [ATTRIBUTION.md](ATTRIBUTION.md) | Upstream credits and licensing boundaries |

### Source policy

Only **Deadlock Wiki**, **Deadlock API**, and the **Deadlock Wiki's
`deadlock-wiki/deadlock-data` repository** are used as published data sources.
The versioned API is the structured authority for item records; wiki-generated
data provides the secondary representation. Hero descriptions and changelogs
come from pinned wiki-data commits. Existing material source disagreements stay
visible rather than being silently merged.

Rules that relied on private confirmations or internal documents were excluded
from this edition. They have not been relabeled as wiki/API-verified. See
[limitations](LIMITATIONS.md) for the resulting coverage boundary.

### Historical archive boundary

The changelogs are useful for explicit historical or patch-note questions only.
They do **not** update, override, or supply missing facts in current entity
records. Consumers implementing search should exclude `patches/` by default.
Historical notes describe changes, not complete historical game states or proof
of observed runtime behavior.

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

Read [attribution and licensing](ATTRIBUTION.md) before redistributing or reusing
the material. Public availability is not a blanket unrestricted-use license.
This project is not affiliated with or endorsed by Valve.
