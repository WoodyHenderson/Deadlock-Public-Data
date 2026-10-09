---
id: patch-review.2026-09-29-pre-rat-king
title: City Never Sleeps through the pre-Rat King checkpoints
domain: patches
topics: [City Never Sleeps, Haunts, breakables, Broker, September 30, October 1, pre-release]
aliases: [September 29 update review, pre-Rat King client history]
summary: Dated official intent and reviewed client-data changes from September 29 through the October 1 pre-release client 6731 checkpoint.
snapshot_id: deadlock-data-pre-rat-king-2026-10-01
current_as_of: "2026-10-01"
evidence_status: source_verified_with_unresolved_runtime_and_mode_details
sources:
  - valve.city-never-sleeps.2026-09-29
  - steam.news.city-never-sleeps.1844751498235383
  - wiki.update.2026-09-29.181123
  - wiki.update.2026-09-30.177156
  - wiki.haunt.177431
  - wiki.sinners-sacrifice.177553
  - github.deadlock-data.gameplay.9b8021ef9af8
  - github.deadlock-data.gameplay.2c01011bbc88
  - github.deadlock-data.gameplay.9830c72afd4e
  - github.deadlock-data.gameplay.527f1326b455
  - github.deadlock-data.gameplay.3d26c988891f
  - github.deadlock-data.gameplay.2553188680e4
  - github.deadlock-data.gameplay.4a3d36286650
  - github.deadlock-data.gameplay.0d46cdecfccf
---

# City Never Sleeps through the pre-Rat King checkpoints

**Date boundary:** client 6731 (October 1) is the last included checkpoint.
Client 6737 / the October 2 Rat King release is not part of this review. This
curated evidence summary is **not** a verbatim changelog: no September 29 or
September 30 raw changelog was present in the pinned upstream archive. Official
intent, generated client data, and later wiki interpretation are kept separate.

## Official September 29 intent

Valve announced a visual/map update; a neutral-camp rework using the player-facing
name Haunts; Steam Vents; Tough Crates and Healing Snacks; the Buff Container
rename and four additional permanent-buff categories; The Broker and Corrupted
Items; and six future hero names, with the first release scheduled for October
2. Announced feature presence does not supply all exact runtime details.

The update notes also state that ability/item inputs respond immediately; a
successful objective parry no longer resets parry cooldown; Sinner's Sacrifice
bonus timing is variable; Walker fireballs stop after the Walker dies; Yamato's
Flying Strike pathing against solid objectives was fixed; Graves can shoot
Venator's traps; and Street Brawl awards a corrupted item after the Round 5
item draft. These remain **patch-note intent**, not independent runtime tests.
Do not generalize the Yamato, Graves, parry, or Walker statements beyond their
named conditions.

## Dated client findings

| Checkpoint | Direct structured-data finding | Treatment |
| --- | --- | --- |
| Sep 25 client 6701 → Sep 29 client 6712/6722 | District/building labels; 42 new `neutral_*` family/tier keys and `citadel_basketball`; 11 prior NPC/helper keys removed; Tough Crate and Healing Snack records; ten Buff Container categories with 0/10/30-minute tiers; Sinner mini-game fields; Broker/convar configuration and corruption penalties. | Retain direct fields with their pins. NPC keys do not enumerate placed camps. Distinguish ordinary crates, Tough Crates, and Buff Containers. Do not treat a zero-filled price table as a shop price or a config as live availability. |
| Sep 29 client 6712 → 6722 | `MapDistrictLocalization` grows from 18 to 20 entries; other reviewed gameplay datasets match. | Additional labels only; no lane, route, or placement inference. |
| Sep 30 client 6723 | The four-entry breakable schedule's second descriptor changes from 180/180 to 300/300 seconds. Many NPC `WeaponInfos` → `Weapon` and hero/weapon/DPS fields appear together; one Venator trap field (`UntargetableModifier`, `IgnoredByNpcTargeting`) appears. | Record the schedule sequence, but keep the descriptor-to-breakable mapping provisional. Broad schema/export additions are not evidence that all hero/NPC stats changed at once. The trap field is direct configuration, not a player-targetability or runtime test. The trap field is not used to infer broader targeting mechanics. |
| Sep 30 client 6726 | `CorruptedUpgrades` appears on 95 item records and 11 penalty definitions are present; FireRate penalty tiers change from -20/-25 to -25/-30; Street Brawl Round 5 buy time changes from 50 to 65 seconds; Mid-Boss `ShieldLogic` is present at base absorption 35/second plus 5 per game minute; four tier-2 boss variants gain `SpawnOnGround: true`; internal `ability_digger_entertunnel` gains `BehaviorCannotCancelDuringChannel`. | The item-specific variant fields and penalty definitions are stored separately in `data/corrupted-items.yaml`. Do not infer availability by mode/date or combine variant bonuses with penalty rolls. Treat NPC spawn flags as configured fields, not proof of a changed live spawn. The internal tunnel ability is not assigned to the released roster. |
| Oct 1 clients 6728, 6730, 6731 | Client 6728 changes boss range-ring alpha, health/name-bar layout settings, photo-mode/ping/subtitle settings, text corrections, and a stat metadata field. Clients 6730 and 6731 change damage-indicator decay (0.5→0.3 seconds) and reporter polling interval (15→5), respectively. | Presentation, settings, copy, and telemetry; no reviewed standard-match gameplay balance delta. The 6726 Mid-Boss shield configuration remains through 6731. |

The second breakable descriptor therefore reads 300/300 in client 6701,
180/180 in 6722, and 300/300 from 6723 through 6731. The 6722 list also adds a
fourth 300/180 descriptor. The client does not label the new descriptor's map
class. Preserve the known September 16 tunnel mapping as a candidate; do not
silently remap either anonymous group.

## Rat King data boundary

Client 6722 already contains a `hero_ratking` entry, and the entry persists in
client 6731. Its `IsSelectable` field is true, but the announcement schedules
the first hero release for October 2; pre-release data presence and that flag
do not independently establish public match availability. The pre-release
hero record has no bound abilities; a generic-looking weapon block becomes
visible when the client exports weapon fields for heroes broadly. Do not use it
to claim Rat King's launch weapon, abilities, stats, or roster availability.
The launch review must compare the October 1 and October 2 client snapshots.

## Unresolved / excluded

- Existing map data supplies 40 named camp markers with tiers and 15 Sinner
  machine markers. The new [composition guide](../general/map/haunt-camps-and-sinner-sites.md)
  adds October 1 wiki camp patterns, family tiers, four Sinner configurations
  (15 machines/11 sites), and the all-machines/all-member-Haunts clear rule.
  This is sourced information, not independent runtime validation.
- Exact family/unit assignments at every named camp, the six unenumerated
  medium combinations, NPC eye-crit/strong-tier melee behavior and runtime
  spawn/activation remain unverified. October 6 wiki descriptions differing
  from October 1 are recorded separately, not treated as a gameplay patch.
- The October 6 coordinate layer is not an independently verified September 29
  placement snapshot; using it for that date retains the documented continuity
  assumption. Derived machine-name groups are not proof of hybrid membership.
- Sinner's `MiniGameFastChance`/`MiniGameFastSpeed` fields do not define the
  variable timing distribution or replace the separate Souls reward model.
- Broker standard/ranked availability, exact first opening/exit conditions,
  prices, and eligibility are not established for each date. Street Brawl's
  configured Round 5 item is mode-specific.
- Client data does not explain whether the breakable schedule change is a
  runtime rebalance, data extraction change, or category update.
- UI/settings-only and telemetry changes were classified but not copied into
  current gameplay rules.

## Published records and limits

The scoped imports are [map timings](../data/map-timings.yaml), the
[corrupted-item sidecar](../data/corrupted-items.yaml),
[Sinner configuration](../npcs/sinners-sacrifice/sinners-sacrifice.yaml), and the
[district](../general/map/districts-and-landmarks.md),
[timed-event](../general/map/timed-events-and-neutral-objectives.md), and
[visibility](../general/map/minimap-and-visibility.md) guides.
The [camp-composition sidecar](../data/haunt-camp-compositions.yaml) also records
pinned wiki patterns and connects the existing map inventory without assigning
unsupported families or unit counts to named markers.
Source commits, revisions, and file hashes are registered in
[the source registry](../sources/source-registry.yaml).

The root baseline, hero/item rosters, and separate map-coordinate snapshot have
not advanced. No private confirmations, internal planning, or private map
source identity are included. The public-only movement, lifesteal, and burst
coverage is preserved. See [limitations](../LIMITATIONS.md) for remaining gaps.
The October 2 release and all later balance/mode changes are separate imports.
