---
id: item.ballistic-enchantment
title: "Ballistic Enchantment"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_bulletshredimbue"]
summary: "Imbue an ability with increased range. Dealing damage with that ability grants you increased weapon damage per unique hero hit. Has reduced effect on non-heroes."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Ballistic Enchantment

Imbue an ability with increased range. Dealing damage with that ability grants you increased weapon damage per unique hero hit. Has reduced effect on non-heroes.

## Identity and Purchase

- **Internal key:** `upgrade_bulletshredimbue`
- **Numeric ID:** `3294954488`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** yes
- **Shop filters:** WeaponDamage
- **Target types:** AllEnemy

## Components

- `upgrade_magic_reach`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Passive | Duration | 14s | normal |
| Passive | Non-Hero Weapon Damage | 5% | normal |
| Passive | Non-Hero Stack Limit | 8 | normal |
| Passive | Weapon Damage per Stack | 20% | important |
| Passive | Ability Range | 22% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `WeaponPowerPerStack`: 15
- `TechRangeMultiplier`: 15
- `TechRadiusMultiplier`: 15
