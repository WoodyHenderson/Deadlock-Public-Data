---
id: general.map.layout-and-traversal
title: Map Layout and Traversal
domain: general
topics:
  - map
  - lanes
  - base
  - jungle
  - traversal
aliases:
  - The Cursed Apple
  - Midtown
  - dl_midtown
  - jungle
summary: The standard map's three lanes, off-lane districts, bases, and traversal systems.
snapshot_id: deadlock-data-pre-rat-king-2026-10-01
current_as_of: "2026-10-06"
evidence_status: needs_primary_verification
sources:
  - wiki.the-cursed-apple.125757
  - wiki.mechanics.110139
  - wiki.movement.78724
  - valve.city-never-sleeps.2026-09-29
  - github.deadlock-data.gameplay.9830c72afd4e
  - wiki.map.181766
---

# Map Layout and Traversal

The standard Deadlock map is The Cursed Apple, internally named `dl_midtown`.
It depicts the game's version of Midtown and Lower Manhattan. The Archmother and
Hidden King teams occupy opposing bases.

## Lanes and Territory

Three lanes connect the teams' sides:

- York, shown as Yellow;
- Broadway, shown as Blue;
- Park, shown as Green and also called Greenwich.

Each lane has team-specific overhead Ziplines and a sequence of defensive
structures. Allied Troopers advancing down a lane extend the territory and
Zipline access available to their team. The Ziplines therefore provide a quick
visual indication of lane pressure as well as transportation.

## Bases and Respawn Rooms

The rear of each base contains a Respawn Room. Dead allied heroes return there.
The room contains the team's main Curiosity Shop and a Soul Well that activates
at three minutes.

Allied heroes in their Respawn Room recover 6% of maximum health plus 60 health
per second. Four room turrets target enemies who enter.

## Off-Lane Areas

The post-update map identifies four named off-lane districts—Theater,
Chinatown, Haunted Lot, and Plaza—without changing the three-lane model. See
[Off-Lane Districts and Landmarks](districts-and-landmarks.md) for the
source-dated location guide and its geography/runtime caveats.

Tunnels, alleys, buildings, and rooftops connect the lanes. The areas outside
the lanes are commonly called the jungle and contain neutral camps, now
player-facingly called Haunts. Ordinary crates, Tough Crates, and Buff
Containers are distinct breakables distributed throughout the map; potential
coordinate markers do not establish live availability. Buff Containers were
formerly called Golden Statues and can provide permanent stat bonuses.

Juke Rooms are marked dead-end spaces with a shadowed Cosmic Veil doorway. They
provide concealment and cornering opportunities, but have only one entrance.

## Long-Distance Traversal

- **Ziplines:** Team-specific transit lines run from each base above all three
  lanes. Their forward availability depends on allied lane progress.
- **Teleporters:** Four teleporters form two pairs that move players horizontally
  between distant map regions.
- **Ropes:** Vertical ropes provide access to upper floors and rooftops.
- **Jump Pads and fans:** Air currents launch heroes upward or across gaps.
- **Stairs, tunnels, and buildings:** These provide regular vertical and
  cross-lane routes.

## Shops

The map overview identifies ten shop locations:

- two team-specific shops in the Respawn Rooms;
- six team-specific lane shops, one on each team's side of each lane;
- two neutral secret shops.

This document records locations only. Item categories, costs, and effects are
outside the current general-mechanics scope.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[The Cursed Apple](https://deadlock.wiki/The_Cursed_Apple?oldid=125757),
[Mechanics](https://deadlock.wiki/Mechanics?oldid=110139), and
[Movement](https://deadlock.wiki/Movement?oldid=78724). District/building
labels come from client 6722; the side/lane layout is described in the later
[map article revision 181766](https://deadlock.wiki/The_Cursed_Apple?oldid=181766),
which was marked under construction when checked. See the linked district guide
for the date and runtime caveats. The Movement page was marked under
construction when originally curated.
