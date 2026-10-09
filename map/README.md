---
id: map.coordinates.guide
title: Map Coordinates and Breakable Concentrations
domain: map
topics: [map, coordinates, camps, crates, tough-crates, buff-containers, jungle, points-of-interest]
aliases: [interactive map, crate locations, tough crate locations, jungle locations, map points]
summary: Lookup guide for a private-source map coordinate snapshot and calculated breakable counts by named area; not a live-spawn or route finder.
snapshot_id: private-map-2026-10-06
current_as_of: "2026-10-06"
evidence_status: derived
sources:
  - private.map-coordinates.2026-10-06
---

# Map coordinates and breakable concentrations

**This is a supplementary map snapshot, not a refresh of the September 3 hero/item/NPC baseline.** The project owner reports permission to use and publicly redistribute this derived coordinate layer **for non-commercial use only**, without identifying or attributing the private source. Identifying provenance and permission correspondence are kept privately by the project owner rather than in this repository. This permission does not establish a general license for the source's site code, imagery, raw exports or commercial uses. Coordinates reflect the extracted map as of **October 6, 2026**; there is no publicly pinned game client version for this layer. We follow the owner's explicit working assumption that map features not mentioned in the October 2 and 5 patches have remained in place since City Never Sleeps; this is not independent patch-time verification. Do not replace current combat/timing records with map data.

## Camp compositions and Sinner sites

The [composition guide](../general/map/haunt-camps-and-sinner-sites.md) and
[structured patterns](../data/haunt-camp-compositions.yaml) supplement this
coordinate inventory with pinned October 1 wiki evidence: three-small ordinary
camps, Haunt family tiers, and four Sinner configurations totaling 15 machines at
11 sites. The guide lists the 11 derived machine-name groups and explains the
hybrid clear rule. Exact family/unit assignments for every named camp are still
not supplied by the inspected sources; **the placements and difficulty tiers
are available**, not broadly unresolved. October 6 wiki differences are dated
separately, and the original coordinate snapshot is unchanged.

See [map interactions and the remaining placement audit](../general/map/map-interactions-and-open-questions.md)
for sourced object behavior and what evidence is still needed to update individual
Theater/basketball-area markers. The coordinate payload was validated, not
refreshed from a newer export in this pass.

## Find what you need

- [Breakable counts by named area](breakable-zones.yaml): best first read for “where are the most Tough Crates?” Counts are **potential map markers**, not currently available loot. `crates` means ordinary wooden crates; `tough_crates` require heavy melee; `statues` means Buff Containers (old name Golden Statues).
- [Named area boundaries](zones.yaml): source subarea polygons and label positions. The same name “Docks” appears in two source regions, kept separately as `docks-3a` and `docks-3b`. `parent` is the source label, not always a district. Bell Tower and Sunken Plaza are distinct, smaller zones; their marker counts are **excluded** from the parent Chinatown/Plaza row to prevent double counting.
- [Individual map markers](coordinates/README.md): one YAML-compatible JSON record per category, including [ordinary crates](coordinates/crates.yaml), [Tough Crates](coordinates/tough_crates.yaml), [Buff Containers](coordinates/statues.yaml), [Haunt camp markers](coordinates/camps.yaml), [Sinner machines](coordinates/sinners_sacrifice.yaml), [snacks](coordinates/snacks.yaml), [steam vents](coordinates/vents.yaml), [shops](coordinates/shops.yaml), and other objective/transit point categories. Read **only the requested category**, not all 983 markers. `item_crates` are a distinct source category and are not counted as ordinary or Tough Crates.

| Named area (source zone, exclusive of nested subareas) | Ordinary crates | Tough Crates | Buff Containers |
| --- | ---: | ---: | ---: |
| Times Square | 52 | **11** | 18 |
| Theater | 49 | **9** | 26 |
| Haunted Lot | 51 | **8** | 27 |
| Chinatown (excluding Bell Tower) | 39 | **6** | 20 |
| Central Park | 27 | **5** | 10 |
| Bell Tower (within Chinatown) | 7 | **4** | 5 |
| Sunken Plaza (within Plaza) | 6 | **4** | 5 |
| Plaza (excluding Sunken Plaza) | 36 | **4** | 17 |

These are **counts, not area-normalized densities**. Other zones and counts, including two separate Docks regions, are in the canonical [summary](breakable-zones.yaml). Source marker totals: **423 ordinary crates, 73 Tough Crates, 166 Buff Containers**, **40 Haunt camps** (4 small, 25 medium, 11 large), **15 individual Sinner machines** (not necessarily 15 sites), 36 healing snacks, and 46 steam vents. Some markers fall outside the source's named-area polygons: 4 ordinary crates, 2 Tough Crates and 1 Buff Container are explicitly `unassigned`, **not discarded**. The source's shop markers cover 6 lane + 2 secret shops, not the two base shops described in the general map guide. The source's 4 shrine markers are not a verified replacement for the baseline structure definitions. Marker coverage varies by category.

## Coordinate and interpretation contract

- `u` increases **right** and `v` increases **down** on the *source's unflipped map image*, both normalized 0–1. This is **not** the team-flipped in-game minimap, GPS latitude/longitude or world X/Y. `h_m` is the source's elevation in metres relative to its own map origin, **not** a floor number or traversable-distance estimate. A map position alone is not an accessible walking route.
- A marker ID such as `map.tough_crates.0001` is a **snapshot-local** stable reference to its source-array index, not a permanent game entity ID. `group` is the source's breakable spawn category number; consult `data/map-timings.yaml` for schedule research, not the geometry itself. Camp `tier`, `first_spawn_s`, `respawn_s` and `tether` are source fields, not validated against the client for this layer. Sinner records represent *machines*, whereas spawn/clear behavior may depend on a combined Haunt camp.
- Named-area membership is a **derived 2D polygon match**; the known nested landmarks Bell Tower and Sunken Plaza take precedence over parents. Other overlaps and points outside polygons are left unassigned rather than guessed. Vertical position is preserved on each marker. To find a floor-specific cluster, filter by `h_m` and verify the environment; do not assume every same-zone marker shares a floor.
- No map artwork, complete veil meshes, zipline paths or route graph are imported. Individual markers provide locations, **not** live availability, guaranteed rewards, optimal paths, visibility or local accessibility. For Haunt identity/behavior and crate/neutral bounty mechanics, consult canonical `npcs/`, `general/map/` and `data/` records with their **own patch contexts**.

## Reproduce/validate

The importer consumes authorized local JSON exports of point and district data, **not** a live website/API scraper. Upstream identity, access details, exports and site code are not checked into the repository; keep the private provenance with the project owner. Public distribution of this derived coordinate layer is authorized as reported by the project owner **only while non-commercial**; do not infer broader rights over the raw exports or source materials. Example with authorized local exports:

```sh
python3 scripts/map/sync_map_coordinates.py --map-input /path/to/map-points.json --zones-input /path/to/map-zones.json
python3 scripts/map/sync_map_coordinates.py --check
python3 -m unittest discover -s scripts/map -p 'test_*.py'
```

For a bounded lookup without loading hundreds of coordinates into an LLM context:

```sh
python3 scripts/map/query_map.py --summary --zone times-square-4
python3 scripts/map/query_map.py --category tough_crates --zone times-square-4 --limit 20
python3 scripts/map/query_map.py --category camps --zone theater-9
```

The query reports the full **matched count**, number **returned** and whether truncated; it does not report live availability or walking routes. Review changes to the source map, polygon labels and any future client patch *before* regenerating. The summary is calculated from pinned point arrays and the zone polygons; its deterministic counts are tested. Do not silently advance the global `README.md` baseline when refreshing this independent map layer.
