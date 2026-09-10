---
id: general.movement.hero-stamina-buckets
title: Hero Stamina Buckets
domain: general
topics: [heroes, movement, stamina, stamina buckets]
aliases: [character buckets, dash speed tiers, stamina usage]
summary: The three hero dash-speed tiers that determine ground and air dash duration.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: needs_primary_verification
sources:
  - wiki.data-hero-data.108817
  - wiki.movement.78724
  - wiki.stamina.unknown
---

# Hero Stamina Buckets

Deadlock's **stamina buckets** are dash-speed balance tiers, not groups based
on the number of stamina charges. A hero's bucket changes how quickly their
ground and air dashes complete. The dash distances remain 10 m on the ground and
8 m in the air; the duration differs by bucket.

## The three buckets

| Bucket | Reported dash-speed modifier (unverified) | Ground dash duration | Air dash duration | Meaning |
| --- | ---: | ---: | ---: | --- |
| 1 | +5% | 0.62 s | 0.43 s | Fastest, snappiest dash |
| 2 | -5% | 0.68 s | 0.47 s | Standard dash |
| 3 | -15% | 0.72 s | 0.51 s | Slowest dash |

The percentage labels above come from the user-supplied summary of the Stamina
reference and still need independent verification against a pinned revision.
The three duration pairs and the hero groupings below are derived from the local
hero records. Their association with the reported percentage labels is provisional;
do not infer a runtime speed formula from those labels. They do not describe
stamina regeneration or a change to dash distance.

## Hero assignments

All 38 snapshot heroes appear once: 9 in Bucket 1, 18 in Bucket 2, and 11 in
Bucket 3. Assignments group the stored ground/air dash duration pairs above.

### Bucket 1 (+5%)

[Calico](../../heroes/calico/calico.md), [Celeste](../../heroes/celeste/celeste.md),
[Grey Talon](../../heroes/grey-talon/grey-talon.md), [Haze](../../heroes/haze/haze.md),
[Holliday](../../heroes/holliday/holliday.md), [Ivy](../../heroes/ivy/ivy.md),
[Mina](../../heroes/mina/mina.md), [Paradox](../../heroes/paradox/paradox.md),
and [The Doorman](../../heroes/the-doorman/the-doorman.md).

### Bucket 2 (-5%)

[Apollo](../../heroes/apollo/apollo.md), [Billy](../../heroes/billy/billy.md),
[Drifter](../../heroes/drifter/drifter.md), [Graves](../../heroes/graves/graves.md),
[Infernus](../../heroes/infernus/infernus.md), [Lash](../../heroes/lash/lash.md),
[McGinnis](../../heroes/mcginnis/mcginnis.md), [Mirage](../../heroes/mirage/mirage.md),
[Pocket](../../heroes/pocket/pocket.md), [Seven](../../heroes/seven/seven.md),
[Silver](../../heroes/silver/silver.md), [Sinclair](../../heroes/sinclair/sinclair.md),
[Vindicta](../../heroes/vindicta/vindicta.md),
[Viscous](../../heroes/viscous/viscous.md), [Vyper](../../heroes/vyper/vyper.md),
[Warden](../../heroes/warden/warden.md), [Wraith](../../heroes/wraith/wraith.md),
and [Yamato](../../heroes/yamato/yamato.md).

### Bucket 3 (-15%)

[Abrams](../../heroes/abrams/abrams.md), [Bebop](../../heroes/bebop/bebop.md),
[Dynamo](../../heroes/dynamo/dynamo.md), [Kelvin](../../heroes/kelvin/kelvin.md),
[Lady Geist](../../heroes/lady-geist/lady-geist.md), [Mo & Krill](../../heroes/mo-and-krill/mo-and-krill.md),
[Paige](../../heroes/paige/paige.md), [Rem](../../heroes/rem/rem.md),
[Shiv](../../heroes/shiv/shiv.md), [Venator](../../heroes/venator/venator.md),
and [Victor](../../heroes/victor/victor.md).

## Stamina usage remains separate

A bucket changes dash timing, not the baseline stamina cost. The [universal
movement rules](universal-movement.md#stamina-actions) list ground dash, air
dash, and air jump as costing 1 stamina each; a dash jump costs 2 total, and a
down dash costs 0.5. Air actions retain their per-jump limits regardless of
bucket.

Likewise, stamina charge count, recovery, stamina-restoring upgrades, stamina
drains, and effects that block or pause stamina are separate mechanics. Consult each
hero's `base_stats.stamina` fields and ability records for those values.

## Evidence boundary

The hero dash durations and distances are derived from the pinned
`Data:HeroData.json` records. The bucket names and percentage labels were supplied
with a link to [Stamina](https://deadlock.wiki/Stamina), but the page could not be
independently retrieved (TLS failure / HTTP 403). No wiki revision or successful
access date is established for that reference. This article remains
`needs_primary_verification` until those labels and their mapping are verified;
the local duration and distance checks do not establish that external evidence.
The current
repository source registry permits Deadlock Wiki, Deadlock API, and the
Deadlock Wiki data repository; forum material is therefore not used as a
repository source. Bucket assignments describe this snapshot and are not a
claim about later patches.
