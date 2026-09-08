---
id: hero.billy
title: Billy
domain: heroes
topics: [hero]
aliases: []
summary: Billy is a selectable Brawler hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.billy.125748
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Billy

Billy is a currently selectable **Brawler** hero. Internal key: `hero_punkgoat`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 820 |
| Health regeneration | 2/s |
| Move speed | 7m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **6.3**
- Rounds/s: **11.765**; magazine: **30**; reload: **2.9s**
- Projectile speed: **513.1m/s**; falloff: **13.97–31.75m**
- Source DPS: **74.12**; sustained: **34.679**

## Abilities

### 1. Bashdown

Internal key: `ability_punkgoat_ult`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Slam your bat into the ground, pulling enemies down and dealing melee damage.
> The slam creates a shockwave that deals spirit damage and applies knockup.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -10s Cooldown
- **Tier 2:** +1 Charge and +2m Radius
- **Tier 3:** -3s Charge Time Now deals 50% Heavy Melee Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorSilentCastFailureFeedback`, `BehaviorChannelled`, `BehaviorExclusiveUse`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorCooldownOnChannelEnd`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorHoldsAtMaxChannel`.

| Card field | Base value |
| --- | ---: |
| Melee Damage | 0 (+0.9 per melee) |
| Damage | 0 (+0 per heavy melee) |
| Damage | 35 (+1.1 per spirit) |
| Duration | 0.4 |
| Move Speed | 0 |
| Duration | 0 |
| Fire Rate | 0 |
| Cooldown | 35 (+1 per cooldown) |
| Cast Range | 4 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 8 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-10}`
- Tier 2: `{"AbilityCastRange":2,"AbilityCharges":1}`
- Tier 3: `{"CountsAsLightMelee":-1,"CountsAsHeavyMelee":1,"HeavyMeleeDamage":{"Value":0,"Scale":{"Value":0.5,"Type":"heavy_melee"}},"MeleeDamage":{"Value":0,"Scale":{"Value":0,"Type":"melee","Multiply":true}},"AbilityCooldownBetweenCharge":-3}`

### 2. Rising Ram

Internal key: `ability_punkgoat_goatflip`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Charge head-first into an enemy and send them into the air along with Billy.
> Cooldown reduced by 50% on impact.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Impact: +25% weapon damage for 5s
- **Tier 2:** 0.4s Charge Duration

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorDontTriggerPostCastOnCastComplete`, `BehaviorMovement`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 40 (+1.9 per spirit) |
| Max Health | 0 |
| Cooldown | 32 (+1 per cooldown) |
| Duration | 0.3 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"WeaponDamageBurst":25,"WeaponDamageBurstDuration":5}`
- Tier 2: `{"AbilityDuration":0.4}`
- Tier 3: `{"MaxHealthBuffPct":10,"MaxHealthBuffDuration":16,"AbilityCooldown":-13}`

### 3. Blasted

Internal key: `ability_punkgoat_blasted`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Passive: Melee hits restore ammo and inflict wrecked on the victim for 7s.

> Active: Bullets are amplified against wrecked enemies. Using melee boosts max health and extends duration.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** While Blasted: +2.25m/s bonus move speed
- **Tier 2:** +1 Bashdown Charge on use and +7% Wrecked Bullet Amp
- **Tier 3:** +50 Melee Bonus Health and increases spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorCooldownOnChannelEnd`, `BehaviorAllowGunFireAfterCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Cooldown | 27 (+1 per cooldown) |
| Duration | 8 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":2.25}`
- Tier 2: `{"GainSlamOnUse":1,"BulletDamageAmp":7}`
- Tier 3: `{"MaxHealthMelee":{"Value":50,"Scale":{"Value":0.6,"Type":"spirit"}}}`

### 4. Chain Gang

Internal key: `ability_punkgoat_tether`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Chain nearby enemies to you. Chained enemies cannot use movement abilities and receive a heavy slow when they pull on the chain.
> After a delay, yank everyone towards Billy and deal spirit damage.
> The chain breaks if you lose line of sight for a short while.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +40% spirit resist & bullet resist
- **Tier 3:** +5m Range +1.3s of Unstoppable Per Hero pulled in

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorSilentCastFailureFeedback`, `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorCanSetQuickCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Per Hero | 0 |
| Damage | 120 (+0.7 per spirit) |
| Duration | 2.8 |
| Bullet Resist | 0 |
| Spirit Resist | 0 |
| Fire Rate | 0 |
| Duration | 0 |
| Cooldown | 175 (+1 per cooldown) |
| Cast Range | 12 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BulletResist":40,"TechResist":40}`
- Tier 2: `{"AbilityCooldown":-40}`
- Tier 3: `{"UnstoppablePerHero":1.3,"AbilityCastRange":5}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Billy](https://deadlock.wiki/Billy?oldid=125748) article and generated data revisions. No wiki media is included.
