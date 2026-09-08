---
id: item.arctic-blast
title: "Arctic Blast"
domain: items
topics: [item, spirit, tier-4]
aliases: ["upgrade_arctic_blast"]
summary: "Release an expanding ice blast that deals spirit damage, Freezing and then Slowing targets it hits. Slowed targets have their stamina regen frozen"
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6684.source-10933105
  - github.deadlock-data.items.311b2e8d895e
---

# Arctic Blast

Release an expanding ice blast that deals spirit damage, Freezing and then Slowing targets it hits. Slowed targets have their stamina regen frozen

## Identity and Purchase

- **Internal key:** `upgrade_arctic_blast`
- **Numeric ID:** `3812615317`
- **Slot:** Spirit
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** instant_cast
- **Active item:** yes
- **Imbued item:** no
- **Shop filters:** MagicDamage, Disruption, Durability
- **Target types:** AllEnemy

## Components

- `upgrade_cold_front`

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Spirit Resist | 10% | normal |
| Active | End Radius | 16m | normal |
| Active | Cooldown | 24.0s | normal |
| Active | Damage | 175 | important |
| Active | Freeze Duration | 1s | important |

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `Damage`: 150
- `AbilityCooldown`: -12
- `TechResist`: 15
- `FreezeDuration`: 0.25
