---
id: item.spirit-burn
title: "Spirit Burn"
domain: items
topics: [item, spirit, tier-4]
aliases: ["upgrade_spirit_burn"]
summary: "Dealing significant spirit damage to an enemy within 5s causes an explosion dealing damage and a burn to that enemy. While burning, enemies take damage over time and receive reduced healing. The cooldown is per enemy, so each target can only be burned once per cooldown. Deals half-damage on non-heroes."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
---

# Spirit Burn

Dealing significant spirit damage to an enemy within 5s causes an explosion dealing damage and a burn to that enemy. While burning, enemies take damage over time and receive reduced healing. The cooldown is per enemy, so each target can only be burned once per cooldown. Deals half-damage on non-heroes.

## Identity and Purchase

- **Internal key:** `upgrade_spirit_burn`
- **Numeric ID:** `343572757`
- **Slot:** Spirit
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** MagicDamage, Durability
- **Target types:** AllEnemy

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Ability Range | 6% | normal |
| Passive | Immunity Duration | 20s | normal |
| Passive | Debuff Duration | 8s | normal |
| Passive | Healing Reduction | -70% | normal |
| Passive | Damage Threshold | 500 | important |
| Passive | Explosion Damage | 50 | important |
| Passive | Damage Per Second | 24 | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `ExplosionDamage`: 160
- `TechRadiusMultiplier`: 12
- `TechRangeMultiplier`: 12
- `DPS`: 20
- `ImmunityDuration`: -6
