---
id: item.mercurial-magnum
title: "Mercurial Magnum"
domain: items
topics: [item, spirit, tier-4]
aliases: ["upgrade_ethereal_bullets"]
summary: "Your imbued ability charges up over time with bonus spirit damage, bonus fire rate, and reloads bullets on use. Until your next reload, your bullets deal bonus spirit damage based on your Spirit Power."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Mercurial Magnum

Your imbued ability charges up over time with bonus spirit damage, bonus fire rate, and reloads bullets on use. Until your next reload, your bullets deal bonus spirit damage based on your Spirit Power.

## Identity and Purchase

- **Internal key:** `upgrade_ethereal_bullets`
- **Numeric ID:** `3919289022`
- **Slot:** Spirit
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** yes
- **Shop filters:** MagicDamage, FireRate
- **Target types:** AllEnemy

## Components

- `upgrade_quick_silver`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Max Ammo | 20% | normal |
| Innate | Spirit Power | 7 | normal |
| Passive | Bullets Reloaded | 100% | normal |
| Passive | Charge-Up Time | 14s | normal |
| Passive | Base Bullet Damage | 25% | important |
| Passive | Damage | 60 | important |
| Passive | Fire Rate | 22% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BonusFireRate`: 20
- `BonusClipSizePercent`: 60
- `Damage`: 120
- `BulletsBonusMagicDamage`: 20
- `TechPower`: 15
