---
id: hero.victor
title: Victor
domain: heroes
topics: [hero]
aliases: []
summary: Victor is a selectable Brawler hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - github.deadlock-data.english.311b2e8d895e
  - wiki.victor.125760
  - wiki.data-hero-data.108817
  - wiki.data-ability-data.114011
  - wiki.data-ability-cards.114010
---

# Victor

Victor is a currently selectable **Brawler** hero. Internal key: `hero_frank`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 800 |
| Health regeneration | 1.5/s |
| Move speed | 6.3m/s |
| Sprint bonus | 1.1m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **12**
- Rounds/s: **5.0505**; magazine: **24**; reload: **2.4s**
- Projectile speed: **203.2m/s**; falloff: **19.99–57.51m**
- Source DPS: **70.175**; sustained: **44.28**

## Abilities

### 1. Pain Battery

Internal key: `ability_frank_shocktarget2`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Taking any damage passively charges up your Pain Battery.
> Once full, activating the ability fires multiple shocking bolts, dealing spirit damage once per target.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Hit: Apply 40% Slow for 2s
- **Tier 3:** On Hero Hit: Heal for 15% of your missing health and increased Spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorShowCastRangeAsSatSphereWhileCasting`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 100 (+1.6 per spirit) |
| Move Speed | 0 |
| Missing Health as Healing | 0 (+1 per healing) |
| Cooldown | 2 (+1 per cooldown) |
| Cast Range | 28 (+1 per range) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"SlowPercent":40,"SlowDuration":"2s"}`
- Tier 2: `{"Damage":50}`
- Tier 3: `{"MissingHealthPercentHeal":15,"Damage":{"Value":0,"Scale":{"Value":0.6,"Type":"spirit"}}}`

### 2. Jumpstart

Internal key: `ability_frank_selfzap`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Deal spirit damage to yourself. Then, gain bonus regeneration and bonus move speed, decaying over time.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +70 Total HP Regen and -8s Cooldown
- **Tier 3:** +1 Charge +50% Debuff Resistance Increases spirit scaling

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Current Health | 15 |
| Total HP Regen | 100 (+1.2 per spirit) |
| Move Speed | 3 |
| Debuff Resist | 0 |
| Cooldown | 30 (+1 per cooldown) |
| Duration | 4.5 (+1 per duration) |
| Charges | 1 (+1 per max charges) |
| Charge Delay | 8 (+1 per charge cooldown) |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":3}`
- Tier 2: `{"TotalHealthRegen":70,"AbilityCooldown":-8}`
- Tier 3: `{"AbilityCharges":1,"TotalHealthRegen":{"Value":0,"Scale":{"Value":0.9,"Type":"spirit"}},"StatusResistancePercent":50}`

### 3. Aura of Suffering

Internal key: `ability_frank_painaura`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Unleash pain, dealing spirit damage over time to both enemies and yourself.
> The damage continues to increase the longer the ability is channeled, up to a maximum amount.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** Enemies receive 25% Move and Dash Slow
- **Tier 2:** +6 Min DPS and +34 Max DPS
- **Tier 3:** +1m Radius Enemies take +15% Damage

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorStartCooldownOnToggleOff`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDoNotAllowSpamProc`, `BehaviorCanCastOnZipline`.

| Card field | Base value |
| --- | ---: |
| Minimum DPS | 13 (+0.15 per spirit) |
| Max DPS | 58 (+0.72 per spirit) |
| Move Speed | 0 |
| Damage | 0 |
| Damage Taken | 0 |
| Self Damage | 70 |
| Debuff Resist | 0 |
| Cooldown | 2 (+1 per cooldown) |
| Duration | 8 |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"SlowPercent":25,"EnemyDashSlowPercent":-25,"DebuffDuration":0.5}`
- Tier 2: `{"MinDps":6,"MaxDPS":34}`
- Tier 3: `{"IncomingDamagePercent":15,"Radius":1}`

### 4. Shocking Reanimation

Internal key: `ability_frank_revive`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Release a wave after taking lethal damage, applying a diminishing slow.
> After a brief channel you reanimate, dealing spirit damage and applying stun to nearby enemies.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** While On Cooldown: Gain +15% Fire Rate and 6 Spirit Damage per Bullet
- **Tier 3:** +175 Damage +1.5 Stun -95s Cooldown

Description source: [`github.deadlock-data.english.311b2e8d895e`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/311b2e8d895eec837441ff3e29b7d7581a61768c/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorCastEvenIfBusyAndExclusive`, `BehaviorChannelled`, `BehaviorCastableWhileBusy`, `BehaviorNotSilencable`, `BehaviorNoTarget`, `BehaviorCastableWhileCmdRestricted`, `BehaviorDisplaysDamageImpact`, `BehaviorCanCastWhileDead`.

| Card field | Base value |
| --- | ---: |
| Rebirth Health | 50 |
| Barrier | 0 |
| Damage | 200 (+2 per spirit) |
| Stun Duration | 1.5 (+1 per duration) |
| Bullet Resist | 0 |
| Spirit Resist | 0 |
| Damage per Bullet | 0 (+0 per spirit) |
| Fire Rate | 0 |
| Move Speed | 120 |
| Slow Duration | 3 (+1 per duration) |
| Cooldown | 240 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"BonusDamagePerBullet":{"Value":6,"Scale":{"Value":0.06,"Type":"spirit"}},"BonusFireRate":15}`
- Tier 2: `{"RespawnHealthPercent":50}`
- Tier 3: `{"Damage":175,"StunDuration":1.5,"AbilityCooldown":-95}`

## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [Victor](https://deadlock.wiki/Victor?oldid=125760) article and generated data revisions. No wiki media is included.
