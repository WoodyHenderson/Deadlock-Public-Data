---
id: hero.rem
title: Rem
domain: heroes
topics: [hero]
aliases: []
summary: Rem is a selectable hero whose generated hero-type field is currently unset; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.rem.124942
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Rem

Rem is a currently selectable hero. The pinned generated data does not assign a hero type. Internal key: `hero_familiar`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 680 |
| Health regeneration | 2/s |
| Move speed | 7.2m/s |
| Sprint bonus | 4m/s |
| Stamina | 3 |
| Light / heavy melee | 58 / 116 |

## Weapon

- Bullet damage: **16**
- Rounds/s: **3.8462**; magazine: **13**; reload: **2s**
- Projectile speed: **160m/s**; falloff: **19.99–57.51m**
- Source DPS: **61.539**; sustained: **38.662**

## Abilities

### 1. Pillow Toss

Internal key: `ability_familiar_ability02`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw your trusty pillow inflicting spirit damage and heavy knockback.
> Landing hits reduces the cooldown of your other abilities.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +2m Radius and applies -35% Fire Rate
- **Tier 3:** +100 Damage and +1 Charge

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorProjectile`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 75 (+1.6 per spirit) |
| Fading Move Speed | 45 |
| Duration | 0.4 |
| Debuff Duration | 3 (+1 per duration) |
| Cooldown | 25 (+1 per cooldown) |
| Cast Range | 40 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 8 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-7}`
- Tier 2: `{"FireRateSlow":35,"Radius":2}`
- Tier 3: `{"Damage":100,"AbilityCharges":1}`

### 2. Tag Along

Internal key: `ability_familiar_attach`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Jump to an ally and nap alongside them. Both you and the ally receive a burst heal based on missing health followed by lingering regeneration.
> Hop between allies with [Ability 2] to apply the heal, once per ally.
> You are knocked off if stunned by an ultimate ability.
> You can use items and all self-casts target your ally instead.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** 35% Bonus Item Range, Duration, and Barrier Effectiveness while napping
- **Tier 3:** +15% Spirit Power and +35 Spirit Power while napping and for 10s after napping Improved Spirit Scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDontBreakInvisibility`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorCooldownOnChannelEnd`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorMovement`, `BehaviorCanSetQuickCast`, `BehaviorDoNotAllowSpamProc`.

| Card field | Base value |
| --- | ---: |
| Missing Health Burst | 15 (+0.03 per spirit) |
| Health Restored | 42 (+0.4 per spirit) |
| Barrier Effectiveness | 0 |
| Bonus Item Duration/Range | 0 |
| Regen Duration | 2 (+1 per duration) |
| Spirit Power | 0 |
| Buff Duration | 0 |
| Bonus Spirit Power | 0 |
| Cooldown | 40 (+1 per cooldown) |
| Duration | 5.5 (+1 per duration) |
| Cast Range | 23 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-8}`
- Tier 2: `{"BonusBarrierAmpPercent":35,"BonusItemDurationPercent":35,"BonusItemRangePercent":35}`
- Tier 3: `{"TechPowerPercent":15,"BonusSpiritPower":35,"HopOffEffecDuration":10,"MissingHealthBurstPct":{"Value":0,"Scale":{"Value":0.016,"Type":"spirit"}},"HealingPerSecond":{"Value":0,"Scale":{"Value":0.34,"Type":"spirit"}}}`

### 3. Lil Helpers

Internal key: `ability_familiar_helpinghands`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Signal a Helper to lend a hand. They can collect boxes, do Sinner's Sacrifices, or be sent to support allies and troopers.
> Follow a hero: Provides a short burst of spirit resist and fading move speed.
> Follow a trooper: Provides healing, damage, resists, and allows tagging along. When no hero is around, souls from trooper kills are split amongst the team.
> Can be cast during Tag Along. Helpers will take a nap for 15.1s after following someone.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +1 Helper +1.5m/s Move Speed
- **Tier 2:** +1 Helper +15% Trooper Damage and Resist
- **Tier 3:** +1 Helper +15% Spirit Resist

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSprint`, `BehaviorAllowSelfCast`, `BehaviorDamageDoesntWakeFromSleep`, `BehaviorDisplaysDamageImpact`, `BehaviorDoNotAllowSpamProc`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Cast Range | 45 (+0 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"HelperCount":1,"BonusMoveSpeed":1.5}`
- Tier 2: `{"HelperCount":1,"InfestDamageTakenPercent":15}`
- Tier 3: `{"HelperCount":1,"TechArmorGain":15}`

### 4. Naptime

Internal key: `ability_familiar_ability01`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Cast your gaze forward, piercing walls and floors. Enemies in the gaze are slowed, have reduced dash distance, and cannot use movement abilities.
> When the channel ends they fall asleep before waking up to a splitting headache that deals heavy spirit damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -1 Stamina On Wake and no Stamina Regen while sleeping
- **Tier 2:** +3m Radius and +0.75s Sleep Duration
- **Tier 3:** -55s cooldown Reduced damage and unstoppable while channeling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorCannotCancelDuringChannel`, `BehaviorDisplaysDamageImpact`, `BehaviorCooldownOnChannelEnd`, `BehaviorRefundHalfCooldownOnChannelInterrupt`.

| Card field | Base value |
| --- | ---: |
| Wake Damage | 120 (+1.6 per spirit) |
| Sleep Damage Threshold | 100 (+3.1 per power increase) |
| Move/Dash Slow | 25 |
| Radius | 19 (+1 per range) |
| Sleep Duration | 4 (+1 per duration) |
| Cooldown | 200 (+1 per cooldown) |
| Cast Range | 24 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"ConsumeStaminaOnWake":1,"NoStaminaRegenDuringSleep":1}`
- Tier 2: `{"SleepDuration":0.75,"Radius":3}`
- Tier 3: `{"DamageResistPctWhileChanneling":50,"UnstoppableWhileChanneling":1,"AbilityCooldown":-55}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Rem](https://deadlock.wiki/Rem?oldid=124942) article and generated data revisions. No wiki media is included.
