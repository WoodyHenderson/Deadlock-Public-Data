---
id: hero.rat-king
title: Rat King
domain: heroes
topics: [hero, abilities]
aliases: []
summary: Rat King stats and abilities through the October 5 balance patch.
snapshot_id: deadlock-data-client-6753
current_as_of: "2026-10-05"
evidence_status: source_verified_with_patch_note_only_addenda
sources:
  - github.deadlock-data.gameplay.edb16660368e
  - github.deadlock-data.english.edb16660368e
  - github.deadlock-data.gameplay.0d46cdecfccf
  - steam.news.rat-king-release.1845383656387709
  - wiki.update.2026-10-02.181191
  - wiki.rat-king.180124
  - github.deadlock-data.changelog.2026-10-05.edb16660368e
---

# Rat King

Stats, cards and English descriptions below use **October 5/client 6753**.
Patch-note-only behavior is labeled separately; this is not an independent runtime test.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 800 |
| Health regeneration | 2/s |
| Move speed | 6.8m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Per-Boon Growth

Configured `LevelScaling` fields from the launch client; keys and values are preserved without deriving a live-match growth formula.

| Source field | Value per boon |
| --- | ---: |
| `BulletDamage` | 0.18 |
| `MaxHealth` | 50.0 |
| `PowerIncreases` | 1 |
| `TechPower` | 1.1 |
| `LightMeleeDamage` | 1.58 |
| `HeavyMeleeDamage` | 3.6656 |
| `DPS` | 1.8 |
| `SustainedDPS` | 1.1368 |


## Weapon

- Bullet damage: **6**
- Rounds/s: **5**; magazine: **24**; reload: **2.8s**
- Projectile speed: **203.2m/s**; falloff: **20–50m**
- Source DPS: **60**; sustained: **37.895**

## Abilities

### 1. Scrap Grenade

Internal key: `ability_ratking_scrap_grenade`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw a grenade of scrap that detonates multiple times, dealing bullet damage and applying slow.
> The grenade can be meleed to knock it away.

**Additional Info2 description** (`RequiresUpgradeIndex: 2`):

- The final detonation has a longer fuse but increased detonation radius, deals increased bullet damage and applies a stronger slow.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** Add an additional final Bigger Detonation

Description source: [`github.deadlock-data.english.edb16660368e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorProjectileFiredAsBullet`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Detonation Damage | 70 (+0.6 per weapon damage increase) |
| Move Speed | 20 (+0.08 per spirit) |
| Detonations | 3 |
| Detonation Radius | 8 (+1 per range) |
| Slow Duration | 4 (+1 per duration) |
| Cooldown | 26 (+1 per cooldown) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-8}`
- Tier 2: `{"DamagePerShrapnel":70}`
- Tier 3: `{"Detonations":1,"BigExplosionDamage":{"Value":300,"Scale":{"Value":1.0,"Type":"weapon_damage_increase"}},"BigExplosionRadius":{"Value":14,"Scale":{"Value":0.0254,"Type":"range"}},"BigExplosionSlowPercent":{"Value":0,"Scale":{"Value":0.12,"Type":"spirit"}}}`

Additional card fields (source `Info2`):

| Card field | Value |
| --- | ---: |
| Big Detonation Damage | 0 (+0 per weapon damage increase) |
| Big Detonation Radius | 0 (+0 per range) |
| Big Detonation Move Speed | 40 (+0 per spirit) |
| Slow Duration | 4 (+1 per duration) |

`RequiresUpgradeIndex`: 2


### 2. Rat Swarm

Internal key: `ability_ratking_ratnibble`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Call forth a swarm of rats that leap onto enemies, dealing spirit damage over time and reducing their bullet resist with every bite. The more rats are attached, the faster they will bite the target.
> Enemies can have multiple rats attached, but can shake off a rat early by performing a ground or air dash.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Increased Swarm Size +4s Debuff Duration
- **Tier 3:** +8 Damage and -1% Bullet Resist per Bite

Description source: [`github.deadlock-data.english.edb16660368e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorAlwaysPreviewRadius`, `BehaviorDisplaysDamageImpact`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage per Bite | 8 (+0.08 per spirit) |
| Bullet Resist per Bite | -1 |
| Bite Interval per Rat | 1 |
| Debuff Duration | 4 (+1 per duration) |
| MaxRats | 5 |
| Cast Range | 50 (+1 per range) |
| Charges | 1 (+1 per max charges) |
| Cooldown | 24 (+1 per cooldown) |
| Charge Delay | 8 (+1 per charge cooldown) |
| Duration | 6 (+1 per duration) |
| Radius | 10 |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1}`
- Tier 2: `{"RatSwarmCols":2,"RatSwarmRows":1,"RatSwarmWidth":100,"DebuffDuration":4}`
- Tier 3: `{"ArmorReductionPerBite":-1,"DamagePerBite":8}`


### 3. Royal Pestments

Internal key: `ability_ratking_ratarmor`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Adorn scrappy armor, gaining barrier based on your max health. As long as the armor holds, bullets have a chance to be deflected back towards the attacker.
> The barrier does not benefit from resists.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +7 Rat Count and +4s Duration
- **Tier 2:** -8s Cooldown +15% Bullet Return Chance
- **Tier 3:** Reduce all damage to a max of 250 +10% Max Health as Barrier

Description source: [`github.deadlock-data.english.edb16660368e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Max Health as Barrier | 15 |
| Bullet Return Chance | 15 (+0.1 per spirit) |
| Cooldown | 22 (+1 per cooldown) |
| Charge Delay | -1 |
| Duration | 6 (+1 per duration) |

Upgrade deltas:
- Tier 1: `{"AbilityDuration":4}`
- Tier 2: `{"ReturnFireChance":15,"AbilityCooldown":-8}`
- Tier 3: `{"MaxHealthPct":10,"MaxDamagePerHit":250}`


### 4. Rule, Ratannia!

Internal key: `ability_ratking_standard_bearer`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Charge up and summon the banner of Ratannia, granting all nearby allies increased move speed, immunity from slows, and reduced incoming damage while near the banner.

**Additional Info2 description**:

- Slam the banner into the ground causing the sewers below to violently erupt, dealing bullet damage while applying knockup and slow to all enemies in the area. Rats will swarm out of the sewers, applying Rat Swarm to enemies they hit.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +2m Move Speed
- **Tier 2:** +5s Flag Duration +8m Radius
- **Tier 3:** +150 Damage and +10% Damage Reduction

Description source: [`github.deadlock-data.english.edb16660368e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/edb16660368ef3b693a4ac6d525697f5570a4dce/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorAlwaysPreviewRadius`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Move Speed | 3 |
| Damage Reduction | 15 |
| Radius | 20 (+1 per range) |
| Cooldown | 160 (+1 per cooldown) |
| Charge Delay | -1 |
| Duration | 10 (+1 per duration) |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":2}`
- Tier 2: `{"FlagDuration":5,"Radius":8}`
- Tier 3: `{"Damage":150,"AllyDamageReduction":10}`

Additional card fields (source `Info2`):

| Card field | Value |
| --- | ---: |
| Damage | 200 (+1.2 per weapon damage increase) |
| Move Speed | 40 |
| Flag Duration | 12 (+1 per duration) |
| Radius | 20 (+1 per range) |


## October 5 Behavior Notes

- **Patch-note-only:** Scrap Grenade bounce-targeting bugs were fixed. Rule, Ratannia! now falls faster while charging; no numeric falling-speed delta is established.

## Release and Innate Behavior

Rat King was released October 2. That launch snapshot is not his current October 5 balance state.
The separately dated October 3 wiki describes crouching at a vent to enter/exit map tunnels, with no entry while in combat. It also says Spellbreaker does not proc on Royal Pestments barrier damage.
These are wiki descriptions, not tested launch behavior; tunnel vents are not identified as Steam Vents.
The YAML retains the incomplete client-6731 comparison as non-launch evidence and the distinct supporting ability/NPC records.

## Sources and Limits

- [October 5 patch changes](../../patches/2026-10-05-balance.md)
- [Pinned client data](https://github.com/deadlock-wiki/deadlock-data/tree/edb16660368ef3b693a4ac6d525697f5570a4dce/data)
- Raw source precision, flags and upgrade deltas are not a complete runtime simulation.
