---
id: item.ricochet
title: "Ricochet"
domain: items
topics: [item, weapon, tier-4]
aliases: ["upgrade_ricochet"]
summary: "Your bullets will ricochet on enemies near your target, applying any bullet procs and dealing a percentage of the original damage."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Ricochet

Your bullets will ricochet on enemies near your target, applying any bullet procs and dealing a percentage of the original damage.

## Identity and Purchase

- **Internal key:** `upgrade_ricochet`
- **Numeric ID:** `2480592370`
- **Slot:** Weapon
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** ClipSize
- **Target types:** HeroEnemy, BossEnemy, TrooperEnemy, PropEnemy, MinionEnemy, Neutral

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Fire Rate | 18% | elevated |
| Other | Ricochet Targets | 2 | normal |
| Other | Ricochet Range | 13m | normal |
| Other | Ricochet Damage | 65% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `RicochetDamagePercent`: 15
- `BonusFireRate`: 25
