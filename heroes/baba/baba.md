---
id: hero.baba
title: Baba
domain: heroes
topics: [hero, abilities, forms]
aliases: []
summary: Baba stats, four abilities and brew variants checked through October 7, with later wiki interactions explicitly dated.
snapshot_id: deadlock-data-client-6763
current_as_of: "2026-10-07"
evidence_status: source_verified_with_official_release_confirmation_and_dated_wiki_context
sources:
  - github.deadlock-data.gameplay.8f2589cb4e64
  - github.deadlock-data.english.8f2589cb4e64
  - github.deadlock-data.gameplay.69b3ca700c80
  - github.deadlock-data.gameplay.edb16660368e
  - steam.news.baba-release.1845383656397580
  - wiki.baba.184291
  - wiki.baba.184568
  - github.deadlock-data.gameplay.5799055efcc7
  - github.deadlock-data.gameplay.be5fb3ee934a
  - github.deadlock-data.gameplay.7fd1dfeb502a
---

# Baba

Valve announced Baba as available on **October 6, 2026**. This record is checked through **October 7 / client 6763**. Initial client 6757 and October 6 evidence stay separate.
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

- Configured base Spirit Resist: **8%**; source `SpiritScaling.TechResist`: **0.12**. No complete stacking formula is inferred.
- Source critical-damage bonus: **-20%**, not the full resulting critical-hit multiplier.

## Per-Boon Growth

Configured `LevelScaling` fields from the launch client; keys and values are preserved without deriving a live-match growth formula.

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

Description source: [`github.deadlock-data.english.8f2589cb4e64`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/8f2589cb4e645a2e9b3ba5363e51b830cd7bbacd/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
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
| Cast Range | 35 (range coefficient 1) |
| Charges | 1 (max charges coefficient 1) |
| Cooldown | 26 (cooldown coefficient 1) |
| Charge Delay | 6 (charge cooldown coefficient 1) |

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

Description source: [`github.deadlock-data.english.8f2589cb4e64`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/8f2589cb4e645a2e9b3ba5363e51b830cd7bbacd/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
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
| Cooldown | 30 (cooldown coefficient 1) |
| Charge Delay | source sentinel -1; not a negative cooldown |
| Duration | 10 (duration coefficient 1) |
| Radius | 8 (range coefficient 1) |

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

Description source: [`github.deadlock-data.english.8f2589cb4e64`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/8f2589cb4e645a2e9b3ba5363e51b830cd7bbacd/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCannotCancelDuringChannel`, `BehaviorProjectileFiredAsBullet`, `BehaviorCooldownOnChannelEnd`, `BehaviorDontInterruptSlideOnCast`, `BehaviorHoldsAtMaxChannel`.

| Card field | Base value |
| --- | ---: |
| Cast Range | 12 (range coefficient 1) |
| Cooldown | 25 (cooldown coefficient 1) |
| Charge Delay | source sentinel -1; not a negative cooldown |
| Radius | 6 (radius coefficient 1) |

Upgrade deltas:
- Tier 1: `{"Radius":3}`
- Tier 2: `{"AbilityCooldown":-12}`
- Tier 3: `{"BrewEffectiveness":33.33,"DamagePerSecond":{"Value":1.3333,"Scale":{"Value":1.3333,"Type":"spirit","Multiply":true},"Multiply":true},"CombatBarrier":{"Value":1.3333,"Scale":{"Value":1.3333,"Type":"spirit","Multiply":true},"Multiply":true},"SilenceDuration":{"Value":1.3333,"Multiply":true},"SpiritResistReduction":{"Value":1.3333,"Multiply":true}}`

#### Soothing Brew

| Card field | Base value |
| --- | ---: |
| Barrier | 100 (+1.2 per spirit) |
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

Description source: [`github.deadlock-data.english.8f2589cb4e64`](https://raw.githubusercontent.com/deadlock-wiki/deadlock-data/8f2589cb4e645a2e9b3ba5363e51b830cd7bbacd/data/localizations/english.json). Bracketed controls denote bindable actions, not default keys. Canonical YAML retains original text and localization keys.
<!-- ability-descriptions:end -->

Behavior flags: `BehaviorChannelled`, `BehaviorNoTarget`, `BehaviorDisplaysDamageImpact`, `BehaviorCooldownOnChannelEnd`, `BehaviorTriggerCancelMashProtectionOnCast`, `BehaviorRequireAbilityButtonToCancel`, `BehaviorShowCastRangeAsSatSphereWhileCasting`.

| Card field | Base value |
| --- | ---: |
| Max Damage | 450 (+1.6 per spirit) |
| Max Pigeon Duration | 2.75 (duration coefficient 1) |
| Time To Max Stacks | 3.5 |
| Max Slow | 32 |
| Cast Range | 18 (range coefficient 1) |
| Cooldown | 150 (cooldown coefficient 1) |
| Charge Delay | source sentinel -1; not a negative cooldown |

Upgrade deltas:
- Tier 1: `{"MaxSlow":32,"AbilityCastRange":4}`
- Tier 2: `{"AbilityCooldown":-55}`
- Tier 3: `{"BarrageMaxDamage":{"Value":125,"Scale":{"Value":1.5,"Type":"spirit"}},"HexDuration":0.5}`

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

## October 7 Review

Brew Tier 3 multiplier fields were re-encoded in a regenerated **client 6759** export before client 6762. This is not evidence of a new balance buff. Feed The Birds' English text changes “the target” to “the targets” / “each target”; that wording does not prove newly added multi-target behavior. The reviewed gameplay/English datasets are unchanged from 6762 to 6763.

See the [October 7 review](../../patches/2026-10-07-review.md) and [historical October 6 record](../../patches/snapshots/baba-2026-10-06.md). No official October 7 hotfix text was verified; these are source-export findings, not reconstructed patch notes.

## Evidence Boundaries

- Baba configuration and English text are checked through October 7 client 6763; the October 6 record remains a historical snapshot.
- Brew multiplier encoding was corrected in a regenerated client-6759 export, not demonstrated as an October 7 balance change.
- Later wiki interaction descriptions remain dated October 8 and are not independently runtime-tested.
- Other heroes, items and global mechanics retain their earlier pins. Later releases exist but are outside this chronological update.
- The reviewed exported datasets are not the entire game client and do not prove the absence of unexported runtime fixes.
- The ultimate retains source lock-on/ramp fields without inferring an exact hit-count or damage formula from their names.
- The two supporting melee/throw records in YAML are not extra numbered abilities.

[Official release announcement](https://store.steampowered.com/news/app/1422450/view/703281025618282871) · [October 6 article](https://deadlock.wiki/Baba?oldid=184291) · [October 8 article](https://deadlock.wiki/Baba?oldid=184568)
