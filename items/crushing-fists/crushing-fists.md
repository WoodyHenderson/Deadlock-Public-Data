---
id: item.crushing-fists
title: "Crushing Fists"
domain: items
topics: [item, weapon, tier-4]
aliases: ["upgrade_crushing_fists"]
summary: "Your melee damage will restore ammo and apply a stacking bullet resist debuff on enemies. Heavy melee applies 2 stacks. If the target reaches max stacks, they will be stunned."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Crushing Fists

Your melee damage will restore ammo and apply a stacking bullet resist debuff on enemies. Heavy melee applies 2 stacks. If the target reaches max stacks, they will be stunned.

## Identity and Purchase

- **Internal key:** `upgrade_crushing_fists`
- **Numeric ID:** `800008313`
- **Slot:** Weapon
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** Melee
- **Target types:** HeroEnemy, TrooperEnemy, MinionEnemy, Neutral

## Components

- `upgrade_melee_charge`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Melee Damage | 22% | normal |
| Innate | Bullet Resist | 12% | normal |
| Innate | Heavy Melee Distance | 60% | elevated |
| Passive | Cooldown | 5s | normal |
| Passive | Bonus Heavy Damage | 25% | important |
| Passive | Stun Duration | 0.75s | normal |
| Passive | Debuff Duration | 8s | normal |
| Passive | Ammo | 15% | important |
| Passive | Bullet Resist | -5% | important |
| Passive | Max Stacks | 6 | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `MeleeDistanceScale`: 40
- `BulletResist`: 12
- `BonusMeleeDamagePercent`: 15
- `BulletResistReduction`: -4
- `BonusHeavyMeleeDamage`: 15
