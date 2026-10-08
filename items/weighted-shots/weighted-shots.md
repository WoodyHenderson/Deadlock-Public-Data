---
id: item.weighted-shots
title: "Weighted Shots"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_weighted_shots"]
summary: "Your bullets build up a Movement Slow on enemies."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
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
- **Game mode:** standard
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
| Passive | Dash Distance | -20% | normal |
| Passive | Slow Duration | 3.5s | normal |
| Passive | Buildup Per Shot | 0.7% | normal |
| Passive | Move Speed | 24% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `StatusResistancePercent`: 10
- `BaseAttackDamagePercent`: 35
- `SlowPercent`: 16
- `GroundDashReductionPercent`: -8
