---
id: item.haunting-shot
title: "Haunting Shot"
domain: items
topics: [item, weapon, tier-5]
aliases: ["upgrade_eldritch_shot"]
summary: "Your next bullet applies a powerful debuff reducing the enemy's damage output, healing and movement speed. It also deals bonus spirit damage based on the targets current Health. The bullet is larger and penetrates through targets."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Haunting Shot

Your next bullet applies a powerful debuff reducing the enemy's damage output, healing and movement speed. It also deals bonus spirit damage based on the targets current Health. The bullet is larger and penetrates through targets.

## Identity and Purchase

- **Internal key:** `upgrade_eldritch_shot`
- **Numeric ID:** `3568217437`
- **Slot:** Weapon
- **Tier:** 5
- **Cost:** 9999 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage, MagicDamage
- **Target types:** AllEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Other | Cooldown | 2.5s | normal |
| Other | Bullet Radius | 1.5m | normal |
| Other | Debuff Duration | 4s | normal |
| Other | Move Speed | 40% | normal |
| Other | Dash Distance | -40% | normal |
| Other | Current Health Damage | 10% | important |
| Other | Damage Penalty | -40% | important |
| Other | Healing Reduction | -40% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `GroundDashReductionPercent`: -10
- `HealthPctDamage`: 5
- `MovementSpeedSlow`: 10
- `HealAmpReceivePenaltyPercent`: -15
- `HealAmpRegenPenaltyPercent`: -15
- `OutgoingDamagePenaltyPercent`: -15
- `AbilityCooldown`: -1
