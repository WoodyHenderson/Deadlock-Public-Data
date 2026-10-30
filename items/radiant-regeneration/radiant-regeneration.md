---
id: item.radiant-regeneration
title: "Radiant Regeneration"
domain: items
topics: [item, spirit, tier-3]
aliases: ["upgrade_resonant_healing"]
summary: "Heal and gain bonus Movement Speed for a short duration when you cast an ability."
snapshot_id: deadlock-data-client-6785
current_as_of: "2026-10-14"
evidence_status: source_verified_with_official_balance_note
sources:
  - deadlock-api.items.client-6785.source-11132425
  - github.deadlock-data.gameplay.3aab395a1392
  - steam.news.deadman-danny-oct14-update.1846651706676198
  - github.deadlock-data.raw-changelog.2026-10-14.3aab395a1392
---

# Radiant Regeneration

Heal and gain bonus Movement Speed for a short duration when you cast an ability.

## Identity and Purchase

- **Internal key:** `upgrade_resonant_healing`
- **Numeric ID:** `2947183272`
- **Slot:** Spirit
- **Tier:** 3
- **Cost:** 3200 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** regen
- **Target types:** none listed

## Components

- `upgrade_mystic_regeneration`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 90 | normal |
| Passive | Regeneration Duration | 7s | normal |
| Passive | Regeneration | 4 HP/s | important |
| Other | Cooldown | 6.0s | normal |
| Other | Duration | 3s | normal |
| Other | Healing on Ability Cast | 65 | important |
| Other | Move Speed | 1.75m | important |

## October 14 Balance Update

Spirit scaling is reduced from **0.04 to 0.035**. The previous client-6782 source, client-6785 API item asset, client-6785 `item-data.json`, and item card support the before/after coefficient; the official note states the same change.

This coefficient is structured source evidence, not a complete in-match healing formula or an independently tested runtime result. Other client-6785 source fields are retained without attributing them to this balance note.

[Official update note](https://store.steampowered.com/news/app/1422450/view/1846651706676198?l=english) · [Client-6785 API pin](https://api.deadlock-api.com/v1/assets/items?language=english&client_version=6785).
## Source Property-Upgrade Fields

### Property-upgrade block 1

- `Regeneration`: 9
- `HealingPerCast`: 60
- `BonusHealth`: 110
- `BonusMoveSpeed`: 1m
