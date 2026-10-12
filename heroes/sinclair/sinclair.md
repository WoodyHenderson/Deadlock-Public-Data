---
id: hero.sinclair
title: Sinclair
domain: heroes
topics: [hero, abilities]
aliases: []
summary: Sinclair stats and abilities through the October 5 balance patch.
snapshot_id: deadlock-data-client-6753
current_as_of: "2026-10-05"
evidence_status: source_verified_with_patch_note_only_addenda
sources:
  - wiki.sinclair.124939
  - github.deadlock-data.gameplay.edb16660368e
  - github.deadlock-data.english.edb16660368e
  - github.deadlock-data.changelog.2026-10-05.edb16660368e
---

# Sinclair

Stats, cards and English descriptions below use **October 5/client 6753**.
Patch-note-only behavior is labeled separately; this is not an independent runtime test.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 730 |
| Health regeneration | 1/s |
| Move speed | 7.2m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Per-Boon Growth

Configured `LevelScaling` fields from the launch client; keys and values are preserved without deriving a live-match growth formula.

| Source field | Value per boon |
| --- | ---: |
| `BulletDamage` | 0.55 |
| `BulletDamageAltFire` | 0.55 |
| `MaxHealth` | 38.0 |
| `PowerIncreases` | 1 |
| `TechPower` | 1.3 |
| `LightMeleeDamage` | 1.58 |
| `HeavyMeleeDamage` | 3.6656 |
| `DPS` | 1.4966 |
| `SustainedDPS` | 1.0501 |


## Weapon

- Bullet damage: **16.5**
- Rounds/s: **2.7211**; magazine: **16**; reload: **2.5s**
- Projectile speed: **300m/s**; falloff: **20–60m**
- Source DPS: **44.898**; sustained: **31.504**

## Abilities

### 1. Vexing Bolt

Internal key: `ability_magician_magicbolt`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Fire a bolt of magic that deals Damage, increasing as it travels. If you have an Assistant, they also cast Vexing Bolt at reduced damage.
> Press [Ability 1] to redirect the bolt towards your crosshairs.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Bolts apply -25% Fire Rate for 5s.
- **Tier 3:** +126 Max Damage. +50% Assistant Damage.

Description source: [`github.deadlock-data.english.edb16660368e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorProjectile`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorTargetThroughWalls`, `BehaviorCleaveDisabled`, `BehaviorCooldownOnChannelEnd`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Minimum Damage | 60 (+0.93 per spirit) |
| Max Damage | 120 (+1.86 per spirit) |
| Assistant Damage | 50 |
| Time for Max Damage | 2 |
| Fire Rate | 0 |
| Debuff Duration | 0 |
| Cast Range | 500 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Cooldown | 24 (+1 per cooldown) |
| Charge Delay | 3 (+1 per charge cooldown) |
| Radius | 3.25 (+1 per radius) |

Upgrade deltas:
- Tier 1: `{"FireRateSlow":25,"DebuffDuration":5}`
- Tier 2: `{"AbilityCooldown":-13}`
- Tier 3: `{"MaxDamage":126.0,"CloneDamagePercentage":50.0}`


### 2. Spectral Assistant

Internal key: `ability_magician_cloneturret`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Summon an Assistant at the targeted location. The Assistant attacks whenever you fire your weapon, dealing Damage.
> While the Assistant is out, you can press [Ability 2] to swap positions with your Assistant.
> Casting Spectral Assistant also reloads your weapon.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +7s Duration & 5m Range
- **Tier 3:** +60% Fire Rate and +12.6 Assistant Damage

Description source: [`github.deadlock-data.english.edb16660368e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorPreventBotUsage`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 15 (+0.36 per spirit) |
| Duration | 6 (+1 per duration) |
| Max Swaps | 2 |
| Cast Range | 15 (+1 per range) |
| Cooldown | 40 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-10}`
- Tier 2: `{"AbilityDuration":7,"AbilityCastRange":5,"LeashRadius":5}`
- Tier 3: `{"BonusFireRate":60,"Damage":12.6}`


### 3. Rabbit Hex

Internal key: `ability_magician_animalhexarea`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Hex a target area and transform all enemies into a Rabbit for a limited duration.
> Rabbits are small and move faster, but take increased Damage and are unable to perform most actions.
> Hex does not interrupt abilities.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +7% Damage Amp and +2m Radius

Description source: [`github.deadlock-data.english.edb16660368e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 0 |
| Hex Duration | 2 (+1 per duration) |
| Damage Amp | 15 (+0.0558 per spirit) |
| Move Speed bonus | 36 |
| Radius | 6 (+1 per range) |
| Cast Range | 24 (+1 per range) |
| Cooldown | 26 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-10}`
- Tier 2: `{"HexDuration":1}`
- Tier 3: `{"Radius":2,"DamageAmpPercentage":7}`


### 4. Audience Participation

Internal key: `ability_magician_copyult`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Copy the Ultimate of an enemy hero for a limited time. Reactivating the ability will use the Copied Ultimate instead.
> Copies will inherit this ability's upgrade points.
> Audience Participation will also copy the cooldown.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Upgrade the Copy.
- **Tier 2:** Upgrade the Copy AGAIN!
- **Tier 3:** Upgrade the Copy ONCE AGAIN!

Description source: [`github.deadlock-data.english.edb16660368e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectilePassThroughWorld`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Copy Duration | 9 (+1 per duration) |
| Copied Cooldown | 60 |
| Cast Range | 20 (+1 per range) |
| Cooldown | 85 (+1 per cooldown) |
| Charge Delay | -1 |


## October 5 Behavior Notes

- **Patch-note-only:** Spectral Assistant gun falloff changed from approximately 25–61m to 20–60m. No separate assistant falloff field is exposed in the inspected ability export; do not infer weapon inheritance.
- Vexing Bolt's `BossDamageScale: 0.5` agrees with the patch note that it deals half damage to objectives. This does not enumerate every valid objective target.

## Sources and Limits

- [October 5 patch changes](../../patches/2026-10-05-balance.md)
- [Pinned client data](https://github.com/deadlock-wiki/deadlock-data/tree/edb16660368ef3b693a4ac6d525697f5570a4dce/data)
- Raw source precision, flags and upgrade deltas are not a complete runtime simulation.
