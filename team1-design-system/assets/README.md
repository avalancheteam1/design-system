# Team1 asset library

This directory is the privacy-safe, distributable asset layer of the Team1 design system. It contains 54 authentic visual files: 38 current global-identity assets and 16 current chapter vectors. Every packaged file is listed exactly once in `asset-index.json` with its source, SHA-256 digest, authority, use status, editability, and rights note.

The assets are source originals. Do not redraw, recolor, crop, stretch, trace, or rebuild a Team1 mark. Keep the original proportions and choose the supplied variant that already fits the background.

## Global identity

The global identity comes from `avalancheteam1/common` commit `9d1b3d1a9d9e3e254149885605504c6dfd84ec54`, Team1's current source of truth at the time of the 2026-08-12 audit.

| Folder | Contents | Intended use |
| --- | --- | --- |
| `identity/wordmark/` | Five SVG and five PNG wordmarks | Full Team1 signature in headers, covers, footers, and co-branding |
| `identity/symbol/` | Five SVG and five PNG symbols | Compact placements where the wordmark would be illegible |
| `identity/symbol/squared/` | Five SVG and five PNG square symbols | Avatars, application icons, and square media |
| `identity/favicon/` | ICO, SVG, and raster web icons | Website metadata and installed-app surfaces |
| `identity/Team1_Main_Red_PFP.png` | Official profile-picture artwork | Team1-owned profile and community surfaces |

Variant selection:

- `MAIN_WHITE`: red symbol with white lettering for dark fields.
- `BLACK_MAIN` in SVG and `MAIN_BLACK` in PNG: red symbol with black lettering for light fields. The filename difference is preserved from the official source.
- `WHITE_ALTERNATIVE`: all-white art for sufficiently dark or photographic fields.
- `BLACK_ALTERNATIVE`: all-black art for sufficiently light fields.
- `RED_ALTERNATIVE`: all-red art for controlled one-colour applications.

Prefer SVG for web, print, and scalable layouts. Use PNG where the destination cannot render SVG. Use the favicon family as supplied; do not substitute a wordmark or a screenshot crop.

The duplicate top-level symbol from the upstream repository is intentionally not packaged because `identity/symbol/Team1_Symbol_Main.svg` is the authoritative copy in this normalized tree.

## Chapter identity

`chapters/` contains 16 current SVG sources audited from Team1's shared brand library. The Brasil, India, LATAM, Türkiye, USA, and Vietnam families were last modified on 2026-08-06. The Korea family contains one 2026-08-06 lockup and four files last modified on 2026-08-07. Thailand files were last modified on 2026-08-06. The sanitized record is in `chapters/provenance.json`; it contains no Drive IDs.

Chapter assets are an optional layer, not a replacement for the global Team1 identity. Before publishing:

1. Confirm the chapter is active and the selected file is approved by the current chapter or regional owner.
2. Keep a global Team1 mark present when the context could otherwise appear independent or unofficial.
3. Use the supplied SVG unchanged. Generate a PNG derivative from the verified SVG only when a destination requires raster output.
4. Verify spelling and locale. In particular, preserve `Brasil` and `Türkiye` as provided.
5. Recheck owner approval whenever the event, campaign, country, or destination changes.

Korea and Thailand include backgrounds, wordmarks, horizontal lockups, and complete lockups. Choose a complete or horizontal lockup when the destination needs a ready-made composition; do not manually recombine their parts.

## Deliberate exclusions

The package does **not** contain:

- font binaries or commercial font licenses;
- QR codes or destination-bearing artwork;
- participant, member, speaker, or staff photography;
- partner, sponsor, Avalanche, or third-party marks;
- event audio, video, or editable production source files;
- baked metrics, time-sensitive claims, campaign graphics, or historical backgrounds;
- legacy Team1 logos or chapter raster tiles from the v1 overview deck;
- the upstream duplicate top-level symbol.

The removed v1 payload and legacy presentation remain recoverable from controlled Git/release history; they are not current reusable brand material.

## Rights, privacy, and integrity

These files are provided for authorized Team1 work. Team1 names and marks remain subject to the organization's brand and trademark controls. Packaging an asset does not grant independent redistribution, sublicensing, merchandising, or third-party use rights. Chapter files require current owner approval before public use.

Do not add personal photos, contact details, tracking links, private Drive identifiers, or unverified destination data to this directory. Add new assets only after source, rights, authority, modification status, and privacy have been reviewed.

Before use, locate the file in `asset-index.json` and compare its SHA-256 digest if provenance matters. Any changed digest means the file is no longer the audited source original and must be reviewed again.
