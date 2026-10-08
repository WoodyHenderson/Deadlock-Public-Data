---
id: item.rebuttal
title: "Rebuttal"
domain: items
topics: [item, vitality, tier-1]
aliases: ["upgrade_melee_rebuttal"]
summary: "On a successful Parry against an enemy Hero, Heal yourself for the damage parried and returns that damage to the target, and temporarily gain increased damage."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Rebuttal

On a successful Parry against an enemy Hero, Heal yourself for the damage parried and returns that damage to the target, and temporarily gain increased damage.

## Identity and Purchase

- **Internal key:** `upgrade_melee_rebuttal`
- **Numeric ID:** `4204808176`
- **Slot:** Vitality
- **Tier:** 1
- **Cost:** 800 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** Durability, Melee, Healing
- **Target types:** AllEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Parry Cooldown | 1.75s | normal |
| Innate | Melee Resist | 18% | normal |
| Innate | Bonus Health | 75 | normal |
| Passive | Buff Duration | 6s | normal |
| Passive | Bonus Damage | 30% | important |
| Passive | Parry Success Heal | Unknown | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `ParryCooldownReduction`: 0.5
- `MeleeResistPercent`: 22
- `BonusDamagePercent`: 20
- `BonusHealth`: 150
