---
id: hero.celeste
title: Celeste
domain: heroes
topics: [hero]
aliases: []
summary: Celeste is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.celeste.125568
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Celeste

Celeste is a currently selectable **Marksman** hero. Internal key: `hero_unicorn`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 690 |
| Health regeneration | 1/s |
| Move speed | 6.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 4 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **18**
- Rounds/s: **1.7241**; magazine: **8**; reload: **2s**
- Projectile speed: **50m/s**; falloff: **22–60m**
- Source DPS: **31.034**; sustained: **21.686**

## Abilities

### 1. Light Eater

Internal key: `ability_unicorn_radiantblast`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Blast enemies in a cone in front of you with a flare of light. Blasted enemies take spirit damage when attacked by Celeste and provides her spirit lifesteal.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -10s Cooldown and +3m Cast Range
- **Tier 3:** +25 Damage and Increased Spirit Scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorUseLagCompensationForUnitTargeting`, `BehaviorDontInterruptSlideOnCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Spirit Lifesteal | 20 (+1 per healing) |
| Flare Damage | 40 (+0.47 per spirit) |
| Duration | 8 |
| Cooldown | 20 (+1 per cooldown) |
| Cast Range | 10 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityLifestealPercentHero":15}`
- Tier 2: `{"AbilityCastRange":3,"AbilityCooldown":-10}`
- Tier 3: `{"Damage":{"Value":25,"Scale":{"Value":0.2,"Type":"spirit"}}}`

### 2. Dazzling Trick

Internal key: `ability_unicorn_prismaticguard`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Surround yourself in a protective prism. If the barrier is destroyed, it silences nearby enemies and deals a portion of the barrier as damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +70 Barrier and Increased Barrier Spirit Scaling
- **Tier 3:** +1.25 Silence Duration and -20s Cooldown. Allows Shining Wonder Bounce.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`.

| Card field | Base value |
| --- | ---: |
| Barrier | 100 (+0.8 per spirit) |
| Move Speed | 0 |
| Buff Duration | 4 (+1 per duration) |
| Cooldown | 34 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":3.5}`
- Tier 2: `{"CombatBarrier":{"Value":70,"Scale":{"Value":0.76,"Type":"spirit"}}}`
- Tier 3: `{"DebuffDuration":1.25,"AbilityCooldown":-20}`

### 3. Radiant Daggers

Internal key: `ability_unicorn_luminousstrike`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Call down a beam of light from the sky. After a short duration, the beam will fully form, causing an explosion that deals spirit damage to all targets in the area.
> Celeste will receive a stacking buff that increases her spirit damage anytime this hits an enemy hero.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -22s Cooldown and +80 Impact Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Impact Damage | 55 (+0.63 per spirit) |
| Spirit Amp per Stack | 7 |
| Fire Rate per Stack | 0 |
| Explosion Radius | 8 (+1 per range) |
| Buff Duration | 30 (+1 per duration) |
| Cooldown | 33 (+1 per cooldown) |
| Cast Range | 30 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 2 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":2}`
- Tier 2: `{"ImpactDamage":80,"AbilityCooldown":-22}`
- Tier 3: `{"MagicIncreasePerStack":4,"FireRatePerStack":9}`

### 4. Shining Wonder

Internal key: `ability_unicorn_dazzlingorb`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Launch a deadly orb of light that deals spirit damage and applies slow and reduces Dash Distance on impact. The orb then bounces to the enemies within range. If no target is found, the orb will linger for a short duration while continuing to look for targets.
> Prioritizes enemy heroes when picking targets.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -20% Move Speed and -15% Dash Distance
- **Tier 2:** +90 Damage and Increased Spirit Scaling
- **Tier 3:** +8 Max Bounces and -30s Cooldown

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorCooldownOnChannelEnd`.

| Card field | Base value |
| --- | ---: |
| Damage | 140 (+0.6 per spirit) |
| Move Speed | 40 |
| Bounces | 8 |
| Dash Distance | -25 |
| Slow Duration | 1.5 (+1 per duration) |
| Bounce Range | 16.5 (+1 per range) |
| Cooldown | 160 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"GroundDashReductionPercent":-15,"SlowPercent":20}`
- Tier 2: `{"Damage":{"Value":90,"Scale":{"Value":0.45,"Type":"spirit"}}}`
- Tier 3: `{"MaxBounces":8,"AbilityCooldown":-30}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Celeste](https://deadlock.wiki/Celeste?oldid=125568) article and generated data revisions. No wiki media is included.
