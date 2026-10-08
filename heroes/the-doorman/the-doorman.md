---
id: hero.the-doorman
title: The Doorman
domain: heroes
topics: [hero]
aliases: []
summary: The Doorman is a selectable Mystic hero; this record covers base stats, weapon data, and abilities.
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - github.deadlock-data.hero-data.fc4f540f12e0
  - github.deadlock-data.ability-data.fc4f540f12e0
  - github.deadlock-data.ability-cards.fc4f540f12e0
  - github.deadlock-data.english.fc4f540f12e0
  - wiki.the-doorman.125570
---

# The Doorman

The Doorman is a currently selectable **Mystic** hero. Internal key: `hero_doorman`. The canonical YAML preserves all generated weapon, ability-card, upgrade, behavior, and hidden fields.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 755 |
| Health regeneration | 1/s |
| Move speed | 7.9m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 3 |
| Light / heavy melee | 50 / 116 |

## Weapon

- Bullet damage: **24**
- Rounds/s: **1.5873**; magazine: **8**; reload: **2.4s**
- Projectile speed: **203.2m/s**; falloff: **19.99–57.51m**
- Source DPS: **38.095**; sustained: **25.806**

## Abilities

### 1. Call Bell

Internal key: `ability_doorman_bomb`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Throw out a call bell that deals spirit damage on impact. After a short delay it explodes, dealing additional spirit damage and causing affected enemies to suffer reduced weapon accuracy and movement slow.
> Can be shot to detonate early.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +1 Charge
- **Tier 2:** +30 Impact Damage +40 Explosion Damage
- **Tier 3:** +4.5m Radius +26s Bell Lifetime Improved Scaling

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Impact Damage | 40 (+0.7 per spirit) |
| Charges | 1 (+1 per max charges) |
| Cooldown | 18 (+1 per cooldown) |
| Charge Delay | 7 (+1 per charge cooldown) |
| Duration | 4 (+1 per duration) |
| Radius | 5.5 (+1 per radius) |

Upgrade deltas:
- Tier 1: `{"AbilityCharges":1}`
- Tier 2: `{"ImpactDamage":30,"ExplosionDamage":40}`
- Tier 3: `{"ProjectileFuse":26,"Radius":4.5,"ImpactDamage":{"Value":0,"Scale":{"Value":0.35,"Type":"spirit"}},"ExplosionDamage":{"Value":0,"Scale":{"Value":0.35,"Type":"spirit"}}}`
### 2. Doorway

Internal key: `ability_doorman_doorway`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Place two connected doors in the world. Players and most projectiles entering one door will exit out through the other. The doors will close at the end of the duration.
> The two doors must be placed within the doorway distance of each other.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** Grants a Barrier first time traveling through doors
- **Tier 3:** +30m Cast Range. +40m Doorway Distance and scales with Spirit Power.

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorAllowAltCast`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Doorway Distance | 65 (+0 per spirit, +1 per range) |
| Barrier | 0 (+0 per spirit) |
| Barrier Duration | 0 |
| Cast Range | 50 (+1 per range) |
| Cooldown | 45 (+1 per cooldown) |
| Charge Delay | -1 |
| Duration | 15 (+1 per duration) |

Upgrade deltas:
- Tier 1: `{"AbilityDuration":20}`
- Tier 2: `{"CombatBarrier":{"Value":250,"Scale":{"Value":1.5,"Type":"spirit"}},"BarrierDuration":12}`
- Tier 3: `{"DoorwayDistance":{"Value":40,"Scale":{"Value":0.15,"Type":"spirit"}},"AbilityCastRange":30}`
### 3. Luggage Cart

Internal key: `ability_doorman_luggage_cart`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Send out a luggage Cart that deals spirit damage and pulls enemy heroes along its path.
> Can be alt cast with [Alt Cast] to target friendly heroes instead.

> If the cart collides with a wall while dragging an enemy, it will deal bonus damage to the targets.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +25m Cast Range +75 Damage on wall impact
- **Tier 3:** -15s Cooldown and 1.25s stun on wall impact

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorAllowSelfCast`, `BehaviorProjectilePassThroughWorld`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Cart Damage | 60 (+0.75 per spirit) |
| Cast Range | 20 (+1 per range) |
| Cooldown | 30 (+1 per cooldown) |
| Charge Delay | -1 |
| Duration | 6 (+1 per duration) |

Upgrade deltas:
- Tier 1: `{"CartDamage":80}`
- Tier 2: `{"AbilityCastRange":25,"WallImpactDamage":{"Value":75,"Scale":{"Value":0.6,"Type":"spirit"}}}`
- Tier 3: `{"StunDuration":1.25,"AbilityCooldown":-15}`
### 4. Hotel Guest

Internal key: `ability_doorman_hotel`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Send the target's physical body to be a guest at the Baroness Hotel. The guest is to promptly make their way to the exit elevator, where they'll be sent back to their original position.
> A stay at the Baroness Hotel is paid for in spirit damage. Failure to check-out on time costs additional spirit damage.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** 1 Stamina Drain and -20 Cooldown
- **Tier 2:** +150 Damage +1.5s Stun on Failure to Check Out
- **Tier 3:** Unstoppable while the Baroness is occupied. 15s Cooldown on Failure to Check Out.

Description source: [`github.deadlock-data.english.fc4f540f12e0`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/fc4f540f12e019a6a2a422e0818917a4eedaf881/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorCannotCancelDuringChannel`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 75 (+1 per spirit) |
| Damage | 125 (+1.5 per spirit) |
| Cast Range | 7 (+1 per range) |
| Cooldown | 140 (+1 per cooldown) |
| Charge Delay | -1 |
| Duration | 6.5 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-20,"StaminaDrain":1}`
- Tier 2: `{"Damage":150,"LateCheckoutDamage":150,"LateCheckoutStun":1.5}`
- Tier 3: `{"UnstoppableWhileHotelOccupied":1,"LateCheckoutCooldown":15}`
## Data Boundaries

Values above are retrieval highlights. Use the adjacent YAML for calculations. It retains raw generated fields without inventing units. Ability descriptions are resolved from pinned English localization data; numeric tables remain separate and are not overwritten by tooltip prose.

## Source Notes

Adapted from the pinned [The Doorman](https://deadlock.wiki/The_Doorman?oldid=125570) article and generated data revisions. No wiki media is included.
