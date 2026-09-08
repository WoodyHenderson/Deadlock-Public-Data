---
id: hero.pocket
title: Pocket
domain: heroes
topics: [hero]
aliases: []
summary: Pocket is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.pocket.125557
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Pocket

Pocket is a currently selectable **Assassin** hero. Internal key: `hero_synth`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 1/s |
| Move speed | 7.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 60 / 116 |

## Weapon

- Bullet damage: **4.28**
- Rounds/s: **1.9048**; magazine: **11**; reload: **2.82s**
- Projectile speed: **558.8m/s**; falloff: **16–45.72m**
- Source DPS: **57.068**; sustained: **38.344**

## Abilities

### 1. Barrage

Internal key: `synth_barrage`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Channel to start launching projectiles that deal spirit damage and apply slow around their impact point. Projectiles that hit a hero grant Pocket increased damage that stacks.
> Casting while airborne will cause Pocket to float.
> Casting AirDash or Flying Cloaking will not cancel Barrage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +4% Amp Per Stack and 3m Radius

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorChannelled`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Amp Per Stack | 6 |
| Damage Per Projectile | 32 (+0.465 per spirit) |
| Movement Slow | 30 |
| Projectile Amount | 4 |
| Slow Duration | 1.5 (+1 per duration) |
| Amp Duration | 15 (+1 per duration) |
| Cooldown | 32 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"DamagePerProjectile":16}`
- Tier 2: `{"AbilityCooldown":-16}`
- Tier 3: `{"AmpPercentPerStack":4,"Radius":3}`

### 2. Flying Cloak

Internal key: `synth_plasma_flux`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Launch a sentient cloak that travels forward and damages enemies. You can press [Ability 2] to teleport to its location.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +5 Weapon Damage for 6s
- **Tier 3:** +1.6s Lifetime and -10s Cooldown.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 60 (+1.3 per spirit) |
| Lifetime | 3.8 (+1 per duration) |
| Cooldown | 25 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":70}`
- Tier 2: `{"WeaponDamageBonus":5,"WeaponDamageBonusDuration":6}`
- Tier 3: `{"MaxLifetime":1.6,"AbilityCooldown":-10}`

### 3. Enchanter's Satchel

Internal key: `synth_pulse`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Escape into your suitcase. When the duration ends, deal spirit damage to nearby enemies. Duration can be ended early by performing any action.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +1.5s Duration +4m Radius -40% Move Speed and Fire Rate for 4s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Channel Duration | 1.5 (+1 per duration) |
| Damage | 65 (+1.1 per spirit) |
| Movement Slow | 0 |
| Fire Rate | 0 |
| Debuff Duration | 0 |
| Cooldown | 17 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-5}`
- Tier 2: `{"Damage":90}`
- Tier 3: `{"FireRateSlow":40,"MoveSlowPercent":40,"DebuffDuration":4,"AbilityChannelTime":1.5,"Radius":4}`

### 4. Affliction

Internal key: `synth_affliction`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Applies damage over time to enemies nearby.
> Affliction's damage is non-lethal and does not apply item procs.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +3s Duration and +4m Radius
- **Tier 3:** Prevents all healing +13 DPS with increase Spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Current Health Damage | 0 (+0 per spirit) |
| Damage Per Second | 32 (+0.21 per spirit) |
| Debuff Duration | 10 (+1 per duration) |
| Healing Reduction | 0 |
| Cooldown | 170 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-35}`
- Tier 2: `{"DebuffDuration":3,"Radius":4}`
- Tier 3: `{"DPS":{"Value":13,"Scale":{"Value":0.1,"Type":"spirit"}},"DisableHealing":1}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Pocket](https://deadlock.wiki/Pocket?oldid=125557) article and generated data revisions. No wiki media is included.
