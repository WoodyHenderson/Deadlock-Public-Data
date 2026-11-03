---
id: hero.violet
title: Violet
domain: heroes
topics: [hero, abilities, release]
aliases: []
summary: First reviewed complete Violet configuration from client 6790 after the October 16 availability post; not an exact launch-day pin.
snapshot_id: deadlock-data-client-6790
current_as_of: "2026-10-16"
evidence_status: source_verified_with_official_release_confirmation
sources:
  - github.deadlock-data.gameplay.596ad0c74b26
  - github.deadlock-data.english.596ad0c74b26
  - github.deadlock-data.gameplay.3aab395a1392
  - github.deadlock-data.gameplay.5b2911aa55e6
  - steam.news.violet-release.1846651706683085
---

# Violet

Valve's [October 16 announcement](https://store.steampowered.com/news/app/1422450/view/1846651706683085?l=english) was published at **21:00:07 UTC** and says Violet is available in-game. The post introduces Living Ink, Flow State, Still Life, and Abstract Landscape; its descriptive text is not a complete mechanical specification.

This record uses the first reviewed complete Violet configuration after the announcement: **client 6790 / source revision 11139717**. Its source commit followed the Steam post by ten minutes. Client 6793 is a same-date follow-up whose 13 selected JSON datasets are byte-identical to client 6790. Neither establishes an exact launch-day configuration; the embedded version times have no declared timezone.

Client 6785 had only an incomplete selectable placeholder. Client 6790's generated `InDevelopment` flag remains true even though Valve explicitly confirms availability; the flag is retained but does not override that release evidence.

Generated client fields and localized descriptions are source evidence, not independent runtime tests. Unrelated adjacent client changes are outside this Violet release record and are not attributed to Violet.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 710 |
| Health regeneration | 2/s |
| Move speed | 6.9m/s |
| Sprint bonus | 2.5m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Per-Boon Growth

Configured `LevelScaling` fields from client 6790; source keys and values are preserved without deriving a live-match growth formula.

| Source field | Value per boon |
| --- | ---: |
| `BulletDamage` | 0.55 |
| `MaxHealth` | 34.0 |
| `PowerIncreases` | 1 |
| `TechPower` | 1.1 |
| `LightMeleeDamage` | 1.2 |
| `HeavyMeleeDamage` | 2.784 |
| `DPS` | 0.84618 |
| `SustainedDPS` | 0.66266 |


## Weapon

- Bullet damage: **30**
- Rounds/s: **1.5385**; magazine: **15**; reload: **2.7s**
- Projectile speed: **495.3m/s**; falloff: **19.99–64.01m**
- Source DPS: **46.155**; sustained: **36.145**

## Abilities

### 1. Living Ink

Internal key: `ability_artist_homingbrush`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Empower ( [ABILITY1] ): Your next 3 bullets come to life, allowing you to steer them as they travel. The bullets deal increased bullet damage and splash spirit damage in a small area.
> Each successful hit against a hero reduces all ability cooldowns, and half for all item cooldowns.

> Draw ( [ADS] ): Paint a solid stroke of ink instead that blocks projectiles and characters from passing through.
> The stroke can be destroyed with a heavy melee, but deals spirit damage to the attacker.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -4s Cooldown 15m Max Draw Distance
- **Tier 2:** On Empower: Gain +10% Fire Rate for 10s, stacking 5 times
- **Tier 3:** +1s Cooldown Reduction Per Hit Improve scaling
Description source: [`github.deadlock-data.english.596ad0c74b26`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/596ad0c74b26dd7b11ef5c62b24a11a34c7813d8/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 35 (+0.7 per spirit) |
| Cooldown Reduction per Hit | 1.5 |
| Bullet Damage | 120 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-4,"MaxDrawDistance":15}`
- Tier 2: `{"MaxStacks":5,"StackDuration":10,"BonusFireRatePerStack":10}`
- Tier 3: `{"BulletDamageMultiplier":30,"CooldownReductionPerHit":1,"Damage":{"Value":0,"Scale":{"Value":0.4,"Type":"spirit"}}}`

### 2. Flow State

Internal key: `ability_artist_rollingprojectile`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Drag a brush that continues to travel forward, leaving a trail that grants bonus slide distance for allies and a fading slow and spirit damage to enemies it passes through, increased the further it travels.
> Re-activate the ability to flick the brush forward, ending the ability early but dealing spirit damage in a larger area.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Slide: +150% Stamina Regeneration
- **Tier 2:** -6s Cooldown +8m Flick Range +4s Trail Duration
- **Tier 3:** On Slide: Gain Damage Amp over time, up to 20% for 6s
Description source: [`github.deadlock-data.english.596ad0c74b26`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/596ad0c74b26dd7b11ef5c62b24a11a34c7813d8/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Minimum Damage | 50 (+0.9 per spirit) |
| Max Damage | 100 (+1.8 per spirit) |
| Slide Distance | 100 |
| Time for Max Damage | 2 |
| Move Speed | 0 |
| Barrier Duration | 0 |
| Fading Move Speed | 60 |
| Slow Duration | 2 (+1 per duration) |
| Debuff Duration | 0 |

Upgrade deltas:
- Tier 1: `{"StaminaCooldownReduction":150}`
- Tier 2: `{"AbilityCooldown":-6,"ExplosionRadius":8,"GroundAuraDuration":4}`
- Tier 3: `{"OutgoingDamagePercent":20,"DamageAmpBuildDuration":4,"DamageAmpDuration":6}`

### 3. Still Life

Internal key: `ability_artist_tether`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Choose a hero to be your subject, dealing spirit damage over time as long as you are looking at them.
> If the sketch is completed they take additional spirit damage, suffer from stun, and drop a sketch that can be picked up.
> For each collected sketch, you permanently gain stats based on the hero.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Cast: Gain 15 Health Regen for 4s, refreshed on pickup
- **Tier 2:** While Drawing: Subjects deal -35% Damage
- **Tier 3:** +20% Move Speed -11s Cooldown +0.35s Stun Duration
Description source: [`github.deadlock-data.english.596ad0c74b26`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/596ad0c74b26dd7b11ef5c62b24a11a34c7813d8/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorDontInterruptSlideOnCast`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorTriggerCancelMashProtectionOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 30 (+0.7 per spirit) |
| Damage | 60 (+1.4 per spirit) |
| Max Move Speed | 0 |
| Stun Duration | 1 (+1 per duration) |
| Move Speed | 0 |
| Barrier | 0 (+0 per spirit) |
| Health Regen | 0 (+0 per spirit) |
| Buff Duration | 0 |

Upgrade deltas:
- Tier 1: `{"BuffDuration":4,"HealthRegen":{"Value":15,"Scale":{"Value":0.25,"Type":"spirit"}}}`
- Tier 2: `{"OutgoingDamagePercent":-35}`
- Tier 3: `{"AbilityCooldown":-11,"StunDuration":0.35,"BonusMoveSpeedPercent":20}`

### 4. Abstract Landscape

Internal key: `ability_artist_bamboogrove`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Create a circular display of ink that blocks vision and grants allies Spirit.
> Enemies inside are revealed, and leaving causes them to take spirit damage and suffer from Silence and slow, destroying the ink in the process.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** On Buff: +25% Spirit Lifesteal +15 Spirit Power
- **Tier 3:** +1.25s Silence Duration +4s Ability Duration Ink is no longer destroyed
Description source: [`github.deadlock-data.english.596ad0c74b26`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/596ad0c74b26dd7b11ef5c62b24a11a34c7813d8/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorCannotCancelDuringChannel`, `BehaviorDontInterruptSlideOnCast`, `BehaviorRefundFullCooldownOnChannelInterrupt`.

| Card field | Base value |
| --- | ---: |
| Spirit Power | 25 |
| Spirit Lifesteal | 0 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20}`
- Tier 2: `{"AbilityLifestealPercentHero":25,"TechPower":15}`
- Tier 3: `{"SilenceDuration":1.25,"AbilityDuration":4,"DestroyOnDamage":-1}`

## Supporting Client Records

The YAML preserves two unnumbered trigger ability records, the `citadel_artist_strokeblocker` NPC record, and four Violet drawing-pickup records. These are supporting generated data, not additional hero slots, map-placement evidence, or independent runtime tests.

## Data Boundaries

- Valve's October 16 post establishes availability; client 6790 is the first reviewed complete post-release configuration, not an exact launch-day stat sheet.
- Client 6785's selectable placeholder has no bound abilities and a provisional configuration; those values are comparison-only.
- Client 6793's selected JSON files match client 6790 exactly; no second Violet snapshot is represented.
- Client `InDevelopment=true` is retained as a data flag and does not override Valve's explicit availability statement.
- Nurse Harrow's adjacent pre-release growth change and unrelated item, HUD, Familiar, Solomon, hideout, localization, and Street Brawl changes are not attributed to Violet.
- No October 16 raw changelog was found in the reviewed source trees. No undocumented balance update or runtime behavior is asserted.

Release evidence: [steam.news.violet-release.1846651706683085](https://store.steampowered.com/news/app/1422450/view/1846651706683085?l=english).
Client data: [github.deadlock-data.gameplay.596ad0c74b26](https://github.com/deadlock-wiki/deadlock-data/tree/596ad0c74b26dd7b11ef5c62b24a11a34c7813d8/data/json).
