---
id: item.escalating-resilience
title: "Escalating Resilience"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_reinforcing_casings"]
summary: "Grants Bullet Resist when your bullets hit an enemy hero. Each shot can only grant one stack."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Escalating Resilience

Grants Bullet Resist when your bullets hit an enemy hero. Each shot can only grant one stack.

## Identity and Purchase

- **Internal key:** `upgrade_reinforcing_casings`
- **Numeric ID:** `2463960640`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage, Durability, FireRate
- **Target types:** none listed

## Components

- `upgrade_clip_size`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 75 | normal |
| Innate | Weapon Damage | 18% | normal |
| Innate | Max Ammo | 35% | elevated |
| Passive | Bullet Resist per Stack | 2% | normal |
| Passive | Stack Duration | 24s | normal |
| Passive | Max Bullet Resist | 30% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BulletResistPerStack`: 2
- `MaxArmorStacks`: 20
- `BonusClipSizePercent`: 30
- `BonusHealth`: 125
- `WeaponPower`: 10
