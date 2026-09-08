---
id: general.rules.death-and-respawning
title: Death and Respawning
domain: general
topics:
  - death
  - respawn
  - death-timer
  - Rejuvenator
aliases:
  - revive
  - respawn timer
  - Last Stand
summary: What happens on death, how respawn time scales, and how Last Stand and Rejuvenator credits modify it.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - wiki.death.95455
  - wiki.souls.124122
---

# Death and Respawning

A hero dies when health reaches zero. Kill and assist Souls are awarded as
applicable, Unsecured Souls may drop, and the dead hero receives a respawn timer.
When that timer reaches zero, the hero returns in the team's Respawn Room.

While dead, players can spectate teammates, browse the shop, communicate, and
select allied objectives on the minimap to view their perspective.

## Base Respawn Time

Respawn time increases linearly between the source's listed control points:

| Match time | Respawn time |
| --- | --- |
| 5:00 | 8 seconds |
| 20:00 | 35 seconds |
| 30:00 | 70 seconds |
| 40:00 | 85 seconds |

The normal timer is capped at 90 seconds. Dying only to a non-player unit, with
no enemy-hero bounty or assist, adds ten seconds to that death's timer.

## Rich-Player Death Penalty

After ten minutes, a hero whose net worth is at least 15% above the killer
team's average can receive an additional respawn penalty. The pinned wiki gives
the range as six seconds at the low threshold around ten minutes, scaling up to
22 seconds for a 30% difference at 25 minutes.

## Last Stand

When attackers defeat the Patron's first phase, the defending team's heroes who
are already dead receive a one-time remaining-timer reduction:

- 30 seconds or more remaining: subtract 20 seconds;
- more than 10 but fewer than 30 seconds: set remaining time to 10 seconds;
- 10 seconds or less: no change.

This applies only at the phase transition. Later deaths use their normal timers.

## Rejuvenator Credits

The Mid-Boss Rejuvenator provides up to three team revive credits. When a hero
dies while a credit is available, that hero revives at the death location after
three seconds and a credit is consumed. The revived death does not pay ordinary
kill Souls, though effect-specific kill triggers may still treat it as a kill.

## Unsecured Souls on Death

An unsecured balance at or above `50 + 5 per match minute` drops as a Soul
Container that any player can claim with heavy melee. Smaller unsecured balances
are lost without a container. See `general/economy/souls-and-bounties.md` for the
full securing and drop rules.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Death](https://deadlock.wiki/Death?oldid=95455) and
[Souls](https://deadlock.wiki/Souls?oldid=124122).