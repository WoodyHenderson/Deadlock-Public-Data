---
id: general.map.timed-events-and-neutral-objectives
title: Timed Events and Neutral Objectives
domain: general
topics:
  - map-timings
  - neutral-camps
  - Mid-Boss
  - Soul-Urn
  - powerups
  - Unstable-Rift
aliases:
  - jungle camps
  - denizens
  - Haunts
  - Buff Containers
  - Tough Crates
  - Healing Snacks
  - The Broker
  - map events
summary: Neutral Haunt camps, recurring map events, breakable types, and unresolved date/mode-specific mechanics.
snapshot_id: deadlock-data-pre-rat-king-2026-10-01
current_as_of: "2026-10-01"
evidence_status: source_conflict
sources:
  - wiki.the-cursed-apple.125757
  - wiki.mechanics.110139
  - wiki.neutral.125766
  - wiki.souls.157718
  - wiki.haunt.177431
  - wiki.sinners-sacrifice.177553
  - wiki.update.2026-09-29.181123
  - valve.city-never-sleeps.2026-09-29
  - github.deadlock-data.gameplay.fc4f540f12e0
  - github.deadlock-data.changelogs.raw.fc4f540f12e0
  - github.deadlock-data.gameplay.9830c72afd4e
  - github.deadlock-data.gameplay.527f1326b455
  - github.deadlock-data.gameplay.3d26c988891f
  - github.deadlock-data.gameplay.0d46cdecfccf
---

# Timed Events and Neutral Objectives

The map adds resources and objectives as match time advances. Exact canonical
times are stored in `data/map-timings.yaml`.

## Baseline Schedule

| Time | Event |
| --- | --- |
| 0:00 | Mid-Boss is present in the central underground area. |
| 2:00 | Small Haunt camps spawn. |
| 3:00 | Base Soul Wells activate; regular crates, Tough Crates, Healing Snacks, and Tier 1 Buff Containers have a configured initial spawn/delay of 180 seconds. |
| 5:00 | Medium Haunt camps and temporary powerups spawn. Client 6731's second breakable schedule descriptor is 300/300 seconds; its tunnel mapping is carried forward from the September 16 patch-note comparison but remains a candidate after the client-6722 discrepancy. |
| 8:00 | Large Haunt camps and Sinner's Sacrifice locations spawn. |
| 10:00 | Soul Urn cycle begins; Tier 2 Buff Containers and mid-boxes spawn. Mid-boxes respawn after 3 minutes. |
| about 11:00 | First Unstable Rift appears, subject to a random timing window and contest setup. |
| 12:00 | Lane Guardians reach their minimum timed damage resistance. |
| 18:00 | Walkers reach their minimum timed damage resistance. |
| 20:00 | Trooper wave interval changes from 30 seconds to 25 seconds. |
| 30:00 | Buff Containers use their Tier 3 configured reward pool. |
| 35:00 | Trooper wave interval changes to 20 seconds and Troopers gain 50% maximum health. |

## Haunt Camps

The September 29 update uses **Haunts** as the player-facing name for neutral
camps. Client datasets retain `neutral_*` internal keys; that naming does not
prove every key is placed in a match. Valve's announcement names Specimen,
Gutter Ghoul, Barrel Mimic, Past Dues, Stage Hands, Crabbage Pot, Festival
Spirit, Shrooms, and Underhands. The [camp-composition and Sinner-site guide](haunt-camps-and-sinner-sites.md)
adds pinned wiki family tiers and composition patterns and links the existing
40 named camp markers. Exact family/unit assignments to every named camp are
not established by the unit-key inventory or the inspected wiki articles.

Haunt units belong to neither team and attack when provoked. A unit's Soul
bounty is shared equally among allied players who damaged it, and the reward is
Unsecured Souls. Haunts do not release Soul Orbs.

| Camp tier | First spawn | Respawn after full clear | Minimap mark |
| --- | --- | --- | --- |
| Small | 2:00 | 1:25 | Triangle with no line |
| Medium | 5:00 | 4:50 | Triangle with one line |
| Large | 8:00 | 5:35 | Triangle with two lines |

The respawn timer starts when the last unit in the camp is killed. Haunt
health increases by 2.1% per minute and damage by 0.5% per minute. Larger
Haunts have higher base bounties. Large neutrals take 20% less melee damage in
an older wiki interpretation, but that behavior conflicts with the wording of
the earlier patch that introduced it. The strong neutral tier's
`MELEE_RESIST_REDUCTION` field is absent from client 6722; field removal alone
does not prove the runtime rule was removed. Keep the melee interaction
unresolved pending direct verification.

## Mid-Boss and Rejuvenator

The Mid-Boss is a durable central neutral with a shield. Its initial respawn
delay is seven minutes after defeat, then six minutes after the next defeat,
and five minutes after subsequent defeats. Shield-absorption fields are absent
from the client-6722 NPC record, then present in clients 6726 and 6731 at 35
absorption per second plus 5 per game minute. This is structured-data history,
not independent runtime verification.

Defeating it drops the Rejuvenator crystal. The crystal must be claimed with
three heavy melee hits. Each successful claim hit grants the team a revive
credit, up to three. A credit revives a hero at their death location after three
seconds and is then consumed. The first claim hit also heals the claiming hero
to full health.

## Soul Urn

The Soul Urn begins its first descent at 10:00 and becomes available after
12.5 seconds. It respawns on five-minute clock intervals and alternates between
the Yellow and Green side lanes, beginning in Yellow. It must be carried to the
deposit point near the opposite side lane.

While carrying it, the courier gains +2 m/s Move Speed (capped at 15 m/s), +1
Stamina, +10% Dash Distance, +25% Stamina Regen, and 100% Slow Resistance. A
trailing-team courier can also receive conditional Bullet, Spirit, and Debuff
Resistance and Sprint Speed bonuses based on the team's Soul deficit.

Depositing it releases Soul Orbs and grants four random permanent buffs.
Opponents can deny the released orbs, while teammates can confirm them to share
the bounty. The September 29 update renames Golden Statues to **Buff
Containers** and adds Bullet Resist, Spirit Resist, Ability Range, and Move
Speed categories. Client 6722 records those values in three match-time tiers;
Ability Range's Tier 1 record also contains a radius modifier, while Tiers 2
and 3 do not. Raw values and relative loot weights are in
`data/map-timings.yaml`; their selection/normalization semantics remain
unresolved, so do not treat them as unconditional independent drop odds.

## Sinner's Sacrifice timing

The September 29 wiki transcription reports the update note that the Sinner
bonus timing is now variable. Client 6722 adds `MiniGameFastChance: 0.4` and
`MiniGameFastSpeed: 0.04191`, but those configuration fields do not specify the
new timing distribution or a changed Souls reward. The older fixed timing
interpretation is retained only as a pre-update reference in
`npcs/sinners-sacrifice/sinners-sacrifice.yaml`. The October 1 Sinner article
reports **15 machines at 11 sites**, including four hybrid sites. Its clear
rule requires all machines and member Haunts to be destroyed, but not nearby
crates or Buff Containers. See the [composition guide](haunt-camps-and-sinner-sites.md)
for the four patterns and named machine groups; exact per-site families remain
unassigned, and the rule is wiki-sourced rather than independently runtime-tested.

## New Breakables and The Broker

Client 6722 configures **Tough Crates** for one heavy-melee hit, with a 180
second initial spawn/respawn and a guaranteed configured `big_gold_pickup` drop.
The pickup record exposes `GoldAmount: 46` and `GoldPerMinuteAmount: 4`; those
fields are preserved separately, without an inferred reward formula. **Healing
Snacks** have a configured 180 second spawn delay/respawn, 4 second regen
duration, and a 10% maximum-health regen field. The final heal amount and live
location availability remain unverified. These object types are distinct from
ordinary crates and Buff Containers.

Clients 6722 and 6731 configure the Broker shop as enabled, with a one-item
stock, an 1800 second base opening time with 120 seconds of variance, and a 900
second restock interval; the bonus and penalty variance fields are 15%.
Configuration alone does not establish live shop availability by mode/date,
prices, or exact opening/exit conditions. October 2 and later changes are
outside this snapshot. The September 29 wiki transcription reports the update
note that Street Brawl grants one corrupted item after the Round 5 draft. Client 6726
adds `CorruptedUpgrades` fields to 95 item records plus 11 penalty definitions;
see `data/corrupted-items.yaml`. Client 6726 also sets Street Brawl's buy-time
vector to `[50, 50, 50, 50, 65]` seconds, with the configured corrupted-item
round at Round 5. The Round 5 buy time was 50 seconds in client 6722. Item
variant data, penalty rolls, shop availability, and mode eligibility remain
separate questions.

## Powerups

Two temporary powerups spawn at five minutes and on every five-minute clock
interval afterward. Claiming one requires a heavy melee attack. Casting, gun,
movement, and survival variants provide temporary bonuses for 160 seconds, with
their strength scaling later into the match.

## Unstable Rift Timing Conflict

The pinned map and mechanics summaries do not agree on the precise delay between
an Unstable Rift's visual spawn, announcement, and contest opening. The baseline
therefore records the first spawn window and recurrence as provisional but does
not expose a trusted contest-start formula. See [known limitations](../../LIMITATIONS.md#unresolved-source-conflicts).

Client 6694 independently verifies the Unstable Rift comeback-resistance
maximums: 10% at match start, +1 percentage point per minute, capped at 40% by
30 minutes. The same data revision no longer contains the previous fixed Rift
comeback-bounty field. This does not resolve the Rift's disputed visual/contest
timing or the complete comeback-reward formula.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[The Cursed Apple](https://deadlock.wiki/The_Cursed_Apple?oldid=125757),
[Mechanics](https://deadlock.wiki/Mechanics?oldid=110139),
[Neutral](https://deadlock.wiki/Neutral?oldid=125766), and
[Souls](https://deadlock.wiki/Souls?oldid=157718), the September 29 Valve
announcement and update transcription, and client data through 6731. No raw
September 29 or September 30 changelog is present in the pinned archive. The
September 30 wiki update is labeled UI/settings-only; client-data differences
are separately classified in the chronological review.
