---
id: patches.2026-10-09-solomon-release
title: October 9, 2026 — Solomon release
domain: patches
topics: [hero-release, solomon, abilities, historical]
current_as_of: "2026-10-09"
evidence_status: source_verified_with_official_release_confirmation
sources:
  - steam.news.solomon-release.1846018067934643
  - github.deadlock-data.gameplay.330a775230e8
  - github.deadlock-data.english.330a775230e8
  - github.deadlock-data.gameplay.8f2589cb4e64
  - github.deadlock-data.gameplay.18998ba13ff3
  - github.deadlock-data.gameplay.3b96422dbf31
---

# October 9, 2026 — Solomon Release

Valve's [“Make Your Move.” announcement](https://store.steampowered.com/news/app/1422450/view/1846018067934643?l=english), published October 9 at **21:00:04 UTC**, confirms Solomon is available in-game and names Setup Bishop, Kingside Knight, Rook Battery, and Develop Queen.

The [Solomon record](../heroes/solomon/solomon.md) and [October 9 snapshot](snapshots/solomon-2026-10-09.md) preserve his weapon, stats, four abilities, cards, upgrade fields, English descriptions, three supporting trigger records, and two Chess-piece NPC records from **client 6774 / source revision 11112755**. The release announcement establishes availability; client data supplies a dated configuration, not an independent runtime test.

## Client Chronology and Limits

- Client 6763 already contained a selectable Solomon entry, but it had no ability bindings, a null hero type, and a provisional weapon/configuration. Those values are preserved only as a pre-release comparison; `IsSelectable` alone does not establish public release.
- Client 6769 supplied the first complete Solomon data. Its version-file time (October 9, 13:38:46) has no declared timezone, so it is not compared directly with the UTC announcement or used to date public availability.
- The reviewed Solomon hero, ability, card, NPC, and English-description data match across clients 6769, 6773, and 6774. Client 6774 is the selected October 9 configuration snapshot used here; Valve's announcement establishes availability.
- Unrelated client-export, settings, mode-data and localization differences are outside this hero release summary and are not presented as Solomon balance changes or evidence of an October 9 hotfix.
- No October 9 raw changelog was found in the reviewed upstream archive. No raw patch file or undocumented runtime-change claim is created.

The wider later-client review and any subsequently changed Solomon values remain separate from this release snapshot.
