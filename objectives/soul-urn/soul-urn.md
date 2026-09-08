---
id: objective.soul-urn
title: Soul Urn
domain: objectives
topics:
  - Soul Urn
  - Spirit Urn
  - Golden Statue buffs
  - movement
  - objectives
aliases:
  - Spirit Urn
  - Soul Jar
  - Spirit Jar
  - Idol
summary: Soul Urn carrying bonuses, delivery rewards, timing, and permanent Golden Statue buffs.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - wiki.soul-urn.114949
---

# Soul Urn

The Soul Urn first spawns at 10:00 and respawns at five-minute intervals. It
alternates between the Yellow and Green side lanes, with the first spawn in
Yellow. It descends for 12.5 seconds before it can be picked up with a light or
heavy melee attack.

## Carrying Bonuses

While carrying the Urn, the courier receives:

- +2 m/s Move Speed, capped at 15 m/s maximum;
- +1 Stamina;
- +10% Dash Distance;
- +25% Stamina Regen; and
- 100% Slow Resistance.

The courier cannot use Ziplines or Teleporters. If the courier is on the
trailing team, conditional bonuses can provide up to +35% Bullet Resistance,
Spirit Resistance, and Debuff Resistance, plus +5 m/s Sprint Speed. These
conditional bonuses scale with the team's Soul deficit, up to a 15% deficit.

## Delivery Rewards

Delivering the Urn grants the courier Souls and four random permanent buffs.
The Soul reward is released as Soul Orbs and can be denied. If the orbs are not
denied, the courier receives them; an ally who confirms an orb shares its value
with the courier.

The four permanent buffs are drawn pseudo-randomly from the following Golden
Statue buff table. Health has twice the normal selection weight; the distribution
also considers permanent buffs received from other sources.

| Buff | Level 1 (0 min) | Level 2 (10 min) | Level 3 (30 min) |
|---|---:|---:|---:|
| Fire Rate | +1.5% | +2% | +2.5% |
| Max Ammo | +3% | +5% | +7% |
| Cooldown Reduction | +0.5% | +0.75% | +1% |
| Weapon Damage | +3% | +4% | +6% |
| Max Health | +15 | +20 | +30 |
| Spirit Power | +2 | +3 | +4 |

Delivery grants four selections; it does not guarantee four different buff
types.

## Evidence and Source

This record is adapted from the pinned Deadlock Wiki Soul Urn revision and its
Permanent Buffs table. The canonical structured values are in the adjacent
`soul-urn.yaml` file. The Soul Urn's base bounty and time growth remain in
`data/economy.yaml`.
