---
id: hero.calico
title: Calico
domain: heroes
topics: [hero]
aliases: []
summary: Calico is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.calico.125743
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Calico

Calico is a currently selectable **Assassin** hero. Internal key: `hero_nano`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 2/s |
| Move speed | 6.8m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 63 / 116 |

## Weapon

- Bullet damage: **1.84**
- Rounds/s: **4.7619**; magazine: **12**; reload: **2.6s**
- Projectile speed: **317.5m/s**; falloff: **19.99–57.51m**
- Source DPS: **78.857**; sustained: **38.812**

## Abilities

### 1. Gloom Bombs

Internal key: `ability_nano_clustergrenade`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a cluster of bombs that detonate after a delay, dealing spirit damage.
> Enemies hit by multiple bombs take 65% damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Per Bomb Touch : -6% Melee Resist for 6s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Bomb Count | 4 |
| Damage | 45 (+0.644 per spirit) |
| Bonus Damage vs Barriers | 0 |
| Cooldown | 14 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-3}`
- Tier 2: `{"MeleeResistReduction":-6,"MeleeResistReductionDuration":6}`
- Tier 3: `{"GrenadeCount":3}`

### 2. Leaping Slash

Internal key: `ability_nano_dash`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Dash forward before slashing all enemies in a circle, dealing melee damage.
> If the ability hits at least one hero, heal a small amount of health.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Heros killed within 3s grant +200 souls
- **Tier 3:** +60 Damage & On Hero Hit: 50% Cooldown Refund

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontTriggerPostCastOnCastComplete`, `BehaviorMovement`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Impact Damage | 10 (+0.8 per melee) |
| Heal Amount | 40 (+1.4 per spirit) |
| Cooldown Refund | 0 |
| Bounty Duration | 0 |
| Cooldown | 13 (+1 per cooldown) |
| Cast Range | 9 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"HealAmount":25}`
- Tier 2: `{"BonusGoldOnKill":200,"BountyDuration":3}`
- Tier 3: `{"CooldownRefundPercent":50,"ImpactDamage":60}`

### 3. Ava

Internal key: `ability_nano_catform`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Turn to shadows and possess Ava. You gain bonus move speed that increases over time, and become hidden on the minimap.
> Taking damage from an enemy hero resets your bonus move speed and puts Ava on a brief cooldown.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +15 Health Regen & +40% Max Move Speed
- **Tier 3:** Gain Damage Amp over time, up to 18%. Lingers for 6s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorCannotCancelDuringChannel`, `BehaviorInhibitSoftCameraCollision`, `BehaviorMovement`, `BehaviorPreventBotUsage`, `BehaviorRequireAbilityButtonToCancel`.

| Card field | Base value |
| --- | ---: |
| Min Move Speed | 30 |
| Max Move Speed | 65 |
| Buff Duration | 15 (+1 per duration) |
| Interrupt Cooldown | 6 |
| Health Regen | 0 |
| Cooldown | 30 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BuffDuration":15}`
- Tier 2: `{"MaxBonusMoveSpeedPercent":40,"HealthRegen":15}`
- Tier 3: `{"OutgoingDamagePercent":18,"DamageAmpDuration":6,"DamageAmpBuildDuration":10}`

### 4. Return to Shadows

Internal key: `ability_nano_shadow_pulse`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Instantly turn to shadows, becoming untargetable, gaining bonus move speed, and dealing spirit damage.
> After a delay, return from the shadows, dealing spirit damage again.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +75 Damage and +20% Move Speed
- **Tier 3:** On Completion: Heal for 450 and refund all ability cooldowns

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorCastableWhileDodging`, `BehaviorMovement`, `BehaviorDeactivateCrouchToggleOnCast`, `BehaviorInhibitSoftCameraCollision`.

| Card field | Base value |
| --- | ---: |
| Damage | 150 (+0.609336 per spirit) |
| Move Speed | 20 |
| Channel Duration | 3 (+1 per duration) |
| Damage | 0 |
| Cooldown | 115 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20}`
- Tier 2: `{"Damage":75,"BonusMoveSpeedPercent":20}`
- Tier 3: `{"RefundCooldowns":1,"HealAmount":450}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Calico](https://deadlock.wiki/Calico?oldid=125743) article and generated data revisions. No wiki media is included.
