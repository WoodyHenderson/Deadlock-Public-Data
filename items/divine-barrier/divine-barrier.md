---
id: item.divine-barrier
title: "Divine Barrier"
domain: items
topics: [item, vitality, tier-4]
aliases: ["upgrade_divine_barrier"]
summary: "Remove all non-stun debuffs from the target and provide them with a Barrier and Move Speed. Can be self-cast. Cooldown is reduced by half when cast on someone else."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Divine Barrier

Remove all non-stun debuffs from the target and provide them with a Barrier and Move Speed. Can be self-cast. Cooldown is reduced by half when cast on someone else.

## Identity and Purchase

- **Internal key:** `upgrade_divine_barrier`
- **Numeric ID:** `1662311306`
- **Slot:** Vitality
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** press
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** Durability, Movement
- **Target types:** HeroFriendly

## Components

- `upgrade_guardian_ward`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Ability Range | 10% | normal |
| Innate | Out of Combat Regen | 1.5 | normal |
| Active | Cooldown | 45s | normal |
| Active | Buff Duration | 6s | normal |
| Active | Cast Range | 40m | normal |
| Active | Barrier | 600 | important |
| Active | Move Speed | 2.75m | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `AbilityCooldown`: -27
- `TechRadiusMultiplier`: 10
- `TechRangeMultiplier`: 10
