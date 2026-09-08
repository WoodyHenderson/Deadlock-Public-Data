---
id: hero.silver
title: Silver
domain: heroes
topics: [hero]
aliases: []
summary: Silver is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.silver.124941
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Silver

Silver is a currently selectable **Marksman** hero. Internal key: `hero_werewolf`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 830 |
| Health regeneration | 2.5/s |
| Move speed | 6.7m/s |
| Sprint bonus | 1.5m/s |
| Stamina | 2 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **5.1**
- Rounds/s: **1.1765**; magazine: **7**; reload: **0.3s**
- Projectile speed: **812.8m/s**; falloff: **17–42m**
- Source DPS: **42.001**; sustained: **29.229**

## Abilities

### 1. Slam Fire

Internal key: `ability_werewolf_unloadgun`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Instantly reload your gun. You gain bonus fire rate and deal bonus weapon damage based on the target's health for a limited number of shots, but suffer from reduced accuracy.
> Deals bonus Weapon Damage against troopers and neutrals.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** If you hit all shots, deal +7% current health as damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Max Shots | 3 |
| Fire Rate | 300 |
| Current Health as Damage | 2.5 |
| Weapon Accuracy | -30 |
| Weapon Damage | 0 |
| Bonus Current Health as Damage | 0 |
| Weapon Damage vs. NPCs | 100 |
| Cooldown | 25 (+1 per cooldown) |
| Duration | 5 (+1 per duration) |
| Cast Range | 0.0254 (+0 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BaseAttackDamagePercent":15}`
- Tier 2: `{"AbilityCooldown":-10}`
- Tier 3: `{"StackDuration":3,"MaxStacks":3,"BonusCurrentHealthDamagePercentage":7}`

### 2. Boot Kick

Internal key: `ability_werewolf_kickflip`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Dash forward and kick the first enemy hit, dealing melee damage while pushing yourself off and marking them.

> Shooting the marked target deals spirit damage and removes the mark.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** On Hero Hit: Restore 2 Stamina
- **Tier 3:** +80 Bonus Damage and kicked enemies deal -35% Damage for 5s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorDontTriggerPostCastOnCastComplete`, `BehaviorMovement`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 0 (+0.9 per melee) |
| Disarm Duration | 0 |
| Debuff Duration | 0 |
| Cooldown | 21 (+1 per cooldown) |
| Cast Range | 10.6 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-6}`
- Tier 2: `{"StaminaRestore":2}`
- Tier 3: `{"OutgoingDamagePercent":-35,"DebuffDuration":5,"BonusDamage":80}`

### 3. Entangling Bola

Internal key: `ability_werewolf_netshot`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a bola, dealing spirit damage, applying slow and preventing movement abilities or stamina.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +0.75s Debuff Duration. Bola ricochets to 2 additional targets

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 40 (+1.6 per spirit) |
| Move Speed | 20 |
| Debuff Duration | 1.5 (+1 per duration) |
| Cooldown | 23 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"SlowPercent":25}`
- Tier 2: `{"AbilityCooldown":-8}`
- Tier 3: `{"RicochetCount":2,"RicochetRange":15,"DebuffDuration":0.75}`

### 4. Lycan Curse

Internal key: `ability_werewolf_transformation`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Passive: Dealing damage generates bloodlust, increased at low health. At max bloodlust, you automatically cast Lycan Curse.
> Active: Instantly transform, gaining increased max health, and stacking fire rate on enemy heroes, and replacing your abilities and weapon with their ferocious versions.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +15% Bullet & Spirit Resistance
- **Tier 2:** +4 m/s Move Speed and 200 Bonus Health
- **Tier 3:** On Hero Kill: Refresh abilities and duration

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Bonus Health | 125 (+15 per power increase) |
| Move Speed | 1.5 |
| Sprint Speed | 0 |
| Fire Rate | 60 (+0.45 per spirit) |
| Bullet Resist | 0 |
| Spirit Resist | 0 |
| Missing Health as Healing | 30 (+1 per healing) |
| Kill Duration Bonus | 0 |
| Heal Amount | 0 (+1 per power increase) |
| Stamina | 0 |
| Cooldown | 60 (+1 per cooldown) |
| Duration | 15 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BulletResist":15,"TechResist":15}`
- Tier 2: `{"BonusMoveSpeed":4,"BonusHealth":200}`
- Tier 3: `{"KillDurationBonus":15,"KillCreditWindow":1.5}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Silver](https://deadlock.wiki/Silver?oldid=124941) article and generated data revisions. No wiki media is included.
