# Deadlock Data Reference

A manually maintained Deadlock knowledgebase. Start with the [keyword index](INDEX.md)
to find a hero, ability, item, or mechanic. Markdown explains behavior; adjacent
YAML preserves structured fields, source precision and dated evidence.

## Snapshot, not a live feed

Records have different cutoff dates. The September 3 root baseline is not a
claim that every record has been refreshed to the latest patch.

- **Baba:** canonical data checked through October 7/client 6763; the October 6/client-6759 launch snapshot is preserved separately. The October 7 export/wording review is not a claim of a gameplay hotfix. October 8 wiki interactions remain labeled as later context.
- **Sinclair and Rat King:** October 5/client 6753, including the balance changes
  and separately labeled patch-note-only behavior. Rat King's October 2 launch
  is preserved as a [historical snapshot](patches/snapshots/rat-king-2026-10-02.yaml).
- **Other 37 heroes and 173 items:** retain their client-6694 September 16 pins.
- **City Never Sleeps map mechanics:** scoped pre-release research through
  October 1, with separately dated wiki descriptions and explicit uncertainties.
- **Corrupted items:** the Broker toggle is dated October 2; the October 4
  Street Brawl removal is recorded separately. The client-6726 variant sidecar
  describes historical configuration, not current mode eligibility.
- **Map coordinates:** the separate October 6 snapshot is unchanged. Markers
  represent potential locations, not live availability or walking routes.

See the [Baba release](patches/2026-10-06-baba-release.md),
[October 7 source review](patches/2026-10-07-review.md),
[October 4/5 changes](patches/2026-10-05-balance.md), and
[limitations](LIMITATIONS.md) for exact scope and unresolved behavior.

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
