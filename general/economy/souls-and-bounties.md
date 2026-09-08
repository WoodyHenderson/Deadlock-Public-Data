---
id: general.economy.souls-and-bounties
title: Souls and Bounties
domain: general
topics:
  - Souls
  - economy
  - Soul-Orbs
  - bounties
  - unsecured-Souls
  - comeback
aliases:
  - currency
  - XP
  - experience
  - denies
  - confirms
summary: How Souls are earned, shared, secured, denied, dropped, and adjusted by catch-up systems.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - wiki.souls.124122
  - wiki.trooper.114174
  - wiki.neutral.125766
---

# Souls and Bounties

Souls are both spendable currency and the experience used for level progression.
Every player starts with 600 Souls. Spending Souls does not remove previously
earned level progress.

## Common Sources

Players gain Souls from Troopers, enemy heroes, structures, neutral camps,
Sinner's Sacrifice machines, crates, the Soul Urn, the Unstable Rift, and other
specific effects. The amount paid for a kill or objective is its bounty.

The current baseline values and growth rates are stored in
`data/economy.yaml`. Important general values include:

- first blood grants a 125-Soul bonus;
- hero kills start at a base bounty of 200, grow by 50 per match minute, and cap
  at 2,200 at 40 minutes;
- standard Troopers are worth 100 plus 2 per match minute;
- objective bounties do not grow with time in the pinned source.

## Floating and Ground Soul Orbs

A normally killed Trooper produces a ground orb and a floating orb, each worth
half of its bounty. Ground orbs cannot be denied. Floating orbs initially appear
dark, then light up and become claimable. Allies confirm their own floating
orbs; enemies deny them and receive the value instead.

If no player claims a floating orb, it automatically awards nearby allies after
about one second. If no allies are nearby, its value is lost. One bullet or
pellet claims an orb regardless of damage, and that shot is refunded to the
weapon's magazine. Latency compensation can affect which competing shot wins.

Melee-last-hitting a Trooper bypasses both orb interactions and awards the full
bounty through normal sharing.

## Local Sharing

For a Trooper reward, allied heroes join the sharing pool when they are within
either of these areas at the time the orb is claimed:

- 45 meters of the Soul Orb;
- 30 meters of the hero who killed the Trooper.

Trooper sharing is not a simple equal split for every party size; the canonical
percentages are in `data/economy.yaml`.

Hero-kill participants qualify for an assist by damaging the killed hero in the
previous ten seconds. Hero-kill sharing uses a separate table, and the killer
receives an additional bonus on multi-player kills.

Neutral bounties are shared equally among allied players who damaged the unit.
Neutrals do not create Soul Orbs.

## Secured and Unsecured Souls

Souls from neutrals, Sinner's Sacrifice machines, and crates are Unsecured Souls.
They count toward spending and level progression immediately but can be lost on
death. Shops spend secured Souls before unsecured Souls.

Unsecured Souls convert to secured Souls every second. The pinned wiki formula
combines:

- 0.5% of the player's current unsecured balance per second;
- a base 1.6 Souls per second that grows with the global bounty rate of 8% per
  match minute.

On death, an unsecured balance of at least `50 + 5 per match minute` drops in a
Soul Container. Any player can claim it with a heavy melee attack. It despawns
after three minutes. A smaller balance is lost without creating a container.

Losing unsecured Souls does not revoke an already reached level, but removes
the equivalent progress toward the next one.

## Comeback and Individual Catch-Up

The lower-net-worth team can receive up to 26% more Souls from Troopers,
neutrals, Sinner's Sacrifice machines, and objectives. The adjustment ignores
the first 3,000 Souls of team difference and reaches its maximum at a 20% net
worth difference.

Hero kills can pay substantially more when the killed hero is richer than the
killer team's average. After eight minutes, the two lowest-net-worth players on
each team also receive passive Soul catch-up equal to 2.5% and 1.5%,
respectively, of the Souls their team gathered during the measured second.

The Soul Urn has its own trailing-team reward adjustment.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Souls](https://deadlock.wiki/Souls?oldid=124122),
[Trooper](https://deadlock.wiki/Trooper?oldid=114174), and
[Neutral](https://deadlock.wiki/Neutral?oldid=125766).
