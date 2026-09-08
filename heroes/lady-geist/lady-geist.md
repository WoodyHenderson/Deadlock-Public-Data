---
id: hero.lady-geist
title: Lady Geist
domain: heroes
topics: [hero]
aliases: []
summary: Lady Geist is a selectable Mystic hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.lady-geist.124875
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Lady Geist

Lady Geist is a currently selectable **Mystic** hero. Internal key: `hero_ghost`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 880 |
| Health regeneration | 1/s |
| Move speed | 6.3m/s |
| Sprint bonus | 2.4m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **20.7**
- Rounds/s: **2.1164**; magazine: **9**; reload: **2.585s**
- Projectile speed: **828m/s**; falloff: **17–48m**
- Source DPS: **43.809**; sustained: **27.247**

## Abilities

### 1. Essence Bomb

Internal key: `ability_blood_bomb`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Sacrifice some of your health to launch a bomb that deals damage after a brief arm time.
> Self damage type is Spirit and can be mitigated.

> Bombs leave a toxic mess on the ground, dealing 26% of the original damage per second, for 6s.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +2m Radius and +50 Damage.
- **Tier 3:** Bombs leave a toxic mess on the ground, dealing 26% of the original damage per second, for 6s.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 90 (+1.22 per spirit) |
| Health Cost | 30 |
| Arming Duration | 0.65 |
| Cooldown | 14 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-5}`
- Tier 2: `{"Damage":50,"Radius":2}`
- Tier 3: `{"BloodSpillDPSPercent":26,"BloodSpillDuration":6}`

### 2. Life Drain

Internal key: `ability_life_drain`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Create a tether that drains enemy health over time and heals you. Target must be in line of sight and within max range to drain. You can shoot and use other abilities during the drain, but your move speed is reduced.
> [Alt Cast] to give health to friendly Heroes.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** Enables and Grants +2 Charges. Increases spirit scaling.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorAllowAltCast`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 24 (+0.3225 per spirit) |
| Damage to Heal | 100 (+1 per healing) |
| Max Tether Range | 28 (+1 per range) |
| Cooldown | 34 (+1 per cooldown) |
| Duration | 2.5 (+1 per duration) |
| Cast Range | 18 (+1 per range) |

Upgrade deltas:
- Tier 1: `{"LifeDrainPerSecond":13}`
- Tier 2: `{"AbilityDuration":2.5}`
- Tier 3: `{"AbilityCharges":3,"AbilityCooldownBetweenCharge":0.1,"LifeDrainPerSecond":{"Value":0,"Scale":{"Value":0.3,"Type":"spirit"}}}`

### 3. Malice

Internal key: `ability_blood_shards`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Sacrifice some of your health to launch blood shards that apply a stack of Malice. Each stack slows the victim and increases the damage they take from you. The slow effect decreases over time.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +25.2 Damage and +4 Blood Shards
- **Tier 3:** +8% Damage Amp

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 23 (+0.558 per spirit) |
| Health Cost | 9 |
| Blood Shards | 3 |
| Max Stacks | 5 |
| Cooldown | 6 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-3}`
- Tier 2: `{"HealthToDamage":25.2,"NumBloodShards":4,"SpreadAngleDegrees":22}`
- Tier 3: `{"VulnerabilityPerStack":8}`

### 4. Soul Exchange

Internal key: `ability_health_swap`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Swaps health levels with an enemy target. There is a minimum health percentage that enemies can be brought down to and a minimum amount of health received based on victims current health.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Silence enemies within 25m for 3s
- **Tier 3:** On cast, +60 Spirit Power, +40% Fire Rate and +50% Spirit Resistance for 8s.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorCleaveDisabled`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Enemy Min Health | 30 |
| Min Health Received | 30 |
| Silence Duration | 0 |
| Silence Radius | 0 |
| Cooldown | 220 (+1 per cooldown) |
| Duration | 0.25 |
| Cast Range | 5.5 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-50}`
- Tier 2: `{"SilenceDuration":3,"SilenceRadius":25}`
- Tier 3: `{"SelfBuffDuration":8,"TechResist":50,"BonusFireRate":40,"BonusSpirit":60}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Lady Geist](https://deadlock.wiki/Lady_Geist?oldid=124875) article and generated data revisions. No wiki media is included.
