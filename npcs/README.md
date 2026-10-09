# NPC Records

This directory contains normalized, calculation-ready records for gameplay NPCs
and NPC-backed structures in standard mode. `roster.yaml` is the authoritative
inclusion and exclusion manifest.

## Scoped map refresh

The small/medium/large neutral records are shared Haunt tier baselines, not
per-family or per-camp rosters. Their core fields and Mid-Boss combat fields are
cross-checked to client 6731; API identity, explicitly legacy values and some
wiki behavior retain older pins. Sinner composition/reward context is separately
pinned. Read each field's source and uncertainty status; missing weakpoint or
melee-resistance fields do not establish runtime removal. See the
[map-interaction review](../general/map/map-interactions-and-open-questions.md)
and [composition guide](../general/map/haunt-camps-and-sinner-sites.md).
Unrelated NPCs and the root baseline have not advanced.

## Record contract

Each record provides:

- stable public identity, aliases, internal class, and numeric asset ID;
- a gameplay classification rather than relying on internal class names;
- normalized meters, seconds, percentage points, and raw precision;
- base combat values, conditional defenses, scaling, attacks, rewards, and
  relationships when established;
- field-level source roles and revision-pinned source IDs;
- references to canonical economy, timing, progression, or rule records instead
  of duplicating those tables.

The client-versioned Deadlock API is authoritative for asset identity and acts
as the primary structured cross-check. The immutable `npc-data.json` artifact
from the approved `deadlock-data` commit supplies unit-normalized fields and
nested behavior omitted by the API response. Pinned wiki pages establish public
names and behavioral context.

Technical helpers, ambient actors, duplicate team models, weak-point helper
entities, hero summons, and mode-specific units are excluded from the standard
roster unless they need a separate reviewed interaction record.

The YAML records are canonical. General Markdown under `general/map/` explains
systems spanning multiple entities and should not be parsed for calculations.
