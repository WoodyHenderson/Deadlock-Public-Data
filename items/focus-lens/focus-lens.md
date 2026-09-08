---
id: item.focus-lens
title: "Focus Lens"
domain: items
topics: [item, spirit, tier-4]
aliases: ["upgrade_focus_lens"]
summary: "Target an enemy to Silence them. A portion of all damage dealt during the silence gets applied to the target when the silence wears off."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Focus Lens

Target an enemy to Silence them. A portion of all damage dealt during the silence gets applied to the target when the silence wears off.

## Identity and Purchase

- **Internal key:** `upgrade_focus_lens`
- **Numeric ID:** `2142980412`
- **Slot:** Spirit
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** press
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** Disruption, MagicDamage
- **Target types:** HeroEnemy

## Components

- `upgrade_spirit_sap`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Fire Rate | 10% | elevated |
| Active | Cast Range | 20m | normal |
| Active | Cooldown | 45s | normal |
| Active | Resist Reduction Duration | 12s | normal |
| Active | Duration | 4.5s | important |
| Active | Damage On Expire | 30% | important |
| Active | Spirit Resist | -9% | important |
| Active | Spirit Power | -30 | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `PercentDamage`: 20
- `BonusFireRate`: 20
- `TechPowerReduction`: -26
- `MagicResistReduction`: -12
- `AbilityDuration`: 0.25
- `AbilityCooldown`: -12
