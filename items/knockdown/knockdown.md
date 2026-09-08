---
id: item.knockdown
title: "Knockdown"
domain: items
topics: [item, spirit, tier-3]
aliases: ["upgrade_target_stun"]
summary: "Apply a Stun after 2s. Stun duration is increased against airborne targets. Increases the target's gravity for the duration of the stun."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Knockdown

Apply a Stun after 2s. Stun duration is increased against airborne targets. Increases the target's gravity for the duration of the stun.

## Identity and Purchase

- **Internal key:** `upgrade_target_stun`
- **Numeric ID:** `1254091416`
- **Slot:** Spirit
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** press
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** MagicDamage, Disruption
- **Target types:** HeroEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 75 | normal |
| Innate | Ability Range | 5% | normal |
| Active | Cast Range | 45m | normal |
| Active | Status Effect Stun | Unknown | important |
| Active | Stun Duration | 0.5s | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `TechRadiusMultiplier`: 6
- `TechRangeMultiplier`: 6
- `StunDuration`: 0.75
- `BonusHealth`: 75
