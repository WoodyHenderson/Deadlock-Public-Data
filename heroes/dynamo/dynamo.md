---
id: hero.dynamo
title: Dynamo
domain: heroes
topics: [hero]
aliases: []
summary: Dynamo is a selectable Mystic hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.dynamo.124881
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Dynamo

Dynamo is a currently selectable **Mystic** hero. Internal key: `hero_dynamo`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 880 |
| Health regeneration | 1.75/s |
| Move speed | 6.7m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **12.6**
- Rounds/s: **3.8095**; magazine: **20**; reload: **2.35s**
- Projectile speed: **320m/s**; falloff: **19.99–57.51m**
- Source DPS: **48**; sustained: **33.158**

## Abilities

### 1. Kinetic Pulse

Internal key: `citadel_ability_stomp`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Release an energy pulse that travels along the ground, dealing spirit damage and applying knockup.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +1 Charge
- **Tier 2:** On Hit: -15% Bullet Resist and -30% Move Speed for 4s
- **Tier 3:** +135 Damage and +20m Cast Range

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 115 (+1.55 per spirit) |
| Duration | 1 |
| Pulse Range | 16 (+1 per range) |
| Pulse Width | 5.5 |
| Cooldown | 26 (+1 per cooldown) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 5 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1}`
- Tier 2: `{"BulletResistReduction":-15,"SlowPercent":30,"SlowDuration":4}`
- Tier 3: `{"Damage":135,"StompRange":20}`

### 2. Quantum Entanglement

Internal key: `citadel_ability_void_sphere`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Briefly become untargetable while teleporting to the target location. Restores stamina upon use.
> [Alt Cast] : Bring nearby allies with you.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** Reduces non-ult debuffs by 50% Replenishes 1 Charge

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorPreventBotUsage`, `BehaviorAllowAltCast`, `BehaviorMovement`, `BehaviorCanSetQuickCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Cast Range | 10 (+1 per range) |
| Duration | 1.4 (+1 per duration) |
| Stamina Restored | 1 |
| Ally Distance | 13 |
| Cooldown | 20 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCastRange":6}`
- Tier 2: `{"AbilityCooldown":-6}`
- Tier 3: `{"ReduceDebuffs":50,"ChargeReplenish":1}`

### 3. Rejuvenating Aurora

Internal key: `citadel_ability_nikuman`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> While channeling, restore health over time to you and any allies nearby.
> You can dash and melee without breaking the channel.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Aura provides +4m Move Speed during channel
- **Tier 2:** -20 Cooldown and +1s Duration
- **Tier 3:** Full move and ability use and additionally heals +2.5% of Max Health per second

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorCanHealPlayers`, `BehaviorDisplaysDamageImpact`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Health Restored | 30 (+0.4 per spirit) |
| Channel Duration | 5 (+1 per duration) |
| Friendly Heal Radius | 8 (+1 per radius) |
| Cooldown | 48 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MovementSpeedBonus":4,"MovementSpeedBonusDuration":8}`
- Tier 2: `{"AbilityCooldown":-20,"AbilityChannelTime":1}`
- Tier 3: `{"NoChannel":1,"HealMaxHealthPercent":2.5}`

### 4. Singularity

Internal key: `citadel_ability_self_vacuum`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Create a singularity in your hands, dealing spirit damage over time, applying stun, and pulling in nearby enemies.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorExclusiveUse`, `BehaviorCastableWhileBusy`, `BehaviorInterruptMeleeOnCast`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 75 (+0.28 per spirit) |
| Max Health as Damage | 0 |
| Singularity Radius | 7 (+1 per radius) |
| Channel Duration | 2.75 (+1 per duration) |
| Cooldown | 250 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"VacuumRadius":2}`
- Tier 2: `{"AbilityChannelTime":0.75}`
- Tier 3: `{"DPSPercentHealth":6}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Dynamo](https://deadlock.wiki/Dynamo?oldid=124881) article and generated data revisions. No wiki media is included.
