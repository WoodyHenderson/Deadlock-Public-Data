---
id: item.trophy-collector
title: "Trophy Collector"
domain: items
topics: [item, vitality, tier-2]
aliases: ["upgrade_trophy_collector"]
summary: "Whenever you score an assist or kill, gain extra sprint, ability range and passive soul generation. This effect stacks and persists through death."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Trophy Collector

Whenever you score an assist or kill, gain extra sprint, ability range and passive soul generation. This effect stacks and persists through death.

## Identity and Purchase

- **Internal key:** `upgrade_trophy_collector`
- **Numeric ID:** `3074274290`
- **Slot:** Vitality
- **Tier:** 2
- **Cost:** 1600 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage, Healing, Movement
- **Target types:** none listed

## Components

- `upgrade_sprint_booster`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Weapon Damage vs. NPCs | -15% | normal |
| Innate | Sprint Speed | 2.0m | normal |
| Innate | Out of Combat Regen | 2 | normal |
| Passive | Max Stacks | 16 | normal |
| Passive | Sprint Speed | 0.15m | important |
| Passive | Ability Range | 0.75% | important |
| Passive | Souls per Minute | 18 | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `StackingTechRadiusMultiplier`: 3
- `StackingTechRangeMultiplier`: 3
- `OutOfCombatHealthRegen`: 6
- `BonusSprintSpeed`: 12m
- `MaxStacks`: 83
