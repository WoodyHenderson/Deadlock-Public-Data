---
id: patches.2026-10-06-baba-release
title: October 6, 2026 — Baba release
domain: patches
topics: [hero-release, baba, abilities, historical]
current_as_of: "2026-10-06"
sources:
  - steam.news.baba-release.1845383656397580
  - github.deadlock-data.gameplay.69b3ca700c80
  - github.deadlock-data.gameplay.7fd1dfeb502a
  - github.deadlock-data.english.7fd1dfeb502a
  - wiki.update.2026-10-06.184307
  - wiki.baba.184291
  - wiki.baba.184568
---

# October 6, 2026 — Baba Release

Valve's [“Mind the Birds!” announcement](https://store.steampowered.com/news/app/1422450/view/703281025618282871), published October 6 at 20:59:54 UTC, confirms **Baba is available**.

## Baba

The [historical October 6 Baba record](snapshots/baba-2026-10-06.md) preserves her initial launch-day state (client 6759), including weapon, stats, four abilities, upgrades and three brew effects. The [canonical Baba record](../heroes/baba/baba.md) is checked through client 6763 after the separate October 7 source review.

1. **Threadsap:** crosshair-guided thread bursts, steals Spirit and grants Spirit damage on bullets while holding stolen Spirit.
2. **Granny Long Legs:** bench form grants movement, jumping and resistances; light melee kicks and heavy melee ground-pounds. It is not another roster hero.
3. **Baba's Brew** (also called **Baba's Brews**): cycles between a barrier, silence, and a damaging burn that reduces Spirit Resist. Aim-down-sights pauses/resumes brewing.
4. **Feed The Birds:** applies bread and stacking slow; pigeons subsequently damage and hex targets, with effects depending on bread count.

The roster contains **40 heroes**. This dated release snapshot uses October 6 **client 6759**; Baba's current canonical record is separately checked through October 7/client 6763. Sinclair and Rat King remain on client 6753; the other 37 heroes retain their earlier pins. No global baseline or item roster is advanced.

## Evidence and Limits

- Initial launch **client 6757** and later same-day **client 6759** have identical Baba hero stats. The initial cards and the earlier Granny Long Legs field are retained separately in [Baba's data](../heroes/baba/baba.yaml).
- Client 6759's version file is dated October 6; its upstream repository commit arrived October 7 UTC. It is not silently substituted for the initial launch checkpoint or treated as the separately announced October 7 hotfix.
- The client still marks Baba `InDevelopment: true`. Valve's explicit release confirmation establishes public availability; the conflicting flag remains visible.
- The weapon lists three projectiles but also `HitOnceAcrossAllBullets: true`. Do not triple the source DPS or assume three damage/proc events on one target.
- Tier 3 Brew is **+33.33% effectiveness**, not +33.33 seconds of silence. The source's multiplier flags remain intact.
- The [October 6 wiki article](https://deadlock.wiki/Baba?oldid=184291) reports the ground pound hitting Sinner's Sacrifice. More detailed movement, parry, ultimate/item and mode descriptions come from the [October 8 article](https://deadlock.wiki/Baba?oldid=184568); they are explicitly dated later context, not launch-day runtime verification.
- Missing fields and tooltip-label edits do not prove changes to runtime mechanics. Exact damage ramps, brew timing formulas and all item interactions are not independently established. The October 7 export/wording findings are dated separately in [the source review](2026-10-07-review.md).

No original October 6 raw changelog was found in the reviewed upstream archive; this page is a sourced summary, not a fabricated raw patch file. October 7 and subsequent changes remain separate updates.

## Other Announcement Context

The same announcement extended the first Ranked season to **November 5, 2026, 2pm PDT**. This is a historical announcement date, not a claim about the current season calendar.
