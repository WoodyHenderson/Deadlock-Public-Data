---
id: hero.bebop
title: Bebop
domain: heroes
topics: [hero]
aliases: []
summary: Bebop is a selectable Brawler hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.bebop.124925
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Bebop

Bebop is a currently selectable **Brawler** hero. Internal key: `hero_bebop`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 880 |
| Health regeneration | 2.5/s |
| Move speed | 6.45m/s |
| Sprint bonus | 4m/s |
| Stamina | 3 |
| Light / heavy melee | 63 / 116 |

## Weapon

- Bullet damage: **4.98**
- Rounds/s: **11.905**; magazine: **66**; reload: **2.35s**
- Projectile speed: **508m/s**; falloff: **19.99–50.8m**
- Source DPS: **59.287**; sustained: **41.637**

## Abilities

### 1. Exploding Uppercut

Internal key: `citadel_ability_uppercut`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Deal melee damage to nearby enemies and apply knockback.
> When they land, they deal spirit damage and apply reduced fire rate to other nearby enemies.
> Exploding Uppercut can be used on allies.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** On Hero Hit: Gain fast spin-up time, 2x weapon range and +30% weapon damage for 9s
- **Tier 3:** On Hero Hit: Set Grapple Arm cooldown to 0 and restores +18% of your missing health

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Uppercut Damage | 0.01 (+1 per melee) |
| Missing HP Heal | 0 |
| Duration | 0.5 |
| Cooldown | 22 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-11}`
- Tier 2: `{"UppercutBuffOnHit":9,"BuffBaseWeaponPct":30}`
- Tier 3: `{"RestoreHookCooldown":1,"MissingHPHeal":18}`

### 2. Sticky Bomb

Internal key: `citadel_ability_sticky_bomb`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Attach a bomb that explodes after a delay, dealing spirit damage to nearby enemies.
> If the bomb hits or kills a hero, you gain permanent bonus damage on Sticky Bomb.
> Stacks diminish by half after 60 hits and 7 kills

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** On Cast: +5m Move Speed and +25% Debuff Resistance for 6s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAllowSelfCast`, `BehaviorDisplaysDamageImpact`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Fuse Time | 3.5 |
| Damage | 85 (+1.5 per spirit) |
| Cooldown | 18 (+1 per cooldown) |
| Duration | 3.5 (+1 per duration) |
| Cast Range | 6 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-8}`
- Tier 2: `{"Damage":85}`
- Tier 3: `{"MovementSpeedBonus":5,"StatusResistancePercent":25,"MovementSpeedBonusDuration":6}`

### 3. Grapple Arm

Internal key: `citadel_ability_hook`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Launch out a mechanical hand that pulls the first character it hits, reeling them in.
> Grapple Arm can be used on allies.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +20% weapon damage against victims for 6s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorPreventBotUsage`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Cast Range | 30 (+1 per range) |
| Damage | 0 (+0.7 per melee) |
| Cooldown | 23 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BulletAmp":20,"BulletAmpDuration":6}`
- Tier 2: `{"AbilityCastRange":30}`
- Tier 3: `{"AbilityCooldown":-11.5}`

### 4. Hyper Beam

Internal key: `citadel_ability_bebop_laser_beam`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Channel a powerful torrent of energy that deals spirit damage and applies slow.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** Hyper Beam heals Bebop for 65% of its damage on Heroes. 20% on non-hero

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 160 (+2.511 per spirit) |
| Move Speed | 25 |
| Beam Length | 70 (+1 per range) |
| Beam Width | 2.9 |
| Cooldown | 120 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20}`
- Tier 2: `{"DPS":108}`
- Tier 3: `{"BeamLifesteal":65,"BeamLifestealNonHeroPercent":20}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Bebop](https://deadlock.wiki/Bebop?oldid=124925) article and generated data revisions. No wiki media is included.
