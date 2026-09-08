---
id: hero.shiv
title: Shiv
domain: heroes
topics: [hero]
aliases: []
summary: Shiv is a selectable Brawler hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.shiv.125552
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Shiv

Shiv is a currently selectable **Brawler** hero. Internal key: `hero_shiv`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 830 |
| Health regeneration | 2/s |
| Move speed | 6.5m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **4.8**
- Rounds/s: **1.8141**; magazine: **10**; reload: **2.8s**
- Projectile speed: **609.6m/s**; falloff: **19.79–41.15m**
- Source DPS: **52.246**; sustained: **34.647**

## Abilities

### 1. Serrated Knives

Internal key: `citadel_ability_shiv_dagger`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a knife that bleeds an enemy. Each additional hit adds a stack and refreshes the bleed duration, causing the bleed to increase per stack.

> Ultimate Unlock: While rage is full knives will ricochet to another enemy and apply a slow to enemies they bleed.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +2 Charges
- **Tier 3:** +12 Bleed DPS with increased Spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCleaveDisabled`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Impact Damage | 0 (+0 per spirit) |
| Bleed DPS Per Knife | 10 (+0.13 per spirit) |
| Bleed Duration | 5 (+1 per duration) |
| Cooldown | 16 (+1 per cooldown) |
| Charges | 2 (+1 per max charges) |
| Charge Delay | 2 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"BleedDuration":2}`
- Tier 2: `{"AbilityCharges":2}`
- Tier 3: `{"BleedDPSPerStack":{"Value":12,"Scale":{"Value":0.07,"Type":"spirit"}}}`

### 2. Slice and Dice

Internal key: `citadel_ability_shiv_dash`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Perform a dash forward, damaging enemies along the path. Hit Enemies have their spirit resist reduced. This debuff can stack.

> Ultimate Unlock: While rage is full an echo of Shiv retraces the dash path after a short delay, damaging enemies again.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -4% Spirit Resist +2m Dash Range
- **Tier 3:** +50 Impact Damage -2s Cooldown per Hero hit.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorDontTriggerPostCastOnCastComplete`, `BehaviorMovement`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Impact Damage | 75 (+1.2 per spirit) |
| Time Window | 12 (+1 per range) |
| Spirit Resist | -6 |
| Debuff Duration | 14 (+1 per duration) |
| Cooldown | 16 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-6}`
- Tier 2: `{"TechArmorDamageReduction":-4,"DashRange":2}`
- Tier 3: `{"ImpactDamage":50,"CooldownReductionOnHit":2,"CooldownReductionOnHitNonHero":1,"MaxCooldownReductionsFromHits":8}`

### 3. Bloodletting

Internal key: `citadel_ability_shiv_defer_damage`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Take only a portion of incoming damage immediately and defer the rest to be taken over time. Activate to clear a portion of the deferred damage.

> Ultimate Unlock: While rage is full the amount of damage deferred is increased.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDamageDoesntWakeFromSleep`, `BehaviorDontConsumeAbilityResourceOnCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Incoming Damage Deferred | 25 |
| Deferred Damage Duration | 6 (+1 per duration) |
| Cooldown | 25 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-15}`
- Tier 2: `{"DeferClearPct":40}`
- Tier 3: `{"DamagePctDeferred":15}`

### 4. Killing Blow

Internal key: `citadel_ability_shiv_killing_blow`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Active: Leap forward, dealing spirit damage to the first enemy hero. If they are below the kill threshold, execute them instead.
> Finishing an enemy with Killing Blow lets you recast for 16s

> Passive: Damaging enemies fills you with rage. While at full rage, Shiv gains increased damage and unlocks special properties on his other abilities.

> Cooldown is increased by +30% if no hero is impacted.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +6 m Range +2 m/s in Full Rage.
- **Tier 2:** +16% Full Rage Bonus Damage -25s Cooldown
- **Tier 3:** +10% Enemy Health Threshold

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorDontTriggerPostCastOnCastComplete`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorMovement`, `BehaviorCanSetQuickCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 200 |
| Enemy health threshold | 18 |
| Cooldown | 145 (+1 per cooldown) |
| Cast Range | 12 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":2,"AbilityCastRange":6}`
- Tier 2: `{"BuffDamage":16,"AbilityCooldown":-25}`
- Tier 3: `{"EnemyHealthPercent":10}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Shiv](https://deadlock.wiki/Shiv?oldid=125552) article and generated data revisions. No wiki media is included.
