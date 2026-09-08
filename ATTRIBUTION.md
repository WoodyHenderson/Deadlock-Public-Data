# Attribution and reuse

## Data sources

- **Deadlock Wiki and its contributors** — <https://deadlock.wiki/>.
  Wiki-derived prose is adapted from the cited articles; generated values retain
  their source references. Article revision URLs and access dates are listed in
  [the source registry](sources/source-registry.yaml).
- **Deadlock API contributors** — <https://deadlock-api.com/> and the versioned
  assets at <https://api.deadlock-api.com/>. API response hashes and client
  versions are recorded where available.
- **Deadlock Wiki data repository contributors** —
  <https://github.com/deadlock-wiki/deadlock-data>. Generated datasets, English
  localization, and raw changelogs use immutable commits identified in the
  registry and [patch manifest](patches/manifest.yaml).

Deadlock, its game text, and related intellectual property belong to Valve and
other applicable rights holders. This repository is an unofficial reference.
No game images or other media assets are included. Links appearing inside raw
changelogs are preserved as part of the upstream text, not additional curated
data sources.

## License boundaries

The source registry records wiki text as **CC BY-NC-SA 4.0**. Preserve attribution
and observe its noncommercial and share-alike conditions where applicable:
<https://creativecommons.org/licenses/by-nc-sa/4.0/>.

That attribution does not assert that all API output, extracted game text,
localizations, or changelog content shares one license. An upstream software
license is not automatically a license for all data returned by that software.
Consult the applicable upstream terms and rights holders for those materials.

No blanket MIT, CC0, or other unrestricted license is asserted over this mixed
collection. Publishing a GitHub copy does not remove upstream restrictions or
grant rights the publisher does not hold. No additional license for original
repository tooling is granted by this notice.

## Changes in this edition

- Organized source material into readable Markdown and structured YAML records.
- Preserved raw fields and added normalized English ability descriptions.
- Removed private-confirmation-only and mixed-provenance interaction tables
  rather than assigning their claims to public sources without evidence.
- Removed internal planning references and application-specific paths.
- Added a standalone index, documentation, and offline validation.
- Preserved raw changelog bytes; normalized manifest dates separately from
  filename variants and retained per-file SHA-256 hashes and source URLs.

Neither normalized text nor derived navigation should be represented as an
unaltered upstream publication. The original artifacts remain identifiable
through the source references.
