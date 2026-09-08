---
id: item.escalating-exposure
title: "Escalating Exposure"
domain: items
topics: [item, spirit, tier-4]
aliases: ["upgrade_escalating_exposure"]
summary: "Dealing spirit damage applies a stacking Spirit Amp that increases your spirit damage to the target."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Escalating Exposure

Dealing spirit damage applies a stacking Spirit Amp that increases your spirit damage to the target.

## Identity and Purchase

- **Internal key:** `upgrade_escalating_exposure`
- **Numeric ID:** `3005970438`
- **Slot:** Spirit
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** MagicDamage, Durability
- **Target types:** AllEnemy

## Components

- `upgrade_magic_vulnerability`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Spirit Resist On Spirit Damage | -8% | normal |
| Innate | Spirit Resist | 17% | normal |
| Passive | Max Stacks | 12 | normal |
| Passive | Duration | 12s | normal |
| Passive | Max Frequency Per Target | 0.7s | normal |
| Passive | Spirit Amp per Stack | 4.5% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `MagicIncreasePerStack`: 1.5
- `TechResist`: 8
- `TechArmorDamageReduction`: -10
- `MaxStacks`: 6
