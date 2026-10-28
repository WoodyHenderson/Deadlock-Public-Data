# Deadlock Data Reference

A manually maintained Deadlock knowledgebase. Start with the [keyword index](INDEX.md)
to find a hero, ability, item, or mechanic. Markdown explains behavior; adjacent
YAML preserves structured fields, source precision and dated evidence.

## Snapshots

Records will frequently have different dates, I may do sweeping updates where each record is updated to the most recent client version, however, in most instances the only time something will have its client version updated is when that specific record itself NEEDS updated, meaning if Apollo last received changes on September 10th his record will probably say that its from the September 10th snapshot. Doing this any other way would just take way too much time.

TLDR: If the most recent patches have been included in the repo, even if most records say they're from previous patches it probably just means they don't need changes.

## Find information

| Path | Contents |
| --- | --- |
| [Hero roster](heroes/roster.yaml) | Hero stats, weapons, abilities, descriptions and upgrades |
| [Item roster](items/roster.yaml) | Item effects, conditions, descriptions and components |
| [NPC roster](npcs/roster.yaml) | Troopers, neutral enemies, structures and objectives |
| [Objective roster](objectives/roster.yaml) | Rejuvenator and Soul Urn |
| [General mechanics](general/) | Topic-specific gameplay explanations |
| [Structured facts](data/) | Economy, progression, timing and general rules |
| [Map guide](map/README.md) | Coordinates, named areas and breakable counts |
| [Historical patches](patches/README.md) | Dated changes and original patch notes |
| [Source registry](sources/source-registry.yaml) | Citations, source revisions and evidence scope |
| [Attribution](ATTRIBUTION.md) | Credits and licensing boundaries |

## Interpretation and retrieval

Prefer the dated canonical entity record for current-snapshot questions.
Use historical patches and snapshots for explicit questions about old values
or when something changed; do not mix different dates into one game state.

Client data establishes configured fields, not independent runtime verification.
Official notes establish announced changes; community descriptions and unresolved
source conflicts remain labeled. Raw flags and coefficients are not a complete
simulation. Bracketed controls such as `[Attack]` are bindable actions, not fixed
keyboard defaults. Numeric upgrade bonuses are distinct from final totals.

Most generated `.yaml` records use JSON syntax, which is valid YAML 1.2; other
records use native YAML. No application, developer tooling, research ledgers,
private interaction tables, source-site code or media is included.

Public source-backed knowledge uses pinned Wiki/API/client data and narrowly
cited official announcements. Omitted private-only claims are not represented
as publicly verified facts. See [attribution](ATTRIBUTION.md) and
[limitations](LIMITATIONS.md) before redistributing or interpreting the records.

This is an independent, non-commercial project and is not affiliated with Valve.
