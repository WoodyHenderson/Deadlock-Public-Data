---
id: item.unstoppable
title: "Unstoppable"
domain: items
topics: [item, vitality, tier-4]
aliases: ["upgrade_unstoppable"]
summary: "Temporarily suppress negative status effects and become immune to Stun, Silence, Sleep, Root, and Disarm. Cannot be used while Stunned or Slept."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Unstoppable

Temporarily suppress negative status effects and become immune to Stun, Silence, Sleep, Root, and Disarm. Cannot be used while Stunned or Slept.

## Identity and Purchase

- **Internal key:** `upgrade_unstoppable`
- **Numeric ID:** `3357231760`
- **Slot:** Vitality
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** instant_cast
- **Active item:** yes
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** Durability, Movement
- **Target types:** none listed

## Components

- `upgrade_debuff_reducer`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Debuff Resist | 25% | normal |
| Innate | Bonus Health | 125 | normal |
| Active | Cooldown | 60.0s | normal |
| Active | Duration | 5.5s | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `AbilityDuration`: 1.25
- `BonusHealth`: 75
- `AbilityCooldown`: -35
- `StatusResistancePercent`: 15
