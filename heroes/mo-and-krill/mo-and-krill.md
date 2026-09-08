---
id: hero.mo-and-krill
title: Mo & Krill
domain: heroes
topics: [hero]
aliases: []
summary: Mo & Krill is a selectable Brawler hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.mo-and-krill.125559
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Mo & Krill

Mo & Krill is a currently selectable **Brawler** hero. Internal key: `hero_krill`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 930 |
| Health regeneration | 1/s |
| Move speed | 8m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **2.82**
- Rounds/s: **5.291**; magazine: **20**; reload: **2.82s**
- Projectile speed: **320m/s**; falloff: **19.99–57.51m**
- Source DPS: **59.682**; sustained: **34.182**

## Abilities

### 1. Scorn

Internal key: `ability_intimidate`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Deal damage to nearby enemies and heal yourself based on the damage done. Heal is stronger against enemy heroes.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -5s Cooldown +1m Radius
- **Tier 3:** Adds a debuff to enemies that lets Mo & Krill deal +15% Damage to them. Stacks and lasts 16s.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCastableWhileBusy`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 50 (+0.75 per spirit) |
| Hero Damage to Heal | 1.2 (+1 per healing) |
| Damage to Heal | 0.35 (+1 per healing) |
| Cooldown | 13 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":35}`
- Tier 2: `{"AbilityCooldown":-5,"Radius":1}`
- Tier 3: `{"DamageBonus":15,"DebuffDuration":16}`

### 2. Burrow

Internal key: `ability_burrow`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Burrow underground, moving faster, and gaining spirit and bullet armor. Damage from enemy heroes will reduce the speed bonus.
> When you jump out, deal spirit damage, slow, and knockup.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +50 Spin DPS
- **Tier 2:** +4s Burrow time and +2 radius
- **Tier 3:** -20 Cooldown and +4m/s Move Speed

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Move Speed | 5 |
| Damage Per Second | 75 (+1.488 per spirit) |
| Spin Duration | 1.5 (+1 per duration) |
| Duration | 1 |
| Bullet Resist | 60 |
| Spirit Resist | 30 |
| Cooldown | 40 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"DPS":50}`
- Tier 2: `{"AbilityChannelTime":4,"Radius":2}`
- Tier 3: `{"AbilityCooldown":-20,"BonusMoveSpeed":4}`

### 3. Sand Blast

Internal key: `ability_throw_sand`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Spray sand that disarms enemies in front of you and deals damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +50 Damage and +5m Range
- **Tier 2:** Slow targets by -30% and reduces dash distances by -30%
- **Tier 3:** +1.5s Duration and -25 Cooldown

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Duration | 2.5 (+1 per duration) |
| Damage | 40 |
| Move Speed | 0 |
| Cooldown | 40 (+1 per cooldown) |
| Cast Range | 25 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":50,"AbilityCastRange":5}`
- Tier 2: `{"SlowPercent":30,"GroundDashReductionPercent":-30}`
- Tier 3: `{"AbilityCooldown":-25,"AbilityDuration":1.5}`

### 4. Combo

Internal key: `ability_ult_combo`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Hold the target in place, stunning them and dealing damage during the channel. If they die during, or within 3 seconds of Combo ending, you permanently gain max health.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +100% lifesteal
- **Tier 2:** -30s Cooldown and +50% Bullet Resist
- **Tier 3:** +0.7s Duration and +40 Damage Per Second and increased scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorDisplaysDamageImpact`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 40 (+0.6 per spirit) |
| Unknown(LifeStealPercentOnHit) | 0 |
| Bonus Max Health Per Kill | 40 (+2 per power increase) |
| Cooldown | 150 (+1 per cooldown) |
| Cast Range | 4 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"LifeStealPercentOnHit":100}`
- Tier 2: `{"AbilityCooldown":-30,"BulletResist":50}`
- Tier 3: `{"AbilityChannelTime":0.7,"DPS":{"Value":40,"Scale":{"Value":0.4,"Type":"spirit"}}}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Mo & Krill](https://deadlock.wiki/Mo_%26_Krill?oldid=125559) article and generated data revisions. No wiki media is included.
