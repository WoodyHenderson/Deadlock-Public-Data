---
id: hero.kelvin
title: Kelvin
domain: heroes
topics: [hero]
aliases: []
summary: Kelvin is a selectable Brawler hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.kelvin.125564
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Kelvin

Kelvin is a currently selectable **Brawler** hero. Internal key: `hero_kelvin`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 880 |
| Health regeneration | 1/s |
| Move speed | 6.7m/s |
| Sprint bonus | 1.1m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **18.6**
- Rounds/s: **3.8095**; magazine: **14**; reload: **2.585s**
- Projectile speed: **160m/s**; falloff: **19.99–57.51m**
- Source DPS: **70.857**; sustained: **41.597**

## Abilities

### 1. Frost Grenade

Internal key: `ability_ice_grenade`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a grenade that explodes in a cloud of freezing ice that heals allies and applies spirit damage and move speed reduction to enemies.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +30 Damage and +30 Heal Amount
- **Tier 2:** -10 Cooldown and debuff now freezes Stamina Regen
- **Tier 3:** +2m Radius. Damage and Heal Spirit Scaling increased.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorCanHealPlayers`, `BehaviorProjectileFiredAsBullet`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 60 (+0.6 per spirit) |
| Heal Amount | 60 (+0.8 per spirit) |
| Move Speed | 40 |
| Slow Duration | 4 (+1 per duration) |
| Cooldown | 30 (+1 per cooldown) |
| Charges | 2 (+1 per max charges) |
| Charge Delay | 7 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"Damage":30,"HealAmount":30}`
- Tier 2: `{"PauseStaminaRegen":1,"AbilityCooldown":-10}`
- Tier 3: `{"Radius":2,"HealAmount":{"Value":0,"Scale":{"Value":0.9,"Type":"spirit"}},"Damage":{"Value":0,"Scale":{"Value":0.8,"Type":"spirit"}}}`

### 2. Ice Path

Internal key: `ability_icepath`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Kelvin creates a floating trail of ice and snow that gives movement bonuses to him and his allies. Kelvin gains 60% slow resistance for the duration. Enemies can also walk on the floating trail.
> Press [Roll] / [Crouch] to travel up or down while in Ice Path.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +2m Move Speed and +35% Bullet Resist for Kelvin while on Ice Path
- **Tier 3:** +35% Spirit and +20 Spirit for Kelvin while on Ice Path

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDontInterruptSprint`, `BehaviorCastableWhileBusy`, `BehaviorInterruptMeleeOnCast`, `BehaviorNoTarget`, `BehaviorPreventBotUsage`, `BehaviorMovement`, `BehaviorDeactivateCrouchToggleOnCast`, `BehaviorRequireAbilityButtonToCancel`.

| Card field | Base value |
| --- | ---: |
| Move Speed | 2 |
| Sprint Speed | 2 |
| Ice Trail Duration | 18 |
| Cooldown | 50 (+1 per cooldown) |
| Duration | 8 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MoveSpeedBonus":2,"BulletResist":35}`
- Tier 2: `{"AbilityCooldown":-25}`
- Tier 3: `{"BonusSpiritPct":35,"BonusSpirit":20}`

### 3. Arctic Beam

Internal key: `ability_icebeam`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Shoot freezing cold energy out in front of you, damaging targets and progressively reducing their movement and fire rate the longer you sustain the beam on them. You have reduced move speed while using Arctic Beam. The beam may also claim Souls.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -25% to Fire Rate and Move Speed
- **Tier 2:** +20 DPS and increased Spirit Scaling
- **Tier 3:** -13s Cooldown and Fires 2 additional Arctic Beams within 10m of the last target hit.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDontAimFacingEnemy`, `BehaviorRequireAbilityButtonToCancel`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 45 (+0.38 per spirit) |
| Max Move Speed | 20 |
| Max Fire Rate | 20 |
| Time To Max Debuff | 2 |
| Beam Length | 25 (+1 per range) |
| Debuff Linger Duration | 2 (+1 per duration) |
| Extra Beam Range | 0 (+0 per range) |
| Max Dash Slow | -20 |
| Cooldown | 28 (+1 per cooldown) |
| Duration | 5 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MaxSlowPercent":25,"MaxFireRateSlowPercent":25}`
- Tier 2: `{"DPS":{"Value":20,"Scale":{"Value":0.6,"Type":"spirit"}}}`
- Tier 3: `{"BeamSplit":{"Value":10,"Scale":{"Value":0.93,"Type":"range"}},"BeamSplitCount":2,"AbilityCooldown":-13}`

### 4. Frozen Shelter

Internal key: `ability_ice_dome`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Target yourself or a Hero to freeze the air and create an impenetrable dome around them. While in the dome, allies gain rapid regeneration and enemies are slowed.
> Objectives becomes Invulnerable and Frozen under Frozen Shelter

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** Purges non-ult debuffs for you and your allies. +65 Health Regen that now scales with Spirit

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCastableWhileBusy`, `BehaviorInterruptMeleeOnCast`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorDisplaysDamageImpact`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorCanSetQuickCast`, `BehaviorAllowSelfCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Health Regen | 90 (+0 per spirit) |
| Fire Rate | 0 |
| Move Speed | 35 |
| Max Health Heal | 0 |
| Cooldown | 185 (+1 per cooldown) |
| Duration | 5 (+1 per duration) |
| Cast Range | 8 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20}`
- Tier 2: `{"AbilityDuration":1.5}`
- Tier 3: `{"BonusHealthRegen":{"Value":65,"Scale":{"Value":1,"Type":"spirit"}},"PurgeOnCast":1}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Kelvin](https://deadlock.wiki/Kelvin?oldid=125564) article and generated data revisions. No wiki media is included.
