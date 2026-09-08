---
id: hero.mina
title: Mina
domain: heroes
topics: [hero]
aliases: []
summary: Mina is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.mina.124886
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Mina

Mina is a currently selectable **Marksman** hero. Internal key: `hero_vampirebat`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 660 |
| Health regeneration | 2/s |
| Move speed | 6.5m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 2 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **7.31**
- Rounds/s: **3.9683**; magazine: **12**; reload: **1.7s**
- Projectile speed: **762m/s**; falloff: **19.99–46m**
- Source DPS: **29.008**; sustained: **18.569**

## Abilities

### 1. Rake

Internal key: `ability_vampirebat_steallife`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Active: Slash with your umbrella, dealing spirit damage, increasing with their missing health. Receive a heal for every target killed.
> Passive: Holding [ADS] causes you to briefly float.
> Rake executes non-heroes below 60 health.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +30 Heal per Kill -8s Cooldown
- **Tier 3:** +7% Missing health damage and increased Heal per Kill Spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`, `BehaviorUseLagCompensationForUnitTargeting`.

| Card field | Base value |
| --- | ---: |
| Damage | 60 (+1 per stats count) |
| Missing Health Damage | 6 |
| Cooldown | 16 (+1 per cooldown) |
| Cast Range | 10 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":60}`
- Tier 2: `{"RakeHealPerKill":30,"AbilityCooldown":-8}`
- Tier 3: `{"MissingHealthDamagePercentage":7,"RakeHealPerKill":{"Value":0,"Scale":{"Value":1.2,"Type":"spirit"}}}`

### 2. Sanguine Retreat

Internal key: `ability_vampirebat_batblink`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Briefly disperse, becoming untargetable and flying to a target location.
> Can be recast within a brief window.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Cast: Gain +25% Fire Rate for 8s and add 8 bullets
- **Tier 3:** +1 Recast +4m Range

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorDisplaysDamageImpact`, `BehaviorPreventBotUsage`, `BehaviorCannotCancelDuringChannel`, `BehaviorAllowAltCast`, `BehaviorMovement`, `BehaviorCanSetQuickCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Cast Range | 9 |
| Recast Window | 4 (+1 per duration) |
| Cooldown | 32 (+1 per cooldown) |
| Duration | 0.65 |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusFireRate":25,"BuffDuration":8,"BonusBullets":8}`
- Tier 2: `{"AbilityCooldown":-10}`
- Tier 3: `{"MaxRecasts":1,"AbilityCastRange":4}`

### 3. Love Bites

Internal key: `ability_vampirebat_lovebites`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Your bullets apply additional spirit damage. Dealing damage your abilities builds up to a vicious bite, dealing a burst of bonus spirit damage.
> Love Bites has a unique cooldown per target.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Proc: +30% Slow for 3s
- **Tier 2:** +3 Spirit Damage per Bullet & +45 Bonus Damage
- **Tier 3:** -5 Cooldown On Proc: +25% Fire Rate for 5s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

| Card field | Base value |
| --- | ---: |
| Spirit Damage Per Bullet | 4 (+0.09 per spirit) |
| Bonus Damage | 45 (+1.85 per spirit) |
| Fire Rate | 0 |
| Move Speed | 0 |
| Slow Duration | 0 |
| Buff Duration | 0 |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"SlowDuration":3,"SlowPercent":30}`
- Tier 2: `{"MagicDamagePerBullet":3,"BonusDamage":45}`
- Tier 3: `{"PerTargetCooldown":-5,"BonusFireRate":25,"BuffDuration":5}`

### 4. Nox Nostra

Internal key: `ability_vampirebat_batswarm`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Active: Unleash a cloud of bats that seek out targets, each dealing spirit damage and applying Silence.
> Passive: Triggering Love Bites against heroes permanently increases the number of bats released.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** On Hit: Deal +0.5% Current Health as Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Bats per Second | 30 |
| Damage | 4.6 (+0.094 per spirit) |
| Debuff Duration | 1.25 (+1 per duration) |
| Current Health | 0 |
| Additional Bats Per Love Bite | 2 |
| Total Bats Released | 75 |
| Cooldown | 150 (+1 per cooldown) |
| Cast Range | 40 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":1.9}`
- Tier 2: `{"AbilityCooldown":-45}`
- Tier 3: `{"CurrentHealthPercent":0.5}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Mina](https://deadlock.wiki/Mina?oldid=124886) article and generated data revisions. No wiki media is included.
