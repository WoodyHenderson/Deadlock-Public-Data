---
id: patches.2026-10-16-violet-release
title: October 16, 2026 — Violet release
domain: patches
topics: [hero-release, violet, abilities, historical]
current_as_of: "2026-10-16"
evidence_status: source_verified_with_official_release_confirmation
sources:
  - steam.news.violet-release.1846651706683085
  - github.deadlock-data.gameplay.596ad0c74b26
  - github.deadlock-data.english.596ad0c74b26
  - github.deadlock-data.gameplay.3aab395a1392
  - github.deadlock-data.gameplay.5b2911aa55e6
---

# October 16, 2026 — Violet Release

Valve's [“Paint the Town” announcement](https://store.steampowered.com/news/app/1422450/view/1846651706683085?l=english), published October 16 at **21:00:07 UTC**, says Violet is “available in-game now” and names Living Ink, Flow State, Still Life, and Abstract Landscape. The post establishes availability and names abilities; it is not a full numerical specification or runtime test.

The [Violet record](../heroes/violet/violet.md) uses the first reviewed complete configuration found after the announcement: **client 6790 / source revision 11139717**. Its upstream source commit was recorded at 21:10:10Z, ten minutes after Valve's post. The `VersionTime` in `version.txt` has no declared timezone. This is a dated post-release configuration candidate, not an exact launch-day stat sheet.

Client 6785 contained a selectable but incomplete Violet placeholder, with a null type and no bound abilities. Its fields are retained only as a pre-release comparison. The client-6790 record has `InDevelopment: true`; this generated flag is preserved, but it does not override Valve's explicit availability statement.

## Client Chronology and Limits

- Client 6793 is a later same-date source checkpoint. All 13 selected JSON datasets are byte-identical to client 6790; only `version.txt` differs. No separate later Violet configuration is inferred.
- The complete client-6790 record includes four numbered abilities, cards, English descriptions, and two unnumbered trigger records. The hero YAML also preserves Violet's stroke-blocker NPC and four drawing-pickup records as supporting generated data, not as independent runtime or placement evidence.
- Client 6790 includes a pre-release Nurse Harrow `LevelScaling` change relative to client 6785. It is not attributed to Violet and remains separate from this release record. Other adjacent item, HUD, Familiar, Solomon, hideout, localization, and Street Brawl differences are outside the Violet release record and are not applied as Violet balance.
- No `2026-10-16` raw changelog was found in either reviewed upstream source tree. No raw patch file or undocumented balance-change claim is created.

The YAML and Markdown record preserve client-generated fields and localized text from the pinned sources; neither is independent runtime verification. The separate October 14 balance update remains unchanged, and no corpus-wide baseline is advanced.
