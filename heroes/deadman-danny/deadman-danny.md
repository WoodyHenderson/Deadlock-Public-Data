---
id: hero.deadman-danny
title: Deadman Danny
domain: heroes
topics: [hero, abilities, release]
aliases: []
summary: First complete Deadman Danny configuration from client 6782 (October 14); Valve confirms the October 13 release, but no exact launch-day data pin is asserted.
snapshot_id: deadlock-data-client-6782
current_as_of: "2026-10-14"
evidence_status: source_verified_with_official_release_confirmation
sources:
  - github.deadlock-data.gameplay.bd95f245ccb1
  - github.deadlock-data.english.bd95f245ccb1
  - github.deadlock-data.gameplay.330a775230e8
  - github.deadlock-data.gameplay.51636a2c4136
  - github.deadlock-data.gameplay.3aab395a1392
  - steam.news.deadman-danny-oct14-update.1846651706676198
  - steam.news.deadman-danny-release.1846018067945303
---

# Deadman Danny

Valve's [October 13 announcement](https://store.steampowered.com/news/app/1422450/view/1846018067945303?l=english) was published at **20:59:55 UTC** and says Danny is available in-game now. The announcement supplies the release date and names, but not the full numerical configuration.

This record uses the first complete Danny configuration found in the reviewed source history: **client 6782 / source revision 11127865, dated October 14**. Client 6774 contained only an incomplete selectable placeholder. No exact October 13 launch-client snapshot is asserted; this is a dated post-release configuration, not a verified launch-day stat sheet.

Generated client fields and localized descriptions are source data, not independent runtime tests. Client 6785 includes the separate October 14 update and is intentionally excluded from these values.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 680 |
| Health regeneration | 2.5/s |
| Move speed | 6.4m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Per-Boon Growth

Configured `LevelScaling` fields from client 6782; source keys and values are preserved without deriving a live-match growth formula.

| Source field | Value per boon |
| --- | ---: |
| `BulletDamage` | 0.42 |
| `BulletDamageAltFire` | 1.6 |
| `MaxHealth` | 39.0 |
| `PowerIncreases` | 1 |
| `TechPower` | 1.1 |
| `LightMeleeDamage` | 1.58 |
| `HeavyMeleeDamage` | 3.6656 |
| `DPS` | 1.68 |
| `SustainedDPS` | 0.87761 |


## Weapon

- Bullet damage: **12**
- Rounds/s: **4**; magazine: **14**; reload: **3.2s**
- Projectile speed: **177.8m/s**; falloff: **18–47m**
- Source DPS: **48**; sustained: **25.075**

## Abilities

### 1. Strix Salvo

Internal key: `ability_deadpack_chargeblast`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Launch a salvo of spirit missiles that lodge into the ground along a line. The missiles explode after a delay or upon detecting an enemy, dealing spirit damage and marking the target.
> Shooting a marked enemy with a charged shot consumes a mark to deal bonus spirit damage and apply a fading slow.
> Hold and drag to select the angle.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** -12s Cooldown
- **Tier 2:** +20 Damage +35 Marked Damage
- **Tier 3:** +2 Missiles, Longer Range, and Improved Spirit Scaling
Description source: [`github.deadlock-data.english.bd95f245ccb1`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/bd95f245ccb152cd4beb359ad0a89e3a86391221/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorDontInterruptSlideOnCast`, `BehaviorRefundHalfCooldownOnChannelInterrupt`.

| Card field | Base value |
| --- | ---: |
| Damage | 27 (+0.74 per spirit) |
| Marked Damage | 45 (+0.9 per spirit) |
| Fading Slow | 40 |
| Fire Rate | 0 |
| Mark Duration | 10 (+1 per duration) |
| Slow Duration | 1.5 (+1 per duration) |
| Explode Delay | 6 (+1 per duration) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-12}`
- Tier 2: `{"Damage":20,"CoatedDamage":35}`
- Tier 3: `{"MarksTotal":2,"Range":14,"CoatedDamage":{"Value":0,"Scale":{"Value":0.2,"Type":"spirit"}},"Damage":{"Value":0,"Scale":{"Value":0.225,"Type":"spirit"}}}`

### 2. Chimera Mk1

Internal key: `ability_deadpack_rocketeer`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Hold [Mantle] to fly, building up heat. When max heat is reached, your jetpack will begin to overheat.
> Overheating: After a short delay, dive to the ground. Upon impact, create an explosion that deals damage and launches you and nearby enemies. If no hero is hit, you stun yourself. Press [Ability 2] to dive early.
> Cooling Down: After overheating, the jetpack cannot be used until it fully cools down.
> Slows affect you while airborne. You always explode on death.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Heat vents faster while grounded
- **Tier 2:** On Hero Hit: Heal and take no self damage
- **Tier 3:** On Hero Hit: -40% Cooldown and +120 Spirit Damage
Description source: [`github.deadlock-data.english.bd95f245ccb1`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/bd95f245ccb152cd4beb359ad0a89e3a86391221/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorCannotCancelDuringChannel`, `BehaviorDisplaysDamageImpact`, `BehaviorMovement`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Cooldown | 21 (-0.25 per power increase, +1 per cooldown) |
| Explosion Damage | 70 (+1.5 per spirit) |
| Explosion Damage | 70 (+1.15 per weapon damage increase) |
| Self Stun | 1.3 |
| Self Damage | 12 |
| Heal On Hit | 0 (+0 per spirit) |

Upgrade deltas:
- Tier 1: `{"HeatDrainRate":-4}`
- Tier 2: `{"HealOnHit":{"Value":150,"Scale":{"Value":1.0,"Type":"spirit"}},"SelfDamageReductionOnPlayerHitPercent":100}`
- Tier 3: `{"ExplosionDamage":120,"OverheatLockoutDurationReductionOnPlayerHitPercent":40}`

### 3. Jettison Fuel

Internal key: `ability_deadpack_flamethrower`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Spray fuel dealing weapon damage over time and shredding bullet resist, building up to a huge backblast that deals spirit damage and knocks you backwards.
> Vents the jetpack when dealing damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +60 Burst Damage On Backblast Hit: +18% Fire Rate for 7s
- **Tier 3:** -10% Bullet Resist Shred On Backblast Hit: Apply a Mark
Description source: [`github.deadlock-data.english.bd95f245ccb1`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/bd95f245ccb152cd4beb359ad0a89e3a86391221/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorSilentCastFailureFeedback`, `BehaviorStartCooldownOnToggleOff`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontAimFacingEnemy`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorDoNotAllowSpamProc`, `BehaviorDoNotCancelOnParry`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 30 (+0.8 per weapon damage increase) |
| Burst Damage | 35 (+0.95 per spirit) |
| Bullet Resist | -15 |
| Debuff Duration | 7 (+1 per duration) |
| Buff Duration | 0 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-8}`
- Tier 2: `{"ScorchDamage":60,"BonusFireRate":18,"BuffDuration":7}`
- Tier 3: `{"BulletResistReduction":-10,"BurstMarkStacks":1}`

### 4. Close The Deal

Internal key: `ability_deadpack_ultimate`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Grab an enemy and give them a hands-on demonstration, flying high into the air before crashing back to the ground.
> You and the participant take spirit damage over time while falling and spirit damage upon impact. Damage is increased to enemies under 50% health.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +0.5s Stun +8 Damage / Meter
Description source: [`github.deadlock-data.english.bd95f245ccb1`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/bd95f245ccb152cd4beb359ad0a89e3a86391221/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorDeactivateCrouchToggleOnCast`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 70 (+1 per spirit) |
| Falling Damage | 3 (+0.09 per spirit) |
| Stun Duration | 0.5 (+1 per duration) |
| Self Damage | 25 |
| Bonus Damage | 50 |

Upgrade deltas:
- Tier 1: `{"Damage":50.0}`
- Tier 2: `{"AbilityCooldown":-35.0}`
- Tier 3: `{"DamagePerMeter":8.0,"StunDuration":0.5}`

## Supporting Client Record

The YAML preserves the unbound `ability_deadpack_zip_line` record. It has no numbered hero binding or card, so it is not counted as a fifth ability and its runtime association is not inferred.

## Data Boundaries

- Valve's October 13 post establishes availability; client 6782 is the first complete reviewed configuration and is dated October 14, not October 13.
- Client 6774's selectable Danny entry had a null type, no bound abilities, and a provisional weapon. Those values are not used as release stats.
- The separate October 14 official update and the later client-6785 configuration are cited only as a boundary. Their later values are not applied to the client-6782 record.
- Some later note statements (charged-shot damage, airborne slow, and Rocket Jumping self-damage/type) do not have directly matching fields in the reviewed hero/card export; no independent runtime behavior is claimed.
- No October 13 raw changelog was found in the pinned archive. Later client changes, Street Brawl configuration, unrelated exports, and current-balance work remain separate.

Release evidence: [steam.news.deadman-danny-release.1846018067945303](https://store.steampowered.com/news/app/1422450/view/1846018067945303?l=english).
Client data: [github.deadlock-data.gameplay.bd95f245ccb1](https://github.com/deadlock-wiki/deadlock-data/tree/bd95f245ccb152cd4beb359ad0a89e3a86391221/data/json).
