---
id: patches.deadlock-data
title: Deadlock historical patch changelogs
domain: patches
topics: [patches, history, balance, changelogs]
aliases: [patch notes, patch history, changelogs, balance history]
summary: Historical Deadlock patch changelogs for explicitly requested historical or change-tracking questions.
snapshot_id: deadlock-patches-through-2026-10-14
current_as_of: "2026-10-14"
evidence_status: source_verified
sources:
  - github.deadlock-data.changelogs.raw.afc8e9c
  - github.deadlock-data.changelogs.raw.fc4f540f12e0
  - github.deadlock-data.changelog.2026-10-05.edb16660368e
  - github.deadlock-data.gameplay.330a775230e8
  - github.deadlock-data.english.330a775230e8
  - steam.news.solomon-release.1846018067934643
  - github.deadlock-data.gameplay.bd95f245ccb1
  - github.deadlock-data.english.bd95f245ccb1
  - github.deadlock-data.gameplay.51636a2c4136
  - github.deadlock-data.gameplay.3aab395a1392
  - steam.news.deadman-danny-release.1846018067945303
  - steam.news.deadman-danny-oct14-update.1846651706676198
  - github.deadlock-data.raw-changelog.2026-10-14.3aab395a1392
---

# Historical Patch Changelogs

This section contains **138 dated raw changelogs** from 2024-05-03 through
2026-10-14, using separately pinned upstream commits. This is not a complete
archive of every intervening update.
See [`manifest.yaml`](manifest.yaml) for the per-file hashes and source paths.
The separate [client-6694 review](2026-09-16-client-6694-review.md) documents
which structured records were refreshed and keeps patch-note-only claims distinct.

The [City Never Sleeps pre-Rat King review](2026-09-29-city-never-sleeps-pre-rat-king-review.md)
covers September 29 through October 1/client 6731. It is curated evidence, not
a raw changelog; no September 29/30 raw file was present in the pinned archive.
Those reviews do not fabricate missing raw files.

The [October 2 Rat King release review](2026-10-02-rat-king-release-review.md)
separately covers Rat King's client-6737 launch, the Broker toggle, and
healing-ping configuration. No raw October 2 changelog is fabricated. Later
wiki descriptions are dated; that launch review excludes later balance.

The [October 6 Baba release](2026-10-06-baba-release.md) preserves the client-6759
launch state in a separate [historical snapshot](snapshots/baba-2026-10-06.md).
The [October 7 source review](2026-10-07-review.md) records an export representation
correction and English wording clarification, not a confirmed hotfix or runtime
change. Baba's current record uses client 6785 after the separate October 14 update.
No October 6 or October 7 raw changelog is fabricated.
The [October 9 Solomon release](2026-10-09-solomon-release.md) uses the selected
client-6774 configuration snapshot; no October 9 raw changelog is fabricated.
The [October 13 Deadman Danny release](2026-10-13-deadman-danny-release.md)
confirms availability separately from client 6782, the first complete reviewed
configuration dated October 14—not an exact launch-day snapshot. The separate
[October 14 balance update](2026-10-14-balance.md) records subsequent client-6785
changes and does not alter that release-era snapshot. The archive now contains
138 raw files, including the byte-pinned [October 14 note](raw/2026-10-14.txt).

The [October 4/5 summary](2026-10-05-balance.md) covers the separate Street Brawl
removal and applied Sinclair/Rat King balance changes. [October 5 raw notes](raw/2026-10-05.txt)
preserve original wording; the [October 2 Rat King snapshot](snapshots/rat-king-2026-10-02.yaml)
preserves historical launch values. The October 14 summary, raw note, and current
client-6785 records are cited independently; they do not advance the corpus-wide
September 3 baseline or the 173-item roster.

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

## Sources

Each raw file has its own immutable source and hash in the manifest. The October 5
entry uses commit `edb16660368ef3b693a4ac6d525697f5570a4dce`; the October 14 entry
uses commit `3aab395a139254c12179f0f829f7488c55da2022`. Earlier files retain
their original pins. Historical snapshots and raw notes are separate from
current canonical entity YAML and must not silently override its dated values.
