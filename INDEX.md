---
id: navigation.index
title: Deadlock Data Keyword Index
domain: meta
topics: [routing, retrieval, navigation, entities]
aliases: [entity index, keyword index]
summary: Direct routes to the public snapshot's hero, ability, item, NPC, objective, and mechanics records.
snapshot_id: deadlock-wiki-2026-09-03
current_as_of: "2026-09-08"
evidence_status: derived
sources: []
---

# Deadlock Data Keyword Index

This index is navigation derived from local records, not gameplay evidence.
Follow the destination's citations and uncertainty flags. Match full names with
context: “Pocket build” identifies a hero; “seven seconds” does not. Normalize
case and punctuation for lookup, but do not assume historical renames or aliases
that the records do not establish. Unknown names may need clarification.

Read Markdown for explanations and adjacent YAML for structured values. The
current snapshot is not a guarantee of live-game freshness. Questions involving
multiple entities require multiple records; a matching keyword is not proof that
the destination fully answers the question.

**Exclude `patches/` from default lookup.** Only consult it for an explicit
historical or patch-note request. Missing current data is not permission to use
historical values as current facts.

## Topic keywords

| Keywords | Starting records |
| --- | --- |
| Win condition, match objective | [Game loop](general/game-loop.md) |
| Souls, income, denies, bounty, comeback | [Economy](general/economy/souls-and-bounties.md); [data](data/economy.yaml) |
| Boons, levels, ability points, upgrades | [Progression](general/progression/boons-and-abilities.md); [data](data/progression.yaml) |
| Item cost, category, components | [Item roster](items/roster.yaml) and named items below; [transaction coverage limits](LIMITATIONS.md) |
| Damage, Spirit, resistance, healing, lifesteal | [Combat stats](general/combat/stats-damage-and-healing.md); [general rules](data/universal-rules.yaml); named effect |
| Weapon, fire rate, burst, magazine, reload | Owning hero's weapon fields below; [formula limitations](LIMITATIONS.md) |
| Cooldown, duration, radius, range, charges | Owning ability or item's explicit descriptions and fields below |
| Status effects, stun, slow, silence, disarm | [Status effects](general/combat/status-effects-and-crowd-control.md); named effect |
| Melee, heavy melee, parry | [Melee and parry](general/combat/weapons-melee-and-parry.md) |
| Stamina, dash, slide, wall jump | [Movement](general/movement/universal-movement.md) |
| Character buckets, stamina buckets, dash speed tiers, dash duration | [Hero stamina buckets](general/movement/hero-stamina-buckets.md) |
| Zipline, lanes, traversal | [Map layout](general/map/map-layout-and-traversal.md) |
| Minimap, detection, visibility | [Visibility](general/map/minimap-and-visibility.md); named ability |
| Death, respawn, revive | [Death](general/rules/death-and-respawning.md); [Rejuvenator](objectives/rejuvenator/rejuvenator.md) |
| Guardian, Walker, Shrine, Patron, Extra Slots, backdoor | [Structures](general/map/objectives-and-structures.md); specific NPC below |
| Trooper waves, Super Troopers | [Troopers](general/map/troopers-and-lane-pressure.md); troop NPC below |
| Spawn times, camps, Mid-Boss, Urn, powerups, Rift | [Timed events](general/map/timed-events-and-neutral-objectives.md); [timings](data/map-timings.yaml); entity below |
| Sources, citations, versions | [Source registry](sources/source-registry.yaml); [attribution](ATTRIBUTION.md) |
| Explicit request for patch notes or change history | [Archive policy](patches/README.md); [manifest](patches/manifest.yaml) |

<!-- entity-routes:start -->
## Heroes and abilities

Each row maps the hero **and every listed ability name** to the same hero
record. Read its Markdown for descriptions; the adjacent, same-named YAML
holds exact fields. Names reflect the pinned roster, not a live-game check.

| Hero / recorded aliases | Ability keywords → this hero |
| --- | --- |
| [Abrams](heroes/abrams/abrams.md) | Siphon Life; Shoulder Charge; Infernal Resilience; Seismic Impact |
| [Apollo](heroes/apollo/apollo.md) | Disengaging Sigil; Riposte; Flawless Advance; Itani Lo Sahn |
| [Bebop](heroes/bebop/bebop.md) | Exploding Uppercut; Sticky Bomb; Grapple Arm; Hyper Beam |
| [Billy](heroes/billy/billy.md) | Bashdown; Rising Ram; Blasted; Chain Gang |
| [Calico](heroes/calico/calico.md) | Gloom Bombs; Leaping Slash; Ava; Return to Shadows |
| [Celeste](heroes/celeste/celeste.md) | Light Eater; Dazzling Trick; Radiant Daggers; Shining Wonder |
| [Drifter](heroes/drifter/drifter.md) | Rend; Stalker's Mark; Bloodscent; Eternal Night |
| [Dynamo](heroes/dynamo/dynamo.md) | Kinetic Pulse; Quantum Entanglement; Rejuvenating Aurora; Singularity |
| [Graves](heroes/graves/graves.md) | Jar of Dead; Grasping Hands; Essence Theft; Borrowed Decree |
| [Grey Talon](heroes/grey-talon/grey-talon.md) | Charged Shot; Rain of Arrows; Spirit Snare; Guided Owl |
| [Haze](heroes/haze/haze.md) | Sleep Dagger; Smoke Bomb; Fixation; Bullet Dance |
| [Holliday](heroes/holliday/holliday.md) | Powder Keg; Bounce Pad; Crackshot; Spirit Lasso |
| [Infernus](heroes/infernus/infernus.md) | Napalm; Flame Dash; Afterburn; Concussive Combustion |
| [Ivy](heroes/ivy/ivy.md) | Entangling Thorns; Kudzu Connection; Stone Form; Air Drop |
| [Kelvin](heroes/kelvin/kelvin.md) | Frost Grenade; Ice Path; Arctic Beam; Frozen Shelter |
| [Lady Geist](heroes/lady-geist/lady-geist.md) | Essence Bomb; Life Drain; Malice; Soul Exchange |
| [Lash](heroes/lash/lash.md) | Ground Strike; Grapple; Flog; Death Slam |
| [McGinnis](heroes/mcginnis/mcginnis.md) | Mini Turret; Medicinal Specter; Spectral Wall; Heavy Barrage |
| [Mina](heroes/mina/mina.md) | Rake; Sanguine Retreat; Love Bites; Nox Nostra |
| [Mirage](heroes/mirage/mirage.md) | Fire Scarabs; Dust Devil; Djinn's Mark; Traveler |
| [Mo & Krill](heroes/mo-and-krill/mo-and-krill.md) | Scorn; Burrow; Sand Blast; Combo |
| [Paige](heroes/paige/paige.md) | Bookwyrm; Plot Armor; Captivating Read; Rallying Charge |
| [Paradox](heroes/paradox/paradox.md) | Pulse Grenade; Time Wall; Kinetic Carbine; Paradoxical Swap |
| [Pocket](heroes/pocket/pocket.md) | Barrage; Flying Cloak; Enchanter's Satchel; Affliction |
| [Rem](heroes/rem/rem.md) | Pillow Toss; Tag Along; Lil Helpers; Naptime |
| [Seven](heroes/seven/seven.md) | Lightning Ball; Static Charge; Power Surge; Storm Cloud |
| [Shiv](heroes/shiv/shiv.md) | Serrated Knives; Slice and Dice; Bloodletting; Killing Blow |
| [Silver](heroes/silver/silver.md) | Slam Fire; Boot Kick; Entangling Bola; Lycan Curse |
| [Sinclair](heroes/sinclair/sinclair.md) | Vexing Bolt; Spectral Assistant; Rabbit Hex; Audience Participation |
| [The Doorman](heroes/the-doorman/the-doorman.md) | Call Bell; Doorway; Luggage Cart; Hotel Guest |
| [Venator](heroes/venator/venator.md) | Consecrating Grenade; Gutshot; Hex-Lined Snap Trap; Ira Domini |
| [Victor](heroes/victor/victor.md) | Pain Battery; Jumpstart; Aura of Suffering; Shocking Reanimation |
| [Vindicta](heroes/vindicta/vindicta.md) | Stake; Flight; Crow Familiar; Assassinate |
| [Viscous](heroes/viscous/viscous.md) | Splatter; The Cube; Puddle Punch; Goo Ball |
| [Vyper](heroes/vyper/vyper.md) | Screwjab Dagger; Lethal Venom; Slither; Petrifying Bola |
| [Warden](heroes/warden/warden.md) | Alchemical Flask; Willpower; Binding Word; Last Stand |
| [Wraith](heroes/wraith/wraith.md) | Card Trick; Project Mind; Full Auto; Telekinesis |
| [Yamato](heroes/yamato/yamato.md) | Power Slash; Flying Slash; Crimson Slash; Shadow Transformation |

Roster: [heroes/roster.yaml](heroes/roster.yaml). Internal hero and ability
keys remain in the canonical YAML; they are not player-facing aliases.

## Items

Every name below is an **item**, linked directly to its explanation.
Use its adjacent YAML for displayed effects, conditions, and purchase fields.
Names that sound like mechanics (e.g. Burst Fire or Spirit Lifesteal) may
also occur in general questions: use the question's context, not just a match.

| Initial | Item keywords → records |
| --- | --- |
| A | [Active Reload](items/active-reload/active-reload.md); [Alchemical Fire](items/alchemical-fire/alchemical-fire.md); [Arcane Surge](items/arcane-surge/arcane-surge.md); [Arctic Blast](items/arctic-blast/arctic-blast.md); [Armor Piercing Rounds](items/armor-piercing-rounds/armor-piercing-rounds.md) |
| B | [Ballistic Enchantment](items/ballistic-enchantment/ballistic-enchantment.md); [Battle Vest](items/battle-vest/battle-vest.md); [Berserker](items/berserker/berserker.md); [Blood Tribute](items/blood-tribute/blood-tribute.md); [Boundless Spirit](items/boundless-spirit/boundless-spirit.md); [Bullet Lifesteal](items/bullet-lifesteal/bullet-lifesteal.md) |
| B | [Bullet Resilience](items/bullet-resilience/bullet-resilience.md); [Bullet Resist Shredder](items/bullet-resist-shredder/bullet-resist-shredder.md); [Burst Fire](items/burst-fire/burst-fire.md) |
| C | [Capacitor](items/capacitor/capacitor.md); [Celestial Blessing](items/celestial-blessing/celestial-blessing.md); [Cheat Death](items/cheat-death/cheat-death.md); [Cloak of Opportunity](items/cloak-of-opportunity/cloak-of-opportunity.md); [Close Quarters](items/close-quarters/close-quarters.md); [Cold Front](items/cold-front/cold-front.md) |
| C | [Colossus](items/colossus/colossus.md); [Compress Cooldown](items/compress-cooldown/compress-cooldown.md); [Counterspell](items/counterspell/counterspell.md); [Crippling Headshot](items/crippling-headshot/crippling-headshot.md); [Crushing Fists](items/crushing-fists/crushing-fists.md); [Cultist Sacrifice](items/cultist-sacrifice/cultist-sacrifice.md) |
| C | [Cursed Relic](items/cursed-relic/cursed-relic.md) |
| D | [Debuff Reducer](items/debuff-reducer/debuff-reducer.md); [Decay](items/decay/decay.md); [Disarming Hex](items/disarming-hex/disarming-hex.md); [Dispel Magic](items/dispel-magic/dispel-magic.md); [Divine Barrier](items/divine-barrier/divine-barrier.md); [Diviner's Kevlar](items/diviner-s-kevlar/diviner-s-kevlar.md) |
| D | [Duration Extender](items/duration-extender/duration-extender.md) |
| E | [Echo Shard](items/echo-shard/echo-shard.md); [Electric Slippers](items/electric-slippers/electric-slippers.md); [Enchanter's Emblem](items/enchanter-s-emblem/enchanter-s-emblem.md); [Enduring Speed](items/enduring-speed/enduring-speed.md); [Escalating Exposure](items/escalating-exposure/escalating-exposure.md); [Escalating Resilience](items/escalating-resilience/escalating-resilience.md) |
| E | [Eternal Gift](items/eternal-gift/eternal-gift.md); [Ethereal Shift](items/ethereal-shift/ethereal-shift.md); [Express Shot](items/express-shot/express-shot.md); [Extended Magazine](items/extended-magazine/extended-magazine.md); [Extra Charge](items/extra-charge/extra-charge.md); [Extra Health](items/extra-health/extra-health.md) |
| E | [Extra Regen](items/extra-regen/extra-regen.md); [Extra Spirit](items/extra-spirit/extra-spirit.md); [Extra Stamina](items/extra-stamina/extra-stamina.md) |
| F | [Fleetfoot](items/fleetfoot/fleetfoot.md); [Focus Lens](items/focus-lens/focus-lens.md); [Fortitude](items/fortitude/fortitude.md); [Frenzy](items/frenzy/frenzy.md); [Frostbite Charm](items/frostbite-charm/frostbite-charm.md); [Fury Trance](items/fury-trance/fury-trance.md) |
| G | [Glass Cannon](items/glass-cannon/glass-cannon.md); [Golden Goose Egg](items/golden-goose-egg/golden-goose-egg.md); [Greater Expansion](items/greater-expansion/greater-expansion.md); [Grit](items/grit/grit.md); [Guardian Ward](items/guardian-ward/guardian-ward.md) |
| H | [Haunting Shot](items/haunting-shot/haunting-shot.md); [Headhunter](items/headhunter/headhunter.md); [Headshot Booster](items/headshot-booster/headshot-booster.md); [Healbane](items/healbane/healbane.md); [Healing Booster](items/healing-booster/healing-booster.md); [Healing Nova](items/healing-nova/healing-nova.md) |
| H | [Healing Rite](items/healing-rite/healing-rite.md); [Healing Tempo](items/healing-tempo/healing-tempo.md); [Heroic Aura](items/heroic-aura/heroic-aura.md); [High-Velocity Rounds](items/high-velocity-rounds/high-velocity-rounds.md); [Hollow Point](items/hollow-point/hollow-point.md); [Hunter's Aura](items/hunter-s-aura/hunter-s-aura.md) |
| I | [Improved Spirit](items/improved-spirit/improved-spirit.md); [Indomitable](items/indomitable/indomitable.md); [Infinite Rounds](items/infinite-rounds/infinite-rounds.md); [Infuser](items/infuser/infuser.md); [Inhibitor](items/inhibitor/inhibitor.md); [Intensifying Magazine](items/intensifying-magazine/intensifying-magazine.md) |
| J | [Juggernaut](items/juggernaut/juggernaut.md) |
| K | [Kinetic Dash](items/kinetic-dash/kinetic-dash.md); [Knockdown](items/knockdown/knockdown.md) |
| L | [Leech](items/leech/leech.md); [Lifestrike](items/lifestrike/lifestrike.md); [Lightning Scroll](items/lightning-scroll/lightning-scroll.md); [Long Range](items/long-range/long-range.md); [Lucky Shot](items/lucky-shot/lucky-shot.md) |
| M | [Magic Carpet](items/magic-carpet/magic-carpet.md); [Majestic Leap](items/majestic-leap/majestic-leap.md); [Melee Charge](items/melee-charge/melee-charge.md); [Melee Lifesteal](items/melee-lifesteal/melee-lifesteal.md); [Mercurial Magnum](items/mercurial-magnum/mercurial-magnum.md); [Metal Skin](items/metal-skin/metal-skin.md) |
| M | [Monster Rounds](items/monster-rounds/monster-rounds.md); [Mystic Burst](items/mystic-burst/mystic-burst.md); [Mystic Conduit](items/mystic-conduit/mystic-conduit.md); [Mystic Expansion](items/mystic-expansion/mystic-expansion.md); [Mystic Regeneration](items/mystic-regeneration/mystic-regeneration.md); [Mystic Reverb](items/mystic-reverb/mystic-reverb.md) |
| M | [Mystic Shot](items/mystic-shot/mystic-shot.md); [Mystic Slow](items/mystic-slow/mystic-slow.md); [Mystic Vulnerability](items/mystic-vulnerability/mystic-vulnerability.md); [Mystical Piano](items/mystical-piano/mystical-piano.md) |
| N | [Nullification Burst](items/nullification-burst/nullification-burst.md) |
| O | [Omnicharge Signet](items/omnicharge-signet/omnicharge-signet.md); [Opening Rounds](items/opening-rounds/opening-rounds.md) |
| P | [Phantom Strike](items/phantom-strike/phantom-strike.md); [Plated Armor](items/plated-armor/plated-armor.md); [Point Blank](items/point-blank/point-blank.md); [Prism Blast](items/prism-blast/prism-blast.md) |
| Q | [Quicksilver Reload](items/quicksilver-reload/quicksilver-reload.md) |
| R | [Radiant Regeneration](items/radiant-regeneration/radiant-regeneration.md); [Rapid Recharge](items/rapid-recharge/rapid-recharge.md); [Rapid Rounds](items/rapid-rounds/rapid-rounds.md); [Reactive Barrier](items/reactive-barrier/reactive-barrier.md); [Rebuttal](items/rebuttal/rebuttal.md); [Recharging Rush](items/recharging-rush/recharging-rush.md) |
| R | [Refresher](items/refresher/refresher.md); [Rescue Beam](items/rescue-beam/rescue-beam.md); [Restorative Locket](items/restorative-locket/restorative-locket.md); [Restorative Shot](items/restorative-shot/restorative-shot.md); [Return Fire](items/return-fire/return-fire.md); [Ricochet](items/ricochet/ricochet.md) |
| R | [Runed Gauntlets](items/runed-gauntlets/runed-gauntlets.md); [Rusted Barrel](items/rusted-barrel/rusted-barrel.md) |
| S | [Scourge](items/scourge/scourge.md); [Seraphim Wings](items/seraphim-wings/seraphim-wings.md); [Shadow Strike](items/shadow-strike/shadow-strike.md); [Shadow Weave](items/shadow-weave/shadow-weave.md); [Sharpshooter](items/sharpshooter/sharpshooter.md); [Shrink Ray](items/shrink-ray/shrink-ray.md) |
| S | [Silence Wave](items/silence-wave/silence-wave.md); [Silencer](items/silencer/silencer.md); [Siphon Bullets](items/siphon-bullets/siphon-bullets.md); [Slowing Bullets](items/slowing-bullets/slowing-bullets.md); [Slowing Hex](items/slowing-hex/slowing-hex.md); [Spellbreaker](items/spellbreaker/spellbreaker.md) |
| S | [Spellslinger](items/spellslinger/spellslinger.md); [Spirit Burn](items/spirit-burn/spirit-burn.md); [Spirit Lifesteal](items/spirit-lifesteal/spirit-lifesteal.md); [Spirit Rend](items/spirit-rend/spirit-rend.md); [Spirit Resilience](items/spirit-resilience/spirit-resilience.md); [Spirit Sap](items/spirit-sap/spirit-sap.md) |
| S | [Spirit Shielding](items/spirit-shielding/spirit-shielding.md); [Spirit Shredder Bullets](items/spirit-shredder-bullets/spirit-shredder-bullets.md); [Spirit Snatch](items/spirit-snatch/spirit-snatch.md); [Spirit Strike](items/spirit-strike/spirit-strike.md); [Spiritual Overflow](items/spiritual-overflow/spiritual-overflow.md); [Split Shot](items/split-shot/split-shot.md) |
| S | [Sprint Boots](items/sprint-boots/sprint-boots.md); [Stalker](items/stalker/stalker.md); [Stamina Mastery](items/stamina-mastery/stamina-mastery.md); [Superior Cooldown](items/superior-cooldown/superior-cooldown.md); [Superior Duration](items/superior-duration/superior-duration.md); [Suppressor](items/suppressor/suppressor.md) |
| S | [Surge of Power](items/surge-of-power/surge-of-power.md); [Swift Striker](items/swift-striker/swift-striker.md) |
| T | [Tankbuster](items/tankbuster/tankbuster.md); [Tesla Bullets](items/tesla-bullets/tesla-bullets.md); [Titanic Magazine](items/titanic-magazine/titanic-magazine.md); [Torment Pulse](items/torment-pulse/torment-pulse.md); [Toxic Bullets](items/toxic-bullets/toxic-bullets.md); [Transcendent Cooldown](items/transcendent-cooldown/transcendent-cooldown.md) |
| T | [Trophy Collector](items/trophy-collector/trophy-collector.md) |
| U | [Unstable Concoction](items/unstable-concoction/unstable-concoction.md); [Unstoppable](items/unstoppable/unstoppable.md) |
| V | [Vampiric Burst](items/vampiric-burst/vampiric-burst.md); [Veil Walker](items/veil-walker/veil-walker.md); [Vortex Web](items/vortex-web/vortex-web.md) |
| W | [Warp Stone](items/warp-stone/warp-stone.md); [Weakening Headshot](items/weakening-headshot/weakening-headshot.md); [Weapon Shielding](items/weapon-shielding/weapon-shielding.md); [Weighted Shots](items/weighted-shots/weighted-shots.md); [Witchmail](items/witchmail/witchmail.md) |

Roster: [items/roster.yaml](items/roster.yaml). Search that roster for
internal keys, components, and item classification when needed.

## NPCs and claimable objectives

Structures such as Walkers are stored under `npcs/`, not `objectives/`.
NPCs have canonical YAML but no per-NPC Markdown. Use the general map
guides in the topic table above for explanatory context.

| Name / recorded aliases | Type and direct record |
| --- | --- |
| Base Guardian / Shrine Guardian / Watcher | structure: [Base Guardian](npcs/base-guardian/base-guardian.yaml) |
| Cockroach / vent cockroach / neutral bug | ambient neutral: [Cockroach](npcs/cockroach/cockroach.yaml) |
| Lane Guardian / Guardian / tier 1 guardian | structure: [Lane Guardian](npcs/lane-guardian/lane-guardian.yaml) |
| Large Neutral / large denizen / large jungle creep | neutral unit: [Large Neutral](npcs/large-neutral/large-neutral.yaml) |
| Medic Trooper / Banner Trooper / medic creep | lane unit: [Medic Trooper](npcs/medic-trooper/medic-trooper.yaml) |
| Medium Neutral / medium denizen / medium jungle creep | neutral unit: [Medium Neutral](npcs/medium-neutral/medium-neutral.yaml) |
| Melee Trooper / melee creep / melee minion | lane unit: [Melee Trooper](npcs/melee-trooper/melee-trooper.yaml) |
| Mid-Boss / Mid Boss / Temple Guardian / The Boss | neutral boss: [Mid-Boss](npcs/mid-boss/mid-boss.yaml) |
| Patron / Weakened Patron / Titan / Core | structure: [Patron](npcs/patron/patron.yaml) |
| Ranged Trooper / Trooper / creep / minion | lane unit: [Ranged Trooper](npcs/ranged-trooper/ranged-trooper.yaml) |
| Shrine / Patron Shrine / generator | structure: [Shrine](npcs/shrine/shrine.yaml) |
| Sinner's Sacrifice / Sinner's machine / vault | map object: [Sinner's Sacrifice](npcs/sinners-sacrifice/sinners-sacrifice.yaml) |
| Small Neutral / small denizen / small jungle creep | neutral unit: [Small Neutral](npcs/small-neutral/small-neutral.yaml) |
| Walker / Sun Walker / tier 2 boss | structure: [Walker](npcs/walker/walker.yaml) |
| Rejuvenator | claimable team buff: [Rejuvenator](objectives/rejuvenator/rejuvenator.yaml) |
| Soul Urn | claimable map objective: [Soul Urn](objectives/soul-urn/soul-urn.yaml) |

<!-- entity-routes:end -->

## Interpretation limits

Guardian may mean Lane Guardian or Base Guardian. General words such as Silver,
Graves, or item names that are also stats need context. Use each record's stored
aliases; do not invent a historical identity mapping. This navigation file does
not implement a retrieval filter—consuming software must enforce history opt-in.

Some specialist interaction rules are intentionally absent from this edition
because the available evidence was not exclusively public-source-backed. See
[LIMITATIONS.md](LIMITATIONS.md) rather than treating missing rules as established.
