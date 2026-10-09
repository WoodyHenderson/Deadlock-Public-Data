---
id: general.map.map-interactions-and-open-questions
title: City Never Sleeps Map Interactions and Remaining Questions
domain: general
topics: [Haunts, Steam Vents, Healing Snacks, Tough Crates, Buff Containers, Sinners Sacrifice, Broker]
aliases: [new map mechanics, vent reveal, snack healing, crate rewards, jackpot timing]
summary: Source-dated map behavior, reconciled pre-release values, and explicit remaining conflicts before later hero releases.
snapshot_id: pre-rat-king-map-with-dated-wiki-interpretations
current_as_of: "2026-10-08"
evidence_status: source_verified_with_explicit_conflicts
sources:
  - github.deadlock-data.gameplay.0d46cdecfccf
  - wiki.haunt.177431
  - wiki.haunt.181836
  - wiki.steam-vent.177398
  - wiki.healing-snack.177162
  - wiki.healing-snack.181344
  - wiki.crate.177311
  - wiki.buff-container.177257
  - wiki.permanent-buff.161283
  - wiki.permanent-buffs.161111
  - wiki.souls-value-table.177401
  - wiki.sinners-sacrifice.177553
  - wiki.sinners-sacrifice.181842
  - wiki.broker.177584
---

# City Never Sleeps Map Interactions

Use [structured interactions](../../data/map-interactions.yaml) for individual
values and evidence boundaries; [camp compositions](haunt-camps-and-sinner-sites.md)
for families, camp patterns and Sinner sites; and the [map guide](../../map/README.md)
for coordinates. Wiki-described behavior is useful evidence, not an independent
in-game test. **The client cutoff remains October 1/client 6731.** Later wiki
interpretations below do not silently update the historical snapshot.

## Haunt attacks and activation

| Family | October 1 wiki description | Additional October 6 wiki detail |
| --- | --- | --- |
| Barrel Mimic | Medium/large explosion attack | Area explosion |
| Past Dues | Small has no melee; medium labeled melee-only | Book barrage, final projectile causes sleep; this coexists with the melee-only label |
| Festival Spirit | No melee; medium/large bomb attack | Homing-firework barrage |
| Slum Shroom | Spore attack slows and reduces healing by 50% | Mines deal damage over time |
| Crabbage Pot | Tier-two melee-area attack | Special described as parryable |
| Stage Hand | Large laser attack | Medium/large laser leaves fire on the ground |
| Specimen | Medium explodes on death | No separate special listed |
| Gutter Ghoul | No family attack detail given | Toxic projectile leaves a damaging puddle |
| Underhand | No melee; medium/large laser leaves fire | Same general description |

The October 1 article describes eye hits as critical damage. The October 6
article describes dormant Haunts ignoring distant damage until active, proximity
activation without automatic aggression, and some parryable melee attacks.
The three client-6731 tier bases have `SightRangePlayers: 38.1` metres. Connecting
that field to the activation threshold follows the wiki, not a measured radius.
Do not assume every special is parryable or all family variants share a weapon.

The canonical [small](../../npcs/small-neutral/small-neutral.yaml),
[medium](../../npcs/medium-neutral/medium-neutral.yaml), and
[large](../../npcs/large-neutral/large-neutral.yaml) records remain **shared tier
baselines**, not an exhaustive roster of placed families. Their unchanged core
health/resistance/reward/weapon values have been cross-checked to client 6731.
Old weakpoint counts/timers are explicitly legacy; absence of those fields or
the old large-tier melee-resistance modifier does not prove runtime removal.
The [Mid-Boss record](../../npcs/mid-boss/mid-boss.yaml) separately pins the
retained 35-per-second plus 5-per-match-minute shield absorption configuration.

## Steam Vents

The October 1 Steam Vent article (marked Stub/Construction) describes:
- Concealment from enemy heroes while allies can still see the occupant.
- Prevention of hero-targeted items/abilities, such as Knockdown—not invulnerability
  or protection from untargeted area damage.
- Reveal on taking damage/receiving an effect, damaging/applying an effect to an
  enemy hero, or an enemy hero entering the same vent.
- A regeneration display of **4.8 with a 0.083 boon-scaling annotation**. The
  exact engine formula/rounding has not been established; no calculator is inferred.

Steam Vents are not tunnel entrances. Their conditions must not be transferred
to other invisibility or tunnel mechanics.

## Healing Snacks: pre-release timing reconciled

The September 30 article explicitly says **3:00 initial spawn, 3:00 respawn
after pickup, and 10% maximum-health healing over four seconds**. These agree
with the pinned pre-release spawn and pickup configuration. Snacks are collected
by proximity, remain until collected, and are not shown on the minimap.

The October 4 revision instead says **2:30 initial spawn**, and adds **20% healing
in Street Brawl**. These are later descriptions, not applied to the October 1
snapshot. The evidence does not identify when or whether the timing difference
became a live gameplay change. The existing map has 36 snack markers.

## Ordinary crates, Tough Crates and respawn groups

The pinned October 1 Souls table explicitly gives these reward models:

| Type | Configured drop chance | Base Souls | Growth per elapsed match minute |
| --- | ---: | ---: | ---: |
| Ordinary crate | 60% | 23 | 2 |
| Tough Crate | 100% | 46 | 4 |

The table displays a floor-rounded linear model; scaling starts at match start,
not crate spawn. This supports the reward interpretation beyond raw field names,
but is not a test of exact engine rounding. A Tough Crate requires one heavy
melee, rejects bullets/abilities/sliding/dodge contact, and has `NoMeleeCleave`.
The wiki specifically excludes upgraded Puddle Punch's heavy-melee damage.

Crate/Buff Container articles bind schedule descriptors **1 → most breakables,
2 → tunnels, 3 → the room above Mid-Boss**. Pinned client 6731 gives respectively
180/180, 300/300 and 600/180 seconds (initial/respawn). This supports the category
mapping; it does not reconcile the intermediate client-6722 tunnel value or
map-marker `group` numbering. **Descriptor 4 remains unidentified** at 300/180.
Uncollected Souls or buff drops can delay object respawn according to the wiki.
The wiki's 518-crate total has ambiguous coverage relative to the coordinate
layer's separate ordinary/Tough/item-crate categories; it does not replace them.

## Buff Containers and permanent buffs

The pre-release article and client configuration agree on a **50% drop chance**,
with one permanent buff per successful container drop. The Permanent Buff page
says buffs persist through death and use levels beginning at **0, 10 and 30
minutes**, based on when received—not three minutes for level one's eligibility.
Three minutes is the usual container spawn, not the earliest buff from all sources.

The pinned template describes **pseudo-random selection**, considering buffs
from all sources; repeated identical buffs reduce the reported chance next time.
Container drops count when generated even if left uncollected, so refusing a
pickup does not reroll that history. Client weights total 10: seven ordinary
categories have weight 1, Health has 2, and Move Speed/Ability Range have 0.5 each.
These are relative weights, **not independent probabilities for each break** or
a guarantee of any particular next drop. The exact stateful algorithm, stacking
and Tier-1-only range-radius modifier interaction remain unverified.

## Sinner jackpot and rewards

The October 1 Sinner article and Souls template explicitly define the base
reward as **`GoldReward × 2`**, reconciling client `155` with **310 base Souls**.
Growth is 1.08% of that base per match minute (3.348 unrounded Souls/minute).
The article describes rounded light/heavy payouts of 1/20 and 1/10 of the value;
the final hit awards half plus one heavy payout. Per-hit rounding and multiplayer
splits mean this is not an exact payout simulator.

Pre-release prose describes randomized jackpot speed, no retaliation during the
jackpot state, and four buffs for a heavy-melee jackpot versus one for light.
Missing the timing gives the remaining Souls without jackpot buffs.

The **October 6** article explains two speeds: 40% fast and 60% slow, consistent
with client `MiniGameFastChance: 0.4`; it describes orange/red blinking for fast
and static white for slow, a choice after 300 damage and jackpot entry at 400.
Those indicator/threshold details remain later wiki interpretation. Exact cycle
durations are not established. The raw `VaultMiniGameHitWindow: 0.5` and
`VaultSuccessDestroyTime: 1.3` are different fields: **1.3 is not established as
the jackpot success window**.

The article also quotes 8 light/4 heavy hits despite 500 health and 50/100 damage
per hit. That reaches 400 damage; special final-destruction handling is not fully
explained. We preserve this conflict rather than invent hits-to-kill arithmetic.

## The Broker before the cutoff

The October 1 article describes a temporary vendor near each Blue-lane Walker,
two shops, first opening about 30 minutes, and reopening about 15 minutes after
closing. It describes converting items into corrupted variants with a random
downside and lists roll restrictions. Exact prices, mode gates, item eligibility
and the implementation of those restrictions remain unverified; configuration
and wiki descriptions are not a complete shop simulator. The article's scheduled
departure is **not** evidence that the October 2 disablement happened; that import
remains separate.

## Remaining work and placement audit

- Exact family/unit assignments for every camp and the six medium combinations.
- Runtime weakpoints/melee resistance, precise vent scaling, jackpot cycle lengths,
  final-hit handling and exact payout rounding.
- The later snack timing's effective date; unidentified breakable descriptor 4;
  exact buff-selection/stacking and corruption-roll implementation.
- **Theater/basketball-area placement re-audit:** the current authorized coordinate
  snapshot was validated, not refreshed. No newer authorized point export or
  dated before/after marker evidence was supplied in this pass. Wiki prose and
  raw NPC definitions cannot identify which individual crates moved or disappeared.
  Keep existing markers until a replacement export or specific verified coordinates
  support a diff. No geometry changes or camp assignments have been guessed.

## Provenance

All wiki statements above are paraphrases of the exact revisions listed in
[this document's metadata](../../sources/source-registry.yaml); the registry
records their timestamps and wikitext hashes. Numeric client checks use the
immutable client-6731 commit and hashes. See [attribution](../../ATTRIBUTION.md)
for reuse boundaries. No artwork, site code or identifying map-source details
are included.
