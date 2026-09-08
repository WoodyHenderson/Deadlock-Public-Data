---
id: item.blood-tribute
title: "Blood Tribute"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_blood_tribute"]
summary: "Toggle: Continually sacrifice Health to improve fire rate, Debuff Resistance and Move Speed."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Blood Tribute

Toggle: Continually sacrifice Health to improve fire rate, Debuff Resistance and Move Speed.

## Identity and Purchase

- **Internal key:** `upgrade_blood_tribute`
- **Numeric ID:** `989206714`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** instant_cast_toggle
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** WeaponDamage
- **Target types:** none listed

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Debuff Resist | 8% | normal |
| Innate | Spirit Resist | 8% | normal |
| Innate | Out of Combat Regen | 4 | normal |
| Active | Fire Rate | 35% | normal |
| Active | Debuff Resist | 35% | normal |
| Active | Move Speed | 2.0m | normal |
| Active | Health Drain | 50/s | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `HealthDrainedPerSecond`: -20
- `BonusFireRate`: 30
- `TechResist`: 14
- `OutOfCombatHealthRegen`: 8
