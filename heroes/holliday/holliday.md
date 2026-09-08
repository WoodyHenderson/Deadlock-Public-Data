---
id: hero.holliday
title: Holliday
domain: heroes
topics: [hero]
aliases: []
summary: Holliday is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.holliday.125565
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Holliday

Holliday is a currently selectable **Marksman** hero. Internal key: `hero_astro`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 2/s |
| Move speed | 8.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 2 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **19.7**
- Rounds/s: **2.1164**; magazine: **10**; reload: **2.75s**
- Projectile speed: **1156m/s**; falloff: **19.99–57.51m**
- Source DPS: **41.693**; sustained: **26.354**

## Abilities

### 1. Powder Keg

Internal key: `ability_explosive_barrel`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a barrel that explodes after a delay, dealing spirit damage, setting enemies on fire and applying knockup.
> The barrel can be detonated early by being shot, melee'd, or detonated by another barrel.
> The burn stacks, so overlapping barrels burn for their combined damage.
> Can be Alt-Cast to place the barrel infront of Holliday.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +40 Impact Damage +13.3333 Burn Damage per Second -5 Charge Time Improved Spirit Scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorIgnoreSelectionMashProtection`, `BehaviorDontInterruptSlideOnCast`, `BehaviorAllowAltCast`, `BehaviorCastImmediateOnOtherAbility`.

| Card field | Base value |
| --- | ---: |
| Impact Damage | 40 (+0.525 per spirit) |
| Damage Per Second | 13.3333 (+0.175 per spirit) |
| Duration | 0.4 |
| Burn Duration | 3 (+1 per duration) |
| Arm Time | 0.1 |
| Cooldown | 28 (+1 per cooldown) |
| Charges | 2 (+1 per max charges) |
| Charge Delay | 7.5 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-10}`
- Tier 2: `{"AbilityCharges":1}`
- Tier 3: `{"ImpactDamage":{"Value":40,"Scale":{"Value":0.25,"Type":"spirit"}},"DPS":{"Value":13.3333,"Scale":{"Value":0.083333,"Type":"spirit"}},"AbilityCooldownBetweenCharge":-5}`

### 2. Bounce Pad

Internal key: `ability_bounce_pad`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Drop a bounce pad in the world that launches any hero.
> You explode on landing, dealing Damage to any nearby enemies.
> The explosion can only occur once per person per Bounce Pad.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -10s Cooldown
- **Tier 2:** You and allies gain a +4m/s move speed bonus for 4s on landing
- **Tier 3:** +0.7s Stomp Stun

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorMovement`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Stomp Damage | 60 (+0.372 per spirit) |
| Radius | 9 (+1 per radius) |
| Air Control | 100 |
| Cooldown | 41 (+1 per cooldown) |
| Duration | 22 (+1 per duration) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 3.5 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-10}`
- Tier 2: `{"SpeedOnLand":4,"SpeedOnLandDuration":4}`
- Tier 3: `{"StompStunDuration":0.7}`

### 3. Crackshot

Internal key: `ability_crackshot`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Headshots deal bonus Damage and applies a Fading Move Speed penalty. This effect can only occur when off cooldown.
> Cooldown is reduced by 50% on NPC hits.
> Crackshot ignores range damage fall-off and does not apply to objectives.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -25% Fading Move Speed
- **Tier 3:** -6s Cooldown on Hero Headshots. -3s on NPC Headshots

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Damage | 55 (+1.116 per spirit) |
| Fading Move Speed | 50 |
| Debuff Duration | 2 (+1 per duration) |
| Cooldown | 20 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"FadingSlowPercent":25}`
- Tier 2: `{"Damage":49.5}`
- Tier 3: `{"AbilityCooldownPerHeadshot":-6,"AbilityCooldownPerHeadshotNPC":-3}`

### 4. Spirit Lasso

Internal key: `ability_gravity_lasso`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw out your lasso, dealing spirit damage, pulling, and applying stun.
> Using a Bounce Pad extends the duration of Spirit Lasso.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorCleaveDisabled`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorDontInterruptSlideOnCast`, `BehaviorInterruptMeleeOnCast`.

| Card field | Base value |
| --- | ---: |
| Duration | 2.25 (+1 per duration) |
| Cast Range | 20 (+1 per range) |
| Damage | 80 (+0.93 per spirit) |
| Cooldown | 130 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":80}`
- Tier 2: `{"AbilityDuration":0.75}`
- Tier 3: `{"AbilityCooldown":-40}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Holliday](https://deadlock.wiki/Holliday?oldid=125565) article and generated data revisions. No wiki media is included.
