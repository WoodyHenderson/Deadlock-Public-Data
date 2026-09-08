---
id: hero.mcginnis
title: McGinnis
domain: heroes
topics: [hero]
aliases: []
summary: McGinnis is a selectable Mystic hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.mcginnis.125561
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# McGinnis

McGinnis is a currently selectable **Mystic** hero. Internal key: `hero_forge`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 2/s |
| Move speed | 6.7m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 2 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **6.08**
- Rounds/s: **4.7619**; magazine: **66**; reload: **3.29s**
- Projectile speed: **650m/s**; falloff: **19.99–57.51m**
- Source DPS: **72.381**; sustained: **45.424**

## Abilities

### 1. Mini Turret

Internal key: `citadel_ability_shieldedsentry`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Deploy a turret that shoots enemies, dealing spirit damage over time. The turret expires after a limited lifetime.
> Turrets deal reduced damage to troopers and objectives.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +10 Turret DPS and +10m Attack Range
- **Tier 3:** +25% Turret Fire Rate and +12s Turret Lifetime

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorPreventTrainingBotUsage`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Turret DPS | 24 (+0.42 per spirit) |
| Turret Health | 100 (+9 per power increase) |
| Attack Range | 30 (+1 per range) |
| Lifetime | 35 (+1 per duration) |
| Cooldown | 18 (+1 per cooldown) |
| Cast Range | 20 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 3 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"TurretAttackRange":10,"TurretDPS":10}`
- Tier 2: `{"AbilityCharges":2}`
- Tier 3: `{"AttackSpeedMult":25,"TurretLifetime":12}`

### 2. Medicinal Specter

Internal key: `citadel_ability_mobile_resupply`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Deploy a spirit that provides healing to nearby allies.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +1.5s Duration
- **Tier 2:** -20s Cooldown and provides +100% Stamina Recovery
- **Tier 3:** +2% Max HP Regen +3m Heal Radius +40% Spirit Resist

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorCanHealPlayers`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Health Regen | 25 (+0.3 per spirit) |
| Heal Radius | 6 (+1 per radius) |
| Unknown(AuraFireRateBonus) | 0 |
| Stamina Recovery | 0 |
| Max Health Regen | 0 |
| Cooldown | 50 (+1 per cooldown) |
| Duration | 6.5 (+1 per duration) |
| Cast Range | 15 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityDuration":1.5}`
- Tier 2: `{"AbilityCooldown":-20,"StaminaCooldownReduction":100}`
- Tier 3: `{"MaxHealthRegenPct":2,"HealRadius":3,"SpiritResist":40}`

### 3. Spectral Wall

Internal key: `citadel_ability_fissure_wall`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Cast a wall that applies slow on enemies it passes through. Erupt the wall to divide the terrain in half and damage nearby enemies.
> After casting, press [Attack] or [Ability 3] to erupt the wall early.
> Can be Destroyed with Melee Attacks

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Amplifies McGinnis's damage by +20% on hit enemies for 7s
- **Tier 2:** -20s Cooldown and +2s Duration
- **Tier 3:** Deploy 2 Mini Turrets near the wall for 8s +30% Slow

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorPreventBotUsage`.

| Card field | Base value |
| --- | ---: |
| Damage | 60 (+0.731203 per spirit) |
| Move Speed | 20 |
| Stun Duration | 0 |
| Minimum Range | 5 |
| Impact Range | 5 |
| Slow Duration | 2.5 (+1 per duration) |
| Debuff Duration | 0 |
| Cooldown | 50 (+1 per cooldown) |
| Duration | 6 (+1 per duration) |
| Cast Range | 50 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusDamagePercent":20,"DebuffDuration":7}`
- Tier 2: `{"AbilityCooldown":-20,"AbilityDuration":2}`
- Tier 3: `{"CreateTurrets":2,"TurretLifeTime":8,"SlowPercent":30}`

### 4. Heavy Barrage

Internal key: `citadel_ability_rocket_barrage`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Unleashes a volley of rockets that home in on a targeted location.
> McGinnis is slowed and is still able to use stamina.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Applies 30% movement and dash slow for 1s
- **Tier 2:** -45s Cooldown and +6s Duration
- **Tier 3:** +2m Radius and +15 Damage per Rocket with increased spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorExclusiveUse`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCleaveDisabled`, `BehaviorDeactivateCrouchToggleOnCast`, `BehaviorCanSetQuickCast`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorDontSwitchAwayOnCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Rocket | 21 (+0.2 per spirit) |
| Rockets per second | 6 |
| Explosion Radius | 4.5 (+1 per radius) |
| Min Range | 8.5 |
| Duration | 8 (+1 per duration) |
| Cooldown | 200 (+1 per cooldown) |
| Cast Range | 36 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MoveSlowPercent":30,"EnemyDashSlowPercent":-18,"MoveSlowDuration":1}`
- Tier 2: `{"AbilityCooldown":-45,"AbilityDuration":6}`
- Tier 3: `{"DamagePerRocket":{"Value":15,"Scale":{"Value":0.16,"Type":"spirit"}},"ExplosionRadius":2}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [McGinnis](https://deadlock.wiki/McGinnis?oldid=125561) article and generated data revisions. No wiki media is included.
