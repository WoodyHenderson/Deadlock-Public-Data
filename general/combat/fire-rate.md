---
id: general.combat.fire-rate
title: Fire Rate
domain: general
topics: [weapons, fire-rate, fire-rate-slow, stacking]
aliases: [attack speed, firing speed, bullets per second, gun cycle time]
summary: Wiki-described Fire Rate bonus and slow aggregation, asymmetric timing modifiers, and interpretation limits.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-11"
evidence_status: source_verified
sources:
  - wiki.fire-rate.110395
---

# Fire Rate

Fire Rate describes how frequently a weapon fires, not how much damage each
bullet deals. The wiki also calls it Bullets Per Second and describes its inverse
as gun cycle time (seconds per bullet). Retrieve the baseline weapon rate from
the owning hero's record. Pellet count, burst timing, reload downtime, and
ability-specific firing behavior require separate interpretation.

These rules reproduce the wiki's general calculation, not independently tested
gameplay. Structured formulas are in [general rules](../../data/universal-rules.yaml)
under `fire_rate`.

## Combining bonuses and slows

Use fractional percentage inputs: +20% is `0.20`, and a 25% slow is `0.25`.
Only include effects whose activation conditions are satisfied.

1. Add all positive Fire Rate bonuses: `B = sum(bonus_i)`.
2. Combine Fire Rate slows multiplicatively:
   `S = 1 - product(1 - slow_i)`.
3. Subtract the combined slow from the bonuses, then apply the lower bound:
   `M = max(-0.50, B - S)`.

The -50% floor applies to the **combined modifier**, not to each slow or to the
slow group before subtracting it from bonuses. No positive cap is established
by this source. Empty bonus/slow groups contribute zero.

## Applying the modifier

Let `R` be the base firing rate and `T = 1 / R` its corresponding interval.
The wiki distinguishes two cases:

| Combined modifier | Final rate | Equivalent interval |
| --- | --- | --- |
| `M >= 0` | `R * (1 + M)` | `T / (1 + M)` |
| `M < 0` | `R / (1 + abs(M))` | `T * (1 + abs(M))` |

The interval forms are algebraic equivalents, not evidence that every internal
weapon timer is modified this way. Under the separately labeled burst working
model, these transforms apply to the within-burst interval only; the post-burst
downtime stays fixed. They therefore do not describe a burst weapon's overall
average rate by themselves.

For an ordinary steady-rate weapon—or the affected within-burst interval—a
negative modifier lengthens the interval instead of directly subtracting the
same percentage from shots per second. Consequently:

- +50% modifier gives 150% of base firing rate.
- -25% modifier gives 80% of base firing rate, not 75%.
- -50% modifier gives about 66.67% of base firing rate, not 50%.

The wiki says the UI reports the combined modifier, not the resulting percentage
change in shots per second. Preserve precision until formatting the answer.

## Worked examples

These use hypothetical inputs, not claims about current item values.

**Bonuses only:** +20% and +30% add to +50%. A base rate of 10 shots/s becomes
15 shots/s; its equivalent interval decreases from 0.1s to about 0.06667s.

**Bonuses and slows:** +18% and +20% bonuses total 38%. Slows of 25% and 28%
combine to `1 - 0.75 * 0.72 = 46%`. Thus `M = 0.38 - 0.46 = -0.08`.
The resulting rate is `R / 1.08`, about 92.59% of base. The UI modifier is -8%,
but shots per second fall by about 7.41%.

**At the floor:** With no bonuses, 25%, 28%, and 32% slows combine to
`1 - 0.75 * 0.72 * 0.68 = 63.28%`. The modifier is clamped to -50%, yielding
`R / 1.5`, not `R * 0.50`.

## Scope and unresolved behavior

- **Burst weapons:** Under the current working model, apply Fire Rate to the
  within-burst firing portion as with ordinary guns, while leaving post-burst
  downtime unchanged. This is a runtime observation requiring primary
  verification, not a Wiki/API-verified timer implementation. See [burst
  profiles and examples](burst-weapons.md). The distinction between the actual
  last-shot-to-next-burst gap and the API's `cycle_time` remains unresolved.
- **Wind-up weapons:** The wiki notes that McGinnis and Victor wind up before
  reaching maximum rate. A steady-rate formula does not describe that ramp.
- **Reload and sustained DPS:** A firing rate alone does not incorporate reloads,
  magazine size, partial bursts, or other downtime.
- **Ability/item procs:** More weapon shots need not mean proportionally more
  procs. Resolve per-burst restrictions, cooldowns, and effect conditions from
  their own records.
- **Other modifiers:** Movement Slow is not Fire Rate Slow. Do not substitute
  movement-slow resistance or arbitrary negative stats for a Fire Rate slow
  without effect-specific evidence.

## Sources

Adapted from [Fire Rate, revision 110395](https://deadlock.wiki/Fire_Rate?oldid=110395),
**Calculation**, **Examples**, and the wind-up notes under **Base Fire Rate**.
The live rendered hero/item tables are not imported here; their dependencies
can change independently of the article revision. Existing hero and item
records remain the authority for snapshot-specific inputs.
