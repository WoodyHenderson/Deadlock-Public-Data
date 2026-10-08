---
id: item.cultist-sacrifice
title: "Cultist Sacrifice"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_non_player_bonus_sacrifice"]
summary: "Target an enemy NPC and consume it for 170% Bonus Souls and grants a powerful long lasting buff."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Cultist Sacrifice

Target an enemy NPC and consume it for 170% Bonus Souls and grants a powerful long lasting buff.

## Identity and Purchase

- **Internal key:** `upgrade_non_player_bonus_sacrifice`
- **Numeric ID:** `709540378`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** press
- **Active item:** yes
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** WeaponDamage, Durability, Healing
- **Target types:** TrooperEnemy, Neutral, MinionEnemy

## Components

- `upgrade_non_player_bonus`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Out of Combat Regen | 2 | normal |
| Innate | Weapon Damage vs. NPCs | 30% | normal |
| Innate | Bullet Resist vs. NPCs | 30% | normal |
| Active | Cooldown | 270s | normal |
| Active | Duration | 160s | normal |
| Active | Weapon Damage | 10% | important |
| Active | Bonus Health | 50 | important |
| Active | Ability Range | 12% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `TechRadiusMultiplier`: 40
- `TechRangeMultiplier`: 40
- `BaseAttackDamagePercent`: 47
- `BonusHealth`: 300
- `NonPlayerBonusWeaponPower`: 30
- `NonPlayerBulletResist`: 30
