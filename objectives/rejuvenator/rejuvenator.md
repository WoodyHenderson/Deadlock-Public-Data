---
id: objective.rejuvenator
title: Rejuvenator
domain: objectives
topics:
  - Mid-Boss
  - Rejuvenator
  - revive-credit
  - team-buff
aliases:
  - Rejuv
  - Rejuvenator crystal
  - Rejuvenation Credit
summary: Claim and expiration rules for the team revive credits dropped by the Mid-Boss.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-04"
evidence_status: source_verified
sources:
  - github.deadlock-data.gameplay.311b2e8d895e
  - wiki.rejuvenator.125036
  - wiki.mid-boss.107274
---

# Rejuvenator

Defeating the Mid-Boss creates a Rejuvenator crystal that descends for six
seconds. It cannot be claimed until it lands. Either team may claim it, including
a team that did not kill the Mid-Boss.

Each heavy-melee hit grants one team-wide Rejuvenation Credit, up to three
credits from the crystal. The first successful claimant is also healed to full.
The buff lasts three minutes or until all credits are consumed.

A participating hero who dies consumes one team credit and revives at the death
location after three seconds with full health. Each hero can consume at most one
credit from that buff. During the delay the hero counts as dead, does not contest
an Unstable Rift, and does not supply ally-presence effects.

A death covered by a Rejuvenation Credit grants no Souls and is not shown as a
kill in the HUD, but it still triggers effects whose condition is an enemy hero
kill. Exact structured values and conditions are canonical in the adjacent YAML.
