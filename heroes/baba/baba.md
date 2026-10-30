---
id: hero.baba
title: Baba
domain: heroes
topics: [hero, abilities, forms]
aliases: []
summary: Current client-6785 Baba configuration with the separate October 14 update and dated patch-note-only behavior.
snapshot_id: deadlock-data-client-6785
current_as_of: "2026-10-14"
evidence_status: source_verified_with_official_release_confirmation_and_patch_note_only_behavior
sources:
  - github.deadlock-data.gameplay.3aab395a1392
  - github.deadlock-data.english.3aab395a1392
  - github.deadlock-data.gameplay.69b3ca700c80
  - github.deadlock-data.gameplay.edb16660368e
  - steam.news.baba-release.1845383656397580
  - wiki.baba.184291
  - wiki.baba.184568
  - github.deadlock-data.gameplay.5799055efcc7
  - github.deadlock-data.gameplay.be5fb3ee934a
  - github.deadlock-data.gameplay.7fd1dfeb502a
  - github.deadlock-data.gameplay.bd95f245ccb1
  - steam.news.deadman-danny-oct14-update.1846651706676198
  - github.deadlock-data.raw-changelog.2026-10-14.3aab395a1392
---

# Baba

Valve announced Baba as available on **October 6, 2026**. This current balance record uses **client 6785** after the separate October 14 update; the client-6759 release snapshot remains historical.
The client still says `InDevelopment: true`. That conflicting flag is preserved, not treated as proof that the officially released hero is unavailable.

## Base Stats

| Stat | Value |
| --- | ---: |
| Maximum health | 780 |
| Health regeneration | 2.5/s |
| Move speed | 6.5m/s |
| Sprint bonus | 1.6m/s |
| Stamina | 2 |
| Light / heavy melee | 50 / 116 |

- Configured base Spirit Resist: **8%**; source `SpiritScaling.TechResist`: **0.1**. No complete stacking formula is inferred.
- Configured base Bullet Resist: **-7%** (client `BulletResist`).
- Source critical-damage bonus: **-20%**, not the full resulting critical-hit multiplier.

## Per-Boon Growth

Configured `LevelScaling` fields from client 6785; keys and values are preserved without deriving a live-match growth formula.

| Source field | Value per boon |
| --- | ---: |
| `BulletDamage` | 0.41 |
| `MaxHealth` | 45.0 |
| `PowerIncreases` | 1 |
| `TechPower` | 1.1 |
| `LightMeleeDamage` | 0.7 |
| `HeavyMeleeDamage` | 1.624 |
| `DPS` | 1.3226 |
| `SustainedDPS` | 0.86014 |


## Weapon

- Bullet damage: **8.8**
- Rounds/s: **3.2258**; magazine: **15**; reload: **2.5s**
- Projectile speed: **177.8m/s**; falloff: **15–42m**
- Source DPS: **28.387**; sustained: **18.462**

BulletsPerShot is 3, AmmoConsumedPerShot is 1, and HitOnceAcrossAllBullets is true. Preserve the source DPS; do not multiply it by three or infer three hits/procs per target.

## Abilities

### 1. Threadsap

Internal key: `ability_baba_bubbling_brew`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Weave a scraggly thread that follows your crosshair before bursting along its path, dealing spirit damage and stealing enemy Spirit, increased in effectiveness for Baba.
> While holding stolen Spirit, Baba deals bonus spirit damage with every bullet.

**Upgrade descriptions** (where supplied by the source):

- **Tier 2:** -12s Cooldown +8s Debuff Duration
- **Tier 3:** +1 Charge On Hit: Pull enemies 7m

Description source: [`github.deadlock-data.english.3aab395a1392`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/3aab395a139254c12179f0f829f7488c55da2022/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorDisplaysDamageImpact`, `BehaviorDontInterruptSlideOnCast`.

| Card field | Base value |
| --- | ---: |
| Spirit Stolen per Hit | 10 (power increase coefficient 0.9) |
| Stolen Spirit Effectiveness | 175 |
| Spirit Damage Per Bullet | 8 (+0.26 per spirit) |
| Debuff Duration | 22 (duration coefficient 1) |
| Max Spirit Stolen | 45 (power increase coefficient 2) |
| Damage | 50 |

Upgrade deltas:
- Tier 1: `{"MagicDamagePerBullet":8}`
- Tier 2: `{"AbilityCooldown":-12,"DebuffDuration":8}`
- Tier 3: `{"AbilityCharges":1,"PullDistance":7}`

### 2. Granny Long Legs

Internal key: `ability_baba_bench_run`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Your bench's legs extend, granting bonus move speed, higher jumps, Debuff Resistance and Melee Resistance.
> Light Melee: Perform a kick that knocks enemies back.
> Heavy Melee: Perform a ground pound that applies knockup, slow, and deals spirit damage.
> Hold [Crouch] to charge a high jump, release to jump.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +2.5m Move Speed
- **Tier 2:** -7s Cooldown
- **Tier 3:** +15% Resists +50% Melee Lifesteal

Description source: [`github.deadlock-data.english.3aab395a1392`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/3aab395a139254c12179f0f829f7488c55da2022/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorNoTarget`, `BehaviorNonCombat`, `BehaviorCastableWhileBusy`.

| Card field | Base value |
| --- | ---: |
| Move Speed | 5 |
| Debuff Resist | 30 |
| Melee Resist | 30 |
| Light Melee Spirit Damage | 0 (+0 per spirit) |
| Light Melee Knockback | 10 (range coefficient 1) |
| Heavy Melee Damage | 75 (+0.6 per spirit) |
| Heavy Melee Movement Slow | 50 |
| Heavy Melee Slow Duration | 4 (duration coefficient 1) |

Upgrade deltas:
- Tier 1: `{"BonusMoveSpeed":2.5}`
- Tier 2: `{"AbilityCooldown":-7}`
- Tier 3: `{"StatusResistancePercent":15,"MeleeResist":15,"MeleeLifesteal":50}`

Granny Long Legs is an ability-driven form, not another roster hero. Light and heavy melee behavior differs; see the dated wiki notes below. Jump-height/force fields remain raw source units in YAML.

### 3. Baba's Brew

Internal key: `ability_baba_hexing_brew`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Brew a pot of tea that applies a magical effect in an area when thrown, cycling over time between a soothing barrier, Silence, or scalding burn that deals spirit damage over time and reduces spirit resist.
> Press [ADS] to pause or resume brewing.

**Upgrade descriptions** (where supplied by the source):

- **Tier 3:** +33.33% Brew Effectiveness

Description source: [`github.deadlock-data.english.3aab395a1392`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/3aab395a139254c12179f0f829f7488c55da2022/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorProjectileFiredAsBullet`, `BehaviorCooldownOnChannelEnd`, `BehaviorDontInterruptSlideOnCast`, `BehaviorHoldsAtMaxChannel`.

| Card field | Base value |
| --- | ---: |
| No card-visible fields | not supplied |

Upgrade deltas:
- Tier 1: `{"Radius":3}`
- Tier 2: `{"AbilityCooldown":-14}`
- Tier 3: `{"BrewEffectiveness":33.33,"DamagePerSecond":{"Value":1.3333,"Scale":{"Value":1.3333,"Type":"spirit","Multiply":true},"Multiply":true},"CombatBarrier":{"Value":1.3333,"Scale":{"Value":1.3333,"Type":"spirit","Multiply":true},"Multiply":true},"SilenceDuration":{"Value":1.3333,"Multiply":true},"SpiritResistReduction":{"Value":1.3333,"Multiply":true}}`

#### Soothing Brew

| Card field | Base value |
| --- | ---: |
| Barrier | 90 (+0.7 per spirit) |
| Barrier Duration | 8 (duration coefficient 1) |

#### Silencing Brew

| Card field | Base value |
| --- | ---: |
| Silence Duration | 3 (duration coefficient 1) |

#### Scalding Brew

| Card field | Base value |
| --- | ---: |
| Burn DPS | 12 (+0.152 per spirit) |
| Burn Spirit Resist | -15 |
| Burn Duration | 8 (duration coefficient 1) |

Also called **Baba's Brews** in official/wiki prose.

Tier 3 remains +33.33% Brew Effectiveness. SilenceDuration and SpiritResistReduction are encoded as Value: 1.3333 with Multiply: true in the regenerated client-6759 export and retained through 6763. This corrects the exported representation; it does not establish an October 7 runtime buff or +33.33 seconds of silence.

### 4. Feed The Birds

Internal key: `ability_baba_ultimate_2`.

<!-- ability-descriptions:start -->
**Description** (pinned English game text):

> Cover targets in front of you with bread, adding a stacking slow .
> When the channel ends a flock of pigeons bombard the targets, dealing spirit damage and hexing each target into a pigeon, increasing in both damage and duration based on bread count.

**Upgrade descriptions** (where supplied by the source):

- **Tier 1:** +4m Cast Range +32% Max Slow
- **Tier 3:** +125 Max Damage +1.5 Spirit Scaling +0.5s Max Duration

Description source: [`github.deadlock-data.english.3aab395a1392`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/3aab395a139254c12179f0f829f7488c55da2022/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCooldownOnChannelEnd`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorShowCastRangeAsSatSphereWhileCasting`.

| Card field | Base value |
| --- | ---: |
| Max Damage | 450 (+1.6 per spirit) |
| Max Pigeon Duration | 2.75 (duration coefficient 1) |
| Time To Max Stacks | 3.5 |
| Max Slow | 32 |

Upgrade deltas:
- Tier 1: `{"MaxSlow":32,"AbilityCastRange":4}`
- Tier 2: `{"AbilityCooldown":-55}`
- Tier 3: `{"BarrageMaxDamage":{"Value":125,"Scale":{"Value":1.5,"Type":"spirit"}},"HexDuration":0.5}`

## October 14 Balance Update

The post-update client-6785 record changes `SpiritScaling.TechResist` from 0.12 to 0.1 and adds `BulletResist: -7`. Threadsap and Granny Long Legs cooldowns, plus Baba's Brew cooldown/barrier fields, are listed in the canonical YAML. These are configured source values; the separate patch-note behavior below is not a runtime test.

[Official October 14 update note](https://store.steampowered.com/news/app/1422450/view/1846651706676198?l=english).

## October 14 Patch-Note-Only Behavior

- Threadsap's enemy Spirit reduction ends when Baba dies.
- Repeated airborne Granny Long Legs light melees have diminishing forward momentum; its light-melee upward launch is reduced; heavy-melee ground pound no longer gains horizontal speed when landing on slopes.

These are note statements without directly matching fields in the reviewed standard configuration, not independent runtime observations.
## Dated Wiki Behavior

These descriptions supplement the client record; they are not independent runtime tests.

**October 6 article:** Granny Long Legs' heavy ground pound can hit Sinner's Sacrifice.

**October 8 article — later descriptions, not backdated:**

### Granny Long Legs

- The ground pound has normal heavy-melee interactions, including Sinner's Sacrifice, Powerups, the Rejuvenator and Graves' Borrowed Decree.
- The light kick can be parried and stuns Baba; the ground pound can be parried without stunning her.
- The heavy-melee cooldown is described as about three times as long while active; no exact cooldown is established by that approximation.
- Crouch charges the high jump instead of sliding or mantle gliding. Baba must be grounded to begin charging and activate the high jump.
- Walking off a ledge and attempting the high jump midair instead performs a normal jump and clears the high-jump charge.
- If the ability expires while charging a high jump, the jump executes even midair and the ability extends until landing or three seconds pass; light and heavy melee are unavailable during that extension.
- Melee charge-up/animation interrupts shooting, but the high jump does not. Melee interrupts reload; heavy melee does so at the end of the ground-pound animation.

### Feed The Birds

- The article says stun and silence do not stop activation; death interrupts charge-up, but effects already activated before death still trigger.
- Targets with bread charges remain affected even if they leave the area before activation.
- The article says Divine Barrier prevents all effects when activated during or after channeling; this is an item-interaction claim, not an independent runtime test.

### Street Brawl

- The article reports no Baba-specific ability modifications beyond global Street Brawl changes. This is separately dated wiki context, not a launch-day mode test.

## Evidence Boundaries

- This current configuration uses post-update client 6785 / source revision 11132425. The October 6 release snapshot and client-6763/6759 history remain separate; client 6782 is the immediate pre-update comparison.
- The official October 14 note was published October 15 UTC. Its stated behavior is patch-note intent, not independent runtime evidence.
- The client-6785 Street Brawl override is stored separately from standard Baba ability data; the earlier export's missing mode record does not establish an earlier runtime value.
- The source TechResist value and SpiritScaling.TechResist coefficient are distinct fields; no full in-match resistance calculation is inferred.
- The ultimate retains source lock-on/ramp fields without inferring an exact hit-count or damage formula from their names.
- The two supporting melee/throw records in YAML are not extra numbered abilities.

[Official release announcement](https://store.steampowered.com/news/app/1422450/view/703281025618282871) · [October 6 article](https://deadlock.wiki/Baba?oldid=184291) · [October 8 article](https://deadlock.wiki/Baba?oldid=184568)
