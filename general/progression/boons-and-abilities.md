---
id: general.progression.boons-and-abilities
title: Boons and Ability Progression
domain: general
topics:
  - Boons
  - leveling
  - abilities
  - ability-points
aliases:
  - levels
  - power increases
  - ability unlocks
summary: How gathered Souls grant Boons, ability unlocks, and ability-upgrade points.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - wiki.boon.98787
  - wiki.souls.124122
---

# Boons and Ability Progression

Level progression is based on total Souls gathered, not current unspent Souls.
Every hero uses the same Soul thresholds, although the base-stat gains from each
Boon vary by hero.

## Reward Pattern

Players begin at level 0 with 600 Souls and one ability unlock. After that:

- every level grants a Boon;
- levels 2, 4, and 7 grant the remaining ability unlocks;
- every other level through level 35 grants one ability point;
- the first three unlocks can only select non-ultimate abilities;
- the ultimate becomes unlockable with the fourth unlock at 3,800 Souls.

The complete threshold table is stored in `data/progression.yaml`.

## Boons

A Boon is the level's base-stat increase. Boons improve base bullet damage,
light and heavy melee damage, health, and Spirit Power. The amount gained is
hero-specific, so this general baseline defines the progression system but does
not contain hero-specific Boon profiles.

The maximum reward-bearing Boon level is 35. After that point, the HUD continues
to display another level for each additional 2,000 Souls, but no further Boon or
ability-point reward is granted.

## Ability Unlocks and Points

Every hero has four abilities. An ability unlock makes one selected ability
available. Ability points then improve unlocked abilities.

Each ability has three upgrade tiers costing 1, 2, and 5 points. Points may be
saved and spent in any order allowed by the current unlock state; players do not
have to finish one ability before upgrading another.

## Unsecured Souls

Unsecured Souls count toward level thresholds. If those Souls are later dropped
on death, an already unlocked level and its rewards remain, but progress toward
the next level is reduced by the amount lost.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Boon](https://deadlock.wiki/Boon?oldid=98787) and
[Souls](https://deadlock.wiki/Souls?oldid=124122).
