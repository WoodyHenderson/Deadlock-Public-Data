---
id: item.guardian-ward
title: "Guardian Ward"
domain: items
topics: [item, vitality, tier-2]
aliases: ["upgrade_guardian_ward"]
summary: "Provide the target with a Barrier and temporary Move Speed. Can be self-cast. Cooldown is reduced by half when cast on someone else."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Guardian Ward

Provide the target with a Barrier and temporary Move Speed. Can be self-cast. Cooldown is reduced by half when cast on someone else.

## Identity and Purchase

- **Internal key:** `upgrade_guardian_ward`
- **Numeric ID:** `857669956`
- **Slot:** Vitality
- **Tier:** 2
- **Cost:** 1600 souls
- **Activation:** press
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** Durability, Movement
- **Target types:** HeroFriendly

## Components

- `upgrade_grit`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Out of Combat Regen | 1.5 | normal |
| Innate | Ability Range | 8% | elevated |
| Active | Cooldown | 60s | normal |
| Active | Buff Duration | 6s | normal |
| Active | Cast Range | 40m | normal |
| Active | Barrier | 250 | important |
| Active | Move Speed | 2.75m | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `TechRangeMultiplier`: 12
- `TechRadiusMultiplier`: 12
- `GuardianWardCombatBarrier`: 250
- `ChannelMoveSpeed`: 2
- `AbilityCooldown`: -12
