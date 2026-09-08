---
id: item.spirit-snatch
title: "Spirit Snatch"
domain: items
topics: [item, spirit, tier-3]
aliases: ["upgrade_spirit_snatch"]
summary: "When you perform a Light or Heavy Melee attack against a hero, the attack deals extra spirit damage and steals Spirit Resist and Spirit Power. Effects are reduced by 30% for Light Melee hits."
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Spirit Snatch

When you perform a Light or Heavy Melee attack against a hero, the attack deals extra spirit damage and steals Spirit Resist and Spirit Power. Effects are reduced by 30% for Light Melee hits.

## Identity and Purchase

- **Internal key:** `upgrade_spirit_snatch`
- **Numeric ID:** `3190916303`
- **Slot:** Spirit
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Imbued item:** no
- **Shop filters:** MagicDamage, Melee
- **Target types:** HeroEnemy

## Components

- `upgrade_acolytes_glove`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Melee Damage | 7% | normal |
| Innate | Bonus Health | 75 | normal |
| Passive | Duration | 10s | normal |
| Passive | Cooldown | 6.0s | normal |
| Passive | Spirit Damage | 50 | important |
| Passive | Spirit Resist Steal | 12% | important |
| Passive | Spirit Power Steal | 25 | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `SpiritDamage`: 50
- `TechArmorGain`: 5
- `TechArmorDamageReduction`: -5
- `TechPowerGain`: 35
- `TechPowerReduction`: -35
