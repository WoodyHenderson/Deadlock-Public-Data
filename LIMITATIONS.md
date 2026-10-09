# Data limitations

This is a pinned reference snapshot, not an exhaustive or independently
runtime-tested description of Deadlock.

## Separate map snapshot

[Map point markers and area counts](map/README.md) come from an October 6, 2026
private-source snapshot. They are potential locations, not live loot availability,
a September 29 client-verified map, or an update to the September 3 gameplay
baseline. Permission to redistribute this derived layer is non-commercial only;
source identity stays private by request. Camp and breakable mechanics still
require independent verification.

## Intentionally excluded rules

The gameplay baseline and scoped updates publish public source-backed material,
including pinned Wiki/API/client data. Seven specialized interaction tables with
private-only or mixed private/public evidence were omitted: Spirit interactions,
hero interactions, melee interactions, ability
modifier interactions, ability duration interactions, Reactive Barrier trigger
coverage, and Indomitable trigger coverage.

A private-only item-selling guide and the `spirit_scaling` and
`item_transactions` sections of the general rules table were also omitted.
Individual item and ability source records remain available, including their
explicit coefficients, descriptions, properties, and numeric upgrade deltas.
These omissions do not establish that the excluded claims are false; they mean
this edition does not publish them as verified public-source rules.

Component relationships do not by themselves establish checkout pricing,
inventory replacement, or inherited-stat behavior. No full runtime simulator or
calculation engine is shipped. Do not invent runtime meanings from field names.

## Unresolved source conflicts

Existing evidence flags are preserved:

- `review.slide-speed-threshold`: the exact flat-ground slide-speed threshold is
  disputed. See [movement](general/movement/universal-movement.md) and
  [general rules](data/universal-rules.yaml).
- `review.unstable-rift-contest-delay`: the contest-start delay lacks a trusted
  formula. See [map timings](data/map-timings.yaml) and
  [timed events](general/map/timed-events-and-neutral-objectives.md).

These identifiers name unresolved issues documented here, not an external or
missing review database. Other field-level uncertainty labels must also be
preserved by consumers.

## City Never Sleeps boundary

The scoped September 29–October 1 refresh stops at client 6731, before the
October 2 Rat King release. It does not advance hero/item rosters or the root
September 3 baseline. Client fields are configuration, official announcements
are patch intent, and later wiki geography is labeled interpretation.

Available: 40 named camp markers with difficulty tiers and 15 Sinner machine
markers in the existing coordinate layer. The [composition guide](general/map/haunt-camps-and-sinner-sites.md)
adds pinned October 1 wiki family tiers, ordinary-camp patterns, 15 machines at
11 sites, four Sinner configurations, and the hybrid clear rule. Machine-name
groups are derived from the map, not independent runtime camp membership.

The [map-interaction review](general/map/map-interactions-and-open-questions.md)
now adds source-dated Haunt attacks, Steam Vent concealment/reveal rules, 10%
max-health snack healing over four seconds, explicit crate reward models,
permanent-buff selection descriptions, and the Sinner GoldReward-times-two
conversion. October 1 wiki bindings support breakable categories 1–3. Canonical
neutral tier and Mid-Boss combat fields are cross-checked to client 6731; absent
weakpoint/melee-resistance fields are not treated as proof of runtime removal.

Still unresolved: exact family/unit assignments at each named Haunt/hybrid camp;
the six medium combinations; engine vent scaling; Sinner cycle lengths,
final-hit handling and exact payout rounding; descriptor 4 and the intermediate
tunnel schedule discrepancy; exact buff-selection/stacking; and Broker prices,
mode gating and eligibility implementation. The later snack timing's effective
date is not established. A fresh authorized marker export or verified before/after
coordinates is still needed for the Theater/basketball-area placement re-audit.
The corrupted-item sidecar is not a list of currently purchasable variants.
That pre-release research does not incorporate the October 2 Broker disablement;
the separate release import below updates its configured state and dated mode evidence.

The separate October 6 coordinate snapshot is unchanged. It is not used to
assert exact September 29 placements. No raw September 29/30 changelog was
available in the pinned archive; the [pre-release review](patches/2026-09-29-city-never-sleeps-pre-rat-king-review.md)
is a curated summary, not a fabricated raw patch file.

## Rat King release boundary

[Rat King](heroes/rat-king/rat-king.md) is pinned to October 2/client 6737.
The official announcement establishes public release; the earlier selectable
flag did not. His client-6731 comparison is incomplete pre-release data, never
launch values. The other 38 heroes retain their previous records.

The October 3 Construction-marked wiki article describes tunnel access via
crouch, no entry during combat, and Spellbreaker not proccing on Royal Pestments
barrier damage. These are separately dated wiki descriptions, not independent
launch runtime tests. Tunnel vents are not equated with Steam Vents.

The Broker enabled convar becomes false in client 6737. Standard/ranked access
is reported unavailable by the later wiki update transcription, not established
by the convar alone. Street Brawl eligibility remains unresolved at this cutoff;
October 4 removal and October 5 balance changes are separate, unapplied updates.
Healing-ping range remains a client-described prompt condition in source units.
Supporting rat NPC fields establish neither neutral-camp placement nor runtime
association with Rat King's summoned rats. No root-baseline or geometry advance
and no fabricated raw October 2 changelog are included.

## Burst timing boundary

[Baseline burst profiles](general/combat/burst-weapons.md) reproduce the versioned
API's average rates. For the current working model, `cycle_time` is assumed to
represent the last-shot-to-next-burst gap. That interpretation is not expressly
confirmed by the API or Wiki and must not be treated as an exact runtime fact.
The documented fixed-gap Fire Rate behavior, partial-burst handling, and
per-bullet proc default are review observations that still need a pinned public
source or reproducible runtime capture. Fixed-gap examples are conditional
calculations, not source-verified gameplay formulas; see [burst timing data](data/burst-weapons.yaml).

## Source text defects and history

Apollo's Itani Lo Sahn tier-three tooltip contains an upstream unresolved
placeholder. Its raw text and warning are preserved in the
[Apollo record](heroes/apollo/apollo.md); do not use the placeholder as a value.

Historical patch files remain byte-for-byte copies of the pinned wiki-data
archive. Same-date file suffixes and Hero Lab variants are separate entries;
filename order is not proof of publication order. Patch dates are not assumed
to be game client IDs. The archive cannot establish a complete historical state,
and is excluded from normal current-snapshot lookup.
