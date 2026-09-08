---
id: general.combat.weapons-melee-and-parry
title: Weapons, Melee, and Parry
domain: general
topics:
  - weapons
  - melee
  - parry
  - combat
aliases:
  - light melee
  - heavy melee
  - gun
  - punch
summary: Universal ranged attacks, light and heavy melee, and the defensive parry mechanic.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-03"
evidence_status: source_verified
sources:
  - wiki.mechanics.110139
  - wiki.melee-attack.114941
  - wiki.melee-damage.104072
---

# Weapons, Melee, and Parry

Every hero has a ranged projectile weapon, light and heavy melee attacks, a
parry, and four hero-specific abilities. This document covers only the universal
weapon, melee, and parry rules.

## Ranged Weapons

Weapon behavior varies by hero, including bullet damage, projectile count,
magazine size, fire rate, reload time, projectile velocity, and effective
range. These values belong in hero-specific structured records and are not part
of the general baseline.

Ranged attacks can damage enemies and claim floating Soul Orbs. One bullet or
pellet claims an orb regardless of its damage, and the claiming shot is refunded
to the magazine.

## Light and Heavy Melee

Pressing the melee control performs a fast light melee. Holding it charges a
heavy melee that deals more damage, lunges forward, has greater reach, and
restricts turning during the animation. Heavy melee can be charged while
airborne and can help reach a ledge without spending stamina.

Heavy melee normally has a one-second cooldown. Missing increases that cooldown
to 1.3 seconds. A heavy melee is required to claim powerups, Rejuvenator credits,
and dropped Unsecured Soul Containers.

Melee-last-hitting a Trooper grants the full bounty without producing ground or
floating Soul Orbs. Melee is also the required interaction for Sinner's
Sacrifice machines; each hit causes 80 retaliation damage to the attacker.

Melee attacks pause an in-progress reload and the reload resumes after the
animation. Melee damage gains 50% of the effect of general Weapon Damage bonuses,
in addition to melee-specific modifiers.

## Parry

Parry is available to every hero. Its animation lasts one second, with incoming
melee attacks parried during the first 0.75 seconds.

A successful parry against an enemy hero:

- prevents the incoming melee damage;
- stuns the attacker for 2.75 seconds;
- causes the attacker to take 25% more damage from all sources for that duration;
- ends the parry animation early and refunds the parry cooldown.

The stun and damage vulnerability from a parry are not shortened by Debuff
Resistance. Unstoppable can prevent the stun. After success, there is a
0.3-second recovery before the defender can act again.

An unsuccessful parry has a 4.5-second cooldown. Trooper melee can be parried,
but doing so neither refunds the cooldown nor ends the parry early. Guardian
melee can also be parried; Walkers cannot normally be parried.

Parrying preserves current movement momentum, so it can be performed while
jumping or dashing.

## Source Notes

Adapted from the pinned Deadlock Wiki revisions for
[Mechanics](https://deadlock.wiki/Mechanics?oldid=110139),
[Melee Attack](https://deadlock.wiki/Melee_Attack?oldid=114941), and
[Melee Damage](https://deadlock.wiki/Melee_Damage?oldid=104072).
