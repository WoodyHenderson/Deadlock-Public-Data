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
  - map events
summary: Neutral camps, recurring map events, their initial availability, and their general rewards.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_conflict
sources:
  - wiki.the-cursed-apple.125757
  - wiki.mechanics.110139
  - wiki.neutral.125766
  - wiki.souls.124122
---

# Timed Events and Neutral Objectives

The map adds resources and objectives as match time advances. Exact canonical
times are stored in `data/map-timings.yaml`.

## Baseline Schedule

| Time | Event |
| --- | --- |
| 0:00 | Mid-Boss is present in the central underground area. |
| 2:00 | Small neutral camps spawn. |
| 3:00 | Base Soul Wells activate; regular crates and Tier 1 Golden Statues spawn. |
| 5:00 | Medium neutral camps and temporary powerups spawn. |
| 8:00 | Large neutral camps and Sinner's Sacrifice locations spawn. |
| 10:00 | Soul Urn cycle begins; Tier 2 Golden Statues and central breakables spawn. |
| about 11:00 | First Unstable Rift appears, subject to a random timing window and contest setup. |
| 12:00 | Lane Guardians reach their minimum timed damage resistance. |
| 18:00 | Walkers reach their minimum timed damage resistance. |
| 20:00 | Trooper wave interval changes from 30 seconds to 25 seconds. |
| 30:00 | Golden Statues upgrade to Tier 3. |
| 35:00 | Trooper wave interval changes to 20 seconds and Troopers gain 50% maximum health. |

## Neutral Camps

Neutral units belong to neither team and attack when provoked. A neutral's Soul
bounty is shared equally among allied players who damaged it, and the reward is
Unsecured Souls. Neutrals do not release Soul Orbs.

| Camp | First spawn | Respawn after full clear | Minimap mark |
| --- | --- | --- | --- |
| Small | 2:00 | 1:25 | Triangle with no line |
| Medium | 5:00 | 4:50 | Triangle with one line |
| Large | 8:00 | 5:35 | Triangle with two lines |

The respawn timer starts when the last unit in the camp is killed. Neutral
health increases by 2.1% per minute and damage by 0.5% per minute. Larger
neutrals have higher base bounties. Large neutrals take 20% less melee damage,
but the wiki notes that this behavior conflicts with the wording of the patch
that introduced it and should receive primary verification.

## Mid-Boss and Rejuvenator

The Mid-Boss is a durable central neutral with a continuously regenerating
shield. It generally requires coordinated damage from multiple heroes. Its
initial respawn delay is seven minutes after defeat, then six minutes after the
next defeat, and five minutes after subsequent defeats.

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

Depositing it releases Soul Orbs and grants four random permanent Golden Statue
buffs. Opponents can deny the released orbs, while teammates can confirm them to
share the bounty. Exact carrying bonuses and Golden Statue buff tiers are
canonical in `objectives/soul-urn/soul-urn.yaml`.

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

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[The Cursed Apple](https://deadlock.wiki/The_Cursed_Apple?oldid=125757),
[Mechanics](https://deadlock.wiki/Mechanics?oldid=110139),
[Neutral](https://deadlock.wiki/Neutral?oldid=125766), and
[Souls](https://deadlock.wiki/Souls?oldid=124122).
