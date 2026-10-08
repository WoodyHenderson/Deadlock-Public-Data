---
id: item.lifestrike
title: "Lifestrike"
domain: items
topics: [item, vitality, tier-3]
aliases: ["upgrade_boxing_glove"]
summary: "Your Melee Attack applies Movement Slow and heals you for a percentage of the Melee Damage dealt plus a fixed amount. This heal is 40% effective vs non-heroes. Cooldown is 1.5x as long for Light Melee hits."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Lifestrike

Your Melee Attack applies Movement Slow and heals you for a percentage of the Melee Damage dealt plus a fixed amount. This heal is 40% effective vs non-heroes. Cooldown is 1.5x as long for Light Melee hits.

## Identity and Purchase

- **Internal key:** `upgrade_boxing_glove`
- **Numeric ID:** `1252627263`
- **Slot:** Vitality
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** Durability, Melee, Healing
- **Target types:** AllEnemy

## Components

- `upgrade_lifestrike_gauntlets`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 125 | normal |
| Innate | Melee Damage | 16% | elevated |
| Passive | Slow Duration | 2.5s | normal |
| Passive | Cooldown | 4.0s | normal |
| Passive | Move Speed | 48% | important |
| Passive | Heal on Melee Hit | 120 | important |
| Passive | Melee Hit Heal | 35% | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BonusMeleeDamagePercent`: 10
- `BonusHealth`: 125
- `AbilityCooldown`: -3
