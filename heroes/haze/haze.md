---
id: hero.haze
title: Haze
domain: heroes
topics: [hero]
aliases: []
summary: Haze is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.haze.124874
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Haze

Haze is a currently selectable **Assassin** hero. Internal key: `hero_haze`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 2/s |
| Move speed | 8.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **5.26**
- Rounds/s: **9.5238**; magazine: **25**; reload: **2.35s**
- Projectile speed: **762m/s**; falloff: **19.99–46m**
- Source DPS: **50.095**; sustained: **26.432**

## Abilities

### 1. Sleep Dagger

Internal key: `ability_sleep_dagger`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a dagger that damages and sleeps the target. Sleeping targets wake up shortly after being damaged. Throwing a Dagger does not break your invisibility. Sleep Dagger does not interrupt enemies' channeling abilities.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -10% Bullet Resist Reduction for 6s on wake-up
- **Tier 2:** +1s Sleep Duration Applies 15 Fixation Stacks
- **Tier 3:** -17s Cooldown -50% Move and Dash Speed for 3s on wake-up

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDamageDoesntWakeFromSleep`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 65 (+2.2 per spirit) |
| Sleep Duration | 2.75 (+1 per duration) |
| Min Sleep Time | 0.2 |
| Wake Up Delay | 0.1 (+0.002 per spirit, +1 per duration) |
| Sleep Movespeed | 1.5 |

Sleep Dagger uses two separate sleep timings. If the sleeping target takes no
 damage, the normal Sleep Duration applies. Once the target takes damage, the
 Spirit-scaled Wake Up Delay begins counting down; the first damage instance does
 not immediately end the sleep.
| Ricochet Range | 0 |
| Cooldown | 30 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BulletResistReduction":-10,"BulletResistReductionDuration":6}`
- Tier 2: `{"SleepDuration":1,"FixationStacks":15}`
- Tier 3: `{"AbilityCooldown":-17,"SlowPercent":50,"GroundDashReductionPercent":-50,"DebuffDuration":3}`

### 2. Smoke Bomb

Internal key: `ability_smoke_bomb`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Fade out of sight, becoming invisible and gaining sprint speed. Attacking removes invisibility, but using items does not. Close enemies can see through your invisibility.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Enable 2 Ability Charges
- **Tier 3:** Dispels non-ult debuffs Grants +50% Bullet Lifesteal for 5s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDamageDoesntWakeFromSleep`, `BehaviorNoTarget`, `BehaviorDontInterruptSprint`, `BehaviorCleaveDisabled`, `BehaviorCanCastOnZipline`.

| Card field | Base value |
| --- | ---: |
| Fade Time | 1.5 |
| Spot Radius | 18 |
| Invis Sprint Speed | 0 |
| Invincible Duration | 0 |
| Cooldown | 33 (+1 per cooldown) |
| Duration | 8 |

Upgrade deltas:
- Tier 1: `{"InvisMoveSpeedMod":7}`
- Tier 2: `{"AbilityCharges":2,"AbilityCooldownBetweenCharge":7}`
- Tier 3: `{"BulletLifesteal":50,"PostInvisBuffDuration":5,"DispelOnUse":1}`

### 3. Fixation

Internal key: `ability_stacking_damage`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Shooting a target increases your bullet damage on that target. Gain one stack per bullet hit, two if the hit is a headshot.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** 40 Spirit damage and 15% slow for 2s to target every 20 stacks
- **Tier 2:** +40 Max Stacks and +5s Duration
- **Tier 3:** +0.11/ per Stack Scales with Weapon Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

| Card field | Base value |
| --- | ---: |
| Weapon Damage | 0.2 (+0 per weapon damage increase) |
| Max Stacks | 40 |
| Spirit Damage | 0 (+0 per spirit) |
| Duration | 6 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"ProcDamage":{"Value":40,"Scale":{"Value":0.8,"Type":"spirit"}},"ProcDamageStackCount":20,"SlowPercent":15,"SlowDuration":2}`
- Tier 2: `{"AbilityDuration":5,"MaxStacks":40}`
- Tier 3: `{"DamageBonusFixedPerStack":{"Value":0.11,"Scale":{"Value":0.0003,"Type":"weapon_damage_increase"}}}`

### 4. Bullet Dance

Internal key: `ability_bullet_flurry`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Enter a flurry, firing your weapon at nearby enemies with perfect accuracy and added Bullet Damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +10% Fire Rate +3m Movespeed
- **Tier 3:** +40% Evasion -65s Cooldown

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorExclusiveUse`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCleaveDisabled`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Fire Rate | 25 |
| Weapon Damage | 7 |
| Targets Hit Per Shot | 1 |
| Bullet Evasion | 30 |
| Channel Move Speed | 4 |
| Cooldown | 165 (+1 per cooldown) |
| Duration | 3.5 |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"WeaponDamageBonus":7}`
- Tier 2: `{"BonusFireRate":10,"ChannelMoveSpeed":3}`
- Tier 3: `{"EvasionPercent":40,"AbilityCooldown":-65}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Haze](https://deadlock.wiki/Haze?oldid=124874) article and generated data revisions. No wiki media is included.
