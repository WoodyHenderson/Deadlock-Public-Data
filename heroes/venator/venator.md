---
id: hero.venator
title: Venator
domain: heroes
topics: [hero]
aliases: []
summary: Venator is a selectable Marksman hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.venator.124906
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Venator

Venator is a currently selectable **Marksman** hero. Internal key: `hero_priest`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 820 |
| Health regeneration | 2/s |
| Move speed | 6.4m/s |
| Sprint bonus | 1m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 125 |

## Weapon

- Bullet damage: **8**
- Rounds/s: **7.9365**; magazine: **33**; reload: **2.8s**
- Projectile speed: **1588m/s**; falloff: **18–47m**
- Source DPS: **63.492**; sustained: **37.942**

## Abilities

### 1. Consecrating Grenade

Internal key: `ability_priest_flashbang`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Fire a grenade that bounces before exploding, dealing weapon damage and setting enemies on fire.
> Burning targets deal pure damage to enemies in the area and suffer from reduced healing.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +1.5m Radius & +1s Burn Duration
- **Tier 3:** -20% Healing Reduction and allow Charges

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 35 (+1 per weapon damage increase) |
| Healing Reduction | -30 |
| Damage Per Second | 10 |
| Max Health as Damage | 0 |
| Move Speed | 0 |
| Fire Rate | 0 |
| Burn Duration | 3.5 (+1 per duration) |
| Burn Radius | 4.5 (+1 per range) |
| Cooldown | 25 (+1 per cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-5}`
- Tier 2: `{"Radius":1.5,"BurnRadius":1.5,"BurnDuration":1}`
- Tier 3: `{"HealAmpReceivePenaltyPercent":-20,"HealAmpRegenPenaltyPercent":-20,"AbilityCharges":1,"AbilityCooldownBetweenCharge":3}`

### 2. Gutshot

Internal key: `ability_priest_knockback`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Fire a blast with your shotgun, dealing weapon damage and pushing enemies back. Enemies near a wall receive stun and take bonus weapon damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -10s Ability Cooldown and +0.4s Stun Duration
- **Tier 3:** On Wall Stun: Your next heavy melee is blessed

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 60 (+0.7 per weapon damage increase) |
| Bonus Damage | 30 (+0.8 per weapon damage increase) |
| Stun Duration | 0.6 (+1 per duration) |
| Debuff Duration | 0 |
| Wall Stun Range | 7 (+1 per range) |
| Cooldown | 23 (+1 per cooldown) |
| Cast Range | 10 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"Damage":25}`
- Tier 2: `{"AbilityCooldown":-10,"StunDuration":0.4}`
- Tier 3: `{"BuffDuration":5}`

### 3. Hex-Lined Snap Trap

Internal key: `ability_priest_beartrap`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Kick a trap that arms after a brief delay.
> The trap springs on the first enemy it touches, dealing spirit damage, applying immobilize, and revealing enemies for a duration afterwards.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +1 Charge Deal +30% damage against revealed targets

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorPreventTrainingBotUsage`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 80 (+2.2 per spirit) |
| Immobilize Duration | 1.25 (+1 per duration) |
| Damage Taken | 0 |
| Reveal Duration | 6 (+1 per duration) |
| Lifetime | 30 (+1 per duration) |
| Cooldown | 28 (+1 per cooldown) |
| Charges | 2 (+1 per max charges) |
| Charge Delay | 8 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-11}`
- Tier 2: `{"ImmobilizeDuration":1}`
- Tier 3: `{"IncomingDamagePercentFromCaster":30,"AbilityCharges":1}`

### 4. Ira Domini

Internal key: `ability_priest_weaponswap`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Load your crossbow with 3 stakes, dealing massively increased weapon damage.
> The final stake is blessed, dealing bonus pure damage and executing low-health enemies.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** While Active: Gain 1.2 m/s Move Speed
- **Tier 2:** -15s Ability Cooldown and +65 Bonus Damage
- **Tier 3:** All Stakes are Blessed

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorDontInterruptSlideOnCast`, `BehaviorRefundHalfCooldownOnChannelInterrupt`.

| Card field | Base value |
| --- | ---: |
| Damage | 120 (+1.5 per weapon damage increase) |
| Bonus Damage | 115 |
| Execute Threshold | 8 |
| Move Speed | 0 |
| Slow Duration | 0 |
| Cooldown | 160 (+1 per cooldown) |
| Duration | 15 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":1.2}`
- Tier 2: `{"BonusDamage":65,"AbilityCooldown":-15}`
- Tier 3: `{"AllStakesBlessed":1}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Venator](https://deadlock.wiki/Venator?oldid=124906) article and generated data revisions. No wiki media is included.
