---
id: item.inhibitor
title: "Inhibitor"
domain: items
topics: [item, vitality, tier-4]
aliases: ["upgrade_inhibitor"]
summary: "Your bullets build up to reduce the target's outgoing damage and apply healing reduction."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Inhibitor

Your bullets build up to reduce the target's outgoing damage and apply healing reduction.

## Identity and Purchase

- **Internal key:** `upgrade_inhibitor`
- **Numeric ID:** `2037039379`
- **Slot:** Vitality
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** WeaponDamage, Disruption, FireRate
- **Target types:** AllEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Weapon Damage | 10% | normal |
| Innate | Bonus Health | 150 | normal |
| Passive | Debuff Duration | 5s | normal |
| Passive | Buildup Per Shot | 0.77% | normal |
| Passive | Damage Penalty | -30% | important |
| Passive | Healing Reduction | -40% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `OutgoingDamagePenaltyPercent`: -20
- `HealAmpReceivePenaltyPercent`: -20
- `HealAmpRegenPenaltyPercent`: -20
- `BonusHealth`: 125
- `BaseAttackDamagePercent`: 20
