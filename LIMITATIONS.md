# Data limitations

This is a pinned reference snapshot, not an exhaustive or independently
runtime-tested description of Deadlock.

## Intentionally excluded rules

This edition publishes only wiki/API-backed source material. Seven specialized
interaction tables with private-only or mixed private/public evidence were
omitted: Spirit interactions, hero interactions, melee interactions, ability
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
