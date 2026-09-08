---
id: item.crippling-headshot
title: "Crippling Headshot"
domain: items
topics: [item, weapon, tier-4]
aliases: ["upgrade_banshee_slugs"]
summary: "Landing a Headshot will reduce their Bullet and Spirit Resist and applies Healing Reduction."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Crippling Headshot

Landing a Headshot will reduce their Bullet and Spirit Resist and applies Healing Reduction.

## Identity and Purchase

- **Internal key:** `upgrade_banshee_slugs`
- **Numeric ID:** `3884003354`
- **Slot:** Weapon
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** WeaponDamage, Disruption
- **Target types:** none listed

## Components

- `upgrade_headshot_booster2`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 125 | normal |
| Passive | Debuff Duration | 12s | normal |
| Passive | Bullet Resist | -16% | important |
| Passive | Spirit Resist | -16% | important |
| Passive | Healing Reduction | -35% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `MagicResistReduction`: -12
- `BulletResistReduction`: -12
- `HealAmpReceivePenaltyPercent`: -25
- `HealAmpRegenPenaltyPercent`: -25
- `BonusHealth`: 150
