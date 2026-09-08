---
id: general.map.objectives-and-structures
title: Objectives and Structures
domain: general
topics:
  - objectives
  - structures
  - backdoor-protection
  - victory
aliases:
  - Guardian
  - Walker
  - Base Guardian
  - Shrine
  - Patron
summary: The ordered lane and base objectives, their unlock effects, and structure protection rules.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - wiki.structures.122019
  - wiki.the-cursed-apple.125757
  - wiki.backdoor-protection.78476
  - wiki.extra-slots.60786
  - wiki.souls.124122
---

# Objectives and Structures

Structures are immobile team objectives. Destroying enemy structures opens the
route to the Patron, awards team Souls, and can unlock additional benefits.

## Objective Order

| Order | Structure | General role | Destruction effect |
| --- | --- | --- | --- |
| 1 | Lane Guardian | First defense in each lane | Opens access toward the Walker. |
| 2 | Walker | Second defense in each lane | Unlocks one Extra Slot for the attacking team. |
| 3 | Base Guardian pair | Final lane defense outside the base | Defeating both in a lane significantly speeds that lane's allied Zipline. |
| 4 | Shrines | Two base structures | Both must be destroyed to expose the Patron. |
| 5 | Patron | Final objective | Defeating both phases wins the match. |

Shrines cannot be damaged until a pair of Base Guardians has been destroyed.
Destroying one Shrine upgrades allied Troopers in that Shrine's corresponding
side lane into Super Troopers. Destroying both Shrines additionally upgrades the
Blue-lane Troopers, so both Shrines are required for Super Troopers in all three
lanes. The Patron cannot be damaged in its normal protected state and becomes
exposed after both Shrines fall.

At 50% health in its first phase, the Patron becomes invulnerable, transforms,
and moves into the team's pit for its weakened phase. If the weakened Patron is
not under attack, it regenerates health. Its first-phase defeat also applies the
defending team's one-time Last Stand respawn-time reduction.

## Structure Attacks

- Lane Guardians use a laser, melee attack, and an area slam.
- Walkers use a laser, projectile salvo, and slam.
- Base Guardians defend in pairs.
- Shrines and the Patron can apply a Curse-style defensive attack.

Exact health, attacks, resistance curves, scaling, and conditional protection
are stored in the canonical records under `npcs/` for the Lane
Guardian, Walker, Base Guardian, Shrine, and Patron. Calculations must use those
records rather than values copied from this overview.

## Objective Soul Bounties

When a structure is destroyed, 30% of its bounty is split among nearby allied
heroes and the remaining 70% is distributed across the whole team, including
those nearby heroes. Current baseline bounties are stored in
`data/economy.yaml`.

The Patron itself has no Soul bounty; destroying its weakened phase ends the
match.

## Extra Slots

Teams begin with three locked Extra Slots. They unlock in order as the team
destroys enemy Walkers:

| Enemy Walkers destroyed | Extra Slots unlocked |
| --- | --- |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

## Backdoor Protection

Every standard structure except a Lane Guardian receives Backdoor Protection
when no enemy Troopers are nearby. Pushing a Trooper wave to the structure
removes the protection. For base structures, pushing any allied lane Zipline to
the enemy base removes protection. Once the enabling lane pressure is gone,
there is a 14-second buffer before protection returns.

Protected Walkers, Base Guardians, Shrines, and Patrons have 65% damage
resistance and active health regeneration. That regeneration only restores the
health lost while protection was active. The Patron separately regenerates up
to full health out of combat.

Base Guardians and Shrines also have proximity-based Bullet Resistance. Base
Guardians start at 40% and Shrines at 60%; each nearby enemy hero reduces that
resistance by 20 percentage points, to a minimum of 0%.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Structures](https://deadlock.wiki/Structures?oldid=122019),
[The Cursed Apple](https://deadlock.wiki/The_Cursed_Apple?oldid=125757),
[Backdoor Protection](https://deadlock.wiki/Backdoor_Protection?oldid=78476),
[Extra Slots](https://deadlock.wiki/Extra_Slots?oldid=60786), and
[Souls](https://deadlock.wiki/Souls?oldid=124122).
