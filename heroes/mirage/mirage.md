---
id: hero.mirage
title: Mirage
domain: heroes
topics: [hero]
aliases: []
summary: Mirage is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.mirage.125560
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Mirage

Mirage is a currently selectable **Assassin** hero. Internal key: `hero_mirage`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 1.5/s |
| Move speed | 7m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **14.8**
- Rounds/s: **2.7211**; magazine: **16**; reload: **2.6s**
- Projectile speed: **828m/s**; falloff: **19.99–57.51m**
- Source DPS: **40.272**; sustained: **27.925**

## Abilities

### 1. Fire Scarabs

Internal key: `mirage_fire_beetles`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Infest an enemy with fire scarabs, stealing life from them and causing them to deal reduced damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +1 Charge +2s Duration

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 8 (+0.1 per spirit) |
| Damage Penalty | -20 |
| Steal Duration | 5 (+1 per duration) |
| Cooldown | 35 (+1 per cooldown) |
| Charges | 2 (+1 per max charges) |
| Charge Delay | 1 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"DPS":7}`
- Tier 2: `{"AbilityCharges":1,"StealDuration":2}`
- Tier 3: `{"OutgoingDamagePenaltyPercent":-15,"DPS":{"Value":0,"Scale":{"Value":0.13,"Type":"spirit"}}}`

### 2. Dust Devil

Internal key: `mirage_tornado`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Transform yourself into a whirlwind that travels forward, damaging enemies, slowing their move speed and lifting them up in the air. After emerging from the tornado you gain bullet evasion.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +60 Damage
- **Tier 2:** -12s Cooldown +30% Evasion
- **Tier 3:** Recast within 6s. Increases spirit scaling.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDontInterruptSprint`, `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorMovement`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 65 (+0.3 per spirit) |
| Lift Duration | 0.3 (+1 per duration) |
| Bullet Evasion Chance | 30 |
| Radius | 4 (+1 per radius) |
| Bullet Evasion Duration | 4 (+1 per duration) |
| Move Speed | 30 |
| Slow Duration | 3 (+1 per duration) |
| Cooldown | 36 (+1 per cooldown) |
| Cast Range | 20 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":60}`
- Tier 2: `{"AbilityCooldown":-12,"WhirlwindEvasionChance":30}`
- Tier 3: `{"RecastWindow":6,"Damage":{"Value":0,"Scale":{"Value":0.6,"Type":"spirit"}}}`

### 3. Djinn's Mark

Internal key: `mirage_sand_phantom`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Active: Consume all Djinn Mark's to deal its damage now.

> Passive: Your shots apply a Djinn Mark on the target. When the mark expires or is consumed, it deals spirit damage and the target is briefly revealed on the map. Each added mark doubles the current damage.
> There is a per target Cooldown for applying additional marks

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Proc: Apply a fading 60% Slow for 0.8s
- **Tier 2:** +20 Base Damage and +3s Multiplier Duration
- **Tier 3:** -0.75s Cooldown +1 Max Marks Stun Victim for 0.5s on Max Marks

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDontInterruptSprint`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCanCastOnZipline`, `BehaviorDoNotAllowSpamProc`.

| Card field | Base value |
| --- | ---: |
| Base Damage | 11 (+0.35 per spirit) |
| Damage Per Mark | 2 |
| Max Stacks | 4 |
| Max Frequency | 2.75 (+1 per cooldown) |
| Djinn's Mark Duration | 5 (+1 per duration) |
| Reveal Duration | 6 (+1 per duration) |
| Proc Max Range | 40 |
| Stun Duration | 0 |
| Cooldown | 2.75 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MovementSpeedSlow":60,"SlowDuration":0.8}`
- Tier 2: `{"ProcDamageBase":20,"VictimStackDuration":3}`
- Tier 3: `{"AbilityCooldown":-0.75,"ProcCooldown":-0.75,"StunDuration":0.5,"MaxStacks":1}`

### 4. Traveler

Internal key: `mirage_teleport`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Target a location on the minimap. After a brief wait, teleport to that location. Taking damage during the wait period causes the teleport to be interrupted.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +3m Move Speed and +20% Fire Rate for 12s
- **Tier 2:** 400 Barrier that scales with Spirit

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCanCastOnZipline`, `BehaviorCastableWhileBusy`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorCanCancelDuringCastDelay`.

| Card field | Base value |
| --- | ---: |
| Wait Time | 2 |
| Fire Rate | 0 |
| Move Speed | 0 |
| Barrier | 0 (+0 per spirit) |
| Move Speed Duration | 0 |
| Interrupt Cooldown | 4 |
| Cooldown | 140 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":3,"BonusFireRate":20,"MovementSpeedBonusDuration":12}`
- Tier 2: `{"CombatBarrier":{"Value":400,"Scale":{"Value":0.6,"Type":"spirit"}}}`
- Tier 3: `{"AbilityCooldown":-90}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Mirage](https://deadlock.wiki/Mirage?oldid=125560) article and generated data revisions. No wiki media is included.
