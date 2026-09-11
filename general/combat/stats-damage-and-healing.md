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
  - wiki.lifesteal.146618
  - wiki.warden.125788
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
  - github.deadlock-data.english.311b2e8d895e
  - deadlock-api.items.client-6684.source-10933105
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

## Healing, Lifesteal, and Healing Reduction

Healing includes direct recovery, health regeneration, and lifesteal. Healing
Amp increases outgoing healing. Lifesteal is divided into separate stat domains:

- **Bullet Lifesteal** returns a percentage of outgoing bullet damage.
- **Spirit Lifesteal** returns a percentage of outgoing Spirit damage.
- **Melee Lifesteal** returns a percentage of outgoing melee damage, but some
  melee-lifesteal items use a one-attack proc with a cooldown and a separate
  flat-healing component rather than behaving like continuously active Bullet or
  Spirit Lifesteal.

Bullet and Spirit Lifesteal are calculated independently. Compatible sources
of the same lifesteal stat stack multiplicatively, not additively. This is not
permission to combine every ability-specific heal or item proc into that stat:

`total lifesteal = 1 - (1 - L1) * (1 - L2) * ...`

For a hypothetical example, 22% and 30% Bullet Lifesteal combine to 45.4%,
not 52%. These are arithmetic inputs, not claims about current item values.

### Non-hero and NPC effectiveness

The general Wiki Lifesteal rule gives reduced effectiveness against creeps and
other non-hero units: Bullet Lifesteal is 60% effective, while Spirit Lifesteal
and continuously applied Melee Lifesteal are 40% effective. These are category
defaults, not overrides for every ability or item.

Resolve the source, target type, upgrade tier, and game mode first. Distinguish
an **absolute percentage of damage returned as healing** from **effectiveness
multiplying an otherwise calculated heal**. An explicit non-hero value replaces
the default for that particular effect; do not apply the category NPC reduction
again. It does not override separate lifesteal sources on the same hero.

### Explicit target-specific rules

These are pinned base values before applicable upgrades and healing modifiers:

| Effect | Hero target | Non-hero target | Interpretation |
| --- | --- | --- | --- |
| [Abrams — Siphon Life](../../heroes/abrams/abrams.md) | 70% | 35% | Absolute percentage of this ability's damage returned as healing. |
| [Bebop — Hyper Beam, tier 3](../../heroes/bebop/bebop.md) | 65% | 20% | Absolute percentage of Hyper Beam damage, not 20% effectiveness of the 65% hero heal. Only unlocked at tier 3. |
| [Warden — Last Stand](../../heroes/warden/warden.md) | 75% | 10% | Separate hero/non-hero lifesteal percentages for this ability. |
| [Lash — Flog](../../heroes/lash/lash.md) | 50% | 16% | Ability-specific damage-to-healing, not a general Spirit Lifesteal bonus. Tier 3 adds 20 percentage points versus heroes and 6 versus non-heroes in the structured upgrades. |
| [Mo & Krill — Scorn](../../heroes/mo-and-krill/mo-and-krill.md) | 1.2× damage | 0.35× damage | Damage-to-heal multipliers, equivalent to 120% and 35%; do not interpret 0.35 as 0.35%. |
| [Melee Lifesteal item](../../items/melee-lifesteal/melee-lifesteal.md) | Flat 100 heal on proc | 30% effectiveness of the proc heal | The pinned item has a flat heal, not an additional damage-percentage component. |
| [Lifestrike](../../items/lifestrike/lifestrike.md) | 100 + 30% of melee damage on proc | 40% effectiveness of the proc heal | Its reduction applies to the described heal, including flat and damage-based components. |

For example, with 100 qualifying damage and no healing modifiers, Siphon Life's
own NPC heal is 35, Hyper Beam tier 3's is 20, and Scorn's is 35. They are not
reduced by another 40% factor. Melee Lifesteal's base NPC proc heals 30; Lifestrike
on 100 melee damage heals `(100 + 0.30 * 100) * 0.40 = 52` against an NPC.
These examples exclude any separate lifesteal effects and available-health caps.

Melee Lifesteal and Lifestrike have proc cooldowns; light melee hits make the
cooldown 1.5× as long. Their cooldowns do not prevent healing from other sources.
Do not add their proc heals to a generic lifesteal percentage pool.

**Mode exception:** [Warden's Street Brawl section](https://deadlock.wiki/Warden?oldid=125788#Street_Brawl)
states Last Stand heals for 48.75% against heroes and 7.5% against non-heroes
in that mode. These values must not replace its standard-mode 75%/10% values.

**Ability scope is also a rule:** Mo & Krill's Combo tier 1 grants 100% lifesteal
for Combo, and Infernus's Concussive Combustion tier 2 grants 100% explosion
lifesteal. Neither description grants 100% global Spirit Lifesteal. These
percentages alone do not establish a different NPC multiplier or how their
healing combines with purchased lifesteal; do not invent either interaction.

### Healing modifiers

Multiple Healing Reduction sources stack multiplicatively:

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
[Healing](https://deadlock.wiki/Healing?oldid=96635), and
[Lifesteal](https://deadlock.wiki/Lifesteal?oldid=146618).
Target-specific values above also reference the linked canonical hero/item
records and their pinned generated-data/localization/API sources. The Lifesteal
hub describes both melee items as having percentage-based heals, but the pinned
Melee Lifesteal item and its live item page instead describe a flat heal; use
the item-specific record. Its worked-example item percentages also differ from
its dynamic item table. No current item values are imported from that example.
