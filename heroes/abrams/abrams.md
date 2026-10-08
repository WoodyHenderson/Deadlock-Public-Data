---
id: hero.abrams
title: Abrams
domain: heroes
topics: [hero]
aliases: []
summary: Abrams is a selectable Brawler hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - github.deadlock-data.hero-data.fc4f540f12e0
  - github.deadlock-data.ability-data.fc4f540f12e0
  - github.deadlock-data.ability-cards.fc4f540f12e0
  - github.deadlock-data.english.fc4f540f12e0
  - wiki.abrams.125768
---

# Abrams

Abrams is a currently selectable **Brawler** hero. Internal key: `hero_atlas`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 800 |
| Health regeneration | 1.5/s |
| Move speed | 6.4m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **3.6**
- Rounds/s: **1.5873**; magazine: **9**; reload: **0.3525s**
- Projectile speed: **609.6m/s**; falloff: **17–40m**
- Source DPS: **51.429**; sustained: **30.542**

## Abilities

### 1. Siphon Life

Internal key: `citadel_ability_bull_heal`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Drain health from nearby enemies, dealing spirit damage over time and healing for a portion of the damage dealt.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +2m Radius and +18 DPS with improved Spirit scaling

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCastableWhileBusy`, `BehaviorNoTarget`.

| Card field | Base value |
| --- | ---: |
| Damage Per Second | 22 (+0.6 per spirit) |
| Duration | 4 (+1 per duration) |
| Lifesteal | 70 (+1 per healing) |
| Lifesteal vs Non-Heroes | 35 (+1 per healing) |
| Cooldown | 42 (+1 per cooldown) |
| Charge Delay | -1 |
| Radius | 8 (+1 per radius) |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20.0}`
- Tier 2: `{"AbilityDuration":2}`
- Tier 3: `{"DPS":{"Value":18,"Scale":{"Value":0.12,"Type":"spirit"}},"Radius":2}`
### 2. Shoulder Charge

Internal key: `citadel_ability_bull_charge`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Charge forward, pulling enemies you hit. Pushing a hero into a wall applies stun.
> If you collide with a hero you move faster during your charge.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Applies +32% Slow for 3s
- **Tier 2:** On Wall Hit: +0.8s Stun Duration
- **Tier 3:** -18s Cooldown On Hero Collide: +1.5 Weapon Damage for 6s

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDontTriggerPostCastOnCastComplete`, `BehaviorMovement`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 30 (+1.4 per spirit) |
| Weapon Damage | 0 |
| Weapon Damage Duration | 0 |
| Cooldown | 33 (+1 per cooldown) |
| Charge Delay | -1 |
| Duration | 1.4 (+1 per duration) |

Upgrade deltas:
- Tier 1: `{"SlowPercent":32,"SlowDuration":3}`
- Tier 2: `{"StunDuration":0.8}`
- Tier 3: `{"AbilityCooldown":-18,"WeaponDamageBonus":1.5,"WeaponPowerIncreaseDuration":6}`
### 3. Infernal Resilience

Internal key: `citadel_ability_passive_beefy`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Gain bonus defensive attributes. Taking damage grants temporary regeneration for a portion of the damage taken.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +20% Debuff Resist and +9% Damage Regenerated

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

| Card field | Base value |
| --- | ---: |
| Damage Regenerated | 13 (+1 per healing) |
| Regeneration Time | 20 |
| Health Regen | 1 |
| Max Health | 0 |
| Melee Lifesteal | 0 |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusMaxHealth":200}`
- Tier 2: `{"MeleeLifesteal":18}`
- Tier 3: `{"RegenIncomingDamagePercent":8,"StatusResistancePercent":20}`

### 4. Seismic Impact

Internal key: `citadel_ability_bull_leap`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Leap high into the air before crashing into the ground, dealing spirit damage and applying stun.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** On cast, become Unstoppable for 5s and +6m Impact Radius

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorMovement`, `BehaviorDeactivateCrouchToggleOnCast`.

| Card field | Base value |
| --- | ---: |
| Immunity Duration | 0 |
| Damage | 100 (+2.325 per spirit) |
| Stun Duration | 1.6 (+1 per duration) |
| Cooldown | 215 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-30.0}`
- Tier 2: `{"StunDuration":0.8}`
- Tier 3: `{"ImmunityDuration":5,"ImpactRadius":6}`
## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Abrams](https://deadlock.wiki/Abrams?oldid=125768) article and generated data revisions. No wiki media is included.
