---
id: item.sharpshooter
title: "Sharpshooter"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_sharpshooter"]
summary: "Deal additional Weapon Damage when beyond a minimum distance from your target."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Sharpshooter

Deal additional Weapon Damage when beyond a minimum distance from your target.

## Identity and Purchase

- **Internal key:** `upgrade_sharpshooter`
- **Numeric ID:** `2152872419`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** WeaponDamage, ClipSize
- **Target types:** none listed

## Components

- `upgrade_long_range`
- `upgrade_high_velocity_mag`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bullet Velocity | 60% | normal |
| Innate | Weapon Damage | 10% | normal |
| Innate | Sprint Speed | 1.0m | normal |
| Innate | Move Speed | -0.7m | normal |
| Innate | Weapon Fall-off Range | 20% | elevated |
| Innate | Weapon Zoom | 25% | elevated |
| Passive | Min. Distance | 15m | normal |
| Passive | Weapon Damage | 60% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `LongRangeBonusWeaponPower`: 40
- `BonusAttackRangePercent`: 10
- `BonusBulletSpeedPercent`: 45
- `BaseAttackDamagePercent`: 15
