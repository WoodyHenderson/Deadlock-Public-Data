---
id: hero.viscous
title: Viscous
domain: heroes
topics: [hero]
aliases: []
summary: Viscous is a selectable Mystic hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.viscous.124936
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Viscous

Viscous is a currently selectable **Mystic** hero. Internal key: `hero_viscous`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 2/s |
| Move speed | 7.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 63 / 116 |

## Weapon

- Bullet damage: **10.34**
- Rounds/s: **4.7619**; magazine: **20**; reload: **2.5s**
- Projectile speed: **254m/s**; falloff: **19.99–57.51m**
- Source DPS: **49.238**; sustained: **30.866**

## Abilities

### 1. Splatter

Internal key: `viscous_goo_grenade`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a ball of goo that deals damage and leaves puddles of goo behind that apply movement slow to enemies in the radius.

> Multiple hits to the same target deal less damage.

> Goo puddles linger on the ground and apply a movement slow to enemies walking on them.
> You and your allies slide faster on goo puddles.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +36 Damage and +2m Radius
- **Tier 3:** Bounces 1 times and improves Spirit Scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 55 (+0.7 per spirit) |
| Bounces | 2 |
| Cooldown | 26 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":36,"Radius":2}`
- Tier 2: `{"AbilityCooldown":-14}`
- Tier 3: `{"MaxBounces":1,"Damage":{"Value":0,"Scale":{"Value":0.9,"Type":"spirit"}}}`

### 2. The Cube

Internal key: `viscous_restorative_goo`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Encase the target in a cube of restorative goo that protects from damage, and increases health regen. Target is unable to take any new actions while cubed. Can be used on self. Press [Mantle] to escape early.

> After exiting the cube, the target has increased move speed and stamina recovery for a short duration.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Increases Move Speed and Stamina Recovery
- **Tier 2:** +25 Health Regen and +1s Duration
- **Tier 3:** Removes all non-ult Debuffs and -20s Cooldown

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorEqualUnitTargetPriority`, `BehaviorAllowSelfCast`, `BehaviorCanHealPlayers`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Health Regen | 40 (+0.3 per spirit) |
| Duration | 3 (+1 per duration) |
| Cooldown | 42 (+1 per cooldown) |
| Cast Range | 26 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":2.5,"StaminaCooldownReduction":30,"PostCubeBuff":1}`
- Tier 2: `{"BonusHealthRegen":25,"AbilityDuration":1}`
- Tier 3: `{"AbilityCooldown":-20,"PurgeDebuffs":1}`

### 3. Puddle Punch

Internal key: `viscous_telepunch`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Materialize a fist in the world that punches everyone in the area, applying knockup.
> Punching an enemy deals melee damage and applies slow.
> You and your allies have increased Air Control.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +1 Charge and +20 Damage
- **Tier 2:** +1.5m Radius and +60% Lifesteal
- **Tier 3:** -14s Cooldown and now deals Heavy Melee Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 20 (+0.6 per melee) |
| Damage | 0 (+0 per heavy melee) |
| Move Speed | 30 |
| Duration | 0.6 |
| Slow Duration | 3 (+1 per duration) |
| Cooldown | 21 (+1 per cooldown) |
| Cast Range | 40 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 1.7 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1,"Damage":20}`
- Tier 2: `{"Radius":1.5,"LifeStealPercentOnHit":60}`
- Tier 3: `{"AbilityCooldown":-14,"UseHeavyMelee":1,"DamageHeavyMelee":{"Value":40,"Scale":{"Value":0.6,"Type":"heavy_melee"}},"Damage":{"Value":-40,"Scale":{"Value":0,"Type":"melee","Multiply":true}}}`

### 4. Goo Ball

Internal key: `viscous_goo_bowling_ball`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Morph into a large goo ball that deals damage and stuns enemies on impact. The ball grants large amounts of Bullet and Spirit resist, bounces off walls and can double jump.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +70 Damage and +20% Resists
- **Tier 3:** +7s Duration and +0.3s Stun Duration

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorDeactivateCrouchToggleOnCast`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorInhibitSoftCameraCollision`.

| Card field | Base value |
| --- | ---: |
| Damage | 110 (+1 per spirit) |
| Stun Duration | 0.5 (+1 per duration) |
| Ball Radius | 1.4 (+1 per radius) |
| Spirit Resist | 35 |
| Bullet Resist | 35 |
| Cooldown | 150 (+1 per cooldown) |
| Duration | 11 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-25}`
- Tier 2: `{"Damage":70,"BulletResist":20,"TechResist":20}`
- Tier 3: `{"AbilityDuration":7,"StunDuration":0.3}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Viscous](https://deadlock.wiki/Viscous?oldid=124936) article and generated data revisions. No wiki media is included.
