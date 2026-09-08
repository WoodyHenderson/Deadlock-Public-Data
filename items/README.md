# Item Knowledgebase

This directory covers all **173 items currently purchasable** in Deadlock client 6684, source revision 10933105.

## Source policy

1. The versioned [Deadlock API](https://api.deadlock-api.com/v1/assets/items?language=english&client_version=6684) is the primary structured authority because it is generated from current game data for community use.
2. [`deadlock-wiki/deadlock-data`](https://github.com/deadlock-wiki/deadlock-data/tree/311b2e8d895eec837441ff3e29b7d7581a61768c/data) at commit `311b2e8d895eec837441ff3e29b7d7581a61768c` is the secondary source and cross-check.
3. A disagreement is retained and queued for review; the secondary source never silently replaces the primary value.

Both sources identify the same client and source revision. [`roster.yaml`](roster.yaml) records the exact inclusion rule, source hashes, counts, and item identifiers.

## Record contract

Each item has retrieval-oriented Markdown and canonical YAML. The YAML preserves:

- display name, numeric ID, internal key, aliases, availability, slot, tier, cost, activation type, and shop filters;
- components and upgrade relationships;
- plain-text descriptions for natural-language retrieval;
- card-visible innate, passive, and active effects in presentation order;
- every primary API property, scaling function, tooltip section, activation field, and upgrade block;
- complete matching secondary `item-data.json` and `item-cards.json` records;
- target types, conditional-use flags, hidden source fields, source priority, patch identity, and evidence boundaries.

Generated source-shaped fields are evidence inputs, not executable mechanics. Calculations require separately reviewed rules that define units, conditions, stacking, ordering, and applicability.

## Deliberate exclusions

Media files, image URLs, icons, and embedded SVG artwork are excluded. They do not contribute mechanics evidence and can dominate retrieval context. Description text is retained without those assets.
