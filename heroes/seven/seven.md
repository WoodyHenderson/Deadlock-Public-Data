---
id: hero.seven
title: Seven
domain: heroes
topics: [hero]
aliases: []
summary: Seven is a selectable Mystic hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.seven.124882
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Seven

Seven is a currently selectable **Mystic** hero. Internal key: `hero_gigawatt`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 1/s |
| Move speed | 6.7m/s |
| Sprint bonus | 1.8m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **10.8**
- Rounds/s: **5.8309**; magazine: **29**; reload: **2.35s**
- Projectile speed: **635m/s**; falloff: **19.99–57.51m**
- Source DPS: **62.974**; sustained: **42.766**

## Abilities

### 1. Lightning Ball

Internal key: `citadel_ability_lightning_ball`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Shoot a ball of lightning that travels in a straight line. Does damage to all targets in its radius. Slows down when damaging enemies and stops if it hits the world.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -35% move speed on hit targets and +1s Lifetime
- **Tier 3:** +58.5 DPS and +1.75m radius

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 75 (+0.5 per spirit) |
| Radius | 4.25 (+1 per radius) |
| Move Speed | 0 |
| Lifetime | 5 (+1 per duration) |
| Cooldown | 26 (+1 per cooldown) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 6 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1}`
- Tier 2: `{"SlowPercent":35,"MaxLifetime":1}`
- Tier 3: `{"DPS":58.5,"ShockRadius":1.75}`

### 2. Static Charge

Internal key: `citadel_ability_static_charge`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Apply a charge to a target enemy hero. After a short duration, the static charge stuns and damages enemies within the radius.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +7m Radius +5m Cast range
- **Tier 3:** +0.9s Stun Duration +160 Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Stun Duration | 0.9 (+1 per duration) |
| Delay Before Stun | 3.5 |
| Damage | 35 (+0.792137 per spirit) |
| Radius | 5 (+1 per radius) |
| Cooldown | 42 (+1 per cooldown) |
| Cast Range | 15 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20}`
- Tier 2: `{"ShockRadius":7,"AbilityCastRange":5}`
- Tier 3: `{"StunDuration":0.9,"Damage":160}`

### 3. Power Surge

Internal key: `ability_power_surge`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Power up your weapon with a shock effect, making your bullets proc shock damage on your target. This shock damage bounces to enemies near your target. Occurs once per burst shot.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +3m Move Speed +8 Damage and increased scaling
- **Tier 3:** +10s Duration Applies -15% Spirit Resist

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Shock Damage | 10 (+0.14 per spirit) |
| Max Jumps | 4 |
| Jump Radius | 10 (+1 per radius) |
| Cooldown | 50 (+1 per cooldown) |
| Duration | 10 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-18}`
- Tier 2: `{"BonusMoveSpeed":3,"BonusPerChain":{"Value":8,"Scale":{"Value":0.23,"Type":"spirit"}},"DamagePerChain":{"Value":8,"Scale":{"Value":0.23,"Type":"spirit"}}}`
- Tier 3: `{"TechResistDebuff":-15,"DebuffDuration":10,"AbilityDuration":10}`

### 4. Storm Cloud

Internal key: `citadel_ability_storm_cloud`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Channel an expanding storm cloud around you that damages all enemies within its radius. Enemies do not take damage when they are out of line-of-sight.

> While channeling, press [Attack] to mark the targeted area to be struck with a powerful lightning bolt that knocks enemies away after a 0.25s delay. One use per cast.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +55% Bullet Resist while channeling Storm Cloud
- **Tier 2:** +7s Channel Time +10m Final Radius +5m Initial Radius
- **Tier 3:** +65 DPS +4m Flight Speed

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorExclusiveUse`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 95 (+0.6 per spirit) |
| Flight Speed | 1.5 |
| Initial Radius | 10 (+1 per radius) |
| Bullet Resist | 0 |
| Cooldown | 205 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BulletResistOnActive":55}`
- Tier 2: `{"Radius":10,"InitialRadius":5,"AbilityChannelTime":7}`
- Tier 3: `{"DPS":65,"FlightControlEnabled":4}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Seven](https://deadlock.wiki/Seven?oldid=124882) article and generated data revisions. No wiki media is included.
