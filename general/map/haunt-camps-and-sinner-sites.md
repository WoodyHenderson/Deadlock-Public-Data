---
id: general.map.haunt-camps-and-sinner-sites
title: Haunt Camp Compositions and Sinner Sites
domain: general
topics: [Haunts, camp compositions, Sinners Sacrifice, families, camp tiers, map]
aliases: [jungle camp types, neutral camp composition, hybrid camps, Sinner locations]
summary: Pinned wiki camp-composition patterns, nine Haunt families, and the existing map's camp tiers and Sinner machine groups, with per-location gaps distinguished.
snapshot_id: wiki-camps-pre-rat-king-with-dated-later-comparison
current_as_of: "2026-10-08"
evidence_status: source_verified_wiki_with_per_location_gaps
sources:
  - wiki.haunt.177431
  - wiki.haunt.181836
  - wiki.sinners-sacrifice.177553
  - wiki.sinners-sacrifice.181842
  - private.map-coordinates.2026-10-06
---

# Haunt Camp Compositions and Sinner Sites

**The map locations are available.** The existing [camp markers](../../map/coordinates/camps.yaml)
contain **40 named camps: 4 small, 25 medium, 11 large**, with position, elevation,
and area. The [Sinner markers](../../map/coordinates/sinners_sacrifice.yaml)
contain **15 machines**. Those are source-backed October 6 placements, not a
missing-data problem. Using them for September 29 retains the documented
[unchanged-placement assumption](../../map/README.md); it is not independent
launch-day verification or a guarantee of live availability.

[Structured compositions](../../data/haunt-camp-compositions.yaml) separate those
placements from the wiki's **October 1, pre-Rat King** composition descriptions.
Later October 6 article differences are shown separately, not silently backdated.
No values are taken from unpinned, live-transcluded NPC templates.

## Ordinary Haunt camps

| Camp tier | October 1 wiki composition | Remaining location-specific detail |
| --- | --- | --- |
| Small / I | Three small Haunts | Family at each named marker is not identified by these sources. |
| Medium / II | Six different combinations of small and medium Haunts | The article does not enumerate the six combinations or map them to named camps. |
| Large / III | At least one large Haunt; some camps also have small/medium Haunts. The article reports six camps of three large Haunts. | No named-location roster is supplied. This dated wiki claim is not a new map-marker count. |

The **October 6** Haunt article instead describes large camps as **three large**
or **one large plus two medium** Haunts. It does not establish whether the
wording changed because of a correction, simplification, or gameplay change.
Do not overwrite the October 1 description or apply an arbitrary alternative to
a named camp.

### Families are not camp locations

| Family | Tiers reported October 1 | October 6 comparison |
| --- | --- | --- |
| Barrel Mimic | II, III | Same |
| Past Dues | I, II | Same |
| Festival Spirit | II, III | Same |
| Slum Shroom (Shrooms) | II, III | Same |
| Crabbage Pot | I, II | Adds III |
| Stage Hand | I, II, III | Lists only II, III |
| Specimen | I, II | Same |
| Gutter Ghoul | I, II, III | Same |
| Underhand | I, II, III | Same |

These are dated **wiki family-tier descriptions**, not a placed-unit inventory.
For example, the source name “Theater Stage 1” does not by itself establish that
its members are Stage Hands, nor does “Basketball” establish a family or count.
The existing camp record still gives each location's difficulty tier.

## Sinner site compositions

The October 1 Sinner article explicitly gives **15 machines at 11 sites**:

| Sites | Machines per site | Haunts per site |
| ---: | ---: | --- |
| 6 | 1 | None |
| 2 | 1 | 2 medium Haunts |
| 2 | 2 | 1 medium Haunt |
| 1 | 3 | None |

This yields **four hybrid sites with six companion medium Haunts**. Those are
unit counts inside Sinner sites, not six additional ordinary camp markers.

**Wiki-described clear rule:** destroy all machines and kill all member Haunts
before the site's respawn timer starts. Nearby ordinary crates and Buff
Containers do **not** need to be destroyed. This is a pinned wiki rule, not an
independent runtime test. The rule is no longer simply “unknown.”

### Named machine groups already present in the map

Grouping the existing markers by equal source name and area gives the following
11 groups. This is a **derived source-label grouping**, not proof of runtime
membership or the family/count of companion Haunts.

| Source location name | Area | Machine markers |
| --- | --- | ---: |
| Chinatown Bell 1 | Bell Tower | 3 |
| Slums Garage Up | Haunted Lot | 2 |
| Theater Balcony | Theater | 2 |
| Drug Store | Times Square | 1 |
| Hotel 1 | Times Square | 1 |
| Park Library | Central Park | 1 |
| York Radio | Stock Exchange | 1 |
| Dock Authority | Docks (`docks-3b`) | 1 |
| Park Club | Central Park | 1 |
| Plaza Pit 1 | Sunken Plaza | 1 |
| Plaza Pit 2 | Sunken Plaza | 1 |

The October 6 Sinner article explicitly places three machines atop Bell Tower
and describes two Sinner sites alongside two Haunt camps in Sunken Plaza. That
supports the landmark context, but does not explicitly assign a particular
Haunt family or unit count to either Plaza marker. Do not use proximity alone
to attach ordinary camp markers to a Sinner group.

## What is still missing

A **complete per-location family-and-unit roster** for all 40 ordinary camps
and the four hybrid sites was not found in the inspected wiki articles. The
family catalogue, small-camp count, Sinner configurations and clear rule are
available; the exact six medium combinations and their named-location mapping
are not. Unknown fields remain explicit rather than inventing a full atlas.
Older map-page totals (12 machines/10 sites, and inconsistent ordinary-camp
counts) do not override the specific Sinner article or the coordinate inventory.

## Sources

Adapted from Deadlock Wiki contributors' [Haunt revision 177431](https://deadlock.wiki/Haunt?oldid=177431)
and [Sinner's Sacrifice revision 177553](https://deadlock.wiki/Sinner%27s_Sacrifice?oldid=177553),
both October 1. Later comparisons use [Haunt revision 181836](https://deadlock.wiki/Haunt?oldid=181836)
and [Sinner revision 181842](https://deadlock.wiki/Sinner%27s_Sacrifice?oldid=181842),
both October 6. Revisions and wikitext hashes for the newly researched pages are
in the [source registry](../../sources/source-registry.yaml). See
[attribution and reuse](../../ATTRIBUTION.md) for wiki and anonymous map-layer
licensing boundaries; no images, source code or raw map exports are republished.
