---
id: hero.wraith
title: Wraith
domain: heroes
topics: [hero]
aliases: []
summary: Wraith is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.wraith.124931
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Wraith

Wraith is a currently selectable **Marksman** hero. Internal key: `hero_wraith`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

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

- Bullet damage: **5.64**
- Rounds/s: **10.582**; magazine: **52**; reload: **2.82s**
- Projectile speed: **571.5m/s**; falloff: **18–52m**
- Source DPS: **59.682**; sustained: **37.921**

## Abilities

### 1. Card Trick

Internal key: `citadel_ability_card_toss`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Deal weapon damage to summon cards of a random suit. Each card can be thrown, dealing damage and applying a different effect depending of its suit. Cards thrown fly towards the enemy or point under your crosshair.
> Alt-cast to throw first card

> Each suit provides a different bonus. Jokers counts as all suits

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +40 Damage and increased Spirit Scaling
- **Tier 3:** All suits are improved and higher chance for Jokers

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorAllowAltCast`, `BehaviorAllowAltCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 45 (+0.55 per spirit) |
| Cooldown | 0.6 (+0 per cooldown) |
| Cast Range | 500 (+0 per range) |
| Charges | 2 (+1 per max charges) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":2}`
- Tier 2: `{"Damage":{"Value":40,"Scale":{"Value":0.4,"Type":"spirit"}}}`
- Tier 3: `{"ImprovedJokerChance":1,"SpadeDamageBonus":40,"DiamondResistShred":-5,"HeartHeal":{"Value":75,"Scale":{"Value":0.5,"Type":"spirit"}},"ClubSlowPercent":20}`

### 2. Project Mind

Internal key: `citadel_ability_projectmind`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Teleport to the targeted location.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** 300 Barrier for 5s. Barrier scales with Spirit Power.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorPreventBotUsage`, `BehaviorMovement`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Cooldown | 46 (+1 per cooldown) |
| Cast Range | 25 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCastRange":15}`
- Tier 2: `{"CombatBarrier":{"Value":300,"Scale":{"Value":1.7,"Type":"spirit"}},"BarrierDuration":5}`
- Tier 3: `{"AbilityCooldown":-32}`

### 3. Full Auto

Internal key: `citadel_ability_wraith_rapidfire`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Temporarily boosts your fire rate and deal bonus spirit damage

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +10% Fire Rate and +3s Duration
- **Tier 3:** Unlimited Ammo and Increased Scaling on Spirit Damage Per Bullet

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

| Card field | Base value |
| --- | ---: |
| Fire Rate | 20 |
| Spirit Damage Per Bullet | 2 (+0.03 per spirit) |
| Spirit Lifesteal | 0 |
| Bullet Lifesteal | 0 |
| Cooldown | 45 (+1 per cooldown) |
| Duration | 5 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20}`
- Tier 2: `{"BonusFireRate":10,"AbilityDuration":3}`
- Tier 3: `{"MagicDamagePerBullet":{"Value":0,"Scale":{"Value":0.045,"Type":"spirit"}},"UnlimitedAmmo":1}`

### 4. Telekinesis

Internal key: `citadel_ability_psychic_lift`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Lift an enemy hero into the air and then slam them towards the target location.

> Slamming the target into the ground deals spirit damage, applying slow and prevents Stamina and movement-based items and abilities

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +1.5s Debuff Duration and +6m Throw and Cast Range

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorProjectilePassThroughWorld`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 100 (+1 per spirit) |
| Throw Range | 13 (+1 per range) |
| Channel Duration | 0.65 (+1 per duration) |
| Cooldown | 150 (+1 per cooldown) |
| Duration | 2.25 (+1 per duration) |
| Cast Range | 10 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":100}`
- Tier 2: `{"AbilityCooldown":-45}`
- Tier 3: `{"AbilityDuration":1.5,"TossDistance":6,"AbilityCastRange":6}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Wraith](https://deadlock.wiki/Wraith?oldid=124931) article and generated data revisions. No wiki media is included.
