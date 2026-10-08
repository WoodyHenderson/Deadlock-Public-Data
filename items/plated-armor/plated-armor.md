---
id: item.plated-armor
title: "Plated Armor"
domain: items
topics: [item, vitality, tier-4]
aliases: ["upgrade_deflecting_armor"]
summary: "Gain a chance to either deflect incoming bullets, preventing all weapon damage or prevent all on-hit effects from bullets."
snapshot_id: deadlock-wiki-2026-09-16
current_as_of: "2026-09-16"
evidence_status: source_verified
sources:
  - deadlock-api.items.client-6694.source-11005995
  - github.deadlock-data.items.fc4f540f12e0
  - github.deadlock-data.changelogs.raw.fc4f540f12e0
---

# Plated Armor

Gain a chance to either deflect incoming bullets, preventing all weapon damage or prevent all on-hit effects from bullets.

## Identity and Purchase

- **Internal key:** `upgrade_deflecting_armor`
- **Numeric ID:** `3491236900`
- **Slot:** Vitality
- **Tier:** 4
- **Cost:** 6400 souls
- **Activation:** passive
- **Active item:** no
- **Game mode:** standard
- **Imbued item:** no
- **Shop filters:** Durability
- **Target types:** none listed

## Components

No component item is listed.

## Displayed Effects

| Section | Effect | Value | Status |
| --- | --- | ---: | --- |
| Innate | Bonus Health | 130 | normal |
| Passive | Deflection Percent | 30% | important |
| Passive | On-Hit Prevention Percent | 50% | important |

## Patch-Note-Only Behavior Notes

- **patch_note_only:** The September 16 patch notes report that on-hit damage prevention now also blocks the on-hit Spirit damage effects from Mercurial Magnum, Vindicta's Flight, Wraith's Full Auto, and Tesla Bullets/Capacitor. This interaction list is patch-note evidence, not an independently exposed structured runtime rule. Source: `github.deadlock-data.changelogs.raw.fc4f540f12e0`.

## Source Property-Upgrade Fields

### Property-upgrade block 1

- `DeflectionPercent`: 15
- `BulletProcDeflectionPercent`: 15
