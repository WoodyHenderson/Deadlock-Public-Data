---
id: hero.apollo
title: Apollo
domain: heroes
topics: [hero]
aliases: []
summary: Apollo is a selectable Assassin hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.apollo.124913
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Apollo

Apollo is a currently selectable **Assassin** hero. Internal key: `hero_fencer`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 770 |
| Health regeneration | 1/s |
| Move speed | 7.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 63 / 116 |

## Weapon

- Bullet damage: **18.5**
- Rounds/s: **2.6316**; magazine: **15**; reload: **2.5s**
- Projectile speed: **127m/s**; falloff: **25.4–25.4m**
- Source DPS: **48.685**; sustained: **33.842**

## Abilities

### 1. Disengaging Sigil

Internal key: `ability_fencer_throwblade`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Draw a sigil sphere in front of you and then leap backwards as it explodes, damaging and slowing enemies caught in it.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Gain +25% Fire Rate and +25% Bullet Speed for 8s
- **Tier 2:** On Player Hit: +1 stamina restored and resets Air Jump/Dash limit
- **Tier 3:** Can be Recast within 4s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorMovement`.

| Card field | Base value |
| --- | ---: |
| Damage | 85 (+1.3 per spirit) |
| Move Speed | 30 |
| Fire Rate | 0 |
| Slow Duration | 4 (+1 per duration) |
| Radius | 6.5 (+1 per range) |
| Cooldown | 12 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusFireRate":25,"BonusBulletSpeedPercent":25,"BuffDuration":8}`
- Tier 2: `{"StaminaToRestore":1,"ResetsAirLimit":1}`
- Tier 3: `{"RecastTime":4}`

### 2. Riposte

Internal key: `ability_fencer_riposte`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Prepare to deflect the next incoming attack. On a successful deflection, briefly become invulnerable and target an enemy hero to dash towards them, stunning them and reducing their Melee Resist.
> Press [Ability 2] to select a target.
> Does not trigger against trooper or neutral damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -25% Melee Resist and +0.4s Stun Duration
- **Tier 3:** Gain 75% Bullet, Spirit & Melee Lifesteal against the Riposte target for 13s

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Invulnerability Duration | 0.3 |
| Cooldown | 22 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-8}`
- Tier 2: `{"MeleeResistReduction":-25,"StunDuration":0.4}`
- Tier 3: `{"TargetLifesteal":75,"TargetLifestealDuration":13}`

### 3. Flawless Advance

Internal key: `ability_fencer_lunge`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Perform a series of lunges in any direction, delivering piercing stabs ahead of you. Hold your ability key to time your attacks, dealing more damage the longer it's held. Releasing your attack during the perfect window deals maximum damage.
> Press [Ability 3] to re-cast.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Perfect Hit on Hero: Heal 35
- **Tier 2:** -12s Cooldown. Gain +60% Bullet Resist during lunge
- **Tier 3:** +65 Perfect Damage with improved Spirit scaling. Increased lunge speed & distance.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorDontTriggerPostCastOnCastComplete`, `BehaviorMovement`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Base Damage | 25 (+0.55 per spirit) |
| Max Hold Damage | 40 (+0.9 per spirit) |
| Max Lunges | 3 |
| Bullet Resist | 0 |
| Cooldown | 26 (+1 per cooldown) |
| Duration | 8 (+1 per duration) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"HealFixedHealth":{"Value":35,"Scale":{"Value":1.3,"Type":"spirit"}}}`
- Tier 2: `{"AbilityCooldown":-12,"BulletResist":60,"DashBuffDuration":1.5}`
- Tier 3: `{"BaseDamage":{"Value":30,"Scale":{"Value":1.15,"Type":"spirit","Multiply":true}},"MaxDamageBeforePerfect":{"Value":45,"Scale":{"Value":1.15,"Type":"spirit","Multiply":true}},"PerfectDamage":{"Value":65,"Scale":{"Value":1.15,"Type":"spirit","Multiply":true}},"AttackDashRange":3,"DashSpeed":13.97}`

### 4. Itani Lo Sahn

Internal key: `ability_fencer_ultimate`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Charge up and perform a long range slash. Struck enemies cannot take action or heal and are stuck in slow motion. When this effect expires, they suffer devastating damage, dealing bonus damage against half-health enemies.
> While in slow motion, Apollo is invulnerable and enemies take reduced damage.
> Hold [Ability 4] or [Attack] to delay the cast.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** IGNORED[]% Max Health Damage

**Source warning** (`ability_fencer_ultimate_t3_desc`): Source contains an unresolved placeholder. Retained verbatim for provenance, not a usable numeric effect; consult the separate upgrade data and review before interpreting this tooltip.

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorDontTriggerPostCastOnCastComplete`, `BehaviorMovement`, `BehaviorNoTarget`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorDeactivateCrouchToggleOnCast`, `BehaviorCannotCancelDuringChannel`, `BehaviorCooldownOnChannelEnd`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorDisplaysDamageImpact`.

| Card field | Base value |
| --- | ---: |
| Delayed Damage | 200 (+2.6 per spirit) |
| Bonus Damage | 60 |
| Time Slow Damage Reduction | 70 |
| Low Health Threshold | 50 |
| Debuff Duration | 1.8 |
| Cooldown | 145 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"DashRange":8}`
- Tier 2: `{"AbilityCooldown":-35}`
- Tier 3: `{"BonusDamagePercent":50}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Apollo](https://deadlock.wiki/Apollo?oldid=124913) article and generated data revisions. No wiki media is included.
