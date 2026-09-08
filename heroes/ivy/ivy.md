---
id: hero.ivy
title: Ivy
domain: heroes
topics: [hero]
aliases: []
summary: Ivy is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.ivy.124889
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Ivy

Ivy is a currently selectable **Marksman** hero. Internal key: `hero_tengu`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 755 |
| Health regeneration | 2/s |
| Move speed | 7.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 4 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **4.45**
- Rounds/s: **13.605**; magazine: **33**; reload: **2.444s**
- Projectile speed: **571.5m/s**; falloff: **19.99–57.51m**
- Source DPS: **60.542**; sustained: **30.157**

## Abilities

### 1. Entangling Thorns

Internal key: `citadel_ability_tengu_urn`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Summon a patch of choking thorns that damage and slows enemies in its radius.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +2m Radius and increased DPS Spirit scaling
- **Tier 3:** Enemies caught in thorns for 2s are Immobilized for +1.6s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 40 (+0.55 per spirit) |
| Move Speed | 35 |
| Cooldown | 32 (+1 per cooldown) |
| Duration | 4 (+1 per duration) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 5 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1}`
- Tier 2: `{"Radius":2,"DPS":{"Value":0,"Scale":{"Value":0.5,"Type":"spirit"}}}`
- Tier 3: `{"TimeToEntangle":2,"EntangleDuration":1.6}`

### 2. Kudzu Connection

Internal key: `citadel_ability_tangotether`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Connect with a nearby ally to gain bonuses, replicated healing, and ignore the move speed penalty while shooting.
> Receive 50% of Bonuses with no connection
> Connection requires line of sight.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +8% Fire Rate and +8% Bullet Lifesteal
- **Tier 3:** Ability is always active

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Fire Rate | 10 (+0.18 per spirit) |
| Bullet Lifesteal | 15 (+0.15 per spirit) |
| Replicated Healing | 35 (+0.85 per power increase) |
| Move Speed | 0 |
| Tether Count | 1 |
| Cooldown | 37 (+1 per cooldown) |
| Duration | 12 (+1 per duration) |
| Cast Range | 16 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MoveSpeedBonus":2}`
- Tier 2: `{"BonusFireRate":8,"BulletLifestealPercent":8}`
- Tier 3: `{"AbilityDuration":-13,"AbilityCooldown":-37}`

### 3. Stone Form

Internal key: `citadel_ability_tengu_stone_form`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Turn yourself into impervious stone and smash into the ground, stunning and damaging enemies nearby. Heals you for a percentage of your max health.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +0.75s Stun Duration and increased Damage spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCastableWhileBusy`, `BehaviorInterruptMeleeOnCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 75 (+0.6 per spirit) |
| Stun Duration | 0.75 (+1 per duration) |
| Max Health Heal | 6 (+1 per healing) |
| Cooldown | 40 (+1 per cooldown) |
| Duration | 3 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"MaxHealthRegen":7}`
- Tier 2: `{"AbilityCooldown":-25}`
- Tier 3: `{"StunDuration":0.75,"Damage":{"Value":0,"Scale":{"Value":1.5,"Type":"spirit"}}}`

### 4. Air Drop

Internal key: `citadel_ability_tengu_airlift`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Grab an ally and take flight with them. Drop your ally to cause an explosion, dealing spirit damage. You and your ally gain increased Outgoing Damage when flying ends.
> Cooldown reduced by 30% when used on allies.
> Taking damage briefly disables using the ability.
> While lifted, your ally cannot attack and deals -20% damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Fly End : 300 Barrier to Ivy and ally that scales with Spirit
- **Tier 2:** +40% Slow for 3s on enemies hit
- **Tier 3:** Silence for 3s on enemies hit. Increases damage and barrier scaling.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorAllowSelfCast`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorMovement`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorCanSetQuickCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Explode Damage | 115 (+0.7 per spirit) |
| Outgoing Damage Bonus | 20 |
| Barrier | 0 (+0 per spirit) |
| Landing Radius | 20 (+1 per radius) |
| Buff Duration | 8 (+1 per duration) |
| Move Speed | 0 |
| Debuff Duration | 0 |
| Bullet Resist | 0 |
| Duration | 0 |
| Silence Duration | 0 |
| Cooldown | 100 (+1 per cooldown) |
| Duration | 21 (+1 per duration) |
| Cast Range | 22 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AirDropBulletShield":{"Value":300,"Scale":{"Value":0.7,"Type":"spirit"}}}`
- Tier 2: `{"SlowPercent":40,"DebuffDuration":3}`
- Tier 3: `{"SilenceDuration":3,"ExplodeDamage":{"Value":0,"Scale":{"Value":1.5,"Type":"spirit"}},"AirDropBulletShield":{"Value":0,"Scale":{"Value":1,"Type":"spirit"}}}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Ivy](https://deadlock.wiki/Ivy?oldid=124889) article and generated data revisions. No wiki media is included.
