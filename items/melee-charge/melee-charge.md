---
id: item.melee-charge
title: "Melee Charge"
domain: items
topics: [item, weapon, tier-2]
aliases: ["upgrade_melee_charge"]
summary: "Your next Heavy Melee attack against an enemy deals increased damage."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Melee Charge

Your next Heavy Melee attack against an enemy deals increased damage.

## Identity and Purchase

- **Internal key:** `upgrade_melee_charge`
- **Numeric ID:** `26002154`
- **Slot:** Weapon
- **Tier:** 2
- **Cost:** 1600 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** Melee
- **Target types:** HeroEnemy, TrooperEnemy, MinionEnemy, Neutral

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Melee Damage | 10% | normal |
| Innate | Bullet Resist | 6% | normal |
| Innate | Heavy Melee Distance | 50% | elevated |
| Passive | Cooldown | 5s | normal |
| Passive | Bonus Heavy Damage | 25% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `MeleeDistanceScale`: 30
- `BulletResist`: 12
- `BonusHeavyMeleeDamage`: 15
