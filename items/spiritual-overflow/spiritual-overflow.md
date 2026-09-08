---
id: item.spiritual-overflow
title: "Spiritual Overflow"
domain: items
topics: [item, weapon, tier-4]
aliases: ["upgrade_tech_overflow"]
summary: "Gain bonus Fire Rate, Spirit Power and Spirit Lifesteal by charging up when shooting enemy heroes."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Spiritual Overflow

Gain bonus Fire Rate, Spirit Power and Spirit Lifesteal by charging up when shooting enemy heroes.

## Identity and Purchase

- **Internal key:** `upgrade_tech_overflow`
- **Numeric ID:** `2226497419`
- **Slot:** Weapon
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** MagicDamage, FireRate
- **Target types:** HeroEnemy

## Components

- `upgrade_health_stealing_magic`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Ability Duration | 13% | normal |
| Innate | Spirit Lifesteal | 13% | normal |
| Innate | Bonus Health | 90 | normal |
| Innate | Spirit Power | 6 | normal |
| Passive | Buildup Per Shot | 0.75% | normal |
| Passive | Duration | 15s | normal |
| Passive | Fire Rate | 30% | important |
| Passive | Spirit Power | 40 | important |
| Passive | Spirit Lifesteal | 10% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BonusAbilityDurationPercent`: 15
- `BonusSpirit`: 30
- `BonusFireRate`: 20
- `AbilityLifestealPercentHero`: 15
- `BonusHealth`: 80
- `TechPower`: 9
