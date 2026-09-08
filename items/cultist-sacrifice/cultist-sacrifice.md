---
id: item.cultist-sacrifice
title: "Cultist Sacrifice"
domain: items
topics: [item, weapon, tier-3]
aliases: ["upgrade_non_player_bonus_sacrifice"]
summary: "Target an enemy NPC and consume it for 180% Bonus Souls and grants a powerful long lasting buff."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Cultist Sacrifice

Target an enemy NPC and consume it for 180% Bonus Souls and grants a powerful long lasting buff.

## Identity and Purchase

- **Internal key:** `upgrade_non_player_bonus_sacrifice`
- **Numeric ID:** `709540378`
- **Slot:** Weapon
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** press
- **Active item:** yes
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
