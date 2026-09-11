---
id: general.combat.burst-weapons
title: Burst Weapons and Timing
domain: general
topics: [weapons, burst, fire-rate, intervals, timing]
aliases: [burst interval, intra-burst interval, burst delay, between bursts]
summary: Baseline burst profiles, API-derived averages, conditional fixed-gap examples, and unresolved timing semantics.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-11"
evidence_status: needs_primary_verification
sources:
  - deadlock-api.weapon.gigawatt.client-6684
  - deadlock-api.weapon.lash.client-6684
  - deadlock-api.weapon.chrono.client-6684
  - deadlock-api.weapon.magician.client-6684
---

# Burst Weapons and Timing

A burst consists of sequential shots. It is different from a shotgun firing
multiple pellets simultaneously, and from the item named Burst Fire.
The baseline hero records distinguish `BulletsPerBurst` from `BulletsPerShot`.

**Coverage boundary:** The baseline fields below are API-supported. The
fixed-gap example is conditional mathematics, not a verified gameplay formula.
The available published sources do not independently establish which burst
timers Fire Rate changes. The separately labeled working model below changes
only within-burst timing; do not apply the general multiplier directly to the
whole-burst average or post-burst downtime.

Structured companion: [burst timing data](../../data/burst-weapons.yaml).
General bonus/slow aggregation: [Fire Rate](fire-rate.md).

## Baseline profiles — client 6684

These are unmodified fields from the versioned API. Times here are milliseconds;
the structured record preserves seconds and the API's precision.

| Hero | Shots per burst | `intra_burst_cycle_time` | `cycle_time` | API shots/s |
| --- | ---: | ---: | ---: | ---: |
| [Seven](../../heroes/seven/seven.md) | 3 | 84 ms | 262.5 ms | 5.830904 |
| [Lash](../../heroes/lash/lash.md) | 3 | 84 ms | 262.5 ms | 5.830904 |
| [Paradox](../../heroes/paradox/paradox.md) | 5 | 73.5 ms | 294 ms | 7.558579 |
| [Sinclair](../../heroes/sinclair/sinclair.md) | 2 | 105 ms | 525 ms | 2.721088 |

All four records have one bullet per shot and `burst_shot_cooldown = 0`.
That zero does **not** prove there is no pause between bursts.

## Reproducing the API average

Let `N = burst_shot_count`, `I = intra_burst_cycle_time`, and `C = cycle_time`.
The returned API rate is reproduced by:

```text
API period = N * I + C
API shots/s = N / (N * I + C)
```

For Seven and Lash: `3 / (3 * 0.084 + 0.2625) = 5.83090379 shots/s`.
For Paradox: `5 / (5 * 0.0735 + 0.294) = 7.55857899 shots/s`.
For Sinclair: `2 / (2 * 0.105 + 0.525) = 2.72108844 shots/s`.

These reproduce an API-derived average; they are not measured shot timelines.

### Working interpretation of `cycle_time`

The current working model treats `cycle_time` as the actual elapsed time from
the last shot of one burst to the first shot of the next. This interpretation is
not expressly confirmed by the API or Wiki. If N shots are evenly spaced by I,
only **N−1** intervals separate the first and last shots. Define G as the actual
last-shot-to-next-first-shot gap:

```text
first-shot-to-next-first-shot period = (N - 1) * I + G
```

The API average expression instead uses **N** intervals plus C. Under the
working interpretation, C is the gap G, so this API expression does not map
cleanly onto the first-shot-to-next-first-shot timeline. For Seven, using
`G = 0.2625s` gives a 0.4305s timeline period and about 6.969 shots/s, which
differs from the API's 5.831. The API-derived gap estimates below preserve the
alternative `G = I + C` reconciliation for traceability; they are not the
current working assumption or measured runtime values. Do not silently resolve
the discrepancy by renaming a field or treating the API rate as a runtime
measurement.

### Estimated gaps for descriptive answers

Using the alternative `G = I + C` reconciliation, retain these as **API-derived
estimates only**; the current working assumption instead treats `C` as `G`:

| Hero | Estimated last-bullet-to-next-burst gap |
| --- | ---: |
| Seven | approximately 0.35s |
| Lash | approximately 0.35s |
| Paradox | approximately 0.37s |
| Sinclair | approximately 0.63s |

These are API-implied estimates, not independently measured values. Their
unrounded derivations are preserved in the structured record for traceability,
not to imply measurement precision. Use them for approximate descriptions;
do not present them as exact runtime constants or verified modified-DPS inputs.
No measured error bound is available, and Sinclair's estimate should not be
silently rounded down to the same gap as the other three heroes.

## Conditional example: a fixed gap, faster bullets within the burst

**Assumptions for this example only:** a three-shot burst, 0.1s between its
shots, and a fixed 0.3s last-shot-to-next-burst gap. These are hypothetical
inputs, not the measured profile of Seven or another hero.

At baseline, shot times could be `0.0, 0.1, 0.2`, followed by the next burst
starting at `0.5`. The rate is `3 / (2 * 0.1 + 0.3) = 6 shots/s`.

Suppose a +50% modifier changes **only** the intra-burst interval to
`0.1 / 1.5 = 0.066667s`, leaving G at 0.3s:

```text
shot times: 0.0, 0.066667, 0.133333
next burst starts: 0.433333
average shots/s: 3 / (2 * (0.1 / 1.5) + 0.3) = 6.923077
```

This is about **15.38% more shots/s**, not 50% more. The pause after the last
bullet is unchanged, but the next burst starts sooner because the previous
burst finishes sooner. Thus “the gap is fixed” does not mean “the time between
burst starts is fixed.”

Even under this fixed-gap assumption, there are two different hypotheses:

- **Keep the actual G fixed:** `(N - 1) * modified_I + G`.
- **Keep the API field C fixed:** `N * modified_I + C`.

They predict different results after modification even if they match the same
baseline average. A statement about an unchanged between-burst gap must specify
which interval was observed; these formulas are not interchangeable.

## Review observations and remaining questions

The current working model, based on runtime observations supplied during review
rather than an independently pinned public source, is:

- Fire Rate bonuses and slows change the within-burst bullet interval using the
  same interval transform as ordinary guns. Under this working model, a +25%
  modifier divides each within-burst interval—and therefore the first-to-last
  firing duration—by 1.25. That duration becomes 80% of baseline, commonly
  described as firing 25% faster.
- Downtime after a burst is unaffected by either Fire Rate bonuses or Fire Rate
  slows. Faster within-burst firing can therefore make the next burst begin
  sooner even when the post-burst downtime itself is unchanged.
- If a magazine has fewer rounds than a full burst requires, the weapon fires
  the remaining rounds and then begins reloading.
- Bullet-based procs, including Toxic Bullets and Mercurial Magnum, trigger per
  qualifying bullet rather than once per burst, subject to their own conditions
  and cooldowns.

These observations are recorded as `needs_primary_verification` in the
structured data and should not be presented as Wiki/API-verified facts.

The remaining public-source questions are:

1. **Timer mapping:** Does API `cycle_time` represent first-to-last within-burst
   duration, or an API-derived timing value with another convention? The supplied
   observation that the inter-burst downtime is approximately 0.3s is retained
   as an estimate, not a precise universal constant.
2. **Proc exceptions:** Resolve any effect-specific cooldown, build-up,
   once-per-shot, or once-per-burst restriction from that effect's record. The
   working default is per qualifying bullet, not an unconditional promise that
   every bullet always procs every effect.

## Sources and evidence limits

Versioned API responses are registered individually with retrieval dates and
response hashes. Their fields provide source support, not independent engine
validation. The modified burst-rate behavior is explicitly labeled as a working
observation, and no executable combat calculation has been added. Unresolved
questions are also recorded in the structured companion.
