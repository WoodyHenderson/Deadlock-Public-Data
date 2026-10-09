---
id: patches.deadlock-data
title: Deadlock historical patch changelogs
domain: patches
topics: [patches, history, balance, changelogs]
aliases: [patch notes, patch history, changelogs, balance history]
summary: Historical Deadlock patch changelogs for explicitly requested historical or change-tracking questions.
snapshot_id: deadlock-wiki-2026-09-17
current_as_of: "2026-09-17"
evidence_status: source_verified
sources:
  - github.deadlock-data.changelogs.raw.afc8e9c
  - github.deadlock-data.changelogs.raw.fc4f540f12e0
---

# Historical Patch Changelogs

This section contains **136 dated raw changelogs** from 2024-05-03 through
2026-09-16, imported from the latest `deadlock-wiki/deadlock-data` commit.
See [`manifest.yaml`](manifest.yaml) for the per-file hashes and source paths.
The separate [client-6694 review](2026-09-16-client-6694-review.md) documents
which structured records were refreshed and keeps patch-note-only claims distinct.

The [City Never Sleeps pre-Rat King review](2026-09-29-city-never-sleeps-pre-rat-king-review.md)
covers September 29 through October 1/client 6731. It is curated evidence, not
a raw changelog; no September 29/30 raw file was present in the pinned archive.
The raw archive and its manifest are unchanged. October 2 and later releases
remain separate imports.

## Retrieval policy

The raw archive is historical evidence and does not by itself update current
hero, item, ability, or mechanic records. A separately reviewed, dated delta may
cite patch-note intent alongside pinned structured data, but must label
patch-note-only behavior and must not treat notes as runtime verification or
silently override structured values. Normal retrieval should search this archive
only for explicit historical changes, old values, or patch-note context.

When used, cite the dated raw changelog and distinguish:

- **Patch-note intent:** what the changelog says was changed;
- **Current state:** what the current pinned game-data record says now;
- **Observed behavior:** what runtime testing establishes, if available.

A patch note may describe intended behavior without proving that the final game
implementation matched it. Changelog text is preserved verbatim; it is not
normalized into current entity facts.

## Source and update policy

The source is pinned to commit
`fc4f540f12e019a6a2a422e0818917a4eedaf881`. Updates should import a new pinned
commit, retain the old manifest/files for reproducibility, and never silently
rewrite current records. New changelog files can be added without requiring a
current knowledgebase refresh.

Raw files are deliberately kept separate from curated Markdown and canonical
entity YAML. Entity names in patch notes are prose and should be linked only
when extraction is unambiguous; a future index may add searchable links without
changing this policy.
