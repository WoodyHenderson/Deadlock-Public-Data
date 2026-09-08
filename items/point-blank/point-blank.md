---
id: item.point-blank
title: "Point Blank"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_close_quarter_combat"]
summary: "When in close range to your target, gain Weapon Damage and your bullets apply a Movement Slow."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Point Blank

When in close range to your target, gain Weapon Damage and your bullets apply a Movement Slow.

## Identity and Purchase

- **Internal key:** `upgrade_close_quarter_combat`
- **Numeric ID:** `2095565695`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage, Durability, Disruption
- **Target types:** HeroEnemy

## Components

- `upgrade_close_range`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 75 | normal |
| Innate | Melee Resist | 30% | normal |
| Passive | Slow Duration | 2s | normal |
| Passive | Close Range | 15m | normal |
| Passive | Weapon Damage | 50% | important |
| Passive | Move Speed | 25% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `CloseRangeBonusWeaponPower`: 30
- `MeleeResistPercent`: 30
- `BonusHealth`: 150
- `SlowPercent`: 5
