---
id: patches.2026-10-13-deadman-danny-release
title: October 13, 2026 — Deadman Danny release
domain: patches
topics: [hero-release, deadman-danny, abilities, historical]
current_as_of: "2026-10-14"
evidence_status: source_verified_with_official_release_confirmation
sources:
  - steam.news.deadman-danny-release.1846018067945303
  - github.deadlock-data.gameplay.bd95f245ccb1
  - github.deadlock-data.english.bd95f245ccb1
  - github.deadlock-data.gameplay.330a775230e8
  - github.deadlock-data.gameplay.51636a2c4136
  - github.deadlock-data.gameplay.346dd6686b38
  - github.deadlock-data.gameplay.3aab395a1392
  - steam.news.deadman-danny-oct14-update.1846651706676198
  - github.deadlock-data.raw-changelog.2026-10-14.3aab395a1392
---

# October 13, 2026 — Deadman Danny Release

Valve's [“Fairfax Industries Employee Spotlight” announcement](https://store.steampowered.com/news/app/1422450/view/1846018067945303?l=english), published October 13 at **20:59:55 UTC**, says Deadman Danny is “available in-game now” and introduces the Chimera Mk1, Strix Salvo, Jettison Fuel, and Close the Deal. This establishes availability and release date, not the complete numerical configuration or every runtime interaction.

The current [Deadman Danny record](../heroes/deadman-danny/deadman-danny.md) uses client 6785 after the separately dated October 14 balance update. The [October 14 release-era snapshot](snapshots/deadman-danny-2026-10-14.md) preserves **client 6782 / source revision 11127865**, the earliest complete Danny configuration found in the reviewed source history. Client 6782 is dated October 14, after the announcement; it is an explicitly dated post-release data snapshot, **not an exact October 13 launch-day snapshot**.

Client 6774 already had a selectable `hero_deadpack` entry, but its type was null, it had no bound abilities, and its weapon was a provisional configuration. Those fields are retained only as a pre-release comparison; they do not establish release or supply the released stats. The incomplete values are not used in the client-6782 record.

## Client Chronology and Limits

- The first client-6782 export and a later same-client exporter recheck have identical bytes for the 14 selected datasets. The later export is not treated as a separate game update.
- Client 6782 supplies four numbered ability cards and their pinned English descriptions/upgrades. It also contains an unbound `ability_deadpack_zip_line` record with no numbered hero card; the record preserves it as supporting generated data, not as a fifth hero ability.
- Valve's separate [“Minor Update - 10-14-2026” post](https://store.steampowered.com/news/app/1422450/view/1846651706676198?l=english), published October 15 at 03:11:58 UTC, and the later client 6785 export show post-release changes. They remain outside this October 13 release record; their patch-note claims are not represented here as independently verified runtime behavior.
- Client 6785, the October 14 raw update note, unrelated export/localization changes, and Street Brawl item-bucket data are not folded into Danny's first complete configuration. See the separate citations for the dated later sources; this summary does not apply that update.
- No October 13 raw changelog was found in the reviewed pinned upstream archive. No October 13 raw file or undocumented runtime-change claim is created.

The [YAML snapshot](snapshots/deadman-danny-2026-10-14.yaml) preserves the source fields and their October 14 pin. Generated client data and localized descriptions are not independent runtime tests, and the client-6782 snapshot is not a claim of October 28 current balance.
