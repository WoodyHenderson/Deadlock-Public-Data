---
id: item.healing-tempo
title: "Healing Tempo"
domain: items
topics: [item, vitality, tier-4]
aliases: ["upgrade_healbuff"]
summary: "Applying heal to yourself or an ally grants the target bonus fire rate and bonus move speed. Does not apply on innate Regen or passive Bullet/Spirit Lifesteals."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Healing Tempo

Applying heal to yourself or an ally grants the target bonus fire rate and bonus move speed. Does not apply on innate Regen or passive Bullet/Spirit Lifesteals.

## Identity and Purchase

- **Internal key:** `upgrade_healbuff`
- **Numeric ID:** `1427630806`
- **Slot:** Vitality
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** FireRate, Healing
- **Target types:** none listed

## Components

- `upgrade_healing_booster`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Spirit Resist | 10% | normal |
| Innate | Health Regen | 6 | normal |
| Innate | Out of Combat Regen | 4 | normal |
| Innate | Healing Effectiveness | 25% | elevated |
| Other | Buff Duration | 7s | normal |
| Other | Fire Rate | 35% | important |
| Other | Move Speed | 1.25m | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `HealAmpRegenPercent`: 10
- `HealAmpCastPercent`: 10
- `TechResist`: 10
- `BonusMoveSpeed`: 2m
- `BonusFireRate`: 20
- `BonusHealthRegen`: 6
