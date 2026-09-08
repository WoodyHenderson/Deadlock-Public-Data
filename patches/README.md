---
id: patches.deadlock-data
title: Deadlock historical patch changelogs
domain: patches
topics: [patches, history, balance, changelogs]
aliases: [patch notes, patch history, changelogs, balance history]
summary: Historical Deadlock patch changelogs for explicitly requested historical or change-tracking questions.
snapshot_id: deadlock-wiki-2026-09-08
current_as_of: "2026-09-08"
evidence_status: source_verified
sources:
  - github.deadlock-data.changelogs.raw.afc8e9c
---

# Historical Patch Changelogs

This section contains **135 dated raw changelogs** from 2024-05-03 through
2026-08-22, imported from the pinned `deadlock-wiki/deadlock-data` commit.
See [`manifest.yaml`](manifest.yaml) for the per-file hashes and source paths.

## Retrieval policy

Patch data is historical evidence only. It must **not influence the current
knowledgebase's hero, item, ability, mechanic, or calculation records** and must
not override current structured data. Normal current-patch retrieval should not
search this section unless the user asks about a historical change, an old value,
when a mechanic changed, or patch-note context.

When used, cite the dated raw changelog and distinguish:

- **Patch-note intent:** what the changelog says was changed;
- **Current state:** what the current pinned game-data record says now;
- **Observed behavior:** what runtime testing establishes, if available.

A patch note may describe intended behavior without proving that the final game
implementation matched it. Changelog text is preserved verbatim; it is not
normalized into current entity facts.

## Source and update policy

The source is pinned to commit
`afc8e9c10bedd12ef7d1cf750bcdb612ed0c21af`. Updates should import a new pinned
commit, retain the old manifest/files for reproducibility, and never silently
rewrite current records. New changelog files can be added without requiring a
current knowledgebase refresh.

Raw files are deliberately kept separate from curated Markdown and canonical
entity YAML. Entity names in patch notes are prose and should be linked only
when extraction is unambiguous; a future index may add searchable links without
changing this policy.
