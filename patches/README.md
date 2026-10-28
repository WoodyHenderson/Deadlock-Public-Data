---
id: patches.deadlock-data
title: Deadlock historical patch changelogs
domain: patches
topics: [patches, history, balance, changelogs]
aliases: [patch notes, patch history, changelogs, balance history]
summary: Historical Deadlock patch changelogs for explicitly requested historical or change-tracking questions.
snapshot_id: deadlock-patches-through-2026-10-13
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
---

# Historical Patch Changelogs

This section contains **137 dated raw changelogs** from 2024-05-03 through
2026-10-05, using separately pinned upstream commits. This is not a complete
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

The [October 6 Baba release](2026-10-06-baba-release.md) covers her release and
preserves the client-6759 launch state in a separate
[historical snapshot](snapshots/baba-2026-10-06.md). Her canonical record is checked
through client 6763. The [October 7 source review](2026-10-07-review.md) records a
same-client export representation correction and English wording clarification;
it does not claim a confirmed hotfix or runtime change. No October 6 or October 7
raw changelog is fabricated; the raw archive still contains 137 files. The
[October 9 Solomon release](2026-10-09-solomon-release.md) uses the selected
client-6774 configuration snapshot and preserves incomplete client-6763 data
only as a pre-release comparison; no October 9 raw changelog is fabricated. The
[October 13 Deadman Danny release](2026-10-13-deadman-danny-release.md) uses
client 6782 as the first complete reviewed configuration dated October 14, not an
exact launch-day snapshot. Valve's announcement establishes October 13 availability;
no October 13 raw changelog is fabricated, and the separate October 14 balance
update is not folded into the release record.

The [October 4/5 summary](2026-10-05-balance.md) covers the separate Street Brawl
removal and applied Sinclair/Rat King balance changes. [October 5 raw notes](raw/2026-10-05.txt)
preserve original wording; the [October 2 Rat King snapshot](snapshots/rat-king-2026-10-02.yaml)
preserves historical launch values.

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

Each raw file has its own immutable source and hash in the manifest. The latest
addition uses commit `edb16660368ef3b693a4ac6d525697f5570a4dce`; earlier files retain
their original pins. Historical snapshots and raw notes are separate from
current canonical entity YAML and must not silently override its dated values.
