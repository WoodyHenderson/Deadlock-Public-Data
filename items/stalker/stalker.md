---
id: item.stalker
title: "Stalker"
domain: items
topics: [item, weapon, tier-2]
aliases: ["upgrade_weapon_backstabber"]
summary: "Dealing weapon damage at close range opens a wound and grants you bonus move speed. Wounded enemies take spirit damage over time, have reduced bullet resist, and are revealed through walls."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Stalker

Dealing weapon damage at close range opens a wound and grants you bonus move speed. Wounded enemies take spirit damage over time, have reduced bullet resist, and are revealed through walls.

## Identity and Purchase

- **Internal key:** `upgrade_weapon_backstabber`
- **Numeric ID:** `98582110`
- **Slot:** Weapon
- **Tier:** 2
- **Cost:** 1600 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage
- **Target types:** none listed

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Footstep Sound Distance | -50% | normal |
| Innate | Bonus Health | 50 | normal |
| Other | Cooldown | 6s | normal |
| Other | Debuff Duration | 5s | normal |
| Other | Close Range | 8m | normal |
| Other | Damage Per Second | 17 | important |
| Other | Bullet Resist | -6% | important |
| Other | Move Speed | 1.5m | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BulletResistReduction`: -10
- `BonusMoveSpeed`: 2m
- `DPS`: 20
- `ReduceFootstepSound`: -50
