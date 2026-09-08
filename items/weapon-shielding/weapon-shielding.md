---
id: item.weapon-shielding
title: "Weapon Shielding"
domain: items
topics: [item, vitality, tier-2]
aliases: ["upgrade_weapon_shielding"]
summary: "Gain a Barrier whenever you take significant weapon damage from enemy Heroes in a small time frame."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Weapon Shielding

Gain a Barrier whenever you take significant weapon damage from enemy Heroes in a small time frame.

## Identity and Purchase

- **Internal key:** `upgrade_weapon_shielding`
- **Numeric ID:** `805079544`
- **Slot:** Vitality
- **Tier:** 2
- **Cost:** 1600 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** Durability
- **Target types:** none listed

## Components

- `upgrade_grit`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Out of Combat Regen | 2.5 | normal |
| Passive | Damage Threshold | 250 | normal |
| Passive | Time Frame | 4.0s | normal |
| Passive | Cooldown | 35s | normal |
| Passive | Barrier Duration | 8s | normal |
| Passive | Barrier | 300 | important |
| Passive | Bullet Resist | 18% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `OutOfCombatHealthRegen`: 3
- `CombatBarrier`: 225
- `BulletResist`: 15
- `AbilityCooldown`: -20
