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
claim about exact wall-jump fatigue recovery. Advanced engine techniques and
hero-specific movement interactions are excluded from this trusted general
baseline.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Movement](https://deadlock.wiki/Movement?oldid=78724) and
[Mechanics](https://deadlock.wiki/Mechanics?oldid=110139).
