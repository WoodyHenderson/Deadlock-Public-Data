---
id: hero.grey-talon
title: Grey Talon
domain: heroes
topics: [hero]
aliases: []
summary: Grey Talon is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.grey-talon.125566
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Grey Talon

Grey Talon is a currently selectable **Marksman** hero. Internal key: `hero_orion`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 1.5/s |
| Move speed | 6.3m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 4 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **23.51**
- Rounds/s: **1.6667**; magazine: **17**; reload: **2.35s**
- Projectile speed: **495.3m/s**; falloff: **18–54m**
- Source DPS: **39.184**; sustained: **31.847**

## Abilities

### 1. Charged Shot

Internal key: `ability_charged_shot`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Charge up a powerful shot that pierces through enemies. Hold [Ability 1] or [Attack] to hold the shot.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +54 Damage
- **Tier 3:** Improved damage scaling and -3s Charge Delay

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorChannelled`, `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 80 (+1 per spirit) |
| Cooldown | 17 (+1 per cooldown) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 4 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1}`
- Tier 2: `{"Damage":54}`
- Tier 3: `{"AbilityCooldownBetweenCharge":-3,"Damage":{"Value":0,"Scale":{"Value":1,"Type":"spirit"}}}`

### 2. Rain of Arrows

Internal key: `ability_power_jump`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Launches you high in the air, allowing you to glide slowly. While airborne, you gain Weapon Damage and multishot on your weapon.
> [Alt Cast] for reduced jump height.
> Press [Mantle] to cancel the glide.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** While airborne, +3 Weapon Damage and weapon damage applies 30% movement slow for 1.5s
- **Tier 3:** While airborne, +30% Bullet Lifesteal, +30% Spirit Lifesteal and +30% Bullet Evasion

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorInputDirectional2d`, `BehaviorNoTarget`, `BehaviorAllowAltCast`, `BehaviorMovement`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Weapon Multishot | 5 |
| Weapon Damage | 3 |
| Move Speed | 0 |
| Slow Duration | 0 |
| Bullet Lifesteal | 0 |
| Spirit Lifesteal | 0 |
| Bullet Evasion | 0 |
| Cooldown | 25 (+1 per cooldown) |
| Duration | 4 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"WeaponDamageBonus":3,"SlowPercent":30,"SlowDuration":1.5}`
- Tier 2: `{"AbilityCooldown":-12}`
- Tier 3: `{"BulletLifestealPercent":30,"TechLifestealPercent":30,"EvasionPercent":30}`

### 3. Spirit Snare

Internal key: `ability_immobilize_trap`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw out a trap that begins to arm itself. Once armed, the trap will trigger when an enemy enters its radius, applying Curse and Movement Slow that interrupts, Silences, Disarms, and prevents item usage.
> Hit the trap with a Charged Shot to detonate early with increased radius.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Applies -15% Bullet Resist for 10s
- **Tier 3:** +1s Curse Duration and +1.5m Radius

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorPreventTrainingBotUsage`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Tether Duration | 2.25 (+1 per duration) |
| Damage | 25 |
| Lifetime | 22 (+1 per duration) |
| Arm Time | 2 |
| Move Speed | 30 |
| Charged Shot Radius | 30 |
| Bullet Damage Amp | 0 |
| Debuff Duration | 0 |
| Cooldown | 34 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20}`
- Tier 2: `{"BulletArmorReduction":-15,"DebuffDuration":10}`
- Tier 3: `{"TetherDuration":1,"Radius":1.5}`

### 4. Guided Owl

Internal key: `ability_guided_arrow`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> After 1.5s cast time, launch a spirit owl that you control and which explodes on impact, damaging and stunning enemies. Hold [Move Forward] to accelerate the owl.
> Press [Mantle] to release control. Gain permanent Spirit Power for each enemy hero killed with Guided Owl.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** After hit, kills enemies that are below 22% Health

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 230 (+0.93744 per spirit) |
| Explosion Radius | 12 (+1 per range) |
| Stun Duration | 0.75 (+1 per duration) |
| Spirit Power Per Kill | 8 |
| Cooldown | 125 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":85}`
- Tier 2: `{"AbilityCooldown":-40}`
- Tier 3: `{"LowHealthEnemyThresholdPct":22}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Grey Talon](https://deadlock.wiki/Grey_Talon?oldid=125566) article and generated data revisions. No wiki media is included.
