---
id: item.fortitude
title: "Fortitude"
domain: items
topics: [item, vitality, tier-3]
aliases: ["upgrade_chonky"]
summary: "After not taking damage for a period, gain health regen."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Fortitude

After not taking damage for a period, gain health regen.

## Identity and Purchase

- **Internal key:** `upgrade_chonky`
- **Numeric ID:** `3585132399`
- **Slot:** Vitality
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage, Durability, Healing, Movement
- **Target types:** none listed

## Components

- `upgrade_health`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 375 | elevated |
| Passive | Restore Delay | 10 s | important |
| Passive | Max Health Regen | 2 % | important |
| Passive | Move Speed | 1.5m | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `RestoreDelay`: -6
- `BonusHealth`: 375
- `BonusMoveSpeed`: 1m
- `HealLifePercentOutOfCombat`: 1
