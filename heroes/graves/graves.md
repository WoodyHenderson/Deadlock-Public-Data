---
id: hero.graves
title: Graves
domain: heroes
topics: [hero]
aliases: []
summary: Graves is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.graves.124944
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Graves

Graves is a currently selectable **Marksman** hero. Internal key: `hero_necro`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 1/s |
| Move speed | 7m/s |
| Sprint bonus | 2.2m/s |
| Stamina | 2 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **3.6**
- Rounds/s: **9.8039**; magazine: **40**; reload: **2.8s**
- Projectile speed: **635m/s**; falloff: **7.62–17.02m**
- Source DPS: **35.294**; sustained: **20.93**

## Abilities

### 1. Jar of Dead

Internal key: `ability_necro_hauntingskull`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Passive: Collect death when anything dies nearby and store it in your Jar of Dead.
> Active: Throw a jar to summon Deadheads that repeatedly deal spirit damage to enemies.
> Deadheads follow you instead if there's no nearby enemies, and prioritize the target of your weapon.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Collecting death heals 5 health per pickup
- **Tier 2:** On Hit: Apply 30% Slow for 1s
- **Tier 3:** +2 Deadheads +4s Deadhead Lifetime

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Deadheads | 4 |
| Damage | 16 (+0.25 per spirit) |
| Search Range | 7 (+1 per range) |
| Dash Range | 15 (+1 per range) |
| Move Speed | 0 |
| Slow Duration | 0 |
| Heal On Pickup | 0 (+0 per spirit) |
| Charges | 4 (+1 per max charges) |
| Charge Delay | 13 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"HealPerPickup":{"Value":5,"Scale":{"Value":0.16,"Type":"spirit"}}}`
- Tier 2: `{"SlowPercent":30,"SlowDuration":1}`
- Tier 3: `{"SkullCount":2,"SkullLifetime":4}`

### 2. Grasping Hands

Internal key: `ability_necro_zombiewall`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Unearth a line of grasping hands, summoning a Ghoul and leaving behind a rift. Enemies who pass through take spirit damage and receive immobilize.
> Alt-Cast [Alt Cast] rotates the orientation of the wall.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +90 Damage and +10m Wall Length
- **Tier 3:** +1 Ghouls Raised -14s Cooldown +0.75s Immobilize Duration

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorAllowAltCast`, `BehaviorCanSetQuickCast`, `BehaviorSuppressAltCastOnceSelected`.

| Card field | Base value |
| --- | ---: |
| Gangsters Summoned | 1 |
| Damage | 90 (+1.6 per spirit) |
| Max Health Damage | 0 |
| Immobilize Duration | 1 (+1 per duration) |
| Cooldown | 34 (+1 per cooldown) |
| Duration | 5 (+1 per duration) |
| Cast Range | 24 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityDuration":2}`
- Tier 2: `{"Damage":90,"ZombieWallLength":10}`
- Tier 3: `{"ImmobilizeDuration":0.75,"SummonCount":1,"AbilityCooldown":-14}`

### 3. Essence Theft

Internal key: `ability_necro_fear`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Your weapon steals weapon damage and spirit resist over time, up to a maximum amount per target.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +1 Max Steal Targets All Summons now apply Essence Theft

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

| Card field | Base value |
| --- | ---: |
| Max Weapon Damage Stolen | 25 (+0.25 per spirit) |
| Max Spirit Resist Stolen | 10 |
| Max Fire Rate Stolen | 0 |
| Max Steal Targets | 3 |
| Time for Max Damage | 4 |
| Duration | 4 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MaxStolenSpiritResist":5}`
- Tier 2: `{"MaxStolenAttackDamage":20}`
- Tier 3: `{"SkullBuildUp":0.15,"ZombieMeleeBuildUp":0.15,"ZombieExplosionBuildUp":1,"MaxStolenTargets":1}`

### 4. Borrowed Decree

Internal key: `ability_necro_gravestone`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Innate: Abilities can summon Ghouls that shamble toward the enemy base, dealing melee damage. They explode when they approach a hero or objective, dealing spirit damage in an area and applying a brief slow

> Active: Create a gravestone at a target location that summons Ghouls over time. Enemies can destroy the gravestone with two heavy melees.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +25% Ghoul Speed -15s Cooldown
- **Tier 2:** +10s Duration -0.3s Time To Spawn
- **Tier 3:** On Death: Deal +5% Current Health as Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorCooldownOnChannelEnd`, `BehaviorCanSetQuickCast`, `BehaviorRefundFullCooldownOnChannelInterrupt`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Cooldown | 140 (+1 per cooldown) |
| Duration | 16 |
| Cast Range | 20 (+1 per range) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-15,"MoveSpeedPercent":25}`
- Tier 2: `{"AbilityDuration":10,"SummonFrequency":-0.3}`
- Tier 3: `{"CurrentHealthDamagePercentage":5}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Graves](https://deadlock.wiki/Graves?oldid=124944) article and generated data revisions. No wiki media is included.
