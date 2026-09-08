# NPC Records

This directory contains normalized, calculation-ready records for gameplay NPCs
and NPC-backed structures in standard mode. `roster.yaml` is the authoritative
inclusion and exclusion manifest.

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
