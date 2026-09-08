---
id: item.express-shot
title: "Express Shot"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_express_shot"]
summary: "Your next attack will fire twice in quick succession with increased damage and velocity. This attack consumes extra ammo."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Express Shot

Your next attack will fire twice in quick succession with increased damage and velocity. This attack consumes extra ammo.

## Identity and Purchase

- **Internal key:** `upgrade_express_shot`
- **Numeric ID:** `690458959`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage
- **Target types:** none listed

## Components

- `upgrade_high_velocity_mag`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Weapon Damage | 8% | normal |
| Innate | Bullet Velocity | 60% | elevated |
| Passive | Bullet Velocity | 100% | normal |
| Passive | Extra Ammo Consumed | 2 | normal |
| Passive | Cooldown | 8s | normal |
| Passive | Weapon Damage | 125% | important |
| Passive | Secondary Fire Weapon Damage | 40% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `ProcBaseAttackDamagePercent`: 75
- `ProcBaseAttackDamagePercentAltFire`: 25
- `BonusBulletSpeedPercent`: 45
- `BaseAttackDamagePercent`: 15
