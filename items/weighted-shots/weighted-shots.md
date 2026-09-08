---
id: item.weighted-shots
title: "Weighted Shots"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_weighted_shots"]
summary: "Your bullets build up a Movement Slow on enemies."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Weighted Shots

Your bullets build up a Movement Slow on enemies.

## Identity and Purchase

- **Internal key:** `upgrade_weighted_shots`
- **Numeric ID:** `3791587546`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage
- **Target types:** HeroEnemy

## Components

- `upgrade_slowing_bullets`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Debuff Resist | 22% | normal |
| Innate | Stamina Recovery | -14% | normal |
| Innate | Move Speed | -0.5m | normal |
| Innate | Weapon Damage | 30% | elevated |
| Passive | Dash Distance | -22% | normal |
| Passive | Slow Duration | 3.5s | normal |
| Passive | Buildup Per Shot | 0.7% | normal |
| Passive | Move Speed | 30% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `StatusResistancePercent`: 10
- `BaseAttackDamagePercent`: 35
- `SlowPercent`: 20
- `GroundDashReductionPercent`: -10
