---
id: hero.warden
title: Warden
domain: heroes
topics: [hero]
aliases: []
summary: Warden is a selectable Brawler hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.warden.124932
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Warden

Warden is a currently selectable **Brawler** hero. Internal key: `hero_warden`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 805 |
| Health regeneration | 2/s |
| Move speed | 6.3m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **17.34**
- Rounds/s: **3.8095**; magazine: **17**; reload: **2.914s**
- Projectile speed: **290m/s**; falloff: **18–47m**
- Source DPS: **66.057**; sustained: **39.962**

## Abilities

### 1. Alchemical Flask

Internal key: `ability_warden_crowd_control`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a flask that damages and reduces the weapon damage and move speed of enemies it hits.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Hit enemies lose 1 Stamina
- **Tier 2:** +35 Damage and -25% Weapon Damage
- **Tier 3:** -7s Cooldown and +2m Radius Applies -30% Fire Rate

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 60 (+0.63 per spirit) |
| Move Speed | 20 |
| Weapon Damage | -25 |
| Slow Duration | 3 (+1 per duration) |
| Debuff Duration | 7 (+1 per duration) |
| Stamina Reduction | 0 |
| Cooldown | 12 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"StaminaReduction":1}`
- Tier 2: `{"Damage":35,"WeaponPowerDebuff":-25}`
- Tier 3: `{"FireRateSlow":30,"AbilityCooldown":-7,"Radius":2}`

### 2. Willpower

Internal key: `ability_warden_high_alert`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Gain a Barrier and bonus move speed.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -24s Cooldown and +2s Duration
- **Tier 3:** +40% Debuff Resistance and improved Barrier scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

| Card field | Base value |
| --- | ---: |
| Barrier | 125 (+0.8 per spirit) |
| Move Speed bonus | 15 |
| Debuff Resist | 0 |
| Cooldown | 40 (+1 per cooldown) |
| Duration | 5 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MoveSpeedBonusPct":20}`
- Tier 2: `{"AbilityCooldown":-24,"AbilityDuration":2}`
- Tier 3: `{"StatusResistancePercent":40,"CombatBarrier":{"Value":0,"Scale":{"Value":2.7,"Type":"spirit"}}}`

### 3. Binding Word

Internal key: `ability_warden_lock_down`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Curse an enemy hero. If they don't move away from their initial position within the escape time, they will be damaged and immobilized.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Warden deals +20% more Bullet Damage to trapped Heroes for 5s
- **Tier 2:** +0.75s Duration
- **Tier 3:** -14s Cooldown Silences enemies until they escape or are immobilized

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 110 (+2.43734 per spirit) |
| Immobilize Duration | 1.75 (+1 per duration) |
| Escape Time | 2.8 |
| Escape Range | 20 (+1 per range) |
| Cooldown | 34 (+1 per cooldown) |
| Cast Range | 15 (+1 per range) |

Upgrade deltas:
- Tier 1: `{"BulletArmorReduction":20,"BulletArmorReductionDuration":5}`
- Tier 2: `{"ImmobilizeDuration":0.75}`
- Tier 3: `{"AbilityCooldown":-14,"SilenceDebuff":1}`

### 4. Last Stand

Internal key: `ability_warden_riot_protocol`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> After charging for 2s, release pulses that damage enemies and heal you based on the damage done.
> While channeling Last Stand you have greatly increased bullet and spirit resist.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +40.5 DPS -30s Cooldown
- **Tier 3:** +4s Duration Unstoppable and +30% Resists while channeling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorExclusiveUse`, `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| DPS | 70 (+1.3 per spirit) |
| Hero Lifesteal | 75 (+1 per healing) |
| Move Speed | 0 |
| Pulse Interval | 0.5 |
| Non-Hero Lifesteal | 10 (+1 per healing) |
| Bullet Resist | 50 |
| Spirit Resist | 50 |
| Cooldown | 180 (+1 per cooldown) |
| Duration | 6 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Radius":4}`
- Tier 2: `{"PulseDPS":40.5,"AbilityCooldown":-30}`
- Tier 3: `{"AbilityDuration":4,"UnstoppableCastDelay":1,"BulletResist":30,"TechResist":30}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Warden](https://deadlock.wiki/Warden?oldid=124932) article and generated data revisions. No wiki media is included.
