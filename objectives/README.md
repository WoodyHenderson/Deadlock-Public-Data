# Objective Records

This directory is the canonical entity layer for claimable or contestable map
objectives that are not ordinary NPC units. NPC-backed objectives such as the
Mid-Boss and structures remain under `npcs/` and link here when
they create an objective reward.

Objective records store their unique claim, contest, ownership, expiration, and
reward behavior. Shared schedules and bounty formulas remain canonical in
`data/map-timings.yaml` and `data/economy.yaml`.
Unknown or disputed timing is never inferred.
