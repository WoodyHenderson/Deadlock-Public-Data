---
id: item.inhibitor
title: "Inhibitor"
domain: items
topics: [item, vitality, tier-4]
aliases: ["upgrade_inhibitor"]
summary: "Your bullets build up to reduce the target's outgoing damage and apply healing reduction."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
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
