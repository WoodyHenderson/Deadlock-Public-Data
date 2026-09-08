---
id: item.kinetic-dash
title: "Kinetic Dash"
domain: items
topics: [item, weapon, tier-2]
aliases: ["upgrade_kinetic_sash"]
summary: "When you Dash-Jump you gain Fire Rate and bonus Ammo until your next reload. Lasts up to 7s."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Kinetic Dash

When you Dash-Jump you gain Fire Rate and bonus Ammo until your next reload. Lasts up to 7s.

## Identity and Purchase

- **Internal key:** `upgrade_kinetic_sash`
- **Numeric ID:** `3977876567`
- **Slot:** Weapon
- **Tier:** 2
- **Cost:** 1600 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** FireRate, ClipSize, Movement, Durability
- **Target types:** none listed

## Components

- `upgrade_improved_stamina`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Stamina | 1 | normal |
| Innate | Stamina Recovery | 12% | normal |
| Passive | Cooldown | 0s | normal |
| Passive | Duration | 7s | normal |
| Passive | Fire Rate | 25% | important |
| Passive | Temporary Ammo | 6 | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BonusFireRate`: 20
- `Stamina`: 1
- `BonusClipSize`: 6
- `StaminaCooldownReduction`: 14
