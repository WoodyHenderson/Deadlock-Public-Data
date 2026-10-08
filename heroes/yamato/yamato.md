---
id: hero.yamato
title: Yamato
domain: heroes
topics: [hero]
aliases: []
summary: Yamato is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - github.deadlock-data.hero-data.fc4f540f12e0
  - github.deadlock-data.ability-data.fc4f540f12e0
  - github.deadlock-data.ability-cards.fc4f540f12e0
  - github.deadlock-data.english.fc4f540f12e0
  - wiki.yamato.124895
---

# Yamato

Yamato is a currently selectable **Assassin** hero. Internal key: `hero_yamato`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 1/s |
| Move speed | 8.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 55 / 128 |

## Weapon

- Bullet damage: **5.31**
- Rounds/s: **2.381**; magazine: **12**; reload: **2.444s**
- Projectile speed: **254m/s**; falloff: **19.99–45.72m**
- Source DPS: **63.216**; sustained: **42.571**
- Alt-fire bullet damage: **50**; rounds/s: **0.95238**; magazine: **9**; reload: **2.1s**

## Abilities

### 1. Power Slash

Internal key: `citadel_ability_power_slash`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Channel to increase damage over 1.4 seconds, then release a fully-charged sword strike.
> Press [Ability 1] or [Attack] to trigger the strike early, dealing partial damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +32% Movement Slow for 3s
- **Tier 2:** -4s Ability Cooldown
- **Tier 3:** +8m Cast Range +150 Damage and Increases Spirit Power scaling

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorShowCastRangeAsSatSphereWhileCasting`.

| Card field | Base value |
| --- | ---: |
| Full Charge Damage | 145 (+1.85 per spirit) |
| Slash Length | 22 (+1 per range) |
| Move Speed | 0 |
| Slow Duration | 0 |
| Bullet Resist | 60 |
| Cooldown | 12 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"SlowDuration":3,"SlowPercent":32}`
- Tier 2: `{"AbilityCooldown":-4}`
- Tier 3: `{"FullChargeDamage":{"Value":150,"Scale":{"Value":0.5,"Type":"spirit"}},"SlashLength":8}`
### 2. Flying Slash

Internal key: `citadel_ability_flying_strike`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a grappling hook to reel yourself towards an enemy, dealing Light melee damage and slowing the target when you arrive.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Gain +35 Spirit Power for 6s
- **Tier 3:** Alt-Cast to Grapple allies +15m Cast Range Gains 1 extra charge

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorMovement`, `BehaviorCanSetQuickCast`, `BehaviorDeactivateCrouchToggleOnCast`, `BehaviorAllowAltCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 0 (+1.2 per melee) |
| Move Speed | 40 |
| Slow Duration | 2.5 (+1 per duration) |
| Cast Range | 26 (+1 per range) |
| Cooldown | 36 (+1 per cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-18}`
- Tier 2: `{"SpiritBonus":35,"BuffDuration":6}`
- Tier 3: `{"AbilityCastRange":15,"CanGrappleAllyHeroes":1,"AbilityCharges":2,"AbilityCooldownBetweenCharge":5}`
### 3. Crimson Slash

Internal key: `citadel_ability_healing_slash`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Slash enemies in front of you, damaging them and slowing their fire rate. If any enemy heroes are hit, you heal.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Hit : +30% Melee Damage for 4s
- **Tier 2:** On Hero Hit : +6% Max Health Heal
- **Tier 3:** -10s Cooldown and increases scaling

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 55 (+0.37 per spirit) |
| Heal on hero hit | 55 (+1.035871 per spirit) |
| Fire Rate | 30 |
| Debuff Duration | 4 (+1 per duration) |
| Cooldown | 16 (+1 per cooldown) |
| Charge Delay | -1 |
| Radius | 13 (+1 per radius) |

Upgrade deltas:
- Tier 1: `{"BuffDuration":4,"BuffMeleeDamage":30}`
- Tier 2: `{"HealMaxHealth":6}`
- Tier 3: `{"AbilityCooldown":-10,"Damage":{"Value":0,"Scale":{"Value":0.6,"Type":"spirit"}},"HealFixedHealth":{"Value":0,"Scale":{"Value":0.4,"Type":"spirit"}}}`
### 4. Shadow Transformation

Internal key: `citadel_ability_infinity_slash`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Become infused with Yamato's shadow soul. After an initial invincible transformation your abilities are refreshed and are 60% faster. You gain immunity to negative status effects and have greatly increased bullet and spirit resist.
> When you get a hero kill, you heal and the duration is extended.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +4m Move Speed and -20 Cooldown
- **Tier 3:** +3s Duration +30% Bullet Resist +30% Spirit Resist

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCleaveDisabled`, `BehaviorCanCancelDuringCastDelay`, `BehaviorCannotCancelDuringChannel`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Duration | 5 (+1 per duration) |
| Ability Speed | 60 |
| Max Health Heal | 15 (+1 per healing) |
| Bullet Resist | 30 |
| Spirit Resist | 30 |
| Duration On Kill | 2 (+1 per duration) |
| MaxHealthHealOnCast | 0 |
| Cooldown | 150 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"WeaponDamageBonus":7}`
- Tier 2: `{"BonusMoveSpeed":4,"AbilityCooldown":-20}`
- Tier 3: `{"AbilityDuration":3.0,"BulletResist":30,"TechResist":30}`
## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Yamato](https://deadlock.wiki/Yamato?oldid=124895) article and generated data revisions. No wiki media is included.
