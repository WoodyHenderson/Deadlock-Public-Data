---
id: item.shadow-strike
title: "Shadow Strike"
domain: items
topics: [item, vitality, tier-5, street-brawl]
aliases: ["upgrade_shadow_strike"]
summary: "Go Invisible on Stamina use with no detection range. Doing a melee attack while invisible will cause you to steal bullet and spirit resistance from them and deal damage over time."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Shadow Strike

**Shadow Strike is a Street Brawl-only item and is not available in standard matches.**

Go Invisible on Stamina use with no detection range. Doing a melee attack while invisible will cause you to steal bullet and spirit resistance from them and deal damage over time.

## Identity and Purchase

- **Internal key:** `upgrade_shadow_strike`
- **Numeric ID:** `2319629810`
- **Slot:** Vitality
- **Tier:** 5
- **Cost:** 9999 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** Street Brawl only
- **Imbued item:** no
- **Shop filters:** none listed
- **Target types:** AllEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Stamina | 3 | normal |
| Innate | Bonus Health | 350 | normal |
| Active | Fade Time | 0.2s | normal |
| Active | Damage Per Second | 125 | important |
| Active | Invisibility Duration | 3s | important |
| Active | Steal Duration | 6s | important |
| Active | Resist Stolen | 40% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `Stamina`: 1
- `BonusHealth`: 250
- `ResistStealAmount`: 20
- `DPS`: 125
- `AbilityDuration`: 3
