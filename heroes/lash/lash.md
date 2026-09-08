---
id: hero.lash
title: Lash
domain: heroes
topics: [hero]
aliases: []
summary: Lash is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.lash.125562
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Lash

Lash is a currently selectable **Assassin** hero. Internal key: `hero_lash`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 2/s |
| Move speed | 7.2m/s |
| Sprint bonus | 2.1m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **8.46**
- Rounds/s: **5.8309**; magazine: **29**; reload: **2.35s**
- Projectile speed: **635m/s**; falloff: **18–54m**
- Source DPS: **49.329**; sustained: **33.5**

## Abilities

### 1. Ground Strike

Internal key: `citadel_ability_lash_down_strike`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Stomp the ground beneath you, damaging enemies in front of you. If you perform Ground Strike while airborne, you quickly dive towards the ground. Damage grows slower after 25m.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Struck enemies are knocked up and slowed by 50% for 3s
- **Tier 3:** Damage Per Meter +110% and improved scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorCanCastOnZipline`.

| Card field | Base value |
| --- | ---: |
| Stomp Damage | 60 (+0.7905 per spirit) |
| Damage Per Meter | 5.5 (+0.04 per spirit) |
| Duration | 0 |
| Enemy Move Speed | 0 |
| Slow Duration | 0 |
| Cooldown | 18 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-10}`
- Tier 2: `{"EnemySlowPct":50,"SlowDuration":3,"StompBounceHeight":400,"TossDuration":1}`
- Tier 3: `{"StompDamagePerMeterPrimary":{"Value":2.13,"Scale":{"Value":0.03255,"Type":"spirit"},"Multiply":true},"StompDamagePerMeterSecondary":{"Value":2.13,"Scale":{"Value":0.008137,"Type":"spirit"},"Multiply":true}}`

### 2. Grapple

Internal key: `citadel_ability_lash`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Pull yourself through the air toward a target. Using Grapple also resets your limit of air jumps and dashes.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +20m Cast Range and gain +7 Weapon Damage for 10s
- **Tier 3:** +1 Charges OnCast : +1 Stamina and +60% Air Control

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorMovement`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Jump Velocity | 20 |
| Weapon Damage | 0 |
| Bonus Duration | 0 |
| Fire Rate | 0 |
| Cooldown | 35 (+1 per cooldown) |
| Cast Range | 30 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 2 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-17}`
- Tier 2: `{"AbilityCastRange":20,"WeaponDamageBonus":7,"WeaponDamageBonusDuration":10}`
- Tier 3: `{"AbilityCharges":1,"RestoreStaminaOnUse":1,"AirControlPercent":60}`

### 3. Flog

Internal key: `ability_lash_flog`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Strike enemies in front of you with your whip, healing for a portion of the damage dealt.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Apply -35% Move speed for 3s
- **Tier 2:** Apply -30% Fire Rate -16s Cooldown
- **Tier 3:** +80 Damage +40 Attack angle +20% Heal

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorNoTarget`, `BehaviorShowCastRangeAsSatSphereWhileCasting`.

| Card field | Base value |
| --- | ---: |
| Damage | 65 (+0.85 per spirit) |
| Heal vs heroes | 50 (+1 per healing) |
| Attack Angle | 38 |
| Heal vs non-heroes | 16 (+1 per healing) |
| Enemy Move Speed | 0 |
| Debuff Duration | 0 |
| Fire Rate | 0 |
| Cooldown | 26 (+1 per cooldown) |
| Cast Range | 20 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"EnemySlowDuration":3,"EnemySlowPct":35}`
- Tier 2: `{"AbilityCooldown":-16,"FireRateSlow":30}`
- Tier 3: `{"Damage":80,"TargetingConeAngle":40,"HealPctVsHeroes":20,"HealPctVsNonHeroes":6}`

### 4. Death Slam

Internal key: `citadel_ability_lash_ultimate`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Focus on enemies to connect whips to them. After channeling, connected enemies are lifted and stunned then slammed into the ground. Your victims and any enemies in the landing zone will be damaged and slowed.
> Press [Attack] to throw connected enemies early. Enemies that are not in line of sight or go out of range during the latch time will not be grabbed.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** Stun enemies in Radius for 1.2s +6m Cast Range

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`, `BehaviorCastRangeIs2d`.

| Card field | Base value |
| --- | ---: |
| Impact Damage | 105 (+0.974938 per spirit) |
| Max Throw Distance | 14 |
| Move Speed | 50 |
| Slow Duration | 4 (+1 per duration) |
| Cast Delay | 0.3 |
| Cooldown | 170 (+1 per cooldown) |
| Cast Range | 20 (+1 per radius) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"ThrowDistance":12}`
- Tier 2: `{"AbilityCooldown":-35}`
- Tier 3: `{"StunDuration":1.2,"AbilityCastRange":6}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Lash](https://deadlock.wiki/Lash?oldid=125562) article and generated data revisions. No wiki media is included.
