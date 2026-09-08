---
id: hero.paige
title: Paige
domain: heroes
topics: [hero]
aliases: []
summary: Paige is a selectable Mystic hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.paige.125555
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Paige

Paige is a currently selectable **Mystic** hero. Internal key: `hero_bookworm`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 680 |
| Health regeneration | 2/s |
| Move speed | 6.9m/s |
| Sprint bonus | 3.5m/s |
| Stamina | 3 |
| Light / heavy melee | 42 / 120 |

## Weapon

- Bullet damage: **35**
- Rounds/s: **2**; magazine: **14**; reload: **2.5s**
- Projectile speed: **43.43m/s**; falloff: **19.99–57.51m**
- Source DPS: **70**; sustained: **51.579**

## Abilities

### 1. Bookwyrm

Internal key: `ability_bookworm_dragonfire`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Conjure a dragon that appears at the target location before flying forward, dealing spirit damage and leaving a burning path in its trail.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -12s Cooldown
- **Tier 2:** +1 Charge +2s Trail Duration +1m Radius
- **Tier 3:** +12m Travel Range +100 Damage +30 DPS

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorProjectilePassThroughWorld`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 60 (+1.3 per spirit) |
| Damage Per Second | 30 (+0.3 per spirit) |
| Trail Duration | 3 (+1 per duration) |
| Dragon Travel Range | 20 (+1 per range) |
| Cooldown | 33 (+1 per cooldown) |
| Duration | 5 (+1 per duration) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 7 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-12}`
- Tier 2: `{"GroundFlameDuration":2,"Radius":1,"AbilityCharges":1}`
- Tier 3: `{"Damage":100,"DPS":30,"DragonTravelRange":12}`

### 2. Plot Armor

Internal key: `ability_bookworm_knightbarrier`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Grant an ally a barrier. While the barrier holds, they gain bonus weapon damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Barrier: +14% Fire Rate
- **Tier 2:** +100 Barrier and +2s Duration
- **Tier 3:** Affects up to 2 additional allies. Increases barrier scaling.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorAllowSelfCast`, `BehaviorCannotCancelDuringChannel`, `BehaviorAllowAltCast`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Barrier | 125 (+1.5 per spirit) |
| Weapon Damage | 25 (+0.3 per spirit) |
| Fire Rate | 0 (+0 per spirit) |
| Cooldown | 28 (+1 per cooldown) |
| Duration | 5 (+1 per duration) |
| Cast Range | 35 (+1 per range) |

Upgrade deltas:
- Tier 1: `{"BonusFireRate":{"Value":14,"Scale":{"Value":0.16,"Type":"spirit"}}}`
- Tier 2: `{"CombatBarrier":100,"AbilityDuration":2}`
- Tier 3: `{"CombatBarrier":{"Value":0,"Scale":{"Value":0.5,"Type":"spirit"}},"BonusTargets":2,"BonusTargetsBarrierPercentage":100}`

### 3. Captivating Read

Internal key: `ability_bookworm_aoemagic`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Target an area with latent magic, applying slow.
> The magic detonates after a delay, dealing spirit damage and applying immobilize.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +1m Radius On Hit: Reduce Spirit Resist by -18% for 6s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 90 (+1.3 per spirit) |
| Immobilize Duration | 1 (+1 per duration) |
| Spirit Resist | 0 |
| Move Speed | 45 |
| Slow Duration | 0.5 (+1 per duration) |
| Cooldown | 30 (+1 per cooldown) |
| Cast Range | 30 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-11}`
- Tier 2: `{"ImmobilizeDuration":1}`
- Tier 3: `{"TechArmorDamageReduction":-18,"DebuffDuration":6,"Radius":1}`

### 4. Rallying Charge

Internal key: `ability_bookworm_knightcharge`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Release a wave of spectral knights and steeds that charge across the entire city, healing allies and dealing spirit damage to enemies.
> The strength of the heal and spirit damage is amplified as the knights travel further.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Increase width by +4 Steeds -45 Cooldown
- **Tier 3:** +160 Damage +0.5s Stun Duration +70% Max Amp

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorCannotCancelDuringChannel`, `BehaviorRefundHalfCooldownOnChannelInterrupt`.

| Card field | Base value |
| --- | ---: |
| Cooldown | 210 (+1 per cooldown) |
| Duration | 13 (+1 per duration) |
| Cast Range | 600 |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"HealAmount":150}`
- Tier 2: `{"KnightCount":4,"KnightCountInFirstWave":4,"AbilityCooldown":-45}`
- Tier 3: `{"Damage":160,"StunDuration":0.5,"MaxAmp":70}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Paige](https://deadlock.wiki/Paige?oldid=125555) article and generated data revisions. No wiki media is included.
