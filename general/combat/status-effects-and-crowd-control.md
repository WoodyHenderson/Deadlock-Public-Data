---
id: general.combat.status-effects-and-crowd-control
title: Status Effects and Crowd Control
domain: general
topics:
  - status-effects
  - buffs
  - debuffs
  - crowd-control
aliases:
  - CC
  - stun
  - silence
  - immobilize
  - debuff resistance
summary: Universal terminology for buffs, debuffs, crowd control, reductions, and immunities.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - wiki.status-effects.114074
  - wiki.crowd-control.110151
---

# Status Effects and Crowd Control

A status effect temporarily modifies a unit after a condition is met. Positive
effects are buffs; negative effects are debuffs. Crowd Control, or CC, is the
subset that restricts movement, weapon use, abilities, items, or actions.

## Common Buff Concepts

- **Barrier:** A temporary pool that absorbs applicable incoming damage before
  breaking.
- **Invincibility:** Prevents hostile targeting and damage for its duration.
- **Regeneration:** Restores health over time rather than as an instant heal.
- **Lifesteal:** Heals for a percentage of applicable damage dealt.
- **Resistance buff:** Reduces incoming damage of the specified classification.
- **Stealth:** Makes the hero invisible, subject to source-specific proximity,
  attack, ability, and damage reveal rules.
- **Unstoppable:** Grants immunity to crowd-control effects but does not prevent
  damage.

## Crowd-Control Terms

| Effect | General behavior |
| --- | --- |
| Movement Slow | Reduces movement and sprint speed; cannot reduce speed below 2 m/s. |
| Stun | Prevents movement and all actions and also interrupts current casts or channels. |
| Sleep | Prevents attacks and abilities and limits movement; Sleep does not itself interrupt a channel. Damage does not universally wake the target instantly: each sleep ability defines its own wake threshold, timer, or condition. |
| Immobilize | Sets voluntary movement speed to zero, blocks movement abilities, and removes upward acceleration; attacks and non-movement abilities remain available. |
| Silence | Prevents ability activation but normally allows active items; it does not interrupt an ability already in progress. |
| Item Silence | Prevents applicable active-item use without necessarily silencing abilities. |
| Disarm | Prevents firing the main weapon; melee and abilities remain available. |
| Interrupt | Immediately cancels a cast or channel but does not prevent starting another afterward. |
| Displace | Applies force that changes the target's position, acceleration, or velocity. |
| Time Stop | Slows movement, animations, casts, channels, inertia, and gravity; already active effects can continue functioning. |
| Curse | Combines interrupt, disarm, ability silence, and active-item silence. |

## Diminishing Returns

Stun, Sleep, Immobilize, tether-style Chain, and Silence are subject to CC
diminishing returns. Applying one of these within nine seconds of another in the
set reduces the new effect's duration. The reduction begins at 15% and can scale
to 35% based on recent qualifying effects. Multiple qualifying effects applied
by one action count as one CC application.

## Slow Resistance

Slow Resistance reduces the strength of a movement slow:

`modified speed = base speed * (1 - slow * (1 - slow resistance))`

For example, 50% Slow Resistance turns a 30% slow into an effective 15% slow.

## Debuff Counters

- **Debuff Resistance** reduces the duration of applicable debuffs; individual
  effects can opt out.
- **Purge** removes active debuffs. Source-specific purges differ in whether they
  can remove effects from ultimate abilities.
- **Unstoppable** prevents crowd control while active.
- **Invincibility** prevents hostile effects from hitting or targeting the hero.

Parry's stun and vulnerability explicitly ignore Debuff Resistance. Effect-level
exceptions must be stored with the effect rather than inferred from these
general rules.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Status Effects](https://deadlock.wiki/Status_Effects?oldid=114074) and
[Crowd Control](https://deadlock.wiki/Crowd_Control?oldid=110151).
