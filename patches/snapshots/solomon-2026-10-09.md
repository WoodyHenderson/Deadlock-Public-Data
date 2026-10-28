---
id: hero.solomon
title: Solomon
domain: heroes
topics: [hero, abilities, release]
aliases: []
summary: Solomon's October 9 release configuration from client 6774; incomplete client-6763 fields remain a separate pre-release comparison.
snapshot_id: deadlock-data-client-6774
current_as_of: "2026-10-09"
evidence_status: source_verified_with_official_release_confirmation
sources:
  - github.deadlock-data.gameplay.330a775230e8
  - github.deadlock-data.english.330a775230e8
  - github.deadlock-data.gameplay.8f2589cb4e64
  - github.deadlock-data.gameplay.18998ba13ff3
  - github.deadlock-data.gameplay.3b96422dbf31
  - steam.news.solomon-release.1846018067934643
---

# Solomon

Valve's [October 9 announcement](https://store.steampowered.com/news/app/1422450/view/1846018067934643?l=english) confirms Solomon is available in-game and names Setup Bishop, Kingside Knight, Rook Battery, and Develop Queen. This record uses the October 9 client 6774 configuration snapshot.

Client data and localized descriptions are generated source, not independent runtime tests. The incomplete client-6763 configuration is retained only in the adjacent YAML comparison and is not used for release stats.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 2/s |
| Move speed | 6.7m/s |
| Sprint bonus | 3.25m/s |
| Stamina | 2 |
| Light / heavy melee | 50 / 116 |

## Per-Boon Growth

Configured `LevelScaling` fields from client 6774; keys and values are preserved without deriving a live-match growth formula.

| Source field | Value per boon |
| --- | ---: |
| `BulletDamage` | 0.4 |
| `MaxHealth` | 40.0 |
| `PowerIncreases` | 1 |
| `TechPower` | 1.1 |
| `LightMeleeDamage` | 1.58 |
| `HeavyMeleeDamage` | 3.6656 |
| `DPS` | 0.8 |
| `SustainedDPS` | 0.45714 |


## Weapon

- Bullet damage: **30**
- Rounds/s: **2**; magazine: **8**; reload: **3s**
- Projectile speed: **355.6m/s**; falloff: **19.99–45.72m**
- Source DPS: **60**; sustained: **34.286**

## Abilities

### 1. Setup Bishop

Internal key: `ability_chessmaster_throwbishop`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Create a bishop that remains in place indefinitely.
> Move ( [ADS] ): Moves the bishop, applying a fading slow and dealing spirit damage to enemies it passes through. After a delay, activates diagonal squares that deal additional spirit damage when stepped on.
> Re-activate to recall all bishops, ending the ability.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +5m Move Distance +15% Fading Slow
- **Tier 2:** +1 Max Pieces Can Recast within 8s
- **Tier 3:** +1 Square Range Squares reduce Spirit Resist by -2.5%, stacking 10 times
Description source: [`github.deadlock-data.english.330a775230e8`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/330a775230e8f6b9dcea9e58260cabb433bd68b7/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Fading Move Speed | 30 |
| Impact Damage | 70 (+2 per spirit) |
| Damage | 25 (+0.64 per spirit) |
| Square Range | 2 |
| Move Distance | 12 (+0.23 per power increase, +1 per range) |
| Slow Duration | 3 (+1 per duration) |
| Move Cooldown | 3 (+1 per cooldown) |
| Spirit Resistance per Stack | 0 |
| Stack Duration | 0 (+1 per duration) |
| Max Stacks | 0 |
| Cast Range | 20 (+1 per range) |
| Cooldown | 12 (+1 per cooldown) |
| Charge Delay | -1 |
| Radius | 3.5 |

Upgrade deltas:
- Tier 1: `{"MoveDistance":5,"FadingSlowPercent":15}`
- Tier 2: `{"MaxPieces":1,"RecastWindow":8}`
- Tier 3: `{"TechArmorDamageReductionPerStack":-2.5,"MaxStacks":10,"StackDuration":10,"TileSteps":1}`

### 2. Kingside Knight

Internal key: `ability_chessmaster_knightbuff`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Promote an ally to be a knight, granting bonus stamina and barrier for a duration.
> If self-cast you develop yourself as king instead, granting double the barrier but no stamina.
> Move ( [ADS] ): Moves the piece, making it invulnerable during the duration before landing.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +80 Barrier +1 Stamina
- **Tier 3:** Can target two allies within radius. On Self: Remove all debuffs after a move
Description source: [`github.deadlock-data.english.330a775230e8`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/330a775230e8f6b9dcea9e58260cabb433bd68b7/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorProjectilePassThroughWorld`, `BehaviorAllowSelfCast`, `BehaviorUseInstantCastUnitTargetUi`, `BehaviorCanSetQuickCast`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Barrier | 80 (+0.8 per spirit) |
| Slow Resist | 0 |
| Stamina | 1 |
| King Move Distance | 7 (+0.14 per power increase, +1 per range) |
| Move Distance | 13 (+0.23 per power increase, +1 per range) |
| Slow Duration | 0 |
| Move Speed | 0 |
| Buff Duration | 7 (+1 per duration) |
| Cast Range | 28 (+1 per range) |
| Cooldown | 25 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-8}`
- Tier 2: `{"Stamina":1,"CombatBarrier":80}`
- Tier 3: `{"MaxPieces":1,"BonusTargetRadius":20,"RemoveDebuffs":1}`

### 3. Rook Battery

Internal key: `ability_chessmaster_forkpiece`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Release a pair of rooks that travel forward, dealing spirit damage and applying immobilize. If the rooks hit a wall, they reflect back in the opposite direction.
> Re-Activate: Split the rooks perpendicularly.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** On Hit: Reduce 25% Fire Rate for 5s
- **Tier 2:** On Hit: 5% Current Health as Damage
- **Tier 3:** +1 Wall Reflects -12s Cooldown +0.5s Immobilize Duration
Description source: [`github.deadlock-data.english.330a775230e8`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/330a775230e8f6b9dcea9e58260cabb433bd68b7/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorProjectile`, `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 50 (+1.3 per spirit) |
| Current Health | 0 |
| Move Speed | 0 |
| Immobilize Duration | 1 (+1 per duration) |
| Debuff Duration | 0 |
| Fire Rate | 0 |
| Slow Duration | 0 |
| Wall Reflects | 1 |
| Cooldown | 33 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"FireRateSlow":25,"DebuffDuration":5}`
- Tier 2: `{"CurrentHealthPercent":5}`
- Tier 3: `{"AbilityCooldown":-12,"ImmobilizeDuration":0.5,"MaxReflectCount":1}`

### 4. Develop Queen

Internal key: `ability_chessmaster_queen`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Summon a queen that crashes down, dealing spirit damage in an area. After a delay, the queen releases squares in straight lines that deal spirit damage again and apply stun.
> Move ( [ADS] ): The queen leaps to the target location, dealing the same effects again.
> Re-activate to recall the queen early, ending the ability.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** +15% Slow. Checkmates heroes below 200 health, executing them.
- **Tier 3:** +2 Moves +1 Square Range
Description source: [`github.deadlock-data.english.330a775230e8`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/330a775230e8f6b9dcea9e58260cabb433bd68b7/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorTargetThroughWalls`, `BehaviorCanSetQuickCast`.

| Card field | Base value |
| --- | ---: |
| Damage | 120 (+1.4 per spirit) |
| Checkmate Threshold | 0 (+0 per power increase) |
| Stun Duration | 1.25 (+1 per duration) |
| Square Range | 3 |
| Move Distance | 16 (+0.23 per power increase, +1 per range) |
| Move Cooldown | 5 (+1 per cooldown) |
| Additional Moves | 2 |
| Move Speed | 15 |
| Slow Duration | 1.5 (+1 per duration) |
| Cast Range | 30 (+1 per range) |
| Cooldown | 210 (+1 per cooldown) |
| Charge Delay | -1 |

Upgrade deltas:
- Tier 1: `{"AbilityCooldown":-40}`
- Tier 2: `{"CheckmateThreshold":{"Value":200,"Scale":{"Value":5,"Type":"power_increase"}},"SlowPercent":15}`
- Tier 3: `{"TileSteps":1,"QueenBonusMoves":2}`

## Supporting Client Records

The YAML preserves three unnumbered trigger ability records and the `citadel_chesspiece_bishop` / `citadel_chesspiece_queen` NPC configurations. They are supporting generated data, not additional hero slots, standard roster NPCs, or placement evidence.

## Data Boundaries

- The release date comes from Valve's announcement; client 6774 is the dated source configuration, not proof of every runtime interaction.
- Client 6763 marked Solomon selectable but had no bound abilities and a provisional weapon/configuration; those values are not presented as release stats.
- The first complete candidate is client 6769; its version-file time has no declared timezone and is not compared directly with the UTC announcement. The reviewed Solomon fields match client 6774.
- Street Brawl item-bucket additions and unrelated convar/localization changes are outside the scope of this standard hero release record and are not presented as Solomon balance changes.
- No October 9 raw changelog was found in the reviewed upstream archive. Later client data and October 14+ updates are outside this snapshot.

Release evidence: [steam.news.solomon-release.1846018067934643](https://store.steampowered.com/news/app/1422450/view/1846018067934643?l=english).
Client data: [github.deadlock-data.gameplay.330a775230e8](https://github.com/deadlock-wiki/deadlock-data/tree/330a775230e8f6b9dcea9e58260cabb433bd68b7/data/json).
