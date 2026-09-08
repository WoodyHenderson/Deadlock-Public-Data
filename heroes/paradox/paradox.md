---
id: hero.paradox
title: Paradox
domain: heroes
topics: [hero]
aliases: []
summary: Paradox is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.paradox.125556
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Paradox

Paradox is a currently selectable **Marksman** hero. Internal key: `hero_chrono`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 1/s |
| Move speed | 6.7m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **6.8**
- Rounds/s: **7.5586**; magazine: **40**; reload: **2.585s**
- Projectile speed: **525m/s**; falloff: **19.99–57.51m**
- Source DPS: **51.398**; sustained: **34.531**

## Abilities

### 1. Pulse Grenade

Internal key: `citadel_ability_chrono_pulse_grenade`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a grenade that begins pulsing when it lands. Each pulse expands the radius and applies spirit damage, time slow, and stacking increased damage for Paradox against the victim.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +20 Pulse Damage and increased Spirit scaling
- **Tier 3:** +4% Damage Amp and +1.6s Duration

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Pulse Damage | 35 (+0.3 per spirit) |
| Bonus Damage per Stack | 4 |
| Radius Per Pulse | 1 (+1 per radius) |
| Pulse Interval | 0.8 |
| Debuff Duration | 8 (+1 per duration) |
| Move Speed | 20 |
| Slow Duration | 0.2 (+1 per duration) |
| Cooldown | 32 (+1 per cooldown) |
| Duration | 3.2 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-12}`
- Tier 2: `{"PulseDamage":{"Value":20,"Scale":{"Value":0.5,"Type":"spirit"}}}`
- Tier 3: `{"DamageAmplificationPerStack":4,"AbilityDuration":1.6}`

### 2. Time Wall

Internal key: `citadel_ability_chrono_time_wall`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Create a time warping wall that stops time for all enemy projectiles and bullets that touch it and increases the speed and damage of friendly bullets.
> Enemies that touch the wall will be briefly slowed and silenced .

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +3.5s Duration +3m Width +1m Height
- **Tier 2:** 2.3s Silence Duration +35% Weapon Damage
- **Tier 3:** +2 Ability Charges

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorCanCancelDuringCastDelay`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Debuff Duration | 0 |
| Movement Slow | 80 |
| Time Stop Duration | 0.5 |
| Ally Weapon Damage | 30 |
| Wall Width | 8 (+1 per range) |
| Wall Height | 4 (+1 per range) |
| Ally Bullet Speed | 2 |
| Cooldown | 25 (+1 per cooldown) |
| Duration | 5.5 (+1 per duration) |
| Cast Range | 5.08 (+1 per range) |

Upgrade deltas:
- Tier 1: `{"TimeWallWidth":3,"TimeWallHeight":1,"AbilityDuration":3.5}`
- Tier 2: `{"FriendlyBulletDamageBonus":35,"DebuffDuration":2.3}`
- Tier 3: `{"AbilityCharges":3,"AbilityCooldownBetweenCharge":2}`

### 3. Kinetic Carbine

Internal key: `citadel_ability_chrono_kinetic_carbine`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Charge up a powerful shot of time energy, dealing spirit damage and applying a Time-Stop to enemies hit. The damage dealt increases with weapon damage. Move speed is increased while charging.
> While in the air and charging, [ADS] to timeslow your movement.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -12s Cooldown Increases Speed Scaling
- **Tier 3:** +2s Charge Hold Duration and +55% Damage Scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDontBreakInvisibility`, `BehaviorDontInterruptSprint`, `BehaviorCastableWhileBusy`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Max Damage | 5 (+125 per weapon power) |
| Max Time-Stop | 0.4 (+1 per duration) |
| Bonus Speed | 25 (+0.13 per spirit) |
| Min Damage | 5 (+25 per weapon power) |
| Charge Hold Duration | 3.5 (+1 per duration) |
| Headshot Damage | 14 |
| Cooldown | 28 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MaxSlowDuration":0.4}`
- Tier 2: `{"AbilityCooldown":-12,"SpeedChange":{"Value":0,"Scale":{"Value":0.06,"Type":"spirit"}}}`
- Tier 3: `{"SpeedBoostDuration":2,"MinBonusBulletDamage":{"Value":0,"Scale":{"Value":55,"Type":"weapon_power"}},"MaxBonusBulletDamage":{"Value":0,"Scale":{"Value":55,"Type":"weapon_power"}}}`

### 4. Paradoxical Swap

Internal key: `citadel_ability_chrono_swap`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Fire a projectile that swaps your position with the target enemy hero.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** 200 Barrier for 8s. Barrier scales with Spirit
- **Tier 2:** -30s Cooldown and +13m Cast Range
- **Tier 3:** Swaps all enemies within 7m of hit target and +10% Max Health Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorCleaveDisabled`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorAllowAltCast`.

| Card field | Base value |
| --- | ---: |
| Swap Damage | 150 (+1.1 per spirit) |
| Max Health Damage | 0 |
| Barrier | 0 (+0 per spirit) |
| Barrier Duration | 0 |
| Multi Target Radius | 0 |
| Cooldown | 110 (+1 per cooldown) |
| Cast Range | 25 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"CombatBarrier":{"Value":200,"Scale":{"Value":1.5,"Type":"spirit"}},"BarrierDuration":8}`
- Tier 2: `{"AbilityCastRange":13,"AbilityCooldown":-30}`
- Tier 3: `{"MultiSwap":7,"MaxHealthDamage":10}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Paradox](https://deadlock.wiki/Paradox?oldid=125556) article and generated data revisions. No wiki media is included.
