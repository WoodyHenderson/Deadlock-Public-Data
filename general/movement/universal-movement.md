---
id: general.movement.universal-movement
title: Universal Movement
domain: general
topics:
  - movement
  - stamina
  - dash
  - jump
  - slide
  - mantle
  - move speed
  - sprint speed
  - movement speed
aliases:
  - air jump
  - double jump
  - dash jump
  - wall jump
  - down dash
summary: Movement actions available to all heroes and their baseline stamina costs.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_conflict
sources:
  - wiki.movement.78724
  - wiki.mechanics.110139
  - wiki.move-speed.146579
---

# Universal Movement

Deadlock movement combines ordinary running and jumping with stamina-powered
actions and map traversal systems. Hero-specific movement speeds and abilities
are outside this baseline.

Distances are displayed in meters and speeds in meters per second. The Source 2
engine uses Hammer units internally; the Movement page approximates one Hammer
unit as 0.0254 meters. Deadlock has no fall damage.

## Running, Sprinting, Crouching, and Sliding

Heroes move with directional controls, jump, and crouch. Sprint activates after
the hero has been out of combat for five seconds. Entering combat or zooming in
ends sprint and returns movement to base speed.

**Move Speed** is the hero's ordinary movement velocity. Move-speed bonuses from
items and abilities stack with diminishing returns rather than simply adding. For
bonuses expressed in meters per second, the Wiki describes the effective bonus
as:

`12 × (1 − product(1 − bonus_i / 12))`

The effective bonus is added to base Move Speed. **Sprint Speed** is separate and
is added to Move Speed while sprinting; sprint bonuses stack additively. Sprint
speed above 2.5 m/s ramps in at 0.6 m/s per second while moving, rather than
appearing immediately at full value.

While firing, a hero normally moves at 75% of the combined Move Speed and Sprint
Speed. Fleetfoot can mitigate this penalty. Zooming does not incur the firing
penalty. Crouch speed is normally 4.8 m/s and is not affected by firing, except
Grey Talon and Warden use 4.4 m/s while firing. Rem and Silver in transformed
form are exceptions to the normal firing movement penalty.

Sprinting is interrupted or reset by taking damage, shooting an enemy hero,
being stunned, immobilized, displaced, or slept, using a Zipline, crouching,
stopping movement input, or zooming in. Light melee, heavy melee, shooting
neutral camps without taking damage, shooting breakables, sliding, using a
Teleporter, walking into walls/corners, and flying on Magic Carpet do not
normally interrupt it. These state transitions are separate from the five-second
condition that initially activates sprint.

Crouching lowers the hero's profile. At sufficient speed, holding crouch starts
a slide that preserves momentum. Sliding also grants infinite ammunition for
the slide's duration.

The pinned sources conflict on the exact flat-ground slide threshold: the
Movement page reports 8.9 m/s, while the Mechanics hub reports 9.6 m/s. Slopes
can initiate a slide separately. No exact slide threshold should be used by a
calculation until this conflict is verified.

## Stamina Actions

For hero-specific dash-speed tiers and ground/air dash durations, see
[Hero Stamina Buckets](hero-stamina-buckets.md).

| Action | Baseline stamina cost | Baseline airborne limit |
| --- | --- | --- |
| Ground dash | 1 | Not applicable |
| Air dash | 1 | Once per jump |
| Air jump | 1 | Once per jump |
| Dash jump | 2 total: 1 for dash and 1 for jump | Not applicable |
| Down dash | 0.5 | Once per jump |
| First wall jump | 0 | Not specified |
| Further wall jumps before landing | 0.5 each | Subject to increasing fatigue |

A dash jump is performed by jumping during the timing window of a ground dash;
the stamina display turns blue during that window. An air dash has less slowdown
at the end than a ground dash. Double-tapping crouch in the air performs a down
dash.

## Wall and Ledge Movement

A wall jump pushes the hero away from a nearby wall. Repeated wall jumps before
landing cost stamina and lose height through fatigue. A wall slide slows the
hero's descent. Mantling climbs a reachable ledge when the player jumps toward
it; holding crouch during the mantle creates a mantle glide with an exit speed
boost.

A melee hit against a hero who is mantling or climbing applies an 80% movement
slow that tapers to 20% over two seconds.

## Source Limitations

The Movement page was marked under construction and included a citation-needed
claim about exact wall-jump fatigue recovery. The Move Speed article's generic
movement formula and many reset conditions are useful reference rules, but
hero-, item-, and ability-specific exceptions should be resolved from their
individual records. The exact flat-ground slide threshold remains disputed:
the Movement page reports 8.9 m/s while the Mechanics hub reports 9.6 m/s.
Advanced engine techniques remain excluded from this trusted general baseline.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Movement](https://deadlock.wiki/Movement?oldid=78724),
[Mechanics](https://deadlock.wiki/Mechanics?oldid=110139), and
[Move Speed](https://deadlock.wiki/Move_Speed?oldid=146579).
