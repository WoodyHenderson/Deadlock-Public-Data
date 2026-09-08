---
id: item.capacitor
title: "Capacitor"
domain: items
topics: [item, weapon, tier-4]
aliases: ["upgrade_capacitor"]
summary: "Launch a projectile that deals damage, applies a strong slow that recovers over time, prevents Stamina usage and Silences their movement-based items and abilities."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Capacitor

Launch a projectile that deals damage, applies a strong slow that recovers over time, prevents Stamina usage and Silences their movement-based items and abilities.

## Identity and Purchase

- **Internal key:** `upgrade_capacitor`
- **Numeric ID:** `710436191`
- **Slot:** Weapon
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** instant_cast
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** MagicDamage, FireRate
- **Target types:** HeroEnemy, CreepEnemy, BossEnemy, MinionEnemy

## Components

- `upgrade_chain_lightning`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Fire Rate | 5% | elevated |
| Passive | Max Frequency | 0.2s | normal |
| Passive | Max Jumps | 6 | normal |
| Passive | Jump Radius | 10m | normal |
| Passive | Shock Damage | 43 | important |
| Passive | Proc Chance | 20% | important |
| Active | Cooldown | 40s | normal |
| Active | Slow Duration | 3s | normal |
| Active | Damage | 100 | important |
| Active | Max Move Speed | 75% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `ProcChance`: 5
- `BonusFireRate`: 15
- `DamagePerChain`: 25
- `AbilityCooldown`: -32
- `Damage`: 25
