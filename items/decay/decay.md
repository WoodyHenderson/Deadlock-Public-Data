---
id: item.decay
title: "Decay"
domain: items
topics: [item, spirit, tier-3]
aliases: ["upgrade_rupture"]
summary: "Inflict damage over time to a target, dealing damage based on their current health. Decay's damage is non-lethal and does not apply item procs."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Decay

Inflict damage over time to a target, dealing damage based on their current health. Decay's damage is non-lethal and does not apply item procs.

## Identity and Purchase

- **Internal key:** `upgrade_rupture`
- **Numeric ID:** `3144988365`
- **Slot:** Spirit
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** press
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** MagicDamage, Disruption
- **Target types:** HeroEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Spirit Power | 8 | normal |
| Innate | Bonus Health | 65 | normal |
| Active | Cast Range | 20m | normal |
| Active | Duration | 10s | normal |
| Active | Cooldown | 30.0s | normal |
| Active | Bleed Damage | 2.6%/sec | important |
| Active | Healing Reduction | -50% | important |
| Active | Cast Range | 20m | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `TechPower`: 12
- `BonusHealth`: 90
- `HealAmpReceivePenaltyPercent`: -20
- `HealAmpRegenPenaltyPercent`: -20
- `DotHealthPercent`: .5
- `AbilityCooldown`: -10
