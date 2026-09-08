---
id: hero.drifter
title: Drifter
domain: heroes
topics: [hero]
aliases: []
summary: Drifter is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.drifter.125577
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Drifter

Drifter is a currently selectable **Assassin** hero. Internal key: `hero_drifter`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 755 |
| Health regeneration | 3.5/s |
| Move speed | 6.9m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 51.5 / 120 |

## Weapon

- Bullet damage: **19.5**
- Rounds/s: **2.2676**; magazine: **12**; reload: **2.444s**
- Projectile speed: **508m/s**; falloff: **22–27m**
- Source DPS: **44.218**; sustained: **30.248**

## Abilities

### 1. Rend

Internal key: `drifter_blood_blast`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Swipe at enemies in a cone ahead of you, dealing spirit damage. If the enemy is in close range, deal bonus melee damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -8s Cooldown
- **Tier 3:** Deals 55% Heavy Melee Damage Silences enemies for 2s if close range

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorNoTarget`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Bonus Damage | 40 (+1.4 per spirit) |
| Damage | 0 (+1.2 per melee) |
| Damage | 0 (+0 per heavy melee) |
| Bullet Lifesteal | 0 |
| Debuff Duration | 0 |
| Close Range | 8 (+1 per range) |
| Lifesteal Duration | 0 |
| Cooldown | 16 (+1 per cooldown) |
| Cast Range | 16 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusDamage":40}`
- Tier 2: `{"AbilityCooldown":-8}`
- Tier 3: `{"DebuffDuration":2,"UseHeavyMelee":1,"DamageHeavyMelee":{"Value":0,"Scale":{"Value":0.55,"Type":"heavy_melee"}},"Damage":{"Value":0,"Scale":{"Value":0,"Type":"melee","Multiply":true}}}`

### 2. Stalker's Mark

Internal key: `drifter_shadow_mark`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Send out a mark that bleeds the first target it hits, dealing spirit damage over time.
> While the enemy is bleeding you can re-activate Stalker's Mark to instantly appear behind their back.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -8% Bullet Resist
- **Tier 2:** -10s Cooldown and +3s Duration
- **Tier 3:** +1.5% Bleed and -40% Healing Reduction

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCleaveDisabled`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Bleed Damage | 2 (+0.015 per spirit) |
| Duration | 5 (+1 per duration) |
| Healing Reduction | 0 |
| Charges | 0 |
| Bullet Resist | 0 |
| Charge Delay | -1 |
| Cooldown | 26 (+1 per cooldown) |

Upgrade deltas:
- Tier 1: `{"BulletResistReduction":-8}`
- Tier 2: `{"AbilityDuration":3,"AbilityCooldown":-10}`
- Tier 3: `{"DotHealthPercent":1.5,"HealAmpReceivePenaltyPercent":-40,"HealAmpRegenPenaltyPercent":-40}`

### 3. Bloodscent

Internal key: `ability_drifter_hunger`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> When enemy heroes are low on health you deal amplified damage against them. These enemies leave a lingering blood trail as they move.

> Isolated heroes leave a trail as they move, and emit their heartbeat from afar.
> You deal amplified damage against isolated heroes, and when isolated heroes die nearby you gain permanent weapon damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +3m/s Move Speed when around an isolated enemy hero
- **Tier 2:** On isolated hero death: Heal 24% of your missing health and restores 2 Stamina

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

| Card field | Base value |
| --- | ---: |
| Amplified Damage | 15 |
| Isolation Range | 20 |
| Move Speed | 0 |
| Cast Range | 80 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":3}`
- Tier 2: `{"HealOnKillPct":24,"StaminaToRestore":2}`
- Tier 3: `{"AmpDamagePercent":11}`

### 4. Eternal Night

Internal key: `drifter_darkness`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Surround nearby enemy heroes in darkness, severely limiting their vision of other units. Affected enemies are briefly revealed to you and are considered isolated for the duration.
> You gain bonus sprint speed.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +2.5s Duration and +1 Max Targets.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectilePassThroughWorld`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Reduced Vision | 15 |
| Sprint Speed | 2 |
| Max Targets | 2 |
| Cooldown | 145 (+1 per cooldown) |
| Duration | 6.5 (+1 per duration) |
| Cast Range | 100 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusSprintSpeed":10}`
- Tier 2: `{"AbilityCooldown":-40}`
- Tier 3: `{"AbilityDuration":2.5,"MaxTargets":1}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Drifter](https://deadlock.wiki/Drifter?oldid=125577) article and generated data revisions. No wiki media is included.
