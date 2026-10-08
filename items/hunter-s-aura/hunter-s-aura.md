---
id: item.hunter-s-aura
title: "Hunter's Aura"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_bullet_armor_reduction_aura"]
summary: "Reduces nearby enemies' Bullet Resist and Fire Rate. If there is only one enemy hero nearby, this effect is doubled."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Hunter's Aura

Reduces nearby enemies' Bullet Resist and Fire Rate. If there is only one enemy hero nearby, this effect is doubled.

## Identity and Purchase

- **Internal key:** `upgrade_bullet_armor_reduction_aura`
- **Numeric ID:** `2481177645`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** WeaponDamage, Disruption, ClipSize
- **Target types:** HeroEnemy, CreepEnemy, MinionEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 100 | normal |
| Innate | Sprint Speed | 0.75m | normal |
| Passive | Radius | 15m | normal |
| Passive | Bullet Resist | -10% | important |
| Passive | Fire Rate | 15% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `FireRateSlow`: 5
- `BulletArmorReduction`: -6
- `BonusHealth`: 125
- `BonusSprintSpeed`: 3m
