---
id: item.headhunter
title: "Headhunter"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_headhunter"]
summary: "Your next headshot against an enemy Hero deals bonus weapon damage, heal you, and briefly grants bonus move speed."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Headhunter

Your next headshot against an enemy Hero deals bonus weapon damage, heal you, and briefly grants bonus move speed.

## Identity and Purchase

- **Internal key:** `upgrade_headhunter`
- **Numeric ID:** `4053935515`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage
- **Target types:** none listed

## Components

- `upgrade_headshot_booster`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Weapon Damage | 5% | normal |
| Innate | Bonus Health | 50 | normal |
| Passive | Move Speed | 1.75m | normal |
| Passive | Move Speed Duration | 3s | normal |
| Passive | Cooldown | 8s | normal |
| Passive | Head Shot Bonus Damage | 75 | important |
| Passive | Heal Per Headshot | 4% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `HeadShotBonusDamage`: 75
- `HealPercentPerHeadshot`: 4
- `AbilityCooldown`: -3
