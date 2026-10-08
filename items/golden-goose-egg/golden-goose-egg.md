---
id: item.golden-goose-egg
title: "Golden Goose Egg"
domain: items
topics: [item, spirit, tier-1]
aliases: ["upgrade_goose_egg"]
summary: "Gain souls over time, as long as you are alive."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
  - github.deadlock-data.changelogs.raw.fc4f540f12e0
---

# Golden Goose Egg

Gain souls over time, as long as you are alive.

## Identity and Purchase

- **Internal key:** `upgrade_goose_egg`
- **Numeric ID:** `2462046703`
- **Slot:** Spirit
- **Tier:** 1
- **Cost:** 800 souls
- **Activation:** instant_cast
- **Active item:** yes
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** Movement
- **Target types:** none listed

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Sprint Speed | 1m | normal |
| Innate | Out of Combat Regen | 1 | normal |
| Innate | Damage Penalty | -15% | elevated |
| Active | Soul Value per Minute | 80 | important |

## Patch-Note-Only Behavior Notes

- **patch_note_only:** The September 16 patch notes state stored Souls on Golden Goose Egg now count toward net worth for comeback calculations. The structured item datasets do not expose an independent field for this behavior. Source: `github.deadlock-data.changelogs.raw.fc4f540f12e0`.

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `BonusSprintSpeed`: 5
- `OutOfCombatHealthRegen`: 10
- `BonusBuffsPerGold`: -50
- `OutgoingDamagePenaltyPercent`: 20
