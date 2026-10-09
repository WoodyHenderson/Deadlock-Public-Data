---
id: general.map.districts-and-landmarks
title: Off-Lane Districts and Landmarks
domain: general
topics: [map, districts, landmarks, Theater, Chinatown, Haunted-Lot, Plaza]
aliases: [City Never Sleeps map, Bell Tower, Sunken Plaza, basketball court, theater roof]
summary: The four named off-lane districts, their nearby lanes and landmarks, with source-date and runtime caveats.
snapshot_id: deadlock-data-pre-rat-king-2026-10-01
current_as_of: "2026-10-06"
evidence_status: needs_primary_verification
sources:
  - valve.city-never-sleeps.2026-09-29
  - github.deadlock-data.gameplay.9830c72afd4e
  - wiki.map.181766
  - wiki.sinners-sacrifice.181842
---

# Off-Lane Districts and Landmarks

The September 29 **City Never Sleeps** announcement describes a major map
update. Client 6722 adds district and building localization labels while
retaining the three-lane map. The later Cursed Apple article (revision 181766,
checked October 6) describes four off-lane districts and their geography. That
wiki description is later interpretation, not a dated September 29 map capture;
client labels establish names, not exact placement, paths, or live mechanics.

| District | Side and nearby lanes (later wiki description) | Named features |
| --- | --- | --- |
| Theater | Archmother side; between Greenwich/Park (Green) and Broadway (Blue) | Theater interior and a broken glass roof entrance |
| Chinatown | Hidden King side; between Greenwich/Park (Green) and Broadway (Blue) | Bell Tower; later wiki article describes rope access and concentrated Souls |
| Haunted Lot | Hidden King side; between York (Yellow) and Broadway (Blue) | Basketball court |
| Plaza | Archmother side; between York (Yellow) and Broadway (Blue) | Sunken Plaza and the stone-sculpture/fog area |

The three primary lanes remain York/Yellow, Broadway/Blue, and Greenwich/Park/Green.
These four districts are **not additional lanes**. The minimap flips with the
player's team orientation; do not treat a fixed left/right view as universal.
No routes, pathfinding edges, travel-time claims, or crate placements are
recorded here.

For existing camp locations, family-tier descriptions, Sinner site counts and
composition patterns, use [Haunt Camp Compositions and Sinner Sites](haunt-camps-and-sinner-sites.md).
It distinguishes known map markers from missing per-location family/unit assignments.

## Landmark behavior and evidence limits

- Valve's update description says the Sunken Plaza fog blocks outside sound and
  drains stamina. The later map article additionally claims that the fog blocks
  vision through the layer and prevents stamina regeneration. The latter details
  are wiki interpretation and have not been independently runtime-tested.
- The later map article says Souls collected in the Bell Tower ring its bell and
  alert players across the map, and reports three Sinner's Sacrifice machines
  there. Preserve those as later wiki claims, not client placement records.
  The separate October 1 Sinner article supplies 15 machines across 11 sites;
  see the composition guide for the count and provenance.
- Valve identifies the Theater and Haunted Lot basketball court as update
  features. Entrances, roof access, and exact court composition come from the
  later map article, not the announcement.
- Steam Vents are described in the update notes as granting invisibility and
  regeneration while standing on them. Exact regeneration, targetability edge
  cases, and placements are not established here.

## Source notes

The client `MapDistrictLocalization` field in client 6722 contains the district
and building labels. Team-side relationships, lane adjacency, landmark
placements, and behavior summaries above are separately attributed to Valve's
announcement or the later wiki revisions. The wiki map article was marked
under construction when checked. The October 6 coordinate snapshot is a
separate map layer and is not used to claim exact September 29 placements.
