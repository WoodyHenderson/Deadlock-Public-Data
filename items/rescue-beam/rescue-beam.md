---
id: item.rescue-beam
title: "Rescue Beam"
domain: items
topics: [item, vitality, tier-3]
aliases: ["upgrade_rescue_beam"]
summary: "Heals a target allied hero and yourself for a percentage of Max Health. Once while healing, you can Pull the target towards you. Can be self-cast."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Rescue Beam

Heals a target allied hero and yourself for a percentage of Max Health. Once while healing, you can Pull the target towards you. Can be self-cast.

## Identity and Purchase

- **Internal key:** `upgrade_rescue_beam`
- **Numeric ID:** `1804594021`
- **Slot:** Vitality
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** press
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** MagicDamage, Durability, Healing, Movement
- **Target types:** HeroFriendly

## Components

- `upgrade_health_stimpak`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Sprint Speed | 0.75m | normal |
| Innate | Ability Range | 6% | normal |
| Active | Channel Duration | 2.5s | normal |
| Active | Cast Range | 35m | normal |
| Active | Cooldown | 60.0s | normal |
| Active | Heal Amount | 20% | important |
| Active | Move Speed | 0m | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `TechRadiusMultiplier`: 20
- `TechRangeMultiplier`: 20
- `HealPercentAmount`: 15
- `AbilityCooldown`: -45
