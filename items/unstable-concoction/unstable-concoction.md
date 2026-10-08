---
id: item.unstable-concoction
title: "Unstable Concoction"
domain: items
topics: [item, spirit, tier-5]
aliases: ["upgrade_unstable_concoction"]
summary: "Consume a concoction that grants you Unstoppable and increased speed, health, spirit and weapon damage. After a short duration you die and explode, stunning nearby enemies and dealing damage based on your maximum health. Dying this way reduces your respawn time by 50%."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Unstable Concoction

Consume a concoction that grants you Unstoppable and increased speed, health, spirit and weapon damage. After a short duration you die and explode, stunning nearby enemies and dealing damage based on your maximum health. Dying this way reduces your respawn time by 50%.

## Identity and Purchase

- **Internal key:** `upgrade_unstable_concoction`
- **Numeric ID:** `1558545403`
- **Slot:** Spirit
- **Tier:** 5
- **Cost:** 9999 souls
- **Activation:** instant_cast
- **Active item:** yes
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** none listed
- **Target types:** AllEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Active | Duration | 4.0s | normal |
| Active | Weapon Damage | 150% | normal |
| Active | Radius | 22m | normal |
| Active | Spirit Power | 150 | normal |
| Active | Max Health Damage | 30% | important |
| Active | Stun Duration | 3.0s | important |
| Active | Move Speed | 10m | important |
| Active | Bonus Health | 3000 | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `StunDuration`: 0.5
- `BaseAttackDamagePercent`: 50
- `TechPower`: 50
- `BonusHealth`: 1300
