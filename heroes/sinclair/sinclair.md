---
id: hero.sinclair
title: Sinclair
domain: heroes
topics: [hero]
aliases: []
summary: Sinclair is a selectable Mystic hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.sinclair.124939
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Sinclair

Sinclair is a currently selectable **Mystic** hero. Internal key: `hero_magician`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 2/s |
| Move speed | 7.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **17.76**
- Rounds/s: **2.7211**; magazine: **16**; reload: **2.5s**
- Projectile speed: **300m/s**; falloff: **25.4–60.96m**
- Source DPS: **48.327**; sustained: **33.909**

## Abilities

### 1. Vexing Bolt

Internal key: `ability_magician_magicbolt`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Fire a bolt of magic that deals Damage, increasing as it travels. If you have an Assistant, they also cast Vexing Bolt at reduced damage.
> Press [Ability 1] to redirect the bolt towards your crosshairs.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Bolts apply -25% Fire Rate for 5s.
- **Tier 3:** +126 Max Damage. +50% Assistant Damage.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorTargetThroughWalls`, `BehaviorCleaveDisabled`, `BehaviorCooldownOnChannelEnd`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Minimum Damage | 60 (+0.93 per spirit) |
| Max Damage | 120 (+1.86 per spirit) |
| Assistant Damage | 50 |
| Time for Max Damage | 2 |
| Fire Rate | 0 |
| Debuff Duration | 0 |
| Cooldown | 24 (+1 per cooldown) |
| Cast Range | 500 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 3 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"FireRateSlow":25,"DebuffDuration":5}`
- Tier 2: `{"AbilityCooldown":-13}`
- Tier 3: `{"MaxDamage":126,"CloneDamagePercentage":50}`

### 2. Spectral Assistant

Internal key: `ability_magician_cloneturret`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Summon an Assistant at the targeted location. The Assistant attacks whenever you fire your weapon, dealing Damage.
> While the Assistant is out, you can press [Ability 2] to swap positions with your Assistant.
> Casting Spectral Assistant also reloads your weapon.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +7s Duration & 5m Range
- **Tier 3:** +60% Fire Rate and +12.6 Assistant Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorPreventBotUsage`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 15 (+0.36 per spirit) |
| Duration | 6 (+1 per duration) |
| Max Swaps | 2 |
| Cooldown | 40 (+1 per cooldown) |
| Cast Range | 15 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-10}`
- Tier 2: `{"AbilityDuration":7,"AbilityCastRange":5,"LeashRadius":5}`
- Tier 3: `{"BonusFireRate":60,"Damage":12.6}`

### 3. Rabbit Hex

Internal key: `ability_magician_animalhexarea`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Hex a target area and transforming all enemies into a Rabbit for a limited duration.
> Rabbits are small and move faster, but take increased Damage and are unable to perform most actions.
> Hex does not interrupt abilities.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +7% Damage Amp and +3m Radius

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 0 |
| Hex Duration | 2 (+1 per duration) |
| Damage Amp | 15 (+0.0558 per spirit) |
| Move Speed bonus | 36 |
| Radius | 6.5 (+1 per range) |
| Cooldown | 26 (+1 per cooldown) |
| Cast Range | 24 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-10}`
- Tier 2: `{"HexDuration":1}`
- Tier 3: `{"Radius":3,"DamageAmpPercentage":7}`

### 4. Audience Participation

Internal key: `ability_magician_copyult`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Copy the Ultimate of an enemy hero for a limited time. Reactivating the ability will use the Copied Ultimate instead.
> Copies will inherit this ability's upgrade points.
> Audience Participation will also copy the cooldown.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Upgrade the Copy.
- **Tier 2:** Upgrade the Copy AGAIN!
- **Tier 3:** Upgrade the Copy ONCE AGAIN!

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Copy Duration | 12 (+1 per duration) |
| Copied Cooldown | 40 |
| Cooldown | 85 (+1 per cooldown) |
| Cast Range | 20 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{}`
- Tier 2: `{}`
- Tier 3: `{}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Sinclair](https://deadlock.wiki/Sinclair?oldid=124939) article and generated data revisions. No wiki media is included.
