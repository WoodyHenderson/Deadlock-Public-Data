---
id: patch-research.2026-10-05-sinclair-rat-king
title: October 5 Sinclair and Rat King balance research
domain: patches
topics: [historical research, Sinclair, Rat King, October 4, October 5]
summary: Source-pinned adjacent-client findings; research only, not applied canonical balance changes.
snapshot_id: research-clients-6737-6746-6753
current_as_of: "2026-10-09"
evidence_status: source_verified_research_not_applied
sources:
  - github.deadlock-data.gameplay.dc1679b9606e
  - github.deadlock-data.gameplay.46c3fd0cfbf2
  - github.deadlock-data.gameplay.edb16660368e
  - github.deadlock-data.changelog.2026-10-05.edb16660368e
  - steam.news.balance.1845383656394833
  - wiki.update.2026-10-04.181723
  - wiki.update.2026-10-05.184305
---

# October 5 Sinclair / Rat King patch research

**Research only:** source pins and findings are published here; canonical hero/mechanics records and the raw archive are unchanged. October 4 is an intervening checkpoint, not part of the October 5 nerfs. The patch contains Rat King buffs as well as nerfs.

## Reproducible evidence

| Checkpoint | Immutable deadlock-data commit | Client / source revision |
| --- | --- | --- |
| October 2 launch | `dc1679b9606effdc9bec37842ed40d8ca927092e` | 6737 / 11076133 |
| October 4 | `46c3fd0cfbf2108f48123e1dddd59e416db1b7ee` | 6746 / 11080740 |
| October 5 | `edb16660368ef3b693a4ac6d525697f5570a4dce` | 6753 / 11087340 |

Downloaded 40 inputs: version, hero data, ability data/cards, NPCs, Street Brawl, convars, item data/cards, generic/misc data, meaningful-stat metadata and English localization for each client, plus the October 5 raw changelog. Each URL and byte hash is in [the input manifest](research/2026-10-05/input-manifest.json). The [85-leaf field-delta ledger](research/2026-10-05/field-deltas.txt) covers nine structured datasets over both transitions; the unchanged item-card/meaningful-stat checks and separate localization changes are described below.

- [Pinned raw October 5 notes](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/changelogs/raw/2026-10-05.txt). SHA-256: `97f051205a4a48b58ace49ef0aa71dd84da047ccbcdd96fa32c964df44d3a304`.
- [Official Steam announcement](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1845383656394833), **Minor Update - 10-05-2026**, GID `1845383656394833`, published **2026-10-05 23:05:32 UTC**. Retrieved through the Steam news API. Its `contents` UTF-8 SHA-256 is `be200138d80e244d57f2c22b81e839e9cd34989faa6895ab1ace75de523a3d08`. Official text agrees with the archived patch lines inspected here.
- [October 5 wiki transcription, revision 184305](https://deadlock.wiki/Update:October_5,_2026?oldid=184305), edited October 7 at 00:09:07 UTC. Wikitext SHA-256: `7bf571018fbc5901f408112371228944c84340787fe288116710e81b4e215358`.
- [October 4 wiki update, revision 181723](https://deadlock.wiki/Update:October_4,_2026?oldid=181723), edited October 5 at 23:10:10 UTC. Wikitext SHA-256: `9b2a54273fdc1e7302e180d9ca48c123d3e9d2929da5d36d11e5c5400fe2bcd1`. Its removal claim is explicitly under **Undocumented Changes**, not official October 5 wording.

The checked-in manifest contains immutable URLs and hashes for reproducing the client downloads. Later article edit dates are not patch dates. The October 5 raw notes exist upstream but have not yet been added to this repository's raw archive.

To verify downloaded inputs and reproduce the ledger offline, retain the manifest's directory/file layout (`CLIENT/data__json__NAME.json`, with slashes replaced by double underscores for other paths), then run:

```sh
python scripts/knowledgebase/check_balance_research.py --inputs-dir /path/to/downloads
```

This verifies source hashes and recorded differences, not runtime behavior.

## Rat King: October 4 → October 5

Internal keys: `hero_ratking`; `ability_ratking_scrap_grenade`, `ability_ratking_ratnibble`, `ability_ratking_standard_bearer`.

| Field / rule | Before | After | Evidence / treatment |
| --- | --- | --- | --- |
| Scrap Grenade damage per shrapnel | 65 | 70 | `DamagePerShrapnel.Value`, card and official notes |
| Scrap Grenade tier 2 damage bonus | +65 | +70 | `Upgrades[1].DamagePerShrapnel`, card and notes |
| Scrap Grenade bounce targeting | Bugs reported | Fix announced | Patch-note-only behavior; no specific corrective field identified |
| Rat Swarm base cooldown | 28s | 24s | `AbilityCooldown.Value`, card and notes |
| Rule, Ratannia! base cooldown | 130s | 160s | `AbilityCooldown.Value` |
| Damage reduction | 20% | 15% | `AllyDamageReduction` |
| Radius | 24m | 20m | `Radius.Value` and both card sections |
| Charge duration | 12s | 10s | `AbilityDuration.Value` |
| Bonus move speed | 3 with spirit coefficient 0.05 | 3, no scale object | Source changes structured scaled field to scalar; notes explicitly say no longer Spirit-scaled |
| Falling during charge | — | Faster falling announced | Patch-note-only behavior; no numeric falling field delta identified |
| Tier 1 move-speed bonus | +1m/s | +2m/s | `Upgrades[0].BonusMoveSpeed` |
| Tier 1 cooldown bonus | -20s | Removed | `Upgrades[0].AbilityCooldown` removed; notes give upgraded total 110s → 160s |
| Tier 2 charge-duration bonus | +8s | Removed | `Upgrades[1].AbilityDuration` removed; notes give upgraded total 20s → 10s |
| Tier 2 flag-duration bonus | +8s | +5s | `Upgrades[1].FlagDuration` |
| Tier 3 damage-reduction bonus | +15% | +10% | `Upgrades[2].AllyDamageReduction`; notes give total 35% → 25% |

All listed numeric deltas agree with the inspected client fields/cards. Do not mistake tier bonuses for final totals. Preserve unchanged tier-2 +8m radius and tier-3 +150 damage fields. Rat King's hero-data block and Royal Pestments configuration do not change in either transition.

## Sinclair: October 4 → October 5

Internal keys: `hero_magician`; `ability_magician_magicbolt`, `ability_magician_cloneturret`, `ability_magician_animalhexarea`, `ability_magician_copyult`.

| Field / rule | Before | After | Evidence / treatment |
| --- | --- | --- | --- |
| Base health regeneration | 2/s | 1/s | `BaseHealthRegen` |
| Bullet damage | 17.76 | 16.5 | `Weapon.BulletDamage` |
| Gun falloff start/end | **25.4 / 60.96m** | **20 / 60m** | Exact client fields; official notes round old values to 25–61 |
| Source weapon DPS | 48.327 | 44.898 | Generated weapon metadata, not independent runtime DPS |
| Source sustained DPS | 33.909 | 31.504 | Generated weapon metadata |
| Vexing Bolt objective damage | No exported `BossDamageScale` field | `BossDamageScale: 0.5` | Notes say half damage to objectives; absence is not a separately measured old multiplier or complete target taxonomy |
| Spectral Assistant falloff | Notes: 25–61m | Notes: 20–60m | **Patch-note-only for the assistant:** its ability-data record does not change and exposes no separate falloff delta; do not invent a clone inheritance field |
| Rabbit Hex radius | 6.5m | 6m | `Radius.Value`, card and notes |
| Rabbit Hex tier 3 radius bonus | +3m | +2m | `Upgrades[2].Radius`, card and English text |
| Audience Participation copy window | 12s | 9s | `CopiedUltWindow.Value` and card |
| Copied cooldown percentage | 40% | 60% | `CopyCooldownPercentage` and card; retain its meaning as a copied cooldown percentage, not a generic cooldown-reduction stat |

Sinclair's repository record currently uses client 6694, not 6746. Before implementation, reconcile any intervening canonical/source differences separately; do not label every difference from that old record an October 5 nerf.

## Localization and cards

Reviewed all 12 Sinclair and 15 Rat King description keys referenced by client-6753 cards against client 6746. Four referenced English strings change:

- Sinclair Rabbit Hex tier 3: +3m → +2m radius; +7% damage amp remains.
- Rat King ultimate tier 1: removes -20s cooldown and changes +1m → +2m movement text.
- Ultimate tier 2: removes +8s charge duration; +8s → +5s flag duration; +8m radius remains.
- Ultimate tier 3: +15% → +10% damage reduction; +150 damage remains.

An implementation must update raw descriptions, rendered text, numeric card fields and structured ability data together. Do not regenerate from launch English after applying the new upgrades.

## Intervening October 4 changes — keep separate

Client 6737 → 6746:

- `generic-data.StreetBrawl.m_iCorruptItemRound`: **5 → 0**. The later wiki explicitly reports corrupted items removed from Street Brawl. Pair the field change with that dated interpretation; zero alone does not define engine semantics.
- Rat King tunnel `AbilityChannelTime`: `{Value: 1.7, Scale: {Value: 1, Type: duration}}` → scalar `1.7`. Digger likewise changes a duration-scaled object to scalar `1.0`. These are source-shape changes; do not claim independently tested scaling removal or release availability for Digger.
- Five Trooper records (`trooper_base`, `trooper_medic`, `trooper_melee`, `trooper_normal`, `trooper_zipline_container`) change `Acceleration` **200 → 1000** and `StrafeSpeed` **0 → 3.81**.
- Hero data/cards, item data/cards, Street Brawl's separate dataset, convars, misc data and meaningful-stat metadata are unchanged in the compared pair. The Street Brawl toggle is in **generic-data**, not street-brawl-data.

## Troopers and additional October 5 changes

- The same five Trooper records change `Acceleration` **1000 → 200** at client 6753; `StrafeSpeed: 3.81` remains. Official notes say Troopers walking too slowly were fixed. Record the announced behavior separately: these numeric fields alone do not explain the runtime bug or prove a new walk-speed formula.
- Prerelease Baba melee growth changes: light **1.1 → 0.7**, heavy **2.552 → 1.624**. Preserve as prerelease evidence for later Baba research, not a released hero import here.
- Tough/wooden crates add `BreakDebrisSpeed` **150 / 75**. Debris configuration, not evidence of changed Souls, spawn times, break methods or coordinates.
- `generic-data.ResourceTypes` adds `ResourceType_Blood` with empty `CantCastOutOfResourceToken` and `HUDSnippetName: blood`. Metadata only; do not infer mechanics or a released hero from it.
- Eighteen changed convar keys concern crosshair, damage-report grouping, minimap effects, spectator camera, player-camera toggle, subtitles and overlay pooling. Full old/new records are in the ledger. They do not establish balance changes, reveal ranges or new ability effects.
- Item data/cards, Street Brawl data and meaningful-stat metadata are unchanged between 6746 and 6753. No broad item refresh is justified by this comparison.

## Snapshot boundary and remaining limits

This historical review does not override canonical records. Rat King remains at his October 2 launch pin; Sinclair remains at client 6694. October 4 mode eligibility and October 5 balance need separate, explicitly dated canonical imports before they become current snapshot values.

A future import must preserve the reconstructible launch record, distinguish tier bonuses from totals, update localized descriptions with the numeric fields, and retain the behavior-only qualifications above. The existing raw archive, map geometry, unrelated heroes, item records and combat/movement coverage are unchanged by this research publication.

**Evidence gaps:** no independent runtime tests; no numerical bounce/falling fix fields; no separate Spectral Assistant falloff field delta; no full objective target list from `BossDamageScale`; no demonstrated causal formula for the Trooper fix. These do not prevent a source-qualified import. No gameplay data has yet been changed by this research pass.
