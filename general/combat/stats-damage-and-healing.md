---
id: general.combat.stats-damage-and-healing
title: Core Stats, Damage, and Healing
domain: general
topics:
  - stats
  - damage
  - resistance
  - health
  - healing
aliases:
  - Weapon
  - Vitality
  - Spirit
  - damage mitigation
summary: The general stat families, damage classifications, resistance stacking, maximum health, and healing rules.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: needs_primary_verification
sources:
  - wiki.stats.87937
  - wiki.health.111364
  - wiki.damage-resistance.125735
  - wiki.damage-amplification.114181
  - wiki.healing.96635
  - wiki.pure-damage.106367
  - wiki.spirit-damage.125734
  - wiki.bullet-damage.108550
---

# Core Stats, Damage, and Healing

## Stat Families

Deadlock groups most stats into three families:

- **Weapon:** ammunition, bullet damage, projectile radius and velocity, fire
  rate, falloff, reload time, Weapon Damage, and melee-related stats.
- **Vitality:** health, regeneration, healing, lifesteal, movement, stamina,
  barriers, evasion, and damage or debuff resistance.
- **Spirit:** Spirit Power, ability cooldown, duration, range, charges, and
  spirit-damage scaling.

Boons, abilities, map buffs, and purchased effects can modify these stats.

## Spirit Scaling

Unless a specific mechanic states otherwise, an explicitly Spirit-scaled value is
calculated as:

`base value + (total Spirit Power * Spirit coefficient)`

This general rule applies to ability damage, item-proc damage, healing, barriers,
and other values whose source field declares a Spirit coefficient. Values without
an explicit Spirit coefficient do not scale with Spirit Power. Each damage or
healing instance uses the current total Spirit Power when that instance occurs.

Mixed-scaling abilities calculate each component independently using its own
scaling type. Spirit scaling does not implicitly apply to weapon- or
melee-scaled values.

## Damage Classifications

- **Weapon Damage** includes ordinary weapon attacks and some ability or NPC
  attacks. Bullet Resistance reduces Weapon Damage.
- **Melee Damage** is a form of Weapon Damage dealt by melee attacks and some
  abilities. It is affected by both Bullet Resistance and Melee Resistance and
  qualifies for applicable Weapon Damage triggers such as Weapon Shielding.
- **Spirit Damage** is common to abilities and is reduced by Spirit Resistance.
- **Pure Damage** is outside the weapon, melee, and spirit categories. The pinned
  source says it bypasses Damage Resistance and barriers; invincibility can prevent it.

The effect's damage classification, not whether it visually looks like a bullet
or spell, determines which resistance applies.

## Resistance Stacking

Multiple resistance sources stack multiplicatively:

`total resistance = 1 - (1 - R1) * (1 - R2) * ...`

Resistance-reduction sources are combined using the same multiplicative method,
then subtracted from total resistance:

`final resistance = total resistance - total resistance reduction`

Final resistance can be negative. For example, -30% resistance means the target
takes 130% of the incoming damage before other applicable modifiers.

## Damage Amplification

The pinned wiki separates damage amplification into additive, multiplicative,
and instance categories. It also documents unique exceptions and a mismatch
between stated patch intent and observed live Damage Reduction stacking.
Consequently, the generalized amplification formula is reference knowledge only
in this baseline. It must not become executable calculation logic until each
supported modifier is typed and verified.

## Maximum Health

The wiki describes maximum health as:

`(starting base health + health gained from Boons) * (1 + base-health bonuses) + bonus health`

Flat bonus health is added after percentage base-health increases. The displayed
maximum is rounded up to the nearest integer. Starting health and health per
Boon are hero-specific and excluded here.

Heroes normally regenerate health over time. The Respawn Room raises recovery
to 6% of maximum health plus 60 health per second. Enemy Medic Packs are another
general source of direct healing.

## Healing and Healing Reduction

Healing includes direct recovery, health regeneration, and lifesteal. Healing
Amp increases outgoing healing. Multiple Healing Reduction sources stack
multiplicatively:

`total reduction = 1 - (1 - R1) * (1 - R2) * ...`

The pinned final-healing order is:

`final healing = initial healing * (1 - total reduction) * (1 + healing amp)`

Repeated applications from the same Healing Reduction source do not stack while
the first is active.

## Evidence Limitation

The Damage Resistance source has an under-construction section, the Spirit
Damage source is a stub, and the Damage Amplification formula is based on
community testing with documented exceptions. The classifications are useful
for retrieval, but executable calculations require a narrower primary-verified
rule set.

## Source Notes

Adapted from pinned Deadlock Wiki revisions listed in this document's `sources`
metadata, including
[Stats](https://deadlock.wiki/Stats?oldid=87937),
[Damage Resistance](https://deadlock.wiki/Damage_Resistance?oldid=125735),
[Damage Amplification](https://deadlock.wiki/Damage_Amplification?oldid=114181),
and [Healing](https://deadlock.wiki/Healing?oldid=96635).
