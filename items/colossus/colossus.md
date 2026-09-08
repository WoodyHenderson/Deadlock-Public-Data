---
id: item.colossus
title: "Colossus"
domain: items
topics: [item, vitality, tier-4]
aliases: ["upgrade_colossus"]
summary: "Grow larger in size, gaining bullet resist, spirit resist, and melee damage. Nearby enemies suffer from slow and have reduced dash speed."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Colossus

Grow larger in size, gaining bullet resist, spirit resist, and melee damage. Nearby enemies suffer from slow and have reduced dash speed.

## Identity and Purchase

- **Internal key:** `upgrade_colossus`
- **Numeric ID:** `2407781327`
- **Slot:** Vitality
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** instant_cast
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** Durability
- **Target types:** none listed

## Components

- `upgrade_health`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Weapon Damage | 15% | normal |
| Innate | Base Health | 25% | elevated |
| Active | Radius | 14m | normal |
| Active | Duration | 7s | normal |
| Active | Cooldown | 37.0s | normal |
| Active | Model Scale | 20% | normal |
| Active | Bullet Resist | 35% | important |
| Active | Spirit Resist | 35% | important |
| Active | Melee Damage | 30% | important |
| Active | Move Speed | 30% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BonusBaseHealth`: 15
- `ModelScaleGrowth`: 0.2
- `ModelScaleGrowthTooltip`: 20
- `BuffBulletResist`: 10
- `BuffTechResist`: 10
- `AbilityCooldown`: -7
