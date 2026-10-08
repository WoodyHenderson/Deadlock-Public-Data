---
id: general.map.minimap-and-visibility
title: Minimap and Visibility
domain: general
topics:
  - minimap
  - visibility
  - line-of-sight
  - pings
aliases:
  - map vision
  - enemy reveal
  - missing ping
  - chat cooldown
  - text chat cooldown
  - ping cooldown
  - ping rate limit
summary: What the minimap displays and the general actions that reveal a hero to the enemy team.
snapshot_id: deadlock-wiki-2026-09-09
current_as_of: "2026-09-09"
evidence_status: needs_primary_verification
sources:
  - wiki.minimap.89774
  - wiki.the-cursed-apple.125757
  - wiki.mechanics.110139
  - wiki.update.2026-09-09.145819
---

# Minimap and Visibility

The minimap is a top-down summary of the match. It displays teammates, lane
Troopers, structures, shops, neutral camps, timed buffs and objectives, and
enemy heroes when reveal conditions are met. Lane coloring and Zipline progress
also communicate current territory.

## General Enemy Reveal Rules

A hero is generally revealed to the enemy team when any of these conditions
apply:

- the hero is in an enemy hero's unobstructed line of sight within approximately
  50 to 60 meters;
- the hero fires their weapon at enemy Troopers;
- the hero fires their weapon at enemy defensive structures, even if the
  structure cannot see or return fire;
- an enemy defensive structure targets or attacks the hero;
- the hero is extremely close to an enemy hero without a vision blocker.

After the revealing action ends, the hero remains on the minimap for
approximately two seconds.

## Actions That Do Not Normally Reveal

The pinned minimap revision says the following do not reveal a hero by
themselves:

- standing near enemy Troopers that are not targeting the hero;
- using abilities or active items against enemy Troopers or heroes;
- being targeted by an enemy hero beyond the normal line-of-sight reveal range;
- standing near enemy Troopers while those Troopers are still riding a Zipline.

Weapon attacks and ability use are therefore not interchangeable for minimap
reveal. Specific hero effects can override these general rules, but those
interactions are outside this baseline.

## Vision Blockers and Leaning

Line-of-sight reveal requires a clear line between the centers of the heroes.
Map geometry can block it. Leaning around a corner exposes only part of the hero
and, according to the pinned wiki revision, does not cause the two heroes to
reveal each other through the normal line-of-sight rule.

## Team Communication

Players can mark that an enemy is missing by opening the scoreboard and
middle-clicking the enemy portrait. Lane and location pings communicate movement
and areas requiring attention.

### Chat and ping rate limit (September 9, 2026)

The September 9 update note reports that sending multiple text messages or pings
in a row disables both text chat and pings for **10 seconds**. The note says this
was added after an exploit that could crash the game server. It does not specify
the exact message-count/window threshold or other timer behavior. This is a dated
update-note report, not an independently verified runtime test.

## Evidence Limitation

The Minimap source page was marked as a stub, and several distances are given as
approximations. Treat the categories above as useful retrieval knowledge, but do
not use the approximate distances as calculation inputs until they have primary
verification.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Minimap](https://deadlock.wiki/Minimap?oldid=89774),
[The Cursed Apple](https://deadlock.wiki/The_Cursed_Apple?oldid=125757), and
[Mechanics](https://deadlock.wiki/Mechanics?oldid=110139).