---
id: hero.vyper
title: Vyper
domain: heroes
topics: [hero]
aliases: []
summary: Vyper is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.vyper.124934
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Vyper

Vyper is a currently selectable **Assassin** hero. Internal key: `hero_viper`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 2/s |
| Move speed | 6.9m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 4 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **6.58**
- Rounds/s: **14.286**; magazine: **24**; reload: **1.6s**
- Projectile speed: **411.5m/s**; falloff: **14.99–33.02m**
- Source DPS: **94.002**; sustained: **48.147**

## Abilities

### 1. Screwjab Dagger

Internal key: `ability_viper_debuffdagger`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a dagger, dealing spirit damage and applying slow.
> Every subsequent dagger against the same target stacks in spirit damage and slow.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** On Hit: -8% Bullet Resist and -6% Bullet Resist per Stack
- **Tier 3:** +2 Max Stacks -2s Charge Delay On Hit: Refund 55% Charge Cooldown

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDontSwitchAwayOnCast`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 50 (+0.8 per spirit) |
| Move Speed | 35 |
| Bullet Resist | 0 |
| Cooldown | 10 (+1 per cooldown) |
| Charges | 2 (+1 per max charges) |
| Charge Delay | 4 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1}`
- Tier 2: `{"BulletResistReduction":-8,"BulletResistReductionPerStack":-6}`
- Tier 3: `{"CooldownRefundPercent":55,"MaxStacks":2,"AbilityCooldownBetweenCharge":-2}`

### 2. Lethal Venom

Internal key: `ability_viper_venom`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Inject a target with lethal venom. After a delay the venom triggers, dealing Spirit Damage. The damage is increased by the target's missing health.
> Lethal Venom will ignore Petrify's damage block.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -40% Healing Reduction and -12s Cooldown
- **Tier 3:** Bullets also build up Lethal Venom

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Minimum Venom Damage | 20 (+0.651 per spirit) |
| Max Venom Damage | 140 (+2.79 per spirit) |
| Missing Health Damage | 0 |
| Health for Max Damage | 30 |
| Venom Buildup Duration | 3 |
| Healing Reduction | 0 |
| Cooldown | 28 (+1 per cooldown) |
| Cast Range | 10 |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"VenomMaxDamage":31.5}`
- Tier 2: `{"HealAmpRegenPenaltyPercent":-40,"HealAmpReceivePenaltyPercent":-40,"AbilityCooldown":-12}`
- Tier 3: `{"BuildUpPerShot":4.5}`

### 3. Slither

Internal key: `ability_viper_snakedash`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> You have increased Slide Distance, can Slide up hills, and can turn faster while Sliding.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** On Slide: Gain 180 barrier for 5s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorPreventBotUsage`, `BehaviorMovement`.

| Card field | Base value |
| --- | ---: |
| Slide Distance | 15 |
| Barrier | 0 (+0 per spirit) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"SlideScale":20}`
- Tier 2: `{"Stamina":2}`
- Tier 3: `{"BuffDuration":5,"CombatBarrier":{"Value":180,"Scale":{"Value":0.8,"Type":"spirit"}},"AbilityCooldown":8}`

### 4. Petrifying Bola

Internal key: `ability_viper_petrifybola`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw an explosive bola. On exploding, the bola Slows and Damages all enemies in the area.
> Direct hits deal Additional Damage and Petrify instead. Petrified units block all damage, but cannot take actions.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +1s Petrify Duration. Petrifies all enemies in the area.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Petrify Duration | 2.2 (+1 per duration) |
| Damage | 50 (+0.744 per spirit) |
| Petrify Damage | 180 (+2.046 per spirit) |
| Move Speed | 50 |
| Slow Duration | 1.5 (+1 per duration) |
| Cooldown | 105 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"PetrifyDamage":49.5}`
- Tier 2: `{"AbilityCooldown":-20}`
- Tier 3: `{"PetrifyDuration":1}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Vyper](https://deadlock.wiki/Vyper?oldid=124934) article and generated data revisions. No wiki media is included.
