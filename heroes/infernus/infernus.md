---
id: hero.infernus
title: Infernus
domain: heroes
topics: [hero]
aliases: []
summary: Infernus is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.infernus.124880
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Infernus

Infernus is a currently selectable **Marksman** hero. Internal key: `hero_inferno`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 830 |
| Health regeneration | 2/s |
| Move speed | 6.7m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **5.5**
- Rounds/s: **9.5238**; magazine: **27**; reload: **2.25s**
- Projectile speed: **660.4m/s**; falloff: **18–55m**
- Source DPS: **52.381**; sustained: **29.204**

## Abilities

### 1. Napalm

Internal key: `ability_incendiary_projectile`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Spew an incendiary mixture, dealing spirit damage, applying slow, and coating targets in napalm.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Napalm Effect: +15% Lifesteal
- **Tier 3:** Napalm Effect: +17% Damage Taken and -33% Healing

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 40 (+0.6 per spirit) |
| Move Speed | 35 |
| Slow Duration | 4 (+1 per duration) |
| Cooldown | 25 (+1 per cooldown) |
| Cast Range | 20 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 6 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1}`
- Tier 2: `{"LifestealPercentHero":15}`
- Tier 3: `{"IncomingDamagePercentFromCaster":17,"HealAmpReceivePenaltyPercent":-33,"HealAmpRegenPenaltyPercent":-33}`

### 2. Flame Dash

Internal key: `ability_flame_dash`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Dash forward, gaining slow resistance while leaving a flaming trail that deals spirit damage over time.
> Hold [Move Forward] while active to dash farther.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +1s Trail Duration and +20 DPS
- **Tier 3:** Enable 2 Ability Charges with 14s Recharge time

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorPreventBotUsage`, `BehaviorMovement`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Max Dash Speed | 20 |
| Damage Per Second | 30 (+0.7 per spirit) |
| Fire Rate | 0 |
| Trail Duration | 4 (+1 per duration) |
| Trail Width | 4.5 (+1 per radius) |
| Slow Resistance | 50 |
| Cooldown | 38 (+1 per cooldown) |
| Duration | 3 (+1 per duration) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-12}`
- Tier 2: `{"DPS":20,"GroundFlameDuration":1}`
- Tier 3: `{"AbilityCharges":2,"AbilityCooldownBetweenCharge":14}`

### 3. Afterburn

Internal key: `ability_afterburn`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Weapon hits build up a burning effect, dealing spirit damage over time.
> Abilities refresh to the base burn duration and weapon hits extend it.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Burn Effect: -35% Spirit Damage
- **Tier 3:** +3s Max Burn Duration

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCleaveDisabled`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 14 (+0.66 per spirit) |
| Unknown(BurnDurationBase) | 3 |
| Burn Duration | 3 (+1 per duration) |
| Spirit Damage | 0 |
| Buildup Per Bullet | 8.1 |
| Buildup Per Headshot | 15.4 |
| Extend Per Headshot | 1 |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"DPS":16}`
- Tier 2: `{"OutgoingTechDamagePercent":-35}`
- Tier 3: `{"BurnDuration":3}`

### 4. Concussive Combustion

Internal key: `ability_fire_bomb`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Become a living bomb, dealing spirit damage and applying stun to all nearby enemies after a delay.
> Once cast, Concussive Combustion cannot be interrupted.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -65s Cooldown and +100% Explosion Lifesteal
- **Tier 3:** +0.9s Stun Duration and +10m Radius

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorCastableWhileBusy`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Explosion Delay | 3.25 |
| Damage | 125 (+0.974938 per spirit) |
| Stun Duration | 1.25 (+1 per duration) |
| Radius | 12 (+1 per radius) |
| Cooldown | 190 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":100}`
- Tier 2: `{"AbilityCooldown":-65,"LifeStealPercentOnHit":100}`
- Tier 3: `{"StunDuration":0.9,"Radius":10}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Infernus](https://deadlock.wiki/Infernus?oldid=124880) article and generated data revisions. No wiki media is included.
