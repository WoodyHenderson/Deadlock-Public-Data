---
id: item.split-shot
title: "Split Shot"
domain: items
topics: [item, weapon, tier-2]
aliases: ["upgrade_split_shot"]
summary: "Make your weapon fire multishot. Hitting more than one Hero per attack will grant a stacking weapon damage bonus. Targets can only be hit once per multishot."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Split Shot

Make your weapon fire multishot. Hitting more than one Hero per attack will grant a stacking weapon damage bonus. Targets can only be hit once per multishot.

## Identity and Purchase

- **Internal key:** `upgrade_split_shot`
- **Numeric ID:** `3647584222`
- **Slot:** Weapon
- **Tier:** 2
- **Cost:** 1600 souls
- **Activation:** instant_cast
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** WeaponDamage
- **Target types:** none listed

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Active | Cooldown | 27s | normal |
| Active | Buff Duration | 5s | normal |
| Active | Max Stacks | 5 | normal |
| Active | Stack Duration | 12s | normal |
| Active | Weapon Multishot | 5 | important |
| Active | Weapon Damage per Stack | 8% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BulletSplitShot`: 4
- `WeaponDamagePerStack`: 8
- `AbilityCooldown`: -8
