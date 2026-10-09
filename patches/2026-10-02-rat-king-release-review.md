---
id: patch-review.2026-10-02-rat-king-release
title: October 2 Rat King release review
domain: patches
topics: [Rat King, hero release, Broker, October 2]
aliases: [Rat King launch review, client 6737 release checkpoint]
summary: Official Rat King release intent and adjacent client 6731-to-6737 findings, kept separate from later October 5 balance changes.
snapshot_id: deadlock-data-client-6737
current_as_of: "2026-10-02"
evidence_status: source_verified_with_later_wiki_interpretations
sources:
  - steam.news.rat-king-release.1845383656387709
  - wiki.update.2026-10-02.181191
  - wiki.rat-king.180124
  - github.deadlock-data.gameplay.0d46cdecfccf
  - github.deadlock-data.hero-data.dc1679b9606e
  - github.deadlock-data.ability-data.dc1679b9606e
  - github.deadlock-data.ability-cards.dc1679b9606e
  - github.deadlock-data.english.dc1679b9606e
  - github.deadlock-data.npcs.dc1679b9606e
  - github.deadlock-data.gameplay.dc1679b9606e
---

# October 2 Rat King release review

**Date boundary:** client 6737, version source revision 11076133, is the launch
checkpoint reviewed here. Client 6753 and October 5 balance changes are later
and are not used for launch values. No October 2 raw changelog was present in
the pinned `deadlock-data` archive; this is a curated review, not a fabricated
raw patch file.

## Official release and client evidence

Valve's Steam announcement, published October 2 at 20:59:51 UTC, says Rat King
is available to play. The client-6737 hero data also marks him selectable, but
that flag was already true in the pre-release client 6731; the official release
announcement establishes public availability. The October 2 wiki update page
(revision 181191, last edited October 4) is a later transcription. Its
separate **Undocumented Changes** section reports that the Broker is no longer
accessible in standard and ranked modes; that line is wiki interpretation,
not official patch-note wording.

| Record | Client 6731 (Oct 1) | Client 6737 (Oct 2) | Treatment |
| --- | --- | --- | --- |
| `hero_ratking` release state | `IsSelectable: true`, but `BoundAbilities` is empty. | Still selectable; four numbered abilities are bound, with launch weapon, base stats, growth and card data. | The playable release is dated by Valve's announcement, not by the pre-release flag. `heroes/rat-king/rat-king.yaml` stores client-6737 launch data and a separate comparison of changed pre-release fields. |
| Base/weapon fields | Partial pre-release values, including 780 health, 7.2 move speed, and a generic-looking weapon block. | 800 health, 6.8 move speed, 3 stamina, 6 bullet damage, 5 rounds/s, 24-round magazine, two bullets per shot, and weapon key `citadel_weapon_ratking_set`. | Do not treat client 6731's incomplete values as the launch build or reverse-engineer launch behavior from the pre-release block. The full source records and all ability/card fields are retained in the hero YAML. |
| Rat King abilities | No bound abilities; no Rat King ability records in `ability-data.json`. | Four numbered ability/card records appear: Scrap Grenade, Rat Swarm, Royal Pestments, and Rule, Ratannia! Supporting ability records and `npc_ratking_rat` also appear. | Imported the four numbered launch abilities with pinned English descriptions. Supporting records are kept apart from the numbered card list; client field presence is not a runtime test. |
| Broker shop | `citadel_corrupted_item_shop_enabled: true`. | The same convar is `false`. | Record the on/off sequence. The Oct 2 wiki transcription says no longer accessible in standard/ranked; Street Brawl availability is not resolved by this review. |
| Other dataset differences | — | `generic-data` and `item-data` match client 6731. `misc-data` adds `DebuffType` metadata to three regen records. `hero-data` changes `hero_familiar.Type` (missing→`Mystic`), `hero_necro`/`hero_unicorn.Type` (`Marksman`→`Mystic`), and both werewolf form types (`Marksman`→`Brawler`); pre-release Baba `LevelScaling.LightMeleeDamage`/`HeavyMeleeDamage` change `0.8`/`1.856`→`1.1`/`2.552`. Besides the Broker toggle, convars add `citadel_ping_can_heal_range: 2500` and two settings-menu defaults, and remove the rendering field `r_particle_explicit_fetch` (previously false). `hero-meaningful-stats` adds true flags for bullet/spirit lifesteal effectiveness; this is display metadata, not a change to every hero's effectiveness. `npc_neutral_bug` respawn changes 30→15 and gains `ReplacementChance: 0.1` / `ReplacementSubclass: npc_neutral_bug_rat`; two rat NPC records are added. The Street Brawl `item-buckets.AvailableItems` list is reordered. | No broad item or map-timing change is inferred. The ping convar description is recorded in the [minimap/visibility guide](../general/map/minimap-and-visibility.md) as client configuration intent, not tested behavior. Type fields and Baba's pre-release scaling are not silently advanced in other hero records. Neutral-bug rat config does not establish camp placement/composition or an association with Rat King's summoned rats. |

The pre-release-to-launch values are recorded in the Rat King hero YAML under
`pre_release_comparison.changed_hero_data_fields_before_release`, labeled as
incomplete and never as launch values. In the new neutral-bug records,
`npc_neutral_bug_rat_swarm.SwarmModifier` contains configured `RatDuration: 6`,
`DamagePerRatPerSecond: 2`, `DamageInterval: 0.5`, and `DashDropFraction: 0.5`;
these are data fields, not a confirmed camp/hero interaction. The separate
`npc_ratking_rat` record is kept with the Rat King import by its distinct key.
The source-pinned card and ability fields support queries about configured
values; descriptions do not establish independent game behavior.

## Broker boundary

By client 6737 the shop-enabled convar is false, following true values through
client 6731. The later October 2 update transcription says the Broker is no
longer accessible in standard and ranked modes. Keep this evidence scoped to
those modes. This review does not establish whether Street Brawl's Round 5
corrupted-item award or any other corrupted-item behavior was available after
the release; the October 4 mode update is a separate step.

## Later wiki context

Rat King's early article revision 180124 (October 3, marked Construction) says
he can enter and exit map tunnels by pressing crouch next to a vent and cannot
enter while in combat. This is a **later wiki description**, not a client
6737 field-level explanation or a runtime test. It also says Spellbreaker does
not proc on damage dealt to the Royal Pestments barrier. Both descriptions are
preserved separately in the hero record. Tunnel vents are not identified as
Steam Vents by this evidence. The prose is not used to infer the behavior of
the unnumbered `ability_ratking_entertunnel` record. The Oct 7
article's additional details and all October 5 balance notes are outside this
launch review.

See the [Rat King launch record](../heroes/rat-king/rat-king.md) for the scoped
canonical import and [limitations](../LIMITATIONS.md#rat-king-release-boundary)
for the remaining evidence and later-date boundaries.
