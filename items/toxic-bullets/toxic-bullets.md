---
id: item.toxic-bullets
title: "Toxic Bullets"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_toxic_bullets"]
summary: "Your bullets build up a Bleed on enemies, causing them to lose a percentage of their Max Health over time. Also applies Healing Reduction on the bleeding target."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Toxic Bullets

Your bullets build up a Bleed on enemies, causing them to lose a percentage of their Max Health over time. Also applies Healing Reduction on the bleeding target.

## Identity and Purchase

- **Internal key:** `upgrade_toxic_bullets`
- **Numeric ID:** `3696726732`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** MagicDamage, Disruption
- **Target types:** HeroEnemy, CreepEnemy, MinionEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Other | Duration | 4s | normal |
| Other | Buildup Per Shot | 1.28% | normal |
| Other | Bleed Damage | 1.9%/sec | important |
| Other | Healing Reduction | -35% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `HealAmpReceivePenaltyPercent`: -30
- `HealAmpRegenPenaltyPercent`: -30
- `DotHealthPercent`: 0.7
