---
id: item.slowing-hex
title: "Slowing Hex"
domain: items
topics: [item, spirit, tier-2]
aliases: ["upgrade_containment"]
summary: "Slows movement of enemy target. Also Silences their movement-based items and abilities. Increases the target's gravity. Does not affect target's stamina usage."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Slowing Hex

Slows movement of enemy target. Also Silences their movement-based items and abilities. Increases the target's gravity. Does not affect target's stamina usage.

## Identity and Purchase

- **Internal key:** `upgrade_containment`
- **Numeric ID:** `1813726886`
- **Slot:** Spirit
- **Tier:** 2
- **Cost:** 1600 souls
- **Activation:** press
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** Movement, Disruption, MagicDamage
- **Target types:** HeroEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Sprint Speed | 0.5m | normal |
| Active | Cast Range | 25m | normal |
| Active | Duration | 3.5s | normal |
| Active | Cooldown | 27s | normal |
| Active | Move Speed | 20% | important |
| Active | Dash Distance | -30% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `SlowPercent`: 10
- `AbilityCooldown`: -18
- `GroundDashReductionPercent`: -6
