---
id: hero.vindicta
title: Vindicta
domain: heroes
topics: [hero]
aliases: []
summary: Vindicta is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.vindicta.124937
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Vindicta

Vindicta is a currently selectable **Marksman** hero. Internal key: `hero_hornet`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 755 |
| Health regeneration | 2/s |
| Move speed | 7.9m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 2 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **12.33**
- Rounds/s: **4.329**; magazine: **19**; reload: **2.914s**
- Projectile speed: **660m/s**; falloff: **19.99–64m**
- Source DPS: **53.377**; sustained: **32.079**

## Abilities

### 1. Stake

Internal key: `citadel_ability_hornet_chain`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a stake that tethers enemies to the location where the stake lands. Enemy movement is restricted to the length of the tether.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +0.75s Tether Duration and +2m Capture Radius

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Tether Duration | 1.75 (+1 per duration) |
| Damage | 40 (+0.5 per spirit) |
| Capture Radius | 9 (+1 per range) |
| Tether Length | 9 |
| Move Speed | 40 |
| Cooldown | 40 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":45}`
- Tier 2: `{"AbilityCooldown":-22}`
- Tier 3: `{"ChainDuration":0.75,"CaptureRadius":2}`

### 2. Flight

Internal key: `citadel_ability_hornet_leap`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Leap into the air and fly. While in flight your weapon deals bonus spirit damage and your items have increased range.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +50% base Ammo while flying
- **Tier 3:** Hero Kills Refresh Duration. +10 Spirit Damage with increased Spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorMovement`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Spirit Damage Per Bullet | 10 (+0.18 per spirit) |
| Item Range | 50 |
| Cooldown | 42 (+1 per cooldown) |
| Duration | 13 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusClipSizePercent":50}`
- Tier 2: `{"AbilityDuration":10}`
- Tier 3: `{"MagicDamagePerBullet":{"Value":10,"Scale":{"Value":0.1,"Type":"spirit"}},"RefreshOnKill":1}`

### 3. Crow Familiar

Internal key: `citadel_ability_hornet_sting`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Your crow familiar deals impact damage, reduces their bullet resist and applies a bleed that deals damage based on the target's current health.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Applies -35% Healing Reduction
- **Tier 2:** +0.5% Bleed Damage -16s Cooldown
- **Tier 3:** +2s Duration -8% Bullet Resist -8% Spirit Resist

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCleaveDisabled`, `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Impact Damage | 40 (+0.744 per spirit) |
| Bleed Damage | 2.2 |
| Debuff Duration | 5 (+1 per duration) |
| Healing Reduction | 0 |
| Bullet Resist | -6 |
| Cooldown | 32 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"HealAmpReceivePenaltyPercent":-35,"HealAmpRegenPenaltyPercent":-35}`
- Tier 2: `{"AbilityCooldown":-16,"DotHealthPercent":0.5}`
- Tier 3: `{"BulletResistReduction":-8,"TechArmorDamageReduction":-8,"DebuffDuration":2}`

### 4. Assassinate

Internal key: `citadel_ability_hornet_snipe`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Use your scoped rifle to fire a powerful shot over long distances. Deal only partial damage until fully charged after 1s of being scoped. Does bonus damage to enemies with less than 50% health remaining. Landing a killing blow on a player with Assassinate grants you bonus weapon damage.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Damage | 90 (+0.93 per spirit) |
| Max Bonus Damage | 90 (+2.3 per spirit) |
| Weapon Damage Per Kill | 6 |
| Full Charge Time | 1 |
| No Charge Damage | 50 |
| Headshot Damage | 20 |
| Cooldown | 55 (+1 per cooldown) |
| Charges | 2 (+1 per max charges) |
| Charge Delay | 2.5 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-15}`
- Tier 2: `{"LowHealthEnemyDamageBonus":80}`
- Tier 3: `{"WeaponDamageBonusPerKill":4}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Vindicta](https://deadlock.wiki/Vindicta?oldid=124937) article and generated data revisions. No wiki media is included.
